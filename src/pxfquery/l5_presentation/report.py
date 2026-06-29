from __future__ import annotations

import base64
from io import BytesIO
import html
from typing import Any

from pxfquery.l5_presentation.model import PxFQueryAnswer
from pxfquery.version import __version__


def render_html_answer(answer: PxFQueryAnswer) -> str:
    html_figures = _html_figure_specs(answer.figures)
    figures = "\n".join(_figure_card(spec, index) for index, spec in enumerate(html_figures, start=1))
    quality = _quality_report(answer)
    context = _context_line(answer)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{_esc(answer.headline)}</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #172033;
      --muted: #5f6b7a;
      --line: #d9e0e8;
      --panel: #ffffff;
      --soft: #f5f7fa;
      --accent: #2f6f8f;
    }}
    body {{
      margin: 0;
      background: var(--soft);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
      line-height: 1.55;
    }}
    main {{
      max-width: 940px;
      margin: 0 auto;
      padding: 32px 24px 48px;
    }}
    header {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 24px;
      margin-bottom: 16px;
    }}
    section {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 22px 24px;
      margin: 16px 0;
    }}
    h1 {{
      margin: 0 0 10px;
      font-size: 28px;
      line-height: 1.18;
      letter-spacing: 0;
    }}
    h2 {{
      margin: 0 0 12px;
      font-size: 17px;
      letter-spacing: 0;
    }}
    h3 {{
      margin: 0 0 10px;
      font-size: 15px;
      color: var(--ink);
      letter-spacing: 0;
    }}
    p {{
      margin: 0 0 10px;
    }}
    footer {{
      color: var(--muted);
      font-size: 13px;
      text-align: right;
      padding: 10px 2px 0;
    }}
    .question {{
      font-size: 18px;
      font-weight: 600;
    }}
    .context {{
      color: var(--muted);
      font-size: 14px;
    }}
    .answer {{
      white-space: pre-wrap;
      font-size: 17px;
    }}
    .figure-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 14px;
    }}
    .figure-card {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      background: #fbfcfe;
    }}
    .figure-card img {{
      display: block;
      width: min(100%, 520px);
      max-height: 360px;
      object-fit: contain;
      background: #ffffff;
      margin: 0 auto;
    }}
    .quality {{
      border-left: 4px solid var(--accent);
      padding-left: 14px;
      color: #243042;
      white-space: pre-wrap;
    }}
    .quality-meta {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
    }}
    .pill {{
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 4px 10px;
      font-size: 12px;
      color: var(--muted);
      background: #ffffff;
    }}
    .empty {{
      color: var(--muted);
      font-style: italic;
    }}
  </style>
</head>
<body>
<main>
  <header>
    <h1>{_esc(answer.headline)}</h1>
    <p class="question">{_esc(answer.question)}</p>
    <p class="context">{_esc(context)}</p>
  </header>

  <section aria-label="Answer">
    <h2>Answer</h2>
    <div class="answer">{_esc(answer.summary)}</div>
  </section>

  <section aria-label="Figures">
    <h2>Figures</h2>
    <div class="figure-grid">
      {figures or '<p class="empty">No figure-ready quantitative evidence was available for this query.</p>'}
    </div>
  </section>

  <section aria-label="Run quality report">
    <h2>Run Quality Report</h2>
    <div class="quality">{_esc(quality["summary"])}</div>
    <div class="quality-meta">{quality["meta"]}</div>
  </section>

  <footer>PxFquery package version {html.escape(__version__)}</footer>
</main>
</body>
</html>"""


def _figure_card(spec: dict[str, Any], index: int) -> str:
    title = str(spec.get("title") or spec.get("kind") or f"Figure {index}")
    image = _figure_png_data_uri(spec)
    if image is None:
        return f'<div class="figure-card"><h3>{_esc(title)}</h3><p class="empty">This figure could not be rendered in the HTML report.</p></div>'
    return f'<div class="figure-card"><h3>{_esc(title)}</h3><img src="{image}" alt="{_esc(title)}"></div>'


def _html_figure_specs(specs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    preferred = {
        "evidence_match_map",
        "function_consensus_bar",
        "reverse_candidate_bubble",
    }
    selected = [spec for spec in specs if str(spec.get("kind") or "") in preferred]
    return selected or specs[:1]


def _figure_png_data_uri(spec: dict[str, Any]) -> str | None:
    try:
        fig = _render_html_figure(spec)
        buffer = BytesIO()
        fig.savefig(buffer, format="png", dpi=150, bbox_inches="tight")
        try:
            import matplotlib.pyplot as plt

            plt.close(fig)
        except Exception:
            pass
        payload = base64.b64encode(buffer.getvalue()).decode("ascii")
        return f"data:image/png;base64,{payload}"
    except Exception:
        return None


def _render_html_figure(spec: dict[str, Any]):
    kind = str(spec.get("kind") or "")
    if kind == "evidence_match_map":
        return _render_html_match_map(spec)
    if kind == "function_consensus_bar":
        return _render_html_consensus_bar(spec)
    if kind == "reverse_candidate_bubble":
        return _render_html_candidate_bubble(spec)
    return _render_html_placeholder(spec)


def _pyplot():
    import matplotlib

    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt

    return plt


def _render_html_match_map(spec: dict[str, Any]):
    plt = _pyplot()
    points = spec.get("points") or []
    fig, ax = plt.subplots(figsize=(2.0, 1.55))
    ax.scatter([0], [0], s=14, color="#8f98a3", edgecolors="#263241", linewidths=0.35, zorder=3)
    for point in points[:10]:
        x = _num(point.get("cell_distance"))
        y = _num(point.get("y_value"))
        size = 12 + min(_num(point.get("n_rows")), 8) * 2.5
        ax.plot([0, x], [0, y], color="#c8d0da", linewidth=0.35, linestyle=":", zorder=1)
        ax.scatter([x], [y], s=size, color="#3f7899", alpha=0.78, edgecolors="#263241", linewidths=0.35, zorder=2)
    ax.set_title("Evidence Match", fontsize=6, pad=3)
    ax.set_xlabel("Cell Distance", fontsize=5)
    ax.set_ylabel("Perturbation Distance", fontsize=5)
    ax.tick_params(labelsize=4.5, length=2, width=0.35)
    ax.grid(alpha=0.18, linewidth=0.35)
    for spine in ax.spines.values():
        spine.set_linewidth(0.45)
    _pad_axes(ax)
    return fig


def _render_html_consensus_bar(spec: dict[str, Any]):
    plt = _pyplot()
    items = list(spec.get("items") or [])[:7]
    if not items:
        return _render_html_placeholder(spec)
    labels = [_short(str(item.get("label") or "Program"), 22) for item in items]
    activated = [_num(item.get("activated_hits")) for item in items]
    suppressed = [_num(item.get("suppressed_hits")) for item in items]
    y = list(range(len(items)))
    fig_h = max(1.45, 0.19 * len(items) + 0.55)
    fig, ax = plt.subplots(figsize=(2.25, fig_h))
    ax.barh(y, activated, color="#b23a48", height=0.45)
    ax.barh(y, suppressed, left=activated, color="#33658a", height=0.45)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=4.8)
    ax.invert_yaxis()
    ax.set_xlabel("Evidence Hits", fontsize=5)
    ax.set_title("Program Support", fontsize=6, pad=3)
    ax.tick_params(axis="x", labelsize=4.5, length=2, width=0.35)
    ax.tick_params(axis="y", length=0, pad=1)
    ax.grid(axis="x", alpha=0.18, linewidth=0.35)
    for spine in ax.spines.values():
        spine.set_linewidth(0.4)
    return fig


def _render_html_candidate_bubble(spec: dict[str, Any]):
    plt = _pyplot()
    items = list(spec.get("candidates") or [])[:6]
    if not items:
        return _render_html_placeholder(spec)
    x = [_num(item.get("support")) for item in items]
    score = [_num(item.get("score")) for item in items]
    max_score = max(score + [1.0])
    sizes = [12 + 34 * (value / max_score) for value in score]
    colors = ["#b23a48" if item.get("exact_cell_support") else "#33658a" for item in items]
    labels = [_short(item.get("label"), 16) for item in items]
    y = list(range(len(items)))
    fig_h = max(1.45, 0.19 * len(items) + 0.55)
    fig, ax = plt.subplots(figsize=(2.3, fig_h))
    ax.scatter(x, y, s=sizes, c=colors, alpha=0.8, edgecolors="#263241", linewidths=0.35)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=4.8)
    ax.invert_yaxis()
    ax.set_title("Candidate Ranking", fontsize=6, pad=3)
    ax.set_xlabel("Support", fontsize=5)
    ax.set_ylabel("")
    ax.tick_params(axis="x", labelsize=4.5, length=2, width=0.35)
    ax.tick_params(axis="y", length=0, pad=1)
    ax.grid(axis="x", alpha=0.18, linewidth=0.35)
    for spine in ax.spines.values():
        spine.set_linewidth(0.45)
    _pad_axes(ax)
    return fig


def _render_html_placeholder(spec: dict[str, Any]):
    plt = _pyplot()
    fig, ax = plt.subplots(figsize=(2.0, 1.3))
    ax.axis("off")
    ax.text(0.5, 0.55, _short(spec.get("title") or "Figure", 30), ha="center", va="center", fontsize=6)
    return fig


def _pad_axes(ax) -> None:
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    dx = max(abs(xmax - xmin) * 0.12, 0.02)
    dy = max(abs(ymax - ymin) * 0.12, 0.02)
    ax.set_xlim(xmin - dx, xmax + dx)
    ax.set_ylim(ymin - dy, ymax + dy)


def _num(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _short(value: Any, max_len: int) -> str:
    text = str(value or "")
    return text if len(text) <= max_len else text[: max_len - 1] + "…"


def _html_figure_size(spec: dict[str, Any]) -> tuple[float, float]:
    kind = str(spec.get("kind") or "")
    if kind == "reverse_function_ring_heatmap":
        return (2.1, 2.1)
    if kind == "reverse_candidate_bubble":
        return (2.4, 1.8)
    if kind == "evidence_match_map":
        return (2.2, 2.0)
    if kind == "function_match_heatmap":
        return (2.6, 1.8)
    if kind == "function_consensus_bar":
        return (2.2, 1.6)
    return (2.4, 1.8)


def _quality_report(answer: PxFQueryAnswer) -> dict[str, str]:
    summary = str(answer.evidence.get("evidence_audit_summary") or "").strip()
    if not summary:
        status = _public_status(answer.evidence.get("dossier_status"))
        strength = _public_strength(answer.evidence.get("evidence_grade"))
        summary = f"The query completed with {status}. Evidence strength: {strength}."
    meta = []
    status = _public_status(answer.evidence.get("dossier_status"))
    if status:
        meta.append(("Status", status))
    strength = _public_strength(answer.evidence.get("evidence_grade"))
    if strength:
        meta.append(("Evidence strength", strength))
    modality = answer.evidence.get("primary_modality")
    if modality:
        meta.append(("Data type", str(modality).upper()))
    html_meta = "".join(f'<span class="pill">{_esc(label)}: {_esc(value)}</span>' for label, value in meta)
    return {"summary": summary, "meta": html_meta}


def _context_line(answer: PxFQueryAnswer) -> str:
    text = str(answer.interpreted_question or "").strip()
    if text:
        return f"Interpreted as: {text}"
    return "Interpreted from the supplied biological query."


def _public_status(value: Any) -> str:
    mapping = {
        "evidence_found": "results available",
        "partial_evidence": "partial results available",
        "unresolved_route": "query not resolved",
        "resource_unavailable": "resources unavailable",
        "no_matrix_hit": "no matrix match",
    }
    return mapping.get(str(value or ""), str(value or "unknown").replace("_", " "))


def _public_strength(value: Any) -> str:
    text = str(value or "")
    mapping = {
        "exact_primary_with_proxy_support": "direct primary evidence with supporting contextual evidence",
        "exact_matrix": "direct matrix evidence",
        "direct_or_close_representative_matrix": "direct or close representative matrix evidence",
        "strong_representative_matrix": "strong representative matrix evidence",
        "usable_neighbor_matrix": "usable neighboring-context evidence",
        "fallback_matrix": "fallback evidence",
        "distant_neighbor_matrix": "distant neighboring-context evidence",
    }
    return mapping.get(text, text.replace("_", " ") or "not reported")


def _esc(value: Any) -> str:
    return html.escape(str(value or ""), quote=True)
