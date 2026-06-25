"""
pxfquery_T031_forward_no_hit_guard.py — T-031 no-hit safety guard

Wraps ForwardQuery to prevent fuzzy false-positive perturbation matches.
When the underlying match quality falls below the configured threshold,
returns ForwardResult.found=False with NOT_FOUND evidence instead of
silently matching a near-token perturbation.

Compatible as a drop-in wrapper: ForwardQuery is used as-is; the guard
intercepts and validates the match after ForwardQuery returns, so
it does not modify T-024 workspace files.

Usage example:
    from loader import load_matrix
    from pxfquery.query.forward import ForwardQuery
    from pxfquery_T031_forward_no_hit_guard import NoHitGuardForwardQuery

    adata, _ = load_matrix(path)
    engine = NoHitGuardForwardQuery(adata)
    result = engine.query("EGFR", cell_line="A549")  # found=True
    result = engine.query("egr", cell_line="A549")    # found=False (short token)
    result = engine.query("egfr_random", cell_line="A549")  # found=False (1-token overlap only)
    result = engine.query("NONSENSE_ZZZ999")           # found=False

Tunable parameters (set on instance):
    min_overlap_for_token_fallback : int = 2
        Minimum number of shared tokens required for token-overlap match to be accepted.
    min_query_length_for_substring : int = 4
        Minimum query length for substring match to be accepted.

Lineage:
    Source: T-024 workspace ForwardQuery + fuzzy_match
    Repaired in: T-031 no_hit_guard_v1
    Version: pxfquery-T-031
"""

from __future__ import annotations
from typing import List, Optional
import re

from pxfquery.query.forward import ForwardQuery, ForwardResult


class NoHitGuardForwardQuery(ForwardQuery):
    """
    ForwardQuery wrapper with no-hit safety guard.

    Parameters
    ----------
    adata : AnnData
        Same as ForwardQuery accepts.
    min_overlap_for_token_fallback : int
        Minimum shared token count for token-overlap fuzzy fallback.
        Default 2 means a single shared token (eg. 'random_egfr' sharing 'egfr'
        with 'EGFR') is rejected as insufficient.
    min_query_length_for_substring : int
        Minimum length of query substring for substring-match acceptance.
        Default 4 prevents short random substrings like 'egr' from matching
        EGR1/EGR2/EGR3.
    """

    def __init__(
        self,
        adata,
        min_overlap_for_token_fallback: int = 2,
        min_query_length_for_substring: int = 4,
    ):
        super().__init__(adata)
        self.min_overlap_for_token_fallback = min_overlap_for_token_fallback
        self.min_query_length_for_substring = min_query_length_for_substring
        self.guard_version = "pxfquery-T-031"

    def query(
        self,
        perturbation: str,
        cell_line: Optional[str] = None,
        top_n: int = 20,
    ) -> ForwardResult:
        result = super().query(perturbation, cell_line=cell_line, top_n=top_n)

        if not result.found:
            return result

        quality = self._assess_match_quality(perturbation, result.perturbation)
        if not quality["accepted"]:
            return ForwardResult.empty(
                perturbation,
                note=(
                    f"No-hit guard (pxfquery-T-031): "
                    f"query '{perturbation}' matched '{result.perturbation}' "
                    f"via {quality['mechanism']} but failed quality check "
                    f"(reason: {quality['reason']}). "
                    f"Threshold: min_overlap_for_token_fallback={self.min_overlap_for_token_fallback}, "
                    f"min_query_length_for_substring={self.min_query_length_for_substring}."
                ),
            )
        return result

    def _assess_match_quality(
        self, query: str, matched: str
    ) -> dict:
        """
        Assess whether a perturbation match is plausible given the query.

        Returns a dict with keys 'accepted', 'mechanism', 'reason'.

        Strategies, ordered by confidence:
        1. Exact match (case-insensitive full equality): always accepted.
        2. Substring match: accepted only if query is long enough to
           avoid random 1-3 char overlap.
        3. Token-overlap match: requires at least min_overlap_for_token_fallback
           shared tokens between query and candidate.

        """
        q = query.strip()
        m = matched.strip()

        # 1. Exact match
        if q.lower() == m.lower():
            return {"accepted": True, "mechanism": "exact", "reason": ""}

        # 2. Substring: q ⊂ m
        if q.lower() in m.lower():
            if len(q) >= self.min_query_length_for_substring:
                return {"accepted": True, "mechanism": "substring", "reason": ""}
            return {
                "accepted": False,
                "mechanism": "substring",
                "reason": (
                    f"query '{q}' ({len(q)} chars) is too short for substring match "
                    f"(min {self.min_query_length_for_substring} required)"
                ),
            }

        # 3. Token-overlap (the most dangerous fallback)
        q_tokens = set(re.split(r"[\s_\-]+", q.lower()))
        m_tokens = set(re.split(r"[\s_\-]+", m.lower()))
        overlap = q_tokens & m_tokens
        overlap_count = len(overlap)

        if overlap_count >= self.min_overlap_for_token_fallback:
            return {"accepted": True, "mechanism": f"token_overlap({overlap_count})", "reason": ""}

        return {
            "accepted": False,
            "mechanism": f"token_overlap({overlap_count})",
            "reason": (
                f"only {overlap_count} shared tokens "
                f"(min {self.min_overlap_for_token_fallback} required): "
                f"query_tokens={sorted(q_tokens)}, matched_tokens={sorted(m_tokens)}"
            ),
        }

    def list_perturbations(self, query: str = "", top_n: int = 10) -> List[str]:
        return super().list_perturbations(query, top_n=top_n)

    def list_cell_lines(self, perturbation: Optional[str] = None) -> List[str]:
        return super().list_cell_lines(perturbation)