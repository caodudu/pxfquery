from __future__ import annotations

import json
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
    response_mode: str = "natural",
) -> dict[str, Any]:
    if llm_provider is None:
        raise RuntimeError("pxf.tl.chat requires a configured PxFquery LLM provider; local template fallback is disabled.")
    if not hasattr(llm_provider, "request_json"):
        raise TypeError("pxf.tl.chat requires the configured LLM provider to expose request_json(...)")
    if response_mode not in {"natural", "json"}:
        raise ValueError("response_mode must be 'natural' or 'json'")

    current_answer = answer or build_answer(question, dossier, mode="python")
    llm_safe_dossier = _strip_llm_hidden_fields(dossier)
    structured_direction_options = _structured_direction_options(current_answer.tables)
    user_payload = {
        "original_question": question,
        "user_message": message,
        "structured_json_contract": {
            "applies_when_response_mode_is_json": True,
            "allowed_activated": structured_direction_options.get("allowed_activated", []),
            "allowed_suppressed": structured_direction_options.get("allowed_suppressed", []),
            "requested_exact_count": _requested_exact_count(message),
            "direction_rule": (
                "For JSON fields named activated and suppressed, activated values must be "
                "selected only from allowed_activated and suppressed values must be selected "
                "only from allowed_suppressed."
            ),
        },
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
            "structured_direction_options": structured_direction_options,
            "tables": current_answer.tables,
            "figures": current_answer.figures,
            "rendering_contract": current_answer.rendering_contract,
        },
        "evidence_boundary": _evidence_boundary_context(llm_safe_dossier),
        "l4_evidence": llm_safe_dossier,
        "history": history or [],
    }
    if response_mode == "json":
        result, provider_evidence = _request_structured_json(llm_provider, user_payload)
        if not isinstance(result, dict):
            raise RuntimeError("pxf.tl.chat json provider returned non-object JSON")
        assistant = json.dumps(result, ensure_ascii=False, sort_keys=True)
        return {
            "user": message,
            "assistant": assistant,
            "response_mode": response_mode,
            "json": result,
            "cited_tables": [str(item) for item in result.get("cited_tables", [])] if isinstance(result.get("cited_tables"), list) else [],
            "warnings": [str(item) for item in result.get("warnings", [])] if isinstance(result.get("warnings"), list) else [],
            "provider_evidence": provider_evidence,
        }

    result, provider_evidence = _request_chat_json(llm_provider, user_payload)
    if not isinstance(result, dict):
        raise RuntimeError("pxf.tl.chat provider returned non-object JSON")
    return {
        "user": message,
        "assistant": str(result.get("response") or ""),
        "response_mode": response_mode,
        "cited_tables": [str(item) for item in result.get("cited_tables", [])],
        "warnings": [str(item) for item in result.get("warnings", [])],
        "provider_evidence": provider_evidence,
    }


def _request_chat_json(llm_provider: Any, user_payload: dict[str, Any]) -> tuple[Any, dict[str, Any]]:
    system_prompt = (
        "You answer a follow-up question for a researcher-facing biomedical result. "
        "Use the complete supplied evidence context, including tables and evidence, but "
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
                "The previous chat response could not be parsed as valid JSON. "
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


def _request_structured_json(llm_provider: Any, user_payload: dict[str, Any]) -> tuple[Any, dict[str, Any]]:
    system_prompt = (
        "You are filling a structured JSON answer for PxFquery. Use only the supplied "
        "current_answer, tables, and supplied evidence. The user's follow-up message defines "
        "the exact JSON schema and allowed candidates. Return exactly one valid JSON "
        "object that follows that schema. In this JSON mode, raw JSON, exact "
        "function identifiers, option IDs, route-derived candidates, and table-derived "
        "candidate labels are allowed when requested by the user. Do not use "
        "outside biomedical knowledge. Do not add candidates that are not in the supplied "
        "allowed values. Do not include scores, prose, markdown, or explanatory fields "
        "unless the user explicitly requests those keys. If current_answer contains "
        "structured_direction_options and the requested JSON has activated and suppressed "
        "arrays, the top-level structured_json_contract is mandatory: activated entries "
        "must come only from structured_json_contract.allowed_activated, suppressed entries "
        "must come only from structured_json_contract.allowed_suppressed, and table "
        "direction overrides natural-language summaries when they disagree. Satisfy this "
        "contract in the first response; repair is only for malformed or invalid output."
    )
    try:
        result, evidence = llm_provider.request_json(
            stage="l5_chat_json",
            system_prompt=system_prompt,
            user_payload=user_payload,
            temperature=0,
        )
    except Exception as first_error:
        repair_payload = {
            "previous_error": f"{type(first_error).__name__}: {first_error}",
            "instruction": (
                "Return exactly one valid JSON object. Follow the user's "
                "schema and allowed values. Do not include markdown or prose. "
                "If current_answer contains structured_direction_options and the requested "
                "JSON has activated and suppressed arrays, activated entries must come "
                "from allowed_activated and suppressed entries must come from "
                "allowed_suppressed."
            ),
            "original_payload": user_payload,
        }
        result, evidence = llm_provider.request_json(
            stage="l5_chat_json_repair",
            system_prompt=system_prompt,
            user_payload=repair_payload,
            temperature=0,
        )
        evidence = {"initial_error": f"{type(first_error).__name__}: {first_error}", "repair": evidence}

    normalized = _normalize_structured_direction_result(result, user_payload)
    violations = _structured_direction_violations(normalized, user_payload)
    if not violations:
        if normalized is not result:
            evidence = {**evidence, "structured_direction_validation": {"status": "passed_after_normalization"}}
        else:
            evidence = {**evidence, "structured_direction_validation": {"status": "passed"}}
        return normalized, evidence

    repair_context = _structured_direction_repair_context(user_payload)
    repair_payload = {
        "previous_response": result,
        "normalized_previous_response": normalized,
        "violations": violations,
        "allowed_activated": repair_context.get("allowed_activated"),
        "allowed_suppressed": repair_context.get("allowed_suppressed"),
        "requested_exact_count": repair_context.get("requested_exact_count"),
        "instruction": (
            "Repair the JSON object only. Keep the same schema and query_id. "
            "Do not add prose, markdown, scores, ranks, or extra keys. "
            "Use activated entries only from allowed_activated. "
            "Use suppressed entries only from allowed_suppressed. "
            "Return exactly requested_exact_count activated entries and exactly "
            "requested_exact_count suppressed entries when requested_exact_count is not null."
        ),
        "original_payload": user_payload,
    }
    repaired, repair_evidence = llm_provider.request_json(
        stage="l5_chat_json_direction_repair",
        system_prompt=system_prompt,
        user_payload=repair_payload,
        temperature=0,
    )
    normalized_repaired = _normalize_structured_direction_result(repaired, user_payload)
    repaired_violations = _structured_direction_violations(normalized_repaired, user_payload)
    if repaired_violations:
        raise RuntimeError(f"structured JSON direction validation failed after repair: {repaired_violations}")
    return normalized_repaired, {
        **evidence,
        "structured_direction_validation": {
            "status": "repaired_by_llm",
            "initial_violations": violations,
            "repair_evidence": repair_evidence,
        },
    }


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


def _structured_direction_options(tables: dict[str, Any]) -> dict[str, list[str]]:
    rows = list((tables or {}).get("ranked_results") or [])
    activated: list[str] = []
    suppressed: list[str] = []
    for row in rows:
        label = str(row.get("label") or row.get("function") or "").strip()
        if not label:
            continue
        direction = str(row.get("direction") or row.get("kind") or "").lower()
        if "suppress" in direction or "down" in direction:
            suppressed.append(label)
        elif "activ" in direction or "up" in direction:
            activated.append(label)
    return {
        "allowed_activated": _dedupe(activated),
        "allowed_suppressed": _dedupe(suppressed),
    }


def _normalize_structured_direction_result(result: Any, user_payload: dict[str, Any]) -> Any:
    if not isinstance(result, dict):
        return result
    if not isinstance(result.get("activated"), list) or not isinstance(result.get("suppressed"), list):
        return result

    current_answer = user_payload.get("current_answer") or {}
    options = current_answer.get("structured_direction_options") or {}
    canonical: dict[str, str] = {}
    for item in list(options.get("allowed_activated") or []) + list(options.get("allowed_suppressed") or []):
        text = str(item).strip()
        if text:
            canonical.setdefault(_structured_value_key(text), text)
    if not canonical:
        return result

    changed = False
    normalized = dict(result)
    for field in ("activated", "suppressed"):
        values: list[Any] = []
        for item in result.get(field) or []:
            if not isinstance(item, str):
                values.append(item)
                continue
            key = _structured_value_key(item)
            value = canonical.get(key, item.strip())
            if value != item:
                changed = True
            values.append(value)
        normalized[field] = values
    return normalized if changed else result


def _structured_direction_violations(result: Any, user_payload: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(result, dict):
        return []
    if not isinstance(result.get("activated"), list) or not isinstance(result.get("suppressed"), list):
        return []

    current_answer = user_payload.get("current_answer") or {}
    options = current_answer.get("structured_direction_options") or {}
    allowed_activated = {_structured_value_key(str(item)) for item in options.get("allowed_activated") or []}
    allowed_suppressed = {_structured_value_key(str(item)) for item in options.get("allowed_suppressed") or []}
    if not allowed_activated or not allowed_suppressed:
        return []

    violations: list[dict[str, Any]] = []
    for item in result.get("activated") or []:
        key = _structured_value_key(str(item))
        if key not in allowed_activated:
            violations.append({"field": "activated", "item": str(item), "allowed_field": "allowed_activated"})
    for item in result.get("suppressed") or []:
        key = _structured_value_key(str(item))
        if key not in allowed_suppressed:
            violations.append({"field": "suppressed", "item": str(item), "allowed_field": "allowed_suppressed"})
    return violations


def _structured_direction_repair_context(user_payload: dict[str, Any]) -> dict[str, Any]:
    current_answer = user_payload.get("current_answer") or {}
    options = current_answer.get("structured_direction_options") or {}
    return {
        "allowed_activated": [str(item) for item in options.get("allowed_activated") or []],
        "allowed_suppressed": [str(item) for item in options.get("allowed_suppressed") or []],
        "requested_exact_count": _requested_exact_count(str(user_payload.get("user_message") or "")),
    }


def _requested_exact_count(text: str) -> int | None:
    matches = re.findall(r"exactly\s+(\d+)", text, flags=re.IGNORECASE)
    if not matches:
        return None
    return int(matches[0])


def _structured_value_key(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "").strip()).casefold()


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


def _strip_llm_hidden_fields(value: Any) -> Any:
    hidden = {"proxy_direction_calibration", "proxy_direction_calibrations"}
    if isinstance(value, dict):
        return {key: _strip_llm_hidden_fields(item) for key, item in value.items() if key not in hidden}
    if isinstance(value, list):
        return [_strip_llm_hidden_fields(item) for item in value]
    if isinstance(value, tuple):
        return [_strip_llm_hidden_fields(item) for item in value]
    return value
