import os
from pathlib import Path

import pytest

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent
from pxfquery.l4_evidence import assemble_evidence


DEFAULT_STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)

STANDARD_RESOURCES = Path(os.environ.get("PXFQUERY_TEST_STANDARD_RESOURCES", DEFAULT_STANDARD_RESOURCES))
L3_LIGHT_RESOURCES_ENV = os.environ.get("PXFQUERY_TEST_L3_LIGHT_RESOURCES")


def _require_standard_resources() -> Path:
    if not STANDARD_RESOURCES.exists():
        pytest.skip("set PXFQUERY_TEST_STANDARD_RESOURCES to run resource-backed L4 tests")
    return STANDARD_RESOURCES


def _require_l3_light_resources() -> Path:
    if not L3_LIGHT_RESOURCES_ENV:
        pytest.skip("set PXFQUERY_TEST_L3_LIGHT_RESOURCES to run real L4 matrix evidence tests")
    path = Path(L3_LIGHT_RESOURCES_ENV)
    if not path.exists():
        pytest.skip(f"PXFQUERY_TEST_L3_LIGHT_RESOURCES does not exist: {path}")
    return path


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


def _qdata_with_intent(pxf: PxFQuery, intent: QueryIntent):
    qdata = pxf.read.query(intent.raw_query)
    qdata.uns["_intent"] = intent
    qdata.uns["intent"] = intent.to_dict()
    return qdata


def test_l4_rejects_bad_l3_schema_as_invalid_upstream_schema():
    dossier = assemble_evidence(
        {"schema_version": "bad-schema", "execution_status": "executed"},
        intent={"query_type": "forward"},
        route_plan={"schema_version": "l2-route-plan/v2"},
    )

    assert dossier["schema_version"] == "l4-evidence-dossier/v1"
    assert dossier["dossier_status"] == "invalid_upstream_schema"
    assert dossier["claim_basis"]["answerability"] == "not_answered"
    assert "change_scores" in dossier["rendering_hints"]["forbidden_transformations"]


def test_l4_partial_evidence_keeps_partial_status_and_limitation():
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q1",
        "query_type": "forward",
        "execution_status": "partial",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [
            {
                "route_id": "forward_001",
                "query_type": "forward",
                "modality": "cp",
                "status": "executed",
                "cell": "CELL_A",
                "route_metadata": {"tier": "exact_cell_exact_perturbation", "perturbation": "PERT_A"},
                "row_match": {"n_rows": 2, "cmap_names": ["PERT_A"], "pert_ids": ["BRD-A"]},
                "scores": {
                    "requested_functions": {"FUNCTION_A": 1.0},
                    "requested_function_records": [{"label": "FUNCTION_A", "score": 1.0}],
                    "score_orientation": "observed_perturbation_effect",
                    "score_multiplier": 1,
                },
                "rankings": {"top_activated": [{"label": "FUNCTION_A", "score": 1.0}], "top_suppressed": []},
                "diagnostics": {},
            }
        ],
        "skipped_routes": [
            {
                "route_id": "forward_002",
                "query_type": "forward",
                "modality": "cp",
                "status": "empty_matrix_hit",
                "route_metadata": {"tier": "exact_cell_proxy_perturbation"},
                "row_match": {},
                "diagnostics": {"message": "no rows matched route cell and perturbation"},
            }
        ],
        "errors": [{"code": "empty_matrix_hit", "message": "no rows matched route cell and perturbation"}],
        "warnings": [],
    }
    route_plan = {
        "schema_version": "l2-route-plan/v2",
        "query_id": "q1",
        "route_status": "routed",
        "combination_route": {"selected_routes": [{"tier": "exact_cell_exact_perturbation"}]},
    }

    dossier = assemble_evidence(execution, intent={"query_type": "forward", "bio_context": "CELL_A", "pert_desc": "PERT_A"}, route_plan=route_plan)

    assert dossier["dossier_status"] == "partial_evidence"
    assert dossier["claim_basis"]["answerability"] == "partially_answered"
    assert dossier["claim_basis"]["claim_strength"] == "low"
    assert any(item["code"] == "partial_evidence" for item in dossier["uncertainty_layer"]["limitations"])
    assert dossier["evidence_layer"]["matrix_evidence"]["primary_result"]["n_rows"] == 2


def test_l4_keeps_rejected_candidates_out_of_default_route_evidence():
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q-debug",
        "query_type": "forward",
        "execution_status": "executed",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [
            {
                "route_id": "forward_001",
                "query_type": "forward",
                "modality": "cp",
                "status": "executed",
                "cell": "A375",
                "route_metadata": {"tier": "exact_cell_exact_perturbation", "perturbation": "erlotinib"},
                "row_match": {"n_rows": 1},
                "scores": {"requested_functions": {}},
                "rankings": {"top_activated": [], "top_suppressed": []},
                "diagnostics": {},
            }
        ],
        "skipped_routes": [],
        "errors": [],
        "warnings": [],
    }
    route_plan = {
        "schema_version": "l2-route-plan/v2",
        "route_status": "routed",
        "combination_route": {"selected_routes": [{"tier": "exact_cell_exact_perturbation"}]},
        "rejected_candidates": [{"candidate": "wrong-context"}],
    }

    dossier = assemble_evidence(execution, intent={"query_type": "forward"}, route_plan=route_plan)
    debug_dossier = assemble_evidence(execution, intent={"query_type": "forward"}, route_plan=route_plan, debug=True)

    assert "rejected_candidates" not in dossier["evidence_layer"]["route_evidence"]
    assert dossier["audit_layer"]["debug"]["default_visibility"] == "hidden"
    assert dossier["audit_layer"]["debug"]["rejected_candidates"] == []
    assert debug_dossier["audit_layer"]["debug"]["rejected_candidates"] == [{"candidate": "wrong-context"}]


def test_l4_synthesis_payload_preserves_exact_primary_with_proxy_support_semantics():
    class Provider:
        def __init__(self):
            self.system_prompts = {}
            self.user_payloads = {}

        def request_json(self, *, stage, system_prompt, user_payload, temperature=0):
            self.system_prompts[stage] = system_prompt
            self.user_payloads[stage] = user_payload
            if stage.startswith("l4_forward_biological_answer"):
                return {
                    "answer": "Erlotinib in A375 cells activates stress programs.",
                    "subquestions": [],
                }, {"provider": "fake", "final_status": "ok", "attempts": [], "parsed_json_hash": "bio"}
            return {
                "summary": "Exact primary matrix evidence with proxy support.",
                "verdict_rationale": "primary exact route plus proxy references",
                "confidence_rationale": "moderate",
            }, {"provider": "fake", "final_status": "ok", "attempts": [], "parsed_json_hash": "audit"}

    provider = Provider()
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q-synthesis",
        "query_type": "forward",
        "execution_status": "executed",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [
            {
                "route_id": "forward_001",
                "query_type": "forward",
                "modality": "cp",
                "status": "executed",
                "cell": "A375",
                "route_metadata": {"tier": "exact_cell_exact_perturbation", "perturbation": "erlotinib"},
                "row_match": {"n_rows": 1},
                "scores": {"requested_functions": {}},
                "rankings": {"top_activated": [], "top_suppressed": []},
                "diagnostics": {},
            }
        ],
        "skipped_routes": [],
        "errors": [],
        "warnings": [],
    }
    route_plan = {
        "schema_version": "l2-route-plan/v2",
        "route_status": "routed",
        "combination_route": {
            "selected_routes": [
                {"tier": "exact_cell_exact_perturbation"},
                {"tier": "exact_cell_proxy_perturbation"},
            ]
        },
    }

    dossier = assemble_evidence(
        execution,
        intent={"query_type": "forward", "bio_context": "A375", "pert_desc": "erlotinib"},
        route_plan=route_plan,
        llm_provider=provider,
        synthesize=True,
    )

    assert dossier["evidence_layer"]["evidence_grade"] == "exact_primary_with_proxy_support"
    bio_stage = "l4_forward_biological_answer"
    assert "biological answer writer" in provider.system_prompts[bio_stage]
    assert "Do not mention PxFquery" in provider.system_prompts[bio_stage]
    assert "audit_context" not in provider.user_payloads[bio_stage]
    assert "claim_basis" not in provider.user_payloads[bio_stage]
    assert provider.user_payloads[bio_stage]["interpreted_intent"]["cell"] == "A375"
    assert provider.user_payloads["l4_execution_quality"]["audit_context"]["evidence_grade"] == "exact_primary_with_proxy_support"
    synthesis = dossier["evidence_layer"]["llm_synthesis"]
    assert synthesis["summary"] == "Erlotinib in A375 cells activates stress programs."
    assert synthesis["biological_summary"] == synthesis["summary"]
    assert synthesis["evidence_audit_summary"] == "Exact primary matrix evidence with proxy support."
    assert "all selected evidence routes were exact" in dossier["claim_basis"]["must_not_claim"]


def test_l4_reverse_concept_context_payload_does_not_promote_primary_cell():
    class Provider:
        def __init__(self):
            self.system_prompt = ""
            self.user_payload = {}
            self.stages = []

        def request_json(self, *, stage, system_prompt, user_payload, temperature=0):
            self.stages.append(stage)
            if stage.startswith("l4_reverse_biological_answer"):
                self.system_prompt = system_prompt
                self.user_payload = user_payload
                return {
                    "answer": "Across NSCLC model-set profiles, afatinib is the most consistently supported candidate.",
                    "subquestions": [],
                    "candidate_interpretation": ["afatinib: candidate supported across multiple NSCLC model-set profiles"],
                    "support_notes": [],
                }, {"provider": "fake", "final_status": "ok", "attempts": []}
            return {"summary": "Reverse query executed."}, {"provider": "fake", "final_status": "ok", "attempts": []}

    provider = Provider()
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q-reverse",
        "query_type": "reverse",
        "execution_status": "executed",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [
            {
                "route_id": "reverse_001",
                "query_type": "reverse",
                "modality": "cp",
                "status": "executed",
                "cell": "HCC827",
                "route_metadata": {"cell_match_type": "concept_representative_cell", "route_quality_score": 0.025},
                "row_match": {"n_rows": 3, "n_ranked_groups": 3},
                "rankings": {"top_perturbations": [{"rank": 1, "label": "AZD-9291", "pert_id": "BRD-A", "score": 16.0}]},
                "scores": {},
                "diagnostics": {},
            },
            {
                "route_id": "reverse_002",
                "query_type": "reverse",
                "modality": "cp",
                "status": "executed",
                "cell": "NCIH1573",
                "route_metadata": {"cell_match_type": "concept_representative_cell", "route_quality_score": 0.025},
                "row_match": {"n_rows": 100, "n_ranked_groups": 100},
                "rankings": {"top_perturbations": [{"rank": 1, "label": "afatinib", "pert_id": "BRD-B", "score": 30.0}]},
                "scores": {},
                "diagnostics": {},
            },
        ],
        "skipped_routes": [],
        "errors": [],
        "warnings": [],
    }

    assemble_evidence(
        execution,
        intent={"query_type": "reverse", "bio_context": "NSCLC model set", "function_desc": "suppress MYC targets"},
        route_plan={"schema_version": "l2-route-plan/v2", "route_status": "routed"},
        llm_provider=provider,
        synthesize=True,
    )

    assert provider.user_payload["interpreted_intent"]["context_scope"] == "concept_or_disease_model_set"
    assert provider.user_payload["interpreted_intent"]["cell"] is None
    assert provider.user_payload["interpreted_intent"]["searched_cells"] == ["HCC827", "NCIH1573"]
    assert provider.user_payload["candidate_summary"][0]["label"] in {"AZD-9291", "afatinib"}
    assert "Do not frame the answer as" in provider.system_prompt


def test_l4_reverse_payload_hides_unreadable_genetic_reagent_ids_from_llm():
    class Provider:
        def __init__(self):
            self.user_payload = {}

        def request_json(self, *, stage, system_prompt, user_payload, temperature=0):
            if stage.startswith("l4_reverse_biological_answer"):
                self.user_payload = user_payload
                return {"answer": "AURKA is the readable candidate.", "subquestions": []}, {"provider": "fake"}
            return {"summary": "Reverse query executed."}, {"provider": "fake"}

    provider = Provider()
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q-reverse-genetic",
        "query_type": "reverse",
        "execution_status": "executed",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [
            {
                "route_id": "reverse_001",
                "query_type": "reverse",
                "modality": "xpr",
                "status": "executed",
                "cell": "A549",
                "route_metadata": {"cell_match_type": "concept_representative_cell"},
                "row_match": {"n_rows": 10, "n_ranked_groups": 10},
                "rankings": {
                    "top_perturbations": [
                        {"rank": 1, "label": "BRDN0000733847", "pert_id": "BRDN0000733847", "score": 10.0},
                        {"rank": 2, "label": "AURKA", "pert_id": "BRDN0001148015", "cmap_name": "AURKA", "score": 9.0},
                    ]
                },
                "scores": {},
                "diagnostics": {},
            }
        ],
        "skipped_routes": [],
        "errors": [],
        "warnings": [],
    }

    assemble_evidence(
        execution,
        intent={"query_type": "reverse", "bio_context": "NSCLC model set", "function_desc": "activate apoptosis"},
        route_plan={"schema_version": "l2-route-plan/v2", "route_status": "routed"},
        llm_provider=provider,
        synthesize=True,
    )

    assert [row["label"] for row in provider.user_payload["candidate_summary"]] == ["AURKA"]
    profile_candidates = provider.user_payload["evidence_profiles"][0]["candidate_perturbations"]
    assert [row["label"] for row in profile_candidates] == ["AURKA"]


def test_l4_synthesis_repairs_quality_report_style_summary():
    class Provider:
        def __init__(self):
            self.stages = []

        def request_json(self, *, stage, system_prompt, user_payload, temperature=0):
            self.stages.append(stage)
            if stage == "l4_forward_biological_answer":
                return {
                    "answer": "PxFquery found evidence grade exact_primary_with_proxy_support.",
                    "subquestions": [],
                }, {"provider": "fake", "final_status": "ok", "attempts": [], "parsed_json_hash": "bad"}
            if stage == "l4_biological_answer_repair":
                return {
                    "answer": "Erlotinib in A375 cells activates stress programs and suppresses cholesterol homeostasis.",
                    "subquestions": [],
                }, {"provider": "fake", "final_status": "ok", "attempts": [], "parsed_json_hash": "repair"}
            return {
                "summary": "Exact primary matrix evidence is present, with proxy routes as supporting references.",
                "verdict_rationale": "Exact primary matrix evidence is present, with proxy routes as supporting references.",
                "confidence_rationale": "Moderate because the primary evidence has one matched row.",
            }, {"provider": "fake", "final_status": "ok", "attempts": [], "parsed_json_hash": "audit"}

    provider = Provider()
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q-repair",
        "query_type": "forward",
        "execution_status": "executed",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [
            {
                "route_id": "forward_001",
                "query_type": "forward",
                "modality": "cp",
                "status": "executed",
                "cell": "A375",
                "route_metadata": {"tier": "exact_cell_exact_perturbation", "perturbation": "erlotinib"},
                "row_match": {"n_rows": 1},
                "scores": {"requested_functions": {}},
                "rankings": {"top_activated": [{"label": "MP5 Stress"}], "top_suppressed": [{"label": "HALLMARK_CHOLESTEROL_HOMEOSTASIS"}]},
                "diagnostics": {},
            }
        ],
        "skipped_routes": [],
        "errors": [],
        "warnings": [],
    }
    route_plan = {
        "schema_version": "l2-route-plan/v2",
        "route_status": "routed",
        "combination_route": {"selected_routes": [{"tier": "exact_cell_exact_perturbation"}, {"tier": "exact_cell_proxy_perturbation"}]},
    }

    dossier = assemble_evidence(
        execution,
        intent={"query_type": "forward", "bio_context": "A375", "pert_desc": "erlotinib"},
        route_plan=route_plan,
        llm_provider=provider,
        synthesize=True,
    )
    synthesis = dossier["evidence_layer"]["llm_synthesis"]

    assert provider.stages == ["l4_forward_biological_answer", "l4_biological_answer_repair", "l4_execution_quality"]
    assert synthesis["summary"].startswith("Erlotinib in A375 cells")
    assert synthesis["biological_summary"] == synthesis["summary"]
    assert synthesis["evidence_audit_summary"].startswith("Exact primary matrix evidence")
    assert synthesis["diagnostics"]["biological_quality_flags"] == []


def test_l4_route_unresolved_is_not_answered():
    execution = {
        "schema_version": "l3-matrix-execution/v1",
        "query_id": "q2",
        "query_type": "reverse",
        "execution_status": "route_plan_unresolved",
        "source_route_schema": "l2-route-plan/v2",
        "executed_routes": [],
        "skipped_routes": [],
        "errors": [{"code": "route_plan_unresolved", "message": "route_status=llm-required"}],
        "warnings": [],
    }
    route_plan = {
        "schema_version": "l2-route-plan/v2",
        "query_id": "q2",
        "route_status": "llm-required",
        "unresolved_dimensions": ["cell"],
    }

    dossier = assemble_evidence(execution, intent={"query_type": "reverse"}, route_plan=route_plan)

    assert dossier["dossier_status"] == "unresolved_route"
    assert dossier["claim_basis"]["claim_type"] == "no_matrix_evidence"
    assert dossier["uncertainty_layer"]["failure_mode"]["status"] == "unresolved_route"
    assert "the query was fully answered" in dossier["claim_basis"]["must_not_claim"]


def test_l4_executes_after_real_forward_l3_route_plan():
    standard_resources = _require_standard_resources()
    l3_light_resources = _require_l3_light_resources()
    pxf = PxFQuery()
    pxf.resources.use(standard_resources, strict=False)
    qdata = _qdata_with_intent(
        pxf,
        _intent(
            raw_query="What functions change after erlotinib in A375?",
            normalized_query="What functions change after erlotinib in A375?",
            query_type="forward",
            bio_context="A375",
            pert_desc="erlotinib",
            pert_class="drug",
            function_desc="apoptosis",
        ),
    )

    pxf.pp.route(qdata)
    pxf.tl.execute(qdata, resource_dir=l3_light_resources, auto_download=False, top_n=5)
    pxf.tl.assemble(qdata)
    dossier = pxf.get.evidence(qdata)

    assert dossier["schema_version"] == "l4-evidence-dossier/v1"
    assert dossier["dossier_status"] == "evidence_found"
    assert dossier["evidence_layer"]["evidence_grade"] == "exact_primary_with_proxy_support"
    assert dossier["claim_basis"]["claim_strength"] == "moderate"
    assert dossier["evidence_layer"]["matrix_evidence"]["primary_result"]["requested_function_scores"]
    assert dossier["evidence_layer"]["literature_evidence"]["status"] == "disabled"
    assert dossier["evidence_layer"]["llm_synthesis"]["status"] == "disabled"


def test_l4_executes_after_real_reverse_l3_route_plan():
    standard_resources = _require_standard_resources()
    l3_light_resources = _require_l3_light_resources()
    pxf = PxFQuery()
    pxf.resources.use(standard_resources, strict=False)
    qdata = _qdata_with_intent(
        pxf,
        _intent(
            raw_query="Which drugs activate apoptosis in A375?",
            normalized_query="Which drugs activate apoptosis in A375?",
            query_type="reverse",
            bio_context="A375",
            pert_class="drug",
            function_desc="apoptosis",
        ),
    )

    pxf.pp.route(qdata)
    pxf.tl.execute(qdata, resource_dir=l3_light_resources, auto_download=False, top_n=5)
    pxf.tl.assemble(qdata)
    dossier = pxf.get.evidence(qdata)
    primary = dossier["evidence_layer"]["matrix_evidence"]["primary_result"]

    assert dossier["dossier_status"] == "evidence_found"
    assert dossier["claim_basis"]["claim_type"] == "ranked_candidate"
    assert primary["ranking_method"] == "signed_dot_projection"
    assert primary["top_perturbations"]
