"""
reverse.py — Reverse query: functional target → perturbation candidates.

Given a desired functional profile (which pathways to activate/suppress),
rank perturbations by cosine similarity to the target vector.

T-032 stability guard: query() now carries a GuardReport and aggregates
warnings from cosine_similarity_matrix and build_target_vector into
ReverseResult.warnings for downstream serialization.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional, Dict, Any
import pandas as pd
import numpy as np

if TYPE_CHECKING:
    from anndata import AnnData

from ..utils import (
    fuzzy_match,
    build_target_vector,
    cosine_similarity_matrix,
    GuardReport,
    GuardEvent,
)


class ReverseQuery:
    def __init__(self, adata: "AnnData"):
        self.adata = adata
        self._obs = adata.obs.copy()
        self._term_names: List[str] = list(adata.var_names)

    def query(
        self,
        activate: Optional[List[str]] = None,
        suppress: Optional[List[str]] = None,
        cell_line: Optional[str] = None,
        top_k: int = 20,
        aggregate: bool = True,
    ) -> "ReverseResult":
        activate = activate or []
        suppress = suppress or []

        if not activate and not suppress:
            return ReverseResult.empty("No activate/suppress terms provided.")

        guard = GuardReport()

        target_vec, matched_terms, unmatched_terms = build_target_vector(
            self._term_names, activate, suppress
        )

        if unmatched_terms:
            guard.add(
                severity="warning",
                scenario="unmatched_terms",
                message=f"Query terms not matched to any functional term: {unmatched_terms}",
                indices=[],
            )
            print(f"[reverse] Warning: terms not matched: {unmatched_terms}")

        if not matched_terms:
            guard.add(
                severity="warning",
                scenario="target_empty",
                message="No activate or suppress terms could be fuzzy-matched to available "
                        "functional terms. Returning empty result.",
                indices=[],
            )
            result = ReverseResult.empty(
                f"No activate/suppress terms matched. Unmatched: {unmatched_terms}"
            )
            result.warnings = guard.warnings
            return result

        vec_norm = float(np.linalg.norm(target_vec))
        if vec_norm == 0.0:
            guard.add(
                severity="warning",
                scenario="zero_norm_target",
                message="Target vector norm is 0 after fuzzy matching. "
                        "No perturbation ranking is possible.",
                indices=[],
            )
            result = ReverseResult.empty(
                "Target vector norm is zero (no matched activate/suppress terms)."
            )
            result.warnings = guard.warnings
            return result

        if cell_line is not None:
            available_cells = self._obs["cell_iname"].unique().tolist()
            cell_matches = fuzzy_match(cell_line, available_cells, top_n=1)
            if not cell_matches:
                guard.add(
                    severity="notice",
                    scenario="cell_not_found",
                    message=f"Cell line '{cell_line}' not found in matrix.",
                    indices=[],
                )
                return ReverseResult.empty(
                    f"Cell line '{cell_line}' not found."
                )
            matched_cell = cell_matches[0]
            mask = (self._obs["cell_iname"] == matched_cell).values
        else:
            matched_cell = None
            mask = np.ones(len(self._obs), dtype=bool)

        X = self.adata.X[mask]
        if hasattr(X, "toarray"):
            X = X.toarray()
        obs_sub = self._obs.iloc[mask].copy()

        if X.shape[0] == 0:
            guard.add(
                severity="warning",
                scenario="empty_matrix",
                message=f"No observations after cell-line filter '{matched_cell}'.",
                indices=[],
            )
            result = ReverseResult.empty(
                f"No observations after filtering for cell line '{matched_cell}'."
            )
            result.warnings = guard.warnings
            return result

        if aggregate:
            X_df = pd.DataFrame(X, index=obs_sub.index, columns=self._term_names)
            X_df["cmap_name"] = obs_sub["cmap_name"].values
            X_df["cell_iname"] = obs_sub["cell_iname"].values
            X_agg = X_df.groupby(["cmap_name", "cell_iname"], observed=True)[self._term_names].mean()
            X_matrix = X_agg.values
            row_labels = X_agg.index
        else:
            X_matrix = X
            row_labels = list(zip(obs_sub["cmap_name"], obs_sub["cell_iname"]))

        sims = cosine_similarity_matrix(X_matrix, target_vec, guard=guard)

        if len(guard) > 0:
            n_abnormal = len([e for e in guard._events if e.scenario != "unmatched_terms"])
            if n_abnormal > 0:
                print(f"[reverse] Guard: {n_abnormal} numerical stability warnings emitted")

        finite_mask = ~np.isnan(sims) & ~np.isinf(sims)
        valid_sims = sims[finite_mask]
        valid_indices = np.where(finite_mask)[0]

        if len(valid_sims) == 0:
            guard.add(
                severity="warning",
                scenario="no_valid_rows",
                message="All rows produced NaN/Inf similarity after guard filtering. "
                        "No candidates to rank.",
                indices=[],
            )
            result = ReverseResult.empty(
                "No valid similarity scores after stability guard filtering."
            )
            result.warnings = guard.warnings
            return result

        top_k_actual = min(top_k, len(valid_sims))
        ranked_idx_local = np.argsort(-valid_sims)[:top_k_actual]
        ranked_idx = valid_indices[ranked_idx_local]

        if aggregate:
            candidates = pd.DataFrame(
                {
                    "cmap_name": [row_labels[i][0] for i in ranked_idx],
                    "cell_iname": [row_labels[i][1] for i in ranked_idx],
                    "similarity": sims[ranked_idx],
                }
            )
        else:
            candidates = pd.DataFrame(
                {
                    "cmap_name": [row_labels[i][0] for i in ranked_idx],
                    "cell_iname": [row_labels[i][1] for i in ranked_idx],
                    "similarity": sims[ranked_idx],
                }
            )
        candidates = candidates.reset_index(drop=True)
        candidates.index = candidates.index + 1

        driving = _get_driving_terms(
            X_matrix, ranked_idx, target_vec, self._term_names, top_n=5
        )
        candidates["driving_terms"] = driving

        result = ReverseResult(
            activate=activate,
            suppress=suppress,
            cell_line=matched_cell,
            target_vector=pd.Series(target_vec, index=self._term_names),
            candidates_df=candidates,
        )
        result.matched_terms = matched_terms
        result.unmatched_terms = unmatched_terms
        result.warnings = guard.warnings
        return result

    def list_terms(self, query: str = "", top_n: int = 20) -> List[str]:
        if not query:
            return self._term_names[:top_n]
        return fuzzy_match(query, self._term_names, top_n=top_n)


def _find_unmatched(queries: List[str], candidates: List[str]) -> List[str]:
    unmatched = []
    for q in queries:
        if not fuzzy_match(q, candidates, top_n=1):
            unmatched.append(q)
    return unmatched


def _get_driving_terms(
    X: np.ndarray,
    ranked_idx: np.ndarray,
    target_vec: np.ndarray,
    term_names: List[str],
    top_n: int = 5,
) -> List[str]:
    results = []
    for i in ranked_idx:
        row = X[i]
        contrib = row * target_vec
        top_idx = np.argsort(-np.abs(contrib))[:top_n]
        terms = [term_names[j] for j in top_idx if contrib[j] != 0]
        results.append(", ".join(terms))
    return results


class ReverseResult:
    def __init__(
        self,
        activate: List[str],
        suppress: List[str],
        cell_line: Optional[str],
        target_vector: pd.Series,
        candidates_df: pd.DataFrame,
        note: str = "",
    ):
        self.activate = activate
        self.suppress = suppress
        self.cell_line = cell_line
        self.target_vector = target_vector
        self.candidates_df = candidates_df
        self.note = note
        self.found = True
        self.matched_terms: List[str] = []
        self.unmatched_terms: List[str] = []
        self.warnings: List[dict] = []

    @classmethod
    def empty(cls, note: str) -> "ReverseResult":
        obj = object.__new__(cls)
        obj.activate = []
        obj.suppress = []
        obj.cell_line = None
        obj.target_vector = pd.Series(dtype=float)
        obj.candidates_df = pd.DataFrame()
        obj.note = note
        obj.found = False
        obj.matched_terms = []
        obj.unmatched_terms = []
        obj.warnings = []
        return obj

    def __repr__(self) -> str:
        if not self.found:
            return f"ReverseResult(found=False, note='{self.note}')"
        return (
            f"ReverseResult("
            f"activate={self.activate}, "
            f"suppress={self.suppress}, "
            f"cell_line={self.cell_line!r}, "
            f"n_candidates={len(self.candidates_df)})"
        )