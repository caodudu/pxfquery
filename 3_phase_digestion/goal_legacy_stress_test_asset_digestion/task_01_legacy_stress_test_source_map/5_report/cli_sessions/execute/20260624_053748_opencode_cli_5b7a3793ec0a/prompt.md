# Execution Prompt
Generated: 2026-06-24 05:20

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-055
name: 01_legacy_stress_test_source_map
phase: digestion
goal: goal_legacy_stress_test_asset_digestion
project: P-012
objective: 'Create a source map for migrated legacy materials that may relate to PxFquery
  stress testing, complex queries, resolver validation, strict edge cases, and old
  validation scripts/reports.


  Deliverables: 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md and
  4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv.


  Reference T-001 because it defines legacy background, old structure interpretation,
  and source authority rules. Reference T-002 because it defines the migrated flat
  asset library and prevents direct legacy-root wandering. Reference T-007 because
  it summarizes current development asset/code/index/report maturity.


  Important constraints: do not scan the unregistered legacy root; do not claim any
  old script is runnable; create candidate source mapping only; record missing or
  ambiguous leads honestly.'
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
fast_pass_last_auto_approved_at: '2026-06-24T05:20:30'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: legacy_flat_asset_library
  type: archive
  source: project_asset
  source_task: T-002
  source_artifact_id: D-001
  origin: 'T-002/D-001: migrated flat asset library v20260614'
  registered: '2026-06-24'
  path: 1_asset/legacy_flat_asset_library
  symlink: true
  status: ready
  notes: 'Primary browse source. Browse subdirs: reports/validation_reports/, code/index_builders/,
    code/pxfquery_package/query/, data/query_indexes/, code/analysis_scripts/, results/gsea_tables/.'
  location: local
- id: A-002
  name: migration_manifest
  type: table
  source: predecessor
  source_task: T-002
  source_artifact_id: D-002
  origin: 'T-002/D-002: migration_manifest_v20260614.json'
  registered: '2026-06-24'
  path: 1_asset/migration_manifest.json
  symlink: true
  status: ready
  notes: Trace which stress-test-related legacy files were migrated or excluded; map
    old paths to new paths.
  location: local
- id: A-003
  name: old_asset_structure_report
  type: document
  source: predecessor
  source_task: T-001
  source_artifact_id: D-003
  origin: 'T-001/D-003: old_asset_structure_report.md'
  registered: '2026-06-24'
  path: 1_asset/old_asset_structure_report.md
  symlink: true
  status: ready
  notes: Legacy structure context for understanding where stress-test assets originally
    lived.
  location: local
- id: A-004
  name: project_background_extraction_report
  type: document
  source: predecessor
  source_task: T-001
  source_artifact_id: D-004
  origin: 'T-001/D-004: project_background_extraction_report.md'
  registered: '2026-06-24'
  path: 1_asset/project_background_extraction_report.md
  symlink: true
  status: ready
  notes: Background context for stress-test asset origins.
  location: local
- id: A-005
  name: pxfquery_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: 'T-007/D-002: pxfquery_development_state_report_v20260617.md'
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_state_report.md
  symlink: true
  status: ready
  notes: Summarizes current component readiness, validation state, and development
    interpretation.
  location: local
- id: A-006
  name: pxfquery_validation_evidence_index
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-004
  origin: 'T-007/D-004: pxfquery_validation_evidence_index_v20260617.csv'
  registered: '2026-06-24'
  path: 1_asset/pxfquery_validation_evidence_index.csv
  symlink: true
  status: ready
  notes: Existing catalog of validation evidence; avoid redundant coverage and identify
    gaps.
  location: local
- id: A-007
  name: pxfquery_development_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: 'T-007/D-005: pxfquery_development_gap_and_risk_list_v20260617.md'
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: Known gaps and risks (e.g., LLM stability 6/9) to cross-reference against
    discovered stress-test materials.
  location: local
- id: A-008
  name: flat_asset_library_structure_zh
  type: document
  source: predecessor
  source_task: T-002
  source_artifact_id: D-005
  origin: 'T-002/D-005: flat_asset_library_structure_zh_v20260615.md'
  registered: '2026-06-24'
  path: 1_asset/flat_asset_library_structure_zh.md
  symlink: true
  status: ready
  notes: Chinese structure explanation for flat library navigation.
  location: local
- id: A-009
  name: not_migrated_assets_report_zh
  type: document
  source: predecessor
  source_task: T-002
  source_artifact_id: D-007
  origin: 'T-002/D-007: not_migrated_assets_report_zh_v20260616.md'
  registered: '2026-06-24'
  path: 1_asset/not_migrated_assets_report_zh.md
  symlink: true
  status: ready
  notes: May contain stress-test content that was intentionally excluded from migration.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/2_protocol/2_protocol_split/protocol.md`

```text
# T-055 01_legacy_stress_test_source_map — Protocol

## Objective

Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. The source map must be a structured guide that later tasks can use to locate, assess, and reuse these materials without directly scanning the unregistered legacy root.

## Position In Project

This is a digestion-phase task under G-005 (legacy stress test asset digestion). It follows T-001 (legacy semantic digestion), T-002 (flat asset migration), and T-007 (development state digestion). This task does not execute, run, or validate any old script. It produces a candidate map only, enabling later assessment tasks to proceed without legacy-root access.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|----------|-------------|------|------------|
| A-001 | T-002 | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ | Primary browse source for all migrated legacy materials that may contain stress-test/validation content |
| A-002 | T-002/D-002 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/migration_manifest_v20260614.json | Full migration manifest to trace which stress-test files were migrated, their source paths, and any not-migrated items |
| A-003 | T-001/D-003 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md | Understanding legacy source structure and identification of operational vs archive layers |
| A-004 | T-001/D-004 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/project_background_extraction_report.md | Project background context for understanding why certain stress-test assets were created |
| A-005 | T-007/D-002 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development state summary to understand which validation gaps are already documented |
| A-006 | T-007/D-004 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Existing validation evidence index to avoid redundant cataloging and identify gaps |
| A-007 | T-007/D-005 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps and risks to cross-reference against discovered stress-test materials |
| A-008 | T-002/D-005 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Chinese structure explanation for the flat library navigation |
| A-009 | T-002/D-007 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Record of intentionally not-migrated assets; may contain stress-test content that was explicitly excluded |

## Execution Steps

1. Read A-001 (flat asset library) structure to understand available directories.
2. Read A-005, A-006, A-007 (T-007 handoff) to understand already-documented validation landscape.
3. Read A-002 (migration manifest) and A-009 (not-migrated report) to identify stress-test-related entries.
4. Browse the following high-priority directories within A-001 for stress-test/validation content:
   - `reports/validation_reports/` — resolver validation, suite runs, stability checks, known risks
   - `code/index_builders/` — test scripts (test_resolver_smoke, test_forward_matrix, verify_resolver_cases, run_forward_question_suite, validate_act1, check_llm_stability)
   - `code/pxfquery_package/query/` — resolver pipeline source with forward search policy (L1-L4 logic)
   - `data/query_indexes/` — index files used by the resolver for query resolution
   - `reports/digested_context/` — any context reports mentioning validation outcomes
   - `code/analysis_scripts/` — GSEA evaluation scripts (cp_gsea_eval, sh_gsea_eval, xpr_gsea_eval) and analysis notebooks
   - `results/gsea_tables/` — GSEA result tables used as validation baselines
5. For each candidate asset found, record:
   - Migrated path within flat library (or explicit not-migrated status)
   - Original legacy source path (from manifest or A-003/A-008 context)
   - Asset type: script, report, data, index, result, design_doc
   - Stress-test relevance category: complex_query, resolver_edge_case, validation_script, validation_report, stability_check, GSEA_evaluation, performance, edge_case_input, known_risk
   - Brief assessment of what it tests or validates
   - Caveat if the asset is not directly runnable or has ambiguous provenance
6. Produce `4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md` with:
   - Summary of scope and approach
   - Categorized inventory of candidate stress-test assets
   - For each category, a table with asset path, type, relevance, and notes
   - Cross-reference to T-007 validation evidence index to show overlap and gaps
   - Honest record of missing or ambiguous leads (e.g., "suite run output referenced but not found")
   - Guidance for later tasks on how to use this map
7. Produce `4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv` with:
   - One row per candidate asset
   - Columns: category, migrated_path, original_path (if known), asset_type, relevance, runnable_claim, T-007_cross_ref, notes

## Constraints

- Do not scan the unregistered legacy root (`/Users/dudu/Documents/3_Project/8_functional_query`). Use only the flat asset library and predecessor artifacts.
- Do not claim any old script is runnable in the current environment. Mark all scripts with `runnable_claim: false` unless explicitly verified.
- Record missing or ambiguous leads honestly. If a validation report references a file not found in the flat library, note the discrepancy.
- Date format for deliverables: `vYYYYMMDD` using the execution date.

## Forbidden

- No execution or modification of legacy scripts.
- No modification of files in the flat asset library.
- No modification of predecessor task artifacts.
- No creation of symlinks or directory copies outside `4_artifact/`.
- No comparison with external databases or web sources.

## Web Search Allowance

Allowed: no
Reason: All required source material is available in migrated project assets and predecessor artifacts.

## Deliverables

| Expected output | Target path | Required |
|-----------------|-------------|----------|
| Legacy stress test source map | 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md | yes |
| Stress test candidate asset index | 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv | yes |

## Acceptance Criteria

- Source map covers all validation_reports/, index_builders/ test scripts, query/resolver code, and GSEA evaluation scripts.
- Each candidate asset has a clear relevance category and provenance.
- Missing or ambiguous leads are explicitly documented, not silently omitted.
- CSV index is machine-readable with consistent columns.
- No legacy-root paths appear in the deliverables (use migrated paths or explicit "not migrated" notation).
- The deliverables reference and complement, not duplicate, the T-007 validation evidence index.

## Failure / Stop Rules

- If the flat asset library is not accessible or is empty, stop and report the precondition failure.
- If the migration manifest is missing critical path mapping, note the gap and proceed with available information.
- If more than 10% of referenced files in validation reports cannot be located in the flat library, flag this as a systematic migration gap.
- If a predecessor artifact (A-003 through A-009) cannot be read, proceed without it and document the limitation.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results (optional for this task; use markdown if sufficient).

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-002
    source_artifact_id: D-001
    path: 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/
    reason: "Primary browse source for all migrated legacy materials potentially related to stress testing, resolver validation, and edge cases"
  - id: A-002
    source_task: T-002
    source_artifact_id: D-002
    path: 3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/migration_manifest_v20260614.json
    reason: "Full migration manifest to trace which stress-test files were migrated or excluded"
  - id: A-003
    source_task: T-001
    source_artifact_id: D-003
    path: 3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md
    reason: "Understanding legacy source structure and operational vs archive layers for stress-test context"
  - id: A-004
    source_task: T-001
    source_artifact_id: D-004
    path: 3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/project_background_extraction_report.md
    reason: "Project background to understand why certain stress-test assets were created"
  - id: A-005
    source_task: T-007
    source_artifact_id: D-002
    path: 3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: "Current development state summary to understand documented validation gaps"
  - id: A-006
    source_task: T-007
    source_artifact_id: D-004
    path: 3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv
    reason: "Existing validation evidence index to avoid redundant cataloging and identify gaps"
  - id: A-007
    source_task: T-007
    source_artifact_id: D-005
    path: 3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: "Known gaps and risks to cross-reference against discovered stress-test materials"
  - id: A-008
    source_task: T-002
    source_artifact_id: D-005
    path: 3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md
    reason: "Structure explanation for navigating the flat library"
  - id: A-009
    source_task: T-002
    source_artifact_id: D-007
    path: 3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md
    reason: "Not-migrated assets that may include stress-test content explicitly excluded"
optional: []
forbidden:
  - path: /Users/dudu/Documents/3_Project/8_functional_query
    reason: "Legacy root is not registered; use flat asset library and predecessor artifacts only"
  - path: 1_project_init/
    reason: "Project protocol and task registration not needed for this execution"
output:
  - path: 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md
    type: document
  - path: 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv
    type: table
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets
  - /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map
  - /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state
  - /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-055 01_legacy_stress_test_source_map

## Check Verdict
green_check

## CyHex Boundaries
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map
- Allowed write dirs: 3_execution/, 4_artifact/, 5_report/
- Forbidden dirs: /Users/dudu/Documents/3_Project/8_functional_query, 1_project_init/, predecessor task folders (T-001, T-002, T-007 contents under 3_phase_digestion/)
- Required registry: 1_asset/registration.yaml (all 9 assets preflight ok)
- Must stop if: flat asset library inaccessible, >10% of referenced files not found in flat library, any predecessor artifact (A-003~A-009) unreadable (note the limitation but proceed)

## Objective Restatement
Create a source map of migrated legacy materials related to PxFquery stress testing, complex queries, resolver validation, edge cases, and old validation scripts/reports. This is a candidate catalog--not execution, not validation. Deliverables: a structured markdown guide and a CSV index for later task use.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ | Primary browse source for migrated stress-test/validation materials | ok |
| A-002 | T-002 migration_manifest_v20260614.json | Trace migrated/excluded files and original paths | ok |
| A-003 | T-001 old_asset_structure_report.md | Legacy source structure context | ok |
| A-004 | T-001 project_background_extraction_report.md | Why stress-test assets were created | ok |
| A-005 | T-007 pxfquery_development_state_report_v20260617.md | Current development state and known validation gaps | ok |
| A-006 | T-007 pxfquery_validation_evidence_index_v20260617.csv | Existing validation evidence (15 entries) to avoid duplication | ok |
| A-007 | T-007 pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps/risks for cross-reference | ok |
| A-008 | T-002 flat_asset_library_structure_zh_v20260615.md | Structure explanation for navigating flat library | ok |
| A-009 | T-002 not_migrated_assets_report_zh_v20260616.md | Explicitly excluded assets that may contain stress-test content | ok |

## Execution Strategy
1. Read A-005, A-006, A-007 to establish the known validation landscape and identify gaps that stress-test sourcing should fill.
2. Read A-002 and A-009 to map stress-test-related entries (filter manifest for keywords: stress, test, validate, smoke, edge, stability, suite) and record not-migrated items.
3. Browse A-001 high-priority directories (reports/validation_reports/ 57 items, code/index_builders/ 19 items, code/pxfquery_package/query/ 5 items, data/query_indexes/ 9 items, reports/digested_context/ 9 items, code/analysis_scripts/ 55 items, results/gsea_tables/ 6 items). Read README files and key scripts/reports to classify relevance.
4. For each candidate asset, record: migrated path, original path, asset type, stress-test relevance category, assessment, runnable_claim (always false), and T-007 cross-reference where applicable.
5. Write legacy_stress_test_source_map_vYYYYMMDD.md: summary, categorized inventory tables per category, cross-reference with A-006, missing/ambiguous leads, guidance for later tasks.
6. Write stress_test_candidate_asset_index_vYYYYMMDD.csv: one row per candidate with columns category, migrated_path, original_path, asset_type, relevance, runnable_claim, T-007_cross_ref, notes.
7. Register both deliverables in 4_artifact/registry.yaml, write 5_report/completion.md.

## Conservative Execution Advice
- Start with: read A-006 (validation evidence index, only 15 rows) and A-002 (migration manifest) to establish a baseline before any directory browsing.
- Smoke/demo command or method: do a single directory scan (reports/validation_reports/) and produce 2-3 candidate rows before committing to full scan of all 7 directories.
- Full run only after: the first 2-3 rows match the expected schema and relevance categories.
- Cost/time risk: low. No API calls, no computation, no network access. Pure file-system read-and-catalog work. The flat library has ~160 files total across target directories; browsing is fast.
- Checkpoint advice: after completing the validation_reports/ scan (largest directory), checkpoint the partial CSV to avoid data loss.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Legacy stress test source map | 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md | Covers all 7 target directories; has categorized inventory tables; cross-references A-006; documents missing leads |
| Stress test candidate asset index | 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv | One row per candidate; all 8 columns present; machine-readable; no legacy-root paths |

## Failure / Stop Conditions
- Flat asset library inaccessible or empty: immediate stop, write 5_report/blocked.md.
- More than ~10% of validation-report-referenced files not found in flat library: flag as systematic migration gap but continue.
- Predecessor artifact (A-003~A-009) unreadable: document limitation and proceed.
- Migration manifest missing critical path mapping: note gap and proceed.

## Notes For Delivery QA
- All 9 assets preflight ok; all symlinks resolve. Flat library target directories all exist with substantial content (57+9+19+5+9+55+6 items).
- The T-007 validation evidence index has 15 entries covering validation_reports/; the source map should complement, not duplicate, these 15 entries. Focus on scripts, indexes, GSEA tables, and any validation reports NOT already in A-006.
- The meta.yaml shows sub_status: check_failed from a prior cycle. This green_check should allow the executing AI to proceed.
- This task is digestion-phase, so 2_project_asset/ browsing is permitted. No legacy-root access needed.
- runnable_claim must always be false for all entries.
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-055 01_legacy_stress_test_source_map
Status: active | Executor: opencode
Objective: Create a source map for migrated legacy materials that may relate to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports.

Deliverables: 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md and 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv.

Reference T-001 because it defines legacy background, old structure interpretation, and source authority rules. Reference T-002 because it defines the migrated flat asset library and prevents direct legacy-root wandering. Reference T-007 because it summarizes current development asset/code/index/report maturity.

Important constraints: do not scan the unregistered legacy root; do not claim any old script is runnable; create candidate source mapping only; record missing or ambiguous leads honestly.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-055 01_legacy_stress_test_source_map — Protocol

## Objective

Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. The source map must be a structured guide that later tasks can use to locate, assess, and reuse these materials without directly scanning the unregistered legacy root.

## Position In Project

This is a digestion-phase task under G-005 (legacy stress test asset digestion). It follows T-001 (legacy semantic digestion), T-002 (flat asset migration), and T-007 (development state digestion). This task does not execute, run, or validate any old script. It produces a candidate map only, enabling later assessment tasks to proceed without legacy-root access.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|----------|-------------|------|------------|
| A-001 | T-002 | 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ | Primary browse source for all migrated legacy materials that may contain stress-test/validation content |
| A-002 | T-002/D-002 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/migration_manifest_v20260614.json | Full migration manifest to trace which stress-test files were migrated, their source paths, and any not-migrated items |
| A-003 | T-001/D-003 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md | Understanding legacy source structure and identification of operational vs archive layers |
| A-004 | T-001/D-004 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/project_background_extraction_report.md | Project background context for understanding why certain stress-test assets were created |
| A-005 | T-007/D-002 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development state summary to understand which validation gaps are already documented |
| A-006 | T-007/D-004 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Existing validation evidence index to avoid redundant cataloging and identify gaps |
| A-007 | T-007/D-005 | ../../../3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps and risks to cross-reference against discovered stress-test materials |
| A-008 | T-002/D-005 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md | Chinese structure explanation for the flat library navigation |
| A-009 | T-002/D-007 | ../../../3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md | Record of intentionally not-migrated assets; may contain stress-test content that was explicitly excluded |

## Execution Steps

1. Read A-001 (flat asset library) structure to understand available directories.
2. Read A-005, A-006, A-007 (T-007 handoff) to understand already-documented validation landscape.
3. Read A-002 (migration manifest) and A-009 (not-migrated report) to identify stress-test-related entries.
4. Browse the following high-priority directories within A-001 for stress-test/validation content:
   - `reports/validation_reports/` — resolver validation, suite runs, stability checks, known risks
   - `code/index_builders/` — test scripts (test_resolver_smoke, test_forward_matrix, verify_resolver_cases, run_forward_question_suite, validate_act1, check_llm_stability)
   - `code/pxfquery_package/query/` — resolver pipeline source with forward search policy (L1-L4 logic)
   - `data/query_indexes/` — index files used by the resolver for query resolution
   - `reports/digested_context/` — any context reports mentioning validation outcomes
   - `code/analysis_scripts/` — GSEA evaluation scripts (cp_gsea_eval, sh_gsea_eval, xpr_gsea_eval) and analysis notebooks
   - `results/gsea_tables/` — GSEA result tables used as validation baselines
5. For each candidate asset found, record:
   - Migrated path within flat library (or explicit not-migrated status)
   - Original legacy source path (from manifest or A-003/A-008 context)
   - Asset type: script, report, data, index, result, design_doc
   - Stress-test relevance category: complex_query, resolver_edge_case, validation_script, validation_report, stability_check, GSEA_evaluation, performance, edge_case_input, known_risk
   - Brief assessment of what it tests or validates
   - Caveat if the asset is not directly runnable or has ambiguous provenance
6. Produce `4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md` with:
   - Summary of scope and approach
   - Categorized inventory of candidate stress-test assets
   - For each category, a table with asset path, type, relevance, and notes
   - Cross-reference to T-007 validation evidence index to show overlap and gaps
   - Honest record of missing or ambiguous leads (e.g., "suite run output referenced but not found")
   - Guidance for later tasks on how to use this map
7. Produce `4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv` with:
   - One row per candidate asset
   - Columns: category, migrated_path, original_path (if known), asset_type, relevance, runnable_claim, T-007_cross_ref, notes

## Constraints

- Do not scan the unregistered legacy root (`/Users/dudu/Documents/3_Project/8_functional_query`). Use only the flat asset library and predecessor artifacts.
- Do not claim any old script is runnable in the current environment. Mark all scripts with `runnable_claim: false` unless explicitly verified.
- Record missing or ambiguous leads honestly. If a validation report references a file not found in the flat library, note the discrepancy.
- Date format for deliverables: `vYYYYMMDD` using the execution date.

## Forbidden

- No execution or modification of legacy scripts.
- No modification of files in the flat asset library.
- No modification of predecessor task artifacts.
- No creation of symlinks or directory copies outside `4_artifact/`.
- No comparison with external databases or web sources.

## Web Search Allowance

Allowed: no
Reason: All required source material is available in migrated project assets and predecessor artifacts.

## Deliverables

| Expected output | Target path | Required |
|-----------------|-------------|----------|
| Legacy stress test source map | 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md | yes |
| Stress test candidate asset index | 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv | yes |

## Acceptance Criteria

- Source map covers all validation_reports/, index_builders/ test scripts, query/resolver code, and GSEA evaluation scripts.
- Each candidate asset has a clear relevance category and provenance.
- Missing or ambiguous leads are explicitly documented, not silently omitted.
- CSV index is machine-readable with consistent columns.
- No legacy-root paths appear in the deliverables (use migrated paths or explicit "not migrated" notation).
- The deliverables reference and complement, not duplicate, the T-007 validation evidence index.

## Failure / Stop Rules

- If the flat asset library is not accessible or is empty, stop and report the precondition failure.
- If the migration manifest is missing critical path mapping, note the gap and proceed with available information.
- If more than 10% of referenced files in validation reports cannot be located in the flat library, flag this as a systematic migration gap.
- If a predecessor artifact (A-003 through A-009) cannot be read, proceed without it and document the limitation.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results (optional for this task; use markdown if sufficient).

### Selected Assets (9)
- A-001 [archive] legacy_flat_asset_library — path: 1_asset/legacy_flat_asset_library — origin: T-002/D-001: migrated flat asset library v20260614
- A-002 [table] migration_manifest — path: 1_asset/migration_manifest.json — origin: T-002/D-002: migration_manifest_v20260614.json
- A-003 [document] old_asset_structure_report — path: 1_asset/old_asset_structure_report.md — origin: T-001/D-003: old_asset_structure_report.md
- A-004 [document] project_background_extraction_report — path: 1_asset/project_background_extraction_report.md — origin: T-001/D-004: project_background_extraction_report.md
- A-005 [document] pxfquery_development_state_report — path: 1_asset/pxfquery_development_state_report.md — origin: T-007/D-002: pxfquery_development_state_report_v20260617.md
- A-006 [table] pxfquery_validation_evidence_index — path: 1_asset/pxfquery_validation_evidence_index.csv — origin: T-007/D-004: pxfquery_validation_evidence_index_v20260617.csv
- A-007 [document] pxfquery_development_gap_and_risk_list — path: 1_asset/pxfquery_development_gap_and_risk_list.md — origin: T-007/D-005: pxfquery_development_gap_and_risk_list_v20260617.md
- A-008 [document] flat_asset_library_structure_zh — path: 1_asset/flat_asset_library_structure_zh.md — origin: T-002/D-005: flat_asset_library_structure_zh_v20260615.md
- A-009 [document] not_migrated_assets_report_zh — path: 1_asset/not_migrated_assets_report_zh.md — origin: T-002/D-007: not_migrated_assets_report_zh_v20260616.md

### Asset Rules

### Required
- 2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/ — Primary browse source for all migrated legacy materials potentially related to stress testing, resolver validation, and edge cases
- 3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/migration_manifest_v20260614.json — Full migration manifest to trace which stress-test files were migrated or excluded
- 3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/old_asset_structure_report.md — Understanding legacy source structure and operational vs archive layers for stress-test context
- 3_phase_digestion/goal_legacy_asset_migration/task_audit_legacy_assets/4_artifact/2_persist/project_background_extraction_report.md — Project background to understand why certain stress-test assets were created
- 3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md — Current development state summary to understand documented validation gaps
- 3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv — Existing validation evidence index to avoid redundant cataloging and identify gaps
- 3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md — Known gaps and risks to cross-reference against discovered stress-test materials
- 3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/flat_asset_library_structure_zh_v20260615.md — Structure explanation for navigating the flat library
- 3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/not_migrated_assets_report_zh_v20260616.md — Not-migrated assets that may include stress-test content explicitly excluded
### Forbidden
- /Users/dudu/Documents/3_Project/8_functional_query — Legacy root is not registered; use flat asset library and predecessor artifacts only
- 1_project_init/ — Project protocol and task registration not needed for this execution
### Output
- 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md
- 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv

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

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/execution_handoff.md`

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
