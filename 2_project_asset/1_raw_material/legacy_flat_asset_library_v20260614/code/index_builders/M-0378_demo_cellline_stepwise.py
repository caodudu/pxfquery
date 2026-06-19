from __future__ import annotations

import json
import os
import sys
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


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    if str(workspace / "script") not in sys.path:
        sys.path.insert(0, str(workspace / "script"))
    _load_env(workspace / ".env")

    from PxFquery.index.cellline_index import CellLineIndex
    from PxFquery.query.resolver import QueryResolver, ResolverConfig
    from PxFquery.query.forward import ForwardQuery
    from PxFquery.query.reverse import ReverseQuery
    from PxFquery.data.loader import DataLoader

    idx = CellLineIndex(
        workspace / "output/store/query_index/cellline_index.json",
        workspace / "output/store/query_index/cellline_neighbors.json",
    )

    model = os.getenv("MINIMAX_MODEL", "MiniMax-M2.7")
    # Build resolver so demo uses exactly the same stepwise chooser as production pipeline.
    loader = DataLoader()
    loader.load_all_local(str(workspace / "output/store/gsea_anndata"))
    forward_engines = {}
    reverse_engines = {}
    for pt in loader.list_loaded():
        ad = loader.get(pt)
        forward_engines[pt] = ForwardQuery(ad)
        reverse_engines[pt] = ReverseQuery(ad)
    resolver = QueryResolver(
        forward_engines=forward_engines,
        reverse_engines=reverse_engines,
        index_dir=workspace / "output/store/query_index",
        config=ResolverConfig(
            provider="minimax",
            model=model,
            api_key=os.getenv("MINIMAX_API_KEY"),
            base_url=os.getenv("MINIMAX_BASE_URL", "https://api.minimax.chat/v1"),
        ),
    )

    contexts = [
        "triple-negative breast cancer",
        "non-small cell lung carcinoma",
        "colorectal adenocarcinoma",
        "NCI-H358-like NSCLC context",
    ]
    demos = []
    for bio_desc in contexts:
        trace: list[dict] = []

        def chooser(desc: str, options: list[str], level: str) -> str:
            fast = resolver._fast_choose_option(desc, options)  # demo trace only
            if fast is not None:
                selected = fast
                source = "fast_rule"
            else:
                try:
                    selected = resolver._call_prompt("llm_map_cell_line", desc, options, level)
                    source = "llm"
                except Exception:
                    selected = options[0]
                    source = "llm_error_fallback_first_option"
            trace.append(
                {
                    "level": level,
                    "options": options,
                    "selected": selected,
                    "source": source,
                }
            )
            return selected

        cells = idx.traverse(bio_context=bio_desc, llm_choose_fn=chooser)
        demos.append(
            {
                "bio_context": bio_desc,
                "trace": trace,
                "resolved_cells": cells,
            }
        )

    report = {
        "time": datetime.now().isoformat(timespec="seconds"),
        "model": model,
        "demos": demos,
    }

    out_json = workspace / "output/store/resolver_demo/cellline_stepwise_demo.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    out_md = workspace / "report/6_llm_resovler_cellline_stepwise_demo.md"
    lines = [
        "# Cellline Stepwise Selection Demo",
        "",
        f"- Time: {report['time']}",
        f"- Model: {model}",
        f"- Demo Count: {len(demos)}",
        "",
        "## Step Traces",
        "",
    ]
    for d in demos:
        lines.append(f"### Context: `{d['bio_context']}`")
        for i, step in enumerate(d["trace"], 1):
            lines.append(
                f"- Step {i} ({step['level']}): selected `{step['selected']}` from {step['options']} (source={step['source']})"
            )
        lines.append(f"- Resolved Cells: `{d['resolved_cells']}`")
        lines.append("")
    out_md.write_text("\n".join(lines), encoding="utf-8")

    print(f"stepwise json: {out_json}")
    print(f"stepwise report: {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
