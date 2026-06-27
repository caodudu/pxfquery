"""
gene_index.py — Gene symbol lookup and semantic neighbor index for PxFquery.

Pre-built index files (output/store/query_index/):
  gene_index_simple.json     : {SYMBOL_UPPER: type_code}  356 KB
  gene_neighbors_simple.json : {symbol: [[neighbor, cosine_int], ...]}  19.5 MB

Type codes
----------
  "pc"   protein_coding
  "mir"  miRNA
  "snr"  snRNA
  "misc" misc_RNA

Storage format of gene_neighbors_simple.json
---------------------------------------------
Values are lists of [neighbor_symbol, cosine_int].
cosine_int = round(cosine × 100). Restore with cosine_int / 100.
Lists are sorted cosine descending. Break early on min_cosine filter.

Lookup flow (resolver should call in order)
--------------------------------------------
1. lookup(name)              — case-insensitive exact match
2. lookup_candidates(names)  — try a list (LLM-normalized candidates)
3. in_matrix(symbol)         — does this gene have experimental data?
4. neighbors(symbol)         — semantic neighbors for proxy queries

TODO: llm_map_gene secondary resolution
  When lookup() returns None, call llm_map_gene(name) → list[str],
  then call lookup_candidates() on the result.
  Handles deprecated gene names, spelling variants, and descriptive queries.
  See PxFquery_code.md § "基因名解析流程" for full spec.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

GENE_TYPE_NAMES: dict[str, str] = {
    "pc":   "protein_coding",
    "mir":  "miRNA",
    "snr":  "snRNA",
    "misc": "misc_RNA",
}

DEFAULT_MIN_COSINE = 0.5


class GeneIndex:
    """
    Gene symbol lookup and semantic neighbor index.

    Parameters
    ----------
    index_path : str or Path
        Path to gene_index_simple.json (UPPERCASE key → type_code).
    neighbors_path : str or Path
        Path to gene_neighbors_simple.json (symbol → [[neighbor, cosine_int], ...]).

    Examples
    --------
    >>> idx = GeneIndex("output/store/query_index/gene_index_simple.json",
    ...                 "output/store/query_index/gene_neighbors_simple.json")
    >>> idx.lookup("kras")
    ('KRAS', 'pc')
    >>> idx.in_matrix("KRAS")
    True
    >>> idx.neighbors("KRAS", min_cosine=0.5)
    [('NRAS', 1.0), ('HRAS', 0.76), ('SOS1', 0.74), ...]
    """

    def __init__(self, index_path: str | Path, neighbors_path: str | Path):
        with open(index_path, encoding="utf-8") as f:
            self._index: dict[str, str] = json.load(f)  # UPPER_SYMBOL → type_code

        with open(neighbors_path, encoding="utf-8") as f:
            self._neighbors_raw: dict[str, list] = json.load(f)  # symbol → [[nbr, cosine_int]]

        # Matrix gene pool = all symbols that appear as neighbors.
        # These are the 7396 genes with experimental data AND embeddings.
        self._matrix_genes: frozenset[str] = frozenset(
            nbr for v in self._neighbors_raw.values() for nbr, _ in v
        )

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def lookup(self, name: str) -> Optional[tuple[str, str]]:
        """
        Look up a gene by symbol (case-insensitive).

        Parameters
        ----------
        name : str
            Gene symbol in any case (e.g. 'kras', 'KRAS', 'Kras').

        Returns
        -------
        (canonical_symbol, type_code) or None
            canonical_symbol: the UPPERCASE gene symbol used as index key.
            type_code: 'pc' | 'mir' | 'snr' | 'misc', or None if not in index.
            Returns None if the gene is not found.
        """
        key = name.strip().upper()
        t = self._index.get(key)
        if t is None:
            return None
        return key, t

    def lookup_candidates(self, names: list[str]) -> Optional[tuple[str, str]]:
        """
        Try a list of candidate names in order, return the first match.

        Intended for use with LLM-normalized name candidates.

        Parameters
        ----------
        names : list[str]
            Candidate symbols to try (e.g. from llm_map_gene).

        Returns
        -------
        (canonical_symbol, type_code) or None
        """
        for name in names:
            result = self.lookup(name)
            if result is not None:
                return result
        return None

    def in_matrix(self, symbol: str) -> bool:
        """
        Return True if the gene has experimental perturbation data in xpr/sh matrices.

        Determined by whether the symbol appears in the precomputed neighbor
        candidate pool (7396 genes with both experimental data and GenePT embeddings).

        Note: 569 additional shRNA reagent IDs (TRCN*) are also in the matrix
        but are not tracked here (reagent IDs, not gene symbols).
        """
        return symbol.upper() in self._matrix_genes

    def neighbors(
        self,
        symbol: str,
        min_cosine: float = DEFAULT_MIN_COSINE,
        top_n: int = 50,
    ) -> list[tuple[str, float]]:
        """
        Return semantic neighbors of a gene, sorted by cosine similarity (descending).

        Neighbors are drawn from the 7396-gene matrix candidate pool,
        computed via GenePT model-3 (3072d, gene text + protein sequence).

        Parameters
        ----------
        symbol : str
            Gene symbol (case-insensitive).
        min_cosine : float
            Minimum cosine similarity threshold (default 0.5).
            Values below this indicate weak functional similarity.
        top_n : int
            Maximum number of neighbors to return.

        Returns
        -------
        list of (symbol, cosine) tuples
            Empty list if gene has no neighbors or is not in the index.
        """
        raw = self._neighbors_raw.get(symbol.upper(), [])
        results = []
        for nbr, c_int in raw:
            c = c_int / 100.0
            if c < min_cosine:
                break  # sorted descending, safe to stop
            results.append((nbr, c))
            if len(results) >= top_n:
                break
        return results

    def gene_type(self, symbol: str) -> Optional[str]:
        """
        Return full gene type name for a symbol, or None if not in index.

        Returns
        -------
        str or None
            e.g. 'protein_coding', 'miRNA', 'snRNA', 'misc_RNA'
        """
        result = self.lookup(symbol)
        if result is None:
            return None
        _, code = result
        return GENE_TYPE_NAMES.get(code, code)

    def has_neighbors(self, symbol: str) -> bool:
        """Return True if the gene has precomputed semantic neighbors."""
        return symbol.upper() in self._neighbors_raw

    def __len__(self) -> int:
        """Number of gene symbols in the index."""
        return len(self._index)

    def __contains__(self, symbol: str) -> bool:
        return self._index.get(symbol.upper()) is not None
