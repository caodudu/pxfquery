"""
T-035 smoke-test orchestrator: re-run each predecessor's deliverable as black box.

Launched with PXFQUERY_T035_TASK_ROOT env var set to the T-035 task root.
Each smoke target runs via `conda run -n pxfquery python <script>` with cwd set to
the predecessor task directory. Captures stdout/stderr/exit/elapsed, writes one
consolidated pxfquery_T035_smoke_results.json.
"""
from __future__ import annotations

import json
import os
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

TASK_ROOT = Path(os.environ.get("PXFQUERY_T035_TASK_ROOT", Path(__file__).resolve().parents[3]))
LOG_DIR = TASK_ROOT / "3_execution" / "02_smoke_runs"
TABLE_DIR = TASK_ROOT / "4_artifact" / "5_table"
TABLE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

CONDA_RUN = "/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python"
PROJECT_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")

SMOKE_TARGETS = [
    {
        "task_id": "T-029",
        "smoke_target": "forward_engine.py",
        "predecessor_path": PROJECT_ROOT / "4_phase_development/goal_deterministic_query_engines_v1/task_forward_query_engine_v1",
        "script": "forward_engine.py",
    },
    {
        "task_id": "T-030",
        "smoke_target": "run_reverse_demo.py",
        "predecessor_path": PROJECT_ROOT / "4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1",
        "script": "run_reverse_demo.py",
    },
    {
        "task_id": "T-031",
        "smoke_target": "test_no_hit_guard.py",
        "predecessor_path": PROJECT_ROOT / "4_phase_development/goal_deterministic_query_engines_v1/task_no_hit_guard_v1",
        "script": "test_no_hit_guard.py",
    },
    {
        "task_id": "T-031",
        "smoke_target": "test_positive_control.py",
        "predecessor_path": PROJECT_ROOT / "4_phase_development/goal_deterministic_query_engines_v1/task_no_hit_guard_v1",
        "script": "test_positive_control.py",
    },
    {
        "task_id": "T-032",
        "smoke_target": "run_stability_guard.py",
        "predecessor_path": PROJECT_ROOT / "4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1",
        "script": "run_stability_guard.py",
    },
    {
        "task_id": "T-033",
        "smoke_target": "hybrid_fast_resolver (no executable)",
        "predecessor_path": PROJECT_ROOT / "4_phase_development/goal_resolver_optional_layer_v1/task_hybrid_fast_resolver_v1",
        "script": None,
    },
]


def run_one(target: dict, idx: int) -> dict:
    slug = f"{target['task_id']}_{target['smoke_target'].split('.')[0]}".replace("-", "_").replace(" ", "_")
    rec = {
        "task_id": target["task_id"],
        "smoke_target": target["smoke_target"],
        "status": None,
        "command": None,
        "cwd": str(target["predecessor_path"]),
        "exit_code": None,
        "elapsed_seconds": None,
        "stdout_summary": None,
        "stderr_sample": None,
        "log_stdout_path": None,
        "log_stderr_path": None,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "note": None,
    }

    if target["script"] is None:
        # T-033 — only check 3_execution for any content
        exec_dir = target["predecessor_path"] / "3_execution"
        has_any = exec_dir.exists() and any(exec_dir.iterdir())
        rec["status"] = "SKIPPED" if not has_any else "UNMET_DEPENDENCY"
        rec["note"] = "T-033 resolver is optional. No executable deliverable present. Marked SKIPPED."
        return rec

    # Check if script exists
    script_path = target["predecessor_path"] / "3_execution" / target["script"]
    if not script_path.exists():
        rec["status"] = "UNMET_DEPENDENCY"
        rec["note"] = f"Script not found at {script_path}"
        return rec

    cmd = f"{CONDA_RUN} python 3_execution/{target['script']}"
    rec["command"] = cmd

    stdout_file = LOG_DIR / f"{slug}_stdout.txt"
    stderr_file = LOG_DIR / f"{slug}_stderr.txt"
    rec["log_stdout_path"] = str(stdout_file)
    rec["log_stderr_path"] = str(stderr_file)

    t0 = time.time()
    try:
        proc = subprocess.run(
            [CONDA_RUN.split()[0], "run", "-n", "pxfquery", "python",
             f"3_execution/{target['script']}"],
            cwd=str(target["predecessor_path"]),
            capture_output=True,
            text=True,
            timeout=600,
        )
        elapsed = time.time() - t0
        stdout_file.write_text(proc.stdout or "", encoding="utf-8")
        stderr_file.write_text(proc.stderr or "", encoding="utf-8")
        rec["exit_code"] = proc.returncode
        rec["elapsed_seconds"] = round(elapsed, 3)
        rec["stdout_summary"] = "\n".join((proc.stdout or "").splitlines()[:30])
        rec["stderr_sample"] = "\n".join((proc.stderr or "").splitlines()[:15])
        rec["status"] = "PASS" if proc.returncode == 0 else "FAIL"
        if proc.returncode != 0:
            rec["note"] = f"Non-zero exit code: {proc.returncode}. Check stderr."
        else:
            rec["note"] = f"Pass: exit=0 elapsed={rec['elapsed_seconds']}s"
    except subprocess.TimeoutExpired:
        rec["status"] = "FAIL"
        rec["note"] = "Timed out after 600s"
    except FileNotFoundError as exc:
        rec["status"] = "FAIL"
        rec["note"] = f"Invocation failed: {exc}"
    except Exception as exc:
        rec["status"] = "FAIL"
        rec["note"] = f"Unexpected: {type(exc).__name__}: {exc}"
    return rec


def main() -> int:
    print(f"=== T-035 Smoke Suite ===")
    print(f"task_root: {TASK_ROOT}")
    print(f"log_dir: {LOG_DIR}")
    print(f"output_dir: {TABLE_DIR}")
    print()

    results = []
    for i, tgt in enumerate(SMOKE_TARGETS):
        print(f"[{i+1}/{len(SMOKE_TARGETS)}] {tgt['task_id']} — {tgt['smoke_target']}")
        rec = run_one(tgt, i)
        results.append(rec)
        print(f"  → {rec['status']}  |  {rec.get('note', '')}")
        print()

    summary = {
        "task": "T-035 smoke_tests_v1",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "conda": f"{CONDA_RUN}",
        "counts": {
            "total": len(results),
            "pass": sum(1 for r in results if r["status"] == "PASS"),
            "fail": sum(1 for r in results if r["status"] == "FAIL"),
            "unmet_dependency": sum(1 for r in results if r["status"] == "UNMET_DEPENDENCY"),
            "skipped": sum(1 for r in results if r["status"] == "SKIPPED"),
        },
        "results": results,
    }

    out_path = TABLE_DIR / "pxfquery_T035_smoke_results.json"
    out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"=== Consolidated: {out_path} ===")
    print(json.dumps(summary["counts"], indent=2))

    return 0 if summary["counts"]["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())