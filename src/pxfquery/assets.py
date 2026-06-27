from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

import yaml


DEFAULT_ASSET_FILES = {
    "matrix.cp_func_ad": ("cp_func_ad.h5ad", "compound perturbation function matrix"),
    "matrix.sh_func_ad": ("sh_func_ad.h5ad", "shRNA perturbation function matrix"),
    "matrix.xpr_func_ad": ("xpr_func_ad.h5ad", "overexpression perturbation function matrix"),
    "index.drug_index": ("drug_index.json", "drug lookup index"),
    "index.gene_index": ("gene_index.json", "gene lookup index"),
    "index.cellline_index": ("cellline_index.json", "cell line lookup index"),
    "index.drug_neighbors": ("drug_neighbors.json", "drug proxy neighbor index"),
    "index.gene_neighbors": ("gene_neighbors.json", "gene proxy neighbor index"),
    "index.cellline_neighbors": ("cellline_neighbors.json", "cell line proxy neighbor index"),
    "index.function_index": ("function_index.json", "function alias/index file"),
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
                if strict:
                    raise FileNotFoundError(f"required asset not found under {base}: {filename}")
                refs[key] = AssetRef(key=key, path=str(base / filename), role=role, exists=False, source="root_scan")
            else:
                refs[key] = AssetRef(key=key, path=str(path), role=role, exists=True, source="root_scan")
        return cls(refs)

    @classmethod
    def from_manifest(cls, manifest: str | Path | dict[str, Any], *, strict: bool = True) -> "AssetRegistry":
        payload = _load_manifest(manifest)
        base = Path(payload.get("root", ".")).expanduser()
        if not base.is_absolute() and isinstance(manifest, (str, Path)):
            base = Path(manifest).expanduser().resolve().parent / base
        base = base.resolve()
        assets = payload.get("assets", payload)
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


def _load_manifest(manifest: str | Path | dict[str, Any]) -> dict[str, Any]:
    if isinstance(manifest, dict):
        return manifest
    path = Path(manifest).expanduser()
    text = path.read_text(encoding="utf-8")
    payload = yaml.safe_load(text)
    if not isinstance(payload, dict):
        raise ValueError("asset manifest must be a mapping")
    return payload
