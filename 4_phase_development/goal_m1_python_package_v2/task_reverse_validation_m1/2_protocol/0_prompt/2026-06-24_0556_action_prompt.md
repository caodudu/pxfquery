# Execution Prompt
Generated: 2026-06-24 05:56

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-051
name: reverse_validation_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Independently validate the M1 reverse query implementation. Use T-049 as
  the implementation under test and rerun the reverse demo case from the contract.
  Deliver smoke logs, JSON output, pass/fail result, and traceability to the loader,
  fixture/manifest, ranking/scoring behavior, and package version used. This task
  must not hide instability by changing acceptance criteria.
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
  repair. Re-run the T-042 reverse demo against the T-049 implementation and record
  traceability to package version, loader, fixture/manifest, ranking/scoring behavior,
  and output JSON. Do not relax acceptance criteria or hide instability. Failure should
  produce evidence for same-layer repair/retry.'
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T05:56:08'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: reverse_query_package_code
  type: code
  source: predecessor
  source_task: T-060
  source_artifact_id: D-001
  origin: T-060/D-001 — package code symlink to T-044 skeleton; validated as implementation
    under test
  registered: '2026-06-24'
  path: 1_asset/reverse_query_package_code
  symlink: true
  status: ready
  notes: 'Symlink target: task_package_skeleton_m1/4_artifact/1_package/pxfquery.
    T-060 delivery_qa red_return flagged this as not self-contained. Used as implementation
    under test with caveat recorded.'
  location: local
- id: A-002
  name: reverse_repair_fixture_m1_1
  type: data
  source: predecessor
  source_task: T-060
  source_artifact_id: D-002
  origin: T-060/D-002 — repair fixture with synthetic A549 + HALLMARK_MYC_TARGETS_V1
  registered: '2026-06-24'
  path: 1_asset/reverse_repair_fixture_m1_1
  symlink: true
  status: ready
  notes: 15 observations x 9 variables; includes HALLMARK_MYC_TARGETS_V1 and A549;
    synthetic non-biological data
  location: local
- id: A-003
  name: reverse_repair_manifest_m1_1
  type: document
  source: predecessor
  source_task: T-060
  source_artifact_id: D-003
  origin: T-060/D-003 — manifest for M1FixtureLoader
  registered: '2026-06-24'
  path: 1_asset/reverse_repair_manifest_m1_1.yaml
  symlink: true
  status: ready
  notes: Loads cp, sh, xpr matrices from reverse_repair_fixture_m1_1/
  location: local
- id: A-004
  name: reverse_demo_evidence_reference
  type: document
  source: predecessor
  source_task: T-060
  source_artifact_id: D-005
  origin: T-060/D-005 — reference positive demo JSON
  registered: '2026-06-24'
  path: 1_asset/reverse_demo_evidence_reference.json
  symlink: true
  status: ready
  notes: Generated by T-060 execution. Used for reproducibility comparison only.
  location: local
- id: A-005
  name: reverse_error_no_hit_evidence_reference
  type: document
  source: predecessor
  source_task: T-060
  source_artifact_id: D-006
  origin: T-060/D-006 — reference no-hit/error JSON
  registered: '2026-06-24'
  path: 1_asset/reverse_error_no_hit_evidence_reference.json
  symlink: true
  status: ready
  notes: Generated by T-060 execution. Used for comparison only.
  location: local
- id: A-006
  name: reverse_ranking_evidence_reference
  type: table
  source: predecessor
  source_task: T-060
  source_artifact_id: D-007
  origin: T-060/D-007 — reference ranking CSV
  registered: '2026-06-24'
  path: 1_asset/reverse_ranking_evidence_reference.csv
  symlink: true
  status: ready
  notes: Generated by T-060 execution. Used for deterministic scoring comparison.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-051 reverse_validation_m1 — Protocol

## Objective

Independently validate the M1 reverse query implementation delivered by T-060 (repair replacement for T-049). Re-run the T-042 reverse demo case against the T-060 package code and repair fixture/manifest. Deliver smoke logs, JSON output, pass/fail result, and traceability to the package version, loader, fixture/manifest, ranking/scoring behavior, and output JSON. Do not hide instability by changing acceptance criteria.

## Position In Project

This task sits under `goal_m1_python_package_v2` and is the independent validation gate for the T-060 reverse query core repair. T-049 (the original implementation) failed with `execute_config_mismatch` and was replaced by T-060. T-060 completed execution but received `red_return` in delivery QA because its registered package-code artifact is a symlink to the T-044 package skeleton, not self-contained task-local code. This validation task treats the T-060 package path (under `4_artifact/1_package/pxfquery/`) as the implementation under test, noting the symlink provenance as a traceability observation. This task does not repair T-060; it independently validates and reports pass/fail honestly.

## Inputs

| Asset ID | Source Task | Source Artifact | Path | Why needed |
|---|---|---|---|---|
| A-001 | T-060 | D-001 | `4_artifact/1_package/pxfquery` | Implementation under test: reverse query package code (note: symlink to T-044; see T-060 delivery_qa.md) |
| A-002 | T-060 | D-002 | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Repair fixture substrate for the T-042 reverse demo case (xpr matrix with HALLMARK_MYC_TARGETS_V1 + A549) |
| A-003 | T-060 | D-003 | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Manifest for loading the repair fixture via T-046 M1FixtureLoader |
| A-004 | T-060 | D-005 | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Reference positive demo JSON for comparison/reproducibility check |
| A-005 | T-060 | D-006 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Reference no-hit/error JSON for comparison |
| A-006 | T-060 | D-007 | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` | Reference ranking evidence for deterministic scoring comparison |

## Execution Steps

1. Record the registered package version and path: inspect `4_artifact/1_package/pxfquery` symlink target, report the resolved path and whether it points to T-044.
2. Load the repair fixture/manifest using the T-046 `M1FixtureLoader` API and confirm matrix shape, target columns, and cell-line coverage.
3. Run the T-042 reverse positive demo case: activate `HALLMARK_APOPTOSIS`, suppress `HALLMARK_MYC_TARGETS_V1`, cell line `A549`, matrix type `xpr`, top-n 3, using the repair xpr matrix. Record stdout, stderr, exit code, and elapsed time.
4. Run the structured no-hit/error cases matching T-042 contract: `NoMatrixLoaded`, `ProgramNotFound`, `ContextNotFound`, `LowConfidenceResult`, empty-target no-hit. Record results.
5. Compare the ranking output against T-060 reference evidence (A-004, A-006): check JSON structure, candidate order, similarity values, and repeatability.
6. Run the CLI reverse interface and confirm smoke output matches documented behavior.
7. Write a structured JSON validation report comparing observed vs. expected behavior with explicit pass/fail per check.
8. Register all accepted outputs in `4_artifact/registry.yaml`.

## Constraints

- Do not modify T-060 artifacts, T-049 artifacts, or any upstream completed task outputs.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not relax acceptance criteria to hide instability. Failure should produce clear evidence for same-layer repair/retry.
- Use the `pxfquery` conda environment: `/Users/dudu/Softwares/miniconda/envs/pxfquery`.
- All reverse query code under test must go through the T-046 loader API; do not write an ad hoc data reader.

## Forbidden

- Modifying predecessor task artifacts (T-042, T-043, T-044, T-046, T-049, T-060).
- Reading project-level raw assets under `2_project_asset/`.
- Reading T024-T040 blocked assets.
- Writing protocols or tasks outside the current task structure.
- Calling downstream prompt endpoints (`/prompt/generate`, `/prompt/generate-check`, `/prompt/generate-delivery`).

## Web Search Allowance

Allowed: no
Reason: This is an independent re-validation of existing task-local artifacts. No external or current information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reverse validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v{date}.json` | yes |
| Smoke logs and evidence | `3_execution/` | yes |
| Validation summary (table/comparison) | `4_artifact/5_table/reverse_validation_comparison_v{date}.csv` | recommended |
| Execution report (HTML) | `4_artifact/3_document/validation_report_v{date}.html` | recommended |
| Completion report | `5_report/completion.md` | yes |
| Artifact registry | `4_artifact/registry.yaml` | yes |

## Acceptance Criteria

- Validation report JSON is produced with structured pass/fail per check.
- All T-042 reverse demo checks run without unhandled exceptions.
- Pass/fail verdict is explicitly stated (not ambiguous).
- Traceability records: package code path and resolved symlink target, loader version, fixture manifest ID, ranking/scoring method.
- If T-060 reference outputs do not reproduce exactly, the report states the difference and does not silently accept them.

## Failure / Stop Rules

- If the T-060 package path is unresolvable or the code cannot be imported, stop and report the import error with full traceback. Do not invent a fallback implementation.
- If the repair fixture cannot be loaded by the T-046 loader API, stop and report the loader error.
- If any validation step throws an unhandled exception, stop and report the error as a failure.
- Do not fail silently; every check must have an explicit pass or fail entry in the validation report.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-060
    source_artifact_id: D-001
    path: 4_artifact/1_package/pxfquery
    reason: "Implementation under test: reverse query package code (symlink to T-044; see T-060 delivery_qa.md for provenance)"
  - id: A-002
    source_task: T-060
    source_artifact_id: D-002
    path: 4_artifact/2_persist/reverse_repair_fixture_m1_1/
    reason: "Repair fixture substrate for T-042 reverse demo (xpr matrix with HALLMARK_MYC_TARGETS_V1 + A549)"
  - id: A-003
    source_task: T-060
    source_artifact_id: D-003
    path: 4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml
    reason: "Manifest for loading the repair fixture via T-046 M1FixtureLoader"
  - id: A-004
    source_task: T-060
    source_artifact_id: D-005
    path: 4_artifact/2_persist/reverse_demo_evidence_v20260624.json
    reason: "Reference positive demo JSON for reproducibility comparison"
  - id: A-005
    source_task: T-060
    source_artifact_id: D-006
    path: 4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json
    reason: "Reference no-hit/error JSON for comparison"
  - id: A-006
    source_task: T-060
    source_artifact_id: D-007
    path: 4_artifact/5_table/reverse_ranking_evidence_v20260624.csv
    reason: "Reference ranking evidence for deterministic scoring comparison"
optional: []
forbidden:
  - path: 2_project_asset/
    reason: "forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed"
output:
  - path: 4_artifact/2_persist/reverse_validation_report_v{date}.json
    type: json_evidence
  - path: 4_artifact/5_table/reverse_validation_comparison_v{date}.csv
    type: table
  - path: 4_artifact/3_document/validation_report_v{date}.html
    type: html_report
  - path: 4_artifact/registry.yaml
    type: registry
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-051 reverse_validation_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: `2_project_asset/`, predecessor task directories (T-042, T-043, T-044, T-046, T-049, T-060)
- Required registry: `1_asset/registration.yaml` (6 assets, all ok)
- Must stop if: package code unresolvable, fixture cannot load, unhandled exception in any validation step

## Objective Restatement
Independently validate M1 reverse query (T-060/T-049) by re-running T-042 reverse demo against registered assets. Produce structured pass/fail report with full traceability. Do not hide instability or relax acceptance criteria.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/reverse_query_package_code` (symlink → T-044 pxfquery/) | Implementation under test | ok |
| A-002 | `1_asset/reverse_repair_fixture_m1_1/` | Fixture with A549 xpr matrix + HALLMARK targets | ok |
| A-003 | `1_asset/reverse_repair_manifest_m1_1.yaml` | Manifest for M1FixtureLoader | ok |
| A-004 | `1_asset/reverse_demo_evidence_reference.json` | Reference positive demo JSON | ok |
| A-005 | `1_asset/reverse_error_no_hit_evidence_reference.json` | Reference no-hit/error JSON | ok |
| A-006 | `1_asset/reverse_ranking_evidence_reference.csv` | Reference ranking CSV | ok |

## Execution Strategy
1. **Package provenance** — inspect symlink target, record resolved path and version.
2. **Load fixture via M1FixtureLoader** — must pass `fixture_root` explicitly (loader does not use manifest's `fixture_package_root` field). Confirm xpr matrix shape (15×9), target columns, A549 coverage.
3. **Positive demo** — `reverse_query(xpr, activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="A549", top_n=3)`. Record stdout/stderr/exit/elapsed, compare with A-004.
4. **No-hit/error cases** — test `NoMatrixLoaded` (None matrix), `ProgramNotFound` (bogus program), `ContextNotFound` (bogus cell line), `LowConfidenceResult`, empty-target no-hit. Compare with A-005.
5. **Ranking comparison** — compare CSV vs A-006 (order, similarity, candidate names). Report exact match or diff.
6. **CLI smoke** — run CLI reverse interface, confirm output matches documented format.
7. **Validation report** — write structured JSON with pass/fail per check (`4_artifact/2_persist/reverse_validation_report_v{date}.json`).
8. **Register outputs** in `4_artifact/registry.yaml`.

## Conservative Execution Advice
- **Start with:** Step 1 (symlink inspection) + Step 2 (loader test with explicit fixture_root). These confirm the substrate before any query runs.
- **Smoke/demo command:**
  ```python
  from data import M1FixtureLoader
  from query.reverse import reverse_query
  loader = M1FixtureLoader("1_asset/reverse_repair_manifest_m1_1.yaml", fixture_root="1_asset/reverse_repair_fixture_m1_1")
  fixture = loader.fixture
  result = reverse_query(fixture.xpr, activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="A549", top_n=3)
  ```
- **Full run only after:** Step 2 passes (fixture loads, shape correct).
- **Cost/time risk:** Negligible — local-only, small synthetic fixture (15 rows). All runs should complete under 60s.
- **Checkpoint advice:** Save intermediate JSON outputs in `3_execution/` after each step.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v{date}.json` | Structured pass/fail per check, explicit verdict |
| Smoke logs & evidence | `3_execution/` | stdout/stderr captures, exit codes |
| Comparison table (CSV) | `4_artifact/5_table/reverse_validation_comparison_v{date}.csv` | Rows match reference; differences explicit |
| Execution report (HTML) | `4_artifact/3_document/validation_report_v{date}.html` | Rendered summary of all checks |
| Completion report | `5_report/completion.md` | Lists executed steps, verdict, traceability |
| Artifact registry | `4_artifact/registry.yaml` | All outputs registered |

## Failure / Stop Conditions
- **Package import error:** Stop, report full traceback. Do not fallback.
- **M1FixtureLoader failure:** Stop if `fixture_root` not accepted or manifest/h5ad unreadable.
- **Unhandled exception in any step:** Stop, record as failure. Do not skip.
- **Reference comparison mismatch:** Record difference explicitly; do not silently accept. Failure is valid evidence.
- **CLI missing or crashes:** Record as failure; do not fabricate CLI output.

## Notes For Delivery QA
- Package is a symlink to T-044 (`task_package_skeleton_m1/4_artifact/1_package/pxfquery`). The validation report must record this as a traceability observation.
- M1FixtureLoader does **not** use the manifest's `fixture_package_root` field. It derives root relative to manifest directory + `fixture_package_m1`, which is wrong for this task. The execution AI must pass `fixture_root` explicitly to `M1FixtureLoader(manifest_path, fixture_root=...)`.
- The reverse_query API signature is: `reverse_query(matrix, activate, suppress, cell_line, matrix_type="xpr", top_n=10, low_confidence_threshold=0.05)`.
- If validation produces failure results (e.g., scores differ from reference), that is valid output — do not relax thresholds to force pass.

```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-051 reverse_validation_m1
Status: active | Executor: hybrid
Objective: Independently validate the M1 reverse query implementation. Use T-049 as the implementation under test and rerun the reverse demo case from the contract. Deliver smoke logs, JSON output, pass/fail result, and traceability to the loader, fixture/manifest, ranking/scoring behavior, and package version used. This task must not hide instability by changing acceptance criteria.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-051 reverse_validation_m1 — Protocol

## Objective

Independently validate the M1 reverse query implementation delivered by T-060 (repair replacement for T-049). Re-run the T-042 reverse demo case against the T-060 package code and repair fixture/manifest. Deliver smoke logs, JSON output, pass/fail result, and traceability to the package version, loader, fixture/manifest, ranking/scoring behavior, and output JSON. Do not hide instability by changing acceptance criteria.

## Position In Project

This task sits under `goal_m1_python_package_v2` and is the independent validation gate for the T-060 reverse query core repair. T-049 (the original implementation) failed with `execute_config_mismatch` and was replaced by T-060. T-060 completed execution but received `red_return` in delivery QA because its registered package-code artifact is a symlink to the T-044 package skeleton, not self-contained task-local code. This validation task treats the T-060 package path (under `4_artifact/1_package/pxfquery/`) as the implementation under test, noting the symlink provenance as a traceability observation. This task does not repair T-060; it independently validates and reports pass/fail honestly.

## Inputs

| Asset ID | Source Task | Source Artifact | Path | Why needed |
|---|---|---|---|---|
| A-001 | T-060 | D-001 | `4_artifact/1_package/pxfquery` | Implementation under test: reverse query package code (note: symlink to T-044; see T-060 delivery_qa.md) |
| A-002 | T-060 | D-002 | `4_artifact/2_persist/reverse_repair_fixture_m1_1/` | Repair fixture substrate for the T-042 reverse demo case (xpr matrix with HALLMARK_MYC_TARGETS_V1 + A549) |
| A-003 | T-060 | D-003 | `4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml` | Manifest for loading the repair fixture via T-046 M1FixtureLoader |
| A-004 | T-060 | D-005 | `4_artifact/2_persist/reverse_demo_evidence_v20260624.json` | Reference positive demo JSON for comparison/reproducibility check |
| A-005 | T-060 | D-006 | `4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json` | Reference no-hit/error JSON for comparison |
| A-006 | T-060 | D-007 | `4_artifact/5_table/reverse_ranking_evidence_v20260624.csv` | Reference ranking evidence for deterministic scoring comparison |

## Execution Steps

1. Record the registered package version and path: inspect `4_artifact/1_package/pxfquery` symlink target, report the resolved path and whether it points to T-044.
2. Load the repair fixture/manifest using the T-046 `M1FixtureLoader` API and confirm matrix shape, target columns, and cell-line coverage.
3. Run the T-042 reverse positive demo case: activate `HALLMARK_APOPTOSIS`, suppress `HALLMARK_MYC_TARGETS_V1`, cell line `A549`, matrix type `xpr`, top-n 3, using the repair xpr matrix. Record stdout, stderr, exit code, and elapsed time.
4. Run the structured no-hit/error cases matching T-042 contract: `NoMatrixLoaded`, `ProgramNotFound`, `ContextNotFound`, `LowConfidenceResult`, empty-target no-hit. Record results.
5. Compare the ranking output against T-060 reference evidence (A-004, A-006): check JSON structure, candidate order, similarity values, and repeatability.
6. Run the CLI reverse interface and confirm smoke output matches documented behavior.
7. Write a structured JSON validation report comparing observed vs. expected behavior with explicit pass/fail per check.
8. Register all accepted outputs in `4_artifact/registry.yaml`.

## Constraints

- Do not modify T-060 artifacts, T-049 artifacts, or any upstream completed task outputs.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Do not relax acceptance criteria to hide instability. Failure should produce clear evidence for same-layer repair/retry.
- Use the `pxfquery` conda environment: `/Users/dudu/Softwares/miniconda/envs/pxfquery`.
- All reverse query code under test must go through the T-046 loader API; do not write an ad hoc data reader.

## Forbidden

- Modifying predecessor task artifacts (T-042, T-043, T-044, T-046, T-049, T-060).
- Reading project-level raw assets under `2_project_asset/`.
- Reading T024-T040 blocked assets.
- Writing protocols or tasks outside the current task structure.
- Calling downstream prompt endpoints (`/prompt/generate`, `/prompt/generate-check`, `/prompt/generate-delivery`).

## Web Search Allowance

Allowed: no
Reason: This is an independent re-validation of existing task-local artifacts. No external or current information is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Reverse validation report (JSON) | `4_artifact/2_persist/reverse_validation_report_v{date}.json` | yes |
| Smoke logs and evidence | `3_execution/` | yes |
| Validation summary (table/comparison) | `4_artifact/5_table/reverse_validation_comparison_v{date}.csv` | recommended |
| Execution report (HTML) | `4_artifact/3_document/validation_report_v{date}.html` | recommended |
| Completion report | `5_report/completion.md` | yes |
| Artifact registry | `4_artifact/registry.yaml` | yes |

## Acceptance Criteria

- Validation report JSON is produced with structured pass/fail per check.
- All T-042 reverse demo checks run without unhandled exceptions.
- Pass/fail verdict is explicitly stated (not ambiguous).
- Traceability records: package code path and resolved symlink target, loader version, fixture manifest ID, ranking/scoring method.
- If T-060 reference outputs do not reproduce exactly, the report states the difference and does not silently accept them.

## Failure / Stop Rules

- If the T-060 package path is unresolvable or the code cannot be imported, stop and report the import error with full traceback. Do not invent a fallback implementation.
- If the repair fixture cannot be loaded by the T-046 loader API, stop and report the loader error.
- If any validation step throws an unhandled exception, stop and report the error as a failure.
- Do not fail silently; every check must have an explicit pass or fail entry in the validation report.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (6)
- A-001 [code] reverse_query_package_code — path: 1_asset/reverse_query_package_code — origin: T-060/D-001 — package code symlink to T-044 skeleton; validated as implementation under test
- A-002 [data] reverse_repair_fixture_m1_1 — path: 1_asset/reverse_repair_fixture_m1_1 — origin: T-060/D-002 — repair fixture with synthetic A549 + HALLMARK_MYC_TARGETS_V1
- A-003 [document] reverse_repair_manifest_m1_1 — path: 1_asset/reverse_repair_manifest_m1_1.yaml — origin: T-060/D-003 — manifest for M1FixtureLoader
- A-004 [document] reverse_demo_evidence_reference — path: 1_asset/reverse_demo_evidence_reference.json — origin: T-060/D-005 — reference positive demo JSON
- A-005 [document] reverse_error_no_hit_evidence_reference — path: 1_asset/reverse_error_no_hit_evidence_reference.json — origin: T-060/D-006 — reference no-hit/error JSON
- A-006 [table] reverse_ranking_evidence_reference — path: 1_asset/reverse_ranking_evidence_reference.csv — origin: T-060/D-007 — reference ranking CSV

### Asset Rules

### Required
- 4_artifact/1_package/pxfquery — Implementation under test: reverse query package code (symlink to T-044; see T-060 delivery_qa.md for provenance)
- 4_artifact/2_persist/reverse_repair_fixture_m1_1/ — Repair fixture substrate for T-042 reverse demo (xpr matrix with HALLMARK_MYC_TARGETS_V1 + A549)
- 4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml — Manifest for loading the repair fixture via T-046 M1FixtureLoader
- 4_artifact/2_persist/reverse_demo_evidence_v20260624.json — Reference positive demo JSON for reproducibility comparison
- 4_artifact/2_persist/reverse_error_no_hit_evidence_v20260624.json — Reference no-hit/error JSON for comparison
- 4_artifact/5_table/reverse_ranking_evidence_v20260624.csv — Reference ranking evidence for deterministic scoring comparison
### Forbidden
- 2_project_asset/ — forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
### Output
- 4_artifact/2_persist/reverse_validation_report_v{date}.json
- 4_artifact/5_table/reverse_validation_comparison_v{date}.csv
- 4_artifact/3_document/validation_report_v{date}.html
- 4_artifact/registry.yaml

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

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_m1_python_package_v2/task_reverse_validation_m1/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1/5_report/execution_handoff.md`

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
