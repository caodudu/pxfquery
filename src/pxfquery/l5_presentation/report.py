from __future__ import annotations

import html

from pxfquery.l5_presentation.model import PxFQueryAnswer


def render_html_answer(answer: PxFQueryAnswer) -> str:
    ranked = _table(answer.tables.get("ranked_results", []))
    routes = _table(answer.tables.get("route_summary", []))
    figures = "\n".join(_figure(spec) for spec in answer.figures)
    limits = "".join(f"<li>{html.escape(item)}</li>" for item in answer.limitations) or "<li>No additional limitations were supplied by the evidence review.</li>"
    source = _summary_source_label(answer.summary_source)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(answer.headline)}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; color: #1f2933; background: #f7f8fa; }}
    main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 56px; }}
    section {{ background: #fff; border: 1px solid #d8dde6; border-radius: 8px; padding: 20px; margin: 16px 0; }}
    h1 {{ font-size: 30px; margin: 0 0 12px; }}
    h2 {{ font-size: 18px; margin: 0 0 12px; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
    th, td {{ border-bottom: 1px solid #e6e9ef; padding: 8px; text-align: left; vertical-align: top; }}
    .summary {{ font-size: 17px; line-height: 1.5; }}
    .figure {{ border: 1px solid #d8dde6; border-radius: 8px; padding: 12px; margin: 10px 0; background: #fbfcfd; }}
    .bars span {{ display: block; height: 14px; margin: 5px 0; background: #33658a; min-width: 2px; }}
    .bubble-row {{ display: flex; align-items: center; gap: 10px; margin: 9px 0; }}
    .bubble {{ display: inline-flex; align-items: center; justify-content: center; border-radius: 50%; background: #7a9e7e; color: white; font-size: 11px; min-width: 18px; min-height: 18px; }}
    .heatmap {{ display: grid; grid-template-columns: minmax(120px, 240px) 1fr; gap: 4px; font-size: 13px; }}
    .heat-cell {{ min-height: 22px; border-radius: 4px; color: #111827; padding: 4px 8px; }}
    .flow {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px; }}
    .flow-node {{ border: 1px solid #b7c3d0; background: #fff; border-radius: 8px; padding: 8px 10px; }}
    .flow-arrow {{ color: #5b6778; }}
    .rules {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 8px; }}
    .rule {{ border-left: 4px solid #33658a; padding: 8px 10px; background: #fff; }}
    .rule.must-not {{ border-left-color: #b23a48; }}
    .muted {{ color: #5b6778; }}
  </style>
</head>
<body>
<main>
  <h1>{html.escape(answer.headline)}</h1>
  <p class="summary">{html.escape(answer.summary)}</p>
  <p class="muted">{html.escape(source)}</p>
  <section><h2>Question</h2><p>{html.escape(answer.question)}</p><p class="muted">{html.escape(answer.interpreted_question)}</p></section>
  <section><h2>Main Evidence</h2>{ranked}</section>
  <section><h2>Process Overview</h2>{routes}</section>
  <section><h2>Figures</h2>{figures or '<p class="muted">The evidence review did not contain quantitative values suitable for plotting.</p>'}</section>
  <section><h2>Evidence Limits</h2><ul>{limits}</ul></section>
</main>
</body>
</html>"""


def _summary_source_label(source: str | None) -> str:
    if source == "l4.llm_synthesis.biological_summary":
        return "Narrative summary generated from the evidence synthesis."
    if source == "l4.llm_synthesis.summary":
        return "Narrative summary generated from the evidence audit."
    if source == "l4.claim_basis.main_claim":
        return "Summary generated from the assembled evidence claim."
    return "Summary generated from the available evidence review."


def _table(rows: list[dict]) -> str:
    if not rows:
        return '<p class="muted">No table rows were supplied.</p>'
    keys = list(dict.fromkeys(key for row in rows for key in row.keys()))
    header = "".join(f"<th>{html.escape(str(key).replace('_', ' ').title())}</th>" for key in keys)
    body = ""
    for row in rows:
        body += "<tr>" + "".join(f"<td>{html.escape(str(row.get(key, '')))}</td>" for key in keys) + "</tr>"
    return f"<table><thead><tr>{header}</tr></thead><tbody>{body}</tbody></table>"


def _figure(spec: dict) -> str:
    title = html.escape(str(spec.get("title") or spec.get("kind") or "Figure"))
    caption = html.escape(str(spec.get("caption") or ""))
    if spec.get("svg"):
        return f'<div class="figure"><h3>{title}</h3>{spec["svg"]}<p class="muted">{caption}</p></div>'
    if spec.get("kind") == "bar":
        values = [abs(float(value or 0)) for value in spec.get("y", [])]
        max_value = max(values) if values else 1.0
        bars = ""
        for label, value in zip(spec.get("x", []), values):
            width = int((value / max_value) * 100) if max_value else 1
            bars += f"<div>{html.escape(str(label))}<span style=\"width:{max(width, 2)}%\"></span></div>"
        return f'<div class="figure"><h3>{title}</h3><div class="bars">{bars}</div><p class="muted">{caption}</p></div>'
    if spec.get("kind") == "bubble":
        sizes = [abs(float(value or 0)) for value in spec.get("size", [])]
        max_size = max(sizes) if sizes else 1.0
        bubbles = ""
        for label, x_value, y_value, size in zip(spec.get("labels", []), spec.get("x", []), spec.get("y", []), sizes):
            px = 20 + int((size / max_size) * 34) if max_size else 20
            bubbles += (
                f'<div class="bubble-row"><span class="bubble" style="width:{px}px;height:{px}px">{html.escape(str(x_value))}</span>'
                f'<span>{html.escape(str(label))}</span><span class="muted">score {html.escape(str(y_value))}</span></div>'
            )
        return f'<div class="figure"><h3>{title}</h3>{bubbles}<p class="muted">{caption}</p></div>'
    if spec.get("kind") == "heatmap":
        flat = [abs(float(row[0] or 0)) for row in spec.get("values", []) if row]
        max_value = max(flat) if flat else 1.0
        cells = ""
        for label, row in zip(spec.get("rows", []), spec.get("values", [])):
            value = float(row[0] or 0) if row else 0.0
            intensity = int((abs(value) / max_value) * 75) if max_value else 0
            color = f"rgba(51, 101, 138, {0.18 + intensity / 100:.2f})"
            cells += f'<div>{html.escape(str(label))}</div><div class="heat-cell" style="background:{color}">{html.escape(str(value))}</div>'
        return f'<div class="figure"><h3>{title}</h3><div class="heatmap">{cells}</div><p class="muted">{caption}</p></div>'
    if spec.get("kind") == "route_flow":
        nodes = spec.get("nodes", [])
        flow = ""
        for idx, node in enumerate(nodes):
            label = node.get("label") if isinstance(node, dict) else node
            if idx:
                flow += '<span class="flow-arrow">-></span>'
            flow += f'<span class="flow-node">{html.escape(str(label).replace("_", " ").title())}</span>'
        meta = f'<p class="muted">status {html.escape(str(spec.get("status")))}; routes {html.escape(str(spec.get("route_count")))}</p>'
        return f'<div class="figure"><h3>{title}</h3><div class="flow">{flow}</div>{meta}<p class="muted">{caption}</p></div>'
    if spec.get("kind") == "evidence_panel":
        rules = ""
        for item in spec.get("items", []):
            rule = str(item.get("rule", "rule"))
            cls = "rule must-not" if rule == "must_not_claim" else "rule"
            rules += f'<div class="{cls}"><strong>{html.escape(rule.replace("_", " "))}</strong><br>{html.escape(str(item.get("text", "")))}</div>'
        confidence = f'<p class="muted">confidence {html.escape(str(spec.get("confidence")))}</p>'
        return f'<div class="figure"><h3>{title}</h3><div class="rules">{rules}</div>{confidence}<p class="muted">{caption}</p></div>'
    return f'<div class="figure"><h3>{title}</h3><p class="muted">{caption}</p></div>'
