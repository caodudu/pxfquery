# Checking Prompt
Generated: 2026-06-24 05:10

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-057
name: 03_legacy_stress_logic_reuse_boundary
phase: digestion
goal: goal_legacy_stress_test_asset_digestion
project: P-012
objective: 'Judge the reuse boundary for legacy stress-test-related logic, scripts,
  reports, and query-validation ideas: which are suitable as references, which require
  rewrite, which are historical-only, and which are insufficiently supported.


  Deliverables: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md
  and 4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv.


  Reference T-001 for authority rules over messy legacy evidence. Reference T-002
  for migrated asset entry points and migration status. Reference T-007 for code/index/report
  maturity. Use T-041 only as a may input if done; otherwise omit it.


  Important constraints: do not modify code, do not repair old scripts, do not run
  production-scale tests; produce reuse decisions with reasons: direct reference,
  rewrite needed, historical evidence only, not usable, or unknown.'
executor: opencode
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
notes: ''
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T05:10:27'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: T-007_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002 pxfquery_development_state_report_v20260617.md
  registered: '2026-06-24'
  path: 1_asset/T-007_development_state_report.md
  symlink: true
  status: ready
  notes: Summarizes intended product scope, implemented components, data/index readiness,
    validation state — needed to assess code/index/report maturity
  location: local
- id: A-002
  name: T-007_module_asset_status_matrix
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-003
  origin: T-007/D-003 pxfquery_module_asset_status_matrix_v20260617.csv
  registered: '2026-06-24'
  path: 1_asset/T-007_module_asset_status_matrix.csv
  symlink: true
  status: ready
  notes: Per-component status (implemented/partial/risk/historical) — needed to classify
    each stress-test asset's maturity
  location: local
- id: A-003
  name: T-007_validation_evidence_index
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-004
  origin: T-007/D-004 pxfquery_validation_evidence_index_v20260617.csv
  registered: '2026-06-24'
  path: 1_asset/T-007_validation_evidence_index.csv
  symlink: true
  status: ready
  notes: Indexes validation reports with result/status/development_implication — primary
    reference for assigning reuse categories to validation evidence
  location: local
- id: A-004
  name: T-007_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005 pxfquery_development_gap_and_risk_list_v20260617.md
  registered: '2026-06-24'
  path: 1_asset/T-007_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: High-priority gaps, risks, claims to avoid — informs which stress-test assets
    carry risk flags
  location: local
- id: A-005
  name: T-001_asset_structure_report
  type: document
  source: predecessor
  source_task: T-001
  source_artifact_id: D-003
  origin: T-001/D-003 old_asset_structure_report.md
  registered: '2026-06-24'
  path: 1_asset/T-001_asset_structure_report.md
  symlink: true
  status: ready
  notes: Authority rules over messy legacy evidence — needed to distinguish operational
    core from archive noise when classifying stress-test assets
  location: local
- id: A-006
  name: T-002_library_structure_guide
  type: document
  source: predecessor
  source_task: T-002
  source_artifact_id: D-005
  origin: T-002/D-005 flat_asset_library_structure_zh_v20260615.md
  registered: '2026-06-24'
  path: 1_asset/T-002_library_structure_guide.md
  symlink: true
  status: ready
  notes: Flat asset library structure guide — entry point for navigating migrated
    assets
  location: local
- id: A-007
  name: T-002_not_migrated_assets_report
  type: document
  source: predecessor
  source_task: T-002
  source_artifact_id: D-007
  origin: T-002/D-007 not_migrated_assets_report_zh_v20260616.md
  registered: '2026-06-24'
  path: 1_asset/T-002_not_migrated_assets_report.md
  symlink: true
  status: ready
  notes: Records which legacy assets were intentionally not migrated — prevents wasting
    effort on unmigrated candidates
  location: local
- id: A-008
  name: PL_stress_test_scripts
  type: code
  source: project_asset
  source_task: project_asset
  source_artifact_id: legacy_flat_asset_library
  origin: T-002/D-001 legacy_flat_asset_library_v20260614/code/index_builders/
  registered: '2026-06-24'
  path: 1_asset/PL_stress_test_scripts
  symlink: true
  status: ready
  notes: Directory containing M-0385 test_resolver_smoke.py, M-0386 test_forward_matrix.py,
    M-0387 (unnamed), M-0388 (unnamed), M-0389 verify_resolver_cases.py — legacy stress-test-adjacent
    test/verify scripts for reuse boundary assessment
  location: local
- id: A-009
  name: PL_validation_reports_dir
  type: document
  source: project_asset
  source_task: project_asset
  source_artifact_id: legacy_flat_asset_library
  origin: T-002/D-001 legacy_flat_asset_library_v20260614/reports/validation_reports/
  registered: '2026-06-24'
  path: 1_asset/PL_validation_reports_dir
  symlink: true
  status: ready
  notes: 57 validation reports including forward matrix tests, LLM question suites,
    stability checks, known risks, execution order guidance, obsolete list — the primary
    stress-test evidence corpus for reuse classification
  location: local
- id: A-010
  name: PL_resolver_source_plus_design
  type: code
  source: project_asset
  source_task: project_asset
  source_artifact_id: legacy_flat_asset_library
  origin: T-002/D-001 legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py
    + code/design_docs/
  registered: '2026-06-24'
  path: 1_asset/PL_resolver_source_plus_design.py
  symlink: true
  status: ready
  notes: Core resolver logic that stress tests target + design documents explaining
    intent — needed to understand what stress-test assets actually test
  loc

...[truncated by CyHex prompt assembler: 1073 chars omitted]
```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/2_protocol/2_protocol_split/protocol.md`

```text
# T-057 03_legacy_stress_logic_reuse_boundary — Protocol

## Objective

Judge the reuse boundary for each legacy stress-test-related logic, script, report, and query-validation idea found in the migrated flat asset library. For each candidate, assign one of: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, or `unknown`. Produce a reusable decision document and a decision matrix CSV.

## Position In Project

This is task 3 of 4 in goal G-026 (legacy_stress_test_asset_digestion). It follows T-055 (source map — pending) and T-056 (scenario inventory — pending). Since predecessors are not yet delivered, this task works directly from T-001/T-002/T-007 digested outputs and the project-level flat asset library. Its output feeds T-058 (development handoff pack).

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Code/index/report maturity overview |
| A-002 | T-007 | 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Per-component maturity for reuse classification |
| A-003 | T-007 | 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Validation evidence status — primary reference for validation-report reuse |
| A-004 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Risk flags for each asset category |
| A-005 | T-001 | 4_artifact/2_persist/old_asset_structure_report.md | Authority rules for distinguishing operational vs archive material |
| A-006 | T-002 | 4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Flat library navigation guide |
| A-007 | T-002 | 4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Prevents evaluating unmigrated assets |
| A-008 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders/ | Legacy test/verify scripts for reuse classification |
| A-009 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/ | 57 validation reports forming the stress-test evidence corpus |
| A-010 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py | Core resolver logic that stress tests exercise |
| A-011 | project_asset | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful/M-0212_act1_validation_minimax.json | JSON validation traces for reproducibility assessment |
| A-012 | T-007 | 4_artifact/2_persist/pxfquery_development_source_map_v20260617.md | Source authority map to avoid superseded/duplicate reports |

## Execution Steps

1. **Read authority and context.** Read A-005 (T-001 authority), A-006 (T-002 structure guide), A-007 (not-migrated report), A-001 (T-007 state report), A-012 (source map) to establish classification criteria and boundary rules.

2. **Read T-007 maturity indexes.** Read A-002 (module asset status matrix), A-003 (validation evidence index), A-004 (gap/risk list) to understand the validated status and risk level of each component that stress-test assets target.

3. **Read legacy validation reports systematically.** Scan A-009 (validation_reports/ directory). For each report, read its content and classify it. At minimum cover:
   - Latest reports index (M-0239)
   - Forward matrix tests (M-0291, M-0257)
   - Forward question suites (M-0266, M-0277, M-0275)
   - LLM stability check (M-0267)
   - Act-1 validation (M-0255)
   - Known risks (M-0243), execution order (M-0244), obsolete list (M-0245)
   - Resolver TODO (M-0290)

4. **Read legacy test scripts.** Read the scripts in A-008 (index_builders/ directory). At minimum:
   - M-0385 test_resolver_smoke.py (if exists)
   - M-0386 test_forward_matrix.py (deterministic mock)
   - M-0389 verify_resolver_cases.py (real LLM)

5. **Read resolver source and design context.** Read A-010 (resolver.py) and relevant design docs from A-008's design_docs/ to understand what the test/verify scripts exercise.

6. **Read validation traces.** Read A-011 (act1 validation JSON) to supplement report-based assessment.

7. **Build decision matrix.** For each evaluated candidate, record:
   - Asset name/path
   - Asset type (script / report / design doc / other)
   - Reuse decision: direct reference / rewrite needed / historical evidence only / not usable / unknown
   - Reasoning summary
   - Key risk or gap
   - Recommended next action

8. **Write deliverable 1: Persist document.** Write `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md` with full reuse-boundary analysis organized by asset category.

9. **Write deliverable 2: Decision matrix.** Write `4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv` with the tabular decision matrix.

10. **Register deliverables.** Update `4_artifact/registry.yaml` with both outputs.

## Constraints

- Do not modify code, repair old scripts, or run production-scale tests.
- Do not scan the unregistered legacy root (8_functional_query).
- If a script or report references workspace paths that do not exist in the current project, note this but do not fix them.
- If T-041 is done, it may be consulted as an optional supplementary source; if T-041 is still active (its current status), omit it.
- If T-055 (source map) or T-056 (scenario inventory) become available during execution, they may be used as cross-reference but must not block this task.
- Use the classification categories exactly: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`.
- Use today's date YYYYMMDD = 20260624.
- Do not treat older/superseded validation reports as primary evidence; use the T-007 validation evidence index (A-003) and the latest reports index (M-0239) for priority.

## Forbidden

- Modifying any file inside `2_project_asset/`, `1_project_init/`, or predecessor task directories.
- Running old scr

...[truncated by CyHex prompt assembler: 2025 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-002
    path: 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: Code/index/report maturity overview for reuse classification context
  - id: A-002
    source_task: T-007
    source_artifact_id: D-003
    path: 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv
    reason: Per-component maturity status — primary reference for classifying each stress-test asset's maturity level
  - id: A-003
    source_task: T-007
    source_artifact_id: D-004
    path: 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv
    reason: Indexes validation reports with result/status/implication — primary reference for assigning reuse categories to validation evidence
  - id: A-004
    source_task: T-007
    source_artifact_id: D-005
    path: 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: High-priority gaps and risks — informs risk flags for each stress-test asset
  - id: A-005
    source_task: T-001
    source_artifact_id: D-003
    path: 4_artifact/2_persist/old_asset_structure_report.md
    reason: Authority rules for distinguishing operational core from archive noise in legacy materials
  - id: A-006
    source_task: T-002
    source_artifact_id: D-005
    path: 4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md
    reason: Flat asset library structure guide — entry point for navigating migrated assets
  - id: A-007
    source_task: T-002
    source_artifact_id: D-007
    path: 4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md
    reason: Prevents evaluating assets that were intentionally not migrated
  - id: A-008
    source_task: project_asset
    source_artifact_id: legacy_flat_asset_library
    path: 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders/
    reason: Legacy test/verify scripts for reuse classification (M-0385 through M-0389 range)
  - id: A-009
    source_task: project_asset
    source_artifact_id: legacy_flat_asset_library
    path: 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/
    reason: 57 validation reports forming the primary stress-test evidence corpus
  - id: A-010
    source_task: project_asset
    source_artifact_id: legacy_flat_asset_library
    path: 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py
    reason: Core resolver logic that stress-test scripts exercise
  - id: A-011
    source_task: project_asset
    source_artifact_id: legacy_flat_asset_library
    path: 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful/M-0212_act1_validation_minimax.json
    reason: JSON validation trace for reproducibility assessment
  - id: A-012
    source_task: T-007
    source_artifact_id: D-001
    path: 4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
    reason: Source authority map to avoid citing superseded or duplicate validation reports
optional:
  - id: MAY-001
    source_task: T-041
    source_artifact_id: null
    path: null
    reason: "T-041 (legacy_source_digest_for_m1) is active but not yet completed. If done by execution time, its package-source digest may supplement resolver/test-script classification; otherwise omit."
forbidden:
  - predecessor task directories (except for reading registered assets at their source paths)
  - /Users/dudu/Documents/3_Project/8_functional_query (legacy source root)
  - 2_project_asset/ except paths explicitly listed in required above
output:
  - path: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md
    type: persist
    description: Full reuse-boundary analysis organized by asset category
  - path: 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv
    type: table
    description: Tabular decision matrix with columns asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action
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
Task phase: digestion
Task ID: T-057 | Name: 03_legacy_stress_logic_reuse_boundary
Status: active | Executor: opencode
Objective: Judge the reuse boundary for legacy stress-test-related logic, scripts, reports, and query-validation ideas: which are suitable as references, which require rewrite, which are historical-only, and which are insufficiently supported.

Deliverables: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md and 4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv.

Reference T-001 for authority rules over messy legacy evidence. Reference T-002 for migrated asset entry points and migration status. Reference T-007 for code/index/report maturity. Use T-041 only as a may input if done; otherwise omit it.

Important constraints: do not modify code, do not repair old scripts, do not run production-scale tests; produce reuse decisions with reasons: direct reference, rewrite needed, historical evidence only, not usable, or unknown.
Notes / User Natural-Language Intent: 
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: digestion
  project_asset_access: allowed
  zero_assets: false
  total_assets: 12
  symlink_sync:
    checked: 12
    linked: 12
    skipped: 0
    changed: false
  counts:
    ok: 12
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: T-007_development_state_report
    required: true
    status: ok
    path: 1_asset/T-007_development_state_report.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: local path exists
  - id: A-002
    name: T-007_module_asset_status_matrix
    required: true
    status: ok
    path: 1_asset/T-007_module_asset_status_matrix.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv
    reason: local path exists
  - id: A-003
    name: T-007_validation_evidence_index
    required: true
    status: ok
    path: 1_asset/T-007_validation_evidence_index.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv
    reason: local path exists
  - id: A-004
    name: T-007_gap_and_risk_list
    required: true
    status: ok
    path: 1_asset/T-007_gap_and_risk_list.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: local path exists
  - id: A-005
    name: T-001_asset_structure_report
    required: true
    status: ok
    path: 1_asset/T-001_asset_structure_report.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md
    reason: local path exists
  - id: A-006
    name: T-002_library_structure_guide
    required: true
    status: ok
    path: 1_asset/T-002_library_structure_guide.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md
    reason: local path exists
  - id: A-007
    name: T-002_not_migrated_assets_report
    required: true
    status: ok
    path: 1_asset/T-002_not_migrated_assets_report.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md
    reason: local path exists
  - id: A-008
    name: PL_stress_test_scripts
    required: true
    status: ok
    path: 1_asset/PL_stress_test_scripts
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders
    reason: local path exists
  - id: A-009
    name: PL_validation_reports_dir
    required: true
    status: ok
    path: 1_asset/PL_validation_reports_dir
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports
    reason: local path exists
  - id: A-010
    name: PL_resolver_source_plus_design
    required: true
    status: ok
    path: 1_asset/PL_resolver_source_plus_design.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py
    reason: local path exists
  - id: A-011
    name: PL_validation_traces
    required: true
    status: ok
    path: 1_asset/PL_validation_traces.json
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful/M-0212_act1_validation_minimax.json
    reason: local path exists
  - id: A-012
    name: T-007_development_source_map
    required: true
    status: ok
    path: 1_asset/T-007_development_source_map.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-057 03_legacy_stress_logic_reuse_boundary

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md` 是否已写
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
