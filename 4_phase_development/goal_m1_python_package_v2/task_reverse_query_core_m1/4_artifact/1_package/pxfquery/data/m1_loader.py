from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Any, Optional

import anndata
import pandas as pd
import yaml


@dataclass
class M1Fixture:
    cp: anndata.AnnData
    sh: anndata.AnnData
    xpr: anndata.AnnData
    cellline_meta: pd.DataFrame
    cellline_info: pd.DataFrame
    compound_meta: pd.DataFrame
    compound_info: pd.DataFrame
    gene_info: pd.DataFrame
    cellline_index: dict
    cellline_neighbors: dict
    cellline_tree: dict
    drug_index: dict
    drug_neighbors: dict
    gene_index_simple: dict
    gene_neighbors_simple: dict
    gene_index: dict
    gene_neighbors: dict
    function_index: dict

    def matrix_shape(self, name: str) -> tuple[int, int]:
        data = getattr(self, name)
        return data.shape

    def matrix_obs_columns(self, name: str) -> list[str]:
        data = getattr(self, name)
        return list(data.obs.columns)

    def matrix_var_names(self, name: str) -> list[str]:
        data = getattr(self, name)
        return list(data.var_names)

    def get_sig_ids(self, name: str) -> list[str]:
        data = getattr(self, name)
        return list(data.obs_names)

    def get_matrix_row(self, name: str, sig_id: str) -> pd.Series:
        data = getattr(self, name)
        idx = data.obs_names.get_loc(sig_id)
        return pd.Series(data.X[idx], index=data.var_names, name=sig_id)


@dataclass
class M1Manifest:
    raw: dict[str, Any]
    resources: list[dict[str, Any]] = field(default_factory=list)

    def fixture_resources(self) -> list[dict[str, Any]]:
        return [r for r in self.resources if r.get("resource_id", "").startswith("m1_fixture_")]

    def resource_by_id(self, resource_id: str) -> Optional[dict[str, Any]]:
        for r in self.resources:
            if r["resource_id"] == resource_id:
                return r
        return None


class M1FixtureLoader:
    def __init__(self, manifest_path: str, fixture_root: Optional[str] = None):
        self._manifest_path = manifest_path
        self._manifest: Optional[M1Manifest] = None
        self._fixture_root = fixture_root
        self._fixture: Optional[M1Fixture] = None

    @property
    def manifest(self) -> M1Manifest:
        if self._manifest is None:
            with open(self._manifest_path, "r") as fh:
                raw = yaml.safe_load(fh)
            self._manifest = M1Manifest(raw=raw, resources=raw.get("resources", []))
        return self._manifest

    @property
    def fixture(self) -> M1Fixture:
        if self._fixture is None:
            self._fixture = self._load_fixture()
        return self._fixture

    def _resolve_root(self) -> str:
        if self._fixture_root:
            return self._fixture_root

        manifest_dir = os.path.dirname(os.path.abspath(self._manifest_path))
        self._fixture_root = os.path.join(manifest_dir, "fixture_package_m1")

        if not os.path.isdir(self._fixture_root):
            raise FileNotFoundError(
                f"Fixture directory not found at derived path {self._fixture_root}. "
                f"Pass fixture_root explicitly."
            )
        return self._fixture_root

    def _load_fixture(self) -> M1Fixture:
        root = self._resolve_root()

        cp_path = os.path.join(root, "cp_func_fixture_m1.h5ad")
        sh_path = os.path.join(root, "sh_func_fixture_m1.h5ad")
        xpr_path = os.path.join(root, "xpr_func_fixture_m1.h5ad")

        for path, label in [(cp_path, "cp"), (sh_path, "sh"), (xpr_path, "xpr")]:
            if not os.path.isfile(path):
                raise FileNotFoundError(f"Missing fixture matrix: {label} ({path})")

        return M1Fixture(
            cp=anndata.read_h5ad(cp_path),
            sh=anndata.read_h5ad(sh_path),
            xpr=anndata.read_h5ad(xpr_path),
            cellline_meta=pd.read_csv(os.path.join(root, "cellline_meta_fixture_m1.csv")),
            cellline_info=pd.read_csv(os.path.join(root, "cellline_info_fixture_m1.csv")),
            compound_meta=pd.read_csv(os.path.join(root, "compound_meta_fixture_m1.csv")),
            compound_info=pd.read_csv(os.path.join(root, "compound_info_fixture_m1.csv")),
            gene_info=pd.read_csv(os.path.join(root, "gene_info_fixture_m1.csv")),
            cellline_index=_read_json(os.path.join(root, "cellline_index_fixture_m1.json")),
            cellline_neighbors=_read_json(os.path.join(root, "cellline_neighbors_fixture_m1.json")),
            cellline_tree=_read_json(os.path.join(root, "cellline_tree_fixture_m1.json")),
            drug_index=_read_json(os.path.join(root, "drug_index_fixture_m1.json")),
            drug_neighbors=_read_json(os.path.join(root, "drug_neighbors_fixture_m1.json")),
            gene_index_simple=_read_json(os.path.join(root, "gene_index_simple_fixture_m1.json")),
            gene_neighbors_simple=_read_json(os.path.join(root, "gene_neighbors_simple_fixture_m1.json")),
            gene_index=_read_json(os.path.join(root, "gene_index_fixture_m1.json")),
            gene_neighbors=_read_json(os.path.join(root, "gene_neighbors_fixture_m1.json")),
            function_index=_read_json(os.path.join(root, "function_index_fixture_m1.json")),
        )


def _read_json(path: str) -> dict:
    with open(path, "r") as fh:
        return json.load(fh)

