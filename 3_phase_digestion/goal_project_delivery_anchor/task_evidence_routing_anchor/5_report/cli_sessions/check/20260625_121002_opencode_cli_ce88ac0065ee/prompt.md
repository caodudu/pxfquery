# Checking Prompt
Generated: 2026-06-25 12:10

## 0. Role

You are the CyHex checking AI for one task.

Your job is to confirm whether the current configuration can be executed by a separate execution AI without wasting time, expanding scope, or guessing missing context.

You are not the configuration AI. You are not the execution AI. Do not redo predecessor discovery. Do not execute the task body. Do not produce final deliverables.

Your output is important because execution AI will read:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md`

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
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/1_meta_info/meta.yaml`

```text
task_id: T-064
name: evidence_routing_anchor
phase: digestion
goal: goal_project_delivery_anchor
project: P-012
objective: Create the evidence-routing and non-hit/proxy/transfer behavior anchor
  for PxFquery. Define exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing,
  and transfer/suggestion routes, with evidence metadata and acceptance cases for
  future stress-test and M3 package milestones.
executor: hybrid
agent_id: AGT-002
config_agent_id: AGT-002
check_agent_id: AGT-002
execute_agent_id: AGT-002
server_id: null
status: active
cyhex_version: 1.2.20
milestone_id: ''
milestone_final: false
created: '2026-06-25'
started: null
completed: null
notes: Do not write implementation code. Produce route taxonomy, acceptance cases,
  metadata contract, and stress-test-oriented anchor assets. | Route behavior must
  include user-facing transfer/suggestion semantics, not just returning empty results.
fast_pass_permission: green
sub_status: config_approved
fast_pass_last_auto_approved: config_review
fast_pass_last_auto_approved_at: '2026-06-25T12:10:02'

```

### Current Task Orchestration Input: orchestration_input.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/1_meta_info/orchestration_input.yaml`

```text
delivery_goal: Exact/proxy/no-hit/transfer evidence-routing anchor for future PxFquery
  package milestones.
predecessor_tasks:
- task_id: T-007
  gate: must
  reason: Trusted development-state digestion for intended exact/proxy/not-found routing
    behavior.
- task_id: T-013
  gate: must
  reason: MVP review evidence about missing query behavior and capability gaps.
- task_id: T-021
  gate: must
  reason: Standard resources/index constraints for feasible exact/proxy/no-hit routes.
- task_id: T-058
  gate: must
  reason: Stress-test digestion handoff containing edge-case and strict-query scenarios.
reference_tasks:
- task_id: T-031
  reason: Historical no-hit guard may be used only as background; do not inherit its
    narrowed scope.
supplemental_notes:
- Do not write implementation code. Produce route taxonomy, acceptance cases, metadata
  contract, and stress-test-oriented anchor assets.
- Route behavior must include user-facing transfer/suggestion semantics, not just
  returning empty results.
- Distinguish deterministic fallback, proxy evidence, and LLM-assisted explanation
  so later code and writing do not conflate them.
suggested_agent:
  strength: weak
  reason: Mostly taxonomy/design asset grounded in done digestion outputs.

```

### Current Task Asset Registry: registration.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/1_asset/registration.yaml`

```text
assets:
  - id: A-001
    name: PxFquery development state report
    type: document
    source: predecessor
    source_task: T-007
    source_artifact_id: D-002
    origin: "T-007/D-002: Summarizes intended product scope, implemented components, data/index readiness, validation state, and development interpretation"
    registered: "2026-06-25"
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md"
    symlink: false
    status: ready
    notes: Intended resolver/proxy/exact routing behavior, known gaps (no-hit fuzzy false-positive, function_index.json missing, always_llm instability)
  - id: A-002
    name: T013 Failure and missing capability list
    type: document
    source: predecessor
    source_task: T-013
    source_artifact_id: D-005
    origin: "T-013/D-005: CAP-05 no-hit fuzzy fallback false-positive risk, CAP-07 resolver blocked by index naming and function_index gap"
    registered: "2026-06-25"
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_function_review/task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md"
    symlink: false
    status: ready
    notes: Specific capability evidence that must be addressed in no-hit, proxy-hit, and transfer/suggestion route definitions
  - id: A-003
    name: Standard resource guide
    type: document
    source: predecessor
    source_task: T-021
    source_artifact_id: D-001
    origin: "T-021/D-001: 19 standard resources with format decisions, schemas, and usage instructions; rebuilt function_index.json"
    registered: "2026-06-25"
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md"
    symlink: false
    status: ready
    notes: Canonical reference for the index and matrix resources that evidence routing operates on
  - id: A-004
    name: Stress test development handoff pack
    type: document
    source: predecessor
    source_task: T-058
    source_artifact_id: D-001
    origin: "T-058/D-001: 7-section handoff pack with 29 stress-test scenarios, pass/fail/borderline map, reusable assets, and known gaps"
    registered: "2026-06-25"
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_legacy_stress_test_asset_digestion/task_04_stress_test_development_handoff_pack/4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md"
    symlink: false
    status: ready
    notes: Scenario inventory for stress-test anchor mapping; covers no-hit, proxy/exact, boundary, overly-broad, and complex query dimensions
  - id: A-005
    name: Development gap and risk list
    type: document
    source: predecessor
    source_task: T-007
    source_artifact_id: D-005
    origin: "T-007/D-005: Lists high-priority gaps, risks, claims to avoid, and safer claims"
    registered: "2026-06-25"
    path: "/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md"
    symlink: false
    status: ready
    notes: Known risks to encode in route constraints: LLM stability 6/9, always_llm latency 167.3s, NOT_FOUND for generic drugs
```

### Current Task Protocol Draft: protocol.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/2_protocol_split/protocol.md`

```text
# T-064 evidence_routing_anchor — Protocol

## Objective

Define the PxFquery evidence-routing behavior contract for future package milestones (including M3).
Produce a complete route taxonomy, acceptance cases, evidence metadata schema, and stress-test-oriented anchor assets. Do not write implementation code.

## Position In Project

This is a digestion-stage anchor task under `goal_project_delivery_anchor`. It defines what PxFquery evidence routing should do at the specification level, using the accumulated understanding from:

- T-007 development state (intended resolver/proxy behavior, validated components, gaps)
- T-013 MVP review (capability pass/fail/blocked evidence, no-hit risk, index gaps)
- T-021 standard resources (standard inputs, rebuilt function_index.json)
- T-058 stress-test handoff (29 scenarios, pass/fail/borderline map, edge-case catalog)

This anchor is a prerequisite for M3 package milestone tasks and future stress-test milestone tasks (ST-M01 through ST-M07 from T-058).

## Inputs

| Asset ID | Source Task | Path | Why needed |
|---|---|---|---|
| A-001 | T-007 | 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Intended resolver/proxy/exact routing behavior, known gaps (no-hit fuzzy false-positive, function_index.json missing, always_llm instability) |
| A-002 | T-013 | 4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md | Specific capability failures: CAP-05 no-hit returns false match, CAP-07 resolver blocked by index naming/function_index gap |
| A-003 | T-021 | 4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md | Standard resource definitions available to evidence routing: 3 functional matrices, 10 query indexes (including rebuilt function_index.json), metadata tables |
| A-004 | T-058 | 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md | 29 stress-test scenarios with hit-level categories (no-hit, proxy/exact, boundary, overly-broad, complex) and reuse-ready assets for acceptance testing |
| A-005 | T-007 | 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | Known risks to encode in route constraints: LLM stability 6/9, always_llm latency, NOT_FOUND for generic drugs |

## Execution Steps

1. Read A-001 through A-005 to understand the current evidence landscape, especially:
   - What exact-hit logic already exists and is validated (deterministic 7/7 matrix test)
   - What proxy routing tiers exist (perturbation proxy, cell-line proxy, both-proxy)
   - What no-hit behavior currently looks like (fuzzy fallback false-positive risk)
   - What is missing or fails (resolver blocked, generic-drug NOT_FOUND, ambiguous context handling)
   - What transfer/suggestion semantics the project goal requires

2. Define the evidence-routing route taxonomy with exactly these route types:
   - **exact-hit**: Perturbation and biological context both resolve to exact index entries; deterministic numeric retrieval from functional matrices.
   - **proxy-hit**: One or both dimensions resolve via neighbor/proxy index; proxy source and confidence documented in evidence metadata.
   - **no-hit**: No resolvable perturbation or impossible context combination; returns structured NO_HIT result with diagnostic metadata.
   - **ambiguous-hit**: Query resolves to multiple plausible perturbations or contexts; returns ranked candidates with confidence and disambiguation guidance.
   - **context-missing**: Query lacks biological context; returns prompt for required context fields with validation rules.
   - **transfer/suggestion**: No-hit or ambiguous-hit triggers user-facing suggestions for reformulated queries, alternative contexts, or related perturbations.

3. For each route type, write structured acceptance cases. Each case must include:
   - Route type
   - Input query description
   - Expected resolution path (which index, which proxy tier, which matrix)
   - Expected evidence metadata fields
   - Pass condition
   - Reference to T-058 stress-test scenarios where applicable

4. Define the evidence metadata contract. Every route response must include:
   - `route_type`: one of the six route types
   - `query_context`: resolved biological context (cell line, tissue, normalization state)
   - `perturbation_resolution`: how perturbation was resolved (exact match, proxy neighbor, unmatched)
   - `function_response`: resolved functional scores or NO_HIT indication
   - `confidence`: route-level confidence classification (high, medium, low) based on resolution quality
   - `proxy_chain`: if proxy was used, the full proxy path (e.g., "A549 → NCI-H226 via subtype neighbor")
   - `diagnostics`: warnings, missing fields, disambiguation candidates
   - `suggestions`: transfer/suggestion list if no-hit or ambiguous

5. Write stress-test-oriented anchor specification:
   - Map each of the 29 T-058 scenarios to one or more route types
   - Mark which route behaviors each scenario exercises
   - Document expected pass/fail/borderline mapping per the T-058 evidence

6. Write the output deliverables under `4_artifact/`:
   - Route taxonomy document with acceptance cases
   - Evidence metadata contract (schema plus field definitions)
   - Stress-test anchor mapping table

## Constraints

- Do not write implementation code (Python, JSON schemas as code are acceptable).
- Distinguish deterministic fallback, proxy evidence, and LLM-assisted explanation so later code and writing do not conflate them.
- The transfer/suggestion route must describe user-facing semantics: what a user sees, not just an empty result or error code.
- Route definitions must reference the T-021 standard resources as the canonical index/matrix input set.
- No-hit behavior must require explicit similarity thresholding (not token-similarity fuzzy match without guard).
- Respect the project rule: resolver/LLM/proxy routing are required capabilities, not optional fallback-only stubs.

## Forbidden

- Do not write Python implementation co

...[truncated by CyHex prompt assembler: 2565 chars omitted]
```

### Current Task Asset Rule Draft: asset_rule.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/3_asset_rule/asset_rule.yaml`

```text
required:
  - id: A-001
    source_task: T-007
    source_artifact_id: D-002
    path: 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md
    reason: Intended resolver/proxy/exact routing behavior, known gaps, and current PxFquery package identity needed to define route semantics.
  - id: A-002
    source_task: T-013
    source_artifact_id: D-005
    path: 4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md
    reason: Specific capability failures (CAP-05 no-hit false-positive, CAP-07 resolver blocked) that must be addressed in route definitions.
  - id: A-003
    source_task: T-021
    source_artifact_id: D-001
    path: 4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md
    reason: Canonical standard resource definitions (matrices, indexes, metadata tables) that route behavior must reference.
  - id: A-004
    source_task: T-058
    source_artifact_id: D-001
    path: 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md
    reason: 29 stress-test scenarios with hit-level categories needed to produce stress-test anchor mapping.
  - id: A-005
    source_task: T-007
    source_artifact_id: D-005
    path: 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md
    reason: Known risks (LLM stability, latency, NOT_FOUND patterns) to encode in route constraints.
optional: []
forbidden:
  - legacy source root directories
  - predecessor 2_protocol/ directories
  - predecessor 1_asset/ directories
  - predecessor 3_execution/ directories
output:
  - path: 4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md
    type: document
  - path: 4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml
    type: data
  - path: 4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv
    type: table
modifiable:
  - 3_execution/
  - 4_artifact/
  - 5_report/
non_modifiable:
  - predecessor task directories
  - 2_project_asset/
  - legacy source root
```


## 2. Task

Project: PxFquery (P-012)
Project phase/status: development / active
Task phase: digestion
Task ID: T-064 | Name: evidence_routing_anchor
Status: active | Executor: hybrid
Objective: Create the evidence-routing and non-hit/proxy/transfer behavior anchor for PxFquery. Define exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, and transfer/suggestion routes, with evidence metadata and acceptance cases for future stress-test and M3 package milestones.
Notes / User Natural-Language Intent: Do not write implementation code. Produce route taxonomy, acceptance cases, metadata contract, and stress-test-oriented anchor assets. | Route behavior must include user-facing transfer/suggestion semantics, not just returning empty results.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor

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
  registration_path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/1_asset/registration.yaml
  asset_rule_path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/3_asset_rule/asset_rule.yaml
  task_phase: digestion
  project_asset_access: allowed
  zero_assets: true
  total_assets: 0
  symlink_sync:
    checked: 0
    linked: 0
    skipped: 0
    changed: false
  counts:
    ok: 0
    planned: 0
    remote: 0
    missing: 0
    empty_file: 0
    empty_dir: 0
    forbidden_scope: 0
  assets:
  - none
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
5. Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md`.
6. Stop after the check report. Do not call any `/prompt/generate*` endpoint.

## 6. Yellow Repair

Enter Yellow Repair when the configuration is close but flawed.

Allowed repairs:
- PATCH task status to active if needed.
- Fix wrong/missing asset path entries in `1_asset/registration.yaml`.
- Fix `2_protocol/3_asset_rule/asset_rule.yaml` if required/forbidden/output rules are inconsistent.
- Revise `2_protocol/2_protocol_split/protocol.md` if steps/deliverables are vague, oversized, or disconnected from selected assets.
- Create/update expected `3_execution/` step folders if protocol requires them.
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md`.
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
- Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/blocked.md` with exact blocker, evidence, and required fix.
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

Write `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md` in this exact structure:

```md
# Check Handoff Before Exec: T-064 evidence_routing_anchor

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
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md` 是否已写
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
