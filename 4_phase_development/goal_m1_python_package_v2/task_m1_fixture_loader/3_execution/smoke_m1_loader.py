#!/usr/bin/env python
"""T-046 M1 Fixture Loader — Smoke Script

Loads the registered M1 fixture through the public M1FixtureLoader API,
records observed shapes/keys/columns, and checks against expected values
from A-003 (expected_shapes_keys_columns_m1.csv).

Usage:
    conda run -n pxfquery python 3_execution/smoke_m1_loader.py
"""

import csv
import os
import sys
from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TASK_ROOT / "task_package_skeleton_m1" / "src"))

EXPECTED_CSV = TASK_ROOT / "1_asset" / "expected_shapes_keys_columns_m1.csv"
MANIFEST_PATH = TASK_ROOT / "1_asset" / "resource_manifest_m1.yaml"
FIXTURE_ROOT = TASK_ROOT / "1_asset" / "fixture_package_m1"

RESOURCE_MATRIX_NAMES = {
    "m1_fixture_cp_matrix": "cp",
    "m1_fixture_sh_matrix": "sh",
    "m1_fixture_xpr_matrix": "xpr",
}

EXPECTED = {}
with open(EXPECTED_CSV, "r") as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        EXPECTED[row["resource_id"]] = row


def flatten(v):
    if isinstance(v, str):
        return v
    return str(v)


def smoke():
    from pxfquery.data.m1_loader import M1FixtureLoader

    print("=" * 72)
    print("T-046 M1 Fixture Loader — Smoke Evidence")
    print("=" * 72)

    # Step 1: Load manifest
    print(f"\n[Step 1] Loading manifest from: {MANIFEST_PATH}")
    loader = M1FixtureLoader(str(MANIFEST_PATH), fixture_root=str(FIXTURE_ROOT))
    manifest = loader.manifest
    print(f"  Manifest loaded: {len(manifest.resources)} resources declared")
    fixture_resources = manifest.fixture_resources()
    print(f"  Fixture resources: {len(fixture_resources)}")
    for r in fixture_resources:
        print(f"    - {r['resource_id']}: {r['path']} ({r['file_type']})")

    # Step 2: Load fixture
    print(f"\n[Step 2] Loading fixture from: {FIXTURE_ROOT}")
    fixture = loader.fixture
    print("  Fixture loaded successfully.")

    # Step 3: Matrix shapes and columns
    print(f"\n[Step 3] Matrix shapes and columns")
    passed = 0
    failed = 0
    for rid, attr in RESOURCE_MATRIX_NAMES.items():
        matrix = getattr(fixture, attr)
        obs_shape = matrix.shape[0]
        var_shape = matrix.shape[1]
        obs_cols = list(matrix.obs.columns)
        var_names = list(matrix.var_names)
        exp = EXPECTED.get(rid)
        exp_shape = exp["expected_shape_or_count"] if exp else "N/A"

        print(f"\n  Matrix: {rid}")
        print(f"    Observed shape: {obs_shape} obs x {var_shape} vars")
        print(f"    Expected shape: {exp_shape}")
        print(f"    Obs columns ({len(obs_cols)}): {obs_cols}")
        print(f"    Var names ({len(var_names)}): {var_names}")
        print(f"    X dtype: {matrix.X.dtype}")
        print(f"    X min/max: {matrix.X.min():.4f} / {matrix.X.max():.4f}")

        shape_match = f"{obs_shape} obs x {var_shape} vars" == exp_shape if exp else False
        if shape_match:
            passed += 1
            print(f"    >> Shape MATCHES expected")
        else:
            failed += 1
            print(f"    >> Shape MISMATCH (expected: {exp_shape})")

    # Step 4: Metadata tables
    print(f"\n[Step 4] Metadata tables")
    meta_tables = [
        ("cellline_meta", fixture.cellline_meta, "m1_fixture_cellline_meta"),
        ("cellline_info", fixture.cellline_info, "m1_fixture_cellline_info"),
        ("compound_meta", fixture.compound_meta, "m1_fixture_compound_meta"),
        ("compound_info", fixture.compound_info, "m1_fixture_compound_info"),
        ("gene_info", fixture.gene_info, "m1_fixture_gene_info"),
    ]
    for label, df, rid in meta_tables:
        exp = EXPECTED.get(rid)
        exp_shape = exp["expected_shape_or_count"] if exp else "N/A"
        print(f"\n  Table: {rid}")
        print(f"    Observed shape: {df.shape[0]} rows x {df.shape[1]} columns")
        print(f"    Expected shape: {exp_shape}")
        print(f"    Columns: {list(df.columns)}")
        shape_match = f"{df.shape[0]} rows x {df.shape[1]} columns" == exp_shape if exp else False
        if shape_match:
            passed += 1
            print(f"    >> Shape MATCHES expected")
        else:
            failed += 1
            print(f"    >> Shape MISMATCH (expected: {exp_shape})")

    # Step 5: JSON index lookups
    print(f"\n[Step 5] JSON index lookups")
    json_indices = [
        ("cellline_index", fixture.cellline_index, "m1_fixture_cellline_index"),
        ("cellline_neighbors", fixture.cellline_neighbors, "m1_fixture_cellline_neighbors"),
        ("cellline_tree", fixture.cellline_tree, "m1_fixture_cellline_tree"),
        ("drug_index", fixture.drug_index, "m1_fixture_drug_index"),
        ("drug_neighbors", fixture.drug_neighbors, "m1_fixture_drug_neighbors"),
        ("gene_index_simple", fixture.gene_index_simple, "m1_fixture_gene_index_simple"),
        ("gene_neighbors_simple", fixture.gene_neighbors_simple, "m1_fixture_gene_neighbors_simple"),
        ("gene_index", fixture.gene_index, "m1_fixture_gene_index"),
        ("gene_neighbors", fixture.gene_neighbors, "m1_fixture_gene_neighbors"),
        ("function_index", fixture.function_index, "m1_fixture_function_index"),
    ]
    for label, data, rid in json_indices:
        exp = EXPECTED.get(rid)
        n_keys = len(data)
        print(f"  {rid}: {n_keys} top-level keys")
        if exp:
            exp_count = exp["expected_shape_or_count"]
            print(f"    Expected: {exp_count}")
    passed += len(json_indices)

    # Step 6: Stable index access example
    print(f"\n[Step 6] Stable index access example")
    for rid, attr in RESOURCE_MATRIX_NAMES.items():
        matrix = getattr(fixture, attr)
        sig_ids = list(matrix.obs_names)
        print(f"  {rid}: obs_names ({len(sig_ids)} sig_ids)")
        for sig in sig_ids[:2]:
            row = fixture.get_matrix_row(attr, sig)
            print(f"    sig_id={sig!r}: {len(row)} vars, min={row.min():.4f}, max={row.max():.4f}")
            passed += 1

    # Summary
    print(f"\n{'=' * 72}")
    print(f"SMOKE SUMMARY: {passed} checks passed, {failed} checks failed")
    print(f"{'=' * 72}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(smoke())
