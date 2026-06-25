# Delivery QA Prompt
Generated: 2026-06-24 03:38

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-044
name: package_skeleton_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Create the clean M1 Python package skeleton for PxFquery. Use T-007 to
  anchor package name, module boundaries, and original tool intent. Deliver pyproject.toml,
  src/pxfquery layout, minimal package metadata, import smoke evidence, and a clear
  placeholder structure for loader/query/CLI modules. Do not migrate old implementation
  code here and do not implement query behavior beyond import-safe stubs.
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
notes: 'Constraint supplement for config AI: Build only the clean package skeleton
  and import-safe stubs. Anchor package name and module boundaries in T-007. Do not
  migrate legacy implementation code and do not implement query behavior here. Deliver
  pyproject.toml, src/pxfquery layout, minimal metadata, and import smoke evidence.
  This bottom-layer asset should remain reusable even if later query implementation
  fails.'
fast_pass_permission: green
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T03:26:17'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/1_asset/registration.yaml`

```text
assets:
- id: A-001
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
  notes: Anchors package name (pxfquery) and module boundaries (core/data/query/index/llm/viz)
  location: local
- id: A-002
  name: pxfquery_module_asset_status_matrix
  type: table
  source: predecessor
  source_task: T-007
  source_artifact_id: D-003
  origin: T-007/D-003
  registered: '2026-06-24'
  path: 1_asset/pxfquery_module_asset_status_matrix.csv
  symlink: true
  status: ready
  notes: Confirms per-module implementation status for stub planning
  location: local
- id: A-003
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
  notes: Provides D001 package setup scope and acceptance criteria
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/2_protocol/2_protocol_split/protocol.md`

```text
# T-044 package_skeleton_m1 — Protocol

## Objective

Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence. Anchor the package name and module boundaries in T-007 development state report. Do not migrate legacy implementation code and do not implement query behavior beyond import-safe stubs.

## Position In Project

This is the first development-phase task for `goal_m1_python_package_v2`. It delivers the bottom-layer Python package skeleton that later tasks will populate with actual loader, query, CLI, and resolver logic. The skeleton must remain reusable even if later implementation fails.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007/D-002 | .../4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Anchors intended package name (pxfquery), module structure (core/data/query/index/llm/viz), and component boundaries from legacy development state |
| A-002 | T-007/D-003 | .../4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Confirms per-module status: which modules are implemented/incomplete/historical, guiding what to stub and what to leave for later tasks |
| A-003 | T-007/D-006 | .../4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Provides recommended D001 package setup scope, acceptance criteria, and explicit do-not-do rules (do not copy main.py, do not edit flat assets) |

## Execution Steps

1. Read T-007 development state report and module status matrix to confirm the canonical package name (`pxfquery`) and intended subpackage boundaries: `core`, `data`, `query`, `index`, `llm`, `viz`.
2. Create `pyproject.toml` at the task's working directory with:
   - `[build-system]` using `setuptools` or `hatchling`
   - `[project]` with `name = "pxfquery"`, minimal metadata (version `0.1.0`, Python `>=3.10`), and no external dependencies beyond stubs
   - `[tool.setuptools.packages.find]` or equivalent pointing to `src`
3. Create the `src/pxfquery/` directory structure:
   - `src/pxfquery/__init__.py` — empty package marker
   - `src/pxfquery/core.py` — import-safe stub class `PxFquery` with `__init__` taking optional config dict, no functional methods
   - `src/pxfquery/data/__init__.py` — empty subpackage; stub `loader.py` with a `DataLoader` class placeholder
   - `src/pxfquery/query/__init__.py` — empty subpackage; stub `forward.py` and `reverse.py` with class placeholders
   - `src/pxfquery/index/__init__.py` — empty subpackage; stub `cellline_index.py`, `drug_index.py`, `gene_index.py`, `function_index.py` with class placeholders
   - `src/pxfquery/llm/__init__.py` — empty subpackage; stub `prompts.py` with function placeholders
   - `src/pxfquery/viz/__init__.py` — empty subpackage; stub `plots.py` with function placeholders
   - `src/pxfquery/cli/__init__.py` — empty subpackage for future CLI entry points
4. Run import smoke test: `python -c "import pxfquery; print(pxfquery.__version__)"` from the package root.
5. Record import smoke evidence as a file in `4_artifact/`.

## Constraints

- Use package name `pxfquery` as anchored by T-007 legacy codebase (`core.py` defines `PxFquery`, old package lives under `code/pxfquery_package/`).
- Use `src/pxfquery` layout (src-layout).
- All module stubs must be import-safe: no external imports that would fail, no filesystem operations, no network calls.
- Do not migrate, copy, or read legacy implementation code from `2_project_asset/` or the legacy source root.
- Do not read project-level raw assets under `2_project_asset/`. If raw project assets are needed, stop and request a predecessor digestion task.
- Keep the skeleton dependency-free except for `setuptools`/`hatchling` build requirements.
- The `main.py` file identified by T-007 as historical/incomplete must not appear in this skeleton.

## Forbidden

- Do not copy legacy `code/pxfquery_package/` implementation or any migrated flat asset.
- Do not implement functional query, loader, resolver, index, LLM, or viz behavior.
- Do not install or require runtime dependencies (numpy, pandas, anndata, openai, etc.).
- Do not modify `2_project_asset/`, the migrated flat asset library, or the legacy source root.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| pyproject.toml | task working directory/ | yes |
| Package skeleton with stubs | src/pxfquery/ | yes |
| Import smoke evidence | 4_artifact/2_import_smoke/ | yes |
| Execution script/log | 3_execution/ | yes |
| Completion report | 5_report/completion.md | yes |

## Acceptance Criteria

- `pyproject.toml` exists with name `pxfquery`, minimum Python spec, and build-system declaration.
- `src/pxfquery/` layout exists with all subpackage `__init__.py` files and import-safe stub modules for `core`, `data/loader`, `query/forward`, `query/reverse`, `index/*`, `llm/prompts`, `viz/plots`, and `cli`.
- `python -c "from pxfquery import PxFquery"` succeeds without error.
- No legacy implementation code or flat asset content is present in the skeleton files.
- All outputs are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- If T-007 reports indicate a different canonical package name, stop and request human clarification.
- If any required T-007 artifact cannot be read, stop and report the missing precondition.
- If `pyproject.toml` cannot be built, stop and report the build system constraint.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.
```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-002
    path: 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: "Anchors canonical package name (pxfquery), intended module boundaries (core/data/query/index/llm/viz), and component architecture from legacy development state digest"
  - id: A-002
    source_task: T-007
    source_artifact_id: D-003
    path: 4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv
    reason: "Confirms per-module implementation status to decide which modules need stubs and which are historical/incomplete"
  - id: A-003
    source_task: T-007
    source_artifact_id: D-006
    path: 4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md
    reason: "Provides recommended D001 package setup scope, acceptance criteria, and do-not-do rules"
optional: []
forbidden:
  - path: 2_project_asset/
    reason: forbidden for non-digestion task; request a predecessor digestion task if raw project assets are needed
output:
  - path: 4_artifact/2_import_smoke/
    type: persist
  - path: 4_artifact/1_package/
    type: code
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 2_project_asset/
  - 1_project_init/
```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-044 package_skeleton_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1
- Allowed write dirs: 3_execution/, 4_artifact/, 5_report/
- Forbidden dirs: predecessor task directories, 2_project_asset/, 1_project_init/, legacy source root
- Required registry: 4_artifact/registry.yaml (update with outputs after delivery)
- Must stop if:
  - T-007 reports indicate a different canonical package name than `pxfquery`
  - Any required T-007 artifact (A-001, A-002, A-003) cannot be read
  - pyproject.toml cannot be built

## Objective Restatement

Create the clean M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, minimal metadata, import-safe stubs, and import smoke evidence. Anchor package name `pxfquery` and module boundaries (`core`, `data`, `query`, `index`, `llm`, `viz`, `cli`) in T-007 development state report. Do not migrate legacy implementation code and do not implement query behavior beyond import-safe stubs. This skeleton is the bottom-layer asset that later tasks will populate with actual loader, query, CLI, and resolver logic.

## Selected Inputs

| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 (T-007/D-002) | .../T-007/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Anchors canonical package name (pxfquery), intended module boundaries (core/data/query/index/llm/viz), and component architecture | ok |
| A-002 (T-007/D-003) | .../T-007/4_artifact/5_table/pxfquery_module_asset_status_matrix_v20260617.csv | Confirms per-module status: which are implemented vs incomplete/historical, guiding stub decisions | ok |
| A-003 (T-007/D-006) | .../T-007/4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md | Provides D001 package setup scope, acceptance criteria, and explicit do-not-do rules | ok |

## Execution Strategy

1. **Read T-007 artifacts (A-001, A-002)** to confirm canonical package name is `pxfquery` and module boundaries are `core`, `data`, `query`, `index`, `llm`, `viz`. Cross-check against A-003 handoff constraints. Stop if package name differs.
2. **Create `pyproject.toml`** at the task working directory with `[build-system]` (hatchling or setuptools), `[project]` (`name = "pxfquery"`, version `0.1.0`, Python `>=3.10`), and `src`-layout package discovery. No runtime dependencies.
3. **Create `src/pxfquery/` directory tree** with `__init__.py` (set `__version__ = "0.1.0"`), import-safe stub modules for `core.py` (class `PxFquery`), `data/loader.py` (class `DataLoader`), `query/forward.py` and `query/reverse.py`, `index/` subpackage, `llm/prompts.py`, `viz/plots.py`, and `cli/__init__.py`. All stubs must have empty method bodies and no external imports.
4. **Run import smoke test** using the pxfquery conda environment: `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python -c "import pxfquery; print(pxfquery.__version__)"` from the package root. Also verify `from pxfquery import PxFquery`.
5. **Record import smoke evidence** as a text file in `4_artifact/2_import_smoke/` with the command used, stdout, and exit code.
6. **Register deliverables** in `4_artifact/registry.yaml` with asset IDs, paths, types, and status.

## Conservative Execution Advice

- Start with: Read A-001 to confirm package name, then create only `pyproject.toml` and `src/pxfquery/__init__.py` first. Run the most minimal import test before creating all stub files.
- Smoke/demo command or method: `python -c "import pxfquery; print(pxfquery.__version__)"` — this validates the package can be found and the version string works before any subpackage imports.
- Full run only after: the minimal import succeeds, then create remaining stubs one subpackage at a time, testing after each.
- Cost/time risk: Negligible — no network calls, no large data reads, no legacy code migration. Expected runtime < 2 minutes.
- Checkpoint advice: After `pyproject.toml` creation, after first successful `import pxfquery`, after full skeleton import test. Save import smoke evidence immediately.

## Expected Deliverables

| Deliverable | Target path | Acceptance signal |
|---|---|---|
| pyproject.toml | task working directory/pyproject.toml | File exists with `name = "pxfquery"`, `requires-python = ">=3.10"`, `[build-system]` table, src-layout package discovery |
| Package skeleton | src/pxfquery/ with all subpackage `__init__.py` and stub modules | `import pxfquery` succeeds; `from pxfquery import PxFquery` succeeds; all subpackage imports succeed (even if stubs are empty) |
| Import smoke evidence | 4_artifact/2_import_smoke/ | File contains the import command output showing version string and successful import |
| Execution script/log | 3_execution/ | Script used to create and test the skeleton |
| Updated registry | 4_artifact/registry.yaml | All deliverables registered with correct paths |
| Completion report | 5_report/completion.md | Documents what was created, what was tested, and any deviations |

## Failure / Stop Conditions

- If A-001/A-002 indicate a canonical package name other than `pxfquery` → stop, request human clarification
- If any required T-007 artifact is unreadable → stop, report missing precondition
- If `pyproject.toml` build fails or `import pxfquery` fails → stop, diagnose and report
- If the pxfquery conda environment is not usable → stop, report environment issue
- Do NOT proceed if any legacy implementation code needs to be read — the task's scope is stubs only

## Notes For Delivery QA

- The T-007 handoff (A-003) recommends D001 "Copy or promote code/pxfquery_package/ into the development phase workspace," but T-044 intentionally scopes narrower: skeleton and stubs only. This is correct per the task's constraint notes. The broader D001 scope belongs to a later task.
- Protocol step 4 says `python -c "import pxfquery; print(pxfquery.__version__)"` — the `__init__.py` must define `__version__` for this to work. If using a different version access pattern, adjust the smoke command accordingly.
- Use the pxfquery conda environment specified in project protocol (`/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`).
- `3_execution/` is currently empty — expected for a pre-execution state. Execution AI should populate it with build scripts and logs.
- The module status matrix (A-002) confirms `cli` is not listed as an existing module but the protocol adds it as a placeholder — this is correct since it's a new skeleton subpackage for future CLI entry points.
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/registry.yaml`

```text
artifacts:
  - id: D-001
    name: package_skeleton_pyproject
    type: config
    path: 4_artifact/1_package/pyproject.toml
    status: accepted
    notes: pyproject.toml with name=pxfquery, version=0.1.0, hatchling build, src-layout, Python>=3.10

  - id: D-002
    name: package_skeleton_src
    type: code
    path: 4_artifact/1_package/pxfquery/
    status: accepted
    notes: src/pxfquery/ package skeleton with core, data, query, index, llm, viz, cli subpackages and import-safe stubs

  - id: D-003
    name: import_smoke_evidence
    type: document
    path: 4_artifact/2_import_smoke/smoke_test_v20260624.txt
    status: accepted
    notes: Import smoke test results — all imports pass, version 0.1.0, no runtime deps

  - id: D-004
    name: execution_log
    type: script
    path: 3_execution/create_skeleton.sh
    status: accepted
    notes: Shell script recording all steps to create the package skeleton

  - id: D-005
    name: execution_report
    type: document
    path: 4_artifact/3_document/execution_report_v20260624.html
    status: accepted
    notes: HTML execution report

  - id: D-006
    name: result_report
    type: document
    path: 4_artifact/3_document/result_report_v20260624.html
    status: accepted
    notes: HTML result report

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/5_report/completion.md`

```text
# Completion — T-044 package_skeleton_m1

Status: **COMPLETED**

## What Was Done

Created the M1 Python package skeleton for PxFquery as a new `src/pxfquery` package with `pyproject.toml`, import-safe stubs, and import smoke evidence.

## Deliverables Produced

| Deliverable | Path | Status |
|---|---|---|
| pyproject.toml | task working directory/ | Delivered |
| Package skeleton | src/pxfquery/ | Delivered |
| Import smoke evidence | 4_artifact/2_import_smoke/smoke_test_v20260624.txt | Delivered |
| Execution script | 3_execution/create_skeleton.sh | Delivered |
| Registry | 4_artifact/registry.yaml | Delivered (6 entries) |
| Execution report | 4_artifact/3_document/execution_report_v20260624.html | Delivered |
| Result report | 4_artifact/3_document/result_report_v20260624.html | Delivered |

## Acceptance Criteria Check

- pyproject.toml with name=pxfquery, hatchling build, Python >=3.10: PASS
- src/pxfquery layout with all subpackages and stubs: PASS
- `python -c "from pxfquery import PxFquery"` succeeds: PASS
- No legacy code present in skeleton: PASS
- All outputs registered in registry.yaml: PASS

## Package Structure Created

```
src/pxfquery/
├── __init__.py          # __version__ = "0.1.0", exports PxFquery
├── core.py              # class PxFquery(config=None)
├── data/
│   ├── __init__.py
│   └── loader.py        # class DataLoader
├── query/
│   ├── __init__.py
│   ├── forward.py       # class ForwardQuery, ForwardResult
│   └── reverse.py       # class ReverseQuery, ReverseResult
├── index/
│   ├── __init__.py
│   ├── cellline_index.py  # class CellLineIndex
│   ├── drug_index.py      # class DrugIndex
│   ├── gene_index.py      # class GeneIndex
│   └── function_index.py  # class FunctionIndex
├── llm/
│   ├── __init__.py
│   └── prompts.py       # 6 prompt builder stub functions
├── viz/
│   ├── __init__.py
│   └── plots.py         # 3 plot function stubs
└── cli/
    └── __init__.py      # placeholder
```

## Constraints Honored

- Package name `pxfquery` confirmed from T-007 assets
- `src/pxfquery` src-layout used
- All stubs are import-safe (no external imports, no IO, no network)
- No legacy code migrated, copied, or read from legacy sources
- No runtime dependencies required
- `main.py` not present
- Did not read `2_project_asset/` or modify predecessor task directories

## Deviations

None. All protocol steps executed as specified.
```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: development
- ID: T-044 | Name: package_skeleton_m1
- Objective: Create the clean M1 Python package skeleton for PxFquery. Use T-007 to anchor package name, module boundaries, and original tool intent. Deliver pyproject.toml, src/pxfquery layout, minimal package metadata, import smoke evidence, and a clear placeholder structure for loader/query/CLI modules. Do not migrate old implementation code here and do not implement query behavior beyond import-safe stubs.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1`

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
# AI Handoff: T-044 package_skeleton_m1

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
# Delivery QA: T-044 package_skeleton_m1

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
