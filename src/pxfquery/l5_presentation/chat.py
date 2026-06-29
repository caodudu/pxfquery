from __future__ import annotations

from typing import Any

from pxfquery.l5_presentation.answer import build_answer
from pxfquery.l5_presentation.model import PxFQueryAnswer


def build_chat_response(
    question: str,
    dossier: dict[str, Any],
    message: str,
    *,
    answer: PxFQueryAnswer | None = None,
    history: list[dict[str, Any]] | None = None,
    llm_provider: Any | None = None,
) -> dict[str, Any]:
    if llm_provider is None:
        raise RuntimeError("pxf.tl.chat requires a configured PxFquery LLM provider; local template fallback is disabled.")
    if not hasattr(llm_provider, "request_json"):
        raise TypeError("pxf.tl.chat requires the configured LLM provider to expose request_json(...)")

    current_answer = answer or build_answer(question, dossier, mode="python")
    user_payload = {
        "original_question": question,
        "user_message": message,
        "current_answer": {
            "headline": current_answer.headline,
            "summary": current_answer.summary,
            "summary_source": current_answer.summary_source,
            "evidence": current_answer.evidence,
            "limitations": current_answer.limitations,
            "tables": current_answer.tables,
            "figures": current_answer.figures,
            "rendering_contract": current_answer.rendering_contract,
        },
        "l4_evidence": dossier,
        "history": history or [],
    }
    result, provider_evidence = _request_chat_json(llm_provider, user_payload)
    if not isinstance(result, dict):
        raise RuntimeError("pxf.tl.chat provider returned non-object JSON")
    return {
        "user": message,
        "assistant": str(result.get("response") or ""),
        "cited_tables": [str(item) for item in result.get("cited_tables", [])],
        "warnings": [str(item) for item in result.get("warnings", [])],
        "provider_evidence": provider_evidence,
    }


def _request_chat_json(llm_provider: Any, user_payload: dict[str, Any]) -> tuple[Any, dict[str, Any]]:
    system_prompt = (
        "Answer the user's follow-up using only the supplied PxFquery L4/L5 evidence. "
        "Do not add candidates, change scores, invent citations, claim clinical efficacy, "
        "or upgrade weak, proxy, partial, or no-hit evidence. Return one valid JSON object "
        "with keys: response, cited_tables, warnings."
    )
    try:
        return llm_provider.request_json(
            stage="l5_chat",
            system_prompt=system_prompt,
            user_payload=user_payload,
            temperature=0,
        )
    except Exception as first_error:
        repair_payload = {
            "previous_error": f"{type(first_error).__name__}: {first_error}",
            "instruction": (
                "The previous L5 chat response could not be parsed as valid JSON. "
                "Return one valid JSON object only. Use normal UTF-8 text in the response; "
                "do not emit malformed backslash escape sequences. Keep the same evidence limits."
            ),
            "original_question": user_payload.get("original_question"),
            "user_message": user_payload.get("user_message"),
            "current_answer": user_payload.get("current_answer"),
            "history": user_payload.get("history", []),
        }
        result, evidence = llm_provider.request_json(
            stage="l5_chat_json_repair",
            system_prompt=system_prompt,
            user_payload=repair_payload,
            temperature=0,
        )
        evidence = {"initial_error": f"{type(first_error).__name__}: {first_error}", "repair": evidence}
        return result, evidence
