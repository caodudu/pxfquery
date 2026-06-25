# Check Handoff Before Exec: T-042 contract_and_demo_spec_m1

## Check Verdict
green_check

## CyHex Boundaries
- Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_contract_and_demo_spec_m1`
- Allowed write dirs: `3_execution/`, `4_artifact/`, `5_report/`; plus `2_protocol/2_protocol_split/protocol.md`, `2_protocol/3_asset_rule/asset_rule.yaml`, `1_asset/registration.yaml`
- Forbidden dirs: `2_project_asset/`, `/Users/dudu/Documents/3_Project/8_functional_query`, any T024-T040 path under `goal_package_foundation_v1/`, `goal_resource_index_packs_v1/`, `goal_deterministic_query_engines_v1/`, `goal_resolver_optional_layer_v1/`, `goal_package_milestone_merge_v1/`
- Required registry: `1_asset/registration.yaml` (7 assets, all ok)
- Must stop if: T-007/T-013 artifacts are missing/contradictory for deterministic contract; raw project asset read is needed; work drifts into implementation/matrix analysis/index rebuilding; demo-case details can't be traced to T-007/T-013 without guessing

## Objective Restatement
Produce a compact M1 API/CLI/demo-spec contract from T-007 (development intent/state) and T-013 (MVP capability/limits). Deliver exact function signatures, CLI commands, one forward + one reverse demo case with JSON shapes, no-hit/error behavior, and pass/fail criteria. No code implementation, no product redesign, no T024-T040 references.

## Selected Inputs
| Asset ID | Path | Why needed | Preflight status |
|---|---|---|---|
| A-001 | `1_asset/t007_development_source_map.md` | Package identity, source priority, carry-forward boundaries | ok |
| A-002 | `1_asset/t007_development_state_report.md` | Component readiness, (B,P,F) model, implemented classes | ok |
| A-003 | `1_asset/t007_development_gap_and_risk_list.md` | Cross-check unsafe claims, scope boundaries (optional) | ok |
| A-004 | `1_asset/t013_mvp_capability_contract.md` | M1 required/gated/forbidden capabilities | ok |
| A-005 | `1_asset/t013_failure_missing_capability_list.md` | Negative cases, known failure modes | ok |
| A-006 | `1_asset/t013_capability_status_matrix.csv` | Tabular pass/fail cross-check (optional) | ok |
| A-007 | `1_asset/t013_run_evidence_bundle` | Prior forward/reverse/no-hit shape reference (optional) | ok |

## Execution Strategy
1. Read A-001, A-002, A-004, A-005 first; then A-003, A-006, A-007 only as cross-checks.
2. Extract M1-relevant facts: package purpose, (B,P,F) model, forward/reverse intent, biological context fields, deterministic evidence boundaries, known missing capabilities, unsafe claims to avoid.
3. Write `4_artifact/2_persist/m1_api_contract.yaml` with function names, parameter schemas, return shapes, error/no-hit output structures.
4. Write CLI contract section in same YAML: commands, flags, demo invocations, exit codes, error behavior.
5. Write `4_artifact/2_persist/m1_demo_cases.yaml` with exactly one forward case and one reverse case: input fields, expected output JSON shape, minimum semantic content, pass/fail assertions.
6. Define no-hit, ambiguous input, missing index, missing resource, unsupported query, low-confidence behavior as deterministic contract-level structures.
7. Write `4_artifact/3_document/m1_contract_summary.md` for human readability.
8. Register all outputs in `4_artifact/registry.yaml`; write `5_report/completion.md`.

## Conservative Execution Advice
- Start with: Read A-001 and A-004 first — they define the package identity anchor and M1 capability boundaries. Draft the (B,P,F) model and forward/reverse intent summary before writing any YAML.
- Smoke/demo command or method: Draft one forward and one reverse output JSON shape from A-002 (core.py function signatures) before finalizing the full contract.
- Full run only after: Primary assets read and M1-relevant facts extracted. Do not write all 5 deliverables before confirming the API shape is traceable to T-007/T-013.
- Cost/time risk: Negligible — spec task with no compute, no network, no LLM calls. Time estimate ~2-4 hours for all 5 deliverables.
- Checkpoint advice: After step 2, verify that the extracted (B,P,F) model and forward/reverse intent are consistent with A-001 §Operational Asset Map and A-004 Required MVP Behavior before writing contract YAML.

## Expected Deliverables
| Deliverable | Target path | Acceptance signal |
|---|---|---|
| Structured API + CLI contract | `4_artifact/2_persist/m1_api_contract.yaml` | Specifies exact function names, args, return JSON shape, error/no-hit shape; CLI has command names, flags, exit codes |
| Forward + reverse demo cases | `4_artifact/2_persist/m1_demo_cases.yaml` | One forward case (B,P → F) and one reverse case (B,F → P); concrete inputs, expected output JSON, pass/fail assertions |
| Human-readable contract summary | `4_artifact/3_document/m1_contract_summary.md` | Compact summary of API, CLI, demo cases, and contract scope |
| Artifact registry | `4_artifact/registry.yaml` | All accepted/reusable outputs registered with IDs |
| Completion note | `5_report/completion.md` | Summarizes what was delivered, any missing preconditions, and handoff assumptions |

## Failure / Stop Conditions
- Stop if protocol cannot be defined without reading `2_project_asset/` or legacy source root.
- Stop if T-007 and T-013 are too contradictory to produce a deterministic contract (record gap in completion.md).
- Stop if work drifts into package code implementation, matrix analysis, index rebuilding, or T024-T040 citations.
- Stop if demo-case details require guessing biological/input specifics not traceable to T-007/T-013.

## Notes For Delivery QA
- The contract is for downstream M1 implementation tasks (T048, T049, T052). Any uncertain biological detail must be expressed as a validation requirement, not a guess.
- Natural-language resolver success is NOT an acceptance dependency for M1 release (only deterministic forward/reverse + CLI).
- No LLM API calls, web search, or network access needed. All evidence is local.
- Previously repaired config (config_repair_20260624.md). The current protocol, registry, and asset rules are consistent.
