# Delivery QA Prompt
Generated: 2026-06-24 05:45

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
sub_status: delivery_review
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
artifacts:
  - id: T-060/D-001
    name: reverse_query_package_code
    type: package_code
    path: 4_artifact/1_package/pxfquery
    status: ready
    provenance: "Task-local package derived from T-044 skeleton with T-046 m1_loader.py and T-060 reverse implementation."
    notes: "Exposes PxFquery.func2pert, deterministic cosine ranking, CLI reverse, and structured error/no-hit behavior."
  - id: T-060/D-002
    name: reverse_repair_fixture_m1_1
    type: repair_fixture_package
    path: 4_artifact/2_persist/reverse_repair_fixture_m1_1
    status: ready
    provenance: "A-004 registered fixture sidecars plus T-060 synthetic repair rows/columns; not raw LINCS/CMAP data."
    notes: "xpr repair matrix has 15 observations x 9 variables and supports A549 + HALLMARK_MYC_TARGETS_V1."
  - id: T-060/D-003
    name: reverse_repair_manifest_m1_1
    type: repair_manifest
    path: 4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml
    status: ready
    provenance: "Task-local manifest for the T-060 repair fixture."
    notes: "Loadable with M1FixtureLoader using explicit fixture_root."
  - id: T-060/D-004
    name: reverse_repair_provenance
    type: provenance_report
    path: 4_artifact/2_persist/reverse_repair_provenance_v20260624.md
    status: ready
    provenance: "Written during T-060 execution."
    notes: "Separates copied predecessor fixture support from synthetic repair content."
  - id: T-060/D-005
    name: reverse_demo_evidence
    type: json_evidence
    path: 4_artifact/2_persist/reverse_demo_evidence_v20260624.json
    status: ready
    provenance: "Generated by 3_execution/run_reverse_evidence.py in pxfquery conda environment."
    notes: "Positive T-042 reverse demo; found=true; includes HALLMARK_MYC_TARGETS_V1 and repeatability check."
  - id: T-060/D-006
    name: reverse_error_no_hit_evidence
    type: json_evidence
    path: 4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json
    status: ready
    provenance: "Generated by 3_execution/run_reverse_evidence.py in pxfquery conda environment."
    notes: "Structured NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, and empty-target no-hit cases."
  - id: T-060/D-007
    name: reverse_ranking_evidence
    type: table
    path: 4_artifact/5_table/reverse_ranking_evidence_v20260624.csv
    status: ready
    provenance: "Generated from the positive reverse demo ranking."
    notes: "Documents deterministic ranked candidates and similarity values."
  - id: T-060/D-008
    name: execution_report
    type: html_report
    path: 4_artifact/3_document/execution_report_v20260624.html
    status: ready
    provenance: "Written during T-060 execution."
    notes: "Records steps, commands, validation, and boundary compliance."
  - id: T-060/D-009
    name: result_report
    type: html_report
    path: 4_artifact/3_document/result_report_v20260624.html
    status: ready
    provenance: "Written during T-060 execution."
    notes: "Summarizes outputs, evidence files, scoring, and caveat."

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/completion.md`

```text
# Completion

Status: completed

Generated: 2026-06-24

## Completed Steps

1. Extracted the T-042 reverse API/demo contract and no-hit/error expectations from registered A-001/A-002.
2. Confirmed the selected original fixture gap: the registered T-043/T-046 fixture coverage lacks `HALLMARK_MYC_TARGETS_V1`, and the original xpr fixture has no A549 rows.
3. Created the task-local repair substrate under `4_artifact/2_persist/reverse_repair_fixture_m1_1/` and `reverse_repair_manifest_m1_1.yaml`.
4. Documented repair provenance in `4_artifact/2_persist/reverse_repair_provenance_v20260624.md`.
5. Built the T-060 reverse query package code under `4_artifact/1_package/pxfquery/`.
6. Ran positive reverse demo, repeatability check, structured no-hit/error cases, compile/import validation, loader compatibility check, and CLI smoke check in the `pxfquery` conda environment.
7. Registered reusable outputs in `4_artifact/registry.yaml`.
8. Wrote HTML execution and result reports.

## Validation Commands

```text
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python 3_execution/generate_reverse_repair_fixture.py
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery env PYTHONPATH=/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/1_package python 3_execution/run_reverse_evidence.py
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery env PYTHONPATH=/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/1_package python -m pxfquery.cli reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --matrix 4_artifact/2_persist/reverse_repair_fixture_m1_1/xpr_func_fixture_m1.h5ad --matrix-type xpr --top-n 3
```

## Evidence

- Positive demo JSON: `4_artifact/2_persist/reverse_demo_evidence_v20260624.json`
- No-hit/error JSON: `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json`
- Ranking CSV: `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv`
- CLI smoke stdout: `3_execution/reverse_cli_smoke_stdout_v20260624.json`

## Caveats

The repair substrate is synthetic contract-bridge support, not original raw LINCS/CMAP data. It is appropriate for T-042/T-060 M1 reverse-core validation and downstream package development, but not for biological interpretation or manuscript evidence.

No upstream predecessor artifacts were modified. No project-level raw assets, legacy roots, web sources, or T024-T040 blocked assets were used.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/5_report/delivery_qa.md`

```text
# Delivery QA

Generated: 2026-06-24

## Verdict

ready_for_check

## QA Summary

- Required repair fixture exists.
- Required repair manifest exists.
- Required provenance report exists.
- Required package code exists.
- Required positive reverse demo JSON exists and reports `found=true`.
- Required no-hit/error JSON exists.
- Required ranking CSV exists.
- Required execution and result HTML reports exist.
- `4_artifact/registry.yaml` registers all reusable deliverables.
- `5_report/completion.md` records completed status and validation commands.

## Boundary Check

No upstream task artifact was edited intentionally. One accidental project-root `3_execution/` placement was created during execution and immediately moved into the task-local `3_execution/`; the temporary root directory was removed.

```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: development
- ID: T-060 | Name: reverse_query_core_repair_m1
- Objective: Create a same-layer replacement for T-049 reverse_query_core_m1. Use T-049 only as a reference incident: it showed that the T-042 reverse demo contract cannot be satisfied by the currently selected T-046 fixture assets because the required suppress term HALLMARK_MYC_TARGETS_V1 is absent and the selected assets did not include a usable fixture package/manifest. This task must (1) produce and register a task-local reverse repair substrate asset, such as a minimal M1.1 fixture/manifest or contract-bridge supplement, that honestly fills the missing reverse positive demo case without modifying completed T-042/T-043/T-046 artifacts; and (2) deliver the reverse query core that T-049 was supposed to deliver, including package code, deterministic ranking/scoring, no-hit/error behavior, runnable demo evidence, structured JSON output, and a clear provenance report. Downstream tasks should consume this task as the must replacement for T-049.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1`

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
# AI Handoff: T-060 reverse_query_core_repair_m1

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
# Delivery QA: T-060 reverse_query_core_repair_m1

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
