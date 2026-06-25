# AI Handoff: T-059 forward_query_core_repair_m1

## Task Goal

T-059 is the same-layer replacement for the blocked T-048 forward-query task. It delivers an M1 forward-query package plus a task-local synthetic repair substrate that satisfies the T-042 required `EGFR/A549/xpr` positive demo without modifying upstream completed task outputs.

## What Was Delivered

- Implemented package source and metadata under `4_artifact/1_package/`.
- Task-local repair manifest and fixture under `4_artifact/2_persist/`.
- Positive-hit and no-hit structured JSON evidence under `4_artifact/2_persist/`.
- Contract assertion table under `4_artifact/5_table/`.
- Provenance and human-readable reports under `4_artifact/3_document/`.
- Registered reusable outputs in `4_artifact/registry.yaml`.

## Core Artifacts

| ID | Path | Why it matters | How to reuse |
|---|---|---|---|
| D-001 | `4_artifact/1_package/` | Authoritative T-059 forward-query package replacing T-048 for downstream M1 work. | Use as the package source for future M1 forward-query integration or tests. |
| D-002 | `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml` | Declares the synthetic repair provenance and fixture bridge. | Read before using the repair fixture; preserve the synthetic_repair label. |
| D-003 | `4_artifact/2_persist/forward_repair_fixture_m1_1/` | Loader-compatible task-local fixture containing the minimal EGFR/A549/xpr bridge row. | Use as the fixture root for T-059 demos and smoke tests. |
| D-004 | `4_artifact/2_persist/forward_query_positive_demo_evidence_v20260624.json` | Shows the required positive demo returns `found=true`. | Use as acceptance evidence for the T-042 positive forward demo. |
| D-005 | `4_artifact/2_persist/forward_query_no_hit_evidence_v20260624.json` | Shows structured no-hit behavior without traceback. | Use as acceptance evidence for no-hit/error behavior. |
| D-006 | `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` | Consolidates validation assertions and pass/fail outcomes. | Read first when checking whether T-059 met the contract. |
| D-007 | `4_artifact/3_document/forward_query_core_repair_report_v20260624.md` | Explains the T-048 replacement role, provenance, and limits. | Use for downstream planning and provenance review. |

## Supporting Artifacts

- D-008 `4_artifact/3_document/execution_report_v20260624.html`: human-readable execution and validation summary.
- D-009 `4_artifact/3_document/result_report_v20260624.html`: human-readable result summary.
- `5_report/completion.md`: completion summary and boundary statement.
- `5_report/delivery_qa.md`: delivery-side QA result.

## Downstream Use

Use T-059, not T-048, as the accepted forward-query core repair source for M1 downstream tasks. Treat the repair fixture as a minimal contract bridge for runnable demos and tests, not as original LINCS/raw biological evidence.

## Known Limits / Risks

- The added `EGFR/A549/xpr` content is `synthetic_repair` and exists only to bridge the T-042 demo contract.
- The repair fixture does not establish biological ranking validity or full-resource coverage.
- No upstream completed outputs were modified; do not infer that T-043/T-046 now natively contain the positive demo case.

## Do Not Read / Do Not Reuse

- Do not reuse T-048 `4_artifact/` as accepted output.
- Do not use T024-T040 blocked assets for this line of work.
- Do not treat project raw assets under `2_project_asset/` as inputs unless a future task explicitly authorizes and registers that use.
- Do not strip or rename the `synthetic_repair` provenance when reusing the repair fixture.

## Recommended Next Reads

1. `4_artifact/registry.yaml`
2. `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv`
3. `4_artifact/3_document/forward_query_core_repair_report_v20260624.md`
4. `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml`
5. `5_report/completion.md`
