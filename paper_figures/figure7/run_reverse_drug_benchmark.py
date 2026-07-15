from __future__ import annotations

import random
from pathlib import Path

import pandas as pd


SEED = 20260702
TASK_TYPE = "reverse_drug"
MODALITY = "cp"
TARGET_N = 100


def select_candidate_rows(metrics_path: Path, n: int = TARGET_N) -> pd.DataFrame:
    """Select reverse-drug benchmark questions from the rule-candidate metrics."""
    metrics = pd.read_csv(metrics_path)
    candidates = metrics[
        (metrics["task_type"] == TASK_TYPE)
        & (metrics["universe_size"] >= 1000)
        & (metrics["function_variance_rank_in_cell"] <= 30)
        & (metrics["top10_count_gt5"] >= 5)
        & (metrics["positive_fraction"].between(0.10, 0.90))
    ].copy()
    records = candidates.to_dict("records")
    random.Random(SEED + 300).shuffle(records)

    selected, used_pairs, used_cells = [], set(), set()
    for row in records:
        pair = (str(row["cell"]), str(row["function"]))
        if len(selected) < n and pair not in used_pairs and str(row["cell"]) not in used_cells:
            selected.append(row)
            used_pairs.add(pair)
            used_cells.add(str(row["cell"]))
    for row in records:
        if len(selected) >= n:
            break
        pair = (str(row["cell"]), str(row["function"]))
        if pair not in used_pairs:
            selected.append(row)
            used_pairs.add(pair)
    return pd.DataFrame(selected)


def question(cell: str, function: str, direction: str) -> str:
    return f"Which small molecules may {direction} {function} in {cell} cells?"


def build_query_medians(checks: pd.DataFrame) -> pd.DataFrame:
    checks = checks[checks["not_found"].astype(str).str.lower() != "true"].copy()
    checks["rank_percentile"] = pd.to_numeric(checks["rank_percentile"], errors="coerce")
    return (
        checks.dropna(subset=["rank_percentile"])
        .groupby(["query_id", "task_type", "field", "system"], dropna=False)
        .agg(
            median_rank_percentile=("rank_percentile", "median"),
            mean_rank_percentile=("rank_percentile", "mean"),
            n_found=("rank_percentile", "size"),
        )
        .reset_index()
    )
