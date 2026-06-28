from __future__ import annotations

import html
import json
import os
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TASK_ROOT = Path(__file__).resolve().parents[1]
ROUTE_REPORT = Path(os.environ.get("PXFQUERY_ROUTE_REPORT", TASK_ROOT / "4_artifact" / "5_table" / "t137_60_l2_validation_latest.json"))
STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)
OUT_TABLE = TASK_ROOT / "4_artifact" / "5_table"
OUT_DOC = TASK_ROOT / "4_artifact" / "3_document"
NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL = "pxfquery_route_reasonableness_audit"
EMAIL = os.environ.get("NCBI_EMAIL", "pxfquery.audit@example.com")
MAX_PMIDS = 3
REQUEST_INTERVAL_SECONDS = float(os.environ.get("NCBI_REQUEST_INTERVAL_SECONDS", "0.55" if not os.environ.get("NCBI_API_KEY") else "0.2"))
LAST_REQUEST_AT = 0.0


def main() -> int:
    route_data = json.loads(ROUTE_REPORT.read_text(encoding="utf-8"))
    resources = _load_resource_helpers()
    cache: dict[str, dict[str, Any]] = {}
    records = []
    for record in route_data["records"]:
        intent = record["route"]["intent"]
        selected = record["route"].get("combination_route", {}).get("selected_routes", [])[:3]
        route_audits = [_audit_selected_route(intent, route, resources, cache) for route in selected]
        records.append(
            {
                "case_id": record["case_id"],
                "query": record["query"],
                "intent": intent,
                "case_reasonableness": _case_reasonableness(route_audits),
                "selected_route_audits": route_audits,
            }
        )
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_route_report": str(ROUTE_REPORT),
        "audit_scope": "External route reasonableness, not internal data availability and not PubMed co-occurrence scoring.",
        "verdict_scale": {
            "direct": "selected route directly matches user semantics and has external support where needed",
            "acceptable_proxy": "selected route is a defensible proxy with external support for the proxy relation",
            "data_only_anchor": "selected route is executable in data but external semantic support for the user context is weak or absent",
            "unsupported": "external support is missing for a required route proposition",
            "wrong": "external evidence contradicts a required route proposition",
        },
        "pubmed": {"base": NCBI_BASE, "tool": TOOL, "email": EMAIL, "max_pmids": MAX_PMIDS},
        "summary": _summary(records),
        "records": records,
    }
    OUT_TABLE.mkdir(parents=True, exist_ok=True)
    OUT_DOC.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = OUT_TABLE / f"route_reasonableness_audit_{stamp}.json"
    html_path = OUT_DOC / f"route_reasonableness_audit_{stamp}.html"
    latest_json = OUT_TABLE / "route_reasonableness_audit_latest.json"
    latest_html = OUT_DOC / "route_reasonableness_audit_latest.html"
    text = json.dumps(result, ensure_ascii=False, indent=2)
    json_path.write_text(text, encoding="utf-8")
    latest_json.write_text(text, encoding="utf-8")
    html_text = _html(result)
    html_path.write_text(html_text, encoding="utf-8")
    latest_html.write_text(html_text, encoding="utf-8")
    print(json_path)
    print(html_path)
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    return 0


def _audit_selected_route(intent: dict[str, Any], route: dict[str, Any], resources: dict[str, Any], cache: dict[str, dict[str, Any]]) -> dict[str, Any]:
    cell = str(route.get("cell") or "")
    context = str(intent.get("bio_context") or "")
    perturbation = _perturbation_label(route, resources)
    functions = _function_labels(intent, route)
    cell_audit = _audit_cell_reasonableness(cell, context, route, cache)
    perturbation_audit = _audit_perturbation_reasonableness(intent, route, perturbation, cache)
    function_audit = _audit_function_reasonableness(intent, route, functions, cache)
    verdict = _combine_verdict(cell_audit, perturbation_audit, function_audit)
    return {
        "route_id": route.get("route_id"),
        "cell": cell,
        "perturbation": perturbation,
        "modality": route.get("modality") or route.get("modalities"),
        "cell_expansion_scope": route.get("cell_expansion_scope"),
        "pair_search_round": route.get("pair_search_round"),
        "reasonableness": verdict,
        "cell_audit": cell_audit,
        "perturbation_audit": perturbation_audit,
        "function_audit": function_audit,
    }


def _audit_cell_reasonableness(cell: str, context: str, route: dict[str, Any], cache: dict[str, dict[str, Any]]) -> dict[str, Any]:
    scope = route.get("cell_expansion_scope")
    if not cell:
        return {"verdict": "not_applicable", "reason": "No cell scope was selected."}
    if _mentions_cell(context, cell):
        return {"verdict": "direct", "reason": "User explicitly named this cell line.", "evidence": []}
    if not context:
        return {"verdict": "acceptable_proxy", "reason": "No user cell context was requested; selected cell only scopes available data.", "evidence": []}
    query = _pubmed_cell_context_query(cell, context)
    evidence = _pubmed_search(query, cache) if query else _empty_evidence(query)
    has_support = evidence["count"] > 0
    if str(scope).startswith("observed_"):
        verdict = "acceptable_proxy" if has_support else "data_only_anchor"
        reason = "Observed anchor has external support for the requested context." if has_support else "Observed anchor is data-executable but not externally supported as a semantic match to the requested context."
    elif scope in {"exact", "selected_leaf"}:
        verdict = "direct" if has_support else "unsupported"
        reason = "Selected cell is externally supported for the requested context." if has_support else "Selected cell lacks external support for the requested context."
    elif scope in {"same_disease_sibling", "same_subtype", "same_lineage"}:
        verdict = "acceptable_proxy" if has_support else "unsupported"
        reason = "Proxy cell is externally supported for the requested context." if has_support else "Proxy cell lacks external support for the requested context."
    else:
        verdict = "weak" if has_support else "unsupported"
        reason = "Cell has some external context support." if has_support else "No external cell-context support found."
    return {"verdict": verdict, "reason": reason, "pubmed_query": query, "evidence": evidence}


def _audit_perturbation_reasonableness(intent: dict[str, Any], route: dict[str, Any], perturbation: str, cache: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if intent.get("query_type") == "reverse":
        modality = str(route.get("modality") or "")
        requested = str(intent.get("genetic_modality") or "").lower()
        if requested in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"} and modality == "sh":
            return {"verdict": "acceptable_proxy", "reason": "Resource lacks CRISPR modality; shRNA is a loss-of-function proxy and route labels it as such."}
        if requested in {"rnai", "shrna", "sh", "sirna", "knockdown"} and modality == "sh":
            return {"verdict": "direct", "reason": "Requested RNAi/knockdown modality matches sh resource modality."}
        if requested in {"overexpression", "xpr", "gof", "gain_of_function"} and modality == "xpr":
            return {"verdict": "direct", "reason": "Requested overexpression modality matches xpr resource modality."}
        if not requested and modality in {"sh", "xpr"}:
            return {"verdict": "acceptable_proxy", "reason": "User requested genetic perturbations without specifying sh/xpr; both modalities are valid route scopes."}
        return {"verdict": "unsupported", "reason": f"Requested modality {requested or 'unspecified'} does not clearly match selected modality {modality}."}
    if not perturbation:
        return {"verdict": "not_applicable", "reason": "No forward perturbation label is available."}
    role = str(route.get("perturbation_role") or "")
    user_term = str(intent.get("pert_desc") or "")
    if _term_overlap(perturbation, user_term) or role in {"exact", "llm-normalized"}:
        query = _pubmed_perturbation_identity_query(perturbation, user_term)
        evidence = _pubmed_search(query, cache) if query else _empty_evidence(query)
        verdict = "direct" if evidence["count"] > 0 or _term_overlap(perturbation, user_term) else "unsupported"
        return {"verdict": verdict, "reason": "Perturbation identity matches user term or LLM-normalized exact entity.", "pubmed_query": query, "evidence": evidence}
    if "proxy" in role or "neighbor" in role:
        return {"verdict": "acceptable_proxy", "reason": f"Selected perturbation is explicitly labeled as {role}; it should be interpreted as proxy evidence, not exact evidence."}
    return {"verdict": "unsupported", "reason": "Perturbation relation to user term is not externally justified by route metadata."}


def _audit_function_reasonableness(intent: dict[str, Any], route: dict[str, Any], functions: list[str], cache: dict[str, dict[str, Any]]) -> dict[str, Any]:
    user_terms = " ".join([str(intent.get("function_desc") or ""), *map(str, intent.get("activate") or []), *map(str, intent.get("suppress") or [])]).strip()
    if intent.get("query_type") == "forward" and not user_terms:
        return {"verdict": "not_applicable", "reason": "Forward query asks for broad outputs; L2 correctly does not force a function filter."}
    if not functions:
        return {"verdict": "not_applicable", "reason": "No function route is selected for this route."}
    labels = " ".join(functions)
    if _semantic_function_overlap(user_terms, labels):
        return {"verdict": "direct", "reason": "Selected function labels semantically match user function terms.", "function_labels": functions}
    query = _pubmed_function_query(user_terms, labels)
    evidence = _pubmed_search(query, cache) if query else _empty_evidence(query)
    verdict = "acceptable_proxy" if evidence["count"] > 0 else "unsupported"
    return {"verdict": verdict, "reason": "Function mapping uses external literature support." if evidence["count"] > 0 else "Function mapping lacks external support and weak lexical agreement.", "pubmed_query": query, "evidence": evidence, "function_labels": functions}


def _combine_verdict(*audits: dict[str, Any]) -> str:
    verdicts = [a["verdict"] for a in audits if a["verdict"] != "not_applicable"]
    if "wrong" in verdicts:
        return "wrong"
    if "data_only_anchor" in verdicts:
        return "data_only_anchor"
    if "unsupported" in verdicts:
        return "unsupported"
    if all(v == "direct" for v in verdicts):
        return "direct"
    return "acceptable_proxy"


def _case_reasonableness(routes: list[dict[str, Any]]) -> str:
    rank = {"direct": 5, "acceptable_proxy": 4, "data_only_anchor": 3, "unsupported": 2, "wrong": 1}
    return max((r["reasonableness"] for r in routes), key=lambda value: rank.get(value, 0)) if routes else "unsupported"


def _load_resource_helpers() -> dict[str, Any]:
    drug_alias_by_id: dict[str, list[str]] = {}
    drug_index_path = STANDARD_RESOURCES / "drug_index.json"
    if drug_index_path.exists():
        data = json.loads(drug_index_path.read_text(encoding="utf-8"))
        for alias, brd in data.items():
            drug_alias_by_id.setdefault(str(brd), []).append(str(alias))
    return {"drug_alias_by_id": drug_alias_by_id}


def _perturbation_label(route: dict[str, Any], resources: dict[str, Any]) -> str:
    record = route.get("perturbation_record") or {}
    for key in ("alias", "symbol", "name"):
        if record.get(key):
            return str(record[key])
    value = route.get("perturbation") or record.get("id")
    if value and str(value).startswith("BRD-"):
        aliases = resources["drug_alias_by_id"].get(str(value), [])
        if aliases:
            return aliases[0]
    return str(value or "")


def _function_labels(intent: dict[str, Any], route: dict[str, Any]) -> list[str]:
    labels = []
    for function in route.get("functions") or []:
        labels.append(str(function.get("label") or function.get("var_name") or ""))
    if intent.get("function_desc"):
        labels.append(str(intent["function_desc"]))
    return [label for label in dict.fromkeys(labels) if label]


def _mentions_cell(context: str, cell: str) -> bool:
    return bool(cell and re.search(rf"\b{re.escape(cell)}\b", context, flags=re.I))


def _term_overlap(a: str, b: str) -> bool:
    aa = set(_tokens(a))
    bb = set(_tokens(b))
    return bool(aa and bb and (aa & bb))


def _semantic_function_overlap(user_terms: str, labels: str) -> bool:
    synonyms = {
        "apoptosis": {"apoptosis", "programmed", "death"},
        "cell cycle": {"cell", "cycle", "e2f", "g2m", "proliferation", "cycling"},
        "emt": {"emt", "epithelial", "mesenchymal", "invasion", "invasive"},
        "myc": {"myc"},
        "kras": {"kras", "ras", "mapk"},
        "interferon": {"interferon", "immune", "inflammatory"},
        "hypoxia": {"hypoxia"},
        "dna repair": {"dna", "repair", "damage"},
        "androgen": {"androgen"},
    }
    user = set(_tokens(user_terms))
    label = set(_tokens(labels))
    if user & label:
        return True
    for words in synonyms.values():
        if user & words and label & words:
            return True
    return False


def _tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-zA-Z0-9]+", str(text).lower()) if len(t) > 1 and t not in {"cell", "cells", "model", "models", "context", "broad", "function", "functional"}]


def _pubmed_cell_context_query(cell: str, context: str) -> str:
    context = _clean_context(context)
    if not context:
        return ""
    return f'("{cell}"[Title/Abstract]) AND ({context}) AND ("cell line"[Title/Abstract] OR cells[Title/Abstract])'


def _pubmed_perturbation_identity_query(perturbation: str, user_term: str) -> str:
    terms = [term for term in {_clean_phrase(perturbation), _clean_phrase(user_term)} if term]
    if not terms:
        return ""
    if len(terms) == 1:
        return f'"{terms[0]}"[Title/Abstract]'
    return " AND ".join(f'"{term}"[Title/Abstract]' for term in terms)


def _pubmed_function_query(user_terms: str, labels: str) -> str:
    left = _clean_phrase(user_terms)
    right = _clean_phrase(labels)
    if not left or not right:
        return ""
    return f'"{left}"[Title/Abstract] AND "{right}"[Title/Abstract]'


def _clean_context(context: str) -> str:
    text = _clean_phrase(context)
    replacements = {
        "lung cancer": '("lung cancer"[Title/Abstract] OR "lung carcinoma"[Title/Abstract] OR NSCLC[Title/Abstract])',
        "breast cancer": '"breast cancer"[Title/Abstract]',
        "ovarian cancer": '"ovarian cancer"[Title/Abstract]',
        "melanoma": 'melanoma[Title/Abstract]',
        "colon cancer": '("colon cancer"[Title/Abstract] OR "colorectal cancer"[Title/Abstract])',
        "liver cancer": '("liver cancer"[Title/Abstract] OR "hepatocellular carcinoma"[Title/Abstract])',
        "pancreatic cancer": '"pancreatic cancer"[Title/Abstract]',
        "prostate cancer": '"prostate cancer"[Title/Abstract]',
        "leukemia": 'leukemia[Title/Abstract]',
        "glioma": 'glioma[Title/Abstract]',
        "kidney cancer": '("kidney cancer"[Title/Abstract] OR "renal cell carcinoma"[Title/Abstract])',
        "gastric cancer": '"gastric cancer"[Title/Abstract]',
        "neural tumor": '("neural tumor"[Title/Abstract] OR neuroblastoma[Title/Abstract] OR glioma[Title/Abstract])',
        "tumor": '(tumor[Title/Abstract] OR cancer[Title/Abstract] OR carcinoma[Title/Abstract])',
    }
    for key, value in replacements.items():
        if key in text:
            return value
    if not text:
        return ""
    return f'"{text}"[Title/Abstract]'


def _clean_phrase(text: str) -> str:
    text = re.sub(r"[_/]+", " ", str(text).lower())
    text = re.sub(r"\b(cells?|models?|context|like|broad|functional|signatures?|readouts?|programs?|what|which|does|after|before)\b", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _pubmed_search(query: str, cache: dict[str, dict[str, Any]]) -> dict[str, Any]:
    if query in cache:
        return cache[query]
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": str(MAX_PMIDS), "tool": TOOL, "email": EMAIL}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?{urllib.parse.urlencode(params)}"
    try:
        payload = _open_json(url)
        result = payload.get("esearchresult", {})
        pmids = result.get("idlist", [])
        evidence = {"query": query, "count": int(result.get("count", 0)), "pmids": pmids, "papers": _pubmed_summaries(pmids, cache)}
    except Exception as exc:
        evidence = {"query": query, "count": 0, "pmids": [], "papers": [], "error": f"{type(exc).__name__}: {exc}"}
    cache[query] = evidence
    return evidence


def _pubmed_summaries(pmids: list[str], cache: dict[str, dict[str, Any]]) -> list[dict[str, str]]:
    if not pmids:
        return []
    key = "summary:" + ",".join(pmids)
    if key in cache:
        return cache[key]["papers"]
    params = {"db": "pubmed", "id": ",".join(pmids), "retmode": "json", "tool": TOOL, "email": EMAIL}
    if os.environ.get("NCBI_API_KEY"):
        params["api_key"] = os.environ["NCBI_API_KEY"]
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?{urllib.parse.urlencode(params)}"
    papers = []
    try:
        payload = _open_json(url)
        result = payload.get("result", {})
        for pmid in pmids:
            item = result.get(pmid, {})
            if item:
                papers.append({"pmid": pmid, "title": item.get("title", ""), "pubdate": item.get("pubdate", ""), "source": item.get("source", "")})
    except Exception as exc:
        papers.append({"pmid": "", "title": f"summary_error: {type(exc).__name__}: {exc}", "pubdate": "", "source": ""})
    cache[key] = {"papers": papers}
    return papers


def _open_json(url: str) -> dict[str, Any]:
    global LAST_REQUEST_AT
    now = time.monotonic()
    wait = REQUEST_INTERVAL_SECONDS - (now - LAST_REQUEST_AT)
    if wait > 0:
        time.sleep(wait)
    with urllib.request.urlopen(url, timeout=30) as handle:
        payload = json.loads(handle.read().decode("utf-8"))
    LAST_REQUEST_AT = time.monotonic()
    return payload


def _summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    case_counts = Counter(record["case_reasonableness"] for record in records)
    route_counts = Counter(route["reasonableness"] for record in records for route in record["selected_route_audits"])
    cases_by_level: dict[str, list[str]] = {}
    for record in records:
        cases_by_level.setdefault(record["case_reasonableness"], []).append(record["case_id"])
    return {"case_counts": dict(case_counts), "route_counts": dict(route_counts), "cases_by_level": cases_by_level}


def _html(result: dict[str, Any]) -> str:
    rows = []
    for record in result["records"]:
        compact = [
            {
                "route_id": route["route_id"],
                "cell": route["cell"],
                "perturbation": route["perturbation"],
                "scope": route["cell_expansion_scope"],
                "verdict": route["reasonableness"],
                "cell": route["cell_audit"]["verdict"],
                "pert": route["perturbation_audit"]["verdict"],
                "function": route["function_audit"]["verdict"],
                "cell_reason": route["cell_audit"]["reason"],
            }
            for route in record["selected_route_audits"]
        ]
        rows.append(
            "<tr>"
            f"<td>{html.escape(record['case_id'])}</td>"
            f"<td>{html.escape(record['case_reasonableness'])}</td>"
            f"<td>{html.escape(record['query'])}</td>"
            f"<td><pre>{html.escape(json.dumps(compact, ensure_ascii=False, indent=2))}</pre></td>"
            "</tr>"
        )
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>L2 route reasonableness audit</title>
<style>body{{font-family:-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif;margin:24px}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ccc;padding:6px;vertical-align:top}}pre{{white-space:pre-wrap;font-size:12px}}</style>
</head><body><h1>L2 route reasonableness audit</h1>
<pre>{html.escape(json.dumps({'source': result['source_route_report'], 'summary': result['summary'], 'scope': result['audit_scope']}, ensure_ascii=False, indent=2))}</pre>
<table><thead><tr><th>Case</th><th>Verdict</th><th>Query</th><th>Selected route audits</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
</body></html>"""


def _empty_evidence(query: str) -> dict[str, Any]:
    return {"query": query, "count": 0, "pmids": [], "papers": []}


if __name__ == "__main__":
    raise SystemExit(main())
