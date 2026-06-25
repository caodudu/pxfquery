# T-053 m1_python_package_milestone — Protocol

## Objective

Aggregate T-050 forward validation, T-051 reverse validation, and T-052 package assembly into a single M1 milestone deliverable. Produce a layered asset map, evidence index, demo commands, known gap report, and the final package location/version. Do not repair or reimplement any lower-layer code.

## Position In Project

This is the capstone task under `goal_m1_python_package_v2`. T-050, T-051, and T-052 are all completed with PASS verdicts. This task collects their outputs, indexes them, and presents the milestone as a consumable handoff for downstream delivery/review.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-050 | `task_forward_validation_m1/4_artifact/5_table/forward_validation_results_v20260624.csv` | Primary forward validation evidence (11 checks, all PASS) |
| A-002 | T-050 | `task_forward_validation_m1/4_artifact/3_document/forward_validation_report_v20260624.md` | Full validation narrative for forward query |
| A-003 | T-051 | `task_reverse_validation_m1/4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | Primary reverse validation evidence (42 checks, all PASS) |
| A-004 | T-051 | `task_reverse_validation_m1/4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | Per-check pass/fail table for reverse validation |
| A-005 | T-051 | `task_reverse_validation_m1/4_artifact/3_document/validation_report_v20260624_055812.html` | Human-readable reverse validation HTML report |
| A-006 | T-052 | `task_package_assembly_m1/4_artifact/1_package/` | Assembled M1 pxfquery package source (v0.1.0) |
| A-007 | T-052 | `task_package_assembly_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Import smoke test evidence |
| A-008 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/forward_demo_v20260624.json` | Forward demo JSON (EGFR/A549/xpr, found:true) |
| A-009 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/reverse_demo_v20260624.json` | Reverse demo JSON (MYC_TARGETS_V1/A549, found:true) |
| A-010 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/cli_help_v20260624.txt` | CLI help text capture |
| A-011 | T-052 | `task_package_assembly_m1/4_artifact/3_document/execution_report_v20260624.html` | Package assembly execution report |
| A-012 | T-052 | `task_package_assembly_m1/4_artifact/3_document/result_report_v20260624.html` | Package assembly result report |

## Execution Steps

1. **Collect & index T-050 forward validation evidence** — Read A-001 and A-002. Record: 11/11 PASS, package v0.1.0, M1FixtureLoader, synthetic_repair manifest.
2. **Collect & index T-051 reverse validation evidence** — Read A-003, A-004, A-005. Record: 42/42 PASS, cosine similarity ranking, top-3 matching reference.
3. **Collect & index T-052 package assembly evidence** — Read A-006 through A-012. Record: pip installable package at source path, version 0.1.0, all 9 acceptance criteria passed, forward/reverse CLI demos working.
4. **Build layered asset map** — Map which predecessor produced which asset, which layer (skeleton → forward implementation → reverse implementation → package assembly → forward validation → reverse validation) each asset belongs to, and which assets are consumed by this milestone.
5. **Write evidence index** — Create a structured index (JSON or Markdown) listing all three evidence streams with verdicts, key metrics, and cross-references.
6. **Record demo commands** — Document working CLI commands for forward query, reverse query, and info subcommand as validated by T-052 and T-050/T-051.
7. **Identify known gaps** — Check for any missing evidence, incomplete coverage, or known limits reported by predecessors. Report precise failed layer if evidence is missing; do not fix.
8. **Write milestone report** — Compile all findings into `5_report/milestone_report_v<timestamp>.md` (or `.html`).
9. **Register deliverables** — Update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not re-run validation or re-assemble the package.
- Do not modify any predecessor task artifact or directory.
- Do not read project-level raw assets under `2_project_asset/`.
- Do not implement, repair, or modify any query logic or package code.
- All information must come from predecessor handoffs and registered artifacts.
- If any required evidence stream is missing, report the failed layer and recommend a same-layer repair task; do not mark gaps as done.

## Forbidden

- Modifying predecessor task files or directories.
- Re-running validation or assembly commands.
- Reading `2_project_asset/` (forbidden for non-digestion task).
- Reading T-024 through T-040 artifacts.
- Creating duplicate or redundant evidence.

## Web Search Allowance

Allowed: no
Reason: All evidence is local from predecessor tasks. No external information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Milestone report | `4_artifact/3_document/milestone_report_v<timestamp>.md` (or .html) | yes |
| Evidence index (structured) | `4_artifact/2_persist/evidence_index_v<timestamp>.json` | yes |
| Layered asset map | `4_artifact/5_table/layered_asset_map_v<timestamp>.csv` (or .md) | yes |
| Known gap report | `4_artifact/5_table/known_gaps_v<timestamp>.md` | yes |
| Demo commands reference | `4_artifact/2_persist/demo_commands_v<timestamp>.md` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- All three evidence streams (T-050, T-051, T-052) are collected and summarized with verdicts.
- Final package location and version (v0.1.0) are documented.
- Layered asset map shows predecessor provenance for each layer.
- Known gaps are explicitly listed, including any predecessor-reported limits.
- Demo commands are verified against T-052 output.
- No predecessor artifacts were modified.
- All deliverables registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- If a predecessor task was not completed successfully (verdict not PASS), report the gap and recommend a same-layer repair. Do not fabricate evidence.
- If any required predecessor artifact path cannot be resolved, report the missing path and recommend investigation in the originating task.
- Do not proceed if the assembled package source (A-006) is missing or non-functional.

## Delivery Requirements

- Register all accepted outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
