from __future__ import annotations

import json
import os
import shutil
import subprocess
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from pxfquery.l1_nlu.parser import NLUBackendError


DEFAULT_L1_BASE_URL = "http://localhost:3000/v1"
DEFAULT_L1_MODEL = "deepseek-ai/deepseek-v4-flash"
L1_API_KEY_ENV = "PXFQUERY_L1_API_KEY"
L1_BASE_URL_ENV = "PXFQUERY_L1_BASE_URL"
L1_MODEL_ENV = "PXFQUERY_L1_MODEL"


@dataclass
class OpenAICompatibleNLUBackend:
    """Backend that asks a configured chat-completions endpoint for L1 intent JSON."""

    base_url: str
    api_key: str
    model: str
    timeout: float = 30.0
    max_tokens: int = 350

    def parse(self, text: str, *, schema: dict[str, Any]) -> dict[str, Any]:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": _user_prompt(text, schema)}],
            "temperature": 0,
            "max_tokens": self.max_tokens,
        }
        response_payload = self._post_chat_completions(payload)
        try:
            content = response_payload["choices"][0]["message"]["content"]
            parsed = json.loads(content)
        except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
            raise NLUBackendError("L1 backend response did not contain valid JSON content") from exc
        if not isinstance(parsed, dict):
            raise NLUBackendError("L1 backend JSON content was not an object")
        return parsed

    def _post_chat_completions(self, payload: dict[str, Any]) -> dict[str, Any]:
        curl = shutil.which("curl")
        if curl is not None:
            return self._post_with_curl(curl, payload)
        return self._post_with_urllib(payload)

    def _post_with_curl(self, curl: str, payload: dict[str, Any]) -> dict[str, Any]:
        try:
            proc = subprocess.run(
                [
                    curl,
                    "-sS",
                    "-m",
                    str(int(self.timeout)),
                    f"{self.base_url.rstrip('/')}/chat/completions",
                    "-H",
                    f"Authorization: Bearer {self.api_key}",
                    "-H",
                    "Content-Type: application/json",
                    "-d",
                    json.dumps(payload),
                ],
                text=True,
                capture_output=True,
                timeout=self.timeout + 5,
            )
        except (TimeoutError, OSError, subprocess.SubprocessError) as exc:
            raise NLUBackendError(f"L1 backend curl request failed: {type(exc).__name__}: {exc}") from exc
        if proc.returncode != 0:
            raise NLUBackendError(f"L1 backend curl request failed: {proc.stderr[:500]}")
        try:
            response_payload = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise NLUBackendError(f"L1 backend returned non-JSON HTTP payload: {proc.stdout[:500]}") from exc
        if "error" in response_payload:
            raise NLUBackendError(f"L1 backend returned error: {response_payload['error']}")
        if not isinstance(response_payload.get("choices"), list):
            raise NLUBackendError(f"L1 backend returned unexpected payload: {proc.stdout[:500]}")
        return response_payload

    def _post_with_urllib(self, payload: dict[str, Any]) -> dict[str, Any]:
        request = urllib.request.Request(
            f"{self.base_url.rstrip('/')}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                response_payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            try:
                body = exc.read().decode("utf-8", errors="replace")
            except Exception:
                body = ""
            raise NLUBackendError(f"L1 backend request failed: HTTP {exc.code}: {body[:500]}") from exc
        except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            raise NLUBackendError(f"L1 backend request failed: {type(exc).__name__}: {exc}") from exc
        if "error" in response_payload:
            raise NLUBackendError(f"L1 backend returned error: {response_payload['error']}")
        if not isinstance(response_payload.get("choices"), list):
            raise NLUBackendError("L1 backend returned unexpected payload")
        return response_payload


def backend_from_env(*, required: bool = False) -> OpenAICompatibleNLUBackend | None:
    api_key = os.environ.get(L1_API_KEY_ENV)
    if not api_key:
        if required:
            raise NLUBackendError(f"L1 backend token is not configured; set {L1_API_KEY_ENV}")
        return None
    return OpenAICompatibleNLUBackend(
        base_url=os.environ.get(L1_BASE_URL_ENV, DEFAULT_L1_BASE_URL),
        api_key=api_key,
        model=os.environ.get(L1_MODEL_ENV, DEFAULT_L1_MODEL),
    )


def _user_prompt(text: str, schema: dict[str, Any]) -> str:
    return "\n".join(
        [
            "You are PxFquery L1 natural-language understanding.",
            "Parse the user question into resolver-compatible intent JSON only.",
            "Do not answer the biomedical question.",
            "Do not list perturbation candidates, scores, citations, or evidence.",
            "Return exactly one JSON object and no markdown.",
            "Schema:",
            json.dumps(schema, ensure_ascii=True, sort_keys=True),
            "Meaning:",
            "forward = user asks what a perturbation does functionally.",
            "reverse = user asks which perturbations can achieve a functional state.",
            "pert_class is genetic for gene knockdown/knockout/overexpression and drug for compounds/inhibitors/treatments.",
            "activate and suppress are short functional goal phrases from the user question; keep empty arrays when absent.",
            f"Question: {text}",
        ]
    )
