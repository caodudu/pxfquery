# Execution Prompt
Generated: 2026-06-24 06:11

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-053
name: m1_python_package_milestone
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Deliver the M1 PxFquery Python package milestone. Use T-050 forward validation,
  T-051 reverse validation, and T-052 package assembly as the three hard evidence
  gates. Deliver the final package location/version, demo commands, validation evidence
  index, layered asset map, and known gap report. Do not fix lower-layer implementation
  here; if evidence is missing, report the precise failed layer and recommend same-layer
  repair tasks.
executor: hybrid
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
notes: 'Constraint supplement for config AI: This is a milestone aggregation task,
  not a repair or implementation task. Hard acceptance is exactly three evidence streams:
  T-050 forward validation, T-051 reverse validation, and T-052 package assembly.
  Deliver final package path/version, demo commands, evidence index, layered asset
  map, and known gaps. If evidence is missing, identify the failed layer and recommend
  same-layer repair tasks; do not modify lower-layer assets or mark optional gaps
  as done.'
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T06:11:17'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: forward_validation_results_table
  type: table
  source: predecessor
  source_task: T-050
  source_artifact_id: D-004
  origin: T-050 forward_validation_m1 / D-004
  registered: '2026-06-24'
  path: 1_asset/forward_validation_results_table.csv
  symlink: true
  status: ready
  notes: 11-check pass/fail table for forward validation; all PASS
  location: local
- id: A-002
  name: forward_validation_report
  type: document
  source: predecessor
  source_task: T-050
  source_artifact_id: D-005
  origin: T-050 forward_validation_m1 / D-005
  registered: '2026-06-24'
  path: 1_asset/forward_validation_report.md
  symlink: true
  status: ready
  notes: Full forward validation narrative with traceability to T-059, M1FixtureLoader,
    synthetic_repair
  location: local
- id: A-003
  name: reverse_validation_report_json
  type: data
  source: predecessor
  source_task: T-051
  source_artifact_id: D-001
  origin: T-051 reverse_validation_m1 / D-001
  registered: '2026-06-24'
  path: 1_asset/reverse_validation_report_json.json
  symlink: true
  status: ready
  notes: 42-check structured validation report with explicit PASS verdict
  location: local
- id: A-004
  name: reverse_validation_comparison_csv
  type: table
  source: predecessor
  source_task: T-051
  source_artifact_id: D-002
  origin: T-051 reverse_validation_m1 / D-002
  registered: '2026-06-24'
  path: 1_asset/reverse_validation_comparison_csv.csv
  symlink: true
  status: ready
  notes: Per-check pass/fail table for all 42 reverse validation checks
  location: local
- id: A-005
  name: reverse_validation_html_report
  type: document
  source: predecessor
  source_task: T-051
  source_artifact_id: D-003
  origin: T-051 reverse_validation_m1 / D-003
  registered: '2026-06-24'
  path: 1_asset/reverse_validation_html_report.html
  symlink: true
  status: ready
  notes: Rendered HTML summary of reverse validation with provenance and verdict
  location: local
- id: A-006
  name: assembled_package_source
  type: code
  source: predecessor
  source_task: T-052
  source_artifact_id: D-001
  origin: T-052 package_assembly_m1 / D-001
  registered: '2026-06-24'
  path: 1_asset/assembled_package_source
  symlink: true
  status: ready
  notes: Assembled M1 pxfquery package v0.1.0 — src/ layout, pyproject.toml, CLI wiring
  location: local
- id: A-007
  name: import_smoke_evidence
  type: document
  source: predecessor
  source_task: T-052
  source_artifact_id: D-002
  origin: T-052 package_assembly_m1 / D-002
  registered: '2026-06-24'
  path: 1_asset/import_smoke_evidence.txt
  symlink: true
  status: ready
  notes: pip install, import pxfquery, version 0.1.0, CLI --help, info command
  location: local
- id: A-008
  name: forward_demo_json
  type: data
  source: predecessor
  source_task: T-052
  source_artifact_id: D-003
  origin: T-052 package_assembly_m1 / D-003
  registered: '2026-06-24'
  path: 1_asset/forward_demo_json.json
  symlink: true
  status: ready
  notes: Forward demo — EGFR/A549/xpr, found:true, top_activated, top_suppressed
  location: local
- id: A-009
  name: reverse_demo_json
  type: data
  source: predecessor
  source_task: T-052
  source_artifact_id: D-004
  origin: T-052 package_assembly_m1 / D-004
  registered: '2026-06-24'
  path: 1_asset/reverse_demo_json.json
  symlink: true
  status: ready
  notes: Reverse demo — HALLMARK_APOPTOSIS activate / HALLMARK_MYC_TARGETS_V1 suppress
    / A549, found:true
  location: local
- id: A-010
  name: cli_help_text
  type: document
  source: predecessor
  source_task: T-052
  source_artifact_id: D-005
  origin: T-052 package_assembly_m1 / D-005
  registered: '2026-06-24'
  path: 1_asset/cli_help_text.txt
  symlink: true
  status: ready
  notes: CLI help for pxfquery, forward, reverse, and info subcommands
  location: local
- id: A-011
  name: package_assembly_execution_report
  type: document
  source: predecessor
  source_task: T-052
  source_artifact_id: D-006
  origin: T-052 package_assembly_m1 / D-006
  registered: '2026-06-24'
  path: 1_asset/package_assembly_execution_report.html
  symlink: true
  status: ready
  notes: Package assembly execution report documenting the assembly process
  location: local
- id: A-012
  name: package_assembly_result_report
  type: document
  source: predecessor
  source_task: T-052
  source_artifact_id: D-007
  origin: T-052 package_assembly_m1 / D-007
  registered: '2026-06-24'
  path: 1_asset/package_assembly_result_report.html
  symlink: true
  status: ready
  notes: Package assembly result report with demo outputs and acceptance criteria
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/2_protocol/2_protocol_split/protocol.md`

```text
# T-053 m1_python_package_milestone — Protocol

## Objective

Aggregate T-050 forward validation, T-051 reverse validation, and T-052 package assembly into a single M1 milestone deliverable. Produce a layered asset map, evidence index, demo commands, known gap report, and the final package location/version. Do not repair or reimplement any lower-layer code.

## Position In Project

This is the capstone task under `goal_m1_python_package_v2`. T-050, T-051, and T-052 are all completed with PASS verdicts. This task collects their outputs, indexes them, and presents the milestone as a consumable handoff for downstream delivery/review.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-050 | `task_forward_validation_m1/4_artifact/5_table/forward_validation_results_v20260624.csv` | Primary forward validation evidence (11 checks, all PASS) |
| A-002 | T-050 | `task_forward_validation_m1/4_artifact/3_document/forward_validation_report_v20260624.md` | Full validation narrative for forward query |
| A-003 | T-051 | `task_reverse_validation_m1/4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | Primary reverse validation evidence (42 checks, all PASS) |
| A-004 | T-051 | `task_reverse_validation_m1/4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | Per-check pass/fail table for reverse validation |
| A-005 | T-051 | `task_reverse_validation_m1/4_artifact/3_document/validation_report_v20260624_055812.html` | Human-readable reverse validation HTML report |
| A-006 | T-052 | `task_package_assembly_m1/4_artifact/1_package/` | Assembled M1 pxfquery package source (v0.1.0) |
| A-007 | T-052 | `task_package_assembly_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Import smoke test evidence |
| A-008 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/forward_demo_v20260624.json` | Forward demo JSON (EGFR/A549/xpr, found:true) |
| A-009 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/reverse_demo_v20260624.json` | Reverse demo JSON (MYC_TARGETS_V1/A549, found:true) |
| A-010 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/cli_help_v20260624.txt` | CLI help text capture |
| A-011 | T-052 | `task_package_assembly_m1/4_artifact/3_document/execution_report_v20260624.html` | Package assembly execution report |
| A-012 | T-052 | `task_package_assembly_m1/4_artifact/3_document/result_report_v20260624.html` | Package assembly result report |

## Execution Steps

1. **Collect & index T-050 forward validation evidence** — Read A-001 and A-002. Record: 11/11 PASS, package v0.1.0, M1FixtureLoader, synthetic_repair manifest.
2. **Collect & index T-051 reverse validation evidence** — Read A-003, A-004, A-005. Record: 42/42 PASS, cosine similarity ranking, top-3 matching reference.
3. **Collect & index T-052 package assembly evidence** — Read A-006 through A-012. Record: pip installable package at source path, version 0.1.0, all 9 acceptance criteria passed, forward/reverse CLI demos working.
4. **Build layered asset map** — Map which predecessor produced which asset, which layer (skeleton → forward implementation → reverse implementation → package assembly → forward validation → reverse validation) each asset belongs to, and which assets are consumed by this milestone.
5. **Write evidence index** — Create a structured index (JSON or Markdown) listing all three evidence streams with verdicts, key metrics, and cross-references.
6. **Record demo commands** — Document working CLI commands for forward query, reverse query, and info subcommand as validated by T-052 and T-050/T-051.
7. **Identify known gaps** — Check for any missing evidence, incomplete coverage, or known limits reported by predecessors. Report precise failed layer if evidence is missing; do not fix.
8. **Write milestone report** — Compile all findings into `5_report/milestone_report_v<timestamp>.md` (or `.html`).
9. **Register deliverables** — Update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not re-run validation or re-assemble the package.
- Do not modify any predecessor task artifact or directory.
- Do not read project-level raw assets under `2_project_asset/`.
- Do not implement, repair, or modify any query logic or package code.
- All information must come from predecessor handoffs and registered artifacts.
- If any required evidence stream is missing, report the failed layer and recommend a same-layer repair task; do not mark gaps as done.

## Forbidden

- Modifying predecessor task files or directories.
- Re-running validation or assembly commands.
- Reading `2_project_asset/` (forbidden for non-digestion task).
- Reading T-024 through T-040 artifacts.
- Creating duplicate or redundant evidence.

## Web Search Allowance

Allowed: no
Reason: All evidence is local from predecessor tasks. No external information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Milestone report | `4_artifact/3_document/milestone_report_v<timestamp>.md` (or .html) | yes |
| Evidence index (structured) | `4_artifact/2_persist/evidence_index_v<timestamp>.json` | yes |
| Layered asset map | `4_artifact/5_table/layered_asset_map_v<timestamp>.csv` (or .md) | yes |
| Known gap report | `4_artifact/5_table/known_gaps_v<timestamp>.md` | yes |
| Demo commands reference | `4_artifact/2_persist/demo_commands_v<timestamp>.md` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- All three evidence streams (T-050, T-051, T-052) are collected and summarized with verdicts.
- Final package location and version (v0.1.0) are documented.
- Layered asset map shows predecessor provenance for each layer.
- Known gaps are explicitly listed, including any predecessor-reported limits.
- Demo commands are verified against T-052 output.
- No predecessor artifacts were modified.
- All deliverables registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- If a predecessor task was not completed successfully (verdict not PASS), report the gap and recommend a same-layer repair. Do not fabricate evidence.
- If any required predecessor artifact path cannot be resolved, report the missing path and recommend investigation in the originating task.
- Do not proceed if the assembled package source (A-006) is missing or non-functional.

## Delivery Requirements

- Register all accepted outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-050
    source_artifact_id: D-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/4_artifact/5_table/forward_validation_results_v20260624.csv
    reason: Primary forward validation evidence — 11-check pass/fail table

  - id: A-002
    source_task: T-050
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/4_artifact/3_document/forward_validation_report_v20260624.md
    reason: Full forward validation narrative and traceability

  - id: A-003
    source_task: T-051
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/2_persist/reverse_validation_report_v20260624_055812.json
    reason: Primary reverse validation evidence — 42-check structured report with PASS verdict

  - id: A-004
    source_task: T-051
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv
    reason: Per-check pass/fail table for reverse validation

  - id: A-005
    source_task: T-051
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/3_document/validation_report_v20260624_055812.html
    reason: Human-readable reverse validation HTML report

  - id: A-006
    source_task: T-052
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/1_package/
    reason: Assembled M1 pxfquery package source (v0.1.0)

  - id: A-007
    source_task: T-052
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt
    reason: Import smoke test evidence — pip install, import, version, CLI

  - id: A-008
    source_task: T-052
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_persist/forward_demo_v20260624.json
    reason: Forward demo JSON — EGFR/A549/xpr, found:true

  - id: A-009
    source_task: T-052
    source_artifact_id: D-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_persist/reverse_demo_v20260624.json
    reason: Reverse demo JSON — MYC_TARGETS_V1/A549, found:true

  - id: A-010
    source_task: T-052
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_persist/cli_help_v20260624.txt
    reason: CLI help text for all subcommands

  - id: A-011
    source_task: T-052
    source_artifact_id: D-006
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/3_document/execution_report_v20260624.html
    reason: Package assembly execution report

  - id: A-012
    source_task: T-052
    source_artifact_id: D-007
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/3_document/result_report_v20260624.html
    reason: Package assembly result report with acceptance criteria

optional: []
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
output:
  - path: 4_artifact/3_document/milestone_report_v<timestamp>.md
    type: document
  - path: 4_artifact/2_persist/evidence_index_v<timestamp>.json
    type: data
  - path: 4_artifact/5_table/layered_asset_map_v<timestamp>.csv
    type: table
  - path: 4_artifact/5_table/known_gaps_v<timestamp>.md
    type: document
  - path: 4_artifact/2_persist/demo_commands_v<timestamp>.md
    type: document
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/
  - /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/
  - /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/
  - /Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-053 m1_python_package_milestone

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, all predecessor task directories (T-050, T-051, T-052)
- Required registry: `1_asset/registration.yaml` (12 assets, all symlinked, all ok)
- Must stop if: any required asset is missing/empty, or predecessor-reported evidence stream fails verdict

## Objective Restatement
Aggregate three completed predecessor evidence streams (T-050 forward validation, T-051 reverse validation, T-052 package assembly) into a single M1 milestone deliverable. Produce: final package path/version, demo commands, evidence index, layered asset map, known gap report. Do not repair or reimplement anything.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/forward_validation_results_table.csv` | 11-check forward pass/fail table | ok |
| A-002 | `1_asset/forward_validation_report.md` | Forward validation narrative | ok |
| A-003 | `1_asset/reverse_validation_report_json.json` | 42-check reverse structured report | ok |
| A-004 | `1_asset/reverse_validation_comparison_csv.csv` | Per-check pass/fail table | ok |
| A-005 | `1_asset/reverse_validation_html_report.html` | Human-readable reverse report | ok |
| A-006 | `1_asset/assembled_package_source` | M1 package source v0.1.0 | ok |
| A-007 | `1_asset/import_smoke_evidence.txt` | pip install + import + CLI evidence | ok |
| A-008 | `1_asset/forward_demo_json.json` | Forward demo output | ok |
| A-009 | `1_asset/reverse_demo_json.json` | Reverse demo output | ok |
| A-010 | `1_asset/cli_help_text.txt` | CLI help capture | ok |
| A-011 | `1_asset/package_assembly_execution_report.html` | Assembly execution report | ok |
| A-012 | `1_asset/package_assembly_result_report.html` | Assembly result with acceptance criteria | ok |

## Execution Strategy
1. **Read evidence trio** — Read A-001/A-002 (forward), A-003/A-004/A-005 (reverse), A-007 (smoke) to confirm all PASS verdicts and extract key metrics.
2. **Read demo and package evidence** — Read A-006 (package source path), A-008/A-009 (demo JSONs), A-010 (CLI help), A-011/A-012 (reports) to capture package location, version, acceptance criteria, and working demo commands.
3. **Build layered asset map** — Create CSV mapping each asset to its predecessor task, layer (skeleton → forward impl → reverse impl → package assembly → forward validation → reverse validation), and milestone consumption role.
4. **Write evidence index** — Produce `evidence_index_v<timestamp>.json` with all three streams, verdicts, metrics, and cross-references.
5. **Write demo commands reference** — Extract working CLI commands from A-008/A-009/A-010 into `demo_commands_v<timestamp>.md`.
6. **Write known gap report** — Scan predecessor outputs for reported limits, incomplete coverage, or missing evidence. List explicitly.
7. **Write milestone report** — Compile into `milestone_report_v<timestamp>.md` with summary, evidence index, asset map, gaps, and demo commands.
8. **Register deliverables** — Update `4_artifact/registry.yaml` with all output artifacts.

## Conservative Execution Advice
- Start with: Read A-001 (forward table), A-003 (reverse JSON), and A-007 (smoke evidence) to confirm all three gates are green before building anything.
- Smoke/demo method: `python -c "import pxfquery; print(pxfquery.__version__)"` at the assembled package source to verify installability (read-only check).
- Full run only after: all three evidence streams confirmed PASS.
- Cost/time risk: negligible — all data is local text/JSON/CSV/HTML. Estimated 10-15 min for reading + writing 6 deliverables.
- Checkpoint advice: After Step 1, if any evidence stream shows FAIL or missing data, stop and switch to gap reporting.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Milestone report | `4_artifact/3_document/milestone_report_v<timestamp>.md` | Contains all three evidence stream summaries, package path, version 0.1.0 |
| Evidence index | `4_artifact/2_persist/evidence_index_v<timestamp>.json` | Structured JSON with verdicts per stream |
| Layered asset map | `4_artifact/5_table/layered_asset_map_v<timestamp>.csv` | CSV with layer, predecessor task, asset ID, description |
| Known gap report | `4_artifact/5_table/known_gaps_v<timestamp>.md` | Lists any predecessor-reported limits or missing coverage |
| Demo commands | `4_artifact/2_persist/demo_commands_v<timestamp>.md` | Working forward/reverse/info CLI commands |
| Completion report | `5_report/completion.md` | Updated to reflect completed status |

## Failure / Stop Conditions
- If any required asset is missing or empty (contradicting preflight), write blocked.md instead.
- If any predecessor evidence stream reports FAIL or INCOMPLETE, document as known gap and do not mark PASS.
- If asset registry.yaml or protocol.md is internally inconsistent and cannot be repaired, write blocked.md.
- Do not proceed to execution if human approval is required after this check.

## Notes For Delivery QA
- This is a pure aggregation task; all evidence must come from predecessor handoffs, not fresh execution.
- Final package location is the symlink at `1_asset/assembled_package_source/` → T-052's `4_artifact/1_package/`.
- Version is v0.1.0 — confirm in smoke evidence and pyproject.toml.
- Known gaps may include: missing edge-case coverage, small test count, or predecessor-reported limitations. These are acceptable if explicitly documented.
- Each output file must include a timestamp in its filename matching the pattern `v<YYYYMMDD_HHMMSS>`.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-053 m1_python_package_milestone
Status: active | Executor: hybrid
Objective: Deliver the M1 PxFquery Python package milestone. Use T-050 forward validation, T-051 reverse validation, and T-052 package assembly as the three hard evidence gates. Deliver the final package location/version, demo commands, validation evidence index, layered asset map, and known gap report. Do not fix lower-layer implementation here; if evidence is missing, report the precise failed layer and recommend same-layer repair tasks.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-053 m1_python_package_milestone — Protocol

## Objective

Aggregate T-050 forward validation, T-051 reverse validation, and T-052 package assembly into a single M1 milestone deliverable. Produce a layered asset map, evidence index, demo commands, known gap report, and the final package location/version. Do not repair or reimplement any lower-layer code.

## Position In Project

This is the capstone task under `goal_m1_python_package_v2`. T-050, T-051, and T-052 are all completed with PASS verdicts. This task collects their outputs, indexes them, and presents the milestone as a consumable handoff for downstream delivery/review.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-050 | `task_forward_validation_m1/4_artifact/5_table/forward_validation_results_v20260624.csv` | Primary forward validation evidence (11 checks, all PASS) |
| A-002 | T-050 | `task_forward_validation_m1/4_artifact/3_document/forward_validation_report_v20260624.md` | Full validation narrative for forward query |
| A-003 | T-051 | `task_reverse_validation_m1/4_artifact/2_persist/reverse_validation_report_v20260624_055812.json` | Primary reverse validation evidence (42 checks, all PASS) |
| A-004 | T-051 | `task_reverse_validation_m1/4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv` | Per-check pass/fail table for reverse validation |
| A-005 | T-051 | `task_reverse_validation_m1/4_artifact/3_document/validation_report_v20260624_055812.html` | Human-readable reverse validation HTML report |
| A-006 | T-052 | `task_package_assembly_m1/4_artifact/1_package/` | Assembled M1 pxfquery package source (v0.1.0) |
| A-007 | T-052 | `task_package_assembly_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt` | Import smoke test evidence |
| A-008 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/forward_demo_v20260624.json` | Forward demo JSON (EGFR/A549/xpr, found:true) |
| A-009 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/reverse_demo_v20260624.json` | Reverse demo JSON (MYC_TARGETS_V1/A549, found:true) |
| A-010 | T-052 | `task_package_assembly_m1/4_artifact/2_persist/cli_help_v20260624.txt` | CLI help text capture |
| A-011 | T-052 | `task_package_assembly_m1/4_artifact/3_document/execution_report_v20260624.html` | Package assembly execution report |
| A-012 | T-052 | `task_package_assembly_m1/4_artifact/3_document/result_report_v20260624.html` | Package assembly result report |

## Execution Steps

1. **Collect & index T-050 forward validation evidence** — Read A-001 and A-002. Record: 11/11 PASS, package v0.1.0, M1FixtureLoader, synthetic_repair manifest.
2. **Collect & index T-051 reverse validation evidence** — Read A-003, A-004, A-005. Record: 42/42 PASS, cosine similarity ranking, top-3 matching reference.
3. **Collect & index T-052 package assembly evidence** — Read A-006 through A-012. Record: pip installable package at source path, version 0.1.0, all 9 acceptance criteria passed, forward/reverse CLI demos working.
4. **Build layered asset map** — Map which predecessor produced which asset, which layer (skeleton → forward implementation → reverse implementation → package assembly → forward validation → reverse validation) each asset belongs to, and which assets are consumed by this milestone.
5. **Write evidence index** — Create a structured index (JSON or Markdown) listing all three evidence streams with verdicts, key metrics, and cross-references.
6. **Record demo commands** — Document working CLI commands for forward query, reverse query, and info subcommand as validated by T-052 and T-050/T-051.
7. **Identify known gaps** — Check for any missing evidence, incomplete coverage, or known limits reported by predecessors. Report precise failed layer if evidence is missing; do not fix.
8. **Write milestone report** — Compile all findings into `5_report/milestone_report_v<timestamp>.md` (or `.html`).
9. **Register deliverables** — Update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not re-run validation or re-assemble the package.
- Do not modify any predecessor task artifact or directory.
- Do not read project-level raw assets under `2_project_asset/`.
- Do not implement, repair, or modify any query logic or package code.
- All information must come from predecessor handoffs and registered artifacts.
- If any required evidence stream is missing, report the failed layer and recommend a same-layer repair task; do not mark gaps as done.

## Forbidden

- Modifying predecessor task files or directories.
- Re-running validation or assembly commands.
- Reading `2_project_asset/` (forbidden for non-digestion task).
- Reading T-024 through T-040 artifacts.
- Creating duplicate or redundant evidence.

## Web Search Allowance

Allowed: no
Reason: All evidence is local from predecessor tasks. No external information is needed.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Milestone report | `4_artifact/3_document/milestone_report_v<timestamp>.md` (or .html) | yes |
| Evidence index (structured) | `4_artifact/2_persist/evidence_index_v<timestamp>.json` | yes |
| Layered asset map | `4_artifact/5_table/layered_asset_map_v<timestamp>.csv` (or .md) | yes |
| Known gap report | `4_artifact/5_table/known_gaps_v<timestamp>.md` | yes |
| Demo commands reference | `4_artifact/2_persist/demo_commands_v<timestamp>.md` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- All three evidence streams (T-050, T-051, T-052) are collected and summarized with verdicts.
- Final package location and version (v0.1.0) are documented.
- Layered asset map shows predecessor provenance for each layer.
- Known gaps are explicitly listed, including any predecessor-reported limits.
- Demo commands are verified against T-052 output.
- No predecessor artifacts were modified.
- All deliverables registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- If a predecessor task was not completed successfully (verdict not PASS), report the gap and recommend a same-layer repair. Do not fabricate evidence.
- If any required predecessor artifact path cannot be resolved, report the missing path and recommend investigation in the originating task.
- Do not proceed if the assembled package source (A-006) is missing or non-functional.

## Delivery Requirements

- Register all accepted outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (12)
- A-001 [table] forward_validation_results_table — path: 1_asset/forward_validation_results_table.csv — origin: T-050 forward_validation_m1 / D-004
- A-002 [document] forward_validation_report — path: 1_asset/forward_validation_report.md — origin: T-050 forward_validation_m1 / D-005
- A-003 [data] reverse_validation_report_json — path: 1_asset/reverse_validation_report_json.json — origin: T-051 reverse_validation_m1 / D-001
- A-004 [table] reverse_validation_comparison_csv — path: 1_asset/reverse_validation_comparison_csv.csv — origin: T-051 reverse_validation_m1 / D-002
- A-005 [document] reverse_validation_html_report — path: 1_asset/reverse_validation_html_report.html — origin: T-051 reverse_validation_m1 / D-003
- A-006 [code] assembled_package_source — path: 1_asset/assembled_package_source — origin: T-052 package_assembly_m1 / D-001
- A-007 [document] import_smoke_evidence — path: 1_asset/import_smoke_evidence.txt — origin: T-052 package_assembly_m1 / D-002
- A-008 [data] forward_demo_json — path: 1_asset/forward_demo_json.json — origin: T-052 package_assembly_m1 / D-003
- A-009 [data] reverse_demo_json — path: 1_asset/reverse_demo_json.json — origin: T-052 package_assembly_m1 / D-004
- A-010 [document] cli_help_text — path: 1_asset/cli_help_text.txt — origin: T-052 package_assembly_m1 / D-005
- A-011 [document] package_assembly_execution_report — path: 1_asset/package_assembly_execution_report.html — origin: T-052 package_assembly_m1 / D-006
- A-012 [document] package_assembly_result_report — path: 1_asset/package_assembly_result_report.html — origin: T-052 package_assembly_m1 / D-007

### Asset Rules

### Required
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/4_artifact/5_table/forward_validation_results_v20260624.csv — Primary forward validation evidence — 11-check pass/fail table
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/4_artifact/3_document/forward_validation_report_v20260624.md — Full forward validation narrative and traceability
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/2_persist/reverse_validation_report_v20260624_055812.json — Primary reverse validation evidence — 42-check structured report with PASS verdict
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/5_table/reverse_validation_comparison_v20260624_055812.csv — Per-check pass/fail table for reverse validation
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/3_document/validation_report_v20260624_055812.html — Human-readable reverse validation HTML report
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/1_package/ — Assembled M1 pxfquery package source (v0.1.0)
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_import_smoke/smoke_test_v20260624.txt — Import smoke test evidence — pip install, import, version, CLI
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_persist/forward_demo_v20260624.json — Forward demo JSON — EGFR/A549/xpr, found:true
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_persist/reverse_demo_v20260624.json — Reverse demo JSON — MYC_TARGETS_V1/A549, found:true
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/2_persist/cli_help_v20260624.txt — CLI help text for all subcommands
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/3_document/execution_report_v20260624.html — Package assembly execution report
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/4_artifact/3_document/result_report_v20260624.html — Package assembly result report with acceptance criteria
### Forbidden
- 2_project_asset/ — forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
### Output
- 4_artifact/3_document/milestone_report_v<timestamp>.md
- 4_artifact/2_persist/evidence_index_v<timestamp>.json
- 4_artifact/5_table/layered_asset_map_v<timestamp>.csv
- 4_artifact/5_table/known_gaps_v<timestamp>.md
- 4_artifact/2_persist/demo_commands_v<timestamp>.md

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

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_m1_python_package_v2/task_m1_python_package_milestone/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_m1_python_package_milestone/5_report/execution_handoff.md`

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
