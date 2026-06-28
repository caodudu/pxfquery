from pathlib import Path

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent
from pxfquery.l2_routing.router import route_intent


STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)


def _intent(**kwargs):
    payload = {
        "raw_query": "test query",
        "normalized_query": "test query",
        "query_type": "forward",
        "bio_context": None,
        "pert_desc": None,
        "pert_class": None,
        "genetic_modality": None,
        "function_desc": None,
    }
    payload.update(kwargs)
    return QueryIntent(**payload)


def test_l2_routes_exact_cell_noncoding_gene_and_function_from_real_indexes():
    assert STANDARD_RESOURCES.exists()
    intent = _intent(
        bio_context="A549",
        pert_desc="MALAT1",
        pert_class="genetic",
        function_desc="apoptosis",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES).to_dict()

    assert route["route_status"] == "routed"
    assert route["cell_route"]["selected"] == ["A549"]
    assert len(route["cell_route"]["candidates"]) <= 6
    assert route["perturbation_route"]["selected"][0]["symbol"] == "MALAT1"
    assert route["perturbation_route"]["selected"][0]["gene_type"] == "lncRNA"
    assert route["perturbation_route"]["selected"][0]["in_matrix"] is False
    assert route["perturbation_route"]["noncoding_supported"] is True
    assert len(route["perturbation_route"]["proxies"]) <= 5
    assert route["function_route"]["selected"][0]["var_name"] == "HALLMARK_APOPTOSIS"
    assert route["llm_calls"] == []


def test_l2_reports_resource_missing_without_registered_indexes():
    intent = _intent(
        bio_context="A549",
        pert_desc="MALAT1",
        pert_class="genetic",
        function_desc="apoptosis",
    )

    route = route_intent(intent).to_dict()

    assert route["route_status"] == "resource-missing"
    assert route["resource_status"]["available"] == {}
    assert "resource indexes" in route["reason"]


def test_l2_does_not_promote_fuzzy_drug_candidates_without_llm_decision():
    assert STANDARD_RESOURCES.exists()
    intent = _intent(
        bio_context="A549",
        pert_desc="erlotnib typo",
        pert_class="drug",
        function_desc="apoptosis",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES).to_dict()

    assert route["route_status"] == "llm_unavailable"
    assert route["perturbation_route"]["status"] == "llm-required"
    assert route["perturbation_route"]["selected"] == []
    assert route["perturbation_route"]["retrieved_candidates"]
    assert route["llm_calls"][0]["stage"] == "drug_normalization"
    assert route["llm_calls"][0]["status"] == "required"


def test_pp_route_uses_registered_resource_pack_and_is_primary_public_route_entry():
    assert STANDARD_RESOURCES.exists()
    pxf = PxFQuery()
    pxf.resources.use(STANDARD_RESOURCES)
    qdata = pxf.read.query("test query")
    qdata.uns["_intent"] = _intent(
        bio_context="A549",
        pert_desc="MALAT1",
        pert_class="genetic",
        function_desc="apoptosis",
    )
    qdata.uns["intent"] = qdata.uns["_intent"].to_dict()

    pxf.pp.route(qdata)

    route = pxf.get.route(qdata)
    assert route["schema_version"] == "l2-route-plan/v2"
    assert route["route_status"] == "routed"
    assert route["resource_status"]["available"]["function_index"].endswith("function_index.json")
