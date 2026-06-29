from __future__ import annotations

import argparse
import html
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def main() -> None:
    parser = argparse.ArgumentParser(description="Render L2-to-L3 replay JSON as a tabbed HTML report.")
    parser.add_argument("json_path", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--title", default="PxFquery L2-to-L3 replay")
    args = parser.parse_args()
    payload = json.loads(args.json_path.read_text(encoding="utf-8"))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(render(payload, args.title), encoding="utf-8")
    print(args.out)


def render(payload: dict[str, Any], title: str) -> str:
    summary = payload["summary"]
    records = payload["records"]
    categories = sorted({str(r.get("category") or "generalization") for r in records})
    statuses = sorted({str(r.get("l3_execution_status")) for r in records})
    return f"""<!doctype html>
<html lang="zh">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<style>
:root {{ --bg:#f7f8fa; --panel:#fff; --ink:#1f2937; --muted:#667085; --line:#d7dce3; --ok:#0f766e; --warn:#b45309; --bad:#b91c1c; --chip:#eef2f7; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
header {{ padding:22px 28px 12px; border-bottom:1px solid var(--line); background:var(--panel); position:sticky; top:0; z-index:3; }}
h1 {{ margin:0 0 8px; font-size:20px; letter-spacing:0; }}
.meta {{ color:var(--muted); font-size:12px; display:flex; flex-wrap:wrap; gap:12px; }}
.tabs {{ display:flex; flex-wrap:wrap; gap:8px; padding:14px 28px 0; background:var(--panel); }}
.tab {{ border:1px solid var(--line); background:#fff; border-radius:6px; padding:7px 10px; cursor:pointer; color:#344054; }}
.tab.active {{ background:#111827; color:#fff; border-color:#111827; }}
main {{ padding:18px 28px 36px; }}
.view {{ display:none; }}
.view.active {{ display:block; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:12px; }}
.metric {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:12px; }}
.metric b {{ display:block; font-size:22px; margin-top:4px; }}
.panel {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; margin:14px 0; overflow:hidden; }}
.panel h2 {{ font-size:16px; margin:0; padding:12px 14px; border-bottom:1px solid var(--line); }}
table {{ border-collapse:collapse; width:100%; }}
th,td {{ border-bottom:1px solid var(--line); padding:8px 10px; text-align:left; vertical-align:top; }}
th {{ font-size:12px; color:#475467; background:#f8fafc; position:sticky; top:109px; z-index:2; }}
tr:hover td {{ background:#fbfcfe; }}
.status {{ display:inline-block; border-radius:999px; padding:2px 8px; font-size:12px; background:var(--chip); }}
.executed {{ color:var(--ok); background:#dff7ef; }}
.partial {{ color:var(--warn); background:#fff1d6; }}
.empty_matrix_hit,.failed {{ color:var(--bad); background:#fee2e2; }}
.filters {{ display:flex; gap:8px; flex-wrap:wrap; margin:0 0 12px; }}
select,input {{ border:1px solid var(--line); border-radius:6px; padding:7px 9px; background:#fff; }}
details {{ border-top:1px solid var(--line); }}
summary {{ cursor:pointer; padding:10px 12px; font-weight:600; }}
pre {{ white-space:pre-wrap; word-break:break-word; margin:0; padding:10px 12px; background:#0b1020; color:#e5e7eb; overflow:auto; }}
.route {{ margin:10px 12px; border:1px solid var(--line); border-radius:6px; overflow:hidden; }}
.small {{ color:var(--muted); font-size:12px; }}
</style>
</head>
<body>
<header>
<h1>{esc(title)}</h1>
<div class="meta">
<span>Source: {esc(summary.get("source_l2_report"))}</span>
<span>L3 resources: {esc(summary.get("l3_resource_dir"))}</span>
</div>
</header>
<nav class="tabs">
<button class="tab active" data-view="summary">Summary</button>
<button class="tab" data-view="category">Category</button>
<button class="tab" data-view="status">Status</button>
<button class="tab" data-view="cases">Case Detail</button>
</nav>
<main>
<section id="summary" class="view active">{summary_view(summary, records)}</section>
<section id="category" class="view">{category_view(records, categories)}</section>
<section id="status" class="view">{status_view(records, statuses)}</section>
<section id="cases" class="view">{cases_view(records, categories, statuses)}</section>
</main>
<script>
document.querySelectorAll('.tab').forEach(btn => btn.addEventListener('click', () => {{
  document.querySelectorAll('.tab').forEach(b => b.classList.remove('active'));
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById(btn.dataset.view).classList.add('active');
}}));
function applyFilters() {{
  const cat = document.getElementById('caseCat').value;
  const status = document.getElementById('caseStatus').value;
  const q = document.getElementById('caseSearch').value.toLowerCase();
  document.querySelectorAll('[data-case-row]').forEach(row => {{
    const okCat = !cat || row.dataset.category === cat;
    const okStatus = !status || row.dataset.status === status;
    const okQ = !q || row.dataset.search.includes(q);
    row.style.display = okCat && okStatus && okQ ? '' : 'none';
  }});
}}
document.querySelectorAll('#caseCat,#caseStatus,#caseSearch').forEach(el => el.addEventListener('input', applyFilters));
</script>
</body>
</html>"""


def summary_view(summary: dict[str, Any], records: list[dict[str, Any]]) -> str:
    metrics = [
        ("Total", summary.get("total")),
        ("L2 OK", summary.get("l2_ok")),
        ("L3 Executed", summary.get("l3_executed")),
        ("L3 Partial", summary.get("l3_partial")),
        ("L3 Failed", summary.get("l3_failed")),
    ]
    metric_html = "".join(f'<div class="metric"><span>{esc(k)}</span><b>{esc(v)}</b></div>' for k, v in metrics)
    partial = [r for r in records if r.get("l3_execution_status") != "executed"]
    return f'<div class="grid">{metric_html}</div><div class="panel"><h2>Non-executed or Partial Cases</h2>{case_table(partial)}</div>'


def category_view(records: list[dict[str, Any]], categories: list[str]) -> str:
    rows = []
    for cat in categories:
        subset = [r for r in records if str(r.get("category") or "generalization") == cat]
        counts = Counter(r.get("l3_execution_status") for r in subset)
        rows.append(
            f"<tr><td>{esc(cat)}</td><td>{len(subset)}</td><td>{counts.get('executed',0)}</td>"
            f"<td>{counts.get('partial',0)}</td><td>{len(subset)-counts.get('executed',0)-counts.get('partial',0)}</td></tr>"
        )
    return '<div class="panel"><h2>By Category</h2><table><tr><th>Category</th><th>Total</th><th>Executed</th><th>Partial</th><th>Failed</th></tr>' + "".join(rows) + "</table></div>"


def status_view(records: list[dict[str, Any]], statuses: list[str]) -> str:
    parts = []
    for status in statuses:
        subset = [r for r in records if str(r.get("l3_execution_status")) == status]
        parts.append(f'<div class="panel"><h2>{esc(status)} ({len(subset)})</h2>{case_table(subset)}</div>')
    return "".join(parts)


def cases_view(records: list[dict[str, Any]], categories: list[str], statuses: list[str]) -> str:
    cat_opts = "".join(f'<option value="{esc(c)}">{esc(c)}</option>' for c in categories)
    status_opts = "".join(f'<option value="{esc(s)}">{esc(s)}</option>' for s in statuses)
    items = []
    for r in records:
        search = " ".join(str(r.get(k, "")) for k in ("case_id", "category", "query", "l3_execution_status")).lower()
        items.append(
            f'<div class="panel" data-case-row data-category="{esc(r.get("category") or "generalization")}" '
            f'data-status="{esc(r.get("l3_execution_status"))}" data-search="{esc(search)}">'
            f'<details><summary>{esc(r.get("case_id"))} · {badge(r.get("l3_execution_status"))} · {esc(r.get("query"))}</summary>'
            f'{route_detail(r)}</details></div>'
        )
    return (
        '<div class="filters"><select id="caseCat"><option value="">All categories</option>'
        + cat_opts
        + '</select><select id="caseStatus"><option value="">All statuses</option>'
        + status_opts
        + '</select><input id="caseSearch" placeholder="Search case/query"></div>'
        + "".join(items)
    )


def case_table(records: list[dict[str, Any]]) -> str:
    if not records:
        return '<div style="padding:12px" class="small">No cases.</div>'
    rows = []
    for r in records:
        rows.append(
            f"<tr><td>{esc(r.get('case_id'))}</td><td>{esc(r.get('category') or 'generalization')}</td>"
            f"<td>{badge(r.get('l3_execution_status'))}</td><td>{esc(r.get('l3_executed_route_count'))}/{esc(r.get('l3_skipped_route_count'))}</td>"
            f"<td>{esc(', '.join(r.get('executed_modalities') or []))}</td><td>{esc(r.get('query'))}</td>"
            f"<td>{esc(', '.join(r.get('l3_error_codes') or []))}</td></tr>"
        )
    return "<table><tr><th>Case</th><th>Category</th><th>Status</th><th>Exec/Skip</th><th>Modalities</th><th>Query</th><th>Errors</th></tr>" + "".join(rows) + "</table>"


def route_detail(record: dict[str, Any]) -> str:
    execution = record.get("execution") or {}
    routes = execution.get("executed_routes") or []
    skipped = execution.get("skipped_routes") or []
    blocks = [f'<div class="small" style="padding:0 12px 10px">Executed routes: {len(routes)}; skipped routes: {len(skipped)}</div>']
    for label, route_list in (("Executed", routes), ("Skipped", skipped)):
        for route in route_list:
            row_match = route.get("row_match") or {}
            meta = route.get("route_metadata") or {}
            rows = [
                ("route_id", route.get("route_id")),
                ("status", route.get("status")),
                ("query_type", route.get("query_type")),
                ("modality", route.get("modality")),
                ("cell", route.get("cell")),
                ("n_rows", row_match.get("n_rows")),
                ("cell_role", meta.get("cell_role")),
                ("evidence_level", meta.get("evidence_level")),
                ("pair_search_round", meta.get("pair_search_round")),
                ("pair_search_reason", meta.get("pair_search_reason")),
            ]
            table = "".join(f"<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in rows if v is not None)
            rankings = route.get("rankings") or {}
            preview = ranking_preview(rankings)
            blocks.append(f'<div class="route"><table><tr><th colspan="2">{esc(label)} Route</th></tr>{table}</table>{preview}</div>')
    if execution.get("errors"):
        blocks.append("<pre>" + esc(json.dumps(execution.get("errors"), indent=2, ensure_ascii=False)) + "</pre>")
    return "".join(blocks)


def ranking_preview(rankings: dict[str, Any]) -> str:
    keys = [
        "top_activated",
        "top_suppressed",
        "top_perturbations",
        "top_loss_of_function_perturbations",
        "top_activating_perturbations_inferred",
    ]
    parts = []
    for key in keys:
        vals = rankings.get(key) or []
        if not vals:
            continue
        rows = []
        for item in vals[:5]:
            label = item.get("label") or item.get("cmap_name") or item.get("pert_id") or item.get("term")
            score = item.get("score", item.get("similarity"))
            rows.append(f"<tr><td>{esc(item.get('rank'))}</td><td>{esc(label)}</td><td>{esc(score)}</td></tr>")
        parts.append(f"<table><tr><th colspan='3'>{esc(key)} preview</th></tr><tr><th>Rank</th><th>Label</th><th>Score</th></tr>{''.join(rows)}</table>")
    return "".join(parts)


def badge(status: Any) -> str:
    cls = str(status or "").replace(" ", "_")
    return f'<span class="status {esc(cls)}">{esc(status)}</span>'


def esc(value: Any) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


if __name__ == "__main__":
    main()
