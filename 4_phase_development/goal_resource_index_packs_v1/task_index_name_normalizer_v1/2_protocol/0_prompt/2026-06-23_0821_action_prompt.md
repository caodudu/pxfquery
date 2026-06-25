# Action Prompt
Generated: 2026-06-23 08:21

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
ID: T-027 | Name: index_name_normalizer_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} runtime query index directory with resolver-compatible filenames from T021 standard indexes. Deliver normalized index pack and schema report.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_index_name_normalizer_v1

## Protocol
---
### protocol.md
# Protocol: task_index_name_normalizer_v1

## Objective

Create a `pxfquery-T-027` runtime query index directory that contains resolver-compatible filenames symlinked from the T-021 standard resources bundle (D-004). Deliver the normalized index pack and a schema report mapping each source file to its normalized output.

The pxfquery `QueryResolver` (see `code/pxfquery_package/query/resolver.py`) expects 7 specific JSON filenames under `index_dir`:
- `cellline_index.json`, `cellline_neighbors.json`
- `gene_index_simple.json`, `gene_neighbors_simple.json`
- `drug_index.json`, `drug_neighbors.json`
- `function_index.json`

The T-021 bundle already uses these exact filenames for its JSON indexes (plus 3 extra JSONs: `cellline_tree.json`, `gene_index.json`, `gene_neighbors.json`). This task normalizes the directory so the resolver can point directly at the T-027 runtime index pack.

## Inputs

- A-001: T-021 standard_resources bundle (D-004) — 19-file bundle under `task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/`. Source of 10 JSON index files.
- A-002: T-025 resource manifest (D-006) — enumerates all 19 files with schema, category, and filenames. Used as the authoritative inventory.
- A-003: T-025 schema summary (D-007) — describes JSON index shapes. Used for cross-reference when producing the schema report.
- A-004: T-021 artifact registry — confirms D-004 identity and file inventory.

## Steps

### Step 1: Read and verify source files

Read A-001 (the T-021/D-004 bundle) and A-002 (T-025/D-006 manifest). Confirm:
- The 10 JSON files exist under the T-021 standard_resources directory.
- Filenames are: `cellline_index.json`, `cellline_neighbors.json`, `cellline_tree.json`, `drug_index.json`, `drug_neighbors.json`, `gene_index_simple.json`, `gene_neighbors_simple.json`, `gene_index.json`, `gene_neighbors.json`, `function_index.json`.
- The 7 resolver-required files are present.

Output: `3_execution/step1_file_inventory.json`.

### Step 2: Create normalized runtime index directory

Create `4_artifact/2_persist/pxfquery_T027_runtime_query_index/` and populate it:

For each of the 7 resolver-required JSON files, create a symlink pointing to the corresponding file in the T-021/D-004 bundle:
- `cellline_index.json` → T-021 bundle `cellline_index.json`
- `cellline_neighbors.json` → T-021 bundle `cellline_neighbors.json`
- `gene_index_simple.json` → T-021 bundle `gene_index_simple.json`
- `gene_neighbors_simple.json` → T-021 bundle `gene_neighbors_simple.json`
- `drug_index.json` → T-021 bundle `drug_index.json`
- `drug_neighbors.json` → T-021 bundle `drug_neighbors.json`
- `function_index.json` → T-021 bundle `function_index.json`

No byte-level copying — symlinks preserve the single source of truth at D-004.

Optionally (not required by resolver but part of the complete index pack), also symlink the 3 supplementary JSON files (`cellline_tree.json`, `gene_index.json`, `gene_neighbors.json`).

Do NOT symlink H5AD matrices or CSV metadata — those are not query indexes and are handled by T-026 (matrix loader).

Output: `4_artifact/2_persist/pxfquery_T027_runtime_query_index/` (directory of symlinks).

### Step 3: Validate normalized index pack

Write and run a Python script that:
1. Lists all symlinks in the normalized directory.
2. For each symlink, resolves and confirms the target file exists and is readable.
3. Loads each JSON file and verifies it is valid JSON.
4. Confirms all 7 resolver-required filenames are present.
5. Confirms a `QueryResolver` would accept this directory as `index_dir` (by inspecting the resolver's expected filenames against the directory contents).

Output: `3_execution/step3_validation.json`.

### Step 4: Write schema report

Write `4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md` mapping:
- Each source index filename (in T-021/D-004) → normalized output filename in the T-027 runtime pack.
- Top-level JSON key shape for each file (from T-025/D-007 schema data).
- Resolution status for each file (symlinked, not symlinked, or missing).
- A summary table listing all 7 resolver-required files with pass/fail status from Step 3 validation.

Output: `4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md`.

### Step 5: Register outputs and write completion

Register deliverables in `4_artifact/registry.yaml` and write `5_report/completion.md`.

### Required Bug-Repair Handling

- If any filename in T-021/D-004 differs from what the resolver expects, do not modify the upstream bundle. Instead, create the symlink with the resolver-compatible name in the T-027 output directory and record the name mapping in the schema report.
- If any required resolver file is missing from T-021/D-004, record the gap, assess whether it can be rebuilt from other T-021 bundle files, and proceed with what is available.

## Constraints

### Scoped Repair And Versioning

- Do not modify the T-021/D-004 bundle. It is read-only input.
- Do not byte-copy JSON files; use symlinks to preserve single source of truth.
- The normalized directory is `pxfquery_T027_runtime_query_index/` — this is the task's versioned output.
- Do not include H5AD or CSV files in the query index directory.
- No HTML reports are required for this configuration-derivation task — the normalized directory and schema report ARE the deliverable. Validation evidence is stored in `3_execution/`.
- If the execution AI's action prompt requires HTML reports per CyHex §3.3.4, produce minimal `execution_report_v{date}.html` and `result_report_v{date}.html` in `4_artifact/3_document/` reflecting the normalization work, and register them.

## Deliverables

1. `4_artifact/2_persist/pxfquery_T027_runtime_query_index/` — normalized runtime index directory with resolver-compatible symlinks.
2. `4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md` — source-to-output schema mapping report.
3. `3_execution/step1_file_inventory.json` — source file inventory evidence.
4. `3_execution/step3_validation.json` — Python validation evidence.
5. `4_artifact/registry.yaml` — updated with T-027 deliverables.
6. `5_report/completion.md` — completion report.
7. `4_artifact/3_document/execution_report_v{date}.html` — execution report (if required by CyHex action prompt).
8. `4_artifact/3_document/result_report_v{date}.html` — result report (if required by CyHex action prompt).

## Acceptance

- All 7 resolver-required filenames exist in the normalized directory.
- Each symlink resolves to a valid JSON file in T-021/D-004.
- All JSON files load as valid JSON.
- The schema report explains the source-to-output mapping for each file.
- No byte-level duplication of T-021 files occurs.
- The resolver's expected filenames are matched exactly.

## Assets (4)
- [deliverable] T-021 standard_resources bundle (D-004) — task_standard_resources_optimal_formats
- [deliverable] T-025 resource manifest (D-006) — task_resource_manifest_v1
- [deliverable] T-025 schema summary (D-007) — task_resource_manifest_v1
- [deliverable] T-021 artifact registry — task_standard_resources_optimal_formats

## Asset Rules

### Required
- A-001
- A-002
### Forbidden
- 1_asset/T-021 standard_resources bundle (D-004) — T-021 bundle is read-only input source. Do not modify or delete files inside it; symlink by reference only.
- ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/ — T-021/D-004 bundle contents are read-only inputs from predecessor task.
- ../../../2_project_asset/ — Project-level raw materials are scoped out; T-021 already consolidated the relevant subset into D-004 and T-025 enumerated it.
- /Users/dudu/Documents/3_Project/8_functional_query — Legacy Windows-era historical source. Not needed for index normalization; migrated assets are sufficient.
### Output
- 4_artifact/2_persist/pxfquery_T027_runtime_query_index/
- 4_artifact/2_persist/pxfquery_T027_schema_report_v20260623.md
- 3_execution/step1_file_inventory.json
- 3_execution/step3_validation.json
- 4_artifact/registry.yaml
- 5_report/completion.md
- 4_artifact/3_document/

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- `3_execution/` 只用于运行脚本、临时过程文件、日志和可恢复作业状态。任何需要验收、复用、登记或交给后续 task 的结果，即使执行中临时生成在 `3_execution/`，结束前也必须移动或复制到 `4_artifact/` 的合适子目录，并登记到 `4_artifact/registry.yaml`。
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_index_name_normalizer_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_index_name_normalizer_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_index_name_normalizer_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
