# Checking Prompt
Generated: 2026-06-24 05:55

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-052
name: package_assembly_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Assemble the runnable M1 package surface. Use T-044 package skeleton plus
  T-048 forward and T-049 reverse implementations. Deliver an installable package,
  import evidence, CLI command wiring, and demo commands for forward and reverse.
  This task may connect modules and package entry points, but must not reimplement
  query logic or replace validation evidence from T-050/T-051.
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
notes: 'Constraint supplement for config AI: Assemble and wire the package surface
  only. Use T-044 skeleton plus T-048/T-049 implementations. Deliver install/import
  evidence, CLI entry points, and demo commands. Do not reimplement forward/reverse
  logic, do not replace validation evidence, and do not use T024-T040 artifacts. If
  assembly fails, report packaging/interface gaps for same-layer repair.'
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-24T05:55:11'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: pxfquery_pyproject_base
  type: config
  source: predecessor
  source_task: T-044
  source_artifact_id: D-001
  origin: T-044/D-001 pyproject.toml
  registered: '2026-06-24'
  path: 1_asset/pxfquery_pyproject_base.toml
  symlink: true
  status: ready
  notes: Base pyproject.toml with name=pxfquery, version=0.1.0, hatchling build, src-layout
  location: local
- id: A-002
  name: pxfquery_cli_init
  type: code
  source: predecessor
  source_task: T-044
  source_artifact_id: D-002
  origin: T-044/D-002 pxfquery/cli/__init__.py
  registered: '2026-06-24'
  path: 1_asset/pxfquery_cli_init.py
  symlink: true
  status: ready
  notes: CLI wiring with forward, reverse, and info subcommands
  location: local
- id: A-003
  name: pxfquery_cli_main_module
  type: code
  source: predecessor
  source_task: T-044
  source_artifact_id: D-002
  origin: T-044/D-002 pxfquery/cli/__main__.py
  registered: '2026-06-24'
  path: 1_asset/pxfquery_cli_main_module.py
  symlink: true
  status: ready
  notes: python -m pxfquery entry point
  location: local
- id: A-004
  name: forward_query_impl
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/query/forward.py
  registered: '2026-06-24'
  path: 1_asset/forward_query_impl.py
  symlink: true
  status: ready
  notes: Forward query implementation (pert2func / pert2func logic)
  location: local
- id: A-005
  name: reverse_query_impl
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/query/reverse.py
  registered: '2026-06-24'
  path: 1_asset/reverse_query_impl.py
  symlink: true
  status: ready
  notes: Reverse query implementation (func2pert / reverse_query logic)
  location: local
- id: A-006
  name: forward_package_data_modules
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/data/
  registered: '2026-06-24'
  path: 1_asset/forward_package_data_modules
  symlink: true
  status: ready
  notes: Data loader modules including M1FixtureLoader and base loader
  location: local
- id: A-007
  name: forward_package_index_modules
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/index/
  registered: '2026-06-24'
  path: 1_asset/forward_package_index_modules
  symlink: true
  status: ready
  notes: Index modules (cellline, drug, function, gene)
  location: local
- id: A-008
  name: forward_package_llm_modules
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/llm/
  registered: '2026-06-24'
  path: 1_asset/forward_package_llm_modules
  symlink: true
  status: ready
  notes: LLM prompt module
  location: local
- id: A-009
  name: forward_package_viz_modules
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/viz/
  registered: '2026-06-24'
  path: 1_asset/forward_package_viz_modules
  symlink: true
  status: ready
  notes: Visualization module
  location: local
- id: A-010
  name: forward_package_core_module
  type: code
  source: predecessor
  source_task: T-059
  source_artifact_id: D-001
  origin: T-059/D-001 src/pxfquery/core.py
  registered: '2026-06-24'
  path: 1_asset/forward_package_core_module.py
  symlink: true
  status: ready
  notes: Reference core module with PxFquery class (func2pert returns NotImplemented
    in T-059; must be rewired in assembly)
  location: local
- id: A-011
  name: forward_repair_fixture
  type: data
  source: predecessor
  source_task: T-059
  source_artifact_id: D-003
  origin: T-059/D-003 forward_repair_fixture_m1_1/
  registered: '2026-06-24'
  path: 1_asset/forward_repair_fixture
  symlink: true
  status: ready
  notes: Forward demo fixture with synthetic EGFR/A549/xpr positive-demo row
  location: local
- id: A-012
  name: forward_repair_manifest
  type: config
  source: predecessor
  source_task: T-059
  source_artifact_id: D-002
  origin: T-059/D-002 forward_repair_manifest_m1_1.yaml
  registered: '2026-06-24'
  path: 1_asset/forward_repair_manifest.yaml
  symlink: true
  status: ready
  notes: Forward repair manifest describing the synthetic_repair fixture provenance
  location: local
- id: A-013
  name: reverse_repair_fixture
  type: data
  source: predecessor
  source_task: T-060
  source_artifact_id: D-002
  origin: T-060/D-002 reverse_repair_fixture_m1_1/
  registered: '2026-06-24'
  path: 1_asset/reverse_repair_fixture
  symlink: true
  status: ready
  notes: Reverse demo fixture with synthetic HALLMARK_MYC_TARGETS_V1 / A549 positive-demo
    support
  location: local
- id: A-014
  name: reverse_repair_manifest
  type: config
  source: predecessor
  source_task: T-060
  source_artifact_id: D-003
  origin: T-060/D-003 reverse_repair_manifest_m1_1.yaml
  registered: '2026-06-24'
  path: 1_asset/reverse_repair_manifest.yam

...[truncated by CyHex prompt assembler: 538 chars omitted]
```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-052 package_assembly_m1 — Protocol

## Objective

Assemble the runnable M1 package surface from predecessor deliverables T-044 (package skeleton), T-059 (forward query core repair), and T-060 (reverse query core repair). Deliver an installable `pxfquery` package under `src/pxfquery/`, import evidence, CLI command wiring with forward/reverse/info subcommands, and demo command output for forward and reverse queries. Wiring and integration only — do not reimplement query logic or replace validation evidence from T-050/T-051.

## Position In Project

Bottom-layer M1 package assembly. Consumes T-044 skeleton structure and CLI wiring, T-059 forward+reverse query implementations, and T-060 reverse repair fixture. The assembled package becomes the single installable surface consumed by downstream M1 validation and demo tasks.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-044/D-001 | `4_artifact/1_package/pyproject.toml` | Base build config (name=pxfquery, hatchling, src-layout) |
| A-015 | T-059/D-001 | `4_artifact/1_package/pyproject.toml` | pyproject.toml with `[project.scripts]` entry |
| A-002 | T-044/D-002 | `pxfquery/cli/__init__.py` | CLI wiring with forward+reverse+info subcommands |
| A-003 | T-044/D-002 | `pxfquery/cli/__main__.py` | `python -m pxfquery` entry |
| A-004 | T-059/D-001 | `src/pxfquery/query/forward.py` | Forward query implementation |
| A-005 | T-059/D-001 | `src/pxfquery/query/reverse.py` | Reverse query implementation |
| A-010 | T-059/D-001 | `src/pxfquery/core.py` | Reference PxFquery class (func2pert needs rewiring) |
| A-006 | T-059/D-001 | `src/pxfquery/data/` | M1FixtureLoader + base loader |
| A-011 | T-059/D-003 | `forward_repair_fixture_m1_1/` | Forward demo fixture (EGFR/A549/xpr) |
| A-012 | T-059/D-002 | `forward_repair_manifest_m1_1.yaml` | Forward repair manifest |
| A-013 | T-060/D-002 | `reverse_repair_fixture_m1_1/` | Reverse demo fixture (HALLMARK_MYC_TARGETS_V1) |
| A-014 | T-060/D-003 | `reverse_repair_manifest_m1_1.yaml` | Reverse repair manifest |

## Execution Steps

1. **Create task-local package directory** at `4_artifact/1_package/` with `src/pxfquery/` layout.
2. **Establish pyproject.toml** — use T-059 version (A-015) with `[project.scripts]` entry; preserve name, version, build config from T-044 (A-001).
3. **Assemble module tree** — copy from T-059 forward package (A-004, A-005, A-006, A-007, A-008, A-009) into `src/pxfquery/`:
   - `query/forward.py` — forward query logic
   - `query/reverse.py` — reverse query logic
   - `data/` — loader modules
   - `index/` — index modules
   - `llm/` — prompt module
   - `viz/` — viz module
4. **Wire core.py** — create `src/pxfquery/core.py` with `PxFquery` class:
   - `pert2func()` delegates to `query/forward.forward_query()`
   - `func2pert()` delegates to `query/reverse.reverse_query()`
   - `load_data()`, `load_fixture()`, `query()` methods from T-059 pattern
   - This is wiring only — each query function already exists in the imported modules.
5. **Wire `__init__.py`** — export `PxFquery` class and `__version__`.
6. **Wire CLI** — copy T-044 `cli/__init__.py` (A-002) and `cli/__main__.py` (A-003); verify forward, reverse, info subcommands all resolve.
7. **Install package** — `pip install -e .` from the task working directory.
8. **Run import smoke** — verify `import pxfquery`, `from pxfquery.core import PxFquery`, `pxfquery --help`, `pxfquery info` all work.
9. **Run forward demo** — use T-059 repair fixture (A-011, A-012):
   ```
   pxfquery forward --perturbation EGFR --cell-line A549 --manifest <manifest_path> --fixture-root <fixture_root>
   ```
   Capture JSON output as evidence.
10. **Run reverse demo** — use T-060 repair fixture (A-013, A-014):
    ```
    pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --manifest <manifest_path> --fixture-root <fixture_root>
    ```
    Capture JSON output as evidence.
11. **Collect evidence** — save import smoke evidence, forward demo JSON, reverse demo JSON, and CLI help text under `4_artifact/`.
12. **Register artifacts** — update `4_artifact/registry.yaml` with all accepted outputs.

## Constraints

- Do not reimplement forward or reverse query logic. All query functions already exist in predecessor modules; only wire them in `core.py`.
- Do not replace, re-validate, or modify validation evidence from T-050/T-051.
- Do not use T024-T040 blocked assets.
- Do not use T-048/T-049 failed predecessor outputs. Use T-059/T-060 replacement outputs only.
- Do not read project-level raw assets under `2_project_asset/`.
- T-060/D-001 (package code) is a symlink to T-044 and is not accepted as standalone reverse implementation. Use T-059 `query/reverse.py` (A-005) as the authoritative reverse query source.
- Preserve `synthetic_repair` provenance labels when using T-059/T-060 fixtures.
- Do not modify predecessor task artifacts.

## Forbidden

- Reimplementing `forward_query()`, `reverse_query()`, or any query logic
- Reading or referencing T-048/T-049 artifacts
- Reading T024-T040 blocked assets
- Reading `2_project_asset/`
- Modifying predecessor task outputs
- Stripping `synthetic_repair` provenance from fixture usage

## Web Search Allowance

Allowed: no
Reason: All required inputs are available from selected predecessor tasks. No external/current information is needed for package assembly.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Assembled package source | `4_artifact/1_package/` | yes |
| Import smoke evidence | `4_artifact/2_import_smoke/smoke_test_v20260624.txt` | yes |
| Forward demo JSON | `4_artifact/2_persist/forward_demo_v20260624.json` | yes |
| Reverse demo JSON | `4_artifact/2_persist/reverse_demo_v20260624.json` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260624.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260624.html` | yes |
| CLI help text | `4_artifact/2

...[truncated by CyHex prompt assembler: 1687 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-044
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml"
    reason: "Canonical base pyproject.toml for the pxfquery package"
  - id: A-002
    source_task: T-044
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/cli/__init__.py"
    reason: "CLI wiring with forward, reverse, and info subcommands"
  - id: A-003
    source_task: T-044
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/cli/__main__.py"
    reason: "python -m pxfquery entry point"
  - id: A-004
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/query/forward.py"
    reason: "Forward query implementation (pert2func)"
  - id: A-005
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/query/reverse.py"
    reason: "Reverse query implementation (reverse_query / func2pert logic)"
  - id: A-010
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/core.py"
    reason: "Reference PxFquery class; func2pert returns NotImplemented and must be rewired in assembly"
  - id: A-006
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/data"
    reason: "Data loader: M1FixtureLoader and base loader for demo fixture loading"
  - id: A-011
    source_task: T-059
    source_artifact_id: D-003
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_repair_fixture_m1_1"
    reason: "Forward demo fixture with synthetic EGFR/A549/xpr positive-demo row"
  - id: A-012
    source_task: T-059
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_repair_manifest_m1_1.yaml"
    reason: "Forward repair manifest documenting synthetic_repair provenance"
  - id: A-013
    source_task: T-060
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_repair_fixture_m1_1"
    reason: "Reverse demo fixture with synthetic HALLMARK_MYC_TARGETS_V1 / A549 support"
  - id: A-014
    source_task: T-060
    source_artifact_id: D-003
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml"
    reason: "Reverse repair manifest documenting synthetic_repair provenance"
  - id: A-015
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/pyproject.toml"
    reason: "pyproject.toml with [project.scripts] entry: pxfquery = pxfquery.cli:main"
optional:
  - id: A-007
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/index"
    reason: "Index modules — not required for M1 demo but included for completeness"
  - id: A-009
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/viz"
    reason: "Viz module — not required for M1 assembly but included for completeness"
  - id: A-008
    source_task: T-059
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/llm"
    reason: "LLM prompt module — not required for M1 assembly but included for completeness"
forbidden:
  - path: 2_project_asset/
    reason: "forbidden for non-digestion task; request a predecessor d

...[truncated by CyHex prompt assembler: 690 chars omitted]
```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: development
Task ID: T-052 | Name: package_assembly_m1
Status: active | Executor: hybrid
Objective: Assemble the runnable M1 package surface. Use T-044 package skeleton plus T-048 forward and T-049 reverse implementations. Deliver an installable package, import evidence, CLI command wiring, and demo commands for forward and reverse. This task may connect modules and package entry points, but must not reimplement query logic or replace validation evidence from T-050/T-051.
Notes / User Natural-Language Intent: Constraint supplement for config AI: Assemble and wire the package surface only. Use T-044 skeleton plus T-048/T-049 implementations. Deliver install/import evidence, CLI entry points, and demo commands. Do not reimplement forward/reverse logic, do not replace validation evidence, and do not use T024-T040 artifacts. If assembly fails, report packaging/interface gaps for same-layer repair.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: development
  project_asset_access: forbidden
  zero_assets: false
  total_assets: 15
  symlink_sync:
    checked: 15
    linked: 15
    skipped: 0
    changed: false
  counts:
    ok: 15
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - id: A-001
    name: pxfquery_pyproject_base
    required: true
    status: ok
    path: 1_asset/pxfquery_pyproject_base.toml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pyproject.toml
    reason: local path exists
  - id: A-002
    name: pxfquery_cli_init
    required: true
    status: ok
    path: 1_asset/pxfquery_cli_init.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/cli/__init__.py
    reason: local path exists
  - id: A-003
    name: pxfquery_cli_main_module
    required: true
    status: ok
    path: 1_asset/pxfquery_cli_main_module.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery/cli/__main__.py
    reason: local path exists
  - id: A-004
    name: forward_query_impl
    required: true
    status: ok
    path: 1_asset/forward_query_impl.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/query/forward.py
    reason: local path exists
  - id: A-005
    name: reverse_query_impl
    required: true
    status: ok
    path: 1_asset/reverse_query_impl.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/query/reverse.py
    reason: local path exists
  - id: A-006
    name: forward_package_data_modules
    required: true
    status: ok
    path: 1_asset/forward_package_data_modules
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/data
    reason: local path exists
  - id: A-007
    name: forward_package_index_modules
    required: true
    status: ok
    path: 1_asset/forward_package_index_modules
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/index
    reason: local path exists
  - id: A-008
    name: forward_package_llm_modules
    required: true
    status: ok
    path: 1_asset/forward_package_llm_modules
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/llm
    reason: local path exists
  - id: A-009
    name: forward_package_viz_modules
    required: true
    status: ok
    path: 1_asset/forward_package_viz_modules
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/viz
    reason: local path exists
  - id: A-010
    name: forward_package_core_module
    required: true
    status: ok
    path: 1_asset/forward_package_core_module.py
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/src/pxfquery/core.py
    reason: local path exists
  - id: A-011
    name: forward_repair_fixture
    required: true
    status: ok
    path: 1_asset/forward_repair_fixture
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_repair_fixture_m1_1
    reason: local path exists
  - id: A-012
    name: forward_repair_manifest
    required: true
    status: ok
    path: 1_asset/forward_repair_manifest.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/2_persist/forward_repair_manifest_m1_1.yaml
    reason: local path exists
  - id: A-013
    name: reverse_repair_fixture
    required: true
    status: ok
    path: 1_asset/reverse_repair_fixture
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_repair_fixture_m1_1
    reason: local path exists
  - id: A-014
    name: reverse_repair_manifest
    required: true
    status: ok
    path: 1_asset/reverse_repair_manifest.yaml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_query_core_repair_m1/4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml
    reason: local path exists
  - id: A-015
    name: forward_package_pyproject_cli
    required: true
    status: ok
    path: 1_asset/forward_package_pyproject_cli.toml
    resolved: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/4_artifact/1_package/pyproject.toml
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-052 package_assembly_m1

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1/5_report/handoff_check_before_exec.md` 是否已写
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
