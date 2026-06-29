from __future__ import annotations

from typing import Any


def build_tables(dossier: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    evidence = dossier.get("evidence_layer") or {}
    matrix = evidence.get("matrix_evidence") or {}
    route = evidence.get("route_evidence") or {}
    primary = matrix.get("primary_result") or {}
    return {
        "ranked_results": _ranked_results(matrix),
        "route_summary": _route_summary(route, matrix),
        "matrix_context": _matrix_context(primary),
        "claim_rules": _claim_rules(dossier),
    }


def _ranked_results(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    primary = matrix.get("primary_result") or {}
    if matrix.get("mode") == "reverse":
        return [_compact_result(item, "candidate") for item in primary.get("top_perturbations") or []]
    rows = []
    for item in primary.get("top_activated") or []:
        row = _compact_result(item, "activated_function")
        row.setdefault("direction", "activated")
        rows.append(row)
    for item in primary.get("top_suppressed") or []:
        row = _compact_result(item, "suppressed_function")
        row.setdefault("direction", "suppressed")
        rows.append(row)
    for item in primary.get("requested_function_records") or []:
        row = _compact_result(item, "requested_function")
        if row not in rows:
            rows.append(row)
    return rows


def _compact_result(item: dict[str, Any], kind: str) -> dict[str, Any]:
    return {
        "rank": item.get("rank"),
        "label": item.get("label") or item.get("name") or item.get("function") or item.get("cmap_name") or item.get("pert_id"),
        "score": item.get("score") if item.get("score") is not None else item.get("value"),
        "direction": item.get("direction"),
        "kind": item.get("kind") or item.get("result_type") or kind,
        "source": item.get("source") or item.get("modality"),
    }


def _route_summary(route: dict[str, Any], matrix: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for item in route.get("selected_routes") or []:
        rows.append(
            {
                "route_id": item.get("route_id"),
                "status": item.get("status") or route.get("status"),
                "cell": item.get("cell") or item.get("matched_cell"),
                "perturbation": item.get("perturbation") or item.get("matched_perturbation"),
                "tier": item.get("tier") or item.get("evidence_tier"),
                "reason": item.get("reason") or item.get("pair_search_reason"),
            }
        )
    for item in matrix.get("executed_routes") or []:
        row = {
            "route_id": item.get("route_id"),
            "status": item.get("status"),
            "cell": item.get("cell"),
            "tier": item.get("tier"),
            "reason": item.get("pair_search_reason"),
        }
        if row not in rows:
            rows.append(row)
    return rows


def _matrix_context(primary: dict[str, Any]) -> list[dict[str, Any]]:
    keys = ["cell", "perturbation", "modality", "n_rows", "n_ranked_groups", "ranking_method", "score_orientation"]
    return [{"field": key, "value": primary.get(key)} for key in keys if primary.get(key) is not None]


def _claim_rules(dossier: dict[str, Any]) -> list[dict[str, Any]]:
    basis = dossier.get("claim_basis") or {}
    rows = []
    for item in basis.get("must_mention") or []:
        rows.append({"rule": "must_mention", "text": str(item)})
    for item in basis.get("must_not_claim") or []:
        rows.append({"rule": "must_not_claim", "text": str(item)})
    return rows
