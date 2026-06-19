from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class CaseResult:
    name: str
    query: str
    result_type: str
    found: bool
    resolver_meta: dict[str, Any]
    summary: str
    top_preview: list[dict[str, Any]]


def _load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _ensure_sys_path(workspace: Path) -> None:
    package_root = workspace / "script"
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))


def _preview(result) -> list[dict[str, Any]]:
    if hasattr(result, "top_activated") and hasattr(result, "top_suppressed"):
        act = [
            {"term": k, "score": float(v)}
            for k, v in result.top_activated.head(5).items()
        ]
        sup = [
            {"term": k, "score": float(v)}
            for k, v in result.top_suppressed.head(5).items()
        ]
        return [{"top_activated": act}, {"top_suppressed": sup}]
    if hasattr(result, "candidates_df"):
        top = result.candidates_df.head(5)
        rows = []
        for _, row in top.iterrows():
            rows.append(
                {
                    "cmap_name": str(row.get("cmap_name")),
                    "cell_iname": str(row.get("cell_iname")),
                    "similarity": float(row.get("similarity", 0.0)),
                    "driving_terms": str(row.get("driving_terms", "")),
                }
            )
        return rows
    return []


def _run_case(pxf, name: str, query: str) -> CaseResult:
    result = pxf.query(query, top_n=10)
    return CaseResult(
        name=name,
        query=query,
        result_type=type(result).__name__,
        found=bool(getattr(result, "found", False)),
        resolver_meta=dict(getattr(result, "resolver_meta", {})),
        summary=str(getattr(result, "summary", "")),
        top_preview=_preview(result),
    )


def _write_markdown(path: Path, provider: str, model: str, cases: list[CaseResult]) -> None:
    lines = []
    lines.append("# 6_llm_resovler Act-1 Validation Report")
    lines.append("")
    lines.append(f"- Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"- Provider: {provider}")
    lines.append(f"- Model: {model}")
    lines.append("")
    lines.append("## Case Results")
    lines.append("")
    for c in cases:
        lines.append(f"### {c.name}")
        lines.append(f"- Query: `{c.query}`")
        lines.append(f"- Result type: `{c.result_type}`")
        lines.append(f"- Found: `{c.found}`")
        lines.append(f"- Resolver meta: `{json.dumps(c.resolver_meta, ensure_ascii=False)}`")
        lines.append("")
        lines.append("Summary:")
        lines.append("")
        lines.append(c.summary)
        lines.append("")
        lines.append("Top preview:")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(c.top_preview, ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    _ensure_sys_path(workspace)
    _load_env(workspace / ".env")

    provider = os.getenv("PXFQUERY_PROVIDER", "minimax")
    if provider == "minimax":
        model = os.getenv("PXFQUERY_MODEL") or os.getenv("MINIMAX_MODEL") or "MiniMax-M2.7"
    else:
        model = os.getenv("PXFQUERY_MODEL") or os.getenv("SILICONFLOW_MODEL") or "Qwen/Qwen2.5-72B-Instruct"

    from PxFquery import PxFquery

    pxf = PxFquery()
    pxf.load_data_dir(str(workspace / "output/store/gsea_anndata"))
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider=provider,
        model=model,
    )

    cases = []
    error_message = None
    try:
        cases = [
            _run_case(
                pxf,
                "forward_egfr_a549",
                "In A549, what pathways are affected by EGFR knockdown?",
            ),
            _run_case(
                pxf,
                "reverse_apoptosis_myc_a549",
                "In A549, recommend perturbations that activate apoptosis and suppress MYC targets.",
            ),
        ]
    except Exception as e:
        error_message = f"{type(e).__name__}: {e}"

    out_dir = workspace / "output/store/resolver_demo"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"act1_validation_{provider}.json"
    payload = {
        "provider": provider,
        "model": model,
        "ok": error_message is None,
        "error": error_message,
        "cases": [asdict(c) for c in cases],
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    report_path = workspace / f"report/6_llm_resovler_act1_validation_{provider}.md"
    _write_markdown(report_path, provider, model, cases)
    if error_message:
        with report_path.open("a", encoding="utf-8") as f:
            f.write("\n## Runtime Error\n\n")
            f.write(error_message + "\n")

    print(f"validation json: {json_path}")
    print(f"validation report: {report_path}")
    return 0 if error_message is None else 1


if __name__ == "__main__":
    raise SystemExit(main())
