from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from pxfquery.l3_execution.matrix_store import FunctionalMatrix, FunctionalMatrixStore
from pxfquery.l3_execution.schema import L3ExecutionResult, L3RouteExecutionResult
from pxfquery.resources import ResourceManager


def execute_route_plan(
    route_plan: Any,
    *,
    resources: ResourceManager,
    resource_dir: str | Path | None = None,
    auto_download: bool = True,
    top_n: int = 20,
) -> L3ExecutionResult:
    if resource_dir is not None:
        resources.use(resource_dir, strict=False)
    route = _route_to_dict(route_plan)
    query_id = route.get("query_id")
    intent = route.get("intent") or {}
    query_type = intent.get("query_type")
    result = L3ExecutionResult(
        query_id=query_id,
        query_type=query_type,
        execution_status="not_started",
        source_route_schema=route.get("schema_version"),
        resource_pack=resources.status().to_dict(),
    )
    if route.get("schema_version") != "l2-route-plan/v2":
        result.execution_status = "schema_mismatch"
        result.errors.append({"code": "schema_mismatch", "message": "expected l2-route-plan/v2"})
        return result
    if route.get("route_status") != "routed":
        result.execution_status = "route_plan_unresolved"
        result.errors.append(
            {
                "code": "route_plan_unresolved",
                "route_status": route.get("route_status"),
                "unresolved_dimensions": route.get("unresolved_dimensions", []),
                "reason": route.get("reason", ""),
            }
        )
        return result

    routes = list((route.get("combination_route") or {}).get("selected_routes") or [])
    if not routes:
        result.execution_status = "no_executable_route"
        result.errors.append({"code": "no_executable_route", "message": "route plan contains no selected routes"})
        return result

    store = FunctionalMatrixStore(
        resources,
        auto_download=auto_download,
        cache=getattr(resources, "_functional_matrix_cache", None),
    )
    for route_item in routes:
        route_results: list[L3RouteExecutionResult] = []
        if query_type == "forward":
            try:
                modalities = _forward_modalities(route_item, route)
            except Exception as exc:
                modalities = []
                route_results.append(_skipped(route_item, query_type, _error_code(exc), str(exc)))
            for modality in modalities:
                try:
                    route_results.append(_execute_forward_route(route_item, route, store, top_n=top_n, modality=modality))
                except Exception as exc:
                    route_results.append(_skipped(route_item, query_type, _error_code(exc), str(exc), modality=modality))
        else:
            try:
                if query_type == "reverse":
                    route_results.append(_execute_reverse_route(route_item, store, top_n=top_n))
                else:
                    route_results.append(_skipped(route_item, query_type, "unsupported_query_type", str(query_type)))
            except Exception as exc:
                route_results.append(_skipped(route_item, query_type, _error_code(exc), str(exc)))
        for route_result in route_results:
            payload = route_result.to_dict()
            if route_result.status == "executed":
                result.executed_routes.append(payload)
            else:
                result.skipped_routes.append(payload)
                result.errors.append({"code": route_result.status, "route_id": route_result.route_id, "message": route_result.diagnostics.get("message", "")})

    result.resource_pack = resources.status().to_dict()
    result.matrix_summary = _matrix_summary(store)
    if result.executed_routes and result.skipped_routes:
        result.execution_status = "partial"
    elif result.executed_routes:
        result.execution_status = "executed"
    else:
        result.execution_status = result.errors[0]["code"] if result.errors else "not_executed"
    return result


def _execute_forward_route(route: dict[str, Any], route_plan: dict[str, Any], store: FunctionalMatrixStore, *, top_n: int, modality: str) -> L3RouteExecutionResult:
    matrix = store.load(modality)
    mask = _row_mask(matrix, cell=route.get("cell"), perturbation=route.get("perturbation"))
    if not bool(mask.any()):
        return _skipped(route, "forward", "empty_matrix_hit", "no rows matched route cell and perturbation", modality=modality)
    X = matrix.X[mask]
    obs = matrix.obs.loc[mask].copy()
    raw_scores = X.mean(axis=0)
    score_multiplier = _score_multiplier(route)
    scores = raw_scores * score_multiplier
    order_desc = np.argsort(-scores)
    order_asc = np.argsort(scores)
    requested = _requested_functions(route_plan)
    requested_scores = {name: float(scores[matrix.var_names.index(name)]) for name in requested if name in matrix.var_names}
    modalities = _forward_modalities(route, route_plan)
    route_id = str(route.get("route_id") or "forward")
    if len(modalities) > 1:
        route_id = f"{route_id}:{modality}"
    return L3RouteExecutionResult(
        route_id=route_id,
        query_type="forward",
        modality=modality,
        status="executed",
        cell=route.get("cell"),
        route_metadata=dict(route),
        row_match={
            "n_rows": int(mask.sum()),
            "sig_ids": obs.get("sig_id", pd.Series(dtype=str)).astype(str).head(50).tolist(),
            "cmap_names": sorted(obs.get("cmap_name", pd.Series(dtype=str)).astype(str).dropna().unique().tolist())[:20],
            "pert_ids": sorted(obs.get("pert_id", pd.Series(dtype=str)).astype(str).dropna().unique().tolist())[:20],
        },
        scores={
            "aggregate": {name: float(value) for name, value in zip(matrix.var_names, scores)},
            "requested_functions": requested_scores,
            "requested_function_records": _score_records(requested_scores),
            "score_orientation": route.get("score_orientation") or "observed_perturbation_effect",
            "score_multiplier": score_multiplier,
            "aggregation": "mean",
        },
        rankings={
            "top_activated": _rank_records(matrix.var_names, scores, order_desc, top_n, positive=True),
            "top_suppressed": _rank_records(matrix.var_names, scores, order_asc, top_n, positive=False),
        },
        diagnostics={"message": "matrix rows matched and scores aggregated"},
    )


def _execute_reverse_route(route: dict[str, Any], store: FunctionalMatrixStore, *, top_n: int) -> L3RouteExecutionResult:
    modality = str(route.get("modality") or "")
    matrix = store.load(modality)
    functions = route.get("functions") or []
    target, warnings = _target_vector(functions, matrix.var_names)
    missing = [f.get("var_name") for f in functions if f.get("var_name") not in matrix.var_names]
    route_id = str(route.get("route_id") or "reverse")
    if missing:
        return _skipped(route, "reverse", "missing_function_column", f"missing function columns: {missing}", modality=modality)
    if not np.any(target):
        return _skipped(route, "reverse", "empty_target_vector", "no nonzero target functions", modality=modality)
    mask = _row_mask(matrix, cell=route.get("cell"), perturbation=None)
    if not bool(mask.any()):
        return _skipped(route, "reverse", "empty_matrix_hit", "no rows matched route cell scope", modality=modality)
    X = np.nan_to_num(np.asarray(matrix.X[mask], dtype=np.float32), nan=0.0, posinf=0.0, neginf=0.0)
    target = np.nan_to_num(np.asarray(target, dtype=np.float32), nan=0.0, posinf=0.0, neginf=0.0)
    obs = matrix.obs.loc[mask].copy()
    raw_n_rows = int(mask.sum())
    X, obs = _aggregate_reverse_replicates(X, obs)
    X, obs, control_filter = _filter_reverse_control_perturbations(X, obs, modality=modality)
    if len(obs) == 0:
        return _skipped(
            route,
            "reverse",
            "no_valid_candidate_after_control_filter",
            "all reverse candidates were filtered as control perturbations",
            modality=modality,
        )
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        projections = np.asarray(X @ target, dtype=np.float32)
    projections = np.nan_to_num(projections, nan=0.0, posinf=0.0, neginf=0.0)
    ranking_mode = str(route.get("reverse_ranking_mode") or "perturbation_only")
    rankings = _reverse_rankings(matrix.var_names, X, obs, target, projections, modality=modality, ranking_mode=ranking_mode, top_n=top_n)
    return L3RouteExecutionResult(
        route_id=route_id,
        query_type="reverse",
        modality=modality,
        status="executed",
        cell=route.get("cell"),
        route_metadata=dict(route),
        row_match={"n_rows": raw_n_rows, "n_ranked_groups": int(len(obs)), "cell_scope": route.get("cell")},
        scores={
            "target_vector": {name: float(value) for name, value in zip(matrix.var_names, target) if value != 0},
            "ranking_method": "signed_dot_projection",
            "interpretation_set_id": route.get("interpretation_set_id"),
            "reverse_ranking_mode": ranking_mode,
        },
        rankings=rankings,
        diagnostics={"message": "reverse route executed", "warnings": warnings, "control_filter": control_filter},
    )


def _row_mask(matrix: FunctionalMatrix, *, cell: str | None, perturbation: str | None) -> np.ndarray:
    obs = matrix.obs
    mask = np.ones(len(obs), dtype=bool)
    if cell:
        if "cell_iname" not in obs:
            return np.zeros(len(obs), dtype=bool)
        mask &= obs["cell_iname"].astype(str).str.upper().to_numpy() == str(cell).upper()
    if perturbation:
        pert_mask = np.zeros(len(obs), dtype=bool)
        for col in ("pert_id", "cmap_name"):
            if col in obs:
                pert_mask |= obs[col].astype(str).str.upper().to_numpy() == str(perturbation).upper()
        mask &= pert_mask
    return mask


def _forward_modalities(route: dict[str, Any], route_plan: dict[str, Any]) -> list[str]:
    record = route.get("perturbation_record") or {}
    if route.get("modality"):
        return [str(route["modality"]).lower()]
    pert = str(route.get("perturbation") or record.get("id") or "")
    if pert.startswith("BRD-") or str(record.get("id", "")).startswith("BRD-"):
        return ["cp"]
    modality = str(((route_plan.get("intent") or {}).get("genetic_modality") or "")).lower()
    if modality in {"rnai", "shrna", "sh", "sirna", "knockdown"}:
        return ["sh"]
    if modality in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion", "xpr"}:
        return ["xpr"]
    if modality in {"overexpression", "gof", "gain_of_function"}:
        return ["xpr", "sh"]
    pert_class = str(((route_plan.get("intent") or {}).get("pert_class") or "")).lower()
    if pert_class == "genetic" or record.get("symbol"):
        return ["xpr", "sh"]
    raise ValueError("unsupported_or_ambiguous_modality: forward route lacks explicit modality")


def _requested_functions(route_plan: dict[str, Any]) -> list[str]:
    selected = ((route_plan.get("function_route") or {}).get("selected")) or []
    return [item.get("var_name") for item in selected if item.get("var_name")]


def _target_vector(functions: list[dict[str, Any]], var_names: list[str]) -> tuple[np.ndarray, list[str]]:
    target = np.zeros(len(var_names), dtype=np.float32)
    warnings = []
    index = {name: i for i, name in enumerate(var_names)}
    for item in functions:
        name = item.get("var_name")
        if name not in index:
            continue
        direction = str(item.get("direction") or "target").lower()
        weight = float(item.get("weight", 1.0) or 1.0)
        if direction in {"suppress", "suppression", "down", "negative"}:
            value = -weight
        elif direction in {"activate", "activation", "up", "positive", "target"}:
            value = weight
        else:
            value = weight
            warnings.append(f"direction_unknown_assumed_positive:{name}:{direction}")
        target[index[name]] = value
    return target, warnings


def _aggregate_reverse_replicates(X: np.ndarray, obs: pd.DataFrame) -> tuple[np.ndarray, pd.DataFrame]:
    if len(obs) <= 1:
        out = obs.reset_index(drop=True).copy()
        out["n_signatures"] = len(out)
        return X, out
    frame = obs.reset_index(drop=True).copy()
    if "cmap_name" in frame:
        pert_key = frame["cmap_name"].astype(str)
    elif "pert_id" in frame:
        pert_key = frame["pert_id"].astype(str)
    else:
        pert_key = pd.Series([str(i) for i in range(len(frame))])
    if "pert_id" in frame:
        pert_key = pert_key.mask(pert_key.isin({"", "nan", "None"}), frame["pert_id"].astype(str))
    frame["_reverse_perturbation_key"] = pert_key
    frame["_reverse_cell_key"] = frame["cell_iname"].astype(str) if "cell_iname" in frame else ""
    groups = frame.groupby(["_reverse_perturbation_key", "_reverse_cell_key"], sort=False, dropna=False).indices
    agg_rows = []
    agg_X = []
    for (_, _), indices in groups.items():
        idx = np.asarray(list(indices), dtype=int)
        first = frame.iloc[int(idx[0])].copy()
        first["n_signatures"] = int(len(idx))
        if "sig_id" in frame:
            first["sig_ids"] = [str(v) for v in frame.iloc[idx]["sig_id"].dropna().tolist()]
        agg_rows.append(first.drop(labels=["_reverse_perturbation_key", "_reverse_cell_key"], errors="ignore"))
        agg_X.append(np.mean(X[idx], axis=0))
    return np.asarray(agg_X, dtype=np.float32), pd.DataFrame(agg_rows).reset_index(drop=True)


def _filter_reverse_control_perturbations(X: np.ndarray, obs: pd.DataFrame, *, modality: str) -> tuple[np.ndarray, pd.DataFrame, dict[str, Any]]:
    if modality not in {"sh", "xpr"} or obs.empty:
        return X, obs, {"enabled": modality in {"sh", "xpr"}, "filtered_groups": 0, "patterns": ["CSS001*"]}
    control_mask = np.zeros(len(obs), dtype=bool)
    for col in ("pert_id", "cmap_name"):
        if col in obs:
            values = obs[col].astype(str).str.upper()
            control_mask |= values.str.startswith("CSS001").to_numpy()
    kept = ~control_mask
    filtered = int(control_mask.sum())
    if filtered == 0:
        return X, obs, {"enabled": True, "filtered_groups": 0, "patterns": ["CSS001*"]}
    return (
        X[kept],
        obs.loc[kept].reset_index(drop=True),
        {
            "enabled": True,
            "filtered_groups": filtered,
            "remaining_groups": int(kept.sum()),
            "patterns": ["CSS001*"],
        },
    )


def _score_multiplier(route: dict[str, Any]) -> int:
    value = route.get("score_multiplier")
    if value is None:
        value = (route.get("perturbation_anchor") or {}).get("score_multiplier")
    try:
        multiplier = int(value)
    except (TypeError, ValueError):
        multiplier = 1
    return -1 if multiplier < 0 else 1


def _reverse_rankings(
    var_names: list[str],
    X: np.ndarray,
    obs: pd.DataFrame,
    target: np.ndarray,
    projections: np.ndarray,
    *,
    modality: str,
    ranking_mode: str,
    top_n: int,
) -> dict[str, list[dict[str, Any]]]:
    if modality not in {"sh", "xpr"}:
        return {"top_perturbations": _projection_records(var_names, X, obs, target, projections, np.argsort(-projections)[:top_n], "drug_treat", 1, top_n)}
    rankings: dict[str, list[dict[str, Any]]] = {}
    if ranking_mode in {"perturbation_only", "bidirectional"}:
        rankings["top_loss_of_function_perturbations"] = _projection_records(
            var_names,
            X,
            obs,
            target,
            projections,
            np.argsort(-projections)[:top_n],
            "inhibit_or_knockout_gene",
            1,
            top_n,
        )
    if ranking_mode in {"activation_only", "bidirectional"}:
        rankings["top_activating_perturbations_inferred"] = _projection_records(
            var_names,
            X,
            obs,
            target,
            projections,
            np.argsort(projections)[:top_n],
            "activate_or_increase_gene",
            -1,
            top_n,
        )
    if "top_loss_of_function_perturbations" in rankings:
        rankings["top_perturbations"] = rankings["top_loss_of_function_perturbations"]
    elif "top_activating_perturbations_inferred" in rankings:
        rankings["top_perturbations"] = rankings["top_activating_perturbations_inferred"]
    return rankings


def _projection_records(
    var_names: list[str],
    X: np.ndarray,
    obs: pd.DataFrame,
    target: np.ndarray,
    projections: np.ndarray,
    order: np.ndarray,
    recommended_operation: str,
    orientation: int,
    top_n: int,
) -> list[dict[str, Any]]:
    records = []
    for idx in order[:top_n]:
        row = obs.iloc[int(idx)]
        raw_projection = float(projections[int(idx)])
        # order is sorted so once sign flips all remaining entries also flip
        if orientation == 1 and raw_projection <= 0:
            break
        if orientation == -1 and raw_projection >= 0:
            break
        oriented_projection = raw_projection * orientation
        oriented_effect = X[int(idx)] * orientation
        records.append(
            {
                "rank": len(records) + 1,
                "score": oriented_projection,
                "raw_projection": raw_projection,
                "recommended_operation": recommended_operation,
                "score_orientation": "observed_perturbation_effect" if orientation == 1 else "inferred_activation_from_opposite_lof_effect",
                "sig_id": _safe_value(row, "sig_id"),
                "pert_id": _safe_value(row, "pert_id"),
                "cmap_name": _safe_value(row, "cmap_name"),
                "cell_iname": _safe_value(row, "cell_iname"),
                "label": _safe_value(row, "cmap_name") or _safe_value(row, "pert_id"),
                "driving_terms": _driving_terms(var_names, oriented_effect * target, top_n=5),
            }
        )
    return records


def _rank_records(var_names: list[str], scores: np.ndarray, order: np.ndarray, top_n: int, *, positive: bool) -> list[dict[str, Any]]:
    rows = []
    for idx in order:
        score = float(scores[int(idx)])
        if positive and score <= 0:
            continue
        if not positive and score >= 0:
            continue
        function = var_names[int(idx)]
        rows.append(
            {
                "rank": len(rows) + 1,
                "label": function,
                "function": function,
                "score": score,
                "direction": "activated" if positive else "suppressed",
            }
        )
        if len(rows) >= top_n:
            break
    return rows


def _driving_terms(var_names: list[str], contributions: np.ndarray, *, top_n: int) -> list[dict[str, Any]]:
    order = np.argsort(-np.abs(contributions))[:top_n]
    return [
        {
            "rank": rank,
            "label": var_names[int(idx)],
            "function": var_names[int(idx)],
            "contribution": float(contributions[int(idx)]),
        }
        for rank, idx in enumerate(order, start=1)
        if float(contributions[int(idx)]) != 0.0
    ][:top_n]


def _score_records(scores: dict[str, float]) -> list[dict[str, Any]]:
    return [
        {
            "rank": rank,
            "label": name,
            "function": name,
            "score": float(value),
        }
        for rank, (name, value) in enumerate(scores.items(), start=1)
    ]


def _skipped(route: dict[str, Any], query_type: str | None, status: str, message: str, *, modality: str | None = None) -> L3RouteExecutionResult:
    return L3RouteExecutionResult(
        route_id=str(route.get("route_id") or "unknown"),
        query_type=str(query_type),
        modality=modality or route.get("modality"),
        status=status,
        cell=route.get("cell"),
        route_metadata=dict(route),
        diagnostics={"message": message},
    )


def _route_to_dict(route_plan: Any) -> dict[str, Any]:
    if isinstance(route_plan, dict):
        return route_plan
    if hasattr(route_plan, "to_dict"):
        return route_plan.to_dict()
    raise TypeError(f"unsupported route_plan type: {type(route_plan)!r}")


def _safe_value(row: pd.Series, key: str) -> Any:
    value = row.get(key)
    if pd.isna(value):
        return None
    return value.item() if hasattr(value, "item") else value


def _matrix_summary(store: FunctionalMatrixStore) -> dict[str, Any]:
    return {
        modality: {
            "shape": list(matrix.X.shape),
            "matrix_path": matrix.matrix_path,
            "obs_path": matrix.obs_path,
            "var_path": matrix.var_path,
        }
        for modality, matrix in store._cache.items()
    }


def _error_code(exc: Exception) -> str:
    text = str(exc)
    for code in [
        "resource_missing",
        "checksum_failed",
        "schema_mismatch",
        "unsupported_modality",
        "unsupported_or_ambiguous_modality",
    ]:
        if code in text:
            return code
    if isinstance(exc, FileNotFoundError):
        return "resource_missing"
    if isinstance(exc, ValueError):
        return "schema_mismatch" if "schema_mismatch" in text else "invalid_route"
    return "execution_error"
