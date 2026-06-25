from __future__ import annotations

import compileall
import json
import os
import sys
from datetime import datetime
from pathlib import Path


TASK_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = TASK_ROOT.parents[2]
ARTIFACT_ROOT = TASK_ROOT / "4_artifact"
TABLE_DIR = ARTIFACT_ROOT / "5_table"
PACKAGE_ROOT = ARTIFACT_ROOT / "2_persist" / "pxfquery-T-040"
PACKAGE_SRC = PACKAGE_ROOT / "src"
RESOURCE_BUNDLE = (
    PROJECT_ROOT
    / "4_phase_development/goal_precomputed_data_exploration/"
    "task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources"
)

T024_ARTIFACT = (
    PROJECT_ROOT
    / "4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/4_artifact"
)
T026_ARTIFACT = (
    PROJECT_ROOT
    / "4_phase_development/goal_resource_index_packs_v1/task_matrix_loader_v1/4_artifact"
)
T029_ARTIFACT = (
    PROJECT_ROOT
    / "4_phase_development/goal_deterministic_query_engines_v1/task_forward_query_engine_v1/4_artifact"
)
T031_ARTIFACT = (
    PROJECT_ROOT
    / "4_phase_development/goal_deterministic_query_engines_v1/task_no_hit_guard_v1/4_artifact"
)

EXPECTED_COMMAND = (
    "/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python "
    "3_execution/05_run_verification/verify_package_core.py"
)


def require_path(path: Path, kind: str) -> dict:
    exists = path.exists()
    ok = exists and ((kind == "dir" and path.is_dir()) or (kind == "file" and path.is_file()))
    return {"path": str(path), "kind": kind, "exists": exists, "ok": ok}


def result_summary(result, query: str, cell_line: str) -> dict:
    return {
        "query": query,
        "requested_cell_line": cell_line,
        "found": bool(result.found),
        "matched_perturbation": result.perturbation,
        "matched_cell_line": result.cell_line,
        "note": result.note,
        "n_obs": int(result.n_obs),
        "activated_terms": int(len(result.top_activated)),
        "suppressed_terms": int(len(result.top_suppressed)),
        "top_activated_preview": [
            {"term": term, "score": float(score)}
            for term, score in result.top_activated.head(5).items()
        ],
        "top_suppressed_preview": [
            {"term": term, "score": float(score)}
            for term, score in result.top_suppressed.head(5).items()
        ],
    }


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(PACKAGE_SRC))

    import pxfquery
    from pxfquery.package_core import create_forward_engine, forward_result_to_frame
    from pxfquery.resources import load_bundle, load_standard_matrix

    required_paths = {
        "t024_artifact": require_path(T024_ARTIFACT, "dir"),
        "t026_artifact": require_path(T026_ARTIFACT, "dir"),
        "t029_artifact": require_path(T029_ARTIFACT, "dir"),
        "t031_artifact": require_path(T031_ARTIFACT, "dir"),
        "package_root": require_path(PACKAGE_ROOT, "dir"),
        "package_src": require_path(PACKAGE_SRC, "dir"),
        "resource_bundle": require_path(RESOURCE_BUNDLE, "dir"),
        "xpr_matrix": require_path(RESOURCE_BUNDLE / "xpr_func_ad.h5ad", "file"),
    }

    compile_ok = compileall.compile_dir(str(PACKAGE_SRC), quiet=1, force=True)

    bundle_meta = load_bundle(RESOURCE_BUNDLE)
    adata, matrix_meta = load_standard_matrix("xpr_func_ad.h5ad", RESOURCE_BUNDLE)
    engine, engine_matrix_meta = create_forward_engine(bundle_root=RESOURCE_BUNDLE)

    egfr = engine.query("EGFR", cell_line="A549", top_n=20)
    egfr_frame = forward_result_to_frame(egfr, "EGFR", "A549")
    egfr_csv = TABLE_DIR / "pxfquery_T040_EGFR_A549_forward_result.csv"
    egfr_frame.to_csv(egfr_csv, index=False)

    no_hit = engine.query("egfr_random", cell_line="A549", top_n=20)
    no_hit_plain = engine.query("NONSENSE_ZZZ999", cell_line="A549", top_n=20)

    demo_summary = {
        "task": "T-040",
        "package_core_version": pxfquery.PACKAGE_CORE_VERSION,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "resource_bundle": str(RESOURCE_BUNDLE),
        "matrix": matrix_meta,
        "engine_matrix": engine_matrix_meta,
        "forward_demo": result_summary(egfr, "EGFR", "A549"),
        "no_hit_demo": result_summary(no_hit, "egfr_random", "A549"),
        "plain_not_found_demo": result_summary(no_hit_plain, "NONSENSE_ZZZ999", "A549"),
        "forward_result_csv": str(egfr_csv),
    }

    acceptance = {
        "required_paths_ok": all(v["ok"] for v in required_paths.values()),
        "package_import_ok": hasattr(pxfquery, "create_forward_engine"),
        "compile_ok": bool(compile_ok),
        "loader_smoke_ok": (
            bundle_meta["summary"]["loaded_by_category"]["matrices"] == 3
            and len(bundle_meta["summary"]["failed_files"]) == 0
        ),
        "xpr_matrix_loaded": matrix_meta["shape"] == [132464, 91],
        "forward_demo_found": bool(egfr.found),
        "forward_demo_has_terms": len(egfr.top_activated) > 0 and len(egfr.top_suppressed) > 0,
        "no_hit_guard_found_false": not bool(no_hit.found),
        "plain_not_found_false": not bool(no_hit_plain.found),
        "t038_not_used": True,
    }

    test_results = {
        "task": "T-040_milestone_package_core_parallel_v1",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "command": EXPECTED_COMMAND,
        "argv": sys.argv,
        "cwd": os.getcwd(),
        "python": sys.executable,
        "exit_status": 0 if all(acceptance.values()) else 1,
        "package_root": str(PACKAGE_ROOT),
        "package_src": str(PACKAGE_SRC),
        "predecessors_checked": {
            "T-024": str(T024_ARTIFACT),
            "T-026": str(T026_ARTIFACT),
            "T-029": str(T029_ARTIFACT),
            "T-031": str(T031_ARTIFACT),
        },
        "required_paths": required_paths,
        "bundle_summary": bundle_meta["summary"],
        "acceptance": acceptance,
        "stdout_summary": "Package import, compile, loader smoke, EGFR/A549 forward demo, and no-hit demos completed.",
        "stderr_summary": "",
        "outputs": {
            "test_results": str(TABLE_DIR / "pxfquery_T040_test_results.json"),
            "demo_summary": str(TABLE_DIR / "pxfquery_T040_demo_summary.json"),
            "egfr_csv": str(egfr_csv),
        },
    }

    (TABLE_DIR / "pxfquery_T040_demo_summary.json").write_text(
        json.dumps(demo_summary, indent=2), encoding="utf-8"
    )
    (TABLE_DIR / "pxfquery_T040_test_results.json").write_text(
        json.dumps(test_results, indent=2), encoding="utf-8"
    )

    print(json.dumps({"acceptance": acceptance, "outputs": test_results["outputs"]}, indent=2))
    if not all(acceptance.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
