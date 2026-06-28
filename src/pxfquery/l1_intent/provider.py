from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

from pxfquery.l1_intent.parser import IntentBackendError
from pxfquery.utils.events import EventLog


DIYGATEWAY_BASE_URL = "http://localhost:3000/v1"
DIYGATEWAY_MODEL = "deepseek-ai/deepseek-v4-flash"
OFFICIAL_DEEPSEEK_BASE_URL = "https://api.deepseek.com/v1"
OFFICIAL_DEEPSEEK_MODEL = "deepseek-v4-flash"
DEFAULT_PROVIDER = "deepseek"

PXFQUERY_LLM_PROVIDER_ENV = "PXFQUERY_LLM_PROVIDER"
PXFQUERY_LLM_API_KEY_ENV = "PXFQUERY_LLM_API_KEY"
PXFQUERY_LLM_BASE_URL_ENV = "PXFQUERY_LLM_BASE_URL"
PXFQUERY_LLM_MODEL_ENV = "PXFQUERY_LLM_MODEL"
PXFQUERY_LLM_TIMEOUT_ENV = "PXFQUERY_LLM_TIMEOUT"


@dataclass
class LLMProviderConfig:
    name: str
    base_url: str
    api_key: str
    model: str
    timeout: float = 60.0
    max_tokens: int = 500
    max_network_attempts: int = 3
    network_retry_sleep: float = 2.0
    max_schema_repairs: int = 1
    restart_on_schema_failure: bool = True
    response_format_json: bool = True
    thinking: str | None = "disabled"


@dataclass
class ProviderEvidence:
    provider: str
    base_url: str
    model: str
    started_at: str
    finished_at: str | None = None
    attempts: list[dict[str, Any]] = field(default_factory=list)
    schema_repairs: int = 0
    chat_restarts: int = 0
    final_status: str = "started"
    parsed_json_hash: str | None = None
    parsed_json_excerpt: str | None = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class ProviderRegistry:
    """Session-local LLM provider registry. It never stores secrets in evidence."""

    def __init__(self, *, event_log: EventLog | None = None) -> None:
        self._providers: dict[str, LLMProvider] = {}
        self.default_provider_name: str | None = None
        self.event_log = event_log or EventLog(enabled=False)

    def register(self, config: LLMProviderConfig, *, default: bool = True) -> LLMProvider:
        provider = LLMProvider(config, event_log=self.event_log)
        return self.register_provider(config.name, provider, default=default)

    def register_provider(self, name: str, provider: "LLMProvider", *, default: bool = True) -> "LLMProvider":
        self._providers[name] = provider
        if default or self.default_provider_name is None:
            self.default_provider_name = name
        return provider

    def get(self, name: str | None = None) -> "LLMProvider | None":
        selected = name or self.default_provider_name
        if selected is None:
            return None
        return self._providers.get(selected)

    def status(self) -> dict[str, Any]:
        return {
            "default_provider": self.default_provider_name,
            "providers": {
                name: {
                    "base_url": provider.config.base_url,
                    "model": provider.config.model,
                    "timeout": provider.config.timeout,
                    "configured": bool(provider.config.api_key),
                }
                for name, provider in self._providers.items()
            },
        }


class LLMProvider:
    def __init__(self, config: LLMProviderConfig, *, event_log: EventLog | None = None) -> None:
        self.config = config
        self.event_log = event_log or EventLog(enabled=False)

    def parse_intent(
        self,
        text: str,
        *,
        schema: dict[str, Any],
        validator: Callable[[dict[str, Any]], Any] | None = None,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        evidence = ProviderEvidence(
            provider=self.config.name,
            base_url=self.config.base_url,
            model=self.config.model,
            started_at=_utc_now(),
        )
        messages = [
            {"role": "system", "content": _system_prompt(schema)},
            {"role": "user", "content": text},
        ]
        self.event_log.stage(
            "l1_intent",
            "provider_start",
            "Starting real LLM intent parse",
            provider=self.config.name,
            base_url=self.config.base_url,
            model=self.config.model,
        )
        try:
            payload = self._request_json(messages, evidence)
            if isinstance(payload, dict):
                if validator is not None:
                    validator(payload)
                _finish_success(evidence, payload)
                return payload, evidence.to_dict()
            raise IntentBackendError("provider returned JSON that is not an object")
        except IntentBackendError as first_error:
            repair_messages = list(messages)
            last_error: Exception = first_error
            for _ in range(self.config.max_schema_repairs):
                evidence.schema_repairs += 1
                repair_messages.append(
                    {
                        "role": "user",
                        "content": f"Invalid intent JSON: {last_error}. Return only one corrected JSON object.",
                    }
                )
                time.sleep(self.config.network_retry_sleep)
                try:
                    payload = self._request_json(repair_messages, evidence)
                    if isinstance(payload, dict):
                        if validator is not None:
                            validator(payload)
                        _finish_success(evidence, payload)
                        return payload, evidence.to_dict()
                    last_error = IntentBackendError("provider returned JSON that is not an object")
                except IntentBackendError as exc:
                    last_error = exc
            if self.config.restart_on_schema_failure:
                evidence.chat_restarts += 1
                time.sleep(self.config.network_retry_sleep)
                restart_messages = [
                    {"role": "system", "content": _system_prompt(schema)},
                    {
                        "role": "user",
                        "content": (
                            f"Parse this query into the required intent JSON. "
                            f"Previous provider output failed validation with: {last_error}. Query: {text}"
                        ),
                    },
                ]
                try:
                    payload = self._request_json(restart_messages, evidence)
                    if isinstance(payload, dict):
                        if validator is not None:
                            validator(payload)
                        _finish_success(evidence, payload)
                        return payload, evidence.to_dict()
                    last_error = IntentBackendError("provider returned JSON that is not an object")
                except IntentBackendError as exc:
                    last_error = exc
            evidence.finished_at = _utc_now()
            evidence.final_status = "failed"
            evidence.error = str(last_error)
            self.event_log.error(
                "l1_intent",
                "provider_failed",
                "LLM intent parse failed",
                provider=self.config.name,
                base_url=self.config.base_url,
                model=self.config.model,
                error=str(last_error),
            )
            raise IntentBackendError(str(last_error)) from last_error

    def request_json(
        self,
        *,
        stage: str,
        system_prompt: str,
        user_payload: dict[str, Any],
        validator: Callable[[Any], Any] | None = None,
        temperature: float = 0,
    ) -> tuple[Any, dict[str, Any]]:
        evidence = ProviderEvidence(
            provider=self.config.name,
            base_url=self.config.base_url,
            model=self.config.model,
            started_at=_utc_now(),
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_payload, ensure_ascii=True, sort_keys=True)},
        ]
        self.event_log.stage(
            stage,
            "provider_start",
            "Starting real LLM JSON request",
            provider=self.config.name,
            base_url=self.config.base_url,
            model=self.config.model,
        )
        payload = self._request_json(messages, evidence, temperature=temperature)
        if validator is not None:
            validator(payload)
        _finish_success(evidence, payload if isinstance(payload, dict) else {"payload": payload})
        return payload, evidence.to_dict()

    def _request_json(self, messages: list[dict[str, str]], evidence: ProviderEvidence, *, temperature: float = 0) -> Any:
        request_payload: dict[str, Any] = {
            "model": self.config.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": self.config.max_tokens,
        }
        if self.config.response_format_json:
            request_payload["response_format"] = {"type": "json_object"}
        if self.config.thinking is not None:
            request_payload["thinking"] = {"type": self.config.thinking}

        last_error: Exception | None = None
        for attempt in range(1, self.config.max_network_attempts + 1):
            attempt_started = time.monotonic()
            try:
                self.event_log.stage(
                    "l1_intent",
                    "provider_attempt",
                    "Calling chat completions endpoint",
                    provider=self.config.name,
                    base_url=self.config.base_url,
                    model=self.config.model,
                    attempt=attempt,
                )
                response_payload = self._post_chat_completions(request_payload)
                content = response_payload["choices"][0]["message"]["content"]
                attempt_record = _attempt_record(
                    attempt,
                    ok=True,
                    elapsed_ms=int((time.monotonic() - attempt_started) * 1000),
                    content=content,
                )
                evidence.attempts.append(attempt_record)
                return json.loads(content)
            except (KeyError, IndexError, TypeError, json.JSONDecodeError, IntentBackendError) as exc:
                last_error = exc
                evidence.attempts.append(
                    _attempt_record(
                        attempt,
                        ok=False,
                        elapsed_ms=int((time.monotonic() - attempt_started) * 1000),
                        error=f"{type(exc).__name__}: {exc}",
                    )
                )
                if attempt < self.config.max_network_attempts:
                    self.event_log.warning(
                        "l1_intent",
                        "provider_retry",
                        "LLM provider attempt failed; sleeping before retry",
                        provider=self.config.name,
                        attempt=attempt,
                        sleep_seconds=self.config.network_retry_sleep,
                        error=f"{type(exc).__name__}: {exc}",
                    )
                    time.sleep(self.config.network_retry_sleep)
        raise IntentBackendError(f"LLM provider request failed after retries: {last_error}") from last_error

    def _post_chat_completions(self, payload: dict[str, Any]) -> dict[str, Any]:
        request = urllib.request.Request(
            f"{self.config.base_url.rstrip('/')}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.config.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.config.timeout) as response:
                body = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise IntentBackendError(f"HTTP {exc.code}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            raise IntentBackendError(f"{type(exc).__name__}: {exc}") from exc
        try:
            response_payload = json.loads(body)
        except json.JSONDecodeError as exc:
            raise IntentBackendError(f"provider returned non-JSON HTTP payload: {body[:500]}") from exc
        if "error" in response_payload:
            raise IntentBackendError(f"provider returned error: {response_payload['error']}")
        if not isinstance(response_payload.get("choices"), list):
            raise IntentBackendError(f"provider returned unexpected payload: {body[:500]}")
        return response_payload


def provider_from_env(*, required: bool = False) -> LLMProvider | None:
    api_key = os.environ.get(PXFQUERY_LLM_API_KEY_ENV)
    if not api_key:
        if required:
            raise IntentBackendError(f"LLM provider token is not configured; set {PXFQUERY_LLM_API_KEY_ENV}")
        return None
    name = os.environ.get(PXFQUERY_LLM_PROVIDER_ENV, DEFAULT_PROVIDER)
    return LLMProvider(
        LLMProviderConfig(
            name=name,
            base_url=os.environ.get(PXFQUERY_LLM_BASE_URL_ENV, OFFICIAL_DEEPSEEK_BASE_URL),
            api_key=api_key,
            model=os.environ.get(PXFQUERY_LLM_MODEL_ENV, OFFICIAL_DEEPSEEK_MODEL),
            timeout=float(os.environ.get(PXFQUERY_LLM_TIMEOUT_ENV, "60")),
        )
    )


def _system_prompt(schema: dict[str, Any]) -> str:
    return "\n".join(
        [
            "You are PxFquery L1 intent parsing.",
            "Return exactly one JSON object and no markdown.",
            "Do not answer the biomedical question.",
            "Do not list perturbation candidates, genes, drugs, scores, citations, route plans, or evidence.",
            "Your job is only to extract the user's wording into intent fields for later resource routing.",
            "Schema:",
            json.dumps(schema, ensure_ascii=True, sort_keys=True),
            "Meanings:",
            "query_type=forward when the user asks what a perturbation does functionally.",
            "query_type=reverse when the user asks which perturbations can achieve a functional state.",
            "pert_class=genetic for gene perturbation and drug for compound/drug treatment.",
            "genetic_modality captures the user's stated genetic modality: rnai, shrna, crispr, knockdown, knockout, overexpression, lof, gof, unknown, or null.",
            "For CMAP/LINCS resources, shRNA/RNAi maps later to sh and CRISPR loss-of-function maps later to xpr; do not perform that resource routing here.",
            "Use null for unknown scalar fields and empty arrays for absent activate/suppress phrases.",
        ]
    )


def _attempt_record(
    attempt: int,
    *,
    ok: bool,
    elapsed_ms: int,
    content: str | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "attempt": attempt,
        "ok": ok,
        "elapsed_ms": elapsed_ms,
    }
    if content is not None:
        out["response_hash"] = _hash_text(content)
        out["response_excerpt"] = content[:500]
    if error is not None:
        out["error"] = error[:500]
    return out


def _finish_success(evidence: ProviderEvidence, payload: dict[str, Any]) -> None:
    encoded = json.dumps(payload, ensure_ascii=True, sort_keys=True)
    evidence.finished_at = _utc_now()
    evidence.final_status = "ok"
    evidence.parsed_json_hash = _hash_text(encoded)
    evidence.parsed_json_excerpt = encoded[:500]


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()
