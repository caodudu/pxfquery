import json, os, yaml

SRC = "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_precomputed_data_exploration/task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources"
TASK = "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_index_health_check_m1"
OUT = os.path.join(TASK, "3_execution")
os.makedirs(OUT, exist_ok=True)

def load_json(name):
    path = os.path.join(SRC, name)
    size = os.path.getsize(path)
    with open(path) as f:
        data = json.load(f)
    return data, size, path

# Step 1
step1 = {}
for fname in ["cellline_index.json", "drug_index.json", "gene_index.json", "function_index.json"]:
    try:
        data, size, path = load_json(fname)
        ttype = type(data).__name__
        elem_count = len(data) if isinstance(data, (dict, list)) else "scalar"
        step1[fname] = {"file_size_bytes": size, "top_level_type": ttype, "element_count": elem_count, "parseable": True}
    except Exception as e:
        step1[fname] = {"parseable": False, "error": str(e)}

with open(os.path.join(OUT, "step1_core_schema_summary.json"), "w") as f:
    json.dump(step1, f, indent=2)
print("=== STEP 1: Core Schema Summary ===")
print(json.dumps(step1, indent=2))

# Load all
cellline_index, _, _ = load_json("cellline_index.json")
drug_index, _, _ = load_json("drug_index.json")
gene_index, _, _ = load_json("gene_index.json")
function_index_raw, _, _ = load_json("function_index.json")

# Step 2
step2 = {}

# cellline_index
cl_valid = "valid"
cl_issues = []
if isinstance(cellline_index, dict):
    non_str = [(k,v) for k,v in cellline_index.items() if not isinstance(v, str)]
    if non_str:
        cl_valid = "warning"
        cl_issues.append(f"{len(non_str)} non-string values")
        cl_issues.append(f"Sample: {non_str[:3]}")
else:
    cl_valid = "invalid"
step2["cellline_index.json"] = {"status": cl_valid, "entry_count": len(cellline_index) if isinstance(cellline_index, dict) else "N/A", "issues": cl_issues}
if isinstance(cellline_index, dict):
    step2["cellline_index.json"]["sample"] = {k: (v[:5] if isinstance(v, list) else v) for k,v in list(cellline_index.items())[:3]}
    if all(isinstance(v, list) for v in cellline_index.values()):
        import itertools
        all_vals_raw = list(itertools.chain.from_iterable(cellline_index.values()))
        step2["cellline_index.json"]["total_names_in_lists"] = len(all_vals_raw)
        step2["cellline_index.json"]["value_overview"] = f"{len(cellline_index)} key(s) -> list values totaling {len(all_vals_raw)} names"
    else:
        try:
            all_vals = set(cellline_index.values())
            step2["cellline_index.json"]["unique_values"] = len(all_vals)
        except TypeError:
            step2["cellline_index.json"]["value_overview"] = "values contain unhashable types, skipping set dedup"

# drug_index
di_valid = "valid"
di_issues = []
if isinstance(drug_index, dict):
    brd_vals = sum(1 for v in drug_index.values() if isinstance(v, str) and v.startswith("BRD-"))
    brd_keys = [k for k in drug_index if k.startswith("BRD-")]
    non_brd_vals = [(k,v) for k,v in list(drug_index.items())[:10] if isinstance(v, str) and not v.startswith("BRD-")]
    if brd_vals < len(drug_index) * 0.8:
        di_valid = "warning"
        di_issues.append(f"Only {brd_vals}/{len(drug_index)} values are BRD-prefixed")
    step2["drug_index.json"] = {"status": di_valid, "entry_count": len(drug_index), "brd_value_count": brd_vals, "brd_key_count": len(brd_keys), "sample_non_brd_values": non_brd_vals, "issues": di_issues}
else:
    step2["drug_index.json"] = {"status": "invalid"}

# gene_index
gi_valid = "valid"
gi_issues = []
if isinstance(gene_index, dict):
    sample_k = next(iter(gene_index))
    sample_v = gene_index[sample_k]
    fields = list(sample_v.keys()) if isinstance(sample_v, dict) else "N/A"
    expected = ["ensembl_id", "gene_symbol", "gene_type"]
    if isinstance(sample_v, dict):
        missing = [f for f in expected if f not in sample_v]
        if missing:
            gi_valid = "warning"
            gi_issues.append(f"Missing expected fields in entries: {missing}")
    types = set()
    for k,v in list(gene_index.items())[:1000]:
        if isinstance(v, dict) and "gene_type" in v:
            types.add(v["gene_type"])
    step2["gene_index.json"] = {"status": gi_valid, "entry_count": len(gene_index), "sample_key": sample_k, "sample_entry_fields": fields, "gene_type_categories": sorted([t for t in types if t is not None]), "issues": gi_issues}
else:
    step2["gene_index.json"] = {"status": "invalid"}

# function_index
fi_valid = "invalid"
fi_issues = []
fi_count = len(function_index_raw) if isinstance(function_index_raw, (list,dict)) else 0
if isinstance(function_index_raw, dict) and "meta" in function_index_raw:
    meta = function_index_raw["meta"]
    vnames = function_index_raw.get("var_names", [])
    aliases = function_index_raw.get("aliases", {})
    fi_valid = "valid"
    fi_count = len(meta)
    if fi_count == 91:
        fi_issues.append("OK: 91 terms (as dict with meta/var_names/aliases)")
    else:
        fi_valid = "warning"
        fi_issues.append(f"meta has {fi_count} entries (expected 91)")
    # Check meta entries
    sample_key = next(iter(meta))
    sample_meta = meta[sample_key]
    meta_fields = list(sample_meta.keys()) if isinstance(sample_meta, dict) else "N/A"
    has_id = all("id" in v for v in meta.values()) if isinstance(meta, dict) and fi_count > 0 else False
    has_name = all("name" in v for v in meta.values()) if isinstance(meta, dict) and fi_count > 0 else False
    cats = {}
    for v in meta.values():
        if isinstance(v, dict):
            cats[v.get("category","?")] = cats.get(v.get("category","?"),0)+1
    fi_issues.append(f"Hallmark: {cats.get('Hallmark',0)}, 3CA MPS: {cats.get('3CA MPS',0)}")
    step2["function_index.json"] = {"status": fi_valid, "entry_count": fi_count, "structure": "dict{meta, var_names, aliases}", "meta_fields": meta_fields, "has_id_field": has_id, "has_name_field": has_name, "category_counts": cats, "issues": fi_issues}
else:
    fi_issues.append(f"Unexpected structure: {type(function_index_raw).__name__}")
    step2["function_index.json"] = {"status": fi_valid, "entry_count": fi_count, "issues": fi_issues}

# data_description
dd_path = os.path.join(SRC, "data_description.yaml")
dd_size = os.path.getsize(dd_path)
with open(dd_path) as f:
    dd = yaml.safe_load(f)
dd_valid = "valid" if dd else "invalid"
dd_keys = list(dd.keys())[:10] if isinstance(dd, dict) else "N/A"
step2["data_description.yaml"] = {"status": dd_valid, "file_size_bytes": dd_size, "top_keys": dd_keys}

with open(os.path.join(OUT, "step2_key_validation.json"), "w") as f:
    json.dump(step2, f, indent=2, default=str)
print("\n=== STEP 2: Key Validation ===")
print(json.dumps(step2, indent=2, default=str))

# Step 3
step3 = {}
for fname in ["cellline_neighbors.json", "cellline_tree.json", "drug_neighbors.json",
               "gene_neighbors.json", "gene_neighbors_simple.json", "gene_index_simple.json"]:
    try:
        data, size, path = load_json(fname)
        ttype = type(data).__name__
        entry = {"file_size_bytes": size, "top_level_type": ttype, "parseable": True}
        if isinstance(data, dict):
            entry["key_count"] = len(data)
            empty = sum(1 for v in data.values() if v is None or (isinstance(v,(list,dict)) and len(v)==0))
            entry["empty_values"] = empty
            non_empty = [v for v in data.values() if isinstance(v,(list,dict)) and len(v)>0]
            if non_empty:
                sizes = [len(v) if isinstance(v,(list,dict)) else 0 for v in non_empty[:100]]
                entry["sample_edge_cardinality"] = {"min": min(sizes), "max": max(sizes), "sample_count": len(sizes)}
            entry["status"] = "valid" if empty < len(data) * 0.5 else ("warning" if empty < len(data) else "invalid")
        elif isinstance(data, list):
            entry["element_count"] = len(data)
            entry["status"] = "valid" if len(data) > 0 else "warning"
        step3[fname] = entry
    except Exception as e:
        step3[fname] = {"parseable": False, "error": str(e)}

if step3.get("cellline_tree.json",{}).get("parseable", False):
    tree,_,_ = load_json("cellline_tree.json")
    if isinstance(tree, dict):
        has_children = any("children" in (v if isinstance(v,dict) else {}) for v in tree.values())
        step3["cellline_tree.json"]["has_hierarchy"] = has_children
        if has_children:
          # check first entry with children
          for k,v in tree.items():
            if isinstance(v,dict) and "children" in v:
              step3["cellline_tree.json"]["children_sample"] = {k: list(v.keys())}
              break

with open(os.path.join(OUT, "step3_neighbor_health.json"), "w") as f:
    json.dump(step3, f, indent=2, default=str)
print("\n=== STEP 3: Neighbor Health ===")
print(json.dumps(step3, indent=2, default=str))
print("\nDONE STEPS 1-3")
