#!/usr/bin/env python3
"""
T-032 reverse_stability_guard_v1 — Stability Guard Demo + Positive Control
=========================================================================
Runs the stability guard and positive-control scenarios for pxfquery-T-032.

Scenario A (positive control): Normal HALLMARK_APOPTOSIS + HALLMARK_MYC_TARGETS_V1
reverse query against cp_func_ad.h5ad (MCF7), asserts no regression.

Scenario B (abnormal guard): Synthetic matrices with zero-norm rows, NaN rows,
Inf rows, unmatched-only targets, and all-zero-norm matrix slices.
Verifies guard warnings are emitted and no guarded values leak into top-K.
"""

import json
import os
import sys
import time
import warnings
from pathlib import Path

import numpy as np

TASK_DIR = Path(__file__).resolve().parent.parent
REPAIRED_DIR = TASK_DIR / "3_execution" / "pxfquery_T-032_repaired" / "src"
BUNDLE_DIR = TASK_DIR / "1_asset" / "T-021 standard resources bundle (D-004)"
ARTIFACT_DIR = TASK_DIR / "4_artifact" / "2_persist"

ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(REPAIRED_DIR))
for key in list(sys.modules.keys()):
    if key.startswith("pxfquery"):
        del sys.modules[key]

import pxfquery
from pxfquery.utils import GuardReport, GuardEvent, cosine_similarity_matrix, build_target_vector
from pxfquery import PxFquery

REPORT = {
    "task": "T-032_reverse_stability_guard_v1",
    "pxfquery_path": pxfquery.__file__,
    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    "scenarios": {},
}

warnings.filterwarnings("ignore", category=RuntimeWarning)


def run_positive_control():
    cp_path = str(BUNDLE_DIR / "cp_func_ad.h5ad")
    if not Path(cp_path).exists():
        return {"status": "fail", "message": f"cp_func_ad.h5ad not found at {cp_path}"}

    pxf = PxFquery()
    pxf.load_data("cp", cp_path)

    t0 = time.time()
    result = pxf.func2pert(
        activate=["HALLMARK_APOPTOSIS"],
        suppress=["HALLMARK_MYC_TARGETS_V1"],
        cell_line="MCF7",
        top_k=20,
    )
    elapsed = time.time() - t0

    candidates = result.candidates_df
    similarities = candidates["similarity"].values if len(candidates) > 0 else np.array([])

    checks = {
        "n_candidates": len(candidates),
        "all_finite": bool(np.all(np.isfinite(similarities))),
        "all_in_range": bool(np.all((similarities >= -1.0) & (similarities <= 1.0))),
        "negative_similarities": bool(np.any(similarities < 0)),
        "positive_similarities": bool(np.any(similarities > 0)),
        "time_sec": round(elapsed, 3),
    }

    warnings_list = getattr(result, "warnings", [])
    guard_warning_count = len([w for w in warnings_list if w.get("scenario", "") in (
        "zero_norm_row", "zero_norm_target", "nan_row", "inf_row", "target_empty"
    )])

    checks["guard_warning_count"] = guard_warning_count
    checks["total_warnings"] = len(warnings_list)

    for scenario in ("zero_norm_row", "zero_norm_target", "nan_row", "inf_row"):
        count = len([w for w in warnings_list if w.get("scenario") == scenario])
        checks[f"scenario_{scenario}"] = count

    top5 = []
    for _, row in candidates.head(5).iterrows():
        top5.append({
            "cmap_name": str(row["cmap_name"]),
            "cell_iname": str(row["cell_iname"]),
            "similarity": float(row["similarity"]),
            "driving_terms": str(row.get("driving_terms", "")),
        })

    candidates_json = candidates.reset_index().to_dict(orient="records")
    with open(ARTIFACT_DIR / "pxfquery_T-032_positive_control_candidates.json", "w") as f:
        json.dump(candidates_json, f, indent=2, default=str)

    meta = {
        "activate": result.activate,
        "suppress": result.suppress,
        "cell_line": result.cell_line,
        "guard_warning_count": guard_warning_count,
        "total_warnings": len(warnings_list),
        "n_candidates": len(candidates),
        "matrix": "cp_func_ad.h5ad",
        "data_bundle": str(BUNDLE_DIR),
    }
    with open(ARTIFACT_DIR / "pxfquery_T-032_positive_control_meta.json", "w") as f:
        json.dump(meta, f, indent=2, default=str)

    passed = checks["all_finite"] and checks["all_in_range"] and guard_warning_count == 0
    return {
        "status": "pass" if passed else "fail",
        "checks": checks,
        "top5": top5,
        "warnings": warnings_list,
        "meta": meta,
    }


def run_scenario_b_case1_zero_norm_row():
    X = np.array([
        [1.0, 2.0, 3.0],
        [0.0, 0.0, 0.0],
        [4.0, 5.0, 6.0],
    ], dtype=np.float64)
    v = np.array([1.0, 0.0, -1.0], dtype=np.float64)
    guard = GuardReport()
    sims = cosine_similarity_matrix(X, v, guard=guard)

    finite = np.isfinite(sims)
    within_range = bool(np.all((sims[finite] >= -1.0) & (sims[finite] <= 1.0)))
    zero_row_warnings = guard.scenario_events("zero_norm_row")

    return {
        "expected_warning_count": 1,
        "actual_warning_count": len(zero_row_warnings),
        "warning_match": len(zero_row_warnings) == 1,
        "all_finite": bool(np.all(finite)),
        "within_range": within_range,
        "similarities": sims.tolist(),
        "warnings": guard.warnings,
    }


def run_scenario_b_case2_nan_row():
    X = np.array([
        [1.0, 2.0, 3.0],
        [np.nan, 0.0, 0.0],
    ], dtype=np.float64)
    v = np.array([1.0, 0.0, -1.0], dtype=np.float64)
    guard = GuardReport()
    sims = cosine_similarity_matrix(X, v, guard=guard)

    finite = np.isfinite(sims)
    nan_warnings = guard.scenario_events("nan_row")

    return {
        "expected_warning_at_least": 1,
        "actual_warning_count": len(nan_warnings),
        "warning_match": len(nan_warnings) >= 1,
        "all_finite": bool(np.all(finite)),
        "similarities": sims.tolist(),
        "warnings": guard.warnings,
    }


def run_scenario_b_case3_inf_row():
    X = np.array([
        [1.0, 2.0, 3.0],
        [np.inf, 0.0, 0.0],
    ], dtype=np.float64)
    v = np.array([1.0, 0.0, -1.0], dtype=np.float64)
    guard = GuardReport()
    sims = cosine_similarity_matrix(X, v, guard=guard)

    finite = np.isfinite(sims)
    inf_warnings = guard.scenario_events("inf_row")

    return {
        "expected_warning_at_least": 1,
        "actual_warning_count": len(inf_warnings),
        "warning_match": len(inf_warnings) >= 1,
        "all_finite": bool(np.all(finite)),
        "similarities": sims.tolist(),
        "warnings": guard.warnings,
    }


def run_scenario_b_case4_unmatched_terms():
    terms = ["GENE_ALPHA", "PATHWAY_BETA", "TERM_GAMMA"]
    vec, matched, unmatched = build_target_vector(
        terms, ["NONEXISTENT_TERM_XYZ"], ["MISSING_TERM"]
    )
    matched_empty = len(matched) == 0
    unmatched_present = len(unmatched) == 2
    zero_vec = np.allclose(vec, 0.0)

    return {
        "matched_empty": matched_empty,
        "unmatched_present": unmatched_present,
        "zero_vector": zero_vec,
        "matched_terms": matched,
        "unmatched_terms": unmatched,
    }


def run_scenario_b_case5_zero_norm_target():
    X = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ], dtype=np.float64)
    v = np.array([0.0, 0.0, 0.0], dtype=np.float64)
    guard = GuardReport()
    sims = cosine_similarity_matrix(X, v, guard=guard)

    target_warnings = guard.scenario_events("zero_norm_target")
    all_zero = bool(np.allclose(sims, 0.0))

    return {
        "expected_warning_count": 1,
        "actual_warning_count": len(target_warnings),
        "warning_match": len(target_warnings) >= 1,
        "all_zero_guard": all_zero,
        "similarities": sims.tolist(),
        "warnings": guard.warnings,
    }


def run_scenario_b_case6_all_zero_norm_rows():
    X = np.array([
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
    ], dtype=np.float64)
    v = np.array([1.0, 0.0, -1.0], dtype=np.float64)
    guard = GuardReport()
    sims = cosine_similarity_matrix(X, v, guard=guard)

    zero_warnings = guard.scenario_events("zero_norm_row")
    all_zero = bool(np.allclose(sims, 0.0))

    return {
        "expected_warning_count_at_least": 1,
        "actual_warning_count": len(zero_warnings),
        "warning_match": len(zero_warnings) >= 1,
        "all_zero_guard": all_zero,
        "similarities": sims.tolist(),
        "warnings": guard.warnings,
    }


def run_backward_compat():
    X = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [0.5, -1.0, 1.0],
    ], dtype=np.float64)
    v = np.array([1.0, 0.0, -1.0], dtype=np.float64)

    guard = GuardReport()
    sims_guarded = cosine_similarity_matrix(X, v, guard=guard)
    sims_legacy = _legacy_cosine(X, v)

    close = bool(np.allclose(sims_guarded, sims_legacy, rtol=1e-12))
    return {
        "backward_compatible": close,
        "guarded": sims_guarded.tolist(),
        "legacy": sims_legacy.tolist(),
        "max_diff": float(np.max(np.abs(sims_guarded - sims_legacy))),
    }


def _legacy_cosine(matrix, vec):
    row_norms = np.linalg.norm(matrix, axis=1)
    vec_norm = np.linalg.norm(vec)
    denom = row_norms * vec_norm
    denom = np.where(denom == 0, 1e-10, denom)
    return (matrix @ vec) / denom


def main():
    print("=== T-032 Stability Guard Demo ===")
    print(f"pxfquery location: {pxfquery.__file__}")
    print(f"Repaired workspace: {REPAIRED_DIR}")
    print()

    all_guard_warnings = []

    print("--- Scenario A: Positive Control ---")
    pa = run_positive_control()
    print(f"  status: {pa['status']}")
    for k, v in pa.get("checks", {}).items():
        print(f"  {k}: {v}")
    REPORT["scenarios"]["A_positive_control"] = pa
    if "warnings" in pa:
        all_guard_warnings.extend(pa["warnings"])

    print("\n--- Scenario B.1: Zero-Norm Row ---")
    sb1 = run_scenario_b_case1_zero_norm_row()
    REPORT["scenarios"]["B1_zero_norm_row"] = sb1
    all_guard_warnings.extend(sb1.get("warnings", []))
    for k, v in sb1.items():
        if k != "warnings":
            print(f"  {k}: {v}")

    print("\n--- Scenario B.2: NaN Row ---")
    sb2 = run_scenario_b_case2_nan_row()
    REPORT["scenarios"]["B2_nan_row"] = sb2
    all_guard_warnings.extend(sb2.get("warnings", []))
    for k, v in sb2.items():
        if k != "warnings":
            print(f"  {k}: {v}")

    print("\n--- Scenario B.3: Inf Row ---")
    sb3 = run_scenario_b_case3_inf_row()
    REPORT["scenarios"]["B3_inf_row"] = sb3
    all_guard_warnings.extend(sb3.get("warnings", []))
    for k, v in sb3.items():
        if k != "warnings":
            print(f"  {k}: {v}")

    print("\n--- Scenario B.4: Unmatched Terms in build_target_vector ---")
    sb4 = run_scenario_b_case4_unmatched_terms()
    REPORT["scenarios"]["B4_unmatched_terms"] = sb4
    for k, v in sb4.items():
        print(f"  {k}: {v}")

    print("\n--- Scenario B.5: Zero-Norm Target Vector ---")
    sb5 = run_scenario_b_case5_zero_norm_target()
    REPORT["scenarios"]["B5_zero_norm_target"] = sb5
    all_guard_warnings.extend(sb5.get("warnings", []))
    for k, v in sb5.items():
        if k != "warnings":
            print(f"  {k}: {v}")

    print("\n--- Scenario B.6: All Zero-Norm Rows ---")
    sb6 = run_scenario_b_case6_all_zero_norm_rows()
    REPORT["scenarios"]["B6_all_zero_norm_rows"] = sb6
    all_guard_warnings.extend(sb6.get("warnings", []))
    for k, v in sb6.items():
        if k != "warnings":
            print(f"  {k}: {v}")

    print("\n--- Backward Compatibility ---")
    bc = run_backward_compat()
    REPORT["scenarios"]["backward_compatibility"] = bc
    for k, v in bc.items():
        print(f"  {k}: {v}")

    # Summary
    scenario_results = {
        k: v for k, v in REPORT["scenarios"].items()
    }
    passed = 0
    failed = 0
    if pa["status"] == "pass":
        passed += 1
    else:
        failed += 1

    for case in [sb1, sb2, sb3, sb4, sb5, sb6]:
        key = "warning_match" if "warning_match" in case else "matched_empty"
        check_val = case.get("warning_match", case.get("matched_empty"))
        if check_val:
            passed += 1
        else:
            failed += 1

    if bc["backward_compatible"]:
        passed += 1
    else:
        failed += 1

    REPORT["summary"] = {
        "total_scenarios": passed + failed,
        "passed": passed,
        "failed": failed,
    }

    guard_warnings_path = ARTIFACT_DIR / "pxfquery_T-032_guard_warnings.json"
    with open(guard_warnings_path, "w") as f:
        json.dump(all_guard_warnings, f, indent=2, default=str)

    validation_path = TASK_DIR / "3_execution" / "stability_guard_validation.json"
    REPORT["validation_path"] = str(validation_path)
    REPORT["guard_warnings_path"] = str(guard_warnings_path)
    REPORT["positive_control_candidates_path"] = str(ARTIFACT_DIR / "pxfquery_T-032_positive_control_candidates.json")
    REPORT["positive_control_meta_path"] = str(ARTIFACT_DIR / "pxfquery_T-032_positive_control_meta.json")
    with open(validation_path, "w") as f:
        json.dump(REPORT, f, indent=2, default=str)

    print(f"\n=== Summary: {passed}/{passed + failed} passed ===")
    print(f"Guard warnings saved to: {guard_warnings_path}")
    print(f"Validation saved to: {validation_path}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())