from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from pxfquery.resources import ResourceManager


@dataclass
class FunctionalMatrix:
    modality: str
    X: np.ndarray
    obs: pd.DataFrame
    var_names: list[str]
    matrix_path: str
    obs_path: str
    var_path: str


class FunctionalMatrixStore:
    def __init__(self, resources: ResourceManager, *, auto_download: bool = True) -> None:
        self.resources = resources
        self.auto_download = auto_download
        self._cache: dict[str, FunctionalMatrix] = {}

    def load(self, modality: str) -> FunctionalMatrix:
        modality = _normalize_modality(modality)
        if modality in self._cache:
            return self._cache[modality]
        status = self.resources.ensure(
            "l3_functional_scores",
            modalities=[modality],
            auto_download=self.auto_download,
        )
        if not status.available:
            missing = ", ".join(status.missing_files)
            raise FileNotFoundError(f"missing L3 resources for {modality}: {missing}")

        matrix_path = self.resources.path("l3_functional_scores", modality=modality, kind="matrix")
        obs_path = self.resources.path("l3_functional_scores", modality=modality, kind="obs")
        var_path = self.resources.path("l3_functional_scores", modality=modality, kind="var")

        X = _read_npz_matrix(matrix_path)
        obs = _read_obs(obs_path)
        var_names = _read_var_names(var_path)
        if X.shape[0] != len(obs):
            raise ValueError(f"schema_mismatch: {modality} X rows {X.shape[0]} != obs rows {len(obs)}")
        if X.shape[1] != len(var_names):
            raise ValueError(f"schema_mismatch: {modality} X cols {X.shape[1]} != var_names {len(var_names)}")
        matrix = FunctionalMatrix(
            modality=modality,
            X=np.asarray(X, dtype=np.float32),
            obs=obs.reset_index(drop=False).rename(columns={"index": "_obs_index"}),
            var_names=list(map(str, var_names)),
            matrix_path=str(matrix_path),
            obs_path=str(obs_path),
            var_path=str(var_path),
        )
        self._cache[modality] = matrix
        return matrix


def _normalize_modality(modality: str) -> str:
    value = str(modality).lower().strip()
    if value not in {"cp", "sh", "xpr"}:
        raise ValueError(f"unsupported_modality: {modality}")
    return value


def _read_npz_matrix(path: Path) -> np.ndarray:
    payload = np.load(path)
    if "X" in payload:
        return payload["X"]
    if {"data", "indices", "indptr", "shape"}.issubset(payload.files):
        from scipy import sparse

        matrix = sparse.csr_matrix(
            (payload["data"].astype(np.float32), payload["indices"], payload["indptr"]),
            shape=tuple(payload["shape"]),
        )
        return matrix.toarray()
    first = payload.files[0]
    return payload[first]


def _read_obs(path: Path) -> pd.DataFrame:
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    return pd.read_csv(path)


def _read_var_names(path: Path) -> list[str]:
    payload: Any = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return [str(v) for v in payload]
    if isinstance(payload, dict) and "var_names" in payload:
        return [str(v) for v in payload["var_names"]]
    raise ValueError(f"schema_mismatch: invalid var_names file {path}")
