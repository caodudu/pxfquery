from __future__ import annotations

from typing import Any

from pxfquery.answer import PxFQueryAnswer


def build_answer(question: str, structured: dict[str, Any], *, resources_status: dict[str, Any] | None = None) -> PxFQueryAnswer:
    intent = structured.get("intent", {})
    context = structured.get("query_context", {})
    function_response = structured.get("function_response", {})
    diagnostics = structured.get("diagnostics", {})

    interpreted = _interpreted_question(intent, context)
    biological_results = _biological_results(function_response)
    evidence = _evidence(structured, resources_status)
    limitations = _limitations(structured, resources_status)

    return PxFQueryAnswer(
        question=question,
        interpreted_question=interpreted,
        biological_results=biological_results,
        evidence=evidence,
        biological_interpretation=_interpretation(intent, biological_results),
        limitations=limitations,
        structured_result=structured,
        engineering={
            "diagnostics": diagnostics,
            "route_status": structured.get("route_status"),
            "trace": _trace(structured),
        },
    )


def _interpreted_question(intent: dict[str, Any], context: dict[str, Any]) -> str:
    direction = intent.get("direction") or "query"
    perturbation_type = intent.get("perturbation_type") or "perturbation"
    function = intent.get("function_target") or "functional programs"
    biological_context = intent.get("biological_context") or context.get("cell_line") or "available biological models"
    if direction == "reverse":
        return f"find {perturbation_type} perturbations associated with {function} in {biological_context}"
    perturbation = intent.get("perturbation_identity") or "the requested perturbation"
    return f"estimate functional effects of {perturbation} in {biological_context}"


def _biological_results(function_response: dict[str, Any]) -> list[dict[str, Any]]:
    scores = function_response.get("scores")
    if isinstance(scores, list):
        return [
            {
                "rank": item.get("rank"),
                "id": item.get("pert_id"),
                "label": item.get("cmap_name") or item.get("pert_id"),
                "score": item.get("score"),
                "result_type": "ranked_perturbation",
            }
            for item in scores
        ]
    if isinstance(scores, dict):
        ranked = sorted(scores.items(), key=lambda item: abs(item[1]), reverse=True)
        return [
            {
                "rank": idx + 1,
                "label": key,
                "score": value,
                "result_type": "function_score",
            }
            for idx, (key, value) in enumerate(ranked)
        ]
    return []


def _evidence(structured: dict[str, Any], resources_status: dict[str, Any] | None) -> dict[str, Any]:
    context = structured.get("query_context", {})
    function_response = structured.get("function_response", {})
    diagnostics = structured.get("diagnostics", {})
    evidence = {
        "biological_context": context.get("biological_context") or "not resolved",
        "context_source": context.get("context_source") or "not resolved",
        "perturbation_type": context.get("perturbation_type") or "unknown",
        "direction": context.get("direction") or "unknown",
        "data_source": _readable_data_source(function_response.get("matrix_source")),
    }
    if resources_status:
        evidence["resource_pack"] = resources_status.get("message") or resources_status.get("source")
        evidence["resource_count"] = resources_status.get("asset_count")
    if diagnostics.get("indexes_searched"):
        evidence["matched_indexes"] = ", ".join(diagnostics["indexes_searched"])
    return evidence


def _readable_data_source(matrix_source: str | None) -> str:
    if matrix_source == "resource_pack_pending":
        return "resource-pack query execution pending"
    if matrix_source == "registered_assets":
        return "registered resource pack metadata; no matrix retrieval was produced"
    return matrix_source or "not retrieved"


def _limitations(structured: dict[str, Any], resources_status: dict[str, Any] | None) -> list[str]:
    limitations = [
        "This version exposes the source-layer architecture. Biological hits require later resource-backed routing and query execution.",
    ]
    diagnostics = structured.get("diagnostics", {})
    if diagnostics.get("missing_fields"):
        limitations.append(f"Missing fields: {', '.join(diagnostics['missing_fields'])}.")
    if diagnostics.get("warnings"):
        limitations.extend(str(item) for item in diagnostics["warnings"])
    if resources_status and not resources_status.get("configured"):
        limitations.append("No local PxFquery resource pack is configured yet.")
    return limitations


def _interpretation(intent: dict[str, Any], results: list[dict[str, Any]]) -> str:
    if not results:
        return "PxFquery parsed the question intent, but no biological result is claimed before resource-backed routing and query execution."
    if intent.get("direction") == "reverse":
        return "Ranked perturbations require resource-backed query execution."
    return "The function scores summarize the current estimated functional response for the requested perturbation."


def _trace(structured: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {"layer": "natural_language_understanding", "event": "intent_parsed"},
        {"layer": "evidence_routing", "event": "route_selected", "status": structured.get("route_status")},
        {"layer": "resource_pack_query_execution", "event": "execution_result_available"},
        {"layer": "evidence_assembly", "event": "evidence_payload_built"},
        {"layer": "biological_result_presentation", "event": "answer_built"},
    ]
