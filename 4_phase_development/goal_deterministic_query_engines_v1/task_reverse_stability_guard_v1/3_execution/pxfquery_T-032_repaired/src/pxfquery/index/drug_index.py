"""
drug_index.py — Drug alias lookup and structural neighbor index for PxFquery.

Pre-built index files (output/store/query_index/):
  drug_index.json     : {alias_lowercase: BRD-id}  176 KB
  drug_neighbors.json : {id_no_prefix: [[neighbor_no_prefix, t_int], ...]}  4.4 MB

Storage format of drug_neighbors.json
--------------------------------------
Keys and neighbor ids have the "BRD-" prefix stripped to save space.
Tanimoto values are stored as integers × 100 (e.g. 54 means 0.54).
This class restores full BRD-ids and float tanimoto on access.

Lookup flow (resolver should call in order)
--------------------------------------------
1. lookup(name)          — exact alias match (covers all known aliases)
2. lookup_aliases(names) — try a list of candidate names (LLM-normalized)
3. neighbors(brd_id)     — structural neighbors for proxy queries

TODO: llm_normalize_drug fallback
  When lookup() returns None, call llm_normalize_drug(name) → list[str],
  then call lookup_aliases() on the result.
  If still None, try real-time PubChem InChIKey match against cp_meta_enriched.csv.
  See PxFquery_code.md § "药物名解析流程" for full spec.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional


# Tanimoto threshold below which neighbors are considered structurally unrelated
DEFAULT_MIN_TANIMOTO = 0.3


class DrugIndex:
    """
    Drug alias lookup and structural neighbor index.

    Parameters
    ----------
    index_path : str or Path
        Path to drug_index.json
    neighbors_path : str or Path
        Path to drug_neighbors.json

    Examples
    --------
    >>> idx = DrugIndex("output/store/query_index/drug_index.json",
    ...                 "output/store/query_index/drug_neighbors.json")
    >>> idx.lookup("erlotinib")
    'BRD-K70301465'
    >>> idx.neighbors("BRD-K70301465", min_tanimoto=0.4)
    [('BRD-K12345678', 0.87), ...]
    """

    def __init__(self, index_path: str | Path, neighbors_path: str | Path):
        with open(index_path, encoding="utf-8") as f:
            self._index: dict[str, str] = json.load(f)  # alias → full BRD-id

        with open(neighbors_path, encoding="utf-8") as f:
            self._neighbors_raw: dict[str, list] = json.load(f)  # id_no_prefix → [[id_no_prefix, t_int]]

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def lookup(self, name: str) -> Optional[str]:
        """
        Look up a drug by name or alias (case-insensitive).

        Parameters
        ----------
        name : str
            Any known alias, trade name, or INN name.

        Returns
        -------
        str or None
            Full BRD-id (e.g. 'BRD-K70301465'), or None if not found.
        """
        return self._index.get(name.lower().strip())

    def lookup_aliases(self, names: list[str]) -> Optional[str]:
        """
        Try a list of candidate names in order, return first match.

        Intended for use with LLM-normalized name candidates.

        Parameters
        ----------
        names : list[str]
            Candidate names to try (e.g. from llm_normalize_drug).

        Returns
        -------
        str or None
            First BRD-id found, or None if none match.
        """
        for name in names:
            result = self.lookup(name)
            if result is not None:
                return result
        return None

    def neighbors(
        self,
        brd_id: str,
        min_tanimoto: float = DEFAULT_MIN_TANIMOTO,
        top_n: int = 50,
    ) -> list[tuple[str, float]]:
        """
        Return structural neighbors of a drug, sorted by Tanimoto (descending).

        Parameters
        ----------
        brd_id : str
            Full BRD-id, e.g. 'BRD-K70301465'.
        min_tanimoto : float
            Minimum Tanimoto threshold (default 0.3). Values below this are
            structurally unrelated and should not be used as proxies.
        top_n : int
            Maximum number of neighbors to return.

        Returns
        -------
        list of (BRD-id, tanimoto) tuples
            Empty list if drug has no neighbors or is not in the index.
        """
        key = brd_id[4:] if brd_id.startswith("BRD-") else brd_id
        raw = self._neighbors_raw.get(key, [])
        results = []
        for neighbor_key, t_int in raw:
            t = t_int / 100.0
            if t < min_tanimoto:
                break  # list is sorted descending
            results.append(("BRD-" + neighbor_key, t))
            if len(results) >= top_n:
                break
        return results

    def has_neighbors(self, brd_id: str) -> bool:
        """Return True if the drug has any precomputed structural neighbors."""
        key = brd_id[4:] if brd_id.startswith("BRD-") else brd_id
        return key in self._neighbors_raw

    def __len__(self) -> int:
        """Number of alias entries in the index."""
        return len(self._index)
