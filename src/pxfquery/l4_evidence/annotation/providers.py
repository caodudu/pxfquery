from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Any


DEFAULT_TIMEOUT = 20.0


def default_annotation_providers(
    sources: tuple[str, ...] | list[str] | None = None,
    *,
    timeout: float = DEFAULT_TIMEOUT,
    email: str | None = None,
    api_key: str | None = None,
) -> list[Any]:
    selected = tuple(sources or ("pubmed", "pubchem", "chembl"))
    providers: list[Any] = []
    for source in selected:
        key = str(source).lower()
        if key == "pubmed":
            providers.append(PubMedAnnotationProvider(timeout=timeout, email=email, api_key=api_key))
        elif key == "pubchem":
            providers.append(PubChemAnnotationProvider(timeout=timeout))
        elif key == "chembl":
            providers.append(ChEMBLAnnotationProvider(timeout=timeout))
        elif key in {"genecards_harmonizome", "harmonizome"}:
            providers.append(GeneCardsHarmonizomeAnnotationProvider(timeout=timeout))
        elif key == "drugbank":
            providers.append(DrugBankUnavailableProvider())
        else:
            providers.append(UnavailableAnnotationProvider(name=key, reason=f"unknown annotation source: {source}"))
    return providers


@dataclass
class PubMedAnnotationProvider:
    timeout: float = DEFAULT_TIMEOUT
    retmax: int = 5
    email: str | None = None
    api_key: str | None = None
    name: str = "pubmed"

    def search(self, *, claim_basis: dict[str, Any], matrix_evidence: dict[str, Any]) -> list[dict[str, Any]]:
        query = _pubmed_query_from_parts(
            claim_basis.get("main_claim"),
            _primary_terms({"claim_basis": claim_basis, "evidence_layer": {"matrix_evidence": matrix_evidence}}),
        )
        return self._search_query(query)

    def annotate(self, *, query: str, evidence_dossier: dict[str, Any]) -> list[dict[str, Any]]:
        pubmed_query = _pubmed_query_from_parts(query, _primary_terms(evidence_dossier))
        return self._search_query(pubmed_query)

    def _search_query(self, query: str) -> list[dict[str, Any]]:
        if not query.strip():
            return []
        params = {
            "db": "pubmed",
            "retmode": "json",
            "retmax": str(self.retmax),
            "sort": "relevance",
            "term": query,
        }
        if self.email or os.environ.get("PXFQUERY_NCBI_EMAIL"):
            params["email"] = self.email or os.environ["PXFQUERY_NCBI_EMAIL"]
        if self.api_key or os.environ.get("NCBI_API_KEY"):
            params["api_key"] = self.api_key or os.environ["NCBI_API_KEY"]
        esearch = _http_json("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(params), timeout=self.timeout)
        ids = ((esearch.get("esearchresult") or {}).get("idlist") or [])[: self.retmax]
        if not ids:
            return [{"source": self.name, "status": "no_hits", "query": query, "records": []}]
        summary_params = {
            "db": "pubmed",
            "retmode": "json",
            "id": ",".join(ids),
        }
        if "email" in params:
            summary_params["email"] = params["email"]
        if "api_key" in params:
            summary_params["api_key"] = params["api_key"]
        summary = _http_json("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" + urllib.parse.urlencode(summary_params), timeout=self.timeout)
        result = summary.get("result") or {}
        records = []
        for pmid in ids:
            item = result.get(str(pmid)) or {}
            if not item:
                continue
            records.append(
                {
                    "pmid": str(pmid),
                    "title": item.get("title"),
                    "journal": item.get("fulljournalname") or item.get("source"),
                    "pubdate": item.get("pubdate"),
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                }
            )
        return [{"source": self.name, "status": "searched", "query": query, "records": records}]


@dataclass
class PubChemAnnotationProvider:
    timeout: float = DEFAULT_TIMEOUT
    max_terms: int = 5
    name: str = "pubchem"

    def annotate(self, *, query: str, evidence_dossier: dict[str, Any]) -> list[dict[str, Any]]:
        records = []
        for term in _compound_terms(evidence_dossier, max_terms=self.max_terms):
            hit = self._annotate_compound(term)
            if hit:
                records.append(hit)
        return records

    def _annotate_compound(self, term: str) -> dict[str, Any] | None:
        encoded = urllib.parse.quote(term, safe="")
        try:
            cid_payload = _http_json(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{encoded}/cids/JSON", timeout=self.timeout)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return {"source": self.name, "status": "no_hits", "term": term, "records": []}
            raise
        cids = ((cid_payload.get("IdentifierList") or {}).get("CID") or [])[:3]
        if not cids:
            return {"source": self.name, "status": "no_hits", "term": term, "records": []}
        prop_names = "MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES,IsomericSMILES"
        prop_payload = _http_json(
            f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{','.join(map(str, cids))}/property/{prop_names}/JSON",
            timeout=self.timeout,
        )
        props = (prop_payload.get("PropertyTable") or {}).get("Properties") or []
        return {
            "source": self.name,
            "status": "found",
            "term": term,
            "records": [
                {
                    "cid": item.get("CID"),
                    "molecular_formula": item.get("MolecularFormula"),
                    "molecular_weight": item.get("MolecularWeight"),
                    "iupac_name": item.get("IUPACName"),
                    "canonical_smiles": item.get("CanonicalSMILES"),
                    "isomeric_smiles": item.get("IsomericSMILES"),
                    "url": f"https://pubchem.ncbi.nlm.nih.gov/compound/{item.get('CID')}",
                }
                for item in props
            ],
        }


@dataclass
class ChEMBLAnnotationProvider:
    timeout: float = DEFAULT_TIMEOUT
    max_terms: int = 5
    limit: int = 1
    max_workers: int = 4
    name: str = "chembl"

    def __post_init__(self) -> None:
        self._molecule_cache: dict[str, dict[str, Any]] = {}

    def annotate(self, *, query: str, evidence_dossier: dict[str, Any]) -> list[dict[str, Any]]:
        terms = _chembl_brdk_candidate_terms(evidence_dossier, max_terms=self.max_terms)
        if not terms:
            return []
        with ThreadPoolExecutor(max_workers=min(self.max_workers, len(terms))) as executor:
            hits = list(executor.map(self._annotate_molecule, terms))
        return [hit for hit in hits if hit]

    def _annotate_molecule(self, term: str) -> dict[str, Any]:
        cache_key = term.strip().lower()
        if cache_key in self._molecule_cache:
            return self._molecule_cache[cache_key]
        search_url = "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json?" + urllib.parse.urlencode({"q": term, "limit": str(self.limit)})
        payload = _http_json(search_url, timeout=self.timeout)
        molecules = payload.get("molecules") or []
        records = []
        for molecule in molecules[: self.limit]:
            chembl_id = molecule.get("molecule_chembl_id")
            mechanisms = []
            if chembl_id:
                mech_url = "https://www.ebi.ac.uk/chembl/api/data/mechanism.json?" + urllib.parse.urlencode({"molecule_chembl_id": chembl_id, "limit": "10"})
                mech_payload = _http_json(mech_url, timeout=self.timeout)
                mechanisms = [
                    self._mechanism_record(item)
                    for item in (mech_payload.get("mechanisms") or [])
                ]
            records.append(
                {
                    "molecule_chembl_id": chembl_id,
                    "pref_name": molecule.get("pref_name"),
                    "molecule_type": molecule.get("molecule_type"),
                    "max_phase": molecule.get("max_phase"),
                    "therapeutic_flag": molecule.get("therapeutic_flag"),
                    "mechanisms": mechanisms,
                    "url": f"https://www.ebi.ac.uk/chembl/explore/compound/{chembl_id}" if chembl_id else None,
                }
            )
        hit = {"source": self.name, "status": "found" if records else "no_hits", "term": term, "records": records}
        self._molecule_cache[cache_key] = hit
        return hit

    def _mechanism_record(self, item: dict[str, Any]) -> dict[str, Any]:
        target_id = item.get("target_chembl_id")
        return {
            "mechanism_of_action": item.get("mechanism_of_action"),
            "target_chembl_id": target_id,
            "target_name": item.get("target_pref_name"),
            "action_type": item.get("action_type"),
        }


@dataclass
class GeneCardsHarmonizomeAnnotationProvider:
    timeout: float = DEFAULT_TIMEOUT
    max_terms: int = 5
    include_associations: bool = False
    name: str = "genecards_harmonizome"

    def annotate(self, *, query: str, evidence_dossier: dict[str, Any]) -> list[dict[str, Any]]:
        records = []
        for symbol in _gene_terms(evidence_dossier, max_terms=self.max_terms):
            hit = self._annotate_gene(symbol)
            if hit:
                records.append(hit)
        return records

    def _annotate_gene(self, symbol: str) -> dict[str, Any]:
        clean = _clean_gene_symbol(symbol)
        if not clean:
            return {"source": self.name, "status": "skipped", "term": symbol, "records": []}
        params = {"showAssociations": "true"} if self.include_associations else {}
        query = ("?" + urllib.parse.urlencode(params)) if params else ""
        url = f"https://maayanlab.cloud/Harmonizome/api/1.0/gene/{urllib.parse.quote(clean, safe='')}{query}"
        try:
            payload = _http_json(url, timeout=self.timeout)
        except urllib.error.HTTPError as exc:
            return {"source": self.name, "status": "http_error", "term": clean, "http_status": exc.code, "url": url, "records": []}
        except Exception as exc:
            return {"source": self.name, "status": "failed", "term": clean, "reason": f"{type(exc).__name__}: {exc}", "url": url, "records": []}
        if not isinstance(payload, dict) or payload.get("status") == 404:
            return {"source": self.name, "status": "no_hits", "term": clean, "url": url, "records": []}
        record = _normalize_harmonizome_gene_record(clean, payload, url)
        return {"source": self.name, "status": "found", "term": clean, "records": [record]}


@dataclass
class DrugBankUnavailableProvider:
    name: str = "drugbank"

    def annotate(self, *, query: str, evidence_dossier: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            {
                "source": self.name,
                "status": "unavailable",
                "reason": "DrugBank is not enabled by default because PxFquery has no public unauthenticated DrugBank API configured.",
            }
        ]


@dataclass
class UnavailableAnnotationProvider:
    name: str
    reason: str

    def annotate(self, *, query: str, evidence_dossier: dict[str, Any]) -> list[dict[str, Any]]:
        return [{"source": self.name, "status": "unavailable", "reason": self.reason}]


def _primary_terms(evidence_dossier: dict[str, Any]) -> list[dict[str, str]]:
    layer = evidence_dossier.get("evidence_layer") or {}
    intent = layer.get("intent_evidence") or {}
    matrix = layer.get("matrix_evidence") or {}
    primary = matrix.get("primary_result") or {}
    terms: list[dict[str, str]] = []
    if intent.get("pert_desc"):
        terms.append({"term": str(intent["pert_desc"]), "role": str(intent.get("pert_class") or "perturbation")})
    if primary.get("perturbation"):
        terms.append({"term": str(primary["perturbation"]), "role": "perturbation"})
    for item in primary.get("top_perturbations") or []:
        label = item.get("label") or item.get("cmap_name") or item.get("pert_id")
        if label:
            role = "compound" if primary.get("modality") == "cp" or item.get("recommended_operation") == "drug_treat" else "gene_or_reagent"
            terms.append({"term": str(label), "role": role})
    if intent.get("bio_context"):
        terms.append({"term": str(intent["bio_context"]), "role": "context"})
    for key in ("function_desc", "activate", "suppress"):
        if intent.get(key):
            terms.append({"term": str(intent[key]), "role": "function"})
    return _dedupe_terms(terms)


def _compound_terms(evidence_dossier: dict[str, Any], *, max_terms: int) -> list[str]:
    layer = evidence_dossier.get("evidence_layer") or {}
    intent = layer.get("intent_evidence") or {}
    matrix = layer.get("matrix_evidence") or {}
    if str(intent.get("pert_class") or "").lower() not in {"drug", "compound"} and not _matrix_has_compound_routes(matrix):
        return []

    terms: list[str] = []
    aliased_perturbations: set[str] = set()
    for route in matrix.get("executed_routes") or []:
        if route.get("modality") != "cp":
            continue
        alias = route.get("perturbation_alias")
        perturbation = route.get("perturbation")
        if alias and _looks_like_compound_term(str(alias)):
            terms.append(str(alias))
            if perturbation:
                aliased_perturbations.add(str(perturbation))
        elif perturbation and _looks_like_compound_term(str(perturbation)):
            terms.append(str(perturbation))

    primary = matrix.get("primary_result") or {}
    if primary.get("modality") == "cp":
        alias = primary.get("perturbation_alias")
        perturbation = primary.get("perturbation")
        if alias and _looks_like_compound_term(str(alias)):
            terms.append(str(alias))
        elif perturbation and str(perturbation) not in aliased_perturbations and _looks_like_compound_term(str(perturbation)):
            terms.append(str(perturbation))

    if not terms and intent.get("pert_class") == "drug" and intent.get("pert_desc"):
        term = str(intent["pert_desc"])
        if _looks_like_compound_term(term):
            terms.append(term)

    return [item["term"] for item in _dedupe_terms([{"term": term, "role": "compound"} for term in terms])[:max_terms]]


def _gene_terms(evidence_dossier: dict[str, Any], *, max_terms: int) -> list[str]:
    layer = evidence_dossier.get("evidence_layer") or {}
    intent = layer.get("intent_evidence") or {}
    matrix = layer.get("matrix_evidence") or {}
    terms: list[str] = []
    if str(intent.get("pert_class") or "").lower() == "genetic" and intent.get("pert_desc"):
        terms.append(str(intent["pert_desc"]))
    primary = matrix.get("primary_result") or {}
    if primary.get("modality") in {"sh", "xpr"}:
        for value in [primary.get("perturbation"), primary.get("cmap_name"), primary.get("label")]:
            if value:
                terms.append(str(value))
        for item in primary.get("top_perturbations") or []:
            label = item.get("label") or item.get("cmap_name") or item.get("pert_id")
            if label:
                terms.append(str(label))
    for route in matrix.get("executed_routes") or []:
        if route.get("modality") not in {"sh", "xpr"}:
            continue
        for value in [route.get("perturbation"), route.get("cmap_name"), route.get("label")]:
            if value:
                terms.append(str(value))
        for item in route.get("top_perturbations") or []:
            label = item.get("label") or item.get("cmap_name") or item.get("pert_id")
            if label:
                terms.append(str(label))
    clean_terms = []
    for term in terms:
        clean = _clean_gene_symbol(term)
        if clean:
            clean_terms.append(clean)
    return [item["term"] for item in _dedupe_terms([{"term": term, "role": "gene"} for term in clean_terms])[:max_terms]]


def _clean_gene_symbol(value: Any) -> str | None:
    text = str(value or "").strip()
    if not text:
        return None
    if text.upper().startswith(("BRD-", "BRDN", "TRCN", "CSS001", "CGS001")):
        return None
    if "_" in text:
        parts = [part for part in text.split("_") if part]
        text = parts[-1] if parts else text
    text = text.strip()
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9-]{1,14}", text):
        return None
    return text.upper()


def _chembl_brdk_candidate_terms(evidence_dossier: dict[str, Any], *, max_terms: int) -> list[str]:
    layer = evidence_dossier.get("evidence_layer") or {}
    intent = layer.get("intent_evidence") or {}
    matrix = layer.get("matrix_evidence") or {}
    if str(intent.get("pert_class") or "").lower() not in {"drug", "compound"} and not _matrix_has_compound_routes(matrix):
        return []

    candidates = _brdk_candidate_rows(matrix)
    terms = []
    for item in candidates[:5]:
        term = _visible_brdk_candidate_term(item)
        if term:
            terms.append(term)
    return [item["term"] for item in _dedupe_terms([{"term": term, "role": "compound"} for term in terms])[:max_terms]]


def _brdk_candidate_rows(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    primary = matrix.get("primary_result") or {}
    if matrix.get("mode") == "forward":
        rows = []
        alias = primary.get("perturbation_alias")
        perturbation = primary.get("perturbation")
        if alias:
            rows.append({"label": alias, "pert_id": perturbation})
        elif perturbation:
            rows.append({"label": perturbation, "pert_id": perturbation})
        for route in matrix.get("executed_routes") or []:
            if route.get("modality") != "cp":
                continue
            alias = route.get("perturbation_alias")
            perturbation = route.get("perturbation")
            if alias:
                rows.append({"label": alias, "pert_id": perturbation})
            elif perturbation:
                rows.append({"label": perturbation, "pert_id": perturbation})
        return rows
    if matrix.get("mode") != "reverse":
        return []
    if primary.get("modality") == "cp":
        return list(primary.get("top_perturbations") or [])
    rows = []
    for route in matrix.get("executed_routes") or []:
        if route.get("modality") == "cp":
            rows.extend(route.get("top_perturbations") or [])
    return rows


def _visible_brdk_candidate_term(item: dict[str, Any]) -> str | None:
    visible = str(item.get("label") or item.get("cmap_name") or "").strip()
    if visible.upper().startswith("BRD-K"):
        return visible
    pert_id = str(item.get("pert_id") or "").strip()
    if not visible and pert_id.upper().startswith("BRD-K"):
        return pert_id
    return None


def _matrix_has_compound_routes(matrix: dict[str, Any]) -> bool:
    primary = matrix.get("primary_result") or {}
    if primary.get("modality") == "cp":
        return True
    return any(route.get("modality") == "cp" for route in matrix.get("executed_routes") or [])


def _looks_like_compound_term(term: str) -> bool:
    text = str(term or "").strip()
    upper = text.upper()
    if not text:
        return False
    if upper.startswith(("CSS001", "CGS001", "TRCN")):
        return False
    if len(text) <= 2 and upper == text:
        return False
    return True


def _pubmed_query_from_parts(query: str | None, terms: list[dict[str, str]]) -> str:
    key_terms = [item["term"] for item in terms if item.get("role") in {"drug", "compound", "perturbation", "context", "function"}]
    if not key_terms and query:
        key_terms = [query]
    key_terms = [term for term in _dedupe_plain(key_terms) if term]
    if not key_terms:
        return ""
    quoted = [f"{_escape_pubmed_term(term)}[Title/Abstract]" for term in key_terms[:4]]
    if len(quoted) == 1:
        return quoted[0]
    return " AND ".join(quoted[:3])


def _escape_pubmed_term(term: str) -> str:
    return '"' + str(term).replace('"', "").strip() + '"'


def _normalize_harmonizome_gene_record(symbol: str, payload: dict[str, Any], url: str) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {"symbol": symbol, "raw": payload, "url": url}
    associations = payload.get("associations") or []
    return {
        "symbol": payload.get("symbol") or symbol,
        "display_name": payload.get("name") or payload.get("symbol") or symbol,
        "summary": payload.get("description") or "",
        "aliases": payload.get("synonyms") if isinstance(payload.get("synonyms"), list) else [],
        "ncbi_entrez_gene_id": payload.get("ncbiEntrezGeneId"),
        "ncbi_entrez_gene_url": payload.get("ncbiEntrezGeneUrl"),
        "proteins": payload.get("proteins") or [],
        "association_count": len(associations) if isinstance(associations, list) else None,
        "associations": associations[:20] if isinstance(associations, list) else [],
        "url": url,
        "raw": payload,
    }


def _dedupe_terms(terms: list[dict[str, str]]) -> list[dict[str, str]]:
    seen = set()
    out = []
    for item in terms:
        term = " ".join(str(item.get("term") or "").strip().split())
        if not term:
            continue
        key = term.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append({"term": term, "role": str(item.get("role") or "unknown")})
    return out


def _dedupe_plain(terms: list[str]) -> list[str]:
    return [item["term"] for item in _dedupe_terms([{"term": term, "role": "term"} for term in terms])]


def _http_json(url: str, *, timeout: float = DEFAULT_TIMEOUT, retries: int = 1) -> dict[str, Any]:
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "pxfquery/annotation"})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError:
            raise
        except Exception as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"annotation_http_json_failed: {last_error}")

