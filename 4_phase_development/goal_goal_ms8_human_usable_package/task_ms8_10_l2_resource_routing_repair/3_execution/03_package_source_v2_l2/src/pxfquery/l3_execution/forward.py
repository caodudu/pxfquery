"""
forward.py — Forward query: perturbation → functional pathway changes.

Given a perturbation name (gene/drug) and optional cell line,
retrieve the top activated and suppressed functional terms.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, List, Optional, Tuple
import pandas as pd
import numpy as np

if TYPE_CHECKING:
    from anndata import AnnData

from pxfquery.utils import fuzzy_match


class ForwardQuery:
    """
    Forward query engine: pert → func.

    Parameters
    ----------
    adata : AnnData
        Loaded score matrix. obs must contain 'pert_id', 'cmap_name', 'cell_iname'.
        var_names are functional term names.

    Examples
    --------
    >>> fq = ForwardQuery(adata)
    >>> result = fq.query("EGFR", cell_line="A549", top_n=20)
    >>> print(result.scores_df)
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
        perturbation: str,
        cell_line: Optional[str] = None,
        top_n: int = 20,
    ) -> "ForwardResult":
        """
        Query functional changes for a given perturbation.

        Parameters
        ----------
        perturbation : str
            Perturbation name. Can be a gene symbol (e.g. 'EGFR'),
            cmap_name, or pert_id. Fuzzy matched.
        cell_line : str, optional
            If provided, restrict to this cell line (fuzzy matched).
            If None, aggregate across all available cell lines (mean).
        top_n : int
            Number of top activated and suppressed terms to return each.

        Returns
        -------
        ForwardResult
        """
        # 1. Match perturbation
        matched_pert, pert_mask = self._match_perturbation(perturbation)
        if pert_mask.sum() == 0:
            return ForwardResult.empty(perturbation)

        # 2. Optionally filter by cell line
        matched_cell = None
        if cell_line is not None:
            cell_mask, matched_cell = self._match_cell_line(cell_line, pert_mask)
            if cell_mask.sum() == 0:
                return ForwardResult.empty(perturbation,
                                          note=f"Cell line '{cell_line}' not found for '{matched_pert}'")
            final_mask = pert_mask & cell_mask
        else:
            final_mask = pert_mask

        # 3. Extract scores and aggregate (mean across replicates/cell lines)
        scores_matrix = self.adata.X[final_mask]
        if hasattr(scores_matrix, "toarray"):
            scores_matrix = scores_matrix.toarray()
        scores = np.mean(scores_matrix, axis=0)  # shape: (n_terms,)

        # 4. Build result
        scores_series = pd.Series(scores, index=self._term_names, name="score")
        scores_series = scores_series.sort_values(ascending=False)

        n_obs_used = int(final_mask.sum())
        cells_used = self._obs.loc[final_mask, "cell_iname"].unique().tolist()

        return ForwardResult(
            perturbation=matched_pert,
            cell_line=matched_cell,
            scores=scores_series,
            top_n=top_n,
            n_obs=n_obs_used,
            cells_used=cells_used,
        )

    def list_perturbations(self, query: str = "", top_n: int = 10) -> List[str]:
        """
        List available perturbation names matching a query string.

        Parameters
        ----------
        query : str
            Search string. Empty string returns first top_n entries.
        top_n : int

        Returns
        -------
        list of str
        """
        all_perts = self._obs["cmap_name"].dropna().unique().tolist()
        if not query:
            return all_perts[:top_n]
        return fuzzy_match(query, all_perts, top_n=top_n)

    def list_cell_lines(self, perturbation: Optional[str] = None) -> List[str]:
        """
        List available cell lines, optionally filtered by perturbation.

        Parameters
        ----------
        perturbation : str, optional

        Returns
        -------
        list of str
        """
        if perturbation:
            _, mask = self._match_perturbation(perturbation)
            return self._obs.loc[mask, "cell_iname"].unique().tolist()
        return self._obs["cell_iname"].unique().tolist()

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _match_perturbation(self, query: str) -> Tuple[str, "pd.Series"]:
        """Return (matched_name, boolean_mask_on_obs)."""
        candidates = self._obs["cmap_name"].dropna().unique().tolist()
        matches = fuzzy_match(query, candidates, top_n=1)
        if not matches:
            # secondary lookup: try pert_id column
            candidates_id = self._obs["pert_id"].dropna().unique().tolist()
            matches = fuzzy_match(query, candidates_id, top_n=1)
            if not matches:
                return query, pd.Series(False, index=self._obs.index)
            matched = matches[0]
            mask = self._obs["pert_id"] == matched
        else:
            matched = matches[0]
            mask = self._obs["cmap_name"] == matched
        return matched, mask

    def _match_cell_line(
        self, query: str, pert_mask: "pd.Series"
    ) -> Tuple["pd.Series", str]:
        """Return (boolean_mask_on_obs, matched_cell_line_name)."""
        available = self._obs.loc[pert_mask, "cell_iname"].unique().tolist()
        matches = fuzzy_match(query, available, top_n=1)
        if not matches:
            return pd.Series(False, index=self._obs.index), query
        matched = matches[0]
        mask = self._obs["cell_iname"] == matched
        return mask, matched


class ForwardResult:
    """
    Result of a forward query.

    Attributes
    ----------
    perturbation : str
        Matched perturbation name.
    cell_line : str or None
        Matched cell line (None = all cell lines aggregated).
    scores : pd.Series
        All term scores, sorted descending.
    top_activated : pd.Series
        Top N activated terms (score > 0).
    top_suppressed : pd.Series
        Top N suppressed terms (score < 0), sorted by most negative first.
    n_obs : int
        Number of observations used for aggregation.
    cells_used : list of str
        Cell lines included.
    found : bool
        False if no match was found.
    note : str
        Human-readable message (e.g. warning about empty result).
    """

    def __init__(
        self,
        perturbation: str,
        cell_line: Optional[str],
        scores: pd.Series,
        top_n: int,
        n_obs: int,
        cells_used: List[str],
        note: str = "",
    ):
        self.perturbation = perturbation
        self.cell_line = cell_line
        self.scores = scores
        self.n_obs = n_obs
        self.cells_used = cells_used
        self.note = note
        self.found = True

        activated = scores[scores > 0].head(top_n)
        suppressed = scores[scores < 0].tail(top_n).sort_values()
        self.top_activated = activated
        self.top_suppressed = suppressed

    @classmethod
    def empty(
        cls,
        perturbation: str,
        note: str = "",
    ) -> "ForwardResult":
        """Create an empty result when no match is found."""
        obj = object.__new__(cls)
        obj.perturbation = perturbation
        obj.cell_line = None
        obj.scores = pd.Series(dtype=float)
        obj.top_activated = pd.Series(dtype=float)
        obj.top_suppressed = pd.Series(dtype=float)
        obj.n_obs = 0
        obj.cells_used = []
        obj.found = False
        obj.note = note or f"No match found for '{perturbation}'"
        return obj

    def __repr__(self) -> str:
        if not self.found:
            return f"ForwardResult(found=False, note='{self.note}')"
        return (
            f"ForwardResult("
            f"perturbation='{self.perturbation}', "
            f"cell_line={self.cell_line!r}, "
            f"n_obs={self.n_obs}, "
            f"top_activated={len(self.top_activated)}, "
            f"top_suppressed={len(self.top_suppressed)})"
        )
