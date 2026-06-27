from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pxfquery.l4_evidence import assemble_evidence
from pxfquery.l1_nlu import parse_query
from pxfquery.l2_routing import route_intent
from pxfquery.l5_presentation.answer import build_answer


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
    def __init__(self, client) -> None:
        self._client = client

    def parse(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        intent = parse_query(target.text, backend=self._client.nlu_backend)
        target.uns["intent"] = intent.to_dict()
        target.uns["_intent"] = intent
        return target if copy else None


class ToolsNamespace:
    def __init__(self, client) -> None:
        self._client = client

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
        if self._client._resolver is None:
            raise RuntimeError("Resolver is not enabled. Call pxf.enable_resolver(index_dir=...) before pxf.tl.execute(qdata).")
        execution = self._client._resolver.execute_intent(
            route_plan.intent.to_resolver_intent(),
            user_input=target.text,
            top_n=route_plan.intent.top_n,
            summarize=False,
        )
        target.uns["execution"] = {
            "query_status": "found" if getattr(execution, "found", False) else "not-found",
            "result": execution,
            "resolver_meta": getattr(execution, "resolver_meta", {}),
        }
        target.uns["_execution"] = execution
        return target if copy else None

    def assemble(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        execution = _require_execution(target)
        result = assemble_evidence(execution)
        result["intent"] = target.uns["intent"]
        result["route_plan"] = target.uns["route_plan"]
        target.uns["result"] = result
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
        raise RuntimeError("qdata has no L1 intent; call pxf.pp.parse(qdata) before downstream tools")
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
        raise RuntimeError("qdata has no execution result; call pxf.tl.execute(qdata) before assembly")
    return qdata.uns["_execution"]
