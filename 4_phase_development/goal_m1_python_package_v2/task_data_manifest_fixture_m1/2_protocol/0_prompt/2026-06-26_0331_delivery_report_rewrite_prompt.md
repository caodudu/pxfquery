# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:31

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-043 data_manifest_fixture_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1`
- Objective:

```text
Prepare the stable M1 data substrate. Use T-014 for precomputed-data understanding and T-021 for standard resource formats. Deliver a resource manifest, a minimal fixture package, expected shapes/keys/columns, and small example records sufficient for loader, forward, and reverse demos. This task must confirm concrete paths and fixture contents; it must not invent data or depend on failed T024-T040 outputs.
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
# T-043 data_manifest_fixture_m1 — Protocol

## Objective

Prepare the stable M1 data substrate for downstream package development. The task must produce a reusable resource manifest, a minimal fixture package, expected shapes/keys/columns, and small example records sufficient for loader, forward-query, and reverse-query demos.

The execution must use T-014 and T-021 as the only predecessor authorities. It must confirm concrete paths and fixture contents from registered predecessor artifacts and must not invent data.

## Position In Project

This is a bottom-layer development task for `goal_m1_python_package_v2`. Its outputs define the reliable data boundary that later loader and query tasks can consume without rereading broad legacy/project raw assets.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` | Canonical standard resource bundle for concrete paths, schemas, shapes, keys, columns, and fixture records. |
| A-002 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` | Authoritative documentation for standard resource format decisions and expected usage. |
| A-003 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/process_records/` | Validation and profiling records for cross-checking the resource bundle. |
| A-004 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/2_persist/pxfquery_t014_precomputed_data_scope_v20260618.md` | Precomputed-data scope and boundaries for deciding the M1 substrate. |
| A-005 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_data_resource_inventory_v20260618.csv` | Resource inventory for aligning manifest entries with predecessor interpretation. |
| A-006 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv` | Matrix schema and coverage summary for expected shape and column/function checks. |

## Steps

1. Inspect only the registered input assets listed above, plus the current task's own writable folders.
2. Confirm the concrete standard resource paths and create `resource_manifest_m1.yaml` with stable resource IDs, relative bundle paths, file types, intended loader roles, required columns/keys, expected shapes, and provenance back to T-014/T-021.
3. Build a minimal fixture package from real records extracted from A-001. Include enough data for loader smoke tests, one forward-query demo path, and one reverse-query demo path. Keep fixture files small and deterministic.
4. Produce `expected_shapes_keys_columns_m1.csv` summarizing each selected resource's expected shape, key fields, columns, index semantics, and validation rule.
5. Produce `sample_records_m1.csv` or equivalent tabular summary showing the exact source resource, row/key identifiers, selected fields, and why each example is included.
6. Write a concise README explaining how downstream tasks should consume the manifest and fixture package, including any known exclusions from the full T-021 standard resource bundle.
7. Register all accepted outputs in `4_artifact/registry.yaml`, write completion reporting, and keep temporary scripts/logs in `3_execution/`.

## Constraints

- Use only T-014 and T-021 registered assets as authorities for input data and schema decisions.
- Do not invent rows, keys, columns, shapes, function names, drugs, genes, cell lines, or scores.
- Fixture records must be copied or derived from registered predecessor assets and must retain enough provenance to trace back to the source file and source identifier.
- Prefer small, deterministic fixtures over broad sampling.
- The fixture must be adequate for loader, forward-query, and reverse-query demonstrations, but it does not need to reproduce full query ranking performance.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not depend on T024-T040 outputs.
- Do not modify predecessor task directories or project protocol/state.

## Forbidden

- Reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Reading unrelated task directories or outputs outside registered T-014/T-021 assets.
- Using outputs from failed T024-T040 tasks.


...[truncated by CyHex prompt assembler: 2774 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: resource_manifest_m1
  type: manifest
  path: 4_artifact/2_persist/resource_manifest_m1.yaml
  status: ready
  provenance: T-043 generated from A-001 through A-006
  notes: Stable M1 resource manifest for full standard resources and fixture resources.
  identity: T-043/D-001
  role: support
  core: false
  lineage_anchor: false
  stars: 1
- id: D-002
  name: fixture_package_m1
  type: package
  path: 4_artifact/2_persist/fixture_package_m1/
  status: ready
  provenance: T-043 bounded extraction from A-001 standard resources
  notes: Small deterministic real-data fixture package for loader, forward, and reverse
    demos.
  identity: T-043/D-002
  role: delivery
  core: false
  lineage_anchor: false
  stars: 1
- id: D-003
  name: expected_shapes_keys_columns_m1
  type: table
  path: 4_artifact/5_table/expected_shapes_keys_columns_m1.csv
  status: ready
  provenance: T-043 generated from A-001 through A-006
  notes: Expected shape, keys, columns, index semantics, and validation rules.
  identity: T-043/D-003
  role: data
  core: false
  lineage_anchor: false
  stars: 2
- id: D-004
  name: sample_records_m1
  type: table
  path: 4_artifact/5_table/sample_records_m1.csv
  status: ready
  provenance: T-043 generated from real A-001 records
  notes: Traceable sample rows and keys used by the fixture package.
  identity: T-043/D-004
  role: data
  core: false
  lineage_anchor: false
  stars: 2
- id: D-005
  name: data_manifest_fixture_m1_readme
  type: document
  path: 4_artifact/2_persist/data_manifest_fixture_m1_readme.md
  status: ready
  provenance: T-043
  notes: Downstream usage and exclusions.
  identity: T-043/D-005
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-006
  name: execution_report_v20260624
  type: document
  path: 4_artifact/3_document/execution_report_v20260624.html
  status: ready
  provenance: T-043
  notes: Human-facing execution method and validation summary.
  identity: T-043/D-006
  role: report
  core: false
  lineage_anchor: false
  stars: 5
- id: D-007
  name: result_report_v20260624
  type: document
  path: 4_artifact/3_document/result_report_v20260624.html
  status: ready
  provenance: T-043
  notes: Human-facing result and downstream handoff summary.
  identity: T-043/D-007
  role: report
  core: false
  lineage_anchor: false
  stars: 5
- id: D-008
  name: validation_log_m1
  type: execution_record
  path: 3_execution/validation_log_m1.json
  status: ready
  provenance: T-043 validation run
  notes: Execution-side validation evidence; not a reusable project artifact.
  identity: T-043/D-008
  role: support
  core: false
  lineage_anchor: false
  stars: 1

```

### Completion Report
```md
# Completion

Task: T-043 data_manifest_fixture_m1
Completed: 2026-06-24
Status: completed

## Completed Steps

1. Confirmed CyHex availability and re-read the check handoff for execution strategy.
2. Inspected only registered assets A-001 through A-006 and current task writable folders.
3. Selected deterministic real records from A-001 for compound, shRNA, and XPR fixture paths.
4. Generated the M1 resource manifest, fixture package, expected shape/key/column table, sample-record table, README, HTML reports, artifact registry, and validation log.
5. Validated all declared output paths, reloaded fixture H5AD files, parsed produced tables, and checked manifest paths.

## Deliverables

- `4_artifact/2_persist/resource_manifest_m1.yaml`
- `4_artifact/2_persist/fixture_package_m1/`
- `4_artifact/5_table/expected_shapes_keys_columns_m1.csv`
- `4_artifact/5_table/sample_records_m1.csv`
- `4_artifact/2_persist/data_manifest_fixture_m1_readme.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`

## Validation Evidence

- Validation status: pass
- Manifest resources checked: 36
- Expected table rows: 36
- Sample record rows: 46
- Validation log: `3_execution/validation_log_m1.json`

## Boundary Notes

No project raw assets under `2_project_asset/`, no legacy source-root reads, no failed T024-T040 outputs, no web/downloaded data, and no synthetic biological records were used.

## Caveat

The fixture package is intentionally small. It supports loader and query smoke/demo wiring, but it is not a substitute for full-resource biological ranking validation.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-043 data_manifest_fixture_m1

## Task Goal
Produce the stable M1 data manifest and a small deterministic real-data fixture package for downstream loader, forward-query, reverse-query, validation, and package-assembly tasks.

## What Was Delivered
T-043 delivered a resource manifest, a fixture package, expected shape/key/column tables, sample records, validation evidence, registry metadata, and human-readable execution/result reports. The fixture package is intentionally small and is meant for deterministic smoke/demo wiring, not biological ranking-performance claims.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/resource_manifest_m1.yaml` | Entry point for full-resource and fixture-resource paths. | T046/T047 should read this first to discover M1 resource paths. |
| D-002 | `4_artifact/2_persist/fixture_package_m1/` | Compact real-data fixture bundle for fast deterministic tests. | T046/T048/T049/T050/T051 may use it for smoke/demo runs. |
| D-003 | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Documents expected shapes, keys, columns, and validation rules. | Loader and validation tasks should use it as acceptance evidence. |
| D-004 | `4_artifact/5_table/sample_records_m1.csv` | Traceable sample rows and keys used by the fixture package. | Query-core tasks should use it to select concrete demo inputs. |

## Supporting Artifacts
- `4_artifact/2_persist/data_manifest_fixture_m1_readme.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `3_execution/validation_log_m1.json`
- `4_artifact/registry.yaml`

## Downstream Use
T046 should implement the minimal fixture loader against D-001 and D-002. T047 may harden resource loading using D-001 and D-003. T048 and T049 should use D-004 only for bounded demo-case selection, and must still follow the API/demo contract from T042 once T042 is done.

## Known Limits / Risks
The fixture is deliberately small. It validates file format, path wiring, loader behavior, and smoke-test mechanics only. It must not be used to claim biological ranking quality or full-resource coverage.

## Do Not Read / Do Not Reuse
Do not use historical T024-T040 outputs as authority for this M1 route. Do not substitute this fixture for full-resource validation when the task explicitly requires full standard resources.

## Recommended Next Reads
1. `4_artifact/2_persist/resource_manifest_m1.yaml`
2. `4_artifact/5_table/expected_shapes_keys_columns_m1.csv`
3. `4_artifact/5_table/sample_records_m1.csv`
4. `5_report/completion.md`

```

## Required Writes

Overwrite or create both files:

1. `4_artifact/3_document/execution_report_v20260626.html`
2. `4_artifact/3_document/result_report_v20260626.html`

Then update `5_report/delivery_qa.md` briefly with `Verdict: yellow_repair`, saying the repair was human-readable report rewriting only. Do not modify core deliverables, registry paths, code, data, or analysis results.

## Writing Standard

Write in Chinese. Use natural-language paragraphs, not an audit checklist. Tables are allowed only for a short artifact guide; they must not be the main report. The report should read like a concise project briefing for a busy human decision-maker, not like a compliance form.

Each HTML report must have at least 900 Chinese characters of visible explanation. Each major section should contain a paragraph of 3-6 sentences. Every paragraph should include task-specific nouns, artifact names, findings, counts, decisions, or boundaries from this task.

Do not copy old HTML with only date/path changes. Do not write generic phrases like "completed successfully" unless you explain exactly what was completed.

Do not expose internal repair mechanics in the visible HTML body. Forbidden visible phrases include "报告重写", "重写版本", "为了通过 validator", "health warning", "低信息量报告修复", and similar wording. It is acceptable to record repair mechanics in `5_report/delivery_qa.md`, but the HTML reports must look like first-class task reports, not patched validator output.

The first screen of each report should immediately orient a reader who knows nothing: name the project problem, explain this task's role in the task chain, and state the concrete outcome. Include a specific project-value paragraph that explains how the task changes future work, risk, capability, or decision-making.

Mandatory final self-check before your final response: inspect the visible text of both HTML files you wrote. If either file contains "报告重写", "重写版本", "为了通过 validator", "validator", "health warning", or "低信息量报告修复", rewrite the visible title/body immediately and check again. Do not finish while any forbidden internal repair phrase remains visible in the HTML reports.

## execution_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 任务意图
2. 输入资产与依据
3. 实际执行过程
4. 关键判断与证据
5. 交付物清单
6. 边界与未完成事项

The execution report should explain the work process: why the task was needed, what evidence was used, what the original execution did, what concrete findings or counts were produced, where the artifacts are, and what was intentionally not done. It should help the project owner reconstruct the task without reading execution logs.

## result_report_v20260626.html Structure

Use these headings and write substantive paragraphs under each:

1. 一句话结论
2. 项目背景
3. 核心结果
4. 项目价值
5. 交付物导读
6. 后续使用方式
7. 边界与风险

The result report should read like a concise project briefing. It should help a human quickly understand the value of this task without reading registry.yaml, completion.md, or source assets. Avoid sounding like a template; if a paragraph could apply to any task, rewrite it with this task's concrete names, decisions, numbers, and consequences.

## Final Response

Return a short Chinese summary:

```md
### 交付报告重写完成
- 写入:
- 修复重点:
- 仍需注意:
```
