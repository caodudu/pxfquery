from __future__ import annotations

import os
from collections import OrderedDict
from pathlib import Path
from typing import Any

import numpy as np

from .data.m1_loader import M1FixtureLoader


VALID_MATRIX_TYPES = {"xpr", "sh", "cp"}


class PxFquery:
    """M1 deterministic forward query entry point backed by the T-046 fixture loader."""

    def __init__(
        self,
        matrix_path: str | None = None,
        matrix_type: str | None = None,
        fixture_root: str | None = None,
    ):
        self.matrix_path = matrix_path
        self.matrix_type = matrix_type or os.environ.get("PXFQUERY_MATRIX_TYPE") or "xpr"
        self.fixture_root = fixture_root
        self.loader: M1FixtureLoader | None = None
        if matrix_path is not None:
            self.load_data(matrix_path, fixture_root=fixture_root)

    def load_data(self, path: str, fixture_root: str | None = None) -> None:
        if not Path(path).is_file():
            raise FileNotFoundError(path)
        self.matrix_path = path
        self.fixture_root = fixture_root
        self.loader = M1FixtureLoader(path, fixture_root=fixture_root)
        _ = self.loader.fixture

    def load_data_dir(self, directory: str, pattern: str = "*.h5ad") -> dict[str, str]:
        return {
            "error": "NotImplemented",
            "message": "load_data_dir is not implemented for the M1 fixture-loader-backed forward core.",
            "query_type": "system",
        }

    def pert2func(
        self,
        perturbation: str,
        cell_line: str,
        matrix_type: str | None = None,
        top_k: int = 20,
    ) -> dict[str, Any]:
        selected_type = _normalize_matrix_type(matrix_type or self.matrix_type)
        if self.loader is None:
            return _no_matrix_loaded()

        fixture = self.loader.fixture
        matrix = getattr(fixture, selected_type)
        obs = matrix.obs

        if "cell_iname" not in obs.columns or "cmap_name" not in obs.columns:
            return {
                "error": "InvalidMatrix",
                "message": "Loaded matrix lacks required obs columns: cell_iname and cmap_name.",
                "query_type": "system",
            }

        pert_values = obs["cmap_name"].astype(str)
        pert_mask = pert_values == perturbation
        if not bool(pert_mask.any()):
            return {
                "error": "PerturbationNotFound",
                "message": f"Perturbation '{perturbation}' was not found in {selected_type} matrix observations.",
                "perturbation": perturbation,
                "matrix_type": selected_type,
                "query_type": "forward",
                "suggestions": [],
            }

        cell_mask = obs["cell_iname"].astype(str) == cell_line
        if not bool(cell_mask.any()):
            return {
                "error": "ContextNotFound",
                "message": f"Cell line '{cell_line}' was not found in {selected_type} matrix observations.",
                "cell_line": cell_line,
                "matrix_type": selected_type,
                "query_type": "forward",
            }

        exact_mask = cell_mask & pert_mask
        if not bool(exact_mask.any()):
            return {
                "error": "PerturbationNotFound",
                "message": (
                    f"Perturbation '{perturbation}' was found, but not for cell line "
                    f"'{cell_line}' in {selected_type} matrix observations."
                ),
                "perturbation": perturbation,
                "matrix_type": selected_type,
                "query_type": "forward",
                "suggestions": [],
            }

        row_positions = np.flatnonzero(exact_mask.to_numpy())
        values = np.asarray(matrix.X[row_positions], dtype=float)
        mean_scores = values.mean(axis=0)
        scores = list(zip([str(v) for v in matrix.var_names], [float(v) for v in mean_scores]))
        activated = sorted((item for item in scores if item[1] > 0), key=lambda item: item[1], reverse=True)
        suppressed = sorted((item for item in scores if item[1] < 0), key=lambda item: item[1])

        return {
            "found": True,
            "perturbation": perturbation,
            "cell_line": cell_line,
            "n_obs": int(len(row_positions)),
            "cells_used": sorted(set(obs.iloc[row_positions]["cell_iname"].astype(str).tolist())),
            "top_activated": _ordered_score_dict(activated[:top_k]),
            "top_suppressed": _ordered_score_dict(suppressed[:top_k]),
            "note": "",
            "warnings": [],
        }

    def func2pert(
        self,
        activate: list[str],
        suppress: list[str],
        cell_line: str,
        matrix_type: str | None = None,
        top_n: int = 10,
    ) -> dict[str, Any]:
        return {
            "error": "NotImplemented",
            "message": "Reverse query is outside the T-048 forward-core implementation scope.",
            "query_type": "system",
        }

    def query(self, **kwargs: Any) -> dict[str, Any]:
        has_perturbation = kwargs.get("perturbation") is not None
        has_function_targets = bool(kwargs.get("activate") or kwargs.get("suppress"))
        if has_perturbation and has_function_targets:
            return {
                "error": "AmbiguousQuery",
                "message": "Both perturbation and functional targets were provided.",
                "query_type": "unknown",
            }
        if has_perturbation:
            return self.pert2func(
                perturbation=kwargs["perturbation"],
                cell_line=kwargs.get("cell_line"),
                matrix_type=kwargs.get("matrix_type"),
                top_k=kwargs.get("top_k", 20),
            )
        if has_function_targets:
            return self.func2pert(
                activate=kwargs.get("activate") or [],
                suppress=kwargs.get("suppress") or [],
                cell_line=kwargs.get("cell_line"),
                matrix_type=kwargs.get("matrix_type"),
                top_n=kwargs.get("top_n", 10),
            )
        return {
            "error": "UnsupportedQuery",
            "message": "Neither perturbation nor activate/suppress targets were provided.",
            "query_type": "unknown",
        }


def _normalize_matrix_type(matrix_type: str) -> str:
    if matrix_type not in VALID_MATRIX_TYPES:
        raise ValueError(f"Unsupported matrix_type '{matrix_type}'. Expected one of {sorted(VALID_MATRIX_TYPES)}.")
    return matrix_type


def _ordered_score_dict(items: list[tuple[str, float]]) -> dict[str, float]:
    return OrderedDict((name, round(value, 6)) for name, value in items)


def _no_matrix_loaded() -> dict[str, str]:
    return {
        "error": "NoMatrixLoaded",
        "message": "No functional matrix is loaded. Call PxFquery(matrix_path) or load_data(path) first.",
        "query_type": "system",
    }
