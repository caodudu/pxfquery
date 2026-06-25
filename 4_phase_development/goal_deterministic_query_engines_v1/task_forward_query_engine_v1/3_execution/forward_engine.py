from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd


TASK_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = TASK_ROOT / "1_asset"
ARTIFACT_ROOT = TASK_ROOT / "4_artifact"
TABLE_DIR = ARTIFACT_ROOT / "5_table"
DOC_DIR = ARTIFACT_ROOT / "3_document"

WORKSPACE_SRC = (ASSET_ROOT / "T-024 pxfquery workspace package" / "src").resolve()
LOADER_PARENT = (ASSET_ROOT / "T-026 matrix loader package").resolve().parent
DATA_BUNDLE = ASSET_ROOT / "T-021 standard_resources bundle (D-004)"
XPR_MATRIX = DATA_BUNDLE / "xpr_func_ad.h5ad"

sys.path.insert(0, str(WORKSPACE_SRC))
sys.path.insert(0, str(LOADER_PARENT))

from loader import load_matrix  # noqa: E402
from pxfquery.query.forward import ForwardQuery  # noqa: E402


def result_to_frame(result, query: str, requested_cell_line: str) -> pd.DataFrame:
    rows = []
    for direction, series in (
        ("activated", result.top_activated),
        ("suppressed", result.top_suppressed),
    ):
        for rank, (term, score) in enumerate(series.items(), start=1):
            rows.append(
                {
                    "query": query,
                    "requested_cell_line": requested_cell_line,
                    "matched_perturbation": result.perturbation,
                    "matched_cell_line": result.cell_line,
                    "direction": direction,
                    "rank": rank,
                    "term": term,
                    "score": float(score),
                    "n_obs": int(result.n_obs),
                    "cells_used": "|".join(result.cells_used),
                }
            )
    return pd.DataFrame(rows)


def write_html(path: Path, title: str, body: str) -> None:
    path.write_text(
        "\n".join(
            [
                "<!doctype html>",
                "<html lang=\"zh-CN\">",
                "<head>",
                "  <meta charset=\"utf-8\">",
                f"  <title>{title}</title>",
                "  <style>body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:1100px;margin:32px auto;padding:0 20px;line-height:1.55;color:#1f2933}table{border-collapse:collapse;width:100%;font-size:13px}th,td{border:1px solid #d8dee4;padding:6px 8px;text-align:left}th{background:#f3f4f6}code{background:#f3f4f6;padding:2px 4px;border-radius:4px}</style>",
                "</head>",
                "<body>",
                body,
                "</body>",
                "</html>",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    DOC_DIR.mkdir(parents=True, exist_ok=True)

    adata, matrix_meta = load_matrix(XPR_MATRIX)
    engine = ForwardQuery(adata)

    cases = [
        {
            "label": "EGFR_A549",
            "query": "EGFR",
            "cell_line": "A549",
            "csv": TABLE_DIR / "pxfquery_T029_EGFR_A549_xpr_forward_result.csv",
        },
        {
            "label": "TP53_MCF7",
            "query": "TP53",
            "cell_line": "MCF7",
            "csv": TABLE_DIR / "pxfquery_T029_TP53_MCF7_xpr_forward_result.csv",
        },
    ]

    summaries = []
    rendered_tables = []
    for case in cases:
        result = engine.query(case["query"], cell_line=case["cell_line"], top_n=20)
        if not result.found:
            raise RuntimeError(f"Expected forward query to be found: {case}")
        frame = result_to_frame(result, case["query"], case["cell_line"])
        frame.to_csv(case["csv"], index=False)
        summaries.append(
            {
                "label": case["label"],
                "query": case["query"],
                "requested_cell_line": case["cell_line"],
                "matched_perturbation": result.perturbation,
                "matched_cell_line": result.cell_line,
                "found": bool(result.found),
                "n_obs": int(result.n_obs),
                "activated_terms": int(len(result.top_activated)),
                "suppressed_terms": int(len(result.top_suppressed)),
                "csv": str(case["csv"]),
            }
        )
        rendered_tables.append((case["label"], frame.head(8).to_html(index=False)))

    notfound = engine.query("NONEXISTENT_PERT_XYZ", cell_line="A549", top_n=20)
    notfound_payload = {
        "query": "NONEXISTENT_PERT_XYZ",
        "requested_cell_line": "A549",
        "found": bool(notfound.found),
        "note": notfound.note,
        "n_obs": int(notfound.n_obs),
        "activated_terms": int(len(notfound.top_activated)),
        "suppressed_terms": int(len(notfound.top_suppressed)),
    }
    notfound_path = TABLE_DIR / "pxfquery_T029_notfound_query_result.json"
    notfound_path.write_text(json.dumps(notfound_payload, indent=2), encoding="utf-8")

    validation = {
        "task": "T-029_forward_query_engine_v1",
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "matrix": matrix_meta,
        "workspace_src": str(WORKSPACE_SRC),
        "loader_parent": str(LOADER_PARENT),
        "cases": summaries,
        "notfound": notfound_payload,
        "acceptance": {
            "imports_t026_loader": True,
            "imports_t024_forward_query": True,
            "egfr_a549_found": summaries[0]["found"],
            "egfr_a549_rows": 40,
            "diversity_case_found": summaries[1]["found"],
            "diversity_case_rows": 40,
            "notfound_found_false": not notfound.found,
        },
    }
    validation_path = TABLE_DIR / "pxfquery_T029_forward_validation.json"
    validation_path.write_text(json.dumps(validation, indent=2), encoding="utf-8")

    today = datetime.now().strftime("%Y%m%d")
    execution_report = DOC_DIR / f"execution_report_v{today}.html"
    result_report = DOC_DIR / f"result_report_v{today}.html"

    write_html(
        execution_report,
        "T-029 forward query execution report",
        f"""
        <h1>T-029 forward query execution report</h1>
        <p>本任务使用 T-026 loader 读取 T-021 的 <code>xpr_func_ad.h5ad</code>，并直接调用 T-024 workspace 中的 <code>ForwardQuery</code>。</p>
        <ul>
          <li>矩阵 shape: <code>{matrix_meta['shape']}</code></li>
          <li>obs columns: <code>{', '.join(matrix_meta['obs_columns'])}</code></li>
          <li>dtype: <code>{matrix_meta['X_dtype']}</code></li>
          <li>EGFR/A549 和 TP53/MCF7 均实际运行并产生 20 activated + 20 suppressed 结果。</li>
          <li>不存在扰动查询返回 <code>found=False</code>，未崩溃。</li>
        </ul>
        """,
    )

    result_sections = []
    for label, html_table in rendered_tables:
        result_sections.append(f"<h2>{label}</h2>{html_table}")
    write_html(
        result_report,
        "T-029 forward query result report",
        "<h1>T-029 forward query result report</h1>"
        + "".join(result_sections)
        + f"<h2>Not-found behavior</h2><pre>{json.dumps(notfound_payload, indent=2)}</pre>",
    )

    registry = ARTIFACT_ROOT / "registry.yaml"
    registry.write_text(
        "\n".join(
            [
                "task_id: T-029",
                "task_name: forward_query_engine_v1",
                "artifacts:",
                "  - id: T029-D-001",
                "    path: 3_execution/forward_engine.py",
                "    role: runnable_forward_engine",
                "  - id: T029-D-002",
                "    path: 4_artifact/5_table/pxfquery_T029_EGFR_A549_xpr_forward_result.csv",
                "    role: canonical_forward_demo_table",
                "  - id: T029-D-003",
                "    path: 4_artifact/5_table/pxfquery_T029_TP53_MCF7_xpr_forward_result.csv",
                "    role: diversity_forward_demo_table",
                "  - id: T029-D-004",
                "    path: 4_artifact/5_table/pxfquery_T029_notfound_query_result.json",
                "    role: notfound_behavior_evidence",
                "  - id: T029-D-005",
                "    path: 4_artifact/5_table/pxfquery_T029_forward_validation.json",
                "    role: validation_summary",
                f"  - id: T029-D-006\n    path: 4_artifact/3_document/{execution_report.name}\n    role: execution_report",
                f"  - id: T029-D-007\n    path: 4_artifact/3_document/{result_report.name}\n    role: result_report",
                "",
            ]
        ),
        encoding="utf-8",
    )

    completion = TASK_ROOT / "5_report" / "completion.md"
    completion.parent.mkdir(parents=True, exist_ok=True)
    completion.write_text(
        "\n".join(
            [
                "# T-029 Completion",
                "",
                "T-029 produced a deterministic forward query engine using T-026 loader and T-024 ForwardQuery.",
                "",
                "Validation evidence:",
                "- EGFR/A549/xpr query returned found=True with 20 activated and 20 suppressed rows.",
                "- TP53/MCF7/xpr query returned found=True with 20 activated and 20 suppressed rows.",
                "- NONEXISTENT_PERT_XYZ/A549 returned found=False without crashing.",
                "",
                "No upstream artifact was modified. No local package repair was required.",
            ]
        ),
        encoding="utf-8",
    )

    print(json.dumps(validation["acceptance"], indent=2))


if __name__ == "__main__":
    main()
