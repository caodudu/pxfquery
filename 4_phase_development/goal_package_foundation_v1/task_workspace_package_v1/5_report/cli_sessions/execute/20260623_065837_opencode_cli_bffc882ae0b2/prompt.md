# Action Prompt
Generated: 2026-06-23 06:58

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
ID: T-024 | Name: workspace_package_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} current package workspace from migrated code without modifying legacy assets. Deliver pyproject/src layout, import/compile smoke evidence, and task reports.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1/task_workspace_package_v1

## Protocol
---
### protocol.md
# Protocol: workspace_package_v1

## Objective
Create a current `pxfquery` package workspace under this task's `4_artifact/` using the migrated legacy package code as a read-only source. Deliver a `pyproject.toml` + `src/` layout that can pass `import pxfquery` and basic smoke checks in the project Python environment, without modifying any legacy assets.

## Inputs
- A-001: Legacy PxFquery package code — Read-only source for all `.py` modules, `pyproject.toml`, and package structure to replicate as a `src/`-layout workspace.
- A-002: T-013 MVP capability review deliverables — Reference for what already passed/failed in the legacy package; guides which smoke tests are realistic and which are expected to fail.
- A-003: Current project protocol — Defines the active runtime environment (`pxfquery` conda env), path boundaries, and non-modification rules for legacy assets.

## Steps
1. Read the legacy package `pyproject.toml`, `__init__.py`, and module tree (data, index, llm, prompt, query, viz) from the migrated asset library to understand the current flat package shape, dependencies, and public API.
2. Create a `src/pxfquery/` directory under `4_artifact/2_persist/workspace/` with the same module tree, copying source `.py` files and preserving all subpackage `__init__.py` files. Place `pyproject.toml`, `README.md`, and any root-level `.py` files (excluding `__pycache__`) in `src/pxfquery/`, adjusting imports if needed for the new package root.
3. Produce a workspace-level `pyproject.toml` at `4_artifact/2_persist/workspace/pyproject.toml` with `[tool.setuptools.packages.find]` configured for `where = ["src"]` and dependencies matching the legacy package.
4. In the `pxfquery` conda environment, run a package install from the workspace directory and test `python -c "from pxfquery import PxFquery; print('import OK')"`. Log the exact command, environment, and stdout/stderr output.
5. Run compile-smoke checks on all migrated `.py` modules using `python -m py_compile` or equivalent, recording which modules pass and which fail. Failures should be triaged. If a scoped package fix is required for this task deliverable to run, implement the fix inside this task workspace and record the lineage and validation evidence.
6. Write a workspace summary, an import/compile smoke evidence log, and register all outputs.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-024`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-024` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.
- Do not modify any file inside `2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/`.
- Do not edit legacy source, regenerate indexes, rebuild matrices, or change package APIs.
- The workspace should live entirely under `4_artifact/2_persist/workspace/`.
- Use the project default conda environment (`/Users/dudu/Softwares/miniconda/envs/pxfquery`) for any Python execution.
- `__pycache__` directories in the legacy source must not be copied.
- Legacy `main.py` is a historical placeholder; include it in the workspace for traceability but it need not pass import or smoke checks as a standalone module.
- If `py_compile` fails on a module, record the failure with the error message and fix scoped package issues when the fix is required for the task deliverable to run. Keep fixes inside this task workspace and document lineage.

## Deliverables
- Workspace root: `4_artifact/2_persist/workspace/`
- Compiled package tree: `4_artifact/2_persist/workspace/src/pxfquery/`
- Workspace `pyproject.toml`: `4_artifact/2_persist/workspace/pyproject.toml`
- Workspace `README.md`: `4_artifact/2_persist/workspace/README.md`
- Import/compile smoke evidence log: `4_artifact/2_persist/pxfquery_t024_smoke_evidence_v20260623.md`
- Workspace summary: `4_artifact/3_document/pxfquery_t024_workspace_summary_v20260623.html`
- Execution report: `4_artifact/3_document/execution_report_v20260623.html`
- Result report: `4_artifact/3_document/result_report_v20260623.html`

## Acceptance
- `4_artifact/2_persist/workspace/src/pxfquery/__init__.py` exists and is byte-identical to the legacy source.
- `import pxfquery` succeeds in the `pxfquery` conda environment after local `pip install -e .` from the workspace directory.
- Smoke evidence log documents the exact commands and their output.
- Legacy assets in `2_project_asset/` remain unmodified.

## Assets (4)
- [raw] Legacy PxFquery package code — legacy_flat_asset_library_v20260614
- [deliverable] T-013 MVP capability review deliverables — goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact
- [deliverable] Current project protocol — project_init
- [reference] Migrated code design documents — legacy_flat_asset_library_v20260614

## Asset Rules

### Required
- ../../../2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/ — Read-only source for migrated legacy package code; provides all .py modules, pyproject.toml README.md and the package tree to mirror into a current src/-layout workspace. No edits allowed in this path.
- ../../../4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/ — T-013 MVP capability review outputs (capability contract, capability status matrix, failure/missing capability list) used to judge which import/compile smoke tests are realistic and which are expected to fail.
- ../../../1_project_init/1_project_protocol/ — Active project boundaries, source authority rules, and the default pxfquery conda environment definition required for any Python execution.
### Forbidden
- /Users/dudu/Documents/3_Project/8_functional_query — Legacy Windows-era project root is historical source only; must not be read or written by this task.
- ../../../2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ — Migrated flat asset library is the input source. The pxfquery_package/ folder must be read-only; it must not be modified, regenerated, or repaired from this task.
- ../../../6_project_deliverable/ — Final project deliverables are not produced by a workspace-creation task and must remain untouched.
### Output
- 3_execution/
- 4_artifact/2_persist/workspace/
- 4_artifact/2_persist/
- 4_artifact/3_document/
- 4_artifact/registry.yaml
- 5_report/completion.md

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- `3_execution/` 只用于运行脚本、临时过程文件、日志和可恢复作业状态。任何需要验收、复用、登记或交给后续 task 的结果，即使执行中临时生成在 `3_execution/`，结束前也必须移动或复制到 `4_artifact/` 的合适子目录，并登记到 `4_artifact/registry.yaml`。
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_package_foundation_v1/task_workspace_package_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_package_foundation_v1/task_workspace_package_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_package_foundation_v1/task_workspace_package_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
