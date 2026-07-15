from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def _short_label(text: str, max_len: int = 26) -> str:
    text = str(text).replace("HALLMARK_", "").replace("_", " ")
    text = text.replace("  ", " ").strip()
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "..."


def _spread_positions(items: list[str], x: float, y_top: float = 0.92, y_bottom: float = 0.12) -> dict[str, tuple[float, float]]:
    if not items:
        return {}
    if len(items) == 1:
        return {items[0]: (x, (y_top + y_bottom) / 2)}
    step = (y_top - y_bottom) / (len(items) - 1)
    return {item: (x, y_top - i * step) for i, item in enumerate(items)}


def render_case(case_dir: Path, case_id: str, output_dir: Path, *, max_functions: int = 10, max_edges_per_route: int = 3) -> Path:
    route_path = case_dir / f"{case_id}_route_summary.csv"
    rf_path = case_dir / f"{case_id}_route_function_results.csv"
    if not route_path.exists() or not rf_path.exists():
        raise FileNotFoundError(f"missing route files for {case_id}")

    routes = pd.read_csv(route_path)
    rf = pd.read_csv(rf_path)
    routes = routes[routes["status"].eq("executed")].copy()
    if routes.empty:
        routes = pd.read_csv(route_path)

    # Pick consensus-readable functions, then only draw per-route edges to those terms.
    ranked_path = case_dir / f"{case_id}_ranked_results.csv"
    if ranked_path.exists():
        ranked = pd.read_csv(ranked_path).head(max_functions)
        selected_functions = list(ranked["label"].astype(str))
    else:
        selected_functions = list(
            rf.assign(abs_score=rf["score"].abs())
            .sort_values("abs_score", ascending=False)["label"]
            .drop_duplicates()
            .head(max_functions)
        )
    selected = rf[rf["label"].astype(str).isin(selected_functions)].copy()

    cells = list(dict.fromkeys(routes["cell"].dropna().astype(str)))
    perts = list(dict.fromkeys(routes["perturbation"].dropna().astype(str)))
    funcs = selected_functions

    pos = {}
    pos.update({f"cell:{k}": v for k, v in _spread_positions(cells, 0.12).items()})
    pos.update({f"pert:{k}": v for k, v in _spread_positions(perts, 0.48).items()})
    pos.update({f"func:{k}": v for k, v in _spread_positions(funcs, 0.86, y_top=0.96, y_bottom=0.08).items()})

    fig_h = max(5.0, min(12.0, 0.45 * max(len(cells), len(perts), len(funcs)) + 2.8))
    fig, ax = plt.subplots(figsize=(11, fig_h))
    ax.set_axis_off()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    ax.text(0.12, 1.02, "Cell context", ha="center", va="bottom", fontsize=12, weight="bold")
    ax.text(0.48, 1.02, "Perturbation evidence", ha="center", va="bottom", fontsize=12, weight="bold")
    ax.text(0.86, 1.02, "Functional programs", ha="center", va="bottom", fontsize=12, weight="bold")

    # Cell -> perturbation route edges: neutral; direct/semantic route type is shown by line style.
    for _, row in routes.iterrows():
        c = f"cell:{row['cell']}"
        p = f"pert:{row['perturbation']}"
        if c not in pos or p not in pos:
            continue
        style = "-" if str(row.get("perturbation_match_type", "")).startswith(("user", "normalized")) else "--"
        ax.annotate(
            "",
            xy=pos[p],
            xytext=pos[c],
            arrowprops=dict(arrowstyle="-", color="#9aa3ad", lw=1.2, linestyle=style, alpha=0.62),
        )

    # Perturbation -> function edges: direction is encoded on the edge.
    edge_rows = []
    for route_id, block in selected.groupby("route_id", sort=False):
        block = block.assign(abs_score=block["score"].abs()).sort_values("abs_score", ascending=False).head(max_edges_per_route)
        edge_rows.append(block)
    draw_edges = pd.concat(edge_rows, ignore_index=True) if edge_rows else selected.head(0)
    max_abs = max(1.0, float(draw_edges["score"].abs().max() if not draw_edges.empty else 1.0))
    for _, row in draw_edges.iterrows():
        p = f"pert:{row['perturbation']}"
        f = f"func:{row['label']}"
        if p not in pos or f not in pos:
            continue
        score = float(row["score"])
        color = "#c94747" if score > 0 else "#2f6fa3"
        lw = 0.7 + 2.6 * min(1.0, abs(score) / max_abs)
        rad = 0.05 * math.sin(hash((p, f)) % 5)
        ax.annotate(
            "",
            xy=pos[f],
            xytext=pos[p],
            arrowprops=dict(
                arrowstyle="-",
                color=color,
                lw=lw,
                alpha=0.58,
                connectionstyle=f"arc3,rad={rad:.2f}",
            ),
        )

    def draw_nodes(prefix: str, items: list[str], face: str, edge: str, size: int) -> None:
        for item in items:
            key = f"{prefix}:{item}"
            if key not in pos:
                continue
            x, y = pos[key]
            ax.scatter([x], [y], s=size, facecolor=face, edgecolor=edge, linewidth=1.4, zorder=5)
            label = _short_label(item, 30 if prefix != "func" else 34)
            ha = "right" if prefix == "cell" else "center" if prefix == "pert" else "left"
            dx = -0.025 if prefix == "cell" else 0 if prefix == "pert" else 0.025
            ax.text(x + dx, y, label, ha=ha, va="center", fontsize=9, zorder=6)

    draw_nodes("cell", cells, "#dbeafe", "#2563eb", 360)
    draw_nodes("pert", perts, "#fef3c7", "#d97706", 420)
    draw_nodes("func", funcs, "#f3f4f6", "#4b5563", 260)

    ax.plot([], [], color="#c94747", lw=3, label="activated edge")
    ax.plot([], [], color="#2f6fa3", lw=3, label="suppressed edge")
    ax.plot([], [], color="#9aa3ad", lw=1.4, label="cell-to-pert route")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.06), ncol=3, frameon=False, fontsize=9)
    ax.set_title(case_id, fontsize=14, weight="bold", pad=18)

    output_dir.mkdir(parents=True, exist_ok=True)
    out_png = output_dir / f"{case_id}_three_layer_route_graph.png"
    out_pdf = output_dir / f"{case_id}_three_layer_route_graph.pdf"
    fig.savefig(out_png, dpi=220, bbox_inches="tight")
    fig.savefig(out_pdf, bbox_inches="tight")
    plt.close(fig)
    return out_png


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--case-id", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-functions", type=int, default=10)
    parser.add_argument("--max-edges-per-route", type=int, default=3)
    args = parser.parse_args()
    out = render_case(
        args.case_dir,
        args.case_id,
        args.output_dir,
        max_functions=args.max_functions,
        max_edges_per_route=args.max_edges_per_route,
    )
    print(out)


if __name__ == "__main__":
    main()

