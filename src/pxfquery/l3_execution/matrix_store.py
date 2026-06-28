from __future__ import annotations

import os
import json
import time
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
    matrix_cache_path: str | None
    obs_path: str
    var_path: str


class FunctionalMatrixStore:
    def __init__(self, resources: ResourceManager, *, auto_download: bool = True, cache: dict[str, FunctionalMatrix] | None = None) -> None:
        self.resources = resources
        self.auto_download = auto_download
        self._cache: dict[str, FunctionalMatrix] = cache if cache is not None else {}

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

        X, matrix_cache_path = _read_matrix(matrix_path)
        obs = _read_obs(obs_path)
        var_names = _read_var_names(var_path)
        if X.shape[0] != len(obs):
            raise ValueError(f"schema_mismatch: {modality} X rows {X.shape[0]} != obs rows {len(obs)}")
        if X.shape[1] != len(var_names):
            raise ValueError(f"schema_mismatch: {modality} X cols {X.shape[1]} != var_names {len(var_names)}")
        matrix = FunctionalMatrix(
            modality=modality,
            X=np.asarray(X),
            obs=obs.reset_index(drop=False).rename(columns={"index": "_obs_index"}),
            var_names=list(map(str, var_names)),
            matrix_path=str(matrix_path),
            matrix_cache_path=str(matrix_cache_path) if matrix_cache_path else None,
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


def _read_matrix(path: Path) -> tuple[np.ndarray, Path | None]:
    if path.suffix == ".npy":
        return np.load(path, mmap_mode="r"), path
    cache_path = _materialized_npy_path(path)
    if cache_path.exists():
        return np.load(cache_path, mmap_mode="r"), cache_path
    _materialize_npy(path, cache_path)
    return np.load(cache_path, mmap_mode="r"), cache_path


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


def _materialized_npy_path(path: Path) -> Path:
    return path.with_suffix(".npy")


def _materialize_npy(source: Path, target: Path) -> None:
    lock = target.with_suffix(target.suffix + ".lock")
    _acquire_lock(lock)
    try:
        if target.exists():
            return
        tmp = target.with_suffix(target.suffix + ".part")
        tmp.unlink(missing_ok=True)
        matrix = _read_npz_matrix(source)
        with tmp.open("wb") as handle:
            np.save(handle, np.asarray(matrix))
        os.replace(tmp, target)
    finally:
        lock.unlink(missing_ok=True)


def _acquire_lock(path: Path, *, timeout: float = 900.0, poll: float = 0.25) -> None:
    started = time.time()
    while True:
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                handle.write(str(os.getpid()))
            return
        except FileExistsError:
            if time.time() - started > timeout:
                raise TimeoutError(f"timed out waiting for matrix cache lock: {path}")
            time.sleep(poll)


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
