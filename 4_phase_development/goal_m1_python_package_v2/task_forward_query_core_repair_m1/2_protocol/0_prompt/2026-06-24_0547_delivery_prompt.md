# Delivery QA Prompt
Generated: 2026-06-24 05:47

## 0. Role

You are the CyHex delivery QA agent for one task.

Your job is to confirm whether the execution output is deliverable, repair delivery metadata/placement/reporting when safe, and prepare a clean handoff for future AI tasks.

You are not the execution agent. Do not redo the task. Do not expand research scope. Do not scan unrelated folders.

## 1. Assembled Delivery Context Snapshot

CyHex has already assembled the project protocol, project state, current task contract, asset registry, artifact registry, completion report, delivery QA note, and handoff records below. Use this snapshot as your default delivery context.

Do not re-read these files in green-pass mode. Open the source paths only if the snapshot is missing, truncated at the exact section you need, or internally contradictory.

You may still call `GET http://localhost:47291/api/version` once to confirm CyHex is running. You do not need to read `cyhex_protocol.md` unless this prompt is missing a delivery rule you must apply.

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


### 1.3 Current Task And Delivery Snapshot
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
status: done
cyhex_version: 1.2.19
created: '2026-06-24'
started: null
completed: '2026-06-24'
notes: 补充要求：这是 T048 的旁路修复/替代交付任务，不是修改 T048，也不是把 T048 标绿。T048 只能作为 reference 错误案例读取，用于理解
  EGFR/A549/xpr 缺口。必须引用 T042 的 API/demo contract、T043 的 fixture/schema、T044 的包骨架、T046
  的 loader API 和 smoke evidence；可参考 T047 hardening 结果。不得修改 upstream done 任务产物；不得使用
  T024-T040 blocked 资产；不得伪造为原始数据。若创建补充 fixture/manifest，必须在本任务内登记为新资产并写明 synthetic/repair
  provenance。验收必须实际运行 forward demo，输出 JSON 可见且格式符合 T042。
fast_pass_permission: green
sub_status: ''
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:31:05'
auto_recovery:
  deliver:
    source_session_id: cli_809925f3d05b
    attempts: 1
    last_attempt_at: '2026-06-24T05:45:24'
fast_pass_accepted: true
fast_pass_accepted_at: '2026-06-24T05:45:35'

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

### Current Task Protocol: protocol.md
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
4. Create a task-local repair substrate under `4_artifact/2_persist/`, such as `forward_repair_manifest_m1_1.yaml` plus `forward_repair_fixture_m1_1/`, that adds the minimal positive demo case needed for T-042. Mark the substrate as `synthetic_repair` or equivalent provenance and explain that it is a contract bridge, not original raw data.
5. Implement the forward query core through the loader-compatible data access layer. Do not write a private ad hoc parser that bypasses the loader contract unless a clear compatibility wrapper is documented.
6. Implement required no-hit behavior and structured JSON output exactly as T-042 specifies.
7. Run the forward demo for the positive `EGFR/A549/xpr` case and at least one no-hit case. Save visible structured JSON evidence in `4_artifact/2_persist/`.
8. Produce an assertion table showing pass/fail for T-042 forward-demo requirements, package import smoke, loader compatibility, positive-hit behavior, no-hit behavior, and provenance labeling.
9. Write a concise provenance/report document explaining how T-059 replaces T-048, what was synthetic/repair, what remained upstream, and why no upstream completed artifacts were modified.

## Constraints

- Treat T-042 as the contract authority for forward API/demo behavior and JSON shape.
- Treat T-043/T-046 as the baseline fixture and loader boundary; extend through a task-local repair substrate only.
- Treat T-044 as the package skeleton source; keep package name `pxfquery` and src-layout conventions.
- T-047 may be used only as optional hardening reference.
- T-048 may be used only as a blocked incident reference; do not reuse its unaccepted code or evidence as authoritative deliverables.
- The repair substrate must clearly state synthetic/repair provenance and must not be represented as original LINCS/raw project data.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Use the configured Python environment unless a documented package/runtime issue requires a narrow exception: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.

## Forbidden

- Do not modify T-042, T-043, T-044, T-046, T-047, or T-048 task outputs.
- Do not mark T-048 done or green.
- Do not use T024-T040 blocked assets.
- Do not read or use project-level raw assets under `2_project_asset/`.
- Do not claim biological ranking validity or full-resource coverage from the minimal repair fixture.
- Do not perform web search for this task.

## Web Search Allowance

Allowed: no

Reason: The task is a local package repair and fixture-bridge implementation. All needed contract, fixture, skeleton, loader, and incident context is available from selected predecessor handoffs and registered artifacts.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Task-local package metadata and implemented package source | `4_artifact/1_package/` | yes |
| Repair fixture/manifest or con

...[truncated by CyHex prompt assembler: 2527 chars omitted]
```

### Current Task Asset Rule: asset_rule.yaml
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
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/4_artifact/
    reason: T-048 produced no accepted registry artifacts and must be used only as an incident reference
output:
  - path: 4_artifact/1_package/
    type: package
  - path: 4_artifact/2_persist/forward_repair_manifest_m1_1.yaml
    type: manifest
  - path: 4_artifact/2_persist/forward_repair_fixture_m1_1/
    type: package
  - path: 4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json
    type: json
  - path: 4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json
    type: json
  - path: 4_artifact/5_table/forward_query_contract_assertions_v20260624.csv
    type: table
  - path: 4_artifact/3_document/forward_query_core_repair_report_v20260624.md
    type: document
  - path: 4_artifact/3_document/execution_report_v20260624.html
    type: report
  - path: 4_artifact/3_document/result_report_v20260624.html
    type: report
  - path: 4_artifact/registry.yaml
    type: registry
modifiable:
  - 3_executio

...[truncated by CyHex prompt assembler: 147 chars omitted]
```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-059 forward_query_core_repair_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1`
- Allowed write dirs: task-local `3_execution/`, `4_artifact/`, and `5_report/`
- Forbidden dirs: predecessor task output directories; `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/`; T024-T040 blocked assets; T-048 `4_artifact/`; any future-stage prompt files under `2_protocol/0_prompt/`
- Required registry: `1_asset/registration.yaml`; accepted reusable outputs must also be registered in `4_artifact/registry.yaml`
- Must stop if: T-042 JSON/API semantics are ambiguous after reading A-001/A-002; satisfying the contract requires mutating T-042/T-043/T-044/T-046/T-047/T-048 outputs; raw `2_project_asset/` or T024-T040 inputs are needed; the repair substrate cannot be transparently labeled synthetic/repair; more broad predecessor context is needed than the registered assets provide

## Objective Restatement
Deliver the same-layer replacement that T-048 failed to deliver: a working M1 forward-query package plus a task-local repair substrate that fills the required `EGFR/A549/xpr` positive demo case. T-048 is only an incident reference. The repair must preserve upstream completed artifacts, use or remain compatible with the T-046 loader boundary, emit T-042-shaped structured JSON for both positive-hit and no-hit cases, and document the synthetic/repair provenance clearly.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | T-042 authority for API, CLI, JSON shape, no-hit behavior, and errors | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | T-042 forward demo case and assertions, including `EGFR/A549/xpr` | ok |
| A-003 | `1_asset/resource_manifest_m1.yaml` | Baseline M1 resource/fixture boundary | ok |
| A-004 | `1_asset/fixture_package_m1` | Existing deterministic fixture package to preserve and bridge without mutation | ok |
| A-005 | `1_asset/expected_shapes_keys_columns_m1.csv` | Schema/shape reference for repair fixture compatibility | ok |
| A-006 | `1_asset/sample_records_m1.csv` | Baseline fixture sample-record context | ok |
| A-007 | `1_asset/package_skeleton_pyproject.toml` | Base package metadata and src-layout anchor | ok |
| A-008 | `1_asset/package_skeleton_src` | Package skeleton to extend with forward-query implementation | ok |
| A-009 | `1_asset/import_smoke_evidence.txt` | Prior import-smoke baseline to replicate | ok |
| A-010 | `1_asset/m1_fixture_loader_code.py` | T-046 loader implementation for compatible data access | ok |
| A-011 | `1_asset/m1_loader_api_documentation.md` | Loader API reference for integration | ok |
| A-012 | `1_asset/smoke_evidence_table.csv` | Baseline loader smoke evidence | ok |
| A-013 | `1_asset/loader_hardening_m1_code.py` | Optional T-047 hardening reference only | ok |
| A-014 | `1_asset/loader_gap_list.md` | Optional T-047 known-gap context only | ok |
| A-015 | `1_asset/t048_blocked_completion_report.md` | T-048 incident reference for the missing positive case | ok |

## Execution Strategy
1. Stage a working package in `3_execution/` from A-007/A-008 and add the T-046 loader code or a compatibility-preserving copy from A-010, guided by A-011.
2. Read A-001/A-002 first and extract the exact forward-query callable/CLI contract, JSON fields, no-hit shape, and pass/fail assertions.
3. Confirm the baseline fixture boundary from A-003/A-004/A-005/A-006/A-012 and the T-048 incident from A-015, only enough to justify the missing `EGFR/A549/xpr` repair case.
4. Create a task-local repair substrate in `4_artifact/2_persist/`, preferably `forward_repair_manifest_m1_1.yaml` plus `forward_repair_fixture_m1_1/`, labeled as `synthetic_repair` or equivalent and explicitly not original LINCS/raw data.
5. Implement forward-query package code in the staged package, preserving T-046 loader API compatibility and avoiding private ad hoc parsing unless wrapped and documented as compatibility-preserving.
6. Run a conservative smoke sequence: import smoke, loader compatibility check, positive `EGFR/A549/xpr` demo, and one no-hit demo.
7. Save visible JSON evidence and assertion evidence into `4_artifact/` only after the demo outputs satisfy T-042 shape and behavior.
8. Write provenance/report documents and `4_artifact/registry.yaml`, making clear that T-059 replaces T-048 for downstream use without modifying upstream artifacts.

## Conservative Execution Advice
- Start with: a read-only contract extraction from A-001/A-002 and a minimal import/loader smoke in `3_execution/`
- Smoke/demo command or method: use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`; first import `pxfquery`, then invoke the forward demo for `perturbation=EGFR`, `cell_line=A549`, `matrix_type=xpr`, then run one deliberately unmatched no-hit query
- Full run only after: the staged package imports, the loader-compatible fixture objects can be loaded, and the repair manifest/fixture provenance is explicit
- Cost/time risk: low local CPU/runtime cost; no network or web search is allowed; avoid broad predecessor scanning because it is the main scope risk
- Checkpoint advice: keep temporary scripts/logs in `3_execution/`; only copy accepted package, fixture, evidence, tables, reports, and registry into `4_artifact/`

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Implemented package metadata/source | `4_artifact/1_package/` | Package imports and forward-query API/CLI behavior match T-042 |
| Repair substrate manifest | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Documents minimal `EGFR/A549/xpr` bridge and synthetic/repair provenance |
| Repair fixture package | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Loader-compatible supplement present and not represented as original raw data |
| Positive demo JSON | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Visible structured JSON conforms to T-042 and reports found/positive result |
| No-hit demo JSON | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Visible structured JSON conforms to T-042 no-hit behavior without crash |
| Contract assertion table | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Pass/fail rows cover import, loader compatibility, positive hit, no-hit, JSON shape, and provenance |
| Provenance/replacement report | `4_artifact/3_document/forward_query_core_repair_report_v20260624.md` | Explains T-059 replacement role, T-048 incident use, repair provenance, and untouched upstream artifacts |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Human-readable execution record exists |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Human-readable result summa

...[truncated by CyHex prompt assembler: 1479 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/registry.yaml`

```text
artifacts:
- id: D-001
  name: forward_query_package_m1_repair
  type: package
  path: 4_artifact/1_package
  status: ready
  provenance: T-044 skeleton plus T-046 loader-compatible forward implementation
  role: core_package
  identity: T-059 replacement forward-query package
  produced_by: T-059
  description: Implemented M1 forward query package with API/CLI behavior, no-hit handling, and T-046 loader-compatible access.
  usable_by: downstream M1 package and forward-query tasks replacing T-048
  core: true
  lineage_anchor: T-044 package skeleton; T-046 loader API; T-059 repair substrate
  stars: 5
- id: D-002
  name: forward_repair_manifest_m1_1
  type: manifest
  path: 4_artifact/2_persist/forward_repair_manifest_m1_1.yaml
  status: ready
  provenance: T-059 synthetic_repair contract bridge
  role: repair_manifest
  identity: synthetic repair manifest for EGFR/A549/xpr contract bridge
  produced_by: T-059
  description: Documents the task-local M1.1 repair substrate and its synthetic_repair provenance.
  usable_by: downstream tasks that need to understand or load the T-059 repair fixture
  core: true
  lineage_anchor: T-042 demo contract; T-043 fixture boundary; T-059 synthetic_repair
  stars: 5
- id: D-003
  name: forward_repair_fixture_m1_1
  type: package
  path: 4_artifact/2_persist/forward_repair_fixture_m1_1
  status: ready
  provenance: T-043 fixture copied task-locally with one synthetic_repair EGFR/A549/xpr
    row
  role: repair_fixture
  identity: task-local M1.1 fixture supplement
  produced_by: T-059
  description: Loader-compatible fixture copy with the minimal synthetic_repair EGFR/A549/xpr positive row required by the T-042 demo contract.
  usable_by: downstream runnable demos and tests for the T-059 forward-query core
  core: true
  lineage_anchor: T-043 fixture; T-046 loader compatibility; T-059 synthetic_repair
  stars: 5
- id: D-004
  name: forward_query_positive_demo_evidence
  type: json
  path: 4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json
  status: ready
  provenance: T-059 validation
  role: positive_demo_evidence
  identity: EGFR/A549/xpr forward demo JSON
  produced_by: T-059
  description: Structured JSON evidence showing the required positive forward demo returns found=true.
  usable_by: acceptance checks and downstream smoke tests
  core: true
  lineage_anchor: T-042 forward demo contract; T-059 validation
  stars: 5
- id: D-005
  name: forward_query_no_hit_evidence
  type: json
  path: 4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json
  status: ready
  provenance: T-059 validation
  role: no_hit_evidence
  identity: structured no-hit forward query JSON
  produced_by: T-059
  description: Structured JSON evidence for no-hit behavior without traceback.
  usable_by: acceptance checks and downstream error-behavior tests
  core: true
  lineage_anchor: T-042 no-hit contract; T-059 validation
  stars: 5
- id: D-006
  name: forward_query_contract_assertions
  type: table
  path: 4_artifact/5_table/forward_query_contract_assertions_v20260624.csv
  status: ready
  provenance: T-059 validation
  role: assertion_table
  identity: T-042 contract assertion results for T-059
  produced_by: T-059
  description: Pass/fail assertion table covering import, loader compatibility, positive hit, no-hit, JSON shape, CLI, provenance, and boundary checks.
  usable_by: reviewers and downstream validation tasks
  core: true
  lineage_anchor: T-042 contract; T-046 loader API; T-059 validation
  stars: 5
- id: D-007
  name: forward_query_core_repair_report
  type: document
  path: 4_artifact/3_document/forward_query_core_repair_report_v20260624.md
  status: ready
  provenance: T-059 report
  role: provenance_report
  identity: repair and replacement report
  produced_by: T-059
  description: Explains how T-059 replaces T-048, what was synthetic repair, what remained upstream, and the limits of the bridge fixture.
  usable_by: future planning, handoff, and provenance review
  core: true
  lineage_anchor: T-048 incident; T-059 delivery
  stars: 5
- id: D-008
  name: execution_report
  type: report
  path: 4_artifact/3_document/execution_report_v20260624.html
  status: ready
  provenance: T-059 report
  role: human_execution_report
  identity: human-readable execution record
  produced_by: T-059
  description: HTML execution summary listing implementation steps and validation checks.
  usable_by: human review and audit
  core: false
  lineage_anchor: T-059 validation
  stars: 3
- id: D-009
  name: result_report
  type: report
  path: 4_artifact/3_document/result_report_v20260624.html
  status: ready
  provenance: T-059 report
  role: human_result_report
  identity: human-readable result summary
  produced_by: T-059
  description: HTML result summary for the T-059 replacement deliverable and its contract-bridge limitation.
  usable_by: human review and acceptance
  core: false
  lineage_anchor: T-059 result summary
  stars: 3

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/completion.md`

```text
# Completion

Status: completed

Completed: 2026-06-24

T-059 delivered the same-layer repair/replacement for T-048. The package, repair substrate, positive/no-hit JSON evidence, assertion table, reports, and artifact registry were produced under the T-059 task directory.

## Validation

- Package import: PASS
- T-046 loader-compatible repair fixture load: PASS
- Positive forward demo `EGFR/A549/xpr`: PASS (`found=true`)
- No-hit forward demo: PASS (structured `PerturbationNotFound` JSON)
- CLI JSON output: PASS
- Synthetic/repair provenance labeling: PASS

Failed checks: 0

## Deliverables

- `4_artifact/1_package/`
- `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml`
- `4_artifact/2_persist/forward_repair_fixture_m1_1/`
- `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json`
- `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json`
- `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv`
- `4_artifact/3_document/forward_query_core_repair_report_v20260624.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`

## Boundary Statement

No predecessor task outputs were modified. No project-level raw assets under `2_project_asset/` and no T024-T040 blocked assets were used. The added EGFR/A549/xpr row is a task-local `synthetic_repair` contract bridge and is not original raw data or biological evidence.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/5_report/delivery_qa.md`

```text
# Delivery QA: T-059 forward_query_core_repair_m1

## Verdict

yellow_repair

## Checks Performed

- Confirmed promised deliverables are present under `4_artifact/` and reasonably accounted for by the artifact registry and completion report.
- Confirmed `4_artifact/registry.yaml` exists and registers all accepted reusable deliverables.
- Confirmed all registry paths exist.
- Confirmed accepted reusable outputs are under `4_artifact/`, not only under `3_execution/`.
- Confirmed `3_execution/` contains working package state, a runner script, and CLI stdout evidence rather than unregistered final-only outputs.
- Confirmed `5_report/completion.md` matches registry and actual delivered paths.
- Confirmed required HTML reports exist and are non-empty:
  - `4_artifact/3_document/execution_report_v20260624.html`
  - `4_artifact/3_document/result_report_v20260624.html`
- Spot-checked HTML report summaries for useful human review content and consistency with completion claims.
- Confirmed task-local handoff information is now sufficient for future AI tasks.

## Repairs Made

- Added downstream-use metadata to `4_artifact/registry.yaml`, including roles, identities, descriptions, reuse guidance, lineage anchors, core flags, and stars.
- Created `5_report/handoff_ai_use.md` for future config/check/execute AI handoff.
- Created this delivery QA report.

## Remaining Issues

None requiring execute revision. This QA did not reopen core code, fixture contents, JSON evidence, or analysis logic because green-pass structure checks did not trigger a red-return condition.

## Execute Revision Required

no

## Next Action

human_acceptance

```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: development
- ID: T-059 | Name: forward_query_core_repair_m1
- Objective: Create a same-layer replacement for T-048 forward_query_core_m1. Use T-048 only as a reference incident: it showed that the T-042 forward demo contract cannot be satisfied by the currently selected T-046 fixture assets. This task must (1) produce and register a task-local forward repair substrate asset, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing EGFR/A549/xpr positive demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver the forward query core that T-048 was supposed to deliver, including package code, no-hit behavior, runnable demo evidence, structured JSON output, and a clear provenance report. Downstream tasks should consume this task as the must replacement for T-048.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1`

The only allowed outside-task reads are the CyHex protocol and project protocol files listed above.

Do not scan predecessor tasks.
Do not scan `2_project_asset/`.
Do not open raw input assets by default.
Do not read arbitrary project folders.
Do not read prompts from `2_protocol/0_prompt/` unless a delivery anomaly specifically requires checking what execution was told. In green-pass mode, do not read config/check/execute prompt files.

If you believe outside-task information is required, stop expansion and record it in `5_report/delivery_qa.md` as a blocker or uncertainty.

## 4. Default Mode: Lightweight Confirmation

Start in Green-pass mode.

Check only whether the delivery structure is internally consistent:

1. `protocol.md` promised deliverables are present or reasonably accounted for.
2. `4_artifact/registry.yaml` exists and registers every accepted/reusable deliverable.
3. Registry paths actually exist.
4. Accepted/reusable outputs are under `4_artifact/`, not only under `3_execution/`.
5. `3_execution/` contains only scripts, temporary files, logs, checkpoints, or resumable job state.
6. `completion.md` matches registry and actual files.
7. Required HTML reports exist:
   - `4_artifact/3_document/execution_report_v20260624.html`
   - `4_artifact/3_document/result_report_v20260624.html`
8. HTML reports are useful for human review and consistent with registry/completion.
9. There is enough handoff information for future AI tasks.

If all checks pass, do not open artifact contents. Only make small metadata/reporting repairs if needed.

## 5. Escalation Triggers

Escalate from Green-pass to Yellow-repair or Red-return only if you find evidence of a problem.

Escalate when any of these occur:

- `completion.md` claims success but registry is empty or missing major outputs.
- A protocol-required deliverable is missing.
- Registry path does not exist.
- Registry describes a reusable/accepted output located only under `3_execution/`.
- HTML reports are missing, empty, or inconsistent with actual deliverables.
- Execution report shows failed commands, interrupted execution, or skipped required steps but completion claims success.
- Output descriptions are too vague for downstream reuse.
- A file appears to be a final result but is not registered.
- The task depends on outside information not authorized by protocol/assets.

## 6. Yellow Repair Permissions

If the execution appears substantively valid but delivery structure is flawed, you may repair delivery packaging only.

Allowed repairs:

1. Move or copy accepted/reusable outputs from `3_execution/` into the correct `4_artifact/` subfolder.
2. Update `4_artifact/registry.yaml`.
3. Add or fix registry fields:
   - `id`
   - `name`
   - `path`
   - `type`
   - `role`
   - `identity`
   - `produced_by`
   - `description`
   - `usable_by`
   - `core`
   - `lineage_anchor`
   - `stars`
4. Create or revise:
   - `5_report/completion.md`
   - `5_report/handoff_ai_use.md`
   - `5_report/delivery_qa.md`
5. Create or revise the two human-readable HTML reports:
   - `4_artifact/3_document/execution_report_v20260624.html`
   - `4_artifact/3_document/result_report_v20260624.html`

Do not modify core deliverable logic, code, data, analysis results, or model outputs.

## 7. Red Return Rules

Return to execution instead of repairing if:

- Required work was not actually executed.
- Core output is missing.
- Tests failed and the failure affects acceptance.
- The task produced placeholder files instead of real outputs.
- You cannot verify execution truthfulness from available task-local evidence.
- Fixing the issue would require rerunning analysis, changing code, changing data, or opening unauthorized outside-task files.

In Red-return mode:

1. Do not mark the task deliverable.
2. Do not fabricate missing reports.
3. Write `5_report/delivery_qa.md` explaining the failure.
4. State exactly what execute revision must do next.

## 8. Registry Star Guidance

Use `stars` to indicate downstream importance:

- `5`: core deliverable, must be considered by downstream tasks.
- `4`: important support artifact, usually useful downstream.
- `3`: useful evidence or report, read when relevant.
- `2`: process support, mostly for audit/reproduction.
- `1`: low-level log, temporary evidence, or bookkeeping.

If a file should not be used downstream, do not over-rate it.

## 9. Required Output Files

At the end of delivery QA, ensure these files exist unless Red-return makes that inappropriate:

1. `4_artifact/registry.yaml`
2. `5_report/completion.md`
3. `5_report/handoff_ai_use.md`
4. `5_report/delivery_qa.md`
5. `4_artifact/3_document/execution_report_v20260624.html`
6. `4_artifact/3_document/result_report_v20260624.html`

## 10. handoff_ai_use.md Required Shape

Write `5_report/handoff_ai_use.md` in this structure:

```md
# AI Handoff: T-059 forward_query_core_repair_m1

## Task Goal
...

## What Was Delivered
...

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|

## Supporting Artifacts
...

## Downstream Use
...

## Known Limits / Risks
...

## Do Not Read / Do Not Reuse
...

## Recommended Next Reads
1. ...
2. ...
```

Keep it concise. This file is for future config/check/execute AI, not for human presentation.

## 11. delivery_qa.md Required Shape

Write `5_report/delivery_qa.md` in this structure:

```md
# Delivery QA: T-059 forward_query_core_repair_m1

## Verdict
green_pass | yellow_repair | red_return

## Checks Performed
...

## Repairs Made
...

## Remaining Issues
...

## Execute Revision Required
yes | no

## Next Action
human_acceptance | execute_revision | blocked
```

## 12. Final Response

Return a concise Chinese report:

```md
### 交付质检结论
Verdict: green_pass | yellow_repair | red_return

### 已确认
- ...

### 已修复
- ...

### 仍需处理
- ...

### 下一步
human_acceptance | execute_revision | blocked
```

Do not claim success if the task needs execute revision.
