# Checking Prompt
Generated: 2026-06-24 13:45

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-061
name: legacy_source_digest_repair_m1
phase: digestion
goal: goal_development_asset_digestion
project: P-012
objective: Create a clean replacement legacy source digest for the M1 Python-package
  milestone. Use T-007 as the trusted source map and read only the explicitly registered
  migrated PxFquery package-source path, not the whole project asset tree. Reference
  T-041 only as a failed historical attempt and do not reuse its outputs as authoritative.
  Deliver a fresh concise source digest, module reuse matrix, and legacy reference
  boundary YAML for downstream M1/M1.1 development tasks. This task must not write
  implementation code and must not modify legacy files or completed task artifacts.
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
notes: 'Bypass replacement for T-041. Special constraints for config/execution AI:
  treat T-041 as failed/context only; do not mark it done and do not depend on its
  artifacts. Large-file guardrail: do not dump or read entire large source/data files
  verbatim. First list filenames and sizes; for each Python file, inspect imports/classes/functions
  with bounded sed/rg windows, preferably under 200 lines per file unless a targeted
  symbol requires more. Do not read binary data, h5ad matrices, notebooks, caches,
  __pycache__, or generated reports. The only raw legacy source allowed is the explicit
  package path exposed by T-007. Required deliverables: 4_artifact/2_persist/legacy_source_digest_repair_m1.md,
  4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv, 4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml,
  execution/result reports, registry, and completion note. Acceptance requires the
  digest to name concrete modules/functions, classify reusable/risky/forbidden pieces,
  state exact downstream reference rules, and document the bounded-read method used.'
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T13:45:04'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: t007_development_source_map
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-001
  origin: T-007/D-001
  registered: '2026-06-24'
  path: 1_asset/t007_development_source_map.md
  symlink: true
  status: ready
  notes: Trusted source map for locating and bounding the migrated PxFquery package-source
    asset.
  location: local
- id: A-002
  name: migrated_pxfquery_package_source
  type: package
  source: project_asset
  source_task: T-007
  source_artifact_id: pxfquery_package_path_from_T007_D001
  origin: T-007/D-001 package source map entry
  registered: '2026-06-24'
  path: 1_asset/migrated_pxfquery_package_source
  symlink: true
  status: ready
  notes: Only raw legacy source directory execution may inspect, using bounded static
    source-reading rules.
  location: local

```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-061 legacy_source_digest_repair_m1 — Protocol

## Objective

Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and inspect only the explicitly registered migrated PxFquery package-source directory. Treat T-041 as a failed historical attempt and do not reuse its outputs as authoritative evidence.

This is a digestion task. It must not write implementation code, run package workflows, modify legacy files, modify completed task artifacts, or promote outputs into project deliverables.

## Position In Project

T-061 replaces the failed/unsafe dependency role that T-041 was intended to serve. Its outputs should give later M1/M1.1 development tasks a concise, bounded, and auditable reference for which legacy package modules can be reused, adapted, or avoided.

T-007 remains the authority for the migrated package-source path and overall development-state source map. T-041 may be mentioned only to explain why a replacement digest was needed.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Trusted source map identifying the migrated PxFquery package-source path and relevant source-priority rules. |
| A-002 | project_asset via T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/` | The only raw legacy package-source directory allowed for bounded static inspection in this task. |

## Execution Steps

1. Confirm the registered A-001 source map and A-002 package-source directory are available; stop if A-002 resolves outside the registered migrated package path.
2. Inventory A-002 filenames and file sizes first. Do not recursively read caches, notebooks, binaries, generated reports, matrix/data files, or `__pycache__`.
3. For each Python source file under A-002, inspect imports, classes, functions, key constants, and entry-point behavior using bounded windows. Prefer no more than 200 source lines per file unless a specific symbol requires a targeted extra window.
4. Identify concrete reusable, adaptable/risky, incomplete, and forbidden pieces for M1/M1.1 development. Name modules, classes, and functions where possible.
5. Record data/index access patterns, hard-coded path assumptions, LLM/API coupling, missing runtime assets, and other downstream risks without executing package code.
6. Write a concise markdown source digest to `4_artifact/2_persist/legacy_source_digest_repair_m1.md`.
7. Write a CSV module reuse matrix to `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`.
8. Write a machine-readable downstream reference-boundary YAML to `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`.
9. Create execution/result reports, update `4_artifact/registry.yaml`, and write `5_report/completion.md`.

## Constraints

- Use T-007/D-001 as the source authority for the package-source path.
- Inspect only A-002 as raw legacy source.
- Use bounded static inspection; do not dump large files verbatim.
- Document the bounded-read method in the digest or execution report.
- Keep all generated analysis notes, scripts, and temporary logs in `3_execution/`.
- Put reusable accepted outputs only under `4_artifact/`.
- Preserve provenance for every conclusion that depends on A-001 or A-002.

## Forbidden

- Do not use T-041 outputs as authoritative inputs.
- Do not mark T-041 complete, repair T-041, or modify any T-041 file.
- Do not scan the whole `2_project_asset/` tree.
- Do not read the historical source root `/Users/dudu/Documents/3_Project/8_functional_query`.
- Do not read raw h5ad matrices, notebooks, binary data, caches, `__pycache__`, or generated reports inside package/source-adjacent paths.
- Do not run package workflows, rebuild indexes, perform biological analysis, perform web search, or write implementation code.
- Do not modify project protocol, predecessor task directories, completed artifacts, or legacy asset files.

## Web Search Allowance

Allowed: no

Reason: The task is a local digestion repair based on T-007 and a registered migrated package-source path. No current external or web evidence is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Replacement source digest | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | yes |
| Module reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | yes |
| Legacy reference boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The digest names concrete modules, classes, functions, and entry points inspected from A-002.
- The digest clearly classifies legacy pieces as reusable, adaptable/risky, incomplete, or forbidden for downstream M1/M1.1 use.
- The CSV matrix contains one row per relevant module/file with reuse status, downstream relevance, risks, and recommended action.
- The boundary YAML states exact downstream reference rules, including what later tasks may cite, adapt, or must avoid.
- T-041 is described only as failed/context and none of its artifacts are used as authority.
- The bounded-read method is documented, including filename/size inventory and per-file inspection limits.
- No implementation code, old-root reads, broad project-asset scans, raw data reads, or web searches are performed.

## Failure / Stop Rules

- Stop if A-001 or A-002 is unavailable or resolves to an unexpected path.
- Stop if completing t

...[truncated by CyHex prompt assembler: 670 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
    reason: Trusted source map that identifies the migrated PxFquery package-source path and source-priority rules.
  - id: A-002
    source_task: project_asset
    source_artifact_id: pxfquery_package_path_from_T007_D001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/
    reason: Only raw legacy package-source directory allowed for bounded static inspection in this digestion repair task.
optional: []
forbidden:
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/4_artifact/
    reason: T-041 outputs are failed/context only and must not be reused as authoritative inputs.
  - path: /Users/dudu/Documents/3_Project/8_functional_query
    reason: Historical source root is outside this task's allowed source boundary.
  - path: unregistered paths under /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/
    reason: Broad project-asset scanning is forbidden; execution may inspect only the registered A-002 package-source directory.
  - path: "**/__pycache__/**"
    reason: Cache files are not source evidence.
  - path: "**/*.h5ad"
    reason: Matrix/data files are outside the static source-digest scope.
  - path: "**/*.ipynb"
    reason: Notebooks are outside the static source-digest scope.
output:
  - path: 4_artifact/2_persist/legacy_source_digest_repair_m1.md
    type: document
  - path: 4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv
    type: table
  - path: 4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml
    type: document
  - path: 4_artifact/3_document/execution_report_v20260624.html
    type: report
  - path: 4_artifact/3_document/result_report_v20260624.html
    type: report
  - path: 4_artifact/registry.yaml
    type: registry
  - path: 5_report/completion.md
    type: report
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - project protocol directories
  - legacy source root
  - registered project assets
  - /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/

```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: digestion
Task ID: T-061 | Name: legacy_source_digest_repair_m1
Status: active | Executor: hybrid
Objective: Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and read only the explicitly registered migrated PxFquery package-source path, not the whole project asset tree. Reference T-041 only as a failed historical attempt and do not reuse its outputs as authoritative. Deliver a fresh concise source digest, module reuse matrix, and legacy reference boundary YAML for downstream M1/M1.1 development tasks. This task must not write implementation code and must not modify legacy files or completed task artifacts.
Notes / User Natural-Language Intent: Bypass replacement for T-041. Special constraints for config/execution AI: treat T-041 as failed/context only; do not mark it done and do not depend on its artifacts. Large-file guardrail: do not dump or read entire large source/data files verbatim. First list filenames and sizes; for each Python file, inspect imports/classes/functions with bounded sed/rg windows, preferably under 200 lines per file unless a targeted symbol requires more. Do not read binary data, h5ad matrices, notebooks, caches, __pycache__, or generated reports. The only raw legacy source allowed is the explicit package path exposed by T-007. Required deliverables: 4_artifact/2_persist/legacy_source_digest_repair_m1.md, 4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv, 4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml, execution/result reports, registry, and completion note. Acceptance requires the digest to name concrete modules/functions, classify reusable/risky/forbidden pieces, state exact downstream reference rules, and document the bounded-read method used.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: digestion
  project_asset_access: allowed
  zero_assets: false
  total_assets: 2
  symlink_sync:
    checked: 2
    linked: 2
    skipped: 0
    changed: false
  counts:
    ok: 2
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: t007_development_source_map
    required: true
    status: ok
    path: 1_asset/t007_development_source_map.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
    reason: local path exists
  - id: A-002
    name: migrated_pxfquery_package_source
    required: true
    status: ok
    path: 1_asset/migrated_pxfquery_package_source
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-061 legacy_source_digest_repair_m1

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md` 是否已写
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
