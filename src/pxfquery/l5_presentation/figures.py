from __future__ import annotations

import html
from pathlib import Path
from typing import Any

from pxfquery.l5_presentation.tables import build_tables


def build_figure_specs(dossier: dict[str, Any], *, max_items: int = 12, include_svg: bool = True) -> list[dict[str, Any]]:
    tables = build_tables(dossier)
    ranked = tables["ranked_results"][:max_items]
    routes = tables["route_summary"]
    rules = tables["claim_rules"]
    specs = []
    if ranked:
        specs.append(_bar_spec(ranked))
        specs.append(_bubble_spec(ranked))
        specs.append(_heatmap_spec(ranked))
    if routes:
        specs.append(_route_flow_spec(routes, dossier))
    if rules:
        specs.append(_evidence_panel_spec(rules, dossier))
    if include_svg:
        for spec in specs:
            spec["svg"] = render_figure_svg(spec)
    return specs


def write_figure_files(
    specs: list[dict[str, Any]],
    output_dir: str | Path,
    *,
    prefix: str = "pxfquery",
    fmt: str = "png",
    dpi: int = 160,
) -> list[str]:
    if not specs:
        raise ValueError("L5 cannot write figures because L4 supplied no figure-ready evidence values.")
    fmt = fmt.lower().lstrip(".")
    if fmt not in {"png", "svg"}:
        raise ValueError("figure format must be 'png' or 'svg'")
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    paths = []
    for idx, spec in enumerate(specs, start=1):
        safe_kind = _safe_name(str(spec.get("kind") or "figure"))
        path = target / f"{prefix}_{idx:02d}_{safe_kind}.{fmt}"
        if fmt == "svg":
            svg = spec.get("svg") or render_figure_svg(spec)
            path.write_text(svg, encoding="utf-8")
        else:
            fig = render_figure_matplotlib(spec)
            fig.savefig(path, dpi=dpi, bbox_inches="tight")
            _close_matplotlib_figure(fig)
        paths.append(str(path))
    return paths


def render_figure_matplotlib(spec: dict[str, Any]):
    kind = spec.get("kind")
    if kind == "bar":
        return _render_bar_matplotlib(spec)
    if kind == "bubble":
        return _render_bubble_matplotlib(spec)
    if kind == "heatmap":
        return _render_heatmap_matplotlib(spec)
    if kind == "route_flow":
        return _render_route_flow_matplotlib(spec)
    if kind == "evidence_panel":
        return _render_evidence_panel_matplotlib(spec)
    raise ValueError(f"unsupported figure kind: {kind}")


def render_figure_svg(spec: dict[str, Any], *, width: int = 860) -> str:
    kind = spec.get("kind")
    if kind == "bar":
        return _render_bar_svg(spec, width=width)
    if kind == "bubble":
        return _render_bubble_svg(spec, width=width)
    if kind == "heatmap":
        return _render_heatmap_svg(spec, width=width)
    if kind == "route_flow":
        return _render_route_flow_svg(spec, width=width)
    if kind == "evidence_panel":
        return _render_evidence_panel_svg(spec, width=width)
    raise ValueError(f"unsupported figure kind: {kind}")


def _bar_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "kind": "bar",
        "title": "Ranked evidence score",
        "x": [str(item.get("label") or "result") for item in rows],
        "y": [_numeric(item.get("score")) for item in rows],
        "color_by": [str(item.get("direction") or item.get("kind") or "result") for item in rows],
        "caption": "Top evidence-backed rows from the primary query route.",
    }


def _bubble_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    scores = [_numeric(item.get("score")) for item in rows]
    return {
        "kind": "bubble",
        "title": "Result magnitude and rank",
        "labels": [str(item.get("label") or "result") for item in rows],
        "x": [item.get("rank") if item.get("rank") is not None else idx + 1 for idx, item in enumerate(rows)],
        "y": scores,
        "size": [max(abs(score), 0.05) for score in scores],
        "caption": "Bubble size follows absolute score magnitude.",
    }


def _heatmap_spec(rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "kind": "heatmap",
        "title": "Primary route score heatmap",
        "rows": [str(item.get("label") or "result") for item in rows],
        "columns": ["primary route"],
        "values": [[_numeric(item.get("score"))] for item in rows],
        "caption": "Compact heatmap view of the main evidence scores.",
    }


def _route_flow_spec(routes: list[dict[str, Any]], dossier: dict[str, Any]) -> dict[str, Any]:
    route_labels = []
    for route in routes[:6]:
        label = route.get("route_id") or route.get("tier") or route.get("status") or "route"
        if route.get("cell"):
            label = f"{label}: {route['cell']}"
        route_labels.append(str(label))
    return {
        "kind": "route_flow",
        "title": "Query evidence path",
        "nodes": ["Question", "Route selection", "Evidence matrix", "Evidence review", "Report"],
        "route_labels": route_labels,
        "route_count": len(routes),
        "status": dossier.get("dossier_status"),
        "caption": "High-level path from the user question to the displayed evidence.",
    }


def _evidence_panel_spec(rules: list[dict[str, Any]], dossier: dict[str, Any]) -> dict[str, Any]:
    return {
        "kind": "evidence_panel",
        "title": "Evidence limits",
        "items": rules,
        "confidence": (dossier.get("uncertainty_layer") or {}).get("confidence"),
        "caption": "Claims the report may mention and claims it must avoid.",
    }


def _render_bar_svg(spec: dict[str, Any], *, width: int) -> str:
    labels = spec.get("x", [])
    values = [_numeric(v) for v in spec.get("y", [])]
    colors = spec.get("color_by", [])
    n = max(len(labels), 1)
    row_h = 34
    left = 250
    mid = left + 250
    height = 86 + n * row_h
    max_abs = max([abs(v) for v in values] or [1.0]) or 1.0
    body = []
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 56 + i * row_h
        bar_w = int((abs(value) / max_abs) * 230)
        x = mid if value >= 0 else mid - bar_w
        color = _direction_color(colors[i] if i < len(colors) else "")
        body.append(f'<text x="12" y="{y + 17}" class="label">{_esc(_short(label, 34))}</text>')
        body.append(f'<rect x="{x}" y="{y}" width="{max(bar_w, 2)}" height="20" rx="3" fill="{color}"/>')
        body.append(f'<text x="{mid + 245}" y="{y + 16}" class="value">{value:.3g}</text>')
    body.append(f'<line x1="{mid}" x2="{mid}" y1="48" y2="{height - 24}" stroke="#475569" stroke-width="1"/>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_bubble_svg(spec: dict[str, Any], *, width: int) -> str:
    labels = spec.get("labels", [])
    yvals = [_numeric(v) for v in spec.get("y", [])]
    sizes = [_numeric(v) for v in spec.get("size", [])]
    n = max(len(labels), 1)
    height = 96 + n * 36
    max_size = max(sizes or [1.0]) or 1.0
    min_v = min(yvals or [0.0])
    max_v = max(yvals or [1.0])
    span = max(max_v - min_v, 1e-9)
    body = []
    for i, label in enumerate(labels):
        value = yvals[i] if i < len(yvals) else 0.0
        radius = 7 + int((abs(sizes[i] if i < len(sizes) else value) / max_size) * 18)
        x = 280 + int(((value - min_v) / span) * 460)
        y = 60 + i * 36
        body.append(f'<text x="12" y="{y + 5}" class="label">{_esc(_short(label, 34))}</text>')
        body.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="#7a9e7e" opacity="0.82"/>')
        body.append(f'<text x="{x + radius + 8}" y="{y + 5}" class="value">{value:.3g}</text>')
    body.append('<text x="280" y="40" class="axis">score axis</text>')
    body.append(f'<line x1="280" x2="740" y1="48" y2="48" stroke="#94a3b8" stroke-width="1"/>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_heatmap_svg(spec: dict[str, Any], *, width: int) -> str:
    labels = spec.get("rows", [])
    values = [(_numeric(row[0]) if row else 0.0) for row in spec.get("values", [])]
    n = max(len(labels), 1)
    row_h = 28
    height = 82 + n * row_h
    max_abs = max([abs(v) for v in values] or [1.0]) or 1.0
    body = []
    for i, (label, value) in enumerate(zip(labels, values)):
        y = 52 + i * row_h
        intensity = abs(value) / max_abs
        color = _heat_color(value, intensity)
        body.append(f'<text x="12" y="{y + 18}" class="label">{_esc(_short(label, 38))}</text>')
        body.append(f'<rect x="300" y="{y}" width="360" height="22" rx="3" fill="{color}"/>')
        body.append(f'<text x="675" y="{y + 17}" class="value">{value:.3g}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_route_flow_svg(spec: dict[str, Any], *, width: int) -> str:
    nodes = spec.get("nodes", [])
    route_labels = spec.get("route_labels", [])
    height = 180 + max(len(route_labels), 1) * 22
    step = max((width - 80) // max(len(nodes), 1), 110)
    body = []
    for i, node in enumerate(nodes):
        x = 36 + i * step
        body.append(f'<rect x="{x}" y="54" width="118" height="44" rx="7" fill="#ffffff" stroke="#64748b"/>')
        body.append(f'<text x="{x + 12}" y="82" class="label">{_esc(_short(str(node), 14))}</text>')
        if i < len(nodes) - 1:
            body.append(f'<line x1="{x + 118}" y1="76" x2="{x + step}" y2="76" stroke="#64748b" marker-end="url(#arrow)"/>')
    body.append(f'<text x="36" y="128" class="value">status: {_esc(str(spec.get("status")))}, routes: {_esc(str(spec.get("route_count")))}</text>')
    for idx, label in enumerate(route_labels[:8]):
        body.append(f'<text x="52" y="{158 + idx * 22}" class="small">- {_esc(_short(label, 95))}</text>')
    return _svg_shell(spec, width, height, "\n".join(body), defs=_arrow_def())


def _render_evidence_panel_svg(spec: dict[str, Any], *, width: int) -> str:
    items = spec.get("items", [])[:10]
    row_h = 42
    height = 94 + max(len(items), 1) * row_h
    body = [f'<text x="28" y="46" class="value">confidence: {_esc(str(spec.get("confidence")))}</text>']
    for i, item in enumerate(items):
        y = 66 + i * row_h
        rule = str(item.get("rule") or "rule")
        text = str(item.get("text") or "")
        color = "#b23a48" if rule == "must_not_claim" else "#33658a"
        body.append(f'<rect x="24" y="{y}" width="{width - 64}" height="30" rx="5" fill="#ffffff" stroke="#d8dde6"/>')
        body.append(f'<rect x="24" y="{y}" width="6" height="30" fill="{color}"/>')
        body.append(f'<text x="42" y="{y + 20}" class="small">{_esc(rule.replace("_", " "))}: {_esc(_short(text, 100))}</text>')
    return _svg_shell(spec, width, height, "\n".join(body))


def _render_bar_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    labels = [str(item) for item in spec.get("x", [])]
    values = [_numeric(v) for v in spec.get("y", [])]
    if not labels or not values:
        raise ValueError("bar figure needs labels and values")
    colors = [_direction_color(str(v)) for v in spec.get("color_by", [])]
    if len(colors) < len(values):
        colors.extend(["#7a9e7e"] * (len(values) - len(colors)))
    fig_h = max(3.2, 0.34 * len(labels) + 1.8)
    fig, ax = plt.subplots(figsize=(9, fig_h))
    y = list(range(len(labels)))
    ax.barh(y, values, color=colors[: len(values)])
    ax.axvline(0, color="#475569", linewidth=0.8)
    ax.set_yticks(y)
    ax.set_yticklabels([_short(label, 42) for label in labels])
    ax.invert_yaxis()
    ax.set_xlabel("matrix score")
    ax.set_title(str(spec.get("title") or "Ranked evidence score"))
    ax.grid(axis="x", alpha=0.25)
    _caption(fig, spec)
    return fig


def _render_bubble_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    labels = [str(item) for item in spec.get("labels", [])]
    x = [_numeric(v) for v in spec.get("x", [])]
    y = [_numeric(v) for v in spec.get("y", [])]
    sizes = [_numeric(v) for v in spec.get("size", [])]
    if not labels or not x or not y:
        raise ValueError("bubble figure needs labels, x, and y values")
    scaled = [80 + 520 * (abs(v) / (max([abs(s) for s in sizes] or [1.0]) or 1.0)) for v in sizes]
    fig_h = max(3.4, 0.32 * len(labels) + 1.8)
    fig, ax = plt.subplots(figsize=(9, fig_h))
    ax.scatter(x[: len(y)], y, s=scaled[: len(y)], color="#7a9e7e", alpha=0.72, edgecolor="#334155")
    for label, xi, yi in zip(labels, x, y):
        ax.text(xi, yi, " " + _short(label, 28), va="center", fontsize=8)
    ax.set_xlabel("rank")
    ax.set_ylabel("matrix score")
    ax.set_title(str(spec.get("title") or "Result magnitude and rank"))
    ax.grid(alpha=0.25)
    _caption(fig, spec)
    return fig


def _render_heatmap_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    labels = [str(item) for item in spec.get("rows", [])]
    values = [[_numeric(v) for v in row] for row in spec.get("values", [])]
    if not labels or not values:
        raise ValueError("heatmap figure needs row labels and values")
    fig_h = max(3.0, 0.32 * len(labels) + 1.5)
    fig, ax = plt.subplots(figsize=(7.8, fig_h))
    image = ax.imshow(values, aspect="auto", cmap="coolwarm")
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels([_short(label, 42) for label in labels])
    ax.set_xticks(range(len(spec.get("columns", ["primary route"]))))
    ax.set_xticklabels(spec.get("columns", ["primary route"]))
    ax.set_title(str(spec.get("title") or "Primary route score heatmap"))
    fig.colorbar(image, ax=ax, shrink=0.72, label="matrix score")
    _caption(fig, spec)
    return fig


def _render_route_flow_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    nodes = [str(item) for item in spec.get("nodes", [])]
    if not nodes:
        raise ValueError("route flow figure needs nodes")
    fig, ax = plt.subplots(figsize=(10, 3.6))
    ax.axis("off")
    xs = [0.08 + i * (0.84 / max(len(nodes) - 1, 1)) for i in range(len(nodes))]
    for idx, (x, label) in enumerate(zip(xs, nodes)):
        ax.text(x, 0.68, label, ha="center", va="center", fontsize=10, bbox={"boxstyle": "round,pad=0.35", "fc": "white", "ec": "#64748b"})
        if idx < len(xs) - 1:
            ax.annotate("", xy=(xs[idx + 1] - 0.07, 0.68), xytext=(x + 0.07, 0.68), arrowprops={"arrowstyle": "->", "color": "#64748b"})
    ax.text(0.02, 0.38, f"status: {spec.get('status')}   routes: {spec.get('route_count')}", fontsize=9, color="#334155")
    route_labels = spec.get("route_labels", [])[:6]
    for idx, label in enumerate(route_labels):
        ax.text(0.04, 0.24 - idx * 0.07, "- " + _short(label, 110), fontsize=8, color="#334155")
    ax.set_title(str(spec.get("title") or "Query evidence path"))
    _caption(fig, spec, y=0.02)
    return fig


def _render_evidence_panel_matplotlib(spec: dict[str, Any]):
    plt = _pyplot()
    items = spec.get("items", [])[:10]
    if not items:
        raise ValueError("evidence panel needs claim rules")
    fig_h = max(3.4, 0.42 * len(items) + 1.5)
    fig, ax = plt.subplots(figsize=(10, fig_h))
    ax.axis("off")
    ax.set_title(str(spec.get("title") or "Evidence limits"), loc="left")
    ax.text(0.02, 0.92, f"confidence: {spec.get('confidence')}", fontsize=9, color="#334155", transform=ax.transAxes)
    for idx, item in enumerate(items):
        y = 0.82 - idx * 0.08
        rule = str(item.get("rule") or "rule")
        color = "#b23a48" if rule == "must_not_claim" else "#33658a"
        ax.text(0.02, y, rule.replace("_", " "), fontsize=8, color="white", bbox={"boxstyle": "round,pad=0.25", "fc": color, "ec": color}, transform=ax.transAxes)
        ax.text(0.22, y, _short(str(item.get("text") or ""), 110), fontsize=8, color="#334155", transform=ax.transAxes)
    _caption(fig, spec, y=0.02)
    return fig


def _svg_shell(spec: dict[str, Any], width: int, height: int, body: str, *, defs: str = "") -> str:
    title = _esc(str(spec.get("title") or "PxFquery figure"))
    caption = _esc(str(spec.get("caption") or ""))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" role="img" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>{title}</title>
{defs}
<style>
  .title {{ font: 700 18px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #1f2933; }}
  .label {{ font: 13px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #263241; }}
  .value {{ font: 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #4b5563; }}
  .small {{ font: 12px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #334155; }}
  .axis {{ font: 11px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; fill: #64748b; }}
</style>
<rect x="0" y="0" width="{width}" height="{height}" fill="#fbfcfd" rx="8"/>
<text x="20" y="28" class="title">{title}</text>
{body}
<text x="20" y="{height - 12}" class="value">{caption}</text>
</svg>'''


def _arrow_def() -> str:
    return '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#64748b"/></marker></defs>'


def _direction_color(value: str) -> str:
    value = value.lower()
    if "suppress" in value or "down" in value or "negative" in value:
        return "#33658a"
    if "activ" in value or "up" in value or "positive" in value:
        return "#b23a48"
    return "#7a9e7e"


def _heat_color(value: float, intensity: float) -> str:
    alpha = 0.22 + min(max(intensity, 0.0), 1.0) * 0.68
    if value < 0:
        return f"rgba(51, 101, 138, {alpha:.2f})"
    return f"rgba(178, 58, 72, {alpha:.2f})"


def _safe_name(value: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in value).strip("_") or "figure"


def _short(value: Any, max_len: int) -> str:
    text = str(value)
    return text if len(text) <= max_len else text[: max_len - 3] + "..."


def _esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def _numeric(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _pyplot():
    import matplotlib

    matplotlib.use("Agg", force=True)
    import matplotlib.pyplot as plt

    return plt


def _caption(fig: Any, spec: dict[str, Any], *, y: float = 0.01) -> None:
    caption = str(spec.get("caption") or "")
    if caption:
        fig.text(0.01, y, caption, fontsize=8, color="#4b5563")
    fig.tight_layout(rect=(0, 0.04, 1, 0.96))


def _close_matplotlib_figure(fig: Any) -> None:
    plt = _pyplot()
    plt.close(fig)
