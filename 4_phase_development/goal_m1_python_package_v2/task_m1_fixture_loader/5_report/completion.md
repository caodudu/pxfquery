# Completion Report — T-046 m1_fixture_loader

## Summary

Implemented a minimal, reusable M1 fixture loader (`M1FixtureLoader`) in the `pxfquery.data.m1_loader` module within the existing M1 Python package skeleton. The loader reads the T-043 manifest and fixture package, validates structure against A-003 expected shapes, and exposes stable matrix/index access APIs suitable for downstream T-048/T-049 use.

## Implementation

### Loader Code
- **Module:** `task_package_skeleton_m1/src/pxfquery/data/m1_loader.py`
- **Public classes:** `M1FixtureLoader`, `M1Fixture`, `M1Manifest`
- **Re-exports in:** `pxfquery.data.__init__` (updated to export new symbols)

The API reads a T-043 `resource_manifest_m1.yaml` manifest and a `fixture_package_m1/` directory, returning documented dataclass objects with AnnData matrices, pandas DataFrames, and dict-based JSON indices. Convenience methods (`matrix_shape`, `get_matrix_row`, etc.) provide stable access for downstream tasks.

The package was installed in dev mode (`pip install -e`) in the project conda environment.

### Smoke Evidence

A smoke script (`3_execution/smoke_m1_loader.py`) loads the registered fixture and validates:

| Check type | Count | Result |
|---|---|---|
| Matrix shapes | 3 | All PASS (4x7) |
| Metadata table shapes | 5 | All PASS |
| JSON index key counts | 10 | All PASS |
| Stable index access examples | 6 | All PASS |
| **Total** | **24** | **24/24 PASS** |

All observed shapes, columns, and key counts match the A-003 expected-shapes reference exactly.

### Environment Changes

- `pxfquery` package re-installed as editable from `task_package_skeleton_m1/` (was pointing to old `goal_package_foundation_v1` path).
- Stale editable-install pth files from T-024 and T-032 cleaned from site-packages.
- No new packages installed.

## Deliverables

| Deliverable | Path | Status |
|---|---|---|
| Loader code | `task_package_skeleton_m1/src/pxfquery/data/m1_loader.py` | Accepted |
| API documentation | `4_artifact/2_persist/API_REFERENCE_v20260624.md` | Accepted |
| Smoke evidence table | `4_artifact/5_table/smoke_evidence_observed_vs_expected_v20260624.csv` | Accepted |
| Smoke script | `3_execution/smoke_m1_loader.py` | Accepted |
| Smoke output log | `3_execution/smoke_output.txt` | Accepted |
| Artifact registry | `4_artifact/registry.yaml` | Updated (5 artifacts) |
| Completion report | `5_report/completion.md` | This file |

## Acceptance Criteria Met

1. **Manifest-driven loading:** Loader reads the registered T-043 manifest and fixture package; no hardcoded paths.
2. **Stable API:** `M1FixtureLoader` exposes `manifest` and `fixture` properties with documented matrix/index access methods.
3. **Smoke evidence:** Records all observed shapes, key names, columns, and stable sig_id row access.
4. **Contract check:** All 24 checks match A-003 expected values.
5. **Scope discipline:** No private query/ranking logic, no raw project-asset reads, no schema invention.

## Scope Limitations

- Fixture loading only; no full-resource hardening.
- No biological ranking or interpretation.
- No query/index resolver integration (reserved for T-048/T-049).

## Stop Rules Compliance

- A-001, A-002, A-003: present and consistent (no stop required).
- No `2_project_asset/` reads performed.
- Package layout identified within project boundary.
- T-043 fixture contract followed without schema invention.
- No expensive/networked/downstream operations attempted.
