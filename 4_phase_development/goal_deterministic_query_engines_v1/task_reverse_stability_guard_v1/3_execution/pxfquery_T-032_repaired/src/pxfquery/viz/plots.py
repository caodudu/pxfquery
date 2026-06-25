"""
plots.py — Visualization functions for PxFquery.

Two backends:
  - plotly  : interactive, for Streamlit demo
  - matplotlib : publication-quality, for paper figures

All functions return the figure object so callers can save or display it.
"""

from __future__ import annotations
from typing import List, Optional, Literal
import pandas as pd
import numpy as np

from ..query.forward import ForwardResult
from ..query.reverse import ReverseResult


Backend = Literal["plotly", "matplotlib"]


# ------------------------------------------------------------------
# Forward query visualization
# ------------------------------------------------------------------

def plot_forward_bar(
    result: ForwardResult,
    top_n: int = 20,
    backend: Backend = "plotly",
    title: Optional[str] = None,
    figsize: tuple = (10, 8),
):
    """
    Horizontal bar chart of top activated and suppressed pathways.

    Activated terms → red; suppressed terms → blue.

    Parameters
    ----------
    result : ForwardResult
    top_n : int
        Number of terms to show on each side (activated / suppressed).
    backend : 'plotly' or 'matplotlib'
    title : str, optional
        Custom plot title. Auto-generated if None.
    figsize : tuple
        Figure size for matplotlib backend only.

    Returns
    -------
    plotly.graph_objects.Figure  or  matplotlib.figure.Figure
    """
    if not result.found:
        raise ValueError(f"Empty result: {result.note}")

    activated = result.top_activated.head(top_n)
    suppressed = result.top_suppressed.head(top_n).sort_values()

    # Combine: suppressed first (negative), then activated (positive)
    combined = pd.concat([suppressed, activated])
    colors = ["#4393c3" if v < 0 else "#d6604d" for v in combined.values]

    auto_title = (
        title or
        f"{result.perturbation}"
        + (f" · {result.cell_line}" if result.cell_line else " · all cell lines")
        + f" (n={result.n_obs})"
    )

    if backend == "plotly":
        return _forward_bar_plotly(combined, colors, auto_title)
    else:
        return _forward_bar_matplotlib(combined, colors, auto_title, figsize)


def _forward_bar_plotly(combined, colors, title):
    import plotly.graph_objects as go

    fig = go.Figure(go.Bar(
        x=combined.values,
        y=combined.index,
        orientation="h",
        marker_color=colors,
        hovertemplate="%{y}: %{x:.3f}<extra></extra>",
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Functional Score (NES × −log10 FDR)",
        yaxis=dict(autorange="reversed"),
        plot_bgcolor="white",
        height=max(400, len(combined) * 22),
        margin=dict(l=250, r=40, t=60, b=40),
    )
    fig.add_vline(x=0, line_width=1, line_color="black")
    return fig


def _forward_bar_matplotlib(combined, colors, title, figsize):
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    fig, ax = plt.subplots(figsize=figsize)
    y_pos = range(len(combined))
    bars = ax.barh(list(y_pos), combined.values, color=colors, edgecolor="none", height=0.7)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(combined.index, fontsize=9)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Functional Score (NES × −log10 FDR)")
    ax.set_title(title, fontsize=11, pad=10)
    ax.invert_yaxis()

    red_patch = mpatches.Patch(color="#d6604d", label="Activated")
    blue_patch = mpatches.Patch(color="#4393c3", label="Suppressed")
    ax.legend(handles=[red_patch, blue_patch], loc="lower right", fontsize=9)

    plt.tight_layout()
    return fig


# ------------------------------------------------------------------
# Reverse query visualization
# ------------------------------------------------------------------

def plot_reverse_table(
    result: ReverseResult,
    top_k: int = 20,
    backend: Backend = "plotly",
    title: Optional[str] = None,
):
    """
    Ranked table of perturbation candidates from a reverse query.

    Parameters
    ----------
    result : ReverseResult
    top_k : int
    backend : 'plotly' or 'matplotlib'
    title : str, optional

    Returns
    -------
    Figure
    """
    if not result.found:
        raise ValueError(f"Empty result: {result.note}")

    df = result.candidates_df.head(top_k).reset_index()
    df = df.rename(columns={"index": "rank"})

    auto_title = title or (
        "Candidate perturbations · "
        + (f"{result.cell_line} · " if result.cell_line else "")
        + f"activate: {', '.join(result.activate[:3])}"
    )

    if backend == "plotly":
        return _reverse_table_plotly(df, auto_title)
    else:
        return _reverse_table_matplotlib(df, auto_title)


def _reverse_table_plotly(df, title):
    import plotly.graph_objects as go

    sim_vals = df["similarity"].values
    bar_colors = [
        f"rgba(211,84,0,{max(0.2, v)})" for v in sim_vals / max(sim_vals + 1e-10)
    ]

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["Rank", "Perturbation", "Cell Line", "Similarity", "Key Terms"],
            fill_color="#4a4a4a",
            font=dict(color="white", size=12),
            align="left",
        ),
        cells=dict(
            values=[
                df["rank"],
                df["cmap_name"],
                df["cell_iname"],
                df["similarity"].round(3),
                df["driving_terms"],
            ],
            align="left",
            font=dict(size=11),
            height=28,
        ),
    )])
    fig.update_layout(title=title, margin=dict(t=60, b=20))
    return fig


def _reverse_table_matplotlib(df, title):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(14, max(4, len(df) * 0.4 + 1.5)))
    ax.axis("off")

    cols = ["rank", "cmap_name", "cell_iname", "similarity", "driving_terms"]
    col_labels = ["Rank", "Perturbation", "Cell Line", "Similarity", "Key Driving Terms"]
    cell_data = [[str(row[c]) if c != "similarity" else f"{row[c]:.3f}"
                  for c in cols] for _, row in df.iterrows()]

    tbl = ax.table(
        cellText=cell_data,
        colLabels=col_labels,
        loc="center",
        cellLoc="left",
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.auto_set_column_width(col=list(range(len(col_labels))))

    ax.set_title(title, fontsize=11, pad=10)
    plt.tight_layout()
    return fig


# ------------------------------------------------------------------
# Heatmap: multi-perturbation × pathway
# ------------------------------------------------------------------

def plot_heatmap(
    scores_df: pd.DataFrame,
    title: str = "Perturbation × Pathway Heatmap",
    backend: Backend = "plotly",
    figsize: tuple = (14, 10),
    vmax: Optional[float] = None,
):
    """
    Heatmap of perturbations (rows) × functional pathways (columns).

    Parameters
    ----------
    scores_df : pd.DataFrame
        DataFrame with perturbation names as index and pathway names as columns.
        Values are functional scores.
    title : str
    backend : 'plotly' or 'matplotlib'
    figsize : tuple
        matplotlib only.
    vmax : float, optional
        Color scale max (symmetric: [-vmax, vmax]).

    Returns
    -------
    Figure
    """
    vmax = vmax or float(np.abs(scores_df.values).max())

    if backend == "plotly":
        return _heatmap_plotly(scores_df, title, vmax)
    else:
        return _heatmap_matplotlib(scores_df, title, vmax, figsize)


def _heatmap_plotly(scores_df, title, vmax):
    import plotly.graph_objects as go

    fig = go.Figure(go.Heatmap(
        z=scores_df.values,
        x=list(scores_df.columns),
        y=list(scores_df.index),
        colorscale="RdBu_r",
        zmid=0,
        zmin=-vmax,
        zmax=vmax,
        hovertemplate="Pert: %{y}<br>Term: %{x}<br>Score: %{z:.3f}<extra></extra>",
        colorbar=dict(title="Score"),
    ))
    fig.update_layout(
        title=title,
        xaxis=dict(tickangle=-45, tickfont=dict(size=9)),
        yaxis=dict(tickfont=dict(size=9)),
        height=max(400, len(scores_df) * 25 + 150),
        margin=dict(l=200, r=80, t=60, b=200),
    )
    return fig


def _heatmap_matplotlib(scores_df, title, vmax, figsize):
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    fig, ax = plt.subplots(figsize=figsize)
    cmap = plt.get_cmap("RdBu_r")
    norm = mcolors.TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
    im = ax.imshow(scores_df.values, aspect="auto", cmap=cmap, norm=norm)

    ax.set_xticks(range(len(scores_df.columns)))
    ax.set_xticklabels(scores_df.columns, rotation=45, ha="right", fontsize=7)
    ax.set_yticks(range(len(scores_df.index)))
    ax.set_yticklabels(scores_df.index, fontsize=8)
    ax.set_title(title, fontsize=11, pad=10)

    plt.colorbar(im, ax=ax, label="Functional Score", shrink=0.6)
    plt.tight_layout()
    return fig
