# Execution Prompt
Generated: 2026-06-24 05:11

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
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:11:44'

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
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-057 03_legacy_stress_logic_reuse_boundary
Status: active | Executor: opencode
Objective: Judge the reuse boundary for legacy stress-test-related logic, scripts, reports, and query-validation ideas: which are suitable as references, which require rewrite, which are historical-only, and which are insufficiently supported.

Deliverables: 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_vYYYYMMDD.md and 4_artifact/5_table/stress_logic_reuse_decision_matrix_vYYYYMMDD.csv.

Reference T-001 for authority rules over messy legacy evidence. Reference T-002 for migrated asset entry points and migration status. Reference T-007 for code/index/report maturity. Use T-041 only as a may input if done; otherwise omit it.

Important constraints: do not modify code, do not repair old scripts, do not run production-scale tests; produce reuse decisions with reasons: direct reference, rewrite needed, historical evidence only, not usable, or unknown.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
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

### Selected Assets (12)
- A-001 [document] T-007_development_state_report — path: 1_asset/T-007_development_state_report.md — origin: T-007/D-002 pxfquery_development_state_report_v20260617.md
- A-002 [table] T-007_module_asset_status_matrix — path: 1_asset/T-007_module_asset_status_matrix.csv — origin: T-007/D-003 pxfquery_module_asset_status_matrix_v20260617.csv
- A-003 [table] T-007_validation_evidence_index — path: 1_asset/T-007_validation_evidence_index.csv — origin: T-007/D-004 pxfquery_validation_evidence_index_v20260617.csv
- A-004 [document] T-007_gap_and_risk_list — path: 1_asset/T-007_gap_and_risk_list.md — origin: T-007/D-005 pxfquery_development_gap_and_risk_list_v20260617.md
- A-005 [document] T-001_asset_structure_report — path: 1_asset/T-001_asset_structure_report.md — origin: T-001/D-003 old_asset_structure_report.md
- A-006 [document] T-002_library_structure_guide — path: 1_asset/T-002_library_structure_guide.md — origin: T-002/D-005 flat_asset_library_structure_zh_v20260615.md
- A-007 [document] T-002_not_migrated_assets_report — path: 1_asset/T-002_not_migrated_assets_report.md — origin: T-002/D-007 not_migrated_assets_report_zh_v20260616.md
- A-008 [code] PL_stress_test_scripts — path: 1_asset/PL_stress_test_scripts — origin: T-002/D-001 legacy_flat_asset_library_v20260614/code/index_builders/
- A-009 [document] PL_validation_reports_dir — path: 1_asset/PL_validation_reports_dir — origin: T-002/D-001 legacy_flat_asset_library_v20260614/reports/validation_reports/
- A-010 [code] PL_resolver_source_plus_design — path: 1_asset/PL_resolver_source_plus_design.py — origin: T-002/D-001 legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py + code/design_docs/
- A-011 [other] PL_validation_traces — path: 1_asset/PL_validation_traces.json — origin: T-002/D-001 legacy_flat_asset_library_v20260614/history/design_traces/M-0213 + provenance/misc_useful/M-0212
- A-012 [document] T-007_development_source_map — path: 1_asset/T-007_development_source_map.md — origin: T-007/D-001 pxfquery_development_source_map_v20260617.md

### Asset Rules

### Required
- 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md — Code/index/report maturity overview for reuse classification context
- 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv — Per-component maturity status — primary reference for classifying each stress-test asset's maturity level
- 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv — Indexes validation reports with result/status/implication — primary reference for assigning reuse categories to validation evidence
- 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md — High-priority gaps and risks — informs risk flags for each stress-test asset
- 4_artifact/2_persist/old_asset_structure_report.md — Authority rules for distinguishing operational core from archive noise in legacy materials
- 4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md — Flat asset library structure guide — entry point for navigating migrated assets
- 4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md — Prevents evaluating assets that were intentionally not migrated
- 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/index_builders/ — Legacy test/verify scripts for reuse classification (M-0385 through M-0389 range)
- 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/ — 57 validation reports forming the primary stress-test evidence corpus
- 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/code/pxfquery_package/query/resolver.py — Core resolver logic that stress-test scripts exercise
- 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/provenance/misc_useful/M-0212_act1_validation_minimax.json — JSON validation trace for reproducibility assessment
- 4_artifact/2_persist/pxfquery_development_source_map_v20260617.md — Source authority map to avoid citing superseded or duplicate validation reports
### Forbidden
- predecessor task directories (except for reading registered assets at their source paths)
- /Users/dudu/Documents/3_Project/8_functional_query (legacy source root)
- 2_project_asset/ except paths explicitly listed in required above
### Output
- 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md
- 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv

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

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/5_report/execution_handoff.md`

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
