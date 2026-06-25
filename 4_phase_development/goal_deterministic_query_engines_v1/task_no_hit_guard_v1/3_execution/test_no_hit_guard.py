"""
test_no_hit_guard.py — Negative no-hit test for T-031 pxfquery-T-031 guard.

Asserts that unsupported/nonsense perturbation names return found=False
through the NoHitGuardForwardQuery, and writes no-hit evidence JSON.
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

    no_hit_queries = [
        ("NONSENSE_ZZZ999", "A549"),
        ("QWERTYASDFG", "A549"),
        ("egr", "A549"),
        ("bra", "A549"),
        ("rab", "A549"),
        ("akt", "A549"),
        ("egfr_random", "A549"),
        ("totally_egfr", "A549"),
        ("something_braf", "A549"),
        ("whatever-egfr", "A549"),
        ("ABCDEF123456", None),
    ]

    results = []
    passed = 0
    failed = 0

    for pert, cell in no_hit_queries:
        result = engine.query(pert, cell_line=cell, top_n=20)
        entry = {
            "query": pert,
            "cell_line": cell,
            "found": bool(result.found),
            "matched_perturbation": getattr(result, "perturbation", None),
            "note": result.note,
            "n_obs": int(result.n_obs),
            "activated_terms": int(len(result.top_activated)),
            "suppressed_terms": int(len(result.top_suppressed)),
            "guard_version": "pxfquery-T-031",
        }
        ok = not result.found
        entry["test_passed"] = ok
        results.append(entry)
        if ok:
            passed += 1
        else:
            failed += 1
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {pert} (cell={cell}) -> found={result.found}")

    summary = {
        "task": "T-031",
        "guard_version": "pxfquery-T-031",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "test_type": "negative_no_hit",
        "engine_config": {
            "min_overlap_for_token_fallback": engine.min_overlap_for_token_fallback,
            "min_query_length_for_substring": engine.min_query_length_for_substring,
        },
        "matrix": str(XPR_MATRIX),
        "matrix_shape": matrix_meta.get("shape"),
        "total_queries": len(no_hit_queries),
        "passed": passed,
        "failed": failed,
        "results": results,
        "acceptance_criteria": {
            "min_queries": 3,
            "all_must_return_found_False": passed == len(no_hit_queries),
        },
    }

    evidence_path = TABLE_DIR / "pxfquery_T031_no_hit_evidence.json"
    evidence_path.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"\nNo-hit evidence written to {evidence_path}")
    print(f"Passed: {passed}/{len(no_hit_queries)}")
    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())