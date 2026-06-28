from __future__ import annotations

from pathlib import Path
from typing import Any

from pxfquery.l1_intent import QueryIntent


MAX_CELL_CANDIDATES = 6
MAX_PERTURBATION_PROXIES = 5
MAX_REVERSE_INTERPRETATION_SETS = 3
MAX_REVERSE_FUNCTIONS_PER_SET = 3
MAX_PAIR_CHECKS = 25
MAX_SELECTED_ROUTES = 3
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
        route_candidates = _forward_route_candidates(cell_route, perturbation_route, intent, pair_metadata)
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
    route_candidates = _reverse_route_candidates(cell_route, function_route, intent)
    pair_availability = _pair_availability_reverse(route_candidates, function_route, reverse_engines)
    return {
        "status": _combination_status(bool(function_route.get("selected")), pair_availability),
        "query_type": "reverse",
        "pair_policy": "cell_scope_only",
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
    exact_cells = [c for c in cells if c.get("role") in {"exact", "llm-tree-leaf", "all-cells"}][:1]
    proxy_cells = [c for c in cells if c not in exact_cells]
    exact_perts = perturbation_route.get("selected", [])[:1]
    proxy_source = (perturbation_route.get("expanded_proxies") if use_pair_metadata else None) or perturbation_route.get("proxies", [])
    proxy_perts = proxy_source[:MAX_EXPANDED_PERTURBATION_PROXIES if use_pair_metadata else MAX_PERTURBATION_PROXIES]
    stages = [
        ("A", "exact_cell_exact_perturbation", exact_cells, exact_perts),
        ("B", "exact_cell_proxy_perturbation", exact_cells, proxy_perts),
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
    if use_pair_metadata and not out:
        for stage, tier, stage_perts in [
            ("E", "observed_anchor_exact_perturbation", exact_perts),
            ("F", "observed_anchor_proxy_perturbation", proxy_perts),
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
    route = {
        "route_id": f"forward_{route_number:03d}",
        "stage": stage,
        "tier": tier,
        "cell": cell.get("cell"),
        "cell_role": cell.get("role"),
        "cell_expansion_scope": cell.get("cell_expansion_scope", "public_candidates"),
        "cell_route_distance": cell.get("cell_route_distance", 0 if cell.get("role") in {"exact", "llm-tree-leaf"} else 1),
        "perturbation": _perturbation_key(pert),
        "perturbation_role": pert.get("role"),
        "perturbation_expansion_scope": _perturbation_expansion_scope(pert),
        "perturbation_source_rank": pert.get("rank"),
        "perturbation_record": pert,
        "modalities": matched_modalities,
        "modality_evidence": _modality_evidence(intent, pert, matched_modalities),
        "pair_search_round": _pair_search_round(cell, pert),
        "pair_search_reason": _pair_search_reason(stage),
        "pair_verified": bool(use_pair_metadata),
        "pair_verification_source": "l3_obs_min" if use_pair_metadata else None,
        "evidence_level": _evidence_level(cell.get("role"), pert.get("role")),
    }
    if len(matched_modalities) == 1:
        route["modality"] = matched_modalities[0]
    return route


def _pair_search_reason(stage: str) -> str:
    if stage == "A":
        return "exact_or_initial_pair_available"
    if stage in {"E", "F"}:
        return "no_observed_pair_in_routed_cell_context; using observed perturbation anchor cell with explicit weak-evidence label"
    return "strict_pair_unavailable_or_additional_observed_evidence"


def _reverse_route_candidates(cell_route: dict[str, Any], function_route: dict[str, Any], intent: QueryIntent) -> list[dict[str, Any]]:
    cells = cell_route.get("candidates", [])[:MAX_CELL_CANDIDATES] or [{"cell": None, "role": "all-cells"}]
    sets = function_route.get("interpretation_sets") or [{"set_id": "selected", "functions": function_route.get("selected", [])}]
    modalities = _reverse_modalities(intent)
    out: list[dict[str, Any]] = []
    for interp in sets[:MAX_REVERSE_INTERPRETATION_SETS]:
        for cell in cells:
            for modality in modalities:
                out.append(
                    {
                        "route_id": f"reverse_{len(out) + 1:03d}",
                        "cell": cell.get("cell"),
                        "cell_role": cell.get("role"),
                        "interpretation_set_id": interp.get("set_id"),
                        "functions": interp.get("functions", [])[:MAX_REVERSE_FUNCTIONS_PER_SET],
                        "modality": modality,
                        "evidence_level": "function-set-and-cell-scope",
                    }
                )
                if len(out) >= MAX_PAIR_CHECKS:
                    return out
    return out


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


def _pair_availability_reverse(route_candidates: list[dict[str, Any]], function_route: dict[str, Any], engines: dict[str, Any] | None) -> dict[str, Any]:
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
        elif requested in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"} and modality == "sh":
            reason = "loss_of_function_proxy"
            match_type = "loss_of_function_proxy"
            rank = "primary"
        elif requested in {"overexpression", "xpr", "gof", "gain_of_function"} and modality == "xpr":
            reason = "requested_overexpression"
            match_type = "exact_requested"
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
    if modality in {"overexpression", "xpr", "gof", "gain_of_function"}:
        return {"primary_modalities": ["xpr"], "fallback_modalities": ["sh"]}
    if modality in {"crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"}:
        return {"primary_modalities": ["sh"], "fallback_modalities": ["xpr"]}
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
        if modality in {"rnai", "shrna", "sh", "sirna", "knockdown", "crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion"}:
            return ["sh"]
        if modality in {"overexpression", "xpr", "gof", "gain_of_function"}:
            return ["xpr"]
        return ["xpr", "sh"]
    return ["cp", "xpr", "sh"]


def _evidence_level(cell_role: str | None, perturbation_role: str | None) -> str:
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
