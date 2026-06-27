"""
cellline_index.py — Cell line validation and tree-guided proxy lookup.

Expected files in output/store/query_index/:
  - cellline_index.json     {"valid_cells": [...]}
  - cellline_neighbors.json {lineage: {disease: {subtype: [cells]}}}
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Callable, Optional


class CellLineIndex:
    """
    Cell line index wrapper for exact validation and LLM-guided tree traversal.
    """

    def __init__(self, index_path: str | Path, neighbors_path: str | Path):
        with open(index_path, encoding="utf-8") as f:
            data = json.load(f)
        with open(neighbors_path, encoding="utf-8") as f:
            self._tree: dict = json.load(f)

        valid_cells = data.get("valid_cells", [])
        self._valid_cells: list[str] = list(valid_cells)
        self._valid_upper_to_canonical: dict[str, str] = {
            c.upper(): c for c in self._valid_cells
        }
        self._cell_path: dict[str, tuple[str, str, str]] = {}
        self._build_reverse_path_map()

    def is_valid(self, name: str) -> bool:
        """Return True if a cell line name exists in matrix-backed valid_cells."""
        return name.strip().upper() in self._valid_upper_to_canonical

    def canonical(self, name: str) -> Optional[str]:
        """Return canonical cell line name with original casing, or None."""
        return self._valid_upper_to_canonical.get(name.strip().upper())

    def valid_cells(self) -> list[str]:
        """Return all matrix-backed valid cell lines."""
        return list(self._valid_cells)

    def traverse(
        self,
        bio_context: str,
        llm_choose_fn: Callable[[str, list[str], str], str],
        max_steps: int = 4,
    ) -> list[str]:
        """
        Traverse lineage -> disease -> subtype tree and return leaf cell candidates.

        Parameters
        ----------
        bio_context : str
            User biological context description, such as "non-small cell lung cancer".
        llm_choose_fn : callable
            Function signature: (bio_context, options, level_name) -> selected_option
        max_steps : int
            Safety bound to avoid unexpected loops.
        """
        node = self._tree
        level = "lineage"
        steps = 0

        while isinstance(node, dict) and steps < max_steps:
            keys = list(node.keys())
            if not keys:
                return []
            if len(keys) == 1:
                selected = keys[0]
            else:
                selected = llm_choose_fn(bio_context, keys, level)
                if selected not in node:
                    selected = self._coerce_selected_option(selected, keys)
            node = node[selected]
            steps += 1
            if level == "lineage":
                level = "disease"
            elif level == "disease":
                level = "subtype"
            else:
                break

        if isinstance(node, list):
            return [c for c in node if self.is_valid(c)]
        return []

    def get_cell_path(self, cell: str) -> Optional[tuple[str, str, str]]:
        """Return (lineage, disease, subtype) for a known cell."""
        return self._cell_path.get(cell.strip().upper())

    def proxy_cells_for(self, cell: str) -> dict[str, list[str]]:
        """
        Return proxy cells grouped by hierarchy around the given cell.

        Keys:
          - same_subtype
          - same_disease
          - same_lineage
        """
        canonical = self.canonical(cell)
        if not canonical:
            return {"same_subtype": [], "same_disease": [], "same_lineage": []}
        path = self.get_cell_path(canonical)
        if not path:
            return {"same_subtype": [], "same_disease": [], "same_lineage": []}
        lineage, disease, subtype = path
        out = {"same_subtype": [], "same_disease": [], "same_lineage": []}
        lineage_node = self._tree.get(lineage, {})
        disease_node = lineage_node.get(disease, {})
        subtype_cells = disease_node.get(subtype, [])
        out["same_subtype"] = [c for c in subtype_cells if c != canonical and self.is_valid(c)]
        disease_cells = []
        for _, cells in disease_node.items():
            disease_cells.extend(cells)
        out["same_disease"] = [
            c for c in disease_cells if c != canonical and c not in out["same_subtype"] and self.is_valid(c)
        ]
        lineage_cells = []
        for _, subd in lineage_node.items():
            for _, cells in subd.items():
                lineage_cells.extend(cells)
        out["same_lineage"] = [
            c
            for c in lineage_cells
            if c != canonical and c not in out["same_subtype"] and c not in out["same_disease"] and self.is_valid(c)
        ]
        return out

    @staticmethod
    def _coerce_selected_option(selected: str, options: list[str]) -> str:
        selected_norm = selected.strip().lower()
        for opt in options:
            if opt.lower() == selected_norm:
                return opt
        for opt in options:
            if selected_norm in opt.lower() or opt.lower() in selected_norm:
                return opt
        return options[0]

    def _build_reverse_path_map(self) -> None:
        for lineage, disease_node in self._tree.items():
            if not isinstance(disease_node, dict):
                continue
            for disease, subtype_node in disease_node.items():
                if not isinstance(subtype_node, dict):
                    continue
                for subtype, cells in subtype_node.items():
                    if not isinstance(cells, list):
                        continue
                    for c in cells:
                        self._cell_path[str(c).upper()] = (lineage, disease, subtype)
