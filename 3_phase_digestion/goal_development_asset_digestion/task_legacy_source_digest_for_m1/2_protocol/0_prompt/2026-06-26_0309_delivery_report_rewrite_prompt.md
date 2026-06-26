# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:09

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: digestion
- Task: T-041 legacy_source_digest_for_m1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1`
- Objective:

```text
Digest the explicitly registered migrated PxFquery package source for the M1 Python-package milestone. Use T-007 as the trusted source map and read only its registered migrated package-code asset path, not the whole project asset tree. Deliver a concise reusable source digest: candidate modules/functions, entry points, data/index access patterns, known unusable or risky legacy parts, and exact recommendations for what later development tasks may reference. This task must not write implementation code and must not modify legacy or completed task artifacts.
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
# Protocol: legacy_source_digest_for_m1

## Objective

Digest the explicitly allowed migrated PxFquery package source into a small reusable M1 reference asset. The task identifies which legacy modules, functions, entry points, data/index access patterns, and known risks should inform the M1 Python package DAG. It does not implement new package code, does not modify legacy files, and does not scan the whole project asset tree.

## Inputs

- A-001: T-007 development source map — use as the authority for the migrated package-source path and source priority.
- A-002: T-007 development state report — use as secondary context for package component status, data/index readiness, and validation state.
- A-003: Migrated PxFquery package source — the only legacy package-source directory this task may inspect.
- A-004: T-007 module asset status matrix — optional tabular cross-check for module and asset status.
- A-005: T-007 development gap and risk list — optional risk cross-check for unsafe legacy components and claims to avoid.

## Steps

1. Confirm the registered A-003 package-source directory exists and limit source inspection to that directory.
2. Inventory top-level package files and modules, including core API, loader, query, index, resolver/LLM, visualization, utilities, and obvious stubs.
3. Identify candidate code and concepts that downstream M1 tasks may safely reference: loader API ideas, forward query logic, reverse query logic, index access patterns, no-hit behavior, and package entry points.
4. Identify unsafe or non-reusable legacy pieces: hard-coded relative paths, pass stubs, NotImplementedError paths, fragile LLM calls, stale README/main entry points, and direct assumptions about old working directories.
5. Produce a concise M1 reuse recommendation table that maps each downstream task type to allowed legacy references and forbidden legacy references.
6. Write deliverables under `4_artifact/` and register them in `4_artifact/registry.yaml`.

## Constraints

- This digestion task is the only new M1 DAG task allowed to inspect the explicit legacy package-source path.
- Do not scan arbitrary project assets or the entire `2_project_asset/` tree.
- Do not modify files under the legacy source path, T-007, or any completed task.
- Do not write M1 implementation code for T046-T053.
- Do not use T024-T040 outputs as authorities.
- If a useful source path is outside A-003, mention it as a gap or future digestion need rather than opening it.

## Deliverables

- `4_artifact/2_persist/legacy_source_digest_m1.md`: concise source digest with package structure, reusable modules, risks, and M1 recommendations.
- `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv`: table of modules/files, status, reuse recommendation, downstream task relevance, and risk notes.
- `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml`: machine-readable allowed/forbidden legacy reference boundaries for downstream tasks.
- `4_artifact/registry.yaml`: registry entries for all reusable deliverables.
- `5_report/completion.md`: completion note including the exact source path inspected and confirmation that no broader project asset scan was performed.

## Acceptance

- The source digest names concrete files/modules and gives direct guidance for T046, T048, T049, and T052.
- The reuse matrix distinguishes usable, risky, incomplete, and forbidden legacy pieces.
- The boundary YAML clearly states that downstream development tasks must use T041 outputs rather than reading raw legacy source directly.
- The task does not create or modify implementation code outside its own `4_artifact/` and `5_report/`.
- The deliverables are registered in `4_artifact/registry.yaml`.

```

### Artifact Registry
```yaml
artifacts:
- id: A-041-001
  name: Legacy source digest for M1
  type: document
  path: 4_artifact/2_persist/legacy_source_digest_m1.md
  description: Concise human-readable source digest of the migrated PxFquery package,
    identifying reusable modules, risks, and M1 recommendations.
  task: T-041
  created: '2026-06-24'
  identity: T-041/A-041-001
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: A-041-002
  name: Legacy module reuse matrix for M1
  type: table
  path: 4_artifact/5_table/legacy_module_reuse_matrix_m1.csv
  description: Machine-checkable table of modules/files with status, reuse recommendation,
    downstream task relevance, and risk notes.
  task: T-041
  created: '2026-06-24'
  identity: T-041/A-041-002
  role: data
  core: false
  lineage_anchor: false
  stars: 2
- id: A-041-003
  name: Legacy reference boundaries for M1
  type: document
  path: 4_artifact/2_persist/legacy_reference_boundaries_m1.yaml
  description: Machine-readable allowed/forbidden legacy reference boundaries for
    downstream M1 tasks (T046, T048, T049, T052).
  task: T-041
  created: '2026-06-24'
  identity: T-041/A-041-003
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: A-041-004
  name: Execution report
  type: report
  path: 4_artifact/3_document/execution_report_v20260624.html
  description: Execution report for T-041 legacy source digest task.
  task: T-041
  created: '2026-06-24'
  identity: T-041/A-041-004
  role: report
  core: false
  lineage_anchor: false
  stars: 5
- id: A-041-005
  name: Result report
  type: report
  path: 4_artifact/3_document/result_report_v20260624.html
  description: Result report for T-041 legacy source digest task.
  task: T-041
  created: '2026-06-24'
  identity: T-041/A-041-005
  role: report
  core: false
  lineage_anchor: false
  stars: 5

```

### Completion Report
```md
# Completion

Task: T-041 legacy_source_digest_for_m1
Generated: 2026-06-24
Status: Completed

## Source Path Inspected

The following single package-source directory was inspected (A-003):
```
/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/
```

## Scope Confirmation

- No broader `2_project_asset/` scan was performed.
- No files outside A-003 were inspected beyond the five registered assets (A-001 through A-005).
- No implementation code was written for M1.
- No legacy files or completed task artifacts were modified.

## Steps Completed

1. Confirmed A-003 symlink resolves to the correct package-source directory.
2. Inventoried all top-level files and submodules:
   - core.py (modern entry point), main.py (legacy stub)
   - data/loader.py, query/forward.py, query/reverse.py, query/resolver.py
   - index/ (4 index wrappers), llm/ (client + prompts), viz/plots.py
   - utils.py, logging_utils.py, pyproject.toml
3. Identified reusable code: DataLoader, ForwardQuery, ReverseQuery, all 4 index classes, utils, logging.
4. Identified unsafe/non-reusable pieces: main.py (pass stubs), resolver.py (hard-coded paths, LLM coupling), prompt/check_link.py (legacy).
5. Identified missing runtime asset: function_index.json not found in migrated `data/query_indexes/`.
6. Produced all deliverables below with M1 task mapping.

## Deliverables Produced

| Deliverable | Path |
|---|---|
| Source digest | `4_artifact/2_persist/legacy_source_digest_m1.md` |
| Reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv` |
| Boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml` |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` |
| Result report | `4_artifact/3_document/result_report_v20260624.html` |
| Registry | `4_artifact/registry.yaml` |
| Completion note | `5_report/completion.md` |

## Acceptance Criteria Met

- [x] Source digest names concrete files/modules with guidance for T046, T048, T049, T052.
- [x] Reuse matrix distinguishes usable, risky, incomplete, and forbidden legacy pieces.
- [x] Boundary YAML states downstream tasks must use T-041 outputs, not raw legacy source.
- [x] No implementation code was created or modified outside `4_artifact/` and `5_report/`.
- [x] All deliverables are registered in `4_artifact/registry.yaml`.

## Key Findings for Downstream Tasks

- **T046**: Use `core.py` as API template; update `pyproject.toml` build system.
- **T048**: `data/loader.py` and `query/forward.py` are stable; avoid `download_zenodo`.
- **T049**: `query/reverse.py` is stable; reference resolver L1-L4 concept only; do NOT reuse resolver class directly.
- **T052**: All 4 index classes reusable as-is; **function_index.json must be rebuilt** (gap GAP-001).

```

### Existing AI Handoff, If Any
```md
(missing)
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
