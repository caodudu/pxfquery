from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")
L2_REPORT = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_10_l2_resource_routing_repair/4_artifact/5_table/"
    "t137_60_l2_validation_latest.json"
)
L3_REPLAY = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table/"
    "t137_60_l2_to_l3_replay_v20260628.json"
)
L3_RESOURCES = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table/"
    "l3_storage_experiment"
)
OUT_DIR = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table"
)


def main() -> None:
    l2_records = {r["case_id"]: r for r in json.loads(L2_REPORT.read_text())["records"]}
    replay_records = json.loads(L3_REPLAY.read_text())["records"]
    obs = {mod: pd.read_parquet(L3_RESOURCES / f"{mod}_obs_min.parquet") for mod in ["cp", "xpr", "sh"]}
    out = []
    for replay in replay_records:
        if replay["l3_execution_status"] != "empty_matrix_hit":
            continue
        l2 = l2_records[replay["case_id"]]
        route = l2["route"]
        selected = (route.get("combination_route") or {}).get("selected_routes") or []
        candidates = (route.get("combination_route") or {}).get("route_candidates") or []
        selected_hits = [_route_hit(route, r, obs) for r in selected]
        candidate_hits = [_route_hit(route, r, obs) for r in candidates]
        any_candidate_pair = any(h["pair_hit"] for h in candidate_hits)
        any_candidate_cell = any(h["cell_hit"] for h in candidate_hits)
        any_candidate_pert = any(h["perturbation_hit"] for h in candidate_hits)
        causes = _causes(selected_hits, candidate_hits, any_candidate_pair, any_candidate_cell, any_candidate_pert)
        out.append(
            {
                "case_id": replay["case_id"],
                "category": replay["category"],
                "query_type": replay["query_type"],
                "query": replay["query"],
                "intent_bio_context": (route.get("intent") or {}).get("bio_context"),
                "intent_pert_desc": (route.get("intent") or {}).get("pert_desc"),
                "intent_pert_class": (route.get("intent") or {}).get("pert_class"),
                "intent_genetic_modality": (route.get("intent") or {}).get("genetic_modality"),
                "selected_route_count": len(selected),
                "candidate_route_count": len(candidates),
                "selected_cell_values": sorted({str(r.get("cell")) for r in selected if r.get("cell")}),
                "selected_perturbation_values": sorted({str(r.get("perturbation")) for r in selected if r.get("perturbation")}),
                "selected_modalities_checked": sorted({m for h in selected_hits for m in h["modalities"]}),
                "selected_any_cell_hit": any(h["cell_hit"] for h in selected_hits),
                "selected_any_perturbation_hit": any(h["perturbation_hit"] for h in selected_hits),
                "selected_any_pair_hit": any(h["pair_hit"] for h in selected_hits),
                "candidate_any_cell_hit": any_candidate_cell,
                "candidate_any_perturbation_hit": any_candidate_pert,
                "candidate_any_pair_hit": any_candidate_pair,
                "candidate_pair_hit_routes": [h["route_id"] for h in candidate_hits if h["pair_hit"]],
                "cause": "+".join(causes),
                "selected_route_diagnostics": selected_hits,
            }
        )
    df = pd.DataFrame(out)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tsv = OUT_DIR / "t137_60_l3_empty_hit_diagnosis_v20260628.tsv"
    js = OUT_DIR / "t137_60_l3_empty_hit_diagnosis_v20260628.json"
    df.to_csv(tsv, sep="\t", index=False)
    js.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print("empty cases", len(out))
    print("cause counts")
    print(Counter(row["cause"] for row in out))
    print("by category/cause")
    print(Counter((row["category"], row["cause"]) for row in out))
    print(tsv)
    print(js)


def _route_hit(route_plan: dict[str, Any], route: dict[str, Any], obs_by_modality: dict[str, pd.DataFrame]) -> dict[str, Any]:
    query_type = (route_plan.get("intent") or {}).get("query_type")
    modalities = _modalities_for_route(route_plan, route)
    cell = route.get("cell")
    perturbation = route.get("perturbation")
    hits = []
    for modality in modalities:
        obs = obs_by_modality[modality]
        cell_mask = _cell_mask(obs, cell)
        if query_type == "reverse":
            pert_mask = pd.Series([True] * len(obs))
        else:
            pert_mask = _pert_mask(obs, perturbation)
        hits.append(
            {
                "modality": modality,
                "cell_hit": bool(cell_mask.any()),
                "perturbation_hit": bool(pert_mask.any()),
                "pair_hit": bool((cell_mask & pert_mask).any()),
                "cell_rows": int(cell_mask.sum()),
                "perturbation_rows": int(pert_mask.sum()),
                "pair_rows": int((cell_mask & pert_mask).sum()),
            }
        )
    return {
        "route_id": route.get("route_id"),
        "cell": cell,
        "perturbation": perturbation,
        "modalities": modalities,
        "cell_hit": any(h["cell_hit"] for h in hits),
        "perturbation_hit": any(h["perturbation_hit"] for h in hits),
        "pair_hit": any(h["pair_hit"] for h in hits),
        "per_modality": hits,
    }


def _modalities_for_route(route_plan: dict[str, Any], route: dict[str, Any]) -> list[str]:
    if route.get("modality"):
        return [str(route["modality"]).lower()]
    intent = route_plan.get("intent") or {}
    pert_class = str(intent.get("pert_class") or "").lower()
    modality = str(intent.get("genetic_modality") or "").lower()
    record = route.get("perturbation_record") or {}
    pert = str(route.get("perturbation") or record.get("id") or "")
    if pert.startswith("BRD-") or str(record.get("id", "")).startswith("BRD-") or pert_class == "drug":
        return ["cp"]
    if pert_class == "genetic":
        if modality in {"rnai", "shrna", "knockdown"}:
            return ["sh"]
        if modality in {"overexpression", "gof", "crispr", "knockout", "ko", "lof"}:
            return ["xpr"]
        return ["xpr", "sh"]
    return ["cp", "xpr", "sh"]


def _cell_mask(obs: pd.DataFrame, cell: str | None) -> pd.Series:
    if not cell:
        return pd.Series([True] * len(obs))
    return obs["cell_iname"].astype(str).str.upper() == str(cell).upper()


def _pert_mask(obs: pd.DataFrame, perturbation: str | None) -> pd.Series:
    if not perturbation:
        return pd.Series([False] * len(obs))
    p = str(perturbation).upper()
    return (obs["pert_id"].astype(str).str.upper() == p) | (obs["cmap_name"].astype(str).str.upper() == p)


def _causes(
    selected_hits: list[dict[str, Any]],
    candidate_hits: list[dict[str, Any]],
    any_candidate_pair: bool,
    any_candidate_cell: bool,
    any_candidate_pert: bool,
) -> list[str]:
    if any_candidate_pair:
        return ["selected_route_missed_available_candidate"]
    selected_cell = any(h["cell_hit"] for h in selected_hits)
    selected_pert = any(h["perturbation_hit"] for h in selected_hits)
    if not any_candidate_cell:
        return ["cell_scope_absent_from_l3_matrix"]
    if not any_candidate_pert:
        return ["perturbation_absent_from_l3_matrix"]
    if selected_cell and selected_pert:
        return ["cell_and_perturbation_present_but_no_pair"]
    return ["candidate_axes_present_but_no_pair"]


if __name__ == "__main__":
    main()
