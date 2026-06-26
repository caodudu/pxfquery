# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:33

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-050 forward_validation_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1`
- Objective:

```text
Independently validate the M1 forward query implementation. Use T-048 as the implementation under test and rerun the forward demo case from the contract. Deliver smoke logs, JSON output, pass/fail result, and traceability to the loader, fixture/manifest, and package version used. This task must not repair the implementation except for task-local test harness files; failures should be reported as validation failures for same-layer repair.
```

## Source Material You May Use

Use only the source material embedded below. Do not read old HTML reports. Do not scan predecessor tasks, raw assets, project asset libraries, CLI logs, prompt files, or unrelated folders.

### Project Overview
```text
# Overview

PxFquery is a macOS-hosted restart of a legacy bioinformatics project for LINCS-based perturbation-to-function analysis.

The project's active purpose is to turn useful legacy code, data, reports, and manuscript strategy into a controlled current workspace for later development and submission work. It is not a continuation of the old Windows-era directory trees.

Scientifically, PxFquery is a Python workflow/tool for querying drug- and gene-induced functional programs from perturbation data. Its core direction is:

- forward query: perturbation and biological context to functional response;
- reverse query: functional target and biological context to candidate perturbations;
- evidence-aware retrieval using exact and proxy matches;
- manuscript positioning around a concrete LINCS functional genomics use case rather than an inflated AI-agent platform claim.

The legacy project contains valuable material, including package code, query indexes, CMAP/LINCS-derived functional matrices, resolver reports, and Genes submission strategy. In the current project, those materials are treated as migrated or registered historical assets. Their useful meaning should be digested into current tasks before reuse.

The current project protocol is the persistent project-level rule layer. It should stay concise, current, and independent of old 4t, Obsidian, checkpoint, or Windows directory protocol shells.

```

### Project Goal
```text
# Goal

## Primary Goal

Build a clean, current PxFquery project that can reuse the valuable legacy assets to support controlled software development, reproducible analysis, and a pragmatic manuscript path.

## Scientific Goal

Position PxFquery as a LINCS-based perturbation-to-function bioinformatics workflow for interpreting drug- and gene-induced functional programs in biological contexts such as cancer cell lines.

## Functional Delivery Goal

PxFquery's project-level functional goal is not limited to static matrix lookup. A project-valid package must preserve the intended user-facing query experience:

- forward query: perturbation and biological context to functional response;
- reverse query: functional target and biological context to candidate perturbations;
- resolver-mediated natural-language or semi-structured query entry;
- exact, proxy, and not-found evidence routing for sparse biological coverage;
- LLM-assisted parsing and summarization through the current configured AI service when a milestone requires the user-facing resolver layer;
- deterministic fallback and transparent evidence metadata when LLM or proxy routing fails.

Milestones may stage these capabilities in layers, but a milestone may not silently redefine PxFquery as only deterministic dictionary or matrix lookup if the user-defined milestone requires resolver, LLM, proxy, or transfer behavior. Any proposed scope reduction, deferral, or optionalization of a functional capability must be explicitly reported to the user before task creation and must receive user approval.

## Manuscript Goal

Prepare for a realistic MDPI Genes-style submission by emphasizing a narrow, reproducible functional genomics workflow and a concrete biological case study, rather than presenting PxFquery as a broad AI-agent platform.

This manuscript path is graduation-oriented and journal-fit-oriented. The target is not to build a genuinely high-novelty tool paper or to compete with venues such as Bioinformatics, Nature-family journals, or other high-bar computational biology outlets. The work should look sufficiently substantial in the style of recent Genes papers while remaining practically lightweight, easy t

...[truncated by CyHex prompt assembler: 1049 chars omitted]
```

### Task Protocol
```text
# T-050 forward_validation_m1 — Protocol

## Objective

Independently validate the M1 forward query implementation delivered by T-059 (same-layer replacement for T-048). Re-run the T-042 forward demo contract case (EGFR/A549/xpr positive hit + no-hit behavior) against the T-059 package and repair fixture, record traceability to package version, loader, fixture/manifest, and output JSON, and produce a pass/fail validation result. This task must not repair the implementation; failures must be reported as validation failures for same-layer repair/retry.

**Note on T-048 vs T-059:** The T-050 meta.yaml references T-048 as the implementation under test, but T-059 is the selected predecessor and is the accepted same-layer replacement for T-048. T-050 validates T-059's output, not T-048's. Use T-059 `4_artifact/1_package/` as the implementation under test.

## Position In Project

This task sits under `goal_m1_python_package_v2` in the development phase. T-059 has already delivered the forward query core package plus a synthetic repair fixture that bridges the T-042 EGFR/A549/xpr demo contract gap. T-050 independently re-runs that demo to confirm the implementation is reproducible and the contract assertions hold from an independent perspective.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-059/D-001 | `4_artifact/1_package/` | M1 forward query package under validation |
| A-002 | T-059/D-003 | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Fixture to re-run the positive demo |
| A-003 | T-059/D-002 | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Traceability to fixture provenance and loader boundary |
| A-004 (optional) | T-059/D-004 | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Reference positive output for comparison |
| A-005 (optional) | T-059/D-005 | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Reference no-hit output for comparison |
| A-006 (optional) | T-059/D-006 | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Reference assertion outcome table |

All asset paths are under the T-059 task directory at `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/`.

## Execution Steps

1. **Environment setup.** Install or configure the T-059 package from `A-001` into the pxfquery conda environment. Record the installed package version (`pip show pxfquery` or equivalent).
2. **Fixture loading smoke test.** Load the repair fixture `A-002` using the T-046-compatible `M1FixtureLoader` (or equivalent loader API in the package). Assert that the fixture loads without error and the xpr matrix has the expected shape (5 obs x 7 vars per the manifest). Record the loader class and path.
3. **Positive forward demo.** Run the EGFR/A549/xpr forward query against the loaded fixture. Collect the returned JSON/dict output. Verify:
   - `found` is `true`
   - `perturbation` is `EGFR`
   - `cell_line` is `A549`
   - `n_obs` is a positive integer
   - `top_activated` is a non-empty numeric dict
   - `top_suppressed` is a non-empty numeric dict
   - Input echo matches the requested perturbation and cell line
4. **No-hit forward demo.** Run a forward query for an unknown perturbation (e.g. `UNKNOWN_GENE_XYZ999`) against the same fixture. Verify:
   - Output is a structured error/no-hit object (e.g. `{"error": "PerturbationNotFound", ...}`)
   - No Python traceback leaks into the output
   - A relevant error message and suggestions are present
5. **Compare with reference.** Compare the re-run positive JSON (step 3) with the reference evidence `A-004`. Structural shape and key fields should match. Numerical values may differ — focus on structural consistency.
6. **CLI smoke test.** Invoke the forward query via CLI (`pxfquery forward ...`) for the positive case. Assert that stdout contains valid JSON and exit code is 0.
7. **Record traceability.** In the validation report, record:
   - Package version (from `pip show pxfquery` or `importlib.metadata`)
   - Loader class and path
   - Fixture manifest path and synthetic_repair provenance label
   - Reference evidence paths used for comparison
   - All re-run output JSON content
8. **Produce pass/fail result.** Compile a validation results table (CSV) with one row per check (import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo), each marked PASS/FAIL.

## Constraints

- Do not repair core logic — this is independent validation only.
- Do not modify T-059 artifacts or any predecessor task outputs.
- Failures must produce evidence for same-layer repair/retry, not silent workaround.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Preserve the `synthetic_repair` provenance label when referencing the repair fixture. Do not strip or rename it.

## Forbidden

- Modifyin

...[truncated by CyHex prompt assembler: 2854 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
  - id: D-001
    name: forward_validation_smoke_log
    type: log
    path: 4_artifact/2_persist/forward_validation_smoke_v20260624.log
    description: Smoke execution log recording install, fixture load, forward demo, no-hit demo, reference comparison, and CLI test.

  - id: D-002
    name: forward_validation_rerun_positive
    type: json
    path: 4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json
    description: Re-run positive forward query JSON output (EGFR/A549/xpr).

  - id: D-003
    name: forward_validation_rerun_nohit
    type: json
    path: 4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json
    description: Re-run no-hit forward query JSON output (UNKNOWN_GENE_XYZ999/A549).

  - id: D-004
    name: forward_validation_results_table
    type: table
    path: 4_artifact/5_table/forward_validation_results_v20260624.csv
    description: Validation results table with 11 PASS/FAIL checks.

  - id: D-005
    name: forward_validation_report
    type: document
    path: 4_artifact/3_document/forward_validation_report_v20260624.md
    description: Validation report documenting all steps, traceability, and overall pass/fail.

  - id: D-006
    name: execution_report
    type: report
    path: 4_artifact/3_document/execution_report_v20260624.html
    description: HTML rendering of smoke log and outputs.

  - id: D-007
    name: result_report
    type: report
    path: 4_artifact/3_document/result_report_v20260624.html
    description: HTML rendering of validation results table.

```

### Completion Report
```md
# Completion

**Task:** T-050 forward_validation_m1
**Completed:** 2026-06-24
**Overall Verdict:** PASS

## Summary

Independently validated the T-059 M1 forward query implementation by re-running the T-042 EGFR/A549/xpr demo contract case. All 11 checks passed.

## Checks Performed

| Check ID | Status |
|---|---|
| SMOKE-001 (package import) | PASS |
| SMOKE-002 (fixture load) | PASS |
| FORWARD-001 (positive hit) | PASS |
| FORWARD-002 (top_activated) | PASS |
| FORWARD-003 (top_suppressed) | PASS |
| FORWARD-004 (input echo) | PASS |
| NOHIT-001 (structured error) | PASS |
| NOHIT-002 (no traceback) | PASS |
| JSON-001 (positive structural match) | PASS |
| JSON-002 (no-hit structural match) | PASS |
| CLI-001 (CLI smoke test) | PASS |

## Deliverables Produced

- `4_artifact/2_persist/forward_validation_smoke_v20260624.log`
- `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json`
- `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json`
- `4_artifact/5_table/forward_validation_results_v20260624.csv`
- `4_artifact/3_document/forward_validation_report_v20260624.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`

## Traceability

- Package: pxfquery v0.1.0 (T-059 package, installed from `3_execution/forward_query_package_m1_local`)
- Loader: pxfquery.data.m1_loader.M1FixtureLoader
- Manifest: `1_asset/forward_repair_manifest_m1_1.yaml` (provenance_label: synthetic_repair)
- Fixture: `1_asset/forward_repair_fixture_m1_1` (xpr shape (5, 7))
- Reference positive: `1_asset/forward_query_positive_demo_evidence.json`
- Reference no-hit: `1_asset/forward_query_no_hit_evidence.json`

## Notes

- This task validates T-059 (replacement for T-048) as specified in protocol clarification.
- Re-run positive output matches reference structurally; the only key difference is `_evidence` field which is T-059 harness-specific metadata.
- Re-run no-hit output matches reference structurally; same `_evidence` difference.
- No core logic was modified. This was pure independent validation.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-050 forward_validation_m1

## Task Goal
Independently validate the M1 forward query implementation (T-059) by re-running the T-042 EGFR/A549/xpr demo contract case. Produce pass/fail, traceability, and evidence.

## What Was Delivered
- Smoke log, re-run positive JSON, re-run no-hit JSON, validation results CSV, validation report MD, two HTML reports
- All 11 checks PASS, overall verdict PASS
- Traceability to package version (0.1.0), loader class (M1FixtureLoader), manifest (synthetic_repair), reference evidence paths

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-004 | 4_artifact/5_table/forward_validation_results_v20260624.csv | Pass/fail per check (11 checks) | Read for acceptance decision |
| D-005 | 4_artifact/3_document/forward_validation_report_v20260624.md | Full validation narrative | Primary evidence for downstream |
| D-002 | 4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json | Re-run positive query output | Compare with T-059 reference |
| D-003 | 4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json | Re-run no-hit query output | Compare with T-059 reference |

## Supporting Artifacts
| ID | Path | Role |
|---|---|---|
| D-001 | 4_artifact/2_persist/forward_validation_smoke_v20260624.log | Low-level execution log for audit |
| D-006 | 4_artifact/3_document/execution_report_v20260624.html | Human-readable execution report |
| D-007 | 4_artifact/3_document/result_report_v20260624.html | Human-readable results dashboard |

## Downstream Use
- Acceptance decision for T-059 M1 forward query package
- Evidence that the M1 forward query satisfies the T-042 contract
- Traceability record linking T-059 package, repair fixture, and demo output

## Known Limits / Risks
- Numerical values (activation/suppression scores) may differ from reference due to floating-point/platform differences — only structural shape was compared
- Re-run output includes `_evidence` field from T-059 harness that reference lacks; stripped before comparison
- T-059 was tested, not T-048 (T-048 was replaced by T-059 per protocol clarification)

## Do Not Read / Do Not Reuse
- T-048 artifacts (superseded by T-059)
- 2_project_asset/ raw assets (forbidden)
- Reference JSON files in 1_asset/ (only for structural comparison, scores unreliable)

## Recommended Next Reads
1. `4_artifact/3_document/forward_validation_report_v20260624.md` — full narrative
2. `4_artifact/5_table/forward_validation_results_v20260624.csv` — pass/fail table

```

## Required Writes

Overwrite or create both files:

1. `4_artifact/3_document/execution_report_v20260626.html`
2. `4_artifact/3_document/result_report_v20260626.html`

Then update `5_report/delivery_qa.md` briefly with `Verdict: yellow_repair`, saying the repair was human-readable report rewriting only. Do not modify core deliverables, registry paths, code, data, or analysis results.

## Writing Standard

Write in Chinese. Use natural-language paragraphs, not an audit checklist. Tables are allowed only for a short artifact guide; they must not be the main report.

Each HTML report must have at least 900 Chinese characters of visible explanation. Each major section should contain a paragraph of 3-6 sentences. Every paragraph should include task-specific nouns, artifact names, findings, counts, decisions, or boundaries from this task.

Do not copy old HTML with only date/path changes. Do not write generic phrases like "completed successfully" unless you explain exactly what was completed.

## execution_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 任务意图
2. 输入资产与依据
3. 实际执行过程
4. 关键判断与证据
5. 交付物清单
6. 边界与未完成事项

The execution report should explain the work process: why the task was needed, what evidence was used, what the original execution did, what concrete findings or counts were produced, where the artifacts are, and what was intentionally not done.

## result_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 一句话结论
2. 项目背景
3. 核心结果
4. 项目价值
5. 交付物导读
6. 后续使用方式
7. 边界与风险

The result report should read like a concise project briefing. It should help a human quickly understand the value of this task without reading registry.yaml, completion.md, or source assets.

## Final Response

Return a short Chinese summary:

```md
### 交付报告重写完成
- 写入:
- 修复重点:
- 仍需注意:
```
