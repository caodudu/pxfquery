from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TASK_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = TASK_ROOT / "3_execution" / "03_package_source_v2_l2"
STANDARD_RESOURCES = Path(
    "/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/"
    "goal_precomputed_data_exploration/task_standard_resources_optimal_formats/"
    "4_artifact/2_persist/standard_resources"
)
REPORT_DIR = TASK_ROOT / "4_artifact" / "2_persist" / "l2_real_llm_validation"
ENV_PATH = TASK_ROOT / ".env"


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
        raise SystemExit("真实 LLM 验证需要 DEEPSEEK_API_KEY 或 PXFQUERY_LLM_API_KEY；未设置时拒绝生成通过报告。")

    base_url = os.environ.get("PXFQUERY_LLM_BASE_URL") or os.environ.get("DEEPSEEK_API_BASE", OFFICIAL_DEEPSEEK_BASE_URL)
    model = os.environ.get("PXFQUERY_LLM_MODEL", OFFICIAL_DEEPSEEK_MODEL)
    if model != "deepseek-v4-flash":
        raise SystemExit(f"本验证要求 deepseek-v4-flash，当前模型是 {model!r}")
    if not STANDARD_RESOURCES.exists():
        raise SystemExit(f"标准资源目录不存在：{STANDARD_RESOURCES}")

    pxf = PxFQuery()
    pxf.settings.register_llm_provider(token=token, base_url=base_url, model=model, timeout=90, max_network_attempts=2)
    pxf.resources.use(STANDARD_RESOURCES)

    scenarios = [
        {
            "id": "S1_exact_cell_noncoding_gene_function",
            "purpose": "exact A549 + exact MALAT1 lncRNA + exact apoptosis；验证非编码基因 proxy 不是占位。",
            "intent": _intent(query_type="forward", bio_context="A549", pert_desc="MALAT1", pert_class="genetic", function_desc="apoptosis"),
            "expect": ["cell_resolved", "gene_malat1_lnrna", "function_apoptosis"],
        },
        {
            "id": "S2_llm_cell_tree_context",
            "purpose": "模糊细胞语境进入真实 LLM cell tree selection。",
            "intent": _intent(query_type="forward", bio_context="non-small cell lung cancer", pert_desc="MALAT1", pert_class="genetic", function_desc="apoptosis"),
            "expect": ["cell_llm_call_ok", "cell_candidates_limited"],
        },
        {
            "id": "S3_llm_drug_typo_normalization",
            "purpose": "药物 typo 先召回 top candidates，再由真实 LLM 选择/假设并回索引校验。",
            "intent": _intent(query_type="forward", bio_context="A549", pert_desc="erlotnib", pert_class="drug", function_desc="apoptosis"),
            "expect": ["drug_llm_call_ok", "drug_resolved"],
        },
        {
            "id": "S4_llm_gene_descriptive_normalization",
            "purpose": "描述性基因名不直接匹配索引时，由真实 LLM 规范化后回索引校验。",
            "intent": _intent(query_type="forward", bio_context="A549", pert_desc="tumor protein p53", pert_class="genetic", function_desc="apoptosis"),
            "expect": ["gene_llm_call_ok", "gene_resolved"],
        },
        {
            "id": "S5_llm_forward_function_mapping",
            "purpose": "模糊功能词由真实 LLM 从固定 91 项 function_index 中选择，不能自由生成。",
            "intent": _intent(query_type="forward", bio_context="A549", pert_desc="MALAT1", pert_class="genetic", function_desc="invasive mesenchymal transition"),
            "expect": ["function_llm_call_ok", "function_resolved"],
        },
        {
            "id": "S6_llm_reverse_three_pass_function_mapping",
            "purpose": "反向查询对模糊功能做三次独立真实 LLM 映射，每次结果都必须回 91 项索引校验。",
            "intent": _intent(query_type="reverse", bio_context="breast cancer", function_desc="more epithelial differentiation and less cell cycling", pert_class="drug"),
            "expect": ["reverse_three_sets", "reverse_llm_calls_ok", "reverse_convergence_recorded"],
        },
    ]

    results = []
    failures = []
    for scenario in scenarios:
        qdata = pxf.read.query(scenario["purpose"])
        qdata.uns["_intent"] = scenario["intent"]
        qdata.uns["intent"] = scenario["intent"].to_dict()
        try:
            pxf.pp.route(qdata)
            route = pxf.get.route(qdata)
            checks = _checks(route)
            ok = all(checks.get(name) for name in scenario["expect"])
            result = {
                "id": scenario["id"],
                "purpose": scenario["purpose"],
                "ok": ok,
                "expected_checks": scenario["expect"],
                "checks": checks,
                "route_status": route["route_status"],
                "route": route,
            }
        except Exception as exc:
            ok = False
            result = {"id": scenario["id"], "purpose": scenario["purpose"], "ok": False, "error": f"{type(exc).__name__}: {exc}"}
        results.append(result)
        if not ok:
            failures.append(result["id"])

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "provider": {"base_url": base_url, "model": model},
        "resource_dir": str(STANDARD_RESOURCES),
        "all_passed": not failures,
        "failures": failures,
        "results": results,
    }
    json_path = REPORT_DIR / "l2_real_llm_validation_report.json"
    md_path = REPORT_DIR / "l2_real_llm_validation_report_zh.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_markdown_report(payload), encoding="utf-8")
    print(json_path)
    print(md_path)
    if failures:
        raise SystemExit(f"L2 真实 LLM 验证失败：{', '.join(failures)}")
    return 0


def _intent(**kwargs: Any):
    from pxfquery.l1_intent import QueryIntent

    data = {
        "raw_query": "validation intent",
        "normalized_query": "validation intent",
        "query_type": "forward",
        "bio_context": None,
        "pert_desc": None,
        "pert_class": None,
        "genetic_modality": None,
        "function_desc": None,
        "activate": [],
        "suppress": [],
        "top_n": None,
    }
    data.update(kwargs)
    return QueryIntent(**data)


def _checks(route: dict[str, Any]) -> dict[str, bool]:
    llm_calls = route.get("llm_calls", [])
    call_stages = {c.get("stage"): c for c in llm_calls}
    perturb = route.get("perturbation_route", {})
    function = route.get("function_route", {})
    cell = route.get("cell_route", {})
    return {
        "cell_resolved": bool(cell.get("selected")),
        "cell_llm_call_ok": any(str(k).startswith("cell_tree_") and v.get("status") == "ok" for k, v in call_stages.items()),
        "cell_candidates_limited": len(cell.get("candidates", [])) <= 6,
        "gene_malat1_lnrna": (perturb.get("selected") or [{}])[0].get("symbol") == "MALAT1" and (perturb.get("selected") or [{}])[0].get("gene_type") == "lncRNA",
        "gene_llm_call_ok": call_stages.get("gene_normalization", {}).get("status") == "ok",
        "gene_resolved": bool(perturb.get("selected")),
        "drug_llm_call_ok": call_stages.get("drug_normalization", {}).get("status") == "ok",
        "drug_resolved": bool(perturb.get("selected")),
        "function_apoptosis": any(x.get("var_name") == "HALLMARK_APOPTOSIS" for x in function.get("selected", [])),
        "function_llm_call_ok": call_stages.get("function_mapping", {}).get("status") == "ok",
        "function_resolved": bool(function.get("selected")),
        "reverse_three_sets": len(function.get("interpretation_sets", [])) == 3,
        "reverse_llm_calls_ok": sum(1 for c in llm_calls if str(c.get("stage", "")).startswith("function_reverse_mapping_") and c.get("status") == "ok") == 3,
        "reverse_convergence_recorded": _reverse_convergence(function) in {"complete_convergence", "partial_divergence", "complete_divergence"},
    }


def _markdown_report(payload: dict[str, Any]) -> str:
    lines = [
        "# T138 L2 真实 LLM 路由验证报告",
        "",
        f"- 生成时间：{payload['generated_at']}",
        f"- 模型：{payload['provider']['model']}",
        f"- Base URL：{payload['provider']['base_url']}",
        f"- 资源目录：`{payload['resource_dir']}`",
        f"- 总结果：{'通过' if payload['all_passed'] else '失败'}",
        "",
        "## 场景结果",
    ]
    for result in payload["results"]:
        lines.extend(
            [
                "",
                f"### {result['id']}",
                f"- 目的：{result['purpose']}",
                f"- 结果：{'通过' if result.get('ok') else '失败'}",
                f"- route_status：{result.get('route_status', 'NA')}",
            ]
        )
        if "error" in result:
            lines.append(f"- 错误：`{result['error']}`")
            continue
        lines.append("- 检查项：")
        for key in result["expected_checks"]:
            lines.append(f"  - {key}: {result['checks'].get(key)}")
        route = result["route"]
        lines.append("- LLM 调用：")
        for call in route.get("llm_calls", []):
            lines.append(
                f"  - {call.get('stage')} / {call.get('status')} / "
                f"{call.get('provider')} / {call.get('model')} / temp={call.get('temperature')} / hash={call.get('parsed_json_hash')}"
            )
        lines.append("- 路由摘要：")
        lines.append(f"  - cell: {route.get('cell_route', {}).get('selected')} candidates={len(route.get('cell_route', {}).get('candidates', []))}")
        lines.append(f"  - perturbation: {route.get('perturbation_route', {}).get('selected')}")
        lines.append(f"  - function: {route.get('function_route', {}).get('selected')}")
        if route.get("function_route", {}).get("interpretation_sets"):
            lines.append(f"  - reverse interpretation sets: {len(route['function_route']['interpretation_sets'])}")
            lines.append(f"  - reverse convergence: {_reverse_convergence(route['function_route'])}")
    lines.append("")
    return "\n".join(lines)


def _reverse_convergence(function_route: dict[str, Any]) -> str:
    sets = function_route.get("interpretation_sets", [])
    if not sets:
        return "not_applicable"
    signatures = {
        tuple(f.get("var_name") for f in item.get("functions", []))
        for item in sets
    }
    if len(signatures) == 1:
        return "complete_convergence"
    if len(signatures) == len(sets):
        return "complete_divergence"
    return "partial_divergence"


if __name__ == "__main__":
    raise SystemExit(main())
