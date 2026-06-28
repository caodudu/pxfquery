from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pxfquery.l3_execution import execute_route_plan
from pxfquery.l4_evidence import assemble_evidence
from pxfquery.l1_intent import parse_intent
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
        intent = parse_intent(target.text, provider=self._client.llm_providers.get())
        target.uns["intent"] = intent.to_dict()
        target.uns["_intent"] = intent
        return target if copy else None

    def route(self, qdata: PxFQueryData, *, copy: bool = False, auto_download: bool = True) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        intent = _require_intent(target)
        if auto_download:
            self._client.resources.ensure("l2_core_indexes", auto_download=True)
            self._client.resources.ensure("l2_proxy_neighbors", auto_download=True)
            if self._client.resources.manifest():
                self._client.resources.ensure("l3_functional_scores", kinds=("obs",), auto_download=True)
        route_plan = route_intent(
            intent,
            assets=self._client.assets,
            index_dir=self._client._index_dir,
            llm_provider=self._client.llm_providers.get(),
        )
        target.uns["route_plan"] = route_plan.to_dict()
        target.uns["_route_plan"] = route_plan
        target.uns["route_status"] = route_plan.route_status
        return target if copy else None


class ToolsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def execute(
        self,
        qdata: PxFQueryData,
        *,
        copy: bool = False,
        resource_dir: str | None = None,
        auto_download: bool = True,
        top_n: int = 20,
    ) -> PxFQueryData | None:
        target = _copy_qdata(qdata) if copy else qdata
        route_plan = _require_route_plan(target)
        execution = execute_route_plan(
            route_plan,
            resources=self._client.resources,
            resource_dir=resource_dir,
            auto_download=auto_download,
            top_n=top_n,
        )
        target.uns["execution"] = execution.to_dict()
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

    def execution(self, qdata: PxFQueryData) -> dict[str, Any]:
        return qdata.uns["execution"]

    def answer(self, qdata: PxFQueryData, *, resources_status: dict[str, Any] | None = None):
        return build_answer(qdata.text, qdata.uns["result"], resources_status=resources_status)


def run_scanpy_style_pipeline(client, text: str) -> PxFQueryData:
    qdata = client.read.query(text)
    client.pp.parse(qdata)
    client.pp.route(qdata)
    client.tl.execute(qdata)
    return qdata


def _copy_qdata(qdata: PxFQueryData) -> PxFQueryData:
    return PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns))


def _require_intent(qdata: PxFQueryData):
    if "_intent" not in qdata.uns:
        raise RuntimeError("qdata has no l1_intent result; call pxf.pp.parse(qdata) before downstream tools")
    return qdata.uns["_intent"]


def _require_route_plan(qdata: PxFQueryData):
    if "_route_plan" not in qdata.uns:
        raise RuntimeError("qdata has no l2 routing result; call pxf.pp.route(qdata) before downstream tools")
    return qdata.uns["_route_plan"]


def _require_execution(qdata: PxFQueryData):
    if "_execution" not in qdata.uns:
        raise RuntimeError("qdata has no execution result; call pxf.tl.execute(qdata) before assembly")
    return qdata.uns["_execution"]
