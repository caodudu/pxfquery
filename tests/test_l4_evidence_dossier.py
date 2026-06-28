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
