from pathlib import Path
import threading
import time

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent
from pxfquery.l2_routing.index.cellline_index import CellLineIndex
from pxfquery.l2_routing.router import _expanded_tree_cells
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


class _ConcurrentProvider:
    def __init__(self):
        self.lock = threading.Lock()
        self.active = 0
        self.max_active = 0

    def request_json(self, *, stage, system_prompt, user_payload, temperature=0, validator=None):
        with self.lock:
            self.active += 1
            self.max_active = max(self.max_active, self.active)
        try:
            time.sleep(0.05)
            payload = self._payload(stage)
            if validator is not None:
                validator(payload)
            return payload, {
                "provider": "fake",
                "base_url": "memory://fake",
                "model": "fake-concurrent",
                "final_status": "ok",
                "attempts": [{"attempt": 1, "ok": True}],
                "parsed_json_hash": stage,
            }
        finally:
            with self.lock:
                self.active -= 1

    @staticmethod
    def _payload(stage):
        if stage == "cell_tree_lineage":
            return {"selected_option": "skin"}
        if stage == "cell_tree_disease":
            return {"selected_option": "skin cancer"}
        if stage == "cell_tree_subtype":
            return {"selected_option": "melanoma"}
        if stage == "drug_normalization":
            return {"selected_alias": "erlotinib", "hypothesis_names": []}
        if stage == "function_mapping":
            return {"selected_var_names": ["HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION"]}
        if stage == "function_reverse_mapping_direct_pathway":
            return {"selected_var_names": ["HALLMARK_APOPTOSIS"]}
        if stage == "function_reverse_mapping_mechanism_or_program":
            return {"selected_var_names": ["HALLMARK_E2F_TARGETS"]}
        if stage == "function_reverse_mapping_phenotype_or_state":
            return {"selected_var_names": ["HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION"]}
        raise AssertionError(f"unexpected LLM stage: {stage}")


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


def test_l2_routes_cell_line_mentions_with_cells_suffix_as_exact():
    assert STANDARD_RESOURCES.exists()
    for context, expected in [("A549 cells", "A549"), ("MCF7 cells", "MCF7")]:
        intent = _intent(
            bio_context=context,
            pert_desc="doxorubicin",
            pert_class="drug",
            function_desc="pathways affected",
        )

        route = route_intent(intent, index_dir=STANDARD_RESOURCES).to_dict()

        assert route["route_status"] == "routed"
        assert route["cell_route"]["mode"] == "exact-cell-with-lineage-proxies"
        assert route["cell_route"]["selected"] == [expected]
        assert not any(call["stage"].startswith("cell_tree_") for call in route["llm_calls"])


def test_l2_marks_normal_same_lineage_anchor_as_semantic_downgrade():
    assert STANDARD_RESOURCES.exists()
    cell_index = CellLineIndex(STANDARD_RESOURCES / "cellline_index.json", STANDARD_RESOURCES / "cellline_neighbors.json")

    expanded = _expanded_tree_cells(["MCF7"], cell_index)
    normal_anchors = [item for item in expanded if item.get("cell_expansion_scope") == "normal_lineage_data_anchor"]

    assert normal_anchors
    assert all(item["source_disease"] == "breast cancer" for item in normal_anchors)
    assert all(item["cell_route_distance"] >= 3 for item in normal_anchors)
    assert all(item.get("semantic_downgrade_reason") for item in normal_anchors)


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


def test_l2_routes_cell_perturbation_and_function_dimensions_in_parallel_with_stable_output_order():
    assert STANDARD_RESOURCES.exists()
    provider = _ConcurrentProvider()
    intent = _intent(
        bio_context="melanoma models",
        pert_desc="erlotnib typo",
        pert_class="drug",
        function_desc="invasive mesenchymal transition",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES, llm_provider=provider).to_dict()

    assert route["route_status"] == "routed"
    assert provider.max_active > 1
    assert [call["stage"] for call in route["llm_calls"]] == [
        "cell_tree_lineage",
        "cell_tree_disease",
        "cell_tree_subtype",
        "drug_normalization",
        "function_mapping",
    ]
    assert route["cell_route"]["mode"] == "llm-cell-tree-selection"
    assert route["perturbation_route"]["mode"] == "llm-normalized-drug"
    assert route["function_route"]["selected"][0]["var_name"] == "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION"


def test_l2_routes_reverse_function_interpretation_passes_in_parallel_with_stable_output_order():
    assert STANDARD_RESOURCES.exists()
    provider = _ConcurrentProvider()
    intent = _intent(
        query_type="reverse",
        bio_context="A549",
        pert_class="drug",
        function_desc="more epithelial differentiation and less cell cycling",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES, llm_provider=provider).to_dict()

    assert route["route_status"] == "routed"
    assert provider.max_active == 3
    assert [call["stage"] for call in route["llm_calls"]] == [
        "function_reverse_mapping_direct_pathway",
        "function_reverse_mapping_mechanism_or_program",
        "function_reverse_mapping_phenotype_or_state",
    ]
    assert [item["perspective"] for item in route["function_route"]["interpretation_sets"]] == [
        "direct_pathway",
        "mechanism_or_program",
        "phenotype_or_state",
    ]
