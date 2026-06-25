# Action Prompt
Generated: 2026-06-23 09:06

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
ID: T-032 | Name: reverse_stability_guard_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} reverse-query numerical stability guard for zero-norm/abnormal similarity warnings. Deliver patch, tests, and ranking sanity evidence.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1

## Protocol
---
### protocol.md
# Protocol: reverse_stability_guard_v1

## Objective

Add a numerical stability guard to the PxFquery reverse query path so that abnormal inputs — zero-norm rows, zero-norm target vectors, NaN/Inf in score rows, fully-empty matrices after cell-line filtering, and unmatched terms — are handled explicitly and never silently corrupt the ranked candidate output. Produce a task-versioned `pxfquery-T-032` package (built on top of the T-024 / pxfquery-T-024 workspace), with an automated stability demo, a normal positive control against T-021/D-004, and visible ranking-sanity evidence so that downstream tasks and humans can trust reverse-query results without re-auditing every cosine call.

## Inputs

- A-001: T-024 workspace package (pxfquery-T-024) — current editable install of pxfquery with `query/reverse.py` (ReverseQuery, ReverseResult), `query/forward.py`, `query/resolver.py`, `data/loader.py` (DataLoader), `core.PxFquery`, and the utility functions `fuzzy_match`, `build_target_vector`, `cosine_similarity_matrix` in `utils.py`. T-032 reads these modules to identify the zero-norm / abnormal-similarity code paths and to install the final repaired workspace as `pxfquery-T-032`.
- A-002: T-026 loader outputs (pxfquery-T-026) — loader package (`load_bundle`, `load_matrix`) and `loader_validation.json` reporting observed matrix shapes, obs columns, and dtypes for 19/19 files. Used at the start of the stability demo to confirm runtime schema before injecting abnormal inputs.
- A-003: T-021 standard resources bundle (D-004) — canonical 19-file float32 H5AD matrices (cp/sh/xpr), JSON indexes, CSV metadata. The actual data for both the positive-control reverse query (apoptosis activate / MYC suppress) and the stability scenarios. Loaded by reference, never copied.
- A-004: T-013 MVP capability review deliverables — capability status matrix (D-003) and failure/missing capability list (D-005). Documents the warning evidence that motivates this guard: `cosine_similarity_matrix` silently fills zero denominators with `1e-10`, which produces arbitrarily large similarity values for zero-norm rows or zero-activation targets and corrupts reverse-query ranking.
- A-005: Current project protocol — pxfquery conda env, workspace boundaries, legacy-source non-modification rules, and the hard rule that any ranked output be saved as a runnable artifact (not a placeholder).

## Steps

1. Read A-001 (`utils.py`, `query/reverse.py`, `core.py`, `data/loader.py`) and audit each function for numerical-stability risk paths: zero-norm row in `cosine_similarity_matrix`, zero-norm target vector (`build_target_vector` returning an all-zero array when no terms fuzzy-match), unmatched terms, NaN/Inf in row data (which can appear after upstream slicing), and the empty-after-aggregation branch.
2. Read A-002's `loader_validation.json` (or completion report) to confirm matrix shapes, obs columns (`pert_id`, `cmap_name`, `cell_iname`), functional term var_names, and dtype (`float32`). Identify which bundle path contains `cp_func_ad.h5ad` (preferred data source for both control and stability scenarios).
3. Build a repaired workspace copy at `3_execution/pxfquery_T-032_repaired/` that mirrors T-024's src/-layout but adds a stability guard layer. Register this copy as a task-versioned PxFquery asset named `pxfquery-T-032`. Required changes inside the repaired copy only:
   - Replace `utils.cosine_similarity_matrix` with a guarded version that emits a `(severity, scenario, message, indices)` warning per guarded event: zero-norm row, zero-norm target, NaN row, Inf row; rows involved in a guarded case get similarity = `0.0` (and are excluded from ranking) rather than `inf`/`-inf`/`nan`.
   - Extend `utils.build_target_vector` to return `(vector, matched_terms, unmatched_terms)` so the caller can distinguish "no activation terms were fuzzy-matched" from "user requested zero activation". If matched is empty, emit a `target_empty` warning and the caller short-circuits with the standard "not found" path instead of returning NaN/Inf.
   - Add a `GuardEvent` dataclass (or equivalent) and a `GuardReport` aggregator on `ReverseResult`, exposing `.warnings` as a list of dicts so the stability demo and downstream consumers can serialize them.
   - Ensure backward compatibility: any non-abnormal input must produce identical similarity values within floating-point tolerance (no ranking regression).
4. Install the repaired workspace as editable (`pip install -e .`) into the `pxfquery` conda env. Verify the installation via `python -c "import pxfquery; print(pxfquery.__file__)"` resolves to the `3_execution/pxfquery_T-032_repaired/` copy.
5. Implement `3_execution/run_stability_guard.py` that executes both required scenarios in one run, all inside `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`:
   - **Scenario A — Normal positive control**: load `cp_func_ad.h5ad` from the A-003 bundle, run `func2pert(activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="MCF7", top_k=20)`, assert all top-K similarities are finite values within `[-1.0, 1.0]` and that the guard report contains zero "zero_norm_row" / "zero_norm_target" / "nan_row" / "inf_row" warnings for this run. Serialize candidates to `pxfquery_T-032_positive_control_candidates.json` and metadata to `pxfquery_T-032_positive_control_meta.json` under `4_artifact/2_persist/`.
   - **Scenario B — Abnormal-similarity guard**: construct a synthetic ReverseQuery (or `PxFquery` instance) over a small matrix that contains (i) an all-zero row, (ii) a NaN row, (iii) an Inf row, (iv) a target activation list that fuzzy-matches to nothing, and (v) a near-empty matrix slice where every row has norm 0. For each sub-case assert that the guard fires the expected warning and that the surviving ranked candidates (if any) contain only finite values in `[-1, 1]`. Serialize the aggregated warnings to `pxfquery_T-032_guard_warnings.json` under `4_artifact/2_persist/`.
6. Write a machine-readable validation record `3_execution/stability_guard_validation.json` capturing: exact command executed, conda env, python version, key package versions, repaired workspace path, scenario inventory, per-scenario expected vs actual (guard warned?, similarity clipped?, ranking preserved?, NaN/Inf counts), and summary pass/fail flags.
7. Write Chinese HTML reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — step-by-step record of guard implementation, scenarios, and outcomes.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — human-readable summary of guard semantics, positive-control top-K ranking, and ranking-sanity evidence.
8. If any repaired code was needed, write `5_report/repair_log.md` describing the source asset (T-024), changed files (inside the `pxfquery-T-032` copy), what was fixed (e.g. zero-denominator fill, unmatched-target no-op, NaN/Inf clipping), validation evidence, and which downstream task should consume the corrected version.
9. Write `5_report/completion.md` summarizing guard behavior, repaired issues, positive-control evidence, and downstream consumption guidance for any follow-up task that depends on stable reverse-query output.
10. Register outputs via `4_artifact/registry.yaml`.

### Required Bug-Repair Handling

- If a bug (e.g. silent division-by-zero, unhandled NaN/Inf, aggregation masking zero rows) prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, named `pxfquery-T-032`.
- Record what was fixed, the source asset or task id, changed files, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task reads `pxfquery-T-024` and emits `pxfquery-T-032` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. Do not modify A-001 (`pxfquery-T-024`), A-002 (`pxfquery-T-026`), A-003 (`T-021/D-004`), or A-004 (`T-013`) in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary. Preserve lineage, validation evidence, and downstream consumption guidance.

### Guard Semantics

- Guard behavior must NEVER corrupt the normal ranking. For any row with non-zero norm and a non-zero target, the similarity returned by the repaired `cosine_similarity_matrix` must equal the legacy cosine within `1e-12` relative tolerance.
- Every guarded event (zero-norm row, zero-norm target, NaN row, Inf row, unmatched-only target) must emit a structured `GuardEvent` warning that is observable to the caller and persisted in JSON. Silent epsilon fills are not acceptable evidence paths.
- Guarded rows must be excluded from the ranked candidate output (similarity → 0, dropped) rather than allowed to dominate the top-K with `inf` / `-inf` / `nan`.
- The positive control must run on the same data, the same env, and the same query as T-030 to make no-regression verifiable by direct comparison.

### Execution Discipline

- All Python execution must use the project default conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- The repaired `pxfquery-T-032` workspace must be installed as editable (`pip install -e .`) in the pxfquery conda env before running either scenario.
- Do not copy T-021/D-004 matrix bytes into this task; load by reference through A-001's `DataLoader` / `core.PxFquery` or A-002's `load_matrix`.
- Do not hard-code matrix shapes, column names, function term names, or file paths from planning notes — discover them at runtime.
- The demo must actually run and produce non-empty artifacts; the stability demo and the positive control must each yield at least one serializable structured output. File existence alone is not acceptable.
- Synthetic abnormal inputs must be built inside this task's `3_execution/`. Do not write or rely on a mutated copy of the upstream H5AD files.

## Deliverables

- `3_execution/run_stability_guard.py` — stability guard demo + positive-control script.
- `3_execution/stability_guard_validation.json` — machine-readable validation record with per-scenario pass/fail.
- `3_execution/pxfquery_T-032_repaired/` — repaired workspace copy (`pxfquery-T-032`) implementing the guard; editable install target for the demo.
- `4_artifact/2_persist/pxfquery_T-032_guard_warnings.json` — structured guard warnings emitted by the abnormal-similarity scenarios.
- `4_artifact/2_persist/pxfquery_T-032_positive_control_candidates.json` — ranked candidate output (rank, cmap_name, cell_iname, similarity, driving_terms) for the normal reverse query.
- `4_artifact/2_persist/pxfquery_T-032_positive_control_meta.json` — query metadata (activate, suppress, cell_line, note, guard_warning_count).
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — T-032 artifact registry.
- `5_report/completion.md` — completion report.
- `5_report/repair_log.md` — only if a `pxfquery-T-024` workspace bug was repaired inside this task.

## Acceptance

- Abnormal similarity cases are handled explicitly: every injected zero-norm row, NaN row, Inf row, and unmatched-only target produces the expected guard warning in `pxfquery_T-032_guard_warnings.json`, and no guarded value leaks into the top-K of any scenario.
- Normal reverse query still returns ranked candidates: the positive-control candidates JSON contains ≥ 1 ranked row, all similarities are finite within `[-1.0, 1.0]`, automobile cell-line and apoptosis/MYC terms are honored, and the guard report shows zero abnormal-similarity warnings for this run.
- The repaired `pxfquery-T-032` workspace is installed as editable and demonstrably imports from its own path, with lineage back to `pxfquery-T-024` recorded in `repair_log.md` when repair happened.
- Validation JSON is non-empty, captures the exact run parameters, and explicitly asserts each scenario outcome.

## Notes

- T-030 reverse-query engine output is consumed transitively via A-001 (the `pxfquery-T-024` ReverseQuery/ReverseResult classes) and A-003 (the standard resources bundle). T-030 itself does not produce required artifacts for T-032; T-032 generates the stability evidence directly from `pxfquery-T-024` plus its own repaired copy.
- T-013 review (A-004) is the warning evidence source. If T-013's gap list is updated in the future, T-032's scenario set should be re-audited; for now the scenarios listed in step 5 cover the failures documented by T-013.
- Downstream task T-033 (or equivalent) that depends on stable reverse-query ranking should consume `pxfquery-T-032` (the edited repaired workspace), not the upstream `pxfquery-T-024`.

## Assets (0)
(none)

## Asset Rules


## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- `3_execution/` 只用于运行脚本、临时过程文件、日志和可恢复作业状态。任何需要验收、复用、登记或交给后续 task 的结果，即使执行中临时生成在 `3_execution/`，结束前也必须移动或复制到 `4_artifact/` 的合适子目录，并登记到 `4_artifact/registry.yaml`。
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
