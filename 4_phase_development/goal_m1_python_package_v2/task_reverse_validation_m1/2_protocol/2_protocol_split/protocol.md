# T-051 reverse_validation_m1 — Protocol

## Objective

Independently validate the M1 reverse query implementation delivered by T-060 (repair replacement for T-049). Re-run the T-042 reverse demo case against the T-060 package code and repair fixture/manifest. Deliver smoke logs, JSON output, pass/fail result, and traceability to the package version, loader, fixture/manifest, ranking/scoring behavior, and output JSON. Do not hide instability by changing acceptance criteria.

## Position In Project

This task sits under `goal_m1_python_package_v2` and is the independent validation gate for the T-060 reverse query core repair. T-049 (the original implementation) failed with `execute_config_mismatch` and was replaced by T-060. T-060 completed execution but received `red_return` in delivery QA because its registered package-code artifact is a symlink to the T-044 package skeleton, not self-contained task-local code. This validation task treats the T-060 package path (under `4_artifact/1_package/pxfquery/`) as the implementation under test, noting the symlink provenance as a traceability observation. This task does not repair T-060; it independently validates and reports pass/fail honestly.

## Inputs

| Asset ID | Source Task | Source Artifact | Path | Why needed |
|---|---|---|---|---|
| A-001 | T-060 | D-001 | `4_artifact/1_package/pxfquery` | Implementation under test: reverse query package code (note: symlink to T-044; see T-060 delivery_qa.md) |
| A-002 | T-060 | D-002 | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Repair fixture substrate for the T-042 reverse demo case (xpr matrix with HALLMARK_MYC_TARGETS_V1 + A549) |
| A-003 | T-060 | D-003 | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Manifest for loading the repair fixture via T-046 M1FixtureLoader |
| A-004 | T-060 | D-005 | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Reference positive demo JSON for comparison/reproducibility check |
| A-005 | T-060 | D-006 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Reference no-hit/error JSON for comparison |
| A-006 | T-060 | D-007 | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` | Reference ranking evidence for deterministic scoring comparison |

## Execution Steps

1. Record the registered package version and path: inspect `4_artifact/1_package/pxfquery` symlink target, report the resolved path and whether it points to T-044.
2. Load the repair fixture/manifest using the T-046 `M1FixtureLoader` API and confirm matrix shape, target columns, and cell-line coverage.
3. Run the T-042 reverse positive demo case: activate `HALLMARK_APOPTOSIS`, suppress `HALLMARK_MYC_TARGETS_V1`, cell line `A549`, matrix type `xpr`, top-n 3, using the repair xpr matrix. Record stdout, stderr, exit code, and elapsed time.
4. Run the structured no-hit/error cases matching T-042 contract: `NoMatrixLoaded`, `ProgramNotFound`, `ContextNotFound`, `LowConfidenceResult`, empty-target no-hit. Record results.
5. Compare the ranking output against T-060 reference evidence (A-004, A-006): check JSON structure, candidate order, similarity values, and repeatability.
6. Run the CLI reverse interface and confirm smoke output matches documented behavior.
7. Write a structured JSON validation report comparing observed vs. expected behavior with explicit pass/fail per check.
8. Register all accepted outputs in `4_artifact/registry.yaml`.

## Constraints

- Do not modify T-060 artifacts, T-049 artifacts, or any upstream completed task outputs.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not relax acceptance criteria to hide instability. Failure should produce clear evidence for same-layer repair/retry.
- Use the `pxfquery` conda environment: `/Users/dudu/Softwares/miniconda/envs/pxfquery`.
- All reverse query code under test must go through the T-046 loader API; do not write an ad hoc data reader.

## Forbidden

- Modifying predecessor task artifacts (T-042, T-043, T-044, T-046, T-049, T-060).
- Reading project-level raw assets under `2_project_asset/`.
- Reading T024-T040 blocked assets.
- Writing protocols or tasks outside the current task structure.
- Calling downstream prompt endpoints (`/prompt/generate`, `/prompt/generate-check`, `/prompt/generate-delivery`).

## Web Search Allowance

Allowed: no
Reason: This is an independent re-validation of existing task-local artifacts. No external or current information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reverse validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v{date}.json` | yes |
| Smoke logs and evidence | `3_execution/` | yes |
| Validation summary (table/comparison) | `4_artifact/5_table/reverse_validation_comparison_v{date}.csv` | recommended |
| Execution report (HTML) | `4_artifact/3_document/validation_report_v{date}.html` | recommended |
| Completion report | `5_report/completion.md` | yes |
| Artifact registry | `4_artifact/registry.yaml` | yes |

## Acceptance Criteria

- Validation report JSON is produced with structured pass/fail per check.
- All T-042 reverse demo checks run without unhandled exceptions.
- Pass/fail verdict is explicitly stated (not ambiguous).
- Traceability records: package code path and resolved symlink target, loader version, fixture manifest ID, ranking/scoring method.
- If T-060 reference outputs do not reproduce exactly, the report states the difference and does not silently accept them.

## Failure / Stop Rules

- If the T-060 package path is unresolvable or the code cannot be imported, stop and report the import error with full traceback. Do not invent a fallback implementation.
- If the repair fixture cannot be loaded by the T-046 loader API, stop and report the loader error.
- If any validation step throws an unhandled exception, stop and report the error as a failure.
- Do not fail silently; every check must have an explicit pass or fail entry in the validation report.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
