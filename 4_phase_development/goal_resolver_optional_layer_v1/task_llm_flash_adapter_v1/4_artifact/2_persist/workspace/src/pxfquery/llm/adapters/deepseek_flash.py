"""deepseek_flash.py — Optional DeepSeek v4 flash adapter (pxfquery-T-034).

This module ships an *optional* `DeepSeekFlashAdapter` that mirrors the public
contract of the legacy `pxfquery.llm.LLMClient` but:

- targets the DeepSeek OpenAI-compatible endpoint (``https://api.deepseek.com/v1``)
  with the DeepSeek v4 flash model by default;
- never raises on connection / auth / HTTP failure — instead returns the
  structured ``{"ok": False, "reason": "...", "latency_ms": N}`` shape used by
  the rest of the PxFquery pipeline as a graceful fallback;
- is installed only when the user opts in via ``pip install pxfquery-T-034[llm-flash]``,
  so the deterministic forward/reverse pipeline continues to work without this
  layer.

CyHex llm_gateway is the active runtime for this session. The adapter does NOT
flip the active model — it is registered as an additional provider that downstream
code can opt into by instantiating it explicitly.
"""

from __future__ import annotations

import json
import os
import re
import time
from typing import Any, Dict, List, Optional

__all__ = ["DeepSeekFlashAdapter", "AdapterUnavailable"]


# Default DeepSeek endpoint and model. Both can be overridden per-instance.
DEFAULT_BASE_URL = "https://api.deepseek.com/v1"
DEFAULT_MODEL = "deepseek-v4-flash"

# Tight probe budget; never let a health_check block the pipeline.
HEALTH_CHECK_TIMEOUT_S = 5.0
HEALTH_CHECK_MAX_TOKENS = 4


class AdapterUnavailable(RuntimeError):
    """Internal signal raised when the adapter cannot reach the endpoint.

    Callers should NOT see this exception — public methods catch it and convert
    it into a structured ``ok=False`` dict so the rest of the pipeline can carry
    on with deterministic results.
    """


def _now_ms(t0: float) -> int:
    return int((time.monotonic() - t0) * 1000)


def _new_result(model: str) -> Dict[str, Any]:
    return {
        "ok": False,
        "model": model,
        "reply": None,
        "latency_ms": None,
        "error_type": None,
        "error_message": None,
        "reason": None,  # populated with a human-readable fallback reason
    }


def _normalize_reply(content: Optional[str]) -> str:
    if not content:
        return ""
    return re.sub(r"[^A-Za-z]", "", content).strip().upper()


class DeepSeekFlashAdapter:
    """Optional DeepSeek v4 flash provider for PxFquery.

    Mirrors the public surface of ``pxfquery.llm.LLMClient`` so a resolver can
    swap providers without changing call sites:

    - ``health_check() -> dict``
    - ``parse_query(user_input, available_terms=None) -> dict``
    - ``summarize_forward(result, max_words=200) -> str``
    - ``summarize_reverse(result, max_words=200) -> str``

    Parameters
    ----------
    api_key : str, optional
        API key. Falls back to ``DEEPSEEK_API_KEY`` or ``OPENAI_API_KEY`` env vars.
        If absent, ``health_check()`` returns a structured ``ok=False, reason=missing_api_key``.
    base_url : str, optional
        OpenAI-compatible endpoint. Defaults to ``https://api.deepseek.com/v1``.
    model : str, optional
        Model identifier. Defaults to ``deepseek-v4-flash``.
    timeout : float, optional
        Per-request timeout in seconds. Defaults to 20.0.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        model: str = DEFAULT_MODEL,
        timeout: float = 20.0,
    ) -> None:
        self.model = model
        self.base_url = base_url
        self.timeout = timeout
        self.api_key = (
            api_key
            or os.getenv("DEEPSEEK_API_KEY")
            or os.getenv("OPENAI_API_KEY")
            or os.getenv("PXFQUERY_API_KEY")
        )
        # The OpenAI client is built lazily — we don't want a missing ``openai``
        # package to break import of this module.
        self._client = None
        self._client_build_error: Optional[str] = None
        if self.api_key:
            try:
                from openai import OpenAI  # type: ignore
                kwargs = {"api_key": self.api_key, "timeout": self.timeout}
                if self.base_url:
                    kwargs["base_url"] = self.base_url
                self._client = OpenAI(**kwargs)
            except Exception as e:  # pragma: no cover - import / build edge cases
                self._client_build_error = f"{type(e).__name__}: {e}"

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _fail(
        self,
        result: Dict[str, Any],
        *,
        error_type: str,
        error_message: str,
        reason: str,
    ) -> Dict[str, Any]:
        result["ok"] = False
        result["error_type"] = error_type
        result["error_message"] = error_message
        result["reason"] = reason
        return result

    def _build_unavailable(self, reason: str, base_message: str = "") -> Dict[str, Any]:
        result = _new_result(self.model)
        result["latency_ms"] = 0
        return self._fail(
            result,
            error_type="AdapterUnavailable",
            error_message=base_message,
            reason=reason,
        )

    def _check_preconditions(self) -> Optional[Dict[str, Any]]:
        """Return a structured unavailable dict if preconditions aren't met."""
        if not self.api_key:
            return self._build_unavailable(
                reason="missing_api_key",
                base_message="No DEEPSEEK_API_KEY / OPENAI_API_KEY / api_key= provided.",
            )
        if self._client is None:
            return self._build_unavailable(
                reason="client_build_failed",
                base_message=self._client_build_error or "openai SDK could not build client.",
            )
        return None

    # ------------------------------------------------------------------
    # Public API (mirrors pxfquery.llm.LLMClient)
    # ------------------------------------------------------------------

    def health_check(self, verbose: bool = False) -> Dict[str, Any]:
        """Probe the endpoint. Always returns a dict, never raises."""
        t0 = time.monotonic()
        result = _new_result(self.model)
        unavailable = self._check_preconditions()
        if unavailable is not None:
            unavailable["latency_ms"] = _now_ms(t0)
            return unavailable
        try:
            resp = self._client.chat.completions.create(  # type: ignore[union-attr]
                model=self.model,
                messages=[
                    {"role": "system", "content": "Connectivity test. Reply exactly: OK"},
                    {"role": "user", "content": "Reply with exactly: OK"},
                ],
                temperature=0,
                max_tokens=HEALTH_CHECK_MAX_TOKENS,
                timeout=HEALTH_CHECK_TIMEOUT_S,
            )
            content = (resp.choices[0].message.content or "").strip()
            result["reply"] = content
            result["ok"] = _normalize_reply(content) == "OK"
            if not result["ok"]:
                result["reason"] = "unexpected_reply"
        except Exception as e:
            result = self._fail(
                result,
                error_type=type(e).__name__,
                error_message=str(e),
                reason="endpoint_unreachable",
            )
        finally:
            result["latency_ms"] = _now_ms(t0)
        if verbose:
            print(json.dumps(result, ensure_ascii=False))
        return result

    def parse_query(
        self,
        user_input: str,
        available_terms: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Parse a natural language query into an INTENT_SCHEMA dict.

        On any failure (missing key, unreachable endpoint, malformed JSON), this
        returns an empty-intent dict with ``{"ok": False, "reason": "..."}``
        added so callers can detect the fallback without exceptions.
        """
        empty = {
            "query_type": None,
            "perturbation": None,
            "cell_line": None,
            "activate": [],
            "suppress": [],
            "top_n": None,
            "ok": False,
            "reason": None,
        }
        unavailable = self._check_preconditions()
        if unavailable is not None:
            empty["reason"] = unavailable["reason"]
            empty["error_type"] = unavailable["error_type"]
            return empty

        terms_hint = ""
        if available_terms:
            sample = available_terms[:30]
            terms_hint = (
                f"\n\nAvailable functional terms (sample): {', '.join(sample)}"
            )
        system_prompt = (
            "You are a bioinformatics query parser for PxFquery. "
            "Return a JSON object only with the schema "
            "{\"query_type\": 'forward'|'reverse'|null, "
            "\"perturbation\": string|null, \"cell_line\": string|null, "
            "\"activate\": list, \"suppress\": list, \"top_n\": int|null}. "
            f"{terms_hint}"
        )
        try:
            resp = self._client.chat.completions.create(  # type: ignore[union-attr]
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                ],
                temperature=0,
                max_tokens=300,
                timeout=self.timeout,
            )
            content = (resp.choices[0].message.content or "").strip()
            content = re.sub(r"^```(?:json)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content)
            intent = json.loads(content)
            intent["ok"] = True
            intent.setdefault("activate", [])
            intent.setdefault("suppress", [])
            return intent
        except Exception as e:
            empty["error_type"] = type(e).__name__
            empty["error_message"] = str(e)
            empty["reason"] = "endpoint_unreachable"
            return empty

    def summarize_forward(self, result: Any, max_words: int = 200) -> str:
        """Summarize a forward query result. Always returns a string."""
        unavailable = self._check_preconditions()
        if unavailable is not None:
            return (
                f"[DeepSeekFlashAdapter unavailable: {unavailable['reason']}. "
                "Deterministic result is unaffected.]"
            )
        # Construct a compact prompt from the result's public attributes.
        perturbation = getattr(result, "perturbation", "perturbation")
        cell_info = getattr(result, "cell_line", None) or "all cell lines"
        try:
            activated = getattr(result, "top_activated", None)
            suppressed = getattr(result, "top_suppressed", None)
            activated_str = (
                "\n".join(
                    f"  {term}: {score:.2f}"
                    for term, score in list(activated.items())[:10]
                )
                if activated is not None
                else "(none)"
            )
            suppressed_str = (
                "\n".join(
                    f"  {term}: {score:.2f}"
                    for term, score in list(suppressed.items())[:10]
                )
                if suppressed is not None
                else "(none)"
            )
        except Exception:
            activated_str, suppressed_str = "(unavailable)", "(unavailable)"

        prompt = (
            "Summarize the forward perturbation-function result below in plain "
            f"scientific English (≤{max_words} words).\n"
            f"Perturbation: {perturbation}\n"
            f"Cell context: {cell_info}\n"
            f"Top activated:\n{activated_str}\n"
            f"Top suppressed:\n{suppressed_str}\n"
        )
        try:
            resp = self._client.chat.completions.create(  # type: ignore[union-attr]
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=400,
                timeout=self.timeout,
            )
            return (resp.choices[0].message.content or "").strip()
        except Exception as e:
            return f"[DeepSeekFlashAdapter summary unavailable: {type(e).__name__}: {e}]"

    def summarize_reverse(self, result: Any, max_words: int = 200) -> str:
        """Summarize a reverse query result. Always returns a string."""
        unavailable = self._check_preconditions()
        if unavailable is not None:
            return (
                f"[DeepSeekFlashAdapter unavailable: {unavailable['reason']}. "
                "Deterministic result is unaffected.]"
            )
        try:
            candidates_df = getattr(result, "candidates_df", None)
            activate = getattr(result, "activate", []) or []
            suppress = getattr(result, "suppress", []) or []
            cell_info = getattr(result, "cell_line", None) or "all cell lines"
            if candidates_df is not None and len(candidates_df) > 0:
                top5 = candidates_df.head(5)
                candidates_str = "\n".join(
                    f"  {row.get('cmap_name','?')} ({row.get('cell_iname','?')}): "
                    f"similarity={row.get('similarity', 0):.3f}"
                    for _, row in top5.iterrows()
                )
            else:
                candidates_str = "(none)"
        except Exception:
            candidates_str, activate, suppress, cell_info = (
                "(unavailable)", [], [], "all cell lines"
            )

        prompt = (
            "Summarize the reverse perturbation-function result below in plain "
            f"scientific English (≤{max_words} words).\n"
            f"Cell context: {cell_info}\n"
            f"Activate: {', '.join(activate) or 'none'}\n"
            f"Suppress: {', '.join(suppress) or 'none'}\n"
            f"Top candidates:\n{candidates_str}\n"
        )
        try:
            resp = self._client.chat.completions.create(  # type: ignore[union-attr]
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=400,
                timeout=self.timeout,
            )
            return (resp.choices[0].message.content or "").strip()
        except Exception as e:
            return f"[DeepSeekFlashAdapter summary unavailable: {type(e).__name__}: {e}]"
