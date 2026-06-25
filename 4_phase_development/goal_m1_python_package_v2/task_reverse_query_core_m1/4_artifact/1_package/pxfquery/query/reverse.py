from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Any, Iterable

import numpy as np


VALID_MATRIX_TYPES = {"cp", "sh", "xpr"}
DEFAULT_LOW_CONFIDENCE_THRESHOLD = 0.05


def cosine_similarity(a: Iterable[float], b: Iterable[float]) -> float:
    left = np.asarray(list(a), dtype=float)
    right = np.asarray(list(b), dtype=float)
    denom = float(np.linalg.norm(left) * np.linalg.norm(right))
    if denom == 0.0:
        return float("nan")
    return float(np.dot(left, right) / denom)


@dataclass
class ReverseQueryCore:
    fixture: Any | None = None
    low_confidence_threshold: float = DEFAULT_LOW_CONFIDENCE_THRESHOLD

    def func2pert(
        self,
        activate: list[str],
        suppress: list[str],
        cell_line: str,
        matrix_type: str | None = None,
        top_n: int = 10,
    ) -> dict[str, Any]:
        matrix_name = matrix_type or "xpr"
        if self.fixture is None:
            return {
                "error": "NoMatrixLoaded",
                "message": "No functional matrix is loaded. Call PxFquery(matrix_path) or load_data(path) first.",
                "query_type": "system",
            }
        if matrix_name not in VALID_MATRIX_TYPES:
            return {
                "error": "InvalidMatrix",
                "message": f"Unsupported matrix_type '{matrix_name}'. Expected one of cp, sh, xpr.",
                "query_type": "system",
            }

        matrix = getattr(self.fixture, matrix_name)
        var_names = self.fixture.matrix_var_names(matrix_name)
        unknown_activate = [term for term in activate if term not in var_names]
        unknown_suppress = [term for term in suppress if term not in var_names]
        if unknown_activate or unknown_suppress:
            return {
                "error": "ProgramNotFound",
                "message": "One or more requested functional program names were not found in the matrix.",
                "unknown_activate": unknown_activate,
                "unknown_suppress": unknown_suppress,
                "query_type": "reverse",
            }

        if "cell_iname" not in matrix.obs.columns:
            return {
                "error": "InvalidMatrix",
                "message": f"Matrix '{matrix_name}' is missing required obs column 'cell_iname'.",
                "query_type": "system",
            }
        if cell_line not in set(matrix.obs["cell_iname"].astype(str)):
            return {
                "error": "ContextNotFound",
                "message": "The given cell line was not found in the matrix observation metadata.",
                "cell_line": cell_line,
                "matrix_type": matrix_name,
                "query_type": "reverse",
            }

        requested_terms = list(activate) + list(suppress)
        if not requested_terms:
            return {
                "error": "ProgramNotFound",
                "message": "At least one activate or suppress functional program is required.",
                "unknown_activate": [],
                "unknown_suppress": [],
                "query_type": "reverse",
            }

        target = [1.0 for _ in activate] + [-1.0 for _ in suppress]
        warnings: list[str] = []
        candidates: list[dict[str, Any]] = []
        obs = matrix.obs
        for sig_id in self.fixture.get_sig_ids(matrix_name):
            row_meta = obs.loc[sig_id]
            if str(row_meta["cell_iname"]) != cell_line:
                continue
            row = self.fixture.get_matrix_row(matrix_name, sig_id)
            observed = [float(row[term]) for term in requested_terms]
            similarity = cosine_similarity(target, observed)
            if not math.isfinite(similarity):
                warnings.append(f"Non-finite similarity filtered for sig_id={sig_id}")
                continue
            candidates.append(
                {
                    "cmap_name": str(row_meta.get("cmap_name", "")),
                    "cell_iname": str(row_meta.get("cell_iname", "")),
                    "similarity": similarity,
                    "driving_terms": ", ".join(requested_terms),
                    "sig_id": str(sig_id),
                    "pert_id": str(row_meta.get("pert_id", "")),
                }
            )

        if not candidates:
            return {
                "found": False,
                "activate": activate,
                "suppress": suppress,
                "cell_line": cell_line,
                "query_type": "reverse",
                "reason": "no perturbations match the requested functional profile",
                "note": "",
            }

        # Deterministic rank: higher similarity first, then stable lexical identifiers.
        candidates.sort(
            key=lambda item: (
                -item["similarity"],
                item["cmap_name"],
                item["cell_iname"],
                item["sig_id"],
            )
        )
        max_abs_similarity = max(abs(item["similarity"]) for item in candidates)
        if max_abs_similarity < self.low_confidence_threshold:
            return {
                "error": "LowConfidenceResult",
                "message": "Query returned results but numerical confidence is low.",
                "query_type": "reverse",
                "details": (
                    f"max_abs_similarity={max_abs_similarity:.6g}; "
                    f"threshold={self.low_confidence_threshold:.6g}"
                ),
                "warnings": warnings,
            }

        public_candidates = [
            {
                "cmap_name": item["cmap_name"],
                "cell_iname": item["cell_iname"],
                "similarity": item["similarity"],
                "driving_terms": item["driving_terms"],
            }
            for item in candidates[: max(0, int(top_n))]
        ]
        return {
            "found": True,
            "activate": activate,
            "suppress": suppress,
            "cell_line": cell_line,
            "candidate_columns": ["cmap_name", "cell_iname", "similarity", "driving_terms"],
            "top_candidates": public_candidates,
            "warnings": warnings,
            "note": "",
        }

