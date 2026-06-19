"""
utils.py — Shared utility functions for PxFquery.
"""

from __future__ import annotations
from typing import List, Optional
import re


def fuzzy_match(query: str, candidates: List[str], top_n: int = 5) -> List[str]:
    """
    Simple fuzzy string matching: case-insensitive substring search,
    with fallback to token overlap scoring.

    Parameters
    ----------
    query : str
        Search string (e.g. "EGFR", "egfr knockout").
    candidates : list of str
        Pool of strings to search in.
    top_n : int
        Max number of matches to return.

    Returns
    -------
    list of str
        Matched strings, best first. Empty list if nothing matches.
    """
    q = query.strip().lower()
    q_tokens = set(re.split(r"[\s_\-]+", q))

    exact = [c for c in candidates if c.lower() == q]
    if exact:
        return exact[:top_n]

    substring = [c for c in candidates if q in c.lower()]
    if substring:
        return substring[:top_n]

    # token overlap fallback
    scored = []
    for c in candidates:
        c_tokens = set(re.split(r"[\s_\-]+", c.lower()))
        overlap = len(q_tokens & c_tokens)
        if overlap > 0:
            scored.append((overlap, c))
    scored.sort(key=lambda x: -x[0])
    return [c for _, c in scored[:top_n]]


def build_target_vector(
    term_names: List[str],
    activate: List[str],
    suppress: List[str],
) -> "np.ndarray":
    """
    Build a target score vector for reverse query.

    Activated terms → +1, suppressed terms → -1, others → 0.

    Parameters
    ----------
    term_names : list of str
        Ordered list of all functional term names (column names of the matrix).
    activate : list of str
        Functional terms to activate.
    suppress : list of str
        Functional terms to suppress.

    Returns
    -------
    np.ndarray of shape (len(term_names),)
    """
    import numpy as np
    vec = np.zeros(len(term_names), dtype=float)
    for t in activate:
        matches = fuzzy_match(t, term_names, top_n=1)
        if matches:
            idx = term_names.index(matches[0])
            vec[idx] = 1.0
    for t in suppress:
        matches = fuzzy_match(t, term_names, top_n=1)
        if matches:
            idx = term_names.index(matches[0])
            vec[idx] = -1.0
    return vec


def cosine_similarity_matrix(matrix: "np.ndarray", vec: "np.ndarray") -> "np.ndarray":
    """
    Compute cosine similarity between each row of matrix and vec.

    Parameters
    ----------
    matrix : np.ndarray, shape (n_obs, n_terms)
    vec : np.ndarray, shape (n_terms,)

    Returns
    -------
    np.ndarray, shape (n_obs,)
    """
    import numpy as np
    row_norms = np.linalg.norm(matrix, axis=1)
    vec_norm = np.linalg.norm(vec)
    denom = row_norms * vec_norm
    denom = np.where(denom == 0, 1e-10, denom)
    return (matrix @ vec) / denom
