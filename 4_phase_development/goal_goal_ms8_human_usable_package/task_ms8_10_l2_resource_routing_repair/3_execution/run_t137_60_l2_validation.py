from __future__ import annotations

import html
import json
import os
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TASK_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = TASK_ROOT / "3_execution" / "03_package_source_v2_l2"
ENV_PATH = TASK_ROOT / ".env"
T137_JSON = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_goal_ms8_human_usable_package/"
    "task_ms8_09_l1_real_llm_gate_repair/4_artifact/5_table/l1_complex_intent_eval_20260627_183235.json"
)
STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)
OUT_TABLE = TASK_ROOT / "4_artifact" / "5_table"
OUT_DOC = TASK_ROOT / "4_artifact" / "3_document"


def _load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def main() -> int:
    _load_env_file(ENV_PATH)
    sys.path.insert(0, str(PACKAGE_ROOT / "src"))
    from pxfquery import PxFQuery
    from pxfquery.l1_intent import OFFICIAL_DEEPSEEK_BASE_URL, OFFICIAL_DEEPSEEK_MODEL, QueryIntent

    token = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("PXFQUERY_LLM_API_KEY")
    if not token:
        raise SystemExit("T137 60题 L2 验证需要真实 DeepSeek key；未配置时拒绝生成报告。")
    base_url = os.environ.get("PXFQUERY_LLM_BASE_URL") or os.environ.get("DEEPSEEK_API_BASE", OFFICIAL_DEEPSEEK_BASE_URL)
    model = os.environ.get("PXFQUERY_LLM_MODEL", OFFICIAL_DEEPSEEK_MODEL)

    payload = json.loads(T137_JSON.read_text(encoding="utf-8"))
    records = payload["records"]
    if len(records) != 60:
        raise SystemExit(f"期望 T137 60 题，实际 {len(records)}")

    pxf = PxFQuery()
    pxf.settings.register_llm_provider(token=token, base_url=base_url, model=model, timeout=90, max_network_attempts=4)
    pxf.resources.use(STANDARD_RESOURCES)

    out_records = []
    for record in records:
        intent = _intent_from_record(record)
        qdata = pxf.read.query(record["query"])
        qdata.uns["_intent"] = intent
        qdata.uns["intent"] = intent.to_dict()
        try:
            pxf.pp.route(qdata)
            route = pxf.get.route(qdata)
            checks = _checks(route, record)
            ok = all(checks.values())
            out_records.append({**record, "l2_ok": ok, "l2_checks": checks, "route_status": route["route_status"], "route": route})
        except Exception as exc:
            out_records.append({**record, "l2_ok": False, "l2_checks": {"exception": False}, "route_status": "exception", "route_error": f"{type(exc).__name__}: {exc}"})

    summary = _summary(out_records)
    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_l1_report": str(T137_JSON),
        "resource_dir": str(STANDARD_RESOURCES),
        "provider": {"base_url": base_url, "model": model},
        "total": len(out_records),
        "passed": sum(1 for r in out_records if r["l2_ok"]),
        "failed": sum(1 for r in out_records if not r["l2_ok"]),
        "summary": summary,
        "records": out_records,
    }

    OUT_TABLE.mkdir(parents=True, exist_ok=True)
    OUT_DOC.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = OUT_TABLE / f"t137_60_l2_validation_{stamp}.json"
    html_path = OUT_DOC / f"t137_60_l2_validation_{stamp}.html"
    latest_html = OUT_DOC / "t137_60_l2_validation_latest.html"
    latest_json = OUT_TABLE / "t137_60_l2_validation_latest.json"
    json_text = json.dumps(result, ensure_ascii=False, indent=2)
    json_path.write_text(json_text, encoding="utf-8")
    latest_json.write_text(json_text, encoding="utf-8")
    html_text = _html_report(result)
    html_path.write_text(html_text, encoding="utf-8")
    latest_html.write_text(html_text, encoding="utf-8")
    print(json_path)
    print(html_path)
    print(f"passed={result['passed']} failed={result['failed']}")
    if result["failed"]:
        raise SystemExit("T137 60题 L2 验证存在失败，请查看 HTML/JSON 报告。")
    return 0


def _intent_from_record(record: dict[str, Any]):
    from pxfquery.l1_intent import QueryIntent

    data = {
        "raw_query": record["query"],
        "normalized_query": record["query"],
        **record["intent"],
        "extracted_phrases": {},
        "parse_confidence": 1.0,
        "parse_method": "t137_real_llm_replay",
        "provider_evidence": record.get("provider_evidence", {}),
    }
    return QueryIntent(**data)


def _checks(route: dict[str, Any], record: dict[str, Any]) -> dict[str, bool]:
    status = route.get("route_status")
    llm_calls = route.get("llm_calls", [])
    intent = route.get("intent", {})
    checks = {
        "resource_indexes_available": bool(route.get("resource_status", {}).get("available")),
        "route_status_terminal": status in {"routed", "no_pair_available"},
        "no_unvalidated_llm": all(call.get("validated") is True for call in llm_calls),
        "has_handoff_payload": bool(route.get("handoff_payload")),
        "has_combination_candidates": bool(route.get("combination_route", {}).get("route_candidates")),
        "candidate_limits_respected": _limits_respected(route),
    }
    if intent.get("bio_context"):
        checks["cell_routed"] = bool(route.get("cell_route", {}).get("candidates") or route.get("cell_route", {}).get("selected"))
    if intent.get("query_type") == "forward":
        checks["perturbation_routed"] = bool(route.get("perturbation_route", {}).get("selected") or route.get("perturbation_route", {}).get("proxies"))
    if intent.get("function_desc") or intent.get("activate") or intent.get("suppress") or intent.get("query_type") == "reverse":
        function_route = route.get("function_route", {})
        no_filter_mode = function_route.get("mode") in {
            "forward-result-scope-no-function-filter",
            "forward-operation-no-function-filter",
        }
        checks["function_routed"] = bool(
            function_route.get("selected")
            or function_route.get("interpretation_sets")
            or (intent.get("query_type") == "forward" and no_filter_mode and function_route.get("status") == "resolved")
        )
    return checks


def _limits_respected(route: dict[str, Any]) -> bool:
    combo = route.get("combination_route", {})
    return (
        len(route.get("cell_route", {}).get("candidates", [])) <= 6
        and len(route.get("perturbation_route", {}).get("proxies", [])) <= 5
        and len(route.get("function_route", {}).get("selected", [])) <= 5
        and len(combo.get("route_candidates", [])) <= 25
        and len(combo.get("selected_routes", [])) <= 3
    )


def _summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_category: dict[str, Counter] = defaultdict(Counter)
    by_status = Counter()
    failed_ids = []
    for record in records:
        by_category[record["category"]]["total"] += 1
        by_category[record["category"]]["passed" if record["l2_ok"] else "failed"] += 1
        by_status[record["route_status"]] += 1
        if not record["l2_ok"]:
            failed_ids.append(record["case_id"])
    return {
        "by_category": {k: dict(v) for k, v in sorted(by_category.items())},
        "by_route_status": dict(by_status),
        "failed_case_ids": failed_ids,
    }


def _html_report(result: dict[str, Any]) -> str:
    rows = []
    for record in result["records"]:
        route = record.get("route", {})
        checks = " ".join(
            f"<span class='{ 'good' if ok else 'bad' }'>{html.escape(k)}: {'PASS' if ok else 'FAIL'}</span>"
            for k, ok in record.get("l2_checks", {}).items()
        )
        llm = "<br>".join(
            html.escape(f"{c.get('stage')} / {c.get('status')} / {c.get('model')} / temp={c.get('temperature')} / validated={c.get('validated')}")
            for c in route.get("llm_calls", [])
        ) or "None"
        selected = html.escape(json.dumps(route.get("selected_route", {}), ensure_ascii=False, indent=2))
        function_route = html.escape(json.dumps(route.get("function_route", {}), ensure_ascii=False, indent=2))
        combo_route = route.get("combination_route", {})
        convergence = html.escape(json.dumps(route.get("function_route", {}).get("reverse_mapping_convergence"), ensure_ascii=False, indent=2))
        unresolved = html.escape(json.dumps(route.get("unresolved_dimensions", []), ensure_ascii=False))
        rows.append(
            f"""
<article class="case" data-ok="{str(record['l2_ok']).lower()}" data-category="{html.escape(record['category'])}">
  <div class="case-head"><strong>{html.escape(record['case_id'])} · {html.escape(record['category'])}</strong><span class="{ 'pass' if record['l2_ok'] else 'fail' }">{'PASS' if record['l2_ok'] else 'FAIL'}</span></div>
  <div class="question">{html.escape(record['query'])}</div>
  <div class="grid">
    <section><h3>L1 Intent</h3><pre>{html.escape(json.dumps(record['intent'], ensure_ascii=False, indent=2))}</pre></section>
    <section><h3>L2 Checks</h3><div class="checks">{checks}</div><p><b>Status:</b> {html.escape(record.get('route_status',''))}</p><p><b>Unresolved:</b> <code>{unresolved}</code></p></section>
    <section><h3>Selected Route</h3><pre>{selected}</pre></section>
    <section><h3>Function Route</h3><pre>{function_route}</pre><p><b>Reverse convergence:</b></p><pre>{convergence}</pre></section>
    <section><h3>LLM Calls</h3><p>{llm}</p></section>
    <section><h3>Combination</h3><pre>{html.escape(json.dumps({'status': combo_route.get('status'), 'candidate_limits': combo_route.get('candidate_limits'), 'selected_routes': combo_route.get('selected_routes')}, ensure_ascii=False, indent=2))}</pre></section>
  </div>
</article>
"""
        )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>T138 L2 over T137 60 Questions</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin:0; background:#f7f7f5; color:#1f2328; }}
header {{ padding:24px 36px; background:#263238; color:white; }}
main {{ padding:24px 36px; }}
.summary {{ display:grid; grid-template-columns: repeat(4,minmax(140px,1fr)); gap:12px; margin-bottom:20px; }}
.card,.case {{ background:white; border:1px solid #d7d9dc; border-radius:6px; padding:14px 16px; }}
.case {{ margin:14px 0; }}
.case-head {{ display:flex; justify-content:space-between; border-bottom:1px solid #eee; padding-bottom:8px; margin-bottom:10px; }}
.pass,.good {{ color:#116329; }}
.fail,.bad {{ color:#b42318; }}
.grid {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
pre {{ white-space:pre-wrap; background:#f6f8fa; padding:10px; border-radius:6px; overflow:auto; }}
.checks span {{ display:inline-block; margin:3px 6px 3px 0; padding:3px 7px; border-radius:999px; background:#eef2f5; font-size:12px; }}
</style></head><body>
<header><h1>T138 L2 over T137 60 Questions</h1><div>Generated: {html.escape(result['generated_at'])}</div></header>
<main>
<section class="summary">
<div class="card"><h3>Total</h3><p>{result['total']}</p></div>
<div class="card"><h3>Passed</h3><p class="pass">{result['passed']}</p></div>
<div class="card"><h3>Failed</h3><p class="fail">{result['failed']}</p></div>
<div class="card"><h3>Model</h3><p>{html.escape(result['provider']['model'])}</p></div>
</section>
<pre>{html.escape(json.dumps(result['summary'], ensure_ascii=False, indent=2))}</pre>
{''.join(rows)}
</main></body></html>"""


if __name__ == "__main__":
    raise SystemExit(main())
