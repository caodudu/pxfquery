# Execution Prompt
Generated: 2026-06-24 05:30

## 0. Role

You are the CyHex execution agent for one task.

Your job is to execute the approved task plan, produce all required deliverables, and record truthful evidence.

You are not the configuration agent.
You are not the checking agent.
Do not rediscover predecessor context.
Do not scan unrelated project folders.
Do not revise the task plan unless execution is impossible.

## 1. Assembled Execution Context Snapshot

CyHex has already assembled the project protocol, project state, current task contract, asset registry, asset rules, check handoff, execution handoff, artifact registry, and completion/delivery notes below. Use this snapshot as your default execution context.

Do not re-read these files before starting execution unless the snapshot is missing, truncated at the exact section you need, or internally contradictory.

You may still call `GET http://localhost:47291/api/version` once to confirm CyHex is running. You do not need to read `cyhex_protocol.md` unless this prompt is missing an execution rule you must apply.

If you need profile secrets, proxy settings, or account configuration, read `~/.cyhex/profile.yaml` only at the moment the relevant tool requires it.

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-060
name: reverse_query_core_repair_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: 'Create a same-layer replacement for T-049 reverse_query_core_m1. Use T-049
  only as a reference incident: it showed that the T-042 reverse demo contract cannot
  be satisfied by the currently selected T-046 fixture assets because the required
  suppress term HALLMARK_MYC_TARGETS_V1 is absent and the selected assets did not
  include a usable fixture package/manifest. This task must (1) produce and register
  a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest
  or contract-bridge supplement, that honestly fills the missing reverse positive
  demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver
  the reverse query core that T-049 was supposed to deliver, including package code,
  deterministic ranking/scoring, no-hit/error behavior, runnable demo evidence, structured
  JSON output, and a clear provenance report. Downstream tasks should consume this
  task as the must replacement for T-049.'
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
notes: 补充要求：这是 T049 的旁路修复/替代交付任务，不是修改 T049，也不是把 T049 标绿。T049 只能作为 reference 错误案例读取，用于理解
  HALLMARK_MYC_TARGETS_V1 / fixture package 缺口。必须引用 T042 的 API/demo contract、T043
  的 fixture/schema、T044 的包骨架、T046 的 loader API 和 smoke evidence；可参考 T045 index health
  与 T047 hardening 结果。不得修改 upstream done 任务产物；不得使用 T024-T040 blocked 资产；不得伪造为原始数据。若创建补充
  fixture/manifest，必须在本任务内登记为新资产并写明 synthetic/repair provenance。验收必须实际运行 reverse demo，输出
  JSON 可见、排名稳定、格式符合 T042。
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:30:29'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/1_asset/registration.yaml`

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
  notes: Authoritative M1 API, CLI, JSON, error, and no-hit contract.
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
  notes: Authoritative reverse demo case and pass/fail assertions.
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
  notes: Base M1 manifest schema and fixture/full-resource path semantics.
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
  notes: Original small M1 fixture package for registered fixture inspection and repair-substrate
    bridging.
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
  notes: Expected shapes, columns, keys, and validation rules.
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
  notes: Traceable fixture sample rows and known fixture keys.
  location: local
- id: A-007
  name: package_skeleton_pyproject
  type: other
  source: predecessor
  source_task: T-044
  source_artifact_id: D-001
  origin: T-044/D-001
  registered: '2026-06-24'
  path: 1_asset/package_skeleton_pyproject.toml
  symlink: true
  status: ready
  notes: Canonical package metadata and build shape.
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
  notes: Base package skeleton to extend with reverse-query implementation.
  location: local
- id: A-009
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
  notes: Accepted M1 fixture loader implementation.
  location: local
- id: A-010
  name: m1_loader_api_reference
  type: document
  source: predecessor
  source_task: T-046
  source_artifact_id: D-002
  origin: T-046/D-002
  registered: '2026-06-24'
  path: 1_asset/m1_loader_api_reference.md
  symlink: true
  status: ready
  notes: Loader API reference for compatible reverse-core implementation.
  location: local
- id: A-011
  name: m1_loader_smoke_evidence
  type: table
  source: predecessor
  source_task: T-046
  source_artifact_id: D-003
  origin: T-046/D-003
  registered: '2026-06-24'
  path: 1_asset/m1_loader_smoke_evidence.csv
  symlink: true
  status: ready
  notes: Accepted fixture-loader smoke evidence and coverage boundary.
  location: local
- id: A-012
  name: index_health_summary
  type: document
  source: predecessor
  source_task: T-045
  source_artifact_id: T-045/D-001/index_health_summary
  origin: T-045/D-001
  registered: '2026-06-24'
  path: 1_asset/index_health_summary.json
  symlink: true
  status: ready
  notes: Optional known index health and schema-gap context.
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
  notes: Optional hardened loader implementation reference.
  location: local
- id: A-014
  name: loader_gap_list_m1
  type: document
  source: predecessor
  source_task: T-047
  source_artifact_id: D-004
  origin: T-047/D-004
  registered: '2026-06-24'
  path: 1_asset/loader_gap_list_m1.md
  symlink: true
  status: ready
  notes: Optional known loader/index gap reference.
  location: local
- id: A-015
  name: t049_completion_incident_reference
  type: document
  source: predecessor
  source_task: T-049
  source_artifact_id: completion_report
  origin: T-049/completion.md
  registered: '2026-06-24'
  path: 1_asset/t049_completion_incident_refe

...[truncated by CyHex prompt assembler: 186 chars omitted]
```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-060 reverse_query_core_repair_m1 — Protocol

## Objective
Create a same-layer replacement for T-049 reverse_query_core_m1. This task must repair the missing reverse-query demo substrate honestly and then deliver the M1 reverse query core that T-049 could not complete.

The execution must produce a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest supplement or contract-bridge fixture, that supports the T-042 reverse positive demo case including `HALLMARK_MYC_TARGETS_V1`. The substrate must be clearly labeled as synthetic/repair support, not as original raw LINCS data. Completed upstream task artifacts must not be modified.

## Position In Project
T-060 replaces T-049 for downstream reverse-query work. Downstream tasks should consume T-060 as the required reverse-query core deliverable and should treat T-049 only as a reference incident explaining why the previous route failed.

This is a development task, not a digestion task. It may create package code, execution evidence, and task-local repair assets, but it must not read project-level raw assets.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 API, CLI, JSON, error, and no-hit contract. |
| A-002 | T-042 | `4_artifact/2_persist/m1_demo_cases.yaml` | Authoritative forward/reverse demo cases and pass/fail assertions, including the reverse positive case. |
| A-003 | T-043 | `4_artifact/2_persist/resource_manifest_m1.yaml` | Base M1 manifest schema and fixture/full-resource path semantics. |
| A-004 | T-043 | `4_artifact/2_persist/fixture_package_m1/` | Original small M1 fixture package to inspect through registered task input only. |
| A-005 | T-043 | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Expected resource shapes, columns, key semantics, and validation rules. |
| A-006 | T-043 | `4_artifact/5_table/sample_records_m1.csv` | Traceable fixture sample rows and known fixture keys. |
| A-007 | T-044 | `4_artifact/1_package/pyproject.toml` | Canonical package metadata and editable package shape. |
| A-008 | T-044 | `4_artifact/1_package/pxfquery/` | Base package skeleton to extend with reverse-query code. |
| A-009 | T-046 | `4_artifact/1_package/pxfquery/data/m1_loader.py` | Accepted M1 fixture loader implementation that reverse code should use or remain compatible with. |
| A-010 | T-046 | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-011 | T-046 | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Loader smoke evidence and observed fixture coverage. |
| A-012 | T-045 | `4_artifact/2_persist/index_health_summary.json` | Optional context for known index shape/coverage gaps and deterministic field handling. |
| A-013 | T-047 | `4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened resource loading and index normalization. |
| A-014 | T-047 | `4_artifact/3_document/loader_gap_list_m1.md` | Optional known-gap reference to avoid rediscovering accepted loader limitations. |
| A-015 | T-049 | `5_report/completion.md` | Incident reference documenting the prior reverse-core block and missing fixture/manifest coverage. |

## Execution Steps
1. Read the T-042 contract and demo cases first. Extract the required reverse API fields, JSON shape, ranking expectations, no-hit/error behavior, and the exact positive demo requirements.
2. Read the T-043/T-046 fixture and loader assets through the registered inputs. Confirm the missing `HALLMARK_MYC_TARGETS_V1` or fixture-package/manifest gap without reading project-level raw assets.
3. Create a task-local reverse repair substrate under `4_artifact/2_persist/`, such as `reverse_repair_fixture_m1_1/` plus `reverse_repair_manifest_m1_1.yaml` or an equivalent contract-bridge supplement. It must include enough records/metadata to run the T-042 reverse positive demo honestly and deterministically.
4. Document substrate provenance in a task-local report: what is copied from registered predecessor fixtures, what is synthetic/repair content, why it exists, and why it must not be represented as original raw data.
5. Build the reverse query core from the T-044 package skeleton and T-046 loader API. Use deterministic scoring/ranking with stable tie-breaking and finite-score filtering. Do not depend on T-049 partial code unless execution records a deliberate reason and compatibility check.
6. Implement required no-hit/error behavior from T-042, including missing program, missing context, empty/low-confidence result, and invalid/no-matrix cases as applicable.
7. Run the reverse positive demo against the task-local repair substrate. Save visible structured JSON evidence and record the command used to reproduce it.
8. Run no-hit/error smoke cases and import/compile checks in the project `pxfquery` conda environment.
9. Produce concise execution/result reports, update `4_artifact/registry.yaml`, and write completion status.

## Constraints
- Follow T-042 output JSON, API, CLI, error, and no-hit contract unless a compatibility note is explicitly written and justified.
- Use T-046 loader API behavior as the baseline loader contract; T-047 may be used only as an optional hardening reference.
- The reverse repair substrate must be task-local, registered, and labeled synthetic/repair provenance where applicable.
- Keep ranking deterministic. Ties must use documented stable sort keys.
- Keep code and evidence inside this task directory. Do not modify upstream done tasks.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not use T024-T040 blocked assets.

## Forbidden
- Do not edit T-042, T-043, T-044, T-045, T-046, T-047, or T-049 artifacts.
- Do not mark T-049 as complete or green.
- Do not present repair/synthetic fixture content as original raw LINCS or CMAP data.
- Do not create a private ad hoc data loader that bypasses the accepted loader API without a written compatibility reason.
- Do not perform web search or external lookup.

## Web Search Allowance
Allowed: no

Reason: The task can be configured from project protocol and selected predecessor handoffs/registries. No current external evidence is required.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Reverse repair substrate package or supplement | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` or equivalent | yes |
| Reverse repair manifest | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` or equivalent | yes |
| Repair provenance report | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | yes |
| Reverse query package code | `4_artifact/1_package/pxfquery/` | yes |
| Reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | yes |
| Reverse no-hit/error JSON evidence | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | yes |
| Ranking/scoring notes or table | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` or equivalent | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |

## Acceptance Criteria
- The reverse positive demo actually runs in the `pxfquery` conda environment and writes visible structured JSON.
- The JSON output follows T-042 field names, object nesting, success/error/no-hit conventions, and pass/fail assertions.
- The demo includes the required suppress target `HALLMARK_MYC_TARGETS_V1`.
- Ranking is deterministic across repeated runs on the same substrate.
- No-hit/error cases are represented as structured JSON rather than uncaught tracebacks.
- The task-local repair substrate is registered in `4_artifact/registry.yaml` with explicit synthetic/repair provenance.
- Upstream completed artifacts remain unchanged.

## Failure / Stop Rules
- Stop if execution cannot satisfy the T-042 reverse positive demo without reading forbidden raw project assets.
- Stop if the only available route is to use T024-T040 blocked assets.
- Stop if the repair substrate cannot be honestly labeled and documented as task-local repair/synthetic support.
- Stop rather than silently changing the T-042 contract.

## Delivery Requirements
- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-042
    source_artifact_id: D-001
    path: 4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml
    reason: Authoritative M1 API, CLI, JSON, error, and no-hit contract.
  - id: A-002
    source_task: T-042
    source_artifact_id: D-002
    path: 4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml
    reason: Authoritative reverse demo case and pass/fail assertions.
  - id: A-003
    source_task: T-043
    source_artifact_id: D-001
    path: 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml
    reason: Base M1 manifest schema and resource path semantics.
  - id: A-004
    source_task: T-043
    source_artifact_id: D-002
    path: 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/
    reason: Original small M1 fixture package for registered fixture inspection and repair-substrate bridging.
  - id: A-005
    source_task: T-043
    source_artifact_id: D-003
    path: 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv
    reason: Expected shapes, columns, keys, and validation rules.
  - id: A-006
    source_task: T-043
    source_artifact_id: D-004
    path: 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv
    reason: Traceable fixture sample rows and known fixture keys.
  - id: A-007
    source_task: T-044
    source_artifact_id: D-001
    path: 4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml
    reason: Canonical package metadata and build shape.
  - id: A-008
    source_task: T-044
    source_artifact_id: D-002
    path: 4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/
    reason: Base package skeleton to extend with reverse-query implementation.
  - id: A-009
    source_task: T-046
    source_artifact_id: D-001
    path: 4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py
    reason: Accepted M1 fixture loader implementation.
  - id: A-010
    source_task: T-046
    source_artifact_id: D-002
    path: 4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md
    reason: Loader API reference for compatible reverse-core implementation.
  - id: A-011
    source_task: T-046
    source_artifact_id: D-003
    path: 4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
    reason: Accepted fixture-loader smoke evidence and coverage boundary.
  - id: A-015
    source_task: T-049
    source_artifact_id: completion_report
    path: 4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/completion.md
    reason: Reference incident documenting why T-049 did not deliver the required reverse demo.
optional:
  - id: A-012
    source_task: T-045
    source_artifact_id: T-045/D-001/index_health_summary
    path: 4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/4_artifact/2_persist/index_health_summary.json
    reason: Optional known index health and schema-gap context.
  - id: A-013
    source_task: T-047
    source_artifact_id: D-001
    path: 4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/1_code/loader_hardening_m1.py
    reason: Optional hardened loader implementation reference.
  - id: A-014
    source_task: T-047
    source_artifact_id: D-004
    path: 4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/4_artifact/3_document/loader_gap_list_m1.md
    reason: Optional known loader/index gap reference.
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
  - path: T024-T040 blocked assets
    reason: explicitly excluded by task intent and predecessor protocol lineage
  - path: predecessor task artifacts
    reason: upstream done task outputs are read-only references and must not be modified
output:
  - path: 4_artifact/1_package/pxfquery/
    type: package_code
  - path: 4_artifact/2_persist/reverse_repair_fixture_m1_1/
    type: repair_fixture_package
  - path: 4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml
    type: repair_manifest
  - path: 4_artifact/2_persist/reverse_repair_provenance_v20260624.md
    type: provenance_report
  - path: 4_artifact/2_persist/reverse_demo_evidence_v20260624.json
    type: json_evidence
  - path: 4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json
    type: json_evidence
  - path: 4_artifact/5_table/reverse_ranking_evidence_v20260624.csv
    type: table
  - path: 4_artifact/3_document/execution_report_v20260624.html
    type: html_report
  - path: 4_artifact/3_document/result_report_v20260624.html
    type: html_report
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 1_project_init/
  - 2_project_asset/

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-060 reverse_query_core_repair_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1`
- Allowed write dirs: task-local `3_execution/`, `4_artifact/`, and `5_report/`.
- Forbidden dirs: predecessor task directories, `1_project_init/`, `2_project_asset/`, legacy/raw asset roots, and T024-T040 blocked assets.
- Required registry: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/1_asset/registration.yaml`
- Must stop if: satisfying the T-042 reverse positive demo requires forbidden raw project assets, blocked T024-T040 assets, editing upstream completed artifacts, silently changing the T-042 contract, or presenting synthetic/repair content as original raw LINCS/CMAP data.

## Objective Restatement
T-060 is a same-layer replacement for failed T-049 reverse-query core delivery. Execution must use T-049 only as an incident reference, create a task-local synthetic/repair reverse substrate that honestly supports the T-042 positive reverse demo including `HALLMARK_MYC_TARGETS_V1`, then implement and verify the M1 reverse query core with deterministic scoring/ranking, structured JSON output, no-hit/error behavior, runnable demo evidence, provenance reporting, and registered reusable outputs.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | Authoritative M1 API, CLI, JSON, error, and no-hit contract. | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | Authoritative reverse demo case and pass/fail assertions. | ok |
| A-003 | `1_asset/resource_manifest_m1.yaml` | Base M1 manifest schema and fixture/full-resource path semantics. | ok |
| A-004 | `1_asset/fixture_package_m1` | Original small M1 fixture package for registered fixture inspection and repair-substrate bridging. | ok |
| A-005 | `1_asset/expected_shapes_keys_columns_m1.csv` | Expected shapes, columns, keys, and validation rules. | ok |
| A-006 | `1_asset/sample_records_m1.csv` | Traceable fixture sample rows and known fixture keys. | ok |
| A-007 | `1_asset/package_skeleton_pyproject.toml` | Canonical package metadata and editable package shape. | ok |
| A-008 | `1_asset/package_skeleton_src` | Base package skeleton to extend with reverse-query implementation. | ok |
| A-009 | `1_asset/m1_fixture_loader_code.py` | Accepted M1 fixture loader implementation. | ok |
| A-010 | `1_asset/m1_loader_api_reference.md` | Loader API reference for compatible reverse-core implementation. | ok |
| A-011 | `1_asset/m1_loader_smoke_evidence.csv` | Accepted fixture-loader smoke evidence and coverage boundary. | ok |
| A-012 | `1_asset/index_health_summary.json` | Optional known index health and schema-gap context. | ok |
| A-013 | `1_asset/loader_hardening_m1_code.py` | Optional hardened loader implementation reference. | ok |
| A-014 | `1_asset/loader_gap_list_m1.md` | Optional known loader/index gap reference. | ok |
| A-015 | `1_asset/t049_completion_incident_reference.md` | Reference incident explaining why T-049 did not satisfy the reverse demo. | ok |

## Execution Strategy
1. Read A-001 and A-002 first; extract the exact reverse API/CLI contract, JSON fields, expected positive demo, ranking assertions, and no-hit/error conventions. Output an implementation checklist in `3_execution/`.
2. Read A-003 through A-011 through the registered task-local links; verify the selected fixture/manifest gap for `HALLMARK_MYC_TARGETS_V1` and loader compatibility. Use A-012 through A-014 only if they reduce ambiguity about index shape or loader hardening.
3. Create a minimal task-local reverse repair substrate in `4_artifact/2_persist/`, with a manifest and fixture/supplement sufficient for the T-042 reverse positive case. Explicitly label copied predecessor-derived material versus synthetic/repair records.
4. Build package code under `4_artifact/1_package/pxfquery/` from the T-044 skeleton and T-046 loader API. Keep the ranking finite, deterministic, and stable under ties with documented sort keys.
5. Implement contract-compatible no-hit and error handling for missing program, missing context, empty or low-confidence results, and invalid/no-matrix cases required by A-001/A-002.
6. Run import/compile checks and the reverse positive demo in `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`; save visible structured JSON evidence and command provenance.
7. Run repeatability and no-hit/error smoke cases; compare JSON shape and ranking stability against the T-042 contract.
8. Register reusable outputs in `4_artifact/registry.yaml`, write provenance/result/execution reports, and write `5_report/completion.md` only after the evidence is present.

## Conservative Execution Advice
- Start with: a small contract extraction and loader smoke check against registered fixture paths before creating or copying any reusable output.
- Smoke/demo command or method: run package import/compile checks, then a single reverse positive demo command in the `pxfquery` conda environment against the task-local repair manifest; repeat once to verify stable ranking.
- Full run only after: the repair substrate loads through the accepted loader path or a documented compatible bridge, and the first JSON output matches T-042 field names and success/no-hit/error conventions.
- Cost/time risk: expected low compute and no network; highest risk is schema mismatch between repair substrate, T-042 contract, and T-046 loader behavior.
- Checkpoint advice: preserve intermediate command logs or scripts in `3_execution/`, but copy only accepted reusable artifacts into `4_artifact/`.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reverse query package code | `4_artifact/1_package/pxfquery/` | Imports/compiles and exposes contract-compatible reverse query behavior. |
| Reverse repair fixture package or supplement | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Contains enough task-local synthetic/repair support for the T-042 positive reverse demo. |
| Reverse repair manifest | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Loads or bridges through the accepted fixture semantics without modifying upstream assets. |
| Repair provenance report | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | Clearly separates copied predecessor material from synthetic/repair content and states it is not raw LINCS/CMAP data. |
| Reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Visible structured JSON includes `HALLMARK_MYC_TARGETS_V1` case and satisfies T-042 assertions. |
| Reverse no-hit/error JSON evidence | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | No-hit/error cases are structured JSON, not uncaught tracebacks. |
| Ranking

...[truncated by CyHex prompt assembler: 1901 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml

Interpretation:

- `handoff_check_before_exec.md` is the execution strategy and risk guidance.
- `protocol.md` is the task contract.
- If they conflict, stop and write `5_report/blocked.md`. Do not guess.
- `registration.yaml` and `asset_rule.yaml` define the selected inputs. Do not perform a new asset discovery pass.
- `execution_handoff.md`, if present, is only for continuing an interrupted or long-context execution session.

## 2. Task Contract

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task: T-060 reverse_query_core_repair_m1
Status: active | Executor: hybrid
Objective: Create a same-layer replacement for T-049 reverse_query_core_m1. Use T-049 only as a reference incident: it showed that the T-042 reverse demo contract cannot be satisfied by the currently selected T-046 fixture assets because the required suppress term HALLMARK_MYC_TARGETS_V1 is absent and the selected assets did not include a usable fixture package/manifest. This task must (1) produce and register a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing reverse positive demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver the reverse query core that T-049 was supposed to deliver, including package code, deterministic ranking/scoring, no-hit/error behavior, runnable demo evidence, structured JSON output, and a clear provenance report. Downstream tasks should consume this task as the must replacement for T-049.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-060 reverse_query_core_repair_m1 — Protocol

## Objective
Create a same-layer replacement for T-049 reverse_query_core_m1. This task must repair the missing reverse-query demo substrate honestly and then deliver the M1 reverse query core that T-049 could not complete.

The execution must produce a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest supplement or contract-bridge fixture, that supports the T-042 reverse positive demo case including `HALLMARK_MYC_TARGETS_V1`. The substrate must be clearly labeled as synthetic/repair support, not as original raw LINCS data. Completed upstream task artifacts must not be modified.

## Position In Project
T-060 replaces T-049 for downstream reverse-query work. Downstream tasks should consume T-060 as the required reverse-query core deliverable and should treat T-049 only as a reference incident explaining why the previous route failed.

This is a development task, not a digestion task. It may create package code, execution evidence, and task-local repair assets, but it must not read project-level raw assets.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 API, CLI, JSON, error, and no-hit contract. |
| A-002 | T-042 | `4_artifact/2_persist/m1_demo_cases.yaml` | Authoritative forward/reverse demo cases and pass/fail assertions, including the reverse positive case. |
| A-003 | T-043 | `4_artifact/2_persist/resource_manifest_m1.yaml` | Base M1 manifest schema and fixture/full-resource path semantics. |
| A-004 | T-043 | `4_artifact/2_persist/fixture_package_m1/` | Original small M1 fixture package to inspect through registered task input only. |
| A-005 | T-043 | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Expected resource shapes, columns, key semantics, and validation rules. |
| A-006 | T-043 | `4_artifact/5_table/sample_records_m1.csv` | Traceable fixture sample rows and known fixture keys. |
| A-007 | T-044 | `4_artifact/1_package/pyproject.toml` | Canonical package metadata and editable package shape. |
| A-008 | T-044 | `4_artifact/1_package/pxfquery/` | Base package skeleton to extend with reverse-query code. |
| A-009 | T-046 | `4_artifact/1_package/pxfquery/data/m1_loader.py` | Accepted M1 fixture loader implementation that reverse code should use or remain compatible with. |
| A-010 | T-046 | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-011 | T-046 | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Loader smoke evidence and observed fixture coverage. |
| A-012 | T-045 | `4_artifact/2_persist/index_health_summary.json` | Optional context for known index shape/coverage gaps and deterministic field handling. |
| A-013 | T-047 | `4_artifact/1_code/loader_hardening_m1.py` | Optional implementation reference for hardened resource loading and index normalization. |
| A-014 | T-047 | `4_artifact/3_document/loader_gap_list_m1.md` | Optional known-gap reference to avoid rediscovering accepted loader limitations. |
| A-015 | T-049 | `5_report/completion.md` | Incident reference documenting the prior reverse-core block and missing fixture/manifest coverage. |

## Execution Steps
1. Read the T-042 contract and demo cases first. Extract the required reverse API fields, JSON shape, ranking expectations, no-hit/error behavior, and the exact positive demo requirements.
2. Read the T-043/T-046 fixture and loader assets through the registered inputs. Confirm the missing `HALLMARK_MYC_TARGETS_V1` or fixture-package/manifest gap without reading project-level raw assets.
3. Create a task-local reverse repair substrate under `4_artifact/2_persist/`, such as `reverse_repair_fixture_m1_1/` plus `reverse_repair_manifest_m1_1.yaml` or an equivalent contract-bridge supplement. It must include enough records/metadata to run the T-042 reverse positive demo honestly and deterministically.
4. Document substrate provenance in a task-local report: what is copied from registered predecessor fixtures, what is synthetic/repair content, why it exists, and why it must not be represented as original raw data.
5. Build the reverse query core from the T-044 package skeleton and T-046 loader API. Use deterministic scoring/ranking with stable tie-breaking and finite-score filtering. Do not depend on T-049 partial code unless execution records a deliberate reason and compatibility check.
6. Implement required no-hit/error behavior from T-042, including missing program, missing context, empty/low-confidence result, and invalid/no-matrix cases as applicable.
7. Run the reverse positive demo against the task-local repair substrate. Save visible structured JSON evidence and record the command used to reproduce it.
8. Run no-hit/error smoke cases and import/compile checks in the project `pxfquery` conda environment.
9. Produce concise execution/result reports, update `4_artifact/registry.yaml`, and write completion status.

## Constraints
- Follow T-042 output JSON, API, CLI, error, and no-hit contract unless a compatibility note is explicitly written and justified.
- Use T-046 loader API behavior as the baseline loader contract; T-047 may be used only as an optional hardening reference.
- The reverse repair substrate must be task-local, registered, and labeled synthetic/repair provenance where applicable.
- Keep ranking deterministic. Ties must use documented stable sort keys.
- Keep code and evidence inside this task directory. Do not modify upstream done tasks.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not use T024-T040 blocked assets.

## Forbidden
- Do not edit T-042, T-043, T-044, T-045, T-046, T-047, or T-049 artifacts.
- Do not mark T-049 as complete or green.
- Do not present repair/synthetic fixture content as original raw LINCS or CMAP data.
- Do not create a private ad hoc data loader that bypasses the accepted loader API without a written compatibility reason.
- Do not perform web search or external lookup.

## Web Search Allowance
Allowed: no

Reason: The task can be configured from project protocol and selected predecessor handoffs/registries. No current external evidence is required.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Reverse repair substrate package or supplement | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` or equivalent | yes |
| Reverse repair manifest | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` or equivalent | yes |
| Repair provenance report | `4_artifact/2_persist/reverse_repair_provenance_v20260624.md` | yes |
| Reverse query package code | `4_artifact/1_package/pxfquery/` | yes |
| Reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | yes |
| Reverse no-hit/error JSON evidence | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | yes |
| Ranking/scoring notes or table | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` or equivalent | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |

## Acceptance Criteria
- The reverse positive demo actually runs in the `pxfquery` conda environment and writes visible structured JSON.
- The JSON output follows T-042 field names, object nesting, success/error/no-hit conventions, and pass/fail assertions.
- The demo includes the required suppress target `HALLMARK_MYC_TARGETS_V1`.
- Ranking is deterministic across repeated runs on the same substrate.
- No-hit/error cases are represented as structured JSON rather than uncaught tracebacks.
- The task-local repair substrate is registered in `4_artifact/registry.yaml` with explicit synthetic/repair provenance.
- Upstream completed artifacts remain unchanged.

## Failure / Stop Rules
- Stop if execution cannot satisfy the T-042 reverse positive demo without reading forbidden raw project assets.
- Stop if the only available route is to use T024-T040 blocked assets.
- Stop if the repair substrate cannot be honestly labeled and documented as task-local repair/synthetic support.
- Stop rather than silently changing the T-042 contract.

## Delivery Requirements
- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (15)
- A-001 [document] m1_api_contract — path: 1_asset/m1_api_contract.yaml — origin: T-042/D-001
- A-002 [document] m1_demo_cases — path: 1_asset/m1_demo_cases.yaml — origin: T-042/D-002
- A-003 [document] resource_manifest_m1 — path: 1_asset/resource_manifest_m1.yaml — origin: T-043/D-001
- A-004 [package] fixture_package_m1 — path: 1_asset/fixture_package_m1 — origin: T-043/D-002
- A-005 [table] expected_shapes_keys_columns_m1 — path: 1_asset/expected_shapes_keys_columns_m1.csv — origin: T-043/D-003
- A-006 [table] sample_records_m1 — path: 1_asset/sample_records_m1.csv — origin: T-043/D-004
- A-007 [other] package_skeleton_pyproject — path: 1_asset/package_skeleton_pyproject.toml — origin: T-044/D-001
- A-008 [package] package_skeleton_src — path: 1_asset/package_skeleton_src — origin: T-044/D-002
- A-009 [code] m1_fixture_loader_code — path: 1_asset/m1_fixture_loader_code.py — origin: T-046/D-001
- A-010 [document] m1_loader_api_reference — path: 1_asset/m1_loader_api_reference.md — origin: T-046/D-002
- A-011 [table] m1_loader_smoke_evidence — path: 1_asset/m1_loader_smoke_evidence.csv — origin: T-046/D-003
- A-012 [document] index_health_summary — path: 1_asset/index_health_summary.json — origin: T-045/D-001
- A-013 [code] loader_hardening_m1_code — path: 1_asset/loader_hardening_m1_code.py — origin: T-047/D-001
- A-014 [document] loader_gap_list_m1 — path: 1_asset/loader_gap_list_m1.md — origin: T-047/D-004
- A-015 [document] t049_completion_incident_reference — path: 1_asset/t049_completion_incident_reference.md — origin: T-049/completion.md

### Asset Rules

### Required
- 4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml — Authoritative M1 API, CLI, JSON, error, and no-hit contract.
- 4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml — Authoritative reverse demo case and pass/fail assertions.
- 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml — Base M1 manifest schema and resource path semantics.
- 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1/ — Original small M1 fixture package for registered fixture inspection and repair-substrate bridging.
- 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv — Expected shapes, columns, keys, and validation rules.
- 4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv — Traceable fixture sample rows and known fixture keys.
- 4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml — Canonical package metadata and build shape.
- 4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/ — Base package skeleton to extend with reverse-query implementation.
- 4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py — Accepted M1 fixture loader implementation.
- 4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md — Loader API reference for compatible reverse-core implementation.
- 4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv — Accepted fixture-loader smoke evidence and coverage boundary.
- 4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/completion.md — Reference incident documenting why T-049 did not deliver the required reverse demo.
### Forbidden
- 2_project_asset/ — forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
- T024-T040 blocked assets — explicitly excluded by task intent and predecessor protocol lineage
- predecessor task artifacts — upstream done task outputs are read-only references and must not be modified
### Output
- 4_artifact/1_package/pxfquery/
- 4_artifact/2_persist/reverse_repair_fixture_m1_1/
- 4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml
- 4_artifact/2_persist/reverse_repair_provenance_v20260624.md
- 4_artifact/2_persist/reverse_demo_evidence_v20260624.json
- 4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json
- 4_artifact/5_table/reverse_ranking_evidence_v20260624.csv
- 4_artifact/3_document/execution_report_v20260624.html
- 4_artifact/3_document/result_report_v20260624.html

## 4. Execution Scope

Allowed:

- Read selected registered assets as needed.
- Use tools required by the task.
- Install missing packages when reasonable and local to the task environment.
- Create scripts, logs, checkpoints, and temporary files under `3_execution/`.
- Write accepted deliverables under `4_artifact/`.
- Write reports under `5_report/`.

Forbidden:

- Do not scan arbitrary predecessor task folders.
- Do not read `2_project_asset/` unless the task protocol explicitly allows it and the task phase permits it.
- Do not read future-stage prompts from `2_protocol/0_prompt/`, especially `*_delivery_prompt.md`.
- Do not overwrite predecessor task deliverables.
- Do not rewrite the task protocol to make execution easier.
- Do not perform destructive filesystem, git, database, or remote operations unless the protocol explicitly requires them and the effect is reversible or backed up.
- Do not mark the task as `done`.

## 5. Step Discipline

Execute by steps.

Before starting, convert the approved plan into a short step list. Each step must have:

- a concrete sub-goal
- the operation to perform
- the expected evidence or output
- the dependency on previous steps, if any

For each step:

1. Do the work.
2. Verify the result.
3. Record evidence in logs, reports, or the final completion summary.
4. If the step fails, record the failure honestly.

If a failed step does not block later independent steps, continue with the independent steps and keep the failure visible.

If a failed step blocks dependent steps, stop. Write `5_report/blocked.md` and do not fabricate substitute deliverables.

Do not let later dependent steps degrade into shallow placeholder work because an earlier dependency failed.

## 6. Efficiency And Cost Controls

Use efficient methods.

For batch work, large data processing, web crawling, model inference, or expensive API calls:

1. Run a small demo, smoke test, or sample first.
2. Estimate runtime, cost, and output size.
3. Proceed to the full run only if the sample succeeds and the expected runtime is reasonable.

If the task appears to require more than 24 hours of continuous execution, stop immediately. Write `5_report/blocked.md`, report `kind=failed`, and return a revision recommendation for human approval. Do not start a 24-hour-plus job.

If there are multiple possible implementation routes, you may run a few short targeted probes. Do not spend a long time exploring every route. Choose the most direct route that can satisfy the protocol.

## 7. Development And Version Safety

If this task modifies or packages code, data, models, or reusable assets:

- Keep this task's version separate from predecessor task outputs.
- Do not modify predecessor task directories.
- Save this task's produced version under the current task's `4_artifact/`.
- Use task ID, date, or version label in internal output names when useful.
- If predecessor tasks provide tests, fixtures, or sample data, run them when applicable.
- If tests fail, report the failure. Do not claim the deliverable is validated.

## 8. Deliverable Rules

Write final accepted outputs under `4_artifact/`.

`3_execution/` is only for scripts, temporary files, logs, checkpoints, and resumable state.

If a reusable result is first created under `3_execution/`, move or copy it to the appropriate `4_artifact/` subfolder before completion.

Register every accepted/reusable deliverable in:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/execution_handoff.md`

Include:

- completed steps
- current in-progress step
- next steps
- files changed
- commands run
- artifacts registered
- known failures
- resume instructions

Then report a stage incident with `kind=handoff` and stop. This is a normal execution handoff, not task completion.

## 11. Final Response

At the end, respond with one of these states:

### Completed

Use only if all required deliverables were produced.

Report:

- completed steps
- deliverables produced
- registry path
- execution report path
- result report path
- tests or validation performed
- remaining caveats, if any

### Partial

Use if some independent work was completed but required deliverables are missing.

Report:

- completed steps
- failed or skipped steps
- partial outputs
- why it is not complete
- path to `blocked.md` or failure report

### Blocked

Use if execution cannot continue.

Report:

- blocking reason
- evidence
- path to `blocked.md`
- exact human revision or input needed
