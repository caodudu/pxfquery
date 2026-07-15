from __future__ import annotations

import json
import random
import re
from pathlib import Path
from typing import Iterable

import pandas as pd


SEED = 20260702
TARGET_RESOLVED = 100
MAX_ATTEMPTED = 216


def query_order(query_id: str) -> int:
    match = re.search(r"_(\d+)$", str(query_id))
    return int(match.group(1)) if match else 10**9


def select_candidate_rows(metrics_path: Path) -> pd.DataFrame:
    """Select the forward-genetic XPR candidate stream used for this benchmark."""
    metrics = pd.read_csv(metrics_path)
    candidates = metrics[
        (metrics["task_type"] == "forward_genetic_xpr")
        & (metrics["n_exact_rows"] >= 3)
        & (metrics["activated_count_gt1"] >= 10)
        & (metrics["suppressed_count_lt_minus1"] >= 10)
        & (metrics["near_zero_count_abs_lt_0_2"] >= 20)
        & (metrics["same_perturbation_other_cell_count"] >= 10)
    ].copy()
    records = candidates.to_dict("records")
    random.Random(SEED + 2020).shuffle(records)

    selected, used_pairs = [], set()
    for row in records:
        pair = (str(row["cell"]), str(row["perturbation"]), "xpr")
        if pair in used_pairs:
            continue
        selected.append(row)
        used_pairs.add(pair)
        if len(selected) >= MAX_ATTEMPTED:
            break
    return pd.DataFrame(selected)


def question(cell: str, perturbation: str) -> str:
    return f"In {cell} cells, what functional programs are changed after {perturbation} CRISPR perturbation?"


def first100_canonical_ids(answer_log: Path) -> list[str]:
    """Apply the released evidence-resolution and nonempty-ranked-table rule."""
    ids = []
    with answer_log.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            gate = record.get("evidence_resolution_gate") or {}
            ranked = ((record.get("answer_tables") or {}).get("ranked_results") or [])
            if gate.get("answer_unresolved") is False and ranked:
                ids.append(str(record["query_id"]))
    return sorted(ids, key=query_order)[:TARGET_RESOLVED]


def build_query_medians(checks_path: Path, query_ids: Iterable[str]) -> pd.DataFrame:
    selected = {str(query_id) for query_id in query_ids}
    checks = pd.read_csv(checks_path)
    checks = checks[checks["query_id"].astype(str).isin(selected)].copy()
    checks = checks[checks["not_found"].astype(str).str.lower() != "true"].copy()
    checks["rank_percentile"] = pd.to_numeric(checks["rank_percentile"], errors="coerce")
    return (
        checks.dropna(subset=["rank_percentile"])
        .groupby(["query_id", "task_type", "field", "system"], dropna=False)
        .agg(
            median_rank_percentile=("rank_percentile", "median"),
            mean_rank_percentile=("rank_percentile", "mean"),
            n_found=("rank_percentile", "size"),
            same_direction_count=("same_direction", lambda values: int(values.astype(str).str.lower().eq("true").sum())),
        )
        .reset_index()
    )

