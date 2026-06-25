# T-028 Function Index Pack — Validation Summary

## Matrix source
- cp_func_ad.h5ad: 91 var terms
- sh_func_ad.h5ad: 91 var terms
- xpr_func_ad.h5ad: 91 var terms
- All three var_names identical: True

## Upstream function_index.json (T-021/D-004 via T-027)
- Present: yes
- Well-formed: var_names=True, aliases=True, meta=True

## T-028 pack validation
- ✓ JSON_loads_ok: T-028 function_index.json loads as valid JSON
- ✓ top_level_keys_present: 7/7 keys found
- ✓ n_functions_equals_91: n_functions=91
- ✓ var_names_match_matrix: T-028 var_names == matrix observed var_names
- ✓ var_set_match_all_matrices: cp:True sh:True xpr:True
- ✓ aliases_covers_all_terms: aliases keys: 91
- ✓ alias_nonnull_self_first: 91/91 ok. broken: 0

**Result: ALL PASS**