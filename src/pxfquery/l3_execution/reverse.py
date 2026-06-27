"""
reverse.py — Reverse query: functional target → perturbation candidates.

Given a desired functional profile (which pathways to activate/suppress),
rank perturbations by cosine similarity to the target vector.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional
import pandas as pd
import numpy as np

if TYPE_CHECKING:
    from anndata import AnnData

from pxfquery.utils import fuzzy_match, build_target_vector, cosine_similarity_matrix


class ReverseQuery:
    """
    Reverse query engine: func → pert.

    Parameters
    ----------
    adata : AnnData
        Loaded score matrix. obs must contain 'pert_id', 'cmap_name', 'cell_iname'.
        var_names are functional term names.

    Examples
    --------
    >>> rq = ReverseQuery(adata)
    >>> result = rq.query(
    ...     activate=["HALLMARK_APOPTOSIS"],
    ...     suppress=["HALLMARK_MYC_TARGETS_V1"],
    ...     cell_line="MCF7",
    ...     top_k=20,
    ... )
    >>> print(result.candidates_df)
    """

    def __init__(self, adata: "AnnData"):
        self.adata = adata
        self._obs = adata.obs.copy()
        self._term_names: List[str] = list(adata.var_names)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def query(
        self,
        activate: Optional[List[str]] = None,
        suppress: Optional[List[str]] = None,
        cell_line: Optional[str] = None,
        top_k: int = 20,
        aggregate: bool = True,
    ) -> "ReverseResult":
        """
        Rank perturbations by similarity to a functional target profile.

        Parameters
        ----------
        activate : list of str, optional
            Functional terms to activate (e.g. ['HALLMARK_APOPTOSIS']).
            Fuzzy matched against available terms.
        suppress : list of str, optional
            Functional terms to suppress.
        cell_line : str, optional
            Restrict search to a specific cell line. If None, uses all.
        top_k : int
            Number of top candidates to return.
        aggregate : bool
            If True, aggregate replicates per (pert_id × cell_line) by mean
            before ranking. If False, rank individual experiments.

        Returns
        -------
        ReverseResult
        """
        activate = activate or []
        suppress = suppress or []

        if not activate and not suppress:
            return ReverseResult.empty("No activate/suppress terms provided.")

        # 1. Build target vector
        target_vec = build_target_vector(self._term_names, activate, suppress)

        # Warn about unmatched terms
        unmatched = _find_unmatched(activate + suppress, self._term_names)
        if unmatched:
            print(f"[reverse] Warning: terms not matched: {unmatched}")

        # 2. Filter by cell line
        if cell_line is not None:
            available_cells = self._obs["cell_iname"].unique().tolist()
            cell_matches = fuzzy_match(cell_line, available_cells, top_n=1)
            if not cell_matches:
                return ReverseResult.empty(
                    f"Cell line '{cell_line}' not found."
                )
            matched_cell = cell_matches[0]
            mask = (self._obs["cell_iname"] == matched_cell).values
        else:
            matched_cell = None
            mask = np.ones(len(self._obs), dtype=bool)

        # 3. Get score matrix (subset)
        X = self.adata.X[mask]
        if hasattr(X, "toarray"):
            X = X.toarray()
        obs_sub = self._obs.iloc[mask].copy()

        # 4. Aggregate replicates per (cmap_name, cell_iname)
        if aggregate:
            X_df = pd.DataFrame(X, index=obs_sub.index, columns=self._term_names)
            X_df["cmap_name"] = obs_sub["cmap_name"].values
            X_df["cell_iname"] = obs_sub["cell_iname"].values
            X_agg = X_df.groupby(["cmap_name", "cell_iname"], observed=True)[self._term_names].mean()
            X_matrix = X_agg.values
            row_labels = X_agg.index  # MultiIndex (cmap_name, cell_iname)
        else:
            X_matrix = X
            row_labels = list(zip(obs_sub["cmap_name"], obs_sub["cell_iname"]))

        # 5. Cosine similarity
        sims = cosine_similarity_matrix(X_matrix, target_vec)

        # 6. Rank and build output DataFrame
        ranked_idx = np.argsort(-sims)[:top_k]
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
        candidates.index = candidates.index + 1  # 1-based rank

        # 7. Add driving terms for top candidates
        driving = _get_driving_terms(
            X_matrix, ranked_idx, target_vec, self._term_names, top_n=5
        )
        candidates["driving_terms"] = driving

        return ReverseResult(
            activate=activate,
            suppress=suppress,
            cell_line=matched_cell,
            target_vector=pd.Series(target_vec, index=self._term_names),
            candidates_df=candidates,
        )

    def list_terms(self, query: str = "", top_n: int = 20) -> List[str]:
        """
        List available functional term names.

        Parameters
        ----------
        query : str
            Optional search string.
        top_n : int

        Returns
        -------
        list of str
        """
        if not query:
            return self._term_names[:top_n]
        return fuzzy_match(query, self._term_names, top_n=top_n)

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------


def _find_unmatched(queries: List[str], candidates: List[str]) -> List[str]:
    """Return query terms that could not be fuzzy-matched."""
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
    """
    For each top candidate, return the terms that contributed most
    to the similarity score (element-wise product with target).
    """
    results = []
    for i in ranked_idx:
        row = X[i]
        contrib = row * target_vec
        top_idx = np.argsort(-np.abs(contrib))[:top_n]
        terms = [term_names[j] for j in top_idx if contrib[j] != 0]
        results.append(", ".join(terms))
    return results


class ReverseResult:
    """
    Result of a reverse query.

    Attributes
    ----------
    activate : list of str
        Requested activation terms.
    suppress : list of str
        Requested suppression terms.
    cell_line : str or None
        Cell line filter applied.
    target_vector : pd.Series
        The constructed target profile (+1/-1/0 per term).
    candidates_df : pd.DataFrame
        Ranked candidates with columns: cmap_name, cell_iname,
        similarity, driving_terms. Index = rank (1-based).
    found : bool
    note : str
    """

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
