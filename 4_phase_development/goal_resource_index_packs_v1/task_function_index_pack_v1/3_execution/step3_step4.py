"""
T-028 Steps 3+4 (rebuilt): Build pxfquery-T-028 function index + validation CSV
Uses upstream structure properly: aliases has lowercase->uppercase strings,
meta has source + label per term.
"""
import json, os, csv

TASK = "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_resource_index_packs_v1/task_function_index_pack_v1"
BUNDLE = os.path.join(TASK, "1_asset", "T-021 standard_resources bundle (D-004)")

# Read observed var_names from step 1
with open(os.path.join(TASK, "3_execution", "01_verify", "01_var_names.json")) as f:
    s1 = json.load(f)
observed_vars = s1["cp_var_names"]
assert len(observed_vars) == 91

# Read upstream function_index.json
with open(os.path.join(BUNDLE, "function_index.json")) as f:
    upstream = json.load(f)

upstream_aliases_lowercase = upstream.get("aliases", {})
upstream_meta = upstream.get("meta", {})

# Build a lowercase -> list-of-aliases collection
# For each uppercase var term:
#   - primary alias: the term itself
#   - lowercase variant of the term
#   - meta.label (human-readable) if available
def _build_alias_list(term):
    aliases = [term]  # Always include self first
    lower = term.lower()
    if lower != term and lower not in aliases:
        aliases.append(lower)
    meta_entry = upstream_meta.get(term, {})
    label = meta_entry.get("label") if isinstance(meta_entry, dict) else None
    if label and label not in aliases:
        aliases.append(label)
    return aliases

t028_pack = {
    "version": "pxfquery-T-028",
    "matrix_source": "T-021 standard_resources bundle (D-004)",
    "loader_source": "pxfquery-T-026 matrix loader",
    "n_functions": 91,
    "var_names": observed_vars,
    "aliases": {},
    "meta": {
        "built_on": "2026-06-23",
        "upstream_function_index_status": "present",
        "upstream_file": "T-021/D-004 function_index.json",
        "alias_seed_sources": [
            "T-021 standard_resources bundle function_index.json (lowercase->uppercase map)",
            "T-021 standard_resources bundle function_index.json (meta.label per term)",
        ],
        "notes": (
            "Upstream function_index.json is present and well-formed in the T-021 bundle. "
            "T-013 flagged function_index.json as missing/incomplete in the *migrated* query "
            "index directory; this corrected pxfquery-T-028 pack closes that gap within T-028 "
            "scope. Each var term carries: (a) itself, (b) lowercase variant, (c) meta.label "
            "(human-readable name when available)."
        ),
    },
}

# Track per-term whether upstream mapping is found
mapping_status = {}
for term in observed_vars:
    alist = _build_alias_list(term)
    t028_pack["aliases"][term] = alist
    mapping_status[term] = {
        "lowercase_in_aliases_map": term.lower() in upstream_aliases_lowercase,
        "meta_label_present": term in upstream_meta,
    }

t028_pack["meta"]["total_alias_values"] = sum(len(v) for v in t028_pack["aliases"].values())
terms_with_full_mapping = sum(1 for m in mapping_status.values()
                              if m["lowercase_in_aliases_map"] and m["meta_label_present"])
t028_pack["meta"]["terms_with_full_upstream_mapping"] = terms_with_full_mapping
t028_pack["meta"]["terms_without_label"] = sum(
    1 for t, m in mapping_status.items() if not m["meta_label_present"]
)

out_dir = os.path.join(TASK, "4_artifact", "2_persist", "pxfquery_T028_function_index")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "function_index.json")
with open(out_path, "w") as f:
    json.dump(t028_pack, f, indent=2, ensure_ascii=False)
print(f"Step 3 done. {out_path}")
print(f"  Terms: {len(observed_vars)}")
print(f"  Total alias values: {t028_pack['meta']['total_alias_values']}")
print(f"  Terms with full upstream mapping (lowercase+label): {terms_with_full_mapping}")
print(f"  Terms without meta.label: {t028_pack['meta']['terms_without_label']}")

# Step 4: Build validation CSV
csv_dir = os.path.join(TASK, "3_execution", "04_validation_table")
os.makedirs(csv_dir, exist_ok=True)
table_dir = os.path.join(TASK, "4_artifact", "5_table")
os.makedirs(table_dir, exist_ok=True)

csv_path = os.path.join(csv_dir, "03_validation.csv")
persist_csv_path = os.path.join(table_dir, "pxfquery_t028_function_index_validation.csv")

rows = []
ok_count = 0
missing_label_terms = []
mismatched_terms = []
for i, term in enumerate(observed_vars):
    in_matrix = term in observed_vars
    alias_list = t028_pack["aliases"].get(term, [term])
    alias_count = len(alias_list)
    mapping = mapping_status[term]
    if not in_matrix:
        status = "MATRIX_VAR_MISMATCH"
        mismatched_terms.append(term)
    elif not mapping["meta_label_present"] and alias_count < 2:
        status = "ALIASES_MISSING_UPSTREAM"
        missing_label_terms.append(term)
    else:
        status = "OK"
        ok_count += 1
    rows.append({
        "function_term": term,
        "var_index": i,
        "in_matrix_var_names": str(in_matrix),
        "alias_count": alias_count,
        "aliases_json": json.dumps(alias_list, ensure_ascii=False),
        "status": status,
    })

for p in [csv_path, persist_csv_path]:
    with open(p, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

non_ok = [r for r in rows if r["status"] != "OK"]
print(f"\nStep 4 done. Validation CSV: {len(rows)} rows")
print(f"  OK: {ok_count}, Non-OK: {len(non_ok)}")
if missing_label_terms:
    print(f"  Terms missing meta.label (still OK with self+lowercase): {len(missing_label_terms)}")
if mismatched_terms:
    print(f"  Mismatched: {len(mismatched_terms)}")