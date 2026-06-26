# Human Delivery Report Rewrite Prompt
Generated: 2026-06-26 03:18

## Role

You are a human-facing project report writer for one CyHex task.

You are not writing for CyHex internals, a validator, or a future AI agent. You are writing for a human project owner or boss who jumps between many tasks and opens this one task at random. Assume that reader did not watch the execution, does not know the surrounding context, and will not open protocol files, registry files, completion notes, CLI logs, source assets, or predecessor tasks. By reading only the two HTML reports you write, that person should understand why this task existed, what it actually did, what it produced, why it matters to the project, what to open next, and what the limits are.

## Task

- Project: PxFquery (P-012)
- Phase: development
- Task: T-021 standard_resources_optimal_formats
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats`
- Objective:

```text
基于整理的预处理数据。从里面指出后续pxfquery的严格输入或者说内置的标准资源以及它们的最优格式，
可以从里面提取。
因为h5ad是一个符合格式而且是给单细胞准备的，
我们准备数据尽可能小。

最后是不是能给我。

尤其是不是几个独立表格，浮点数是不是降低

本任务输出将作为后续开发与测试的标准资源。所以交付需要小心加全。

每一个资源都应该python检验过确认

并且有详细介绍。
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
# T-021: standard_resources_optimal_formats — Protocol

## Objective

Based on the organized precomputed data (from T-014), identify and define PxFquery's standard built-in resources and their optimal formats. This includes:

1. Identify which data assets are PxFquery's "standard built-in resources" — the strict inputs needed by the pxfquery package.
2. Determine the optimal storage format for each resource (h5ad is the natural format for single-cell data, but we want data as small as possible).
3. Assess whether separate independent tables are better than a single monolithic matrix. Evaluate float precision reduction (float64 → float32 or lower).
4. Produce Python-verified, production-grade standard resource files that will serve as the foundation for downstream development and testing.
5. Each resource must be Python-verified and documented in detail.

## Inputs / Asset Sources

All assets registered in `1_asset/registration.yaml`:
- **A-001**: T-014 data resource inventory (`5_table/pxfquery_t014_data_resource_inventory_v20260618.csv`)
- **A-002**: T-014 matrix schema coverage (`5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv`)
- **A-003**: T-014 precomputed data understanding report (`3_document/pxfquery_t014_precomputed_data_understanding_report_v20260618.html`)
- **A-004**: Precomputed functional matrices — legacy flat library `data/functional_matrices/` (6 H5AD files)
- **A-005**: Metadata tables — legacy flat library `data/metadata_tables/`
- **A-006**: Query indexes — legacy flat library `data/query_indexes/`
- **A-007**: T-014 follow-up G007 task proposals (`2_persist/pxfquery_t014_followup_g007_task_proposals_v20260618.md`)
- **A-008**: pxfquery package code — legacy flat library `code/pxfquery_package/`

Direct legacy flat library paths:
- `data/functional_matrices/` (canonical H5AD set: M-0105–M-0107)
- `data/metadata_tables/` (9 files)
- `data/query_indexes/` (9 JSONs — note: `function_index.json` is missing)

## Steps

### Step 1: Read T-014 predecessor artifacts and pxfquery package code

Read the T-014 deliverables to understand the precomputed data landscape:
- Resource inventory (66 files documented with roles/readiness)
- Matrix schema/coverage (11 H5ADs inspected)
- Precomputed data understanding report
- Follow-up G007 proposals

Read the pxfquery package code (`code/pxfquery_package/`) to identify what the package actually expects:

| Asset | Package expects | Format | Schema invariant |
|---|---|---|---|
| Functional matrices | `{xpr,sh,cp}_func_ad.h5ad` | h5ad (via `anndata.read_h5ad`) | obs: sig_id, project_code, cell_iname, pert_id, cmap_name, pert_dose, pert_time; var: 91 function terms |
| Cell line index | `cellline_index.json` | JSON | `{"valid_cells": [...]}` |
| Cell line neighbors | `cellline_neighbors.json` | JSON | `{lineage:{disease:{subtype:[cells]}}}` |
| Drug index | `drug_index.json` | JSON | `{"alias_lower": "BRD-..."}` |
| Drug neighbors | `drug_neighbors.json` | JSON | `{id_no_prefix: [[id_no_prefix, t_int], ...]}` |
| Gene index (simple) | `gene_index_simple.json` | JSON | `{"SYMBOL_UPPER": "type_code"}` |
| Gene neighbors (simple) | `gene_neighbors_simple.json` | JSON | `{symbol: [[neighbor, cosine_int], ...]}` |
| Function index | `function_index.json` | JSON | `{var_names, meta, aliases}` — **MISSING** |
| Cell line tree | `cellline_tree.json` | JSON | `{tree, cell_index, meta}` |
| Full gene index | `gene_index.json` | JSON | `{lowercase: {symbol, gene_type, in_matrix}}` |
| Full gene neighbors | `gene_neighbors.json` | JSON | same shape as simple |

Output: `3_execution/step1_package_format_audit.md`

### Step 2: Verify canonical dataset and identify duplicates

Inspect the functional matrices directory. Two vintage pairs exist (M-0105–M-0107 and M-0199–M-0201). Verify they are identical and select the canonical set. For each selected canonical file:

- Load H5AD, extract `obs` schema, `var` names (91 HALLMARK terms), `X` shape, dtype
- Record: file size, matrix dimensions, memory footprint, float precision
- Sample a few rows to understand score distribution (range, mean, sparsity if any)

Output: `3_execution/step2_matrix_profiling.md`

### Step 3: Assess optimal format and precision reduction

For each functional matrix, evaluate:

1. **Float precision**: Can float64 → float32 be applied without meaningful loss? Measure min/max, distribution shift, rank correlation between float64 and float32 versions.
2. **Storage format**: Compare h5ad (AnnData on-disk), parquet (columnar per var), and feather (fast row-oriented). Measure file size, load time, and query-read performance.
3. **Separation into tables**: Can the functional matrix be split into standalone tables? Assess: perturbation metadata table (obs data), function metadata table (var names + descriptions), and sparse score table (perturbation × function). Measure size trade-offs.
4. **Missing function_index.json**: Check whether the 91 HALLMARK names can be reconstructed from matrix `var` at

...[truncated by CyHex prompt assembler: 4784 chars omitted]
```

### Artifact Registry
```yaml
artifacts:
- id: D-001
  name: pxfquery_standard_resource_guide_v20260623.md
  path: 4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md
  type: persist
  origin_step: 06_write_resource_documentation
  purpose: Comprehensive guide documenting all 19 standard resources with format decisions,
    schemas, precision analysis, and usage instructions.
  usable_by: future development and testing tasks
  created: '2026-06-23'
  identity: T-021/D-001
  role: support
  core: false
  lineage_anchor: false
  stars: 5
  notes: Documentation deliverable for T-021; the standard resource bundle is the
    core artifact.
- id: D-002
  name: execution_report_v20260623.html
  path: 4_artifact/3_document/execution_report_v20260623.html
  type: document
  origin_step: 07_write_completion_report
  purpose: Execution summary showing all 7 steps completed, assets used, files written,
    and zero failures.
  usable_by: human acceptance review
  created: '2026-06-23'
  identity: T-021/D-002
  role: report
  core: false
  stars: 5
  notes: CyHex-mandatory execution HTML report.
  lineage_anchor: false
- id: D-003
  name: result_report_v20260623.html
  path: 4_artifact/3_document/result_report_v20260623.html
  type: document
  origin_step: 07_write_completion_report
  purpose: Visual result report with resource overview, size comparison charts, precision
    validation, and package compatibility checklist.
  usable_by: non-developer readers, manuscript preparation
  created: '2026-06-23'
  identity: T-021/D-003
  role: report
  core: false
  stars: 5
  notes: CyHex-mandatory result HTML report with visualizations.
  lineage_anchor: false
- id: D-004
  name: standard_resources
  path: 4_artifact/2_persist/standard_resources/
  type: persist
  origin_step: 04_produce_standard_resources
  purpose: 'Canonical PxFquery standard resource bundle: float32 H5AD matrices, query
    indexes, metadata tables, and data_description.'
  usable_by: downstream PxFquery development, testing, packaging, and data-loading
    tasks
  created: '2026-06-23'
  identity: T-021/D-004
  role: deliverable
  core: true
  lineage_anchor: true
  stars: 5
  notes: Post-execution relocation from 4_artifact/2_persist/standard_resources/ into 4_artifact
    so the bundle is visible and registered as a deliverable.
- id: D-005
  name: process_records
  path: 4_artifact/2_persist/process_records/
  type: persist
  origin_step: 01-05_execution_evidence
  purpose: Audit, profiling, format-evaluation, production, and validation records
    supporting the standard resource bundle.
  usable_by: human review, downstream verification, and future debugging
  created: '2026-06-23'
  identity: T-021/D-005
  role: support
  core: false
  lineage_anchor: false
  stars: 5
  notes: Post-execution relocation from execution step result files into 4_artifact.
- id: D-006
  name: handoff_check_before_exec
  path: 5_report/handoff_check_before_exec.md
  type: report
  origin_step: 00_cyhex_1_2_19_repair
  purpose: Check-to-execute handoff reconstructed for newer CyHex prompt logic.
  usable_by: downstream tasks and future prompt flows
  created: '2026-06-24'
  identity: T-021/D-006
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-007
  name: cyhex_1_2_19_supplement
  path: 5_report/cyhex_1_2_19_supplement.md
  type: report
  origin_step: 00_cyhex_1_2_19_repair
  purpose: Low-pollution supplement explaining T-021 reliability and reuse boundaries.
  usable_by: future planners, auditors, and downstream tasks
  created: '2026-06-24'
  identity: T-021/D-007
  role: support
  core: false
  lineage_anchor: false
  stars: 4
core_artifact_id: D-004

```

### Completion Report
```md
# T-021 standard_resources_optimal_formats — Completion Report

**Generated:** 2026-06-23 05:10
**Status:** Execution complete, deliverables ready for human acceptance

---

## 1. Task Summary

**Objective:** Identify and produce PxFquery's standard built-in resources in optimal formats, with Python-verified accuracy and comprehensive documentation.

**Key results:**
- 19 standard resource files produced (323.46 MB total)
- Original legacy footprint: 1,472.98 MB (h5ad float64 only)
- Data savings: **1,149.52 MB (78.1%)** including all metadata and indexes
- H5AD functional matrices: **82% size reduction** via float64 → float32
- All **18 verified files pass** Python validation
- **function_index.json** (missing since T-007/T-014) rebuilt

---

## 2. Steps Executed

| Step | Description | Status | Output |
|---|---|---|---|
| 1 | Package code format audit | Done | `4_artifact/2_persist/process_records/step1_package_format_audit.json` |
| 2 | Matrix profiling & duplicate verification | Done | `4_artifact/2_persist/process_records/step2_matrix_profiling.json` — duplicates confirmed identical |
| 3 | Optimal format evaluation | Done | `4_artifact/2_persist/process_records/step3_format_evaluation.json` — float32 is lossless |
| 4 | Produce standard resources | Done | 19 files under `4_artifact/2_persist/standard_resources/` |
| 5 | Python verification & validation | Done | `4_artifact/2_persist/process_records/step5_verification_results.json` — 18/18 PASS |
| 6 | Write resource guide | Done | `4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` |
| 7 | Write completion/history reports | Done | This file + HTML reports |

---

## 3. Standard Resources Produced

All files under `4_artifact/2_persist/standard_resources/`:

### Functional Matrices (float32 h5ad, 264.85 MB total)
| File | Description | Size |
|---|---|---|
| `cp_func_ad.h5ad` | Compound perturbation scores (201,014 × 91) | 105.11 MB |
| `sh_func_ad.h5ad` | shRNA perturbation scores (189,365 × 91) | 95.52 MB |
| `xpr_func_ad.h5ad` | ORF perturbation scores (132,464 × 91) | 64.22 MB |

### Query Indexes (10 JSON files, 56.49 MB total)
| File | Size | Note |
|---|---|---|
| `cellline_index.json` | 3.5 KB | |
| `cellline_neighbors.json` | 6.5 KB | |
| `cellline_tree.json` | 49 KB | |
| `drug_index.json` | 172 KB | |
| `drug_neighbors.json` | 4.38 MB | |
| `gene_index_simple.json` | 348 KB | |
| `gene_neighbors_simple.json` | 19.50 MB | |
| `gene_index.json` | 6.12 MB | |
| `gene_neighbors.json` | 21.76 MB | |
| **`function_index.json`** | **17 KB** | **Rebuilt (was missing)** |

### Metadata Tables (5 CSV files, 6.25 MB total)
| File | Rows | Size |
|---|---|---|
| `cellline_meta_standard.csv` | 240 | 15 KB |
| `cellline_info_standard.csv` | 240 | 35 KB |
| `compound_meta_standard.csv` | 6,647 | 948 KB |
| `compound_info_standard.csv` | 39,321 | 4.19 MB |
| `gene_info_standard.csv` | 12,328 | 1.09 MB |

### Other (1 file)
| File | Size |
|---|---|
| `data_description.yaml` | 5 KB |

---

## 4. Key Decisions

### Format Decisions

| Decision | Evidence |
|---|---|
| **h5ad float32** (not float64) | Rank correlation = 1.00000 across all 91 functions; 82% file size reduction |
| **h5ad** (not parquet/feather/table-split) | pxfquery package exclusively uses `anndata.read_h5ad` |
| **JSON** for indexes | Already compact, directly compatible with pxfquery |
| **CSV** for metadata | Small (<5 MB), human-readable, pandas-compatible |
| **M-0105~M-0107** (canonical set) | M-0199~M-0201 confirmed byte-identical duplicates by MD5 |
| **Enriched metadata** selected | M-0234, M-0235 chosen over duplicate simple versions |

### Float Precision

| Property | Value |
|---|---|
| Per-function rank correlation | 1.000000 (all 273 tested columns) |
| Top 5% rank overlap | 100% (all columns) |
| Bottom 5% rank overlap | 100% (all columns) |
| Max absolute error | ~0.00025 (at score scale [-10, +10]) |

**Conclusion:** float32 is lossless for query purposes.

---

## 5. Gap Closure

| Gap | Source | Status |
|---|---|---|
| `function_index.json` missing | T-007, T-014 | **Closed** — rebuilt from matrix var_names with all 91 terms (50 Hallmark + 41 3CA MPS) |
| 5 CMAP upstream H5ADs truncated | T-014 | **Unresolvable** — files are corrupt in migrated assets; not needed for pxfquery runtime |

---

## 6. Verification Results

| Category | Tested | Pass | Fail |
|---|---|---|---|
| H5AD matrices | 3 | 3 | 0 |
| JSON indexes | 10 | 10 | 0 |
| CSV metadata | 5 | 5 | 0 |
| **Total** | **18** | **18** | **0** |

---

## 7. Deliverables

1. `4_artifact/2_persist/process_records/step1_package_format_audit.json` — Package format audit
2. `4_artifact/2_persist/process_records/step2_matrix_profiling.json` — Matrix profiling
3. `4_artifact/2_persist/process_records/step3_format_evaluation.json` — Format evaluation
4. `4_artifact/2_persist/process_records/step5_verification_results.json` — Python verification
5. `4_artifact/2_persist/standard_resources/` — 19 standard resource files (323.46 MB)
6. `4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` — Resource guide
7. `4_artifact/3_document/execution_report_v20260623.html` — Execution report
8. `4_artifact/3_document/result_report_v20260623.html` — Result report
9. `5_report/completion.md` — This report

---

## 8. Asset Registration

Updated `1_asset/registration.yaml` with 8 assets (A-001 to A-008):
- A-001~A-003: T-014 predecessor artifacts (inventory, schema, report)
- A-004: Precomputed functional matrices (legacy source)
- A-005: Metadata tables (legacy source)
- A-006: Query indexes (legacy source)
- A-007: T-014 follow-up proposals
- A-008: PxFquery package code (format reference)
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
