"""T-040 package-core resource access helpers.

This module vendors the T-026 loader interface into the T-040 package-core
branch. It opens standard resource files by reference and records observed
structure at runtime; it does not copy matrix, index, or metadata bytes.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any

import anndata as ad
import pandas as pd
import yaml

__task_version__ = "pxfquery-T-040"


DEFAULT_STANDARD_RESOURCE_BUNDLE = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/"
    "4_phase_development/goal_precomputed_data_exploration/"
    "task_standard_resources_optimal_formats/4_artifact/2_persist/standard_resources"
)


def resolve_bundle_root(bundle_root: str | os.PathLike[str] | None = None) -> Path:
    """Return the standard resource bundle root used by package-core checks."""
    root = Path(bundle_root) if bundle_root is not None else DEFAULT_STANDARD_RESOURCE_BUNDLE
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"Standard resource bundle not found: {root}")
    return root


def load_matrix(path: str | os.PathLike[str]):
    """Load one H5AD matrix and return ``(AnnData, metadata)``."""
    matrix_path = Path(path).expanduser().resolve()
    t0 = time.time()
    a = ad.read_h5ad(matrix_path)
    dt = time.time() - t0
    meta = {
        "resolved_path": str(matrix_path),
        "shape": list(a.shape),
        "n_obs": int(a.shape[0]),
        "n_var": int(a.shape[1]),
        "obs_columns": list(a.obs.columns),
        "var_shape": list(a.var.shape) if a.var is not None else None,
        "X_dtype": str(a.X.dtype),
        "load_sec": round(dt, 4),
    }
    return a, meta


def load_index(path: str | os.PathLike[str]) -> tuple[Any, dict[str, Any]]:
    """Load one JSON index and return ``(data, metadata)``."""
    index_path = Path(path).expanduser().resolve()
    t0 = time.time()
    data = json.loads(index_path.read_text(encoding="utf-8"))
    dt = time.time() - t0
    meta = {
        "resolved_path": str(index_path),
        "top_level_keys": list(data.keys()) if isinstance(data, dict) else None,
        "type": "dict" if isinstance(data, dict) else "list",
        "item_count": len(data),
        "load_sec": round(dt, 4),
    }
    return data, meta


def load_metadata(path: str | os.PathLike[str]):
    """Load one CSV metadata table and return ``(DataFrame, metadata)``."""
    metadata_path = Path(path).expanduser().resolve()
    t0 = time.time()
    df = pd.read_csv(metadata_path)
    dt = time.time() - t0
    meta = {
        "resolved_path": str(metadata_path),
        "columns": list(df.columns),
        "n_rows": int(len(df)),
        "n_cols": int(len(df.columns)),
        "dtypes": {c: str(df[c].dtype) for c in df.columns},
        "load_sec": round(dt, 4),
    }
    return df, meta


def load_description(path: str | os.PathLike[str]) -> tuple[Any, dict[str, Any]]:
    """Load one YAML data description and return ``(data, metadata)``."""
    description_path = Path(path).expanduser().resolve()
    t0 = time.time()
    data = yaml.safe_load(description_path.read_text(encoding="utf-8"))
    dt = time.time() - t0
    meta = {
        "resolved_path": str(description_path),
        "top_level_keys": list(data.keys()) if isinstance(data, dict) else None,
        "load_sec": round(dt, 4),
    }
    return data, meta


def load_bundle(bundle_root: str | os.PathLike[str] | None = None) -> dict[str, Any]:
    """Load all standard resource files and return observed load metadata."""
    root = resolve_bundle_root(bundle_root)
    result: dict[str, Any] = {
        "bundle_root": str(root),
        "matrices": [],
        "indexes": [],
        "metadata": [],
        "description": None,
        "summary": {"total_files_loaded": 0, "failed_files": [], "warnings": []},
    }

    for fpath in sorted(root.iterdir()):
        if not fpath.is_file():
            continue
        try:
            if fpath.name.endswith(".h5ad"):
                _, meta = load_matrix(fpath)
                meta["filename"] = fpath.name
                result["matrices"].append(meta)
            elif fpath.name.endswith(".json"):
                _, meta = load_index(fpath)
                meta["filename"] = fpath.name
                result["indexes"].append(meta)
            elif fpath.name.endswith(".csv"):
                _, meta = load_metadata(fpath)
                meta["filename"] = fpath.name
                result["metadata"].append(meta)
            elif fpath.name == "data_description.yaml" or fpath.name.endswith(".yaml"):
                _, meta = load_description(fpath)
                meta["filename"] = fpath.name
                result["description"] = meta
            else:
                continue
            result["summary"]["total_files_loaded"] += 1
        except Exception as exc:  # pragma: no cover - captured in validation record
            result["summary"]["failed_files"].append({"filename": fpath.name, "error": repr(exc)})

    result["summary"]["loaded_by_category"] = {
        "matrices": len(result["matrices"]),
        "indexes": len(result["indexes"]),
        "metadata": len(result["metadata"]),
        "description": 1 if result["description"] else 0,
    }
    return result


def load_standard_matrix(
    name: str = "xpr_func_ad.h5ad",
    bundle_root: str | os.PathLike[str] | None = None,
):
    """Load one named matrix from the standard resource bundle."""
    root = resolve_bundle_root(bundle_root)
    return load_matrix(root / name)
