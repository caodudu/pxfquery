# Execution Prompt
Generated: 2026-06-24 04:54

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-049
name: reverse_query_core_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Implement the M1 reverse query core. Use T-042 for reverse API/demo contract
  and T-046 for all data access through the fixture loader; optionally use T-047 hardening
  and T-041 source digest if available. Deliver reverse query code, stable ranking/scoring
  behavior required by the contract, and in-task demo evidence with structured JSON
  output. Do not write a private ad hoc loader and do not depend on failed T024-T040
  assets.
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
notes: 'Constraint supplement for config AI: Implement reverse query through the T-046
  loader API only. Do not write an ad hoc data reader or bypass the loader. Follow
  T-042 contract exactly and include ranking/scoring stability as part of this task''s
  own acceptance. T-047 and T-041 are optional accelerators only. Deliver code plus
  in-task demo JSON evidence; if loader/index behavior is insufficient, report the
  precise gap rather than inventing hidden data handling.'
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T04:54:54'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: m1_api_contract
  type: document
  source: predecessor
  source_task: T-042
  source_artifact_id: D-001
  origin: T-042/D-001
  registered: '2026-06-24'
  path: 1_asset/m1_api_contract.yaml
  symlink: true
  status: ready
  notes: Authoritative M1 API/CLI contract, including reverse query function signature,
    JSON shape, error/no-hit behavior, and pass/fail scope.
  location: local
- id: A-002
  name: m1_demo_cases
  type: document
  source: predecessor
  source_task: T-042
  source_artifact_id: D-002
  origin: T-042/D-002
  registered: '2026-06-24'
  path: 1_asset/m1_demo_cases.yaml
  symlink: true
  status: ready
  notes: Exact reverse demo input, expected output fields, ranking/scoring assertions,
    and no-hit variants for implementation evidence.
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
  notes: Human-readable orientation for the M1 contract and scope boundaries.
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
  notes: Required loader implementation. Reverse query data access must go through
    this API rather than private parsing.
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
  notes: API reference for M1FixtureLoader, M1Fixture, and M1Manifest; execution should
    follow these public access methods.
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
  notes: Evidence that the fixture loader exposes expected matrix/index structures;
    useful for diagnosing loader gaps without bypassing it.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-049 reverse_query_core_m1 — Protocol

## Objective

Implement the M1 reverse query core for PxFquery: given functional target intent and biological context, return candidate perturbations using the T-046 fixture loader and the exact T-042 M1 contract. The implementation must provide deterministic ranking/scoring behavior, structured JSON demo evidence, and clear stop reporting if the registered loader/index API cannot support a required contract behavior.

## Position In Project

This is a development task under `goal_m1_python_package_v2`. It follows the M1 contract/demo specification from T-042 and the fixture loader from T-046. It must produce reverse-query implementation evidence only; it must not broaden the product design, inspect raw legacy assets, or build a private data loading path.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 reverse API/CLI contract, JSON shape, errors, no-hit behavior, and scope. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Exact reverse demo case and pass/fail assertions for ranking/scoring evidence. |
| A-003 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md` | Optional orientation for contract boundaries and M1 scope. |
| A-004 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Required loader implementation; all reverse query data access must go through this API. |
| A-005 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for stable public methods and returned structures. |
| A-006 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Optional evidence for expected fixture structures when diagnosing assumptions. |

## Execution Steps

1. Read the registered T-042 contract and demo cases, then extract the reverse query function signature, accepted input fields, output JSON shape, no-hit/error objects, and required pass/fail assertions.
2. Read the T-046 loader API documentation and reusable loader code. Use the loader as the only access path to fixture matrices, indexes, and metadata.
3. Implement the reverse query core in task-local package code, preserving M1 contract names and return fields. Keep the method deterministic and fixture-focused.
4. Define a stable ranking/scoring procedure that can be reproduced from loaded fixture data. Record tie-breaking rules explicitly in code comments or evidence when needed.
5. Run an in-task reverse demo against the T-042 reverse demo case and emit structured JSON evidence under `4_artifact/2_persist/`.
6. Include no-hit/error behavior evidence if the T-042 contract requires it for reverse query.
7. If the loader or fixture index cannot support a required contract behavior, stop implementation at the precise gap and document the missing loader/index capability instead of inventing private data handling.

## Constraints

- Use T-042 as the contract authority for public API shape, CLI-facing behavior, JSON output, errors, and no-hit behavior.
- Use T-046 as the only fixture data access authority.
- Do not write a private ad hoc loader, private manifest reader, direct fixture parser, or direct raw asset reader.
- Ranking/scoring must be deterministic for identical inputs and fixture data.
- Keep the implementation M1-sized: reverse query core, contract compatibility, and demo evidence only.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Keep scripts, temporary logs, and exploratory notes in `3_execution/`; accepted reusable code/evidence belongs in `4_artifact/`.

## Forbidden

- Do not read `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Do not read or depend on failed T024-T040 assets.
- Do not read the historical source root `/Users/dudu/Documents/3_Project/8_functional_query`.
- Do not implement LLM resolver behavior, fuzzy biological interpretation, production resource hardening, plotting, or full-resource claims.
- Do not silently change T-042 contract fields or thresholds; document any unavoidable compatibility gap.

## Web Search Allowance

Allowed: no

Reason: This task can be configured from project protocol plus selected predecessor handoffs and accepted artifacts. No current external information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reverse query package code integrated with the M1 package structure | `4_artifact/1_package/` | yes |
| Structured reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | yes |
| Optional reverse no-hit/error evidence JSON if required by T-042 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | conditional |
| Concise execution/result report for human review | `4_artifact/3_document/` | yes |
| Optional ranking/scoring validation table | `4_artifact/5_table/` | optional |
| Artifact registry for accepted outputs | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- Reverse query code follows the T-042 contract for callable/API behavior and JSON output shape.
- All data access for fixture matrices/indexes/metadata goes through the T-046 loader API.
- The T-042 reverse demo case produces structured JSON evidence with required fields populated.
- Ranking and tie-breaking are deterministic and documented well enough for check-stage reproduction.
- Required no-hit/error behavior is implemented or a precise contract/loader gap is reported.
- No project-level raw assets, direct legacy roots, or T024-T040 assets are used.

## Failure / Stop Rules

- Stop and report a configuration or execution gap if the T-046 loader cannot expose data needed for the T-042 reverse contract.
- Stop rather than create hidden parsing logic if fixture data appear unavailable through the loader.
- Stop if satisfying the reverse query contract would require raw `2_project_asset/` data in this non-digestion task.
- Stop if the only available path depends on T024-T040 artifacts.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-042
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml
    reason: Authoritative M1 reverse API, CLI, JSON shape, error/no-hit behavior, and pass/fail scope.
  - id: A-002
    source_task: T-042
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml
    reason: Exact reverse demo case, expected fields, ranking/scoring assertions, and no-hit variants.
  - id: A-004
    source_task: T-046
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py
    reason: Required fixture loader code; all reverse query data access must use this loader API.
  - id: A-005
    source_task: T-046
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md
    reason: Public loader API documentation needed to avoid private ad hoc parsing.
optional:
  - id: A-003
    source_task: T-042
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md
    reason: Human-readable orientation for contract boundaries.
  - id: A-006
    source_task: T-046
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv
    reason: Loader smoke evidence useful for diagnosing fixture shape assumptions.
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
  - path: /Users/dudu/Documents/3_Project/8_functional_query
    reason: direct legacy-root reads are outside this task scope; use registered predecessor outputs only
  - path: T024-T040 predecessor artifacts
    reason: explicitly excluded as failed or non-authoritative inputs for M1 implementation
output:
  - path: 4_artifact/1_package/
    type: package_code
  - path: 4_artifact/2_persist/
    type: structured_json_or_yaml_evidence
  - path: 4_artifact/3_document/
    type: execution_and_result_reports
  - path: 4_artifact/5_table/
    type: optional_validation_tables
  - path: 5_report/completion.md
    type: completion_report
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 1_project_init/
  - 2_project_asset/

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-049 reverse_query_core_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`, `/Users/dudu/Documents/3_Project/8_functional_query`, predecessor task directories, `1_project_init/`
- Required registry: `1_asset/registration.yaml`
- Must stop if: the T-046 loader cannot expose data needed by the T-042 reverse contract; reverse behavior would require raw project assets, direct legacy-root reads, failed T024-T040 artifacts, or private ad hoc parsing.

## Objective Restatement
Implement the M1 reverse query core for PxFquery using the T-042 contract/demo specification and the T-046 fixture loader as the only data access route. The execution must produce deterministic ranking/scoring behavior, task-local package code, structured JSON demo evidence, and a concise result report. If loader or fixture capabilities are insufficient, execution should document the precise contract/loader gap rather than invent hidden data handling.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/m1_api_contract.yaml` | Authoritative M1 reverse API/CLI contract, JSON shape, errors, no-hit behavior, and pass/fail scope. | ok |
| A-002 | `1_asset/m1_demo_cases.yaml` | Exact reverse demo case, expected output fields, ranking/scoring assertions, and no-hit variants. | ok |
| A-003 | `1_asset/m1_contract_summary.md` | Optional orientation for contract boundaries and M1 scope. | ok |
| A-004 | `1_asset/m1_fixture_loader_code.py` | Required fixture loader implementation; all reverse query data access must use this loader API. | ok |
| A-005 | `1_asset/m1_loader_api_documentation.md` | Public loader API documentation for M1FixtureLoader, M1Fixture, and M1Manifest. | ok |
| A-006 | `1_asset/m1_loader_smoke_evidence.csv` | Optional smoke evidence for diagnosing expected fixture structures without bypassing the loader. | ok |

## Execution Strategy
1. Read A-001 and A-002 to extract the exact reverse callable/API signature, required input fields, JSON output shape, no-hit/error behavior, and demo pass/fail assertions; record the extracted contract notes in `3_execution/`.
2. Read A-005 and A-004 to identify public loader methods and returned fixture structures; run a minimal loader smoke check through the documented API and save temporary observations in `3_execution/`.
3. Implement task-local reverse query package code under `4_artifact/1_package/`, importing or vendoring the T-046 loader code as appropriate while preserving loader-only data access.
4. Implement deterministic scoring/ranking from loaded fixture data, including explicit tie-breaking rules based on stable fields such as score, perturbation identifier, or contract-defined ordering.
5. Run the T-042 reverse demo case and write structured JSON evidence to `4_artifact/2_persist/reverse_demo_evidence_v20260624.json`.
6. Run no-hit/error variants if required by A-001/A-002 and write `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` when applicable.
7. Write a concise human-readable execution/result report in `4_artifact/3_document/`, register accepted outputs in `4_artifact/registry.yaml`, and finish with `5_report/completion.md`.

## Conservative Execution Advice
- Start with: contract extraction plus one minimal loader smoke check through documented T-046 API methods.
- Smoke/demo command or method: use `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...` from the task path, with temporary scripts kept under `3_execution/`.
- Full run only after: the loader smoke check confirms fixture matrices/indexes/metadata needed by the reverse contract are reachable without private parsing.
- Cost/time risk: expected to be low; fixture-level execution should be small and offline. No web search, network crawling, raw asset loading, plotting, or full-resource analysis is allowed.
- Checkpoint advice: before writing reusable outputs, checkpoint the extracted contract fields and loader-access assumptions in `3_execution/` so any incompatibility can be reported precisely.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Reverse query package code | `4_artifact/1_package/` | Code exposes reverse behavior matching T-042 and uses T-046 loader-only data access. |
| Reverse demo evidence JSON | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | JSON contains required contract fields and satisfies T-042 demo ranking/scoring assertions. |
| Reverse no-hit/error evidence JSON | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Present when required by T-042; shows required no-hit/error shape. |
| Execution/result report | `4_artifact/3_document/` | Concise report explains implementation, deterministic ranking, demo result, and any limitations. |
| Optional ranking/scoring validation table | `4_artifact/5_table/` | Useful if ranking assertions need tabular reproduction evidence. |
| Artifact registry | `4_artifact/registry.yaml` | Registers all accepted reusable outputs with paths and descriptions. |
| Completion report | `5_report/completion.md` | Summarizes completion status, evidence paths, and any unresolved gap. |

## Failure / Stop Conditions
- Stop if any required contract behavior can only be satisfied by reading `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Stop if implementation would require direct reads from `/Users/dudu/Documents/3_Project/8_functional_query`.
- Stop if the only available implementation path depends on failed T024-T040 assets.
- Stop if T-046 public loader methods do not expose the matrix, index, or metadata fields required by T-042.
- Stop if ranking/scoring would require guessing undocumented thresholds or silently changing T-042 fields.
- Stop if a private manifest reader, direct fixture parser, or other ad hoc data loader seems necessary.

## Notes For Delivery QA
- Verify the delivered code imports and runs from the task-local package path under the `pxfquery` conda environment.
- Confirm no accepted reusable output remains only in `3_execution/`.
- Confirm `4_artifact/registry.yaml` exists and names every accepted code/evidence/report artifact.
- Confirm demo JSON is structured, deterministic, and contract-shaped rather than only a prose log.
- Confirm completion reporting distinguishes successful implementation from any precise loader/contract gap.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-049 reverse_query_core_m1
Status: active | Executor: hybrid
Objective: Implement the M1 reverse query core. Use T-042 for reverse API/demo contract and T-046 for all data access through the fixture loader; optionally use T-047 hardening and T-041 source digest if available. Deliver reverse query code, stable ranking/scoring behavior required by the contract, and in-task demo evidence with structured JSON output. Do not write a private ad hoc loader and do not depend on failed T024-T040 assets.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-049 reverse_query_core_m1 — Protocol

## Objective

Implement the M1 reverse query core for PxFquery: given functional target intent and biological context, return candidate perturbations using the T-046 fixture loader and the exact T-042 M1 contract. The implementation must provide deterministic ranking/scoring behavior, structured JSON demo evidence, and clear stop reporting if the registered loader/index API cannot support a required contract behavior.

## Position In Project

This is a development task under `goal_m1_python_package_v2`. It follows the M1 contract/demo specification from T-042 and the fixture loader from T-046. It must produce reverse-query implementation evidence only; it must not broaden the product design, inspect raw legacy assets, or build a private data loading path.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml` | Authoritative M1 reverse API/CLI contract, JSON shape, errors, no-hit behavior, and scope. |
| A-002 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml` | Exact reverse demo case and pass/fail assertions for ranking/scoring evidence. |
| A-003 | T-042 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/3_document/m1_contract_summary.md` | Optional orientation for contract boundaries and M1 scope. |
| A-004 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py` | Required loader implementation; all reverse query data access must go through this API. |
| A-005 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md` | Loader API reference for stable public methods and returned structures. |
| A-006 | T-046 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Optional evidence for expected fixture structures when diagnosing assumptions. |

## Execution Steps

1. Read the registered T-042 contract and demo cases, then extract the reverse query function signature, accepted input fields, output JSON shape, no-hit/error objects, and required pass/fail assertions.
2. Read the T-046 loader API documentation and reusable loader code. Use the loader as the only access path to fixture matrices, indexes, and metadata.
3. Implement the reverse query core in task-local package code, preserving M1 contract names and return fields. Keep the method deterministic and fixture-focused.
4. Define a stable ranking/scoring procedure that can be reproduced from loaded fixture data. Record tie-breaking rules explicitly in code comments or evidence when needed.
5. Run an in-task reverse demo against the T-042 reverse demo case and emit structured JSON evidence under `4_artifact/2_persist/`.
6. Include no-hit/error behavior evidence if the T-042 contract requires it for reverse query.
7. If the loader or fixture index cannot support a required contract behavior, stop implementation at the precise gap and document the missing loader/index capability instead of inventing private data handling.

## Constraints

- Use T-042 as the contract authority for public API shape, CLI-facing behavior, JSON output, errors, and no-hit behavior.
- Use T-046 as the only fixture data access authority.
- Do not write a private ad hoc loader, private manifest reader, direct fixture parser, or direct raw asset reader.
- Ranking/scoring must be deterministic for identical inputs and fixture data.
- Keep the implementation M1-sized: reverse query core, contract compatibility, and demo evidence only.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Keep scripts, temporary logs, and exploratory notes in `3_execution/`; accepted reusable code/evidence belongs in `4_artifact/`.

## Forbidden

- Do not read `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset`.
- Do not read or depend on failed T024-T040 assets.
- Do not read the historical source root `/Users/dudu/Documents/3_Project/8_functional_query`.
- Do not implement LLM resolver behavior, fuzzy biological interpretation, production resource hardening, plotting, or full-resource claims.
- Do not silently change T-042 contract fields or thresholds; document any unavoidable compatibility gap.

## Web Search Allowance

Allowed: no

Reason: This task can be configured from project protocol plus selected predecessor handoffs and accepted artifacts. No current external information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reverse query package code integrated with the M1 package structure | `4_artifact/1_package/` | yes |
| Structured reverse demo JSON evidence | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | yes |
| Optional reverse no-hit/error evidence JSON if required by T-042 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | conditional |
| Concise execution/result report for human review | `4_artifact/3_document/` | yes |
| Optional ranking/scoring validation table | `4_artifact/5_table/` | optional |
| Artifact registry for accepted outputs | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- Reverse query code follows the T-042 contract for callable/API behavior and JSON output shape.
- All data access for fixture matrices/indexes/metadata goes through the T-046 loader API.
- The T-042 reverse demo case produces structured JSON evidence with required fields populated.
- Ranking and tie-breaking are deterministic and documented well enough for check-stage reproduction.
- Required no-hit/error behavior is implemented or a precise contract/loader gap is reported.
- No project-level raw assets, direct legacy roots, or T024-T040 assets are used.

## Failure / Stop Rules

- Stop and report a configuration or execution gap if the T-046 loader cannot expose data needed for the T-042 reverse contract.
- Stop rather than create hidden parsing logic if fixture data appear unavailable through the loader.
- Stop if satisfying the reverse query contract would require raw `2_project_asset/` data in this non-digestion task.
- Stop if the only available path depends on T024-T040 artifacts.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (6)
- A-001 [document] m1_api_contract — path: 1_asset/m1_api_contract.yaml — origin: T-042/D-001
- A-002 [document] m1_demo_cases — path: 1_asset/m1_demo_cases.yaml — origin: T-042/D-002
- A-003 [document] m1_contract_summary — path: 1_asset/m1_contract_summary.md — origin: T-042/D-003
- A-004 [code] m1_fixture_loader_code — path: 1_asset/m1_fixture_loader_code.py — origin: T-046/D-001
- A-005 [document] m1_loader_api_documentation — path: 1_asset/m1_loader_api_documentation.md — origin: T-046/D-002
- A-006 [table] m1_loader_smoke_evidence — path: 1_asset/m1_loader_smoke_evidence.csv — origin: T-046/D-003

### Asset Rules

### Required
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_api_contract.yaml — Authoritative M1 reverse API, CLI, JSON shape, error/no-hit behavior, and pass/fail scope.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1/4_artifact/2_persist/m1_demo_cases.yaml — Exact reverse demo case, expected fields, ranking/scoring assertions, and no-hit variants.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/1_package/pxfquery/data/m1_loader.py — Required fixture loader code; all reverse query data access must use this loader API.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_fixture_loader/4_artifact/2_persist/API_REFERENCE_v20260624.md — Public loader API documentation needed to avoid private ad hoc parsing.
### Forbidden
- 2_project_asset/ — forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
- /Users/dudu/Documents/3_Project/8_functional_query — direct legacy-root reads are outside this task scope; use registered predecessor outputs only
- T024-T040 predecessor artifacts — explicitly excluded as failed or non-authoritative inputs for M1 implementation
### Output
- 4_artifact/1_package/
- 4_artifact/2_persist/
- 4_artifact/3_document/
- 4_artifact/5_table/
- 5_report/completion.md

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

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_m1_python_package_v2/task_reverse_query_core_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_m1/5_report/execution_handoff.md`

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
