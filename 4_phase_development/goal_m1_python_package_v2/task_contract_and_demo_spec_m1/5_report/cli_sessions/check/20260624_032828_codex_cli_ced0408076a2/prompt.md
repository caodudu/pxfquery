# Checking Prompt
Generated: 2026-06-24 03:28

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-042
name: contract_and_demo_spec_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: 'Define the minimal M1 contract for the PxFquery Python package. Use T-007
  for original tool intent and T-013 for MVP gap/function expectations. Deliver a
  compact API and CLI contract plus exact forward and reverse demo cases: input fields,
  output JSON shape, required no-hit/error behavior, and pass/fail criteria. Do not
  implement code, do not rewrite the full product design, and do not reference failed
  T024-T040 assets as authorities.'
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
notes: 'Constraint supplement for config AI: Keep this task small and authoritative.
  Produce the single M1 API/CLI/demo contract that downstream tasks must follow: no
  broad product redesign, no long narrative report, no implementation code. Use only
  T-007 and T-013 as authoritative inputs. Do not treat T024-T040 as usable assets.
  Acceptance must include exact forward/reverse demo inputs, expected output JSON
  shape, no-hit/error behavior, and pass/fail criteria.'
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T03:28:28'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/1_asset/registration.yaml`

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
  notes: Anchor source authority, package identity, and safe carry-forward boundaries.
  location: local
- id: A-002
  name: t007_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002
  registered: '2026-06-24'
  path: 1_asset/t007_development_state_report.md
  symlink: true
  status: ready
  notes: Keep the M1 contract aligned with actual PxFquery tool intent and known component
    readiness.
  location: local
- id: A-003
  name: t007_development_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005
  registered: '2026-06-24'
  path: 1_asset/t007_development_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: Optional cross-check for unsafe claims, scope boundaries, and no-hit/error
    behavior.
  location: local
- id: A-004
  name: t013_mvp_capability_contract
  type: document
  source: predecessor
  source_task: T-013
  source_artifact_id: D-001
  origin: T-013/D-001
  registered: '2026-06-24'
  path: 1_asset/t013_mvp_capability_contract.md
  symlink: true
  status: ready
  notes: Primary authority for M1 required capabilities, scope limits, and prohibited
    claims.
  location: local
- id: A-005
  name: t013_failure_missing_capability_list
  type: document
  source: predecessor
  source_task: T-013
  source_artifact_id: D-005
  origin: T-013/D-005
  registered: '2026-06-24'
  path: 1_asset/t013_failure_missing_capability_list.md
  symlink: true
  status: ready
  notes: Define negative cases and capabilities M1 must not claim.
  location: local
- id: A-006
  name: t013_capability_status_matrix
  type: table
  source: predecessor
  source_task: T-013
  source_artifact_id: D-003
  origin: T-013/D-003
  registered: '2026-06-24'
  path: 1_asset/t013_capability_status_matrix.csv
  symlink: true
  status: ready
  notes: Optional tabular cross-check for pass/fail criteria.
  location: local
- id: A-007
  name: t013_run_evidence_bundle
  type: other
  source: predecessor
  source_task: T-013
  source_artifact_id: D-004
  origin: T-013/D-004
  registered: '2026-06-24'
  path: 1_asset/t013_run_evidence_bundle
  symlink: true
  status: ready
  notes: Optional evidence-shape reference for prior forward, reverse, and no-hit
    examples; not current M1 output.
  location: local

```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-042 contract_and_demo_spec_m1 — Protocol

## Objective

Define the single minimal M1 contract for the PxFquery Python package. The execution task must produce a compact API contract, CLI contract, forward demo case, reverse demo case, output JSON schema, no-hit/error behavior, and pass/fail criteria for downstream M1 implementation tasks.

This is a specification task only. It must not implement package code, run package tests, rebuild indexes, analyze raw data, or rewrite the full product design.

## Position In Project

T-042 sits at the start of `goal_m1_python_package_v2`. It translates the authoritative T-007 development-state digestion and T-013 MVP run-through review into a small M1 contract that later implementation and validation tasks can follow without inventing names, argument shapes, output schemas, demo inputs, or acceptance rules.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-001 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Anchor source authority, package identity, and safe carry-forward boundaries. |
| A-002 | T-007/D-002 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Keep the M1 contract faithful to the actual PxFquery tool and known component readiness. |
| A-003 | T-007/D-005 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Cross-check unsafe claims, scope boundaries, and no-hit/error behavior. |
| A-004 | T-013/D-001 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Primary authority for M1 required capabilities, gate capabilities, out-of-scope items, and prohibited claims. |
| A-005 | T-013/D-005 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Define negative cases and capabilities M1 must not claim. |
| A-006 | T-013/D-003 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Optional compact cross-check for pass/fail criteria. |
| A-007 | T-013/D-004 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/6_archive/pxfquery_t013_run_evidence_bundle_v20260618/` | Optional evidence-shape reference for prior forward, reverse, and no-hit examples; do not treat as current implementation output. |

## Execution Steps

1. Read A-001, A-002, A-004, and A-005 first; use A-003, A-006, and A-007 only as targeted cross-checks.
2. Extract only M1-relevant facts: package purpose, `(B, P, F)` model, forward query intent, reverse query intent, biological context fields, deterministic evidence boundaries, known missing capabilities, and unsafe claims to avoid.
3. Define a compact Python API contract with exact function names, required parameters, optional parameters, return JSON-like structures, and error/no-hit structures.
4. Define a compact CLI contract with exact command names, required flags, demo commands, output mode, exit behavior, and nonzero/error behavior.
5. Define exactly one forward demo case and exactly one reverse demo case. Each case must include exact input fields, expected output JSON shape, minimum required semantic content, and pass/fail assertions.
6. Define no-hit, ambiguous input, missing index, missing resource, unsupported query, and low-confidence behavior as deterministic contract-level outputs rather than uncaught crashes.
7. Write only the expected contract deliverables under `4_artifact/`, register them in `4_artifact/registry.yaml`, and summarize completion in `5_report/completion.md`.

## Constraints

- Do not implement code, run package tests, rebuild indexes, analyze raw matrices, or create package release artifacts.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not read the historical source root directly.
- Do not use T024-T040 outputs as authoritative inputs.
- Keep the contract small, deterministic, and directly actionable for T048, T049, and T052.
- M1 acceptance must not depend on LLM resolver success.
- Any uncertain biological or data-specific detail must be expressed as a validation requirement for later M1 implementation or validation tasks, not guessed here.

## Forbidden

- Reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Reading `/Users/dudu/Documents/3_Project/8_functional_query`.
- Reading or citing failed/polluted T024-T040 task outputs as authorities.
- Expanding the task into full product design, manuscript strategy, package implementation, or algorithm repair.
- Calling downstream CyHex prompt endpoints from this configuration or execution task.

## Web Search Allowance

Allowed: no

Reason: The M1 contract must be derived from local authoritative predecessor outputs T-007 and T-013. No current external or web evidence is needed to define API, CLI, demo cases, no-hit/error behavior, or pass/fail criteria.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Structured API and CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` | yes |
| Exact forward and reverse demo case

...[truncated by CyHex prompt assembler: 1876 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
    reason: Anchor source authority, package identity, and safe carry-forward boundaries.
  - id: A-002
    source_task: T-007
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: Keep the M1 contract aligned with actual PxFquery tool intent and known component readiness.
  - id: A-004
    source_task: T-013
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md
    reason: Primary authority for M1 required capabilities, scope limits, and prohibited claims.
  - id: A-005
    source_task: T-013
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md
    reason: Define negative cases and capabilities M1 must not claim.
optional:
  - id: A-003
    source_task: T-007
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: Cross-check unsafe claims, scope boundaries, and no-hit/error behavior.
  - id: A-006
    source_task: T-013
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv
    reason: Optional tabular cross-check for pass/fail criteria.
  - id: A-007
    source_task: T-013
    source_artifact_id: D-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/6_archive/pxfquery_t013_run_evidence_bundle_v20260618/
    reason: Optional evidence-shape reference for prior forward, reverse, and no-hit examples.
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
  - path: /Users/dudu/Documents/3_Project/8_functional_query
    reason: Direct legacy-root reads are outside this development contract task.
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
output:
  - path: 4_artifact/2_persist/m1_api_contract.yaml
    type: yaml
    reason: Structured API and CLI contract.
  - path: 4_artifact/2_persist/m1_demo_cases.yaml
    type: yaml
    reason: Exact forward and reverse demo cases with pass/fail assertions.
  - path: 4_artifact/3_document/m1_contract_summary.md
    type: markdown
    reason: Short human-readable contract summary.
  - path: 4_artifact/registry.yaml
    type: yaml
    reason: Registry for accepted/reusable task outputs.
  - path: 5_report/completion.md
    type: markdown
    reason: Completion note and handoff assumptions.
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
  - 2_protocol/2_protocol_split/protocol.md
  - 2_protocol/3_asset_rule/asset_rule.yaml
  - 1_asset/registration.yaml
non_modifiable:
  - /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state
  - /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review

```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task ID: T-042 | Name: contract_and_demo_spec_m1
Status: active | Executor: hybrid
Objective: Define the minimal M1 contract for the PxFquery Python package. Use T-007 for original tool intent and T-013 for MVP gap/function expectations. Deliver a compact API and CLI contract plus exact forward and reverse demo cases: input fields, output JSON shape, required no-hit/error behavior, and pass/fail criteria. Do not implement code, do not rewrite the full product design, and do not reference failed T024-T040 assets as authorities.
Notes / User Natural-Language Intent: Constraint supplement for config AI: Keep this task small and authoritative. Produce the single M1 API/CLI/demo contract that downstream tasks must follow: no broad product redesign, no long narrative report, no implementation code. Use only T-007 and T-013 as authoritative inputs. Do not treat T024-T040 as usable assets. Acceptance must include exact forward/reverse demo inputs, expected output JSON shape, no-hit/error behavior, and pass/fail criteria.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: development
  project_asset_access: forbidden
  zero_assets: false
  total_assets: 7
  symlink_sync:
    checked: 7
    linked: 7
    skipped: 0
    changed: false
  counts:
    ok: 7
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: t007_development_source_map
    required: true
    status: ok
    path: 1_asset/t007_development_source_map.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
    reason: local path exists
  - id: A-002
    name: t007_development_state_report
    required: true
    status: ok
    path: 1_asset/t007_development_state_report.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: local path exists
  - id: A-003
    name: t007_development_gap_and_risk_list
    required: true
    status: ok
    path: 1_asset/t007_development_gap_and_risk_list.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: local path exists
  - id: A-004
    name: t013_mvp_capability_contract
    required: true
    status: ok
    path: 1_asset/t013_mvp_capability_contract.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md
    reason: local path exists
  - id: A-005
    name: t013_failure_missing_capability_list
    required: true
    status: ok
    path: 1_asset/t013_failure_missing_capability_list.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md
    reason: local path exists
  - id: A-006
    name: t013_capability_status_matrix
    required: false
    status: ok
    path: 1_asset/t013_capability_status_matrix.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv
    reason: local path exists
  - id: A-007
    name: t013_run_evidence_bundle
    required: false
    status: ok
    path: 1_asset/t013_run_evidence_bundle
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/6_archive/pxfquery_t013_run_evidence_bundle_v20260618
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-042 contract_and_demo_spec_m1

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md` 是否已写
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
