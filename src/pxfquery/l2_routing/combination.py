from __future__ import annotations

from pathlib import Path
from typing import Any

from pxfquery.l1_intent import QueryIntent


MAX_CELL_CANDIDATES = 6
MAX_PERTURBATION_PROXIES = 5
MAX_REVERSE_INTERPRETATION_SETS = 3
MAX_REVERSE_FUNCTIONS_PER_SET = 3
MAX_PAIR_CHECKS = 25
MAX_SELECTED_ROUTES = 6
MAX_EXPANDED_CELL_CANDIDATES = 25
MAX_EXPANDED_PERTURBATION_PROXIES = 50
MODALITIES = ("cp", "sh", "xpr")


def route_combinations(
    intent: QueryIntent,
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    function_route: dict[str, Any],
    *,
    forward_engines: dict[str, Any] | None = None,
    reverse_engines: dict[str, Any] | None = None,
    resources: Any | None = None,
    pair_policy: str = "observed",
) -> dict[str, Any]:
    pair_policy = _normalize_pair_policy(pair_policy)
    cell_candidates = cell_route.get("candidates") or [{"cell": None, "role": "all-cells"}]
    if intent.query_type == "forward":
        selected_pert = perturbation_route.get("selected", [])
        proxy_pert = perturbation_route.get("proxies", [])
        tiers = [
            {"tier": "exact_cell_exact_perturbation", "cell_role": "exact", "perturbation_role": "exact"},
            {"tier": "exact_cell_proxy_perturbation", "cell_role": "exact", "perturbation_role": "proxy"},
            {"tier": "proxy_cell_exact_perturbation", "cell_role": "proxy", "perturbation_role": "exact"},
            {"tier": "proxy_cell_proxy_perturbation", "cell_role": "proxy", "perturbation_role": "proxy"},
        ]
        pair_metadata = _load_pair_metadata(resources) if pair_policy == "observed" else None
        route_candidates = _rank_routes_by_quality(_forward_route_candidates(cell_route, perturbation_route, intent, pair_metadata))
        pair_availability = _pair_availability_forward(route_candidates, forward_engines, pair_metadata, pair_policy)
        status = _combination_status(bool(selected_pert or proxy_pert), pair_availability)
        return {
            "status": status,
            "query_type": "forward",
            "pair_policy": pair_policy,
            "tier_order": tiers,
            "route_candidates": route_candidates,
            "selected_routes": _selected_available_routes(route_candidates, pair_availability),
            "candidate_limits": {
                "max_cell_candidates": MAX_CELL_CANDIDATES,
                "max_perturbation_proxies": MAX_PERTURBATION_PROXIES,
                "max_expanded_cell_candidates": MAX_EXPANDED_CELL_CANDIDATES,
                "max_expanded_perturbation_proxies": MAX_EXPANDED_PERTURBATION_PROXIES,
                "max_pair_checks": MAX_PAIR_CHECKS,
                "max_selected_routes": MAX_SELECTED_ROUTES,
            },
            "pair_availability": pair_availability,
        }
    pair_metadata = _load_pair_metadata(resources) if pair_policy == "observed" else None
    route_candidates = _rank_routes_by_quality(_reverse_route_candidates(cell_route, function_route, intent, pair_metadata))
    pair_availability = _pair_availability_reverse(route_candidates, function_route, reverse_engines, pair_metadata, pair_policy)
    return {
        "status": _combination_status(bool(function_route.get("selected")), pair_availability),
        "query_type": "reverse",
        "pair_policy": "observed_cell_scope" if pair_metadata else "cell_scope_only",
        "cell_candidate_count": len(cell_candidates),
        "function_set_count": len(function_route.get("interpretation_sets", [])),
        "route_candidates": route_candidates,
        "selected_routes": _selected_available_routes(route_candidates, pair_availability),
        "candidate_limits": {
            "max_cell_candidates": MAX_CELL_CANDIDATES,
            "default_interpretation_sets": MAX_REVERSE_INTERPRETATION_SETS,
            "max_functions_per_set": MAX_REVERSE_FUNCTIONS_PER_SET,
            "max_selected_routes": MAX_SELECTED_ROUTES,
        },
        "pair_availability": pair_availability,
    }


def _forward_route_candidates(
    cell_route: dict[str, Any],
    perturbation_route: dict[str, Any],
    intent: QueryIntent,
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
) -> list[dict[str, Any]]:
    use_pair_metadata = bool(pair_metadata)
    cells = (cell_route.get("expanded_candidates") if use_pair_metadata else None) or cell_route.get("candidates", [])
    cells = cells[:MAX_EXPANDED_CELL_CANDIDATES if use_pair_metadata else MAX_CELL_CANDIDATES]
    normal_lineage_anchor_cells = [c for c in cells if c.get("cell_expansion_scope") == "normal_lineage_data_anchor"]
    if use_pair_metadata:
        cells = [c for c in cells if c.get("cell_expansion_scope") != "normal_lineage_data_anchor"]
    exact_cells = [c for c in cells if c.get("role") in {"exact", "all-cells"}][:1]
    representative_cells = [c for c in cells if c.get("role") == "llm-tree-leaf"]
    proxy_cells = [c for c in cells if c not in exact_cells and c not in representative_cells]
    exact_perts = perturbation_route.get("selected", [])[:1]
    proxy_source = (perturbation_route.get("expanded_proxies") if use_pair_metadata else None) or perturbation_route.get("proxies", [])
    proxy_perts = proxy_source[:MAX_EXPANDED_PERTURBATION_PROXIES if use_pair_metadata else MAX_PERTURBATION_PROXIES]
    stages = [
        ("A", "exact_cell_exact_perturbation", exact_cells, exact_perts),
        ("R", "representative_cell_representative_perturbation", representative_cells, exact_perts),
        ("B", "exact_cell_proxy_perturbation", exact_cells, proxy_perts),
        ("S", "representative_cell_proxy_perturbation", representative_cells, proxy_perts),
        ("C", "proxy_cell_exact_perturbation", proxy_cells, exact_perts),
        ("D", "proxy_cell_proxy_perturbation", proxy_cells, proxy_perts),
    ]
    out: list[dict[str, Any]] = []
    for stage, tier, stage_cells, stage_perts in stages:
        for cell in stage_cells:
            for pert in stage_perts:
                modalities = _forward_modalities(intent, pert)
                matched_modalities = _pair_metadata_modalities(pair_metadata, cell.get("cell"), pert, modalities) if use_pair_metadata else modalities
                if use_pair_metadata:
                    matched_modalities = _select_primary_or_fallback_modalities(intent, matched_modalities)
                if use_pair_metadata and not matched_modalities:
                    continue
                out.append(_make_forward_route(intent, len(out) + 1, stage, tier, cell, pert, matched_modalities, use_pair_metadata))
                if len(out) >= MAX_PAIR_CHECKS:
                    return out
    if use_pair_metadata and not out and normal_lineage_anchor_cells:
        for stage, tier, stage_cells, stage_perts in [
            ("E", "normal_lineage_anchor_exact_perturbation", normal_lineage_anchor_cells, exact_perts),
            ("F", "normal_lineage_anchor_proxy_perturbation", normal_lineage_anchor_cells, proxy_perts),
        ]:
            for cell in stage_cells:
                for pert in stage_perts:
                    modalities = _forward_modalities(intent, pert)
                    matched_modalities = _select_primary_or_fallback_modalities(
                        intent,
                        _pair_metadata_modalities(pair_metadata, cell.get("cell"), pert, modalities),
                    )
                    if not matched_modalities:
                        continue
                    out.append(_make_forward_route(intent, len(out) + 1, stage, tier, cell, pert, matched_modalities, use_pair_metadata))
                    if len(out) >= MAX_PAIR_CHECKS:
                        return out
    if use_pair_metadata and not out:
        for stage, tier, stage_perts in [
            ("G", "observed_anchor_exact_perturbation", exact_perts),
            ("H", "observed_anchor_proxy_perturbation", proxy_perts),
        ]:
            for pert in stage_perts:
                modalities = _forward_modalities(intent, pert)
                for cell in _observed_anchor_cells(pair_metadata, pert, modalities):
                    matched_modalities = _select_primary_or_fallback_modalities(
                        intent,
                        _pair_metadata_modalities(pair_metadata, cell.get("cell"), pert, modalities),
                    )
                    if not matched_modalities:
                        continue
                    out.append(_make_forward_route(intent, len(out) + 1, stage, tier, cell, pert, matched_modalities, use_pair_metadata))
                    if len(out) >= MAX_PAIR_CHECKS:
                        return out
    return out


def _make_forward_route(
    intent: QueryIntent,
    route_number: int,
    stage: str,
    tier: str,
    cell: dict[str, Any],
    pert: dict[str, Any],
    matched_modalities: list[str],
    use_pair_metadata: bool,
) -> dict[str, Any]:
    anchor = _perturbation_anchor(intent, pert, matched_modalities)
    cell_distance = _cell_match_distance(cell)
    pert_distance = _perturbation_match_distance(pert)
    modality_evidence = _modality_evidence(intent, pert, matched_modalities)
    primary_modality = _primary_modality_evidence(modality_evidence)
    modality_distance = _modality_match_distance(primary_modality)
    route_quality = _route_quality(cell_distance, pert_distance)
    route = {
        "route_id": f"forward_{route_number:03d}",
        "stage": stage,
        "tier": tier,
        "cell": cell.get("cell"),
        "cell_role": cell.get("role"),
        "cell_expansion_scope": cell.get("cell_expansion_scope", "public_candidates"),
        "cell_route_distance": cell.get("cell_route_distance", 0 if cell.get("role") in {"exact", "llm-tree-leaf"} else 1),
        "cell_match_type": _cell_match_type(cell),
        "cell_match_distance": cell_distance,
        "source_disease": cell.get("source_disease"),
        "candidate_disease": cell.get("candidate_disease"),
        "perturbation": _perturbation_key(pert),
        "perturbation_role": pert.get("role"),
        "perturbation_expansion_scope": _perturbation_expansion_scope(pert),
        "perturbation_source_rank": pert.get("rank"),
        "perturbation_match_type": _perturbation_match_type(pert),
        "perturbation_match_distance": pert_distance,
        "perturbation_record": pert,
        "modalities": matched_modalities,
        "modality_evidence": modality_evidence,
        "modality_match_type": primary_modality.get("modality_match_type"),
        "modality_rank": primary_modality.get("modality_rank"),
        "modality_match_distance": modality_distance,
        "modality_reason": primary_modality.get("reason"),
        "requested_modality": primary_modality.get("requested_modality"),
        "perturbation_anchor": anchor,
        "score_orientation": anchor["score_orientation"],
        "score_multiplier": anchor["score_multiplier"],
        "recommended_operation": anchor["recommended_operation"],
        "pair_search_round": _pair_search_round(cell, pert),
        "pair_search_reason": _pair_search_reason(stage),
        "pair_verified": bool(use_pair_metadata),
        "pair_verification_source": "l3_obs_min" if use_pair_metadata else None,
        "evidence_level": _evidence_level(cell.get("role"), pert.get("role"), cell.get("cell_expansion_scope")),
        "semantic_downgrade_reason": cell.get("semantic_downgrade_reason"),
        "route_quality_score": route_quality,
        "route_quality": _route_quality_label(route_quality),
    }
    if len(matched_modalities) == 1:
        route["modality"] = matched_modalities[0]
    return route


def _pair_search_reason(stage: str) -> str:
    if stage == "A":
        return "exact_or_initial_pair_available"
    if stage in {"E", "F"}:
        return "no_observed_pair_in_cancer_context; using normal same-lineage data anchor with explicit semantic downgrade"
    if stage in {"G", "H"}:
        return "no_observed_pair_in_routed_cell_context; using observed perturbation anchor cell with explicit weak-evidence label"
    return "strict_pair_unavailable_or_additional_observed_evidence"


def _reverse_route_candidates(
    cell_route: dict[str, Any],
    function_route: dict[str, Any],
    intent: QueryIntent,
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
) -> list[dict[str, Any]]:
    use_pair_metadata = bool(pair_metadata)
    cells = (cell_route.get("expanded_candidates") if use_pair_metadata else None) or cell_route.get("candidates", [])
    cells = cells[:MAX_EXPANDED_CELL_CANDIDATES if use_pair_metadata else MAX_CELL_CANDIDATES] or [{"cell": None, "role": "all-cells"}]
    sets = function_route.get("interpretation_sets") or [{"set_id": "selected", "functions": function_route.get("selected", [])}]
    modalities = _reverse_modalities(intent)
    out: list[dict[str, Any]] = []
    for interp in sets[:MAX_REVERSE_INTERPRETATION_SETS]:
        for cell in cells:
            for modality in modalities:
                if use_pair_metadata and not _pair_metadata_has_cell(pair_metadata, modality, cell.get("cell")):
                    continue
                out.append(_make_reverse_route(len(out) + 1, cell, interp, modality, use_pair_metadata, intent))
                if len(out) >= MAX_PAIR_CHECKS:
                    return out
    if use_pair_metadata and not out:
        for interp in sets[:MAX_REVERSE_INTERPRETATION_SETS]:
            for modality in modalities:
                for cell in _observed_modality_anchor_cells(pair_metadata, modality):
                    out.append(_make_reverse_route(len(out) + 1, cell, interp, modality, use_pair_metadata, intent))
                    if len(out) >= MAX_PAIR_CHECKS:
                        return out
    return out


def _make_reverse_route(
    route_number: int,
    cell: dict[str, Any],
    interpretation_set: dict[str, Any],
    modality: str,
    use_pair_metadata: bool,
    intent: QueryIntent,
) -> dict[str, Any]:
    role = cell.get("role")
    evidence = "observed_modality_anchor" if role == "observed-anchor" else "function-set-and-observed-cell-scope" if use_pair_metadata else "function-set-and-cell-scope"
    reverse_mode = _genetic_reverse_mode(modality, intent)
    cell_distance = _cell_match_distance(cell)
    route_quality = _route_quality(cell_distance, 0.0)
    return {
        "route_id": f"reverse_{route_number:03d}",
        "cell": cell.get("cell"),
        "cell_role": role,
        "cell_expansion_scope": cell.get("cell_expansion_scope"),
        "cell_route_distance": cell.get("cell_route_distance"),
        "cell_match_type": _cell_match_type(cell),
        "cell_match_distance": cell_distance,
        "interpretation_set_id": interpretation_set.get("set_id"),
        "functions": interpretation_set.get("functions", [])[:MAX_REVERSE_FUNCTIONS_PER_SET],
        "modality": modality,
        "reverse_ranking_mode": reverse_mode,
        "pair_search_round": "observed_modality_anchor_cell" if role == "observed-anchor" else "observed_cell_scope" if use_pair_metadata else None,
        "pair_search_reason": "reverse route cell has observed rows for requested modality" if role != "observed-anchor" else "no routed cell-context rows for requested reverse modality; using observed modality anchor cell with explicit weak-evidence label",
        "pair_verified": bool(use_pair_metadata),
        "pair_verification_source": "l3_obs_min" if use_pair_metadata else None,
        "evidence_level": evidence,
        "route_quality_score": route_quality,
        "route_quality": _route_quality_label(route_quality),
    }


def _combination_status(has_required_axis: bool, pair_availability: dict[str, Any]) -> str:
    if not has_required_axis:
        return "blocked-by-required-axis"
    if pair_availability.get("status") == "observed_pair_metadata_missing":
        return "resource-missing"
    if pair_availability.get("status") in {"checked", "checked_l3_obs_min"} and pair_availability.get("any_available") is False:
        return "no_pair_available"
    if pair_availability.get("status") == "checked" and pair_availability.get("all_functions_present") is False:
        return "no_pair_available"
    return "planned"


def _selected_available_routes(route_candidates: list[dict[str, Any]], pair_availability: dict[str, Any]) -> list[dict[str, Any]]:
    checks = {c.get("route_id"): c for c in pair_availability.get("checks", []) if c.get("route_id")}
    selected = []
    for route in route_candidates:
        check = checks.get(route.get("route_id"))
        if check is None or check.get("available", True):
            selected.append(route)
        if len(selected) >= MAX_SELECTED_ROUTES:
            break
    return selected


def _rank_routes_by_quality(routes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ranked = sorted(
        routes,
        key=lambda route: (
            _route_sort_modality_distance(route),
            float(route.get("route_quality_score", 1.0)),
            float(route.get("perturbation_match_distance", 0.0)),
            float(route.get("cell_match_distance", 0.0)),
            int(route.get("perturbation_source_rank") or 999),
            int(route.get("cell_route_distance") or 999),
        ),
    )
    for rank, route in enumerate(ranked, 1):
        route["route_quality_rank"] = rank
    return ranked


def _route_sort_modality_distance(route: dict[str, Any]) -> float:
    requested = str(route.get("requested_modality") or "").casefold()
    if requested not in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion", "xpr"}:
        return 0.0
    try:
        return float(route.get("modality_match_distance", 0.0))
    except (TypeError, ValueError):
        return 0.0


def _pair_availability_forward(
    route_candidates: list[dict[str, Any]],
    engines: dict[str, Any] | None,
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
    pair_policy: str,
) -> dict[str, Any]:
    if pair_policy == "observed" and not pair_metadata:
        return {
            "status": "observed_pair_metadata_missing",
            "checks": [],
            "any_available": False,
            "required_resources": ["cp_obs_min.parquet/csv", "sh_obs_min.parquet/csv", "xpr_obs_min.parquet/csv"],
            "message": "observed pair policy requires L3 obs_min metadata resources; pass pair_policy='global' only when theoretical routes are intended",
        }
    if pair_metadata:
        checks = [{**route, "available": True, "reject_reason": None} for route in route_candidates[:MAX_PAIR_CHECKS]]
        return {
            "status": "checked_l3_obs_min",
            "checks": checks,
            "any_available": bool(checks),
            "checked_modalities": sorted(pair_metadata),
            "pair_metadata_policy": "route_candidates are prefiltered to observed (cell, perturbation) pairs from L3 obs_min metadata resources",
        }
    if not engines:
        return {"status": "not_checked_no_loaded_matrix_engine"}
    checks = []
    for route in route_candidates[:MAX_PAIR_CHECKS]:
        for pert_type, engine in engines.items():
            if not _route_modality_matches(pert_type, route.get("perturbation_record")):
                continue
            obs = getattr(getattr(engine, "adata", None), "obs", None)
            available = _obs_has_pair(obs, route.get("cell"), route.get("perturbation")) if obs is not None else False
            checks.append({**route, "pert_type": pert_type, "available": available, "reject_reason": None if available else "pair not present in loaded matrix metadata"})
    return {"status": "checked", "checks": checks, "any_available": any(c["available"] for c in checks)}


def _pair_availability_reverse(
    route_candidates: list[dict[str, Any]],
    function_route: dict[str, Any],
    engines: dict[str, Any] | None,
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
    pair_policy: str,
) -> dict[str, Any]:
    if pair_policy == "observed" and not pair_metadata:
        return {
            "status": "observed_pair_metadata_missing",
            "checks": [],
            "any_available": False,
            "required_resources": ["cp_obs_min.parquet/csv", "sh_obs_min.parquet/csv", "xpr_obs_min.parquet/csv"],
            "message": "observed reverse routing requires obs_min metadata to prefilter cell scope by modality rows",
        }
    if pair_metadata:
        checks = [{**route, "available": True, "reject_reason": None, "cell_available": True} for route in route_candidates[:MAX_PAIR_CHECKS]]
        return {
            "status": "checked_l3_obs_min",
            "checks": checks,
            "any_available": bool(checks),
            "all_functions_present": True,
            "checked_modalities": sorted(pair_metadata),
            "pair_metadata_policy": "reverse route candidates are prefiltered to cells with observed rows for each requested modality",
        }
    if not engines:
        return {"status": "not_checked_no_loaded_matrix_engine"}
    checks = []
    for route in route_candidates[:MAX_PAIR_CHECKS]:
        engine = engines.get(route.get("modality"))
        if engine is None:
            checks.append({**route, "available": False, "reject_reason": "requested modality not loaded"})
            continue
        adata = getattr(engine, "adata", None)
        obs = getattr(getattr(engine, "adata", None), "obs", None)
        var_names = set(map(str, getattr(adata, "var_names", [])))
        functions = [f.get("var_name") for f in route.get("functions", [])]
        functions_present = {f: f in var_names for f in functions}
        cell_available = _obs_has_cell(obs, route.get("cell")) if obs is not None and route.get("cell") else True
        available = bool(functions) and all(functions_present.values()) and cell_available
        checks.append(
            {
                **route,
                "available": available,
                "functions_present": functions_present,
                "cell_available": cell_available,
                "has_cell_filter_columns": obs is not None,
                "reject_reason": None if available else "function columns or cell scope not present in loaded matrix metadata",
            }
        )
    return {
        "status": "checked",
        "checks": checks,
        "any_available": any(c["available"] for c in checks),
        "all_functions_present": all(all(c.get("functions_present", {}).values()) for c in checks) if checks else False,
    }


def _obs_has_pair(obs: Any, cell: str | None, perturbation: str | None) -> bool:
    if cell is None or perturbation is None:
        return False
    try:
        cell_mask = obs["cell_iname"].astype(str).str.upper() == str(cell).upper() if "cell_iname" in obs else True
        pert_mask = False
        for col in ["pert_id", "cmap_name", "target", "gene_symbol"]:
            if col in obs:
                pert_mask = pert_mask | (obs[col].astype(str).str.upper() == str(perturbation).upper())
        return bool((cell_mask & pert_mask).any())
    except Exception:
        return False


def _obs_has_cell(obs: Any, cell: str | None) -> bool:
    if cell is None:
        return True
    try:
        if "cell_iname" not in obs:
            return True
        return bool((obs["cell_iname"].astype(str).str.upper() == str(cell).upper()).any())
    except Exception:
        return False


def _load_pair_metadata(resources: Any | None) -> dict[str, set[tuple[str, str]]] | None:
    if resources is None:
        return None
    out: dict[str, set[tuple[str, str]]] = {}
    for modality in MODALITIES:
        path = getattr(resources, f"{modality}_obs", None)
        pairs = _read_obs_pairs(path, modality=modality)
        if pairs:
            out[modality] = pairs
    return out or None


def _normalize_pair_policy(pair_policy: str) -> str:
    value = str(pair_policy or "observed").lower().strip()
    if value not in {"observed", "global"}:
        raise ValueError("pair_policy must be 'observed' or 'global'")
    return value


def _read_obs_pairs(path: Path | None, *, modality: str) -> set[tuple[str, str]]:
    if path is None or not path.exists():
        return set()
    try:
        import pandas as pd

        obs = pd.read_parquet(path) if path.suffix.lower() == ".parquet" else pd.read_csv(path)
    except Exception:
        return set()
    if "cell_iname" not in obs:
        return set()
    pert_cols = ["pert_id", "cmap_name"] if modality == "cp" else ["cmap_name", "pert_id"]
    pairs: set[tuple[str, str]] = set()
    cells = obs["cell_iname"].astype(str).str.upper()
    for col in pert_cols:
        if col not in obs:
            continue
        perts = obs[col].astype(str).str.upper()
        valid = (cells != "") & (cells != "NAN") & (perts != "") & (perts != "NAN")
        pairs.update(zip(cells[valid].tolist(), perts[valid].tolist(), strict=False))
    return pairs


def _pair_metadata_modalities(
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
    cell: str | None,
    perturbation_record: dict[str, Any] | None,
    modalities: list[str],
) -> list[str]:
    if not pair_metadata or cell is None or perturbation_record is None:
        return []
    perturbation_values = _perturbation_values(perturbation_record)
    if not perturbation_values:
        return []
    cell_key = str(cell).upper()
    matched: list[str] = []
    for modality in modalities:
        pairs = pair_metadata.get(modality)
        if not pairs:
            continue
        if any((cell_key, value) in pairs for value in perturbation_values):
            matched.append(modality)
    return matched


def _cell_match_type(cell: dict[str, Any] | None) -> str:
    if not cell:
        return "all_available_contexts"
    role = str(cell.get("role") or "")
    scope = str(cell.get("cell_expansion_scope") or "")
    if role == "exact":
        return "user_specified_cell"
    if role == "all-cells":
        return "all_available_contexts"
    if role == "llm-tree-leaf":
        return "concept_representative_cell"
    if scope == "same_disease_sibling" or role in {"same_subtype", "same_disease", "same_disease_sibling"}:
        return "same_disease_cell"
    if scope == "same_lineage" or role == "same_lineage":
        return "same_lineage_cell"
    if scope == "normal_lineage_data_anchor":
        return "normal_lineage_data_anchor"
    if role == "observed-anchor":
        return "observed_data_anchor_cell"
    return role or scope or "cell_context_candidate"


def _cell_match_distance(cell: dict[str, Any] | None) -> float:
    if not cell:
        return 0.5
    raw = cell.get("cell_route_distance")
    try:
        base = min(max(float(raw) / 3.0, 0.0), 1.0)
    except (TypeError, ValueError):
        base = 0.5
    role = str(cell.get("role") or "")
    scope = str(cell.get("cell_expansion_scope") or "")
    modifier = 0.0
    if role == "exact":
        modifier -= 0.05
    elif role == "llm-tree-leaf":
        modifier += 0.05
    elif role == "observed-anchor":
        modifier += 0.1
    if scope == "normal_lineage_data_anchor":
        modifier += 0.1
    return round(min(max(base + modifier, 0.0), 1.0), 3)


def _perturbation_match_type(record: dict[str, Any] | None) -> str:
    if not record:
        return "missing_perturbation"
    role = str(record.get("role") or "")
    if role == "exact":
        return "user_specified_perturbation"
    if role == "llm-normalized":
        return "normalized_named_perturbation"
    if role == "mechanism-class-proxy":
        return "mechanism_representative"
    if role == "structural-proxy":
        return "structural_neighbor"
    if role in {"semantic-proxy", "supporting-semantic-neighbor"}:
        return "semantic_neighbor"
    return role or "perturbation_candidate"


def _perturbation_match_distance(record: dict[str, Any] | None) -> float:
    if not record:
        return 1.0
    match_type = _perturbation_match_type(record)
    if match_type in {"user_specified_perturbation", "normalized_named_perturbation"}:
        similarity = 1.0
    elif match_type == "mechanism_representative":
        similarity = 0.95
    elif match_type in {"semantic_neighbor", "structural_neighbor"}:
        try:
            similarity = float(record.get("similarity"))
        except (TypeError, ValueError):
            similarity = 0.25
    else:
        similarity = 0.25
    base = 1.0 - min(max(similarity, 0.0), 1.0)
    modifier = 0.0
    if match_type == "semantic_neighbor":
        modifier -= 0.05
    elif match_type == "structural_neighbor":
        modifier += 0.0
    return round(min(max(base + modifier, 0.0), 1.0), 3)


def _route_quality(cell_distance: float, perturbation_distance: float) -> float:
    return round(min(max((cell_distance + perturbation_distance) / 2.0, 0.0), 1.0), 3)


def _primary_modality_evidence(modality_evidence: list[dict[str, str]]) -> dict[str, str]:
    if not modality_evidence:
        return {
            "modality": "",
            "reason": "missing_modality_evidence",
            "requested_modality": "unspecified",
            "modality_match_type": "missing_modality_evidence",
            "modality_rank": "fallback",
        }
    primary = [item for item in modality_evidence if item.get("modality_rank") == "primary"]
    return (primary or modality_evidence)[0]


def _modality_match_distance(modality_evidence: dict[str, str]) -> float:
    rank = str(modality_evidence.get("modality_rank") or "")
    match_type = str(modality_evidence.get("modality_match_type") or "")
    if rank == "primary" and match_type in {"exact_requested", "unspecified_allowed", "opposite_lof_inference"}:
        return 0.0
    if rank == "primary":
        return 0.1
    if match_type == "loss_of_function_proxy":
        return 0.35
    return 0.45


def _route_quality_label(score: float) -> str:
    if score <= 0.12:
        return "direct_or_close_representative"
    if score <= 0.3:
        return "strong_representative"
    if score <= 0.55:
        return "usable_neighbor"
    if score <= 0.75:
        return "distant_neighbor"
    return "fallback"


def _observed_anchor_cells(
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
    perturbation_record: dict[str, Any] | None,
    modalities: list[str],
) -> list[dict[str, Any]]:
    if not pair_metadata or perturbation_record is None:
        return []
    perturbation_values = set(_perturbation_values(perturbation_record))
    if not perturbation_values:
        return []
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for modality in modalities:
        for cell, perturbation in sorted(pair_metadata.get(modality, set())):
            if perturbation not in perturbation_values or cell in seen:
                continue
            seen.add(cell)
            out.append(
                {
                    "cell": cell,
                    "role": "observed-anchor",
                    "rank": len(out) + 1,
                    "cell_expansion_scope": "observed_perturbation_anchor",
                    "cell_route_distance": 3,
                }
            )
            if len(out) >= MAX_EXPANDED_CELL_CANDIDATES:
                return out
    return out


def _pair_metadata_has_cell(
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
    modality: str,
    cell: str | None,
) -> bool:
    if not pair_metadata or cell is None:
        return False
    cell_key = str(cell).upper()
    return any(observed_cell == cell_key for observed_cell, _perturbation in pair_metadata.get(modality, set()))


def _observed_modality_anchor_cells(
    pair_metadata: dict[str, set[tuple[str, str]]] | None,
    modality: str,
) -> list[dict[str, Any]]:
    if not pair_metadata:
        return []
    cells = sorted({cell for cell, _perturbation in pair_metadata.get(modality, set())})
    out: list[dict[str, Any]] = []
    for cell in cells[:MAX_EXPANDED_CELL_CANDIDATES]:
        out.append(
            {
                "cell": cell,
                "role": "observed-anchor",
                "rank": len(out) + 1,
                "cell_expansion_scope": "observed_modality_anchor",
                "cell_route_distance": 3,
            }
        )
    return out


def _perturbation_values(record: dict[str, Any]) -> list[str]:
    values = []
    for key in ("id", "symbol", "alias"):
        value = record.get(key)
        if value:
            values.append(str(value).upper())
    return list(dict.fromkeys(values))


def _perturbation_expansion_scope(record: dict[str, Any] | None) -> str:
    if not record:
        return "none"
    role = str(record.get("role") or "")
    if role == "exact" or role == "llm-normalized":
        return "exact"
    if "proxy" in role or "neighbor" in role:
        return "semantic_or_structural_neighbor"
    return role or "unknown"


def _pair_search_round(cell: dict[str, Any], perturbation: dict[str, Any]) -> str:
    if cell.get("cell_expansion_scope") == "normal_lineage_data_anchor":
        return "normal_lineage_data_anchor_cell"
    if cell.get("role") == "observed-anchor":
        return "observed_anchor_cell"
    cell_distance = int(cell.get("cell_route_distance") or 0)
    pert_scope = _perturbation_expansion_scope(perturbation)
    exact_pert = pert_scope == "exact"
    if cell_distance == 0 and exact_pert:
        return "strict"
    if cell_distance > 0 and exact_pert:
        return "expand_cell"
    if cell_distance == 0 and not exact_pert:
        return "expand_perturbation"
    return "expand_cell_and_perturbation"


def _modality_evidence(intent: QueryIntent, perturbation_record: dict[str, Any] | None, modalities: list[str]) -> list[dict[str, str]]:
    requested = _normalize_genetic_modality(intent.genetic_modality)
    plan = _genetic_modality_plan(intent)
    out = []
    for modality in modalities:
        if str(perturbation_record.get("id", "") if perturbation_record else "").startswith("BRD-"):
            reason = "compound_perturbation"
            match_type = "exact_requested"
            rank = "primary"
        elif not requested and modality in {"sh", "xpr"}:
            reason = "unspecified_genetic_modality"
            match_type = "unspecified_allowed"
            rank = "primary"
        elif requested in {"rnai", "shrna", "sh", "sirna", "knockdown"} and modality == "sh":
            reason = "requested_knockdown"
            match_type = "exact_requested"
            rank = "primary"
        elif requested in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"} and modality == "xpr":
            reason = "requested_crispr_loss_of_function"
            match_type = "exact_requested"
            rank = "primary"
        elif requested in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"} and modality == "sh":
            reason = "loss_of_function_proxy"
            match_type = "loss_of_function_proxy"
            rank = "fallback"
        elif requested in {"overexpression", "gof", "gain_of_function"} and modality in {"xpr", "sh"}:
            reason = "inferred_activation_from_lof_resource"
            match_type = "opposite_lof_inference"
            rank = "primary"
        else:
            reason = "opposite_modality_fallback"
            match_type = "opposite_modality_fallback"
            rank = "fallback"
        if plan and modality in plan["primary_modalities"]:
            rank = "primary"
        elif plan and modality in plan["fallback_modalities"]:
            rank = "fallback"
        out.append(
            {
                "modality": modality,
                "reason": reason,
                "requested_modality": requested or "unspecified",
                "modality_match_type": match_type,
                "modality_rank": rank,
            }
        )
    return out


def _select_primary_or_fallback_modalities(intent: QueryIntent, modalities: list[str]) -> list[str]:
    plan = _genetic_modality_plan(intent)
    if not _normalize_genetic_modality(intent.genetic_modality):
        return modalities
    primary = [m for m in modalities if m in plan["primary_modalities"]]
    if primary:
        return primary
    return [m for m in modalities if m in plan["fallback_modalities"]]


def _perturbation_key(record: dict[str, Any] | None) -> str | None:
    if not record:
        return None
    return record.get("id") or record.get("symbol") or record.get("alias")


def _forward_modalities(intent: QueryIntent, perturbation_record: dict[str, Any] | None) -> list[str]:
    if not perturbation_record:
        return []
    if str(perturbation_record.get("id", "")).startswith("BRD-"):
        return ["cp"]
    if perturbation_record.get("symbol"):
        plan = _genetic_modality_plan(intent)
        return [*plan["primary_modalities"], *plan["fallback_modalities"]]
    if intent.pert_class == "drug":
        return ["cp"]
    if intent.pert_class == "genetic":
        return ["xpr", "sh"]
    return []


def _genetic_modality_plan(intent: QueryIntent) -> dict[str, list[str]]:
    modality = _normalize_genetic_modality(intent.genetic_modality)
    if not modality:
        return {"primary_modalities": ["sh", "xpr"], "fallback_modalities": []}
    if modality in {"rnai", "shrna", "sh", "sirna", "knockdown"}:
        return {"primary_modalities": ["sh"], "fallback_modalities": ["xpr"]}
    if modality in {"overexpression", "gof", "gain_of_function"}:
        return {"primary_modalities": ["xpr", "sh"], "fallback_modalities": []}
    if modality in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"}:
        return {"primary_modalities": ["xpr"], "fallback_modalities": ["sh"]}
    if modality == "xpr":
        return {"primary_modalities": ["xpr"], "fallback_modalities": ["sh"]}
    return {"primary_modalities": ["sh", "xpr"], "fallback_modalities": []}


def _normalize_genetic_modality(value: str | None) -> str:
    text = _normalize_token(value or "").replace(" ", "_")
    aliases = {
        "loss_of_function": "loss_of_function",
        "loss_function": "loss_of_function",
        "gain_of_function": "gain_of_function",
        "gain_function": "gain_of_function",
        "sirna": "sirna",
        "shrna": "shrna",
    }
    return aliases.get(text, text)


def _route_modality_matches(pert_type: str, perturbation_record: dict[str, Any] | None) -> bool:
    if not perturbation_record:
        return False
    if perturbation_record.get("id", "").startswith("BRD-"):
        return pert_type == "cp"
    if perturbation_record.get("symbol"):
        return pert_type in {"xpr", "sh"}
    return True


def _reverse_modalities(intent: QueryIntent) -> list[str]:
    if intent.pert_class == "drug":
        return ["cp"]
    if intent.pert_class == "genetic":
        modality = _normalize_genetic_modality(intent.genetic_modality)
        if modality in {"rnai", "shrna", "sh", "sirna", "knockdown"}:
            return ["sh"]
        if modality in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion", "xpr"}:
            return ["xpr", "sh"]
        if modality in {"overexpression", "gof", "gain_of_function"}:
            return ["xpr", "sh"]
        return ["xpr", "sh"]
    return ["cp", "xpr", "sh"]


def _perturbation_anchor(intent: QueryIntent, perturbation_record: dict[str, Any] | None, modalities: list[str]) -> dict[str, Any]:
    if perturbation_record and str(perturbation_record.get("id", "")).startswith("BRD-"):
        return {
            "entity_type": "compound",
            "recommended_operation": "drug_treat",
            "score_orientation": "observed_drug_perturbation_effect",
            "score_multiplier": 1,
        }
    requested = _normalize_genetic_modality(intent.genetic_modality)
    activation_requested = requested in {"overexpression", "gof", "gain_of_function"}
    operation = "activate_or_increase_gene" if activation_requested else "inhibit_or_knockdown_gene"
    return {
        "entity_type": "gene",
        "gene": perturbation_record.get("symbol") if perturbation_record else None,
        "recommended_operation": operation,
        "evidence_modality": ",".join(modalities),
        "score_orientation": "inferred_activation_from_lof" if activation_requested else "observed_lof_perturbation_effect",
        "score_multiplier": -1 if activation_requested else 1,
    }


def _genetic_reverse_mode(modality: str, intent: QueryIntent) -> str:
    if modality not in {"sh", "xpr"}:
        return "perturbation_only"
    requested = _normalize_genetic_modality(intent.genetic_modality)
    if requested in {"rnai", "shrna", "sh", "sirna", "knockdown", "crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion", "xpr"}:
        return "perturbation_only"
    if requested in {"overexpression", "gof", "gain_of_function"}:
        return "activation_only"
    return "bidirectional"


def _evidence_level(cell_role: str | None, perturbation_role: str | None, cell_scope: str | None = None) -> str:
    if cell_scope == "normal_lineage_data_anchor":
        return "normal_lineage_data_anchor"
    if cell_role == "observed-anchor":
        return "observed_perturbation_anchor"
    cell_exact = cell_role in {"exact", "llm-tree-leaf", "all-cells"}
    pert_exact = perturbation_role in {"exact", "llm-normalized"}
    if cell_exact and pert_exact:
        return "exact_cell_exact_perturbation"
    if cell_exact:
        return "exact_cell_proxy_perturbation"
    if pert_exact:
        return "proxy_cell_exact_perturbation"
    return "proxy_cell_proxy_perturbation"


def _normalize_token(text: str) -> str:
    out = []
    for ch in text.strip().lower():
        out.append(ch if ch.isalnum() else " ")
    return " ".join("".join(out).split())
