from urllib.parse import parse_qs, urlparse

from pxfquery.l4_evidence.annotation import (
    ChEMBLAnnotationProvider,
    GeneCardsHarmonizomeAnnotationProvider,
    PubChemAnnotationProvider,
    PubMedAnnotationProvider,
    default_annotation_providers,
)
from pxfquery.l4_evidence.annotation import providers as provider_module


def _dossier():
    return {
        "schema_version": "l4-evidence-dossier/v1",
        "dossier_status": "evidence_found",
        "claim_basis": {"main_claim": "erlotinib in A375"},
        "evidence_layer": {
            "intent_evidence": {
                "pert_desc": "erlotinib",
                "pert_class": "drug",
                "bio_context": "A375",
                "function_desc": "apoptosis",
            },
            "matrix_evidence": {
                "mode": "forward",
                "primary_result": {
                    "cell": "A375",
                    "perturbation": "erlotinib",
                    "modality": "cp",
                    "n_rows": 1,
                },
            },
        },
    }


def test_default_annotation_providers_include_real_public_sources_and_drugbank_unavailable():
    providers = default_annotation_providers(("pubmed", "pubchem", "chembl", "drugbank"), timeout=1)

    assert [provider.name for provider in providers] == ["pubmed", "pubchem", "chembl", "drugbank"]
    assert providers[-1].annotate(query="x", evidence_dossier=_dossier())[0]["status"] == "unavailable"


def test_default_annotation_providers_include_gene_external_sources():
    providers = default_annotation_providers(("genecards_harmonizome",), timeout=1)

    assert [provider.name for provider in providers] == ["genecards_harmonizome"]
    assert isinstance(providers[0], GeneCardsHarmonizomeAnnotationProvider)


def test_pubmed_provider_uses_eutils_search_and_summary(monkeypatch):
    calls = []

    def fake_http_json(url, *, timeout=20.0, retries=1):
        calls.append(url)
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if parsed.path.endswith("/esearch.fcgi"):
            assert params["db"] == ["pubmed"]
            assert params["retmode"] == ["json"]
            assert "erlotinib" in params["term"][0]
            return {"esearchresult": {"idlist": ["123", "456"]}}
        if parsed.path.endswith("/esummary.fcgi"):
            assert params["id"] == ["123,456"]
            return {
                "result": {
                    "123": {"title": "Erlotinib and apoptosis", "fulljournalname": "Journal A", "pubdate": "2020"},
                    "456": {"title": "A375 response", "source": "Journal B", "pubdate": "2021"},
                }
            }
        raise AssertionError(url)

    monkeypatch.setattr(provider_module, "_http_json", fake_http_json)

    records = PubMedAnnotationProvider(timeout=1).annotate(query="erlotinib A375 apoptosis", evidence_dossier=_dossier())

    assert len(calls) == 2
    assert records[0]["status"] == "searched"
    assert records[0]["records"][0]["pmid"] == "123"
    assert records[0]["records"][0]["url"] == "https://pubmed.ncbi.nlm.nih.gov/123/"


def test_pubchem_provider_fetches_cid_and_properties(monkeypatch):
    def fake_http_json(url, *, timeout=20.0, retries=1):
        if "/cids/JSON" in url:
            assert "erlotinib" in url
            return {"IdentifierList": {"CID": [176870]}}
        if "/property/" in url:
            return {
                "PropertyTable": {
                    "Properties": [
                        {
                            "CID": 176870,
                            "MolecularFormula": "C22H23N3O4",
                            "MolecularWeight": 393.4,
                            "IUPACName": "erlotinib",
                            "CanonicalSMILES": "COCCOC1=CC2=C(C=C1OCCOC)N=CN=C2NC3=CC=CC=C3C#C",
                        }
                    ]
                }
            }
        raise AssertionError(url)

    monkeypatch.setattr(provider_module, "_http_json", fake_http_json)

    records = PubChemAnnotationProvider(timeout=1).annotate(query="x", evidence_dossier=_dossier())

    assert records[0]["status"] == "found"
    assert records[0]["term"] == "erlotinib"
    assert records[0]["records"][0]["cid"] == 176870


def _reverse_drug_dossier_with_candidates():
    dossier = _dossier()
    dossier["evidence_layer"]["matrix_evidence"] = {
        "mode": "reverse",
        "primary_result": {
            "cell": "A375",
            "modality": "cp",
            "top_perturbations": [
                {"rank": 1, "label": "afatinib", "pert_id": "BRD-K66175015"},
                {"rank": 2, "label": "BRD-K63750851", "pert_id": "BRD-K63750851"},
                {"rank": 3, "label": "AZD-9291", "pert_id": "BRD-K42805893"},
                {"rank": 4, "label": "BRD-K12345678", "pert_id": "BRD-K12345678"},
                {"rank": 5, "label": "BRD-K87654321", "pert_id": "BRD-K87654321"},
                {"rank": 6, "label": "BRD-K00000000", "pert_id": "BRD-K00000000"},
            ],
        },
        "executed_routes": [],
    }
    return dossier


def test_chembl_provider_fetches_only_visible_brdk_reverse_candidates(monkeypatch):
    searched_terms = []

    def fake_http_json(url, *, timeout=20.0, retries=1):
        if "molecule/search.json" in url:
            searched_terms.append(parse_qs(urlparse(url).query)["q"][0])
            return {"molecules": [{"molecule_chembl_id": "CHEMBL553", "pref_name": "ERLOTINIB", "molecule_type": "Small molecule"}]}
        if "mechanism.json" in url:
            return {
                "mechanisms": [
                    {
                        "mechanism_of_action": "EGFR inhibitor",
                        "target_chembl_id": "CHEMBL203",
                        "target_pref_name": "Epidermal growth factor receptor",
                        "action_type": "INHIBITOR",
                    }
                ]
            }
        assert "target/CHEMBL203.json" not in url
        raise AssertionError(url)

    monkeypatch.setattr(provider_module, "_http_json", fake_http_json)

    records = ChEMBLAnnotationProvider(timeout=1).annotate(query="x", evidence_dossier=_reverse_drug_dossier_with_candidates())

    assert sorted(searched_terms) == sorted(["BRD-K63750851", "BRD-K12345678", "BRD-K87654321"])
    assert records[0]["status"] == "found"
    assert records[0]["term"] == "BRD-K63750851"
    assert records[0]["records"][0]["molecule_chembl_id"] == "CHEMBL553"
    assert records[0]["records"][0]["mechanisms"][0]["target_name"] == "Epidermal growth factor receptor"


def test_chembl_provider_queries_forward_visible_brdk_but_not_readable_names(monkeypatch):
    searched_terms = []

    def fake_http_json(url, *, timeout=20.0, retries=1):
        if "molecule/search.json" in url:
            searched_terms.append(parse_qs(urlparse(url).query)["q"][0])
            return {"molecules": []}
        raise AssertionError(url)

    monkeypatch.setattr(provider_module, "_http_json", fake_http_json)

    forward_brdk = _dossier()
    forward_brdk["evidence_layer"]["matrix_evidence"]["primary_result"]["perturbation"] = "BRD-K00000001"
    assert ChEMBLAnnotationProvider(timeout=1).annotate(query="x", evidence_dossier=forward_brdk)[0]["term"] == "BRD-K00000001"
    assert searched_terms == ["BRD-K00000001"]


def test_chembl_provider_does_not_query_non_brdk_readable_names(monkeypatch):
    calls = []

    def fake_http_json(url, *, timeout=20.0, retries=1):
        calls.append(url)
        raise AssertionError(url)

    monkeypatch.setattr(provider_module, "_http_json", fake_http_json)

    assert ChEMBLAnnotationProvider(timeout=1).annotate(query="x", evidence_dossier=_dossier()) == []
    readable_reverse = _reverse_drug_dossier_with_candidates()
    readable_reverse["evidence_layer"]["matrix_evidence"]["primary_result"]["top_perturbations"] = [
        {"rank": 1, "label": "afatinib", "pert_id": "BRD-K66175015"},
        {"rank": 2, "label": "AZD-9291", "pert_id": "BRD-K42805893"},
    ]
    assert ChEMBLAnnotationProvider(timeout=1).annotate(query="x", evidence_dossier=readable_reverse) == []
    assert calls == []


def test_compound_terms_skip_genetic_routes_and_prefer_alias_over_brd():
    genetic = _dossier()
    genetic["evidence_layer"]["intent_evidence"]["pert_class"] = "genetic"
    genetic["evidence_layer"]["matrix_evidence"]["primary_result"] = {
        "cell": "A549",
        "perturbation": "MYC",
        "modality": "sh",
    }
    genetic["evidence_layer"]["matrix_evidence"]["executed_routes"] = [
        {"cell": "A549", "perturbation": "MYC", "modality": "sh"}
    ]

    drug = _dossier()
    drug["evidence_layer"]["matrix_evidence"]["executed_routes"] = [
        {
            "cell": "A549",
            "perturbation": "BRD-K61468417",
            "perturbation_alias": "doxorubicin",
            "modality": "cp",
        }
    ]

    assert provider_module._compound_terms(genetic, max_terms=5) == []
    drug_terms = provider_module._compound_terms(drug, max_terms=5)
    assert "doxorubicin" in drug_terms
    assert "BRD-K61468417" not in drug_terms


def test_gene_terms_clean_symbols_and_skip_reagent_ids():
    dossier = _dossier()
    dossier["evidence_layer"]["intent_evidence"]["pert_class"] = "genetic"
    dossier["evidence_layer"]["intent_evidence"]["pert_desc"] = "KRAS-2B"
    dossier["evidence_layer"]["matrix_evidence"] = {
        "mode": "reverse",
        "primary_result": {
            "cell": "A549",
            "modality": "sh",
            "top_perturbations": [
                {"label": "TSAI_VEGFA"},
                {"label": "TRCN0000001"},
                {"label": "BRDN0000733847"},
            ],
        },
        "executed_routes": [
            {"cell": "A549", "modality": "xpr", "perturbation": "MYC"},
        ],
    }

    assert provider_module._gene_terms(dossier, max_terms=10) == ["KRAS-2B", "VEGFA", "MYC"]


def test_genecards_harmonizome_provider_uses_harmonizome_gene_endpoint(monkeypatch):
    def fake_http_json(url, *, timeout=20.0, retries=1):
        assert url == "https://maayanlab.cloud/Harmonizome/api/1.0/gene/MYC"
        return {
            "symbol": "MYC",
            "name": "MYC proto-oncogene",
            "description": "MYC encodes a transcription factor.",
            "synonyms": ["BHLHE39", "C-MYC"],
            "ncbiEntrezGeneId": 4609,
            "ncbiEntrezGeneUrl": "http://www.ncbi.nlm.nih.gov/gene/4609",
            "proteins": [{"symbol": "MYC_HUMAN"}],
        }

    monkeypatch.setattr(provider_module, "_http_json", fake_http_json)
    dossier = _dossier()
    dossier["evidence_layer"]["intent_evidence"]["pert_class"] = "genetic"
    dossier["evidence_layer"]["intent_evidence"]["pert_desc"] = "MYC"

    records = GeneCardsHarmonizomeAnnotationProvider(timeout=1).annotate(query="x", evidence_dossier=dossier)

    assert records[0]["status"] == "found"
    assert records[0]["records"][0]["display_name"] == "MYC proto-oncogene"
    assert records[0]["records"][0]["aliases"] == ["BHLHE39", "C-MYC"]
    assert records[0]["records"][0]["ncbi_entrez_gene_id"] == 4609
