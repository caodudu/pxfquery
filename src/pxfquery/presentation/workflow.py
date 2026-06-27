from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from pxfquery.execution.assets import AssetRegistry
from pxfquery.evidence.pipeline import run_query_pipeline
from pxfquery.nlu import parse_query
from pxfquery.presentation import build_answer
from pxfquery.routing import route_intent


@dataclass
class PxFQueryData:
    """Mutable query work object, similar in spirit to AnnData for a query."""

    text: str
    obs: dict = field(default_factory=dict)
    uns: dict = field(default_factory=dict)


class SettingsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def register_assets(
        self,
        *,
        root: str | Path | None = None,
        manifest: str | Path | dict | None = None,
        strict: bool = True,
    ) -> AssetRegistry:
        if (root is None) == (manifest is None):
            raise ValueError("pass exactly one of root=... or manifest=...")
        registry = AssetRegistry.from_manifest(manifest, strict=strict) if manifest is not None else AssetRegistry.from_root(root, strict=strict)
        self._client.assets = registry
        return registry

    def get_asset(self, key: str):
        if self._client.assets is None:
            raise ValueError("register assets before accessing runtime data assets")
        return self._client.assets.get(key)

    def list_assets(self) -> list[str]:
        if self._client.assets is None:
            return []
        return self._client.assets.keys()


class ReadNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def query(self, text: str) -> PxFQueryData:
        return PxFQueryData(text=text.strip())


class PreprocessingNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def parse(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns)) if copy else qdata
        intent = parse_query(target.text)
        target.uns["intent"] = intent.to_dict()
        target.uns["_intent_obj"] = intent
        target.uns["assets"] = {
            "registered_before_parse": self._client.assets is not None,
            "keys": self._client.assets.keys() if self._client.assets is not None else [],
        }
        return target if copy else None


class ToolsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def route(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns)) if copy else qdata
        intent = target.uns.get("_intent_obj")
        if intent is None:
            self._client.pp.parse(target)
            intent = target.uns["_intent_obj"]
        route_plan = route_intent(intent)
        target.uns["route_plan"] = route_plan.to_dict()
        target.uns["_route_plan_obj"] = route_plan
        target.uns["route_status"] = route_plan.route_status
        return target if copy else None

    def resolve(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns)) if copy else qdata
        intent = target.uns.get("_intent_obj")
        if intent is None:
            self._client.pp.parse(target)
            intent = target.uns["_intent_obj"]
        result = run_query_pipeline(target.text)
        if self._client.assets is not None:
            if isinstance(result.get("function_response"), dict):
                result["function_response"]["matrix_source"] = "registered_assets"
            result["assets"] = self._client.assets.to_dict()
            result["asset_registry"] = {
                "registered_before_query": True,
                "keys": self._client.assets.keys(),
            }
        target.uns["result"] = result
        target.uns["answer"] = build_answer(target.text, result, resources_status=self._client.resources.status().to_dict())
        target.uns["route_status"] = result["route_status"]
        return target if copy else None


class GetNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def intent(self, qdata: PxFQueryData) -> dict:
        if "intent" not in qdata.uns:
            self._client.pp.parse(qdata)
        return qdata.uns["intent"]

    def result(self, qdata: PxFQueryData) -> dict:
        if "result" not in qdata.uns:
            self._client.tl.resolve(qdata)
        return qdata.uns["result"]

    def answer(self, qdata: PxFQueryData):
        if "answer" not in qdata.uns:
            self._client.tl.resolve(qdata)
        return qdata.uns["answer"]


def one_shot_query(client, text: str) -> dict:
    qdata = client.read.query(text)
    client.pp.parse(qdata)
    client.tl.resolve(qdata)
    return client.get.result(qdata)


def one_shot_parse(client, text: str) -> dict:
    qdata = client.read.query(text)
    client.pp.parse(qdata)
    return client.get.intent(qdata)
