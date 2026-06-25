#!/usr/bin/env python3
"""Step 1: Inventory all JSON files in the T-021/D-004 standard_resources bundle."""
import json
import os
from pathlib import Path

TASK_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_index_name_normalizer_v1")
BUNDLE_PATH = TASK_ROOT / "1_asset/T-021 standard_resources bundle (D-004)"
MANIFEST_PATH = TASK_ROOT / "1_asset/T-025 resource manifest (D-006).yaml"
OUTPUT_PATH = TASK_ROOT / "3_execution/01_inventory/step1_file_inventory.json"

# 7 resolver-required filenames (from pxfquery/query/resolver.py)
RESOLVER_REQUIRED = {
    "cellline_index.json", "cellline_neighbors.json",
    "gene_index_simple.json", "gene_neighbors_simple.json",
    "drug_index.json", "drug_neighbors.json",
    "function_index.json",
}

# All JSON files we expect in the bundle (10 files)
EXPECTED_JSON = RESOLVER_REQUIRED | {
    "cellline_tree.json", "gene_index.json", "gene_neighbors.json",
}

inventory = {
    "step": 1,
    "task": "T-027 index_name_normalizer_v1",
    "bundle_path": str(BUNDLE_PATH.resolve()),
    "manifest_path": str(MANIFEST_PATH.resolve()),
}

# Check bundle directory exists
if not BUNDLE_PATH.exists():
    inventory["error"] = f"Bundle path does not exist: {BUNDLE_PATH}"
    print(json.dumps(inventory, indent=2))
    OUTPUT_PATH.write_text(json.dumps(inventory, indent=2))
    exit(1)

inventory["bundle_resolves_to"] = str(BUNDLE_PATH.resolve())

# List all files
all_files = sorted(os.listdir(str(BUNDLE_PATH)))
inventory["total_files_in_bundle"] = len(all_files)
inventory["all_filenames"] = all_files

# Filter JSON files
json_files = [f for f in all_files if f.endswith(".json")]
inventory["json_file_count"] = len(json_files)
inventory["json_files"] = sorted(json_files)

# Check each expected JSON
expected_status = {}
for ef in sorted(EXPECTED_JSON):
    exists = ef in json_files
    fpath = BUNDLE_PATH / ef
    size = fpath.stat().st_size if exists else 0
    expected_status[ef] = {
        "exists": exists,
        "resolver_required": ef in RESOLVER_REQUIRED,
        "size_bytes": size,
    }
inventory["expected_json_status"] = expected_status

# Count resolver-required present
required_present = sum(1 for ef in RESOLVER_REQUIRED if ef in json_files)
inventory["resolver_required_count"] = len(RESOLVER_REQUIRED)
inventory["resolver_required_present"] = required_present
inventory["all_resolver_required_present"] = required_present == len(RESOLVER_REQUIRED)

# File size summary
file_sizes = {}
for f in json_files:
    fpath = BUNDLE_PATH / f
    file_sizes[f] = fpath.stat().st_size
inventory["json_file_sizes_bytes"] = file_sizes

print(json.dumps(inventory, indent=2))
OUTPUT_PATH.write_text(json.dumps(inventory, indent=2))
print(f"\nInventory written to: {OUTPUT_PATH}")