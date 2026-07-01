from __future__ import annotations

import re
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
        "presentation_policy": {
            "audience": "researcher-facing natural language answer",
            "use_complete_evidence": True,
            "do_not_expose": [
                "raw JSON",
                "raw program identifiers",
                "numbered program codes",
                "route IDs",
                "row counts",
                "numeric scores",
                "table values",
                "MCP",
                "backend tool names",
                "internal layer names",
            ],
            "if_not_supported": "say the current evidence does not support the requested activation",
        },
        "current_answer": {
            "headline": current_answer.headline,
            "summary": current_answer.summary,
            "summary_source": current_answer.summary_source,
            "evidence": current_answer.evidence,
            "limitations": current_answer.limitations,
            "program_direction_summary": _program_direction_context(current_answer.tables),
            "tables": current_answer.tables,
            "figures": current_answer.figures,
            "rendering_contract": current_answer.rendering_contract,
        },
        "evidence_boundary": _evidence_boundary_context(dossier),
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
        "You answer a follow-up question for a researcher-facing biomedical result. "
        "Use the complete supplied evidence context, including tables and L4 evidence, but "
        "produce only a clean user-facing natural-language answer. The presentation_policy "
        "is mandatory. Do not infer from outside knowledge. If the follow-up asks whether a "
        "program is activated, judge support from the supplied evidence and the program "
        "direction summary. If it is not supported as an activated program, say the current "
        "evidence does not support that activation. Do not add candidates, change directions, "
        "invent citations, claim clinical efficacy, or upgrade weak, proxy, partial, or no-hit "
        "evidence. Do not mention PxFquery, MCP, backend tools, internal layers, raw JSON, "
        "raw program identifiers, all-caps database IDs, numbered program codes, exact/proxy "
        "labels, route IDs, row counts, numeric scores, or table values. Use readable "
        "biological phrases. Return one valid JSON object with keys: response, cited_tables, "
        "warnings."
    )
    try:
        result, evidence = llm_provider.request_json(
            stage="l5_chat",
            system_prompt=system_prompt,
            user_payload=user_payload,
            temperature=0,
        )
        violations = _presentation_policy_violations(str((result or {}).get("response") or ""))
        if violations:
            repair_payload = {
                "policy_violations": violations,
                "previous_response": str((result or {}).get("response") or ""),
                "instruction": (
                    "Rewrite the response so it satisfies the presentation policy. "
                    "Use the same evidence context and answer the same follow-up. "
                    "Do not remove the scientific conclusion; only change the presentation "
                    "to avoid forbidden internal details."
                ),
                "original_payload": user_payload,
            }
            repaired, repair_evidence = llm_provider.request_json(
                stage="l5_chat_policy_repair",
                system_prompt=system_prompt,
                user_payload=repair_payload,
                temperature=0,
            )
            return repaired, {"initial": evidence, "policy_repair": repair_evidence, "violations": violations}
        return result, evidence
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


def _presentation_policy_violations(text: str) -> list[str]:
    patterns = {
        "raw_program_identifier": r"\bHALLMARK_|(?:\bMP\s*\d+\b)|(?:\bMPS?[_\s-]*\d+\b)",
        "numeric_score_or_table_value": r"\bscore\b|\b\d+\.\d+\b",
        "backend_or_protocol_mention": r"\bPxFquery\b|\bMCP\b|\bJSON\b|\bbackend\b|\btool\b",
        "route_or_row_metadata": r"\broute\b|\brow count\b|\bmatched row\b",
    }
    return [name for name, pattern in patterns.items() if re.search(pattern, text, flags=re.IGNORECASE)]


def _program_direction_context(tables: dict[str, Any]) -> dict[str, list[str]]:
    rows = list((tables or {}).get("ranked_results") or [])
    activated: list[str] = []
    suppressed: list[str] = []
    for row in rows:
        label = _readable_label(str(row.get("label") or row.get("function") or ""))
        if not label:
            continue
        direction = str(row.get("direction") or row.get("kind") or "").lower()
        if "suppress" in direction or "down" in direction:
            suppressed.append(label)
        elif "activ" in direction or "up" in direction:
            activated.append(label)
    return {
        "activated": _dedupe(activated),
        "suppressed": _dedupe(suppressed),
    }


def _evidence_boundary_context(dossier: dict[str, Any]) -> dict[str, Any]:
    matrix = ((dossier or {}).get("evidence_layer") or {}).get("matrix_evidence") or {}
    routes = matrix.get("executed_routes") or []
    contexts = _dedupe([str(route.get("cell") or route.get("context") or "") for route in routes if route.get("cell") or route.get("context")])
    perturbations = _dedupe([str(route.get("perturbation") or route.get("perturbation_label") or "") for route in routes if route.get("perturbation") or route.get("perturbation_label")])
    return {
        "contexts": contexts,
        "perturbations": perturbations,
        "scope": "matrix-backed perturbation functional programs",
    }


def _readable_label(text: str) -> str:
    text = re.sub(r"\bHALLMARK_([A-Z0-9_]+)\b", lambda m: m.group(1).replace("_", " ").title(), text)
    text = re.sub(r"\b(?:3CA_)?MPS?[_\s-]*(\d+)\s*[-_:.)]*\s*", "", text)
    text = re.sub(r"\bMP\s*(\d+)\s*[-_:.)]*\s*", "", text)
    text = text.replace("_", " ")
    return re.sub(r"\s{2,}", " ", text).strip()


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        key = item.casefold()
        if item and key not in seen:
            seen.add(key)
            output.append(item)
    return output
