from __future__ import annotations

import csv
import json
import math
import os
import sys
from pathlib import Path
from typing import Any


TASK_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = TASK_ROOT / "4_artifact" / "1_package"
MANIFEST_PATH = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/"
    "task_m1_fixture_loader/1_asset/resource_manifest_m1.yaml"
)

sys.path.insert(0, str(PACKAGE_ROOT))

from pxfquery import PxFquery  # noqa: E402


def main() -> int:
    persist_dir = TASK_ROOT / "4_artifact" / "2_persist"
    table_dir = TASK_ROOT / "4_artifact" / "5_table"
    persist_dir.mkdir(parents=True, exist_ok=True)
    table_dir.mkdir(parents=True, exist_ok=True)

    smoke = loader_smoke()
    query = PxFquery(str(MANIFEST_PATH), matrix_type="xpr")
    demo = query.pert2func("EGFR", "A549", matrix_type="xpr", top_k=20)
    no_hit = {
        "unknown_perturbation": query.pert2func("UNKNOWN_GENE_XYZ999", "A549", matrix_type="xpr", top_k=20),
        "unknown_cell_line": query.pert2func("EGFR", "UNKNOWN_CELL_LINE", matrix_type="xpr", top_k=20),
        "no_matrix_loaded": PxFquery().pert2func("EGFR", "A549", matrix_type="xpr", top_k=20),
    }

    demo_bundle = {
        "task_id": "T-048",
        "case_id": "DEMO-001",
        "source_contract": "T-042/D-001 and T-042/D-002",
        "loader_source": "T-046/D-001",
        "loader_manifest_path": str(MANIFEST_PATH),
        "loader_smoke": smoke,
        "input": {
            "perturbation": "EGFR",
            "cell_line": "A549",
            "matrix_type": "xpr",
            "top_k": 20,
        },
        "observed": demo,
    }
    no_hit_bundle = {
        "task_id": "T-048",
        "case_id": "DEMO-001.no_hit_variants",
        "source_contract": "T-042/D-001 and T-042/D-002",
        "loader_source": "T-046/D-001",
        "input": {
            "matrix_type": "xpr",
            "variants": ["unknown_perturbation", "unknown_cell_line", "no_matrix_loaded"],
        },
        "observed": no_hit,
    }

    write_json(persist_dir / "forward_query_demo_evidence_v20260624.json", demo_bundle)
    write_json(persist_dir / "forward_query_no_hit_evidence_v20260624.json", no_hit_bundle)

    assertions = build_assertions(demo, no_hit, smoke)
    with open(table_dir / "forward_query_contract_assertions_v20260624.csv", "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["assertion_id", "scope", "expected", "observed", "status"])
        writer.writeheader()
        writer.writerows(assertions)

    return 0 if all(row["status"] == "PASS" for row in assertions) else 1


def loader_smoke() -> dict[str, Any]:
    query = PxFquery(str(MANIFEST_PATH), matrix_type="xpr")
    fixture = query.loader.fixture
    xpr = fixture.xpr
    return {
        "status": "PASS",
        "matrix_type": "xpr",
        "shape": list(fixture.matrix_shape("xpr")),
        "obs_columns": fixture.matrix_obs_columns("xpr"),
        "var_names": fixture.matrix_var_names("xpr"),
        "sig_ids": fixture.get_sig_ids("xpr"),
        "matching_rows_for_EGFR_A549": int(
            ((xpr.obs["cmap_name"].astype(str) == "EGFR") & (xpr.obs["cell_iname"].astype(str) == "A549")).sum()
        ),
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    with open(path, "w") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def build_assertions(demo: dict[str, Any], no_hit: dict[str, Any], smoke: dict[str, Any]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    def add(assertion_id: str, scope: str, expected: str, observed: Any, passed: bool) -> None:
        rows.append(
            {
                "assertion_id": assertion_id,
                "scope": scope,
                "expected": expected,
                "observed": json.dumps(observed, ensure_ascii=False, sort_keys=True),
                "status": "PASS" if passed else "FAIL",
            }
        )

    add("SMOKE-001", "loader", "loader exposes xpr matrix with EGFR/A549 row", smoke, smoke["matching_rows_for_EGFR_A549"] >= 1)
    add("FWD-001", "demo", "found == true", demo.get("found"), demo.get("found") is True)
    add("FWD-002", "demo", "input echo EGFR/A549", {"perturbation": demo.get("perturbation"), "cell_line": demo.get("cell_line")}, demo.get("perturbation") == "EGFR" and demo.get("cell_line") == "A549")
    add("FWD-003", "demo", "n_obs >= 1 and cells_used contains A549", {"n_obs": demo.get("n_obs"), "cells_used": demo.get("cells_used")}, demo.get("n_obs", 0) >= 1 and "A549" in demo.get("cells_used", []))
    add("FWD-004", "demo", "top_activated non-empty numeric dict", demo.get("top_activated"), is_numeric_dict(demo.get("top_activated")) and len(demo.get("top_activated", {})) >= 1)
    add("FWD-005", "demo", "top_suppressed non-empty numeric dict", demo.get("top_suppressed"), is_numeric_dict(demo.get("top_suppressed")) and len(demo.get("top_suppressed", {})) >= 1)
    add("FWD-006", "demo", "activated positive and suppressed negative", {"top_activated": demo.get("top_activated"), "top_suppressed": demo.get("top_suppressed")}, values_positive(demo.get("top_activated")) and values_negative(demo.get("top_suppressed")))
    add("NOHIT-001", "unknown_perturbation", "error == PerturbationNotFound", no_hit["unknown_perturbation"], no_hit["unknown_perturbation"].get("error") == "PerturbationNotFound")
    add("NOHIT-002", "unknown_cell_line", "error == ContextNotFound", no_hit["unknown_cell_line"], no_hit["unknown_cell_line"].get("error") == "ContextNotFound")
    add("NOHIT-003", "no_matrix_loaded", "error == NoMatrixLoaded", no_hit["no_matrix_loaded"], no_hit["no_matrix_loaded"].get("error") == "NoMatrixLoaded")
    add("NOHIT-004", "no_hit_shape", "all no-hit responses include query_type", {k: v.get("query_type") for k, v in no_hit.items()}, all(v.get("query_type") in {"forward", "system"} for v in no_hit.values()))
    return rows


def is_numeric_dict(value: Any) -> bool:
    return isinstance(value, dict) and all(isinstance(k, str) and isinstance(v, (int, float)) and math.isfinite(v) for k, v in value.items())


def values_positive(value: Any) -> bool:
    return is_numeric_dict(value) and all(v > 0 for v in value.values())


def values_negative(value: Any) -> bool:
    return is_numeric_dict(value) and all(v < 0 for v in value.values())


if __name__ == "__main__":
    raise SystemExit(main())
