# Delivery QA Prompt
Generated: 2026-06-25 12:59

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
sub_status: delivery_review
fast_pass_last_auto_approved: check_review
fast_pass_last_auto_approved_at: '2026-06-25T12:20:02'

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

### Current Task Protocol: protocol.md
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

- Do not write Python implementation code.
- Do not run stress tests.
- Do not modify predecessor task outputs.
- Do not read predecessor `2_protocol/`, `1_asset/`, or `3_execution/` directories.
- Do not recursively scan predecessor task directories.
- Do not read legacy source root or unregistered project assets.
- Do not perform web search.

## Web Search Allowance

Allowed: no
Reason: All required information is available from the four predecessor tasks (T-007, T-013, T-021, T-058) and the project protocol. The route taxonomy is a design/specification asset grounded in completed digestion and review outputs.

## Deliverables

| Expected output | Target path | Required |
|---|---|---|
| Evidence routing route taxonomy with acceptance cases | 4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md | yes |
| Evidence metadata contract (schema + field definitions) | 4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml | yes |
| Stress-test anchor mapping (T-058 scenarios → routes) | 4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv | yes |

## Acceptance Criteria

1. All six route types (exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion) are defined with concrete acceptance cases.
2. Each acceptance case includes route type, input query, expected resolution path, evidence metadata fields, and pass condition.
3. Evidence metadata contract defines all required fields with types, descriptions, and valid value ranges.
4. Stress-test mapping covers all 29 T-058 scenarios with route-type assignment and expected behavior.
5. No-hit route requires explicit similarity thresholding; fuzzy fallback is described as disallowed unless thresholded.
6. Transfer/suggestion route describes user-facing suggestion semantics (reformulated queries, alternative contexts, related perturbations).
7. Route definitions reference T-021 standard resources where applicable.
8. All three deliverables are registered in `4_artifact/registry.yaml`.

## Failure / Stop Rules

- Stop if T-007/T-013/T-021/T-058 evidence is insufficient to define any of the six route types. Write the missing route as explicit gap note.
- Stop if project protocol contradicts the route taxonomy in a way that cannot be resolved by noting the conflict.
- Do not produce placeholder-only deliverables.

## Delivery Requirements

- Register all accepted/reusable outputs in `4_artifact/registry.yaml`.
- Keep scripts/logs/temp state in `3_execution/`.
- Move or copy accepted/reusable outputs into `4_artifact/`.
- Write `5_report/completion.md`.
```

### Current Task Asset Rule: asset_rule.yaml
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

### Check Handoff: handoff_check_before_exec.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md`

```text
# Check Handoff Before Exec: T-064 evidence_routing_anchor

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`
- Forbidden dirs: Predecessor `2_protocol/`, `1_asset/`, `3_execution/`; legacy source root (`/Users/dudu/Documents/3_Project/8_functional_query`); unregistered project assets
- Required registry: `1_asset/registration.yaml` (A-001 through A-005)
- Must stop if: Any required asset missing/empty; protocol contradiction unresolvable; cannot define any of the 6 route types; would produce placeholder-only deliverables

## Objective Restatement
Define the PxFquery evidence-routing behavior contract as a specification anchor for future M3 and stress-test milestones. Produce: (1) route taxonomy with 6 route types and acceptance cases, (2) evidence metadata contract schema, (3) stress-test scenario-to-route mapping. Do not write implementation code.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_state_report_v20260617.md | Intended resolver/proxy/exact routing behavior, known gaps | ok (file exists, 7649 bytes) |
| A-002 | task_mvp_algorithm_run-through_review/4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md | CAP-05 no-hit false-positive, CAP-07 resolver blocked | ok (file exists, 1503 bytes) |
| A-003 | task_standard_resources_optimal_formats/4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md | Canonical index/matrix reference for route definitions | ok (file exists, 13002 bytes) |
| A-004 | task_04_stress_test_development_handoff_pack/4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md | 29 stress-test scenarios for route mapping | ok (file exists, 33744 bytes) |
| A-005 | task_digest_pxfquery_development_state/4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md | LLM stability, latency, NOT_FOUND risk constraints | ok (file exists, 4847 bytes) |

Note: Preflight reported `zero_assets: true` because no symlinks exist in `1_asset/`. This is a mechanical preflight artifact; all 5 registration paths point to real, non-empty predecessor files.

## Execution Strategy
1. Read A-003 (standard resource guide) first to establish canonical index/matrix input set; read A-004 (stress-test handoff) second for scenario inventory
2. Read A-001, A-002, A-005 to extract current exact/proxy/no-hit behavior, gaps, and risk constraints
3. Define 6 route types (exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion) with semantics, resolution paths, and threshold rules
4. Write acceptance cases for each route type — each case includes input query, expected resolution path, evidence metadata fields, pass condition, and T-058 scenario reference where applicable
5. Define evidence metadata contract with 8 required fields (route_type, query_context, perturbation_resolution, function_response, confidence, proxy_chain, diagnostics, suggestions) — types, descriptions, valid ranges
6. Map all 29 T-058 stress-test scenarios to route types with expected pass/fail/borderline classification; write all 3 deliverables and register in `4_artifact/registry.yaml`

## Conservative Execution Advice
- Start with: Read A-003 (standard resources) to confirm the foundation indexes/matrices that all routes reference
- Smoke/demo method: After reading A-003 + A-004, draft the route taxonomy outline before filling in detailed acceptance cases
- Full run only after: Confirming all 6 route types can be meaningfully defined from available evidence
- Cost/time risk: Low — all inputs are local documents; work is specification/writing
- Checkpoint advice: After Step 2 (route taxonomy draft), pause and verify all 6 types are well-grounded in evidence before proceeding to acceptance cases

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Evidence routing route taxonomy with acceptance cases | 4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md | All 6 route types defined; each with input query, resolution path, metadata fields, pass condition, T-058 reference |
| Evidence metadata contract | 4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml | 8 required fields; each with type, description, valid value range |
| Stress-test anchor mapping | 4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv | All 29 T-058 scenarios mapped to route types; pass/fail/borderline per T-058 evidence |

## Failure / Stop Conditions
- Stop if any required asset cannot be read (file missing/empty) — write gap note in route taxonomy
- Stop if predecessor evidence is insufficient to define any of the 6 route types — write missing route as explicit gap note
- Stop if project protocol contradicts route taxonomy in an unresolvable way
- Do not produce placeholder-only deliverables with empty acceptance cases or no-op mapping
- Do not write Python implementation code
- Do not run stress tests
- Do not modify predecessor task outputs

## Notes For Delivery QA
- No-hit route must require explicit similarity thresholding; fuzzy fallback described as disallowed unless thresholded
- Transfer/suggestion route must describe user-facing semantics (reformulated queries, alternative contexts, related perturbations) not just empty results
- Distinguish deterministic fallback, proxy evidence, and LLM-assisted explanation clearly
- Route definitions must reference T-021 standard resources as the canonical input set
- All three deliverables must be registered in `4_artifact/registry.yaml` upon completion
```

### Execution Handoff: execution_handoff.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/execution_handoff.md`

```text
(missing)
```

### Artifact Registry: registry.yaml
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/registry.yaml`

```text
artifacts:
  - id: D-001
    name: Evidence routing route taxonomy with acceptance cases
    type: document
    path: 4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md
    format: markdown
    registered: "2026-06-25"
    status: ready
    notes: >
      Full route taxonomy for 6 route types (exact-hit, proxy-hit, no-hit,
      ambiguous-hit, context-missing, transfer/suggestion). Contains 21
      acceptance cases, route decision flow diagram, and distinction table
      separating deterministic, proxy, and LLM-assisted routing. All route
      definitions reference T-021 standard resources.
    dependencies: [A-001, A-002, A-003, A-004, A-005]
    acceptance_criteria:
      - All six route types defined with concrete acceptance cases
      - No-hit requires explicit similarity thresholding
      - Transfer/suggestion describes user-facing semantics
      - Route definitions reference T-021 standard resources

  - id: D-002
    name: Evidence metadata contract
    type: data
    path: 4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml
    format: yaml
    registered: "2026-06-25"
    status: ready
    notes: >
      8-field metadata contract (route_type, query_context, perturbation_resolution,
      function_response, confidence, proxy_chain, diagnostics, suggestions) with
      full type definitions, enum values, property schemas, and route-type-specific
      constraints. Includes protocol-named llm_fields and threshold_policy sections
      for LLM role limits and proxy threshold enforcement (drug Tanimoto 0.40,
      gene cosine 0.50, and cell-line lineage/subtype routing).
    dependencies: [A-003, A-004, A-005]
    acceptance_criteria:
      - All 8 fields with types descriptions and valid value ranges
      - Route-type-specific field constraints defined
      - Similarity thresholds documented in threshold_policy
      - LLM role limits documented in llm_fields

  - id: D-003
    name: Stress-test anchor mapping (T-058 scenarios → routes)
    type: table
    path: 4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv
    format: csv
    registered: "2026-06-25"
    status: ready
    notes: >
      Maps all 29 T-058 stress-test scenarios to route types with primary/secondary
      assignment, expected behavior, proxy potential, LLM dependency, acceptance
      criteria, and implementation notes. Covers all 9 dimensions from T-058:
      complex queries (3), strict queries (3), boundary queries (4), no-hit
      behavior (3), overly broad results (3), proxy/exact matching (4), difficult
      combos (3), LLM mode cross-checks (3), missing/partial index (3).
    dependencies: [A-004]
    acceptance_criteria:
      - All 29 T-058 scenarios mapped to route types
      - Pass/fail/borderline classification per T-058 evidence
      - Acceptance criteria and evidence references included

  - id: R-001
    name: Execution report
    type: report
    path: 4_artifact/3_document/execution_report_v20260625.html
    format: html
    registered: "2026-06-25"
    status: ready
    notes: >
      HTML execution report for T-064 evidence routing anchor.
    dependencies: [D-001, D-002, D-003]
    acceptance_criteria:
      - Execution report artifact exists
      - Report is registered with accepted T-064 deliverables

  - id: R-002
    name: Result report
    type: report
    path: 4_artifact/3_document/result_report_v20260625.html
    format: html
    registered: "2026-06-25"
    status: ready
    notes: >
      HTML result report for T-064 evidence routing anchor.
    dependencies: [D-001, D-002, D-003]
    acceptance_criteria:
      - Result report artifact exists
      - Report is registered with accepted T-064 deliverables

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/completion.md`

```text
# Completion — T-064 evidence_routing_anchor

Task: T-064
Phase: Digestion
Goal: goal_project_delivery_anchor
Status: Completed
Completed: 2026-06-25

## Repair Context

The OpenCode execute session entered `execute_stalled` after task-local artifacts had been repaired. Recovery verification was limited to the T-064-local deliverables listed below; predecessor task outputs, protocol files, and existing CLI sessions were not modified.

## Deliverable Summary

All three required deliverables were produced and registered:

| # | ID | Deliverable | Path | Status |
|---|---|---|---|---|
| 1 | D-001 | Evidence routing route taxonomy with acceptance cases | 4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md | Ready |
| 2 | D-002 | Evidence metadata contract | 4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml | Ready |
| 3 | D-003 | Stress-test anchor mapping (29 T-058 scenarios → routes) | 4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv | Ready |

## Acceptance Criteria Verification

| # | Criterion | Status |
|---|---|---|
| 1 | All six route types defined with concrete acceptance cases | Pass — 21 acceptance cases covering all 6 types |
| 2 | Each acceptance case includes route type, input query, expected resolution path, evidence metadata fields, pass condition | Pass — All 21 cases structured per protocol |
| 3 | Evidence metadata contract defines all 8 required response fields plus protocol-named `llm_fields` and `threshold_policy` sections | Pass — Complete YAML schema with property definitions, enum values, route-type-specific constraints, LLM role limits, and proxy threshold policy |
| 4 | Stress-test mapping covers all 29 T-058 scenarios with route type assignment and expected behavior | Pass — All 29 scenarios mapped with primary/secondary routes, acceptance criteria, evidence references |
| 5 | No-hit route requires explicit similarity thresholding; fuzzy fallback disallowed unless thresholded | Pass — Threshold enforced in route definition, AC-007 (threshold guard), AC-011 (CAP-05), and metadata contract threshold configuration |
| 6 | Transfer/suggestion route describes user-facing suggestion semantics | Pass — AC-018 through AC-021 define reformulated queries, alternative contexts, related perturbations, disambiguation, LLM-assisted and deterministic fallback suggestions |
| 7 | Route definitions reference T-021 standard resources where applicable | Pass — Canonical resource set table in taxonomy §1, cross-reference table in §6, standard resources list in metadata contract |
| 8 | All three deliverables and both HTML reports registered in 4_artifact/registry.yaml | Pass — Deliverables registered as D-001, D-002, D-003; reports registered as R-001, R-002 |

## Execution Summary

1. Read all 5 predecessor assets (A-001 through A-005) to establish evidence landscape.
2. Confirmed all 6 route types can be meaningfully defined from available evidence.
3. Defined route taxonomy with: exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion. Each type has resolution path, confidence rules, and structured acceptance cases.
4. Wrote evidence metadata contract with 8 required response fields, full property schemas, enum values, `llm_fields`, `threshold_policy`, and route-type-specific field constraints.
5. Mapped all 29 T-058 stress-test scenarios to route types with primary/secondary assignment, expected behaviors, acceptance criteria, and evidence references.
6. Registered all deliverables and HTML reports in 4_artifact/registry.yaml.

## Gaps and Caveats

1. **ambiguous-hit not covered by T-058 scenarios:** The 29 T-058 scenarios do not include a dedicated ambiguous-hit scenario. AC-012 through AC-014 define acceptance cases for gene collision, reverse near-tie, and drug multi-BRD ambiguity. Future stress-test milestones should add explicit ambiguous-hit scenarios.
2. **transfer/suggestion scenario coverage is indirect:** T-058 does not have dedicated transfer/suggestion scenarios. AC-018 through AC-021 are derived from no-hit and context-missing scenarios (SC-011, SC-012) plus gap-filling. This is acceptable because the transfer/suggestion route is triggered by no-hit or ambiguous-hit, but dedicated transfer-focused stress tests would strengthen future validation.
3. **function_index.json runtime path not verified:** T-021 rebuilt function_index.json but the runtime path alignment with the pxfquery package resolver was not verified in this task (not in scope — T-064 is specification-only).
4. **No predecessor evidence was insufficient to define any route type.** All 6 routes are well-grounded in the T-007/T-013/T-021/T-058 evidence base. No contradiction with project protocol was found.

## Predecessor Asset Usage

| Asset | Source Task | How used |
|---|---|---|
| A-001 | T-007 | Established intended resolver/proxy behavior, validated components (7/7 matrix), data readiness, development interpretation |
| A-002 | T-013 | Defined CAP-05 (no-hit false-positive) and CAP-07 (resolver blocked) as constraints; informed threshold enforcement and no-hit route design |
| A-003 | T-021 | Canonical resource set (3 matrices, 10 indexes, 5 metadata tables) used throughout all route definitions and acceptance cases |
| A-004 | T-058 | 29 scenarios mapped to route types; stress-test anchor mapping deliverable directly derived from scenario inventory |
| A-005 | T-007 | Risk constraints (LLM stability 6/9, latency 167.3s, NOT_FOUND patterns) encoded in route confidence rules and LLM-assisted boundary

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. Project protocol dir: /Users/dudu/Documents/3_Project/12_PxFquery/1_project_init/1_project_protocol
3. Current task: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor
4. Current artifact docs dir: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/3_document

Fallback path if the API response cannot be inspected but the local app is available:
- ~/.cyhex/app/protocols/cyhex_protocol.md

For `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/3_execution/`, inspect file names and directory structure first. Open specific files only if an anomaly requires it.

## 2. Task

This is not a new main state-machine stage. It is a delivery-side quality branch inside `delivery_review`.

- Project: PxFquery (P-012)
- Phase: digestion
- ID: T-064 | Name: evidence_routing_anchor
- Objective: Create the evidence-routing and non-hit/proxy/transfer behavior anchor for PxFquery. Define exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, and transfer/suggestion routes, with evidence metadata and acceptance cases for future stress-test and M3 package milestones.
- Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor

## 3. Hard Scope Boundary

You may read only inside this task directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor`

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
# AI Handoff: T-064 evidence_routing_anchor

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
# Delivery QA: T-064 evidence_routing_anchor

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
