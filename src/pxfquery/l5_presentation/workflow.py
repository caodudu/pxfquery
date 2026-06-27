from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pxfquery.l4_evidence import assemble_evidence
from pxfquery.l3_execution import execute_route
from pxfquery.l1_nlu import parse_query
from pxfquery.l5_presentation.answer import build_answer
from pxfquery.l2_routing import route_intent


@dataclass
class PxFQueryData:
    """Mutable query object used by the scanpy-style user interface."""

    text: str
    obs: dict[str, Any] = field(default_factory=dict)
    uns: dict[str, Any] = field(default_factory=dict)


class ReadNamespace:
    def query(self, text: str) -> PxFQueryData:
        return PxFQueryData(text=text.strip())


class PreprocessingNamespace:
    def parse(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        intent = parse_query(target.text)
        target.uns["intent"] = intent.to_dict()
        target.uns["_intent"] = intent
        return target if copy else None


class ToolsNamespace:
    def route(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        intent = _require_intent(target)
        route_plan = route_intent(intent)
        target.uns["route_plan"] = route_plan.to_dict()
        target.uns["_route_plan"] = route_plan
        target.uns["route_status"] = route_plan.route_status
        return target if copy else None

    def execute(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        route_plan = _require_route_plan(target)
        execution = execute_route(route_plan)
        target.uns["execution"] = {
            "query_status": execution.query_status,
            "result": execution.result,
            "execution_note": execution.execution_note,
        }
        target.uns["_execution"] = execution
        return target if copy else None

    def assemble(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        execution = _require_execution(target)
        target.uns["result"] = assemble_evidence(execution)
        return target if copy else None


class GetNamespace:
    def intent(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["intent"]

    def route(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["route_plan"]

    def result(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["result"]

    def answer(self, qdata: PxFQueryData, *, resources_status: dict[str, Any] | None = None):
        return build_answer(qdata.text, qdata.uns["result"], resources_status=resources_status)


def run_scanpy_style_pipeline(client, text: str) -> PxFQueryData:
    qdata = client.read.query(text)
    client.pp.parse(qdata)
    client.tl.route(qdata)
    client.tl.execute(qdata)
    client.tl.assemble(qdata)
    return qdata


def _copy_qdata(qdata: PxFQueryData) -> PxFQueryData:
    return PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns))


def _require_intent(qdata: PxFQueryData):
    if "_intent" not in qdata.uns:
        intent = parse_query(qdata.text)
        qdata.uns["intent"] = intent.to_dict()
        qdata.uns["_intent"] = intent
    return qdata.uns["_intent"]


def _require_route_plan(qdata: PxFQueryData):
    if "_route_plan" not in qdata.uns:
        intent = _require_intent(qdata)
        route_plan = route_intent(intent)
        qdata.uns["route_plan"] = route_plan.to_dict()
        qdata.uns["_route_plan"] = route_plan
        qdata.uns["route_status"] = route_plan.route_status
    return qdata.uns["_route_plan"]


def _require_execution(qdata: PxFQueryData):
    if "_execution" not in qdata.uns:
        route_plan = _require_route_plan(qdata)
        execution = execute_route(route_plan)
        qdata.uns["execution"] = {
            "query_status": execution.query_status,
            "result": execution.result,
            "execution_note": execution.execution_note,
        }
        qdata.uns["_execution"] = execution
    return qdata.uns["_execution"]
