from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

from pxfquery import PxFQuery


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--env-file")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--artifact-dir", required=True)
    parser.add_argument("--top-n", type=int, default=20)
    parser.add_argument("--synthesize", action="store_true")
    parser.add_argument("--chat", choices=["none", "sample", "all"], default="sample")
    parser.add_argument("--sample-chat-per-dataset", type=int, default=2)
    parser.add_argument("--limit-per-dataset", type=int)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args(argv)

    if args.env_file:
        _load_env_file(args.env_file)

    started = time.time()
    project_root = Path(args.project_root).resolve()
    artifact_dir = Path(args.artifact_dir).resolve()
    artifact_dir.mkdir(parents=True, exist_ok=True)

    report: dict[str, Any] = {
        "schema_version": "pxfquery-l5-parse-first-validation/v1",
        "package_root": str(Path(__file__).resolve().parents[1]),
        "artifact_dir": str(artifact_dir),
        "parameters": {
            "top_n": args.top_n,
            "synthesize": args.synthesize,
            "chat": args.chat,
            "sample_chat_per_dataset": args.sample_chat_per_dataset,
            "limit_per_dataset": args.limit_per_dataset,
            "workers": args.workers,
            "query_source_note": "The referenced files are used only as raw query lists; this script re-runs current T141 pxf.tl.parse(query) before every L5 output.",
        },
        "datasets": {},
        "parse_failures": [],
        "l5_failures": [],
    }

    datasets = {
        "t140_60_raw_queries": project_root
        / "4_phase_development/G-035_goal_ms8_human_usable_package/T-140_ms8_12_l4_evidence_dossier_plan/4_artifact/5_table/t137_60_l1_to_l4_parallel_latest.json",
        "t139_50_raw_queries": project_root
        / "4_phase_development/G-035_goal_ms8_human_usable_package/T-139_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table/generalization_50_l1_l2_to_l3_replay_latest.json",
    }

    for dataset_name, source_path in datasets.items():
        report["datasets"][dataset_name] = _validate_dataset(
            dataset_name,
            source_path,
            artifact_dir / dataset_name,
            top_n=args.top_n,
            synthesize=args.synthesize,
            chat=args.chat,
            sample_chat_per_dataset=args.sample_chat_per_dataset,
            limit=args.limit_per_dataset,
            workers=max(1, args.workers),
            parse_failures=report["parse_failures"],
            l5_failures=report["l5_failures"],
        )

    report["parse_failure_count"] = len(report["parse_failures"])
    report["l5_failure_count"] = len(report["l5_failures"])
    report["elapsed_seconds"] = round(time.time() - started, 2)
    out = Path(args.output_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(_compact_report(report), ensure_ascii=False, indent=2))
    return 0 if not report["l5_failures"] else 1


def _validate_dataset(
    dataset_name: str,
    source_path: Path,
    output_dir: Path,
    *,
    top_n: int,
    synthesize: bool,
    chat: str,
    sample_chat_per_dataset: int,
    limit: int | None,
    workers: int,
    parse_failures: list[dict[str, Any]],
    l5_failures: list[dict[str, Any]],
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = _load_records(source_path)
    if limit is not None:
        rows = rows[:limit]
    stats: dict[str, Any] = {
        "source": str(source_path),
        "total": len(rows),
        "parse_ok": 0,
        "answer_ok": 0,
        "html_ok": 0,
        "mcp_ok": 0,
        "png_figure_ok": 0,
        "svg_figure_ok": 0,
        "chat_ok": 0,
        "dossier_status_counts": {},
        "summary_sources": {},
        "figure_kind_counts": {},
        "samples": [],
    }

    jobs = []
    sample_chat_remaining = sample_chat_per_dataset
    for idx, row in enumerate(rows):
        should_chat = chat == "all" or (chat == "sample" and sample_chat_remaining > 0)
        if should_chat and chat == "sample":
            sample_chat_remaining -= 1
        jobs.append((idx, row, should_chat))

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [
            pool.submit(
                _validate_one_query,
                dataset_name,
                idx,
                row,
                output_dir,
                top_n,
                synthesize,
                should_chat,
            )
            for idx, row, should_chat in jobs
        ]
        for future in as_completed(futures):
            result = future.result()
            if result["status"] == "parse_failed":
                parse_failures.append(result["failure"])
                continue
            if result["status"] == "l5_failed":
                stats["parse_ok"] += 1
                _inc(stats["dossier_status_counts"], result.get("dossier_status"))
                l5_failures.append(result["failure"])
                continue
            stats["parse_ok"] += 1
            stats["answer_ok"] += 1
            stats["html_ok"] += 1
            stats["mcp_ok"] += 1
            stats["png_figure_ok"] += 1
            stats["svg_figure_ok"] += 1
            if result.get("chat_ok"):
                stats["chat_ok"] += 1
            _inc(stats["dossier_status_counts"], result.get("dossier_status"))
            _inc(stats["summary_sources"], result.get("summary_source"))
            for kind in result.get("figure_kinds", []):
                _inc(stats["figure_kind_counts"], kind)
            if len(stats["samples"]) < 5:
                stats["samples"].append(result["sample"])
    return stats


def _validate_one_query(
    dataset_name: str,
    idx: int,
    row: dict[str, Any],
    output_dir: Path,
    top_n: int,
    synthesize: bool,
    should_chat: bool,
) -> dict[str, Any]:
    case_id = str(row.get("case_id") or f"{idx:03d}")
    query = str(row.get("query") or row.get("question") or "").strip()
    if not query:
        return {
            "status": "parse_failed",
            "failure": {"dataset": dataset_name, "case_id": case_id, "stage": "input", "error": "missing query text"},
        }
    case_dir = output_dir / _safe_name(case_id)
    client = PxFQuery()
    try:
        qdata = client.tl.parse(query, top_n=top_n, synthesize=synthesize)
        dossier = qdata.uns.get("evidence_dossier")
        if not isinstance(dossier, dict) or dossier.get("schema_version") != "l4-evidence-dossier/v1":
            raise RuntimeError("pxf.tl.parse did not produce an L4 evidence dossier")
    except Exception as exc:
        return {
            "status": "parse_failed",
            "failure": {
                "dataset": dataset_name,
                "case_id": case_id,
                "query": query,
                "stage": "pxf.tl.parse",
                "error": f"{type(exc).__name__}: {exc}",
            },
        }

    try:
        client.tl.answer(qdata, mode="python")
        answer = client.get.answer(qdata)
        _require(answer.summary, "empty L5 summary")
        _require(answer.summary_source.startswith("l4."), "L5 summary was not derived from L4")
        figure_kinds = [str(spec.get("kind")) for spec in answer.figures]

        html_path = case_dir / "answer.html"
        html_path.parent.mkdir(parents=True, exist_ok=True)
        client.tl.answer(qdata, mode="html", output=html_path)
        html_text = html_path.read_text(encoding="utf-8")
        _require("<html" in html_text.lower(), "HTML report missing HTML document")
        _require("<svg" in html_text, "HTML report did not embed rendered SVG figures")

        client.tl.answer(qdata, mode="mcp")
        mcp_payload = client.get.answer(qdata).mcp
        _require(isinstance(mcp_payload, dict), "MCP answer payload is not a dict")
        _require(mcp_payload.get("schema_version") == "pxfquery-l5-mcp/v1", "MCP answer schema mismatch")
        _require(bool(mcp_payload.get("evidence_contract")), "MCP answer lacks evidence contract")

        client.tl.figures(qdata, output_dir=case_dir / "png", format="png")
        png_paths = [Path(item) for item in qdata.uns["figure_outputs"]]
        _require(png_paths, "no PNG figures written")
        _require(all(path.read_bytes().startswith(b"\x89PNG") for path in png_paths), "PNG figure file header invalid")

        client.tl.figures(qdata, output_dir=case_dir / "svg", format="svg")
        svg_paths = [Path(item) for item in qdata.uns["figure_outputs"]]
        _require(svg_paths, "no SVG figures written")
        _require(all(path.read_text(encoding="utf-8").startswith("<svg") for path in svg_paths), "SVG figure file invalid")

        chat_ok = False
        if should_chat:
            client.tl.chat(qdata, "请用中文概括主要证据、图表含义和限制。", print_response=False)
            response = client.get.chat(qdata)
            _require(response.strip(), "empty chat response")
            _require(len(client.get.chat_history(qdata)) >= 1, "chat history was not retained")
            (case_dir / "chat.json").write_text(
                json.dumps(qdata.uns["last_chat"], ensure_ascii=False, indent=2, default=str),
                encoding="utf-8",
            )
            chat_ok = True

        return {
            "status": "ok",
            "case_id": case_id,
            "query": query,
            "dossier_status": dossier.get("dossier_status"),
            "summary_source": answer.summary_source,
            "figure_kinds": figure_kinds,
            "chat_ok": chat_ok,
            "sample": {
                "case_id": case_id,
                "query": query,
                "dossier_status": dossier.get("dossier_status"),
                "summary_source": answer.summary_source,
                "summary_preview": answer.summary[:260],
                "html": str(html_path),
                "png_count": len(png_paths),
                "svg_count": len(svg_paths),
                "figure_kinds": figure_kinds,
            },
        }
    except Exception as exc:
        return {
            "status": "l5_failed",
            "dossier_status": (qdata.uns.get("evidence_dossier") or {}).get("dossier_status"),
            "failure": {
                "dataset": dataset_name,
                "case_id": case_id,
                "query": query,
                "stage": "l5_after_parse",
                "dossier_status": (qdata.uns.get("evidence_dossier") or {}).get("dossier_status"),
                "error": f"{type(exc).__name__}: {exc}",
            },
        }


def _load_records(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    records = data.get("records") if isinstance(data, dict) else data
    if not isinstance(records, list):
        raise ValueError(f"{path} does not contain a records list")
    return records


def _compact_report(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": report["schema_version"],
        "parameters": report["parameters"],
        "datasets": {
            name: {key: value for key, value in stats.items() if key not in {"samples", "source"}}
            for name, stats in report["datasets"].items()
        },
        "parse_failure_count": report["parse_failure_count"],
        "l5_failure_count": report["l5_failure_count"],
        "elapsed_seconds": report["elapsed_seconds"],
        "parse_failure_preview": report["parse_failures"][:5],
        "l5_failure_preview": report["l5_failures"][:5],
    }


def _load_env_file(path: str | os.PathLike[str]) -> None:
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ[key.strip()] = value.strip()


def _safe_name(text: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_"} else "_" for ch in text)[:80] or "case"


def _inc(counter: dict[str, int], key: Any) -> None:
    text = str(key)
    counter[text] = counter.get(text, 0) + 1


def _require(condition: Any, message: str) -> None:
    if not condition:
        raise AssertionError(message)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
