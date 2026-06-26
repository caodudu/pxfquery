# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:33

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-051 reverse_validation_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1`
- Objective:

```text
Independently validate the M1 reverse query implementation. Use T-049 as the implementation under test and rerun the reverse demo case from the contract. Deliver smoke logs, JSON output, pass/fail result, and traceability to the loader, fixture/manifest, ranking/scoring behavior, and package version used. This task must not hide instability by changing acceptance criteria.
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
| Execution report (HTML) | `4_artifact/3_document/validation_report_v{date}.html` | recomme

...[truncated by CyHex prompt assembler: 1411 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
  - id: D-001
    name: reverse_validation_report
    type: json_evidence
    path: 2_persist/reverse_validation_report_v20260624_055812.json
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Structured validation report with 42 pass/fail checks, explicit PASS verdict

  - id: D-002
    name: reverse_validation_comparison_csv
    type: table
    path: 5_table/reverse_validation_comparison_v20260624_055812.csv
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Comparison table of all 42 validation checks with pass/fail per row

  - id: D-003
    name: reverse_validation_html_report
    type: html_report
    path: 3_document/validation_report_v20260624_055812.html
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Rendered HTML summary of all validation checks, package provenance, verdict

  - id: D-004
    name: validation_smoke_log
    type: log
    path: ../3_execution/validation_smoke_log_v20260624_055812.json
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Smoke log with stdout/stderr/exit codes/elapsed times for each step

  - id: D-005
    name: step3_positive_demo_output
    type: log
    path: ../3_execution/step3_positive_demo_output.json
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Raw positive demo output including elapsed time and full result JSON

  - id: D-006
    name: step4_nohit_output
    type: log
    path: ../3_execution/step4_nohit_output.json
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Raw no-hit/error case output for all 5 error conditions

  - id: D-007
    name: validation_script
    type: code
    path: ../3_execution/run_validation.py
    generated: "2026-06-24"
    task_id: T-051
    checksum: null
    description: Automated validation script executing all 8 protocol steps

```

### Completion Report
```md
# Completion — T-051 reverse_validation_m1

## Verdict

**PASS — 42/42 checks passed.**

The M1 reverse query implementation (T-060/T-044) is validated as functionally correct against the T-042 contract. All positive demo, no-hit/error, ranking, and CLI checks produce expected outputs.

## Steps Executed

| Step | Description | Result |
|------|-------------|--------|
| 1 | Package provenance — inspected symlink, recorded resolved path, version | PASS |
| 2 | Fixture loading via M1FixtureLoader — confirmed xpr shape (15×9), target columns, A549 | PASS |
| 3 | Positive demo — reverse_query(activate=APOPTOSIS, suppress=MYC_TARGETS_V1, cell=A549, top_n=3) — output matches reference | PASS |
| 4 | No-hit/error cases — NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, empty-target no-hit | PASS |
| 5 | Ranking comparison — observed top-3 sig_ids/similarity/order match reference JSON and CSV | PASS |
| 6 | CLI smoke — `info` and `reverse` commands run, correct exit codes, correct JSON output | PASS |
| 7 | Validation report written — structured JSON with per-check pass/fail, explicit verdict | PASS |
| 8 | Artifact registry written | PASS |

## Traceability

| Attribute | Value |
|-----------|-------|
| Package version | 0.1.0 |
| Package code path | `1_asset/reverse_query_package_code` (symlink) |
| Resolved symlink target | `task_package_skeleton_m1/4_artifact/1_package/pxfquery` (T-044) |
| Loader | `pxfquery.data.m1_loader.M1FixtureLoader` |
| Manifest ID | `reverse_repair_manifest_m1_1` |
| Fixture | `reverse_repair_fixture_m1_1` (xpr: 15×9) |
| Ranking/scoring method | Cosine similarity (target vector +1 activate / -1 suppress) |
| Sort keys | similarity desc, cmap_name asc, cell_iname asc, sig_id asc |

## Deliverables

| Deliverable | Path | Required |
|---|---|---|
| Validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | yes |
| Comparison table (CSV) | `4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | recommended |
| Validation report (HTML) | `4_artifact/3_document/validation_report_v20260624_055812.html` | recommended |
| Smoke logs & evidence | `3_execution/` | yes |
| Artifact registry | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Caveats

- The package code is a symlink to T-044 (`task_package_skeleton_m1`), not a self-contained local copy. This is a known structural observation (recorded in T-060 delivery_qa) but does not affect functional correctness.
- The ranking comparison checked top-3 against reference (matching the `top_n=3` protocol parameter). The full reference has 10 candidates; the first 3 match exactly.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-051 reverse_validation_m1

## Task Goal
Independently validate the M1 reverse query implementation (T-060/T-049) by re-running the T-042 reverse demo against registered assets, producing structured pass/fail evidence with full traceability.

## What Was Delivered
- **Verdict: PASS** — 42/42 checks passed. M1 reverse query is functionally correct against the T-042 contract.
- All positive demo, no-hit/error, ranking, and CLI checks produce expected outputs.
- Package provenance recorded: symlink to T-044, version 0.1.0.
- Ranking/scoring: cosine similarity (target vector +1 activate / -1 suppress), sort keys match reference.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | Structured 42-check pass/fail report with explicit PASS verdict | Read as primary validation evidence; feed into downstream acceptance |
| D-002 | `4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | Per-check pass/fail table for human review or summary | Use for acceptance checklist or audit trail |
| D-003 | `4_artifact/3_document/validation_report_v20260624_055812.html` | Rendered HTML summary of all checks, provenance, verdict | Human-readable presentation of validation results |

## Supporting Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-004 | `3_execution/validation_smoke_log_v20260624_055812.json` | Complete smoke log with stdout/stderr/exit/elapsed per step | Reproduction or debugging |
| D-005 | `3_execution/step3_positive_demo_output.json` | Raw positive demo JSON output | Direct comparison or re-analysis |
| D-006 | `3_execution/step4_nohit_output.json` | Raw no-hit/error case outputs for 5 conditions | Error-handling test evidence |
| D-007 | `3_execution/run_validation.py` | Automated validation script for all 8 protocol steps | Direct reuse for re-validation or extension |

## Downstream Use
- This validation is the gate for M1 reverse query acceptance. A downstream task (e.g., T-052 or algorithm review) can use D-001 as primary evidence that the implementation meets the T-042 contract.
- If any downstream task needs to extend the validation (e.g., more programs, cell lines, full 10-candidate ranking), use D-007 as the template.

## Known Limits / Risks
- Package code is a symlink to T-044 (`task_package_skeleton_m1`), not self-contained. Does not affect functional correctness.
- Ranking comparison checked top-3 only (matches `top_n=3` protocol). Full reference has 10 candidates; first 3 match exactly.
- Fixture is synthetic (15×9), not biological data. Validation confirms code works correctly, not biological accuracy.

## Do Not Read / Do Not Reuse
- Do not read `1_asset/` directly; use registered artifact paths.
- Do not read predecessor task directories (T-042, T-043, T-044, T-046, T-049, T-060).

## Recommended Next Reads
1. `4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` — primary validation evidence
2. `5_report/completion.md` — task summary
3. `4_artifact/3_document/validation_report_v20260624_055812.html` — human-readable report

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
