# Delivery QA Prompt
Generated: 2026-06-24 17:34

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
notes: 'T061 recovery: prior check_review was based on deterministic local evidence
  but CyHex fast-pass requires a completed check session. Rolled back to check_interrupted
  to start a minimal recovery check session using 2_protocol/0_prompt/2026-06-24_1710_minimal_check_recovery_prompt.md.
  Existing evidence: 5_report/deterministic_check_20260624_1656.md and 5_report/handoff_check_before_exec.md.'
fast_pass_permission: green
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T17:06:12'
auto_recovery:
  execute:
    source_session_id: cli_dcacea2b0cc1
    attempts: 1
    last_attempt_at: '2026-06-24T17:18:17'

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

### Current Task Protocol: protocol.md
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
- Stop if completing the digest requires reading outside A-002 or outside the allowed predecessor context.
- Stop if package files are too large to inspect safely with bounded static windows; report the limitation instead of dumping contents.
- Stop if execution would require running package code, rebuilding indexes, reading matrices, or using T-041 outputs as authority.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
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

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-061 legacy_source_digest_repair_m1

## Check Verdict
yellow_repair

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: T-041 task files, predecessor task directories, project protocol directories, registered project assets, historical source root `/Users/dudu/Documents/3_Project/8_functional_query`, and broad unregistered `2_project_asset/` paths outside A-002.
- Required registry: `1_asset/registration.yaml`
- Must stop if: A-001 or A-002 is missing, A-002 resolves outside the registered migrated package-source path, the digest would require reading T-041 outputs as authority, execution would need raw matrices/notebooks/binaries, or execution would need to modify legacy/project assets.

## Objective Restatement
Create a clean replacement digestion asset for the failed T-041 role. The execution AI should use T-007 as the trusted source map, inspect only the registered migrated PxFquery package-source directory, and produce a concise source digest, module reuse matrix, and downstream reference-boundary YAML for future M1/M1.1 development tasks. This task must not implement package code or promote outputs into final project deliverables.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t007_development_source_map.md` | Trusted T-007 source map for migrated package path and source-priority context. | ready; symlink resolves to existing file |
| A-002 | `1_asset/migrated_pxfquery_package_source` | Only raw legacy package-source directory allowed for bounded static inspection. | ready; symlink resolves to existing directory with about 30 files at max depth 2 |

## Execution Strategy
1. Confirm A-001 and A-002 still resolve to the paths registered in `1_asset/registration.yaml`; stop on mismatch.
2. Inventory A-002 filenames and sizes first, saving notes or helper output under `3_execution/`.
3. Inspect only Python/source files under A-002 with bounded windows. Prefer imports, classes, functions, constants, and entry-point behavior; do not dump whole large files.
4. Classify each relevant module/file as reusable, adaptable/risky, incomplete, or forbidden for downstream M1/M1.1 tasks.
5. Record data/index access assumptions, hard-coded paths, LLM/API coupling, missing runtime assets, and downstream risks.
6. Write the three required reusable outputs under `4_artifact/`, then write reports, registry, and completion note.

## Conservative Execution Advice
- Start with: `find 1_asset/migrated_pxfquery_package_source -maxdepth 2 -type f -print` plus file sizes.
- Smoke/demo command or method: inspect a small subset first, such as package entry points and query-related modules, then expand to all Python files.
- Full run only after: A-001 and A-002 resolve correctly and no forbidden path is needed.
- Cost/time risk: low to moderate; this is static source digestion, not code execution or matrix analysis.
- Checkpoint advice: if any file appears too large, inspect only targeted symbol windows and document the skipped regions.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Replacement source digest | `4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Names concrete modules/classes/functions and classifies reuse status. |
| Module reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv` | One row per relevant module/file with reuse status, downstream relevance, risks, and recommended action. |
| Legacy reference boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Machine-readable rules for what later tasks may cite, adapt, or must avoid. |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | Explains bounded-read method and execution steps. |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | Summarizes accepted findings and downstream use. |
| Artifact registry | `4_artifact/registry.yaml` | Registers all accepted outputs. |
| Completion note | `5_report/completion.md` | States what was produced and what was intentionally not done. |

## Failure / Stop Conditions
- A required asset is missing, empty, or resolves outside the registered boundary.
- Execution needs to read T-041 outputs as authoritative evidence.
- Execution needs unregistered project assets, historical source root files, raw h5ad matrices, notebooks, binaries, caches, or generated reports.
- Execution needs to run package workflows, rebuild indexes, perform biological analysis, perform web search, or write implementation code.
- The package-source inspection cannot be completed without dumping large files verbatim.

## Notes For Delivery QA
- Delivery QA should verify that outputs are fresh T-061 artifacts, not copied from T-041.
- Delivery QA should check that the digest documents the bounded-read method and the A-002 file inventory.
- Delivery QA should confirm the registry points only to T-061 outputs under `4_artifact/`.
- Delivery QA should treat this as a digestion/reference asset, not as a package milestone deliverable.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/registry.yaml`

```text
artifacts:
  - id: D-001
    name: legacy_source_digest_repair_m1
    type: document
    path: 2_persist/legacy_source_digest_repair_m1.md
    status: ready
    created: "2026-06-24"
    provenance:
      - A-001
      - A-002
    notes: "Fresh bounded replacement digest for M1/M1.1 legacy package-source reuse; T-041 not used as authority."
  - id: D-002
    name: legacy_module_reuse_matrix_repair_m1
    type: table
    path: 5_table/legacy_module_reuse_matrix_repair_m1.csv
    status: ready
    created: "2026-06-24"
    provenance:
      - A-001
      - A-002
    notes: "Module/file-level reuse classification matrix with risks and recommended downstream actions."
  - id: D-003
    name: legacy_reference_boundaries_repair_m1
    type: document
    path: 2_persist/legacy_reference_boundaries_repair_m1.yaml
    status: ready
    created: "2026-06-24"
    provenance:
      - A-001
      - A-002
    notes: "Machine-readable downstream citation, adaptation, and avoidance rules."
  - id: D-004
    name: execution_report_v20260624
    type: report
    path: 3_document/execution_report_v20260624.html
    status: ready
    created: "2026-06-24"
    provenance:
      - A-001
      - A-002
    notes: "Execution method and evidence report."
  - id: D-005
    name: result_report_v20260624
    type: report
    path: 3_document/result_report_v20260624.html
    status: ready
    created: "2026-06-24"
    provenance:
      - A-001
      - A-002
    notes: "Human-facing result summary for delivered digest outputs."

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/completion.md`

```text
# Completion

Task: T-061 legacy_source_digest_repair_m1

Date: 2026-06-24

Status: completed

## Completed Steps

1. Verified A-001 and A-002 resolved to the registered T-007 source map and migrated package-source directory.
2. Confirmed CyHex local API availability once; app version 1.2.19.
3. Inventoried A-002 only using symlink-following bounded commands; recorded 25 files and 22 Python files.
4. Performed static-only source inspection through line counts, grep indexes, AST structure, and targeted source windows.
5. Classified legacy modules as reusable, adaptable/risky, incomplete, or forbidden for downstream M1/M1.1 use.
6. Wrote the required digest, reuse matrix, reference-boundary YAML, execution report, result report, and artifact registry.

## Deliverables Produced

- `4_artifact/2_persist/legacy_source_digest_repair_m1.md`
- `4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv`
- `4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Evidence Files In 3_execution

- `3_execution/a002_file_inventory_20260624.txt`
- `3_execution/a002_python_symbol_index_20260624.txt`
- `3_execution/a002_definitions_20260624.txt`
- `3_execution/a002_ast_structure_20260624.txt`
- `3_execution/a002_risk_pattern_index_20260624.txt`

## Boundary Statement

No package workflows were run. No implementation code was written. No matrix files, notebooks, caches, generated reports, broad project asset paths, historical source root files, or T-041 outputs were read as authority. Web search was not used.

## Caveats

This was a source-digestion task only. It did not validate runtime behavior against real h5ad matrices or JSON query indexes. Downstream implementation tasks must register those assets and run deterministic tests before treating the legacy logic as operational.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-061 | Name: legacy_source_digest_repair_m1
- Objective: Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and read only the explicitly registered migrated PxFquery package-source path, not the whole project asset tree. Reference T-041 only as a failed historical attempt and do not reuse its outputs as authoritative. Deliver a fresh concise source digest, module reuse matrix, and legacy reference boundary YAML for downstream M1/M1.1 development tasks. This task must not write implementation code and must not modify legacy files or completed task artifacts.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1`

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
# AI Handoff: T-061 legacy_source_digest_repair_m1

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
# Delivery QA: T-061 legacy_source_digest_repair_m1

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
