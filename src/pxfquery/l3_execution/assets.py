from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
from typing import Any


DEFAULT_ASSET_FILES = {
    "matrix.cp_func_ad": ("cp_func_ad.h5ad", "compound perturbation function matrix"),
    "matrix.sh_func_ad": ("sh_func_ad.h5ad", "shRNA perturbation function matrix"),
    "matrix.xpr_func_ad": ("xpr_func_ad.h5ad", "CRISPR/loss-of-function perturbation function matrix"),
    "metadata.cellline_info": ("cellline_info_standard.csv", "extended cell line metadata"),
    "metadata.cellline_meta": ("cellline_meta_standard.csv", "standard cell line metadata"),
    "metadata.compound_info": ("compound_info_standard.csv", "compound target/MOA metadata"),
    "metadata.compound_meta": ("compound_meta_standard.csv", "standard compound metadata"),
    "metadata.gene_info": ("gene_info_standard.csv", "gene metadata"),
    "index.drug_index": ("drug_index.json", "drug lookup index"),
    "index.gene_index": ("gene_index.json", "gene lookup index"),
    "index.gene_index_simple": ("gene_index_simple.json", "simple gene lookup index"),
    "index.cellline_index": ("cellline_index.json", "cell line lookup index"),
    "index.drug_neighbors": ("drug_neighbors.json", "drug proxy neighbor index"),
    "index.gene_neighbors": ("gene_neighbors.json", "gene proxy neighbor index"),
    "index.cellline_neighbors": ("cellline_neighbors.json", "cell line proxy neighbor index"),
    "index.cellline_tree": ("cellline_tree.json", "cell line lineage tree"),
    "index.function_index": ("function_index.json", "function alias/index file"),
    "l3_functional_scores.cp.matrix": ("cp_X_dense_thr0.1_round2_float16_compressed.npz", "compound perturbation lightweight score matrix"),
    "l3_functional_scores.cp.obs": ("cp_obs_min.parquet", "compound perturbation L3 observation metadata"),
    "l3_functional_scores.cp.var": ("cp_var_names.json", "compound perturbation L3 function names"),
    "l3_functional_scores.sh.matrix": ("sh_X_dense_thr0.1_round2_float16_compressed.npz", "shRNA perturbation lightweight score matrix"),
    "l3_functional_scores.sh.obs": ("sh_obs_min.parquet", "shRNA perturbation L3 observation metadata"),
    "l3_functional_scores.sh.var": ("sh_var_names.json", "shRNA perturbation L3 function names"),
    "l3_functional_scores.xpr.matrix": ("xpr_X_dense_thr0.1_round2_float16_compressed.npz", "CRISPR/loss-of-function perturbation lightweight score matrix"),
    "l3_functional_scores.xpr.obs": ("xpr_obs_min.parquet", "CRISPR/loss-of-function perturbation L3 observation metadata"),
    "l3_functional_scores.xpr.var": ("xpr_var_names.json", "CRISPR/loss-of-function perturbation L3 function names"),
    "matrix.cp_obs_min": ("cp_obs_min.parquet", "compound perturbation L3 observation metadata"),
    "matrix.sh_obs_min": ("sh_obs_min.parquet", "shRNA perturbation L3 observation metadata"),
    "matrix.xpr_obs_min": ("xpr_obs_min.parquet", "CRISPR/loss-of-function perturbation L3 observation metadata"),
    "provenance.data_description": ("data_description.yaml", "data provenance description"),
}

OPTIONAL_ROOT_SCAN_KEYS = {
    key
    for key in DEFAULT_ASSET_FILES
    if key.startswith("l3_functional_scores.") or key in {"matrix.cp_obs_min", "matrix.sh_obs_min", "matrix.xpr_obs_min"}
}


@dataclass
class AssetRef:
    key: str
    path: str
    role: str
    exists: bool
    source: str = "registered"
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class AssetRegistry:
    def __init__(self, refs: dict[str, AssetRef] | None = None) -> None:
        self._refs = refs or {}

    @classmethod
    def from_root(cls, root: str | Path, *, strict: bool = True) -> "AssetRegistry":
        base = Path(root).expanduser().resolve()
        refs: dict[str, AssetRef] = {}
        for key, (filename, role) in DEFAULT_ASSET_FILES.items():
            path = _find_one(base, filename)
            if path is None:
                if strict and key not in OPTIONAL_ROOT_SCAN_KEYS:
                    raise FileNotFoundError(f"required asset not found under {base}: {filename}")
                refs[key] = AssetRef(key=key, path=str(base / filename), role=role, exists=False, source="root_scan")
            else:
                refs[key] = AssetRef(key=key, path=str(path), role=role, exists=True, source="root_scan")
        return cls(refs)

    @classmethod
    def from_manifest(cls, manifest: str | Path | dict[str, Any], *, strict: bool = True, base_dir: str | Path | None = None) -> "AssetRegistry":
        payload = _load_manifest(manifest)
        base = Path(base_dir or payload.get("root", ".")).expanduser()
        if not base.is_absolute() and isinstance(manifest, (str, Path)):
            base = Path(manifest).expanduser().resolve().parent / base
        base = base.resolve()
        assets = payload.get("assets") or _asset_entries_from_files(payload.get("files")) or payload
        refs: dict[str, AssetRef] = {}
        for key, value in assets.items():
            if key == "root":
                continue
            if isinstance(value, str):
                rel_path = value
                role = DEFAULT_ASSET_FILES.get(key, (Path(value).name, "registered asset"))[1]
                metadata: dict[str, Any] = {}
            else:
                rel_path = value["path"]
                role = value.get("role", DEFAULT_ASSET_FILES.get(key, (Path(rel_path).name, "registered asset"))[1])
                metadata = {k: v for k, v in value.items() if k not in {"path", "role"}}
            path = Path(rel_path).expanduser()
            if not path.is_absolute():
                path = base / path
            exists = path.exists()
            if strict and not exists:
                raise FileNotFoundError(f"registered asset does not exist for {key}: {path}")
            refs[key] = AssetRef(key=key, path=str(path.resolve()), role=role, exists=exists, source="manifest", metadata=metadata)
        return cls(refs)

    def get(self, key: str) -> AssetRef:
        try:
            return self._refs[key]
        except KeyError as exc:
            raise KeyError(f"asset is not registered: {key}") from exc

    def keys(self) -> list[str]:
        return sorted(self._refs)

    def to_dict(self) -> dict[str, dict[str, Any]]:
        return {key: ref.to_dict() for key, ref in sorted(self._refs.items())}


def _find_one(root: Path, filename: str) -> Path | None:
    direct = root / filename
    if direct.exists():
        return direct.resolve()
    matches = sorted(root.rglob(filename))
    return matches[0].resolve() if matches else None


def _asset_entries_from_files(files: Any) -> dict[str, Any]:
    if not isinstance(files, dict):
        return {}
    mapping = {
        "l2.cellline_index": "index.cellline_index",
        "l2.cellline_neighbors": "index.cellline_neighbors",
        "l2.cellline_tree": "index.cellline_tree",
        "l2.drug_index": "index.drug_index",
        "l2.drug_neighbors": "index.drug_neighbors",
        "l2.gene_index": "index.gene_index",
        "l2.gene_index_simple": "index.gene_index_simple",
        "l2.gene_neighbors": "index.gene_neighbors",
        "l2.function_index": "index.function_index",
    }
    out: dict[str, Any] = {}
    for key, value in files.items():
        if not isinstance(value, dict):
            continue
        out[mapping.get(key, key)] = value
    return out


def _load_manifest(manifest: str | Path | dict[str, Any]) -> dict[str, Any]:
    if isinstance(manifest, dict):
        return manifest
    path = Path(manifest).expanduser()
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in {".yaml", ".yml"}:
        import yaml

        payload = yaml.safe_load(text)
    else:
        payload = json.loads(text)
    if not isinstance(payload, dict):
        raise ValueError("asset manifest must be a mapping")
    return payload
