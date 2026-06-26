# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:09

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-061 legacy_source_digest_repair_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1`
- Objective:

```text
Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and read only the explicitly registered migrated PxFquery package-source path, not the whole project asset tree. Reference T-041 only as a failed historical attempt and do not reuse its outputs as authoritative. Deliver a fresh concise source digest, module reuse matrix, and legacy reference boundary YAML for downstream M1/M1.1 development tasks. This task must not write implementation code and must not modify legacy files or completed task artifacts.
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
# T-061 legacy_source_digest_repair_m1 — Protocol

## Objective

Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and inspect only the explicitly registered migrated PxFquery package-source directory. Treat T-041 as a failed historical attempt and do not reuse its outputs as authoritative evidence.

This is a digestion task. It must not write implementation code, run package workflows, modify legacy files, modify completed task artifacts, or promote outputs into project deliverables.

## Position In Project

T-061 replaces the failed/unsafe dependency role that T-041 was intended to serve. Its outputs should give later M1/M1.1 development tasks a concise, bounded, and auditable reference for which legacy package modules can be reused, adapted, or avoided.

T-007 remains the authority for the migrated package-source path and overall development-state source map. T-041 may be mentioned only to explain why a replacement digest was needed.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Trusted source map identifying the migrated PxFquery package-source path and relevant source-priority rules. |
| A-002 | project_asset via T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/` | The only raw legacy package-source directory allowed for bounded static inspection in this task. |

## Execution Steps

1. Confirm the registered A-001 source map and A-002 package-source directory are available; stop if A-002 resolves outside the registered migrated package path.
2. Inventory A-002 filenames and file sizes first. Do not recursively read caches, notebooks, binaries, generated reports, matrix/data files, or `__pycache__`.
3. For each Python source file under A-002, inspect imports, classes, functions, key constants, and entry-point behavior using bounded windows. Prefer no more than 200 source lines per file unless a specific symbol requires a targeted extra window.
4. Identify concrete reusable, adaptable/risky, incomplete, and forbidden pieces for M1/M1.1 development. Name modules, classes, and functions where possible.
5. Record data/index access patterns, hard-coded path assumptions, LLM/API coupling, missing runtime assets, and other downstream risks without executing package code.
6. Write a concise markdown source digest to `4_artifact/2_persist/legacy_source_digest_repair_m1.md`.
7. Write a CSV module reuse matrix to `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`.
8. Write a machine-readable downstream reference-boundary YAML to `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`.
9. Create execution/result reports, update `4_artifact/registry.yaml`, and write `5_report/completion.md`.

## Constraints

- Use T-007/D-001 as the source authority for the package-source path.
- Inspect only A-002 as raw legacy source.
- Use bounded static inspection; do not dump large files verbatim.
- Document the bounded-read method in the digest or execution report.
- Keep all generated analysis notes, scripts, and temporary logs in `3_execution/`.
- Put reusable accepted outputs only under `4_artifact/`.
- Preserve provenance for every conclusion that depends on A-001 or A-002.

## Forbidden

- Do not use T-041 outputs as authoritative inputs.
- Do not mark T-041 complete, repair T-041, or modify any T-041 file.
- Do not scan the whole `2_project_asset/` tree.
- Do not read the historical source root `/Users/dudu/Documents/3_Project/8_functional_query`.
- Do not read raw h5ad matrices, notebooks, binary data, caches, `__pycache__`, or generated reports inside package/source-adjacent paths.
- Do not run package workflows, rebuild indexes, perform biological analysis, perform web search, or write implementation code.
- Do not modify project protocol, predecessor task directories, completed artifacts, or legacy asset files.

## Web Search Allowance

Allowed: no

Reason: The task is a local digestion repair based on T-007 and a registered migrated package-source path. No current external or web evidence is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Replacement source digest | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | yes |
| Module reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | yes |
| Legacy reference boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | y

...[truncated by CyHex prompt assembler: 1670 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: legacy_source_digest_repair_m1
  type: document
  role: core_digest
  path: 2_persist/legacy_source_digest_repair_m1.md
  status: ready
  created: '2026-06-24'
  produced_by: T-061
  usable_by: downstream_m1_m1_1_development_tasks
  core: true
  stars: 5
  provenance:
  - A-001
  - A-002
  description: Concise bounded source digest naming inspected legacy package modules,
    functions, classes, reuse classes, source boundaries, and M1/M1.1 implications.
  notes: Fresh bounded replacement digest for M1/M1.1 legacy package-source reuse;
    T-041 not used as authority.
  identity: T-061/D-001
  lineage_anchor: true
- id: D-002
  name: legacy_module_reuse_matrix_repair_m1
  type: table
  role: core_module_matrix
  path: 5_table/legacy_module_reuse_matrix_repair_m1.csv
  status: ready
  created: '2026-06-24'
  produced_by: T-061
  usable_by: downstream_m1_m1_1_development_tasks
  core: true
  stars: 5
  provenance:
  - A-001
  - A-002
  description: CSV matrix classifying each relevant legacy package file/module by
    reuse status, downstream relevance, risks, and recommended action.
  notes: Module/file-level reuse classification matrix with risks and recommended
    downstream actions.
  identity: T-061/D-002
  lineage_anchor: true
- id: D-003
  name: legacy_reference_boundaries_repair_m1
  type: document
  role: core_boundary_rules
  path: 2_persist/legacy_reference_boundaries_repair_m1.yaml
  status: ready
  created: '2026-06-24'
  produced_by: T-061
  usable_by: downstream_m1_m1_1_development_tasks
  core: true
  stars: 5
  provenance:
  - A-001
  - A-002
  description: Machine-readable boundary rules for what downstream tasks may cite,
    adapt, or must avoid from the bounded T-061 legacy source inspection.
  notes: Machine-readable downstream citation, adaptation, and avoidance rules.
  identity: T-061/D-003
  lineage_anchor: true
- id: D-004
  name: execution_report_v20260624
  type: report
  role: execution_audit
  path: 3_document/execution_report_v20260624.html
  status: ready
  created: '2026-06-24'
  produced_by: T-061
  usable_by: audit_or_reproduction_review
  core: false
  stars: 3
  provenance:
  - A-001
  - A-002
  description: Human-readable execution report documenting the bounded static inspection
    method and delivered files.
  notes: Execution method and evidence report.
  identity: T-061/D-004
  lineage_anchor: false
- id: D-005
  name: result_report_v20260624
  type: report
  role: result_summary
  path: 3_document/result_report_v20260624.html
  status: ready
  created: '2026-06-24'
  produced_by: T-061
  usable_by: human_review_and_downstream_orientation
  core: false
  stars: 3
  provenance:
  - A-001
  - A-002
  description: Human-facing result summary of the delivered digest outputs and downstream
    use boundaries.
  notes: Human-facing result summary for delivered digest outputs.
  identity: T-061/D-005
  lineage_anchor: false

```

### Completion Report
```md
# Completion

Task: T-061 legacy_source_digest_repair_m1

Date: 2026-06-24

Status: completed

## Completed Steps

1. Verified A-001 and A-002 resolved to the registered T-007 source map and migrated package-source directory.
2. Confirmed CyHex local API availability once; app version 1.2.19.
3. Inventoried A-002 only using symlink-following bounded commands; recorded 25 files and 22 Python files.
4. Performed static-only source inspection through line counts, grep indexes, AST structure, and targeted source windows.
5. Classified legacy modules as reusable, adaptable/risky, incomplete, or forbidden for downstream M1/M1.1 use.
6. Wrote the required digest, reuse matrix, reference-boundary YAML, execution report, result report, and artifact registry.

## Deliverables Produced

- `4_artifact/2_persist/legacy_source_digest_repair_m1.md`
- `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`
- `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Evidence Files In 3_execution

- `3_execution/a002_file_inventory_20260624.txt`
- `3_execution/a002_python_symbol_index_20260624.txt`
- `3_execution/a002_definitions_20260624.txt`
- `3_execution/a002_ast_structure_20260624.txt`
- `3_execution/a002_risk_pattern_index_20260624.txt`

## Boundary Statement

No package workflows were run. No implementation code was written. No matrix files, notebooks, caches, generated reports, broad project asset paths, historical source root files, or T-041 outputs were read as authority. Web search was not used.

## Caveats

This was a source-digestion task only. It did not validate runtime behavior against real h5ad matrices or JSON query indexes. Downstream implementation tasks must register those assets and run deterministic tests before treating the legacy logic as operational.

```

### Existing AI Handoff, If Any
```md
# AI Handoff: T-061 legacy_source_digest_repair_m1

## Task Goal
Create a clean replacement legacy source digest for the M1 Python-package milestone using T-007 as the trusted source map and only the registered migrated PxFquery package-source path. T-041 is failed historical context only.

## What Was Delivered
T-061 delivered a bounded static source digest, a module reuse matrix, a downstream reference-boundary YAML, and two human-readable HTML reports. The work stayed inside task outputs and did not run package workflows, write implementation code, read raw matrices, read the historical source root, or use web search.

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Main concise digest of inspected legacy package modules, entry points, risks, and reuse classifications. | Read first for M1/M1.1 planning and cite as the bounded T-061 source interpretation. |
| D-002 | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | Module/file-level reuse matrix with recommended downstream actions. | Use to choose which legacy modules to reuse, adapt, isolate, or avoid. |
| D-003 | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Machine-readable rules for allowed citation/adaptation boundaries. | Use as the guardrail before any downstream task cites or adapts T-061 findings. |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html`: execution method and bounded-inspection audit.
- `4_artifact/3_document/result_report_v20260624.html`: human-facing result summary.
- `3_execution/a002_file_inventory_20260624.txt`: task-local inventory evidence.
- `3_execution/a002_python_symbol_index_20260624.txt`, `a002_definitions_20260624.txt`, `a002_ast_structure_20260624.txt`, `a002_risk_pattern_index_20260624.txt`: task-local static-inspection support files.

## Downstream Use
Use D-001 through D-003 as the authoritative T-061 package-source digestion package for future M1/M1.1 configuration, check, and execution tasks. Treat the outputs as planning and boundary evidence, not as runtime validation.

## Known Limits / Risks
This task did not execute the legacy package, rebuild indexes, inspect raw h5ad matrices, validate biological outputs, or prove that any legacy module runs in the current environment. Downstream implementation tasks must register runtime assets and run deterministic tests before treating legacy logic as operational.

## Do Not Read / Do Not Reuse
Do not use T-041 artifacts as authority. Do not use this task as permission to read the historical source root, broad `2_project_asset/` paths, raw matrices, notebooks, caches, or generated reports. Do not treat `3_execution/` support files as final reusable deliverables unless auditing T-061.

## Recommended Next Reads
1. `4_artifact/2_persist/legacy_source_digest_repair_m1.md`
2. `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`
3. `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`

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
