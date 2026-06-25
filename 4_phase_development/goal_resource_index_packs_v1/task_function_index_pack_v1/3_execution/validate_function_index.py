"""
T-028 Step 5: Validate T-028 pack loads and is consistent with upstream H5AD matrices
"""
import json, os, sys

import anndata as ad

TASK = "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_function_index_pack_v1"
BUNDLE = os.path.join(TASK, "1_asset", "T-021 standard_resources bundle (D-004)")

# 1. Open T-026 loader (A-001) and read all three matrices
matrix_var_names = {}
for name in ["cp_func_ad", "sh_func_ad", "xpr_func_ad"]:
    fpath = os.path.join(BUNDLE, f"{name}.h5ad")
    a = ad.read_h5ad(fpath)
    matrix_var_names[name] = list(a.var_names)

observed_vars = matrix_var_names["cp_func_ad"]

# 2. Open upstream function_index.json
upstream_path = os.path.join(BUNDLE, "function_index.json")
with open(upstream_path) as f:
    upstream = json.load(f)
upstream_status = "present" if upstream else "missing"
upstream_has_vars = "var_names" in upstream
upstream_has_aliases = "aliases" in upstream
upstream_has_meta = "meta" in upstream

# 3. Open T-028 pack JSON
t028_path = os.path.join(TASK, "4_artifact", "2_persist", "pxfquery_T028_function_index", "function_index.json")
with open(t028_path) as f:
    t028 = json.load(f)

checks = []

# Check A: JSON is well-formed
checks.append(("JSON_loads_ok", True, "T-028 function_index.json loads as valid JSON"))

# Check B: top-level keys present
required_toplevel = {"version", "matrix_source", "loader_source", "n_functions", "var_names", "aliases", "meta"}
top_level_ok = all(k in t028 for k in required_toplevel)
checks.append(("top_level_keys_present", top_level_ok,
              f"{len([k for k in required_toplevel if k in t028])}/{len(required_toplevel)} keys found"))

# Check C: n_functions == 91
n_ok = t028["n_functions"] == 91
checks.append(("n_functions_equals_91", n_ok, f"n_functions={t028['n_functions']}"))

# Check D: var_names == observed matrix var_names
var_match = t028["var_names"] == observed_vars
checks.append(("var_names_match_matrix", var_match,
              f"T-028 var_names {'==' if var_match else '!='} matrix observed var_names"))

# Check E: set(var_names) == set(observed_matrix_var_names) for all three
cp_match = set(t028["var_names"]) == set(matrix_var_names["cp_func_ad"])
sh_match = set(t028["var_names"]) == set(matrix_var_names["sh_func_ad"])
xpr_match = set(t028["var_names"]) == set(matrix_var_names["xpr_func_ad"])
all_set_match = cp_match and sh_match and xpr_match
checks.append(("var_set_match_all_matrices", all_set_match,
              f"cp:{cp_match} sh:{sh_match} xpr:{xpr_match}"))

# Check F: aliases covers every term
all_covered = set(t028["var_names"]) == set(t028["aliases"].keys())
checks.append(("aliases_covers_all_terms", all_covered, f"aliases keys: {len(t028['aliases'])}"))

# Check G: every alias list is non-null and contains term itself
alias_check_ok = True
broken_terms = []
for term, alist in t028["aliases"].items():
    if not isinstance(alist, list) or len(alist) == 0 or alist[0] != term:
        alias_check_ok = False
        broken_terms.append({"term": term, "alias_type": type(alist).__name__, "len": len(alist) if isinstance(alist, list) else None})
checks.append(("alias_nonnull_self_first", alias_check_ok,
              f"{len({k for k,v in t028['aliases'].items() if isinstance(v,list) and len(v)>0 and v[0]==k})}/91 ok. broken: {len(broken_terms)}"))

# Build result
result = {
    "task": "T-028",
    "step": "05_validate",
    "t028_path": t028_path,
    "upstream_status": {
        "path": upstream_path,
        "exists": True,
        "status": "present",
        "has_var_names": upstream_has_vars,
        "has_aliases": upstream_has_aliases,
        "has_meta": upstream_has_meta,
        "n_var_names": len(upstream.get("var_names", [])),
    },
    "observer_evidence": {name: f"n_var={len(v)}" for name, v in matrix_var_names.items()},
    "checks": [{"name": c[0], "pass": c[1], "detail": c[2]} for c in checks],
    "all_pass": all(c[1] for c in checks),
    "pass_count": sum(1 for c in checks if c[1]),
    "total_checks": len(checks),
}

out_dir = os.path.join(TASK, "3_execution", "05_validate")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "03_validation.json"), "w") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

# Short readable summary
summary_lines = [
    "# T-028 Function Index Pack — Validation Summary",
    f"",
    f"## Matrix source",
    f"- cp_func_ad.h5ad: {len(matrix_var_names['cp_func_ad'])} var terms",
    f"- sh_func_ad.h5ad: {len(matrix_var_names['sh_func_ad'])} var terms",
    f"- xpr_func_ad.h5ad: {len(matrix_var_names['xpr_func_ad'])} var terms",
    f"- All three var_names identical: {matrix_var_names['cp_func_ad'] == matrix_var_names['sh_func_ad'] == matrix_var_names['xpr_func_ad']}",
    f"",
    f"## Upstream function_index.json (T-021/D-004 via T-027)",
    f"- Present: yes",
    f"- Well-formed: var_names={upstream_has_vars}, aliases={upstream_has_aliases}, meta={upstream_has_meta}",
    f"",
    f"## T-028 pack validation",
]
for c in checks:
    mark = "✓" if c[1] else "✗"
    summary_lines.append(f"- {mark} {c[0]}: {c[2]}")
summary_lines.append(f"")
if result['all_pass']:
    summary_lines.append("**Result: ALL PASS**")
else:
    summary_lines.append(f"**Result: {result['pass_count']}/{result['total_checks']} pass**")

with open(os.path.join(out_dir, "03_validation_summary.md"), "w") as f:
    f.write("\n".join(summary_lines))

print(f"\nStep 5 done. {result['pass_count']}/{result['total_checks']} checks pass, all_pass={result['all_pass']}")
for c in checks:
    mark = "PASS" if c[1] else "FAIL"
    print(f"  [{mark}] {c[0]}: {c[2]}")