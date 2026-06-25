# Delivery QA Prompt
Generated: 2026-06-25 12:42

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


### 1.3 Current Task And Delivery Snapshot
### Current Task Meta: meta.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-062
name: algorithm_package_delivery_anchor
phase: digestion
goal: goal_project_delivery_anchor
project: P-012
objective: Create the authoritative PxFquery algorithm-package delivery anchor. Define
  the project-valid package capability set, acceptance rubric, downgrade rules, and
  milestone classification vocabulary so future package milestones cannot silently
  shrink into deterministic lookup only.
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
notes: Digestion anchor only; do not write package code and do not redefine the milestone
  to the easiest deterministic subset. | Separate manuscript claim restraint from
  development deliverable scope; LLM/resolver is not optional merely because manuscript
  claims must be conservative.
fast_pass_permission: green
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-25T12:19:58'

```

### Current Task Orchestration Input: orchestration_input.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/2_protocol/1_meta_info/orchestration_input.yaml`

```text
delivery_goal: Authoritative algorithm-package delivery anchor for PxFquery milestones.
predecessor_tasks:
- task_id: T-003
  gate: must
  reason: Project protocol normalization history, including the source of prior LLM/resolver
    optionalization that must now be corrected.
- task_id: T-007
  gate: must
  reason: Trusted development-state digestion for intended tool behavior and legacy
    capability map.
- task_id: T-013
  gate: must
  reason: MVP gap/review evidence for expected package capabilities and missing pieces.
- task_id: T-021
  gate: must
  reason: Trusted standard resource/data basis for package capability grounding.
reference_tasks:
- task_id: T-061
  reason: Reference for migrated source boundaries if needed; do not rescan raw legacy
    project.
supplemental_notes:
- Digestion anchor only; do not write package code and do not redefine the milestone
  to the easiest deterministic subset.
- Separate manuscript claim restraint from development deliverable scope; LLM/resolver
  is not optional merely because manuscript claims must be conservative.
- 'Expected outputs: machine-readable anchor YAML, capability matrix, downgrade rules,
  milestone review rubric, and Chinese HTML/Markdown summary under 4_artifact/.'
suggested_agent:
  strength: strong
  reason: Project-level scope anchor.

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/1_asset/registration.yaml`

```text
assets:
- id: A-001
  name: project_protocol_revision_report
  type: document
  source: predecessor
  source_task: T-003
  source_artifact_id: T003-A-001
  origin: T-003/T003-A-001
  registered: '2026-06-25'
  path: 1_asset/project_protocol_revision_report.md
  symlink: true
  status: ready
  notes: Use to preserve the protocol-normalization history and avoid reviving obsolete
    legacy protocol structures.
  location: local
- id: A-002
  name: pxfquery_development_state_report
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-002
  origin: T-007/D-002
  registered: '2026-06-25'
  path: 1_asset/pxfquery_development_state_report.md
  symlink: true
  status: ready
  notes: Use as the main digestion source for intended PxFquery package identity,
    behavior, and completion boundary.
  location: local
- id: A-003
  name: pxfquery_development_gap_and_risk_list
  type: document
  source: predecessor
  source_task: T-007
  source_artifact_id: D-005
  origin: T-007/D-005
  registered: '2026-06-25'
  path: 1_asset/pxfquery_development_gap_and_risk_list.md
  symlink: true
  status: ready
  notes: Use to anchor missing-capability, risk, and overclaim controls.
  location: local
- id: A-004
  name: mvp_capability_contract
  type: document
  source: predecessor
  source_task: T-013
  source_artifact_id: D-001
  origin: T-013/D-001
  registered: '2026-06-25'
  path: 1_asset/mvp_capability_contract.md
  symlink: true
  status: ready
  notes: Use to preserve previously defined MVP capability gates while expanding them
    into an authoritative package-delivery anchor.
  location: local
- id: A-005
  name: capability_status_matrix
  type: table
  source: predecessor
  source_task: T-013
  source_artifact_id: D-003
  origin: T-013/D-003
  registered: '2026-06-25'
  path: 1_asset/capability_status_matrix.csv
  symlink: true
  status: ready
  notes: Use as current-run evidence for delivered, partial, blocked, failed, and
    missing package capabilities.
  location: local
- id: A-006
  name: failure_missing_capability_list
  type: document
  source: predecessor
  source_task: T-013
  source_artifact_id: D-005
  origin: T-013/D-005
  registered: '2026-06-25'
  path: 1_asset/failure_missing_capability_list.md
  symlink: true
  status: ready
  notes: Use to define downgrade and stop rules for missing resolver, proxy, or natural-language
    behavior.
  location: local
- id: A-007
  name: standard_resource_guide
  type: document
  source: predecessor
  source_task: T-021
  source_artifact_id: D-001
  origin: T-021/D-001
  registered: '2026-06-25'
  path: 1_asset/standard_resource_guide.md
  symlink: true
  status: ready
  notes: Use to ground package capability expectations in the verified standard data/resource
    basis without loading raw resource files.
  location: local
- id: A-008
  name: standard_resources_bundle
  type: other
  source: predecessor
  source_task: T-021
  source_artifact_id: D-004
  origin: T-021/D-004
  registered: '2026-06-25'
  path: 1_asset/standard_resources_bundle
  symlink: true
  status: ready
  notes: Use as the registered canonical resource bundle reference for acceptance
    language; execution should inspect only names/metadata if needed, not rerun validation
    or raw analysis.
  location: local

```

### Current Task Protocol: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/2_protocol/2_protocol_split/protocol.md`

```text
# T-062 algorithm_package_delivery_anchor — Protocol

## Objective

Create the authoritative PxFquery algorithm-package delivery anchor for future package milestones. The anchor must define the project-valid package capability set, acceptance rubric, downgrade rules, and milestone classification vocabulary so later milestones cannot silently shrink PxFquery into deterministic lookup only.

This is a digestion and governance task only. It must not write package code, rerun algorithm tests, rebuild data resources, or create final project deliverables.

## Position In Project

T-062 sits under the project delivery-anchor goal and converts prior digestion/review evidence into a durable task-level authority for later development planning, milestone review, and capability acceptance. It must separate conservative manuscript claims from development delivery scope: manuscript claim restraint does not make resolver, LLM-assisted parsing/summarization, proxy routing, or user-facing query transfer optional when those capabilities are part of a milestone.

The output should be strong enough for future CyHex tasks to classify package milestones as delivered, partial, blocked, downgraded, deferred, or out of scope, and to identify whether any deferral or scope reduction was user-approved.

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-003 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_normalize_project_protocol_from_migrated_context/4_artifact/2_persist/project_protocol_revision_report_v20260616.md` | Preserve protocol-normalization history and source-boundary context. |
| A-002 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` | Main source for intended package identity, behavior, and completion boundary. |
| A-003 | T-007 | `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` | Risk, missing-capability, and overclaim controls. |
| A-004 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md` | Prior MVP capability contract to generalize into delivery-anchor rules. |
| A-005 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv` | Current-run capability status evidence. |
| A-006 | T-013 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md` | Known failure, blocked, partial, and missing capabilities. |
| A-007 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md` | Verified standard resource basis and runtime data expectations. |
| A-008 | T-021 | `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/` | Canonical standard resource bundle reference for acceptance language. |

## Execution Steps

1. Read the registered predecessor artifacts and extract only the capability, acceptance, risk, downgrade, and resource-basis facts needed for a package-delivery anchor.
2. Define the project-valid PxFquery package capability set, including at minimum forward query, reverse query, biological context handling, exact evidence routing, proxy evidence routing, not-found routing, resolver-mediated natural-language or semi-structured entry, LLM-assisted parsing/summarization where required by milestone scope, deterministic fallback, transparent evidence metadata, and standard resource compatibility.
3. Produce a machine-readable anchor YAML that records each capability, required evidence, allowed fallback, acceptance state vocabulary, downgrade triggers, and user-approval requirements.
4. Produce a capability matrix table mapping capabilities to required evidence, current predecessor evidence, acceptance threshold, likely failure modes, and whether absence is a blocker, partial delivery, or approved deferral.
5. Write downgrade rules that clearly distinguish runtime fallback from scope downgrade. A fallback path may be valid behavior, but it cannot count as delivery of the primary resolver/LLM/proxy capability unless the milestone explicitly accepts fallback-only behavior.
6. Write a milestone review rubric and classification vocabulary for future package milestones. Include labels for delivered, partial, blocked, failed, downgraded, deferred-user-approved, deferred-not-approved, out-of-scope, and evidence-insufficient.
7. Write a concise Chinese Markdown and HTML summary for human review. The summary should explain the anchor purpose, required capability set, downgrade rules, and how future milestones should use the rubric.
8. Register all reusable outputs in `4_artifact/registry.yaml` and write `5_report/completion.md`.

## Constraints

- Keep this task at digestion/anchor level; do not implement or repair package behavior.
- Use predecessor evidence and the current project protocol as authority. Do not promote old legacy protocol shells into current rules.
- Preserve the full development delivery scope when a milestone calls for resolver, LLM-assisted behavior, proxy routing, transfer behavior, or user-facing query entry.
- Keep manuscript claim restraint separate from software delivery acceptance.
- Use the T-021 standard resources as the canonical data/resource basis for future package compatibility language.
- Store temporary notes, scripts, and intermediate construction files in `3_execution/`; store accepted reusable outputs in `4_artifact/`.

## Forbidden

- Do not write or modify package source code.
- Do not run algorithm tests, rebuild query indexes, regenerate matrices, or perform raw data analysis.
- Do not use web search or external sources.
- Do not read from `/Users/dudu/Documents/3_Project/8_functional_query` directly.
- Do not modify predecessor task directories, project protocol files, project assets, or final project deliverable directories.
- Do not mark the task complete without producing the required anchor YAML, capability matrix, downgrade rules, review rubric, vocabulary, and Chinese summary.

## Web Search Allowance

Allowed: no

Reason: The current task can be safely configured and executed from project protocol plus selected predecessor artifacts. No current external facts are needed to define the project-internal delivery anchor.

Required evidence files, if allowed:
- None.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Machine-readable package delivery anchor | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | yes |
| Capability matrix | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | yes |
| Downgrade rules | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | yes |
| Milestone review rubric | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | yes |
| Milestone classification vocabulary | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | yes |
| Chinese Markdown summary | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` | yes |
| Chinese HTML summary | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` | yes |
| Artifact registry update | `4_artifact/registry.yaml` | yes |
| Completion report | `5_report/completion.md` | yes |

## Acceptance Criteria

- The anchor explicitly preserves PxFquery as a perturbation-to-function package with forward and reverse query behavior, not deterministic lookup only.
- Resolver, LLM-assisted parsing/summarization, proxy routing, not-found routing, deterministic fallback, and transparent evidence metadata are represented as delivery capabilities when a milestone includes them.
- Downgrade rules state that removing, optionalizing, or deferring a required capability requires explicit user approval and must be labeled in future milestone review.
- The rubric distinguishes evidence of working behavior from planned behavior, fallback behavior, blocked behavior, missing behavior, and user-approved deferral.
- The capability matrix ties each capability to predecessor evidence and standard reso

...[truncated by CyHex prompt assembler: 1174 chars omitted]
```

### Current Task Asset Rule: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-003
    source_artifact_id: T003-A-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_asset_migration/task_normalize_project_protocol_from_migrated_context/4_artifact/2_persist/project_protocol_revision_report_v20260616.md"
    reason: "Protocol-normalization history and source-boundary context for the delivery anchor."
  - id: A-002
    source_task: T-007
    source_artifact_id: D-002
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md"
    reason: "Authoritative digestion of intended PxFquery package identity and behavior."
  - id: A-003
    source_task: T-007
    source_artifact_id: D-005
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md"
    reason: "Risk and overclaim controls for acceptance and downgrade rules."
  - id: A-004
    source_task: T-013
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_mvp_capability_contract_v20260618.md"
    reason: "Prior MVP capability contract to generalize into package-delivery capability anchors."
  - id: A-005
    source_task: T-013
    source_artifact_id: D-003
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/5_table/pxfquery_t013_capability_status_matrix_v20260618.csv"
    reason: "Current-run capability status evidence."
  - id: A-006
    source_task: T-013
    source_artifact_id: D-005
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md"
    reason: "Known failure, blocked, partial, and missing capabilities for stop and downgrade rules."
  - id: A-007
    source_task: T-021
    source_artifact_id: D-001
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md"
    reason: "Verified standard resource basis for package capability grounding."
  - id: A-008
    source_task: T-021
    source_artifact_id: D-004
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources/"
    reason: "Canonical resource bundle reference for acceptance criteria; not a mandate to rerun validation."
optional: []
forbidden:
  - "Implementation or modification of package source code."
  - "Running algorithm tests, rebuilding resources, or analyzing raw matrices as task execution."
  - "Writing final project deliverables under 6_project_deliverable/."
  - "Direct reads from /Users/dudu/Documents/3_Project/8_functional_query unless a later approved task explicitly registers that source."
output:
  - path: "4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml"
    type: yaml
  - path: "4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv"
    type: table
  - path: "4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md"
    type: document
  - path: "4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md"
    type: document
  - path: "4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml"
    type: yaml
  - path: "4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html"
    type: document
  - path: "4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md"
    type: document
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 1_project_init/1_project_protocol/
  - 2_project_asset/
  - 6_project_deliverable/

```

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-062 algorithm_package_delivery_anchor

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: predecessor task directories, `/Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol/`, `/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/`, `/Users/dudu/Documents/3_Project/12_PxFquery/6_project_deliverable/`, and `/Users/dudu/Documents/3_Project/8_functional_query`
- Required registry: `1_asset/registration.yaml` with eight ready registered assets A-001 through A-008
- Must stop if: registered assets are insufficient for a governance anchor, execution would require package code changes, algorithm tests, raw matrix analysis, web lookup, direct legacy-root inspection, or required outputs cannot be written under this task's allowed directories

## Objective Restatement
Create a task-level authoritative delivery anchor for future PxFquery algorithm-package milestones. The execution AI should digest registered predecessor evidence into capability definitions, acceptance vocabulary, downgrade controls, and review rubrics that prevent future milestones from silently reducing PxFquery to deterministic lookup only. This is a governance/digestion task, not a code, test, resource-build, or final-deliverable task.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/project_protocol_revision_report.md` | Protocol-normalization history and source-boundary context. | ok |
| A-002 | `1_asset/pxfquery_development_state_report.md` | Main source for intended package identity, behavior, and completion boundary. | ok |
| A-003 | `1_asset/pxfquery_development_gap_and_risk_list.md` | Risk, missing-capability, and overclaim controls. | ok |
| A-004 | `1_asset/mvp_capability_contract.md` | Prior MVP capability gates to generalize into package-delivery anchors. | ok |
| A-005 | `1_asset/capability_status_matrix.csv` | Current-run evidence for delivered, partial, blocked, failed, and missing capabilities. | ok |
| A-006 | `1_asset/failure_missing_capability_list.md` | Known failure, blocked, partial, and missing capabilities for stop and downgrade rules. | ok |
| A-007 | `1_asset/standard_resource_guide.md` | Verified standard resource basis for package compatibility and acceptance language. | ok |
| A-008 | `1_asset/standard_resources_bundle` | Canonical standard resource bundle reference; inspect names/metadata only if needed. | ok |

## Execution Strategy
1. Read only the registered assets A-001 through A-008 plus the current task protocol and project protocol snapshot; extract capability, acceptance, risk, downgrade, and resource-basis facts into temporary notes under `3_execution/`.
2. Build a project-valid capability set covering forward query, reverse query, biological context handling, exact/proxy/not-found routing, resolver-mediated query entry, LLM-assisted parsing/summarization where milestone scope requires it, deterministic fallback, transparent evidence metadata, and T-021 standard resource compatibility.
3. Write `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` with capability IDs, evidence requirements, allowed fallbacks, acceptance states, downgrade triggers, and user-approval requirements.
4. Write `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` mapping each capability to predecessor evidence, acceptance threshold, failure modes, and blocker/partial/deferral treatment.
5. Write downgrade and review documents under `4_artifact/2_persist/`, explicitly distinguishing runtime fallback from scope downgrade and defining future milestone labels.
6. Write Chinese Markdown and HTML summaries that explain the anchor purpose, required capability set, downgrade rules, and rubric use without overstating implementation readiness.
7. Register reusable outputs in `4_artifact/registry.yaml`, then write `5_report/completion.md` summarizing sources used, outputs produced, and any evidence limits.

## Conservative Execution Advice
- Start with: a short extraction pass over A-004, A-005, and A-006 to verify the T-013 vocabulary and missing-capability evidence before drafting the full anchor.
- Smoke/demo command or method: create a small temporary capability skeleton in `3_execution/` for three representative capabilities: forward query, resolver/LLM entry, and proxy evidence routing; verify each can carry fields for evidence, fallback, downgrade trigger, and approval requirement.
- Full run only after: the skeleton confirms the YAML and CSV schemas can represent deterministic, resolver/LLM, proxy, fallback, not-found, and resource-compatibility capabilities without collapsing them into one lookup category.
- Cost/time risk: low compute and no network/API cost; risk is mainly semantic overreach or accidental scope reduction.
- Checkpoint advice: before writing final `4_artifact/` outputs, compare capability coverage against the protocol's minimum capability list and against A-006 missing-capability categories.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Machine-readable package delivery anchor | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` | YAML parses and includes capabilities, evidence requirements, fallbacks, states, downgrade triggers, and approval rules. |
| Capability matrix | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` | CSV opens cleanly and maps each required capability to predecessor evidence, threshold, failure modes, and delivery treatment. |
| Downgrade rules | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` | Clearly separates runtime fallback from scope downgrade and requires explicit user approval for required-capability deferral/removal. |
| Milestone review rubric | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` | Future reviewers can classify delivered, partial, blocked, failed, downgraded, deferred, out-of-scope, and evidence-insufficient states. |
| Classification vocabulary | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` | YAML parses and defines all required milestone labels with usage rules. |
| Chinese Markdown summary | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` | Human-readable Chinese summary covers purpose, capability set, downgrade rules, and rubric use. |
| Chinese HTML summary | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` | HTML renders as a readable human-review summary. |
| Artifact registry update | `4_artifact/registry.yaml` | All reusable outputs are registered with paths, types, provenance, a

...[truncated by CyHex prompt assembler: 1689 chars omitted]
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/registry.yaml`

```text
artifacts:
  - id: T062-A-001
    name: pxfquery_algorithm_package_delivery_anchor
    type: yaml
    path: 2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-001
        - A-002
        - A-003
        - A-004
        - A-005
        - A-006
        - A-007
        - A-008
    notes: Machine-readable delivery anchor with capabilities, evidence requirements, fallback rules, and downgrade triggers.
  - id: T062-A-002
    name: pxfquery_algorithm_capability_matrix
    type: table
    path: 5_table/pxfquery_algorithm_capability_matrix_v20260625.csv
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-002
        - A-003
        - A-004
        - A-005
        - A-006
        - A-007
    notes: Capability-to-evidence matrix for future package milestone reviews.
  - id: T062-A-003
    name: pxfquery_algorithm_downgrade_rules
    type: document
    path: 2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-001
        - A-002
        - A-003
        - A-004
        - A-006
    notes: Rules distinguishing runtime fallback from scope downgrade and requiring approval for capability reduction.
  - id: T062-A-004
    name: pxfquery_milestone_review_rubric
    type: document
    path: 2_persist/pxfquery_milestone_review_rubric_v20260625.md
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-002
        - A-003
        - A-005
        - A-006
        - A-007
    notes: Review rubric and evidence hierarchy for algorithm-package milestone acceptance.
  - id: T062-A-005
    name: pxfquery_milestone_classification_vocabulary
    type: yaml
    path: 2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-003
        - A-004
        - A-005
        - A-006
    notes: Machine-readable vocabulary for delivered, partial, blocked, failed, downgraded, deferred, out-of-scope, and evidence-insufficient states.
  - id: T062-A-006
    name: pxfquery_algorithm_package_delivery_anchor_summary_md
    type: document
    path: 2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-001
        - A-002
        - A-003
        - A-004
        - A-005
        - A-006
        - A-007
    notes: Chinese human-readable summary of anchor purpose, capability set, downgrade rules, and review use.
  - id: T062-A-007
    name: pxfquery_algorithm_package_delivery_anchor_summary_html
    type: document
    path: 3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - T062-A-006
    notes: Chinese HTML summary for human review.
  - id: T062-A-008
    name: execution_report
    type: document
    path: 3_document/execution_report_v20260625.html
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - A-001
        - A-002
        - A-003
        - A-004
        - A-005
        - A-006
        - A-007
        - A-008
    notes: Required Chinese execution report for T-062.
  - id: T062-A-009
    name: result_report
    type: document
    path: 3_document/result_report_v20260625.html
    created: '2026-06-25'
    status: accepted
    provenance:
      task_id: T-062
      sources:
        - T062-A-001
        - T062-A-002
        - T062-A-003
        - T062-A-004
        - T062-A-005
        - T062-A-006
    notes: Required Chinese result report summarizing produced anchor artifacts.

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/5_report/completion.md`

```text
# Completion

Task: T-062 algorithm_package_delivery_anchor  
Completed: 2026-06-25  
Status: Completed

## Completed Steps

1. Confirmed task-local structure and selected registered assets A-001 through A-008 were available through the task `1_asset/` registry links.
2. Read only the registered predecessor artifacts needed for capability, acceptance, risk, downgrade, and resource-basis extraction.
3. Wrote step discipline and extraction notes under `3_execution/step_list_and_extraction_notes_v20260625.md`.
4. Produced all required reusable deliverables under `4_artifact/`.
5. Validated the two YAML files parse as dictionaries and the capability matrix parses as CSV with 11 capability rows.
6. Registered accepted artifacts in `4_artifact/registry.yaml`.
7. Wrote required Chinese HTML execution and result reports.

## Deliverables Produced

| Deliverable | Path |
|---|---|
| Machine-readable package delivery anchor | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml` |
| Capability matrix | `4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv` |
| Downgrade rules | `4_artifact/2_persist/pxfquery_algorithm_downgrade_rules_v20260625.md` |
| Milestone review rubric | `4_artifact/2_persist/pxfquery_milestone_review_rubric_v20260625.md` |
| Milestone classification vocabulary | `4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml` |
| Chinese Markdown summary | `4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.md` |
| Chinese HTML summary | `4_artifact/3_document/pxfquery_algorithm_package_delivery_anchor_summary_v20260625.html` |
| Required execution report | `4_artifact/3_document/execution_report_v20260625.html` |
| Required result report | `4_artifact/3_document/result_report_v20260625.html` |
| Artifact registry | `4_artifact/registry.yaml` |

## Validation Evidence

Command run:

```bash
/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python -c "from pathlib import Path; import yaml,csv; base=Path('3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor'); files=['4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml','4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml']; [print(f, type(yaml.safe_load((base/f).read_text())).__name__) for f in files]; rows=list(csv.DictReader((base/'4_artifact/5_table/pxfquery_algorithm_capability_matrix_v20260625.csv').open(newline=''))); print('matrix_rows', len(rows)); print('matrix_fields', ','.join(rows[0].keys()))"
```

Observed output:

```text
4_artifact/2_persist/pxfquery_algorithm_package_delivery_anchor_v20260625.yaml dict
4_artifact/2_persist/pxfquery_milestone_classification_vocabulary_v20260625.yaml dict
matrix_rows 11
matrix_fields capability_id,capability,required_when,required_evidence,current_predecessor_evidence,acceptance_threshold,likely_failure_modes,absence_treatment,user_approval_required_for_deferral
```

## Evidence Limits

- This was a digestion/governance task only.
- No package source code was modified.
- No algorithm tests were run.
- No query indexes, matrices, or raw resources were rebuilt.
- No web search or external sources were used.
- No direct read from `/Users/dudu/Documents/3_Project/8_functional_query` was performed.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-062 | Name: algorithm_package_delivery_anchor
- Objective: Create the authoritative PxFquery algorithm-package delivery anchor. Define the project-valid package capability set, acceptance rubric, downgrade rules, and milestone classification vocabulary so future package milestones cannot silently shrink into deterministic lookup only.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor`

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
   - `4_artifact/3_document/execution_report_v20260625.html`
   - `4_artifact/3_document/result_report_v20260625.html`
8. HTML reports are useful for human review and consistent with registry/completion.
   Default language is Chinese unless protocol or human instruction explicitly requires another language.
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
   - `4_artifact/3_document/execution_report_v20260625.html`
   - `4_artifact/3_document/result_report_v20260625.html`
   Default language is Chinese unless protocol or human instruction explicitly requires another language.

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
5. `4_artifact/3_document/execution_report_v20260625.html`
6. `4_artifact/3_document/result_report_v20260625.html`

## 10. handoff_ai_use.md Required Shape

Write `5_report/handoff_ai_use.md` in this structure:

```md
# AI Handoff: T-062 algorithm_package_delivery_anchor

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
# Delivery QA: T-062 algorithm_package_delivery_anchor

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
