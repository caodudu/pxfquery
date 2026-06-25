from __future__ import annotations

import csv
import json
from pathlib import Path

from pxfquery import PxFquery
from pxfquery.data.m1_loader import M1FixtureLoader


TASK_ROOT = Path(__file__).resolve().parents[1]
MATRIX = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_repair_fixture_m1_1" / "xpr_func_fixture_m1.h5ad"
MANIFEST = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_repair_manifest_m1_1.yaml"
FIXTURE_ROOT = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_repair_fixture_m1_1"
DEMO_JSON = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_demo_evidence_v20260624.json"
ERROR_JSON = TASK_ROOT / "4_artifact" / "2_persist" / "reverse_error_no_hit_evidence_v20260624.json"
RANKING_CSV = TASK_ROOT / "4_artifact" / "5_table" / "reverse_ranking_evidence_v20260624.csv"


def _assert_positive(result: dict) -> None:
    assert result["found"] is True
    assert result["activate"] == ["HALLMARK_APOPTOSIS"]
    assert result["suppress"] == ["HALLMARK_MYC_TARGETS_V1"]
    assert result["cell_line"] == "A549"
    assert result["candidate_columns"] == ["cmap_name", "cell_iname", "similarity", "driving_terms"]
    assert 1 <= len(result["top_candidates"]) <= 10
    similarities = [row["similarity"] for row in result["top_candidates"]]
    assert similarities == sorted(similarities, reverse=True)
    assert all(isinstance(value, (int, float)) for value in similarities)


def main() -> None:
    loader = M1FixtureLoader(str(MANIFEST), fixture_root=str(FIXTURE_ROOT))
    fixture = loader.fixture
    assert fixture.matrix_shape("xpr") == (15, 9)
    assert "HALLMARK_MYC_TARGETS_V1" in fixture.matrix_var_names("xpr")

    query = PxFquery(str(MATRIX), matrix_type="xpr")
    positive = query.func2pert(
        activate=["HALLMARK_APOPTOSIS"],
        suppress=["HALLMARK_MYC_TARGETS_V1"],
        cell_line="A549",
        matrix_type="xpr",
        top_n=10,
    )
    repeat = query.func2pert(
        activate=["HALLMARK_APOPTOSIS"],
        suppress=["HALLMARK_MYC_TARGETS_V1"],
        cell_line="A549",
        matrix_type="xpr",
        top_n=10,
    )
    _assert_positive(positive)
    assert positive["top_candidates"] == repeat["top_candidates"]

    evidence = {
        "command": (
            "conda run -n pxfquery env "
            "PYTHONPATH=<task>/4_artifact/1_package "
            "python 3_execution/run_reverse_evidence.py"
        ),
        "matrix": str(MATRIX.relative_to(TASK_ROOT)),
        "manifest": str(MANIFEST.relative_to(TASK_ROOT)),
        "loader_check": {
            "loader": "pxfquery.data.m1_loader.M1FixtureLoader",
            "xpr_shape": list(fixture.matrix_shape("xpr")),
            "has_HALLMARK_MYC_TARGETS_V1": True,
            "has_A549": True,
        },
        "result": positive,
        "repeatability": {
            "same_top_candidates_on_repeat": positive["top_candidates"] == repeat["top_candidates"],
            "stable_sort_keys": ["similarity desc", "cmap_name asc", "cell_iname asc", "sig_id asc"],
        },
    }
    DEMO_JSON.write_text(json.dumps(evidence, indent=2))

    errors = {
        "command": (
            "conda run -n pxfquery env "
            "PYTHONPATH=<task>/4_artifact/1_package "
            "python 3_execution/run_reverse_evidence.py"
        ),
        "cases": {
            "no_matrix_loaded": PxFquery().func2pert(["HALLMARK_APOPTOSIS"], [], "A549"),
            "unknown_program": query.func2pert(["NONEXISTENT_PROGRAM_XXX"], [], "A549"),
            "unknown_cell_line": query.func2pert(["HALLMARK_APOPTOSIS"], [], "UNKNOWN_CELL_LINE"),
            "low_confidence": query.func2pert(["NON_DIFFERENTIALLY_SCORED_PROGRAM"], [], "A549"),
            "empty_target_no_hit": query.func2pert([], [], "A549"),
        },
    }
    assert errors["cases"]["no_matrix_loaded"]["error"] == "NoMatrixLoaded"
    assert errors["cases"]["unknown_program"]["error"] == "ProgramNotFound"
    assert errors["cases"]["unknown_cell_line"]["error"] == "ContextNotFound"
    assert errors["cases"]["low_confidence"]["error"] == "LowConfidenceResult"
    assert errors["cases"]["empty_target_no_hit"]["found"] is False
    ERROR_JSON.write_text(json.dumps(errors, indent=2))

    with RANKING_CSV.open("w", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["rank", "cmap_name", "cell_iname", "similarity", "driving_terms", "sig_id"],
        )
        writer.writeheader()
        for rank, candidate in enumerate(positive["top_candidates"], start=1):
            writer.writerow({"rank": rank, **candidate})


if __name__ == "__main__":
    main()
