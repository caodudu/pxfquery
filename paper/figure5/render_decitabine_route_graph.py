from __future__ import annotations

import math
import textwrap
from pathlib import Path

import pandas as pd


TASK_ROOT = Path(__file__).resolve().parents[1]
CASE_ID = "R15C01_DECITABINE_LEUKEMIA"
ROUND_ID = "round15_nucleoside_refine_queries_v0522"

TABLE_DIR = (
    TASK_ROOT
    / "4_artifact"
    / "5_table"
    / "figure5"
    / "panel_a_iter"
    / ROUND_ID
    / CASE_ID
)
OUT_DIR = (
    TASK_ROOT
    / "4_artifact"
    / "4_picture"
    / "figure5"
    / "panel_a_selected"
    / CASE_ID
)

PERT_NAME = {
    "BRD-K79254416": "decitabine",
    "BRD-K33106058": "cytarabine",
    "BRD-A18929998": "cytarabine",
    "BRD-K15108141": "gemcitabine",
}

DISPLAY_FUNCTIONS = [
    "MP17 Interferon/MHC-II (I)",
    "HALLMARK_TNFA_SIGNALING_VIA_NFKB",
    "MP5 Stress ",
    "MP20 MYC",
    "HALLMARK_MYC_TARGETS_V1",
    "MP11 Translation initiation",
]


def _display_function(label: str) -> str:
    text = str(label or "").strip()
    text = text.replace("HALLMARK_", "").replace("_", " ")
    return text


def _wrap(text: str, width: int) -> str:
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False))


def _layer_positions(items: list[str], y: float, x0: float, x1: float) -> dict[str, tuple[float, float]]:
    if len(items) == 1:
        return {items[0]: ((x0 + x1) / 2, y)}
    step = (x1 - x0) / (len(items) - 1)
    return {item: (x0 + i * step, y) for i, item in enumerate(items)}


def _draw_node(ax, xy, label, face, edge, *, size, fs, width, yoff):
    x, y = xy
    ax.scatter([x], [y], s=size, facecolor=face, edgecolor=edge, linewidth=1.6, zorder=4)
    ax.text(
        x,
        y - yoff,
        _wrap(label, width),
        ha="center",
        va="top",
        fontsize=fs,
        linespacing=1.04,
        zorder=5,
        color="#111827",
    )


def main() -> None:
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D

    plt.rcParams["pdf.fonttype"] = 42
    plt.rcParams["ps.fonttype"] = 42
    plt.rcParams["svg.fonttype"] = "none"
    plt.rcParams["font.family"] = "Arial"
    plt.rcParams["text.usetex"] = False

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    route = pd.read_csv(TABLE_DIR / "route_summary.csv")
    funcs = pd.read_csv(TABLE_DIR / "route_function_results.csv")

    executed = route[route["status"] == "executed"].copy()
    executed["drug"] = executed.apply(
        lambda row: PERT_NAME.get(str(row["perturbation"]), str(row["perturbation_alias"] or row["perturbation"])),
        axis=1,
    )
    executed = executed[["cell", "drug", "perturbation_match_type"]].drop_duplicates()

    funcs["drug"] = funcs.apply(
        lambda row: PERT_NAME.get(str(row["perturbation"]), str(row["perturbation_alias"] or row["perturbation"])),
        axis=1,
    )
    sub = funcs[funcs["label"].isin(DISPLAY_FUNCTIONS)].copy()

    cells = ["JURKAT", "THP1", "SKM1", "NOMO1"]
    drugs = ["decitabine", "cytarabine", "gemcitabine"]
    functions = DISPLAY_FUNCTIONS

    cell_pos = {f"cell:{k}": v for k, v in _layer_positions(cells, 0.78, 0.13, 0.94).items()}
    drug_pos = {f"drug:{k}": v for k, v in _layer_positions(drugs, 0.49, 0.13, 0.94).items()}
    fn_pos = {f"fn:{k}": v for k, v in _layer_positions(functions, 0.17, 0.08, 0.98).items()}
    pos = {**cell_pos, **drug_pos, **fn_pos}

    fig, ax = plt.subplots(figsize=(11.8, 7.1))
    ax.set_axis_off()
    ax.set_xlim(-0.08, 1.03)
    ax.set_ylim(0.00, 0.98)

    ax.text(-0.055, 0.78, "Cell\nContext", ha="left", va="center", fontsize=10, weight="bold", color="#374151")
    ax.text(-0.055, 0.49, "Perturbation\nEvidence", ha="left", va="center", fontsize=10, weight="bold", color="#374151")
    ax.text(-0.055, 0.17, "Consensus\nPrograms", ha="left", va="center", fontsize=10, weight="bold", color="#374151")

    for _, row in executed.iterrows():
        c = f"cell:{row['cell']}"
        d = f"drug:{row['drug']}"
        if c not in pos or d not in pos:
            continue
        linestyle = "-" if "user_specified" in str(row["perturbation_match_type"]) else "--"
        ax.annotate(
            "",
            xy=pos[d],
            xytext=pos[c],
            arrowprops=dict(arrowstyle="-", color="#9ca3af", lw=1.3, linestyle=linestyle, alpha=0.62),
            zorder=1,
        )

    collapsed: dict[tuple[str, str], list[float]] = {}
    for _, row in sub.iterrows():
        collapsed.setdefault((str(row["drug"]), str(row["label"])), []).append(float(row["score"]))
    max_abs = max([abs(v) for vals in collapsed.values() for v in vals] + [1.0])
    for (drug, fn), vals in collapsed.items():
        d = f"drug:{drug}"
        f = f"fn:{fn}"
        if d not in pos or f not in pos:
            continue
        score = sum(vals) / len(vals)
        color = "#b23a48" if score > 0 else "#33658a"
        lw = 0.65 + 2.8 * min(abs(score) / max_abs, 1.0)
        ax.annotate(
            "",
            xy=pos[f],
            xytext=pos[d],
            arrowprops=dict(arrowstyle="-", color=color, lw=lw, alpha=0.52),
            zorder=2,
        )

    for cell in cells:
        _draw_node(ax, pos[f"cell:{cell}"], cell, "#dbeafe", "#2563eb", size=360, fs=9.0, width=12, yoff=0.050)
    for drug in drugs:
        _draw_node(ax, pos[f"drug:{drug}"], drug, "#fef3c7", "#d97706", size=390, fs=9.0, width=14, yoff=0.050)
    for fn in functions:
        scores = sub[sub["label"] == fn]["score"].astype(float).tolist()
        mean_score = sum(scores) / len(scores) if scores else 0.0
        edge = "#b23a48" if mean_score >= 0 else "#33658a"
        _draw_node(
            ax,
            pos[f"fn:{fn}"],
            _display_function(fn),
            "#f9fafb",
            edge,
            size=300,
            fs=8.2,
            width=18,
            yoff=0.040,
        )

    handles = [
        Line2D([0], [0], color="#9ca3af", lw=1.4, label="cell-to-perturbation match"),
        Line2D([0], [0], color="#b23a48", lw=2.8, label="activated function edge"),
        Line2D([0], [0], color="#33658a", lw=2.8, label="suppressed function edge"),
    ]
    ax.legend(handles=handles, loc="lower center", bbox_to_anchor=(0.5, -0.035), ncol=3, frameon=False, fontsize=9)
    ax.set_title("Evidence Match Network", fontsize=15, weight="bold", pad=8)
    fig.tight_layout(rect=(0, 0.03, 1, 0.96))

    pdf = OUT_DIR / "figure5a_r15c01_decitabine_leukemia_route_graph_full_labels_editable_text.pdf"
    png = OUT_DIR / "figure5a_r15c01_decitabine_leukemia_route_graph_full_labels_editable_text.png"
    svg = OUT_DIR / "figure5a_r15c01_decitabine_leukemia_route_graph_full_labels_editable_text.svg"
    fig.savefig(pdf, bbox_inches="tight")
    fig.savefig(png, dpi=180, bbox_inches="tight")
    fig.savefig(svg, bbox_inches="tight")
    plt.close(fig)
    print(pdf)
    print(png)
    print(svg)


if __name__ == "__main__":
    main()

