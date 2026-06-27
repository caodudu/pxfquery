from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass


DEFAULT_PROVIDER = "llm_gateway/deepseek-ai/deepseek-v4-flash"
DEFAULT_BASE_URL = "http://localhost:3000/v1"


@dataclass
class ProviderConfig:
    name: str
    base_url: str
    api_key: str | None = None
    api_key_env: str = "LLM_GATEWAY_API_KEY"
    model: str | None = None


@dataclass
class ProviderCheckResult:
    provider: str
    mode: str
    real_provider_success: bool
    prompt: str
    response: str | None
    error: str | None
    latency_seconds: float
    base_url: str

    def to_dict(self) -> dict:
        return asdict(self)


_PROVIDER_REGISTRY: dict[str, ProviderConfig] = {
    DEFAULT_PROVIDER: ProviderConfig(
        name=DEFAULT_PROVIDER,
        base_url=DEFAULT_BASE_URL,
        api_key_env="LLM_GATEWAY_API_KEY",
        model="deepseek-ai/deepseek-v4-flash",
    )
}


def register_llm_provider(
    name: str,
    *,
    base_url: str,
    api_key: str | None = None,
    api_key_env: str = "LLM_GATEWAY_API_KEY",
    model: str | None = None,
) -> None:
    """Register an OpenAI-compatible LLM provider route for runtime checks."""

    _PROVIDER_REGISTRY[name] = ProviderConfig(
        name=name,
        base_url=base_url.rstrip("/"),
        api_key=api_key,
        api_key_env=api_key_env,
        model=model,
    )


def get_llm_provider(name: str) -> ProviderConfig:
    try:
        return _PROVIDER_REGISTRY[name]
    except KeyError as exc:
        raise KeyError(f"LLM provider is not registered: {name}") from exc


def list_llm_providers() -> list[str]:
    return sorted(_PROVIDER_REGISTRY)


def provider_check(
    *,
    provider: str = DEFAULT_PROVIDER,
    prompt: str = "Return JSON with key pxfquery_provider_check and value ok.",
    mode: str = "real",
    timeout: float = 20.0,
    base_url: str | None = None,
) -> ProviderCheckResult:
    config = _PROVIDER_REGISTRY.get(provider)
    base = (base_url or os.environ.get("LLM_GATEWAY_BASE_URL") or (config.base_url if config else DEFAULT_BASE_URL)).rstrip("/")
    api_key_env = config.api_key_env if config else "LLM_GATEWAY_API_KEY"
    api_key = (config.api_key if config else None) or os.environ.get(api_key_env)
    model = (config.model if config and config.model else provider.replace("llm_gateway/", "", 1))
    started = time.time()
    if mode != "real":
        return ProviderCheckResult(
            provider=provider,
            mode=mode,
            real_provider_success=False,
            prompt=prompt,
            response=None,
            error=f"provider check skipped because mode={mode}",
            latency_seconds=round(time.time() - started, 3),
            base_url=base,
        )

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 80,
    }
    curl_result = _curl_fallback(base, payload, provider, prompt, timeout, started, api_key=api_key)
    if curl_result is not None:
        return curl_result
    request = urllib.request.Request(
        f"{base}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key or 'local-llm-gateway'}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
        return ProviderCheckResult(
            provider=provider,
            mode="real",
            real_provider_success=True,
            prompt=prompt,
            response=raw,
            error=None,
            latency_seconds=round(time.time() - started, 3),
            base_url=base,
        )
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
        body = ""
        if isinstance(exc, urllib.error.HTTPError):
            try:
                body = exc.read().decode("utf-8", errors="replace")
            except Exception:
                body = ""
        return ProviderCheckResult(
            provider=provider,
            mode="real",
            real_provider_success=False,
            prompt=prompt,
            response=None,
            error=f"{type(exc).__name__}: {exc}; body={body[:500]}",
            latency_seconds=round(time.time() - started, 3),
            base_url=base,
        )


def _curl_fallback(
    base: str,
    payload: dict,
    provider: str,
    prompt: str,
    timeout: float,
    started: float,
    api_key: str | None,
) -> ProviderCheckResult | None:
    curl = shutil.which("curl")
    if curl is None or not api_key:
        return None
    proc = subprocess.run(
        [
            curl,
            "-sS",
            "-m",
            str(int(timeout)),
            f"{base}/chat/completions",
            "-H",
            f"Authorization: Bearer {api_key}",
            "-H",
            "Content-Type: application/json",
            "-d",
            json.dumps(payload),
        ],
        text=True,
        capture_output=True,
        timeout=timeout + 5,
    )
    if proc.returncode != 0:
        return None
    try:
        parsed = json.loads(proc.stdout)
    except json.JSONDecodeError:
        parsed = None
    if isinstance(parsed, dict) and "choices" in parsed:
        return ProviderCheckResult(
            provider=provider,
            mode="real",
            real_provider_success=True,
            prompt=prompt,
            response=proc.stdout,
            error=None,
            latency_seconds=round(time.time() - started, 3),
            base_url=base,
        )
    return None
