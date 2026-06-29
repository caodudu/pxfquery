"""Re-run 60 T-137 questions through updated combination routing + L3 execution,
then check direction/score-orientation semantics for each case.

Usage (from 04_package_source_v3_l3 dir):
    PYTHONPATH=src conda run -n pxfquery python scripts/run_l3_direction_analysis.py

Outputs to 4_artifact/5_table/:
    l3_direction_analysis_<timestamp>.json   -- full per-case detail
    l3_direction_analysis_<timestamp>.tsv    -- flat summary

What this checks:
  Forward queries
    * score_multiplier matches pert type / genetic_modality intent
      drug          → +1  observed_drug_perturbation_effect
      genetic LoF   → +1  observed_lof_perturbation_effect
      genetic GoF   → -1  inferred_activation_from_lof
    * top_activated / top_suppressed exist and scores are finite
    * No NaN/inf in aggregate scores

  Reverse queries
    * reverse_ranking_mode matches intent
      drug          → perturbation_only, top_perturbations
      genetic LoF   → perturbation_only, top_loss_of_function_perturbations
      genetic GoF   → activation_only,   top_activating_perturbations_inferred
      genetic unspec→ bidirectional,      both lists
    * Each list is non-empty when l3 executed
    * Scores are finite, ordered descending
    * driving_terms orientation sign is consistent
"""
from __future__ import annotations

import json
import math
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from pxfquery.l1_intent.schema import QueryIntent
from pxfquery.l2_routing.combination import route_combinations
from pxfquery.l3_execution import execute_route_plan
from pxfquery.resources import ResourceManager

ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")

L2_REPORT = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package"
    / "task_ms8_10_l2_resource_routing_repair/4_artifact/5_table"
    / "t137_60_l2_validation_20260628_131252.json"
)
STANDARD_RESOURCES = (
    ROOT
    / "4_phase_development/goal_precomputed_data_exploration"
    / "task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources"
)
L3_RESOURCES = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package"
    / "task_ms8_11_l3_resource_pack_query_execution_repair/1_asset"
    / "l3_light_resource_pack"
)
OUT_DIR = (
    ROOT
    / "4_phase_development/goal_goal_ms8_human_usable_package"
    / "task_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table"
)

# ─── Direction expectation rules ───────────────────────────────────────────

_LOF_MODALITIES = {
    "rnai", "shrna", "sh", "sirna", "knockdown",
    "crispr", "knockout", "ko", "lof", "loss_of_function", "delete", "deletion", "xpr",
}
_GOF_MODALITIES = {"overexpression", "gof", "gain_of_function"}


def _expected_forward(intent: dict[str, Any]) -> dict[str, Any]:
    pert_class = (intent.get("pert_class") or "").lower()
    gmod = (intent.get("genetic_modality") or "").lower()
    if pert_class == "drug":
        return {"score_multiplier": 1, "orientation": "observed_drug_perturbation_effect"}
    if gmod in _GOF_MODALITIES:
        return {"score_multiplier": -1, "orientation": "inferred_activation_from_lof"}
    if gmod in _LOF_MODALITIES or pert_class == "genetic":
        return {"score_multiplier": 1, "orientation": "observed_lof_perturbation_effect"}
    return {"score_multiplier": 1, "orientation": "observed_perturbation_effect"}


def _expected_reverse(intent: dict[str, Any]) -> dict[str, Any]:
    pert_class = (intent.get("pert_class") or "").lower()
    gmod = (intent.get("genetic_modality") or "").lower()
    if pert_class == "drug":
        return {"ranking_mode": "perturbation_only", "primary_list": "top_perturbations"}
    if gmod in _LOF_MODALITIES:
        return {"ranking_mode": "perturbation_only", "primary_list": "top_loss_of_function_perturbations"}
    if gmod in _GOF_MODALITIES:
        return {"ranking_mode": "activation_only", "primary_list": "top_activating_perturbations_inferred"}
    # unspecified genetic or unknown
    return {"ranking_mode": "bidirectional", "primary_list": "both"}


# ─── Helpers ───────────────────────────────────────────────────────────────

def _finite_check(scores: list[float]) -> bool:
    return all(math.isfinite(s) for s in scores)


def _descending(scores: list[float]) -> bool:
    return all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1))


def _intent_from_dict(d: dict[str, Any]) -> QueryIntent:
    known = {f.name for f in QueryIntent.__dataclass_fields__.values()}
    return QueryIntent(**{k: v for k, v in d.items() if k in known})


class _FakeResources:
    """Minimal stub that exposes obs paths for combination.py pair_metadata loading."""
    def __init__(self, root: Path) -> None:
        self._root = root
        for modality in ("cp", "sh", "xpr"):
            for ext in (".parquet", ".csv"):
                candidate = root / f"{modality}_obs_min{ext}"
                if candidate.exists():
                    setattr(self, f"{modality}_obs", candidate)
                    break
            else:
                setattr(self, f"{modality}_obs", None)


# ─── Per-case processing ────────────────────────────────────────────────────

def _process_case(record: dict[str, Any], resources: ResourceManager, fake_res: _FakeResources, top_n: int) -> dict[str, Any]:
    t0 = time.time()
    case_id = record.get("case_id", "?")
    query = record.get("query", "")
    route = record.get("route", {})
    stored_intent = route.get("intent", {})
    query_type = stored_intent.get("query_type", "")

    # ── Re-run combination routing with updated code ──────────────────────
    intent_obj = _intent_from_dict(stored_intent)
    cell_route = route.get("cell_route", {})
    perturbation_route = route.get("perturbation_route", {})
    function_route = route.get("function_route", {})

    try:
        new_combo = route_combinations(
            intent_obj,
            cell_route,
            perturbation_route,
            function_route,
            resources=fake_res,
            pair_policy="observed",
        )
    except Exception as exc:
        new_combo = {"status": f"combination_error:{exc}", "selected_routes": []}

    # Build updated route plan
    updated_route = dict(route)
    updated_route["combination_route"] = new_combo

    # ── L3 execution ──────────────────────────────────────────────────────
    execution = execute_route_plan(
        updated_route,
        resources=resources,
        resource_dir=L3_RESOURCES,
        auto_download=False,
        top_n=top_n,
    ).to_dict()

    # ── Semantic analysis ─────────────────────────────────────────────────
    selected = new_combo.get("selected_routes") or []
    analysis = _analyze(query_type, stored_intent, selected, execution)

    elapsed = time.time() - t0
    return {
        "case_id": case_id,
        "query": query,
        "category": record.get("category"),
        "query_type": query_type,
        "pert_class": stored_intent.get("pert_class"),
        "genetic_modality": stored_intent.get("genetic_modality"),
        "l2_ok": record.get("l2_ok", record.get("ok")),
        "combo_status": new_combo.get("status"),
        "selected_route_count": len(selected),
        "l3_status": execution.get("execution_status"),
        "l3_executed_count": len(execution.get("executed_routes", [])),
        "l3_skipped_count": len(execution.get("skipped_routes", [])),
        "analysis": analysis,
        "elapsed_s": round(elapsed, 2),
        # keep route details for HTML/inspection
        "selected_routes_summary": [_route_summary(r) for r in selected],
        "executed_routes_summary": [_execution_summary(r) for r in execution.get("executed_routes", [])],
        "skipped_routes_summary": [_skip_summary(r) for r in execution.get("skipped_routes", [])],
    }


def _route_summary(r: dict[str, Any]) -> dict[str, Any]:
    return {
        "route_id": r.get("route_id"),
        "modality": r.get("modality"),
        "cell": r.get("cell"),
        "perturbation": r.get("perturbation"),
        "score_multiplier": r.get("score_multiplier"),
        "score_orientation": r.get("score_orientation"),
        "recommended_operation": r.get("recommended_operation"),
        "reverse_ranking_mode": r.get("reverse_ranking_mode"),
        "tier": r.get("tier"),
        "evidence_level": r.get("evidence_level"),
        "pair_verified": r.get("pair_verified"),
    }


def _execution_summary(r: dict[str, Any]) -> dict[str, Any]:
    rankings = r.get("rankings", {})
    scores = r.get("scores", {})
    return {
        "route_id": r.get("route_id"),
        "query_type": r.get("query_type"),
        "modality": r.get("modality"),
        "cell": r.get("cell"),
        "n_rows": (r.get("row_match") or {}).get("n_rows"),
        "score_multiplier": scores.get("score_multiplier"),
        "score_orientation": scores.get("score_orientation"),
        "ranking_method": scores.get("ranking_method"),
        "reverse_ranking_mode": scores.get("reverse_ranking_mode"),
        "top_activated": rankings.get("top_activated", [])[:3],
        "top_suppressed": rankings.get("top_suppressed", [])[:3],
        "top_perturbations": rankings.get("top_perturbations", [])[:3],
        "top_loss_of_function_perturbations": rankings.get("top_loss_of_function_perturbations", [])[:3],
        "top_activating_perturbations_inferred": rankings.get("top_activating_perturbations_inferred", [])[:3],
    }


def _skip_summary(r: dict[str, Any]) -> dict[str, Any]:
    return {
        "route_id": r.get("route_id"),
        "status": r.get("status"),
        "modality": r.get("modality"),
        "message": (r.get("diagnostics") or {}).get("message"),
    }


def _analyze(
    query_type: str,
    intent: dict[str, Any],
    selected_routes: list[dict[str, Any]],
    execution: dict[str, Any],
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    issues: list[str] = []

    executed = execution.get("executed_routes", [])
    l3_ok = bool(executed)

    if query_type == "forward":
        exp = _expected_forward(intent)
        for route in selected_routes:
            actual_mult = route.get("score_multiplier")
            actual_orient = route.get("score_orientation")
            mult_ok = actual_mult == exp["score_multiplier"]
            orient_ok = actual_orient == exp["orientation"] if exp["orientation"] else True
            checks.append({
                "check": "forward_score_multiplier",
                "route_id": route.get("route_id"),
                "expected": exp["score_multiplier"],
                "actual": actual_mult,
                "pass": mult_ok,
            })
            checks.append({
                "check": "forward_score_orientation",
                "route_id": route.get("route_id"),
                "expected": exp["orientation"],
                "actual": actual_orient,
                "pass": orient_ok,
            })
            if not mult_ok:
                issues.append(f"score_multiplier wrong on {route.get('route_id')}: expected {exp['score_multiplier']}, got {actual_mult}")
            if not orient_ok:
                issues.append(f"score_orientation wrong on {route.get('route_id')}: expected {exp['orientation']}, got {actual_orient}")

        for er in executed:
            rankings = er.get("rankings", {})
            top_act = rankings.get("top_activated", [])
            top_sup = rankings.get("top_suppressed", [])
            sc = er.get("scores", {})
            agg = sc.get("aggregate", {})
            # check score multiplier present in execution output
            actual_mult = sc.get("score_multiplier")
            exp_mult = exp["score_multiplier"]
            mult_exec_ok = actual_mult == exp_mult
            checks.append({
                "check": "execution_score_multiplier",
                "route_id": er.get("route_id"),
                "expected": exp_mult,
                "actual": actual_mult,
                "pass": mult_exec_ok,
            })
            if not mult_exec_ok:
                issues.append(f"execution score_multiplier mismatch on {er.get('route_id')}: expected {exp_mult}, got {actual_mult}")

            # check score finiteness
            agg_values = list(agg.values())
            if agg_values and not _finite_check(agg_values):
                issues.append(f"non-finite aggregate scores in {er.get('route_id')}")
                checks.append({"check": "score_finite", "route_id": er.get("route_id"), "pass": False})
            else:
                checks.append({"check": "score_finite", "route_id": er.get("route_id"), "pass": True})

            # For GoF: top_activated should reflect suppressed-in-LoF (inverted by -1)
            # We can only verify sign consistency: with mult=-1, top_activated scores should be >0
            if exp_mult == -1 and top_act:
                all_pos = all(r.get("score", 0) > 0 for r in top_act)
                checks.append({"check": "gof_top_activated_positive", "route_id": er.get("route_id"), "pass": all_pos})
                if not all_pos:
                    issues.append(f"GoF top_activated has non-positive scores on {er.get('route_id')}")

    elif query_type == "reverse":
        exp = _expected_reverse(intent)
        for route in selected_routes:
            actual_mode = route.get("reverse_ranking_mode")
            mode_ok = actual_mode == exp["ranking_mode"]
            checks.append({
                "check": "reverse_ranking_mode",
                "route_id": route.get("route_id"),
                "expected": exp["ranking_mode"],
                "actual": actual_mode,
                "pass": mode_ok,
            })
            if not mode_ok:
                issues.append(f"reverse_ranking_mode wrong on {route.get('route_id')}: expected {exp['ranking_mode']}, got {actual_mode}")

        for er in executed:
            rankings = er.get("rankings", {})
            scores = er.get("scores", {})
            actual_mode = scores.get("reverse_ranking_mode")
            primary = exp["primary_list"]

            if primary == "both":
                lof_list = rankings.get("top_loss_of_function_perturbations", [])
                act_list = rankings.get("top_activating_perturbations_inferred", [])
                has_lof = bool(lof_list)
                has_act = bool(act_list)
                checks.append({"check": "bidirectional_has_lof_list", "route_id": er.get("route_id"), "pass": has_lof})
                checks.append({"check": "bidirectional_has_act_list", "route_id": er.get("route_id"), "pass": has_act})
                if not has_lof:
                    issues.append(f"bidirectional missing top_loss_of_function_perturbations on {er.get('route_id')}")
                if not has_act:
                    issues.append(f"bidirectional missing top_activating_perturbations_inferred on {er.get('route_id')}")
                # Lof scores should be descending
                if lof_list:
                    lof_scores = [r.get("score", 0) for r in lof_list]
                    checks.append({"check": "lof_scores_descending", "route_id": er.get("route_id"), "pass": _descending(lof_scores)})
                # Act inferred scores should also be descending (they're already oriented)
                if act_list:
                    act_scores = [r.get("score", 0) for r in act_list]
                    checks.append({"check": "act_scores_descending", "route_id": er.get("route_id"), "pass": _descending(act_scores)})
                # raw_projection on lof list should be positive (selected by -proj desc)
                if lof_list:
                    raw_ok = all(r.get("raw_projection", 0) >= 0 for r in lof_list)
                    checks.append({"check": "lof_raw_projection_positive", "route_id": er.get("route_id"), "pass": raw_ok})
                    if not raw_ok:
                        issues.append(f"lof list has negative raw_projection on {er.get('route_id')}")
                # raw_projection on act list should be negative (selected by proj asc)
                if act_list:
                    raw_ok = all(r.get("raw_projection", 0) <= 0 for r in act_list)
                    checks.append({"check": "act_raw_projection_negative", "route_id": er.get("route_id"), "pass": raw_ok})
                    if not raw_ok:
                        issues.append(f"act-inferred list has positive raw_projection on {er.get('route_id')}")
            elif primary == "top_loss_of_function_perturbations":
                lst = rankings.get("top_loss_of_function_perturbations", [])
                has_list = bool(lst)
                checks.append({"check": "lof_list_present", "route_id": er.get("route_id"), "pass": has_list})
                if not has_list:
                    issues.append(f"expected top_loss_of_function_perturbations missing on {er.get('route_id')}")
                if lst:
                    raw_ok = all(r.get("raw_projection", 0) >= 0 for r in lst)
                    checks.append({"check": "lof_raw_projection_positive", "route_id": er.get("route_id"), "pass": raw_ok})
                    if not raw_ok:
                        issues.append(f"lof list has negative raw_projection on {er.get('route_id')}")
                    sc_ok = _descending([r.get("score", 0) for r in lst])
                    checks.append({"check": "lof_scores_descending", "route_id": er.get("route_id"), "pass": sc_ok})
            elif primary == "top_activating_perturbations_inferred":
                lst = rankings.get("top_activating_perturbations_inferred", [])
                has_list = bool(lst)
                checks.append({"check": "act_list_present", "route_id": er.get("route_id"), "pass": has_list})
                if not has_list:
                    issues.append(f"expected top_activating_perturbations_inferred missing on {er.get('route_id')}")
                if lst:
                    raw_ok = all(r.get("raw_projection", 0) <= 0 for r in lst)
                    checks.append({"check": "act_raw_projection_negative", "route_id": er.get("route_id"), "pass": raw_ok})
                    if not raw_ok:
                        issues.append(f"act-inferred list has positive raw_projection on {er.get('route_id')}")
            else:
                # top_perturbations (drug)
                lst = rankings.get("top_perturbations", [])
                has_list = bool(lst)
                checks.append({"check": "top_perturbations_present", "route_id": er.get("route_id"), "pass": has_list})
                if not has_list:
                    issues.append(f"expected top_perturbations missing on {er.get('route_id')}")
                if lst:
                    sc_ok = _descending([r.get("score", 0) for r in lst])
                    checks.append({"check": "drug_scores_descending", "route_id": er.get("route_id"), "pass": sc_ok})

            # Check driving_terms orientation consistency
            # For orientation=1 (LoF direct), driving_terms.contribution should have same sign as (X[i]*target) components
            # For orientation=-1 (GoF inferred), driving_terms should have same sign as (-X[i]*target) components
            # We can't check this purely from output without raw matrix, so just check contribution is finite
            all_lists = (
                list(rankings.get("top_perturbations", []))
                + list(rankings.get("top_loss_of_function_perturbations", []))
                + list(rankings.get("top_activating_perturbations_inferred", []))
            )
            for candidate in all_lists:
                dt = candidate.get("driving_terms", [])
                for term in dt:
                    if not math.isfinite(term.get("contribution", 0)):
                        issues.append(f"non-finite driving_term contribution on {er.get('route_id')}: {term.get('function')}")

    return {
        "query_type": query_type,
        "expected": _expected_forward(intent) if query_type == "forward" else _expected_reverse(intent),
        "checks": checks,
        "issues": issues,
        "pass": not issues,
        "check_count": len(checks),
        "pass_count": sum(1 for c in checks if c.get("pass")),
        "fail_count": sum(1 for c in checks if not c.get("pass")),
        "l3_executed": l3_ok,
    }


# ─── Main ──────────────────────────────────────────────────────────────────

def main() -> None:
    print(f"Loading L2 report: {L2_REPORT}")
    data = json.loads(L2_REPORT.read_text(encoding="utf-8"))
    records = data["records"]
    print(f"  {len(records)} cases")

    # Standard resources for L2 pair_metadata (obs_min files)
    fake_res = _FakeResources(STANDARD_RESOURCES)
    print(f"  pair_metadata obs paths: cp={getattr(fake_res,'cp_obs',None)}, sh={getattr(fake_res,'sh_obs',None)}")

    # L3 resource manager
    resources = ResourceManager()
    resources.use(L3_RESOURCES, strict=False)

    TOP_N = 10

    print(f"\nRunning {len(records)} cases in parallel (8 workers)...")
    case_results = [None] * len(records)

    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {
            pool.submit(_process_case, rec, resources, fake_res, TOP_N): i
            for i, rec in enumerate(records)
        }
        done = 0
        for future in as_completed(futures):
            idx = futures[future]
            try:
                case_results[idx] = future.result()
            except Exception as exc:
                rec = records[idx]
                case_results[idx] = {
                    "case_id": rec.get("case_id"),
                    "query": rec.get("query"),
                    "error": str(exc),
                    "analysis": {"pass": False, "issues": [str(exc)], "checks": []},
                }
            done += 1
            if done % 10 == 0:
                print(f"  {done}/{len(records)} done")

    # ── Summary stats ─────────────────────────────────────────────────────
    all_issues: list[str] = []
    for r in case_results:
        all_issues.extend(r.get("analysis", {}).get("issues", []))

    issue_counts = Counter(
        i.split(":")[0].strip() if ":" in i else i
        for i in all_issues
    )

    status_counts = Counter(r.get("l3_status") for r in case_results)
    analysis_pass = sum(1 for r in case_results if r.get("analysis", {}).get("pass"))
    check_total = sum(r.get("analysis", {}).get("check_count", 0) for r in case_results)
    check_pass = sum(r.get("analysis", {}).get("pass_count", 0) for r in case_results)

    # Direction-specific stats
    fwd_mult_wrong = [
        r for r in case_results
        if r.get("query_type") == "forward"
        and any("score_multiplier wrong" in iss for iss in r.get("analysis", {}).get("issues", []))
    ]
    rev_mode_wrong = [
        r for r in case_results
        if r.get("query_type") == "reverse"
        and any("reverse_ranking_mode wrong" in iss for iss in r.get("analysis", {}).get("issues", []))
    ]
    lof_raw_neg = [
        r for r in case_results
        if any("lof list has negative raw_projection" in iss for iss in r.get("analysis", {}).get("issues", []))
    ]
    act_raw_pos = [
        r for r in case_results
        if any("act-inferred list has positive raw_projection" in iss for iss in r.get("analysis", {}).get("issues", []))
    ]

    summary = {
        "source_l2_report": str(L2_REPORT),
        "l3_resource_dir": str(L3_RESOURCES),
        "total": len(case_results),
        "l3_status_counts": dict(status_counts),
        "analysis_pass": analysis_pass,
        "analysis_fail": len(case_results) - analysis_pass,
        "check_total": check_total,
        "check_pass": check_pass,
        "check_fail": check_total - check_pass,
        "direction_bugs": {
            "forward_score_multiplier_wrong": len(fwd_mult_wrong),
            "reverse_ranking_mode_wrong": len(rev_mode_wrong),
            "lof_raw_projection_negative": len(lof_raw_neg),
            "act_inferred_raw_projection_positive": len(act_raw_pos),
        },
        "top_issue_types": dict(issue_counts.most_common(15)),
        "fwd_mult_wrong_cases": [r["case_id"] for r in fwd_mult_wrong],
        "rev_mode_wrong_cases": [r["case_id"] for r in rev_mode_wrong],
        "lof_raw_neg_cases": [r["case_id"] for r in lof_raw_neg],
        "act_raw_pos_cases": [r["case_id"] for r in act_raw_pos],
    }

    # ── Save outputs ──────────────────────────────────────────────────────
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = OUT_DIR / f"l3_direction_analysis_{ts}.json"
    tsv_path = OUT_DIR / f"l3_direction_analysis_{ts}.tsv"

    payload = {"summary": summary, "records": case_results}
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    import pandas as pd
    flat = []
    for r in case_results:
        an = r.get("analysis", {})
        flat.append({
            "case_id": r.get("case_id"),
            "query": r.get("query"),
            "category": r.get("category"),
            "query_type": r.get("query_type"),
            "pert_class": r.get("pert_class"),
            "genetic_modality": r.get("genetic_modality"),
            "l2_ok": r.get("l2_ok"),
            "l3_status": r.get("l3_status"),
            "l3_executed": r.get("l3_executed_count"),
            "analysis_pass": an.get("pass"),
            "check_pass": an.get("pass_count"),
            "check_fail": an.get("fail_count"),
            "issues": "; ".join(an.get("issues", [])),
            "expected": json.dumps(an.get("expected", {})),
            "elapsed_s": r.get("elapsed_s"),
        })
    pd.DataFrame(flat).to_csv(tsv_path, sep="\t", index=False)

    # ── Print summary ─────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("L3 Direction Analysis Summary")
    print("=" * 60)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"\nJSON: {json_path}")
    print(f"TSV:  {tsv_path}")

    if fwd_mult_wrong:
        print(f"\n⚠️  Forward score_multiplier errors ({len(fwd_mult_wrong)}):")
        for r in fwd_mult_wrong:
            print(f"  [{r['case_id']}] {r['query'][:80]}")
            for iss in r["analysis"]["issues"]:
                if "multiplier" in iss:
                    print(f"    → {iss}")

    if rev_mode_wrong:
        print(f"\n⚠️  Reverse ranking_mode errors ({len(rev_mode_wrong)}):")
        for r in rev_mode_wrong:
            print(f"  [{r['case_id']}] {r['query'][:80]}")
            for iss in r["analysis"]["issues"]:
                if "ranking_mode" in iss:
                    print(f"    → {iss}")

    if lof_raw_neg or act_raw_pos:
        print(f"\n⚠️  Projection sign errors: lof_neg={len(lof_raw_neg)}, act_pos={len(act_raw_pos)}")

    if not (fwd_mult_wrong or rev_mode_wrong or lof_raw_neg or act_raw_pos):
        print("\n✓ No direction/orientation bugs found")


if __name__ == "__main__":
    main()
