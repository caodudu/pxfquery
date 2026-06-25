# Delivery QA Prompt
Generated: 2026-06-24 05:11

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-056
name: 02_stress_query_scenario_inventory
phase: digestion
goal: goal_legacy_stress_test_asset_digestion
project: P-012
objective: 'Abstract a future stress-test scenario inventory from migrated materials
  and existing digestion results, focusing on complex queries, strict queries, boundary
  queries, no-hit behavior, overly broad results, proxy/exact matching, and difficult
  perturbation/cell-line/function combinations.


  Deliverables: 4_artifact/2_persist/stress_query_scenario_inventory_vYYYYMMDD.md
  and 4_artifact/5_table/stress_query_scenario_table_vYYYYMMDD.csv.


  Reference T-007 because it explains forward/reverse query intent, resolver/index
  status, and current development-state boundaries. Use T-041 only as a may input
  if it is done; if T-041 is still active or unavailable, omit it completely and proceed
  from T-007.


  Important constraints: deliver stress-test scenarios and rationale only, not implementation;
  do not run large tests; do not treat old scripts as current acceptance criteria.'
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
fast_pass_last_auto_approved_at: '2026-06-24T05:09:48'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: pxfquery_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002 — pxfquery_development_state_report_v20260617.md
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_state_report.md
  symlink: true
  status: ready
  notes: 'Core reference: forward/reverse query mechanism, resolver proxy/exact matching
    modes, index gaps, validation state — essential for designing stress-test scenario
    categories.'
  location: local
- id: A-002
  name: pxfquery_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005 — pxfquery_development_gap_and_risk_list_v20260617.md
  registered: '2026-06-24'
  path: 1_asset/pxfquery_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: Directly lists high-priority gaps, risky patterns, claims to avoid — feeds
    stress-test scenario categories like NOT_FOUND behavior, proxy instability, LLM
    stability risks.
  location: local
- id: A-003
  name: pxfquery_development_handoff
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-006
  origin: T-007/D-006 — pxfquery_development_phase_handoff_v20260617.md
  registered: '2026-06-24'
  path: 1_asset/pxfquery_development_handoff.md
  symlink: true
  status: ready
  notes: Development boundaries, recommended test cases (EGFR/A549, apoptosis/MYC/A549),
    do-not-do list — informs stress-test scenario constraints and realistic query
    combinations.
  location: local
- id: A-004
  name: pxfquery_module_asset_status_matrix
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-003
  origin: T-007/D-003 — pxfquery_module_asset_status_matrix_v20260617.csv
  registered: '2026-06-24'
  path: 1_asset/pxfquery_module_asset_status_matrix.csv
  symlink: true
  status: ready
  notes: Tabular status of all package modules — helps ensure stress-test categories
    cover all query components (forward, reverse, resolver, index types).
  location: local
- id: A-005
  name: pxfquery_validation_evidence_index
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-004
  origin: T-007/D-004 — pxfquery_validation_evidence_index_v20260617.csv
  registered: '2026-06-24'
  path: 1_asset/pxfquery_validation_evidence_index.csv
  symlink: true
  status: ready
  notes: Indexes existing validation reports — provides data points for actual pass/fail/stress
    patterns observed historically.
  location: local
- id: A-006
  name: forward_matrix_test_report
  type: document
  source: project_asset
  source_task: T-007
  source_artifact_id: M-0257
  origin: T-007 / project asset — M-0257 forward matrix test
  registered: '2026-06-24'
  path: 1_asset/forward_matrix_test_report.md
  symlink: true
  status: ready
  notes: 7/7 deterministic matrix test results covering EXACT, PROXY_PERT, PROXY_CELL,
    PROXY_BOTH search levels — concrete examples of working proxy/exact scenarios.
  location: local
- id: A-007
  name: known_risks_list
  type: document
  source: project_asset
  source_task: T-007
  source_artifact_id: M-0243
  origin: T-007 / project asset — M-0243 known risks
  registered: '2026-06-24'
  path: 1_asset/known_risks_list.md
  symlink: true
  status: ready
  notes: '6 known risk categories: LLM stability (6/9), always_llm latency, mode inconsistency,
    NOT_FOUND+PROXY coexistence — direct input for stress-test boundary scenarios.'
  location: local
- id: A-008
  name: latest_reports_index
  type: document
  source: project_asset
  source_task: T-007
  source_artifact_id: M-0239
  origin: T-007 / project asset — M-0239 latest reports index
  registered: '2026-06-24'
  path: 1_asset/latest_reports_index.md
  symlink: true
  status: ready
  notes: Authority routing for validation report conflicts — helps resolve which historical
    test results to trust when designing scenario expectations.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/2_protocol/2_protocol_split/protocol.md`

```text
# T-056 02_stress_query_scenario_inventory — Protocol

## Objective

Abstract a future stress-test scenario inventory from migrated materials and T-007 digestion results. The inventory must cover: complex queries, strict queries, boundary queries, no-hit (NOT_FOUND) behavior, overly broad results, proxy/exact matching edge cases, and difficult perturbation/cell-line/function combinations. Deliver scenarios and rationale only — not implementation or test execution.

## Position In Project

This is a digestion-phase task under goal_legacy_stress_test_asset_digestion. It precedes any actual stress-test execution tasks. It consumes T-007's development-state understanding to derive what a future stress-test framework must cover, without running tests or building infrastructure.

T-041 (legacy_source_digest_for_m1) is still active; omitted per constraint.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-002 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Forward/reverse query mechanism, resolver modes, index gaps — foundational for scenario categories |
| A-002 | T-007/D-005 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known gaps/risks directly inform stress-test pattern categories |
| A-003 | T-007/D-006 | 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Concrete query examples and do-not-do boundaries |
| A-004 | T-007/D-003 | 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Module coverage verification for scenario completeness |
| A-005 | T-007/D-004 | 4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv | Historical pass/fail patterns as scenario data points |
| A-006 | T-007/M-0257 | reports/validation_reports/M-0257_6_llm_resovler_forward_matrix.md | 7/7 deterministic EXACT/PROXY test cases as scenario templates |
| A-007 | T-007/M-0243 | reports/validation_reports/M-0243_known_risks.md | LLM stability risks, mode inconsistency, NOT_FOUND+PROXY boundaries |
| A-008 | T-007/M-0239 | reports/validation_reports/M-0239_latest_reports_index.md | Authority rules for validation conflict resolution |

## Execution Steps

1. Read all registered input assets (A-001 through A-008) to extract query semantics, resolver behavior, known edge cases, and validation evidence.
2. Derive and categorize stress-test scenarios covering these dimensions:
   - **Complex queries**: multi-gene, multi-drug, combined perturbation+context queries that stress resolver intent parsing and evidence bundling
   - **Strict queries**: exact-match-only cases that should produce EXACT hits; cases where proxy fallback should be explicitly disallowed
   - **Boundary queries**: cell-line not in index, drug not in index, function alias edge cases, empty/partial perturbation strings
   - **No-hit behavior**: queries expected to produce NOT_FOUND — generic drug descriptions (EGFR inhibitor), unknown cell lines, impossible gene+context combinations
   - **Overly broad results**: queries likely to produce many proxy hits or ambiguous evidence bundles (common drugs like DMSO, pan-cancer queries)
   - **Proxy/exact matching**: cases where EXACT vs PROXY_PERT vs PROXY_CELL vs PROXY_BOTH must be explicitly distinguished and the boundary tested
   - **Difficult combos**: perturbation+cell-line+function triples that are biologically questionable, conflict across indexes, or fail in historical reports
   - **LLM mode cross-checks**: scenarios where always_llm vs hybrid_fast vs deterministic produce different results
   - **Missing/partial index**: function_index.json gap scenarios, partial neighbor failures
3. For each scenario, record: unique ID, category, query parameters (forward/reverse, perturbation, context, function intent), expected resolver hit level, expected pass/fail, rationale citing specific source evidence, and notes on historical validation status.
4. Compile the narrative inventory document from step 3 results.
5. Compile the tabular CSV from the same scenario records.
6. Register outputs in 4_artifact/registry.yaml.

## Constraints

- Deliver stress-test scenarios and rationale only. Do not implement test code, run queries, or build test infrastructure.
- Do not reference T-041; it is still active and not available.
- Do not read old legacy root scripts or run them.
- Base all scenario derivation on the 8 registered input assets only.
- Keep scenarios grounded in T-007 evidence (validation reports, gaps, known risks). Do not invent hypothetical scenarios without documented precedent.
- Use the latest-reports-index (A-008) authority rules when historical validation reports conflict.

## Forbidden

- No test execution or query runs.
- No modification of predecessor artifacts or project assets.
- No creation of package code or test scripts.
- No reading of T-041 outputs.
- No web search for external information.

## Web Search Allowance

Allowed: no
Reason: All required information is available in registered T-007 artifacts and project assets.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Stress-test scenario inventory (narrative) | 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md | yes |
| Stress-test scenario table (CSV) | 4_artifact/5_table/stress_query_scenario_table_v20260624.csv | yes |
| Artifact registry update | 4_artifact/registry.yaml | yes |

## Acceptance Criteria

- Inventory covers all 9 scenario dimensions listed in Execution Steps step 2.
- Each scenario has a unique ID, category, query parameters, expected resolver hit level, expected pass/fail, rationale citing specific source evidence.
- CSV table has one row per scenario with columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence.
- Narrative document explains each scenario's motivation and traces back to registered asset evidence.
- No implementation code or test scripts are delivered.
- Outputs are registered in 4_artifact/registry.yaml.

## Failure / Stop Rules

- If any required input asset (A-001 through A-008) is unreadable or corrupted, report and stop.
- If scenario derivation cannot be grounded in registered asset evidence, mark those scenarios as speculative with explicit notes.

## Delivery Requirements

- Register all accepted outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md"
    reason: "Understand forward/reverse query intent, resolver proxy/exact modes, index completeness — foundational for stress-test scenario categories."
  - id: A-002
    source_task: T-007
    source_artifact_id: D-005
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md"
    reason: "Extract stress-test scenario patterns from known gaps: missing function_index, LLM instability, generic drug fallback failures, NOT_FOUND cases."
  - id: A-003
    source_task: T-007
    source_artifact_id: D-006
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md"
    reason: "Provides concrete query examples (EGFR/A549, apoptosis/MYC/A549) and do-not-do boundaries for realistic stress-test scenario design."
  - id: A-004
    source_task: T-007
    source_artifact_id: D-003
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv"
    reason: "Ensure stress-test categories cover all query components: forward, reverse, resolver, index types."
  - id: A-005
    source_task: T-007
    source_artifact_id: D-004
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/5_table/pxfquery_validation_evidence_index_v20260617.csv"
    reason: "Map historical pass/fail patterns into stress-test scenario expectations."
  - id: A-006
    source_task: T-007
    source_artifact_id: M-0257
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/M-0257_6_llm_resovler_forward_matrix.md"
    reason: "7/7 deterministic test cases provide concrete EXACT/PROXY examples as scenario templates."
  - id: A-007
    source_task: T-007
    source_artifact_id: M-0243
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/M-0243_known_risks.md"
    reason: "Direct stress-test category input: LLM stability modes, NOT_FOUND+PROXY boundaries, inconsistent behavior across query modes."
  - id: A-008
    source_task: T-007
    source_artifact_id: M-0239
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/reports/validation_reports/M-0239_latest_reports_index.md"
    reason: "Authority rules for resolving validation report conflicts when assessing expected vs unexpected behavior."
optional: []
forbidden: []
output:
  - path: 4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md
    type: document
  - path: 4_artifact/5_table/stress_query_scenario_table_v20260624.csv
    type: table
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 2_project_asset/

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-056 02_stress_query_scenario_inventory

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories, `2_project_asset/` (read-only via symlinks), non-modifiable per asset_rule.yaml
- Required registry: `4_artifact/registry.yaml` — currently empty, must be updated after deliverables
- Must stop if: any step attempts to run test code, execute queries, modify predecessor assets, or read T-041 outputs

## Objective Restatement
Derive a categorized stress-test scenario inventory (narrative + CSV) from 8 registered T-007 assets. Cover 9 scenario dimensions: complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index. Deliver rationale only — no implementation, no test execution, no legacy root reads.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/pxfquery_development_state_report.md` | Forward/reverse query mechanism, resolver modes, index gaps — foundational for scenario categories | ok |
| A-002 | `1_asset/pxfquery_gap_and_risk_list.md` | Known gaps/risks directly inform stress-test pattern categories | ok |
| A-003 | `1_asset/pxfquery_development_handoff.md` | Concrete query examples (EGFR/A549, apoptosis/MYC/A549) and do-not-do boundaries | ok |
| A-004 | `1_asset/pxfquery_module_asset_status_matrix.csv` | Module coverage verification for scenario completeness | ok |
| A-005 | `1_asset/pxfquery_validation_evidence_index.csv` | Historical pass/fail patterns as scenario data points | ok |
| A-006 | `1_asset/forward_matrix_test_report.md` | 7/7 deterministic EXACT/PROXY test cases as scenario templates | ok |
| A-007 | `1_asset/known_risks_list.md` | LLM stability risks, mode inconsistency, NOT_FOUND+PROXY boundaries | ok |
| A-008 | `1_asset/latest_reports_index.md` | Authority rules for validation conflict resolution | ok |

## Execution Strategy
1. Read all 8 registered input assets (A-001 through A-008) — extract query semantics, resolver modes, known edge cases, historical validation evidence.
2. Derive and categorize stress-test scenarios across all 9 dimensions listed in protocol step 2.
3. For each scenario, record: unique ID, category, query parameters (forward/reverse, perturbation, context, function intent), expected resolver hit level, expected pass/fail, rationale citing specific source evidence, source reference.
4. Compile narrative inventory document (`4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md`) — explain each scenario's motivation with evidence traceback.
5. Compile tabular CSV (`4_artifact/5_table/stress_query_scenario_table_v20260624.csv`) — one row per scenario with all columns.
6. Update `4_artifact/registry.yaml` with both output artifacts.
7. (Optional) Write execution summary to `5_report/completion.md`.

## Conservative Execution Advice
- Start with: Read A-001 (development state report) to understand query model, then read A-007 (known risks) for concrete edge cases — these two provide the widest coverage.
- Smoke/demo method: After reading 2-3 assets, draft 5 representative scenarios covering 5 different categories to confirm the derivation pattern works before scaling to full set.
- Full run only after: the 5-scenario smoke draft is coherent and correctly cites sources.
- Cost/time risk: Low — all processing is local file reading and document writing. No API calls, no test execution. Estimated 1-2 hours for thorough coverage.
- Checkpoint advice: After step 2 (scenario derivation), commit a draft scenario list to `3_execution/scenario_draft.yaml` before writing final documents.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Scenario inventory (narrative) | `4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md` | Covers all 9 dimensions; each scenario has ID, category, params, expected hit level, expected result, rationale, source evidence |
| Scenario table (CSV) | `4_artifact/5_table/stress_query_scenario_table_v20260624.csv` | One row per scenario with 10+ columns; parseable by standard CSV tools |
| Artifact registry update | `4_artifact/registry.yaml` | Both outputs registered with correct source_task=T-056, type, path, status=active |

## Failure / Stop Conditions
- Any registered asset is found empty, truncated, or corrupt during read → stop, document in `5_report/blocked.md`
- Scenario derivation requires information not in the 8 registered assets → stop, do not invent hypotheticals without documented precedent per protocol constraint
- Any step begins to write test code, execute queries, or build infrastructure → stop immediately — this is explicitly forbidden
- T-041 outputs are referenced or read → stop — T-041 is active and omitted by constraint
- LLM stability issues cause repeated contradictory scenario classifications → checkpoint and flag for human review

## Notes For Delivery QA
- Verify CSV columns match: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence
- Verify narrative document includes at least one scenario per dimension (9 total minimum)
- Verify no test code, no query execution results, no legacy root paths appear in deliverables
- Verify artifact registry entries point to the correct absolute paths within this task's `4_artifact/`
- Date in filenames should match execution date (YYYYMMDD format)

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/registry.yaml`

```text
artifacts:
  - id: D-001
    name: stress_query_scenario_inventory
    type: document
    description: "Narrative inventory of 29 stress-test scenarios across 9 dimensions, grounded in T-007 digestion evidence"
    task_id: T-056
    source: task_output
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md"
    status: active
    created: "2026-06-24"
    notes: "Covers complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, difficult combos, LLM mode cross-checks, missing/partial index"

  - id: D-002
    name: stress_query_scenario_table
    type: table
    description: "Tabular CSV of 29 stress-test scenarios with columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence"
    task_id: T-056
    source: task_output
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/5_table/stress_query_scenario_table_v20260624.csv"
    status: active
    created: "2026-06-24"
    notes: "One row per scenario; parseable by standard CSV tools"

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/5_report/completion.md`

```text
# Completion

Task: T-056 02_stress_query_scenario_inventory
Generated: 2026-06-24
Agent: opencode (AGT-002)

## Summary

Executed the task protocol successfully. Delivered 29 stress-test scenarios derived from 8 registered T-007 input assets (A-001 through A-008).

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Narrative inventory | `4_artifact/2_persist/stress_query_scenario_inventory_v20260624.md` | delivered |
| Tabular CSV | `4_artifact/5_table/stress_query_scenario_table_v20260624.csv` | delivered |
| Artifact registry | `4_artifact/registry.yaml` | updated |

## Coverage

All 9 scenario dimensions covered with at least 2 scenarios each (29 total):

| Dimension | Scenario IDs | Count |
|---|---|---|
| Complex queries | SC-001, SC-002, SC-003 | 3 |
| Strict queries | SC-004, SC-005, SC-006 | 3 |
| Boundary queries | SC-007, SC-008, SC-009, SC-010 | 4 |
| No-hit behavior | SC-011, SC-012, SC-013 | 3 |
| Overly broad results | SC-014, SC-015, SC-016 | 3 |
| Proxy/exact matching | SC-017, SC-018, SC-019, SC-020 | 4 |
| Difficult combos | SC-021, SC-022, SC-023 | 3 |
| LLM mode cross-checks | SC-024, SC-025, SC-026 | 3 |
| Missing/partial index | SC-027, SC-028, SC-029 | 3 |

## Acceptance Criteria Verification

- [x] Covers all 9 scenario dimensions
- [x] Each scenario has unique ID, category, query parameters, expected hit level, expected result, rationale citing source evidence
- [x] CSV columns: ID, category, query_type, perturbation, context, function_intent, expected_hit_level, expected_result, rationale, source_evidence
- [x] Narrative explains each scenario's motivation with evidence traceback
- [x] No implementation code, test scripts, or query execution results delivered
- [x] Outputs registered in `4_artifact/registry.yaml`

## Constraints Observed

- No test execution or query runs performed
- No modification of predecessor artifacts or project assets
- No package code or test scripts created
- No T-041 outputs read or referenced
- All scenario derivation grounded in registered T-007 evidence (A-001 through A-008)
- Used latest-reports-index authority rules (A-008) when applicable

## Notes

- 4 scenarios marked as speculative or borderline (SC-014, SC-015, SC-016, SC-029) where the evidence supports the category but exact behavior cannot be predicted from T-007 reports alone
- 2 scenarios (SC-011, SC-012) flagged as mode-dependent with expected_result=PASS or FAIL to document known inconsistency
- 1 scenario (SC-009, empty perturbation) has no direct T-007 precedent but is derived from documented gaps (A-002 §1-4, unverified runnable state)

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-056 | Name: 02_stress_query_scenario_inventory
- Objective: Abstract a future stress-test scenario inventory from migrated materials and existing digestion results, focusing on complex queries, strict queries, boundary queries, no-hit behavior, overly broad results, proxy/exact matching, and difficult perturbation/cell-line/function combinations.

Deliverables: 4_artifact/2_persist/stress_query_scenario_inventory_vYYYYMMDD.md and 4_artifact/5_table/stress_query_scenario_table_vYYYYMMDD.csv.

Reference T-007 because it explains forward/reverse query intent, resolver/index status, and current development-state boundaries. Use T-041 only as a may input if it is done; if T-041 is still active or unavailable, omit it completely and proceed from T-007.

Important constraints: deliver stress-test scenarios and rationale only, not implementation; do not run large tests; do not treat old scripts as current acceptance criteria.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_02_stress_query_scenario_inventory`

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
# AI Handoff: T-056 02_stress_query_scenario_inventory

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
# Delivery QA: T-056 02_stress_query_scenario_inventory

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
