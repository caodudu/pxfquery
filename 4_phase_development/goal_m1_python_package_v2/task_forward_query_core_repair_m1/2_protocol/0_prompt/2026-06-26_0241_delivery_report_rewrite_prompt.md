# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 02:41

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner who jumps between many tasks and opens this one task at random. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-059 forward_query_core_repair_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1`
- Objective:

```text
Create a same-layer replacement for T-048 forward_query_core_m1. Use T-048 only as a reference incident: it showed that the T-042 forward demo contract cannot be satisfied by the currently selected T-046 fixture assets. This task must (1) produce and register a task-local forward repair substrate asset, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing EGFR/A549/xpr positive demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver the forward query core that T-048 was supposed to deliver, including package code, no-hit behavior, runnable demo evidence, structured JSON output, and a clear provenance report. Downstream tasks should consume this task as the must replacement for T-048.
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
# T-059 forward_query_core_repair_m1 — Protocol

## Objective

Create a same-layer repair/replacement for T-048 `forward_query_core_m1`. T-048 is only a reference incident showing that the T-042 required forward demo case `EGFR/A549/xpr` cannot be satisfied by the currently selected T-046 fixture assets.

This task must deliver a working M1 forward query core plus a task-local repair substrate, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly supplies the missing positive demo case without modifying completed T-042, T-043, T-044, T-046, or T-047 outputs. The repair substrate must be labeled as synthetic/repair provenance, not as original raw data.

## Position In Project

T-059 replaces T-048 for downstream forward-query work. It does not reopen T-048, mark T-048 as successful, or alter upstream completed artifacts. Downstream tasks should consume T-059 outputs as the authoritative M1 forward-query core repair deliverable.

Because seven predecessor tasks are selected, execution should use the registered handoff-derived assets only. If the executor finds that more predecessor context is needed beyond the registered assets, stop and recommend an intermediate digestion/integration task instead of expanding into broad predecessor reading.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Contract authority for public API, CLI shape, JSON output, no-hit behavior, and error semantics. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Defines the exact required forward demo case and assertions, including `EGFR/A549/xpr`. |
| A-003 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml` | Baseline M1 resource/fixture manifest to preserve compatibility and describe existing substrate boundaries. |
| A-004 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/` | Existing deterministic fixture package that must remain unchanged and should be extended only through a task-local repair substrate. |
| A-005 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Fixture schema and expected structure reference for any repair supplement. |
| A-006 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv` | Traceable sample-record context and fixture content reference; useful for documenting the missing positive case. |
| A-007 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml` | Base package metadata and src-layout anchor. |
| A-008 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/` | Base package skeleton to extend with forward-query code. |
| A-009 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Prior import-smoke baseline to replicate after implementation. |
| A-010 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Loader implementation that forward query must use or remain compatible with. |
| A-011 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-012 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Evidence that baseline fixture loading worked before the repair. |
| A-013 | T-047 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened loading behavior; not required to replace the T-046 API. |
| A-014 | T-047 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_p

...[truncated by CyHex prompt assembler: 6527 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: forward_query_package_m1_repair
  type: package
  path: 4_artifact/1_package
  status: ready
  provenance: T-044 skeleton plus T-046 loader-compatible forward implementation
  role: core_package
  identity: T-059 replacement forward-query package
  produced_by: T-059
  description: Implemented M1 forward query package with API/CLI behavior, no-hit handling, and T-046 loader-compatible access.
  usable_by: downstream M1 package and forward-query tasks replacing T-048
  core: true
  lineage_anchor: T-044 package skeleton; T-046 loader API; T-059 repair substrate
  stars: 5
- id: D-002
  name: forward_repair_manifest_m1_1
  type: manifest
  path: 4_artifact/2_persist/forward_repair_manifest_m1_1.yaml
  status: ready
  provenance: T-059 synthetic_repair contract bridge
  role: repair_manifest
  identity: synthetic repair manifest for EGFR/A549/xpr contract bridge
  produced_by: T-059
  description: Documents the task-local M1.1 repair substrate and its synthetic_repair provenance.
  usable_by: downstream tasks that need to understand or load the T-059 repair fixture
  core: true
  lineage_anchor: T-042 demo contract; T-043 fixture boundary; T-059 synthetic_repair
  stars: 5
- id: D-003
  name: forward_repair_fixture_m1_1
  type: package
  path: 4_artifact/2_persist/forward_repair_fixture_m1_1
  status: ready
  provenance: T-043 fixture copied task-locally with one synthetic_repair EGFR/A549/xpr
    row
  role: repair_fixture
  identity: task-local M1.1 fixture supplement
  produced_by: T-059
  description: Loader-compatible fixture copy with the minimal synthetic_repair EGFR/A549/xpr positive row required by the T-042 demo contract.
  usable_by: downstream runnable demos and tests for the T-059 forward-query core
  core: true
  lineage_anchor: T-043 fixture; T-046 loader compatibility; T-059 synthetic_repair
  stars: 5
- id: D-004
  name: forward_query_positive_demo_evidence
  type: json
  path: 4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json
  status: ready
  provenance: T-059 validation
  role: positive_demo_evidence
  identity: EGFR/A549/xpr forward demo JSON
  produced_by: T-059
  description: Structured JSON evidence showing the required positive forward demo returns found=true.
  usable_by: acceptance checks and downstream smoke tests
  core: true
  lineage_anchor: T-042 forward demo contract; T-059 validation
  stars: 5
- id: D-005
  name: forward_query_no_hit_evidence
  type: json
  path: 4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json
  status: ready
  provenance: T-059 validation
  role: no_hit_evidence
  identity: structured no-hit forward query JSON
  produced_by: T-059
  description: Structured JSON evidence for no-hit behavior without traceback.
  usable_by: acceptance checks and downstream error-behavior tests
  core: true
  lineage_anchor: T-042 no-hit contract; T-059 validation
  stars: 5
- id: D-006
  name: forward_query_contract_assertions
  type: table
  path: 4_artifact/5_table/forward_query_contract_assertions_v20260624.csv
  status: ready
  provenance: T-059 validation
  role: assertion_table
  identity: T-042 contract assertion results for T-059
  produced_by: T-059
  description: Pass/fail assertion table covering import, loader compatibility, positive hit, no-hit, JSON shape, CLI, provenance, and boundary checks.
  usable_by: reviewers and downstream validation tasks
  core: true
  lineage_anchor: T-042 contract; T-046 loader API; T-059 validation
  stars: 5
- id: D-007
  name: forward_query_core_repair_report
  type: document
  path: 4_artifact/3_document/forward_query_core_repair_report_v20260624.md
  status: ready
  provenance: T-059 report
  role: provenance_report
  identity: repair and replacement report
  produced_by: T-059
  description: Explains how T-059 replaces T-048, what was synthetic repair, what remained upstream, and the limits of the bridge fixture.
  usable_by: future planning, handoff, and provenance review
  core: true
  lineage_anchor: T-048 incident; T-059 delivery
  stars: 5
- id: D-008
  name: execution_report
  type: report
  path: 4_artifact/3_document/execution_report_v20260624.html
  status: ready
  provenance: T-059 report
  role: human_execution_report
  identity: human-readable execution record
  produced_by: T-059
  description: HTML execution summary listing implementation steps and validation checks.
  usable_by: human review and audit
  core: false
  lineage_anchor: T-059 validation
  stars: 3
- id: D-009
  name: result_report
  type: report
  path: 4_artifact/3_document/result_report_v20260624.html
  status: ready
  provenance: T-059 report
  role: human_result_report
  identity: human-readable result summary
  produced_by: T-059
  description: HTML result summary for the T-059 replacement deliverable and its contract-bridge limitation.
  usable_by: human review and acceptance
  core: false
  lineage_anchor: T-059 result summary
  stars: 3

```

### Completion Report
```md
# Completion

Status: completed

Completed: 2026-06-24

T-059 delivered the same-layer repair/replacement for T-048. The package, repair substrate, positive/no-hit JSON evidence, assertion table, reports, and artifact registry were produced under the T-059 task directory.

## Validation

- Package import: PASS
- T-046 loader-compatible repair fixture load: PASS
- Positive forward demo `EGFR/A549/xpr`: PASS (`found=true`)
- No-hit forward demo: PASS (structured `PerturbationNotFound` JSON)
- CLI JSON output: PASS
- Synthetic/repair provenance labeling: PASS

Failed checks: 0

## Deliverables

- `4_artifact/1_package/`
- `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml`
- `4_artifact/2_persist/forward_repair_fixture_m1_1/`
- `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json`
- `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json`
- `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv`
- `4_artifact/3_document/forward_query_core_repair_report_v20260624.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`

## Boundary Statement

No predecessor task outputs were modified. No project-level raw assets under `2_project_asset/` and no T024-T040 blocked assets were used. The added EGFR/A549/xpr row is a task-local `synthetic_repair` contract bridge and is not original raw data or biological evidence.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-059 forward_query_core_repair_m1

## Task Goal

T-059 is the same-layer replacement for the blocked T-048 forward-query task. It delivers an M1 forward-query package plus a task-local synthetic repair substrate that satisfies the T-042 required `EGFR/A549/xpr` positive demo without modifying upstream completed task outputs.

## What Was Delivered

- Implemented package source and metadata under `4_artifact/1_package/`.
- Task-local repair manifest and fixture under `4_artifact/2_persist/`.
- Positive-hit and no-hit structured JSON evidence under `4_artifact/2_persist/`.
- Contract assertion table under `4_artifact/5_table/`.
- Provenance and human-readable reports under `4_artifact/3_document/`.
- Registered reusable outputs in `4_artifact/registry.yaml`.

## Core Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/1_package/` | Authoritative T-059 forward-query package replacing T-048 for downstream M1 work. | Use as the package source for future M1 forward-query integration or tests. |
| D-002 | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Declares the synthetic repair provenance and fixture bridge. | Read before using the repair fixture; preserve the synthetic_repair label. |
| D-003 | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Loader-compatible task-local fixture containing the minimal EGFR/A549/xpr bridge row. | Use as the fixture root for T-059 demos and smoke tests. |
| D-004 | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Shows the required positive demo returns `found=true`. | Use as acceptance evidence for the T-042 positive forward demo. |
| D-005 | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Shows structured no-hit behavior without traceback. | Use as acceptance evidence for no-hit/error behavior. |
| D-006 | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Consolidates validation assertions and pass/fail outcomes. | Read first when checking whether T-059 met the contract. |
| D-007 | `4_artifact/3_document/forward_query_core_repair_report_v20260624.md` | Explains the T-048 replacement role, provenance, and limits. | Use for downstream planning and provenance review. |

## Supporting Artifacts

- D-008 `4_artifact/3_document/execution_report_v20260624.html`: human-readable execution and validation summary.
- D-009 `4_artifact/3_document/result_report_v20260624.html`: human-readable result summary.
- `5_report/completion.md`: completion summary and boundary statement.
- `5_report/delivery_qa.md`: delivery-side QA result.

## Downstream Use

Use T-059, not T-048, as the accepted forward-query core repair source for M1 downstream tasks. Treat the repair fixture as a minimal contract bridge for runnable demos and tests, not as original LINCS/raw biological evidence.

## Known Limits / Risks

- The added `EGFR/A549/xpr` content is `synthetic_repair` and exists only to bridge the T-042 demo contract.
- The repair fixture does not establish biological ranking validity or full-resource coverage.
- No upstream completed outputs were modified; do not infer that T-043/T-046 now natively contain the positive demo case.

## Do Not Read / Do Not Reuse

- Do not reuse T-048 `4_artifact/` as accepted output.
- Do not use T024-T040 blocked assets for this line of work.
- Do not treat project raw assets under `2_project_asset/` as inputs unless a future task explicitly authorizes 

...[truncated by CyHex prompt assembler: 407 chars omitted]
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
