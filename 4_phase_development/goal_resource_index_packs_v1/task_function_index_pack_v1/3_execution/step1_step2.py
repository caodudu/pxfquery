"""
T-028 Step 1: Verify 91-term matrix var source
T-028 Step 2: Read upstream function_index.json
"""
import json, os, sys

import anndata as ad

TASK = "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_function_index_pack_v1"
BUNDLE = os.path.join(TASK, "1_asset", "T-021 standard_resources bundle (D-004)")

# Step 1: load var_names from all three H5AD matrices
var_names_by_matrix = {}
for name in ["cp_func_ad", "sh_func_ad", "xpr_func_ad"]:
    fpath = os.path.join(BUNDLE, f"{name}.h5ad")
    if not os.path.exists(fpath):
        print(f"ERROR: {fpath} not found", file=sys.stderr)
        sys.exit(1)
    a = ad.read_h5ad(fpath)
    vn = list(a.var_names)
    var_names_by_matrix[name] = {
        "n_var": len(vn),
        "var_names": vn,
        "dtype": str(a.X.dtype),
        "shape": list(a.shape)
    }
    print(f"  {name}: n_var={len(vn)}, dtype={a.X.dtype}, shape={a.shape}")

all_same = all(
    var_names_by_matrix["cp_func_ad"]["var_names"] == v["var_names"]
    for v in var_names_by_matrix.values()
)
assert all_same, "var_names mismatch across matrices!"
assert len(var_names_by_matrix["cp_func_ad"]["var_names"]) == 91, \
    f"Expected 91, got {len(var_names_by_matrix['cp_func_ad']['var_names'])}"

observed_vars = var_names_by_matrix["cp_func_ad"]["var_names"]

step1 = {
    "step": "01_verify_matrix_var_source",
    "cp_var_names": var_names_by_matrix["cp_func_ad"]["var_names"],
    "sh_var_names": var_names_by_matrix["sh_func_ad"]["var_names"],
    "xpr_var_names": var_names_by_matrix["xpr_func_ad"]["var_names"],
    "n_var": len(observed_vars),
    "all_three_identical": all_same,
    "dtypes": {k: v["dtype"] for k, v in var_names_by_matrix.items()},
    "shapes": {k: v["shape"] for k, v in var_names_by_matrix.items()},
}

out_dir = os.path.join(TASK, "3_execution", "01_verify")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "01_var_names.json"), "w") as f:
    json.dump(step1, f, indent=2, ensure_ascii=False)
print(f"\nStep 1 done. n_var={len(observed_vars)}, all_identical={all_same}")

# Step 2: read upstream function_index.json
upstream_path = os.path.join(BUNDLE, "function_index.json")
with open(upstream_path) as f:
    upstream = json.load(f)

step2 = {
    "step": "02_inspect_upstream_function_index",
    "resolved_path": os.path.abspath(upstream_path),
    "file_exists": True,
    "top_level_keys": list(upstream.keys()),
    "n_var_names": len(upstream.get("var_names", [])),
    "n_aliases_keys": len(upstream.get("aliases", {})),
    "total_alias_values": sum(len(v) for v in upstream.get("aliases", {}).values()),
    "status": "present_and_well_formed",
    "var_names_match_observed": upstream.get("var_names", []) == observed_vars,
}

out_dir2 = os.path.join(TASK, "3_execution", "02_inspect")
os.makedirs(out_dir2, exist_ok=True)
with open(os.path.join(out_dir2, "02_upstream_function_index.json"), "w") as f:
    json.dump(step2, f, indent=2, ensure_ascii=False)
print(f"\nStep 2 done. Status: {step2['status']}, n_var: {step2['n_var_names']}, "
      f"aliases: {step2['n_aliases_keys']} keys/{step2['total_alias_values']} values, "
      f"match: {step2['var_names_match_observed']}")