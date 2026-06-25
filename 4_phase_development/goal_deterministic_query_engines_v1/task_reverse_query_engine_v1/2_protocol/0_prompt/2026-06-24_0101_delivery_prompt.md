# Delivery QA Prompt
Generated: 2026-06-24 01:01

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-030
name: reverse_query_engine_v1
phase: development
goal: goal_deterministic_query_engines_v1
project: P-012
objective: Create pxfquery-{task_id} reverse query engine deliverable. Reproduce apoptosis
  activation/MYC suppression style candidate ranking with serializable outputs and
  reports.
executor: hybrid
agent_id: null
config_agent_id: null
check_agent_id: null
execute_agent_id: null
server_id: null
status: blocked
cyhex_version: 1.2.3
created: '2026-06-23'
started: null
completed: '2026-06-23'
notes: 反向查询引擎构建
fast_pass_permission: green
sub_status: null
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-23T08:46:53'
fast_pass_accepted: true
fast_pass_accepted_at: '2026-06-23T08:48:14'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/1_asset/registration.yaml`

```text
assets:
  - id: A-001
    name: T-024 workspace package (pxfquery-T-024)
    type: deliverable
    source: predecessor
    origin: goal_package_foundation_v1/task_workspace_package_v1
    registered: '2026-06-23'
    path: 1_asset/T-024 workspace package (pxfquery-T-024)
    symlink: true
    notes: Current pxfquery workspace with src/-layout, ReverseQuery class, ReverseResult,
      DataLoader, and core.PxFquery. Installed as editable into pxfquery conda env for
      demo execution. Symlink target verified: ../goal_package_foundation_v1/task_workspace_package_v1/4_artifact/2_persist/workspace/
    location: local
  - id: A-002
    name: T-026 loader outputs (pxfquery-T-026)
    type: deliverable
    source: predecessor
    origin: goal_resource_index_packs_v1/task_matrix_loader_v1
    registered: '2026-06-23'
    path: 1_asset/T-026 loader outputs (pxfquery-T-026)
    symlink: true
    notes: pxfquery-T-026 loader package (load_bundle, load_matrix) and loader_validation.json
      recording observed matrix shapes, obs columns, and dtypes for 19/19 files. Reference
      for runtime schema discovery. Symlink target verified: ../goal_resource_index_packs_v1/task_matrix_loader_v1/4_artifact/2_persist/loader/
    location: local
  - id: A-003
    name: T-021 standard resources bundle (D-004)
    type: deliverable
    source: predecessor
    origin: goal_precomputed_data_exploration/task_standard_resources_optimal_formats
    registered: '2026-06-23'
    path: 1_asset/T-021 standard resources bundle (D-004)
    symlink: true
    notes: Canonical 19-file float32 H5AD matrices (cp/sh/xpr), JSON indexes, CSV metadata.
      Actual data consumed by the reverse demo. Load by reference only. Symlink target verified:
      ../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/
      (19 files: cp_func_ad.h5ad, sh_func_ad.h5ad, xpr_func_ad.h5ad, 10 JSON indexes, 5 CSV metadata, data_description.yaml).
    location: local
  - id: A-004
    name: T-013 MVP capability review deliverables
    type: deliverable
    source: predecessor
    origin: goal_algorithm_function_review/task_mvp_algorithm_run-through_review
    registered: '2026-06-23'
    path: 1_asset/T-013 MVP capability review deliverables
    symlink: true
    notes: T-013 capability status matrix (D-003) and failure/missing capability list (D-005).
      Used as gap reference for scoping the T-030 reverse demo as a v1 repair+delivery.
      Symlink target verified: ../goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/
    location: local
  - id: A-005
    name: Current project protocol
    type: deliverable
    source: self
    origin: project_init
    registered: '2026-06-23'
    path: 1_asset/Current project protocol
    symlink: true
    notes: Defines pxfquery conda environment, workspace boundaries, source authority,
      and non-modification rules for the demo runtime. Symlink target verified: ../../../1_project_init/1_project_protocol/
    location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/2_protocol/2_protocol_split/protocol.md`

```text
# Protocol: reverse_query_engine_v1

## Objective
Create a `pxfquery-T-030` reverse query engine deliverable that runs a deterministic reverse query demo (apoptosis activation / MYC suppression style candidate ranking) producing serializable, ranked candidate outputs and validation reports. The deliverable reuses the T-024 workspace package and T-026 loader/outputs, and must produce fresh runnable evidence — not an in-place repair of upstream artifacts.

## Inputs
- A-001: T-024 workspace package (pxfquery-T-024) — `4_artifact/2_persist/workspace/` with src/-layout, editable install support, pyproject.toml, and the complete reverse.py/ForwardQuery/ReverseQuery module tree. Installed as editable into the `pxfquery` conda env for demo execution.
- A-002: T-026 loader outputs (pxfquery-T-026) — `4_artifact/2_persist/loader/` loader package (`load_bundle`, `load_matrix`), validation JSON (`loader_validation.json`) recording observed matrix shapes/dtypes/obs columns, and completion report listing 19/19 loads succeeded. Provides the `load_matrix` function to open T-021/D-004 matrices without hard-coding schema.
- A-003: T-021 standard resources bundle (D-004) — canonical 19-file float32 H5AD matrices (cp/sh/xpr), JSON indexes, CSV metadata. The actual data consumed by the reverse demo via A-002 loader.
- A-004: T-013 MVP capability review deliverables — capability status matrix (D-003) and failure/missing capability list (D-005). Used to understand what already passed/failed in the legacy reverse query path and to position the T-030 reverse demo as a scoped v1 repair+delivery, not a re-review.
- A-005: Current project protocol — defines conda environment, workspace boundaries, and legacy asset non-modification rules.

## Steps
1. Read and understand the T-024 workspace reverse query code (`query/reverse.py`, `core.py`, `utils.py`, `data/loader.py`) to know the existing `ReverseQuery` class API, `ReverseResult` schema, `build_target_vector`, `cosine_similarity_matrix`, and fuzzy match helpers.
2. Read T-026 `loader_validation.json` or completion report to confirm matrix shapes, obs columns (`pert_id`, `cmap_name`, `cell_iname`), functional term var_names, and dtype (float32). Also confirm which bundle path contains the three H5AD files.
3. Implement a reverse query demo script `3_execution/run_reverse_demo.py` that:
   - Installs/imports pxfquery from the T-024 workspace (editable install) in the `pxfquery` conda environment.
   - Uses `data.loader.DataLoader` or `core.PxFquery.load_data_dir()` to load at least one perturbation type matrix (prefer `cp` for compound coverage) from the A-003 bundle path.
   - Runs a reverse query targeting apoptosis activation and MYC suppression: `activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"]`, optionally filtered to a relevant cell line (e.g., MCF7).
   - Serializes the ranked candidates as a structured JSON file `4_artifact/2_persist/pxfquery_T-030_reverse_demo_candidates.json` (one record per row: rank, cmap_name, cell_iname, similarity, driving_terms).
   - Serializes the full `ReverseResult` metadata (activate, suppress, cell_line, note) into a separate JSON `4_artifact/2_persist/pxfquery_T-030_reverse_demo_meta.json`.
   - Runs entirely inside `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
4. If the demo script encounters a runtime bug (e.g. import error, column mismatch, dtype issue, missing dependency), repair it within this task scope:
   - Apply minimal fixes to a local copy of the affected workspace module(s) under `3_execution/pxfquery_T-030_repaired/`, not in the T-024 workspace.
   - Record what was fixed, which source asset (T-024), the changed file(s), and validation evidence in `5_report/repair_log.md`.
   - The repaired code should be registered as a deliverable and versioned as `pxfquery-T-030`.
5. Write a machine-readable validation record `3_execution/demo_validation.json` capturing: exact command executed, environment (python version, key package versions), matrices loaded, query parameters, candidate count, top-5 candidates with scores, and any warnings.
6. Write Chinese HTML reports:
   - `4_artifact/3_document/execution_report_vYYYYMMDD.html` — step-by-step execution record.
   - `4_artifact/3_document/result_report_vYYYYMMDD.html` — human-readable result report showing ranked candidate table, query parameters, and matrix schema summary.
7. Write `5_report/completion.md` summarizing what was built, run evidence, repaired issues (if any), and downstream consumption guidance.

### Required Bug-Repair Handling

- If a bug prevents this task from producing a runnable deliverable, repair it within this task scope instead of only reporting it.
- Produce the repaired output as a task-versioned PxFquery asset, for example `pxfquery-T-030`.
- Record what was fixed, the source asset or task id, changed files/assets, validation evidence, and which downstream task should consume the repaired version.

## Constraints

### Scoped Repair And Versioning

- Every task in this DAG has authority to fix bugs inside its own scope when required to make its deliverable run.
- Input assets and output deliverables may intentionally be different PxFquery versions. This task may read an upstream version and emit `pxfquery-T-030` as a corrected local version.
- Do not overwrite unrelated completed upstream artifacts in place. If an upstream asset is wrong, create a corrected downstream asset in this task and document the divergence.
- Repairs must stay inside this task boundary unless the active task explicitly owns the upstream artifact. Preserve lineage, validation evidence, and downstream consumption guidance.

### Execution Discipline

- All Python execution must use the project default conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- The T-024 workspace must be installed as editable (`pip install -e .`) in the `pxfquery` conda env before running the demo.
- Do not copy T-021/D-004 matrix bytes into this task; load by reference through the T-024 workspace data loader or T-026 loader.
- Do not hard-code matrix shapes, column names, or file paths from planning notes — discover them at runtime.
- The demo must actually run and produce non-empty candidate outputs. File existence alone is not acceptable.

## Deliverables
- `3_execution/run_reverse_demo.py` — reverse query demo script.
- `3_execution/demo_validation.json` — machine-readable validation record.
- `4_artifact/2_persist/pxfquery_T-030_reverse_demo_candidates.json` — ranked candidate output (array of {rank, cmap_name, cell_iname, similarity, driving_terms}).
- `4_artifact/2_persist/pxfquery_T-030_reverse_demo_meta.json` — query metadata (activate, suppress, cell_line, note).
- `4_artifact/3_document/execution_report_vYYYYMMDD.html` — Chinese execution report.
- `4_artifact/3_document/result_report_vYYYYMMDD.html` — Chinese result report.
- `4_artifact/registry.yaml` — T-030 artifact registry.
- `5_report/completion.md` — completion report.
- `5_report/repair_log.md` — only if repairs were performed.

## Acceptance
- The reverse demo script actually runs and produces visible, structured candidate results in JSON format.
- Top candidates show meaningful compound/drug names with similarity scores and driving pathway terms.
- Validation JSON is non-empty and captures the exact run parameters and evidence.
- If a T-024 workspace bug blocked the demo, the repair log records the fix with lineage back to T-024.
- T-023 is not required; T-013 provides the gap/capability reference for this v1 task.
```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
version: 1
required:
  - id: A-001
    path: ../../goal_package_foundation_v1/task_workspace_package_v1/4_artifact/2_persist/workspace/
    reason: T-024 current pxfquery workspace (src/-layout, pyproject.toml). Provides the ReverseQuery class, ReverseResult schema, DataLoader, core.PxFquery, and all utility functions. Must be installed as editable in the pxfquery conda env before running the reverse demo.
  - id: A-002
    path: ../../goal_resource_index_packs_v1/task_matrix_loader_v1/4_artifact/2_persist/loader/
    reason: T-026 loader package providing load_matrix/load_bundle functions and loader_validation.json with observed matrix shapes, obs columns, and dtypes. Used as a reference for runtime schema discovery and as an alternative loading path if T-024 DataLoader needs repair.
  - id: A-003
    path: ../../goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/
    reason: T-021/D-004 canonical standard resource bundle (cp_func_ad.h5ad, sh_func_ad.h5ad, xpr_func_ad.h5ad + indexes + metadata). The actual data consumed by the reverse demo. Load by reference; do not copy.
  - id: A-004
    path: ../../goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/
    reason: T-013 MVP capability status matrix and failure/missing capability list. Used to understand what already passed or failed in the legacy reverse query path and to scope T-030 as a deterministic v1 delivery rather than a re-review.
  - id: A-005
    path: ../../../1_project_init/1_project_protocol/
    reason: Current project protocol defining the pxfquery conda environment, workspace boundaries, source authority rules, and non-modification rules for legacy assets.
optional: []
forbidden:
  - path: ../../../2_project_asset/1_raw_material/
    reason: Legacy flat asset library is read-only. T-021/D-004 is the consolidated data source; T-024 and T-026 already bridge from legacy code/data to current workspace.
  - path: /Users/dudu/Documents/3_Project/8_functional_query
    reason: Legacy Windows-era historical source. Not needed for reverse query engine task.
  - path: ../../goal_algorithm_function_review/
    reason: T-013 deliverables are read-only reference inputs. Do not modify or regenerate review artifacts.
  - path: ../../goal_package_foundation_v1/task_workspace_package_v1/4_artifact/
    reason: T-024 workspace is read-only input. Bugs found in it should be repaired in T-030's own scope (3_execution/pxfquery_T-030_repaired/) and not by modifying the T-024 workspace.
  - path: ../../../6_project_deliverable/
    reason: Final project deliverables are not produced by this task.
output:
  - path: 3_execution/run_reverse_demo.py
    description: Reverse query demo script that loads matrices, runs ReverseQuery with apoptosis/MYC targeting, and serializes ranked candidates.
  - path: 3_execution/demo_validation.json
    description: Machine-readable validation record capturing run command, environment, query params, candidate count, and top-5 evidence.
  - path: 3_execution/pxfquery_T-030_repaired/
    description: Local repaired workspace module copies, only if bugs in T-024 workspace blocked the demo.
  - path: 4_artifact/2_persist/
    description: Serialized candidate JSON (pxfquery_T-030_reverse_demo_candidates.json) and metadata JSON (pxfquery_T-030_reverse_demo_meta.json).
  - path: 4_artifact/3_document/
    description: Chinese execution_report_vYYYYMMDD.html and result_report_vYYYYMMDD.html.
  - path: 4_artifact/registry.yaml
    description: T-030 artifact registry.
  - path: 5_report/completion.md
    description: Completion report with run evidence, repaired issues if any, and downstream guidance.
  - path: 5_report/repair_log.md
    description: Repair log, only if a bug in T-024 workspace was repaired inside this task.
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
  - 1_asset/registration.yaml
non_modifiable:
  - 2_protocol/
  - ../../../1_project_init/1_project_protocol/
  - ../../../2_project_asset/
  - ../../goal_package_foundation_v1/
  - ../../goal_precomputed_data_exploration/
  - ../../goal_resource_index_packs_v1/
  - ../../goal_algorithm_function_review/
  - ../../../6_project_deliverable/
  - /Users/dudu/Documents/3_Project/8_functional_query
notes:
  - Load matrices by reference through T-024 workspace DataLoader/PxFquery or T-026 loader; do not copy upstream matrix bytes.
  - Do not hard-code matrix shapes, obs columns, or var term names from planning notes — discover at runtime.
  - Repair scope is T-030 local: if T-024 has a bug, fix it in 3_execution/pxfquery_T-030_repaired/ and document lineage.
  - T-023 is not required; T-013 status matrix is the capability reference for this v1.
  - Acceptable target pattern if exact "HALLMARK_APOPTOSIS" or "HALLMARK_MYC_TARGETS_V1" do not match: fuzzy-match and record the actual matched terms.
```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/5_report/handoff_check_before_exec.md`

```text
(missing)
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: development
- ID: T-030 | Name: reverse_query_engine_v1
- Objective: Create pxfquery-{task_id} reverse query engine deliverable. Reproduce apoptosis activation/MYC suppression style candidate ranking with serializable outputs and reports.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1/task_reverse_query_engine_v1`

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
# AI Handoff: T-030 reverse_query_engine_v1

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
# Delivery QA: T-030 reverse_query_engine_v1

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
