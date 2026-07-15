from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from pandas.errors import EmptyDataError

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
mpl.rcParams["font.family"] = "DejaVu Sans"


def clean_label(text: str) -> str:
    return str(text).replace("HALLMARK_", "").replace("_", " ").replace("  ", " ").strip()


def short_label(text: str, max_len: int = 24) -> str:
    text = clean_label(text)
    return text if len(text) <= max_len else text[: max_len - 1] + "..."


def wrapped_label(text: str, max_line: int = 16, max_lines: int = 2) -> str:
    text = str(text).replace("HALLMARK_", "").replace("_", " ").replace("  ", " ").strip()
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if len(candidate) <= max_line:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][: max_line - 1].rstrip() + "..."
    return "\n".join(lines)


def layer_positions(items: list[str], y: float, x0: float = 0.08, x1: float = 0.92) -> dict[str, tuple[float, float]]:
    if not items:
        return {}
    if len(items) == 1:
        return {items[0]: ((x0 + x1) / 2, y)}
    step = (x1 - x0) / (len(items) - 1)
    return {item: (x0 + i * step, y) for i, item in enumerate(items)}


def consensus_top3_terms(ranked: pd.DataFrame) -> list[str]:
    activated = ranked[ranked["score"] > 0].sort_values("score", ascending=False).head(3)
    suppressed = ranked[ranked["score"] < 0].sort_values("score", ascending=True).head(3)
    return list(activated["label"].astype(str)) + list(suppressed["label"].astype(str))


def render_case(case_dir: Path, case_id: str, output_dir: Path) -> Path:
    route_path = case_dir / f"{case_id}_route_summary.csv"
    rf_path = case_dir / f"{case_id}_route_function_results.csv"
    selected_scores_path = case_dir / f"{case_id}_selected_function_route_scores.csv"
    ranked_path = case_dir / f"{case_id}_ranked_results.csv"
    routes = pd.read_csv(route_path)
    ranked = pd.read_csv(ranked_path)

    routes = routes[routes["status"].eq("executed")].copy()
    if routes.empty:
        routes = pd.read_csv(route_path)

    funcs = consensus_top3_terms(ranked)
    if selected_scores_path.exists() and selected_scores_path.stat().st_size > 0:
        try:
            rf = pd.read_csv(selected_scores_path)
        except EmptyDataError:
            rf = pd.read_csv(rf_path)
    else:
        rf = pd.read_csv(rf_path)
    rf = rf[rf["label"].astype(str).isin(funcs)].copy()

    cells = list(dict.fromkeys(routes["cell"].dropna().astype(str)))
    perts = list(dict.fromkeys(routes["perturbation"].dropna().astype(str)))

    pos: dict[str, tuple[float, float]] = {}
    pos.update({f"cell:{k}": v for k, v in layer_positions(cells, 0.78, x0=0.16, x1=0.92).items()})
    pos.update({f"pert:{k}": v for k, v in layer_positions(perts, 0.49, x0=0.14, x1=0.94).items()})
    pos.update({f"func:{k}": v for k, v in layer_positions(funcs, 0.18, x0=0.12, x1=0.96).items()})

    width = max(8.2, 1.05 * max(len(cells), len(perts), len(funcs)))
    fig, ax = plt.subplots(figsize=(width, 9.2))
    ax.set_axis_off()
    ax.set_xlim(-0.10, 1)
    ax.set_ylim(0, 1)

    ax.text(-0.085, 0.78, "Cell\ncontext", ha="left", va="center", fontsize=10, weight="bold", color="#374151")
    ax.text(-0.085, 0.49, "Perturbation\nevidence", ha="left", va="center", fontsize=10, weight="bold", color="#374151")
    ax.text(-0.085, 0.18, "Top consensus\nfunctional\nprograms", ha="left", va="center", fontsize=10, weight="bold", color="#374151")

    # Cell -> perturbation route edges. Semantic/proxy routes use dashed lines.
    for _, row in routes.iterrows():
        c = f"cell:{row['cell']}"
        p = f"pert:{row['perturbation']}"
        if c not in pos or p not in pos:
            continue
        match_type = str(row.get("perturbation_match_type", ""))
        linestyle = "-" if match_type.startswith(("user", "normalized")) else "--"
        ax.annotate(
            "",
            xy=pos[p],
            xytext=pos[c],
            arrowprops=dict(arrowstyle="-", color="#9ca3af", lw=1.4, linestyle=linestyle, alpha=0.62),
        )

    max_abs = max(1.0, float(rf["score"].abs().max() if not rf.empty else 1.0))
    # Collapse route/cell-level scores to one perturbation-function edge.
    if not rf.empty:
        rf = rf.groupby(["perturbation", "label"], as_index=False)["score"].mean()
        rf = rf[rf["score"].abs() > 1e-12].copy()
    for _, row in rf.iterrows():
        p = f"pert:{row['perturbation']}"
        f = f"func:{row['label']}"
        if p not in pos or f not in pos:
            continue
        score = float(row["score"])
        color = "#c94747" if score > 0 else "#2f6fa3"
        lw = 0.7 + 2.8 * min(1.0, abs(score) / max_abs)
        ax.annotate(
            "",
            xy=pos[f],
            xytext=pos[p],
            arrowprops=dict(arrowstyle="-", color=color, lw=lw, alpha=0.5),
        )

    def draw_node(
        x: float,
        y: float,
        label: str,
        face: str,
        edge: str,
        size: int,
        fs: int = 10,
        max_line: int = 16,
        yoff: float = 0.055,
    ) -> None:
        ax.scatter([x], [y], s=size, facecolor=face, edgecolor=edge, linewidth=1.7, zorder=4)
        ax.text(x, y - yoff, wrapped_label(label, max_line=max_line), ha="center", va="top", fontsize=fs, zorder=5, linespacing=1.05)

    for cell in cells:
        draw_node(*pos[f"cell:{cell}"], cell, "#dbeafe", "#2563eb", 390, fs=9, max_line=12)
    for pert in perts:
        draw_node(*pos[f"pert:{pert}"], pert, "#fef3c7", "#d97706", 420, fs=9, max_line=12)
    for func in funcs:
        score = float(ranked.loc[ranked["label"].astype(str).eq(func), "score"].iloc[0])
        # Neutral node, small ring tint only marks final consensus sign; route direction remains edge-coded.
        edge = "#c94747" if score > 0 else "#2f6fa3"
        draw_node(*pos[f"func:{func}"], func, "#f9fafb", edge, 330, fs=8, max_line=15, yoff=0.045)

    ax.plot([], [], color="#c94747", lw=3, label="activated evidence edge")
    ax.plot([], [], color="#2f6fa3", lw=3, label="suppressed evidence edge")
    ax.plot([], [], color="#9ca3af", lw=1.4, label="cell-to-pert route")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.04), ncol=3, frameon=False, fontsize=10)
    ax.set_title(case_id, fontsize=15, weight="bold", pad=16)

    output_dir.mkdir(parents=True, exist_ok=True)
    out_png = output_dir / f"{case_id}_vertical_top3_route_graph.png"
    out_pdf = output_dir / f"{case_id}_vertical_top3_route_graph.pdf"
    fig.savefig(out_png, dpi=240, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    plt.close(fig)
    return out_png


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    print(render_case(args.case_dir, args.case_id, args.output_dir))


if __name__ == "__main__":
    main()


