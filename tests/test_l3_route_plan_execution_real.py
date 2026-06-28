import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent
from pxfquery.l3_execution.executor import _aggregate_reverse_replicates, _filter_reverse_control_perturbations, _rank_records, _reverse_rankings


DEFAULT_STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)

STANDARD_RESOURCES = Path(os.environ.get("PXFQUERY_TEST_STANDARD_RESOURCES", DEFAULT_STANDARD_RESOURCES))
L3_LIGHT_RESOURCES_ENV = os.environ.get("PXFQUERY_TEST_L3_LIGHT_RESOURCES")


def _require_standard_resources() -> Path:
    if not STANDARD_RESOURCES.exists():
        pytest.skip("set PXFQUERY_TEST_STANDARD_RESOURCES to run resource-backed L2 tests")
    return STANDARD_RESOURCES


def _require_l3_light_resources() -> Path:
    if not L3_LIGHT_RESOURCES_ENV:
        pytest.skip("set PXFQUERY_TEST_L3_LIGHT_RESOURCES to run real L3 matrix execution tests")
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


def test_l3_rank_records_keep_human_label_and_machine_function_field():
    records = _rank_records(
        ["HALLMARK_APOPTOSIS", "HALLMARK_MYC_TARGETS_V1"],
        scores=[1.25, -0.75],
        order=[0, 1],
        top_n=2,
        positive=True,
    )

    assert records == [
        {
            "rank": 1,
            "label": "HALLMARK_APOPTOSIS",
            "function": "HALLMARK_APOPTOSIS",
            "score": 1.25,
            "direction": "activated",
        }
    ]


def test_l3_reverse_genetic_bidirectional_projection_keeps_perturbation_anchors():
    X = np.array([[2.0], [-3.0]], dtype=np.float32)
    obs = pd.DataFrame(
        [
            {"sig_id": "s1", "pert_id": "GENE_A", "cmap_name": "GENE_A", "cell_iname": "A375"},
            {"sig_id": "s2", "pert_id": "GENE_B", "cmap_name": "GENE_B", "cell_iname": "A375"},
        ]
    )
    rankings = _reverse_rankings(
        ["HALLMARK_APOPTOSIS"],
        X,
        obs,
        np.array([1.0], dtype=np.float32),
        np.asarray(X @ np.array([1.0], dtype=np.float32), dtype=np.float32),
        modality="xpr",
        ranking_mode="bidirectional",
        top_n=1,
    )

    lof = rankings["top_loss_of_function_perturbations"][0]
    activation = rankings["top_activating_perturbations_inferred"][0]
    assert lof["label"] == "GENE_A"
    assert lof["recommended_operation"] == "inhibit_or_knockout_gene"
    assert lof["score"] == 2.0
    assert activation["label"] == "GENE_B"
    assert activation["recommended_operation"] == "activate_or_increase_gene"
    assert activation["score"] == 3.0
    assert activation["raw_projection"] == -3.0


def test_l3_reverse_projection_records_filter_wrong_sign_hits():
    X = np.array([[2.0], [-3.0]], dtype=np.float32)
    obs = pd.DataFrame(
        [
            {"sig_id": "s1", "pert_id": "GENE_A", "cmap_name": "GENE_A", "cell_iname": "A375"},
            {"sig_id": "s2", "pert_id": "GENE_B", "cmap_name": "GENE_B", "cell_iname": "A375"},
        ]
    )
    rankings = _reverse_rankings(
        ["HALLMARK_APOPTOSIS"],
        X,
        obs,
        np.array([1.0], dtype=np.float32),
        np.asarray(X @ np.array([1.0], dtype=np.float32), dtype=np.float32),
        modality="xpr",
        ranking_mode="perturbation_only",
        top_n=2,
    )

    lof = rankings["top_loss_of_function_perturbations"]
    assert [item["label"] for item in lof] == ["GENE_A"]
    assert all(item["raw_projection"] > 0 for item in lof)


def test_l3_reverse_filters_css001_control_sequences_before_ranking():
    X = np.array([[30.0], [5.0], [4.0]], dtype=np.float32)
    obs = pd.DataFrame(
        [
            {"sig_id": "ctrl", "pert_id": "CSS001_CONTROL", "cmap_name": "CSS001", "cell_iname": "MCF7"},
            {"sig_id": "s1", "pert_id": "GENE_A", "cmap_name": "GENE_A", "cell_iname": "MCF7"},
            {"sig_id": "s2", "pert_id": "GENE_B", "cmap_name": "GENE_B", "cell_iname": "MCF7"},
        ]
    )

    filtered_X, filtered_obs, diagnostics = _filter_reverse_control_perturbations(X, obs, modality="sh")
    rankings = _reverse_rankings(
        ["HALLMARK_MYC_TARGETS_V1"],
        filtered_X,
        filtered_obs,
        np.array([1.0], dtype=np.float32),
        np.asarray(filtered_X @ np.array([1.0], dtype=np.float32), dtype=np.float32),
        modality="sh",
        ranking_mode="perturbation_only",
        top_n=10,
    )

    assert diagnostics["filtered_groups"] == 1
    assert all(not str(item["pert_id"]).startswith("CSS001") for item in rankings["top_perturbations"])
    assert [item["label"] for item in rankings["top_perturbations"]] == ["GENE_A", "GENE_B"]


def test_l3_reverse_aggregates_signature_replicates_by_perturbation_and_cell():
    X = np.array([[2.0, 0.0], [4.0, 2.0], [-3.0, 1.0]], dtype=np.float32)
    obs = pd.DataFrame(
        [
            {"sig_id": "s1", "pert_id": "P1", "cmap_name": "GENE_A", "cell_iname": "A375"},
            {"sig_id": "s2", "pert_id": "P1", "cmap_name": "GENE_A", "cell_iname": "A375"},
            {"sig_id": "s3", "pert_id": "P2", "cmap_name": "GENE_B", "cell_iname": "A375"},
        ]
    )

    agg_X, agg_obs = _aggregate_reverse_replicates(X, obs)

    assert agg_X.shape == (2, 2)
    assert agg_obs.loc[0, "cmap_name"] == "GENE_A"
    assert agg_obs.loc[0, "n_signatures"] == 2
    assert agg_obs.loc[0, "sig_ids"] == ["s1", "s2"]
    np.testing.assert_allclose(agg_X[0], np.array([3.0, 1.0], dtype=np.float32))


def test_l3_executes_real_forward_route_plan_from_t138_l2():
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
    assert qdata.uns["route_plan"]["schema_version"] == "l2-route-plan/v2"
    assert qdata.uns["route_plan"]["route_status"] == "routed"

    pxf.tl.execute(qdata, resource_dir=l3_light_resources, auto_download=False, top_n=5)
    execution = pxf.get.execution(qdata)

    assert execution["schema_version"] == "l3-matrix-execution/v1"
    assert execution["execution_status"] == "executed"
    assert execution["executed_routes"]
    route = execution["executed_routes"][0]
    assert route["query_type"] == "forward"
    assert route["modality"] == "cp"
    assert route["row_match"]["n_rows"] > 0
    assert route["rankings"]["top_activated"]
    assert route["rankings"]["top_suppressed"]
    assert "HALLMARK_APOPTOSIS" in route["scores"]["requested_functions"]


def test_l3_execute_does_not_require_or_call_old_resolver():
    standard_resources = _require_standard_resources()
    l3_light_resources = _require_l3_light_resources()
    pxf = PxFQuery()
    pxf.resources.use(standard_resources, strict=False)

    class ExplodingResolver:
        def execute_intent(self, *args, **kwargs):
            raise AssertionError("old resolver must not be called by L3")

    pxf._resolver = ExplodingResolver()
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
    pxf.tl.execute(qdata, resource_dir=l3_light_resources, auto_download=False, top_n=3)

    assert pxf.get.execution(qdata)["execution_status"] == "executed"


def test_l3_resource_missing_is_structured_failure(tmp_path):
    standard_resources = _require_standard_resources()
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
    pxf.tl.execute(qdata, resource_dir=tmp_path, auto_download=False, top_n=3)
    execution = pxf.get.execution(qdata)

    assert execution["execution_status"] == "resource_missing"
    assert execution["executed_routes"] == []
    assert execution["errors"][0]["code"] == "resource_missing"


def test_l3_executes_real_reverse_route_plan_from_t138_l2():
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
    assert qdata.uns["route_plan"]["schema_version"] == "l2-route-plan/v2"
    assert qdata.uns["route_plan"]["route_status"] == "routed"

    pxf.tl.execute(qdata, resource_dir=l3_light_resources, auto_download=False, top_n=5)
    execution = pxf.get.execution(qdata)

    assert execution["schema_version"] == "l3-matrix-execution/v1"
    assert execution["execution_status"] == "executed"
    assert execution["executed_routes"]
    route = execution["executed_routes"][0]
    assert route["query_type"] == "reverse"
    assert route["modality"] == "cp"
    assert route["row_match"]["n_rows"] > 0
    assert route["scores"]["target_vector"]
    assert route["rankings"]["top_perturbations"]
