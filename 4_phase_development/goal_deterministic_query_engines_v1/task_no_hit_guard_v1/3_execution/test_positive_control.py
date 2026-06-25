"""
test_positive_control.py — Positive-control re-run for T-031 pxfquery-T-031 guard.

Asserts that known perturbations (EGFR, TP53) return found=True with
functional terms through the NoHitGuardForwardQuery, confirming the guard
does not break the deterministic forward query path.
"""

from __future__ import annotations
import json
import os
import sys
from datetime import datetime
from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = TASK_ROOT / "1_asset"
ARTIFACT_ROOT = TASK_ROOT / "4_artifact"

WORKSPACE_SRC = (ASSET_ROOT / "T-024 pxfquery workspace package" / "src").resolve()
LOADER_PARENT = (ASSET_ROOT / "T-026 matrix loader package").resolve().parent
DATA_BUNDLE = ASSET_ROOT / "T-021 standard_resources bundle (D-004)"
XPR_MATRIX = DATA_BUNDLE / "xpr_func_ad.h5ad"
GUARD_DIR = ARTIFACT_ROOT / "2_persist"

sys.path.insert(0, str(WORKSPACE_SRC))
sys.path.insert(0, str(LOADER_PARENT))
sys.path.insert(0, str(GUARD_DIR))

from loader import load_matrix
from pxfquery_T031_forward_no_hit_guard import NoHitGuardForwardQuery


def main() -> int:
    TABLE_DIR = ARTIFACT_ROOT / "5_table"
    TABLE_DIR.mkdir(parents=True, exist_ok=True)

    adata, matrix_meta = load_matrix(XPR_MATRIX)
    engine = NoHitGuardForwardQuery(adata)

    positive_cases = [
        ("EGFR", "A549"),
        ("TP53", "MCF7"),
    ]

    results = []
    passed = 0
    failed = 0

    for pert, cell in positive_cases:
        result = engine.query(pert, cell_line=cell, top_n=20)
        entry = {
            "query": pert,
            "cell_line": cell,
            "found": bool(result.found),
            "matched_perturbation": result.perturbation,
            "matched_cell_line": result.cell_line,
            "n_obs": int(result.n_obs),
            "cells_used": result.cells_used if hasattr(result, "cells_used") else [],
            "activated_terms": int(len(result.top_activated)),
            "suppressed_terms": int(len(result.top_suppressed)),
            "top_activated": list(result.top_activated.head(5).items()),
            "top_suppressed": list(result.top_suppressed.head(5).items()),
            "guard_version": "pxfquery-T-031",
        }
        ok = (result.found
              and len(result.top_activated) >= 1
              and len(result.top_suppressed) >= 1)
        entry["test_passed"] = ok
        results.append(entry)
        if ok:
            passed += 1
        else:
            failed += 1
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {pert}/{cell} -> found={result.found} "
              f"activated={len(result.top_activated)} suppressed={len(result.top_suppressed)} "
              f"n_obs={result.n_obs}")

    summary = {
        "task": "T-031",
        "guard_version": "pxfquery-T-031",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "test_type": "positive_control",
        "engine_config": {
            "min_overlap_for_token_fallback": engine.min_overlap_for_token_fallback,
            "min_query_length_for_substring": engine.min_query_length_for_substring,
        },
        "matrix": str(XPR_MATRIX),
        "matrix_shape": matrix_meta.get("shape"),
        "total_cases": len(positive_cases),
        "passed": passed,
        "failed": failed,
        "results": results,
        "acceptance_criteria": {
            "all_must_return_found_True": passed == len(positive_cases),
            "each_must_have_activated_and_suppressed": all(
                r["activated_terms"] >= 1 and r["suppressed_terms"] >= 1
                for r in results
            ),
        },
    }

    evidence_path = TABLE_DIR / "pxfquery_T031_positive_control_evidence.json"
    evidence_path.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nPositive-control evidence written to {evidence_path}")
    print(f"Passed: {passed}/{len(positive_cases)}")
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())