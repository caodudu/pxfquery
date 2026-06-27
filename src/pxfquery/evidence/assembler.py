from __future__ import annotations

from pxfquery.execution import QueryExecution


def assemble_evidence(execution: QueryExecution) -> dict:
    route_plan = execution.route_plan
    intent = route_plan.intent
    diagnostics = {
        "warnings": [],
        "missing_fields": intent.missing_fields,
        "note": "Natural-language intent was parsed; no resource-backed entity resolution or retrieval was performed.",
    }
    return {
        "schema_version": "2026-06-27",
        "route_status": route_plan.route_status,
        "route_plan": route_plan.to_dict(),
        "intent": intent.to_dict(),
        "query_context": {
            "biological_context": intent.biological_context,
            "context_source": "natural_language_surface",
            "perturbation_type": intent.perturbation_type,
            "direction": intent.direction,
        },
        "perturbation_resolution": {
            "original_query": intent.perturbation_identity,
            "resolved_name": None,
            "resolved_id": None,
            "method": "pending_resource_resolution",
        },
        "function_response": {
            "status": execution.query_status,
            "scores": execution.result["scores"],
            "candidates": execution.result["candidates"],
            "function_terms": [intent.function_target] if intent.function_target else [],
        },
        "evidence_records": [],
        "diagnostics": diagnostics,
        "suggestions": _suggestions(intent, route_plan.route_status),
        "layer_chain": [
            "nlu.parse_query",
            "routing.route_intent",
            "execution.execute_route",
            "evidence.assemble_evidence",
        ],
        "execution_note": execution.execution_note,
    }


def _suggestions(intent, route_status: str) -> list[dict]:
    if route_status == "needs-intent-completion":
        return [
            {
                "type": "missing_field",
                "text": "Complete the missing intent fields before routing to resource-backed evidence.",
                "required_fields": intent.missing_fields,
            }
        ]
    return []
