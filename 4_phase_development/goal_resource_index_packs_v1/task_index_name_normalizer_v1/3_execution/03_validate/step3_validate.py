#!/usr/bin/env python3
"""Step 3: Validate the normalized T-027 index pack."""
import json
import os
import sys
from pathlib import Path

TASK_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_index_name_normalizer_v1")
INDEX_DIR = TASK_ROOT / "4_artifact/2_persist/pxfquery_T027_runtime_query_index"
OUTPUT_PATH = TASK_ROOT / "3_execution/03_validate/step3_validation.json"

# 7 resolver-required filenames (from pxfquery/query/resolver.py + reverse.py)
RESOLVER_REQUIRED = {
    "cellline_index.json", "cellline_neighbors.json",
    "gene_index_simple.json", "gene_neighbors_simple.json",
    "drug_index.json", "drug_neighbors.json",
    "function_index.json",
}

result = {
    "step": 3,
    "task": "T-027 index_name_normalizer_v1",
    "index_dir": str(INDEX_DIR),
    "passed": False,
}

if not INDEX_DIR.exists():
    result["error"] = f"Index directory not found: {INDEX_DIR}"
    OUTPUT_PATH.write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    sys.exit(1)

# 1. List all symlinks
entries = sorted(os.listdir(str(INDEX_DIR)))
symlink_details = []
for entry in entries:
    fpath = INDEX_DIR / entry
    is_link = fpath.is_symlink()
    if not is_link:
        symlink_details.append({"name": entry, "is_symlink": False})
        continue
    target = os.readlink(str(fpath))
    target_exists = (fpath.resolve().exists())
    target_size = fpath.resolve().stat().st_size if target_exists else 0
    symlink_details.append({
        "name": entry,
        "is_symlink": True,
        "target": target,
        "target_exists": target_exists,
        "target_size_bytes": target_size,
    })

result["all_entries"] = symlink_details

# 2. Check all 7 resolver-required filenames present
filenames_present = {entry for entry in entries if (INDEX_DIR / entry).exists()}
required_status = {}
for rf in sorted(RESOLVER_REQUIRED):
    present = rf in filenames_present
    fpath = INDEX_DIR / rf
    if present and fpath.is_symlink():
        target = os.readlink(str(fpath))
        target_resolvable = (fpath.resolve().exists())
    else:
        target = None
        target_resolvable = False
    required_status[rf] = {
        "present": present,
        "is_symlink": fpath.is_symlink() if fpath.exists() else False,
        "target": target,
        "target_resolvable": target_resolvable,
    }
result["resolver_required_status"] = required_status

# 3. JSON load validation (Python-honest load)
json_load_status = {}
for fname in entries:
    fpath = INDEX_DIR / fname
    if not (fpath.exists() and fname.endswith(".json")):
        continue
    try:
        with open(str(fpath), "r", encoding="utf-8") as f:
            data = json.load(f)
        # Capture top-level key shape (str repr, sample keys only)
        if isinstance(data, dict):
            keys = list(data.keys())[:10]
            size = len(data)
        elif isinstance(data, list):
            keys = f"list[{len(data)}]"
            size = len(data)
        else:
            keys = type(data).__name__
            size = None
        json_load_status[fname] = {
            "valid_json": True,
            "type": type(data).__name__,
            "top_level_keys_sample": keys,
            "size_estimate": size,
        }
    except Exception as e:
        json_load_status[fname] = {
            "valid_json": False,
            "error": str(e),
        }
result["json_load_status"] = json_load_status

# 4. Final pass/fail summary
all_required_present = all(s["present"] for s in required_status.values())
all_required_resolvable = all(s["target_resolvable"] for s in required_status.values())
all_required_valid_json = all(
    json_load_status.get(rf, {}).get("valid_json") is True
    for rf in RESOLVER_REQUIRED
)
result["checks"] = {
    "all_required_present": all_required_present,
    "all_required_resolvable": all_required_resolvable,
    "all_required_valid_json": all_required_valid_json,
    "all_json_files_valid": all(v.get("valid_json") for v in json_load_status.values()),
}
result["passed"] = all([
    result["checks"]["all_required_present"],
    result["checks"]["all_required_resolvable"],
    result["checks"]["all_required_valid_json"],
    result["checks"]["all_json_files_valid"],
])

# 5. Resolver-accept check (file presence only — does not load QueryResolver)
result["resolver_acceptance"] = {
    "tested_with_QueryResolver_init": False,
    "reason": "Resolver init requires LLM client + loaded AnnData matrices (out of scope for this task). Acceptance verified by filename-only check.",
    "resolver_required_filenames": sorted(RESOLVER_REQUIRED),
    "all_filenames_present_in_index_dir": sorted(filenames_present),
    "index_dir_is_valid_index_dir": all_required_present,
}

OUTPUT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False))
print(json.dumps(result, indent=2, ensure_ascii=False))
print(f"\nValidation result: {'PASSED' if result['passed'] else 'FAILED'}")
