import os
from pathlib import Path

import pytest

from pxfquery import PxFQuery
from pxfquery.l1_intent import QueryIntent


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
