from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from pxfquery.assets import AssetRegistry
from pxfquery.layers import build_layered_answer
from pxfquery.llm import ProviderCheckResult, get_llm_provider, list_llm_providers, provider_check, register_llm_provider
from pxfquery.parser import parse_query
from pxfquery.query import load_corpus, query as run_query, run_corpus, summarize_records
from pxfquery.resolver import classify_route, resolve_intent


@dataclass
class PxFQueryData:
    """Mutable query work object, similar in spirit to AnnData for a query."""

    text: str
    obs: dict = field(default_factory=dict)
    uns: dict = field(default_factory=dict)


class SettingsNamespace:
    def __init__(self, client) -> None:
        self._client = client

    @property
    def provider(self) -> str | None:
        return self._client.provider

    @property
    def provider_mode(self) -> str:
        return self._client.provider_mode

    def register_llm(
        self,
        name: str,
        *,
        base_url: str,
        api_key: str | None = None,
        api_key_env: str = "LLM_GATEWAY_API_KEY",
        model: str | None = None,
        mode: str = "real",
    ) -> None:
        register_llm_provider(
            name,
            base_url=base_url,
            api_key=api_key,
            api_key_env=api_key_env,
            model=model,
        )
        self._client.provider = name
        self._client.provider_mode = mode

    def provider_check(
        self,
        *,
        provider: str | None = None,
        prompt: str = "Return JSON with key ms7_provider_check and value ok.",
        mode: str | None = None,
        timeout: float = 20.0,
    ) -> ProviderCheckResult:
        selected = provider or self._client.provider
        if selected is None:
            raise ValueError("register an LLM provider before provider_check")
        return provider_check(
            provider=selected,
            prompt=prompt,
            mode=mode or self._client.provider_mode,
            timeout=timeout,
        )

    def get_llm_provider(self, name: str):
        return get_llm_provider(name)

    def list_llm_providers(self) -> list[str]:
        return list_llm_providers()

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

    def corpus(self, path: str | Path) -> list[dict]:
        return load_corpus(path)


class PreprocessingNamespace:
    def __init__(self, client) -> None:
        self._client = client

    def parse(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns)) if copy else qdata
        intent = parse_query(
            target.text,
            ai_route_used=self._client.provider_mode == "real",
            fallback_used=self._client.provider_mode != "real",
        )
        target.uns["intent"] = intent.to_dict()
        target.uns["_intent_obj"] = intent
        target.uns["provider"] = {
            "name": self._client.provider,
            "mode": self._client.provider_mode,
            "registered_before_parse": self._client.provider is not None,
        }
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
        route_type = classify_route(intent, provider_mode=self._client.provider_mode)
        target.uns["route_type"] = route_type.value
        return target if copy else None

    def resolve(self, qdata: PxFQueryData, *, copy: bool = False) -> PxFQueryData | None:
        target = PxFQueryData(text=qdata.text, obs=dict(qdata.obs), uns=dict(qdata.uns)) if copy else qdata
        intent = target.uns.get("_intent_obj")
        if intent is None:
            self._client.pp.parse(target)
            intent = target.uns["_intent_obj"]
        result = resolve_intent(intent, provider_mode=self._client.provider_mode)
        if self._client.provider is not None:
            result["provider"]["name"] = self._client.provider
            result["provider"]["registered_before_query"] = True
        if self._client.assets is not None:
            if isinstance(result.get("function_response"), dict):
                result["function_response"]["matrix_source"] = "registered_assets"
            result["assets"] = self._client.assets.to_dict()
            result["asset_registry"] = {
                "registered_before_query": True,
                "keys": self._client.assets.keys(),
            }
        target.uns["result"] = result
        target.uns["answer"] = build_layered_answer(target.text, result, resources_status=self._client.resources.status().to_dict())
        target.uns["route_type"] = result["route_type"]
        return target if copy else None

    def run_corpus(self, corpus_path: str | Path, *, families: Iterable[str] | None = None) -> list[dict]:
        return run_corpus(corpus_path, families=families, provider_mode=self._client.provider_mode)


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

    def summary(self, records: list[dict]) -> dict:
        return summarize_records(records)


def one_shot_query(client, text: str) -> dict:
    qdata = client.read.query(text)
    client.pp.parse(qdata)
    client.tl.resolve(qdata)
    return client.get.result(qdata)


def one_shot_parse(client, text: str) -> dict:
    qdata = client.read.query(text)
    client.pp.parse(qdata)
    return client.get.intent(qdata)
