# Execution Prompt
Generated: 2026-06-25 12:20

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
sub_status: check_approved
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
artifacts: []

```

### Completion Report: completion.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/completion.md`

```text
# Completion

Pending.

```

### Delivery QA Report: delivery_qa.md
Path: `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/delivery_qa.md`

```text
(missing)
```


Legacy source paths, for anomaly-only fallback:

1. ~/.cyhex/app/protocols/cyhex_protocol.md
2. ~/.cyhex/profile.yaml
3. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/handoff_check_before_exec.md        <- Read this first; it is the checking AI's execution strategy and risk guidance.
4. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/execution_handoff.md        <- If this session needs a long-context handoff, write it here before stopping.
5. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/2_protocol_split/protocol.md
6. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/1_asset/registration.yaml
7. /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/2_protocol/3_asset_rule/asset_rule.yaml

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
Task: T-064 evidence_routing_anchor
Status: active | Executor: hybrid
Objective: Create the evidence-routing and non-hit/proxy/transfer behavior anchor for PxFquery. Define exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, and transfer/suggestion routes, with evidence metadata and acceptance cases for future stress-test and M3 package milestones.
Task path: /Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor

The task is complete only when all protocol deliverables are produced or explicitly reported as impossible.

The core deliverable is important, but it is not the only deliverable. Do not produce only the core deliverable and claim full completion.

## 3. Embedded Task Contract

### Protocol
---
### protocol.md
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

### Selected Assets (0)
(none)

### Asset Rules

### Required
- 4_artifact/2_persist/pxfquery_development_state_report_v20260617.md — Intended resolver/proxy/exact routing behavior, known gaps, and current PxFquery package identity needed to define route semantics.
- 4_artifact/2_persist/pxfquery_t013_failure_missing_capability_list_v20260618.md — Specific capability failures (CAP-05 no-hit false-positive, CAP-07 resolver blocked) that must be addressed in route definitions.
- 4_artifact/2_persist/pxfquery_standard_resource_guide_v20260623.md — Canonical standard resource definitions (matrices, indexes, metadata tables) that route behavior must reference.
- 4_artifact/2_persist/stress_test_development_handoff_pack_v20260624.md — 29 stress-test scenarios with hit-level categories needed to produce stress-test anchor mapping.
- 4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md — Known risks (LLM stability, latency, NOT_FOUND patterns) to encode in route constraints.
### Forbidden
- legacy source root directories
- predecessor 2_protocol/ directories
- predecessor 1_asset/ directories
- predecessor 3_execution/ directories
### Output
- 4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md
- 4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml
- 4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv

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

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/registry.yaml`

Required reports:

1. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/3_document/execution_report_v{YYYYMMDD}.html`
2. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/4_artifact/3_document/result_report_v{YYYYMMDD}.html`
3. `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/completion.md`

The HTML reports are required unless the task is blocked before producing deliverables.

Default language for the two HTML reports is Chinese. Use another language only when the task protocol or human instruction explicitly requires it. The reports should be human-readable, structured, and suitable for quick review by the project owner.

## 9. Truthfulness Rules

Never claim completion for work that was not performed.

Never hide failed commands, missing assets, skipped steps, empty files, placeholder outputs, or untested assumptions.

If only part of the task is complete, say it is partial.

If execution cannot continue, write:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/blocked.md`

Include:

- what was completed
- which step failed
- exact evidence
- why later steps cannot continue
- what revision or input is needed

Then report a stage incident if possible:

`POST /api/projects/12_PxFquery/tasks/goal_project_delivery_anchor/task_evidence_routing_anchor/stage_incident`

Use:

- `failed` for task failure
- `capability_failed` for missing tools, permissions, accounts, network, or model capability
- `config_mismatch` for protocol, prompt, asset registry, or task graph contradictions

## 10. Long Context Handoff

If the execution session becomes too long or state is becoming hard to preserve, stop cleanly.

Write or update:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor/5_report/execution_handoff.md`

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
