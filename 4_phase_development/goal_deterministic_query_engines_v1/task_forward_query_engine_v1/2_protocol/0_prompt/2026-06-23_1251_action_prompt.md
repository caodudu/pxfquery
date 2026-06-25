# Action Prompt
Generated: 2026-06-23 12:51

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
ID: T-029 | Name: forward_query_engine_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} forward query engine deliverable. Reproduce EGFR/A549/xpr style deterministic query with serializable result tables and reports.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_forward_query_engine_v1

## Protocol
---
### protocol.md
# Protocol: forward_query_engine_v1

## Objective
Create a `pxfquery-T-029` deterministic forward query engine that loads T-021 standard resources (xpr functional matrix) via the T-026 loader, uses the T-024 pxfquery package `ForwardQuery` class to run EGFR/A549/xpr-style forward queries, and writes serializable result tables and reports.

## Inputs
- **A-001**: T-024 pxfquery workspace package — `4_artifact/2_persist/workspace/src/pxfquery/` containing `ForwardQuery`, `ForwardResult`, `DataLoader`, and the full package tree. The engine uses this as the query class source.
- **A-002**: T-026 matrix loader package — `4_artifact/2_persist/loader/__init__.py` provides `load_matrix()`, `load_bundle()`, `load_index()`, `load_metadata()`. The engine delegates resource loading to this package.
- **A-003**: T-021 standard_resources bundle (D-004) — `xpr_func_ad.h5ad` float32 functional matrix (132464 obs x 91 vars) with `cmap_name`, `pert_id`, `cell_iname` obs columns, plus JSON indexes (gene_index.json, drug_index.json, cellline_index.json, function_index.json) and CSV metadata tables. The primary data source for forward queries.
- **A-004**: T-013 MVP capability contract (D-001) — Capability/gap evidence listing known fuzzy-match issues and index-naming breaks. Used to set realistic query behavior expectations and decide when to repair vs. document.
- **A-005**: T-013 failure/missing capability list (D-005) — Documents that `function_index.json` is present in xpr bundle, that fuzzy match has false-positive risk, and that resolver/NL layer is not in scope. Tunes repair decisions.

## Steps
1. Read T-024 workspace package to understand `ForwardQuery`, `ForwardResult`, and `DataLoader` API. Confirm `import pxfquery` works or identify import-blocking issues from T-013 evidence.
2. Read T-026 loader package to understand `load_matrix()`, `load_bundle()`, and the loader validation evidence (`loader_validation.json`) to know the exact xpr matrix shape, obs columns, and dtype before writing any engine code.
3. Implement the forward query engine script at `3_execution/forward_engine.py` that:
   - Imports from T-026 loader to open `xpr_func_ad.h5ad` from the A-003 bundle.
   - Passes the loaded AnnData to `ForwardQuery`.
   - Runs `query("EGFR", cell_line="A549", top_n=20)` to reproduce the canonical forward demo.
   - Runs one additional query with a different gene (e.g. `TP53`) and cell line (e.g. `MCF7`) as diversity evidence.
   - Runs a not-found query with a nonexistent perturbation to verify `ForwardResult.found=False` behavior.
   - Runs each query and immediately writes serialized result tables.
4. Write serialized output under `4_artifact/5_table/`:
   - `pxfquery_T029_EGFR_A549_xpr_forward_result.csv` — top activated and suppressed terms with scores.
   - `pxfquery_T029_TP53_MCF7_xpr_forward_result.csv` — diversity case.
   - `pxfquery_T029_notfound_query_result.json` — not-found behavior evidence.
5. If the forward query fails because of a scoped package bug (e.g. import error, dtype incompatibility, column name mismatch between legacy ForwardQuery expectations and A-003 xpr H5AD structure), repair it inside this task scope by producing a corrected local version at `4_artifact/2_persist/pxfquery_T029_<name>_repaired.py`. Record what was fixed, source asset id, changed files, validation evidence, and downstream consumption guidance in `5_report/repair_log.md`.
6. Produce CyHex-mandatory reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese HTML step-by-step execution report.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese HTML result report showing query results, tables, and schema documentation.
7. Write `4_artifact/registry.yaml` registering all T-029 deliverables.
8. Write `5_report/completion.md` summarizing what was produced and what remains for downstream tasks.

### Required Bug-Repair Handling
- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, e.g. `pxfquery-T-029`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning
- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read upstream versions and emit `pxfquery-T-029` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Engine Discipline
- The engine must load data from A-003 bundle by reference using the T-026 loader; it must not copy upstream `.h5ad` or `.json` bytes.
- The engine must use T-024 workspace's `ForwardQuery` class directly (import from workspace `src/pxfquery/query/forward.py`), not a custom reimplementation.
- The engine script must be runnable from the `pxfquery` conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/forward_engine.py`.
- The engine must NOT depend on resolver/NL/LLM layers. This is a **deterministic** forward query engine v1. T-013 evidence confirms resolver is blocked by index-naming issues; those are out of scope for this task.
- If the `function_index.json` or any index file is needed, it is in A-003 (T-021 bundle has `function_index.json` with keys `var_names`, `meta`, `aliases` — confirmed by T-026 loader validation).
- Forward query uses T-026's `load_matrix()` and T-024's `ForwardQuery` class; it does not need any index for the basic xpr matrix path.

### T-013 Knowledge Integration
- T-013 CAP-05 (fuzzy match false-positive): The engine should accept fuzzy match as-is for this v1 unless it prevents a runnable result. If a false positive prevents the EGFR/A549 demo, repair the fuzzy match threshold inside this task scope and document.
- T-013 CAP-03 (index naming): Not relevant — forward query does not use resolver/indexes.
- T-013 CAP-07 (resolver/NL blocked): Confirmed out of scope for deterministic engine v1.

## Deliverables
- `3_execution/forward_engine.py` — Runnable forward query engine script.
- `4_artifact/5_table/pxfquery_T029_EGFR_A549_xpr_forward_result.csv` — EGFR/A549 canonical forward result table.
- `4_artifact/5_table/pxfquery_T029_TP53_MCF7_xpr_forward_result.csv` — Diversity case result table.
- `4_artifact/5_table/pxfquery_T029_notfound_query_result.json` — Not-found behavior evidence.
- `4_artifact/2_persist/pxfquery_T029_<name>_repaired.py` — Present only if repair was required.
- `4_artifact/registry.yaml` — T-029 deliverable registry.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — CyHex-mandatory execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — CyHex-mandatory result report.
- `5_report/completion.md` — Completion report.
- `5_report/repair_log.md` — Present only if bug was repaired.

## Acceptance
- `forward_engine.py` imports T-026 loader and T-024 ForwardQuery successfully.
- EGFR/A549/xpr query actually runs and produces `ForwardResult.found=True`.
- Result tables exist, are non-empty, and contain scores for top 20 activated + top 20 suppressed functional terms.
- At least one additional diversity query (different gene/cell-line) runs successfully.
- Not-found query produces `ForwardResult.found=False` without crashing.
- All Python execution uses the pxfquery conda environment.
- T-023 is not required; T-013 capability evidence is the gap reference for this v1 task.

## Assets (9)
- [deliverable] T-024 pxfquery workspace package — goal_package_foundation_v1/task_workspace_package_v1
- [deliverable] T-026 matrix loader package — goal_resource_index_packs_v1/task_matrix_loader_v1
- [deliverable] T-021 standard_resources bundle (D-004) — goal_precomputed_data_exploration/task_standard_resources_optimal_formats
- [deliverable] T-013 MVP capability contract (D-001) — goal_algorithm_function_review/task_mvp_algorithm_run-through_review
- [deliverable] T-013 failure/missing capability list (D-005) — goal_algorithm_function_review/task_mvp_algorithm_run-through_review
- [deliverable] Current project protocol — project_init
- [support] T-026 loader validation record (D-003) — goal_resource_index_packs_v1/task_matrix_loader_v1
- [support] T-026 loader validation summary (D-004) — goal_resource_index_packs_v1/task_matrix_loader_v1
- [deliverable] T-013 capability status matrix (D-003) — goal_algorithm_function_review/task_mvp_algorithm_run-through_review

## Asset Rules

### Required
- ../../goal_package_foundation_v1/task_workspace_package_v1/4_artifact/2_persist/workspace/ — T-024 pxfquery workspace package with ForwardQuery, ForwardResult, DataLoader, and full package tree. Read-only source for the forward query class; the engine imports ForwardQuery directly from this workspace.
- ../../goal_resource_index_packs_v1/task_matrix_loader_v1/4_artifact/2_persist/loader/ — T-026 matrix loader package providing load_matrix(), load_bundle(), load_index(), load_metadata(). The engine delegates resource loading to this package. Read-only.
- ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/ — T-021 standard_resources bundle (D-004) containing xpr_func_ad.h5ad float32 functional matrix (132464 obs x 91 vars) with cmap_name/pert_id/cell_iname obs columns, plus JSON indexes and CSV metadata tables. The primary data source for forward queries. Read-only by reference; no byte-level copy.
- ../../goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md — T-013 MVP capability contract defining required MVP behavior, gated/optional behavior, and out-of-scope claims. Used to set realistic acceptance boundaries for the forward engine.
- ../../goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md — T-013 failure and missing capability list documenting known fuzzy-match false-positive risk and resolver-blocking issues. Used to decide when to repair vs. document divergence.
- ../../../1_project_init/1_project_protocol/ — Current project protocol defining environment, boundaries, and the pxfquery conda runtime. Required for any Python execution.
### Forbidden
- /Users/dudu/Documents/3_Project/8_functional_query — Legacy Windows-era project root is historical source only; must not be read or written by this task.
- ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/ — T-021/D-004 bundle contents are read-only inputs. Do not modify, delete, or regenerate files inside this path. All loads are by reference via T-026 loader.
- ../../goal_package_foundation_v1/task_workspace_package_v1/4_artifact/2_persist/workspace/ — T-024 workspace is a completed upstream deliverable. Do not modify workspace files in place. If a package bug must be fixed, create a corrected local copy inside this task's 4_artifact.
- ../../../2_project_asset/ — Project-level raw materials are downstream from A-003 standard resources. T-021 bundle is already the consolidated data source.
- ../../../6_project_deliverable/ — Final external deliverables are not produced by a development task and must remain untouched.
### Output
- 3_execution/forward_engine.py
- 4_artifact/5_table/
- 4_artifact/2_persist/
- 4_artifact/3_document/
- 4_artifact/registry.yaml
- 5_report/completion.md
- 5_report/repair_log.md

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- `3_execution/` 只用于运行脚本、临时过程文件、日志和可恢复作业状态。任何需要验收、复用、登记或交给后续 task 的结果，即使执行中临时生成在 `3_execution/`，结束前也必须移动或复制到 `4_artifact/` 的合适子目录，并登记到 `4_artifact/registry.yaml`。
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_forward_query_engine_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_forward_query_engine_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_forward_query_engine_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
