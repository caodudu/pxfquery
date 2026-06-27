"""
function_index.py — Functional gene set index for PxFquery.

Pre-built index file (output/store/query_index/):
  function_index.json  (< 50 KB)

    {
      "var_names":  [...],          # 91 exact var names matching h5ad .var_names
      "meta": {
        "<var_name>": {
          "source":  "hallmark" | "3ca_mps",
          "label":   "<human-readable name>",
          "mp_id":   <int>          # 3ca_mps only
        }
      },
      "aliases": {
        "<lowercase_alias>": "<var_name>",
        ...
      }
    }

Lookup flow (resolver should call in order)
--------------------------------------------
1. lookup(name)         — case-insensitive exact match against aliases and var_names
2. validate(var_name)   — check whether a var_name is in the index
3. for_llm()            — formatted list of all 91 functions for LLM selection prompt

When lookup() returns None, pass for_llm() output to llm_map_function() in llm/prompts.py.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Optional


class FunctionIndex:
    """
    Functional gene set lookup index.

    Covers the 91 var columns used in xpr/sh/cp h5ad matrices:
    50 MSigDB Hallmark gene sets and 41 3CA MPS (v1) programs.

    Parameters
    ----------
    index_path : str or Path
        Path to function_index.json.

    Examples
    --------
    >>> idx = FunctionIndex("output/store/query_index/function_index.json")
    >>> idx.lookup("emt")
    'HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION'
    >>> idx.lookup("apoptosis")
    'HALLMARK_APOPTOSIS'
    >>> idx.validate("HALLMARK_APOPTOSIS")
    True
    >>> idx.label("HALLMARK_APOPTOSIS")
    'Apoptosis'
    >>> len(idx)
    91
    """

    def __init__(self, index_path: str | Path):
        with open(index_path, encoding="utf-8") as f:
            data = json.load(f)

        # Format A (new): {"var_names", "meta", "aliases"}
        # Format B (legacy): {"functions": {var_name: {...}}}
        if "var_names" in data and "meta" in data and "aliases" in data:
            self._var_names: list[str] = data["var_names"]
            self._meta: dict[str, dict] = data["meta"]
            self._aliases: dict[str, str] = data["aliases"]  # lowercase -> var_name
            self._aliases.update(self._build_aliases_from_meta(self._meta))
        else:
            functions = data.get("functions", {})
            self._var_names = list(functions.keys())
            self._meta = {
                vn: {
                    "source": meta.get("source", "unknown"),
                    "label": meta.get("label", vn),
                    "mp_id": meta.get("mp_id"),
                }
                for vn, meta in functions.items()
            }
            self._aliases = self._build_aliases_from_legacy(functions)
        self._var_set: frozenset[str] = frozenset(self._var_names)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def lookup(self, name: str) -> Optional[str]:
        """
        Look up a function by name or alias (case-insensitive).

        Checks aliases first (covers abbreviations like 'emt', 'oxphos'),
        then falls back to a direct var_name match (case-insensitive).

        Parameters
        ----------
        name : str
            Any alias, abbreviation, or exact var_name.

        Returns
        -------
        str or None
            Exact var_name (e.g. 'HALLMARK_APOPTOSIS'), or None if not found.
        """
        key = name.strip().lower()
        # alias table (covers normalized labels + curated abbreviations)
        result = self._aliases.get(key)
        if result is not None:
            return result
        # direct var_name match (user might pass exact var_name)
        for vn in self._var_names:
            if vn.strip().lower() == key:
                return vn
        return None

    def validate(self, var_name: str) -> bool:
        """
        Return True if var_name is a valid h5ad column name.

        Parameters
        ----------
        var_name : str
            Exact var_name string.
        """
        return var_name in self._var_set

    def label(self, var_name: str) -> Optional[str]:
        """
        Return the human-readable label for a var_name, or None if not found.

        Parameters
        ----------
        var_name : str
            Exact var_name.
        """
        m = self._meta.get(var_name)
        return m["label"] if m else None

    def source(self, var_name: str) -> Optional[str]:
        """
        Return the source of a function: 'hallmark' or '3ca_mps', or None.

        Parameters
        ----------
        var_name : str
            Exact var_name.
        """
        m = self._meta.get(var_name)
        return m["source"] if m else None

    def all_var_names(self, source: Optional[str] = None) -> list[str]:
        """
        Return all 91 var_names, optionally filtered by source.

        Parameters
        ----------
        source : str or None
            'hallmark', '3ca_mps', or None (all).
        """
        if source is None:
            return list(self._var_names)
        return [vn for vn in self._var_names if self._meta[vn]["source"] == source]

    def for_llm(self, source: Optional[str] = None) -> str:
        """
        Return a compact listing of all functions formatted for an LLM prompt.

        Each line: '<index>. [<source>] <label>  |  <var_name>'

        The LLM should use the exact var_name when specifying a function.

        Parameters
        ----------
        source : str or None
            Filter to 'hallmark' or '3ca_mps' only, or None for all 91.

        Returns
        -------
        str
            Newline-separated listing.
        """
        lines = []
        entries = [
            (vn, self._meta[vn])
            for vn in self._var_names
            if source is None or self._meta[vn]["source"] == source
        ]
        for i, (vn, m) in enumerate(entries, 1):
            src_tag = "H" if m["source"] == "hallmark" else "M"
            lines.append(f"{i:>3}. [{src_tag}] {m['label']:<40}  |  {vn}")
        return "\n".join(lines)

    def __len__(self) -> int:
        """Number of gene sets (var columns) in the index."""
        return len(self._var_names)

    def __contains__(self, var_name: str) -> bool:
        """Support 'HALLMARK_APOPTOSIS' in idx syntax."""
        return var_name in self._var_set

    @staticmethod
    def _build_aliases_from_legacy(functions: dict[str, dict]) -> dict[str, str]:
        aliases: dict[str, str] = {}
        for var_name, meta in functions.items():
            aliases[var_name.lower()] = var_name
            label = str(meta.get("label", "")).strip().lower()
            if label:
                aliases[label] = var_name

        curated = {
            "emt": "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION",
            "apoptosis": "HALLMARK_APOPTOSIS",
            "oxphos": "HALLMARK_OXIDATIVE_PHOSPHORYLATION",
            "p53": "HALLMARK_P53_PATHWAY",
            "myc": "HALLMARK_MYC_TARGETS_V1",
            "g2m": "HALLMARK_G2M_CHECKPOINT",
            "upr": "HALLMARK_UNFOLDED_PROTEIN_RESPONSE",
            "hypoxia": "HALLMARK_HYPOXIA",
            "cell cycle g2/m": "MP1  Cell Cycle - G2/M",
            "respiration": "MP2  Respiration",
        }
        for k, v in curated.items():
            if v in functions:
                aliases[k] = v
        return aliases

    @staticmethod
    def _build_aliases_from_meta(meta: dict[str, dict]) -> dict[str, str]:
        aliases: dict[str, str] = {}
        for var_name, item in meta.items():
            aliases[var_name.lower()] = var_name
            label = str(item.get("label", "")).strip().lower()
            if label:
                aliases[label] = var_name
                aliases[label.replace(" ", "_")] = var_name

        curated = {
            "emt": "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION",
            "epithelial mesenchymal transition": "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION",
            "oxphos": "HALLMARK_OXIDATIVE_PHOSPHORYLATION",
            "p53": "HALLMARK_P53_PATHWAY",
            "myc": "HALLMARK_MYC_TARGETS_V1",
            "glycolysis": "HALLMARK_GLYCOLYSIS",
            "apoptosis": "HALLMARK_APOPTOSIS",
            "cell cycle": "HALLMARK_E2F_TARGETS",
            "proliferation": "HALLMARK_E2F_TARGETS",
            "inflammation": "HALLMARK_INFLAMMATORY_RESPONSE",
            "interferon gamma": "HALLMARK_INTERFERON_GAMMA_RESPONSE",
            "interferon alpha": "HALLMARK_INTERFERON_ALPHA_RESPONSE",
        }
        for key, value in curated.items():
            if value in meta:
                aliases[key] = value
        return aliases
