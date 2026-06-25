# Forward Query Core Repair Report

Generated: 2026-06-24

## Replacement Role

T-059 replaces T-048 for downstream M1 forward-query work. T-048 was used only as an incident reference showing that the registered T-046 fixture lacks the T-042 required `EGFR/A549/xpr` positive case.

## Repair Substrate

The repair substrate is task-local:

- `4_artifact/2_persist/forward_repair_manifest_m1_1.yaml`
- `4_artifact/2_persist/forward_repair_fixture_m1_1/`

The fixture is a compatibility-preserving copy of the T-043 fixture package with one appended xpr row:

- `sig_id`: `T059_SYNTHETIC_EGFR_A549_XPR`
- `perturbation`: `EGFR`
- `cell_line`: `A549`
- `matrix_type`: `xpr`
- provenance label: `synthetic_repair_contract_bridge`

The synthetic row uses T-042 shape-example scores only to satisfy the demo contract. It is not original LINCS/raw data and must not be used as biological evidence.

## Implementation

The package under `4_artifact/1_package/` preserves the T-044 package name and src-layout. It copies the T-046 `M1FixtureLoader` implementation and uses that loader API for fixture access. `PxFquery.pert2func()` returns the T-042 forward result shape for exact hits and structured JSON error/no-hit objects for missing inputs.

## Upstream Boundary

No T-042, T-043, T-044, T-046, T-047, or T-048 output directory was modified. No `2_project_asset/` raw assets or T024-T040 blocked assets were used.
