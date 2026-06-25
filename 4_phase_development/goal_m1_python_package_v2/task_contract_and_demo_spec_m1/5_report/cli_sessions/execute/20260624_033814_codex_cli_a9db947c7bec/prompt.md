# Execution Prompt
Generated: 2026-06-24 03:38

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
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T03:38:14'

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

### Current Task Protocol: protocol.md
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
| Exact forward and reverse demo cases with assertions | `4_artifact/2_persist/m1_demo_cases.yaml` | yes |
| Short human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | yes |
| Artifact registry for accepted outputs | `4_artifact/registry.yaml` | yes |
| Completion note | `5_report/completion.md` | yes |

## Acceptance Criteria

- The API and CLI contracts specify exact names, argument fields, optional fields, output schema, and error/no-hit schema.
- The forward demo case and reverse demo case are concrete, traceable to T-007/T-013 context, and include pass/fail assertions.
- No-hit, ambiguous input, missing index, missing resource, unsupported query, and low-confidence behavior are specified without requiring LLM availability.
- The contract states that deterministic forward and reverse behavior is M1 scope, while natural-language resolver success and broad biological generalization are out of scope unless later validated.
- T024-T040 are excluded as authorities.
- All accepted/reusable outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- Stop if execution cannot define the M1 contract without reading raw project assets or the legacy source root.
- Stop if T-007 and T-013 artifacts are missing or too contradictory to support a deterministic contract.
- Stop if the work would require implementation, package repair, matrix analysis, index rebuilding, or web evidence.
- Stop if demo-case details cannot be made traceable to T-007/T-013 without guessing; record the missing precondition in `5_report/completion.md`.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
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

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-042 contract_and_demo_spec_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`; plus `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`, `1_asset/registration.yaml`
- Forbidden dirs: `2_project_asset/`, `/Users/dudu/Documents/3_Project/8_functional_query`, any T024-T040 path under `goal_package_foundation_v1/`, `goal_resource_index_packs_v1/`, `goal_deterministic_query_engines_v1/`, `goal_resolver_optional_layer_v1/`, `goal_package_milestone_merge_v1/`
- Required registry: `1_asset/registration.yaml` (7 assets, all ok)
- Must stop if: T-007/T-013 artifacts are missing/contradictory for deterministic contract; raw project asset read is needed; work drifts into implementation/matrix analysis/index rebuilding; demo-case details can't be traced to T-007/T-013 without guessing

## Objective Restatement
Produce a compact M1 API/CLI/demo-spec contract from T-007 (development intent/state) and T-013 (MVP capability/limits). Deliver exact function signatures, CLI commands, one forward + one reverse demo case with JSON shapes, no-hit/error behavior, and pass/fail criteria. No code implementation, no product redesign, no T024-T040 references.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t007_development_source_map.md` | Package identity, source priority, carry-forward boundaries | ok |
| A-002 | `1_asset/t007_development_state_report.md` | Component readiness, (B,P,F) model, implemented classes | ok |
| A-003 | `1_asset/t007_development_gap_and_risk_list.md` | Cross-check unsafe claims, scope boundaries (optional) | ok |
| A-004 | `1_asset/t013_mvp_capability_contract.md` | M1 required/gated/forbidden capabilities | ok |
| A-005 | `1_asset/t013_failure_missing_capability_list.md` | Negative cases, known failure modes | ok |
| A-006 | `1_asset/t013_capability_status_matrix.csv` | Tabular pass/fail cross-check (optional) | ok |
| A-007 | `1_asset/t013_run_evidence_bundle` | Prior forward/reverse/no-hit shape reference (optional) | ok |

## Execution Strategy
1. Read A-001, A-002, A-004, A-005 first; then A-003, A-006, A-007 only as cross-checks.
2. Extract M1-relevant facts: package purpose, (B,P,F) model, forward/reverse intent, biological context fields, deterministic evidence boundaries, known missing capabilities, unsafe claims to avoid.
3. Write `4_artifact/2_persist/m1_api_contract.yaml` with function names, parameter schemas, return shapes, error/no-hit output structures.
4. Write CLI contract section in same YAML: commands, flags, demo invocations, exit codes, error behavior.
5. Write `4_artifact/2_persist/m1_demo_cases.yaml` with exactly one forward case and one reverse case: input fields, expected output JSON shape, minimum semantic content, pass/fail assertions.
6. Define no-hit, ambiguous input, missing index, missing resource, unsupported query, low-confidence behavior as deterministic contract-level structures.
7. Write `4_artifact/3_document/m1_contract_summary.md` for human readability.
8. Register all outputs in `4_artifact/registry.yaml`; write `5_report/completion.md`.

## Conservative Execution Advice
- Start with: Read A-001 and A-004 first — they define the package identity anchor and M1 capability boundaries. Draft the (B,P,F) model and forward/reverse intent summary before writing any YAML.
- Smoke/demo command or method: Draft one forward and one reverse output JSON shape from A-002 (core.py function signatures) before finalizing the full contract.
- Full run only after: Primary assets read and M1-relevant facts extracted. Do not write all 5 deliverables before confirming the API shape is traceable to T-007/T-013.
- Cost/time risk: Negligible — spec task with no compute, no network, no LLM calls. Time estimate ~2-4 hours for all 5 deliverables.
- Checkpoint advice: After step 2, verify that the extracted (B,P,F) model and forward/reverse intent are consistent with A-001 §Operational Asset Map and A-004 Required MVP Behavior before writing contract YAML.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Structured API + CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` | Specifies exact function names, args, return JSON shape, error/no-hit shape; CLI has command names, flags, exit codes |
| Forward + reverse demo cases | `4_artifact/2_persist/m1_demo_cases.yaml` | One forward case (B,P → F) and one reverse case (B,F → P); concrete inputs, expected output JSON, pass/fail assertions |
| Human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | Compact summary of API, CLI, demo cases, and contract scope |
| Artifact registry | `4_artifact/registry.yaml` | All accepted/reusable outputs registered with IDs |
| Completion note | `5_report/completion.md` | Summarizes what was delivered, any missing preconditions, and handoff assumptions |

## Failure / Stop Conditions
- Stop if protocol cannot be defined without reading `2_project_asset/` or legacy source root.
- Stop if T-007 and T-013 are too contradictory to produce a deterministic contract (record gap in completion.md).
- Stop if work drifts into package code implementation, matrix analysis, index rebuilding, or T024-T040 citations.
- Stop if demo-case details require guessing biological/input specifics not traceable to T-007/T-013.

## Notes For Delivery QA
- The contract is for downstream M1 implementation tasks (T048, T049, T052). Any uncertain biological detail must be expressed as a validation requirement, not a guess.
- Natural-language resolver success is NOT an acceptance dependency for M1 release (only deterministic forward/reverse + CLI).
- No LLM API calls, web search, or network access needed. All evidence is local.
- Previously repaired config (config_repair_20260624.md). The current protocol, registry, and asset rules are consistent.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/2_protocol/3_asset_rule/asset_rule.yaml

Interpretation:

- `handoff_check_before_exec.md` is the execution strategy and risk guidance.
- `protocol.md` is the task contract.
- If they conflict, stop and write `5_report/blocked.md`. Do not guess.
- `registration.yaml` and `asset_rule.yaml` define the selected inputs. Do not perform a new asset discovery pass.
- `execution_handoff.md`, if present, is only for continuing an interrupted or long-context execution session.

## 2. Task Contract

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task: T-042 contract_and_demo_spec_m1
Status: active | Executor: hybrid
Objective: Define the minimal M1 contract for the PxFquery Python package. Use T-007 for original tool intent and T-013 for MVP gap/function expectations. Deliver a compact API and CLI contract plus exact forward and reverse demo cases: input fields, output JSON shape, required no-hit/error behavior, and pass/fail criteria. Do not implement code, do not rewrite the full product design, and do not reference failed T024-T040 assets as authorities.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
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
| Exact forward and reverse demo cases with assertions | `4_artifact/2_persist/m1_demo_cases.yaml` | yes |
| Short human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | yes |
| Artifact registry for accepted outputs | `4_artifact/registry.yaml` | yes |
| Completion note | `5_report/completion.md` | yes |

## Acceptance Criteria

- The API and CLI contracts specify exact names, argument fields, optional fields, output schema, and error/no-hit schema.
- The forward demo case and reverse demo case are concrete, traceable to T-007/T-013 context, and include pass/fail assertions.
- No-hit, ambiguous input, missing index, missing resource, unsupported query, and low-confidence behavior are specified without requiring LLM availability.
- The contract states that deterministic forward and reverse behavior is M1 scope, while natural-language resolver success and broad biological generalization are out of scope unless later validated.
- T024-T040 are excluded as authorities.
- All accepted/reusable outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- Stop if execution cannot define the M1 contract without reading raw project assets or the legacy source root.
- Stop if T-007 and T-013 artifacts are missing or too contradictory to support a deterministic contract.
- Stop if the work would require implementation, package repair, matrix analysis, index rebuilding, or web evidence.
- Stop if demo-case details cannot be made traceable to T-007/T-013 without guessing; record the missing precondition in `5_report/completion.md`.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (7)
- A-001 [document] t007_development_source_map — path: 1_asset/t007_development_source_map.md — origin: T-007/D-001
- A-002 [document] t007_development_state_report — path: 1_asset/t007_development_state_report.md — origin: T-007/D-002
- A-003 [document] t007_development_gap_and_risk_list — path: 1_asset/t007_development_gap_and_risk_list.md — origin: T-007/D-005
- A-004 [document] t013_mvp_capability_contract — path: 1_asset/t013_mvp_capability_contract.md — origin: T-013/D-001
- A-005 [document] t013_failure_missing_capability_list — path: 1_asset/t013_failure_missing_capability_list.md — origin: T-013/D-005
- A-006 [table] t013_capability_status_matrix — path: 1_asset/t013_capability_status_matrix.csv — origin: T-013/D-003
- A-007 [other] t013_run_evidence_bundle — path: 1_asset/t013_run_evidence_bundle — origin: T-013/D-004

### Asset Rules

### Required
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md — Anchor source authority, package identity, and safe carry-forward boundaries.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md — Keep the M1 contract aligned with actual PxFquery tool intent and known component readiness.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md — Primary authority for M1 required capabilities, scope limits, and prohibited claims.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md — Define negative cases and capabilities M1 must not claim.
### Forbidden
- 2_project_asset/ — forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
- /Users/dudu/Documents/3_Project/8_functional_query — Direct legacy-root reads are outside this development contract task.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_foundation_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_deterministic_query_engines_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resolver_optional_layer_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1 — T024-T040 are a failed/polluted prior route and must not be authoritative inputs.
### Output
- 4_artifact/2_persist/m1_api_contract.yaml — Structured API and CLI contract.
- 4_artifact/2_persist/m1_demo_cases.yaml — Exact forward and reverse demo cases with pass/fail assertions.
- 4_artifact/3_document/m1_contract_summary.md — Short human-readable contract summary.
- 4_artifact/registry.yaml — Registry for accepted/reusable task outputs.
- 5_report/completion.md — Completion note and handoff assumptions.

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

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/5_report/execution_handoff.md`

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
