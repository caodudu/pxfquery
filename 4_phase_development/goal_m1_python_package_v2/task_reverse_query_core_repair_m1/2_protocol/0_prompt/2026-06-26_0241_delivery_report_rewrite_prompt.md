# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:41

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-060 reverse_query_core_repair_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1`
- Objective:

```text
Create a same-layer replacement for T-049 reverse_query_core_m1. Use T-049 only as a reference incident: it showed that the T-042 reverse demo contract cannot be satisfied by the currently selected T-046 fixture assets because the required suppress term HALLMARK_MYC_TARGETS_V1 is absent and the selected assets did not include a usable fixture package/manifest. This task must (1) produce and register a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing reverse positive demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver the reverse query core that T-049 was supposed to deliver, including package code, deterministic ranking/scoring, no-hit/error behavior, runnable demo evidence, structured JSON output, and a clear provenance report. Downstream tasks should consume this task as the must replacement for T-049.
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
# T-060 reverse_query_core_repair_m1 — Protocol

## Objective
Create a same-layer replacement for T-049 reverse_query_core_m1. This task must repair the missing reverse-query demo substrate honestly and then deliver the M1 reverse query core that T-049 could not complete.

The execution must produce a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest supplement or contract-bridge fixture, that supports the T-042 reverse positive demo case including `HALLMARK_MYC_TARGETS_V1`. The substrate must be clearly labeled as synthetic/repair support, not as original raw LINCS data. Completed upstream task artifacts must not be modified.

## Position In Project
T-060 replaces T-049 for downstream reverse-query work. Downstream tasks should consume T-060 as the required reverse-query core deliverable and should treat T-049 only as a reference incident explaining why the previous route failed.

This is a development task, not a digestion task. It may create package code, execution evidence, and task-local repair assets, but it must not read project-level raw assets.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 API, CLI, JSON, error, and no-hit contract. |
| A-002 | T-042 | `4_artifact/2_persist/m1_demo_cases.yaml` | Authoritative forward/reverse demo cases and pass/fail assertions, including the reverse positive case. |
| A-003 | T-043 | `4_artifact/2_persist/resource_manifest_m1.yaml` | Base M1 manifest schema and fixture/full-resource path semantics. |
| A-004 | T-043 | `4_artifact/2_persist/fixture_package_m1/` | Original small M1 fixture package to inspect through registered task input only. |
| A-005 | T-043 | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Expected resource shapes, columns, key semantics, and validation rules. |
| A-006 | T-043 | `4_artifact/5_table/sample_records_m1.csv` | Traceable fixture sample rows and known fixture keys. |
| A-007 | T-044 | `4_artifact/1_package/pyproject.toml` | Canonical package metadata and editable package shape. |
| A-008 | T-044 | `4_artifact/1_package/pxfquery/` | Base package skeleton to extend with reverse-query code. |
| A-009 | T-046 | `4_artifact/1_package/pxfquery/data/m1_loader.py` | Accepted M1 fixture loader implementation that reverse code should use or remain compatible with. |
| A-010 | T-046 | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-011 | T-046 | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Loader smoke evidence and observed fixture coverage. |
| A-012 | T-045 | `4_artifact/2_persist/index_health_summary.json` | Optional context for known index shape/coverage gaps and deterministic field handling. |
| A-013 | T-047 | `4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened resource loading and index normalization. |
| A-014 | T-047 | `4_artifact/3_document/loader_gap_list_m1.md` | Optional known-gap reference to avoid rediscovering accepted loader limitations. |
| A-015 | T-049 | `5_report/completion.md` | Incident reference documenting the prior reverse-core block and missing fixture/manifest coverage. |

## Execution Steps
1. Read the T-042 contract and demo cases first. Extract the required reverse API fields, JSON shape, ranking expectations, no-hit/error behavior, and the exact positive demo requirements.
2. Read the T-043/T-046 fixture and loader assets through the registered inputs. Confirm the missing `HALLMARK_MYC_TARGETS_V1` or fixture-package/manifest gap without reading project-level raw assets.
3. Create a task-local reverse repair substrate under `4_artifact/2_persist/`, such as `reverse_repair_fixture_m1_1/` plus `reverse_repair_manifest_m1_1.yaml` or an equivalent contract-bridge supplement. It must include enough records/metadata to run the T-042 reverse positive demo honestly and deterministically.
4. Document substrate provenance in a task-local report: what is copied from registered predecessor fixtures, what is synthetic/repair content, why it exists, and why it must not be represented as original raw data.
5. Build the reverse query core from the T-044 package skeleton and T-046 loader API. Use deterministic scoring/ranking with stable tie-breaking and finite-score filtering. Do not depend on T-049 partial code unless execution records a deliberate reason and compatibility check.
6. Implement required no-hit/error behavior from T-042, including missing program, missing context, empty/low-confidence result, and invalid/no-matrix cases as applicable.
7. Run the reverse positive demo against the task-local repair substrate. Save visible structured JSON evidence and record the command used to reproduce it.
8. Run no-hit/error smoke cases and import/compile checks in the project `pxfquery` conda environment.
9. Produce concise execu

...[truncated by CyHex prompt assembler: 3729 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
  - id: T-060/D-001
    name: reverse_query_package_code
    type: package_code
    path: 4_artifact/1_package/pxfquery
    status: ready
    provenance: "Task-local package derived from T-044 skeleton with T-046 m1_loader.py and T-060 reverse implementation."
    notes: "Exposes PxFquery.func2pert, deterministic cosine ranking, CLI reverse, and structured error/no-hit behavior."
  - id: T-060/D-002
    name: reverse_repair_fixture_m1_1
    type: repair_fixture_package
    path: 4_artifact/2_persist/reverse_repair_fixture_m1_1
    status: ready
    provenance: "A-004 registered fixture sidecars plus T-060 synthetic repair rows/columns; not raw LINCS/CMAP data."
    notes: "xpr repair matrix has 15 observations x 9 variables and supports A549 + HALLMARK_MYC_TARGETS_V1."
  - id: T-060/D-003
    name: reverse_repair_manifest_m1_1
    type: repair_manifest
    path: 4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml
    status: ready
    provenance: "Task-local manifest for the T-060 repair fixture."
    notes: "Loadable with M1FixtureLoader using explicit fixture_root."
  - id: T-060/D-004
    name: reverse_repair_provenance
    type: provenance_report
    path: 4_artifact/2_persist/reverse_repair_provenance_v20260624.md
    status: ready
    provenance: "Written during T-060 execution."
    notes: "Separates copied predecessor fixture support from synthetic repair content."
  - id: T-060/D-005
    name: reverse_demo_evidence
    type: json_evidence
    path: 4_artifact/2_persist/reverse_demo_evidence_v20260624.json
    status: ready
    provenance: "Generated by 3_execution/run_reverse_evidence.py in pxfquery conda environment."
    notes: "Positive T-042 reverse demo; found=true; includes HALLMARK_MYC_TARGETS_V1 and repeatability check."
  - id: T-060/D-006
    name: reverse_error_no_hit_evidence
    type: json_evidence
    path: 4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json
    status: ready
    provenance: "Generated by 3_execution/run_reverse_evidence.py in pxfquery conda environment."
    notes: "Structured NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, and empty-target no-hit cases."
  - id: T-060/D-007
    name: reverse_ranking_evidence
    type: table
    path: 4_artifact/5_table/reverse_ranking_evidence_v20260624.csv
    status: ready
    provenance: "Generated from the positive reverse demo ranking."
    notes: "Documents deterministic ranked candidates and similarity values."
  - id: T-060/D-008
    name: execution_report
    type: html_report
    path: 4_artifact/3_document/execution_report_v20260624.html
    status: ready
    provenance: "Written during T-060 execution."
    notes: "Records steps, commands, validation, and boundary compliance."
  - id: T-060/D-009
    name: result_report
    type: html_report
    path: 4_artifact/3_document/result_report_v20260624.html
    status: ready
    provenance: "Written during T-060 execution."
    notes: "Summarizes outputs, evidence files, scoring, and caveat."

```

### Completion Report
```md
# Completion

Status: completed

Generated: 2026-06-24

## Completed Steps

1. Extracted the T-042 reverse API/demo contract and no-hit/error expectations from registered A-001/A-002.
2. Confirmed the selected original fixture gap: the registered T-043/T-046 fixture coverage lacks `HALLMARK_MYC_TARGETS_V1`, and the original xpr fixture has no A549 rows.
3. Created the task-local repair substrate under `4_artifact/2_persist/reverse_repair_fixture_m1_1/` and `reverse_repair_manifest_m1_1.yaml`.
4. Documented repair provenance in `4_artifact/2_persist/reverse_repair_provenance_v20260624.md`.
5. Built the T-060 reverse query package code under `4_artifact/1_package/pxfquery/`.
6. Ran positive reverse demo, repeatability check, structured no-hit/error cases, compile/import validation, loader compatibility check, and CLI smoke check in the `pxfquery` conda environment.
7. Registered reusable outputs in `4_artifact/registry.yaml`.
8. Wrote HTML execution and result reports.

## Validation Commands

```text
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/generate_reverse_repair_fixture.py
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery env PYTHONPATH=/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/1_package python 3_execution/run_reverse_evidence.py
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery env PYTHONPATH=/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/1_package python -m pxfquery.cli reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --matrix 4_artifact/2_persist/reverse_repair_fixture_m1_1/xpr_func_fixture_m1.h5ad --matrix-type xpr --top-n 3
```

## Evidence

- Positive demo JSON: `4_artifact/2_persist/reverse_demo_evidence_v20260624.json`
- No-hit/error JSON: `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json`
- Ranking CSV: `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv`
- CLI smoke stdout: `3_execution/reverse_cli_smoke_stdout_v20260624.json`

## Caveats

The repair substrate is synthetic contract-bridge support, not original raw LINCS/CMAP data. It is appropriate for T-042/T-060 M1 reverse-core validation and downstream package development, but not for biological interpretation or manuscript evidence.

No upstream predecessor artifacts were modified. No project-level raw assets, legacy roots, web sources, or T024-T040 blocked assets were used.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-060 reverse_query_core_repair_m1

## Task Goal
T-060 should replace failed T-049 by delivering a task-local synthetic/repair reverse substrate and a task-local reverse query core package that satisfies the T-042 reverse demo contract, including `HALLMARK_MYC_TARGETS_V1`, deterministic ranking, structured JSON evidence, and no-hit/error behavior.

## What Was Delivered
The task directory contains the repair fixture, manifest, provenance report, positive demo evidence JSON, no-hit/error evidence JSON, ranking CSV, and human-readable HTML reports under `4_artifact/`.

Delivery QA did not accept the task because the registered package-code artifact is not task-local package code. `4_artifact/1_package/pxfquery` is a symlink to the predecessor T-044 package skeleton outside this task, and no T-060 reverse query package source files were present inside the T-060 artifact package directory.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| T-060/D-002 | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Repair fixture substrate for the reverse demo case. | Can be reused after execute revision verifies package code against it. |
| T-060/D-003 | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Manifest for loading the repair fixture. | Use with the accepted loader path during revised execution. |
| T-060/D-004 | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | States synthetic/repair provenance and non-biological-evidence caveat. | Read before reusing or extending the fixture. |
| T-060/D-005 | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Positive reverse demo evidence claimed by execution. | Re-check after task-local package code is actually delivered. |
| T-060/D-006 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Structured no-hit/error evidence claimed by execution. | Re-check after task-local package code is actually delivered. |
| T-060/D-007 | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` | Ranking evidence for candidate order and similarity. | Re-check deterministic ranking after execute revision. |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html`: human-readable execution summary.
- `4_artifact/3_document/result_report_v20260624.html`: human-readable result summary and caveat.
- `3_execution/`: scripts, smoke output, fixture summary, and checklist for revision audit.

## Downstream Use
Do not treat T-060 as accepted downstream input until execute revision delivers task-local package code under `4_artifact/1_package/pxfquery/` and reruns the validation evidence from that task-local package.

## Known Limits / Risks
- Current package-code registry entry points to an upstream predecessor symlink, not a self-contained T-060 package artifact.
- Existing JSON and CSV evidence may still be useful for audit, but it must be regenerated or explicitly revalidated after the package-code placement is fixed.
- The repair substrate is synthetic contract-bridge support, not raw LINCS/CMAP data or biological evidence.

## Do Not Read / Do Not Reuse
- Do not reuse `4_artifact/1_package/pxfquery` as accepted T-060 package code in its current state.
- Do not read project raw assets or T024-T040 blocked assets for this revision.
- Do not modify predecessor task artifacts to fix T-060.

## Recommended Next Reads
1. `5_report/delivery_qa.md`
2. `4_artifact/registry.yaml`
3. `5_report/completion

...[truncated by CyHex prompt assembler: 111 chars omitted]
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
