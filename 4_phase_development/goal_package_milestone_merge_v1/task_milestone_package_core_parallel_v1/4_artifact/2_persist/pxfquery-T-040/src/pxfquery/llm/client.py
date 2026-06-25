"""
client.py — LLM integration for PxFquery.

Uses litellm to support any OpenAI-compatible API (OpenAI, SiliconFlow,
DeepSeek, Ollama, etc.). The LLM is responsible for:
  1. Parsing natural language queries into structured intent
  2. Summarizing query results in plain language

The LLM does NOT perform any computation — all scoring and ranking
is done by the query modules.
"""

from __future__ import annotations
import json
import os
import re
import time
from typing import Any, Dict, List, Optional

from ..logging_utils import LoggingSettings, configure_logger
from ..query.forward import ForwardResult
from ..query.reverse import ReverseResult


# ------------------------------------------------------------------
# Intent schema returned by parse_query()
# ------------------------------------------------------------------
INTENT_SCHEMA = {
    "query_type": "forward | reverse",
    "perturbation": "string or null",
    "cell_line": "string or null",
    "activate": ["list of functional terms"],
    "suppress": ["list of functional terms"],
    "top_n": "integer or null",
}


class LLMClient:
    """
    Thin litellm wrapper for PxFquery.

    Parameters
    ----------
    api_key : str, optional
        API key. Falls back to OPENAI_API_KEY / SILICONFLOW_API_KEY env vars.
    base_url : str, optional
        API base URL (e.g. 'https://api.siliconflow.cn/v1').
        Leave None for official OpenAI.
    model : str
        Model identifier, e.g. 'gpt-4o-mini', 'deepseek-chat',
        'Qwen/Qwen2.5-72B-Instruct'.

    Examples
    --------
    >>> client = LLMClient(api_key="sk-...", base_url="https://api.siliconflow.cn/v1",
    ...                    model="Qwen/Qwen2.5-72B-Instruct")
    >>> client.health_check()
    >>> intent = client.parse_query("MCF7里抑制MYC激活凋亡的候选药物")
    >>> summary = client.summarize_forward(result)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: str = "gpt-4o-mini",
    ):
        self.model = model
        self.base_url = base_url

        # Resolve API key
        self.api_key = (
            api_key
            or os.getenv("OPENAI_API_KEY")
            or os.getenv("SILICONFLOW_API_KEY")
            or os.getenv("PXFQUERY_API_KEY")
        )
        if not self.api_key:
            raise ValueError(
                "No API key provided. Pass api_key= or set OPENAI_API_KEY "
                "/ SILICONFLOW_API_KEY environment variable."
            )

        self._client = self._build_client()
        self._logger = configure_logger(
            "pxfquery.llm",
            LoggingSettings(verbosity="normal"),
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def health_check(self, verbose: bool = True) -> Dict[str, Any]:
        """
        Test connectivity with a minimal prompt.

        Returns
        -------
        dict with keys: ok, model, reply, latency_ms, error_type, error_message
        """
        t0 = time.monotonic()
        result = {
            "ok": False, "model": self.model,
            "reply": None, "latency_ms": None,
            "error_type": None, "error_message": None,
        }
        try:
            resp = self._client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Connectivity test. Reply exactly: OK"},
                    {"role": "user", "content": "Reply with exactly: OK"},
                ],
                temperature=0,
                max_tokens=5,
            )
            content = (resp.choices[0].message.content or "").strip()
            result["reply"] = content
            normalized = re.sub(r"[^A-Za-z]", "", content).upper()
            result["ok"] = (normalized == "OK")
        except Exception as e:
            result["error_type"] = type(e).__name__
            result["error_message"] = str(e)
        finally:
            result["latency_ms"] = int((time.monotonic() - t0) * 1000)

        if verbose:
            self._logger.info("LLM health_check: %s", json.dumps(result, ensure_ascii=False))
        return result

    def parse_query(
        self,
        user_input: str,
        available_terms: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Parse a natural language query into structured intent.

        Parameters
        ----------
        user_input : str
            Free-form user query, e.g.
            "A549里敲掉EGFR会激活哪些通路" or
            "find drugs that suppress MYC and activate apoptosis in MCF7".
        available_terms : list of str, optional
            If provided, the LLM will be guided to use these term names.

        Returns
        -------
        dict with keys matching INTENT_SCHEMA:
            query_type, perturbation, cell_line, activate, suppress, top_n
        """
        terms_hint = ""
        if available_terms:
            sample = available_terms[:30]
            terms_hint = (
                f"\n\nAvailable functional terms (sample): {', '.join(sample)}"
            )

        system_prompt = f"""You are a bioinformatics query parser for PxFquery, a perturbation-function query tool.

Your job: parse the user's natural language query and return a JSON object.

JSON schema:
{{
  "query_type": "forward" or "reverse",
  "perturbation": "gene or drug name, or null",
  "cell_line": "cell line name, or null",
  "activate": ["list of functional pathway terms to activate"],
  "suppress": ["list of functional pathway terms to suppress"],
  "top_n": integer or null
}}

Rules:
- "forward" query: user wants to know what a perturbation does functionally
- "reverse" query: user wants to find perturbations that achieve a functional goal
- Extract cell line names (e.g. A549, MCF7, HeLa, PC3)
- Extract pathway terms as closely as possible to MSigDB Hallmark naming
  (e.g. HALLMARK_APOPTOSIS, HALLMARK_MYC_TARGETS_V1)
- If top_n is not mentioned, return null{terms_hint}

Return ONLY the JSON object, no other text."""

        try:
            resp = self._client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                ],
                temperature=0,
                max_tokens=300,
            )
            content = resp.choices[0].message.content.strip()
            # Strip markdown code fences if present
            content = re.sub(r"^```(?:json)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content)
            return json.loads(content)
        except json.JSONDecodeError as e:
            self._logger.warning("Failed to parse JSON response: %s", e)
            return _empty_intent()
        except Exception as e:
            self._logger.warning("parse_query error: %s: %s", type(e).__name__, e)
            return _empty_intent()

    def summarize_forward(self, result: ForwardResult, max_words: int = 200) -> str:
        """
        Summarize a forward query result in plain language.

        Parameters
        ----------
        result : ForwardResult
        max_words : int
            Target summary length in words.

        Returns
        -------
        str — Plain language summary, ≤ max_words words.
        """
        if not result.found:
            return f"No results found. {result.note}"

        activated_str = "\n".join(
            f"  {term}: {score:.2f}"
            for term, score in result.top_activated.head(10).items()
        )
        suppressed_str = "\n".join(
            f"  {term}: {score:.2f}"
            for term, score in result.top_suppressed.head(10).items()
        )

        cell_info = result.cell_line or f"all cell lines ({', '.join(result.cells_used[:5])})"

        prompt = f"""You are summarizing a bioinformatics query result for a scientific audience.

Query: What are the functional consequences of perturbing '{result.perturbation}' in {cell_info}?

Top ACTIVATED pathways (higher score = stronger activation):
{activated_str}

Top SUPPRESSED pathways (more negative = stronger suppression):
{suppressed_str}

Write a concise scientific summary in ≤{max_words} words.
Focus on biological interpretation. Do not invent information beyond what is listed.
Do not use bullet points."""

        try:
            resp = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=400,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"[LLM summary unavailable: {e}]"

    def summarize_reverse(self, result: ReverseResult, max_words: int = 200) -> str:
        """
        Summarize a reverse query result in plain language.

        Parameters
        ----------
        result : ReverseResult
        max_words : int

        Returns
        -------
        str
        """
        if not result.found:
            return f"No results found. {result.note}"

        top5 = result.candidates_df.head(5)
        candidates_str = "\n".join(
            f"  {row['cmap_name']} ({row['cell_iname']}): similarity={row['similarity']:.3f}, "
            f"key terms: {row['driving_terms']}"
            for _, row in top5.iterrows()
        )

        activate_str = ", ".join(result.activate) if result.activate else "none"
        suppress_str = ", ".join(result.suppress) if result.suppress else "none"
        cell_info = result.cell_line or "all cell lines"

        prompt = f"""You are summarizing a bioinformatics perturbation recommendation result.

Query goal:
  Cell line: {cell_info}
  Activate: {activate_str}
  Suppress: {suppress_str}

Top recommended perturbations (ranked by cosine similarity):
{candidates_str}

Write a concise scientific summary in ≤{max_words} words.
Explain why the top candidates are recommended based on the driving terms.
Do not invent information beyond what is listed."""

        try:
            resp = self._client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=400,
            )
            return resp.choices[0].message.content.strip()
        except Exception as e:
            return f"[LLM summary unavailable: {e}]"

    # ------------------------------------------------------------------
    # Private
    # ------------------------------------------------------------------

    def _build_client(self):
        """Build an OpenAI-compatible client."""
        from openai import OpenAI
        kwargs = {"api_key": self.api_key}
        if self.base_url:
            kwargs["base_url"] = self.base_url
        return OpenAI(**kwargs)


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _empty_intent() -> Dict[str, Any]:
    return {
        "query_type": None,
        "perturbation": None,
        "cell_line": None,
        "activate": [],
        "suppress": [],
        "top_n": None,
    }
