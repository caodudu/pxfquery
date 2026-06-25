# Delivery QA Prompt
Generated: 2026-06-24 05:54

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-050
name: forward_validation_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Independently validate the M1 forward query implementation. Use T-048 as
  the implementation under test and rerun the forward demo case from the contract.
  Deliver smoke logs, JSON output, pass/fail result, and traceability to the loader,
  fixture/manifest, and package version used. This task must not repair the implementation
  except for task-local test harness files; failures should be reported as validation
  failures for same-layer repair.
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
notes: 'Constraint supplement for config AI: This is independent validation, not implementation
  repair. Re-run the T-042 forward demo against the T-048 implementation and record
  traceability to package version, loader, fixture/manifest, and output JSON. Do not
  relax acceptance criteria and do not repair core logic here except for task-local
  validation harness files. Failure should produce evidence for same-layer repair/retry.'
fast_pass_permission: green
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:49:45'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: forward_query_package_m1_repair
  type: package
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 forward query package (replacement for T-048)
  registered: '2026-06-24'
  path: 1_asset/forward_query_package_m1_repair
  symlink: true
  status: ready
  notes: M1 forward query package under independent validation. T-059 replaced T-048
    as the implementation under test.
  location: local
- id: A-002
  name: forward_repair_fixture_m1_1
  type: package
  source: predecessor
  source_task: T-059
  source_artifact_id: D-003
  origin: T-059/D-003 task-local M1.1 fixture with synthetic_repair EGFR/A549/xpr
    row
  registered: '2026-06-24'
  path: 1_asset/forward_repair_fixture_m1_1
  symlink: true
  status: ready
  notes: Loader-compatible fixture to re-run the T-042 forward demo case.
  location: local
- id: A-003
  name: forward_repair_manifest_m1_1
  type: manifest
  source: predecessor
  source_task: T-059
  source_artifact_id: D-002
  origin: T-059/D-002 synthetic repair provenance manifest
  registered: '2026-06-24'
  path: 1_asset/forward_repair_manifest_m1_1.yaml
  symlink: true
  status: ready
  notes: 'Used for traceability: fixture provenance, synthetic_repair label, loader
    boundary.'
  location: local
- id: A-004
  name: forward_query_positive_demo_evidence
  type: json
  source: predecessor
  source_task: T-059
  source_artifact_id: D-004
  origin: T-059/D-004 reference positive demo JSON
  registered: '2026-06-24'
  path: 1_asset/forward_query_positive_demo_evidence.json
  symlink: true
  status: ready
  notes: Reference output to compare against re-run result for independent validation.
  location: local
- id: A-005
  name: forward_query_no_hit_evidence
  type: json
  source: predecessor
  source_task: T-059
  source_artifact_id: D-005
  origin: T-059/D-005 reference no-hit JSON
  registered: '2026-06-24'
  path: 1_asset/forward_query_no_hit_evidence.json
  symlink: true
  status: ready
  notes: Reference no-hit output to compare against re-run result.
  location: local
- id: A-006
  name: forward_query_contract_assertions
  type: table
  source: predecessor
  source_task: T-059
  source_artifact_id: D-006
  origin: T-059/D-006 contract assertion table
  registered: '2026-06-24'
  path: 1_asset/forward_query_contract_assertions.csv
  symlink: true
  status: ready
  notes: Reference assertion table listing the T-042 contract checks against T-059.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-050 forward_validation_m1 — Protocol

## Objective

Independently validate the M1 forward query implementation delivered by T-059 (same-layer replacement for T-048). Re-run the T-042 forward demo contract case (EGFR/A549/xpr positive hit + no-hit behavior) against the T-059 package and repair fixture, record traceability to package version, loader, fixture/manifest, and output JSON, and produce a pass/fail validation result. This task must not repair the implementation; failures must be reported as validation failures for same-layer repair/retry.

**Note on T-048 vs T-059:** The T-050 meta.yaml references T-048 as the implementation under test, but T-059 is the selected predecessor and is the accepted same-layer replacement for T-048. T-050 validates T-059's output, not T-048's. Use T-059 `4_artifact/1_package/` as the implementation under test.

## Position In Project

This task sits under `goal_m1_python_package_v2` in the development phase. T-059 has already delivered the forward query core package plus a synthetic repair fixture that bridges the T-042 EGFR/A549/xpr demo contract gap. T-050 independently re-runs that demo to confirm the implementation is reproducible and the contract assertions hold from an independent perspective.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-059/D-001 | `4_artifact/1_package/` | M1 forward query package under validation |
| A-002 | T-059/D-003 | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Fixture to re-run the positive demo |
| A-003 | T-059/D-002 | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Traceability to fixture provenance and loader boundary |
| A-004 (optional) | T-059/D-004 | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Reference positive output for comparison |
| A-005 (optional) | T-059/D-005 | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Reference no-hit output for comparison |
| A-006 (optional) | T-059/D-006 | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Reference assertion outcome table |

All asset paths are under the T-059 task directory at `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/`.

## Execution Steps

1. **Environment setup.** Install or configure the T-059 package from `A-001` into the pxfquery conda environment. Record the installed package version (`pip show pxfquery` or equivalent).
2. **Fixture loading smoke test.** Load the repair fixture `A-002` using the T-046-compatible `M1FixtureLoader` (or equivalent loader API in the package). Assert that the fixture loads without error and the xpr matrix has the expected shape (5 obs x 7 vars per the manifest). Record the loader class and path.
3. **Positive forward demo.** Run the EGFR/A549/xpr forward query against the loaded fixture. Collect the returned JSON/dict output. Verify:
   - `found` is `true`
   - `perturbation` is `EGFR`
   - `cell_line` is `A549`
   - `n_obs` is a positive integer
   - `top_activated` is a non-empty numeric dict
   - `top_suppressed` is a non-empty numeric dict
   - Input echo matches the requested perturbation and cell line
4. **No-hit forward demo.** Run a forward query for an unknown perturbation (e.g. `UNKNOWN_GENE_XYZ999`) against the same fixture. Verify:
   - Output is a structured error/no-hit object (e.g. `{"error": "PerturbationNotFound", ...}`)
   - No Python traceback leaks into the output
   - A relevant error message and suggestions are present
5. **Compare with reference.** Compare the re-run positive JSON (step 3) with the reference evidence `A-004`. Structural shape and key fields should match. Numerical values may differ — focus on structural consistency.
6. **CLI smoke test.** Invoke the forward query via CLI (`pxfquery forward ...`) for the positive case. Assert that stdout contains valid JSON and exit code is 0.
7. **Record traceability.** In the validation report, record:
   - Package version (from `pip show pxfquery` or `importlib.metadata`)
   - Loader class and path
   - Fixture manifest path and synthetic_repair provenance label
   - Reference evidence paths used for comparison
   - All re-run output JSON content
8. **Produce pass/fail result.** Compile a validation results table (CSV) with one row per check (import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo), each marked PASS/FAIL.

## Constraints

- Do not repair core logic — this is independent validation only.
- Do not modify T-059 artifacts or any predecessor task outputs.
- Failures must produce evidence for same-layer repair/retry, not silent workaround.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Preserve the `synthetic_repair` provenance label when referencing the repair fixture. Do not strip or rename it.

## Forbidden

- Modifying T-059 package code, fixture, manifest, or JSON evidence.
- Modifying any upstream completed task output.
- Introducing new synthetic data or bridging fixtures.
- Reading project-level raw assets under `2_project_asset/`.
- Using T-048 `4_artifact/` as accepted reference (use T-059 artifacts only).
- Using T024-T040 blocked assets.

## Web Search Allowance

Allowed: no
Reason: All required contract assertions and reference evidence are available from predecessor T-059.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Smoke execution log | `4_artifact/2_persist/forward_validation_smoke_v20260624.log` | yes |
| Re-run positive forward JSON | `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json` | yes |
| Re-run no-hit forward JSON | `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json` | yes |
| Validation results table | `4_artifact/5_table/forward_validation_results_v20260624.csv` | yes |
| Validation report (MD) | `4_artifact/3_document/forward_validation_report_v20260624.md` | yes |
| Execution report (HTML) | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report (HTML) | `4_artifact/3_document/result_report_v20260624.html` | yes |

## Acceptance Criteria

- All required deliverables exist under `4_artifact/` with correct paths.
- Validation results CSV records one PASS/FAIL per check (≥6 checks: import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo).
- All FAIL results include a clear reason and evidence path.
- Traceability record includes package version, loader identity, fixture manifest path, synthetic_repair provenance label, and reference evidence paths.
- Positive re-run output structurally matches the T-059 reference evidence (same key fields, same found=true).
- No-hit re-run output contains a structured error object, not a raw Python traceback.

## Failure / Stop Rules

- If the T-059 package cannot be imported or installed → mark import FAIL and stop. This is a precondition failure.
- If the repair fixture cannot be loaded by the package's loader → mark fixture load FAIL and stop. The fixture may be incompatible.
- If the positive demo returns found=false or errors → mark positive demo FAIL and continue to collect evidence. Do not repair.
- If the no-hit demo produces a raw traceback instead of a structured error → mark no-hit FAIL and continue. Collect the traceback as evidence.
- Zero FAIL results → overall verdict PASS. One or more FAIL results → overall verdict FAIL.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-059
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package
    reason: "M1 forward query package under independent validation (T-059 replacement for T-048)."
  - id: A-002
    source_task: T-059
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_repair_fixture_m1_1
    reason: "Repair fixture needed to re-run the EGFR/A549/xpr positive demo."
  - id: A-003
    source_task: T-059
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_repair_manifest_m1_1.yaml
    reason: "Manifest for traceability to fixture provenance and synthetic_repair label."
optional:
  - id: A-004
    source_task: T-059
    source_artifact_id: D-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json
    reason: "Reference positive demo JSON for comparison against re-run output."
  - id: A-005
    source_task: T-059
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json
    reason: "Reference no-hit JSON for comparison against re-run output."
  - id: A-006
    source_task: T-059
    source_artifact_id: D-006
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/5_table/forward_query_contract_assertions_v20260624.csv
    reason: "Reference contract assertion table for expected pass/fail criteria."
forbidden:
  - path: 2_project_asset/
    reason: "forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed"
output:
  - path: 4_artifact/2_persist/forward_validation_smoke_v20260624.log
    type: log
  - path: 4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json
    type: json
  - path: 4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json
    type: json
  - path: 4_artifact/5_table/forward_validation_results_v20260624.csv
    type: table
  - path: 4_artifact/3_document/forward_validation_report_v20260624.md
    type: document
  - path: 4_artifact/3_document/execution_report_v20260624.html
    type: report
  - path: 4_artifact/3_document/result_report_v20260624.html
    type: report
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-050 forward_validation_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories, T-048 `4_artifact/`
- Required registry: `1_asset/registration.yaml` (all 6 assets preflighted ok)
- Must stop if: package import fails (precondition failure), fixture cannot be loaded (compatibility failure)
- Also stop if T-059 is not installed, then install it first

## Objective Restatement
Independently validate T-059's M1 forward query by re-running the T-042 EGFR/A549/xpr demo against the T-059 package + repair fixture, recording traceability (package version, loader, manifest, reference evidence), and producing pass/fail against contract assertions. No core logic repair — only validation harness files may be touched.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/forward_query_package_m1_repair` → T-059 `4_artifact/1_package/` | M1 forward query package under test | ok |
| A-002 | `1_asset/forward_repair_fixture_m1_1` → T-059 `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Fixture with synthetic EGFR/A549/xpr row (5 obs x 7 vars) | ok |
| A-003 | `1_asset/forward_repair_manifest_m1_1.yaml` | Manifest with `provenance_label: synthetic_repair`, loader boundary info | ok |
| A-004 | `1_asset/forward_query_positive_demo_evidence.json` | Reference positive output for structural comparison | ok (optional) |
| A-005 | `1_asset/forward_query_no_hit_evidence.json` | Reference no-hit output for structural comparison | ok (optional) |
| A-006 | `1_asset/forward_query_contract_assertions.csv` | Reference contract checks already passed by T-059 | ok (optional) |

## Execution Strategy
1. **Install T-059 package.** `pip install -e 1_asset/forward_query_package_m1_repair` in pxfquery conda env. Record version from `pip show pxfquery`.
2. **Fixture loading smoke test.** Use `PxFquery(manifest_path=A-003, fixture_root=A-002)` or `M1FixtureLoader` directly. Assert `xpr` matrix shape is (5, 7). Record loader class = `M1FixtureLoader`.
3. **Positive forward demo.** Call `PxFquery.pert2func("EGFR", "A549", matrix_type="xpr")`. Verify `found=true`, `perturbation=EGFR`, `cell_line=A549`, `n_obs` positive int, `top_activated` and `top_suppressed` non-empty numeric dicts, input echo matches.
4. **No-hit forward demo.** Call `pert2func("UNKNOWN_GENE_XYZ999", "A549")`. Verify structured `{"error": "PerturbationNotFound", ...}`, no raw traceback, error message and suggestions present.
5. **Compare with reference (A-004/A-005).** Structural key match only — numerical values may differ.
6. **CLI smoke test.** `pxfquery forward --manifest <A-003 path> --fixture-root <A-002 path> --perturbation EGFR --cell-line A549`. Assert exit 0, stdout valid JSON.
7. **Record traceability.** Package version, loader identity, manifest path, synthetic_repair label, reference paths, all output JSON.
8. **Compile pass/fail table.** One CSV row per check (import, fixture load, positive hit, no-hit, JSON shape, CLI, input echo), each PASS/FAIL.

## Conservative Execution Advice
- Start with: Step 1 (install) + Step 2 (fixture smoke test) — if either fails, stop and report precondition failure.
- Smoke/demo command: `python -c "from pxfquery.core import PxFquery; q=PxFquery(manifest_path='<A-003>', fixture_root='<A-002>'); print(q.loader.fixture.xpr.shape)"` → expected `(5, 7)`
- Full run only after: Step 2 passes (fixture loads, shape matches manifest).
- Cost/time risk: Low — local execution, no API calls, small fixture (5 obs x 7 vars), ~1 min total.
- Checkpoint advice: Save output JSON after step 3 and step 4 before proceeding to comparison.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Smoke execution log | `4_artifact/2_persist/forward_validation_smoke_v20260624.log` | File exists, contains install + fixture load output |
| Re-run positive forward JSON | `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json` | Valid JSON with `found: true`, `perturbation: EGFR`, `cell_line: A549` |
| Re-run no-hit forward JSON | `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json` | Valid JSON with `error: PerturbationNotFound` |
| Validation results table | `4_artifact/5_table/forward_validation_results_v20260624.csv` | ≥6 rows, each PASS/FAIL with evidence path |
| Validation report (MD) | `4_artifact/3_document/forward_validation_report_v20260624.md` | Documents all steps, traceability, and overall pass/fail |
| Execution report (HTML) | `4_artifact/3_document/execution_report_v20260624.html` | HTML rendering of smoke log + outputs |
| Result report (HTML) | `4_artifact/3_document/result_report_v20260624.html` | HTML rendering of validation results table |

## Failure / Stop Conditions
- Package cannot be imported → mark import FAIL, stop.
- Fixture cannot be loaded by `M1FixtureLoader` or `PxFquery.load_fixture()` → mark fixture load FAIL, stop.
- Positive demo returns `found=false` or error → mark positive demo FAIL, continue to collect evidence (do not repair).
- No-hit demo returns raw traceback instead of structured error → mark no-hit FAIL, collect traceback as evidence, continue.
- CLI returns non-zero exit or invalid JSON → mark CLI FAIL, continue.
- Zero failures → overall PASS. One or more → overall FAIL.

## Notes For Delivery QA
- The protocol references T-048 in meta.yaml but actually uses T-059 artifacts. The clarification note at the top of protocol.md resolves this. All assets come from T-059.
- Do NOT strip or rename the `synthetic_repair` provenance label.
- Do NOT modify T-059 package code, fixtures, manifests, or evidence.
- Reference JSON files (A-004, A-005) are for structural comparison only — numerical scores may differ due to floating-point or platform differences.
- The package uses hatchling build backend; `pip install -e` from the symlink path works.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/4_artifact/registry.yaml`

```text
artifacts:
  - id: D-001
    name: forward_validation_smoke_log
    type: log
    path: 4_artifact/2_persist/forward_validation_smoke_v20260624.log
    description: Smoke execution log recording install, fixture load, forward demo, no-hit demo, reference comparison, and CLI test.

  - id: D-002
    name: forward_validation_rerun_positive
    type: json
    path: 4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json
    description: Re-run positive forward query JSON output (EGFR/A549/xpr).

  - id: D-003
    name: forward_validation_rerun_nohit
    type: json
    path: 4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json
    description: Re-run no-hit forward query JSON output (UNKNOWN_GENE_XYZ999/A549).

  - id: D-004
    name: forward_validation_results_table
    type: table
    path: 4_artifact/5_table/forward_validation_results_v20260624.csv
    description: Validation results table with 11 PASS/FAIL checks.

  - id: D-005
    name: forward_validation_report
    type: document
    path: 4_artifact/3_document/forward_validation_report_v20260624.md
    description: Validation report documenting all steps, traceability, and overall pass/fail.

  - id: D-006
    name: execution_report
    type: report
    path: 4_artifact/3_document/execution_report_v20260624.html
    description: HTML rendering of smoke log and outputs.

  - id: D-007
    name: result_report
    type: report
    path: 4_artifact/3_document/result_report_v20260624.html
    description: HTML rendering of validation results table.

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/5_report/completion.md`

```text
# Completion

**Task:** T-050 forward_validation_m1
**Completed:** 2026-06-24
**Overall Verdict:** PASS

## Summary

Independently validated the T-059 M1 forward query implementation by re-running the T-042 EGFR/A549/xpr demo contract case. All 11 checks passed.

## Checks Performed

| Check ID | Status |
|---|---|
| SMOKE-001 (package import) | PASS |
| SMOKE-002 (fixture load) | PASS |
| FORWARD-001 (positive hit) | PASS |
| FORWARD-002 (top_activated) | PASS |
| FORWARD-003 (top_suppressed) | PASS |
| FORWARD-004 (input echo) | PASS |
| NOHIT-001 (structured error) | PASS |
| NOHIT-002 (no traceback) | PASS |
| JSON-001 (positive structural match) | PASS |
| JSON-002 (no-hit structural match) | PASS |
| CLI-001 (CLI smoke test) | PASS |

## Deliverables Produced

- `4_artifact/2_persist/forward_validation_smoke_v20260624.log`
- `4_artifact/2_persist/forward_validation_rerun_positive_v20260624.json`
- `4_artifact/2_persist/forward_validation_rerun_nohit_v20260624.json`
- `4_artifact/5_table/forward_validation_results_v20260624.csv`
- `4_artifact/3_document/forward_validation_report_v20260624.md`
- `4_artifact/3_document/execution_report_v20260624.html`
- `4_artifact/3_document/result_report_v20260624.html`

## Traceability

- Package: pxfquery v0.1.0 (T-059 package, installed from `3_execution/forward_query_package_m1_local`)
- Loader: pxfquery.data.m1_loader.M1FixtureLoader
- Manifest: `1_asset/forward_repair_manifest_m1_1.yaml` (provenance_label: synthetic_repair)
- Fixture: `1_asset/forward_repair_fixture_m1_1` (xpr shape (5, 7))
- Reference positive: `1_asset/forward_query_positive_demo_evidence.json`
- Reference no-hit: `1_asset/forward_query_no_hit_evidence.json`

## Notes

- This task validates T-059 (replacement for T-048) as specified in protocol clarification.
- Re-run positive output matches reference structurally; the only key difference is `_evidence` field which is T-059 harness-specific metadata.
- Re-run no-hit output matches reference structurally; same `_evidence` difference.
- No core logic was modified. This was pure independent validation.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: development
- ID: T-050 | Name: forward_validation_m1
- Objective: Independently validate the M1 forward query implementation. Use T-048 as the implementation under test and rerun the forward demo case from the contract. Deliver smoke logs, JSON output, pass/fail result, and traceability to the loader, fixture/manifest, and package version used. This task must not repair the implementation except for task-local test harness files; failures should be reported as validation failures for same-layer repair.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_validation_m1`

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
# AI Handoff: T-050 forward_validation_m1

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
# Delivery QA: T-050 forward_validation_m1

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
