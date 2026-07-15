from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import wilcoxon


PXF_COLOR = "#d62728"
LLM_COLOR = "#1f77b4"
SYSTEMS = ["PxFquery", "Direct LLM"]

FORWARD_PANELS = [
    ("activated_top3", "Activated top3"),
    ("suppressed_top3", "Suppressed top3"),
    ("activated_top5", "Activated top5"),
    ("suppressed_top5", "Suppressed top5"),
]
REVERSE_PANELS = [
    ("recommendations_top1", "Top1"),
    ("recommendations_top3", "Top3"),
    ("recommendations_top5", "Top5"),
    ("recommendations_top10", "Top10"),
]


@dataclass(frozen=True)
class DatasetSpec:
    figure_id: str
    task_type: str
    source_name: str
    output_stem: str
    panels: list[tuple[str, str]]


DATASETS = [
    DatasetSpec(
        figure_id="fig4_panel_b",
        task_type="forward_genetic",
        source_name="forward_genetic_xpr100_first100",
        output_stem="fig4_panel_b_forward_genetic_xpr",
        panels=FORWARD_PANELS,
    ),
    DatasetSpec(
        figure_id="fig5_panel_b",
        task_type="forward_drug",
        source_name="forward_drug_100_first100",
        output_stem="fig5_panel_b_forward_drug",
        panels=FORWARD_PANELS,
    ),
    DatasetSpec(
        figure_id="fig6_panel_b",
        task_type="reverse_genetic",
        source_name="reverse_genetic_100",
        output_stem="fig6_panel_b_reverse_genetic",
        panels=REVERSE_PANELS,
    ),
    DatasetSpec(
        figure_id="fig7_panel_b",
        task_type="reverse_drug",
        source_name="reverse_drug_100",
        output_stem="fig7_panel_b_reverse_drug",
        panels=REVERSE_PANELS,
    ),
]


def configure_matplotlib() -> None:
    mpl.rcParams.update(
        {
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "font.family": "Arial",
            "axes.unicode_minus": False,
        }
    )


def query_order(query_id: str) -> int:
    match = re.search(r"_(\d+)$", str(query_id))
    return int(match.group(1)) if match else 10**9


def pvalue_stars(pvalue: float | None) -> str:
    if pvalue is None or not np.isfinite(pvalue):
        return "n.s."
    if pvalue < 1e-4:
        return "****"
    if pvalue < 1e-3:
        return "***"
    if pvalue < 1e-2:
        return "**"
    if pvalue < 0.05:
        return "*"
    return "n.s."


def paired_pvalue(data: pd.DataFrame) -> tuple[float | None, int]:
    pivot = data.pivot_table(
        index="query_id",
        columns="system",
        values="median_rank_percentile",
        aggfunc="first",
    ).dropna(subset=SYSTEMS)
    if len(pivot) < 2:
        return None, len(pivot)
    diff = pivot["PxFquery"].astype(float) - pivot["Direct LLM"].astype(float)
    if np.allclose(diff.to_numpy(), 0):
        return 1.0, len(pivot)
    return float(wilcoxon(pivot["PxFquery"], pivot["Direct LLM"]).pvalue), len(pivot)


def first100_canonical_ids(answers_path: Path) -> list[str]:
    ids: list[str] = []
    with answers_path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            gate = record.get("evidence_resolution_gate") or {}
            rows = ((record.get("answer_tables") or {}).get("ranked_results") or [])
            if gate.get("answer_unresolved") is False and rows:
                ids.append(str(record.get("query_id")))
    return sorted(ids, key=query_order)[:100]


def build_forward_query_median(checks_path: Path, query_ids: Iterable[str]) -> pd.DataFrame:
    selected_ids = {str(query_id) for query_id in query_ids}
    checks = pd.read_csv(checks_path)
    checks = checks[checks["query_id"].astype(str).isin(selected_ids)].copy()
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


def write_csv(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def prepare_release_data(task_root: Path, release_root: Path) -> None:
    table_root = task_root / "4_artifact/5_table"
    data_dir = release_root / "data"

    forward_sources = [
        (
            "forward_genetic_xpr100_first100",
            "fg_xpr100_resolved_official_t144_20260703",
        ),
        (
            "forward_drug_100_first100",
            "fd100_resolved_official_t144_20260703",
        ),
    ]
    for output_name, source_dir_name in forward_sources:
        source_dir = table_root / source_dir_name
        query_ids = first100_canonical_ids(source_dir / "filtered_batch_pxfquery_answers.jsonl")
        query_median = build_forward_query_median(source_dir / "filtered_batch_checks.csv", query_ids)
        write_csv(pd.DataFrame({"query_id": query_ids}), data_dir / "query_ids" / f"{output_name}_query_ids.csv")
        write_csv(query_median, data_dir / "query_medians" / f"{output_name}_query_median.csv")

    reverse = pd.read_csv(table_root / "rg_rd_batch100_current/rg_rd_batch100_current_query_median.csv")
    for task_type, output_name in [
        ("reverse_genetic", "reverse_genetic_100"),
        ("reverse_drug", "reverse_drug_100"),
    ]:
        query_median = reverse[reverse["task_type"] == task_type].copy()
        query_ids = sorted(query_median["query_id"].astype(str).unique(), key=query_order)
        write_csv(pd.DataFrame({"query_id": query_ids}), data_dir / "query_ids" / f"{output_name}_query_ids.csv")
        write_csv(query_median, data_dir / "query_medians" / f"{output_name}_query_median.csv")

    source_manifest = pd.DataFrame(
        [
            {
                "dataset": "forward_genetic_xpr100_first100",
                "source": str(table_root / "fg_xpr100_resolved_official_t144_20260703"),
                "selection": "first 100 canonical evaluable xpr forward genetic queries with nonempty ranked evidence table",
            },
            {
                "dataset": "forward_drug_100_first100",
                "source": str(table_root / "fd100_resolved_official_t144_20260703"),
                "selection": "first 100 canonical evaluable forward drug queries with nonempty ranked evidence table",
            },
            {
                "dataset": "reverse_genetic_100",
                "source": str(table_root / "rg_rd_batch100_current/rg_rd_batch100_current_query_median.csv"),
                "selection": "existing reverse genetic benchmark query-median table",
            },
            {
                "dataset": "reverse_drug_100",
                "source": str(table_root / "rg_rd_batch100_current/rg_rd_batch100_current_query_median.csv"),
                "selection": "existing reverse drug benchmark query-median table",
            },
        ]
    )
    write_csv(source_manifest, data_dir / "audit" / "source_manifest.csv")


def draw_panel(ax: plt.Axes, data: pd.DataFrame, title: str) -> dict[str, object]:
    values_by_system = [
        data[data["system"] == system]["median_rank_percentile"].dropna().astype(float).to_numpy()
        for system in SYSTEMS
    ]
    violin = ax.violinplot(
        values_by_system,
        positions=[0, 1],
        widths=0.72,
        showmeans=False,
        showmedians=False,
        showextrema=False,
    )
    for body, color in zip(violin["bodies"], [PXF_COLOR, LLM_COLOR]):
        body.set_facecolor(color)
        body.set_edgecolor(color)
        body.set_alpha(0.16)
        body.set_linewidth(0.9)

    for x, vals in enumerate(values_by_system):
        if len(vals):
            q1, median, q3 = np.percentile(vals, [25, 50, 75])
            ax.vlines(x, q1, q3, color="#555555", linewidth=2.2, alpha=0.58, zorder=3)
            ax.hlines(q1, x - 0.13, x + 0.13, color="#555555", linewidth=1.1, alpha=0.58, zorder=3)
            ax.hlines(q3, x - 0.13, x + 0.13, color="#555555", linewidth=1.1, alpha=0.58, zorder=3)
            ax.hlines(median, x - 0.18, x + 0.18, color="black", linewidth=1.25, zorder=4)

    rng = np.random.default_rng(20260702)
    for x, color, vals in zip([0, 1], [PXF_COLOR, LLM_COLOR], values_by_system):
        jitter = rng.uniform(-0.13, 0.13, len(vals))
        ax.scatter(
            np.full(len(vals), x) + jitter,
            vals,
            s=16,
            c=color,
            edgecolor="white",
            linewidth=0.22,
            alpha=0.36,
            zorder=5,
        )

    pvalue, paired_n = paired_pvalue(data)
    significance = pvalue_stars(pvalue)
    ax.text(0.5, 0.985, significance, transform=ax.transAxes, ha="center", va="top", fontsize=10)
    ax.set_title(title, fontsize=9)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(SYSTEMS, fontsize=8)
    ax.set_ylim(105, -5)
    ax.grid(axis="y", alpha=0.22)
    return {
        "paired_n": paired_n,
        "paired_wilcoxon_p": pvalue,
        "significance": significance,
        "pxf_median": float(np.nanmedian(values_by_system[0])) if len(values_by_system[0]) else np.nan,
        "llm_median": float(np.nanmedian(values_by_system[1])) if len(values_by_system[1]) else np.nan,
    }


def plot_dataset(release_root: Path, spec: DatasetSpec) -> pd.DataFrame:
    query_median_path = release_root / "data/query_medians" / f"{spec.source_name}_query_median.csv"
    data = pd.read_csv(query_median_path)
    data = data[data["task_type"] == spec.task_type].copy()
    data["median_rank_percentile"] = pd.to_numeric(data["median_rank_percentile"], errors="coerce")

    fig, axes = plt.subplots(2, 2, figsize=(6.6, 5.8), sharey=True)
    summary_rows = []
    for ax, (field, title) in zip(axes.ravel(), spec.panels):
        panel_data = data[data["field"] == field].copy()
        row = draw_panel(ax, panel_data, title)
        row.update(
            {
                "figure_id": spec.figure_id,
                "task_type": spec.task_type,
                "field": field,
                "field_title": title,
            }
        )
        summary_rows.append(row)
    for ax in axes.ravel()[::2]:
        ax.set_ylabel("Experimental rank percentile (%)")
    fig.tight_layout()

    pdf_path = release_root / "figures/pdf" / f"{spec.output_stem}.pdf"
    png_path = release_root / "figures/png" / f"{spec.output_stem}.png"
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, dpi=220, bbox_inches="tight")
    plt.close(fig)
    return pd.DataFrame(summary_rows)


def plot_release_figures(release_root: Path) -> pd.DataFrame:
    configure_matplotlib()
    summaries = [plot_dataset(release_root, spec) for spec in DATASETS]
    summary = pd.concat(summaries, ignore_index=True)
    write_csv(summary, release_root / "data/audit/panel_b_summary.csv")

    figure_manifest = pd.DataFrame(
        [
            {
                "figure_id": spec.figure_id,
                "task_type": spec.task_type,
                "source_name": spec.source_name,
                "pdf": str(Path("figures/pdf") / f"{spec.output_stem}.pdf"),
                "png": str(Path("figures/png") / f"{spec.output_stem}.png"),
            }
            for spec in DATASETS
        ]
    )
    write_csv(figure_manifest, release_root / "data/audit/figure_manifest.csv")
    return summary


def parse_args() -> argparse.Namespace:
    default_release_root = Path(__file__).resolve().parents[1]
    default_task_root = default_release_root.parents[2]
    parser = argparse.ArgumentParser(description="Prepare and plot PxFquery panel B benchmark figures.")
    parser.add_argument("--task-root", type=Path, default=default_task_root)
    parser.add_argument("--release-root", type=Path, default=default_release_root)
    parser.add_argument("--mode", choices=["all", "prepare", "plot"], default="all")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.mode in {"all", "prepare"}:
        prepare_release_data(args.task_root, args.release_root)
    if args.mode in {"all", "plot"}:
        summary = plot_release_figures(args.release_root)
        print(summary.to_string(index=False))


if __name__ == "__main__":
    main()

