from __future__ import annotations

import numpy as np


def forward_query(matrix, perturbation: str, cell_line: str, matrix_type: str = "xpr", top_k: int = 20) -> dict:
    if matrix is None:
        return {
            "error": "NoMatrixLoaded",
            "message": "No functional matrix is loaded. Call PxFquery(matrix_path) or load_data(path) first.",
            "query_type": "system",
        }
    obs = matrix.obs
    if "cmap_name" not in obs.columns or perturbation not in set(obs["cmap_name"].astype(str)):
        return {
            "error": "PerturbationNotFound",
            "message": "The given perturbation name was not found in the matrix observation metadata.",
            "perturbation": perturbation,
            "matrix_type": matrix_type,
            "query_type": "forward",
            "suggestions": [],
        }
    if "cell_iname" not in obs.columns or cell_line not in set(obs["cell_iname"].astype(str)):
        return {
            "error": "ContextNotFound",
            "message": "The given cell line was not found in the matrix observation metadata.",
            "cell_line": cell_line,
            "matrix_type": matrix_type,
            "query_type": "forward",
        }
    mask = (obs["cmap_name"].astype(str).to_numpy() == perturbation) & (
        obs["cell_iname"].astype(str).to_numpy() == cell_line
    )
    row_indices = np.flatnonzero(mask)
    if len(row_indices) == 0:
        return {
            "found": False,
            "perturbation": perturbation,
            "cell_line": cell_line,
            "query_type": "forward",
            "reason": "perturbation and cell line combination not found in matrix",
            "note": "",
        }
    values = np.asarray(matrix.X[row_indices], dtype=float).mean(axis=0)
    pairs = list(zip(list(matrix.var_names), values))
    activated = sorted((p for p in pairs if p[1] > 0), key=lambda item: (-item[1], item[0]))[:top_k]
    suppressed = sorted((p for p in pairs if p[1] < 0), key=lambda item: (item[1], item[0]))[:top_k]
    return {
        "found": True,
        "perturbation": perturbation,
        "cell_line": cell_line,
        "n_obs": int(len(row_indices)),
        "cells_used": [cell_line],
        "top_activated": {name: round(float(value), 6) for name, value in activated},
        "top_suppressed": {name: round(float(value), 6) for name, value in suppressed},
        "note": "",
        "warnings": [],
    }
