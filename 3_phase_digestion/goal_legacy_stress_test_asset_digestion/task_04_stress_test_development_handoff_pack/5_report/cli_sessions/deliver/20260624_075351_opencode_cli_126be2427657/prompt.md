# Delivery QA Prompt
Generated: 2026-06-24 07:53

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-058
name: 04_stress_test_development_handoff_pack
phase: digestion
goal: goal_legacy_stress_test_asset_digestion
project: P-012
objective: 'Integrate the completed digestion outputs from tasks 01-03 into a development-phase
  handoff pack for a future PxFquery stress-test milestone.


  Deliverables: 4_artifact/2_persist/stress_test_development_handoff_pack_vYYYYMMDD.md
  and 4_artifact/2_persist/recommended_stress_test_milestone_tasks_vYYYYMMDD.md.


  Must use tasks 01, 02, and 03 because this task is an integration/handoff layer
  and should not redo source mapping, scenario inventory, or reuse-boundary judgment.
  Reference T-007 to keep the handoff aligned with current development asset understanding.


  Important constraints: do not implement or run stress tests; do not compensate for
  missing upstream quality by inventing results; recommend future development tasks
  only, and keep the result as digestion-stage asset handoff.'
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
fast_pass_last_auto_approved_at: '2026-06-24T07:23:00'
auto_recovery:
  check:
    source_session_id: cli_c9c3674d8454
    attempts: 1
    last_attempt_at: '2026-06-24T07:21:47'
  execute:
    source_session_id: cli_9c722234e19b
    attempts: 1
    last_attempt_at: '2026-06-24T07:41:13'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: legacy_stress_test_source_map
  type: document
  source: predecessor
  source_task: T-055
  source_artifact_id: D-001
  origin: T-055/D-001
  registered: '2026-06-24'
  path: 1_asset/legacy_stress_test_source_map.md
  symlink: true
  status: ready
  notes: Primary catalog of ~160 stress-test candidate assets across 7 target directories;
    needed for understanding legacy material landscape
  location: local
- id: A-002
  name: stress_test_candidate_asset_index
  type: table
  source: predecessor
  source_task: T-055
  source_artifact_id: D-002
  origin: T-055/D-002
  registered: '2026-06-24'
  path: 1_asset/stress_test_candidate_asset_index.csv
  symlink: true
  status: ready
  notes: Machine-readable CSV index for filtering stress-test candidates by category,
    type, relevance, and T-007 cross-ref
  location: local
- id: A-003
  name: stress_query_scenario_inventory
  type: document
  source: predecessor
  source_task: T-056
  source_artifact_id: D-001
  origin: T-056/D-001
  registered: '2026-06-24'
  path: 1_asset/stress_query_scenario_inventory.md
  symlink: true
  status: ready
  notes: Narrative inventory of 29 stress-test scenarios across 9 dimensions with
    rationale and evidence traceback
  location: local
- id: A-004
  name: stress_query_scenario_table
  type: table
  source: predecessor
  source_task: T-056
  source_artifact_id: D-002
  origin: T-056/D-002
  registered: '2026-06-24'
  path: 1_asset/stress_query_scenario_table.csv
  symlink: true
  status: ready
  notes: Tabular CSV of 29 stress-test scenarios; parseable for downstream test framework
    use
  location: local
- id: A-005
  name: legacy_stress_logic_reuse_boundary
  type: document
  source: predecessor
  source_task: T-057
  source_artifact_id: D-001
  origin: T-057/D-001
  registered: '2026-06-24'
  path: 1_asset/legacy_stress_logic_reuse_boundary.md
  symlink: true
  status: ready
  notes: Full reuse-boundary analysis covering 65 classified legacy assets with decisions
    and reasoning
  location: local
- id: A-006
  name: stress_logic_reuse_decision_matrix
  type: table
  source: predecessor
  source_task: T-057
  source_artifact_id: D-002
  origin: T-057/D-002
  registered: '2026-06-24'
  path: 1_asset/stress_logic_reuse_decision_matrix.csv
  symlink: true
  status: ready
  notes: 'Machine-readable CSV with columns: asset_name, asset_path, asset_type, reuse_decision,
    reasoning, risk_gap, recommended_action. 65 rows'
  location: local
- id: A-007
  name: pxfquery_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_state_report.md
  symlink: true
  status: ready
  notes: Summarizes intended product scope, implemented components, data/index readiness,
    validation state, and development interpretation
  location: local
- id: A-008
  name: pxfquery_development_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: Lists high-priority gaps, risks, claims to avoid, and safer claims for development
    phase
  location: local
- id: A-009
  name: pxfquery_development_phase_handoff
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-006
  origin: T-007/D-006
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_phase_handoff.md
  symlink: true
  status: ready
  notes: Provides recommended next development tasks and carry-forward guidance from
    T-007
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/2_protocol/2_protocol_split/protocol.md`

```text
# T-058 04_stress_test_development_handoff_pack — Protocol

## Objective

Integrate the completed digestion outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a single development-phase handoff pack. The pack serves as a structured bridge from the stress-test digestion goal to a future stress-test milestone in the development phase.

Produce two deliverables:
1. A narrative handoff pack consolidating what is known, reusable, risky, and missing across all three predecessor outputs.
2. A set of recommended future development tasks (not execution steps) that a stress-test milestone should include.

Reference T-007 to keep the handoff aligned with current development asset understanding (code maturity, index status, known gaps).

## Position In Project

This is the final integration task of `goal_legacy_stress_test_asset_digestion`. It is a pure digestion-stage handoff task:
- Does not implement or run stress tests.
- Does not compensate for missing upstream quality by inventing results.
- Recommends future development tasks only.

The output is a digestion-stage handoff pack, not a development-phase execution plan.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-055 | 4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md | Primary catalog of ~160 stress-test candidate assets; used to understand what legacy material exists and where |
| A-002 | T-055 | 4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv | Machine-readable index for filtering candidates by category, type, or relevance |
| A-003 | T-056 | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | Narrative inventory of 29 stress-test scenarios across 9 dimensions with rationale |
| A-004 | T-056 | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | Tabular scenario table; parseable for downstream test framework use |
| A-005 | T-057 | 4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md | Reuse-boundary analysis covering 65 classified legacy assets with decisions |
| A-006 | T-057 | 4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv | Machine-readable decision matrix with reuse_decision, reasoning, risk_gap, recommended_action per asset |
| A-007 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Current development-state understanding: code, data, index, and report maturity |
| A-008 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | High-priority gaps, risks, and claims-to-avoid for development phase |
| A-009 | T-007 | 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Recommended next development tasks and carry-forward guidance from T-007 |

## Execution Steps

1. **Read all registered inputs** (A-001 through A-009) to build a complete picture of the stress-test digestion landscape.
2. **Synthesize the three dimensions:**
   - From T-055: what legacy stress-test assets exist, their categories, and known gaps.
   - From T-056: what stress-test scenarios should be exercised, grouped by query dimension.
   - From T-057: which legacy assets are directly referable, which need rewrite, which are historical-only, and which are not usable.
3. **Cross-reference with T-007** to align the handoff with the current development state — ensuring recommendations are grounded in what the codebase actually supports today.
4. **Write the handoff pack** (`stress_test_development_handoff_pack_v20260624.md`):
   - Section 1: Summary of consolidated digestion findings (what the three predecessors collectively established).
   - Section 2: Asset-to-scenario cross-walk (which source assets map to which test scenarios).
   - Section 3: Reuse-ready assets (from T-057 decisions marked "direct reference").
   - Section 4: Rewrite-required assets and their risk profile.
   - Section 5: Known gaps and missing assets (from T-055 missing leads + T-057 "not usable" + T-007 gap list).
   - Section 6: Alignment with current development state (via T-007 cross-ref).
   - Section 7: Handoff integrity check (are predecessor outputs internally consistent? Any unresolved contradictions?).
5. **Write recommended milestone tasks** (`recommended_stress_test_milestone_tasks_v20260624.md`):
   - Define a logical task sequence for a future stress-test milestone.
   - Each recommended task should have: name, objective, estimated scope, predecessor dependency, and rationale anchored in T-055/056/057/007 evidence.
   - Do not prescribe implementation details — recommend what should be done, not how.
6. **Register both deliverables** in `4_artifact/registry.yaml`.
7. **Write `5_report/completion.md`**.

## Constraints

- Do not implement or run stress tests.
- Do not compensate for missing upstream quality by inventing results.
- Recommend future development tasks only; keep the result as digestion-stage asset handoff.
- Do not modify predecessor task outputs.
- Do not read raw legacy assets or scan unregistered directories.
- If predecessor outputs conflict or are ambiguous, record the conflict honestly rather than picking a side silently.

## Forbidden

- Running pxfquery code, queries, or tests.
- Modifying legacy scripts or source files.
- Creating new stress-test scenarios beyond what predecessors already describe.
- Reading unregistered predecessor task directories or `3_execution/`.
- Reading `2_protocol/0_prompt/` files.

## Web Search Allowance

Allowed: no
Reason: All information needed for this integration/handoff task is sourced from completed predecessor digestion outputs and T-007 development state. No external or current web information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Handoff pack | 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md | yes |
| Recommended milestone tasks | 4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md | yes |

## Acceptance Criteria

- The handoff pack integrates findings from all three predecessors (T-055, T-056, T-057) in a coherent, non-redundant narrative.
- The recommended milestone tasks are grounded in predecessor evidence, not invented.
- Cross-reference with T-007 is explicit and traceable.
- Gaps, risks, and ambiguous findings from predecessors are honestly carried forward, not patched.
- Both deliverables are registered in `4_artifact/registry.yaml`.
- `5_report/completion.md` is written.

## Failure / Stop Rules

- If any predecessor meta shows `status != done`, stop and report the incomplete dependency.
- If any required input asset (A-001 through A-009) cannot be read at its registered path, stop and report the missing asset.
- If predecessor outputs are internally contradictory in a way that prevents coherent synthesis, stop and escalate rather than guessing.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-055
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/2_persist/legacy_stress_test_source_map_v20260624.md
    reason: "Primary catalog of ~160 stress-test candidate assets; needed to understand what legacy material exists"
  - id: A-002
    source_task: T-055
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_01_legacy_stress_test_source_map/4_artifact/5_table/stress_test_candidate_asset_index_v20260624.csv
    reason: "Machine-readable index for filtering candidates by category, type, or relevance"
  - id: A-003
    source_task: T-056
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md
    reason: "Narrative inventory of 29 stress-test scenarios across 9 dimensions with rationale"
  - id: A-004
    source_task: T-056
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/5_table/stress_query_scenario_table_v20260624.csv
    reason: "Tabular scenario table; parseable for downstream test framework use"
  - id: A-005
    source_task: T-057
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/2_persist/legacy_stress_logic_reuse_boundary_v20260624.md
    reason: "Reuse-boundary analysis covering 65 classified legacy assets with decisions"
  - id: A-006
    source_task: T-057
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_03_legacy_stress_logic_reuse_boundary/4_artifact/5_table/stress_logic_reuse_decision_matrix_v20260624.csv
    reason: "Machine-readable decision matrix with reuse_decision, reasoning, risk_gap, recommended_action per asset"
  - id: A-007
    source_task: T-007
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: "Current development-state understanding: code, data, index, and report maturity"
  - id: A-008
    source_task: T-007
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: "High-priority gaps, risks, and claims-to-avoid for development phase"
  - id: A-009
    source_task: T-007
    source_artifact_id: D-006
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md
    reason: "Recommended next development tasks and carry-forward guidance from T-007"
optional: []
forbidden:
  - predecessor task directories (except registered paths)
  - legacy source root
  - T-041 task outputs
output:
  - path: 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md
    type: document
  - path: 4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md
    type: document
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 2_project_asset/
  - /Users/dudu/Documents/3_Project/8_functional_query
```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-058 04_stress_test_development_handoff_pack

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories (except registered paths), `2_project_asset/`, `/Users/dudu/Documents/3_Project/8_functional_query`, `2_protocol/0_prompt/` files
- Required registry: `1_asset/registration.yaml` (verified 9/9 assets ok)
- Must stop if: any A-001–A-009 cannot be read; predecessor outputs internally contradict; meta shows predecessor status != done

## Objective Restatement

Integrate the completed digestion outputs from T-055 (source map), T-056 (scenario inventory), and T-057 (reuse boundary) into a development-phase handoff pack. Produce two deliverables: a narrative handoff pack consolidating all three dimensions, and a set of recommended future stress-test milestone tasks. Cross-reference with T-007 to align with current development state. This is a pure digestion-stage handoff — do not implement or run stress tests, do not invent results to compensate for upstream quality.

## Selected Inputs

| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | 1_asset/legacy_stress_test_source_map.md → T-055/D-001 | Primary catalog of ~160 stress-test candidate assets; categorizes by type, relevance, T-007 cross-ref | ok |
| A-002 | 1_asset/stress_test_candidate_asset_index.csv → T-055/D-002 | Machine-readable CSV index for filtering stress-test candidates | ok |
| A-003 | 1_asset/stress_query_scenario_inventory.md → T-056/D-001 | Narrative inventory of 29 stress-test scenarios across 9 dimensions with rationale | ok |
| A-004 | 1_asset/stress_query_scenario_table.csv → T-056/D-002 | Tabular CSV of 29 scenarios; parseable for downstream use | ok |
| A-005 | 1_asset/legacy_stress_logic_reuse_boundary.md → T-057/D-001 | Reuse-boundary analysis: 65 classified legacy assets with decisions | ok |
| A-006 | 1_asset/stress_logic_reuse_decision_matrix.csv → T-057/D-002 | Machine-readable decision matrix: reuse_decision, reasoning, risk_gap, recommended_action per asset | ok |
| A-007 | 1_asset/pxfquery_development_state_report.md → T-007/D-002 | Current development-state understanding | ok |
| A-008 | 1_asset/pxfquery_development_gap_and_risk_list.md → T-007/D-005 | High-priority gaps, risks, and claims-to-avoid | ok |
| A-009 | 1_asset/pxfquery_development_phase_handoff.md → T-007/D-006 | Recommended next development tasks and carry-forward guidance | ok |

## Execution Strategy

1. **Re-read all 9 input assets** (A-001 through A-009) to build a complete picture. The checking phase has already confirmed all assets are readable and semantically self-consistent.

2. **Synthesize the three predecessor dimensions into a consolidated findings summary:**
   - T-055: ~160 candidate assets across 10 categories (validation scripts, validation reports, resolver source, query indexes, GSEA eval scripts, GSEA result tables, index builders, demo scripts, digested context, background tutorials). 8 known gaps/missing leads documented.
   - T-056: 29 stress-test scenarios across 9 dimensions (complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index). Each scenario has rationale, expected hit level, expected result, and source evidence anchors.
   - T-057: 65 classified legacy assets (10 direct reference, 11 rewrite needed, 38 historical evidence only, 6 not usable). Clear evidence hierarchy: M-0239 as report authority, deterministic path stronger than LLM, function_index.json as critical rebuild gap.

3. **Cross-reference with T-007 development state** (A-007, A-008, A-009):
   - Align the handoff with the 5-step development interpretation from A-007 (package runnability → index completeness → deterministic smoke → hybrid_fast → case study).
   - Map T-007 gap/risk list to the handoff's risk profile.
   - Use T-007's recommended tasks (D001–D005) as cross-validation for the milestone task recommendations.

4. **Write the handoff pack** (`stress_test_development_handoff_pack_v20260624.md`) with 7 sections:
   - Section 1: Summary of consolidated digestion findings
   - Section 2: Asset-to-scenario cross-walk (map source assets to test scenarios)
   - Section 3: Reuse-ready assets (10 direct-reference items from T-057)
   - Section 4: Rewrite-required assets and risk profile (11 scripts from T-057)
   - Section 5: Known gaps and missing assets (T-055 missing leads + T-057 not usable + T-007 gap list)
   - Section 6: Alignment with current development state (T-007 cross-ref)
   - Section 7: Handoff integrity check (predecessor consistency review)

5. **Write recommended milestone tasks** (`recommended_stress_test_milestone_tasks_v20260624.md`):
   - Logical task sequence for a future stress-test milestone.
   - Each task: name, objective, estimated scope, predecessor dependency, rationale anchored in T-055/056/057/007 evidence.
   - Do not prescribe implementation details.

6. **Register both deliverables** in `4_artifact/registry.yaml`.

7. **Write `5_report/completion.md`**.

## Conservative Execution Advice

- Start with: Reading all 9 input assets to confirm content coherence. The 5-report directory already has a cli_sessions folder and an existing completion.md; work alongside these, do not overwrite unrelated files.
- Smoke/demo method: Before writing full deliverable text, draft a brief outline of each section and verify it maps to the exact assets and predecessor evidence — this prevents scope drift into writing new analysis.
- Full run only after: All asset-to-scenario cross-walk entries are traceable to concrete rows/sections in the 6 input CSVs/MDs; no synthetic scenarios should appear.
- Cost/time risk: This is a text-synthesis task with no compute, network, or storage cost beyond reading existing files. Risk is scope drift (inventing scenarios) or omission (missing a documented gap).
- Checkpoint advice: After step 2 (synthesis), self-review that all key facts carry forward into the handoff pack. After step 4 section 7 (integrity check), verify no predecessor contradiction was suppressed.

## Expected Deliverables

| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Handoff pack | `4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md` | Contains all 7 required sections; all cross-references traceable to predecessor evidence; no invented scenarios |
| Recommended milestone tasks | `4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md` | Each task has name/objective/scope/dependency/rationale anchored in predecessor evidence; task count between 4-8; no implementation prescriptions |
| Updated registry | `4_artifact/registr

...[truncated by CyHex prompt assembler: 1631 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/4_artifact/registry.yaml`

```text
artifacts:
- id: D-001
  name: stress_test_development_handoff_pack
  type: document
  path: 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md
  version: v20260624
  created: '2026-06-24'
  status: delivered
  notes: 7-section narrative handoff pack consolidating T-055, T-056, T-057, and T-007
    findings into a single bridge from stress-test digestion to a future stress-test
    milestone.
  identity: T-058/D-001
  role: support
  core: false
  lineage_anchor: false
  stars: 4
- id: D-002
  name: recommended_stress_test_milestone_tasks
  type: document
  path: 4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md
  version: v20260624
  created: '2026-06-24'
  status: delivered
  notes: 7 recommended future development tasks (ST-M01 through ST-M07) forming a
    logical stress-test milestone sequence. Each task has name, objective, estimated
    scope, predecessor dependency, and rationale anchored in T-055/056/057/007 evidence.
  identity: T-058/D-002
  role: support
  core: false
  lineage_anchor: false
  stars: 4

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/5_report/completion.md`

```text
# Completion

Task: T-058 04_stress_test_development_handoff_pack
Completed: 2026-06-24

## Deliverables Produced

| ID | Deliverable | Path | Status |
|---|---|---|---|
| D-001 | Stress Test Development Handoff Pack | `4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md` | delivered |
| D-002 | Recommended Stress Test Milestone Tasks | `4_artifact/2_persist/recommended_stress_test_milestone_tasks_v20260624.md` | delivered |

## Execution Summary

All 9 registered input assets (A-001 through A-009) were read and synthesized. The three predecessor dimensions (T-055 source map, T-056 scenario inventory, T-057 reuse boundary) were cross-referenced with T-007 development state to produce a coherent handoff pack with 7 sections:

1. **Summary of consolidated digestion findings**: Synthesized ~160 cataloged assets, 29 stress-test scenarios, and 65 classified legacy assets into a unified evidence hierarchy.
2. **Asset-to-scenario cross-walk**: Mapped all 29 scenarios to their primary source assets with T-057 reuse decisions and T-007 cross-references.
3. **Reuse-ready assets**: Listed 10 direct-reference assets (8 reports + resolver.py + design docs) ready for immediate handoff.
4. **Rewrite-required assets and risk profile**: Cataloged 11 scripts needing rewrite with risk assessment, and ranked M-0373 (function index builder) as highest rewrite priority.
5. **Known gaps and missing assets**: Consolidated 19 gaps from T-055 (8), T-057 (1 not-usable group), and T-007 (11), ranked by priority.
6. **Alignment with current development state**: Mapped the handoff to T-007's 5-step development interpretation and safer claims.
7. **Handoff integrity check**: Verified cross-consistency of predecessor outputs; documented 4 honest ambiguities (Act-1 authority conflict, suite variant proliferation, GSEA symlinks, mode coexistence).

The recommended milestone tasks define 7 sequential tasks (ST-M01 through ST-M07) with objectives, scope estimates, dependencies, and rationale anchored in predecessor evidence.

## Integrity Check Pass

- All 29 T-056 scenarios are traceable to T-055 cataloged assets
- All T-057 reuse decisions are consistent with T-055 content descriptions
- T-007 cross-references are explicit in both Section 2 cross-walk and Section 6 alignment
- No new scenarios, assets, or test cases were invented
- Gaps and ambiguities from predecessors are carried forward honestly
- The deterministic 7/7 matrix test (M-0291) is independently identified as the strongest evidence by all three predecessors
- The `function_index.json` gap is independently confirmed by all three predecessors
- Both deliverables are registered in `4_artifact/registry.yaml`

## Constraint Compliance

- [x] Did not implement or run stress tests
- [x] Did not compensate for missing upstream quality by inventing results
- [x] Recommended future development tasks only; handoff is digestion-stage
- [x] Did not modify predecessor task outputs
- [x] Did not read raw legacy assets or scan unregistered directories
- [x] Did not read `2_protocol/0_prompt/` files
- [x] No web search performed (disallowed by protocol)
- [x] Both deliverables registered in `4_artifact/registry.yaml`
- [x] `5_report/completion.md` written
```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-058 | Name: 04_stress_test_development_handoff_pack
- Objective: Integrate the completed digestion outputs from tasks 01-03 into a development-phase handoff pack for a future PxFquery stress-test milestone.

Deliverables: 4_artifact/2_persist/stress_test_development_handoff_pack_vYYYYMMDD.md and 4_artifact/2_persist/recommended_stress_test_milestone_tasks_vYYYYMMDD.md.

Must use tasks 01, 02, and 03 because this task is an integration/handoff layer and should not redo source mapping, scenario inventory, or reuse-boundary judgment. Reference T-007 to keep the handoff aligned with current development asset understanding.

Important constraints: do not implement or run stress tests; do not compensate for missing upstream quality by inventing results; recommend future development tasks only, and keep the result as digestion-stage asset handoff.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack`

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
# AI Handoff: T-058 04_stress_test_development_handoff_pack

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
# Delivery QA: T-058 04_stress_test_development_handoff_pack

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
