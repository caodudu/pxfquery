# Blocked: T-048 forward_query_core_m1

## What Was Completed

- Contract and demo requirements were extracted from the registered T-042 assets.
- T-046 loader API documentation and loader implementation were inspected through registered task assets.
- A task-local forward query implementation was created under `4_artifact/1_package/pxfquery/`.
- A rerunnable evidence script was created under `3_execution/run_forward_query_evidence_v20260624.py`.
- Structured observed evidence and assertion CSV were generated under `4_artifact/`.

## Failed Step

Step 4 failed: run the required T-042 forward demo case and assert it against the contract.

Required input:

- `perturbation="EGFR"`
- `cell_line="A549"`
- `matrix_type="xpr"`

Observed result:

- `4_artifact/2_persist/forward_query_demo_evidence_v20260624.json` records `error="PerturbationNotFound"`.
- `4_artifact/5_table/forward_query_contract_assertions_v20260624.csv` records forward demo assertions as `FAIL`.

## Exact Evidence

The loader-exposed `xpr` matrix has shape `[4, 7]` and these signature IDs:

- `XPR025_BICR6.311_96H:E13`
- `XPR028_PC3.311B_96H:J15`
- `XPR015_A375.311_96H:E11`
- `XPR031_U251MG.311_96H:E03`

The observed `xpr` rows are:

| cell_iname | cmap_name |
|---|---|
| BICR6 | STAC |
| PC3 | SLC19A3 |
| A375 | CPVL |
| U251MG | ORAI3 |

There is no `EGFR` perturbation and no `A549` cell line in the loader-exposed `xpr` matrix. The observed count for EGFR/A549 rows is `0`.

## Why Later Steps Cannot Continue

The protocol requires the exact T-042 forward demo case to produce `found=true`, non-empty `top_activated`, and non-empty `top_suppressed`. Producing that output from the current fixture would require changing the contract, changing the fixture, or bypassing the T-046 loader. All three are forbidden in the current task.

Because the demo evidence cannot pass, the HTML reports, final registry, and complete downstream handoff would be misleading if written as accepted deliverables.

## Required Revision

Revise the task inputs by either:

- registering a loader-compatible fixture with an EGFR/A549/xpr row;
- revising T-042/A-002 to specify a demo hit that exists in the T-046 fixture; or
- approving a new matrix type and exact demo case in the contract.

## Stage Incident 2026-06-24T05:06:46

- sub_status: `execute_config_mismatch`
- reason: T048 cannot satisfy T042 forward demo contract with T046 fixture: required EGFR/A549/xpr hit is absent from loader-exposed fixture matrices.

### Evidence

See task_forward_query_core_m1/5_report/blocked.md and 4_artifact/5_table/forward_query_contract_assertions_v20260624.csv. EGFR/A549 matching rows in xpr fixture: 0.
