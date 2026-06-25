# Checking Prompt
Generated: 2026-06-24 04:05

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-047
name: resource_loader_hardening_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Harden the loader against real M1 manifest and index resources. Use T-043
  for manifest/fixture definitions and T-045 for index health findings; optionally
  use T-041 legacy source digest if available for implementation clues. Deliver enhanced
  loader behavior, real-path/index smoke results, and a clear gap list if full hardening
  is blocked. This is a reusable enhancement asset and must not block the M1 fixture-based
  path if real resources are incomplete.
executor: hybrid
agent_id: AGT-002
config_agent_id: AGT-002
check_agent_id: AGT-002
execute_agent_id: AGT-002
server_id: null
status: active
cyhex_version: 1.2.19
created: '2026-06-24'
started: null
completed: null
notes: 'Constraint supplement for config AI: This is an enhancement/reuse asset, not
  an M1 blocker. Use T-043 and T-045 as hard inputs; use T-041 only if done and available
  as may input. Harden real manifest/index loading where feasible and report gaps
  honestly. Do not mutate authoritative indexes and do not block the fixture loader
  path if real resources remain incomplete.'
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T04:05:07'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: resource_manifest_m1
  type: other
  source: predecessor
  source_task: T-043
  source_artifact_id: D-001
  origin: T-043/D-001
  registered: '2026-06-24'
  path: 1_asset/resource_manifest_m1.yaml
  symlink: true
  status: ready
  notes: Entry point for all M1 resource paths (full standard and fixture), loader
    roles, required keys/columns, expected shapes, validation rules
  location: local
- id: A-002
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
  notes: Acceptance evidence for expected shapes, keys, columns, and index semantics
  location: local
- id: A-003
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
  notes: Traceable sample rows and keys used by the fixture package for smoke verification
  location: local
- id: A-004
  name: index_health_summary
  type: other
  source: predecessor
  source_task: T-045
  source_artifact_id: T-045/D-001/index_health_summary
  origin: T-045/T-045/D-001
  registered: '2026-06-24'
  path: 1_asset/index_health_summary.json
  symlink: true
  status: ready
  notes: Machine-readable per-index schema status, key completeness, known gaps, patch
    recommendations for loader configuration
  location: local
- id: A-005
  name: index_health_report
  type: document
  source: predecessor
  source_task: T-045
  source_artifact_id: T-045/D-002/index_health_report
  origin: T-045/T-045/D-002
  registered: '2026-06-24'
  path: 1_asset/index_health_report.md
  symlink: true
  status: ready
  notes: Human-readable index health overview with pass/warn/block per index and M1
    readiness verdict
  location: local
- id: A-006
  name: gap_notes
  type: document
  source: predecessor
  source_task: T-045
  source_artifact_id: T-045/D-003/gap_notes
  origin: T-045/T-045/D-003
  registered: '2026-06-24'
  path: 1_asset/gap_notes.md
  symlink: true
  status: ready
  notes: Detailed gap severity, demo impact, and resolution paths for loader hardening
    decisions
  location: local
- id: A-007
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
  notes: Compact real-data fixture bundle for deterministic loader smoke/demo runs
  location: local
- id: A-008
  name: data_manifest_fixture_m1_readme
  type: document
  source: predecessor
  source_task: T-043
  source_artifact_id: D-005
  origin: T-043/D-005
  registered: '2026-06-24'
  path: 1_asset/data_manifest_fixture_m1_readme.md
  symlink: true
  status: ready
  notes: Downstream usage notes and known exclusions
  location: local

```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-047 resource_loader_hardening_m1 — Protocol

## Objective

Harden the M1 Python-package resource loader against real full matrix/index resources and the fixture package, using T-043 manifest/fixture definitions and T-045 index health findings. Deliver enhanced loader behavior (real-path loading, schema-aware unwrap, field normalization), smoke results against both full resources and fixtures, and a clear gap/block list for anything that cannot be safely hardened. This is a reusable enhancement asset and must not block the M1 fixture-only path if real resources are incomplete.

## Position In Project

- G-005 `goal_m1_python_package_v2` — development phase, enhancement/reuse asset
- Hard inputs: T-043 data manifest & fixture package, T-045 index health check
- T-041 legacy source digest is not delivered — exclude from configuration; execution may not use it
- T-047 is NOT an M1 blocker — if real resources are incomplete, report gaps and continue with fixture-based path

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-043/D-001 | 4_artifact/2_persist/resource_manifest_m1.yaml | Entry point for full standard resource paths (h5ad, csv, json) and fixture resource paths; defines loader role, required keys/columns, expected shapes, validation rules |
| A-002 | T-043/D-003 | 4_artifact/5_table/expected_shapes_keys_columns_m1.csv | Acceptance evidence for expected shapes, keys, columns, and index semantics |
| A-003 | T-043/D-004 | 4_artifact/5_table/sample_records_m1.csv | Traceable sample rows and keys for smoke verification |
| A-004 | T-045/D-001 | 4_artifact/2_persist/index_health_summary.json | Machine-readable per-index schema status, key completeness, known gaps, patch recommendations |
| A-005 | T-045/D-002 | 4_artifact/2_persist/index_health_report.md | Human-readable index health overview with pass/warn/block per index and M1 readiness verdict |
| A-006 | T-045/D-003 | 4_artifact/3_document/gap_notes.md | Detailed gap severity, demo impact, and resolution paths |
| A-007 | T-043/D-002 | 4_artifact/2_persist/fixture_package_m1/ | Compact real-data fixture bundle for deterministic loader smoke/demo runs |
| A-008 | T-043/D-005 | 4_artifact/2_persist/data_manifest_fixture_m1_readme.md | Downstream usage notes and exclusions |

## Execution Steps

1. **Load and validate the resource manifest.** Read `resource_manifest_m1.yaml` (A-001) and confirm that all listed resource paths are resolvable and non-empty. Record any missing full-resource paths as a gap.
2. **Read index health summary.** Load `index_health_summary.json` (A-004) and extract per-index schema requirements, field mappings, known gaps, and patch recommendations. Cross-reference with `expected_shapes_keys_columns_m1.csv` (A-002).
3. **Implement or enhance the loader against real full resources.** For each resource type (h5ad matrices, csv metadata, json indexes), implement or enhance loader functions that:
   - Open real `.h5ad` matrices (cp_func_ad, sh_func_ad, xpr_func_ad) and validate obs columns, var_names, and shapes against manifest expectations.
   - Load real CSV metadata tables and validate key columns, row counts against manifest.
   - Load real JSON indexes and validate schema/top-level structure against manifest and T-045 health summary.
   - Handle the `function_index.json` non-standard dict structure (`meta/var_names/aliases`) — unwrap per T-045 handoff.
   - Normalize field names where T-045 reports discrepancies (e.g., `gene_index.json` uses `symbol` not `gene_symbol`; `cellline_tree.json` is flat with 3 keys only, not hierarchical).
4. **Run loader smoke tests with the fixture package.** Load all fixture resources from `fixture_package_m1/` (A-007) and verify:
   - Fixture matrices are readable, shapes match manifest, obs columns and var_names are present.
   - Fixture metadata CSV files match expected row counts and key columns.
   - Fixture JSON indexes are parsable and match expected top-level keys.
5. **Execute real full-resource loading where feasible.** Attempt to load full standard resources from paths defined in the manifest. For each resource:
   - If load succeeds: record shape, key presence, and any field normalizations applied.
   - If load fails or a resource is missing: document the specific gap (path, reason), assess whether fixture covers the gap, and classify as block/warn/note.
6. **Produce gap list.** Aggregate all gaps from steps 1–5 into a structured gap list with: resource ID, path, issue, severity (block/warn/info), whether fixture covers it, recommended action.
7. **Produce smoke results report.** Generate a machine-readable result summary (JSON) and a human-readable report (MD) with: per-resource load status, shape/key validation results, any field normalizations applied, gap list.
8. **Deliver artifacts.** Register all accepted outputs in `4_artifact/registry.yaml`. Write `5_report/completion.md`.

## Constraints

- This is an enhancement/reuse asset — do NOT block the M1 fixture-based path if real resources are incomplete.
- Do NOT mutate or overwrite authoritative full-resource indexes or standard resources under `t021_standard_resources_bundle/`.
- Prefer the fixture path as a deterministic fallback when real resource loading is blocked.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- T-041 legacy source digest is NOT available (still executing). Do not use it.
- Use the `pxfquery` conda environment for all Python execution: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.

## Forbidden

- Do not modify legacy source roots or authoritative index files.
- Do not read `2_project_asset/`.
- Do not depend on T-041 outputs.
- Do not block the M1 fixture-only path.

## Web Search Allowance

Allowed: no
Reason: All required inputs are provided by T-043 and T-045 predecessor handoffs. No external/current information is needed.


...[truncated by CyHex prompt assembler: 1835 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-043
    source_artifact_id: D-001
    path: 4_artifact/2_persist/resource_manifest_m1.yaml
    reason: Entry point for all M1 resource paths, loader roles, expected shapes, keys, columns, and validation rules
  - id: A-002
    source_task: T-043
    source_artifact_id: D-003
    path: 4_artifact/5_table/expected_shapes_keys_columns_m1.csv
    reason: Acceptance evidence for expected shapes, keys, columns, and index semantics
  - id: A-003
    source_task: T-043
    source_artifact_id: D-004
    path: 4_artifact/5_table/sample_records_m1.csv
    reason: Traceable sample rows and keys for smoke verification
  - id: A-004
    source_task: T-045
    source_artifact_id: T-045/D-001/index_health_summary
    path: 4_artifact/2_persist/index_health_summary.json
    reason: Machine-readable per-index schema status, key completeness, gaps, and patch recommendations for loader configuration
  - id: A-005
    source_task: T-045
    source_artifact_id: T-045/D-002/index_health_report
    path: 4_artifact/2_persist/index_health_report.md
    reason: Human-readable index health overview with pass/warn/block per index and M1 readiness verdict
  - id: A-006
    source_task: T-045
    source_artifact_id: T-045/D-003/gap_notes
    path: 4_artifact/3_document/gap_notes.md
    reason: Detailed gap severity, demo impact, and resolution paths for loader hardening decisions
  - id: A-007
    source_task: T-043
    source_artifact_id: D-002
    path: 4_artifact/2_persist/fixture_package_m1/
    reason: Compact real-data fixture bundle for deterministic loader smoke/demo runs; fallback when real resources are incomplete
  - id: A-008
    source_task: T-043
    source_artifact_id: D-005
    path: 4_artifact/2_persist/data_manifest_fixture_m1_readme.md
    reason: Downstream usage notes and known exclusions for contextual guidance
optional: []
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
output:
  - path: 4_artifact/1_code/loader_hardening_m1.py
    type: code
  - path: 4_artifact/2_persist/loader_smoke_results_m1.json
    type: data
  - path: 4_artifact/3_document/loader_smoke_report_m1.md
    type: document
  - path: 4_artifact/3_document/loader_gap_list_m1.md
    type: document
  - path: 4_artifact/3_document/execution_report_v*.html
    type: report
  - path: 4_artifact/3_document/result_report_v*.html
    type: report
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task ID: T-047 | Name: resource_loader_hardening_m1
Status: active | Executor: hybrid
Objective: Harden the loader against real M1 manifest and index resources. Use T-043 for manifest/fixture definitions and T-045 for index health findings; optionally use T-041 legacy source digest if available for implementation clues. Deliver enhanced loader behavior, real-path/index smoke results, and a clear gap list if full hardening is blocked. This is a reusable enhancement asset and must not block the M1 fixture-based path if real resources are incomplete.
Notes / User Natural-Language Intent: Constraint supplement for config AI: This is an enhancement/reuse asset, not an M1 blocker. Use T-043 and T-045 as hard inputs; use T-041 only if done and available as may input. Harden real manifest/index loading where feasible and report gaps honestly. Do not mutate authoritative indexes and do not block the fixture loader path if real resources remain incomplete.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: development
  project_asset_access: forbidden
  zero_assets: false
  total_assets: 8
  symlink_sync:
    checked: 8
    linked: 8
    skipped: 0
    changed: false
  counts:
    ok: 8
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: resource_manifest_m1
    required: true
    status: ok
    path: 1_asset/resource_manifest_m1.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/resource_manifest_m1.yaml
    reason: local path exists
  - id: A-002
    name: expected_shapes_keys_columns_m1
    required: true
    status: ok
    path: 1_asset/expected_shapes_keys_columns_m1.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/expected_shapes_keys_columns_m1.csv
    reason: local path exists
  - id: A-003
    name: sample_records_m1
    required: true
    status: ok
    path: 1_asset/sample_records_m1.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/5_table/sample_records_m1.csv
    reason: local path exists
  - id: A-004
    name: index_health_summary
    required: true
    status: ok
    path: 1_asset/index_health_summary.json
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/4_artifact/2_persist/index_health_summary.json
    reason: local path exists
  - id: A-005
    name: index_health_report
    required: true
    status: ok
    path: 1_asset/index_health_report.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/4_artifact/2_persist/index_health_report.md
    reason: local path exists
  - id: A-006
    name: gap_notes
    required: true
    status: ok
    path: 1_asset/gap_notes.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/4_artifact/3_document/gap_notes.md
    reason: local path exists
  - id: A-007
    name: fixture_package_m1
    required: true
    status: ok
    path: 1_asset/fixture_package_m1
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/fixture_package_m1
    reason: local path exists
  - id: A-008
    name: data_manifest_fixture_m1_readme
    required: true
    status: ok
    path: 1_asset/data_manifest_fixture_m1_readme.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_data_manifest_fixture_m1/4_artifact/2_persist/data_manifest_fixture_m1_readme.md
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-047 resource_loader_hardening_m1

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1/5_report/handoff_check_before_exec.md` 是否已写
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
