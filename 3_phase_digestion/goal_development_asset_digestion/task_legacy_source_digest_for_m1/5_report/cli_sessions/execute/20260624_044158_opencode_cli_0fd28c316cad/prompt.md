# Execution Prompt
Generated: 2026-06-24 03:35

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-041
name: legacy_source_digest_for_m1
phase: digestion
goal: goal_development_asset_digestion
project: P-012
objective: 'Digest the explicitly registered migrated PxFquery package source for
  the M1 Python-package milestone. Use T-007 as the trusted source map and read only
  its registered migrated package-code asset path, not the whole project asset tree.
  Deliver a concise reusable source digest: candidate modules/functions, entry points,
  data/index access patterns, known unusable or risky legacy parts, and exact recommendations
  for what later development tasks may reference. This task must not write implementation
  code and must not modify legacy or completed task artifacts.'
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
notes: 'Constraint supplement for config AI: This digestion task is the only new DAG
  task allowed to read the explicit legacy package-source path exposed through T-007
  registered assets. Do not scan the whole project asset tree. Do not modify legacy
  files or completed task artifacts. Deliver reusable source digest only.'
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T03:35:09'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: T-007 development source map
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-001
  origin: T-007/D-001
  registered: '2026-06-24'
  path: 1_asset/T-007 development source map.md
  symlink: true
  status: ready
  notes: Trusted source map defining the migrated PxFquery package-code path and source
    priority rules. Execution must use this to locate the package source, not scan
    the whole project asset tree.
  location: local
- id: A-002
  name: T-007 development state report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002
  registered: '2026-06-24'
  path: 1_asset/T-007 development state report.md
  symlink: true
  status: ready
  notes: Summarizes component status, data/index readiness, and validation state from
    T-007. Execution uses this as secondary confirmation, not as the primary source
    authority.
  location: local
- id: A-003
  name: Migrated PxFquery package source
  type: code
  source: project_asset
  source_task: null
  source_artifact_id: null
  origin: legacy_flat_asset_library_v20260614/code/pxfquery_package/
  registered: '2026-06-24'
  path: 1_asset/Migrated PxFquery package source
  symlink: true
  status: ready
  notes: The only legacy package-source directory this task is allowed to read. Identified
    by T-007/D-001 source map. Contains core.py, data/, index/, query/, llm/, viz/,
    utils.py, logging_utils.py, and legacy stubs.
  location: local
- id: A-004
  name: T-007 module asset status matrix
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-003
  origin: T-007/D-003
  registered: '2026-06-24'
  path: 1_asset/T-007 module asset status matrix.csv
  symlink: true
  status: ready
  notes: Optional reference for component status and data asset location. Execution
    may use this to verify module availability when the source map or report is ambiguous.
  location: local
- id: A-005
  name: T-007 development gap and risk list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005
  registered: '2026-06-24'
  path: 1_asset/T-007 development gap and risk list.md
  symlink: true
  status: ready
  notes: Optional reference for known gaps, risks, and claims to avoid. Execution
    may use this to confirm identified unusable or risky legacy parts.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/2_protocol/2_protocol_split/protocol.md`

```text
# Protocol: legacy_source_digest_for_m1

## Objective

Digest the explicitly allowed migrated PxFquery package source into a small reusable M1 reference asset. The task identifies which legacy modules, functions, entry points, data/index access patterns, and known risks should inform the M1 Python package DAG. It does not implement new package code, does not modify legacy files, and does not scan the whole project asset tree.

## Inputs

- A-001: T-007 development source map — use as the authority for the migrated package-source path and source priority.
- A-002: T-007 development state report — use as secondary context for package component status, data/index readiness, and validation state.
- A-003: Migrated PxFquery package source — the only legacy package-source directory this task may inspect.
- A-004: T-007 module asset status matrix — optional tabular cross-check for module and asset status.
- A-005: T-007 development gap and risk list — optional risk cross-check for unsafe legacy components and claims to avoid.

## Steps

1. Confirm the registered A-003 package-source directory exists and limit source inspection to that directory.
2. Inventory top-level package files and modules, including core API, loader, query, index, resolver/LLM, visualization, utilities, and obvious stubs.
3. Identify candidate code and concepts that downstream M1 tasks may safely reference: loader API ideas, forward query logic, reverse query logic, index access patterns, no-hit behavior, and package entry points.
4. Identify unsafe or non-reusable legacy pieces: hard-coded relative paths, pass stubs, NotImplementedError paths, fragile LLM calls, stale README/main entry points, and direct assumptions about old working directories.
5. Produce a concise M1 reuse recommendation table that maps each downstream task type to allowed legacy references and forbidden legacy references.
6. Write deliverables under `4_artifact/` and register them in `4_artifact/registry.yaml`.

## Constraints

- This digestion task is the only new M1 DAG task allowed to inspect the explicit legacy package-source path.
- Do not scan arbitrary project assets or the entire `2_project_asset/` tree.
- Do not modify files under the legacy source path, T-007, or any completed task.
- Do not write M1 implementation code for T046-T053.
- Do not use T024-T040 outputs as authorities.
- If a useful source path is outside A-003, mention it as a gap or future digestion need rather than opening it.

## Deliverables

- `4_artifact/2_persist/legacy_source_digest_m1.md`: concise source digest with package structure, reusable modules, risks, and M1 recommendations.
- `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv`: table of modules/files, status, reuse recommendation, downstream task relevance, and risk notes.
- `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml`: machine-readable allowed/forbidden legacy reference boundaries for downstream tasks.
- `4_artifact/registry.yaml`: registry entries for all reusable deliverables.
- `5_report/completion.md`: completion note including the exact source path inspected and confirmation that no broader project asset scan was performed.

## Acceptance

- The source digest names concrete files/modules and gives direct guidance for T046, T048, T049, and T052.
- The reuse matrix distinguishes usable, risky, incomplete, and forbidden legacy pieces.
- The boundary YAML clearly states that downstream development tasks must use T041 outputs rather than reading raw legacy source directly.
- The task does not create or modify implementation code outside its own `4_artifact/` and `5_report/`.
- The deliverables are registered in `4_artifact/registry.yaml`.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
version: 1
required:
  - A-001
  - A-003
optional:
  - A-002
  - A-004
  - A-005
forbidden:
  - path: /Users/dudu/Documents/3_Project/8_functional_query
    reason: Use the migrated registered package source, not the old historical root.
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1
    reason: T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1
    reason: T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1
    reason: T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resolver_optional_layer_v1
    reason: T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
  - path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1
    reason: T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
modifiable:
  - 2_protocol/2_protocol_split/protocol.md
  - 2_protocol/3_asset_rule/asset_rule.yaml
  - 1_asset/registration.yaml
  - 4_artifact/
  - 5_report/
non_modifiable:
  - /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package
  - /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state
output:
  - path: 4_artifact/2_persist/legacy_source_digest_m1.md
    reason: Human-readable reusable source digest.
  - path: 4_artifact/5_table/legacy_module_reuse_matrix_m1.csv
    reason: Machine-checkable module reuse matrix.
  - path: 4_artifact/2_persist/legacy_reference_boundaries_m1.yaml
    reason: Downstream raw-source access boundary for M1 tasks.
  - path: 5_report/completion.md
    reason: Completion note and source-scope confirmation.
notes:
  - A-003 is the only allowed legacy package-source directory from project assets.
  - Do not scan the broad 2_project_asset tree; read only registered assets and the A-003 symlink.
  - This task digests source into reusable references; it must not implement M1 package code.

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-041 legacy_source_digest_for_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1`
- Allowed write dirs: `4_artifact/`, `5_report/`, `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`, `1_asset/registration.yaml`
- Forbidden dirs: `/Users/dudu/Documents/3_Project/8_functional_query` (historical root), `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1` (T024-T040 failed route), `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resolver_optional_layer_v1`, `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1`. Also forbidden: arbitrary `2_project_asset/` scanning, completed task folders outside registered assets, legacy package source modifications.
- Required registry: `4_artifact/registry.yaml` (exists, currently empty).
- Must stop if: A-003 directory is inaccessible/unreadable; any required asset becomes missing; source map contradicts A-003 path; protocol scope drifts beyond A-003.

## Objective Restatement
Digest the migrated PxFquery package source (at the single path registered in T-007's source map) into a concise M1 reference asset: inventory the package structure, identify reusable modules/functions/patterns, flag unsafe or non-reusable legacy parts, and produce a reuse matrix + boundary YAML so downstream M1 tasks (T046, T048, T049, T052) can use digested knowledge instead of reading raw legacy source.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/T-007 development source map.md` | Authority for A-003 path and source priority | ok |
| A-002 | `1_asset/T-007 development state report.md` | Secondary context for component status/readiness | ok |
| A-003 | `1_asset/Migrated PxFquery package source` (→ `legacy_flat_asset_library_v20260614/code/pxfquery_package`) | Only legacy package-source directory to inspect | ok |
| A-004 | `1_asset/T-007 module asset status matrix.csv` | Optional cross-check for module/asset status | ok |
| A-005 | `1_asset/T-007 development gap and risk list.md` | Optional risk cross-check for unsafe components | ok |

## Execution Strategy
1. Read A-001 (source map) to confirm A-003 path and understand source priority rules.
2. Read A-003 directory tree: inventory top-level files/modules (core.py, data/, index/, query/, llm/, viz/, utils.py, logging_utils.py, stubs).
3. Read individual package files in A-003 to identify: entry points, loader API patterns, forward/reverse query logic, index access patterns, no-hit behavior.
4. Read A-005 (gap/risk list) for cross-reference on unsafe legacy parts; read A-002/A-004 if ambiguity arises.
5. Produce three deliverables:
   - `4_artifact/2_persist/legacy_source_digest_m1.md`: concise human-readable source digest.
   - `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv`: module/file status + reuse recommendation + downstream task mapping.
   - `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml`: machine-readable allowed/forbidden reference boundaries.
6. Register deliverables in `4_artifact/registry.yaml`.
7. Write `5_report/completion.md` with exact A-003 path and scope confirmation.

## Conservative Execution Advice
- Start with: Read A-001 source map → confirm A-003 path is correct → list A-003 top-level contents.
- Smoke/demo command or method: `ls -R` on A-003 to verify directory structure matches expectations before detailed reading.
- Full run only after: Source map confirms A-003 is the correct and sufficient path; no ambiguity about which files belong to package source vs. unrelated files.
- Cost/time risk: Low — all reads are local filesystem. No API calls, no network, no compute-heavy processing.
- Checkpoint advice: After step 2 (inventory), confirm the structure vs. expected modules listed in the protocol. If a major module is missing, flag in digest rather than blocking.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Source digest | `4_artifact/2_persist/legacy_source_digest_m1.md` | Names concrete files/modules, gives guidance for T046/T048/T049/T052 |
| Reuse matrix | `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv` | Distinguishes usable/risky/incomplete/forbidden entries |
| Boundary YAML | `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml` | States downstream tasks must use T-041 outputs, not raw legacy source |
| Completion note | `5_report/completion.md` | Documents exact A-003 path inspected, confirms no broader scan |
| Registry | `4_artifact/registry.yaml` | All deliverable paths registered |

## Failure / Stop Conditions
- A-003 symlink broken or target missing → block, write `5_report/blocked.md`.
- Source map (A-001) reports a different package path than resolved A-003 → block for contradiction.
- Any attempt to read outside A-003 within legacy package tree → stop, document gap, do not expand scope.
- Artifact registry write fails due to permissions → stop and report.

## Notes For Delivery QA
- All deliverables must refer only to A-003 content; no external package scanning.
- Reuse matrix must explicitly map to downstream task IDs (T046, T048, T049, T052).
- Boundary YAML must forbid downstream tasks from reading raw legacy source directly — they must consume T-041 outputs.
- The task must NOT write any implementation code for M1.
- The completion note must affirm that `2_project_asset/` was not broadly scanned.
- Established symlinks verified: all 5 assets link to valid resolved targets. No repair needed.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-041 legacy_source_digest_for_m1
Status: active | Executor: hybrid
Objective: Digest the explicitly registered migrated PxFquery package source for the M1 Python-package milestone. Use T-007 as the trusted source map and read only its registered migrated package-code asset path, not the whole project asset tree. Deliver a concise reusable source digest: candidate modules/functions, entry points, data/index access patterns, known unusable or risky legacy parts, and exact recommendations for what later development tasks may reference. This task must not write implementation code and must not modify legacy or completed task artifacts.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# Protocol: legacy_source_digest_for_m1

## Objective

Digest the explicitly allowed migrated PxFquery package source into a small reusable M1 reference asset. The task identifies which legacy modules, functions, entry points, data/index access patterns, and known risks should inform the M1 Python package DAG. It does not implement new package code, does not modify legacy files, and does not scan the whole project asset tree.

## Inputs

- A-001: T-007 development source map — use as the authority for the migrated package-source path and source priority.
- A-002: T-007 development state report — use as secondary context for package component status, data/index readiness, and validation state.
- A-003: Migrated PxFquery package source — the only legacy package-source directory this task may inspect.
- A-004: T-007 module asset status matrix — optional tabular cross-check for module and asset status.
- A-005: T-007 development gap and risk list — optional risk cross-check for unsafe legacy components and claims to avoid.

## Steps

1. Confirm the registered A-003 package-source directory exists and limit source inspection to that directory.
2. Inventory top-level package files and modules, including core API, loader, query, index, resolver/LLM, visualization, utilities, and obvious stubs.
3. Identify candidate code and concepts that downstream M1 tasks may safely reference: loader API ideas, forward query logic, reverse query logic, index access patterns, no-hit behavior, and package entry points.
4. Identify unsafe or non-reusable legacy pieces: hard-coded relative paths, pass stubs, NotImplementedError paths, fragile LLM calls, stale README/main entry points, and direct assumptions about old working directories.
5. Produce a concise M1 reuse recommendation table that maps each downstream task type to allowed legacy references and forbidden legacy references.
6. Write deliverables under `4_artifact/` and register them in `4_artifact/registry.yaml`.

## Constraints

- This digestion task is the only new M1 DAG task allowed to inspect the explicit legacy package-source path.
- Do not scan arbitrary project assets or the entire `2_project_asset/` tree.
- Do not modify files under the legacy source path, T-007, or any completed task.
- Do not write M1 implementation code for T046-T053.
- Do not use T024-T040 outputs as authorities.
- If a useful source path is outside A-003, mention it as a gap or future digestion need rather than opening it.

## Deliverables

- `4_artifact/2_persist/legacy_source_digest_m1.md`: concise source digest with package structure, reusable modules, risks, and M1 recommendations.
- `4_artifact/5_table/legacy_module_reuse_matrix_m1.csv`: table of modules/files, status, reuse recommendation, downstream task relevance, and risk notes.
- `4_artifact/2_persist/legacy_reference_boundaries_m1.yaml`: machine-readable allowed/forbidden legacy reference boundaries for downstream tasks.
- `4_artifact/registry.yaml`: registry entries for all reusable deliverables.
- `5_report/completion.md`: completion note including the exact source path inspected and confirmation that no broader project asset scan was performed.

## Acceptance

- The source digest names concrete files/modules and gives direct guidance for T046, T048, T049, and T052.
- The reuse matrix distinguishes usable, risky, incomplete, and forbidden legacy pieces.
- The boundary YAML clearly states that downstream development tasks must use T041 outputs rather than reading raw legacy source directly.
- The task does not create or modify implementation code outside its own `4_artifact/` and `5_report/`.
- The deliverables are registered in `4_artifact/registry.yaml`.

### Selected Assets (5)
- A-001 [document] T-007 development source map — path: 1_asset/T-007 development source map.md — origin: T-007/D-001
- A-002 [document] T-007 development state report — path: 1_asset/T-007 development state report.md — origin: T-007/D-002
- A-003 [code] Migrated PxFquery package source — path: 1_asset/Migrated PxFquery package source — origin: legacy_flat_asset_library_v20260614/code/pxfquery_package/
- A-004 [table] T-007 module asset status matrix — path: 1_asset/T-007 module asset status matrix.csv — origin: T-007/D-003
- A-005 [document] T-007 development gap and risk list — path: 1_asset/T-007 development gap and risk list.md — origin: T-007/D-005

### Asset Rules

### Required
- A-001
- A-003
### Forbidden
- /Users/dudu/Documents/3_Project/8_functional_query — Use the migrated registered package source, not the old historical root.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resolver_optional_layer_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
### Output
- 4_artifact/2_persist/legacy_source_digest_m1.md — Human-readable reusable source digest.
- 4_artifact/5_table/legacy_module_reuse_matrix_m1.csv — Machine-checkable module reuse matrix.
- 4_artifact/2_persist/legacy_reference_boundaries_m1.yaml — Downstream raw-source access boundary for M1 tasks.
- 5_report/completion.md — Completion note and source-scope confirmation.

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

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_development_asset_digestion/task_legacy_source_digest_for_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_for_m1/5_report/execution_handoff.md`

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
