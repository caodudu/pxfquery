# Delivery QA Prompt
Generated: 2026-06-26 01:48

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

## Functional Delivery Goal

PxFquery's project-level functional goal is not limited to static matrix lookup. A project-valid package must preserve the intended user-facing query experience:

- forward query: perturbation and biological context to functional response;
- reverse query: functional target and biological context to candidate perturbations;
- resolver-mediated natural-language or semi-structured query entry;
- exact, proxy, and not-found evidence routing for sparse biological coverage;
- LLM-assisted parsing and summarization through the current configured AI service when a milestone requires the user-facing resolver layer;
- deterministic fallback and transparent evidence metadata when LLM or proxy routing fails.

Milestones may stage these capabilities in layers, but a milestone may not silently redefine PxFquery as only deterministic dictionary or matrix lookup if the user-defined milestone requires resolver, LLM, proxy, or transfer behavior. Any proposed scope reduction, deferral, or optionalization of a functional capability must be explicitly reported to the user before task creation and must receive user approval.

## Manuscript Goal

Prepare for a realistic MDPI Genes-style submission by emphasizing a narrow, reproducible functional genomics workflow and a concrete biological case study, rather than presenting PxFquery as a broad AI-agent platform.

This manuscript path is graduation-oriented and journal-fit-oriented. The target is not to build a genuinely high-novelty tool paper or to compete with venues such as Bioinformatics, Nature-family journals, or other high-bar computational biology outlets. The work should look sufficiently substantial in the style of recent Genes papers while remaining practically lightweight, easy t

...[truncated by CyHex prompt assembler: 1049 chars omitted]
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


...[truncated by CyHex prompt assembler: 3052 chars omitted]
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
- T-002 migration outputs define which assets were migrated, reda

...[truncated by CyHex prompt assembler: 565 chars omitted]
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

Task dependency and artifact lineage edges were backfilled into `1_project_init/2_task_registration/task_graph.yaml` from existing asset registrations, artifact registries, and completion reports. This records current task references only; it does not

...[truncated by CyHex prompt assembler: 59 chars omitted]
```


### 1.3 Current Task And Delivery Snapshot
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
status: done
cyhex_version: 1.2.19
created: '2026-06-24'
started: null
completed: '2026-06-24'
notes: 旧压力测试资产源映射
fast_pass_permission: green
sub_status: ''
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:20:30'
auto_recovery:
  execute:
    source_session_id: cli_5b7a3793ec0a
    attempts: 1
    last_attempt_at: '2026-06-24T05:48:41'
  deliver:
    source_session_id: cli_8fefc997f59a
    attempts: 1
    last_attempt_at: '2026-06-24T06:01:04'
fast_pass_accepted: true
fast_pass_accepted_at: '2026-06-24T06:01:53'

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
6. Produce `4_art

...[truncated by CyHex prompt assembler: 3436 chars omitted]
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/registry.yaml`

```text
artifacts:
- id: D-001
  name: legacy_stress_test_source_map
  type: document
  path: 4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md
  status: accepted
  description: Categorized inventory of migrated legacy stress-test assets covering
    7 target directories in the flat asset library. Includes cross-reference to T-007
    validation evidence index, missing/ambiguous leads documentation, and guidance
    for later tasks.
  generated: '2026-06-24'
  identity: T-055/D-001
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-002
  name: stress_test_candidate_asset_index
  type: table
  path: 4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv
  status: accepted
  description: 'Machine-readable CSV index of stress-test candidate assets. Columns:
    category, migrated_path, original_path, asset_type, relevance, runnable_claim,
    T-007_cross_ref, notes.'
  generated: '2026-06-24'
  identity: T-055/D-002
  role: data
  core: false
  lineage_anchor: false
  stars: 2

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/completion.md`

```text
# Completion Report — T-055 01_legacy_stress_test_source_map

Generated: 2026-06-24

## Status
Completed.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Legacy stress test source map | `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` | Accepted |
| Stress test candidate asset index | `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` | Accepted |

## Coverage Summary

All 7 target directories were browsed and cataloged:
- `reports/validation_reports/` — 57 items (15 overlapped with T-007, ~42 newly cataloged)
- `code/index_builders/` — 19 items (6 validation scripts, 6 index builders, 6 demos, 1 install doc)
- `code/pxfquery_package/query/` — 5 items (resolver.py 1072 lines, forward.py, reverse.py, init, pycache)
- `data/query_indexes/` — 9 index files (function_index.json confirmed missing)
- `reports/digested_context/` — 9 items (minimal validation relevance)
- `code/analysis_scripts/` — 55 items (GSEA eval scripts, notebooks, duplicates)
- `results/gsea_tables/` — 6 large symlink items (244-372MB each)

Total candidate assets cataloged: ~160 entries in the CSV index.

## Key Findings

1. **Strongest validation baseline**: M-0386 (test_forward_matrix.py) with deterministic 7/7 pass rate.
2. **Critical gap**: `function_index.json` missing from migrated query indexes. Must be rebuilt via M-0373.
3. **LLM stability risk**: 6/9 success rate documented; conservative claims advised.
4. **Performance data**: always_LLM is ~200x slower than hybrid_fast (167.3s vs 0.825s for comparable queries).
5. **Script path assumptions**: All scripts use legacy workspace paths; none are directly runnable in current environment.
6. **Duplicate scripts**: M-013x and M-034x/035x series appear to be duplicates from different legacy versions.
7. **Systematic migration gap**: No GSEA table symlinks >10% of referenced files were unresolvable, but the function_index.json gap is significant.

## Notes

- `runnable_claim: false` set for all entries per protocol constraint.
- T-007 cross-reference documented in source map section 3.
- Missing/ambiguous leads documented in source map section 4.
- Guidance for later tasks provided in source map section 5.
- No legacy-root paths appear in deliverables.
- No modifications made to flat asset library or predecessor artifacts.

```

### AI Handoff: handoff_ai_use.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/handoff_ai_use.md`

```text
# AI Handoff: T-055 01_legacy_stress_test_source_map

## Task Goal
Create a source map of migrated legacy materials potentially related to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports. This is a candidate catalog only -- no execution, no validation.

## What Was Delivered
- `legacy_stress_test_source_map_v20260624.md`: Categorized inventory of ~160 candidate stress-test assets across 7 target directories in the flat asset library. Includes cross-reference to T-007 validation evidence index, missing/ambiguous leads, and guidance for later tasks.
- `stress_test_candidate_asset_index_v20260624.csv`: Machine-readable index with one row per candidate asset (8 columns).

## Core Artifacts
| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` | Primary catalog of all stress-test candidates with relevance categories and T-007 cross-ref | Read first to identify which assets to use for validation suite design |
| D-002 | `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` | Queryable machine-readable index for filtering by category, type, or cross-ref | Load as DataFrame for filtering/analysis |

## Supporting Artifacts
- `4_artifact/3_document/execution_report_v20260624.html` — execution process summary
- `4_artifact/3_document/result_report_v20260624.html` — result summary for human review

## Downstream Use
1. **Validation suite design**: Use section 2.1 (validation scripts) and section 5 guidance to build a current-environment validation suite.
2. **Gap remediation**: Rebuild `function_index.json` via M-0373_build_function_index.py.
3. **Baseline comparison**: Use M-0386 (test_forward_matrix.py) as primary regression test.
4. **Performance characterization**: Reference M-0277 (timing) and M-0275 (hybrid_fast v3) for expectations.
5. **LLM risk assessment**: Reference M-0377 and M-0267 (6/9 success rate) for conservative claims.

## Known Limits / Risks
- All scripts marked `runnable_claim: false` — none are directly runnable in current environment.
- `function_index.json` is missing from migrated query indexes (must be rebuilt).
- GSEA eval scripts have HPC-specific dependencies (SLURM, scanpy, gseapy).
- GSEA tables in results/gsea_tables/ are symlink placeholders (244-372MB each).
- Duplicate script pairs exist (M-013x vs M-034x/035x series).
- Suite run variants require deduplication.

## Do Not Read / Do Not Reuse
- Legacy root (`/Users/dudu/Documents/3_Project/8_functional_query`) — not registered for task access.
- Predecessor task folders (T-001, T-002, T-007) — outputs are already consumed via asset registry.
- `1_project_init/` — not needed for stress-test source map consumption.
- Flat asset library (`2_project_asset/`) — read-only; do not modify.

## Recommended Next Reads
1. `4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md` — full catalog
2. `4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv` — machine index
3. `5_report/completion.md` — execution summary

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/5_report/delivery_qa.md`

```text
# Delivery QA: T-055 01_legacy_stress_test_source_map

## Verdict
yellow_repair

## Checks Performed
1. ✅ Protocol deliverables present: `legacy_stress_test_source_map_v20260624.md` and `stress_test_candidate_asset_index_v20260624.csv`
2. ✅ `4_artifact/registry.yaml` exists, registers D-001 and D-002 (both accepted)
3. ✅ Registry paths exist and resolve
4. ✅ Accepted outputs are under `4_artifact/`, not under `3_execution/`
5. ✅ `3_execution/` is empty (appropriate for read-only cataloging task)
6. ✅ `5_report/completion.md` matches registry and files
7. ❌ HTML reports (`execution_report_v20260624.html`, `result_report_v20260624.html`) missing from `4_artifact/3_document/`
8. ❌ `5_report/handoff_ai_use.md` missing
9. ✅ Core deliverable content (source map, CSV) is substantive and well-structured

## Repairs Made
- Created `4_artifact/3_document/execution_report_v20260624.html` — execution process summary
- Created `4_artifact/3_document/result_report_v20260624.html` — result summary for human review
- Created `5_report/handoff_ai_use.md` — structured handoff for future AI tasks
- Created `5_report/delivery_qa.md` — this file

## Remaining Issues
None. All packaging gaps have been filled. Core deliverables were already complete and correct.

## Execute Revision Required
no

## Next Action
human_acceptance

```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-055 | Name: 01_legacy_stress_test_source_map
- Objective: Create a source map for migrated legacy materials that may relate to PxFquery stress testing, complex queries, resolver validation, strict edge cases, and old validation scripts/reports.

Deliverables: 4_artifact/2_persist/legacy_stress_test_source_map_vYYYYMMDD.md and 4_artifact/5_table/stress_test_candidate_asset_index_vYYYYMMDD.csv.

Reference T-001 because it defines legacy background, old structure interpretation, and source authority rules. Reference T-002 because it defines the migrated flat asset library and prevents direct legacy-root wandering. Reference T-007 because it summarizes current development asset/code/index/report maturity.

Important constraints: do not scan the unregistered legacy root; do not claim any old script is runnable; create candidate source mapping only; record missing or ambiguous leads honestly.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map`

The only allowed outside-task reads are the CyHex protocol and project protocol files listed above.

Do not scan predecessor tasks.
Do not scan `2_project_asset/`.
Do not open raw input assets by default.
Do not read arbitrary project folders.
Do not read prompts from `2_protocol/0_prompt/` unless a delivery anomaly specifically requires checking what execution was told. In green-pass mode, do not read config/check/execute prompt files.

If you believe outside-task information is required, stop expansion and record it in `5_report/delivery_qa.md` as a blocker or uncertainty.

## 4. Human Report Rewrite Fast Path

Use this fast path immediately when the only visible delivery issue is that the HTML reports are missing, outdated, empty, or too thin for human understanding.

In this mode, do not inspect old HTML reports. Old thin reports are not evidence; they are the defect being repaired.

Do not read raw input assets, predecessor tasks, project asset libraries, old prompt files, or large execution outputs. Use only the assembled snapshot above plus these task-local files if the snapshot is insufficient:

- `4_artifact/registry.yaml`
- `5_report/completion.md`
- `5_report/handoff_ai_use.md`
- `2_protocol/2_protocol_split/protocol.md`

For this fast path, temporarily switch role:

You are no longer writing for CyHex internals, future agents, or a validator. You are writing for a human project owner who jumps between many tasks and opens one task at random. That person should understand what happened without reading protocol files, registries, CLI logs, or predecessor tasks.

Write both files before doing anything else:

1. `4_artifact/3_document/execution_report_v20260626.html`
2. `4_artifact/3_document/result_report_v20260626.html`

The two HTML reports are for human reading, not machine bookkeeping. They must be standalone Chinese narrative reports with concrete task-specific information.

Do not write them as checklist/audit notes. Avoid rows that merely say "file exists", "status accepted", or "check passed". Use tables only for a short artifact guide if it genuinely helps. Most content should be natural-language paragraphs that explain intent, context, decisions, concrete results, and value.

Minimum substance target:

- Each HTML report should have at least 900 Chinese characters of visible human-facing explanation.
- Each major section should contain a paragraph of 3-6 sentences, not just bullets.
- Every paragraph should mention task-specific nouns, artifacts, findings, counts, decisions, or limits from this task.
- A reader should be able to answer: "Why was this task created?", "What did it actually do?", "What did we learn?", "Why does this matter to the project?", and "What should I open or reuse next?"

Disallowed weak style:

- A bare list of files.
- A QA checklist with green checks.
- Generic phrases such as "completed successfully" without saying what was completed.
- Copying old HTML with only date/path changes.
- Mechanical section filling where the same sentence would fit any task.

`execution_report_v20260626.html` must include these sections with substantive paragraphs:

- 任务意图: why this task existed in this project.
- 输入资产与依据: which registered/completion evidence was used and why it was sufficient.
- 实际执行过程: what the original execution actually did, in concrete steps.
- 关键判断与证据: the task-specific findings, counts, files, test outcomes, or decisions.
- 交付物清单: accepted outputs and how to read/use them.
- 边界与未完成事项: what was not done, risk, and why it is acceptable or needs follow-up.

`result_report_v20260626.html` must include these sections with substantive paragraphs:

- 一句话结论: the task result in one plain sentence.
- 项目背景: how this task fits the current project.
- 核心结果: the concrete result, not just file names.
- 项目价值: why the result matters downstream.
- 交付物导读: what each artifact is for and which one to open first.
- 后续使用方式: how a future human or AI should reuse the result.
- 边界与风险: limits, missing pieces, and caution.

After writing the two HTML reports, update `5_report/delivery_qa.md` and `5_report/handoff_ai_use.md` only if needed. Then stop and return the final response. Do not continue reading files after both reports are written unless a write failed.

## 5. Default Mode: Lightweight Confirmation

Start in Green-pass mode.

Check only whether the delivery structure is internally consistent:

1. `protocol.md` promised deliverables are present or reasonably accounted for.
2. `4_artifact/registry.yaml` exists and registers every accepted/reusable deliverable.
3. Registry paths actually exist.
4. Accepted/reusable outputs are under `4_artifact/`, not only under `3_execution/`.
5. `3_execution/` contains only scripts, temporary files, logs, checkpoints, or resumable job state.
6. `completion.md` matches registry and actual files.
7. Required HTML reports exist:
   - `4_artifact/3_document/execution_report_v20260626.html`
   - `4_artifact/3_document/result_report_v20260626.html`
8. HTML reports are useful for human review and consistent with registry/completion.
   Default language is Chinese unless protocol or human instruction explicitly requires another language.
   "Useful" means a person who did not participate in the task can understand the task intent, input basis, actual work, core result, project value, deliverable usage, follow-up use, and boundaries by reading only the two HTML reports.
9. There is enough handoff information for future AI tasks.

If all checks pass, do not open artifact contents. Only make small metadata/reporting repairs if needed.

## 6. Escalation Triggers

Escalate from Green-pass to Yellow-repair or Red-return only if you find evidence of a problem.

Escalate when any of these occur:

- `completion.md` claims success but registry is empty or missing major outputs.
- A protocol-required deliverable is missing.
- Registry path does not exist.
- Registry describes a reusable/accepted output located only under `3_execution/`.
- HTML reports are missing, empty, inconsistent with actual deliverables, or too thin to explain the task to a human reader.
- Execution report shows failed commands, interrupted execution, or skipped required steps but completion claims success.
- Output descriptions are too vague for downstream reuse.
- A file appears to be a final result but is not registered.
- The task depends on outside information not authorized by protocol/assets.

## 7. Yellow Repair Permissions

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
   - `4_artifact/3_document/execution_report_v20260626.html`
   - `4_artifact/3_document/result_report_v20260626.html`
   Default language is Chinese unless protocol or human instruction explicitly requires another language.
   The revised reports must be standalone narrative reports, not file-existence summaries. The execution report must cover task intent, input basis, real work, evidence, deliverables, and boundaries. The result report must cover one-sentence conclusion, project background, core result, project value, deliverable guide, future use, and boundaries/risks.

Do not modify core deliverable logic, code, data, analysis results, or model outputs.

## 8. Red Return Rules

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

## 9. Registry Star Guidance

Use `stars` to indicate downstream importance:

- `5`: core deliverable, must be considered by downstream tasks.
- `4`: important support artifact, usually useful downstream.
- `3`: useful evidence or report, read when relevant.
- `2`: process support, mostly for audit/reproduction.
- `1`: low-level log, temporary evidence, or bookkeeping.

If a file should not be used downstream, do not over-rate it.

## 10. Required Output Files

At the end of delivery QA, ensure these files exist unless Red-return makes that inappropriate:

1. `4_artifact/registry.yaml`
2. `5_report/completion.md`
3. `5_report/handoff_ai_use.md`
4. `5_report/delivery_qa.md`
5. `4_artifact/3_document/execution_report_v20260626.html`
6. `4_artifact/3_document/result_report_v20260626.html`

## 11. handoff_ai_use.md Required Shape

Write `5_report/handoff_ai_use.md` in this structure:

```md
# AI Handoff: T-055 01_legacy_stress_test_source_map

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

## 12. delivery_qa.md Required Shape

Write `5_report/delivery_qa.md` in this structure:

```md
# Delivery QA: T-055 01_legacy_stress_test_source_map

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

## 13. Final Response

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
