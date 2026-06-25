# Checking Prompt
Generated: 2026-06-24 05:27

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md`

Write it carefully. It should give execution strategy, risk controls, expected outputs, and stop conditions.

## 1. Assembled Context Snapshot

CyHex has already assembled the project protocol, project state, and current task configuration below. Use this snapshot as your default context.

Do not re-read these files in green_check. Open the source paths only if the snapshot is missing, truncated at the exact section you need, or internally contradictory.

You may still call `GET http://localhost:47291/api/version` once to confirm CyHex is running. You do not need to read `cyhex_protocol.md` unless this prompt is missing a checking rule you must apply.

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

### 1.1 Project Protocol Snapshot
### Project Protocol: 0_overview.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/0_overview.md`

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

### Project Protocol: 1_goal.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/1_goal.md`

```text
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

```

### Project Protocol: 2_rule.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/2_rule.md`

```text
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

```

### Project Protocol: 3_environment.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/3_environment.md`

```text
# Environment

## Active Paths

- Project root: `/Users/dudu/Documents/3_Project/12_PxFquery`
- Project protocol: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol`
- Migrated legacy asset library: `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614`
- Historical source root: `/Users/dudu/Documents/3_Project/8_functional_query`

## Runtime Context

- Primary operating system: macOS.
- Project orchestration: CyHex local app and CyHex task structure.
- Historical code context: Python package/workflow for PxFquery, including perturbation data loading, query indexes, forward/reverse query logic, resolver logic, and LLM-assisted natural-language interpretation.

## Python Runtime

- Default Python environment: `/Users/dudu/Softwares/miniconda/envs/pxfquery`.
- Default command style: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- Use this environment for PxFquery code execution, data analysis, crawling scripts, statistics scripts, LLM/API helper scripts, and manuscript-supporting analysis unless a task explicitly documents why another runtime is required.
- Do not use the base conda environment for project execution except for environment inspection or conda management.
- If a required Python package is missing, a task may install it into the `pxfquery` environment when the package is necessary for that task; the task output should record the package name, install command, and reason.

## Data And Asset Context

- Core historical data include CMAP/LINCS AD perturbation matrices, functional score matrices, compound metadata, cell line metadata, gene metadata, gene sets, query indexes, reports, and manuscript strategy files.
- Large or binary assets should be treated as registered raw materials, not as text context to load casually.
- Current tasks should read only the assets needed for their protocol step and should preserve provenance for reused materials.

## Source Authority

- T-001 digestion outputs define the current interpretation of legacy background, structure, and source priority.
- T-002 migration outputs define which assets were migrated, redacted, or intentionally not migrated.
- The flat asset library is the preferred readable source for migrated legacy content.
- Direct legacy-root reads are exceptional and must be justified by task output.

## Language And Documentation

- Local project explanations may be written in Chinese when that improves maintainability.
- Code package names, filenames, technical identifiers, and manuscript-facing labels may remain in English.
- Persistent project protocol should remain concise and avoid embedding CyHex system internals or old legacy protocol mechanics.

```


### 1.2 Project State Snapshot
### Project State: state.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/state.yaml`

```text
project_id: P-012
name: PxFquery
created: '2026-06-13'
target_delivery: ''
current_phase: development
status: active
focus: 4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review
notes: Entering development phase. Current focus is configuring T-013 under G-005
  for MVP algorithm run-through review; G-006 is reserved for later algorithm version
  development.

```

### Project State: current_state.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/3_project_state/current_state.md`

```text
# Current State — PxFquery

Updated: 2026-06-22

## Project Status

PxFquery is an active CyHex project migrated from legacy functional-query materials. The project is in development, with current focus on `4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review`.

The project currently has no final external deliverable registered in `6_project_deliverable/`. Existing outputs are task-level digestion, review, evidence, and preparation artifacts under each task's `4_artifact/`.

## Active Tasks Needing Human Review Or Continuation

- T-012 `task_genes_bioinformatics_deliverable_catalog`: delivered catalogs/supplements and remains active pending acceptance.
- T-013 `task_mvp_algorithm_run-through_review`: delivered MVP review evidence and remains active pending acceptance or follow-up decision.
- T-014 `task_understand_pxfquery_precomputed_data`: delivered precomputed-data understanding package and remains active pending acceptance.
- T-015 `task_mdpi_submission_package_and_guide`: delivered submission-rule package and remains active pending acceptance.

## Current Rules

- Use CyHex naming for current project governance. Historical Cyber wording in old files is legacy context only.
- Do not modify legacy source roots directly. Prefer migrated assets and task-registered sources.
- Do not treat task-level reports as final project deliverables until a future task explicitly promotes them into `6_project_deliverable/` and registers them.

## CyHex 1.0.23 Task Graph Backfill

Updated: 2026-06-22

Task dependency and artifact lineage edges were backfilled into `1_project_init/2_task_registration/task_graph.yaml` from existing asset registrations, artifact registries, and completion reports. This records current task references only; it does not change task status, task outputs, or delivered artifacts.

```


### 1.3 Current Task Snapshot
### Current Task Meta: meta.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-059
name: forward_query_core_repair_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: 'Create a same-layer replacement for T-048 forward_query_core_m1. Use T-048
  only as a reference incident: it showed that the T-042 forward demo contract cannot
  be satisfied by the currently selected T-046 fixture assets. This task must (1)
  produce and register a task-local forward repair substrate asset, such as a minimal
  M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing
  EGFR/A549/xpr positive demo case without modifying completed T-042/T-043/T-046 artifacts;
  and (2) deliver the forward query core that T-048 was supposed to deliver, including
  package code, no-hit behavior, runnable demo evidence, structured JSON output, and
  a clear provenance report. Downstream tasks should consume this task as the must
  replacement for T-048.'
executor: hybrid
agent_id: AGT-001
config_agent_id: AGT-001
check_agent_id: AGT-001
execute_agent_id: AGT-001
server_id: null
status: active
cyhex_version: 1.2.19
created: '2026-06-24'
started: null
completed: null
notes: 补充要求：这是 T048 的旁路修复/替代交付任务，不是修改 T048，也不是把 T048 标绿。T048 只能作为 reference 错误案例读取，用于理解
  EGFR/A549/xpr 缺口。必须引用 T042 的 API/demo contract、T043 的 fixture/schema、T044 的包骨架、T046
  的 loader API 和 smoke evidence；可参考 T047 hardening 结果。不得修改 upstream done 任务产物；不得使用
  T024-T040 blocked 资产；不得伪造为原始数据。若创建补充 fixture/manifest，必须在本任务内登记为新资产并写明 synthetic/repair
  provenance。验收必须实际运行 forward demo，输出 JSON 可见且格式符合 T042。
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T05:27:56'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: m1_api_contract
  type: document
  source: predecessor
  source_task: T-042
  source_artifact_id: D-001
  origin: T-042/D-001
  registered: '2026-06-24'
  path: 1_asset/m1_api_contract.yaml
  symlink: true
  status: ready
  notes: Contract authority for public API, CLI, JSON output shape, no-hit behavior,
    and error semantics.
  location: local
- id: A-002
  name: m1_demo_cases
  type: document
  source: predecessor
  source_task: T-042
  source_artifact_id: D-002
  origin: T-042/D-002
  registered: '2026-06-24'
  path: 1_asset/m1_demo_cases.yaml
  symlink: true
  status: ready
  notes: Defines required forward demo case EGFR/A549/xpr and pass/fail assertions.
  location: local
- id: A-003
  name: resource_manifest_m1
  type: document
  source: predecessor
  source_task: T-043
  source_artifact_id: D-001
  origin: T-043/D-001
  registered: '2026-06-24'
  path: 1_asset/resource_manifest_m1.yaml
  symlink: true
  status: ready
  notes: Baseline manifest for existing M1 fixture resources; repair must remain task-local.
  location: local
- id: A-004
  name: fixture_package_m1
  type: package
  source: predecessor
  source_task: T-043
  source_artifact_id: D-002
  origin: T-043/D-002
  registered: '2026-06-24'
  path: 1_asset/fixture_package_m1
  symlink: true
  status: ready
  notes: Existing deterministic fixture package to preserve and bridge without modifying
    upstream output.
  location: local
- id: A-005
  name: expected_shapes_keys_columns_m1
  type: table
  source: predecessor
  source_task: T-043
  source_artifact_id: D-003
  origin: T-043/D-003
  registered: '2026-06-24'
  path: 1_asset/expected_shapes_keys_columns_m1.csv
  symlink: true
  status: ready
  notes: Schema and shape reference for loader-compatible repair fixture design.
  location: local
- id: A-006
  name: sample_records_m1
  type: table
  source: predecessor
  source_task: T-043
  source_artifact_id: D-004
  origin: T-043/D-004
  registered: '2026-06-24'
  path: 1_asset/sample_records_m1.csv
  symlink: true
  status: ready
  notes: Traceable sample records and fixture-content context.
  location: local
- id: A-007
  name: package_skeleton_pyproject
  type: code
  source: predecessor
  source_task: T-044
  source_artifact_id: D-001
  origin: T-044/D-001
  registered: '2026-06-24'
  path: 1_asset/package_skeleton_pyproject.toml
  symlink: true
  status: ready
  notes: Package metadata and src-layout base.
  location: local
- id: A-008
  name: package_skeleton_src
  type: package
  source: predecessor
  source_task: T-044
  source_artifact_id: D-002
  origin: T-044/D-002
  registered: '2026-06-24'
  path: 1_asset/package_skeleton_src
  symlink: true
  status: ready
  notes: Package skeleton to copy into task-local working package and extend.
  location: local
- id: A-009
  name: import_smoke_evidence
  type: document
  source: predecessor
  source_task: T-044
  source_artifact_id: D-003
  origin: T-044/D-003
  registered: '2026-06-24'
  path: 1_asset/import_smoke_evidence.txt
  symlink: true
  status: ready
  notes: Import smoke baseline to replicate after implementation.
  location: local
- id: A-010
  name: m1_fixture_loader_code
  type: code
  source: predecessor
  source_task: T-046
  source_artifact_id: D-001
  origin: T-046/D-001
  registered: '2026-06-24'
  path: 1_asset/m1_fixture_loader_code.py
  symlink: true
  status: ready
  notes: Loader implementation that the forward query must use or remain compatible
    with.
  location: local
- id: A-011
  name: m1_loader_api_documentation
  type: document
  source: predecessor
  source_task: T-046
  source_artifact_id: D-002
  origin: T-046/D-002
  registered: '2026-06-24'
  path: 1_asset/m1_loader_api_documentation.md
  symlink: true
  status: ready
  notes: Documents loader classes and stable API expected by downstream query tasks.
  location: local
- id: A-012
  name: smoke_evidence_table
  type: table
  source: predecessor
  source_task: T-046
  source_artifact_id: D-003
  origin: T-046/D-003
  registered: '2026-06-24'
  path: 1_asset/smoke_evidence_table.csv
  symlink: true
  status: ready
  notes: Baseline fixture-loader smoke evidence.
  location: local
- id: A-013
  name: loader_hardening_m1_code
  type: code
  source: predecessor
  source_task: T-047
  source_artifact_id: D-001
  origin: T-047/D-001
  registered: '2026-06-24'
  path: 1_asset/loader_hardening_m1_code.py
  symlink: true
  status: ready
  notes: Optional hardened loader reference; do not use to bypass the T-046 loader
    API boundary.
  location: local
- id: A-014
  name: loader_gap_list
  type: document
  source: predecessor
  source_task: T-047
  source_artifact_id: D-004
  origin: T-047/D-004
  registered: '2026-06-24'
  path: 1_asset/loader_gap_list.md
  symlink: true
  status: ready
  notes: Optional known-gap context for loader compatibility decisions.
  location: local
- id: A-015
  name: t048_blocked_completion_report
  type: document
  source: predecessor
  source_task: T

...[truncated by CyHex prompt assembler: 311 chars omitted]
```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-059 forward_query_core_repair_m1 — Protocol

## Objective

Create a same-layer repair/replacement for T-048 `forward_query_core_m1`. T-048 is only a reference incident showing that the T-042 required forward demo case `EGFR/A549/xpr` cannot be satisfied by the currently selected T-046 fixture assets.

This task must deliver a working M1 forward query core plus a task-local repair substrate, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly supplies the missing positive demo case without modifying completed T-042, T-043, T-044, T-046, or T-047 outputs. The repair substrate must be labeled as synthetic/repair provenance, not as original raw data.

## Position In Project

T-059 replaces T-048 for downstream forward-query work. It does not reopen T-048, mark T-048 as successful, or alter upstream completed artifacts. Downstream tasks should consume T-059 outputs as the authoritative M1 forward-query core repair deliverable.

Because seven predecessor tasks are selected, execution should use the registered handoff-derived assets only. If the executor finds that more predecessor context is needed beyond the registered assets, stop and recommend an intermediate digestion/integration task instead of expanding into broad predecessor reading.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Contract authority for public API, CLI shape, JSON output, no-hit behavior, and error semantics. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Defines the exact required forward demo case and assertions, including `EGFR/A549/xpr`. |
| A-003 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml` | Baseline M1 resource/fixture manifest to preserve compatibility and describe existing substrate boundaries. |
| A-004 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/` | Existing deterministic fixture package that must remain unchanged and should be extended only through a task-local repair substrate. |
| A-005 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Fixture schema and expected structure reference for any repair supplement. |
| A-006 | T-043 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv` | Traceable sample-record context and fixture content reference; useful for documenting the missing positive case. |
| A-007 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml` | Base package metadata and src-layout anchor. |
| A-008 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/` | Base package skeleton to extend with forward-query code. |
| A-009 | T-044 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Prior import-smoke baseline to replicate after implementation. |
| A-010 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Loader implementation that forward query must use or remain compatible with. |
| A-011 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-012 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Evidence that baseline fixture loading worked before the repair. |
| A-013 | T-047 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened loading behavior; not required to replace the T-046 API. |
| A-014 | T-047 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/3_document/loader_gap_list_m1.md` | Optional known-gap context if the executor needs to compare repair behavior with hardening results. |
| A-015 | T-048 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/completion.md` | Reference incident report documenting the EGFR/A549/xpr fixture gap and failed assertion. |

## Execution Steps

1. Stage a task-local working package in `3_execution/` from T-044 package metadata/skeleton, then integrate T-046 loader code or a compatibility-preserving copy of it.
2. Read the T-042 API/demo contract and identify the exact forward output fields, no-hit object, error behavior, and pass/fail assertions that must be satisfied.
3. Confirm from the registered T-043/T-046 context that the baseline fixture lacks the `EGFR/A549/xpr` positive case. Do not treat this confirmation as a reason to modify upstream fixture assets.
4. Cr

...[truncated by CyHex prompt assembler: 5527 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-042
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml
    reason: M1 API/CLI/JSON/no-hit contract authority.
  - id: A-002
    source_task: T-042
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml
    reason: Exact required forward demo case and acceptance assertions.
  - id: A-003
    source_task: T-043
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml
    reason: Baseline M1 manifest and fixture boundary reference.
  - id: A-004
    source_task: T-043
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/
    reason: Existing deterministic fixture package to preserve and bridge without mutation.
  - id: A-005
    source_task: T-043
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv
    reason: Schema/shape reference for repair fixture compatibility.
  - id: A-006
    source_task: T-043
    source_artifact_id: D-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv
    reason: Sample-record context for documenting baseline fixture contents.
  - id: A-007
    source_task: T-044
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml
    reason: Base package metadata and src-layout.
  - id: A-008
    source_task: T-044
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/
    reason: Package skeleton to extend with forward-query implementation.
  - id: A-009
    source_task: T-044
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt
    reason: Import smoke baseline to replicate after implementation.
  - id: A-010
    source_task: T-046
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py
    reason: Loader implementation required for forward-query data access compatibility.
  - id: A-011
    source_task: T-046
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md
    reason: Loader API reference for correct integration.
  - id: A-012
    source_task: T-046
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
    reason: Loader smoke evidence baseline.
  - id: A-015
    source_task: T-048
    source_artifact_id: completion_report
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/completion.md
    reason: Blocked incident reference documenting the EGFR/A549/xpr fixture gap.
optional:
  - id: A-013
    source_task: T-047
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/1_code/loader_hardening_m1.py
    reason: Optional hardened loader implementation reference.
  - id: A-014
    source_task: T-047
    source_artifact_id: D-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/3_document/loader_gap_list_m1.md
    reason: Optional known-gap context for loader compatibility decisions.
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
  - path: T024-T040
    reason: blocked predecessor assets are not valid authorities or inputs for this repair task
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_

...[truncated by CyHex prompt assembler: 1147 chars omitted]
```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task ID: T-059 | Name: forward_query_core_repair_m1
Status: active | Executor: hybrid
Objective: Create a same-layer replacement for T-048 forward_query_core_m1. Use T-048 only as a reference incident: it showed that the T-042 forward demo contract cannot be satisfied by the currently selected T-046 fixture assets. This task must (1) produce and register a task-local forward repair substrate asset, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing EGFR/A549/xpr positive demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver the forward query core that T-048 was supposed to deliver, including package code, no-hit behavior, runnable demo evidence, structured JSON output, and a clear provenance report. Downstream tasks should consume this task as the must replacement for T-048.
Notes / User Natural-Language Intent: 补充要求：这是 T048 的旁路修复/替代交付任务，不是修改 T048，也不是把 T048 标绿。T048 只能作为 reference 错误案例读取，用于理解 EGFR/A549/xpr 缺口。必须引用 T042 的 API/demo contract、T043 的 fixture/schema、T044 的包骨架、T046 的 loader API 和 smoke evidence；可参考 T047 hardening 结果。不得修改 upstream done 任务产物；不得使用 T024-T040 blocked 资产；不得伪造为原始数据。若创建补充 fixture/manifest，必须在本任务内登记为新资产并写明 synthetic/repair provenance。验收必须实际运行 forward demo，输出 JSON 可见且格式符合 T042。
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1

## 3. Hard Scope Boundary

Allowed reads by default:
- CyHex protocol.
- Project protocol/state listed above.
- Current task files listed above.
- Registered local asset paths only if the preflight summary or protocol quality check requires content inspection.

Selected predecessor artifacts are allowed only through the current task's `1_asset/registration.yaml`.

Do not scan arbitrary predecessor task folders.
Do not browse unrelated task material.
Do not scan `2_project_asset/` unless this task phase is digestion.
If this is development/translation and a needed input only exists in `2_project_asset/`, stop and require a predecessor digestion task or corrected registration.
Do not read future-stage prompts from `2_protocol/0_prompt/`:
- Do not read `*_action_prompt.md`
- Do not read `*_delivery_prompt.md`
- Do not read any prompt for a stage after checking

## 4. Backend Asset Preflight

CyHex has already performed mechanical asset checks before generating this prompt.

Do not repeat `ls`/full-path scanning for every registered asset when this summary is clean. Use the summary first.

```yaml
asset_preflight:
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: development
  project_asset_access: forbidden
  zero_assets: false
  total_assets: 15
  symlink_sync:
    checked: 15
    linked: 15
    skipped: 0
    changed: false
  counts:
    ok: 15
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: m1_api_contract
    required: true
    status: ok
    path: 1_asset/m1_api_contract.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml
    reason: local path exists
  - id: A-002
    name: m1_demo_cases
    required: true
    status: ok
    path: 1_asset/m1_demo_cases.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml
    reason: local path exists
  - id: A-003
    name: resource_manifest_m1
    required: true
    status: ok
    path: 1_asset/resource_manifest_m1.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml
    reason: local path exists
  - id: A-004
    name: fixture_package_m1
    required: true
    status: ok
    path: 1_asset/fixture_package_m1
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1
    reason: local path exists
  - id: A-005
    name: expected_shapes_keys_columns_m1
    required: true
    status: ok
    path: 1_asset/expected_shapes_keys_columns_m1.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv
    reason: local path exists
  - id: A-006
    name: sample_records_m1
    required: true
    status: ok
    path: 1_asset/sample_records_m1.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv
    reason: local path exists
  - id: A-007
    name: package_skeleton_pyproject
    required: true
    status: ok
    path: 1_asset/package_skeleton_pyproject.toml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml
    reason: local path exists
  - id: A-008
    name: package_skeleton_src
    required: true
    status: ok
    path: 1_asset/package_skeleton_src
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery
    reason: local path exists
  - id: A-009
    name: import_smoke_evidence
    required: true
    status: ok
    path: 1_asset/import_smoke_evidence.txt
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt
    reason: local path exists
  - id: A-010
    name: m1_fixture_loader_code
    required: true
    status: ok
    path: 1_asset/m1_fixture_loader_code.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py
    reason: local path exists
  - id: A-011
    name: m1_loader_api_documentation
    required: true
    status: ok
    path: 1_asset/m1_loader_api_documentation.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md
    reason: local path exists
  - id: A-012
    name: smoke_evidence_table
    required: true
    status: ok
    path: 1_asset/smoke_evidence_table.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
    reason: local path exists
  - id: A-013
    name: loader_hardening_m1_code
    required: true
    status: ok
    path: 1_asset/loader_hardening_m1_code.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/1_code/loader_hardening_m1.py
    reason: local path exists
  - id: A-014
    name: loader_gap_list
    required: true
    status: ok
    path: 1_asset/loader_gap_list.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/3_document/loader_gap_list_m1.md
    reason: local path exists
  - id: A-015
    name: t048_blocked_completion_report
    required: true
    status: ok
    path: 1_asset/t048_blocked_completion_report.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/completion.md
    reason: local path exists
```

Interpretation:
- `ok`: no deeper asset-path inspection needed by default.
- `planned`: acceptable only if protocol explicitly says execution will acquire/search it.
- `remote`: acceptable only if execution has tool/network ability and protocol names the acquisition method.
- `missing`, `empty_file`, `empty_dir`, `forbidden_scope`: anomaly. Enter Yellow repair or Red block.
- `zero_assets: true`: acceptable only for a no-input task, a pure code/UI task based on current repo, or a task whose protocol explicitly starts with permitted web/search acquisition. Otherwise block or repair.

## 5. Default Mode: Green Check

Start in Green Check mode.

In Green Check:
1. Read required files.
2. Trust clean mechanical asset preflight unless protocol/registry text contradicts it.
3. Do not inspect every asset content.
4. Check whether the configuration is executable.
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md`.
- Do not generate downstream prompts. CyHex backend will generate the execution prompt only after check approval.

When repairing an asset anomaly, inspect only the specific selected predecessor artifact registry/handoff/report needed to correct the path. Do not scan whole predecessor folders.

## 7. Red Block

Enter Red Block when execution would waste time or fake success.

Block if:
- A required local asset is missing/empty and cannot be repaired from selected records.
- A development/translation task requires raw `2_project_asset/` access.
- `zero_assets: true` but the task clearly needs input assets and no permitted acquisition step exists.
- Protocol lacks concrete steps or deliverables and cannot be repaired from current information.
- The task needs a capability not available to execution AI.
- The current protocol, asset registry, and asset rules cannot be made mutually consistent.

In Red Block:
- Do not execute the task.
- Do not write deliverables.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/blocked.md` with exact blocker, evidence, and required fix.
- Do not claim checking passed.

## 8. Execution Plan Quality Gate

The plan is passable only if:
1. It has about 4-8 concrete execution steps unless the task is genuinely tiny.
2. Each step names an operation, input, and expected intermediate or final output.
3. It includes a conservative first move: smoke test, demo subset, dry run, small sample, or UI sanity check where applicable.
4. It considers compute/time/network/API cost.
5. It defines stop conditions before expensive or destructive operations.
6. Deliverables are concrete: expected file type, likely path, and acceptance signal.
7. It does not ask execution AI to rediscover all predecessor context.
8. It does not allow final reusable outputs to remain only in `3_execution/`.

If these are not true, repair protocol and handoff before passing.

## 9. Required handoff_check_before_exec.md Shape

Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-059 forward_query_core_repair_m1

## Check Verdict
green_check | yellow_repair

## CyHex Boundaries
- Task path:
- Allowed write dirs:
- Forbidden dirs:
- Required registry:
- Must stop if:

## Objective Restatement
...

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|

## Execution Strategy
1. ...
2. ...
3. ...

## Conservative Execution Advice
- Start with:
- Smoke/demo command or method:
- Full run only after:
- Cost/time risk:
- Checkpoint advice:

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|

## Failure / Stop Conditions
- ...

## Notes For Delivery QA
- ...
```

Do not write `green_check` if you had to block. Use `yellow_repair` if you repaired anything before passing.

## 10. Final Response

Output a concise checking report with exactly these sections:

### 一、我准备如何遵守 CyHex
- 本 task 实际路径
- 允许写入目录
- 禁止目录/行为
- 执行阶段必须先读的文件
- 触发 `5_report/blocked.md` 的条件

### 二、我准备如何达成任务目标
- 用自己的话复述目标
- 4-8 步执行策略
- 保守起步/试跑建议
- 预期交付物和验收信号

### 三、检查与修复
- 资产预检结论
- 计划质量结论
- 修复了什么
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md` 是否已写
- 是否避免调用下游 prompt 生成
- 剩余阻断

End with exactly one of:
- `检查完成。请确认：检查通过，开始执行 / 提出修改意见`
- `检查发现问题，无法进入执行。需要补充：...`

## 11. Hard Stops
- 不执行任务本体
- 不写 4_artifact/ 交付物
- 不把 task 标记为 done
- 不跳过人类检查确认点
