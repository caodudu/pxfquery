from pathlib import Path
import threading
import time

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent
from pxfquery.l2_routing.combination import _genetic_modality_plan, _genetic_reverse_mode, _make_forward_route, _rank_routes_by_quality, _reverse_modalities
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


class _CellTreeRepairProvider:
    def __init__(self):
        self.stages = []

    def request_json(self, *, stage, system_prompt, user_payload, temperature=0, validator=None):
        self.stages.append(stage)
        if stage == "cell_tree_lineage":
            payload = {}
        elif stage == "cell_tree_lineage_empty_object_repair":
            payload = {"selected_option": "central_nervous_system", "reason": "glioblastoma is a CNS tumor"}
        elif stage == "cell_tree_disease":
            payload = {"selected_option": "brain cancer"}
        elif stage == "cell_tree_subtype":
            payload = {"selected_option": "glioblastoma"}
        else:
            payload = {"selected_var_names": ["HALLMARK_E2F_TARGETS"]}
        return payload, {
            "provider": "fake",
            "base_url": "memory://fake",
            "model": "fake-cell-repair",
            "final_status": "ok",
            "attempts": [{"attempt": 1, "ok": True}],
            "parsed_json_hash": stage,
        }


class _ProstateProvider:
    def request_json(self, *, stage, system_prompt, user_payload, temperature=0, validator=None):
        if stage == "cell_tree_lineage":
            payload = {"selected_option": "prostate"}
        elif stage == "cell_tree_subtype":
            payload = {"selected_option": "carcinoma"}
        elif stage.startswith("function_reverse_mapping_"):
            payload = {"selected_var_names": ["HALLMARK_APOPTOSIS"]}
        else:
            payload = {}
        return payload, {
            "provider": "fake",
            "base_url": "memory://fake",
            "model": "fake-prostate",
            "final_status": "ok",
            "attempts": [{"attempt": 1, "ok": True}],
            "parsed_json_hash": stage,
        }


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


def test_l2_exact_drug_routes_include_readable_aliases_from_packaged_index():
    assert STANDARD_RESOURCES.exists()
    intent = _intent(
        bio_context="A549",
        pert_desc="doxorubicin",
        pert_class="drug",
        function_desc="pathways affected",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES).to_dict()

    selected = route["perturbation_route"]["selected"][0]
    assert selected["id"] == "BRD-K61468417"
    assert selected["alias"] == "doxorubicin"
    assert "doxorubicin" in selected["aliases"]
    assert route["perturbation_route"]["proxies"]
    assert route["perturbation_route"]["proxies"][0]["id"].startswith("BRD-")


def test_l2_marks_normal_same_lineage_anchor_as_semantic_downgrade():
    assert STANDARD_RESOURCES.exists()
    cell_index = CellLineIndex(STANDARD_RESOURCES / "cellline_index.json", STANDARD_RESOURCES / "cellline_neighbors.json")

    expanded = _expanded_tree_cells(["MCF7"], cell_index)
    normal_anchors = [item for item in expanded if item.get("cell_expansion_scope") == "normal_lineage_data_anchor"]

    assert normal_anchors
    assert all(item["source_disease"] == "breast cancer" for item in normal_anchors)
    assert all(item["cell_route_distance"] >= 3 for item in normal_anchors)
    assert all(item.get("semantic_downgrade_reason") for item in normal_anchors)


def test_l2_genetic_modality_plan_treats_xpr_as_crispr_lof_not_overexpression():
    crispr = _intent(pert_class="genetic", genetic_modality="crispr")
    xpr = _intent(pert_class="genetic", genetic_modality="xpr")
    knockout = _intent(pert_class="genetic", genetic_modality="knockout")
    gof = _intent(pert_class="genetic", genetic_modality="overexpression")
    unknown = _intent(pert_class="genetic", genetic_modality=None)

    assert _genetic_modality_plan(crispr) == {"primary_modalities": ["xpr"], "fallback_modalities": []}
    assert _genetic_modality_plan(xpr) == {"primary_modalities": ["xpr"], "fallback_modalities": []}
    assert _genetic_modality_plan(knockout) == {"primary_modalities": ["xpr"], "fallback_modalities": ["sh"]}
    assert _genetic_modality_plan(gof) == {"primary_modalities": ["xpr", "sh"], "fallback_modalities": []}
    assert _genetic_reverse_mode("xpr", crispr) == "perturbation_only"
    assert _genetic_reverse_mode("xpr", gof) == "activation_only"
    assert _genetic_reverse_mode("xpr", unknown) == "bidirectional"


def test_l2_reverse_genetic_modality_sources_follow_requested_operation():
    crispr = _intent(query_type="reverse", pert_class="genetic", genetic_modality="crispr")
    xpr = _intent(query_type="reverse", pert_class="genetic", genetic_modality="xpr")
    knockout = _intent(query_type="reverse", pert_class="genetic", genetic_modality="knockout")
    lof = _intent(query_type="reverse", pert_class="genetic", genetic_modality="lof")

    assert _reverse_modalities(crispr) == ["xpr"]
    assert _reverse_modalities(xpr) == ["xpr"]
    assert _reverse_modalities(knockout) == ["xpr", "sh"]
    assert _reverse_modalities(lof) == ["xpr", "sh"]


def test_l2_crispr_fallback_sh_route_carries_lower_modality_quality():
    intent = _intent(pert_class="genetic", genetic_modality="knockout")
    cell = {"cell": "A549", "role": "exact", "cell_expansion_scope": "exact", "cell_route_distance": 0}
    pert = {"symbol": "IGF2R", "role": "exact", "rank": 1}

    xpr_route = _make_forward_route(intent, 1, "A", "exact", cell, pert, ["xpr"], True)
    sh_route = _make_forward_route(intent, 2, "A", "exact", cell, pert, ["sh"], True)

    assert xpr_route["modality_rank"] == "primary"
    assert xpr_route["modality_match_distance"] == 0.0
    assert xpr_route["route_quality_score"] == 0.0
    assert sh_route["modality_rank"] == "fallback"
    assert sh_route["modality_match_type"] == "loss_of_function_proxy"
    assert sh_route["modality_match_distance"] > xpr_route["modality_match_distance"]
    assert sh_route["route_quality_score"] == xpr_route["route_quality_score"]


def test_l2_drug_forward_route_keeps_exact_modality_quality():
    intent = _intent(pert_class="drug", genetic_modality=None)
    cell = {"cell": "A549", "role": "exact", "cell_expansion_scope": "exact", "cell_route_distance": 0}
    pert = {"id": "BRD-K70401845", "alias": "erlotinib", "role": "exact", "rank": 1}

    route = _make_forward_route(intent, 1, "A", "exact", cell, pert, ["cp"], True)

    assert route["modality_rank"] == "primary"
    assert route["modality_match_type"] == "exact_requested"
    assert route["modality_match_distance"] == 0.0
    assert route["route_quality_score"] == 0.0


def test_l2_crispr_primary_modality_proxy_ranks_before_fallback_exact():
    intent = _intent(pert_class="genetic", genetic_modality="knockout")
    cell = {"cell": "A549", "role": "exact", "cell_expansion_scope": "exact", "cell_route_distance": 0}
    exact = {"symbol": "TARGET", "role": "exact", "rank": 1}
    proxy = {"symbol": "PROXY", "role": "supporting-semantic-neighbor", "similarity": 0.75, "rank": 1}

    sh_exact = _make_forward_route(intent, 1, "A", "exact", cell, exact, ["sh"], True)
    xpr_proxy = _make_forward_route(intent, 2, "B", "proxy", cell, proxy, ["xpr"], True)

    ranked = _rank_routes_by_quality([sh_exact, xpr_proxy])

    assert ranked[0]["perturbation"] == "PROXY"
    assert ranked[0]["modality"] == "xpr"
    assert ranked[0]["modality_rank"] == "primary"
    assert ranked[1]["perturbation"] == "TARGET"
    assert ranked[1]["modality"] == "sh"
    assert ranked[1]["modality_rank"] == "fallback"


def test_l2_knockdown_route_sort_does_not_prioritize_modality_over_exact_gene():
    intent = _intent(pert_class="genetic", genetic_modality="knockdown")
    cell = {"cell": "MCF7", "role": "exact", "cell_expansion_scope": "exact", "cell_route_distance": 0}
    exact = {"symbol": "TARGET", "role": "exact", "rank": 1}
    proxy = {"symbol": "PROXY", "role": "supporting-semantic-neighbor", "similarity": 0.75, "rank": 1}

    xpr_exact = _make_forward_route(intent, 1, "A", "exact", cell, exact, ["xpr"], True)
    sh_proxy = _make_forward_route(intent, 2, "B", "proxy", cell, proxy, ["sh"], True)

    ranked = _rank_routes_by_quality([xpr_exact, sh_proxy])

    assert ranked[0]["perturbation"] == "TARGET"
    assert ranked[0]["modality"] == "xpr"
    assert ranked[0]["modality_rank"] == "fallback"
    assert ranked[1]["perturbation"] == "PROXY"
    assert ranked[1]["modality"] == "sh"
    assert ranked[1]["modality_rank"] == "primary"


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


def test_l2_cell_tree_repairs_empty_json_and_records_repair_attempt():
    assert STANDARD_RESOURCES.exists()
    provider = _CellTreeRepairProvider()
    intent = _intent(
        query_type="reverse",
        bio_context="glioblastoma",
        pert_class="drug",
        function_desc="less proliferative",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES, llm_provider=provider).to_dict()

    assert route["cell_route"]["status"] == "resolved"
    assert route["cell_route"]["selected"] == ["GI1"]
    lineage_call = next(call for call in route["llm_calls"] if call["stage"] == "cell_tree_lineage")
    assert lineage_call["repair_attempted"] is True
    assert "cell_tree_lineage_empty_object_repair" in provider.stages


def test_l2_cell_tree_uses_unique_tree_option_without_llm_call():
    assert STANDARD_RESOURCES.exists()
    provider = _ProstateProvider()
    intent = _intent(
        query_type="reverse",
        bio_context="prostate cancer",
        pert_class="drug",
        function_desc="apoptosis",
    )

    route = route_intent(intent, index_dir=STANDARD_RESOURCES, llm_provider=provider).to_dict()

    assert route["cell_route"]["status"] == "resolved"
    skipped = [call for call in route["llm_calls"] if call.get("selection_method") == "deterministic_unique_tree_option"]
    assert skipped
    assert all(call["validated"] for call in skipped)
