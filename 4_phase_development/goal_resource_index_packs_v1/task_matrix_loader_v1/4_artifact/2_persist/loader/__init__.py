"""
pxfquery-T-026 matrix/resource loader package.

Loads T-021 standard resources (H5AD matrices, JSON indexes, CSV metadata, YAML description)
from a bundle directory and reports observed structure at runtime.
No hard-coded shapes or column lists.
"""
import os
import json
import time
import yaml
import pandas as pd
import anndata as ad

__version__ = "1.0.0"
__task_version__ = "pxfquery-T-026"


def load_matrix(path):
    """Load an H5AD matrix file and return (ann_data, metadata_dict)."""
    t0 = time.time()
    a = ad.read_h5ad(path)
    dt = time.time() - t0
    meta = {
        "resolved_path": os.path.abspath(path),
        "shape": list(a.shape),
        "n_obs": a.shape[0],
        "n_var": a.shape[1],
        "obs_columns": list(a.obs.columns),
        "var_shape": list(a.var.shape) if a.var is not None else None,
        "X_dtype": str(a.X.dtype),
        "load_sec": round(dt, 4),
    }
    return a, meta


def load_index(path):
    """Load a JSON index file and return (data, metadata_dict)."""
    t0 = time.time()
    with open(path, "r") as f:
        data = json.load(f)
    dt = time.time() - t0
    meta = {
        "resolved_path": os.path.abspath(path),
        "top_level_keys": list(data.keys()) if isinstance(data, dict) else None,
        "type": "dict" if isinstance(data, dict) else "list",
        "item_count": len(data) if isinstance(data, dict) else len(data),
        "load_sec": round(dt, 4),
    }
    if isinstance(data, dict):
        sample = {}
        for k in list(data.keys())[:3]:
            v = data[k]
            sample[k] = {"type": type(v).__name__, "len": len(v) if isinstance(v, (list, dict)) else None}
        meta["key_sample"] = sample
    return data, meta


def load_metadata(path):
    """Load a CSV metadata file and return (dataframe, metadata_dict)."""
    t0 = time.time()
    df = pd.read_csv(path)
    dt = time.time() - t0
    meta = {
        "resolved_path": os.path.abspath(path),
        "columns": list(df.columns),
        "n_rows": len(df),
        "n_cols": len(df.columns),
        "dtypes": {c: str(df[c].dtype) for c in df.columns},
        "load_sec": round(dt, 4),
    }
    return df, meta


def load_description(path):
    """Load a YAML data_description file and return (data, metadata_dict)."""
    t0 = time.time()
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    dt = time.time() - t0
    meta = {
        "resolved_path": os.path.abspath(path),
        "top_level_keys": list(data.keys()) if isinstance(data, dict) else None,
        "load_sec": round(dt, 4),
    }
    return data, meta


def load_bundle(bundle_root):
    """
    Load all files in a T-021 standard resources bundle directory.

    Returns a dict with keys: 'matrices', 'indexes', 'metadata', 'description',
    'summary', each containing per-file loading metadata.
    """
    bundle_root = os.path.abspath(bundle_root)
    if not os.path.isdir(bundle_root):
        raise NotADirectoryError(f"Bundle root not found: {bundle_root}")

    result = {
        "bundle_root": bundle_root,
        "matrices": [],
        "indexes": [],
        "metadata": [],
        "description": None,
        "summary": {"total_files_loaded": 0, "failed_files": [], "warnings": []},
    }

    files = sorted(os.listdir(bundle_root))

    for fname in files:
        fpath = os.path.join(bundle_root, fname)
        if not os.path.isfile(fpath):
            continue

        try:
            ext = os.path.splitext(fname)[1].lower()
            if fname.endswith(".h5ad"):
                _, meta = load_matrix(fpath)
                meta["filename"] = fname
                result["matrices"].append(meta)
                result["summary"]["total_files_loaded"] += 1
            elif fname.endswith(".json"):
                _, meta = load_index(fpath)
                meta["filename"] = fname
                result["indexes"].append(meta)
                result["summary"]["total_files_loaded"] += 1
            elif fname.endswith(".csv"):
                _, meta = load_metadata(fpath)
                meta["filename"] = fname
                result["metadata"].append(meta)
                result["summary"]["total_files_loaded"] += 1
            elif fname == "data_description.yaml":
                _, meta = load_description(fpath)
                meta["filename"] = fname
                result["description"] = meta
                result["summary"]["total_files_loaded"] += 1
            elif fname.endswith(".yaml"):
                _, meta = load_description(fpath)
                meta["filename"] = fname
                result["description"] = meta
                result["summary"]["total_files_loaded"] += 1
        except Exception as e:
            result["summary"]["failed_files"].append({
                "filename": fname,
                "error": repr(e),
            })

    result["summary"]["loaded_by_category"] = {
        "matrices": len(result["matrices"]),
        "indexes": len(result["indexes"]),
        "metadata": len(result["metadata"]),
        "description": 1 if result["description"] else 0,
    }

    return result