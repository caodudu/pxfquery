from __future__ import annotations

from typing import Any

from pxfquery.l3_execution import ForwardResult, ReverseResult


def assemble_evidence(execution: Any) -> dict:
    if isinstance(execution, ForwardResult):
        return _assemble_forward(execution)
    if isinstance(execution, ReverseResult):
        return _assemble_reverse(execution)
    raise TypeError(f"Unsupported execution result type: {type(execution)!r}")


def _assemble_forward(result: ForwardResult) -> dict:
    meta = getattr(result, "resolver_meta", {}) or {}
    activated = _series_records(result.top_activated if result.found else None, "activated_function")
    suppressed = _series_records(result.top_suppressed if result.found else None, "suppressed_function")
    return {
        "schema_version": "2026-06-27",
        "query_type": "forward",
        "route_status": meta.get("hit_level") or ("FOUND" if result.found else "NOT_FOUND"),
        "resolver_meta": meta,
        "query_context": {
            "biological_context": result.cell_line,
            "cells_used": list(getattr(result, "cells_used", [])),
            "perturbation": result.perturbation,
            "n_observations": int(getattr(result, "n_obs", 0)),
        },
        "function_response": {
            "status": "found" if result.found else "not-found",
            "activated": activated,
            "suppressed": suppressed,
            "scores": _scores_dict(result.scores if result.found else None),
            "candidates": [],
        },
        "evidence_records": meta.get("evidence_candidates", []),
        "diagnostics": {
            "note": getattr(result, "note", ""),
            "warnings": [],
            "missing_fields": [],
        },
        "layer_chain": [
            "l1_nlu.parse_query",
            "l2_routing.route_intent",
            "l3_execution.forward_or_reverse_query",
            "l4_evidence.assemble_evidence",
        ],
    }


def _assemble_reverse(result: ReverseResult) -> dict:
    meta = getattr(result, "resolver_meta", {}) or {}
    candidates = result.candidates_df.reset_index(names="rank").to_dict(orient="records") if result.found else []
    return {
        "schema_version": "2026-06-27",
        "query_type": "reverse",
        "route_status": "FOUND" if result.found else "NOT_FOUND",
        "resolver_meta": meta,
        "query_context": {
            "biological_context": result.cell_line,
            "activate": list(result.activate),
            "suppress": list(result.suppress),
        },
        "function_response": {
            "status": "found" if result.found else "not-found",
            "activated": [],
            "suppressed": [],
            "scores": None,
            "candidates": candidates,
        },
        "evidence_records": candidates,
        "diagnostics": {
            "note": getattr(result, "note", ""),
            "warnings": [],
            "missing_fields": [],
        },
        "layer_chain": [
            "l1_nlu.parse_query",
            "l2_routing.route_intent",
            "l3_execution.forward_or_reverse_query",
            "l4_evidence.assemble_evidence",
        ],
    }


def _series_records(series, result_type: str) -> list[dict[str, Any]]:
    if series is None:
        return []
    out = []
    for rank, (name, score) in enumerate(series.items(), 1):
        out.append({"rank": rank, "label": name, "score": float(score), "result_type": result_type})
    return out


def _scores_dict(series) -> dict[str, float] | None:
    if series is None:
        return None
    return {str(name): float(score) for name, score in series.items()}
