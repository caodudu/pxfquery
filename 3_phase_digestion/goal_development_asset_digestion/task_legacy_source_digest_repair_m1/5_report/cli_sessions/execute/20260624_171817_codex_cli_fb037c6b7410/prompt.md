# Execution Prompt
Generated: 2026-06-24 17:06

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
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T17:06:12'

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
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml

Interpretation:

- `handoff_check_before_exec.md` is the execution strategy and risk guidance.
- `protocol.md` is the task contract.
- If they conflict, stop and write `5_report/blocked.md`. Do not guess.
- `registration.yaml` and `asset_rule.yaml` define the selected inputs. Do not perform a new asset discovery pass.
- `execution_handoff.md`, if present, is only for continuing an interrupted or long-context execution session.

## 2. Task Contract

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: digestion
Task: T-061 legacy_source_digest_repair_m1
Status: active | Executor: hybrid
Objective: Create a clean replacement legacy source digest for the M1 Python-package milestone. Use T-007 as the trusted source map and read only the explicitly registered migrated PxFquery package-source path, not the whole project asset tree. Reference T-041 only as a failed historical attempt and do not reuse its outputs as authoritative. Deliver a fresh concise source digest, module reuse matrix, and legacy reference boundary YAML for downstream M1/M1.1 development tasks. This task must not write implementation code and must not modify legacy files or completed task artifacts.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
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

### Selected Assets (2)
- A-001 [document] t007_development_source_map — path: 1_asset/t007_development_source_map.md — origin: T-007/D-001
- A-002 [package] migrated_pxfquery_package_source — path: 1_asset/migrated_pxfquery_package_source — origin: T-007/D-001 package source map entry

### Asset Rules

### Required
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md — Trusted source map that identifies the migrated PxFquery package-source path and source-priority rules.
- /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/ — Only raw legacy package-source directory allowed for bounded static inspection in this digestion repair task.
### Forbidden
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/4_artifact/ — T-041 outputs are failed/context only and must not be reused as authoritative inputs.
- /Users/dudu/Documents/3_Project/8_functional_query — Historical source root is outside this task's allowed source boundary.
- unregistered paths under /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/ — Broad project-asset scanning is forbidden; execution may inspect only the registered A-002 package-source directory.
- **/__pycache__/** — Cache files are not source evidence.
- **/*.h5ad — Matrix/data files are outside the static source-digest scope.
- **/*.ipynb — Notebooks are outside the static source-digest scope.
### Output
- 4_artifact/2_persist/legacy_source_digest_repair_m1.md
- 4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv
- 4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml
- 4_artifact/3_document/execution_report_v20260624.html
- 4_artifact/3_document/result_report_v20260624.html
- 4_artifact/registry.yaml
- 5_report/completion.md

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

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/5_report/execution_handoff.md`

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
