from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path


def _load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


QUESTION_BANK = [
    ("Q1_exact_gene_cell", "In A549, what pathways are affected by EGFR knockdown?"),
    ("Q2_disease_not_cellname", "In non-small cell lung carcinoma, what happens if EGFR is suppressed?"),
    ("Q3_unknown_cell_label", "For NCI-H358-like NSCLC context, what pathways change after EGFR knockdown?"),
    ("Q4_gene_alias_style", "In A549, what functional changes follow ErbB1 knockdown?"),
    ("Q5_generic_drug_desc", "In A549, what pathways are affected by an EGFR inhibitor?"),
    ("Q6_specific_drug_name", "In A549, what pathways change after erlotinib treatment?"),
    ("Q7_breast_context", "In triple-negative breast cancer context, what pathways are altered by KRAS perturbation?"),
    ("Q8_colorectal_context", "In colorectal adenocarcinoma context, what happens when MYC is perturbed?"),
    ("Q9_unknown_cell_and_disease", "In pancreatic neuroendocrine tumor context, what changes after KRAS perturbation?"),
    ("Q10_nonexistent_cell", "In MCLF1234 cells, what pathways are changed by EGFR knockdown?"),
    ("Q11_rare_gene_proxy", "In HCC1954, report pathway impact for perturbing GPRC5D."),
    ("Q12_nonexistent_gene", "In MCF7, what pathways change after perturbing FAKEGENE999?"),
    ("Q13_nonexistent_drug", "In PC3, estimate pathway response for l-theanine-like perturbation."),
    ("Q14_noisy_input", "A549 + EGFR KD, tell me key activated/suppressed programs."),
]


def _build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run forward resolver question suite with timing diagnostics.")
    p.add_argument("--provider", default="minimax", choices=["minimax", "siliconflow", "mock"])
    p.add_argument("--model", default=None)
    p.add_argument("--limit", type=int, default=3, help="How many questions to run from the suite head.")
    p.add_argument("--ids", nargs="*", default=None, help="Run only selected question IDs.")
    p.add_argument("--top-n", type=int, default=10)
    p.add_argument("--no-summary", action="store_true", help="Skip summary generation to reduce latency/cost.")
    p.add_argument("--output-tag", default=None, help="Optional suffix for output file names.")
    p.add_argument("--resolver-mode", default="always_llm", choices=["always_llm", "hybrid_fast"])
    return p


def _select_queries(limit: int, ids: list[str] | None):
    if ids:
        idset = set(ids)
        chosen = [x for x in QUESTION_BANK if x[0] in idset]
        return chosen
    return QUESTION_BANK[: max(0, limit)]


def main() -> int:
    args = _build_arg_parser().parse_args()
    workspace = Path(__file__).resolve().parents[3]
    if str(workspace / "script") not in sys.path:
        sys.path.insert(0, str(workspace / "script"))
    _load_env(workspace / ".env")

    from PxFquery import PxFquery

    pxf = PxFquery()
    pxf.load_data_dir(str(workspace / "output/store/gsea_anndata"))
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider=args.provider,
        model=args.model or os.getenv("MINIMAX_MODEL", "MiniMax-M2.7"),
        summary_include_numbers=False,
        use_fast_path=(args.resolver_mode == "hybrid_fast"),
    )

    queries = _select_queries(args.limit, args.ids)
    if not queries:
        raise ValueError("No queries selected. Check --limit/--ids.")

    resolver = getattr(pxf, "_resolver", None)
    prompt_timing_total: dict[str, dict[str, float]] = {}
    if resolver is not None and hasattr(resolver, "_call_prompt"):
        original_call_prompt = resolver._call_prompt

        def _timed_call_prompt(name: str, *f_args, **f_kwargs):
            t0 = time.perf_counter()
            out = original_call_prompt(name, *f_args, **f_kwargs)
            dt = time.perf_counter() - t0
            item = prompt_timing_total.setdefault(name, {"count": 0.0, "seconds": 0.0})
            item["count"] += 1.0
            item["seconds"] += dt
            return out

        resolver._call_prompt = _timed_call_prompt

    rows = []
    suite_t0 = time.perf_counter()
    for qid, qtext in queries:
        before = {k: v.copy() for k, v in prompt_timing_total.items()}
        t0 = time.perf_counter()
        if args.no_summary and resolver is not None:
            res = resolver.resolve_and_query(
                user_input=qtext,
                top_n=args.top_n,
                summarize=False,
            )
        else:
            res = pxf.query(qtext, top_n=args.top_n)
        elapsed = time.perf_counter() - t0
        per_query_prompt = {}
        keys = set(before.keys()) | set(prompt_timing_total.keys())
        for k in sorted(keys):
            b = before.get(k, {"count": 0.0, "seconds": 0.0})
            a = prompt_timing_total.get(k, {"count": 0.0, "seconds": 0.0})
            dc = a["count"] - b["count"]
            ds = a["seconds"] - b["seconds"]
            if dc > 0 or ds > 0:
                per_query_prompt[k] = {"count": int(dc), "seconds": round(ds, 3)}
        rows.append(
            {
                "id": qid,
                "query": qtext,
                "found": bool(getattr(res, "found", False)),
                "hit_level": (getattr(res, "resolver_meta", {}) or {}).get("hit_level"),
                "pert_type": (getattr(res, "resolver_meta", {}) or {}).get("pert_type"),
                "selected_source": (getattr(res, "resolver_meta", {}) or {}).get("selected_source"),
                "source_overview": (getattr(res, "resolver_meta", {}) or {}).get("source_overview"),
                "composite_mode": (getattr(res, "resolver_meta", {}) or {}).get("composite_mode"),
                "resolver_meta": getattr(res, "resolver_meta", {}),
                "llm_call_stats": (getattr(res, "resolver_meta", {}) or {}).get("llm_call_stats", {}),
                "summary": str(getattr(res, "summary", "")),
                "timing_seconds": round(elapsed, 3),
                "prompt_timing": per_query_prompt,
            }
        )
        print(f"[{qid}] {elapsed:.2f}s")

    suite_elapsed = round(time.perf_counter() - suite_t0, 3)
    prompt_timing_final = {
        k: {"count": int(v["count"]), "seconds": round(v["seconds"], 3)}
        for k, v in sorted(prompt_timing_total.items())
    }

    model_name = args.model or os.getenv("MINIMAX_MODEL", "MiniMax-M2.7")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    tag = args.output_tag or f"{args.provider}_{ts}"
    out_json_dir = workspace / "output/store/resolver_demo/suite_runs"
    out_json_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_json_dir / f"{ts}__forward_question_suite_{tag}.json"
    payload = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "provider": args.provider,
        "model": model_name,
        "query_count": len(rows),
        "resolver_mode": args.resolver_mode,
        "no_summary": bool(args.no_summary),
        "suite_timing_seconds": suite_elapsed,
        "prompt_timing_total": prompt_timing_final,
        "rows": rows,
    }
    out_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    out_md_dir = workspace / "report/6_llm_resovler_suite_runs"
    out_md_dir.mkdir(parents=True, exist_ok=True)
    out_md = out_md_dir / f"{ts}__6_llm_resovler_forward_question_suite_{tag}.md"
    lines = [
        f"# Forward Question Suite ({args.provider})",
        "",
        f"- Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"- Provider: {args.provider}",
        f"- Model: {model_name}",
        f"- Query Count: {len(rows)}",
        f"- Resolver Mode: {args.resolver_mode}",
        f"- No Summary: {bool(args.no_summary)}",
        f"- Suite Time (s): {suite_elapsed}",
        "",
        "| ID | Found | HitLevel | Source | Query |",
        "|----|-------|----------|--------|-------|",
    ]
    for r in rows:
        q_short = r["query"].replace("|", "/")
        source_cell = r.get("source_overview") or r.get("selected_source")
        lines.append(
            f"| `{r['id']}` | `{r['found']}` | `{r['hit_level']}` | `{source_cell}` | {q_short} |"
        )
    lines.append("")
    lines.append("## Prompt Timing Total")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(prompt_timing_final, ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## Detailed Results")
    lines.append("")
    for r in rows:
        lines.append(f"### {r['id']}")
        lines.append(f"- Query: `{r['query']}`")
        lines.append(f"- Found: `{r['found']}`")
        lines.append(f"- Hit Level: `{r['hit_level']}`")
        lines.append(f"- Selected Source: `{r['selected_source']}`")
        lines.append(f"- Source Overview: `{r.get('source_overview')}`")
        lines.append(f"- Composite Mode: `{r['composite_mode']}`")
        lines.append(f"- Timing (s): `{r['timing_seconds']}`")
        lines.append("")
        lines.append("Prompt Timing:")
        lines.append("```json")
        lines.append(json.dumps(r["prompt_timing"], ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("")
        lines.append("Resolver Meta:")
        lines.append("```json")
        lines.append(json.dumps(r["resolver_meta"], ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("")
        lines.append("LLM Call Stats:")
        lines.append("```json")
        lines.append(json.dumps(r["llm_call_stats"], ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("")
        lines.append("Summary:")
        lines.append("")
        lines.append(r["summary"] if r["summary"] else "(empty)")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"question suite json: {out_json}")
    print(f"question suite report: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
