"""Package-core facade assembled by T-040."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from pxfquery.query.no_hit_guard import NoHitGuardForwardQuery
from pxfquery.resources import (
    DEFAULT_STANDARD_RESOURCE_BUNDLE,
    load_bundle,
    load_standard_matrix,
    resolve_bundle_root,
)

PACKAGE_CORE_VERSION = "pxfquery-T-040"


def create_forward_engine(
    matrix_name: str = "xpr_func_ad.h5ad",
    bundle_root: str | Path | None = None,
) -> tuple[NoHitGuardForwardQuery, dict[str, Any]]:
    """Load a standard matrix and return the guarded forward-query engine."""
    adata, matrix_meta = load_standard_matrix(matrix_name, bundle_root=bundle_root)
    return NoHitGuardForwardQuery(adata), matrix_meta


def forward_result_to_frame(result, query: str, requested_cell_line: str) -> pd.DataFrame:
    """Convert a ForwardResult into a serializable activated/suppressed table."""
    rows = []
    for direction, series in (
        ("activated", result.top_activated),
        ("suppressed", result.top_suppressed),
    ):
        for rank, (term, score) in enumerate(series.items(), start=1):
            rows.append(
                {
                    "query": query,
                    "requested_cell_line": requested_cell_line,
                    "matched_perturbation": result.perturbation,
                    "matched_cell_line": result.cell_line,
                    "direction": direction,
                    "rank": rank,
                    "term": term,
                    "score": float(score),
                    "n_obs": int(result.n_obs),
                    "cells_used": "|".join(result.cells_used),
                }
            )
    return pd.DataFrame(rows)


def run_forward_demo(
    perturbation: str = "EGFR",
    cell_line: str = "A549",
    top_n: int = 20,
    bundle_root: str | Path | None = None,
) -> dict[str, Any]:
    """Run a deterministic guarded forward-query demo and return summary data."""
    engine, matrix_meta = create_forward_engine(bundle_root=bundle_root)
    result = engine.query(perturbation, cell_line=cell_line, top_n=top_n)
    return {
        "query": perturbation,
        "requested_cell_line": cell_line,
        "found": bool(result.found),
        "matched_perturbation": result.perturbation,
        "matched_cell_line": result.cell_line,
        "n_obs": int(result.n_obs),
        "activated_terms": int(len(result.top_activated)),
        "suppressed_terms": int(len(result.top_suppressed)),
        "note": result.note,
        "matrix": matrix_meta,
    }


__all__ = [
    "DEFAULT_STANDARD_RESOURCE_BUNDLE",
    "NoHitGuardForwardQuery",
    "PACKAGE_CORE_VERSION",
    "create_forward_engine",
    "forward_result_to_frame",
    "load_bundle",
    "load_standard_matrix",
    "resolve_bundle_root",
    "run_forward_demo",
]
