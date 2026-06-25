# Execution Prompt
Generated: 2026-06-25 13:10

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

## Functional Delivery Goal

PxFquery's project-level functional goal is not limited to static matrix lookup. A project-valid package must preserve the intended user-facing query experience:

- forward query: perturbation and biological context to functional response;
- reverse query: functional target and biological context to candidate perturbations;
- resolver-mediated natural-language or semi-structured query entry;
- exact, proxy, and not-found evidence routing for sparse biological coverage;
- LLM-assisted parsing and summarization through the current configured AI service when a milestone requires the user-facing resolver layer;
- deterministic fallback and transparent evidence metadata when LLM or proxy routing fails.

Milestones may stage these capabilities in layers, but a milestone may not silently redefine PxFquery as only deterministic dictionary or matrix lookup if the user-defined milestone requires resolver, LLM, proxy, or transfer behavior. Any proposed scope reduction, deferral, or optionalization of a functional capability must be explicitly reported to the user before task creation and must receive user approval.

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

- Functional delivery expectations take priority over convenience-driven scope reduction. If the user defines a milestone as requiring resolver, LLM, proxy routing, natural-language entry, or transfer/fallback behavior, those capabilities remain in scope until the user explicitly approves a change.
- Keep scope pragmatic in implementation method: prioritize working code, traceable evidence, manuscript-grade results, and clear provenance over broad platform claims. Pragmatism does not authorize removing required user-facing capabilities from a milestone.
- Do not overstate LLM or agent capabilities in manuscript claims or external positioning. This claim-control rule does not mean LLM/resolver functions are optional in development deliverables when they are part of the project or milestone goal.
- Deterministic indexes and evidence retrieval are an important scientific foundation, but they do not replace resolver, LLM-assisted parsing/summarization, exact/proxy/not-found routing, or user-facing query transfer behavior when those are expected capabilities.
- Treat Genes as a pragmatic graduation target with a relatively low acceptance bar compared with high-impact bioinformatics venues; do not design tasks as if the project must satisfy Bioinformatics, Nature-family, or top-tier computational biology expectations.
- Favor work that appears substantial in figures, tables, workflow steps, coverage summaries, and case-study evidence while staying lightweight enough to finish quickly.
- Prefer simple, readable, Genes-like manuscript logic over technically ambitious novelty claims.
- When choosing between a clever but hard-to-explain method and a familiar Genes-style analysis pattern, prefer the familiar and explainable pattern unless the task explicitly requires innovation.
- Separate hard constraints from soft working preferences so future tasks can follow rules without inheriting unnecessary commentary.

## Milestone Scope Control

- A milestone is defined by the user's stated deliverable goal, not by the easiest subset of features to implement.
- Task decomposition, DAG parallelism, green/yellow/red fast-pass labels, `must`/`may` gates, and bypass repair tasks are tools for preserving the target deliverable while managing risk. They must not be used to quietly shrink the deliverable.
- If a task or agent proposes moving a required capability to a later milestone, marking it optional, replacing it with a deterministic fallback, or accepting a partial substitute, that is a scope downgrade. It must be surfaced as a user decision before the DAG or task is created.
- Fallback behavior is valid only as explicit runtime behavior and evidence. It cannot be counted as delivery of the primary LLM/resolver capability unless the milestone explicitly says fallback-only is acceptable.
- After each package milestone, create or run a review against the project capability anchor to state which anchored capabilities are delivered, partial, missing, downgraded, or deferred, and whether any deferral was user-approved.

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-063
name: llm_resolver_capability_anchor
phase: digestion
goal: goal_project_delivery_anchor
project: P-012
objective: Create the LLM/resolver capability anchor for future PxFquery package milestones.
  Specify user-facing natural-language/semi-structured query behavior, CyHex-configured
  AI service use, exact/proxy/not-found handoff with LLM assistance, fallback semantics,
  demo cases, and acceptance evidence for M3-level resolver delivery.
executor: hybrid
agent_id: AGT-001
config_agent_id: AGT-001
check_agent_id: AGT-001
execute_agent_id: AGT-001
server_id: null
status: active
cyhex_version: 1.2.20
milestone_id: ''
milestone_final: false
created: '2026-06-25'
started: null
completed: null
notes: Do not implement API code; produce a functional design and acceptance anchor.
  | LLM capability is required when a milestone includes user-facing resolver. Current
  desired model route is CyHex-registered AI address, deepseek-v4-pro unless a later
  task explicitly changes it.
fast_pass_permission: green
sub_status: check_approved
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-25T13:10:01'

```

### Current Task Orchestration Input: orchestration_input.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/2_protocol/1_meta_info/orchestration_input.yaml`

```text
delivery_goal: LLM/resolver capability design anchor for future PxFquery milestones,
  especially M3.
predecessor_tasks:
- task_id: T-007
  gate: must
  reason: Trusted development-state source for intended resolver and query-entry behavior.
- task_id: T-013
  gate: must
  reason: MVP gap/review evidence about missing resolver/NL/LLM behavior.
- task_id: T-061
  gate: must
  reason: Clean replacement source digest for legacy source boundaries and resolver-related
    source hints.
- task_id: T-062
  gate: must
  reason: Overall algorithm-package anchor defines where LLM/resolver fits in the
    capability hierarchy.
reference_tasks:
- task_id: T-033
  reason: Historical blocked resolver attempt; reference only as failure/anti-pattern.
- task_id: T-034
  reason: Historical blocked LLM adapter attempt; reference only as failure/anti-pattern.
supplemental_notes:
- Do not implement API code; produce a functional design and acceptance anchor.
- LLM capability is required when a milestone includes user-facing resolver. Current
  desired model route is CyHex-registered AI address, deepseek-v4-pro unless a later
  task explicitly changes it.
- Fallback is runtime behavior and evidence, not proof that primary LLM/resolver capability
  is delivered.
suggested_agent:
  strength: strong
  reason: Prior planning mistakenly downgraded LLM/resolver.

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: t007_development_source_map
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-001
  origin: T-007/D-001
  registered: '2026-06-25'
  path: 1_asset/t007_development_source_map.md
  symlink: true
  status: ready
  notes: Trusted source map for interpreting migrated PxFquery development assets
    and resolver-related source authority.
  location: local
- id: A-002
  name: t007_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002
  registered: '2026-06-25'
  path: 1_asset/t007_development_state_report.md
  symlink: true
  status: ready
  notes: Summarizes intended product scope, implemented components, data/index readiness,
    validation state, and development interpretation.
  location: local
- id: A-003
  name: t007_development_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005
  registered: '2026-06-25'
  path: 1_asset/t007_development_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: Carries forward known resolver, validation, claim, and development risks.
  location: local
- id: A-004
  name: t013_mvp_capability_contract
  type: document
  source: predecessor
  source_task: T-013
  source_artifact_id: D-001
  origin: T-013/D-001
  registered: '2026-06-25'
  path: 1_asset/t013_mvp_capability_contract.md
  symlink: true
  status: ready
  notes: Defines reviewed MVP capability expectations and boundaries relevant to resolver
    acceptance.
  location: local
- id: A-005
  name: t013_capability_status_matrix
  type: table
  source: predecessor
  source_task: T-013
  source_artifact_id: D-003
  origin: T-013/D-003
  registered: '2026-06-25'
  path: 1_asset/t013_capability_status_matrix.csv
  symlink: true
  status: ready
  notes: Capability status evidence showing which MVP behaviors passed, failed, were
    partial, or blocked.
  location: local
- id: A-006
  name: t013_failure_missing_capability_list
  type: document
  source: predecessor
  source_task: T-013
  source_artifact_id: D-005
  origin: T-013/D-005
  registered: '2026-06-25'
  path: 1_asset/t013_failure_missing_capability_list.md
  symlink: true
  status: ready
  notes: Identifies missing resolver/natural-language/LLM behaviors and runtime blockers
    that the anchor must address.
  location: local
- id: A-007
  name: t061_legacy_source_digest
  type: document
  source: predecessor
  source_task: T-061
  source_artifact_id: D-001
  origin: T-061/D-001
  registered: '2026-06-25'
  path: 1_asset/t061_legacy_source_digest.md
  symlink: true
  status: ready
  notes: Bounded source digest for legacy package modules, resolver-related source
    hints, and reuse classifications.
  location: local
- id: A-008
  name: t061_legacy_reference_boundaries
  type: document
  source: predecessor
  source_task: T-061
  source_artifact_id: D-003
  origin: T-061/D-003
  registered: '2026-06-25'
  path: 1_asset/t061_legacy_reference_boundaries.yaml
  symlink: true
  status: ready
  notes: Machine-readable boundary rules for citing or adapting source-digest findings
    without expanding legacy reads.
  location: local
- id: A-009
  name: t062_algorithm_package_delivery_anchor
  type: document
  source: predecessor
  source_task: T-062
  source_artifact_id: T062-A-001
  origin: T-062/T062-A-001
  registered: '2026-06-25'
  path: 1_asset/t062_algorithm_package_delivery_anchor.yaml
  symlink: true
  status: ready
  notes: Primary package capability anchor that places resolver/LLM behavior in the
    overall milestone hierarchy.
  location: local
- id: A-010
  name: t062_algorithm_capability_matrix
  type: table
  source: predecessor
  source_task: T-062
  source_artifact_id: T062-A-002
  origin: T-062/T062-A-002
  registered: '2026-06-25'
  path: 1_asset/t062_algorithm_capability_matrix.csv
  symlink: true
  status: ready
  notes: Capability-to-evidence matrix to align resolver acceptance criteria with
    package-level review.
  location: local
- id: A-011
  name: t062_algorithm_downgrade_rules
  type: document
  source: predecessor
  source_task: T-062
  source_artifact_id: T062-A-003
  origin: T-062/T062-A-003
  registered: '2026-06-25'
  path: 1_asset/t062_algorithm_downgrade_rules.md
  symlink: true
  status: ready
  notes: Defines fallback versus downgrade rules that this resolver-specific anchor
    must inherit.
  location: local
- id: A-012
  name: t062_milestone_review_rubric
  type: document
  source: predecessor
  source_task: T-062
  source_artifact_id: T062-A-004
  origin: T-062/T062-A-004
  registered: '2026-06-25'
  path: 1_asset/t062_milestone_review_rubric.md
  symlink: true
  status: ready
  notes: Evidence hierarchy and review procedure for future M3-level resolver acceptance.
  location: local
- id: A-013
  name: t062_milestone_classification_vocabulary
  type: document
  source: predecessor
  source_task: T-062
  sourc

...[truncated by CyHex prompt assembler: 344 chars omitted]
```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/2_protocol/2_protocol_split/protocol.md`

```text
# T-063 llm_resolver_capability_anchor — Protocol

## Objective

Create the task-level LLM/resolver capability anchor for future PxFquery package milestones, especially M3-level resolver delivery. The task must define the user-facing natural-language and semi-structured query behavior, CyHex-configured AI service use, exact/proxy/not-found handoff with LLM assistance, fallback semantics, demo cases, and acceptance evidence. It must not implement API code or run package tests.

## Position In Project

This is a digestion/governance task under `goal_project_delivery_anchor`. It refines the T-062 algorithm-package delivery anchor for the specific resolver/LLM layer so later package milestones cannot count deterministic matrix lookup alone as delivery of user-facing resolver behavior when resolver capability is in scope.

The anchor should preserve the project-defined capability shape:

- forward query: biological context plus perturbation to functional response;
- reverse query: desired function plus biological context to candidate perturbations;
- natural-language or semi-structured query entry;
- resolver-mediated exact, proxy, and not-found evidence routing;
- LLM-assisted parsing and summarization through the current CyHex-configured AI service route, currently deepseek-v4-pro unless a later task explicitly changes it;
- deterministic fallback and transparent evidence metadata when LLM, proxy routing, or coverage fails.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Trusted source map for migrated PxFquery development assets and resolver-related source authority. |
| A-002 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Intended product scope and matrix/index/resolver design interpretation. |
| A-003 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Known resolver, validation, and claim risks. |
| A-004 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Reviewed MVP capability expectations and boundaries. |
| A-005 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Capability status evidence for passed, partial, blocked, failed, and missing behavior. |
| A-006 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Missing resolver, natural-language, LLM, and runtime-index behaviors that must not be silently downgraded. |
| A-007 | T-061 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Bounded source digest for legacy package modules and resolver-related source hints. |
| A-008 | T-061 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Boundary rules for citing or adapting T-061 findings. |
| A-009 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | Package-level capability anchor to refine for resolver delivery. |
| A-010 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | Capability-to-evidence matrix for milestone acceptance alignment. |
| A-011 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Rules distinguishing runtime fallback from unapproved scope downgrade. |
| A-012 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Evidence hierarchy and review procedure for future package milestones. |
| A-013 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | Classification vocabulary for delivered, partial, blocked, failed, downgraded, deferred, and evidence-insufficient states. |

## Execution Steps

1. Read the registered inputs and extract only the resolver-relevant capability requirements, existing gaps, source-boundary rules, downgrade rules, and acceptance vocabulary.
2. Define the expected M3-level user-facing resolver behavior for natural-language and semi-structured query entry, including required input fields, supported ambiguity handling, structured parse output, evidence metadata, and user-facing summary behavior.
3. Specify the CyHex-configured AI service requirement: future resolver milestones that claim LLM capability must route through the current CyHex-registered AI address and currently desired `deepseek-v4-pro` model route unless a later task explicitly changes that route.
4. Define exact, proxy, and not-found resolver routing semantics, including how LLM assistance may parse, normalize, explain, or summarize but must not fabricate matrix evidence.
5. Define fallback semantics for unavailable LLM service, parse failure, proxy failure, missing indexes, unsupported cell lines, unsupported perturbations, unsupported functions, and low-confidence matches. Mark fallback as runtime behavior and evidence, not proof that primary LLM/resolver delivery is complete.
6. Create a demo case catalog with concrete required case types for future M3 acceptance: exact forward query, exact reverse query, proxy forward query, proxy reverse query, not-found query, ambiguous natural-language query, semi-structured query, LLM-service-unavailable fallback, and evidence-metadata inspection.
7. Create an acceptance matrix mapping each resolver capability to required evidence, minimum acceptable behavior, disallowed substitutes, failure labels, and review status vocabulary inherited from T-062.
8. Write a machine-readable resolver capability anchor YAML and a concise human-readable functional design Markdown document.
9. Write required execution and result reports, and register all accepted/reusable outputs in the current task artifact registry.

## Constraints

- This is a design and acceptance-anchor task only.
- Use selected predecessor artifacts and project protocol context; do not perform implementation, runtime tests, raw-data analysis, web search, or manuscript writing.
- Treat T-062 as the package-level anchor and make this task a resolver-specific refinement, not a competing replacement.
- Preserve the difference between conservative manuscript claims and development delivery scope: conservative claims do not make LLM/resolver functions optional when a milestone includes them.
- Require transparent provenance and evidence metadata for exact, proxy, fallback, and not-found outcomes.
- Treat LLM output as parsing/summarization/normalization assistance, not as independent biological evidence.
- Make any proposed deferral, optionalization, or fallback-only acceptance of required resolver behavior visible as a downgrade requiring explicit user approval.

## Forbidden

- Do not implement or modify package/API/source code.
- Do not run package workflows, tests, notebooks, matrix inspection, or biological analysis.
- Do not read or modify legacy source roots.
- Do not browse predecessor task directories beyond registered assets and allowed handoff/report files.
- Do not create final project deliverables under `6_project_deliverable/`.
- Do not call downstream CyHex prompt endpoints.
- Do not use web search.

## Web Search Allowance

Allowed: no

Reason: The current task is a project-internal capability and acceptance anchor. The required information is availab

...[truncated by CyHex prompt assembler: 3127 chars omitted]
```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md
    reason: Trusted source map for migrated PxFquery development assets and resolver-related source authority.
  - id: A-002
    source_task: T-007
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: Describes intended product scope and the matrix/index/resolver design interpretation.
  - id: A-003
    source_task: T-007
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: Carries forward resolver, validation, and claim risks that the anchor must address.
  - id: A-004
    source_task: T-013
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md
    reason: Defines reviewed MVP capability expectations and boundaries relevant to resolver acceptance.
  - id: A-005
    source_task: T-013
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv
    reason: Provides capability status evidence for pass, partial, blocked, failed, and missing behaviors.
  - id: A-006
    source_task: T-013
    source_artifact_id: D-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md
    reason: Identifies missing resolver, natural-language, LLM, and runtime-index behaviors.
  - id: A-007
    source_task: T-061
    source_artifact_id: D-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_source_digest_repair_m1.md
    reason: Bounded source digest for legacy package modules and resolver-related source hints.
  - id: A-008
    source_task: T-061
    source_artifact_id: D-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml
    reason: Boundary rules for citing/adapting T-061 source-digest findings.
  - id: A-009
    source_task: T-062
    source_artifact_id: T062-A-001
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml
    reason: Primary package-level capability anchor that this resolver-specific anchor must refine.
  - id: A-010
    source_task: T-062
    source_artifact_id: T062-A-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv
    reason: Capability-to-evidence matrix for aligning resolver acceptance with package milestones.
  - id: A-011
    source_task: T-062
    source_artifact_id: T062-A-003
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md
    reason: Rules distinguishing valid runtime fallback from unapproved scope downgrade.
  - id: A-012
    source_task: T-062
    source_artifact_id: T062-A-004
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md
    reason: Evidence hierarchy and review procedure for future resolver-capability acceptance.
  - id: A-013
    source_task: T-062
    source_artifact_id: T062-A-005
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml
    reason: Classification vocabulary for delivered, partial, blocked, failed, downgraded, deferred, out-of-scope, and evidence-insufficient states.
optional:
  - id: O-001
    source_task: T-061
    source_artifact_id: D-002
    path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/5_table/legacy_module_reuse_matrix_repair_m1.csv
    reason: Optional module-level support if execution needs finer-grained resolver source hints.
forbidden:
  - predecessor task directory browsing beyond registered assets and listed handoff/report files
  - downstream prompt endpoints
  - package source implementation or modification
  - raw matrix/data analysis
  - legacy source root reads unless a future task explicitly registers and justifies them
  - final project deliverable directory modifications
output:
  - path: 4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml
    type: yaml
  - path: 4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md
    type: document
  - path: 4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix

...[truncated by CyHex prompt assembler: 473 chars omitted]
```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-063 llm_resolver_capability_anchor

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories except registered asset symlinks/paths, legacy source root `/Users/dudu/Documents/3_Project/8_functional_query`, `1_project_init/`, `2_project_asset/`, `6_project_deliverable/`
- Required registry: `1_asset/registration.yaml`
- Must stop if: required registered assets become unavailable; defining the anchor would require code implementation, package tests, raw matrix/data analysis, web search, direct legacy-root reads, downstream prompt generation, or a silent downgrade of required LLM/resolver behavior into deterministic lookup or fallback-only behavior.

## Objective Restatement
Create a resolver-specific capability and acceptance anchor for future PxFquery package milestones, especially M3. The output should define the required user-facing natural-language/semi-structured resolver behavior, CyHex-configured AI service use, exact/proxy/not-found routing, fallback semantics, demo cases, and acceptance evidence. This is a design/governance task only; it must not implement or test resolver code.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t007_development_source_map.md` | Trusted source map for migrated development assets and resolver-related source authority. | ok |
| A-002 | `1_asset/t007_development_state_report.md` | Intended product scope plus matrix/index/resolver design interpretation. | ok |
| A-003 | `1_asset/t007_development_gap_and_risk_list.md` | Known resolver, validation, and claim risks. | ok |
| A-004 | `1_asset/t013_mvp_capability_contract.md` | Reviewed MVP capability expectations and boundaries. | ok |
| A-005 | `1_asset/t013_capability_status_matrix.csv` | Evidence for passed, partial, blocked, failed, and missing behaviors. | ok |
| A-006 | `1_asset/t013_failure_missing_capability_list.md` | Missing resolver, natural-language, LLM, and runtime-index behaviors. | ok |
| A-007 | `1_asset/t061_legacy_source_digest.md` | Bounded legacy source digest and resolver-related source hints. | ok |
| A-008 | `1_asset/t061_legacy_reference_boundaries.yaml` | Boundary rules for citing/adapting T-061 findings. | ok |
| A-009 | `1_asset/t062_algorithm_package_delivery_anchor.yaml` | Package-level capability anchor that this task refines. | ok |
| A-010 | `1_asset/t062_algorithm_capability_matrix.csv` | Capability-to-evidence matrix for milestone alignment. | ok |
| A-011 | `1_asset/t062_algorithm_downgrade_rules.md` | Runtime fallback versus unapproved downgrade rules. | ok |
| A-012 | `1_asset/t062_milestone_review_rubric.md` | Evidence hierarchy and review procedure. | ok |
| A-013 | `1_asset/t062_milestone_classification_vocabulary.yaml` | Status vocabulary for delivered/partial/blocked/failed/downgraded/deferred/evidence-insufficient states. | ok |

## Execution Strategy
1. Read only the registered inputs above plus the current task protocol/asset rules; extract resolver-relevant requirements, gaps, source boundaries, downgrade rules, and acceptance vocabulary into working notes under `3_execution/`.
2. Draft the M3 resolver behavior model: supported query modes, required parse fields, ambiguity handling, structured output, confidence/evidence metadata, and user-facing summary expectations.
3. Specify the CyHex-configured AI-service rule: milestones claiming LLM resolver capability must use the current CyHex-registered AI route, currently `deepseek-v4-pro`, unless a later task explicitly changes it.
4. Define exact, proxy, and not-found routing semantics for forward and reverse queries, including what LLM assistance may do and what it must not claim as biological evidence.
5. Define fallback semantics for LLM unavailability, parse failure, proxy failure, missing indexes, unsupported entities, and low-confidence matches; classify fallback as runtime behavior/evidence, not as proof of primary resolver delivery.
6. Build the required demo case catalog and acceptance matrix, covering exact/proxy/not-found, forward/reverse, ambiguous natural language, semi-structured input, LLM-unavailable fallback, and metadata inspection.
7. Produce the reusable YAML anchor, design Markdown, CSV matrix, demo catalog, HTML reports, artifact registry update, and completion report in the specified output directories.

## Conservative Execution Advice
- Start with: a narrow extraction pass over A-009, A-010, A-011, A-012, and A-013 to inherit T-062 vocabulary and downgrade rules before reading the broader T-007/T-013/T-061 context.
- Smoke/demo command or method: create a short `3_execution/` outline or scratch table listing the required output files, resolver capabilities, and status vocabulary before drafting final artifacts.
- Full run only after: confirming the outline contains all required behavior classes: natural-language, semi-structured, forward, reverse, exact, proxy, not-found, fallback, metadata, and downgrade handling.
- Cost/time risk: low compute and no network/API cost; the main risk is over-reading predecessor context or accidentally expanding into implementation/testing.
- Checkpoint advice: before writing final artifacts, compare planned outputs against the deliverables and acceptance criteria in `2_protocol/2_protocol_split/protocol.md`; if a needed claim would require code/runtime proof, label it as future acceptance evidence rather than current proof.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Machine-readable LLM/resolver capability anchor | `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml` | Defines resolver capabilities, AI-service rule, routing semantics, fallback/downgrade rules, and acceptance evidence in structured form. |
| Human-readable resolver functional design | `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md` | Concisely explains M3 user-facing resolver behavior without claiming implementation or test success. |
| Resolver acceptance matrix | `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv` | Maps each capability to required evidence, minimum behavior, disallowed substitutes, failure labels, and review status vocabulary. |
| Resolver demo case catalog | `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md` | Covers exact/proxy/not-found, forward/reverse, ambiguous NL, semi-structured, LLM-unavailable fallback, and metadata inspection cases. |
| Execution report | `4_artifact/3_document/execution_report_v20260625.html` | Records what was read, how outputs were produced, and confirms no implementation/tests/web/legacy-root reads occurred. |
| Result report | `4_artifact/3_d

...[truncated by CyHex prompt assembler: 1871 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/registry.yaml`

```text
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/2_protocol/3_asset_rule/asset_rule.yaml

Interpretation:

- `handoff_check_before_exec.md` is the execution strategy and risk guidance.
- `protocol.md` is the task contract.
- If they conflict, stop and write `5_report/blocked.md`. Do not guess.
- `registration.yaml` and `asset_rule.yaml` define the selected inputs. Do not perform a new asset discovery pass.
- `execution_handoff.md`, if present, is only for continuing an interrupted or long-context execution session.

## 2. Task Contract

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: digestion
Task: T-063 llm_resolver_capability_anchor
Status: active | Executor: hybrid
Objective: Create the LLM/resolver capability anchor for future PxFquery package milestones. Specify user-facing natural-language/semi-structured query behavior, CyHex-configured AI service use, exact/proxy/not-found handoff with LLM assistance, fallback semantics, demo cases, and acceptance evidence for M3-level resolver delivery.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
# T-063 llm_resolver_capability_anchor — Protocol

## Objective

Create the task-level LLM/resolver capability anchor for future PxFquery package milestones, especially M3-level resolver delivery. The task must define the user-facing natural-language and semi-structured query behavior, CyHex-configured AI service use, exact/proxy/not-found handoff with LLM assistance, fallback semantics, demo cases, and acceptance evidence. It must not implement API code or run package tests.

## Position In Project

This is a digestion/governance task under `goal_project_delivery_anchor`. It refines the T-062 algorithm-package delivery anchor for the specific resolver/LLM layer so later package milestones cannot count deterministic matrix lookup alone as delivery of user-facing resolver behavior when resolver capability is in scope.

The anchor should preserve the project-defined capability shape:

- forward query: biological context plus perturbation to functional response;
- reverse query: desired function plus biological context to candidate perturbations;
- natural-language or semi-structured query entry;
- resolver-mediated exact, proxy, and not-found evidence routing;
- LLM-assisted parsing and summarization through the current CyHex-configured AI service route, currently deepseek-v4-pro unless a later task explicitly changes it;
- deterministic fallback and transparent evidence metadata when LLM, proxy routing, or coverage fails.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` | Trusted source map for migrated PxFquery development assets and resolver-related source authority. |
| A-002 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Intended product scope and matrix/index/resolver design interpretation. |
| A-003 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Known resolver, validation, and claim risks. |
| A-004 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Reviewed MVP capability expectations and boundaries. |
| A-005 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Capability status evidence for passed, partial, blocked, failed, and missing behavior. |
| A-006 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Missing resolver, natural-language, LLM, and runtime-index behaviors that must not be silently downgraded. |
| A-007 | T-061 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_source_digest_repair_m1.md` | Bounded source digest for legacy package modules and resolver-related source hints. |
| A-008 | T-061 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml` | Boundary rules for citing or adapting T-061 findings. |
| A-009 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | Package-level capability anchor to refine for resolver delivery. |
| A-010 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | Capability-to-evidence matrix for milestone acceptance alignment. |
| A-011 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Rules distinguishing runtime fallback from unapproved scope downgrade. |
| A-012 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Evidence hierarchy and review procedure for future package milestones. |
| A-013 | T-062 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | Classification vocabulary for delivered, partial, blocked, failed, downgraded, deferred, and evidence-insufficient states. |

## Execution Steps

1. Read the registered inputs and extract only the resolver-relevant capability requirements, existing gaps, source-boundary rules, downgrade rules, and acceptance vocabulary.
2. Define the expected M3-level user-facing resolver behavior for natural-language and semi-structured query entry, including required input fields, supported ambiguity handling, structured parse output, evidence metadata, and user-facing summary behavior.
3. Specify the CyHex-configured AI service requirement: future resolver milestones that claim LLM capability must route through the current CyHex-registered AI address and currently desired `deepseek-v4-pro` model route unless a later task explicitly changes that route.
4. Define exact, proxy, and not-found resolver routing semantics, including how LLM assistance may parse, normalize, explain, or summarize but must not fabricate matrix evidence.
5. Define fallback semantics for unavailable LLM service, parse failure, proxy failure, missing indexes, unsupported cell lines, unsupported perturbations, unsupported functions, and low-confidence matches. Mark fallback as runtime behavior and evidence, not proof that primary LLM/resolver delivery is complete.
6. Create a demo case catalog with concrete required case types for future M3 acceptance: exact forward query, exact reverse query, proxy forward query, proxy reverse query, not-found query, ambiguous natural-language query, semi-structured query, LLM-service-unavailable fallback, and evidence-metadata inspection.
7. Create an acceptance matrix mapping each resolver capability to required evidence, minimum acceptable behavior, disallowed substitutes, failure labels, and review status vocabulary inherited from T-062.
8. Write a machine-readable resolver capability anchor YAML and a concise human-readable functional design Markdown document.
9. Write required execution and result reports, and register all accepted/reusable outputs in the current task artifact registry.

## Constraints

- This is a design and acceptance-anchor task only.
- Use selected predecessor artifacts and project protocol context; do not perform implementation, runtime tests, raw-data analysis, web search, or manuscript writing.
- Treat T-062 as the package-level anchor and make this task a resolver-specific refinement, not a competing replacement.
- Preserve the difference between conservative manuscript claims and development delivery scope: conservative claims do not make LLM/resolver functions optional when a milestone includes them.
- Require transparent provenance and evidence metadata for exact, proxy, fallback, and not-found outcomes.
- Treat LLM output as parsing/summarization/normalization assistance, not as independent biological evidence.
- Make any proposed deferral, optionalization, or fallback-only acceptance of required resolver behavior visible as a downgrade requiring explicit user approval.

## Forbidden

- Do not implement or modify package/API/source code.
- Do not run package workflows, tests, notebooks, matrix inspection, or biological analysis.
- Do not read or modify legacy source roots.
- Do not browse predecessor task directories beyond registered assets and allowed handoff/report files.
- Do not create final project deliverables under `6_project_deliverable/`.
- Do not call downstream CyHex prompt endpoints.
- Do not use web search.

## Web Search Allowance

Allowed: no

Reason: The current task is a project-internal capability and acceptance anchor. The required information is available from project protocol, current task intent, and selected predecessor handoffs/artifact registries. No current external evidence is required.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Machine-readable LLM/resolver capability anchor | `4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml` | yes |
| Human-readable resolver functional design | `4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md` | yes |
| Resolver acceptance matrix | `4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv` | yes |
| Resolver demo case catalog | `4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md` | yes |
| Execution report | `4_artifact/3_document/execution_report_v20260625.html` | yes |
| Result report | `4_artifact/3_document/result_report_v20260625.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The anchor explicitly defines M3-level resolver delivery as more than deterministic lookup when resolver is in scope.
- Natural-language and semi-structured entry behavior is specified with required parse fields, ambiguity handling, confidence/evidence metadata, and user-facing output expectations.
- CyHex-configured AI service use is specified, including current desired route `deepseek-v4-pro` and the rule that a later task must explicitly approve any route change.
- Exact, proxy, and not-found handoff behavior is defined for both forward and reverse query modes.
- Fallback semantics are concrete and classify fallback as runtime behavior/evidence, not delivery of the primary LLM/resolver capability.
- Demo cases cover exact, proxy, not-found, ambiguous, semi-structured, and LLM-unavailable scenarios.
- Acceptance evidence requirements include both functional behavior and metadata/provenance evidence.
- Downgrade, deferral, optionalization, and fallback-only acceptance rules are consistent with T-062.
- The task output does not claim that resolver code works, that LLM service was tested, or that missing indexes were repaired.

## Failure / Stop Rules

- Stop if registered predecessor assets are unavailable and the missing asset prevents defining resolver behavior without guessing.
- Stop if the work would require source-code implementation, runtime testing, matrix/raw-data analysis, web search, or direct legacy-root reads.
- Stop if predecessor evidence conflicts in a way that makes the required resolver capability impossible to define safely; report the conflict in `5_report/completion.md`.
- Stop if any output would silently downgrade required LLM/resolver capability into deterministic lookup, fallback-only behavior, or a deferred optional feature.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
- Write required HTML reports if execution produces human-facing results.

### Selected Assets (13)
- A-001 [document] t007_development_source_map — path: 1_asset/t007_development_source_map.md — origin: T-007/D-001
- A-002 [document] t007_development_state_report — path: 1_asset/t007_development_state_report.md — origin: T-007/D-002
- A-003 [document] t007_development_gap_and_risk_list — path: 1_asset/t007_development_gap_and_risk_list.md — origin: T-007/D-005
- A-004 [document] t013_mvp_capability_contract — path: 1_asset/t013_mvp_capability_contract.md — origin: T-013/D-001
- A-005 [table] t013_capability_status_matrix — path: 1_asset/t013_capability_status_matrix.csv — origin: T-013/D-003
- A-006 [document] t013_failure_missing_capability_list — path: 1_asset/t013_failure_missing_capability_list.md — origin: T-013/D-005
- A-007 [document] t061_legacy_source_digest — path: 1_asset/t061_legacy_source_digest.md — origin: T-061/D-001
- A-008 [document] t061_legacy_reference_boundaries — path: 1_asset/t061_legacy_reference_boundaries.yaml — origin: T-061/D-003
- A-009 [document] t062_algorithm_package_delivery_anchor — path: 1_asset/t062_algorithm_package_delivery_anchor.yaml — origin: T-062/T062-A-001
- A-010 [table] t062_algorithm_capability_matrix — path: 1_asset/t062_algorithm_capability_matrix.csv — origin: T-062/T062-A-002
- A-011 [document] t062_algorithm_downgrade_rules — path: 1_asset/t062_algorithm_downgrade_rules.md — origin: T-062/T062-A-003
- A-012 [document] t062_milestone_review_rubric — path: 1_asset/t062_milestone_review_rubric.md — origin: T-062/T062-A-004
- A-013 [document] t062_milestone_classification_vocabulary — path: 1_asset/t062_milestone_classification_vocabulary.yaml — origin: T-062/T062-A-005

### Asset Rules

### Required
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_source_map_v20260617.md — Trusted source map for migrated PxFquery development assets and resolver-related source authority.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md — Describes intended product scope and the matrix/index/resolver design interpretation.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md — Carries forward resolver, validation, and claim risks that the anchor must address.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md — Defines reviewed MVP capability expectations and boundaries relevant to resolver acceptance.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv — Provides capability status evidence for pass, partial, blocked, failed, and missing behaviors.
- /Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md — Identifies missing resolver, natural-language, LLM, and runtime-index behaviors.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_source_digest_repair_m1.md — Bounded source digest for legacy package modules and resolver-related source hints.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/4_artifact/2_persist/legacy_reference_boundaries_repair_m1.yaml — Boundary rules for citing/adapting T-061 source-digest findings.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml — Primary package-level capability anchor that this resolver-specific anchor must refine.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv — Capability-to-evidence matrix for aligning resolver acceptance with package milestones.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md — Rules distinguishing valid runtime fallback from unapproved scope downgrade.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md — Evidence hierarchy and review procedure for future resolver-capability acceptance.
- /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml — Classification vocabulary for delivered, partial, blocked, failed, downgraded, deferred, out-of-scope, and evidence-insufficient states.
### Forbidden
- predecessor task directory browsing beyond registered assets and listed handoff/report files
- downstream prompt endpoints
- package source implementation or modification
- raw matrix/data analysis
- legacy source root reads unless a future task explicitly registers and justifies them
- final project deliverable directory modifications
### Output
- 4_artifact/2_persist/pxfquery_llm_resolver_capability_anchor_v20260625.yaml
- 4_artifact/2_persist/pxfquery_llm_resolver_functional_design_v20260625.md
- 4_artifact/5_table/pxfquery_llm_resolver_acceptance_matrix_v20260625.csv
- 4_artifact/2_persist/pxfquery_llm_resolver_demo_case_catalog_v20260625.md
- 4_artifact/3_document/execution_report_v20260625.html
- 4_artifact/3_document/result_report_v20260625.html

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

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

Default language for the two HTML reports is Chinese. Use another language only when the task protocol or human instruction explicitly requires it. The reports should be human-readable, structured, and suitable for quick review by the project owner.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/execution_handoff.md`

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
