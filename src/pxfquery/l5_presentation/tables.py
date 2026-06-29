from __future__ import annotations

from typing import Any


def build_tables(dossier: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    evidence = dossier.get("evidence_layer") or {}
    matrix = evidence.get("matrix_evidence") or {}
    route = evidence.get("route_evidence") or {}
    primary = matrix.get("primary_result") or {}
    return {
        "ranked_results": _ranked_results(matrix),
        "primary_route_ranked_results": _primary_route_ranked_results(matrix),
        "route_summary": _route_summary(route, matrix),
        "route_target_functions": _route_target_functions(matrix),
        "route_function_results": _route_function_results(matrix),
        "matrix_context": _matrix_context(primary),
        "claim_rules": _claim_rules(dossier),
    }


def _ranked_results(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    primary = matrix.get("primary_result") or {}
    if matrix.get("mode") == "reverse":
        return _reverse_candidate_consensus(matrix)
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


def _primary_route_ranked_results(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    primary = matrix.get("primary_result") or {}
    if matrix.get("mode") == "reverse":
        return [_compact_result(item, "primary_route_candidate") for item in primary.get("top_perturbations") or []]
    return []


def _compact_result(item: dict[str, Any], kind: str) -> dict[str, Any]:
    return {
        "rank": item.get("rank"),
        "label": item.get("label") or item.get("name") or item.get("function") or item.get("cmap_name") or item.get("pert_id"),
        "score": item.get("score") if item.get("score") is not None else item.get("value"),
        "direction": item.get("direction"),
        "kind": item.get("kind") or item.get("result_type") or kind,
        "source": item.get("source") or item.get("modality"),
    }


def _reverse_candidate_consensus(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    exact_route_ids = {
        route.get("route_id")
        for route in matrix.get("executed_routes") or []
        if route.get("cell_match_type") == "user_specified_cell"
    }
    for route in matrix.get("executed_routes") or []:
        route_id = route.get("route_id")
        cell = route.get("cell")
        modality = route.get("modality")
        is_exact_route = route_id in exact_route_ids
        for item in route.get("top_perturbations") or []:
            key = _candidate_key(item)
            if not key:
                continue
            score = item.get("score") if item.get("score") is not None else item.get("value")
            try:
                score_value = float(score)
            except (TypeError, ValueError):
                continue
            group = groups.setdefault(
                key,
                {
                    "label": item.get("label") or item.get("cmap_name") or item.get("pert_id") or key,
                    "pert_id": item.get("pert_id"),
                    "cmap_name": item.get("cmap_name"),
                    "recommended_operation": item.get("recommended_operation"),
                    "score_orientation": item.get("score_orientation"),
                    "source": modality,
                    "scores": [],
                    "exact_scores": [],
                    "route_ids": set(),
                    "cells": set(),
                    "best": None,
                    "best_exact": None,
                },
            )
            group["scores"].append(score_value)
            if is_exact_route:
                group["exact_scores"].append(score_value)
            if route_id:
                group["route_ids"].add(route_id)
            if cell:
                group["cells"].add(cell)
            best = group.get("best")
            if best is None or score_value > best["score"]:
                group["best"] = {"score": score_value, "route_id": route_id, "cell": cell}
            best_exact = group.get("best_exact")
            if is_exact_route and (best_exact is None or score_value > best_exact["score"]):
                group["best_exact"] = {"score": score_value, "route_id": route_id, "cell": cell}

    rows: list[dict[str, Any]] = []
    for group in groups.values():
        scores = group["scores"]
        exact_scores = group["exact_scores"]
        best = group.get("best") or {}
        best_exact = group.get("best_exact") or {}
        support_routes = sorted(group["route_ids"])
        support_cells = sorted(group["cells"])
        mean_score = sum(scores) / len(scores)
        exact_mean_score = sum(exact_scores) / len(exact_scores) if exact_scores else None
        rows.append(
            {
                "label": group.get("label"),
                "score": exact_mean_score if exact_mean_score is not None else mean_score,
                "mean_score": mean_score,
                "exact_cell_score": exact_mean_score,
                "best_score": best.get("score"),
                "best_exact_cell_score": best_exact.get("score"),
                "exact_cell_support": bool(exact_scores),
                "support_routes": len(support_routes),
                "support_cells": len(support_cells),
                "route_ids": ", ".join(support_routes),
                "cells": ", ".join(support_cells),
                "best_route_id": best_exact.get("route_id") or best.get("route_id"),
                "best_cell": best_exact.get("cell") or best.get("cell"),
                "pert_id": group.get("pert_id"),
                "cmap_name": group.get("cmap_name"),
                "recommended_operation": group.get("recommended_operation"),
                "score_orientation": group.get("score_orientation"),
                "kind": "candidate_consensus",
                "source": group.get("source"),
            }
        )
    if exact_route_ids:
        rows.sort(
            key=lambda item: (
                not item["exact_cell_support"],
                -(item.get("exact_cell_score") or float("-inf")),
                -item["support_routes"],
                -item["support_cells"],
                -(item.get("mean_score") or 0.0),
                str(item.get("label") or ""),
            )
        )
    else:
        rows.sort(key=lambda item: (-item["support_routes"], -item["support_cells"], -item["score"], -(item.get("best_score") or 0.0), str(item.get("label") or "")))
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def _candidate_key(item: dict[str, Any]) -> str:
    for key in ("pert_id", "cmap_name", "label", "name"):
        value = item.get(key)
        if value is not None and str(value).strip():
            return str(value).strip().lower()
    return ""


def _route_summary(route: dict[str, Any], matrix: dict[str, Any]) -> list[dict[str, Any]]:
    if matrix.get("mode") == "reverse":
        return _executed_route_summary(matrix)
    rows = []
    for item in route.get("selected_routes") or []:
        rows.append(
            {
                "route_id": item.get("route_id"),
                "status": item.get("status") or route.get("status"),
                "cell": item.get("cell") or item.get("matched_cell"),
                "perturbation": item.get("perturbation") or item.get("matched_perturbation"),
                "perturbation_alias": item.get("perturbation_alias") or (item.get("perturbation_record") or {}).get("alias"),
                "tier": item.get("tier") or item.get("evidence_tier"),
                "cell_match_type": item.get("cell_match_type"),
                "perturbation_match_type": item.get("perturbation_match_type"),
                "cell_match_distance": item.get("cell_match_distance"),
                "perturbation_match_distance": item.get("perturbation_match_distance"),
                "route_quality_score": item.get("route_quality_score"),
                "route_quality": item.get("route_quality"),
                "score_orientation": item.get("score_orientation"),
                "recommended_operation": item.get("recommended_operation"),
                "reason": item.get("reason") or item.get("pair_search_reason"),
            }
        )
    for item in matrix.get("executed_routes") or []:
        row = {
            "route_id": item.get("route_id"),
            "status": item.get("status"),
            "cell": item.get("cell"),
            "perturbation": item.get("perturbation"),
            "perturbation_alias": item.get("perturbation_alias"),
            "tier": item.get("tier"),
            "cell_match_type": item.get("cell_match_type"),
            "perturbation_match_type": item.get("perturbation_match_type"),
            "cell_match_distance": item.get("cell_match_distance"),
            "perturbation_match_distance": item.get("perturbation_match_distance"),
            "route_quality_score": item.get("route_quality_score"),
            "route_quality": item.get("route_quality"),
            "score_orientation": item.get("score_orientation"),
            "recommended_operation": item.get("recommended_operation"),
            "reason": item.get("pair_search_reason"),
        }
        if row not in rows:
            rows.append(row)
    return rows


def _executed_route_summary(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    seen: set[str] = set()
    for item in matrix.get("executed_routes") or []:
        route_id = item.get("route_id")
        key = str(route_id) if route_id is not None else repr(sorted(item.items()))
        if key in seen:
            continue
        seen.add(key)
        rows.append(
            {
                "route_id": route_id,
                "status": item.get("status"),
                "cell": item.get("cell"),
                "modality": item.get("modality"),
                "perturbation": item.get("perturbation"),
                "perturbation_alias": item.get("perturbation_alias"),
                "tier": item.get("tier"),
                "cell_match_type": item.get("cell_match_type"),
                "perturbation_match_type": item.get("perturbation_match_type"),
                "cell_match_distance": item.get("cell_match_distance"),
                "perturbation_match_distance": item.get("perturbation_match_distance"),
                "route_quality_score": item.get("route_quality_score"),
                "route_quality": item.get("route_quality"),
                "score_orientation": item.get("score_orientation"),
                "recommended_operation": item.get("recommended_operation"),
                "n_rows": item.get("n_rows"),
                "n_ranked_groups": item.get("n_ranked_groups"),
                "reason": item.get("pair_search_reason"),
            }
        )
    return rows


def _route_function_results(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    if matrix.get("mode") != "forward":
        return []
    rows = []
    for route in matrix.get("executed_routes") or []:
        for direction_key in ("top_activated", "top_suppressed"):
            for item in route.get(direction_key) or []:
                rows.append(
                    {
                        "route_id": route.get("route_id"),
                        "cell": route.get("cell"),
                        "perturbation": route.get("perturbation"),
                        "perturbation_alias": route.get("perturbation_alias"),
                        "modality": route.get("modality"),
                        "score_orientation": route.get("score_orientation"),
                        "recommended_operation": route.get("recommended_operation"),
                        "route_quality_score": route.get("route_quality_score"),
                        "route_quality": route.get("route_quality"),
                        "cell_match_type": route.get("cell_match_type"),
                        "perturbation_match_type": route.get("perturbation_match_type"),
                        "rank": item.get("rank"),
                        "label": item.get("label") or item.get("function"),
                        "function": item.get("function") or item.get("label"),
                        "score": item.get("score"),
                        "direction": item.get("direction") or ("activated" if direction_key == "top_activated" else "suppressed"),
                    }
                )
    return rows


def _route_target_functions(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    if matrix.get("mode") != "reverse":
        return []
    rows = []
    for route in matrix.get("executed_routes") or []:
        target_vector = route.get("target_vector") or {}
        for item in route.get("functions") or []:
            var_name = item.get("var_name")
            rows.append(
                {
                    "route_id": route.get("route_id"),
                    "cell": route.get("cell"),
                    "modality": route.get("modality"),
                    "interpretation_set_id": route.get("interpretation_set_id"),
                    "function_rank": item.get("rank"),
                    "label": item.get("label") or var_name,
                    "var_name": var_name,
                    "source": item.get("source"),
                    "direction": item.get("direction"),
                    "input": item.get("input"),
                    "target_weight": target_vector.get(var_name),
                    "route_quality": route.get("route_quality"),
                    "cell_match_type": route.get("cell_match_type"),
                }
            )
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
