from __future__ import annotations

import math
from typing import Iterable

import numpy as np


CANDIDATE_COLUMNS = ["cmap_name", "cell_iname", "similarity", "driving_terms"]


def reverse_query(
    matrix,
    activate: Iterable[str],
    suppress: Iterable[str],
    cell_line: str,
    matrix_type: str = "xpr",
    top_n: int = 10,
    low_confidence_threshold: float = 0.05,
) -> dict:
    activate = list(activate or [])
    suppress = list(suppress or [])
    if matrix is None:
        return {
            "error": "NoMatrixLoaded",
            "message": "No functional matrix is loaded. Call PxFquery(matrix_path) or load_data(path) first.",
            "query_type": "system",
        }

    var_names = list(matrix.var_names)
    obs = matrix.obs
    unknown_activate = [program for program in activate if program not in var_names]
    unknown_suppress = [program for program in suppress if program not in var_names]
    if unknown_activate or unknown_suppress:
        return {
            "error": "ProgramNotFound",
            "message": "One or more requested functional program names were not found in the matrix.",
            "unknown_activate": unknown_activate,
            "unknown_suppress": unknown_suppress,
            "query_type": "reverse",
        }

    if "cell_iname" not in obs.columns or cell_line not in set(obs["cell_iname"].astype(str)):
        return {
            "error": "ContextNotFound",
            "message": "The given cell line was not found in the matrix observation metadata.",
            "cell_line": cell_line,
            "matrix_type": matrix_type,
            "query_type": "reverse",
        }

    terms = activate + suppress
    if not terms:
        return {
            "found": False,
            "activate": activate,
            "suppress": suppress,
            "cell_line": cell_line,
            "query_type": "reverse",
            "reason": "no functional target programs were provided",
            "note": "",
        }

    target = np.array([1.0] * len(activate) + [-1.0] * len(suppress), dtype=np.float64)
    target_norm = float(np.linalg.norm(target))
    if target_norm == 0.0:
        return _low_confidence("target vector has zero norm")

    row_mask = obs["cell_iname"].astype(str).to_numpy() == cell_line
    row_indices = np.flatnonzero(row_mask)
    term_indices = [var_names.index(term) for term in terms]
    scores = []
    warnings = []

    for row_index in row_indices:
        row = np.asarray(matrix.X[row_index, term_indices], dtype=np.float64).reshape(-1)
        row_norm = float(np.linalg.norm(row))
        if row_norm == 0.0:
            warnings.append(f"zero-norm candidate skipped: {obs.iloc[row_index].get('sig_id', matrix.obs_names[row_index])}")
            continue
        similarity = float(np.dot(row, target) / (row_norm * target_norm))
        if not math.isfinite(similarity):
            warnings.append(f"non-finite similarity skipped: {obs.iloc[row_index].get('sig_id', matrix.obs_names[row_index])}")
            continue
        scores.append((similarity, row_index))

    if not scores:
        return {
            "found": False,
            "activate": activate,
            "suppress": suppress,
            "cell_line": cell_line,
            "query_type": "reverse",
            "reason": "no perturbations match the requested functional profile",
            "note": "",
            "warnings": warnings,
        }

    max_abs_similarity = max(abs(score) for score, _ in scores)
    if max_abs_similarity < low_confidence_threshold:
        return {
            "error": "LowConfidenceResult",
            "message": "Query returned results but numerical confidence is low.",
            "query_type": "reverse",
            "details": f"max_abs_similarity={max_abs_similarity:.6f}; threshold={low_confidence_threshold:.6f}",
            "warnings": warnings,
        }

    def sort_key(item):
        similarity, row_index = item
        row_obs = obs.iloc[row_index]
        return (
            -similarity,
            str(row_obs.get("cmap_name", "")),
            str(row_obs.get("cell_iname", "")),
            str(row_obs.get("sig_id", matrix.obs_names[row_index])),
        )

    ranked = sorted(scores, key=sort_key)[: max(int(top_n), 0)]
    top_candidates = []
    driving_terms = ", ".join(suppress + activate)
    for similarity, row_index in ranked:
        row_obs = obs.iloc[row_index]
        top_candidates.append(
            {
                "cmap_name": str(row_obs.get("cmap_name", matrix.obs_names[row_index])),
                "cell_iname": str(row_obs.get("cell_iname", cell_line)),
                "similarity": round(float(similarity), 6),
                "driving_terms": driving_terms,
                "sig_id": str(row_obs.get("sig_id", matrix.obs_names[row_index])),
            }
        )

    return {
        "found": bool(top_candidates),
        "activate": activate,
        "suppress": suppress,
        "cell_line": cell_line,
        "candidate_columns": CANDIDATE_COLUMNS,
        "top_candidates": top_candidates,
        "warnings": warnings,
        "note": "Ranking sort keys: similarity descending, cmap_name ascending, cell_iname ascending, sig_id ascending.",
    }


def _low_confidence(details: str) -> dict:
    return {
        "error": "LowConfidenceResult",
        "message": "Query returned results but numerical confidence is low.",
        "query_type": "reverse",
        "details": details,
        "warnings": [],
    }
