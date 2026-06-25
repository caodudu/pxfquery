# Execution Prompt
Generated: 2026-06-24 03:25

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-043
name: data_manifest_fixture_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Prepare the stable M1 data substrate. Use T-014 for precomputed-data understanding
  and T-021 for standard resource formats. Deliver a resource manifest, a minimal
  fixture package, expected shapes/keys/columns, and small example records sufficient
  for loader, forward, and reverse demos. This task must confirm concrete paths and
  fixture contents; it must not invent data or depend on failed T024-T040 outputs.
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
notes: 'Constraint supplement for config AI: This is a stable bottom-layer asset task.
  It must produce reusable manifest schema, concrete paths, minimal fixture files
  or fixture package, expected shapes/keys/columns, and sample records. Use T-014
  and T-021 only as authorities. Do not invent data, do not scan unrelated project
  assets, and do not use T024-T040 outputs. Downstream loader/query tasks depend on
  this task for reliable data boundaries.'
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T03:25:09'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: t021_standard_resources_bundle
  type: package
  source: predecessor
  source_task: T-021
  source_artifact_id: D-004
  origin: T-021/D-004
  registered: '2026-06-24'
  path: 1_asset/t021_standard_resources_bundle
  symlink: true
  status: ready
  notes: Canonical standard resource bundle from which execution must confirm paths,
    schemas, shapes, keys, columns, and fixture records.
  location: local
- id: A-002
  name: t021_standard_resource_guide
  type: document
  source: predecessor
  source_task: T-021
  source_artifact_id: D-001
  origin: T-021/D-001
  registered: '2026-06-24'
  path: 1_asset/t021_standard_resource_guide.md
  symlink: true
  status: ready
  notes: Authoritative documentation for standard resource format decisions, schemas,
    and usage.
  location: local
- id: A-003
  name: t021_process_records
  type: document
  source: predecessor
  source_task: T-021
  source_artifact_id: D-005
  origin: T-021/D-005
  registered: '2026-06-24'
  path: 1_asset/t021_process_records
  symlink: true
  status: ready
  notes: Validation and profiling records supporting the standard resource bundle;
    use to cross-check fixture boundaries, not as a substitute for inspecting registered
    resources.
  location: local
- id: A-004
  name: t014_precomputed_data_scope
  type: document
  source: predecessor
  source_task: T-014
  source_artifact_id: D-001
  origin: T-014/D-001
  registered: '2026-06-24'
  path: 1_asset/t014_precomputed_data_scope.md
  symlink: true
  status: ready
  notes: Precomputed-data scope and boundaries for deciding what belongs in the M1
    data substrate.
  location: local
- id: A-005
  name: t014_data_resource_inventory
  type: table
  source: predecessor
  source_task: T-014
  source_artifact_id: D-002
  origin: T-014/D-002
  registered: '2026-06-24'
  path: 1_asset/t014_data_resource_inventory.csv
  symlink: true
  status: ready
  notes: Bounded resource inventory to align manifest entries with the earlier precomputed-data
    interpretation.
  location: local
- id: A-006
  name: t014_matrix_schema_coverage
  type: table
  source: predecessor
  source_task: T-014
  source_artifact_id: D-003
  origin: T-014/D-003
  registered: '2026-06-24'
  path: 1_asset/t014_matrix_schema_coverage.csv
  symlink: true
  status: ready
  notes: Matrix schema and bounded sample summary used to verify expected shapes and
    column/function coverage.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-043 data_manifest_fixture_m1 — Protocol

## Objective

Prepare the stable M1 data substrate for downstream package development. The task must produce a reusable resource manifest, a minimal fixture package, expected shapes/keys/columns, and small example records sufficient for loader, forward-query, and reverse-query demos.

The execution must use T-014 and T-021 as the only predecessor authorities. It must confirm concrete paths and fixture contents from registered predecessor artifacts and must not invent data.

## Position In Project

This is a bottom-layer development task for `goal_m1_python_package_v2`. Its outputs define the reliable data boundary that later loader and query tasks can consume without rereading broad legacy/project raw assets.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` | Canonical standard resource bundle for concrete paths, schemas, shapes, keys, columns, and fixture records. |
| A-002 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` | Authoritative documentation for standard resource format decisions and expected usage. |
| A-003 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/process_records/` | Validation and profiling records for cross-checking the resource bundle. |
| A-004 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/2_persist/pxfquery_t014_precomputed_data_scope_v20260618.md` | Precomputed-data scope and boundaries for deciding the M1 substrate. |
| A-005 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_data_resource_inventory_v20260618.csv` | Resource inventory for aligning manifest entries with predecessor interpretation. |
| A-006 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv` | Matrix schema and coverage summary for expected shape and column/function checks. |

## Steps

1. Inspect only the registered input assets listed above, plus the current task's own writable folders.
2. Confirm the concrete standard resource paths and create `resource_manifest_m1.yaml` with stable resource IDs, relative bundle paths, file types, intended loader roles, required columns/keys, expected shapes, and provenance back to T-014/T-021.
3. Build a minimal fixture package from real records extracted from A-001. Include enough data for loader smoke tests, one forward-query demo path, and one reverse-query demo path. Keep fixture files small and deterministic.
4. Produce `expected_shapes_keys_columns_m1.csv` summarizing each selected resource's expected shape, key fields, columns, index semantics, and validation rule.
5. Produce `sample_records_m1.csv` or equivalent tabular summary showing the exact source resource, row/key identifiers, selected fields, and why each example is included.
6. Write a concise README explaining how downstream tasks should consume the manifest and fixture package, including any known exclusions from the full T-021 standard resource bundle.
7. Register all accepted outputs in `4_artifact/registry.yaml`, write completion reporting, and keep temporary scripts/logs in `3_execution/`.

## Constraints

- Use only T-014 and T-021 registered assets as authorities for input data and schema decisions.
- Do not invent rows, keys, columns, shapes, function names, drugs, genes, cell lines, or scores.
- Fixture records must be copied or derived from registered predecessor assets and must retain enough provenance to trace back to the source file and source identifier.
- Prefer small, deterministic fixtures over broad sampling.
- The fixture must be adequate for loader, forward-query, and reverse-query demonstrations, but it does not need to reproduce full query ranking performance.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not depend on T024-T040 outputs.
- Do not modify predecessor task directories or project protocol/state.

## Forbidden

- Reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Reading unrelated task directories or outputs outside registered T-014/T-021 assets.
- Using outputs from failed T024-T040 tasks.
- Creating synthetic biological records or placeholder data that could be mistaken for real resources.
- Running external web search or downloading external data.

## Web Search Allowance

Allowed: no

Reason: The task is an internal data-substrate configuration and fixture task. The selected predecessor artifacts provide the needed authorities, and current/external information is not required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| M1 resource manifest | `4_artifact/2_persist/resource_manifest_m1.yaml` | Yes |
| Minimal fixture package | `4_artifact/2_persist/fixture_package_m1/` | Yes |
| Expected shapes/keys/columns table | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Yes |
| Sample records table | `4_artifact/5_table/sample_records_m1.csv` | Yes |
| Usage/readme document | `4_artifact/2_persist/data_manifest_fixture_m1_readme.md` | Yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Yes |
| Updated artifact registry | `4_artifact/registry.yaml` | Yes |
| Completion report | `5_report/completion.md` | Yes |

## Acceptance Criteria

- Manifest entries point to concrete, existing resources from the registered T-021 standard resource bundle or to fixture files generated in this task.
- Each manifest entry includes resource type, loader role, required keys/columns, expected shape or record count rule, provenance, and validation notes.
- Fixture files are small, deterministic, and contain only real data copied or boundedly extracted from registered assets.
- Expected shapes/keys/columns are explicitly documented for matrices, indexes, metadata tables, and fixture files used by loader/forward/reverse demos.
- Sample records are traceable to their source resource and include enough examples for downstream smoke tests.
- Outputs do not require project-level raw asset reads and do not reference T024-T040.

## Failure / Stop Rules

- Stop if registered predecessor assets are missing, unreadable, or insufficient to create real fixtures without guessing.
- Stop if execution appears to require `/2_project_asset/` or direct legacy source reads.
- Stop if no coherent minimal forward/reverse demo fixture can be extracted from registered resources.
- Stop if validation contradicts T-014/T-021 authority records in a way that changes the intended resource boundary.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-021
    source_artifact_id: D-004
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/"
    reason: "Canonical standard resource bundle for confirming concrete resource paths, schemas, shapes, keys, columns, and fixture records."
  - id: A-002
    source_task: T-021
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md"
    reason: "Authoritative guide for standard resource format decisions and expected usage."
  - id: A-003
    source_task: T-021
    source_artifact_id: D-005
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/process_records/"
    reason: "Supporting validation and profiling records for cross-checking the resource bundle."
  - id: A-004
    source_task: T-014
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/2_persist/pxfquery_t014_precomputed_data_scope_v20260618.md"
    reason: "Precomputed-data scope and boundaries for the M1 data substrate."
  - id: A-005
    source_task: T-014
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_data_resource_inventory_v20260618.csv"
    reason: "Bounded resource inventory for aligning manifest entries with predecessor interpretation."
  - id: A-006
    source_task: T-014
    source_artifact_id: D-003
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv"
    reason: "Matrix schema and coverage summary for expected shape and column/function checks."
optional: []
forbidden:
  - path: 2_project_asset/
    reason: "forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed"
  - path: "4_phase_development/**/task_*T024*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T025*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T026*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T027*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T028*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T029*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T030*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T031*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T032*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T033*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T034*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T035*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T036*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T037*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T038*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T039*"
    reason: "do not depend on failed T024-T040 outputs"
  - path: "4_phase_development/**/task_*T040*"
    reason: "do not depend on failed T024-T040 outputs"
output:
  - path: 4_artifact/2_persist/resource_manifest_m1.yaml
    type: manifest
  - path: 4_artifact/2_persist/fixture_package_m1/
    type: package
  - path: 4_artifact/5_table/expected_shapes_keys_columns_m1.csv
    type: table
  - path: 4_artifact/5_table/sample_records_m1.csv
    type: table
  - path: 4_artifact/2_persist/data_manifest_fixture_m1_readme.md
    type: document
  - path: 4_artifact/3_document/execution_report_v20260624.html
    type: document
  - path: 4_artifact/3_document/result_report_v20260624.html
    type: document
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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-043 data_manifest_fixture_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories, `1_project_init/`, unrelated task outputs, failed T024-T040 outputs, and future-stage prompts under `2_protocol/0_prompt/`
- Required registry: `1_asset/registration.yaml`, with all six required assets preflighted as ready symlinks
- Must stop if: a required registered asset is unreadable or inconsistent, fixture records cannot be traced to A-001, downstream-ready examples require raw project assets or failed T024-T040 outputs, or execution would need to invent biological records, schema fields, identifiers, paths, or scores

## Objective Restatement
Prepare the stable M1 data substrate for later package development by producing a small, traceable resource manifest and fixture package derived only from registered T-014 and T-021 predecessor assets. The result should give downstream loader, forward-query, and reverse-query tasks enough concrete paths, schemas, shapes, columns, keys, and sample records to run demos without rediscovering broad legacy context.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t021_standard_resources_bundle` | Canonical standard resource bundle for concrete resource files, schemas, shapes, keys, columns, and real fixture records | ok |
| A-002 | `1_asset/t021_standard_resource_guide.md` | Authoritative guide for standard resource format decisions and expected usage | ok |
| A-003 | `1_asset/t021_process_records` | Validation and profiling records for cross-checking resource bundle boundaries | ok |
| A-004 | `1_asset/t014_precomputed_data_scope.md` | Precomputed-data scope and boundary authority for deciding the M1 substrate | ok |
| A-005 | `1_asset/t014_data_resource_inventory.csv` | Resource inventory for aligning manifest entries with predecessor interpretation | ok |
| A-006 | `1_asset/t014_matrix_schema_coverage.csv` | Matrix schema and coverage summary for expected shape and column/function checks | ok |

## Execution Strategy
1. Start with a narrow read of A-002, A-004, A-005, and A-006 to identify the resource categories, schema expectations, and matrix/index boundaries already approved by T-014/T-021; write only notes or scripts under `3_execution/`.
2. Inspect only the relevant files inside A-001 needed for the M1 loader, forward-query, and reverse-query substrate; do not scan unrelated project assets or predecessor directories outside the registered symlink.
3. Cross-check selected A-001 resources against A-003 process records and T-014 tables, then draft the manifest schema with stable resource IDs, relative bundle paths, file types, loader roles, keys, expected shapes, validation rules, and provenance.
4. Build a deterministic fixture package under `4_artifact/2_persist/fixture_package_m1/` from real A-001 records only, keeping enough linked rows/columns for loader smoke tests and one forward/reverse demo path.
5. Generate `expected_shapes_keys_columns_m1.csv` with one row per selected resource, including shape, key fields, required columns, index semantics, validation rule, and source/provenance.
6. Generate `sample_records_m1.csv` documenting exact source resource, row/key identifiers, selected fields, inclusion reason, and traceability back to source records.
7. Write `data_manifest_fixture_m1_readme.md`, `resource_manifest_m1.yaml`, and concise HTML execution/result reports explaining what is included, what is excluded from the full T-021 bundle, and how downstream tasks should consume the outputs.
8. Register all accepted outputs in `4_artifact/registry.yaml`; keep temporary scripts, logs, and validation snippets in `3_execution/`, not as final reusable outputs.

## Conservative Execution Advice
- Start with: a tiny schema/path survey of the six registered assets, especially A-002/A-004 for boundaries and A-005/A-006 for expected resource classes.
- Smoke/demo command or method: run a small local Python validation script from `3_execution/` using `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` to load only the chosen fixture files and verify declared shapes, keys, required columns, and sample IDs.
- Full run only after: the selected resources are traceable to A-001 and their inclusion is consistent with A-002/A-004/A-005/A-006 and, where applicable, A-003 validation records.
- Cost/time risk: expected cost is local file I/O only; no web, no downloads, no broad raw-asset scan, and no expensive recomputation should be needed.
- Checkpoint advice: before writing final artifacts, keep a `3_execution/` draft list of selected source files and sample identifiers; stop if the list cannot support both forward and reverse demo paths without synthetic data.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| M1 resource manifest | `4_artifact/2_persist/resource_manifest_m1.yaml` | YAML contains stable resource IDs, relative paths, file types, loader roles, required keys/columns, expected shapes, validation rules, and T-014/T-021 provenance |
| Minimal fixture package | `4_artifact/2_persist/fixture_package_m1/` | Small deterministic files copied/derived from real A-001 records, sufficient for loader smoke tests and one forward/reverse demo path |
| Expected shapes/keys/columns table | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | CSV lists selected resources with shape, keys, columns, index semantics, validation rule, and provenance |
| Sample records table | `4_artifact/5_table/sample_records_m1.csv` | CSV traces each sample/example record to exact source resource and identifiers with inclusion reason |
| Usage/readme document | `4_artifact/2_persist/data_manifest_fixture_m1_readme.md` | Markdown explains downstream use, fixture contents, known exclusions, and boundary rules |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | HTML summarizes method, inputs inspected, validation steps, and any limitations |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | HTML summarizes final outputs, acceptance checks, and downstream handoff notes |
| Artifact registry update | `4_artifact/registry.yaml` | Registry records all accepted outputs with paths, types, provenance, and status |

## Failure / Stop Conditions
- Stop if any registered required asset is missing, empty, unreadable, or materially inconsistent with the registry/preflight summary.
- Stop if the selected fixture cannot be built from real A-001 records with explicit provenance.
- Stop if a loader/forward/reverse demo path would require invented data, placeholder biological records, or unverifiable keys/scores.
- Stop if need

...[truncated by CyHex prompt assembler: 927 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-043 data_manifest_fixture_m1
Status: active | Executor: hybrid
Objective: Prepare the stable M1 data substrate. Use T-014 for precomputed-data understanding and T-021 for standard resource formats. Deliver a resource manifest, a minimal fixture package, expected shapes/keys/columns, and small example records sufficient for loader, forward, and reverse demos. This task must confirm concrete paths and fixture contents; it must not invent data or depend on failed T024-T040 outputs.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-043 data_manifest_fixture_m1 — Protocol

## Objective

Prepare the stable M1 data substrate for downstream package development. The task must produce a reusable resource manifest, a minimal fixture package, expected shapes/keys/columns, and small example records sufficient for loader, forward-query, and reverse-query demos.

The execution must use T-014 and T-021 as the only predecessor authorities. It must confirm concrete paths and fixture contents from registered predecessor artifacts and must not invent data.

## Position In Project

This is a bottom-layer development task for `goal_m1_python_package_v2`. Its outputs define the reliable data boundary that later loader and query tasks can consume without rereading broad legacy/project raw assets.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` | Canonical standard resource bundle for concrete paths, schemas, shapes, keys, columns, and fixture records. |
| A-002 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` | Authoritative documentation for standard resource format decisions and expected usage. |
| A-003 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/process_records/` | Validation and profiling records for cross-checking the resource bundle. |
| A-004 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/2_persist/pxfquery_t014_precomputed_data_scope_v20260618.md` | Precomputed-data scope and boundaries for deciding the M1 substrate. |
| A-005 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_data_resource_inventory_v20260618.csv` | Resource inventory for aligning manifest entries with predecessor interpretation. |
| A-006 | T-014 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv` | Matrix schema and coverage summary for expected shape and column/function checks. |

## Steps

1. Inspect only the registered input assets listed above, plus the current task's own writable folders.
2. Confirm the concrete standard resource paths and create `resource_manifest_m1.yaml` with stable resource IDs, relative bundle paths, file types, intended loader roles, required columns/keys, expected shapes, and provenance back to T-014/T-021.
3. Build a minimal fixture package from real records extracted from A-001. Include enough data for loader smoke tests, one forward-query demo path, and one reverse-query demo path. Keep fixture files small and deterministic.
4. Produce `expected_shapes_keys_columns_m1.csv` summarizing each selected resource's expected shape, key fields, columns, index semantics, and validation rule.
5. Produce `sample_records_m1.csv` or equivalent tabular summary showing the exact source resource, row/key identifiers, selected fields, and why each example is included.
6. Write a concise README explaining how downstream tasks should consume the manifest and fixture package, including any known exclusions from the full T-021 standard resource bundle.
7. Register all accepted outputs in `4_artifact/registry.yaml`, write completion reporting, and keep temporary scripts/logs in `3_execution/`.

## Constraints

- Use only T-014 and T-021 registered assets as authorities for input data and schema decisions.
- Do not invent rows, keys, columns, shapes, function names, drugs, genes, cell lines, or scores.
- Fixture records must be copied or derived from registered predecessor assets and must retain enough provenance to trace back to the source file and source identifier.
- Prefer small, deterministic fixtures over broad sampling.
- The fixture must be adequate for loader, forward-query, and reverse-query demonstrations, but it does not need to reproduce full query ranking performance.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not depend on T024-T040 outputs.
- Do not modify predecessor task directories or project protocol/state.

## Forbidden

- Reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Reading unrelated task directories or outputs outside registered T-014/T-021 assets.
- Using outputs from failed T024-T040 tasks.
- Creating synthetic biological records or placeholder data that could be mistaken for real resources.
- Running external web search or downloading external data.

## Web Search Allowance

Allowed: no

Reason: The task is an internal data-substrate configuration and fixture task. The selected predecessor artifacts provide the needed authorities, and current/external information is not required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| M1 resource manifest | `4_artifact/2_persist/resource_manifest_m1.yaml` | Yes |
| Minimal fixture package | `4_artifact/2_persist/fixture_package_m1/` | Yes |
| Expected shapes/keys/columns table | `4_artifact/5_table/expected_shapes_keys_columns_m1.csv` | Yes |
| Sample records table | `4_artifact/5_table/sample_records_m1.csv` | Yes |
| Usage/readme document | `4_artifact/2_persist/data_manifest_fixture_m1_readme.md` | Yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Yes |
| Updated artifact registry | `4_artifact/registry.yaml` | Yes |
| Completion report | `5_report/completion.md` | Yes |

## Acceptance Criteria

- Manifest entries point to concrete, existing resources from the registered T-021 standard resource bundle or to fixture files generated in this task.
- Each manifest entry includes resource type, loader role, required keys/columns, expected shape or record count rule, provenance, and validation notes.
- Fixture files are small, deterministic, and contain only real data copied or boundedly extracted from registered assets.
- Expected shapes/keys/columns are explicitly documented for matrices, indexes, metadata tables, and fixture files used by loader/forward/reverse demos.
- Sample records are traceable to their source resource and include enough examples for downstream smoke tests.
- Outputs do not require project-level raw asset reads and do not reference T024-T040.

## Failure / Stop Rules

- Stop if registered predecessor assets are missing, unreadable, or insufficient to create real fixtures without guessing.
- Stop if execution appears to require `/2_project_asset/` or direct legacy source reads.
- Stop if no coherent minimal forward/reverse demo fixture can be extracted from registered resources.
- Stop if validation contradicts T-014/T-021 authority records in a way that changes the intended resource boundary.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (6)
- A-001 [package] t021_standard_resources_bundle — path: 1_asset/t021_standard_resources_bundle — origin: T-021/D-004
- A-002 [document] t021_standard_resource_guide — path: 1_asset/t021_standard_resource_guide.md — origin: T-021/D-001
- A-003 [document] t021_process_records — path: 1_asset/t021_process_records — origin: T-021/D-005
- A-004 [document] t014_precomputed_data_scope — path: 1_asset/t014_precomputed_data_scope.md — origin: T-014/D-001
- A-005 [table] t014_data_resource_inventory — path: 1_asset/t014_data_resource_inventory.csv — origin: T-014/D-002
- A-006 [table] t014_matrix_schema_coverage — path: 1_asset/t014_matrix_schema_coverage.csv — origin: T-014/D-003

### Asset Rules

### Required
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/ — Canonical standard resource bundle for confirming concrete resource paths, schemas, shapes, keys, columns, and fixture records.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md — Authoritative guide for standard resource format decisions and expected usage.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/process_records/ — Supporting validation and profiling records for cross-checking the resource bundle.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/2_persist/pxfquery_t014_precomputed_data_scope_v20260618.md — Precomputed-data scope and boundaries for the M1 data substrate.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_data_resource_inventory_v20260618.csv — Bounded resource inventory for aligning manifest entries with predecessor interpretation.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_understand_pxfquery_precomputed_data/4_artifact/5_table/pxfquery_t014_matrix_schema_coverage_v20260618.csv — Matrix schema and coverage summary for expected shape and column/function checks.
### Forbidden
- 2_project_asset/ — forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
- 4_phase_development/**/task_*T024* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T025* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T026* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T027* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T028* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T029* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T030* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T031* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T032* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T033* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T034* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T035* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T036* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T037* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T038* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T039* — do not depend on failed T024-T040 outputs
- 4_phase_development/**/task_*T040* — do not depend on failed T024-T040 outputs
### Output
- 4_artifact/2_persist/resource_manifest_m1.yaml
- 4_artifact/2_persist/fixture_package_m1/
- 4_artifact/5_table/expected_shapes_keys_columns_m1.csv
- 4_artifact/5_table/sample_records_m1.csv
- 4_artifact/2_persist/data_manifest_fixture_m1_readme.md
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

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_m1_python_package_v2/task_data_manifest_fixture_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/5_report/execution_handoff.md`

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
