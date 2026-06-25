# Checking Prompt
Generated: 2026-06-24 04:52

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-048
name: forward_query_core_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Implement the M1 forward query core. Use T-042 for API/demo contract and
  T-046 for all data access through the fixture loader; optionally use T-047 hardening
  and T-041 source digest if available. Deliver forward query code, no-hit behavior
  required by the contract, and in-task demo evidence with structured JSON output.
  Do not write a private ad hoc loader and do not treat mock data as a replacement
  for T-046.
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
notes: 'Constraint supplement for config AI: Implement forward query through the T-046
  loader API only. Do not write an ad hoc data reader or bypass the loader. Follow
  T-042 contract exactly and include no-hit behavior as part of this task''s own acceptance.
  T-047 and T-041 are optional accelerators only. Deliver code plus in-task demo JSON
  evidence; if loader is insufficient, report the precise interface gap rather than
  replacing it.'
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T04:52:01'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: m1_api_contract
  type: table
  source: predecessor
  source_task: T-042
  source_artifact_id: D-001
  origin: T-042/D-001
  registered: '2026-06-24'
  path: 1_asset/m1_api_contract.yaml
  symlink: true
  status: ready
  notes: Authoritative M1 public API, CLI, return-shape, and error/no-hit contract
    for the forward query implementation.
  location: local
- id: A-002
  name: m1_demo_cases
  type: table
  source: predecessor
  source_task: T-042
  source_artifact_id: D-002
  origin: T-042/D-002
  registered: '2026-06-24'
  path: 1_asset/m1_demo_cases.yaml
  symlink: true
  status: ready
  notes: Exact forward demo case and no-hit variants that this task must implement
    and prove with structured JSON evidence.
  location: local
- id: A-003
  name: m1_contract_summary
  type: document
  source: predecessor
  source_task: T-042
  source_artifact_id: D-003
  origin: T-042/D-003
  registered: '2026-06-24'
  path: 1_asset/m1_contract_summary.md
  symlink: true
  status: ready
  notes: Human-readable orientation for the M1 API/CLI/demo scope; secondary to the
    contract YAML files.
  location: local
- id: A-004
  name: m1_fixture_loader_code
  type: code
  source: predecessor
  source_task: T-046
  source_artifact_id: D-001
  origin: T-046/D-001
  registered: '2026-06-24'
  path: 1_asset/m1_fixture_loader_code.py
  symlink: true
  status: ready
  notes: Reusable fixture loader implementation; all T-048 fixture data access must
    go through this loader API.
  location: local
- id: A-005
  name: m1_loader_api_documentation
  type: document
  source: predecessor
  source_task: T-046
  source_artifact_id: D-002
  origin: T-046/D-002
  registered: '2026-06-24'
  path: 1_asset/m1_loader_api_documentation.md
  symlink: true
  status: ready
  notes: Reference for M1FixtureLoader, M1Fixture, and M1Manifest usage during forward
    query implementation.
  location: local
- id: A-006
  name: m1_loader_smoke_evidence
  type: table
  source: predecessor
  source_task: T-046
  source_artifact_id: D-003
  origin: T-046/D-003
  registered: '2026-06-24'
  path: 1_asset/m1_loader_smoke_evidence.csv
  symlink: true
  status: ready
  notes: Optional evidence that the fixture loader had passing structure checks before
    T-048 implementation.
  location: local

```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-048 forward_query_core_m1 — Protocol

## Objective
Implement the M1 forward query core for PxFquery. The implementation must follow the T-042 API/demo contract exactly and must access all M1 fixture data through the T-046 loader API. Deliver reusable forward query code plus in-task structured JSON demo evidence, including the required no-hit behavior.

## Position In Project
T-048 is a development task in `goal_m1_python_package_v2`. It turns the accepted M1 contract from T-042 and the accepted fixture loader from T-046 into the first deterministic forward query implementation. This task is not a full production-data task, not a reverse-query task, and not a resolver/LLM task.

## Inputs
| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Authoritative API, CLI, JSON shape, and no-hit/error contract. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Exact forward demo case and pass/fail assertions, including no-hit variants. |
| A-003 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md` | Secondary human-readable orientation for scope and constraints. |
| A-004 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Loader implementation that must be used for all fixture data access. |
| A-005 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for correct use of `M1FixtureLoader`, `M1Fixture`, and `M1Manifest`. |
| A-006 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Optional evidence that the loader passed fixture structure checks before this task. |

## Execution Steps
1. Read A-001 and A-002 first. Extract only the forward query contract, forward demo case, output JSON shape, pass/fail assertions, and no-hit/error requirements.
2. Read A-005 and inspect A-004 as needed to use the T-046 loader API correctly.
3. Create a task-local implementation of the M1 forward query core under `3_execution/` while developing, then place accepted reusable code under `4_artifact/1_package/`.
4. Implement deterministic forward query behavior for the T-042 forward contract. Data access must call the T-046 loader API; do not parse fixture files directly.
5. Implement required no-hit behavior from T-042 as first-class behavior, not as an afterthought or manual report note.
6. Run an in-task demo/smoke script that exercises the forward demo case and required no-hit case(s), writing structured JSON evidence under `4_artifact/2_persist/`.
7. Compare observed JSON against the T-042 expected shape and assertions. Record pass/fail status in a concise evidence table or JSON summary.
8. Write completion and human-facing report files that state what was implemented, which contract assertions passed, and any unresolved loader/API gaps.

## Constraints
- Follow T-042 exactly for public API names, input fields, output JSON shape, and no-hit/error behavior.
- Use T-046 loader API for all M1 fixture data access.
- Do not write a private ad hoc loader, fixture reader, manifest parser, CSV/TSV reader, or direct matrix/index parser.
- Do not treat mock data as a replacement for the T-046 fixture loader.
- Keep this task scoped to forward query core behavior. Reverse query, LLM interpretation, resolver logic, plotting, and production-scale resource hardening are out of scope.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- If the T-046 loader API is insufficient, document the precise missing interface and stop or degrade only with an explicit compatibility note; do not bypass the loader.

## Forbidden
- Reading or parsing `2_project_asset/`.
- Directly reading fixture package internals or predecessor raw assets instead of using the registered T-046 loader API.
- Using T024-T040 outputs, migrated raw code, or legacy project roots as authority for this task.
- Changing the T-042 contract silently.
- Implementing reverse query, resolver/LLM behavior, or full production-data ranking claims.

## Web Search Allowance
Allowed: no
Reason: This is a local development task fully configured from selected predecessor handoffs and accepted artifacts. No current external evidence is required.

## Deliverables
| Expected output | Target path | Required |
|---|---|---|
| Forward query package code | `4_artifact/1_package/pxfquery/` | yes |
| Demo/smoke script used to generate evidence | `3_execution/` | yes |
| Structured forward demo JSON evidence | `4_artifact/2_persist/forward_query_demo_evidence_v20260624.json` | yes |
| Structured no-hit JSON evidence | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | yes |
| Contract assertion summary | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | yes |
| Human-readable execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Human-readable result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| Completion report | `5_report/completion.md` | yes |
| AI handoff for downstream tasks | `5_report/handoff_ai_use.md` | yes |

## Acceptance Criteria
- Forward query implementation exists as reusable package code in `4_artifact/1_package/`.
- All fixture d

...[truncated by CyHex prompt assembler: 1292 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-042
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml
    reason: Authoritative M1 API, CLI, output JSON, and no-hit/error contract for forward query implementation.
  - id: A-002
    source_task: T-042
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml
    reason: Exact forward demo and no-hit assertions that T-048 must implement and prove.
  - id: A-004
    source_task: T-046
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py
    reason: Loader implementation required for all M1 fixture data access.
  - id: A-005
    source_task: T-046
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md
    reason: Loader API reference required to avoid ad hoc fixture parsing.
optional:
  - id: A-003
    source_task: T-042
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md
    reason: Human-readable orientation for M1 scope; secondary to contract YAML.
  - id: A-006
    source_task: T-046
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
    reason: Loader smoke evidence for context if execution needs to confirm prior loader readiness.
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
  - path: /Users/dudu/Documents/3_Project/8_functional_query/
    reason: legacy source root is not an allowed input for this implementation task
  - path: predecessor raw assets or fixture internals bypassing T-046 loader API
    reason: T-048 must use the registered T-046 loader API, not private parsers or direct data reads
output:
  - path: 4_artifact/1_package/pxfquery/
    type: package_code
  - path: 4_artifact/2_persist/forward_query_demo_evidence_v20260624.json
    type: structured_json
  - path: 4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json
    type: structured_json
  - path: 4_artifact/5_table/forward_query_contract_assertions_v20260624.csv
    type: table
  - path: 4_artifact/3_document/execution_report_v20260624.html
    type: html_report
  - path: 4_artifact/3_document/result_report_v20260624.html
    type: html_report
  - path: 4_artifact/registry.yaml
    type: artifact_registry
  - path: 5_report/completion.md
    type: completion_report
  - path: 5_report/handoff_ai_use.md
    type: downstream_handoff
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 1_project_init/
  - 2_project_asset/

```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task ID: T-048 | Name: forward_query_core_m1
Status: active | Executor: hybrid
Objective: Implement the M1 forward query core. Use T-042 for API/demo contract and T-046 for all data access through the fixture loader; optionally use T-047 hardening and T-041 source digest if available. Deliver forward query code, no-hit behavior required by the contract, and in-task demo evidence with structured JSON output. Do not write a private ad hoc loader and do not treat mock data as a replacement for T-046.
Notes / User Natural-Language Intent: Constraint supplement for config AI: Implement forward query through the T-046 loader API only. Do not write an ad hoc data reader or bypass the loader. Follow T-042 contract exactly and include no-hit behavior as part of this task's own acceptance. T-047 and T-041 are optional accelerators only. Deliver code plus in-task demo JSON evidence; if loader is insufficient, report the precise interface gap rather than replacing it.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: development
  project_asset_access: forbidden
  zero_assets: false
  total_assets: 6
  symlink_sync:
    checked: 6
    linked: 6
    skipped: 0
    changed: false
  counts:
    ok: 6
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: m1_api_contract
    required: true
    status: ok
    path: 1_asset/m1_api_contract.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml
    reason: local path exists
  - id: A-002
    name: m1_demo_cases
    required: true
    status: ok
    path: 1_asset/m1_demo_cases.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml
    reason: local path exists
  - id: A-003
    name: m1_contract_summary
    required: false
    status: ok
    path: 1_asset/m1_contract_summary.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md
    reason: local path exists
  - id: A-004
    name: m1_fixture_loader_code
    required: true
    status: ok
    path: 1_asset/m1_fixture_loader_code.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py
    reason: local path exists
  - id: A-005
    name: m1_loader_api_documentation
    required: true
    status: ok
    path: 1_asset/m1_loader_api_documentation.md
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md
    reason: local path exists
  - id: A-006
    name: m1_loader_smoke_evidence
    required: false
    status: ok
    path: 1_asset/m1_loader_smoke_evidence.csv
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-048 forward_query_core_m1

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_m1/5_report/handoff_check_before_exec.md` 是否已写
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
