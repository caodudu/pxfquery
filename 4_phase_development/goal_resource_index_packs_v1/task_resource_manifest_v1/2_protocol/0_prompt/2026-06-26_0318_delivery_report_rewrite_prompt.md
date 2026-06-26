# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:18

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-025 resource_manifest_v1
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_resource_manifest_v1`
- Objective:

```text
Create pxfquery-{task_id} standard resource manifest from T021 standard_resources D-004. Deliver manifest, schema summary, and usage notes.
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
# task_resource_manifest_v1 — Protocol

## Objective

Build the `pxfquery-T025` standard resource manifest from the T-021 `standard_resources` bundle (D-004). This task is a configuration/derivation step: its deliverables are a manifest file, a schema summary, and usage notes — no new data is produced.

The manifest is the formal, machine-readable record of every file in the T-021 bundle and must be reusable by:

1. The CyHex task graph (as the registered output asset for T-025).
2. Downstream development and testing tasks that need to know exactly which files exist, where they live, what each file's role is, and what schema/integrity expectations apply.
3. Future release / packaging tasks that will vendor the bundle.

## Inputs

- A-001: T-021 standard_resources bundle (D-004) — the 19-file bundle under `task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`. The bundle is the source of truth for every entry in the manifest.
- A-002: T-021 standard resource guide (D-001) — cross-reference document explaining each file; reused (not copied) to derive usage notes.
- A-003/A-004: T-021 HTML reports — historical record, optional reference.
- A-005: T-021 process records — optional audit trail for precision / format decisions.
- A-006: T-021 artifact registry — confirms D-004 identity and core status.

## Steps

### Step 1: Enumerate bundle contents

List every file under `goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` (relative path from this task: `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources`). Record 19 files: 3 H5AD matrices, 10 JSON indexes, 5 CSV metadata tables, 1 YAML data description. For each entry record: filename, format, file size in bytes (rounded MB), and SHA-style identifier when present inside the bundle (e.g. data_description.yaml ids).

Output: inline table inside the manifest draft.

### Step 2: Derive schema summary

For each file classify schema into one of three categories:

1. **Tabular matrix (H5AD)** — `obs` columns (sig_id, project_code, cell_iname, pert_id, cmap_name, pert_dose, pert_time, plus dtype-specific extras), `var` names (91 function terms), `X` dtype (float32), `X` shape. The manifest captures obs columns verbatim and var count; it does not duplicate the 91 function names (those belong to `function_index.json`).
2. **JSON index** — store the top-level key shape (e.g. cellline_index.json → `{valid_cells: [...]}`; cellline_neighbors.json → `{bone: {bone cancer: {ewing's sarcoma: [...]}}}` lineage tree; drug_neighbors.json → `{BRD-suffix: [[neighbor, sim_int]]}`).
3. **CSV metadata** — column names and row counts (from T-021 verification: cellline ~240 rows, compound ~6,647 / ~39,321, gene ~12,328).

For `data_description.yaml`: capture only its `id / name / path / format / dimensions / key_fields` conventions; do not copy its full asset entries.

Output: schema inventory embedded in the manifest.

### Step 3: Build manifest YAML

Write `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml` with this minimal structure:

```yaml
manifest_version: 1
task_id: T-025
name: pxfquery-T025 standard resource manifest
generated: 2026-06-23
source_bundle:
  identity: T-021/D-004
  path: ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/
  file_count: 19
  total_size_estimate_mb: <measured at execution time>
files:
  - id: SRM-001
    filename: cp_func_ad.h5ad
    category: matrix
    format: h5ad
    role: compound (cp) perturbation functional score matrix
    obs_columns: [...]
    var_columns_count: 91
    notes: float32; dimensions 201014x91
  - ... (one entry per file)
```

Each entry carries: `id`, `filename`, `category` (matrix/index/metadata/description), `format`, `role`, `notes`. Matrix entries also carry `obs_columns` and `var_count`. Index entries carry `top_level_keys`. Metadata entries carry `row_count_estimate` and `key_columns`.

Place this in `4_artifact/2_persist/` so it lives next to the T-025 schema summary and usage notes.

Output: `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml`.

### Step 4: Write schema summary

Write `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md` as a human-readable Markdown reference. One section per file category:

1. **Functional matrices (H5AD)** — common obs schema, var=91 functions, float32, score semantics.
2. **Query indexes (JSON)** — purpose of each: cell/drug/gene lookup, neighbor graphs, function index, cell-line lineage tree. Brief shape description per file.
3. **Metadata tables (CSV)** — purpose of each, key columns, row counts.
4. **data_description.yaml** — convention-only; entries inside are descriptive sub-records of the bundle.

Output: `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md`.

### Step 5: Write 

...[truncated by CyHex prompt assembler: 5078 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-006
  name: pxfquery_T025_standard_resource_manifest
  path: 4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml
  type: persist
  origin_step: 03_build_manifest
  purpose: YAML manifest enumerating all 19 files in the T-021/D-004 standard_resources
    bundle with schema, category, role, key columns, size, and verification notes.
  usable_by: downstream development, testing, and packaging tasks; CyHex task graph
    asset registration
  created: '2026-06-23'
  identity: T-025/D-006
  role: deliverable
  core: true
  lineage_anchor: true
  stars: 5
  notes: Single-file YAML manifest. The primary output asset for T-025.
- id: D-007
  name: pxfquery_T025_schema_summary
  path: 4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md
  type: persist
  origin_step: 04_write_schema_summary
  purpose: Human-readable Markdown schema reference organized by file category (matrices,
    indexes, metadata, description).
  usable_by: developers and reviewers needing quick schema reference
  created: '2026-06-23'
  identity: T-025/D-007
  role: support
  core: false
  stars: 5
  notes: Companion document to the manifest YAML; self-contained and independently
    readable.
  lineage_anchor: false
- id: D-008
  name: pxfquery_T025_usage_notes
  path: 4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md
  type: persist
  origin_step: 05_write_usage_notes
  purpose: Usage instructions covering Python loading snippets, bundle reference rules,
    verification expectations, hard rules, and provenance.
  usable_by: downstream tasks as quick-start guide for consuming the bundle
  created: '2026-06-23'
  identity: T-025/D-008
  role: support
  core: false
  stars: 5
  notes: Includes Python code snippets for h5ad/json/csv loading.
  lineage_anchor: false
- id: D-009
  name: step6_validation
  path: 3_execution/step6_validation.json
  type: support
  origin_step: 06_validate_manifest
  purpose: Python validation evidence confirming manifest filename match, file count,
    bundle size, and data_description.yaml reference.
  usable_by: human review and future reproducibility checks
  created: '2026-06-23'
  identity: T-025/D-009
  role: support
  core: false
  stars: 5
  notes: 19/19 file match, 0.00% size deviation, all files exist on disk.
  lineage_anchor: false
- id: D-010
  name: execution_report_v20260623.html
  path: 4_artifact/3_document/execution_report_v20260623.html
  type: document
  origin_step: 07_completion
  purpose: Chinese HTML execution report covering all 7 steps, asset usage, validation,
    and known gaps.
  usable_by: human acceptance review
  created: '2026-06-23'
  identity: T-025/D-010
  role: report
  core: false
  stars: 5
  notes: CyHex-mandatory execution HTML report.
  lineage_anchor: false
- id: D-011
  name: result_report_v20260623.html
  path: 4_artifact/3_document/result_report_v20260623.html
  type: document
  origin_step: 07_completion
  purpose: Chinese HTML result report with resource overview, size distribution charts,
    schema consistency summary, and deliverable inventory.
  usable_by: non-developer readers, manuscript preparation
  created: '2026-06-23'
  identity: T-025/D-011
  role: report
  core: false
  stars: 5
  notes: CyHex-mandatory result HTML report with inline visualizations.
  lineage_anchor: false
- id: D-012
  name: handoff_check_before_exec
  path: 5_report/handoff_check_before_exec.md
  type: report
  origin_step: 00_cyhex_1_2_19_repair
  purpose: CyHex 1.2.19 check-to-execute handoff summary reconstructed from completed task evidence.
  usable_by: downstream tasks and future prompt flows that require check handoff context
  created: '2026-06-24'
  identity: T-025/D-012
  role: support
  core: false
  stars: 4
  notes: Added after completion to satisfy updated CyHex prompt expectations without changing the core manifest artifact.
  lineage_anchor: false
- id: D-013
  name: cyhex_1_2_19_supplement
  path: 5_report/cyhex_1_2_19_supplement.md
  type: report
  origin_step: 00_cyhex_1_2_19_repair
  purpose: Low-pollution supplemental file explaining what parts of T-025 are useful as future reference assets.
  usable_by: future planners, auditors, and tasks deciding whether to keep or reuse T-025
  created: '2026-06-24'
  identity: T-025/D-013
  role: support
  core: false
  stars: 4
  notes: Does not alter original execution outputs; it only labels reliable reuse boundaries.
  lineage_anchor: false
core_artifact_id: D-006

```

### Completion Report
```md
# T-025 resource_manifest_v1 — Completion Report

**Generated:** 2026-06-23
**Status:** Execution complete, deliverables ready for human acceptance

---

## 1. Task Summary

**Objective:** Build the `pxfquery-T025` standard resource manifest from the T-021 `standard_resources` bundle (D-004).

**Key results:**
- 19-file manifest YAML produced, mapping every file in the T-021 bundle
- Schema summary and usage notes delivered as self-contained Markdown documents
- Python validation: 19/19 filename match, 0.00% bundle size deviation, all files exist on disk
- No byte-level duplication — all references point to T-021/D-004

---

## 2. Steps Executed

| Step | Description | Status | Output |
|------|------------|--------|--------|
| 1 | Enumerate bundle contents | Done | Inline tables in manifest draft |
| 2 | Derive schema summary | Done | H5AD obs columns, JSON top-level keys, CSV columns/row counts extracted |
| 3 | Build manifest YAML | Done | `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml` |
| 4 | Write schema summary | Done | `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md` |
| 5 | Write usage notes | Done | `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md` |
| 6 | Python validate manifest | Done | `3_execution/step6_validation.json` — PASS (all 5 checks) |
| 7 | Register artifacts + completion | Done | `4_artifact/registry.yaml` + this file |

---

## 3. Deliverables

1. `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml` — 19-entry manifest YAML (T-025/D-006, core)
2. `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md` — schema summary (T-025/D-007)
3. `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md` — usage notes (T-025/D-008)
4. `3_execution/step6_validation.json` — validation evidence (T-025/D-009)
5. `4_artifact/3_document/execution_report_v20260623.html` — execution report (T-025/D-010)
6. `4_artifact/3_document/result_report_v20260623.html` — result report (T-025/D-011)
7. `4_artifact/registry.yaml` — artifact registration (D-006..D-011)
8. `5_report/completion.md` — this report

---

## 4. Verification Results

| Check | Result |
|-------|--------|
| File count matches bundle | PASS (19/19) |
| Exact filename match | PASS (no differences) |
| All manifest files exist on disk | PASS (all 19 exist) |
| data_description.yaml referenced | PASS |
| Bundle size within 5% | PASS (323.47 MB, 0.00% deviation) |

---

## 5. What Was Intentionally Not Produced

- No byte-level copies of bundle files (all references point to A-001)
- No new data files (manifest is inventory only)
- Two Chinese HTML reports (D-010/D-011) generated per CyHex protocol §3.3.4 alongside the three primary deliverables

---

## 6. Noted Repairs During Execution

- **Config-stage path bug:** The original config wrote `../../../task_standard_resources_optimal_formats/...` which resolved to a non-existent directory. Repaired during the check stage to `../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/...`. All 6 asset paths in `registration.yaml`, protocol.md, and asset_rule.yaml were corrected.
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
