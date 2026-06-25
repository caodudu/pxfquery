# Action Prompt
Generated: 2026-06-23 16:52

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
ID: T-036 | Name: demo_cli_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} user demo CLI/script with readable forward and reverse outputs. Deliver example output files and reports.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_demo_cli_v1

## Protocol
---
### protocol.md
# Protocol: demo_cli_v1

## Objective
Create `pxfquery-T-036`, a user-facing demo CLI/script that produces readable deterministic forward, reverse, and no-hit outputs from already validated milestone evidence. This task should not require optional resolver or LLM success.

## Inputs
- **A-001**: T-029 forward query artifacts. Required source for forward demo outputs and validation JSON.
- **A-002**: T-035 smoke test artifacts. Required integration evidence showing which upstream paths are runnable. T-035 records T-030 as `UNMET_DEPENDENCY`, so T-036 must not hard-depend on T-030 artifacts.
- **A-003**: T-031 no-hit guard artifacts. Required source for user-visible no-hit/negative demo output.
- **A-004**: T-032 reverse stability artifacts. Required source for reverse positive-control candidates and guard warning examples.
- **A-005**: T-032 reverse stability execution. Required validation JSON and repaired package path for reverse demo fallback.
- **A-006**: T-030 reverse query task record. Optional lineage reference only; visible artifact registry is empty.
- **A-007**: Current project protocol. Runtime and boundary rules.

## Steps
1. Verify required assets resolve and are non-empty: T-029 validation/result tables, T-035 smoke results, T-031 no-hit evidence, T-032 positive-control/reverse stability evidence.
2. Implement `3_execution/pxfquery_demo_cli.py`, a lightweight demo CLI with deterministic modes:
   - `forward`: read and display T-029 EGFR/A549 output in a readable table/JSON.
   - `reverse`: read and display T-032 positive-control reverse candidates and metadata.
   - `no-hit`: read and display T-031 no-hit evidence showing guarded negative behavior.
   - `all`: run all three modes and write consolidated demo output.
3. Run the demo CLI in the `pxfquery` conda environment:
   `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/pxfquery_demo_cli.py all`.
4. Write outputs:
   - `4_artifact/5_table/pxfquery_T036_forward_demo.json`
   - `4_artifact/5_table/pxfquery_T036_reverse_demo.json`
   - `4_artifact/5_table/pxfquery_T036_no_hit_demo.json`
   - `4_artifact/5_table/pxfquery_T036_demo_summary.json`
   - `4_artifact/2_persist/pxfquery_demo_cli.py`
   - `4_artifact/2_persist/pxfquery_T036_usage.md`
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html`
   - `4_artifact/3_document/result_report_vYYYYMMDD.html`
   - `4_artifact/registry.yaml`
   - `5_report/completion.md`
5. If a scoped integration issue prevents a runnable demo, repair only inside T-036 outputs and document in `5_report/repair_log.md`.

### Required Bug-Repair Handling
- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-036`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints
- Do not modify upstream completed artifacts in T-029/T-031/T-032/T-035.
- Do not require T-030 artifact content; T-030 is a lineage reference only because T-035 recorded its executable reverse demo as unmet.
- Do not require T-033 resolver output or any LLM adapter output.
- All Python execution must use the `pxfquery` conda environment.
- The demo should use lightweight JSON/CSV evidence already produced by upstream tasks; do not load large H5AD matrices.

## Deliverables
- `3_execution/pxfquery_demo_cli.py` — runnable demo CLI/script.
- `4_artifact/2_persist/pxfquery_demo_cli.py` — registered reusable copy.
- `4_artifact/2_persist/pxfquery_T036_usage.md` — usage notes.
- `4_artifact/5_table/pxfquery_T036_forward_demo.json` — readable forward demo output.
- `4_artifact/5_table/pxfquery_T036_reverse_demo.json` — readable reverse demo output.
- `4_artifact/5_table/pxfquery_T036_no_hit_demo.json` — readable no-hit demo output.
- `4_artifact/5_table/pxfquery_T036_demo_summary.json` — consolidated demo evidence.
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — result report.
- `4_artifact/registry.yaml` — deliverable registry.
- `5_report/completion.md` — completion report.

## Acceptance
- Demo CLI runs locally in the `pxfquery` conda environment.
- Demo writes visible, readable forward, reverse, and no-hit outputs.
- Demo does not require optional LLM/resolver success.
- Demo does not fail because T-030 direct artifacts are absent; it uses T-032 reverse evidence for the reverse user demo.
- Output includes actual command results and files, not just file-existence claims.

## Assets (7)
- [deliverable] T-029 forward query artifacts — goal_deterministic_query_engines_v1/task_forward_query_engine_v1
- [deliverable] T-035 smoke test artifacts — goal_package_milestone_merge_v1/task_smoke_tests_v1
- [deliverable] T-031 no-hit guard artifacts — goal_deterministic_query_engines_v1/task_no_hit_guard_v1
- [deliverable] T-032 reverse stability artifacts — goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1
- [deliverable] T-032 reverse stability execution — goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1
- [support] T-030 reverse query task record — goal_deterministic_query_engines_v1/task_reverse_query_engine_v1
- [deliverable] Current project protocol — project_init

## Asset Rules

### Required
- 1_asset/T-029 forward query artifacts — T-029 forward query engine artifact bundle (4_artifact/) containing forward_engine.py and result tables. The demo CLI reuses this engine as the forward entry point and the EGFR/A549 CSV as the canonical example file humans see.
- 1_asset/T-030 reverse query task record — T-030 reverse query engine task root — the demo CLI reuses T-030 run_reverse_demo.py and 4_artifact/ if delivered; otherwise the demo skips the reverse block and records UNMET_DEPENDENCY. Read-only.
- 1_asset/T-035 smoke test artifacts — T-035 integration smoke evidence — confirms which predecessors are runnable. Used by the demo to decide whether the reverse / no-hit / stability branches can be exercised as living scripts or must be invoked via static re-run commands.
- 1_asset/Current project protocol — Current project protocol defining the pxfquery conda environment, workspace boundaries, and source authority rules required for any Python execution.
### Forbidden
- ../../../../2_project_asset/ — Project-level raw materials / legacy flat asset library are read-only. T-021 standard resources bundle is already the consolidated data source used by A-001.
- ../../../../6_project_deliverable/ — Final milestone deliverables are produced by T-037 / task_milestone_merge_v1, not by this demo CLI task.
- /Users/dudu/Documents/3_Project/8_functional_query — Legacy Windows-era historical source root must not be read or written by this task.
### Output
- 3_execution/
- 4_artifact/
- 5_report/

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- `3_execution/` 只用于运行脚本、临时过程文件、日志和可恢复作业状态。任何需要验收、复用、登记或交给后续 task 的结果，即使执行中临时生成在 `3_execution/`，结束前也必须移动或复制到 `4_artifact/` 的合适子目录，并登记到 `4_artifact/registry.yaml`。
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_demo_cli_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_demo_cli_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_demo_cli_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
