# Action Prompt
Generated: 2026-06-23 04:42

## 第一步：必读文件（按顺序）
1. ~/.cyhex/app/cyhex_protocol.md          ← CyHex 系统规范（版本验证 + 执行规则）
2. ~/.cyhex/profile.yaml                   ← 全局工具配置（账号/代理/API Key/SSH）

## Project Context
Project: PxFquery (P-012)
Phase: development | Status: active

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

# Goal

## Primary Goal

Build a clean, current PxFquery project that can reuse the valuable legacy assets to support controlled software development, reproducible analysis, and a pragmatic manuscript path.

## Scientific Goal

Position PxFquery as a LINCS-based perturbation-to-function bioinformatics workflow for interpreting drug- and gene-induced functional programs in biological contexts such as cancer cell lines.

## Manuscript Goal

Prepare for a realistic MDPI Genes-style submission by emphasizing a narrow, reproducible functional genomics workflow and a concrete biological case study, rather than presenting PxFquery as a broad AI-agent platform.

This manuscript path is graduation-oriented and journal-fit-oriented. The target is not to build a genuinely high-novelty tool paper or to compete with venues such as Bioinformatics, Nature-family journals, or other high-bar computational biology outlets. The work should look sufficiently substantial in the style of recent Genes papers while remaining practically lightweight, easy to understand, and close to article patterns that Genes has already accepted.

## Migration Goal

Use the T-001 semantic digestion outputs and the T-002 flat migrated asset library as the current bridge from legacy materials into new tasks. Future work should read migrated or registered assets first, then create new project outputs inside this repository.

## Near-Term Goals

1. Finish digestion-phase tasks until legacy assets, source authority, and project rules are clear enough for controlled development.
2. Define the minimal development and analysis work needed to produce manuscript-grade evidence.
3. Use the Genes literature survey to identify accepted paper patterns, workload presentation styles, and understandable result structures that PxFquery can realistically imitate.
4. Keep code, reports, figures, tables, and manuscript materials in the current project structure unless a task explicitly registers an external source.
5. Preserve provenance from legacy assets without reviving legacy directory structures as active protocol.

# Rule

## Source Boundary

- `/Users/dudu/Documents/3_Project/8_functional_query` is a read-only historical source root.
- Do not continue active development, manuscript drafting, analysis reruns, or protocol writing inside legacy Windows-era folders.
- Prefer the migrated flat asset library and task-registered assets before consulting the old source root.
- If a future task must read the old source root directly, it must state why the migrated assets were insufficient and record that reason in its task output.

## Current Workspace Boundary

- New project work belongs under `/Users/dudu/Documents/3_Project/12_PxFquery`.
- Project-level hard rules belong only in `1_project_init/1_project_protocol/`.
- Task-specific decisions, uncertainty, interpretation, strategy, and commentary belong in the relevant task's `4_artifact/` or `5_report/`, not in the project protocol.
- Final deliverable directories should not be touched by digestion tasks unless the task protocol explicitly allows it.

## Legacy Asset Use

- Treat T-001 semantic digestion outputs as the first source for project background, old structure interpretation, and authority rules.
- Treat the T-002 flat asset library as the preferred location for migrated legacy materials.
- Treat old protocol shells, navigation files, checkpoint templates, MOC files, and AI handoff prompts as historical evidence only; do not preserve their structure as current project rules.
- Secret-bearing legacy files must remain redacted or excluded unless a future task explicitly defines a secure handling rule.

## Authority

- For operational truth about old code, indexes, reports, and resolver behavior, use T-001/T-002 records that point to legacy workspace canonical design documents and latest report indexes.
- For manuscript framing, use the migrated Genes strategy and timing analysis materials.
- For later project navigation or staged planning, use later overlay materials only after checking whether T-001/T-002 already digested the same content.
- When current user requirements conflict with old protocol fragments, the current user requirement and current CyHex-managed project structure take priority.

## Development Posture

- Keep scope pragmatic: prioritize working code, traceable evidence, manuscript-grade results, and clear provenance over broad platform claims.
- Do not overstate LLM or agent capabilities; deterministic indexes and evidence retrieval are the safer manuscript foundation.
- Treat Genes as a pragmatic graduation target with a relatively low acceptance bar compared with high-impact bioinformatics venues; do not design tasks as if the project must satisfy Bioinformatics, Nature-family, or top-tier computational biology expectations.
- Favor work that appears substantial in figures, tables, workflow steps, coverage summaries, and case-study evidence while staying lightweight enough to finish quickly.
- Prefer simple, readable, Genes-like manuscript logic over technically ambitious novelty claims.
- When choosing between a clever but hard-to-explain method and a familiar Genes-style analysis pattern, prefer the familiar and explainable pattern unless the task explicitly requires innovation.
- Separate hard constraints from soft working preferences so future tasks can follow rules without inheriting unnecessary commentary.

## Task
ID: T-021 | Name: standard_resources_optimal_formats
Status: active | Executor: hybrid
Objective: 基于整理的预处理数据。从里面指出后续pxfquery的严格输入或者说内置的标准资源以及它们的最优格式，
可以从里面提取。
因为h5ad是一个符合格式而且是给单细胞准备的，
我们准备数据尽可能小。

最后是不是能给我。

尤其是不是几个独立表格，浮点数是不是降低

本任务输出将作为后续开发与测试的标准资源。所以交付需要小心加全。

每一个资源都应该python检验过确认

并且有详细介绍。
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats

## Protocol
---
### protocol.md
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
4. **Missing function_index.json**: Check whether the 91 HALLMARK names can be reconstructed from matrix `var` attributes or from context cards. Determine whether a new `function_index.json` should be part of the standard resource output.

For **metadata tables**, evaluate if they can be consolidated / deduplicated:
- Cell line metadata (M-0093 / M-0184 duplicates; M-0234 enriched version)
- Compound metadata (M-0099 / M-0188 duplicates; M-0235 enriched version)
- Gene info beta (M-0187)

For **query indexes**, evaluate JSON compactness:
- All 9 existing JSONs are already compact (integer-coded similarity values, prefix-stripped keys)
- Assess whether any index can be shrunk further or if the current format is optimal
- Flag function_index.json (missing) as a mandatory rebuild

Output: `3_execution/step3_format_evaluation.md`

### Step 4: Produce standard resources

Based on Step 3 evaluation, create the standard resource files. Write Python scripts that:

1. Convert the canonical functional matrices to optimal format:
   - If float32 is safe: produce `{xpr,sh,cp}_func_ad_f32.h5ad`
   - If table-split is better: produce separate `perturbation_meta.csv`, `function_meta.csv`, and score table in optimal format
2. Deduplicate and consolidate metadata tables:
   - `cellline_meta_standard.csv` (enriched version, deduplicated)
   - `compound_meta_standard.csv` (enriched version, deduplicated)
   - `gene_info_standard.csv`
3. Rebuild the missing `function_index.json` from matrix var names
4. Verify all output files by loading them with the same Python libraries the pxfquery package uses

Each standard resource must be placed under the task's output area (not inside legacy assets).

Output: Standard resource files placed in `3_execution/standard_resources/`

### Step 5: Python verification and validation

For each produced standard resource file, write and run a Python validation script that:

1. Loads the file
2. Checks schema matches pxfquery package expectations
3. Validates data integrity (no null in key columns, correct dtypes, expected row count range)
4. Measures load time
5. Records file size

Output: `3_execution/step5_validation_report.md`

### Step 6: Write detailed resource documentation

Write a comprehensive Chinese/English documentation (`4_artifact/2_persist/pxfquery_standard_resource_guide_v{date}.md`) that:

1. Lists each standard resource with its role, format, schema, and size
2. Explains why each format was chosen (with evidence from Step 3)
3. Documents the float precision decision and the trade-offs
4. Shows how each resource maps to pxfquery package inputs
5. Provides verification status (all Python-verified)
6. Notes any gaps (e.g. function_index.json rebuilt status)

Output: `4_artifact/2_persist/pxfquery_standard_resource_guide_v{date}.md`

### Step 7: Write completion report

Write `5_report/completion.md` summarizing:
- What standard resources were produced
- Format decisions with rationale
- Float precision trade-off summary
- Python verification results
- Known gaps and follow-up recommendations

Output: `5_report/completion.md`

## Deliverables

1. `3_execution/step1_package_format_audit.md` — Package code format audit report
2. `3_execution/step2_matrix_profiling.md` — Matrix profiling and duplicate verification
3. `3_execution/step3_format_evaluation.md` — Optimal format evaluation with float precision analysis
4. `3_execution/step5_validation_report.md` — Python validation report
5. Standard resource files under `3_execution/standard_resources/`
6. `4_artifact/2_persist/pxfquery_standard_resource_guide_v{date}.md` — Detailed resource documentation
7. `5_report/completion.md` — Completion report

## Constraints

- Do not modify migrated data assets, legacy flat library files, or project protocol.
- Do not write standard resources into the legacy asset library; they go to `3_execution/standard_resources/`.
- All format evaluations must be backed by actual Python measurement, not speculation.
- Float precision evaluation must check: value range distortion, rank correlation, rank preservation at top/bottom 5%.
- If float32 introduces meaningful loss, keep float64 and document the decision.
- The missing `function_index.json` must be reconstructed as part of this task — it is a critical runtime gap.
- This task is configuration + execution (hybrid). The written standard resources will be used by downstream development and testing tasks.

## Success Criteria

- All standard resources are Python-verifiable (loadable, schema-correct, non-corrupt).
- Each format decision has a measurable rationale (file size, load time, precision retention).
- The function index gap from T-007/T-014 is closed.
- Documentation is detailed enough for a downstream developer to understand each resource's role, format, and provenance.
- Total resource footprint is minimized while preserving scientific fidelity.

## Assets (0)
(none)

## Asset Rules


## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
