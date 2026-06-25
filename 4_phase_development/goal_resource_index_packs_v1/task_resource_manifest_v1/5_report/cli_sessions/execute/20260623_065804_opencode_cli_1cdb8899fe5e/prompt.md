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
ID: T-025 | Name: resource_manifest_v1
Status: active | Executor: hybrid
Objective: Create pxfquery-{task_id} standard resource manifest from T021 standard_resources D-004. Deliver manifest, schema summary, and usage notes.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_resource_manifest_v1

## Protocol
---
### protocol.md
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

### Step 5: Write usage notes

Write `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md` describing:

1. How to load the bundle (suggested Python snippets for h5ad via `anndata.read_h5ad`, JSON via `json.load`, CSV via `pandas.read_csv`).
2. How downstream tasks should reference the bundle path: the canonical path is the T-021 bundle path; the manifest is the declared inventory but the bytes always come from A-001.
3. Verification expectations: any consumer of the bundle must Python-load every file before relying on its schema; matrix dimensions must match the manifest claims.
4. Provenance pointer back to T-021/D-004 and T-021/D-001 guide.
5. Hard rules: do not split the bundle; do not move files; do not duplicate into this task's own directory.

Output: `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md`.

### Step 6: Validate manifest

Run a Python check that:

1. Lists the bundle directory and confirms the manifest's `files:` list has exactly the same filenames as `os.listdir(bundle_path)`.
2. Confirms the file count in the manifest matches `len(os.listdir(bundle_path))`.
3. Confirms each manifest entry's filename points to an existing file.
4. Confirms `data_description.yaml` is referenced and exists.
5. Records total bundle size in MB and writes it into the manifest header.

Save the validation output to `3_execution/step6_validation.json`.

Output: validation JSON + a one-line confirmation in completion.md.

### Step 7: Register outputs and write completion

Register the three artefact files in `4_artifact/registry.yaml` (D-006 manifest, D-007 schema summary, D-008 usage notes, D-009 validation record) and the manifest is added as an input-side asset for future tasks by writing `1_asset/registration.yaml` updates for any consumer-facing entries. Write `5_report/completion.md` summarising what was produced and what was intentionally not produced (no new data, no byte-level copies).

Output: registry update + completion.md.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-025`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-025` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

- Do not modify the T-021 bundle. It is read-only input.
- Do not copy any bundle bytes into this task directory. The manifest is the inventory; the actual data lives at A-001.
- Manifest must be single-file and parseable as YAML (no anchors to cross-task files).
- Do not duplicate the 91 function names verbatim inside the manifest; reference `function_index.json` instead.
- Schema summary and usage notes may cite external paths but must remain readable on their own.
- No HTML reports are required for this configuration task — manifest, schema summary, and usage notes ARE the deliverable. Loading/validation evidence is captured in `3_execution/` plus `5_report/completion.md`.

## Deliverables

1. `4_artifact/2_persist/pxfquery_T025_standard_resource_manifest_v20260623.yaml` — the manifest.
2. `4_artifact/2_persist/pxfquery_T025_schema_summary_v20260623.md` — schema summary.
3. `4_artifact/2_persist/pxfquery_T025_usage_notes_v20260623.md` — usage notes.
4. `4_artifact/registry.yaml` — updated with T-025 artefacts.
5. `3_execution/step6_validation.json` — Python validation evidence.
6. `5_report/completion.md` — completion report.

## Acceptance

- Manifest lists exactly the 19 files in the T-021 bundle (binary byte-for-byte equality between manifest `files[]` filenames and `os.listdir(bundle_path)`).
- Each matrix entry records `obs` columns and a 91-var count consistent with T-021.
- Each JSON index entry records its top-level key shape.
- Each CSV entry records key columns and approximate row count.
- Total bundle size in the manifest is within ±5% of the actual `os.path.getsize` sum.
- `data_description.yaml` is included and labelled as `description`.
- No byte-level duplication of bundle files occurs in this task directory.
- Schema summary and usage notes are self-contained Markdown files that a developer can read independently of T-021/D-001.
- `4_artifact/registry.yaml` lists every new artefact with a stable `identity: T-025/D-006..009`.

## Assets (6)
- [deliverable] T-021 standard_resources bundle (D-004) — task_standard_resources_optimal_formats
- [deliverable] T-021 standard resource guide (D-001) — task_standard_resources_optimal_formats
- [deliverable] T-021 execution report (D-002) — task_standard_resources_optimal_formats
- [deliverable] T-021 result report (D-003) — task_standard_resources_optimal_formats
- [deliverable] T-021 process records (D-005) — task_standard_resources_optimal_formats
- [deliverable] T-021 artifact registry — task_standard_resources_optimal_formats

## Asset Rules

### Required
- A-001
- A-002
### Forbidden
- ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/ — T-021 bundle and all its artefacts are read-only input. Do not modify upstream deliverables.
- ../../../2_project_asset/ — Project-level raw materials are scoped out; T-021 already consolidated the relevant subset into D-004.
- /Users/dudu/Documents/3_Project/8_functional_query — Legacy Windows-era historical source. Not needed for manifest derivation.
### Output
- 4_artifact/2_persist/
- 4_artifact/registry.yaml
- 3_execution/
- 5_report/

## Instructions
读完上方所有文件后再执行。
- 资产文件按需读取（先读 registration.yaml，再取 required 资产内容）
- 产出写入 4_artifact/ 或 5_report/，以 Protocol ## Deliverables 为准
- 3_execution/ 下按 Steps 编号建子文件夹（§14）：01_xxx/ 02_xxx/
- `3_execution/` 只用于运行脚本、临时过程文件、日志和可恢复作业状态。任何需要验收、复用、登记或交给后续 task 的结果，即使执行中临时生成在 `3_execution/`，结束前也必须移动或复制到 `4_artifact/` 的合适子目录，并登记到 `4_artifact/registry.yaml`。
- 真实性最高优先级：没做就是没做，做不出来就是做不出来。不得把未执行 Step、失败测试、空壳文件、占位结果或"以后再做"包装成完成交付。
- 如果无法完成或只能部分完成，立即写 `5_report/blocked.md`，说明已做什么、哪一步没做成、失败证据、需要什么才能继续；如果可以调用 CyHex API，同时 POST `/api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_resource_manifest_v1/stage_incident`，body: `{"stage":"execute","kind":"failed|capability_failed|config_mismatch","reason":"...","evidence":"..."}`。工具/权限/联网/看图/读写/账号能力不足用 `capability_failed`；缺失关键数据，或 CyHex 登记、协议、资产规则、task_graph 与实际文件夹内容不一致，用 `config_mismatch`。最终回复必须明确说"未完成"或"部分完成"，不得请求验收通过。
- 如果发现自己在重复无意义尝试、没有新增证据、无法形成下一步计划，不要继续消耗时间；写 `5_report/blocked.md` 并上报 `kind=failed`。
- 如果任务需要三四天级后台运行，不要让本 CLI session 一直监听；在 `3_execution/` 写可恢复脚本、日志、pid/状态文件和检查点，调用 `POST /api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_resource_manifest_v1/durable_jobs` 登记 command/log_file/status_file，启动 durable job 后结束本轮 session，并在脚本里写入完成回调：`PATCH /api/projects/12_PxFquery/tasks/goal_resource_index_packs_v1/task_resource_manifest_v1/durable_jobs/{job_id}`。完成只代表进入 `execute_job_ready` 等待检查，不代表 done。
- **强制产出两份 HTML 报告**，写入 `4_artifact/3_document/`，两份均登记为 5 星（§5 §15）：
  1. `execution_report_v{YYYYMMDD}.html` — 执行情况报告：任务摘要、每步执行情况、交付物清单、失败/阻断记录
  2. `result_report_v{YYYYMMDD}.html` — 结果报告：高可读性成果展示，含可视化图表，面向非开发者阅读
- 产出物登记到 4_artifact/registry.yaml（§15）
- 写 5_report/completion.md（结果摘要 + 输出清单）
- 执行完成后不要自行 PATCH status → done；输出交付清单并等待人类验收。验收通过后由人类或验收流程 PATCH done。
