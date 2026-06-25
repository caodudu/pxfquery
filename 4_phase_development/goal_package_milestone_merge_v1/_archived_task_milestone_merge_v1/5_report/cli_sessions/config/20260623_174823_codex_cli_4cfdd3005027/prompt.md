# Action Prompt
Generated: 2026-06-23 17:47

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
ID: T-037 | Name: milestone_merge_v1
Status: active | Executor: codex
Objective: Create pxfquery-T-037 slim runnable package core: package workspace, loader/resource access, deterministic forward query, no-hit guard, and minimal package tests. Leave reverse/demo/final report completion to T-038.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_milestone_merge_v1

## Protocol
---
### protocol.md
# Protocol: milestone_merge_v1

## Objective
Create `pxfquery-T-037`, a slim runnable package core milestone assembled only from the minimum upstream assets required for a working package foundation: package workspace, loader/resource access, deterministic forward query, no-hit guard, and minimal package tests. Reverse/stability demo is moved to T-038, and final aggregation is moved to T-039.

## Inputs
- A-001: T-024 pxfquery workspace package — base src-layout package and pyproject foundation.
- A-002: T-021 standard resources bundle — canonical runtime resource files available through the loader lineage; use only the minimum files needed for local validation.
- A-003: T-025 standard resource manifest — optional resource inventory reference; do not make it a hard execution dependency.
- A-004: T-026 matrix/resource loader package — loader implementation and validation evidence to merge into the package.
- A-005: T-027 runtime query index directory — optional runtime-index reference only. Do not require it for T-037 package-core completion.
- A-006: T-028 function index pack — optional function-index reference only. Do not require it for T-037 package-core completion.
- A-007: T-029 forward query engine artifacts — runnable deterministic forward path and canonical result/evidence files.
- A-008: T-031 no-hit guard artifacts — false-positive guard module and no-hit/positive-control evidence.
- A-009: T-032 reverse stability guard artifacts and repaired package — optional reference only in T-037; T-038 consumes this as a hard input.
- A-010: T-035 integration smoke test artifacts — optional reference only in T-037; T-038 consumes this as a hard input.
- A-011: T-030 reverse query task record — lineage context only; its direct artifact registry is empty and must not block T-037.
- A-012: T-036 demo CLI task record — lineage context only; it must not block T-037 because T-037 produces its own final demo.
- A-013: Current project protocol — runtime environment and workspace-boundary reference.

## Steps
1. Verify only the T-037 required assets: A-001, A-002, A-004, A-007, A-008, and A-013. Treat A-003/A-005/A-006/A-009/A-010/A-011/A-012 as optional lineage/reference context and read them only if a specific missing detail is needed.
2. Create the T-037 package workspace under `4_artifact/2_persist/pxfquery-T-037/` from A-001, then merge loader/resource access, deterministic forward query evidence, and no-hit guard behavior into a coherent runnable package layout.
3. Vendor or reference only the minimum resource files needed for deterministic demo/test execution under the T-037 package artifact. Preserve upstream resources as read-only; if copying, keep checksums or file-size evidence in the lineage report.
4. Implement package entry points or scripts for deterministic forward and no-hit modes only. Do not require reverse/stability, optional resolver, LLM success, T-030 direct reverse artifacts, or T-036 demo artifacts.
5. Run focused checks in the project `pxfquery` conda environment: install/import smoke, compile checks, resource-loader check, forward demo, and no-hit negative demo.
6. If a bug blocks a runnable T-037 milestone, repair it inside the T-037 package artifact only. Do not overwrite upstream task artifacts. Record repaired files, source asset, validation evidence, and downstream consumption guidance.
7. Produce deliverables: merged package, test/demo logs and JSON/CSV outputs, package handoff notes, lineage report, artifact registry, completion report, and the two required Chinese HTML reports.

## Constraints
- This task configures and later executes a merged package milestone; it must not promote outputs into `6_project_deliverable/`.
- Do not modify upstream predecessor task artifacts, project raw assets, or the historical source root.
- Use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` for Python execution unless the executor documents a specific blocker.
- T-030 direct reverse output is missing and is outside T-037 package-core scope.
- T-036 demo output is not a hard input and is outside T-037 package-core scope.
- T-032/T-035 are handled by T-038, and final aggregation is handled by T-039; do not pull them back into T-037 as hard requirements.
- Config, check, and execute must be launched as separate fresh CLI sessions. Do not resume a previous long Codex thread for later stages.
- Optional resolver/LLM assets are outside the required milestone path and must not block completion.
- Large matrices and resource files should be inspected by manifest/schema/sample or loader validation rather than dumped into reports.

## Deliverables
- `4_artifact/2_persist/pxfquery-T-037/` — merged runnable Python package milestone.
- `4_artifact/2_persist/pxfquery_T037_handoff.md` — package-core handoff and usage notes for T-038.
- `4_artifact/2_persist/pxfquery_T037_lineage.md` — upstream asset-to-package lineage report for T-037 required inputs.
- `4_artifact/5_table/pxfquery_T037_test_results.json` — final test and smoke evidence.
- `4_artifact/5_table/pxfquery_T037_demo_summary.json` — forward/no-hit package-core demo evidence.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — output artifact registry.
- `5_report/completion.md` — completion and remaining-risk report.
- `5_report/repair_log.md` — only if scoped package repairs were needed.

## Acceptance
- The T-037 package installs or imports successfully in the `pxfquery` conda environment.
- Final tests include actual commands, exit status, and output files for import/compile, resource loading, forward query, no-hit guard, and reverse/stability demo behavior.
- The deterministic demo produces readable forward and no-hit outputs without requiring reverse/stability, optional resolver, or LLM assets.
- The lineage report maps every consumed upstream asset to the package core and explicitly states that reverse/stability and final demo/report completion moved to T-038.
- Required Chinese HTML reports exist under `4_artifact/3_document/`.

## Assets (13)
- [deliverable] T-024 pxfquery workspace package — T-024/ART-001
- [deliverable] T-021 standard resources bundle — T-021/D-004 via T-025/T-026 asset lineage
- [deliverable] T-025 standard resource manifest — T-025/D-006
- [deliverable] T-026 matrix/resource loader package — T-026/D-001
- [deliverable] T-027 runtime query index directory — T-027 completion deliverable D-001
- [deliverable] T-028 function index pack — T-028/D-001
- [deliverable] T-029 forward query engine artifacts — T-029/T029-D-001..D-007
- [deliverable] T-031 no-hit guard artifacts — T-031/T031-D-001..D-010
- [deliverable] T-032 reverse stability guard artifacts and repaired package — T-032/T032-D-001..D-010
- [deliverable] T-035 integration smoke test artifacts — T-035/T035-D-001..D-010
- [reference] T-030 reverse query task record — T-030 task root
- [reference] T-036 demo CLI task record — T-036 task root
- [reference] Current project protocol — project_init

## Asset Rules

### Required
- A-001
- A-002
- A-004
- A-007
- A-008
- A-013
### Forbidden
- ../../../2_project_asset/ — Project-level raw materials and migrated legacy assets are read-only; consume through registered predecessor outputs.
- ../../../6_project_deliverable/ — Final project deliverable promotion is outside this milestone task.
- /Users/dudu/Documents/3_Project/8_functional_query — Historical source root is not needed for this merge and must not be read or written.
- ../../../4_phase_development/goal_package_foundation_v1/task_workspace_package_v1/ — Upstream T-024 is read-only; copy from it into T-037 instead of editing in place.
- ../../../4_phase_development/goal_resource_index_packs_v1/ — Upstream resource/index predecessor tasks are read-only.
- ../../../4_phase_development/goal_deterministic_query_engines_v1/ — Upstream query-engine and guard predecessor tasks are read-only.
- ../task_smoke_tests_v1/ — T-035 smoke evidence is read-only.
- ../task_demo_cli_v1/ — T-036 is context only and must not be modified by T-037.
### Output
- 3_execution/
- 4_artifact/2_persist/pxfquery-T-037/
- 4_artifact/2_persist/pxfquery_T037_handoff.md
- 4_artifact/2_persist/pxfquery_T037_lineage.md
- 4_artifact/5_table/
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
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_milestone_merge_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_milestone_merge_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_milestone_merge_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
