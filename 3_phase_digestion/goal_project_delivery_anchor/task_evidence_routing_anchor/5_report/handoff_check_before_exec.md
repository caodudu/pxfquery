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