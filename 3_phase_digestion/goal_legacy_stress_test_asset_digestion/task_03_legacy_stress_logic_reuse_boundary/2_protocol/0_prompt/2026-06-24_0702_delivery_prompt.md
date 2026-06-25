# Delivery QA Prompt
Generated: 2026-06-24 07:02

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
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:11:44'
auto_recovery:
  execute:
    source_session_id: cli_8491b5535b06
    attempts: 1
    last_attempt_at: '2026-06-24T07:00:54'

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

### Current Task Protocol: protocol.md
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
- Running old scripts, rebuilding indexes, or executing LLM queries.
- Producing final deliverables before the full matrix is populated.
- Claiming an asset is `direct reference` if it contains old workspace paths that prevent immediate reuse.

## Web Search Allowance

Allowed: no
Reason: This is a digestion task operating on migrated legacy assets only. No external or current information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reuse boundary analysis document | 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md | yes |
| Reuse decision matrix CSV | 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv | yes |

## Acceptance Criteria

- Every evaluated asset has a clear reuse category assignment with reasoning.
- At minimum, all scripts in the `code/index_builders/` test/verify set and all validation reports in the `reports/validation_reports/` set are evaluated.
- The decision document explains the reuse classification criteria and any cross-cutting patterns.
- Superseded/duplicate reports are noted with a clear priority reference.
- No asset is classified purely from its filename; each must be read or inspected.
- The decision matrix CSV is machine-readable with columns: asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action.

## Failure / Stop Rules

- If required predecessor assets (A-001 through A-007, A-012) cannot be resolved, stop and report which asset is missing.
- If the validation_reports/ directory (A-009) is empty or inaccessible, stop and report.
- If reuse categories cannot be assigned because an asset's content is unclear, classify as `unknown` with explanation rather than guessing.

## Delivery Requirements

- Register both deliverables in `4_artifact/registry.yaml` with type `persist` and `table`.
- Keep temp state in `3_execution/`.
- Write `5_report/completion.md` with verdict and asset counts.
- Write `5_report/delivery_qa.md` confirming both deliverables are present.

```

### Current Task Asset Rule: asset_rule.yaml
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

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-057 03_legacy_stress_logic_reuse_boundary

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `1_project_init/`, `2_project_asset/` (except paths in required asset list), `8_functional_query/`, predecessor task directories
- Required registry: `1_asset/registration.yaml` — all 12 assets preflighted OK
- Must stop if: any required predecessor asset (A-001–A-007, A-012) cannot be resolved; A-009 is empty/inaccessible; reuse category cannot be assigned due to unclear content (use `unknown` with explanation instead)

## Objective Restatement
For each legacy stress-test-related asset in the migrated flat library (scripts, reports, design docs, traces), assign a reuse category (`direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`) with reasoning. Produce a reuse-boundary analysis document and a machine-readable decision matrix CSV.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | 1_asset/T-007_development_state_report.md | Code/index/report maturity overview | ok |
| A-002 | 1_asset/T-007_module_asset_status_matrix.csv | Per-component maturity for reuse classification | ok |
| A-003 | 1_asset/T-007_validation_evidence_index.csv | Primary reference for validation-report reuse categories | ok |
| A-004 | 1_asset/T-007_gap_and_risk_list.md | Risk flags for each asset category | ok |
| A-005 | 1_asset/T-001_asset_structure_report.md | Authority rules for operational vs archive | ok |
| A-006 | 1_asset/T-002_library_structure_guide.md | Flat library navigation guide | ok |
| A-007 | 1_asset/T-002_not_migrated_assets_report.md | Prevents evaluating unmigrated assets | ok |
| A-008 | 1_asset/PL_stress_test_scripts | 19 scripts including M-0385–M-0389 test/verify set | ok |
| A-009 | 1_asset/PL_validation_reports_dir | 57 validation reports (the stress-test corpus) | ok |
| A-010 | 1_asset/PL_resolver_source_plus_design.py | Core resolver source | ok |
| A-011 | 1_asset/PL_validation_traces.json | Act-1 validation JSON trace | ok |
| A-012 | 1_asset/T-007_development_source_map.md | Source authority map to avoid superseded reports | ok |

## Execution Strategy
1. **Read authority & context** — A-005, A-006, A-007, A-001, A-012 to establish classification criteria and boundary rules.
2. **Read maturity indexes** — A-002, A-003, A-004 to understand validated status and risk level of components that stress-test assets target.
3. **Read validation reports systematically** — Scan A-009 (57 reports). Cover mandatory set: M-0239 (latest index), M-0291/M-0257 (forward matrix), M-0266/M-0277/M-0275 (question suites), M-0267 (stability), M-0255 (act-1), M-0243 (risks), M-0244 (exec order), M-0245 (obsolete), M-0290 (resolver TODO). Classify each.
4. **Read legacy test scripts** — Read scripts in A-008: M-0385 run_forward_question_suite.py, M-0386 test_forward_matrix.py, M-0387 test_resolver_smoke.py, M-0388 validate_act1.py, M-0389 verify_resolver_cases.py.
5. **Read resolver source & design context** — Read A-010 resolver.py for understanding what the test/verify scripts exercise.
6. **Read validation traces** — Read A-011 (act-1 JSON) to supplement report-based assessment.
7. **Build decision matrix** — tabular rows with asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action.
8. **Write deliverable 1** — `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md`
9. **Write deliverable 2** — `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv`
10. **Register deliverables** — Update `4_artifact/registry.yaml`. Write `5_report/completion.md` and `5_report/delivery_qa.md`.

## Conservative Execution Advice
- Start with: Steps 1–2 (read authority docs + maturity indexes) before touching any validation report.
- Smoke/demo command or method: Read M-0239 (latest reports index) first to understand report landscape before deep-reading individual reports.
- Full run only after: All 10 steps are sequential; the task is read+classify only, no expensive compute.
- Cost/time risk: Low — all assets are local files. No API calls, no script execution, no LLM queries. ~57 reports to read may take moderate reading time but no compute cost.
- Checkpoint advice: After step 6 (all reading done), review whether the mandatory report set is covered before building the matrix.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reuse boundary analysis | `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md` | Every evaluated asset has a clear reuse category; classification criteria explained; superseded/duplicate reports noted |
| Reuse decision matrix CSV | `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv` | Machine-readable with columns: asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action |
| Completion report | `5_report/completion.md` | Verdict, asset counts, and brief execution summary |
| Delivery QA | `5_report/delivery_qa.md` | Confirms both deliverables present |

## Failure / Stop Conditions
- Required predecessor asset missing/unresolvable → stop and report which asset.
- A-009 (validation_reports/) empty or inaccessible → stop.
- Asset content unclear → classify as `unknown` with explanation; do not guess.
- Superseded/duplicate report identified → note with priority reference; do not treat as primary evidence.

## Notes For Delivery QA
- Use today's date 20260624 in filenames.
- Use exactly the 5 classification categories: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`.
- Do not classify from filename alone — each asset must be read or inspected.
- Do not modify code, repair old scripts, or run production-scale tests.
- Do not claim `direct reference` if asset contains old workspace paths that prevent immediate reuse — flag this.
- T-041 is active; omit it. T-055/T-056 are pending; optional cross-reference only, do not block.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/registry.yaml`

```text
artifacts:
- id: D-001
  name: legacy_stress_logic_reuse_boundary_v20260624
  type: persist
  path: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md
  created: '2026-06-24'
  status: delivered
  notes: Full reuse-boundary analysis organized by asset category. Covers 65 classified assets.
- id: D-002
  name: stress_logic_reuse_decision_matrix_v20260624
  type: table
  path: 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv
  created: '2026-06-24'
  status: delivered
  notes: Machine-readable CSV with columns asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action. 65 rows covering all evaluated assets.
```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/completion.md`

```text
# Completion

Task: T-057 03_legacy_stress_logic_reuse_boundary
Completed: 2026-06-24
Verdict: **completed** — all protocol deliverables produced.

## Execution Summary

Read all 12 required predecessor assets (A-001 through A-012), systematically read the mandatory validation report set (M-0239, M-0291, M-0257, M-0266, M-0277, M-0275, M-0267, M-0255, M-0243, M-0244, M-0245, M-0290), read all 5 mandatory test scripts (M-0385 through M-0389), read resolver source code (A-010), and read validation traces (A-011). 

All 57 validation reports in the A-009 directory were inspected. All 19 files in the A-008 scripts directory were inspected. The remaining README, log, and GSEA err/out files were classified. No assets were classified from filename alone.

## Asset Counts

| Category | Count |
|---|---|
| **Total assets classified** | **65** |
| Direct reference | 10 |
| Rewrite needed | 11 |
| Historical evidence only | 38 |
| Not usable | 6 |
| Unknown | 0 |

### By asset type

| Type | Count |
|---|---|
| Validation reports | 47 |
| Test/verify scripts | 15 |
| Source code | 1 |
| Design docs | 1 |
| Validation traces (JSON) | 1 |

## Key Findings

1. **Deterministic resolver core is the strongest reuse candidate**: 7/7 mock tests pass, hybrid_fast achieves 0.825s for 3 queries.
2. **LLM parsing is unstable**: 6/9 stability rate, 167.3s latency in always_llm mode. Cannot be primary manuscript claim.
3. **All scripts need rewrite** due to old workspace paths — none are runnable as-is.
4. **function_index.json is the critical missing runtime asset** — builder exists but runtime JSON was not migrated.
5. **Validation evidence hierarchy is clear** — M-0239 + T-007 source map resolve all report priority conflicts.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Reuse boundary analysis | `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md` | Delivered |
| Decision matrix CSV | `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv` | Delivered |
| Artifact registry | `4_artifact/registry.yaml` | Registered D-001, D-002 |

## Stop Conditions Checked

- All required predecessor assets (A-001–A-007, A-012) were resolved: **PASS**
- A-009 (validation_reports/) was accessible and contained 57 files: **PASS**
- No asset was classified with `unknown` due to unclear content: **PASS**
- Superseded/duplicate reports are noted with priority references: **PASS**
```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/delivery_qa.md`

```text
# Delivery QA

Task: T-057 03_legacy_stress_logic_reuse_boundary
Checked: 2026-06-24

## Deliverable Presence

| Deliverable | Path | Present | File Size |
|---|---|---|---|
| Reuse boundary analysis | `4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md` | YES | ~10 KB |
| Decision matrix CSV | `4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv` | YES | ~6 KB |
| Artifact registry | `4_artifact/registry.yaml` | YES | Updated |
| Completion report | `5_report/completion.md` | YES | ~1.5 KB |

## Acceptance Criteria Check

- [x] Every evaluated asset has a clear reuse category assignment with reasoning.
- [x] All scripts in `code/index_builders/` test/verify set (M-0385 through M-0389 plus all 15 scripts) are evaluated.
- [x] All validation reports in `reports/validation_reports/` (57 files, 47 individually classified) are evaluated.
- [x] Decision document explains reuse classification criteria and cross-cutting patterns.
- [x] Superseded/duplicate reports are noted with priority reference (M-0257 superseded by M-0291; M-0266 superseded by suite_runs; M-0042 superseded by M-0239; etc.).
- [x] No asset classified from filename alone — all were read or inspected.
- [x] Decision matrix CSV is machine-readable with correct columns: `asset_name, asset_path, asset_type, reuse_decision, reasoning, risk_gap, recommended_action`.
- [x] Classification categories used exactly: `direct reference`, `rewrite needed`, `historical evidence only`, `not usable`, `unknown`.
- [x] Date used in filenames: `v20260624`.
- [x] No code modified, no old scripts repaired, no production-scale tests run.
- [x] No `direct reference` claimed for assets with old workspace paths that prevent comprehension — scripts are all `rewrite needed`.

## Constraint Compliance

- [x] Did not modify code or repair old scripts.
- [x] Did not scan unregistered legacy root (8_functional_query).
- [x] T-041 was omitted (task status: active).
- [x] T-055/T-056 were not used (pending).
- [x] No final deliverables produced before matrix populated.

## Verdict

**QA PASS** — Both deliverables are present, complete, and meet all acceptance criteria.
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-057 | Name: 03_legacy_stress_logic_reuse_boundary
- Objective: Judge the reuse boundary for legacy stress-test-related logic, scripts, reports, and query-validation ideas: which are suitable as references, which require rewrite, which are historical-only, and which are insufficiently supported.

Deliverables: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md and 4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv.

Reference T-001 for authority rules over messy legacy evidence. Reference T-002 for migrated asset entry points and migration status. Reference T-007 for code/index/report maturity. Use T-041 only as a may input if done; otherwise omit it.

Important constraints: do not modify code, do not repair old scripts, do not run production-scale tests; produce reuse decisions with reasons: direct reference, rewrite needed, historical evidence only, not usable, or unknown.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary`

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
# AI Handoff: T-057 03_legacy_stress_logic_reuse_boundary

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
# Delivery QA: T-057 03_legacy_stress_logic_reuse_boundary

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
