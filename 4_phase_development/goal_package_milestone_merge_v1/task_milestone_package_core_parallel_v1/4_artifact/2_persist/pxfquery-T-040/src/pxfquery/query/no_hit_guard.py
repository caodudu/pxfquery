"""T-040 no-hit guard for deterministic forward queries.

This is the package-core integration of the T-031 guard. It subclasses the
T-024 ``ForwardQuery`` implementation and returns ``ForwardResult.found=False``
when fuzzy perturbation matching falls below conservative quality thresholds.
"""

from __future__ import annotations

import re
from typing import List, Optional

from pxfquery.query.forward import ForwardQuery, ForwardResult


class NoHitGuardForwardQuery(ForwardQuery):
    """ForwardQuery wrapper with explicit no-hit behavior."""

    def __init__(
        self,
        adata,
        min_overlap_for_token_fallback: int = 2,
        min_query_length_for_substring: int = 4,
    ):
        super().__init__(adata)
        self.min_overlap_for_token_fallback = min_overlap_for_token_fallback
        self.min_query_length_for_substring = min_query_length_for_substring
        self.guard_version = "pxfquery-T-040"

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
        if quality["accepted"]:
            return result

        return ForwardResult.empty(
            perturbation,
            note=(
                f"NOT_FOUND by pxfquery-T-040 no-hit guard: query '{perturbation}' "
                f"matched '{result.perturbation}' via {quality['mechanism']} but failed "
                f"quality check ({quality['reason']})."
            ),
        )

    def _assess_match_quality(self, query: str, matched: str) -> dict[str, object]:
        q = query.strip()
        m = matched.strip()

        if q.lower() == m.lower():
            return {"accepted": True, "mechanism": "exact", "reason": ""}

        if q.lower() in m.lower():
            if len(q) >= self.min_query_length_for_substring:
                return {"accepted": True, "mechanism": "substring", "reason": ""}
            return {
                "accepted": False,
                "mechanism": "substring",
                "reason": (
                    f"query length {len(q)} is below "
                    f"min_query_length_for_substring={self.min_query_length_for_substring}"
                ),
            }

        q_tokens = set(re.split(r"[\s_\-]+", q.lower()))
        m_tokens = set(re.split(r"[\s_\-]+", m.lower()))
        overlap_count = len(q_tokens & m_tokens)
        if overlap_count >= self.min_overlap_for_token_fallback:
            return {"accepted": True, "mechanism": f"token_overlap({overlap_count})", "reason": ""}

        return {
            "accepted": False,
            "mechanism": f"token_overlap({overlap_count})",
            "reason": (
                f"only {overlap_count} shared tokens; "
                f"min_overlap_for_token_fallback={self.min_overlap_for_token_fallback}"
            ),
        }

    def list_perturbations(self, query: str = "", top_n: int = 10) -> List[str]:
        return super().list_perturbations(query, top_n=top_n)

    def list_cell_lines(self, perturbation: Optional[str] = None) -> List[str]:
        return super().list_cell_lines(perturbation)
