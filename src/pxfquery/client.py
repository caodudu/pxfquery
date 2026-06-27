from __future__ import annotations

from pathlib import Path
from typing import Iterable

from pxfquery._version import __version__
from pxfquery.llm import ProviderCheckResult, get_llm_provider, list_llm_providers, register_llm_provider, provider_check
from pxfquery.query import load_corpus, run_corpus, summarize_records
from pxfquery.workflow import (
    GetNamespace,
    PreprocessingNamespace,
    ReadNamespace,
    SettingsNamespace,
    ToolsNamespace,
    one_shot_parse,
    one_shot_query,
)


class PxFQuery:
    """Main user-facing PxFquery client with scverse-style namespaces."""

    def __init__(self, *, provider: str | None = None, provider_mode: str = "disabled") -> None:
        self.provider = provider
        self.provider_mode = provider_mode
        self.settings = SettingsNamespace(self)
        self.read = ReadNamespace(self)
        self.pp = PreprocessingNamespace(self)
        self.tl = ToolsNamespace(self)
        self.get = GetNamespace(self)

    @property
    def version(self) -> str:
        return __version__

    def register_llm_provider(
        self,
        name: str,
        *,
        base_url: str,
        api_key: str | None = None,
        api_key_env: str = "LLM_GATEWAY_API_KEY",
        model: str | None = None,
        mode: str = "real",
    ) -> None:
        self.settings.register_llm(
            name,
            base_url=base_url,
            api_key=api_key,
            api_key_env=api_key_env,
            model=model,
            mode=mode,
        )

    def parse(self, text: str) -> dict:
        return one_shot_parse(self, text)

    def query(self, text: str) -> dict:
        return one_shot_query(self, text)

    def run_corpus(self, corpus_path: str | Path, *, families: Iterable[str] | None = None) -> list[dict]:
        return self.tl.run_corpus(corpus_path, families=families)

    def summarize_records(self, records: list[dict]) -> dict:
        return summarize_records(records)

    def load_corpus(self, path: str | Path) -> list[dict]:
        return load_corpus(path)

    def provider_check(
        self,
        *,
        provider: str | None = None,
        prompt: str = "Return JSON with key ms7_provider_check and value ok.",
        mode: str = "real",
        timeout: float = 20.0,
    ) -> ProviderCheckResult:
        selected = provider or self.provider
        if selected is None:
            raise ValueError("provider is required; pass provider=... or call register_llm_provider(...) first")
        return self.settings.provider_check(provider=selected, prompt=prompt, mode=mode, timeout=timeout)

    def get_llm_provider(self, name: str):
        return get_llm_provider(name)

    def list_llm_providers(self) -> list[str]:
        return list_llm_providers()
