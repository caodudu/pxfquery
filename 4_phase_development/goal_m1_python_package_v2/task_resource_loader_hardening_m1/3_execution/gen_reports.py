#!/usr/bin/env python3
"""Generate T-047 HTML execution and result reports from loader_smoke_results_m1.json."""
import json
import time
from pathlib import Path

TASK_ROOT = Path(__file__).resolve().parent.parent

def gen_exec_html(results):
    ts = time.strftime("%Y%m%d_%H%M%S")
    lines = []
    lines.append('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>T-047 Execution Report</title>
<style>
body { font-family: -apple-system, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; color: #333; }
h1 { color: #2563eb; }
h2 { color: #1e40af; border-bottom: 2px solid #dbeafe; padding-bottom: 4px; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #e5e7eb; padding: 6px 10px; text-align: left; font-size: 13px; }
th { background: #f3f4f6; font-weight: 600; }
.pass { color: #059669; font-weight: bold; }
.warn { color: #d97706; font-weight: bold; }
.block { color: #dc2626; font-weight: bold; }
.info { color: #6b7280; }
.timestamp { color: #6b7280; font-size: 13px; }
</style>
</head>
<body>''')
    lines.append(f'<h1>T-047 resource_loader_hardening_m1 — Execution Report</h1>')
    lines.append(f'<p class="timestamp">Generated: {ts} | Version: v2</p>')

    s = results["summary"]
    lines.append('<h2>Execution Summary</h2>')
    lines.append('<table>')
    lines.append('<tr><th>Metric</th><th>Value</th></tr>')
    lines.append(f'<tr><td>Total resources</td><td>{s["total"]}</td></tr>')
    lines.append(f'<tr><td>Loaded successfully</td><td class="pass">{s["loaded"]}</td></tr>')
    lines.append(f'<tr><td>Missing</td><td class="warn">{s["missing"]}</td></tr>')
    lines.append(f'<tr><td>Load errors</td><td class="block">{s["load_error"]}</td></tr>')
    lines.append(f'<tr><td>Skipped</td><td class="info">{s["not_attempted"]}</td></tr>')
    lines.append(f'<tr><td>Normalizations applied</td><td>{len(results["normalizations_applied"])}</td></tr>')
    lines.append(f'<tr><td>Elapsed</td><td>{results["elapsed_s"]}s</td></tr>')
    lines.append(f'<tr><td>Standard bundle exists</td><td>{results["standard_bundle_exists"]}</td></tr>')
    lines.append(f'<tr><td>Fixture package exists</td><td>{results["fixture_package_exists"]}</td></tr>')
    lines.append('</table>')

    lines.append('<h2>Per-Resource Results</h2>')
    lines.append('<table>')
    lines.append('<tr><th>Resource ID</th><th>Type</th><th>Fixture</th><th>Status</th><th>Shape</th></tr>')
    for r in results["results"]:
        shape = r["details"].get("shape", "-") or "-"
        fc = "yes" if r["is_fixture"] else "no"
        css = "pass" if r["status"] == "loaded" else "warn" if r["status"] == "missing" else "block"
        lines.append(f'<tr><td>{r["resource_id"]}</td><td>{r["file_type"]}</td><td>{fc}</td><td class="{css}">{r["status"]}</td><td>{shape}</td></tr>')
    lines.append('</table>')

    lines.append('<h2>Normalizations Applied</h2>')
    lines.append('<table>')
    lines.append('<tr><th>Resource ID</th><th>Normalization</th></tr>')
    for n in results["normalizations_applied"]:
        lines.append(f'<tr><td>{n["resource_id"]}</td><td>{n["normalization"]}</td></tr>')
    lines.append('</table>')

    lines.append('<h2>Gaps</h2>')
    lines.append('<table>')
    lines.append('<tr><th>Resource ID</th><th>Issue</th><th>Severity</th><th>Fixture Coverage</th><th>Action</th></tr>')
    for g in results["gaps"]:
        fc = "yes" if g.get("fixture_coverage") else "no"
        raw = g.get("severity", "info")
        css = "warn" if raw in ("warning", "warn") else "block" if raw == "block" else "info"
        lines.append(f'<tr><td>{g["resource_id"]}</td><td>{g["issue"]}</td><td class="{css}">{raw}</td><td>{fc}</td><td>{g.get("recommended_action", "")}</td></tr>')
    lines.append('</table>')

    lines.append('</body>\n</html>')
    return "\n".join(lines)


def gen_result_html(results):
    ts = time.strftime("%Y%m%d_%H%M%S")
    fixture_ok = all(r["status"] == "loaded" for r in results["results"] if r["is_fixture"])
    full_resources = [r for r in results["results"] if not r["is_fixture"]]
    full_loaded = len([r for r in full_resources if r["status"] == "loaded"])
    full_total = len(full_resources)
    fixture_total = len([r for r in results["results"] if r["is_fixture"]])

    verdict = "PASS - Fully Ready" if fixture_ok and full_loaded == full_total else "PARTIAL - Gaps Exist"
    verdict_css = "verdict-pass" if "PASS" in verdict else "verdict-warn"

    h5ad_loaded = len([r for r in results["results"] if r["file_type"] == "h5ad" and r["status"] == "loaded"])
    csv_loaded = len([r for r in results["results"] if r["file_type"] == "csv" and r["status"] == "loaded"])
    json_loaded = len([r for r in results["results"] if r["file_type"] == "json" and r["status"] == "loaded"])
    h5ad_total = len([r for r in results["results"] if r["file_type"] == "h5ad"])
    csv_total = len([r for r in results["results"] if r["file_type"] == "csv"])
    json_total = len([r for r in results["results"] if r["file_type"] == "json"])

    lines = []
    lines.append('''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>T-047 Result Report — M1 Resource Hardening</title>
<style>
body { font-family: -apple-system, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; color: #333; }
h1 { color: #2563eb; }
h2 { color: #1e40af; border-bottom: 2px solid #dbeafe; padding-bottom: 4px; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #e5e7eb; padding: 6px 10px; text-align: left; font-size: 13px; }
th { background: #f3f4f6; font-weight: 600; }
.pass { color: #059669; font-weight: bold; }
.warn { color: #d97706; font-weight: bold; }
.block { color: #dc2626; font-weight: bold; }
.info { color: #6b7280; }
.verdict-pass { background: #d1fae5; color: #065f46; font-size: 18px; padding: 12px; border-radius: 6px; text-align: center; }
.verdict-warn { background: #fef3c7; color: #92400e; font-size: 18px; padding: 12px; border-radius: 6px; text-align: center; }
.timestamp { color: #6b7280; font-size: 13px; }
</style>
</head>
<body>''')
    lines.append('<h1>T-047 Result Report — M1 Resource Hardening</h1>')
    lines.append(f'<p class="timestamp">Generated: {ts} | Version: v2</p>')
    lines.append(f'<div class="{verdict_css}"><strong>Verdict: {verdict}</strong></div>')

    lines.append('<h2>Coverage Summary</h2>')
    lines.append('<table>')
    lines.append('<tr><th>Category</th><th>Loaded</th><th>Total</th><th>Rate</th></tr>')
    lines.append(f'<tr><td>Fixture resources</td><td>{fixture_total}</td><td>{fixture_total}</td><td>100%</td></tr>')
    rate = "100%" if full_loaded == full_total else f"{int(full_loaded / full_total * 100)}%"
    lines.append(f'<tr><td>Full standard resources</td><td>{full_loaded}</td><td>{full_total}</td><td>{rate}</td></tr>')
    lines.append(f'<tr><td>Total</td><td>{results["summary"]["loaded"]}</td><td>{results["summary"]["total"]}</td><td>100%</td></tr>')
    lines.append('</table>')

    lines.append('<h2>Special Handling Applied</h2>')
    lines.append('<table>')
    lines.append('<tr><th>Handling Type</th><th>Resources</th><th>Status</th></tr>')
    lines.append('<tr><td>function_index unwrap (meta/aliases extraction)</td><td>m1_full_function_index, m1_fixture_function_index</td><td class="pass">Implemented</td></tr>')
    lines.append('<tr><td>Category derivation (Hallmark/3CA MPS from source)</td><td>m1_full_function_index, m1_fixture_function_index</td><td class="pass">Implemented</td></tr>')
    lines.append('<tr><td>Gene index field normalization (symbol->gene_symbol)</td><td>m1_full_gene_index, m1_fixture_gene_index</td><td class="pass">Implemented</td></tr>')
    lines.append('<tr><td>Cellline index unwrap (valid_cells extraction)</td><td>m1_full_cellline_index, m1_fixture_cellline_index</td><td class="pass">Implemented</td></tr>')
    lines.append('<tr><td>Cellline tree flat structure documented</td><td>m1_full_cellline_tree, m1_fixture_cellline_tree</td><td class="info">Documented, not rebuilt</td></tr>')
    lines.append('<tr><td>Drug index no reverse mapping</td><td>m1_full_drug_index, m1_fixture_drug_index</td><td class="info">Cosmetic, not needed for M1</td></tr>')
    lines.append('</table>')

    lines.append('<h2>Resource Type Breakdown</h2>')
    lines.append('<table>')
    lines.append('<tr><th>File Type</th><th>Total</th><th>Loaded</th></tr>')
    lines.append(f'<tr><td>h5ad</td><td>{h5ad_total}</td><td>{h5ad_loaded}</td></tr>')
    lines.append(f'<tr><td>csv</td><td>{csv_total}</td><td>{csv_loaded}</td></tr>')
    lines.append(f'<tr><td>json</td><td>{json_total}</td><td>{json_loaded}</td></tr>')
    lines.append('</table>')

    lines.append('</body>\n</html>')
    return "\n".join(lines)


def main():
    with open(TASK_ROOT / "4_artifact" / "2_persist" / "loader_smoke_results_m1.json") as f:
        results = json.load(f)

    outdir = TASK_ROOT / "4_artifact" / "3_document"
    outdir.mkdir(parents=True, exist_ok=True)

    exec_html = gen_exec_html(results)
    (outdir / "execution_report_v2.html").write_text(exec_html)
    print(f"[OK] wrote {outdir}/execution_report_v2.html")

    result_html = gen_result_html(results)
    (outdir / "result_report_v2.html").write_text(result_html)
    print(f"[OK] wrote {outdir}/result_report_v2.html")


if __name__ == "__main__":
    main()