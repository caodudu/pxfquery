from __future__ import annotations

import html
import json
import os
import re
from pathlib import Path
from typing import Any

from pxfquery.l5_presentation.tables import build_tables


def build_figure_specs(dossier: dict[str, Any], *, max_items: int = 12, include_svg: bool = False) -> list[dict[str, Any]]:
    if include_svg:
        raise ValueError("SVG figures are not part of the accepted L5 figure surface; use PDF or PNG export.")
    tables = build_tables(dossier)
    ranked = tables["ranked_results"][:max_items]
    routes = tables["route_summary"]
    route_functions = tables.get("route_function_results", [])
    target_functions = tables.get("route_target_functions", [])
    query_type = str(dossier.get("query_type") or (dossier.get("evidence_layer") or {}).get("intent_evidence", {}).get("query_type") or "")
    matrix = (dossier.get("evidence_layer") or {}).get("matrix_evidence") or {}
    specs = []
    if routes and query_type != "reverse":
        specs.append(_route_evidence_map_spec(routes, query_type=query_type, dossier=dossier))
        route_graph = _forward_route_graph_spec(routes, ranked, matrix)
        if route_graph:
            specs.append(route_graph)
    if query_type == "reverse":
        if target_functions:
            specs.extend(_reverse_function_ring_heatmap_specs(target_functions))
        if ranked:
            specs.append(_reverse_candidate_bubble_spec(ranked))
    else:
        if route_functions:
            heatmap = _function_route_heatmap_spec(route_functions, ranked, max_items=max_items)
            specs.append(heatmap)
            specs.append(_function_consensus_bar_spec(route_functions, heatmap.get("rows", [])))
        elif ranked:
            specs.append(_program_direction_summary_spec(ranked))
    return specs


def write_figure_files(
    specs: list[dict[str, Any]],
    output_dir: str | Path,
    *,
    prefix: str = "pxfquery",
    fmt: str = "pdf",
    dpi: int = 160,
) -> list[str]:
    if not specs:
        raise ValueError("L5 cannot write figures because L4 supplied no figure-ready evidence values.")
    fmt = fmt.lower().lstrip(".")
    if fmt not in {"pdf", "png"}:
        raise ValueError("figure format must be 'pdf' or 'png'")
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    paths = []
    for idx, spec in enumerate(specs, start=1):
        safe_kind = _safe_name(str(spec.get("kind") or "figure"))
        path = target / f"{prefix}_{idx:02d}_{safe_kind}.{fmt}"
        fig = render_figure_matplotlib(spec)
        fig.savefig(path, dpi=dpi, bbox_inches="tight")
        _close_matplotlib_figure(fig)
        paths.append(str(path))
    return paths


def render_figure_matplotlib(spec: dict[str, Any]):
    kind = spec.get("kind")
    if kind in {"evidence_match_map", "route_evidence_map"}:
        return _render_route_evidence_map_matplotlib(spec)
    if kind == "forward_route_graph":
        return _render_forward_route_graph_matplotlib(spec)
    if kind in {"function_match_heatmap", "function_route_heatmap"}:
        return _render_function_route_heatmap_matplotlib(spec)
    if kind == "program_direction_summary":
        return _render_program_direction_summary_matplotlib(spec)
    if kind == "function_consensus_bar":
        return _render_function_consensus_bar_matplotlib(spec)
    if kind == "reverse_candidate_support":
        return _render_reverse_candidate_support_matplotlib(spec)
    if kind == "target_function_map":
        return _render_target_function_map_matplotlib(spec)
    if kind == "reverse_function_ring_heatmap":
        return _render_reverse_function_ring_heatmap_matplotlib(spec)
    if kind == "reverse_candidate_bubble":
        return _render_reverse_candidate_bubble_matplotlib(spec)
    if kind == "reverse_candidate_support_bar":
        return _render_reverse_candidate_support_bar_matplotlib(spec)
    if kind == "bar":
        return _render_bar_matplotlib(spec)
    if kind == "bubble":
        return _render_bubble_matplotlib(spec)
    if kind == "heatmap":
        return _render_heatmap_matplotlib(spec)
    if kind == "route_flow":
        return _render_route_flow_matplotlib(spec)
    if kind == "evidence_panel":
        return _render_evidence_panel_matplotlib(spec)
    raise ValueError(f"unsupported figure kind: {kind}")


def render_figure_svg(spec: dict[str, Any], *, width: int = 860) -> str:
    raise ValueError("SVG figures are not part of the accepted L5 figure surface; use PDF or PNG export.")
    kind = spec.get("kind")
    if kind == "route_evidence_map":
        return _render_route_evidence_map_svg(spec, width=width)
    if kind == "function_route_heatmap":
        return _render_function_route_heatmap_svg(spec, width=width)
    if kind == "program_direction_summary":
        return _render_program_direction_summary_svg(spec, width=width)
    if kind == "function_consensus_bar":
        return _render_function_consensus_bar_svg(spec, width=width)
    if kind == "reverse_candidate_support":
        return _render_reverse_candidate_support_svg(spec, width=width)
    if kind == "target_function_map":
        return _render_target_function_map_svg(spec, width=width)
    if kind == "reverse_candidate_support_bar":
        return _render_reverse_candidate_support_bar_svg(spec, width=width)
    if kind == "bar":
        return _render_bar_svg(spec, width=width)
    if kind == "bubble":
        return _render_bubble_svg(spec, width=width)
    if kind == "heatmap":
        return _render_heatmap_svg(spec, width=width)
    if kind == "route_flow":
        return _render_route_flow_svg(spec, width=width)
    if kind == "evidence_panel":
        return _render_evidence_panel_svg(spec, width=width)
    raise ValueError(f"unsupported figure kind: {kind}")


def _route_evidence_map_spec(routes: list[dict[str, Any]], *, query_type: str, dossier: dict[str, Any]) -> dict[str, Any]:
    points = []
    seen = set()
    route_pool = routes
    executed_routes = [route for route in routes if str(route.get("status") or "") == "executed"]
    if executed_routes:
        route_pool = executed_routes
    for route in route_pool:
        route_id = str(route.get("route_id") or "")
        status = str(route.get("status") or "")
        key = (route_id, status)
        if key in seen or (query_type == "reverse" and status and status != "executed"):
            continue
        seen.add(key)
        cell_distance = _numeric(route.get("cell_match_distance"))
        pert_distance = _numeric(route.get("perturbation_match_distance"))
        route_quality_score = _numeric(route.get("route_quality_score"))
        if query_type == "reverse" and route.get("perturbation_match_distance") is None:
            y_value = route_quality_score
            y_label = "route quality distance"
        else:
            y_value = pert_distance
            y_label = "perturbation distance"
        display_id = f"R{len(points) + 1}"
        points.append(
            {
                "display_id": display_id,
                "route_id": route_id,
                "cell": _plot_label(str(route.get("cell") or ""), "Cell"),
                "perturbation": _plot_label(str(route.get("perturbation") or route.get("perturbation_alias") or route.get("modality") or ""), "Perturbation"),
                "cell_distance": cell_distance,
                "y_value": y_value,
                "route_quality_score": route_quality_score,
                "route_quality": str(route.get("route_quality") or ""),
                "cell_match_type": str(route.get("cell_match_type") or ""),
                "perturbation_match_type": str(route.get("perturbation_match_type") or ""),
                "status": status,
                "n_rows": _numeric(route.get("n_rows")),
            }
        )
    perturbations = [point["perturbation"] for point in points if point.get("perturbation")]
    common_perturbation = perturbations[0] if perturbations and len(set(perturbations)) == 1 else ""
    intent = (dossier.get("evidence_layer") or {}).get("intent_evidence") or {}
    query_context = str(intent.get("bio_context") or "").strip()
    query_perturbation = str(intent.get("pert_desc") or intent.get("function_desc") or "").strip()
    query_label = "Query"
    if (query_context or query_perturbation) and not (_has_non_ascii(query_context) or _has_non_ascii(query_perturbation)):
        parts = [part for part in (query_context, query_perturbation) if part]
        query_label = f"Query({'; '.join(parts)})"
    return {
        "kind": "evidence_match_map",
        "title": "Evidence Match Map",
        "query_type": query_type or "unknown",
        "query_context": query_context,
        "query_perturbation": query_perturbation,
        "query_label": query_label,
        "x_label": "Cell Distance",
        "y_label": _title_label(y_label if points else "perturbation distance"),
        "points": points[:16],
        "common_perturbation": common_perturbation,
        "caption": "Each point is an executed evidence match; closer to the origin means better-matched context and perturbation evidence.",
    }


def _function_route_heatmap_spec(route_rows: list[dict[str, Any]], ranked: list[dict[str, Any]], *, max_items: int) -> dict[str, Any]:
    summaries = _function_summaries(route_rows)
    consensus = [item for item in summaries if item["route_count"] >= 2]
    pool = consensus or summaries
    selected = sorted(pool, key=lambda item: (-item["route_count"], -abs(item["mean_score"]), item["label"]))[: min(max_items, 12)]
    top_functions = [item["label"] for item in selected]
    if not top_functions:
        for row in ranked:
            label = str(row.get("label") or "")
            if label and label not in top_functions:
                top_functions.append(label)
            if len(top_functions) >= min(max_items, 10):
                break
    routes = []
    route_labels = []
    route_label_map: dict[str, str] = {}
    for row in route_rows:
        route_id = str(row.get("route_id") or "")
        if route_id and route_id not in routes:
            routes.append(route_id)
            cell = row.get("cell")
            pert = row.get("perturbation")
            label = _short_route_label(_plot_label(str(cell or route_id), "Cell"), _plot_label(str(pert or ""), "Perturbation"))
            if label in route_label_map.values():
                label = f"{label}-{len(routes)}"
            route_label_map[route_id] = label
            route_labels.append(label)
        if len(routes) >= 8:
            break
    values = []
    for function in top_functions:
        row_values = []
        for route_id in routes:
            matches = [item for item in route_rows if str(item.get("route_id") or "") == route_id and str(item.get("function") or "") == function]
            row_values.append(_numeric(matches[0].get("score")) if matches else 0.0)
        values.append(row_values)
    row_order, col_order, ordering_method = _cluster_orders(values)
    top_functions = [top_functions[i] for i in row_order]
    route_labels = [route_labels[i] for i in col_order]
    values = [[values[i][j] for j in col_order] for i in row_order]
    return {
        "kind": "function_match_heatmap",
        "title": "Functional Signal Clustered By Evidence Match",
        "rows": [_plot_label(label, "Function") for label in top_functions],
        "columns": [_plot_label(label, "Match") for label in route_labels],
        "values": values,
        "ordering": ordering_method,
        "caption": "Rows are selected consensus functional programs; columns are executed evidence matches. Hierarchical clustering groups similar match/function patterns when available.",
    }


def _forward_route_graph_spec(routes: list[dict[str, Any]], ranked: list[dict[str, Any]], matrix: dict[str, Any]) -> dict[str, Any] | None:
    if str(matrix.get("mode") or "").lower() == "reverse":
        return None
    selected_functions = _top_directional_functions(ranked, per_direction=3)
    if not selected_functions:
        return None
    selected_keys = {_function_match_key(item): item for item in selected_functions}
    selected_lookup = {_function_match_key(item): item for item in selected_functions}

    route_lookup = {str(route.get("route_id") or ""): route for route in routes if route.get("route_id")}
    raw_routes = matrix.get("raw_route_results") or []
    raw_lookup = {str(route.get("route_id") or ""): route for route in raw_routes if route.get("route_id")}
    route_nodes: list[dict[str, Any]] = []
    function_edges: list[dict[str, Any]] = []
    seen_routes: set[str] = set()

    for route in routes:
        if str(route.get("status") or "") != "executed":
            continue
        route_id = str(route.get("route_id") or "")
        if not route_id or route_id in seen_routes:
            continue
        seen_routes.add(route_id)
        raw_route = raw_lookup.get(route_id) or {}
        metadata = raw_route.get("route_metadata") or {}
        cell = str(route.get("cell") or raw_route.get("cell") or metadata.get("cell") or "").strip()
        perturbation = str(
            route.get("perturbation")
            or route.get("perturbation_alias")
            or metadata.get("perturbation")
            or ((metadata.get("perturbation_record") or {}).get("alias"))
            or raw_route.get("perturbation")
            or ""
        ).strip()
        if not cell or not perturbation:
            continue
        route_nodes.append(
            {
                "route_id": route_id,
                "cell": _plot_label(cell, "Cell"),
                "perturbation": _plot_label(perturbation, "Perturbation"),
                "cell_match_type": str(route.get("cell_match_type") or metadata.get("cell_match_type") or ""),
                "perturbation_match_type": str(route.get("perturbation_match_type") or metadata.get("perturbation_match_type") or ""),
            }
        )
        aggregate = ((raw_route.get("scores") or {}).get("aggregate") or {}) if raw_route else {}
        for function_id, score in aggregate.items():
            key = _function_match_key(str(function_id))
            if key not in selected_keys:
                continue
            score_value = _numeric(score)
            if abs(score_value) <= 1e-12:
                continue
            function_edges.append(
                {
                    "route_id": route_id,
                    "cell": _plot_label(cell, "Cell"),
                    "perturbation": _plot_label(perturbation, "Perturbation"),
                    "function": selected_lookup[key],
                    "score": score_value,
                    "direction": "activated" if score_value > 0 else "suppressed",
                }
            )

    if not route_nodes or not function_edges:
        return None
    function_scores = {str(row.get("label") or ""): _numeric(row.get("score")) for row in ranked}
    return {
        "kind": "forward_route_graph",
        "title": "Evidence Match Network",
        "cells": _dedupe_values([item["cell"] for item in route_nodes]),
        "perturbations": _dedupe_values([item["perturbation"] for item in route_nodes]),
        "functions": [_plot_label(item, "Function") for item in selected_functions],
        "routes": route_nodes,
        "function_edges": function_edges,
        "function_scores": function_scores,
        "caption": "Layered view of matched cell contexts, perturbation evidence, and consensus functional programs.",
    }


def _top_directional_functions(ranked: list[dict[str, Any]], *, per_direction: int) -> list[str]:
    activated: list[tuple[float, str]] = []
    suppressed: list[tuple[float, str]] = []
    for row in ranked:
        label = str(row.get("label") or row.get("function") or "").strip()
        if not label:
            continue
        score = _numeric(row.get("score"))
        direction = str(row.get("direction") or row.get("kind") or "").lower()
        if "suppress" in direction or "down" in direction or score < 0:
            suppressed.append((score, label))
        elif "activ" in direction or "up" in direction or score > 0:
            activated.append((score, label))
    activated = sorted(activated, key=lambda item: (-item[0], item[1]))[:per_direction]
    suppressed = sorted(suppressed, key=lambda item: (item[0], item[1]))[:per_direction]
    return _dedupe_values([label for _, label in activated + suppressed])


def _function_match_key(value: str) -> str:
    text = str(value or "").strip().casefold()
    text = re.sub(r"\s+", " ", text)
    return text


def _dedupe_values(values: list[Any]) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for value in values:
        text = str(value or "").strip()
        key = text.casefold()
        if text and key not in seen:
            seen.add(key)
            output.append(text)
    return output


def _function_consensus_bar_spec(route_rows: list[dict[str, Any]], ordered_functions: list[str]) -> dict[str, Any]:
    summaries = _function_summaries(route_rows)
    by_label = {item["label"]: item for item in summaries}
    ordered = [by_label[label] for label in ordered_functions if label in by_label]
    if not ordered:
        ordered = summaries
    ordered = sorted(ordered, key=lambda item: (-item["route_count"], item["dominant_direction"], -abs(item["mean_score"]), item["label"]))
    return {
        "kind": "function_consensus_bar",
        "title": "Functional Program Evidence Support",
        "items": ordered[:12],
        "caption": "Bar length is the number of evidence matches where the program appears in top activated or suppressed results.",
    }


def _program_direction_summary_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "kind": "program_direction_summary",
        "title": "Functional program direction summary",
        "items": [
            {
                "label": str(item.get("label") or "program"),
                "score": _numeric(item.get("score")),
                "direction": str(item.get("direction") or item.get("kind") or ""),
            }
            for item in rows[:12]
        ],
        "caption": "Top functional programs from the selected matrix evidence, grouped by activation or suppression direction.",
    }


def _reverse_candidate_support_spec(rows: list[dict[str, Any]], matrix: dict[str, Any]) -> dict[str, Any]:
    selected = rows[:12]
    candidate_keys = [_candidate_key_from_label(item) for item in selected]
    routes = []
    route_keys = []
    for route in matrix.get("executed_routes") or []:
        route_id = str(route.get("route_id") or "")
        if not route_id:
            continue
        cell = str(route.get("cell") or "")
        modality = str(route.get("modality") or "")
        label = _short_route_label(_plot_label(cell or route_id, "Cell"), _plot_label(modality, "Modality"))
        if label in route_keys:
            label = f"{label}-{len(route_keys) + 1}"
        routes.append(route)
        route_keys.append(label)
        if len(routes) >= 10:
            break
    values = []
    for candidate, key in zip(selected, candidate_keys):
        row_values = []
        for route in routes:
            match_score = 0.0
            for item in route.get("top_perturbations") or []:
                if _candidate_key_from_label(item) == key:
                    match_score = max(match_score, _numeric(item.get("score") if item.get("score") is not None else item.get("value")))
            row_values.append(match_score)
        values.append(row_values)
    return {
        "kind": "reverse_candidate_support",
        "title": "Candidate Support Across Evidence Matches",
        "rows": [_plot_label(str(item.get("label") or "candidate"), "Candidate") for item in selected],
        "columns": [_plot_label(label, "Match") for label in route_keys],
        "values": values,
        "candidates": [
            {
                "label": _plot_label(str(item.get("label") or "candidate"), "Candidate"),
                "score": _numeric(item.get("score")),
                "mean_score": _numeric(item.get("mean_score")),
                "best_score": _numeric(item.get("best_score")),
                "support_routes": int(_numeric(item.get("support_routes"))),
                "support_cells": int(_numeric(item.get("support_cells"))),
                "cells": str(item.get("cells") or item.get("cell") or ""),
                "exact_cell_support": bool(item.get("exact_cell_support")),
            }
            for item in rows[:12]
        ],
        "caption": "Rows are recommended candidates; columns are executed evidence matches. Color intensity shows the functional match score in each match.",
    }


def _reverse_candidate_support_bar_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "kind": "reverse_candidate_support_bar",
        "title": "Candidate Cross-Context Support",
        "items": [
            {
                "label": _plot_label(str(item.get("label") or "candidate"), "Candidate"),
                "support_routes": int(_numeric(item.get("support_routes"))),
                "support_cells": int(_numeric(item.get("support_cells"))),
                "best_score": _numeric(item.get("best_score")),
                "exact_cell_support": bool(item.get("exact_cell_support")),
            }
            for item in rows[:12]
        ],
        "caption": "Bar length summarizes how many independent evidence matches/cells support each candidate.",
    }


def _reverse_function_ring_heatmap_specs(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_source: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        source = _normalize_function_source(row.get("source"))
        if source:
            by_source.setdefault(source, []).append(row)
    specs = []
    for source in ["hallmark", "3ca_mps"]:
        source_rows = by_source.get(source, [])
        universe = _function_universe(source)
        functions = [item["label"] for item in universe]
        function_by_var = {item["var_name"]: item["label"] for item in universe}
        function_seen = set(functions)
        matches = []
        match_seen = set()
        value_map: dict[tuple[str, str], float] = {}
        direction_map: dict[tuple[str, str], str] = {}
        if not functions:
            functions = [_function_source_empty_label(source)]
            function_seen = set(functions)
        for row in source_rows:
            var_name = str(row.get("var_name") or "")
            raw_label = str(row.get("label") or var_name or "")
            label = function_by_var.get(var_name) or _function_display_label(raw_label, var_name, source)
            if label and label not in function_seen:
                function_seen.add(label)
                functions.append(label)
            match = _short_route_label(_plot_label(row.get("cell"), "Cell"), _plot_label(row.get("modality"), "Modality"))
            if match and match not in match_seen:
                match_seen.add(match)
                matches.append(match)
            weight = _numeric(row.get("target_weight"))
            direction = str(row.get("direction") or "")
            value_map[(match, label)] = weight
            direction_map[(match, label)] = direction
        if not matches:
            matches = ["No Match"]
        values = []
        directions = []
        for match in matches:
            value_row = []
            direction_row = []
            for function in functions:
                value_row.append(value_map.get((match, function), 0.0))
                direction_row.append(direction_map.get((match, function), ""))
            values.append(value_row)
            directions.append(direction_row)
        specs.append(
            {
                "kind": "reverse_function_ring_heatmap",
                "title": f"{_function_source_title(source)} Functional Targets",
                "source": source,
                "functions": functions,
                "matches": matches,
                "values": values,
                "directions": directions,
                "caption": "Annular heatmap of requested functional targets by evidence match.",
            }
        )
    return specs


def _reverse_candidate_bubble_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    candidates = []
    for item in rows[:14]:
        rank = int(_numeric(item.get("rank"))) or len(candidates) + 1
        score = _numeric(item.get("best_score") if item.get("best_score") is not None else item.get("score"))
        support = int(_numeric(item.get("support_routes") or item.get("support_cells")))
        cells = str(item.get("cells") or item.get("best_cell") or "")
        candidates.append(
            {
                "label": _plot_label(str(item.get("label") or "Candidate"), "Candidate"),
                "rank": rank,
                "score": score,
                "support": support,
                "support_cells": int(_numeric(item.get("support_cells"))),
                "cells": _plot_label(cells, "Cells"),
                "exact_cell_support": bool(item.get("exact_cell_support")),
            }
        )
    return {
        "kind": "reverse_candidate_bubble",
        "title": "Perturbation Candidate Ranking",
        "x_label": "Match Support Count",
        "y_label": "Score Rank",
        "candidates": candidates,
        "caption": "Bubble x-position shows evidence support count; y-position shows ranking; size follows score value.",
    }


def _target_function_map_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    items = []
    seen: set[tuple[str, str, str]] = set()
    for row in rows:
        label = str(row.get("label") or row.get("var_name") or "")
        direction = str(row.get("direction") or "")
        source = str(row.get("source") or "")
        key = (label, direction, source)
        if not label or key in seen:
            continue
        seen.add(key)
        items.append(
            {
                "label": _plot_label(label, "Function"),
                "direction": direction,
                "target_weight": _numeric(row.get("target_weight")),
                "source": source,
                "input": str(row.get("input") or ""),
            }
        )
        if len(items) >= 10:
            break
    return {
        "kind": "target_function_map",
        "title": "Requested Functional State",
        "items": items,
        "caption": "Reverse queries first map the user's requested state to concrete functional programs before ranking perturbations.",
    }


def _function_summaries(route_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for row in route_rows:
        label = str(row.get("function") or "")
        route_id = str(row.get("route_id") or "")
        if not label or not route_id:
            continue
        score = _numeric(row.get("score"))
        direction = str(row.get("direction") or ("activated" if score >= 0 else "suppressed"))
        item = grouped.setdefault(
            label,
            {"label": label, "route_ids": set(), "scores": [], "activated": 0, "suppressed": 0},
        )
        item["route_ids"].add(route_id)
        item["scores"].append(score)
        if direction.startswith("suppress") or score < 0:
            item["suppressed"] += 1
        else:
            item["activated"] += 1
    summaries = []
    for item in grouped.values():
        scores = item["scores"]
        activated = int(item["activated"])
        suppressed = int(item["suppressed"])
        if activated and suppressed:
            direction = "mixed"
        elif suppressed:
            direction = "suppressed"
        else:
            direction = "activated"
        summaries.append(
            {
                "label": item["label"],
                "route_count": len(item["route_ids"]),
                "activated_hits": activated,
                "suppressed_hits": suppressed,
                "mean_score": sum(scores) / max(len(scores), 1),
                "max_abs_score": max([abs(score) for score in scores] or [0.0]),
                "dominant_direction": direction,
            }
        )
    return summaries


def _candidate_key_from_label(item: dict[str, Any]) -> str:
    for key in ("pert_id", "cmap_name", "label", "name"):
        value = item.get(key)
        if value is not None and str(value).strip():
            return str(value).strip().lower()
    return ""


def _cluster_orders(values: list[list[float]]) -> tuple[list[int], list[int], str]:
    row_count = len(values)
    col_count = len(values[0]) if values else 0
    if row_count == 0 or col_count == 0:
        return list(range(row_count)), list(range(col_count)), "empty"
    try:
        import numpy as np
        from scipy.cluster.hierarchy import leaves_list, linkage
        from scipy.spatial.distance import pdist

        arr = np.asarray(values, dtype=float)
        row_order = list(range(row_count))
        col_order = list(range(col_count))
        if row_count > 1:
            row_dist = pdist(arr, metric="correlation")
            if np.isfinite(row_dist).all() and not np.allclose(row_dist, 0):
                row_order = [int(i) for i in leaves_list(linkage(row_dist, method="average"))]
        if col_count > 1:
            col_dist = pdist(arr.T, metric="correlation")
            if np.isfinite(col_dist).all() and not np.allclose(col_dist, 0):
                col_order = [int(i) for i in leaves_list(linkage(col_dist, method="average"))]
        return row_order, col_order, "hierarchical_correlation_average"
    except Exception:
        row_scores = [(idx, sum(abs(v) for v in row)) for idx, row in enumerate(values)]
        col_scores = [(idx, sum(abs(values[i][idx]) for i in range(row_count))) for idx in range(col_count)]
        return (
            [idx for idx, _ in sorted(row_scores, key=lambda item: -item[1])],
            [idx for idx, _ in sorted(col_scores, key=lambda item: -item[1])],
            "fallback_abs_score_order",
        )


def _group_route_points(points: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[float, float, str], dict[str, Any]] = {}
    for point in points:
        x = round(_numeric(point.get("cell_distance")), 2)
        y = round(_numeric(point.get("y_value")), 2)
        pert = str(point.get("perturbation") or "")
        key = (x, y, pert)
        group = groups.setdefault(
            key,
            {
                "cell_distance": x,
                "y_value": y,
                "perturbation_group": _short(pert, 18),
                "cells": [],
                "route_count": 0,
            },
        )
        group["route_count"] += 1
        cell = str(point.get("cell") or "")
        if cell and cell not in group["cells"]:
            group["cells"].append(cell)
    grouped = []
    for group in groups.values():
        cells = group["cells"]
        group["cell_group"] = cells[0] if len(cells) == 1 else "Multiple Cells"
        grouped.append(group)
    grouped.sort(key=lambda item: (_numeric(item.get("cell_distance")), _numeric(item.get("y_value")), str(item.get("perturbation_group"))))
    return grouped


def _render_route_evidence_map_svg(spec: dict[str, Any], *, width: int) -> str:
    points = spec.get("points", [])
    height = 360
    left, top, plot_w, plot_h = 86, 58, width - 170, 220
    max_x = max([_numeric(p.get("cell_distance")) for p in points] + [1.0])
    max_y = max([_numeric(p.get("y_value")) for p in points] + [1.0])
    body = [
        f'<line x1="{left}" y1="{top + plot_h}" x2="{left + plot_w}" y2="{top + plot_h}" stroke="#64748b"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top + plot_h}" stroke="#64748b"/>',
        f'<text x="{left + plot_w - 90}" y="{top + plot_h + 34}" class="axis">{_esc(spec.get("x_label"))}</text>',
        f'<text x="18" y="{top + 16}" class="axis">{_esc(spec.get("y_label"))}</text>',
    ]
    for idx, point in enumerate(points):
        x = left + int((_numeric(point.get("cell_distance")) / max(max_x, 1e-9)) * plot_w)
        y = top + plot_h - int((_numeric(point.get("y_value")) / max(max_y, 1e-9)) * plot_h)
        radius = 6 + min(int(_numeric(point.get("n_rows")) ** 0.5), 14)
        color = "#33658a" if str(point.get("status")) == "executed" else "#7a9e7e"
        label = point.get("cell") or point.get("route_id") or f"route {idx + 1}"
        detail = point.get("perturbation") or point.get("route_quality") or ""
        body.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{color}" opacity="0.78"/>')
        body.append(f'<text x="{x + radius + 5}" y="{y + 4}" class="small">{_esc(_short(label, 18))}</text>')
        if detail:
            body.append(f'<text x="{x + radius + 5}" y="{y + 18}" class="axis">{_esc(_short(detail, 22))}</text>')
    body.append(f'<text x="{left}" y="{height - 44}" class="axis">Point size reflects matched matrix rows when available.</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_function_route_heatmap_svg(spec: dict[str, Any], *, width: int) -> str:
    rows = [str(item) for item in spec.get("rows", [])]
    cols = [str(item) for item in spec.get("columns", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    cell_w = max(54, min(110, (width - 310) // max(len(cols), 1)))
    row_h = 30
    left, top = 260, 76
    height = 112 + max(len(rows), 1) * row_h
    max_abs = max([abs(v) for row in values for v in row] + [1.0]) or 1.0
    body = []
    for j, col in enumerate(cols):
        body.append(f'<text x="{left + j * cell_w + 4}" y="58" class="axis">{_esc(_short(col, 12))}</text>')
    for i, label in enumerate(rows):
        y = top + i * row_h
        body.append(f'<text x="14" y="{y + 18}" class="label">{_esc(_short(label, 34))}</text>')
        for j in range(len(cols)):
            value = values[i][j] if i < len(values) and j < len(values[i]) else 0.0
            intensity = abs(value) / max_abs
            color = _heat_color(value, intensity)
            x = left + j * cell_w
            body.append(f'<rect x="{x}" y="{y}" width="{cell_w - 4}" height="22" rx="3" fill="{color}"/>')
            if abs(value) > 0:
                body.append(f'<text x="{x + 6}" y="{y + 16}" class="axis">{value:.2g}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_program_direction_summary_svg(spec: dict[str, Any], *, width: int) -> str:
    items = spec.get("items", [])
    row_h = 32
    height = 84 + max(len(items), 1) * row_h
    mid = 470
    max_abs = max([abs(_numeric(item.get("score"))) for item in items] + [1.0]) or 1.0
    body = [f'<line x1="{mid}" x2="{mid}" y1="48" y2="{height - 32}" stroke="#64748b"/>']
    for i, item in enumerate(items):
        y = 56 + i * row_h
        score = _numeric(item.get("score"))
        width_abs = int((abs(score) / max_abs) * 260)
        x = mid if score >= 0 else mid - width_abs
        body.append(f'<text x="14" y="{y + 16}" class="label">{_esc(_short(item.get("label"), 42))}</text>')
        body.append(f'<rect x="{x}" y="{y}" width="{max(width_abs, 2)}" height="19" rx="3" fill="{_direction_color(str(item.get("direction")))}"/>')
        body.append(f'<text x="{mid + 275}" y="{y + 15}" class="value">{score:.3g}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_function_consensus_bar_svg(spec: dict[str, Any], *, width: int) -> str:
    items = spec.get("items", [])
    row_h = 36
    height = 92 + max(len(items), 1) * row_h
    left = 300
    max_count = max([_numeric(item.get("route_count")) for item in items] + [1.0]) or 1.0
    body = [f'<text x="{left}" y="50" class="axis">matches with top/bottom hit</text>']
    for i, item in enumerate(items):
        y = 66 + i * row_h
        count = _numeric(item.get("route_count"))
        mean_score = _numeric(item.get("mean_score"))
        bar_w = int((count / max_count) * 260)
        color = _direction_color(str(item.get("dominant_direction")))
        body.append(f'<text x="14" y="{y + 17}" class="label">{_esc(_short(item.get("label"), 36))}</text>')
        body.append(f'<rect x="{left}" y="{y}" width="{max(bar_w, 2)}" height="20" rx="3" fill="{color}" opacity="0.86"/>')
        body.append(f'<text x="{left + 270}" y="{y + 16}" class="axis">{int(count)} matches</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_reverse_candidate_support_svg(spec: dict[str, Any], *, width: int) -> str:
    rows = [str(item) for item in spec.get("rows", [])]
    cols = [str(item) for item in spec.get("columns", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    cell_w = max(48, min(92, (width - 300) // max(len(cols), 1)))
    row_h = 28
    left, top = 230, 76
    height = 112 + max(len(rows), 1) * row_h
    max_value = max([abs(v) for row in values for v in row] + [1.0]) or 1.0
    body = []
    for j, col in enumerate(cols):
        body.append(f'<text x="{left + j * cell_w + 4}" y="58" class="axis">{_esc(_short(col, 12))}</text>')
    for i, label in enumerate(rows):
        y = top + i * row_h
        body.append(f'<text x="14" y="{y + 18}" class="label">{_esc(_short(label, 28))}</text>')
        for j in range(len(cols)):
            value = values[i][j] if i < len(values) and j < len(values[i]) else 0.0
            intensity = abs(value) / max_value
            color = _single_heat_color(intensity)
            x = left + j * cell_w
            body.append(f'<rect x="{x}" y="{y}" width="{cell_w - 4}" height="22" rx="3" fill="{color}"/>')
            if value > 0:
                body.append(f'<text x="{x + 6}" y="{y + 16}" class="axis">{value:.2g}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_reverse_candidate_support_bar_svg(spec: dict[str, Any], *, width: int) -> str:
    items = spec.get("items", [])
    row_h = 34
    height = 88 + max(len(items), 1) * row_h
    left = 280
    max_support = max([_numeric(item.get("support_cells")) for item in items] + [1.0]) or 1.0
    body = [f'<text x="{left}" y="50" class="axis">supporting cells</text>']
    for i, item in enumerate(items):
        y = 64 + i * row_h
        support = _numeric(item.get("support_cells"))
        route_support = _numeric(item.get("support_routes"))
        bar_w = int((support / max_support) * 230)
        body.append(f'<text x="14" y="{y + 17}" class="label">{_esc(_short(item.get("label"), 32))}</text>')
        body.append(f'<rect x="{left}" y="{y}" width="{max(bar_w, 2)}" height="20" rx="3" fill="#33658a" opacity="0.86"/>')
        body.append(f'<text x="{left + 242}" y="{y + 16}" class="axis">{int(support)} cells / {int(route_support)} matches</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_target_function_map_svg(spec: dict[str, Any], *, width: int) -> str:
    items = spec.get("items", [])
    row_h = 34
    height = 88 + max(len(items), 1) * row_h
    body = [
        '<text x="22" y="52" class="axis">requested function</text>',
        '<text x="390" y="52" class="axis">direction</text>',
        '<text x="520" y="52" class="axis">source</text>',
    ]
    for i, item in enumerate(items):
        y = 66 + i * row_h
        direction = str(item.get("direction") or "")
        weight = _numeric(item.get("target_weight"))
        color = _direction_color(direction)
        body.append(f'<text x="22" y="{y + 18}" class="label">{_esc(_short(item.get("label"), 42))}</text>')
        body.append(f'<rect x="390" y="{y}" width="92" height="22" rx="3" fill="{color}" opacity="0.82"/>')
        body.append(f'<text x="398" y="{y + 16}" class="axis">{_esc(direction)} {weight:.1f}</text>')
        body.append(f'<text x="520" y="{y + 16}" class="axis">{_esc(_short(item.get("source"), 24))}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_route_evidence_map_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    points = spec.get("points", [])
    if not points:
        raise ValueError("route evidence map needs route points")
    fig, ax = plt.subplots(figsize=(6.6, 5.2))
    grouped_points = _group_route_points(points)
    x = [_numeric(point.get("cell_distance")) for point in grouped_points]
    y = [_numeric(point.get("y_value")) for point in grouped_points]
    sizes = [90 + min(_numeric(point.get("route_count")) * 48, 360) for point in grouped_points]
    cell_values = [str(point.get("cell_group") or "") for point in grouped_points]
    perturbation_values = [str(point.get("perturbation_group") or "") for point in grouped_points]
    cell_palette = _palette(cell_values)
    perturbation_palette = _palette(perturbation_values)
    facecolors = [perturbation_palette.get(value, "#f8fafc") for value in perturbation_values]
    edgecolors = [cell_palette.get(value, "#263241") for value in cell_values]
    for xi, yi in zip(x, y):
        ax.plot([0, xi], [0, yi], linestyle="--", linewidth=0.8, color="#9ca3af", alpha=0.55, zorder=1)
    ax.scatter(x, y, s=sizes, c=facecolors, alpha=0.78, edgecolors=edgecolors, linewidths=1.8)
    ax.scatter([0], [0], s=120, marker="o", c="#9ca3af", edgecolors="#374151", linewidths=1.2, zorder=5)
    ax.annotate(_short(spec.get("query_label") or "Query", 44), (0, 0), xytext=(6, 6), textcoords="offset points", fontsize=8, color="#111827")
    x_min, x_max = min([0.0] + x), max([0.0] + x)
    y_min, y_max = min([0.0] + y), max([0.0] + y)
    x_pad = max((x_max - x_min) * 0.16, 0.035)
    y_pad = max((y_max - y_min) * 0.16, 0.035)
    ax.set_xlim(x_min - x_pad, x_max + x_pad)
    ax.set_ylim(y_min - y_pad, y_max + y_pad)
    ax.set_xlabel(str(spec.get("x_label") or "Cell Distance"))
    ax.set_ylabel(str(spec.get("y_label") or "Perturbation Distance"))
    ax.set_title(str(spec.get("title") or "Evidence route map"))
    ax.grid(alpha=0.24)
    from matplotlib.lines import Line2D

    for xi, yi, point in zip(x, y, grouped_points):
        count = int(_numeric(point.get("route_count")))
        if count > 1:
            ax.annotate(str(count), (xi, yi), ha="center", va="center", fontsize=8, color="white", weight="bold")
    cell_handles = [
        Line2D([0], [0], marker="o", color="white", label=_short(value, 14), markerfacecolor="white", markeredgecolor=color, markeredgewidth=2, markersize=7)
        for value, color in list(cell_palette.items())[:8]
    ]
    perturbation_handles = [
        Line2D([0], [0], marker="o", color="white", label=_short(value, 16), markerfacecolor=color, markeredgecolor="#263241", markersize=7)
        for value, color in list(perturbation_palette.items())[:6]
    ]
    if cell_handles:
        legend1 = ax.legend(handles=cell_handles, title="Cell", loc="center left", bbox_to_anchor=(1.02, 0.68), fontsize=7, title_fontsize=8, frameon=True, borderaxespad=0.0)
        ax.add_artist(legend1)
    if perturbation_handles:
        ax.legend(handles=perturbation_handles, title="Perturbation", loc="center left", bbox_to_anchor=(1.02, 0.30), fontsize=7, title_fontsize=8, frameon=True, borderaxespad=0.0)
    fig.subplots_adjust(right=0.73)
    return fig


def _render_forward_route_graph_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    cells = [str(item) for item in spec.get("cells", [])]
    perturbations = [str(item) for item in spec.get("perturbations", [])]
    functions = [str(item) for item in spec.get("functions", [])]
    routes = list(spec.get("routes") or [])
    edges = list(spec.get("function_edges") or [])
    if not cells or not perturbations or not functions or not routes or not edges:
        raise ValueError("forward route graph needs cells, perturbations, functions, routes, and function edges")

    max_layer = max(len(cells), len(perturbations), len(functions), 3)
    fig_w = min(max(6.8, 0.82 * max_layer + 2.0), 10.2)
    fig, ax = plt.subplots(figsize=(fig_w, 6.2))
    ax.set_axis_off()
    ax.set_xlim(-0.08, 1.02)
    ax.set_ylim(0.02, 0.98)

    cell_pos = {f"cell:{name}": pos for name, pos in _layer_positions(cells, 0.78, x0=0.14, x1=0.94).items()}
    pert_pos = {f"pert:{name}": pos for name, pos in _layer_positions(perturbations, 0.49, x0=0.14, x1=0.94).items()}
    func_pos = {f"func:{name}": pos for name, pos in _layer_positions(functions, 0.18, x0=0.10, x1=0.96).items()}
    pos = {**cell_pos, **pert_pos, **func_pos}

    ax.text(-0.055, 0.78, "Cell\nContext", ha="left", va="center", fontsize=8.5, weight="bold", color="#374151")
    ax.text(-0.055, 0.49, "Perturbation\nEvidence", ha="left", va="center", fontsize=8.5, weight="bold", color="#374151")
    ax.text(-0.055, 0.18, "Consensus\nPrograms", ha="left", va="center", fontsize=8.5, weight="bold", color="#374151")

    for route in routes:
        c_key = f"cell:{route.get('cell')}"
        p_key = f"pert:{route.get('perturbation')}"
        if c_key not in pos or p_key not in pos:
            continue
        match_type = str(route.get("perturbation_match_type") or "")
        linestyle = "-" if _is_direct_match_type(match_type) else "--"
        ax.annotate(
            "",
            xy=pos[p_key],
            xytext=pos[c_key],
            arrowprops=dict(arrowstyle="-", color="#9ca3af", lw=1.25, linestyle=linestyle, alpha=0.62),
            zorder=1,
        )

    max_abs = max([abs(_numeric(edge.get("score"))) for edge in edges] + [1.0])
    collapsed_edges: dict[tuple[str, str], list[float]] = {}
    for edge in edges:
        key = (str(edge.get("perturbation") or ""), str(edge.get("function") or ""))
        collapsed_edges.setdefault(key, []).append(_numeric(edge.get("score")))
    for (perturbation, function), values in collapsed_edges.items():
        p_key = f"pert:{perturbation}"
        f_key = f"func:{_plot_label(function, 'Function')}"
        if p_key not in pos or f_key not in pos:
            continue
        score = sum(values) / len(values)
        color = "#b23a48" if score > 0 else "#33658a"
        lw = 0.65 + 2.7 * min(abs(score) / max_abs, 1.0)
        ax.annotate(
            "",
            xy=pos[f_key],
            xytext=pos[p_key],
            arrowprops=dict(arrowstyle="-", color=color, lw=lw, alpha=0.50),
            zorder=2,
        )

    for cell in cells:
        _draw_route_graph_node(ax, pos[f"cell:{cell}"], cell, "#dbeafe", "#2563eb", size=300, fs=7.7, max_line=11, yoff=0.050)
    for perturbation in perturbations:
        _draw_route_graph_node(ax, pos[f"pert:{perturbation}"], perturbation, "#fef3c7", "#d97706", size=320, fs=7.7, max_line=12, yoff=0.050)
    function_scores = spec.get("function_scores") or {}
    for function in functions:
        raw_score = _numeric(function_scores.get(function))
        edge_color = "#b23a48" if raw_score >= 0 else "#33658a"
        _draw_route_graph_node(ax, pos[f"func:{function}"], function, "#f9fafb", edge_color, size=255, fs=7.0, max_line=14, yoff=0.041)

    from matplotlib.lines import Line2D

    handles = [
        Line2D([0], [0], color="#9ca3af", lw=1.4, label="cell-to-perturbation match"),
        Line2D([0], [0], color="#b23a48", lw=2.8, label="activated function edge"),
        Line2D([0], [0], color="#33658a", lw=2.8, label="suppressed function edge"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.045), ncol=3, frameon=False, fontsize=7.8)
    ax.set_title(str(spec.get("title") or "Evidence Match Network"), fontsize=12, weight="bold", pad=8)
    fig.tight_layout(rect=(0, 0.03, 1, 0.96))
    return fig


def _render_function_route_heatmap_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    rows = [str(item) for item in spec.get("rows", [])]
    cols = [str(item) for item in spec.get("columns", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    if not rows or not cols or not values:
        raise ValueError("function route heatmap needs rows, columns, and values")
    try:
        import pandas as pd
        import seaborn as sns

        df = pd.DataFrame(values, index=[_short(row, 48) for row in rows], columns=[_short(col, 28) for col in cols])
        vmin, vmax = _symmetric_color_limits(values)
        fig_h = max(3.8, 0.30 * len(rows) + 1.6)
        fig_w = max(6.6, 0.58 * len(cols) + 3.5)
        if len(rows) > 1 and len(cols) > 1:
            grid = sns.clustermap(
                df,
                cmap="vlag",
                center=0,
                vmin=vmin,
                vmax=vmax,
                linewidths=0.35,
                linecolor="#f1f5f9",
                figsize=(fig_w, fig_h),
                cbar_kws={"label": ""},
                method="average",
                metric="correlation",
            )
            grid.fig.suptitle(str(spec.get("title") or "Functional signal clustered by evidence match"), y=1.02)
            grid.ax_heatmap.set_xlabel("Evidence Match")
            grid.ax_heatmap.set_ylabel("Functional Program")
            grid.ax_heatmap.tick_params(axis="x", rotation=45, labelsize=8)
            grid.ax_heatmap.tick_params(axis="y", labelsize=8)
            return grid.fig
        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        sns.heatmap(df, ax=ax, cmap="vlag", center=0, vmin=vmin, vmax=vmax, linewidths=0.35, linecolor="#f1f5f9", cbar_kws={"label": ""})
        ax.set_title(str(spec.get("title") or "Functional signal clustered by evidence match"))
        ax.set_xlabel("Evidence Match")
        ax.set_ylabel("Functional Program")
        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        return fig
    except Exception:
        fig_h = max(3.0, 0.32 * len(rows) + 1.6)
        fig, ax = plt.subplots(figsize=(8.8, fig_h))
        vmin, vmax = _symmetric_color_limits(values)
        image = ax.imshow(values, aspect="auto", cmap="coolwarm", vmin=vmin, vmax=vmax)
        ax.set_yticks(range(len(rows)))
        ax.set_yticklabels([_short(row, 44) for row in rows])
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels([_short(col, 24) for col in cols], rotation=45, ha="right")
        ax.set_title(str(spec.get("title") or "Functional signal clustered by evidence match"))
        ax.set_xlabel("Evidence Match")
        ax.set_ylabel("Functional Program")
        fig.colorbar(image, ax=ax, shrink=0.72, label="signed functional score")
        _caption(fig, spec)
        return fig


def _render_program_direction_summary_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("items", [])
    labels = [str(item.get("label") or "") for item in items]
    scores = [_numeric(item.get("score")) for item in items]
    colors = [_direction_color(str(item.get("direction") or "")) for item in items]
    if not labels:
        raise ValueError("program direction summary needs items")
    fig_h = max(3.2, 0.34 * len(labels) + 1.6)
    fig, ax = plt.subplots(figsize=(8.6, fig_h))
    ax.barh(range(len(labels)), scores, color=colors)
    ax.axvline(0, color="#475569", linewidth=0.8)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels([_short(label, 42) for label in labels])
    ax.invert_yaxis()
    ax.set_xlabel("signed functional score")
    ax.set_title(str(spec.get("title") or "Functional program direction summary"))
    ax.grid(axis="x", alpha=0.24)
    return fig


def _render_function_consensus_bar_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("items", [])
    if not items:
        raise ValueError("function consensus bar needs items")
    labels = [str(item.get("label") or "") for item in items]
    activated = [_numeric(item.get("activated_hits")) for item in items]
    suppressed = [_numeric(item.get("suppressed_hits")) for item in items]
    counts = [a + s for a, s in zip(activated, suppressed)]
    fig_h = max(2.8, 0.28 * len(items) + 1.2)
    fig, ax = plt.subplots(figsize=(5.0, fig_h))
    y = list(range(len(labels)))
    ax.barh(y, activated, color=_direction_color("activated"), label="Activated")
    ax.barh(y, suppressed, left=activated, color=_direction_color("suppressed"), label="Suppressed")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels([_short(label, 44) for label in labels])
    ax.invert_yaxis()
    ax.set_xlabel("Evidence Match Hit Count")
    ax.set_title(str(spec.get("title") or "Functional program evidence support"))
    ax.grid(axis="x", alpha=0.24)
    ax.set_xlim(0, max(counts) + 0.8)
    for idx, item in enumerate(items):
        ax.text(counts[idx] + 0.05, idx, f"{int(counts[idx])}", va="center", fontsize=8)
    ax.legend(loc="lower right", fontsize=7, frameon=True)
    return fig


def _render_reverse_candidate_support_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    rows = [str(item) for item in spec.get("rows", [])]
    cols = [str(item) for item in spec.get("columns", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    if not rows or not cols or not values:
        raise ValueError("reverse candidate support needs rows, columns, and values")
    try:
        import pandas as pd
        import seaborn as sns

        df = pd.DataFrame(values, index=[_short(row, 34) for row in rows], columns=[_short(col, 20) for col in cols])
        fig_h = max(3.0, 0.30 * len(rows) + 1.2)
        fig_w = max(5.6, 0.46 * len(cols) + 3.2)
        fig, ax = plt.subplots(figsize=(fig_w, fig_h))
        sns.heatmap(df, ax=ax, cmap="Blues", linewidths=0.35, linecolor="#f1f5f9", cbar_kws={"label": ""})
        ax.set_title(str(spec.get("title") or "Candidate Support Across Evidence Matches"))
        ax.set_xlabel("Evidence Match")
        ax.set_ylabel("Candidate")
        ax.tick_params(axis="x", rotation=45, labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        return fig
    except Exception:
        fig_h = max(3.0, 0.30 * len(rows) + 1.2)
        fig, ax = plt.subplots(figsize=(6.8, fig_h))
        image = ax.imshow(values, aspect="auto", cmap="Blues")
        ax.set_yticks(range(len(rows)))
        ax.set_yticklabels([_short(row, 34) for row in rows])
        ax.set_xticks(range(len(cols)))
        ax.set_xticklabels([_short(col, 20) for col in cols], rotation=45, ha="right")
        ax.set_xlabel("Evidence Match")
        ax.set_ylabel("Candidate")
        ax.set_title(str(spec.get("title") or "Candidate Support Across Evidence Matches"))
        fig.colorbar(image, ax=ax, shrink=0.72, label="")
        return fig


def _render_reverse_candidate_support_bar_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("items", [])
    if not items:
        raise ValueError("reverse candidate support bar needs items")
    labels = [str(item.get("label") or "") for item in items]
    support_cells = [_numeric(item.get("support_cells")) for item in items]
    support_matches = [_numeric(item.get("support_routes")) for item in items]
    fig_h = max(2.8, 0.28 * len(items) + 1.2)
    fig, ax = plt.subplots(figsize=(5.2, fig_h))
    y = list(range(len(labels)))
    ax.barh(y, support_cells, color="#33658a", alpha=0.86)
    ax.set_yticks(y)
    ax.set_yticklabels([_short(label, 34) for label in labels])
    ax.invert_yaxis()
    ax.set_xlabel("Supporting Cell Count")
    ax.set_title(str(spec.get("title") or "Candidate Cross-Context Support"))
    ax.grid(axis="x", alpha=0.24)
    ax.set_xlim(0, max(support_cells + [1.0]) + 0.8)
    for idx, (cells, matches) in enumerate(zip(support_cells, support_matches)):
        ax.text(cells + 0.05, idx, f"{int(cells)} cells / {int(matches)} matches", va="center", fontsize=8)
    return fig


def _render_reverse_function_ring_heatmap_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    import math

    functions = [str(item) for item in spec.get("functions", [])]
    matches = [str(item) for item in spec.get("matches", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    directions = spec.get("directions", [])
    if not functions or not matches:
        raise ValueError("reverse function ring heatmap needs functions and matches")
    n_functions = len(functions)
    n_matches = len(matches)
    fig_size = 4.8 if n_functions <= 8 else 5.6
    fig, ax = plt.subplots(figsize=(fig_size, fig_size), subplot_kw={"projection": "polar"})
    ax.set_theta_direction(-1)
    ax.set_theta_offset(math.pi / 2)
    width = 2 * math.pi / max(n_functions, 1)
    inner = 0.34
    ring_h = 0.46 / max(n_matches, 1)
    max_abs = max([abs(v) for row in values for v in row] + [1.0]) or 1.0
    for ring_idx, match in enumerate(matches):
        bottom = inner + ring_idx * ring_h
        for func_idx, function in enumerate(functions):
            theta = (2 * math.pi * func_idx / n_functions)
            value = values[ring_idx][func_idx] if ring_idx < len(values) and func_idx < len(values[ring_idx]) else 0.0
            direction = ""
            if ring_idx < len(directions) and func_idx < len(directions[ring_idx]):
                direction = str(directions[ring_idx][func_idx] or "")
            color = _reverse_target_color(value, direction, max_abs)
            ax.bar(theta, ring_h, width=width, bottom=bottom, color=color, edgecolor=color, linewidth=0, align="edge")
    label_radius = inner + max(n_matches * ring_h, ring_h) * 0.50
    for func_idx, function in enumerate(functions):
        theta = 2 * math.pi * (func_idx + 0.5) / n_functions
        rotation = math.degrees(math.pi / 2 - theta)
        if rotation < -90:
            rotation += 180
        if rotation > 90:
            rotation -= 180
        ax.text(theta, label_radius, function, ha="center", va="center", fontsize=5.6, rotation=rotation, rotation_mode="anchor", color="#111827")
    ax.set_ylim(0, inner + n_matches * ring_h + 0.10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines["polar"].set_visible(False)
    ax.set_title(str(spec.get("title") or "Functional Targets"), pad=16)
    from matplotlib.patches import Patch

    handles = [
        Patch(facecolor="#b23a48", edgecolor="#d1d5db", label="Activated"),
        Patch(facecolor="#33658a", edgecolor="#d1d5db", label="Suppressed"),
        Patch(facecolor="#ffffff", edgecolor="#d1d5db", label="Not Matched"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.08), ncol=3, fontsize=7, frameon=False)
    return fig


def _render_reverse_candidate_bubble_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("candidates", [])
    if not items:
        raise ValueError("reverse candidate bubble needs candidates")
    x = [_numeric(item.get("support")) for item in items]
    y = [_numeric(item.get("rank")) for item in items]
    scores = [_numeric(item.get("score")) for item in items]
    max_score = max(scores + [1.0]) or 1.0
    sizes = [70 + 430 * (score / max_score) for score in scores]
    colors = ["#b23a48" if item.get("exact_cell_support") else "#33658a" for item in items]
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.scatter(x, y, s=sizes, c=colors, alpha=0.76, edgecolors="#263241", linewidths=0.8)
    ax.invert_yaxis()
    ax.set_xlabel(str(spec.get("x_label") or "Match Support Count"))
    ax.set_ylabel(str(spec.get("y_label") or "Score Rank"))
    ax.set_title(str(spec.get("title") or "Perturbation Candidate Ranking"))
    ax.grid(alpha=0.24)
    ax.set_xlim(min([0] + x) - 0.35, max([1] + x) + 0.65)
    ax.set_ylim(max(y + [1]) + 0.8, min(y + [1]) - 0.8)
    label_items = sorted(items, key=lambda item: (-_numeric(item.get("support")), -_numeric(item.get("score")), _numeric(item.get("rank"))))[:5]
    for item in label_items:
        label = str(item.get("label") or "")
        cells = str(item.get("cells") or "")
        if not label:
            continue
        px = _numeric(item.get("support"))
        py = _numeric(item.get("rank"))
        cell_text = f"({_short(cells, 28)})" if cells else ""
        ax.annotate(_short(label, 24), (px, py), xytext=(7, 8), textcoords="offset points", fontsize=7, color="#111827")
        if cell_text:
            cell_color = "#b23a48" if item.get("exact_cell_support") else "#33658a"
            ax.annotate(cell_text, (px, py), xytext=(7, -2), textcoords="offset points", fontsize=6.5, color=cell_color)
    from matplotlib.lines import Line2D

    handles = [
        Line2D([0], [0], marker="o", color="white", label="Exact Cell Support", markerfacecolor="#b23a48", markeredgecolor="#263241", markersize=7),
        Line2D([0], [0], marker="o", color="white", label="Context Match Support", markerfacecolor="#33658a", markeredgecolor="#263241", markersize=7),
    ]
    ax.legend(handles=handles, loc="lower right", fontsize=7, frameon=True)
    return fig


def _render_target_function_map_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("items", [])
    if not items:
        raise ValueError("target function map needs items")
    fig_h = max(3.4, 0.32 * len(items) + 1.6)
    fig, ax = plt.subplots(figsize=(7.0, fig_h))
    ax.axis("off")
    ax.set_title(str(spec.get("title") or "Requested Functional State"), loc="left")
    for idx, item in enumerate(items):
        y = 0.92 - idx * (0.82 / max(len(items), 1))
        label = str(item.get("label") or "")
        direction = str(item.get("direction") or "")
        color = _direction_color(direction)
        ax.text(0.02, y, _short(label, 44), fontsize=8, color="#263241", transform=ax.transAxes)
        ax.text(0.56, y, f"{direction} {_numeric(item.get('target_weight')):.1f}", fontsize=8, color="white", bbox={"boxstyle": "round,pad=0.22", "fc": color, "ec": color}, transform=ax.transAxes)
        ax.text(0.78, y, _short(item.get("source"), 22), fontsize=8, color="#334155", transform=ax.transAxes)
    return fig


def _bar_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "kind": "bar",
        "title": "Ranked evidence score",
        "x": [str(item.get("label") or "result") for item in rows],
        "y": [_numeric(item.get("score")) for item in rows],
        "color_by": [str(item.get("direction") or item.get("kind") or "result") for item in rows],
        "caption": "Top evidence-backed rows from the primary query route.",
    }


def _bubble_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scores = [_numeric(item.get("score")) for item in rows]
    return {
        "kind": "bubble",
        "title": "Result magnitude and rank",
        "labels": [str(item.get("label") or "result") for item in rows],
        "x": [item.get("rank") if item.get("rank") is not None else idx + 1 for idx, item in enumerate(rows)],
        "y": scores,
        "size": [max(abs(score), 0.05) for score in scores],
        "caption": "Bubble size follows absolute score magnitude.",
    }


def _heatmap_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "kind": "heatmap",
        "title": "Primary Match Score Heatmap",
        "rows": [str(item.get("label") or "result") for item in rows],
        "columns": ["primary match"],
        "values": [[_numeric(item.get("score"))] for item in rows],
        "caption": "Compact heatmap view of the main evidence scores.",
    }


def _route_flow_spec(routes: list[dict[str, Any]], dossier: dict[str, Any]) -> dict[str, Any]:
    route_labels = []
    for route in routes[:6]:
        label = route.get("route_id") or route.get("tier") or route.get("status") or "route"
        if route.get("cell"):
            label = f"{label}: {route['cell']}"
        route_labels.append(str(label))
    return {
        "kind": "route_flow",
        "title": "Query evidence path",
        "nodes": ["Question", "Evidence matching", "Evidence matrix", "Evidence review", "Report"],
        "route_labels": route_labels,
        "route_count": len(routes),
        "status": dossier.get("dossier_status"),
        "caption": "High-level path from the user question to the displayed evidence.",
    }


def _evidence_panel_spec(rules: list[dict[str, Any]], dossier: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "evidence_panel",
        "title": "Evidence limits",
        "items": rules,
        "confidence": (dossier.get("uncertainty_layer") or {}).get("confidence"),
        "caption": "Claims the report may mention and claims it must avoid.",
    }


def _render_bar_svg(spec: dict[str, Any], *, width: int) -> str:
    labels = spec.get("x", [])
    values = [_numeric(v) for v in spec.get("y", [])]
    colors = spec.get("color_by", [])
    n = max(len(labels), 1)
    row_h = 34
    left = 250
    mid = left + 250
    height = 86 + n * row_h
    max_abs = max([abs(v) for v in values] or [1.0]) or 1.0
    body = []
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 56 + i * row_h
        bar_w = int((abs(value) / max_abs) * 230)
        x = mid if value >= 0 else mid - bar_w
        color = _direction_color(colors[i] if i < len(colors) else "")
        body.append(f'<text x="12" y="{y + 17}" class="label">{_esc(_short(label, 34))}</text>')
        body.append(f'<rect x="{x}" y="{y}" width="{max(bar_w, 2)}" height="20" rx="3" fill="{color}"/>')
        body.append(f'<text x="{mid + 245}" y="{y + 16}" class="value">{value:.3g}</text>')
    body.append(f'<line x1="{mid}" x2="{mid}" y1="48" y2="{height - 24}" stroke="#475569" stroke-width="1"/>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_bubble_svg(spec: dict[str, Any], *, width: int) -> str:
    labels = spec.get("labels", [])
    yvals = [_numeric(v) for v in spec.get("y", [])]
    sizes = [_numeric(v) for v in spec.get("size", [])]
    n = max(len(labels), 1)
    height = 96 + n * 36
    max_size = max(sizes or [1.0]) or 1.0
    min_v = min(yvals or [0.0])
    max_v = max(yvals or [1.0])
    span = max(max_v - min_v, 1e-9)
    body = []
    for i, label in enumerate(labels):
        value = yvals[i] if i < len(yvals) else 0.0
        radius = 7 + int((abs(sizes[i] if i < len(sizes) else value) / max_size) * 18)
        x = 280 + int(((value - min_v) / span) * 460)
        y = 60 + i * 36
        body.append(f'<text x="12" y="{y + 5}" class="label">{_esc(_short(label, 34))}</text>')
        body.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="#7a9e7e" opacity="0.82"/>')
        body.append(f'<text x="{x + radius + 8}" y="{y + 5}" class="value">{value:.3g}</text>')
    body.append('<text x="280" y="40" class="axis">score axis</text>')
    body.append(f'<line x1="280" x2="740" y1="48" y2="48" stroke="#94a3b8" stroke-width="1"/>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_heatmap_svg(spec: dict[str, Any], *, width: int) -> str:
    labels = spec.get("rows", [])
    values = [(_numeric(row[0]) if row else 0.0) for row in spec.get("values", [])]
    n = max(len(labels), 1)
    row_h = 28
    height = 82 + n * row_h
    max_abs = max([abs(v) for v in values] or [1.0]) or 1.0
    body = []
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 52 + i * row_h
        intensity = abs(value) / max_abs
        color = _heat_color(value, intensity)
        body.append(f'<text x="12" y="{y + 18}" class="label">{_esc(_short(label, 38))}</text>')
        body.append(f'<rect x="300" y="{y}" width="360" height="22" rx="3" fill="{color}"/>')
        body.append(f'<text x="675" y="{y + 17}" class="value">{value:.3g}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_route_flow_svg(spec: dict[str, Any], *, width: int) -> str:
    nodes = spec.get("nodes", [])
    route_labels = spec.get("route_labels", [])
    height = 180 + max(len(route_labels), 1) * 22
    step = max((width - 80) // max(len(nodes), 1), 110)
    body = []
    for i, node in enumerate(nodes):
        x = 36 + i * step
        body.append(f'<rect x="{x}" y="54" width="118" height="44" rx="7" fill="#ffffff" stroke="#64748b"/>')
        body.append(f'<text x="{x + 12}" y="82" class="label">{_esc(_short(str(node), 14))}</text>')
        if i < len(nodes) - 1:
            body.append(f'<line x1="{x + 118}" y1="76" x2="{x + step}" y2="76" stroke="#64748b" marker-end="url(#arrow)"/>')
    body.append(f'<text x="36" y="128" class="value">status: {_esc(str(spec.get("status")))}, routes: {_esc(str(spec.get("route_count")))}</text>')
    for idx, label in enumerate(route_labels[:8]):
        body.append(f'<text x="52" y="{158 + idx * 22}" class="small">- {_esc(_short(label, 95))}</text>')
    return _svg_shell(spec, width, height, "\n".join(body), defs=_arrow_def())


def _render_evidence_panel_svg(spec: dict[str, Any], *, width: int) -> str:
    items = spec.get("items", [])[:10]
    row_h = 42
    height = 94 + max(len(items), 1) * row_h
    body = [f'<text x="28" y="46" class="value">confidence: {_esc(str(spec.get("confidence")))}</text>']
    for i, item in enumerate(items):
        y = 66 + i * row_h
        rule = str(item.get("rule") or "rule")
        text = str(item.get("text") or "")
        color = "#b23a48" if rule == "must_not_claim" else "#33658a"
        body.append(f'<rect x="24" y="{y}" width="{width - 64}" height="30" rx="5" fill="#ffffff" stroke="#d8dde6"/>')
        body.append(f'<rect x="24" y="{y}" width="6" height="30" fill="{color}"/>')
        body.append(f'<text x="42" y="{y + 20}" class="small">{_esc(rule.replace("_", " "))}: {_esc(_short(text, 100))}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_bar_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    labels = [str(item) for item in spec.get("x", [])]
    values = [_numeric(v) for v in spec.get("y", [])]
    if not labels or not values:
        raise ValueError("bar figure needs labels and values")
    colors = [_direction_color(str(v)) for v in spec.get("color_by", [])]
    if len(colors) < len(values):
        colors.extend(["#7a9e7e"] * (len(values) - len(colors)))
    fig_h = max(3.2, 0.34 * len(labels) + 1.8)
    fig, ax = plt.subplots(figsize=(9, fig_h))
    y = list(range(len(labels)))
    ax.barh(y, values, color=colors[: len(values)])
    ax.axvline(0, color="#475569", linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels([_short(label, 42) for label in labels])
    ax.invert_yaxis()
    ax.set_xlabel("matrix score")
    ax.set_title(str(spec.get("title") or "Ranked evidence score"))
    ax.grid(axis="x", alpha=0.25)
    return fig


def _render_bubble_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    labels = [str(item) for item in spec.get("labels", [])]
    x = [_numeric(v) for v in spec.get("x", [])]
    y = [_numeric(v) for v in spec.get("y", [])]
    sizes = [_numeric(v) for v in spec.get("size", [])]
    if not labels or not x or not y:
        raise ValueError("bubble figure needs labels, x, and y values")
    scaled = [80 + 520 * (abs(v) / (max([abs(s) for s in sizes] or [1.0]) or 1.0)) for v in sizes]
    fig_h = max(3.4, 0.32 * len(labels) + 1.8)
    fig, ax = plt.subplots(figsize=(9, fig_h))
    ax.scatter(x[: len(y)], y, s=scaled[: len(y)], color="#7a9e7e", alpha=0.72, edgecolor="#334155")
    for label, xi, yi in zip(labels, x, y):
        ax.text(xi, yi, " " + _short(label, 28), va="center", fontsize=8)
    ax.set_xlabel("rank")
    ax.set_ylabel("matrix score")
    ax.set_title(str(spec.get("title") or "Result magnitude and rank"))
    ax.grid(alpha=0.25)
    _caption(fig, spec)
    return fig


def _render_heatmap_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    labels = [str(item) for item in spec.get("rows", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    if not labels or not values:
        raise ValueError("heatmap figure needs row labels and values")
    fig_h = max(3.0, 0.32 * len(labels) + 1.5)
    fig, ax = plt.subplots(figsize=(7.8, fig_h))
    vmin, vmax = _symmetric_color_limits(values)
    image = ax.imshow(values, aspect="auto", cmap="coolwarm", vmin=vmin, vmax=vmax)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels([_short(label, 42) for label in labels])
    ax.set_xticks(range(len(spec.get("columns", ["primary match"]))))
    ax.set_xticklabels(spec.get("columns", ["primary match"]))
    ax.set_title(str(spec.get("title") or "Primary match score heatmap"))
    fig.colorbar(image, ax=ax, shrink=0.72, label="matrix score")
    _caption(fig, spec)
    return fig


def _symmetric_color_limits(values: list[list[float]]) -> tuple[float, float]:
    max_abs = 0.0
    for row in values:
        for value in row:
            try:
                number = float(value)
            except (TypeError, ValueError):
                continue
            if number != number:
                continue
            max_abs = max(max_abs, abs(number))
    if max_abs <= 0:
        max_abs = 1.0
    return -max_abs, max_abs


def _render_route_flow_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    nodes = [str(item) for item in spec.get("nodes", [])]
    if not nodes:
        raise ValueError("route flow figure needs nodes")
    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.axis("off")
    xs = [0.08 + i * (0.84 / max(len(nodes) - 1, 1)) for i in range(len(nodes))]
    for idx, (x, label) in enumerate(zip(xs, nodes)):
        ax.text(x, 0.68, label, ha="center", va="center", fontsize=10, bbox={"boxstyle": "round,pad=0.35", "fc": "white", "ec": "#64748b"})
        if idx < len(xs) - 1:
            ax.annotate("", xy=(xs[idx + 1] - 0.07, 0.68), xytext=(x + 0.07, 0.68), arrowprops={"arrowstyle": "->", "color": "#64748b"})
    ax.text(0.02, 0.38, f"status: {spec.get('status')}   matches: {spec.get('route_count')}", fontsize=9, color="#334155")
    route_labels = spec.get("route_labels", [])[:6]
    for idx, label in enumerate(route_labels):
        ax.text(0.04, 0.24 - idx * 0.07, "- " + _short(label, 110), fontsize=8, color="#334155")
    ax.set_title(str(spec.get("title") or "Query evidence path"))
    _caption(fig, spec, y=0.02)
    return fig


def _render_evidence_panel_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("items", [])[:10]
    if not items:
        raise ValueError("evidence panel needs claim rules")
    fig_h = max(3.4, 0.42 * len(items) + 1.5)
    fig, ax = plt.subplots(figsize=(10, fig_h))
    ax.axis("off")
    ax.set_title(str(spec.get("title") or "Evidence limits"), loc="left")
    ax.text(0.02, 0.92, f"confidence: {spec.get('confidence')}", fontsize=9, color="#334155", transform=ax.transAxes)
    for idx, item in enumerate(items):
        y = 0.82 - idx * 0.08
        rule = str(item.get("rule") or "rule")
        color = "#b23a48" if rule == "must_not_claim" else "#33658a"
        ax.text(0.02, y, rule.replace("_", " "), fontsize=8, color="white", bbox={"boxstyle": "round,pad=0.25", "fc": color, "ec": color}, transform=ax.transAxes)
        ax.text(0.22, y, _short(str(item.get("text") or ""), 110), fontsize=8, color="#334155", transform=ax.transAxes)
    _caption(fig, spec, y=0.02)
    return fig


def _svg_shell(spec: dict[str, Any], width: int, height: int, body: str, *, defs: str = "") -> str:
    title = _esc(str(spec.get("title") or "PxFquery figure"))
    caption = _esc(str(spec.get("caption") or ""))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{title}</title>
{defs}
<style>
  .title {{ font: 700 18px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #1f2933; }}
  .label {{ font: 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #263241; }}
  .value {{ font: 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4b5563; }}
  .small {{ font: 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #334155; }}
  .axis {{ font: 11px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #64748b; }}
</style>
<rect x="0" y="0" width="{width}" height="{height}" fill="#fbfcfd" rx="8"/>
<text x="20" y="28" class="title">{title}</text>
{body}
<text x="20" y="{height - 12}" class="value">{caption}</text>
</svg>'''


def _arrow_def() -> str:
    return '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#64748b"/></marker></defs>'


def _direction_color(value: str) -> str:
    value = value.lower()
    if "suppress" in value or "down" in value or "negative" in value:
        return "#33658a"
    if "activ" in value or "up" in value or "positive" in value:
        return "#b23a48"
    if "mixed" in value:
        return "#6b7280"
    return "#7a9e7e"


def _title_label(value: Any) -> str:
    return str(value).replace("_", " ").title()


def _has_non_ascii(value: Any) -> bool:
    return any(ord(char) > 127 for char in str(value or ""))


def _plot_label(value: Any, fallback: str) -> str:
    text = str(value or "").strip()
    if not text or _has_non_ascii(text):
        return fallback
    return text


def _normalize_function_source(value: Any) -> str:
    text = str(value or "").strip().lower().replace("-", "_")
    if text in {"hallmark", "h"}:
        return "hallmark"
    if text in {"3ca_mps", "3ca_mp", "3ca", "mps", "mp3", "3ca_mp3"}:
        return "3ca_mps"
    return text


def _function_source_title(source: str) -> str:
    if source == "hallmark":
        return "Hallmark"
    if source == "3ca_mps":
        return "3CA MPS"
    return str(source or "Function").replace("_", " ").title()


def _function_source_empty_label(source: str) -> str:
    if source == "hallmark":
        return "No Hallmark Target"
    if source == "3ca_mps":
        return "No 3CA MPS Target"
    return "No Target"


def _function_universe(source: str) -> list[dict[str, str]]:
    index_path = _function_index_path()
    if index_path is None:
        return []
    try:
        data = json.loads(index_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    rows: list[dict[str, str]] = []
    wanted = _normalize_function_source(source)
    if "var_names" in data and "meta" in data:
        for var_name in data.get("var_names") or []:
            meta = (data.get("meta") or {}).get(var_name) or {}
            if _normalize_function_source(meta.get("source")) != wanted:
                continue
            rows.append(
                {
                    "var_name": str(var_name),
                    "label": _function_display_label(str(meta.get("label") or var_name), var_name, wanted),
                }
            )
    else:
        for var_name, meta in (data.get("functions") or {}).items():
            if _normalize_function_source(meta.get("source")) != wanted:
                continue
            rows.append(
                {
                    "var_name": str(var_name),
                    "label": _function_display_label(str(meta.get("label") or var_name), var_name, wanted),
                }
            )
    return rows


def _function_index_path() -> Path | None:
    candidates: list[Path] = []
    env_root = os.environ.get("PXFQUERY_RESOURCE_DIR")
    if env_root:
        candidates.append(Path(env_root).expanduser() / "function_index.json")
    try:
        from pxfquery.resources.manager import DEFAULT_CACHE_DIR, default_manifest

        manifest = default_manifest()
        file_info = (manifest.get("files") or {}).get("l2.function_index") or {}
        rel = file_info.get("path") or file_info.get("filename") or "function_index.json"
        cache_subdir = str(manifest.get("cache_subdir") or manifest.get("version") or manifest.get("resource_version") or "default")
        candidates.append(DEFAULT_CACHE_DIR / cache_subdir / rel)
    except Exception:
        pass
    for path in candidates:
        if path.exists():
            return path
    return None


def _function_display_label(label: str, var_name: Any, source: str) -> str:
    text = _plot_label(label or var_name, "Function")
    raw = str(var_name or text)
    if source == "hallmark":
        text = raw.replace("HALLMARK_", "").replace("_", " ").title()
    elif source == "3ca_mps":
        text = raw.replace("3CA_MPS_", "").replace("3CA_MP_", "").replace("MP_", "").replace("_", " ")
        text = re.sub(r"^\s*MPS?\s*\d+\s*[-_:.)]*\s*", "", text, flags=re.IGNORECASE)
        text = re.sub(r"^\s*\d+\s*[-_:.)]+\s*", "", text)
        text = text.title()
    return _plot_label(text, "Function")


def _reverse_target_color(value: float, direction: str, max_abs: float) -> str:
    if abs(value) <= 0:
        return "#ffffff"
    intensity = 0.32 + min(abs(value) / max(max_abs, 1e-9), 1.0) * 0.62
    direction_text = str(direction or "").lower()
    if value < 0 or "suppress" in direction_text or "down" in direction_text:
        return _blend_with_white("#33658a", intensity)
    return _blend_with_white("#b23a48", intensity)


def _blend_with_white(hex_color: str, intensity: float) -> str:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    amount = min(max(intensity, 0.0), 1.0)
    rr = int(255 * (1 - amount) + r * amount)
    gg = int(255 * (1 - amount) + g * amount)
    bb = int(255 * (1 - amount) + b * amount)
    return f"#{rr:02x}{gg:02x}{bb:02x}"


def _heat_color(value: float, intensity: float) -> str:
    alpha = 0.22 + min(max(intensity, 0.0), 1.0) * 0.68
    if value < 0:
        return f"rgba(51, 101, 138, {alpha:.2f})"
    return f"rgba(178, 58, 72, {alpha:.2f})"


def _palette(values: list[str]) -> dict[str, str]:
    colors = [
        "#33658a",
        "#b23a48",
        "#7a9e7e",
        "#6d597a",
        "#e09f3e",
        "#2a9d8f",
        "#9b5de5",
        "#577590",
        "#bc6c25",
        "#4d908e",
        "#a44a3f",
        "#277da1",
    ]
    out: dict[str, str] = {}
    for value in values:
        key = str(value or "unknown")
        if key not in out:
            out[key] = colors[len(out) % len(colors)]
    return out


def _layer_positions(items: list[str], y: float, *, x0: float, x1: float) -> dict[str, tuple[float, float]]:
    if not items:
        return {}
    if len(items) == 1:
        return {items[0]: ((x0 + x1) / 2.0, y)}
    step = (x1 - x0) / max(len(items) - 1, 1)
    return {item: (x0 + step * idx, y) for idx, item in enumerate(items)}


def _draw_route_graph_node(
    ax: Any,
    xy: tuple[float, float],
    label: str,
    face: str,
    edge: str,
    *,
    size: int,
    fs: float,
    max_line: int,
    yoff: float,
) -> None:
    x, y = xy
    ax.scatter([x], [y], s=size, facecolor=face, edgecolor=edge, linewidth=1.45, zorder=4)
    ax.text(
        x,
        y - yoff,
        _wrap_label(label, max_line=max_line, max_lines=2),
        ha="center",
        va="top",
        fontsize=fs,
        zorder=5,
        linespacing=1.02,
        color="#111827",
    )


def _wrap_label(value: Any, *, max_line: int, max_lines: int) -> str:
    text = _plot_label(str(value or ""), "Label").replace("HALLMARK_", "").replace("_", " ").strip()
    words = text.split()
    if not words:
        return ""
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if len(candidate) <= max_line:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max(max_line - 3, 1)].rstrip() + "..."
    return "\n".join(lines)


def _is_direct_match_type(value: str) -> bool:
    text = str(value or "").lower()
    return text.startswith(("user", "normalized", "exact")) or "specified" in text


def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value).strip("_") or "figure"


def _short(value: Any, max_len: int) -> str:
    text = str(value)
    return text if len(text) <= max_len else text[: max_len - 3] + "..."


def _short_route_label(cell: str, perturbation: str) -> str:
    cell = cell.strip()
    perturbation = perturbation.strip()
    if not perturbation or perturbation.startswith("BRD-"):
        return _short(cell or perturbation or "route", 16)
    return _short(f"{cell}/{perturbation}" if cell else perturbation, 20)


def _esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _numeric(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _pyplot():
    import matplotlib

    matplotlib.use("Agg", force=True)
    matplotlib.rcParams["pdf.fonttype"] = 42
    matplotlib.rcParams["ps.fonttype"] = 42
    matplotlib.rcParams["font.sans-serif"] = [
        "Arial Unicode MS",
        "Heiti TC",
        "STHeiti",
        "Hiragino Sans GB",
        "Songti SC",
        "DejaVu Sans",
    ]
    matplotlib.rcParams["axes.unicode_minus"] = False
    import matplotlib.pyplot as plt

    return plt


def _caption(fig: Any, spec: dict[str, Any], *, y: float = 0.01) -> None:
    caption = str(spec.get("caption") or "")
    if caption:
        fig.text(0.01, y, caption, fontsize=8, color="#4b5563")
    fig.tight_layout(rect=(0, 0.04, 1, 0.96))


def _close_matplotlib_figure(fig: Any) -> None:
    plt = _pyplot()
    plt.close(fig)
