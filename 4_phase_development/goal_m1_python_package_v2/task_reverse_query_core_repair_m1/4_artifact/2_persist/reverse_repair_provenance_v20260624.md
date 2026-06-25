# Reverse Repair Substrate Provenance

Task: T-060 reverse_query_core_repair_m1
Generated: 2026-06-24

## Purpose

This substrate exists only to repair the T-042 reverse positive demo path that T-049 could not satisfy from the previously selected fixture coverage. The repair target is the reverse query case:

- activate: `HALLMARK_APOPTOSIS`
- suppress: `HALLMARK_MYC_TARGETS_V1`
- cell line: `A549`
- matrix type: `xpr`

## Copied From Registered Inputs

The repair package under `4_artifact/2_persist/reverse_repair_fixture_m1_1/` copies the registered T-043 fixture package sidecar files from A-004:

- cell line CSV/JSON sidecars
- compound CSV/JSON sidecars
- gene CSV/JSON sidecars
- function index JSON sidecar
- original cp, sh, and xpr matrix structure before task-local repair columns/rows were added

These copied files are predecessor-derived fixture support, not new raw data.

## Synthetic / Repair Content

The following content is task-local synthetic repair support:

- Added matrix variables in cp, sh, and xpr: `HALLMARK_MYC_TARGETS_V1` and `NON_DIFFERENTIALLY_SCORED_PROGRAM`.
- Added 10 synthetic A549 xpr candidate rows for the T-042 reverse positive demo.
- Added one synthetic A549 low-confidence xpr control row.
- Added `repair_provenance` metadata on synthetic xpr rows.

The synthetic scores were chosen only to create deterministic reverse-query behavior for the contract bridge. They are not original LINCS, CMAP, or biological measurements and must not be cited or reused as empirical evidence.

## Loader Compatibility

The substrate is readable by the accepted T-046 `M1FixtureLoader` implementation when called with:

```text
M1FixtureLoader("4_artifact/2_persist/reverse_repair_manifest_m1_1.yaml",
                fixture_root="4_artifact/2_persist/reverse_repair_fixture_m1_1")
```

The validation evidence confirms the repair xpr matrix shape is 15 observations x 9 variables, includes A549 rows, and includes `HALLMARK_MYC_TARGETS_V1`.

## Boundary Statement

No upstream completed artifacts were modified. No project-level raw assets, legacy roots, web sources, or T024-T040 blocked assets were used.
