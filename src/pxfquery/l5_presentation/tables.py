from __future__ import annotations

import re
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
    if matrix.get("mode") == "reverse":
        return _reverse_candidate_consensus(matrix)
    return _forward_function_consensus(matrix)


def _forward_function_consensus(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    for route in matrix.get("executed_routes") or []:
        route_id = route.get("route_id")
        cell = route.get("cell")
        route_quality_score = _float_or_none(route.get("route_quality_score"))
        route_quality = route.get("route_quality")
        is_direct_route = _is_direct_forward_route(route)
        for direction_key, default_direction in (("top_activated", "activated"), ("top_suppressed", "suppressed")):
            for item in route.get(direction_key) or []:
                label = item.get("label") or item.get("function")
                if not label:
                    continue
                direction = str(item.get("direction") or default_direction).lower()
                score = _float_or_none(item.get("score"))
                if score is None:
                    continue
                signed_score = _signed_forward_score(score, direction)
                key = _function_key(str(label))
                group = groups.setdefault(
                    key,
                    {
                        "label": str(label),
                        "scores": [],
                        "route_ids": set(),
                        "cells": set(),
                        "direct_route_ids": set(),
                        "activated_route_ids": set(),
                        "suppressed_route_ids": set(),
                        "best_abs_score": 0.0,
                        "best_route_quality_score": None,
                        "best_route_quality": None,
                    },
                )
                group["scores"].append(signed_score)
                if route_id:
                    group["route_ids"].add(str(route_id))
                    if signed_score >= 0:
                        group["activated_route_ids"].add(str(route_id))
                    else:
                        group["suppressed_route_ids"].add(str(route_id))
                    if is_direct_route:
                        group["direct_route_ids"].add(str(route_id))
                if cell:
                    group["cells"].add(str(cell))
                if abs(score) > group["best_abs_score"]:
                    group["best_abs_score"] = abs(score)
                if route_quality_score is not None:
                    best_quality_score = group.get("best_route_quality_score")
                    if best_quality_score is None or route_quality_score < best_quality_score:
                        group["best_route_quality_score"] = route_quality_score
                        group["best_route_quality"] = route_quality

        for item in route.get("requested_function_records") or []:
            label = item.get("label") or item.get("function")
            if not label:
                continue
            key = _function_key(str(label))
            groups.setdefault(
                key,
                {
                    "label": str(label),
                    "scores": [],
                    "route_ids": set(),
                    "cells": set(),
                    "direct_route_ids": set(),
                    "activated_route_ids": set(),
                    "suppressed_route_ids": set(),
                    "best_abs_score": 0.0,
                    "best_route_quality_score": route_quality_score,
                    "best_route_quality": route_quality,
                    "requested": True,
                },
            )

    if not groups:
        return _primary_forward_results(matrix)

    rows: list[dict[str, Any]] = []
    for group in groups.values():
        scores = group.get("scores") or []
        route_ids = sorted(group["route_ids"])
        cells = sorted(group["cells"])
        activated_support = len(group["activated_route_ids"])
        suppressed_support = len(group["suppressed_route_ids"])
        if scores:
            mean_signed_score = sum(scores) / len(scores)
            mean_abs_score = sum(abs(value) for value in scores) / len(scores)
        else:
            mean_signed_score = 0.0
            mean_abs_score = 0.0
        if activated_support > suppressed_support:
            direction = "activated"
        elif suppressed_support > activated_support:
            direction = "suppressed"
        elif mean_signed_score > 0:
            direction = "activated"
        elif mean_signed_score < 0:
            direction = "suppressed"
        else:
            direction = "mixed"
        rows.append(
            {
                "label": group.get("label"),
                "score": mean_signed_score,
                "mean_score": mean_signed_score,
                "mean_abs_score": mean_abs_score,
                "best_abs_score": group.get("best_abs_score"),
                "direction": direction,
                "kind": "function_consensus",
                "source": "matched_evidence",
                "support_routes": len(route_ids),
                "support_cells": len(cells),
                "route_ids": ", ".join(route_ids),
                "cells": ", ".join(cells),
                "direct_route_support": bool(group["direct_route_ids"]),
                "direct_support_routes": len(group["direct_route_ids"]),
                "activated_support_routes": activated_support,
                "suppressed_support_routes": suppressed_support,
                "direction_consistent": not (activated_support and suppressed_support),
                "best_route_quality_score": group.get("best_route_quality_score"),
                "best_route_quality": group.get("best_route_quality"),
            }
        )
    has_direct_support = any(item["direct_support_routes"] for item in rows)
    if has_direct_support:
        rows.sort(
            key=lambda item: (
                -item["direct_support_routes"],
                -item["support_routes"],
                -item["support_cells"],
                not item["direction_consistent"],
                -(item.get("mean_abs_score") or 0.0),
                -(item.get("best_abs_score") or 0.0),
                str(item.get("label") or ""),
            )
        )
    else:
        rows.sort(
            key=lambda item: (
                -item["support_routes"],
                -item["support_cells"],
                not item["direction_consistent"],
                -(item.get("mean_abs_score") or 0.0),
                -(item.get("best_abs_score") or 0.0),
                str(item.get("label") or ""),
            )
        )
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def _primary_forward_results(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    primary = matrix.get("primary_result") or {}
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


def _signed_forward_score(score: float, direction: str) -> float:
    normalized = str(direction or "").strip().casefold().replace("-", "_")
    activated = {
        "activated",
        "activation",
        "activate",
        "up",
        "upregulated",
        "up_regulated",
        "positive",
    }
    suppressed = {
        "suppressed",
        "suppression",
        "suppress",
        "down",
        "downregulated",
        "down_regulated",
        "negative",
    }
    if normalized in activated:
        return abs(score)
    if normalized in suppressed:
        return -abs(score)
    return abs(score) if score >= 0 else -abs(score)


def _primary_route_ranked_results(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    primary = matrix.get("primary_result") or {}
    if matrix.get("mode") == "reverse":
        modality = primary.get("modality")
        return [_compact_result(item, "primary_route_candidate") for item in primary.get("top_perturbations") or [] if not _unreadable_reverse_candidate(item, modality=modality)]
    return _primary_forward_results(matrix)


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
            if _unreadable_reverse_candidate(item, modality=modality):
                continue
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
                    "label": _display_reverse_candidate_label(item.get("label") or item.get("cmap_name") or item.get("pert_id") or key, modality=modality),
                    "raw_identifier": (item.get("label") or item.get("cmap_name") or item.get("pert_id") or key) if _raw_candidate_identifier(item.get("label") or item.get("cmap_name") or item.get("pert_id") or key) else None,
                    "annotation_status": "alias_missing" if modality == "cp" and _raw_candidate_identifier(item.get("label") or item.get("cmap_name") or item.get("pert_id") or key) else "not_required",
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
                "raw_identifier": group.get("raw_identifier"),
                "annotation_status": group.get("annotation_status"),
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
    _mark_reverse_candidate_groups(rows)
    for rank, row in enumerate(rows, start=1):
        row["rank"] = rank
    return rows


def _mark_reverse_candidate_groups(rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    top_score = _float_or_none(rows[0].get("score"))
    if top_score is None:
        return
    leading_count = 0
    for row in rows:
        score = _float_or_none(row.get("score"))
        if score is None:
            break
        if score == top_score or abs(score - top_score) <= max(0.5, abs(top_score) * 0.05):
            leading_count += 1
        else:
            break
        if leading_count >= 5:
            break
    if leading_count < 3:
        leading_count = min(3, len(rows))
    for index, row in enumerate(rows):
        row["candidate_group"] = "leading_tied_group" if index < leading_count else "lower_ranked_support"


def _candidate_key(item: dict[str, Any]) -> str:
    for key in ("pert_id", "cmap_name", "label", "name"):
        value = item.get(key)
        if value is not None and str(value).strip():
            return str(value).strip().lower()
    return ""


def _function_key(label: str) -> str:
    return re.sub(r"\s+", " ", str(label).replace("_", " ").strip()).casefold()


def _float_or_none(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _is_direct_forward_route(route: dict[str, Any]) -> bool:
    cell_match = str(route.get("cell_match_type") or route.get("cell_role") or "").casefold()
    pert_match = str(route.get("perturbation_match_type") or route.get("perturbation_role") or "").casefold()
    cell_distance = _float_or_none(route.get("cell_match_distance"))
    pert_distance = _float_or_none(route.get("perturbation_match_distance"))
    cell_direct = "user_specified" in cell_match or "exact" in cell_match or cell_distance == 0.0
    pert_direct = "user_specified" in pert_match or "exact" in pert_match or "mechanism" in pert_match or pert_distance == 0.0
    return bool(cell_direct and pert_direct)


def _unreadable_reverse_candidate(item: dict[str, Any], *, modality: str | None) -> bool:
    label = str(item.get("label") or item.get("cmap_name") or item.get("pert_id") or "").strip()
    if modality in {"sh", "xpr"} and re.fullmatch(r"BRDN\d+", label):
        return True
    if modality in {"sh", "xpr"} and not _looks_like_gene_symbol(label):
        return True
    return False


def _looks_like_gene_symbol(value: Any) -> bool:
    text = str(value or "").strip()
    if not text:
        return False
    return bool(re.fullmatch(r"[A-Z][A-Z0-9-]{1,14}", text))


def _display_reverse_candidate_label(value: Any, *, modality: str | None) -> str:
    label = str(value or "").strip()
    if modality == "cp" and _raw_candidate_identifier(label):
        return "Unnamed compound"
    return label


def _raw_candidate_identifier(value: Any) -> bool:
    text = str(value or "").strip()
    return bool(re.fullmatch(r"BRD-[A-Z][A-Z0-9-]*", text, flags=re.IGNORECASE) or re.fullmatch(r"BRDN\d+", text, flags=re.IGNORECASE))


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
