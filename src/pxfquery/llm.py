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


def provider_check(
    *,
    provider: str = DEFAULT_PROVIDER,
    prompt: str = "Return JSON with key ms7_provider_check and value ok.",
    mode: str = "real",
    timeout: float = 20.0,
    base_url: str | None = None,
) -> ProviderCheckResult:
    base = (base_url or os.environ.get("LLM_GATEWAY_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
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
        "model": provider.replace("llm_gateway/", "", 1),
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": 80,
    }
    curl_result = _curl_fallback(base, payload, provider, prompt, timeout, started)
    if curl_result is not None:
        return curl_result
    request = urllib.request.Request(
        f"{base}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('LLM_GATEWAY_API_KEY', 'local-llm-gateway')}",
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
) -> ProviderCheckResult | None:
    curl = shutil.which("curl")
    key = os.environ.get("LLM_GATEWAY_API_KEY")
    if curl is None or not key:
        return None
    proc = subprocess.run(
        [
            curl,
            "-sS",
            "-m",
            str(int(timeout)),
            f"{base}/chat/completions",
            "-H",
            f"Authorization: Bearer {key}",
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
