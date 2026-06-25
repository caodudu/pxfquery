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