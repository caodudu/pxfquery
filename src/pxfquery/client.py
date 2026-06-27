from __future__ import annotations

from pathlib import Path
from typing import Iterable

from pxfquery.llm import ProviderCheckResult, register_llm_provider, provider_check
from pxfquery.query import load_corpus, parse, query, run_corpus, summarize_records


class PxFQuery:
    """Main user-facing PxFquery client.

    The module-level functions remain available for lightweight scripts, but
    application code should generally instantiate this class so provider
    configuration and default runtime behavior are explicit.
    """

    def __init__(self, *, provider: str | None = None, provider_mode: str = "disabled") -> None:
        self.provider = provider
        self.provider_mode = provider_mode

    def register_llm_provider(
        self,
        name: str,
        *,
        base_url: str,
        api_key: str | None = None,
        api_key_env: str = "LLM_GATEWAY_API_KEY",
        model: str | None = None,
    ) -> None:
        register_llm_provider(
            name,
            base_url=base_url,
            api_key=api_key,
            api_key_env=api_key_env,
            model=model,
        )
        if self.provider is None:
            self.provider = name

    def parse(self, text: str) -> dict:
        return parse(text, provider_mode=self.provider_mode)

    def query(self, text: str) -> dict:
        return query(text, provider_mode=self.provider_mode)

    def run_corpus(self, corpus_path: str | Path, *, families: Iterable[str] | None = None) -> list[dict]:
        return run_corpus(corpus_path, families=families, provider_mode=self.provider_mode)

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
        return provider_check(provider=selected, prompt=prompt, mode=mode, timeout=timeout)
