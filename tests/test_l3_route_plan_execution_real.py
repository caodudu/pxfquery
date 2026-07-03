import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent
from pxfquery.l3_execution.executor import execute_route_plan, _aggregate_reverse_replicates, _execute_forward_route, _filter_reverse_control_perturbations, _rank_records, _reverse_rankings
from pxfquery.l3_execution.matrix_store import FunctionalMatrix


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


def test_l3_reverse_genetic_skips_unreadable_brdn_reagents_before_ranking():
    X = np.array([[9.0], [5.0], [4.0]], dtype=np.float32)
    obs = pd.DataFrame(
        [
            {"sig_id": "s1", "pert_id": "BRDN0000733847", "cmap_name": None, "cell_iname": "A549"},
            {"sig_id": "s2", "pert_id": "BRDN0001148015", "cmap_name": "AURKA", "cell_iname": "A549"},
            {"sig_id": "s3", "pert_id": "HAHN-000205", "cmap_name": "PSMA1", "cell_iname": "A549"},
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

    assert [item["label"] for item in rankings["top_perturbations"]] == ["AURKA", "PSMA1"]
    assert all(not str(item["label"]).startswith("BRDN") for item in rankings["top_perturbations"])


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


class _FakeStore:
    def __init__(self, matrix: FunctionalMatrix) -> None:
        self.matrix = matrix

    def load(self, modality: str) -> FunctionalMatrix:
        assert modality == self.matrix.modality
        return self.matrix


class _FakeResources:
    def __init__(self, matrix: FunctionalMatrix) -> None:
        self._functional_matrix_cache = {matrix.modality: matrix}

    def status(self):
        class _Status:
            def to_dict(self):
                return {}

        return _Status()

    def ensure(self, *args, **kwargs):
        class _Status:
            available = True
            missing_files: list[str] = []

        return _Status()


def _calibration_matrix(modality: str = "sh") -> FunctionalMatrix:
    obs = pd.DataFrame(
        [
            {"sig_id": "q", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "QUERY"},
            {"sig_id": "t1", "pert_id": "TARGET", "cmap_name": "TARGET", "cell_iname": "C1"},
            {"sig_id": "p1", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "C1"},
            {"sig_id": "t2", "pert_id": "TARGET", "cmap_name": "TARGET", "cell_iname": "C2"},
            {"sig_id": "p2", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "C2"},
            {"sig_id": "t3", "pert_id": "TARGET", "cmap_name": "TARGET", "cell_iname": "C3"},
            {"sig_id": "p3", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "C3"},
        ]
    )
    X = np.array(
        [
            [2.0, -1.0],
            [1.0, -1.0],
            [-1.0, 1.0],
            [2.0, -2.0],
            [-2.0, 2.0],
            [3.0, -3.0],
            [-3.0, 3.0],
        ],
        dtype=np.float32,
    )
    return FunctionalMatrix(
        modality=modality,
        X=X,
        obs=obs,
        var_names=["F_POS", "F_NEG"],
        matrix_path="synthetic",
        matrix_cache_path=None,
        obs_path="synthetic",
        var_path="synthetic",
    )


def _weak_negative_calibration_matrix(modality: str = "sh") -> FunctionalMatrix:
    obs = pd.DataFrame(
        [
            {"sig_id": "q", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "QUERY"},
            {"sig_id": "t1", "pert_id": "TARGET", "cmap_name": "TARGET", "cell_iname": "C1"},
            {"sig_id": "p1", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "C1"},
            {"sig_id": "t2", "pert_id": "TARGET", "cmap_name": "TARGET", "cell_iname": "C2"},
            {"sig_id": "p2", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "C2"},
            {"sig_id": "t3", "pert_id": "TARGET", "cmap_name": "TARGET", "cell_iname": "C3"},
            {"sig_id": "p3", "pert_id": "PROXY", "cmap_name": "PROXY", "cell_iname": "C3"},
        ]
    )
    X = np.array(
        [
            [2.0, -1.0, 0.5],
            [1.0, 0.0, 0.0],
            [-0.12, 0.99, 0.0],
            [0.0, 1.0, 0.0],
            [0.99, -0.12, 0.0],
            [1.0, 1.0, 0.0],
            [-1.0, 1.0, 0.0],
        ],
        dtype=np.float32,
    )
    return FunctionalMatrix(
        modality=modality,
        X=X,
        obs=obs,
        var_names=["F_POS", "F_NEG", "F_LOW"],
        matrix_path="synthetic",
        matrix_cache_path=None,
        obs_path="synthetic",
        var_path="synthetic",
    )


def test_l3_forward_genetic_proxy_direction_calibration_flips_negative_shared_cell_profile():
    matrix = _calibration_matrix("sh")
    route = {
        "route_id": "forward_001",
        "cell": "QUERY",
        "perturbation": "PROXY",
        "perturbation_match_type": "semantic_neighbor",
        "perturbation_match_distance": 0.5,
        "modality": "sh",
    }
    route_plan = {"intent": {"query_type": "forward", "pert_desc": "TARGET"}}

    result = _execute_forward_route(route, route_plan, _FakeStore(matrix), top_n=2, modality="sh")

    calibration = result.scores["proxy_direction_calibration"]
    assert calibration["status"] == "flipped"
    assert calibration["score_multiplier"] == -1
    assert calibration["score_weight"] == 1.0
    assert calibration["n_common_cells"] == 3
    assert result.scores["score_multiplier"] == -1
    assert result.scores["score_weight"] == 1.0
    assert result.scores["effective_score_multiplier"] == -1.0
    assert result.rankings["top_activated"][0]["label"] == "F_NEG"
    assert result.rankings["top_suppressed"][0]["label"] == "F_POS"


def test_l3_forward_genetic_proxy_direction_calibration_flips_at_moderate_negative_threshold():
    matrix = _weak_negative_calibration_matrix("sh")
    route = {
        "route_id": "forward_001",
        "cell": "QUERY",
        "perturbation": "PROXY",
        "perturbation_match_type": "semantic_neighbor",
        "perturbation_match_distance": 0.5,
        "modality": "sh",
    }
    route_plan = {"intent": {"query_type": "forward", "pert_desc": "TARGET"}}

    result = _execute_forward_route(route, route_plan, _FakeStore(matrix), top_n=2, modality="sh")

    calibration = result.scores["proxy_direction_calibration"]
    assert calibration["status"] == "flipped"
    assert calibration["score_multiplier"] == -1
    assert calibration["negative_cells"] > calibration["positive_cells"]
    assert calibration["median_correlation"] <= -0.10
    assert result.rankings["top_activated"][0]["label"] == "F_NEG"


def test_l3_forward_genetic_proxy_direction_calibration_excludes_below_threshold_proxy():
    matrix = _weak_negative_calibration_matrix("sh")
    route = {
        "route_id": "forward_001",
        "cell": "QUERY",
        "perturbation": "PROXY",
        "perturbation_match_type": "semantic_neighbor",
        "perturbation_match_distance": 0.5,
        "modality": "sh",
    }
    route_plan = {"intent": {"query_type": "forward", "pert_desc": "TARGET"}}

    result = _execute_forward_route(
        route,
        route_plan,
        _FakeStore(matrix),
        top_n=2,
        modality="sh",
        calibration_config={"direction_threshold": 0.95},
    )

    calibration = result.scores["proxy_direction_calibration"]
    assert calibration["status"] == "excluded"
    assert calibration["reason"] == "below_direction_threshold"
    assert calibration["score_multiplier"] == 1
    assert calibration["score_weight"] == 0.0
    assert result.scores["score_multiplier"] == 1
    assert result.scores["score_weight"] == 0.0
    assert result.scores["effective_score_multiplier"] == 0.0
    np.testing.assert_allclose(result.scores["aggregate"]["F_POS"], 0.0)


def test_l3_forward_drug_proxy_direction_calibration_is_disabled_by_default():
    matrix = _calibration_matrix("cp")
    route = {
        "route_id": "forward_001",
        "cell": "QUERY",
        "perturbation": "PROXY",
        "perturbation_match_type": "structural_neighbor",
        "perturbation_match_distance": 0.5,
        "modality": "cp",
    }
    route_plan = {"intent": {"query_type": "forward", "pert_desc": "TARGET"}}

    result = _execute_forward_route(route, route_plan, _FakeStore(matrix), top_n=2, modality="cp")

    calibration = result.scores["proxy_direction_calibration"]
    assert calibration["status"] == "disabled"
    assert calibration["score_multiplier"] == 1
    assert calibration["score_weight"] == 1.0
    assert result.scores["effective_score_multiplier"] == 1.0
    assert result.rankings["top_activated"][0]["label"] == "F_POS"


def test_l3_forward_drug_proxy_direction_calibration_can_be_enabled():
    matrix = _calibration_matrix("cp")
    route = {
        "route_id": "forward_001",
        "cell": "QUERY",
        "perturbation": "PROXY",
        "perturbation_match_type": "structural_neighbor",
        "perturbation_match_distance": 0.5,
        "modality": "cp",
    }
    route_plan = {"intent": {"query_type": "forward", "pert_desc": "TARGET"}}

    result = _execute_forward_route(
        route,
        route_plan,
        _FakeStore(matrix),
        top_n=2,
        modality="cp",
        calibration_config={"drug": True},
    )

    calibration = result.scores["proxy_direction_calibration"]
    assert calibration["status"] == "flipped"
    assert result.scores["score_multiplier"] == -1
    assert result.scores["score_weight"] == 1.0
    assert result.rankings["top_activated"][0]["label"] == "F_NEG"


def test_proxy_direction_calibration_does_not_run_for_reverse_routes():
    matrix = _calibration_matrix("sh")
    route_plan = {
        "schema_version": "l2-route-plan/v2",
        "query_id": "reverse_calibration_guard",
        "route_status": "routed",
        "intent": {"query_type": "reverse"},
        "combination_route": {
            "selected_routes": [
                {
                    "route_id": "reverse_001",
                    "cell": "QUERY",
                    "modality": "sh",
                    "functions": [{"var_name": "F_POS", "direction": "activate", "weight": 1.0}],
                }
            ]
        },
    }

    result = execute_route_plan(
        route_plan,
        resources=_FakeResources(matrix),
        auto_download=False,
        top_n=2,
        forward_proxy_direction_calibration={"enabled": True, "genetic": True, "drug": True},
    )

    assert result.execution_status == "executed"
    route = result.executed_routes[0]
    assert "proxy_direction_calibration" not in route["scores"]
    assert "proxy_direction_calibration" not in route["route_metadata"]


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
