"""
utils.py — Shared utility functions for PxFquery.

T-032 stability guard: cosine_similarity_matrix now emits structured
GuardEvent warnings for zero-norm rows, zero-norm targets, NaN/Inf rows,
instead of silently filling NaN/Inf into the candidate ranking.

build_target_vector now returns (vector, matched_terms, unmatched_terms)
so the caller can detect when no terms were fuzzy-matched.
"""

from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class GuardEvent:
    severity: str
    scenario: str
    message: str
    indices: List[int] = field(default_factory=list)

    def to_dict(self):
        return {
            "severity": self.severity,
            "scenario": self.scenario,
            "message": self.message,
            "indices": self.indices,
        }


class GuardReport:
    def __init__(self):
        self._events: List[GuardEvent] = []

    def add(self, **kwargs):
        self._events.append(GuardEvent(**kwargs))

    @property
    def warnings(self) -> List[dict]:
        return [e.to_dict() for e in self._events]

    def __len__(self):
        return len(self._events)

    def __bool__(self):
        return len(self._events) > 0

    def scenario_events(self, scenario: str) -> List[dict]:
        return [e.to_dict() for e in self._events if e.scenario == scenario]


def fuzzy_match(query: str, candidates: List[str], top_n: int = 5) -> List[str]:
    q = query.strip().lower()
    q_tokens = set(re.split(r"[\s_\-]+", q))

    exact = [c for c in candidates if c.lower() == q]
    if exact:
        return exact[:top_n]

    substring = [c for c in candidates if q in c.lower()]
    if substring:
        return substring[:top_n]

    scored = []
    for c in candidates:
        c_tokens = set(re.split(r"[\s_\-]+", c.lower()))
        overlap = len(q_tokens & c_tokens)
        if overlap > 0:
            scored.append((overlap, c))
    scored.sort(key=lambda x: -x[0])
    return [c for _, c in scored[:top_n]]


def _strict_match_one(query: str, candidates: List[str]) -> Optional[str]:
    """
    Strict match for build_target_vector: exact or substring only.
    Avoids token-overlap false positives (e.g. 'TERM' matching 'TERM_GAMMA').
    """
    q = query.strip().lower()
    for c in candidates:
        if c.lower() == q:
            return c
    for c in candidates:
        if q in c.lower():
            return c
    return None


def build_target_vector(
    term_names: List[str],
    activate: List[str],
    suppress: List[str],
) -> Tuple["np.ndarray", List[str], List[str]]:
    import numpy as np
    vec = np.zeros(len(term_names), dtype=float)
    matched_activate = []
    matched_suppress = []
    unmatched_activate = []
    unmatched_suppress = []
    for t in activate:
        match = _strict_match_one(t, term_names)
        if match is not None:
            idx = term_names.index(match)
            vec[idx] = 1.0
            matched_activate.append(t)
        else:
            unmatched_activate.append(t)
    for t in suppress:
        match = _strict_match_one(t, term_names)
        if match is not None:
            idx = term_names.index(match)
            vec[idx] = -1.0
            matched_suppress.append(t)
        else:
            unmatched_suppress.append(t)
    matched_terms = matched_activate + matched_suppress
    unmatched_terms = unmatched_activate + unmatched_suppress
    return vec, matched_terms, unmatched_terms


def cosine_similarity_matrix(
    matrix: "np.ndarray",
    vec: "np.ndarray",
    guard: Optional["GuardReport"] = None,
) -> "np.ndarray":
    import numpy as np

    n_rows = matrix.shape[0]
    sims = np.empty(n_rows, dtype=float)

    row_norms = np.linalg.norm(matrix, axis=1)
    vec_norm_val = np.linalg.norm(vec)

    if vec_norm_val == 0.0:
        if guard is not None:
            guard.add(
                severity="warning",
                scenario="zero_norm_target",
                message=f"Target vector norm is 0 (all-zero target). "
                        f"Returning zeros for all {n_rows} rows.",
                indices=list(range(n_rows)),
            )
        return np.zeros(n_rows, dtype=float)

    nan_rows = np.isnan(row_norms)
    if nan_rows.any() and guard is not None:
        idx = list(np.where(nan_rows)[0])
        guard.add(
            severity="warning",
            scenario="nan_row",
            message=f"NaN-norm rows detected at indices {idx}. "
                    f"Setting similarity to 0.0 for these rows.",
            indices=idx,
        )

    inf_rows = np.isinf(row_norms) & ~nan_rows
    if inf_rows.any() and guard is not None:
        idx = list(np.where(inf_rows)[0])
        guard.add(
            severity="warning",
            scenario="inf_row",
            message=f"Inf-norm rows detected at indices {idx}. "
                    f"Setting similarity to 0.0 for these rows.",
            indices=idx,
        )

    zero_rows = (row_norms == 0.0) & ~nan_rows
    if zero_rows.any() and guard is not None:
        idx = list(np.where(zero_rows)[0])
        guard.add(
            severity="notice",
            scenario="zero_norm_row",
            message=f"Zero-norm rows detected at indices {idx}. "
                    f"Setting similarity to 0.0 for these rows.",
            indices=idx,
        )

    valid = ~nan_rows & ~inf_rows
    inner = matrix @ vec

    inner_nan = np.isnan(inner)
    if inner_nan.any() and guard is not None:
        idx = list(np.where(inner_nan)[0])
        guard.add(
            severity="warning",
            scenario="nan_row",
            message=f"NaN values in matrix rows at indices {idx}. "
                    f"Setting similarity to 0.0.",
            indices=idx,
        )

    inner_inf = np.isinf(inner) & ~inner_nan
    if inner_inf.any() and guard is not None:
        idx = list(np.where(inner_inf)[0])
        guard.add(
            severity="warning",
            scenario="inf_row",
            message=f"Inf values in matrix rows at indices {idx}. "
                    f"Setting similarity to 0.0.",
            indices=idx,
        )

    problematic = nan_rows | inf_rows | zero_rows | inner_nan | inner_inf
    sims[problematic] = 0.0

    ok = ~problematic
    if ok.any():
        denom = row_norms[ok] * vec_norm_val
        sims[ok] = inner[ok] / denom
        sims[ok] = np.clip(sims[ok], -1.0, 1.0)

    return sims