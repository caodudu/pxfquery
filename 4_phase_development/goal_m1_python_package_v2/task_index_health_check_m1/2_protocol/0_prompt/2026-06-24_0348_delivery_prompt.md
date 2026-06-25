# Delivery QA Prompt
Generated: 2026-06-24 03:48

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-045
name: index_health_check_m1
phase: development
goal: goal_m1_python_package_v2
project: P-012
objective: Check the health of M1-relevant indexes before any real loader hardening.
  Use T-021 standard-resource outputs to verify index schema, readability, required
  keys, missing fields, and known gaps for forward/reverse demos. Deliver an index
  health report and machine-readable check summary. This task must not rebuild or
  overwrite authoritative indexes; it may only report minimal patch recommendations.
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
notes: 'Constraint supplement for config AI: This is an audit/check asset, not a rebuild
  task. Verify only M1-relevant index schema, readability, required keys, and gaps
  from T-021. Do not overwrite or regenerate authoritative indexes. Deliver machine-readable
  health summary plus human-readable gap notes. This task supports T-047 hardening
  and should not block the fixture-only M1 path.'
fast_pass_permission: green
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-24T03:33:42'

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/1_asset/registration.yaml`

```text
assets:
- id: T-021/D-004/cellline_index
  name: cellline_index.json
  type: deliverable
  source: T-021
  path: 1_asset/cellline_index.json
  description: M1 valid cell line names catalog
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/cellline_index.json
  symlink: true
  location: local
- id: T-021/D-004/cellline_neighbors
  name: cellline_neighbors.json
  type: deliverable
  source: T-021
  path: 1_asset/cellline_neighbors.json
  description: M1 lineage-based cell grouping
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/cellline_neighbors.json
  symlink: true
  location: local
- id: T-021/D-004/cellline_tree
  name: cellline_tree.json
  type: deliverable
  source: T-021
  path: 1_asset/cellline_tree.json
  description: M1 cell line ontology tree
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/cellline_tree.json
  symlink: true
  location: local
- id: T-021/D-004/drug_index
  name: drug_index.json
  type: deliverable
  source: T-021
  path: 1_asset/drug_index.json
  description: M1 drug alias to BRD-id lookup index
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/drug_index.json
  symlink: true
  location: local
- id: T-021/D-004/drug_neighbors
  name: drug_neighbors.json
  type: deliverable
  source: T-021
  path: 1_asset/drug_neighbors.json
  description: M1 drug similarity neighbor graph
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/drug_neighbors.json
  symlink: true
  location: local
- id: T-021/D-004/gene_index_simple
  name: gene_index_simple.json
  type: deliverable
  source: T-021
  path: 1_asset/gene_index_simple.json
  description: M1 gene symbol-to-type compact index
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_index_simple.json
  symlink: true
  location: local
- id: T-021/D-004/gene_neighbors_simple
  name: gene_neighbors_simple.json
  type: deliverable
  source: T-021
  path: 1_asset/gene_neighbors_simple.json
  description: M1 gene semantic neighbor graph (compact)
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_neighbors_simple.json
  symlink: true
  location: local
- id: T-021/D-004/gene_index
  name: gene_index.json
  type: deliverable
  source: T-021
  path: 1_asset/gene_index.json
  description: M1 full gene lookup index
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_index.json
  symlink: true
  location: local
- id: T-021/D-004/gene_neighbors
  name: gene_neighbors.json
  type: deliverable
  source: T-021
  path: 1_asset/gene_neighbors.json
  description: M1 full gene semantic neighbor graph
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/gene_neighbors.json
  symlink: true
  location: local
- id: T-021/D-004/function_index
  name: function_index.json
  type: deliverable
  source: T-021
  path: 1_asset/function_index.json
  description: M1 function term catalog (91 terms, rebuilt by T-021)
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/function_index.json
  symlink: true
  location: local
- id: T-021/D-004/data_description
  name: data_description.yaml
  type: deliverable
  source: T-021
  path: 1_asset/data_description.yaml
  description: M1 asset metadata reference for interpreting index fields
  readonly: true
  origin: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/data_description.yaml
  symlink: true
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/2_protocol/2_protocol_split/protocol.md`

```text
# task_index_health_check_m1 — Protocol

## Objective

Check the health of M1-relevant query indexes from T-021 standard resources before real loader hardening (T-047). Verify index schema, readability, required keys, missing fields, and known gaps for forward/reverse demos. Deliver an index health report and machine-readable check summary. Must not rebuild or overwrite authoritative indexes; may only report minimal patch recommendations.

This is an audit/check asset, not a rebuild task. T-045 supports T-047 (resource_loader_hardening_m1) and must not block the fixture-only M1 path.

## Steps

### Step 1 — Load and inspect required core indexes
- Read `cellline_index.json`, `drug_index.json`, `gene_index.json`, `function_index.json` using Python
- Verify each is valid JSON and parseable
- Record file size, top-level type (array/object), and rough element count
- Output: per-index schema summary in `3_execution/step1_core_schema_summary.json`

### Step 2 — Validate M1-required keys for each core index
- cellline_index: check for valid cell line name list
- drug_index: check for drug alias → BRD-id mapping keys
- gene_index: check for gene symbol lookup keys and type annotation
- function_index: check for 91 function terms (50 Hallmark + 41 3CA MPS) and term-to-id mapping
- Report any structural anomalies (null keys, duplicate keys, malformed values)
- Output: `3_execution/step2_key_validation.json`

### Step 3 — Inspect optional neighbor/tree indexes for forward/reverse query fitness
- Read cellline_neighbors.json, cellline_tree.json, drug_neighbors.json, gene_neighbors.json, gene_neighbors_simple.json, gene_index_simple.json
- Verify neighbor graphs have expected edge cardinality (non-empty for major entities)
- Verify cellline_tree is a valid tree structure
- Report any missing or degenerate graphs that would break proxy-matching in forward/reverse queries
- Output: `3_execution/step3_neighbor_health.json`

### Step 4 — Cross-reference index coverage with M1 demo requirements
- Consult T-042 contract or T-042 demo cases for expected entity types (drug, gene, cell line, function term)
- Check whether the indexes cover the entity types needed for forward query (perturbation + context → function) and reverse query (function + context → perturbation)
- Identify index-to-demo gaps: entities present in demo case but missing from index
- Output: `3_execution/step4_coverage_gap.json`

### Step 5 — Generate machine-readable health summary
- Produce `4_artifact/2_persist/index_health_summary.json` with:
  - per-index schema status (valid/invalid/warning)
  - per-index key completeness score
  - per-index size in bytes and element count
  - known gaps list
  - patch recommendations (if any minimal fixes are safe)
- Output: `4_artifact/2_persist/index_health_summary.json`

### Step 6 — Generate human-readable health report
- Produce `4_artifact/2_persist/index_health_report.md` summarizing:
  - which indexes pass, which have warnings, which block M1 use
  - key findings for T-047 (loader hardening)
  - advice on whether fixture path alone is sufficient or real indexes are M1-ready
- Output: `4_artifact/2_persist/index_health_report.md`

### Step 7 — Write gap notes for human review
- Produce `4_artifact/3_document/gap_notes.md` with:
  - human-readable narrative of each gap
  - affected M1 demo case (forward/reverse)
  - severity (blocker / warning / cosmetic)
  - suggested resolution path (e.g. patch index, adjust demo, accept gap)
- Output: `4_artifact/3_document/gap_notes.md`

## Deliverables

| Path | Type | Description |
|------|------|-------------|
| `4_artifact/2_persist/index_health_summary.json` | deliverable | Machine-readable index health summary with per-index schema, key completeness, size, gaps, and patch recommendations |
| `4_artifact/2_persist/index_health_report.md` | deliverable | Human-readable health report with pass/warn/block per index and T-047 handoff advice |
| `4_artifact/3_document/gap_notes.md` | support | Human-readable gap narrative with severity, affected demo case, and resolution path |
```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - T-021/D-004/cellline_index
  - T-021/D-004/drug_index
  - T-021/D-004/gene_index
  - T-021/D-004/function_index
  - T-021/D-004/data_description

optional:
  - T-021/D-004/cellline_neighbors
  - T-021/D-004/cellline_tree
  - T-021/D-004/drug_neighbors
  - T-021/D-004/gene_index_simple
  - T-021/D-004/gene_neighbors_simple
  - T-021/D-004/gene_neighbors

forbidden:
  - /Users/dudu/Documents/3_Project/8_functional_query
  - /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/*.h5ad
  - /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/*.csv

output:
  - 4_artifact/2_persist/index_health_report.md
  - 4_artifact/2_persist/index_health_summary.json
  - 4_artifact/3_document/gap_notes.md

modifiable: []

non_modifiable:
  - T-021/D-004/*
```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-045 index_health_check_m1

## Check Verdict
yellow_repair

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: T-021 standard_resources (read-only), legacy source root `/Users/dudu/Documents/3_Project/8_functional_query`, raw `2_project_asset/`, any `.h5ad` or `.csv` in T-021 standard_resources
- Required registry: `1_asset/registration.yaml` (repaired), `2_protocol/3_asset_rule/asset_rule.yaml` (repaired)
- Must stop if: any required T-021 index is unreadable, function_index.json has != 91 terms, a core index is missing M1-forward/reverse required keys, or index corruption prevents valid JSON parsing

## Objective Restatement
Audit the 10 M1-relevant query indexes from T-021's standard-resource output (D-004). Verify JSON schema validity, required keys for forward/reverse query demos, neighbor graph completeness, and coverage gaps against M1 demo cases. Produce machine-readable health summary + human-readable report + gap notes. Do not modify any index; only report and recommend patches. This is input for T-047 loader hardening.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| T-021/D-004/cellline_index | standard_resources/cellline_index.json | Core index for cell line name validation in queries | required (3.5 KB, exists) |
| T-021/D-004/drug_index | standard_resources/drug_index.json | Core index for drug alias → BRD-id resolution | required (176 KB, exists) |
| T-021/D-004/gene_index | standard_resources/gene_index.json | Core index for gene symbol lookup and type | required (6.1 MB, exists) |
| T-021/D-004/function_index | standard_resources/function_index.json | Core index for function term catalog (91 terms) | required (17 KB, exists) |
| T-021/D-004/data_description | standard_resources/data_description.yaml | Field-level index semantics reference | required (5 KB, exists) |
| T-021/D-004/cellline_neighbors | standard_resources/cellline_neighbors.json | Optional: lineage-based cell grouping for proxy matches | optional (6.5 KB, exists) |
| T-021/D-004/cellline_tree | standard_resources/cellline_tree.json | Optional: cell line ontology tree for reverse query context expansion | optional (49 KB, exists) |
| T-021/D-004/drug_neighbors | standard_resources/drug_neighbors.json | Optional: drug similarity graph for proxy perturbation matching | optional (4.4 MB, exists) |
| T-021/D-004/gene_index_simple | standard_resources/gene_index_simple.json | Optional: compact gene symbol-to-type index | optional (356 KB, exists) |
| T-021/D-004/gene_neighbors | standard_resources/gene_neighbors.json | Optional: full gene semantic neighbor graph | optional (21.8 MB, exists) |
| T-021/D-004/gene_neighbors_simple | standard_resources/gene_neighbors_simple.json | Optional: compact gene semantic neighbor graph | optional (19.5 MB, exists) |

## Execution Strategy
1. **Load required core indexes** — Python read cellline_index, drug_index, gene_index, function_index, and data_description.yaml. Verify valid JSON/YAML parse. Record top-level type, schema shape, and element count per index. Write `3_execution/step1_core_schema/step1_core_schema_summary.json`.
2. **Validate M1-required keys** — For each core index, check: cellline_index has valid name list; drug_index has alias→BRD-id bidirectional mapping; gene_index has symbol→type lookup; function_index has exactly 91 terms with id/name/category fields. Report anomalies (nulls, duplicates, malformed). Write `3_execution/step2_key_validation/step2_key_validation.json`.
3. **Inspect optional neighbor/tree indexes** — Load cellline_neighbors, cellline_tree, drug_neighbors, gene_neighbors (simple+full), gene_index_simple. Check: neighbor graphs have non-empty edges for major entities; cellline_tree is valid tree structure. Flag empty/degenerate graphs that would break proxy matching. Write `3_execution/step3_neighbor_health/step3_neighbor_health.json`.
4. **Cross-reference with M1 demo requirements** — Compare index entity coverage against forward-query needs (perturbation→function) and reverse-query needs (function→perturbation). Use T-042 contract demo cases if accessible via standard resource references; otherwise flag as coverage-gap-tbd. Write `3_execution/step4_coverage_gap/step4_coverage_gap.json`.
5. **Produce machine-readable health summary** — Consolidate steps 1-4 into `4_artifact/2_persist/index_health_summary.json` with per-index status (valid/warning/invalid), key completeness, size/element counts, gap list, and patch recommendations.
6. **Produce human-readable health report** — Write `4_artifact/2_persist/index_health_report.md` with pass/warning/block per index, T-047 handoff advice, and verdict on fixture-only vs real-index readiness.
7. **Write gap notes** — Produce `4_artifact/3_document/gap_notes.md` with human-readable gap narrative, severity, affected demo case, and resolution path.

## Conservative Execution Advice
- **Start with:** step 1 — load just `function_index.json` (smallest required core index, 17 KB) to verify JSON parse and schema shape before loading the 6 MB gene_index or 21 MB neighbor graphs
- **Smoke/demo command or method:** `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python -c "import json; d=json.load(open('...standard_resources/function_index.json')); print(type(d), len(d) if isinstance(d, (dict,list)) else 'scalar', list(d.keys())[:5] if isinstance(d, dict) else '')"`
- **Full run only after:** all 4 required core indexes pass JSON parse and have non-empty, well-structured content
- **Cost/time risk:** very low — all indexes are local JSON/YAML under ~330 MB total; no network, no API, no compute-heavy operations. Largest file is gene_neighbors.json at 21.8 MB, parseable in seconds
- **Checkpoint advice:** after step 2 (key validation) — if core indexes are structurally valid, the task is ~60% done and the rest is optional-inspection + report-writing. If any core index is corrupt, stop and write incomplete-gap into summary

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| index_health_summary.json | `4_artifact/2_persist/index_health_summary.json` | Valid JSON with per-index schema status, key completeness, element counts, gap list, patch recommendations for all 4 required + up to 6 optional indexes |
| index_health_report.md | `4_artifact/2_persist/index_health_report.md` | Clear pass/warn/block per index; explicit T-047 handoff sentence; fixture-only vs real-index M1 readiness verdict |
| gap_notes.md | `4_artifact/3_document/gap_notes.md` | Each gap has severity, affected demo case, and resolution path. No gap should be listed without a severity label |

## Failure / Stop Conditions
- Any required core index (cellline_index, drug_index, gene_index, function_index) fails JSON parse →

...[truncated by CyHex prompt assembler: 952 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/4_artifact/registry.yaml`

```text
artifacts:
  - id: T-045/D-001/index_health_summary
    name: index_health_summary.json
    type: deliverable
    path: 4_artifact/2_persist/index_health_summary.json
    description: Machine-readable index health summary with per-index schema, key completeness, size, gaps, and patch recommendations
    created: '2026-06-24'

  - id: T-045/D-002/index_health_report
    name: index_health_report.md
    type: deliverable
    path: 4_artifact/2_persist/index_health_report.md
    description: Human-readable health report with pass/warn/block per index and T-047 handoff advice
    created: '2026-06-24'

  - id: T-045/D-003/gap_notes
    name: gap_notes.md
    type: support
    path: 4_artifact/3_document/gap_notes.md
    description: Human-readable gap narrative with severity, affected demo case, and resolution path
    created: '2026-06-24'

  - id: T-045/D-004/execution_report
    name: execution_report_v20260624.html
    type: report
    path: 4_artifact/3_document/execution_report_v20260624.html
    description: Execution report documenting steps performed
    created: '2026-06-24'

  - id: T-045/D-005/result_report
    name: result_report_v20260624.html
    type: report
    path: 4_artifact/3_document/result_report_v20260624.html
    description: Result report with per-index health status and M1 readiness verdict
    created: '2026-06-24'

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/5_report/completion.md`

```text
# Completion — T-045 index_health_check_m1

**Status:** completed  
**Completed:** 2026-06-24  
**Executor:** AGT-002 (CyHex execution agent)

## Completed Steps

1. ✅ **Step 1** — Loaded and inspected 4 core indexes (cellline, drug, gene, function) — all valid JSON
2. ✅ **Step 2** — Validated M1-required keys: cellline (240 names), drug (5,958 entries, 98%+ BRD), gene (78,061 entries, 3 fields), function (91 terms, non-standard structure), data_description (valid YAML)
3. ✅ **Step 3** — Inspected 6 optional neighbor/tree indexes — all valid; neighbor graphs have uniform 50-edge cardinality; cellline_tree is flat (not hierarchical)
4. ✅ **Step 4** — Cross-referenced with T-013 demo evidence (T-042 not yet executed). All expected demo entities (EGFR, A549, HALLMARK_APOPTOSIS, HALLMARK_MYC_TARGETS_V1) present in indexes. 6 structural gaps identified.
5. ✅ **Step 5** — Generated `index_health_summary.json`
6. ✅ **Step 6** — Generated `index_health_report.md`
7. ✅ **Step 7** — Generated `gap_notes.md`

## Deliverables Produced

| Deliverable | Path | Status |
|---|---|---|
| index_health_summary.json | `4_artifact/2_persist/index_health_summary.json` | ✓ |
| index_health_report.md | `4_artifact/2_persist/index_health_report.md` | ✓ |
| gap_notes.md | `4_artifact/3_document/gap_notes.md` | ✓ |
| execution_report_v20260624.html | `4_artifact/3_document/execution_report_v20260624.html` | ✓ |
| result_report_v20260624.html | `4_artifact/3_document/result_report_v20260624.html` | ✓ |

## Registry

Artifact registry updated: `4_artifact/registry.yaml`

## Execution Report

`4_artifact/3_document/execution_report_v20260624.html`

## Result Report

`4_artifact/3_document/result_report_v20260624.html`

## Validation Performed

- All 10 indexes validated: JSON parse, schema shape, element counts
- Key completeness scores computed per index
- Neighbor graphs checked for empty/missing edges
- Entity coverage checked against T-013 historical demo entities
- `index_health_summary.json` validated as parseable JSON

## Caveats

- T-042 (contract_and_demo_spec_m1) has not been executed — coverage gap analysis uses T-013 historical evidence as proxy. Re-check when actual T-042 demo cases exist.
- function_index.json has non-standard structure (dict with meta/var_names/aliases) — loaders must unwrap before use.
- cellline_tree.json is flat, not hierarchical — proxy expansion via ontology not available without rebuild.

## T-047 Handoff

**Verdict: M1-ready.** All indexes valid. 4 warnings (non-blocking). No fixture-only path needed — real indexes are ready for loader hardening.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: development
- ID: T-045 | Name: index_health_check_m1
- Objective: Check the health of M1-relevant indexes before any real loader hardening. Use T-021 standard-resource outputs to verify index schema, readability, required keys, missing fields, and known gaps for forward/reverse demos. Deliver an index health report and machine-readable check summary. This task must not rebuild or overwrite authoritative indexes; it may only report minimal patch recommendations.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1`

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
# AI Handoff: T-045 index_health_check_m1

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
# Delivery QA: T-045 index_health_check_m1

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
