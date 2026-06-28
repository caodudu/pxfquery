from __future__ import annotations

import html
import json
import os
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TASK_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = TASK_ROOT / "3_execution" / "03_package_source_v2_l2"
ENV_PATH = TASK_ROOT / ".env"
STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)
OUT_TABLE = TASK_ROOT / "4_artifact" / "5_table"
OUT_DOC = TASK_ROOT / "4_artifact" / "3_document"


QUESTIONS = [
    "In a lung adenocarcinoma context, what broad functional signatures shift after treating with the EGFR inhibitor Tarceva?",
    "For triple negative breast cancer-like cells, what pathways are affected by doxorubicin treatment?",
    "In melanoma models, ask what vemurafenib does to MAPK output and downstream cell-state programs.",
    "For colorectal cancer cells, route the effect of 5-FU on apoptosis and cell-cycle signatures.",
    "In prostate cancer context, what is the functional footprint of enzalutamide exposure?",
    "For ovarian tumor models without naming a cell line, what functional changes follow cisplatin treatment?",
    "In pancreatic cancer, what does gemcitabine do to proliferation and stress-response readouts?",
    "For glioblastoma-like cells, ask what temozolomide changes across hallmark programs.",
    "In liver cancer context, what pathway readouts shift after sorafenib?",
    "For leukemia-like cells, what functions change after imatinib treatment?",
    "In A549, what is the effect of knocking down MALAT1 on apoptosis-related readouts?",
    "For breast cancer cells, suppress estrogen receptor alpha / ESR1 and report functional effects.",
    "In liver tumor models, CRISPR loss of CTNNB1: which signatures change?",
    "For ovarian cancer, knock out BRCA-1 and ask for broad functional consequences.",
    "In glioma-like cells, RNAi against IDH1: what pathways or states are altered?",
    "In melanoma, perturb BRAF and ask what functional programs respond.",
    "For pancreatic cancer, knock down KRAS and report pathway-level output.",
    "In prostate cancer, overexpress MYC and ask for cell-cycle and growth signatures.",
    "For lung cancer, suppress EGFR and ask for downstream functional effects.",
    "In colon cancer context, knock down beta catenin / CTNNB1 and ask what states shift.",
    "Which compounds in breast cancer context may increase programmed cell death and reduce cycling?",
    "Find drugs in lung cancer models that suppress MYC targets and proliferation-like programs.",
    "In ovarian cancer, which treatments could increase DNA damage or repair stress signatures?",
    "For melanoma, search compounds that reduce MAPK or growth-factor signaling output.",
    "In glioblastoma context, which drugs may increase differentiation-like state and lower division?",
    "Which genetic perturbations in breast cancer could increase apoptosis?",
    "In liver cancer, find knockdowns that suppress beta-catenin or Wnt-like output.",
    "For ovarian cancer, find RNAi perturbations that decrease DNA repair programs.",
    "In neural tumor context, which gene perturbations increase differentiation and reduce cycling?",
    "In pancreatic cancer, what gene KOs would reduce KRAS pathway output?",
    "For immune-like tumor states, which shRNA perturbations activate interferon response signatures?",
    "Find genetic perturbations in melanoma that reduce epithelial-mesenchymal or invasive programs.",
    "Which genes, when suppressed in prostate cancer, may reduce androgen response?",
    "In leukemia-like context, find genetic perturbations that decrease MYC/E2F target programs.",
    "In lung cancer cells, which overexpression perturbations might increase hypoxia-like signatures?",
    "For a noncoding RNA query in lung cancer, route MALAT1 perturbation even if direct data are sparse.",
    "In breast cancer context, query NEAT1 knockdown and ask for broad pathway consequences.",
    "For liver tumor models, ask about H19 lncRNA perturbation and available proxy evidence.",
    "In glioma-like cells, ask whether XIST perturbation can be routed to functional programs.",
    "For ovarian cancer, query miR-21 perturbation and route available gene/proxy evidence.",
    "In A375 melanoma, what functional effects follow BRD-K style compound BRD-K81418486?",
    "For MCF7, what pathway readouts shift after tamoxifen or an estrogen receptor antagonist?",
    "In HEPG2, what changes after knocking down TP53?",
    "For HCC827, ask what gefitinib does to apoptosis and growth-factor signaling.",
    "In PC3 prostate cancer cells, what functions change after suppressing AR?",
    "For SKOV3-like ovarian cells, route paclitaxel functional effects.",
    "In K562 leukemia, what signatures change after BCR-ABL inhibition?",
    "For U87-like glioma cells, ask about EGFR inhibition and broad pathway outputs.",
    "In a vague epithelial tumor context, what drugs could raise apoptosis while lowering E2F targets?",
    "In a vague carcinoma context, what gene knockdowns could reduce inflammatory response and proliferation?",
]


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
    from pxfquery.l1_intent import OFFICIAL_DEEPSEEK_BASE_URL, OFFICIAL_DEEPSEEK_MODEL

    token = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("PXFQUERY_LLM_API_KEY")
    if not token:
        raise SystemExit("50题泛化验证需要真实 DeepSeek key；未配置时拒绝生成通过报告。")
    base_url = os.environ.get("PXFQUERY_LLM_BASE_URL") or os.environ.get("DEEPSEEK_API_BASE", OFFICIAL_DEEPSEEK_BASE_URL)
    model = os.environ.get("PXFQUERY_LLM_MODEL", OFFICIAL_DEEPSEEK_MODEL)
    max_workers = int(os.environ.get("PXFQUERY_VALIDATION_WORKERS", "8"))

    def run_one(index_and_question: tuple[int, str]) -> tuple[int, dict[str, Any]]:
        index, question = index_and_question
        pxf = PxFQuery()
        pxf.settings.register_llm_provider(token=token, base_url=base_url, model=model, timeout=90, max_network_attempts=4)
        pxf.resources.use(STANDARD_RESOURCES)
        qdata = pxf.read.query(question)
        try:
            pxf.pp.parse(qdata)
            pxf.pp.route(qdata)
            route = pxf.get.route(qdata)
            checks = _checks(route)
            ok = all(checks.values())
            return index, {
                "case_id": f"G{index:02d}",
                "query": question,
                "ok": ok,
                "checks": checks,
                "intent": qdata.uns["intent"],
                "route_status": route["route_status"],
                "route": route,
            }
        except Exception as exc:
            return index, {
                "case_id": f"G{index:02d}",
                "query": question,
                "ok": False,
                "checks": {"no_exception": False},
                "route_status": "exception",
                "error": f"{type(exc).__name__}: {exc}",
            }

    records_by_index: list[dict[str, Any] | None] = [None] * len(QUESTIONS)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_one, item) for item in enumerate(QUESTIONS, 1)]
        for future in as_completed(futures):
            index, record = future.result()
            records_by_index[index - 1] = record
            print(f"completed {index:02d}/{len(QUESTIONS)} {record['case_id']} ok={record['ok']} status={record['route_status']}", flush=True)
    records = [record for record in records_by_index if record is not None]

    result = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": {"base_url": base_url, "model": model},
        "resource_dir": str(STANDARD_RESOURCES),
        "parallel_workers": max_workers,
        "total": len(records),
        "passed": sum(1 for r in records if r["ok"]),
        "failed": sum(1 for r in records if not r["ok"]),
        "summary": _summary(records),
        "records": records,
    }
    OUT_TABLE.mkdir(parents=True, exist_ok=True)
    OUT_DOC.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = OUT_TABLE / f"generalization_50_l1_l2_validation_{stamp}.json"
    html_path = OUT_DOC / f"generalization_50_l1_l2_validation_{stamp}.html"
    latest_json = OUT_TABLE / "generalization_50_l1_l2_validation_latest.json"
    latest_html = OUT_DOC / "generalization_50_l1_l2_validation_latest.html"
    text = json.dumps(result, ensure_ascii=False, indent=2)
    json_path.write_text(text, encoding="utf-8")
    latest_json.write_text(text, encoding="utf-8")
    page = _html_report(result)
    html_path.write_text(page, encoding="utf-8")
    latest_html.write_text(page, encoding="utf-8")
    print(json_path)
    print(html_path)
    print(f"passed={result['passed']} failed={result['failed']}")
    if result["failed"]:
        raise SystemExit("50题泛化 L1+L2 验证存在失败，请查看 HTML/JSON 报告。")
    return 0


def _checks(route: dict[str, Any]) -> dict[str, bool]:
    intent = route.get("intent", {})
    llm_calls = route.get("llm_calls", [])
    status = route.get("route_status")
    function_route = route.get("function_route", {})
    no_filter_mode = function_route.get("mode") in {
        "forward-result-scope-no-function-filter",
        "forward-operation-no-function-filter",
    }
    checks = {
        "no_exception": True,
        "resource_indexes_available": bool(route.get("resource_status", {}).get("available")),
        "route_status_terminal": status in {"routed", "no_pair_available", "needs-intent-completion"},
        "no_unvalidated_llm": all(call.get("validated") is True for call in llm_calls),
        "has_handoff_payload_or_intent_completion": bool(route.get("handoff_payload")) or status == "needs-intent-completion",
        "observed_availability_checked": _observed_availability_checked(route),
        "candidate_limits_respected": _limits_respected(route),
    }
    if status != "needs-intent-completion":
        checks["has_combination_candidates"] = bool(route.get("combination_route", {}).get("route_candidates"))
    if intent.get("bio_context") and status != "needs-intent-completion":
        checks["cell_routed"] = bool(route.get("cell_route", {}).get("candidates") or route.get("cell_route", {}).get("selected"))
    if intent.get("query_type") == "forward" and status != "needs-intent-completion":
        checks["perturbation_routed"] = bool(route.get("perturbation_route", {}).get("selected") or route.get("perturbation_route", {}).get("proxies"))
    if (intent.get("function_desc") or intent.get("activate") or intent.get("suppress") or intent.get("query_type") == "reverse") and status != "needs-intent-completion":
        checks["function_routed_or_explicit_no_filter"] = bool(
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


def _observed_availability_checked(route: dict[str, Any]) -> bool:
    combo = route.get("combination_route", {})
    if combo.get("pair_policy") not in {"observed", "observed_cell_scope"}:
        return True
    availability = combo.get("pair_availability", {})
    return availability.get("status") == "checked_l3_obs_min" and availability.get("any_available") is True


def _summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    by_status = Counter(r["route_status"] for r in records)
    failed = [r["case_id"] for r in records if not r["ok"]]
    return {"by_route_status": dict(by_status), "failed_case_ids": failed}


def _html_report(result: dict[str, Any]) -> str:
    rows = []
    for record in result["records"]:
        route = record.get("route", {})
        checks = " ".join(
            f"<span class='{ 'good' if ok else 'bad' }'>{html.escape(k)}: {'PASS' if ok else 'FAIL'}</span>"
            for k, ok in record.get("checks", {}).items()
        )
        llm = "<br>".join(
            html.escape(f"{c.get('stage')} / {c.get('status')} / {c.get('model')} / temp={c.get('temperature')} / validated={c.get('validated')}")
            for c in route.get("llm_calls", [])
        ) or "None"
        rows.append(
            f"""
<article class="case">
  <div class="case-head"><strong>{html.escape(record['case_id'])}</strong><span class="{ 'pass' if record['ok'] else 'fail' }">{'PASS' if record['ok'] else 'FAIL'}</span></div>
  <p>{html.escape(record['query'])}</p>
  <div class="grid">
    <section><h3>Checks</h3><div class="checks">{checks}</div><p><b>Status:</b> {html.escape(record.get('route_status',''))}</p></section>
    <section><h3>L1 Intent</h3><pre>{html.escape(json.dumps(record.get('intent', {}), ensure_ascii=False, indent=2))}</pre></section>
    <section><h3>Selected Route</h3><pre>{html.escape(json.dumps(route.get('selected_route', {}), ensure_ascii=False, indent=2))}</pre></section>
    <section><h3>LLM Calls</h3><p>{llm}</p></section>
  </div>
  <pre>{html.escape(record.get('error', ''))}</pre>
</article>
"""
        )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>T138 Generalization 50 L1+L2 Validation</title>
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
<header><h1>T138 Generalization 50 L1+L2 Validation</h1><div>Generated: {html.escape(result['generated_at'])}</div></header>
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
