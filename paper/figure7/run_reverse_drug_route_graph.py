from __future__ import annotations

import argparse
import json
import os
import pickle
import sys
import time
import traceback
from pathlib import Path


PROJECT_ROOT = Path("/Users/dudu/Documents/3_Project/12_PxFquery")
TASK_ROOT = PROJECT_ROOT / "5_phase_translation/G-011_paper_figure_planning/T-150_figure7_reverse_drug_query_notebook_figure_workb"
T144_ROOT = PROJECT_ROOT / "4_phase_development/G-035_goal_ms8_human_usable_package/T-144_ms8_14_user_value_l5_output_rework"
SRC_ROOT = TASK_ROOT / "3_execution/t144_package_source_for_fig7a/src"
RESOURCE_ROOT = Path("/Users/dudu/.cache/pxfquery/resources/v20260628")

sys.path.insert(0, str(SRC_ROOT))
os.environ["PYTHONPATH"] = str(SRC_ROOT) + os.pathsep + os.environ.get("PYTHONPATH", "")


def load_env() -> None:
    for env_path in [Path.home() / ".env", TASK_ROOT / "1_asset/.env", T144_ROOT / "1_asset/.env"]:
        if not env_path.exists():
            continue
        for raw in env_path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())
    if os.environ.get("DEEPSEEK_API_KEY") and not os.environ.get("PXFQUERY_LLM_API_KEY"):
        os.environ["PXFQUERY_LLM_API_KEY"] = os.environ["DEEPSEEK_API_KEY"]
    if os.environ.get("DEEPSEEK_API_BASE") and not os.environ.get("PXFQUERY_LLM_BASE_URL"):
        os.environ["PXFQUERY_LLM_BASE_URL"] = os.environ["DEEPSEEK_API_BASE"]
    os.environ.setdefault("PXFQUERY_LLM_PROVIDER", "deepseek")
    os.environ.setdefault("PXFQUERY_LLM_MODEL", "deepseek-v4-flash")


def answer_to_dict(answer):
    if hasattr(answer, "to_dict"):
        return answer.to_dict()
    if hasattr(answer, "__dict__"):
        return dict(answer.__dict__)
    return {"text": str(answer)}


def get_summary(answer_dict: dict) -> str:
    for key in ["summary", "biological_summary", "answer", "text"]:
        value = answer_dict.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    for value in answer_dict.values():
        if isinstance(value, str) and len(value) > 40:
            return value.strip()
    return str(answer_dict)[:1000]


def load_brd_name_index() -> dict[str, str]:
    drug_index_path = RESOURCE_ROOT / "drug_index.json"
    if not drug_index_path.exists():
        return {}
    try:
        drug_index = json.loads(drug_index_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out: dict[str, str] = {}
    for name, value in drug_index.items():
        values = value if isinstance(value, list) else [value]
        for brd in values:
            if isinstance(brd, str):
                out.setdefault(brd, str(name))
    return out


BRD_NAME_INDEX = load_brd_name_index()


def display_label(row: dict) -> str:
    label = row.get("label") or row.get("cmap_name") or row.get("pert_id")
    pert_id = row.get("pert_id") or row.get("cmap_name")
    if (not label or label == "Unnamed compound") and isinstance(pert_id, str):
        return BRD_NAME_INDEX.get(pert_id, pert_id)
    if isinstance(label, str) and label.startswith("BRD-"):
        return BRD_NAME_INDEX.get(label, label)
    return str(label)


def compact_top(answer_dict: dict) -> list[dict]:
    ranked = ((answer_dict.get("tables") or {}).get("ranked_results") or [])[:8]
    rows = []
    for index, row in enumerate(ranked, start=1):
        rows.append(
            {
                "rank": row.get("rank", index),
                "label": display_label(row),
                "raw_label": row.get("label"),
                "cmap_name": row.get("cmap_name"),
                "pert_id": row.get("pert_id"),
                "score": row.get("score"),
                "support": row.get("support") or row.get("support_count") or row.get("match_support_count"),
                "cells": row.get("cells") or row.get("cell_iname") or row.get("support_cells"),
            }
        )
    return rows


def compact_targets(answer_dict: dict) -> list[dict]:
    targets = ((answer_dict.get("tables") or {}).get("route_target_functions") or [])[:20]
    return [
        {
            "route_id": row.get("route_id"),
            "label": row.get("label") or row.get("function_label") or row.get("var_name"),
            "direction": row.get("direction"),
            "source": row.get("source"),
            "cell": row.get("cell") or row.get("cell_iname"),
        }
        for row in targets
    ]


def compact_routes(answer_dict: dict) -> list[dict]:
    routes = ((answer_dict.get("tables") or {}).get("route_summary") or [])[:20]
    keys = ["route_id", "status", "cell", "cell_iname", "modality", "route_quality", "route_quality_score"]
    return [{key: row.get(key) for key in keys if key in row} for row in routes]


def compact_fig_specs(answer) -> list[dict]:
    specs = []
    for spec in getattr(answer, "figures", []) or []:
        item = {"kind": spec.get("kind"), "title": spec.get("title")}
        if spec.get("kind") == "reverse_layered_route_graph":
            item.update(
                {
                    "target_functions": len(spec.get("target_functions", [])),
                    "candidates": len(spec.get("candidates", [])),
                }
            )
        elif spec.get("kind") == "reverse_candidate_bubble":
            item.update({"candidates": len(spec.get("candidates", [])), "top": spec.get("candidates", [])[:5]})
        elif spec.get("kind") == "reverse_function_ring_heatmap":
            item.update(
                {
                    "source": spec.get("source"),
                    "functions": len(spec.get("functions", [])),
                    "matches": len(spec.get("matches", [])),
                }
            )
        specs.append(item)
    return specs


def run_one(args: argparse.Namespace) -> dict:
    load_env()
    from pxfquery import PxFQuery

    fig_root = TASK_ROOT / "4_artifact/4_picture/figure7/figure7a_clean_rerun" / args.round_id / args.run_id
    run_root = TASK_ROOT / "4_artifact/1_tmp/figure7a_clean_rerun_qdata_answers" / args.round_id / args.run_id
    table_root = TASK_ROOT / "4_artifact/5_table/figure7/figure7a_clean_rerun" / args.round_id
    for path in [fig_root / "png", fig_root / "pdf", run_root, table_root]:
        path.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    result = {
        "round_id": args.round_id,
        "run_id": args.run_id,
        "source_context": args.source_context,
        "query": args.query,
        "status": "started",
    }
    try:
        client = PxFQuery()
        qdata = client.tl.parse(args.query, top_n=args.top_n, progress=False)
        client.tl.answer(qdata, progress=False)
        answer = client.get.answer(qdata)
        answer_dict = answer_to_dict(answer)
        with open(run_root / f"{args.run_id}_qdata.pkl", "wb") as handle:
            pickle.dump(qdata, handle)
        answer_path = run_root / f"{args.run_id}_answer.json"
        answer_path.write_text(json.dumps(answer_dict, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        client.tl.figures(qdata, output_dir=fig_root / "pdf", prefix=args.run_id)
        pdf_paths = [str(Path(path)) for path in qdata.uns.get("figure_outputs", [])]
        client.tl.figures(qdata, output_dir=fig_root / "png", prefix=args.run_id, format="png")
        png_paths = [str(Path(path)) for path in qdata.uns.get("figure_outputs", [])]
        route_png = [path for path in png_paths if "route" in Path(path).name or "evidence" in Path(path).name or "layered" in Path(path).name]
        route_pdf = [path for path in pdf_paths if "route" in Path(path).name or "evidence" in Path(path).name or "layered" in Path(path).name]
        result.update(
            {
                "status": "ok",
                "elapsed_seconds": round(time.perf_counter() - started, 2),
                "answer_summary": get_summary(answer_dict),
                "top_candidates": compact_top(answer_dict),
                "target_functions": compact_targets(answer_dict),
                "routes": compact_routes(answer_dict),
                "figure_specs": compact_fig_specs(answer),
                "png_paths": png_paths,
                "pdf_paths": pdf_paths,
                "route_png_paths": route_png,
                "route_pdf_paths": route_pdf,
                "answer_json_path": str(answer_path),
                "qdata_pickle_path": str(run_root / f"{args.run_id}_qdata.pkl"),
            }
        )
    except Exception as exc:
        result.update(
            {
                "status": "error",
                "elapsed_seconds": round(time.perf_counter() - started, 2),
                "error": f"{type(exc).__name__}: {exc}",
                "traceback": traceback.format_exc(),
            }
        )
    out_path = table_root / f"{args.run_id}_result.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"run_id": args.run_id, "status": result["status"], "elapsed_seconds": result.get("elapsed_seconds")}, ensure_ascii=False))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--round-id", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--source-context", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-n", type=int, default=8)
    run_one(parser.parse_args())


if __name__ == "__main__":
    main()

