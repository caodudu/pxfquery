from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

from pxfquery import PxFQuery
from pxfquery.l4_evidence import assemble_evidence


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--env-file")
    parser.add_argument("--output-json", required=True)
    parser.add_argument("--artifact-dir", required=True)
    parser.add_argument("--run-deepseek-chat", action="store_true")
    parser.add_argument("--run-mcp", action="store_true")
    args = parser.parse_args(argv)

    project_root = Path(args.project_root).resolve()
    package_root = Path(__file__).resolve().parents[1]
    artifact_dir = Path(args.artifact_dir).resolve()
    artifact_dir.mkdir(parents=True, exist_ok=True)
    if args.env_file:
        _load_env_file(args.env_file)

    started = time.time()
    report: dict[str, Any] = {
        "schema_version": "pxfquery-l5-real-validation/v1",
        "package_root": str(package_root),
        "artifact_dir": str(artifact_dir),
        "datasets": {},
        "entrypoints": {},
        "failures": [],
    }

    t140_60 = project_root / "4_phase_development/goal_goal_ms8_human_usable_package/task_ms8_12_l4_evidence_dossier_plan/4_artifact/5_table/t137_60_l1_to_l4_parallel_latest.json"
    t139_50_l3 = project_root / "4_phase_development/goal_goal_ms8_human_usable_package/task_ms8_11_l3_resource_pack_query_execution_repair/4_artifact/5_table/generalization_50_l1_l2_to_l3_replay_latest.json"
    report["datasets"]["t140_60_l4"] = _validate_dataset(
        "t140_60_l4",
        t140_60,
        artifact_dir / "t140_60",
        dossier_loader=lambda row: row["evidence_dossier"],
        failure_sink=report["failures"],
    )
    report["datasets"]["t139_50_l3_assembled_l4"] = _validate_dataset(
        "t139_50_l3_assembled_l4",
        t139_50_l3,
        artifact_dir / "t139_50",
        dossier_loader=lambda row: assemble_evidence(row["execution"]),
        failure_sink=report["failures"],
    )
    report["entrypoints"]["cli"] = _validate_cli(package_root, project_root, args.env_file, artifact_dir / "cli")
    if args.run_mcp:
        report["entrypoints"]["mcp"] = asyncio.run(_validate_mcp(package_root, project_root, args.env_file, artifact_dir / "mcp"))
    if args.run_deepseek_chat:
        report["entrypoints"]["deepseek_chat"] = _validate_deepseek_chat(t140_60, artifact_dir / "deepseek_chat")

    report["failure_count"] = len(report["failures"])
    report["elapsed_seconds"] = round(time.time() - started, 2)
    out = Path(args.output_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(_compact_report(report), ensure_ascii=False, indent=2))
    return 0 if not report["failures"] else 1


def _validate_dataset(name: str, path: Path, output_dir: Path, *, dossier_loader, failure_sink: list[dict[str, Any]]) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data["records"]
    pxf = PxFQuery()
    stats = {
        "source": str(path),
        "total": len(rows),
        "answer_ok": 0,
        "html_ok": 0,
        "mcp_ok": 0,
        "png_figure_ok": 0,
        "svg_figure_ok": 0,
        "figure_kind_counts": {},
        "summary_sources": {},
        "sample_outputs": [],
    }
    for idx, row in enumerate(rows):
        case_id = str(row.get("case_id") or idx)
        query = row.get("query") or f"{name}:{case_id}"
        try:
            dossier = dossier_loader(row)
            qdata = pxf.read.query(query)
            qdata.uns["evidence_dossier"] = dossier
            qdata.uns["result"] = dossier
            pxf.tl.answer(qdata, mode="python")
            answer = pxf.get.answer(qdata)
            _require(answer.summary, "empty answer summary")
            _require(answer.summary_source.startswith("l4."), "summary source is not L4")
            stats["answer_ok"] += 1
            stats["summary_sources"][answer.summary_source] = stats["summary_sources"].get(answer.summary_source, 0) + 1
            for spec in answer.figures:
                kind = spec.get("kind")
                stats["figure_kind_counts"][kind] = stats["figure_kind_counts"].get(kind, 0) + 1
            pxf.tl.answer(qdata, mode="html", output=output_dir / f"{case_id}.html")
            html_text = Path(qdata.uns["answer_output"]).read_text(encoding="utf-8")
            _require("<svg" in html_text, "HTML lacks rendered SVG figures")
            stats["html_ok"] += 1
            pxf.tl.answer(qdata, mode="mcp")
            payload = pxf.get.answer(qdata).mcp
            _require(payload["schema_version"] == "pxfquery-l5-mcp/v1", "bad MCP payload schema")
            _require(bool(payload.get("evidence_contract")), "MCP payload lacks evidence contract")
            stats["mcp_ok"] += 1
            fig_base = output_dir / "figures" / case_id
            pxf.tl.figures(qdata, output_dir=fig_base / "png", format="png")
            _require(all(Path(item).read_bytes().startswith(b"\x89PNG") for item in qdata.uns["figure_outputs"]), "PNG figure output invalid")
            stats["png_figure_ok"] += 1
            pxf.tl.figures(qdata, output_dir=fig_base / "svg", format="svg")
            _require(all(Path(item).read_text(encoding="utf-8").startswith("<svg") for item in qdata.uns["figure_outputs"]), "SVG figure output invalid")
            stats["svg_figure_ok"] += 1
            if len(stats["sample_outputs"]) < 3:
                stats["sample_outputs"].append(
                    {
                        "case_id": case_id,
                        "query": query,
                        "html": str(output_dir / f"{case_id}.html"),
                        "figure_kinds": [spec.get("kind") for spec in answer.figures],
                        "summary_source": answer.summary_source,
                        "summary_preview": answer.summary[:220],
                    }
                )
        except Exception as exc:
            failure_sink.append({"dataset": name, "case_id": case_id, "query": query, "error": f"{type(exc).__name__}: {exc}"})
    return stats


def _validate_cli(package_root: Path, project_root: Path, env_file: str | None, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    query = "What pathways are affected by doxorubicin in A549 cells?"
    env = os.environ.copy()
    env["PYTHONPATH"] = str(package_root / "src")
    base_cmd = [sys.executable, "-m", "pxfquery.cli"]
    if env_file:
        base_cmd.extend(["--env-file", str(Path(env_file).resolve())])
    html_path = output_dir / "cli_report.html"
    figure_dir = output_dir / "figures"
    answer = subprocess.run(base_cmd + ["answer", query, "--mode", "mcp"], cwd=package_root, env=env, text=True, capture_output=True, timeout=120)
    html_run = subprocess.run(base_cmd + ["answer", query, "--mode", "html", "--output", str(html_path)], cwd=package_root, env=env, text=True, capture_output=True, timeout=120)
    fig_run = subprocess.run(base_cmd + ["figures", query, "--output-dir", str(figure_dir), "--format", "png"], cwd=package_root, env=env, text=True, capture_output=True, timeout=120)
    chat_run = subprocess.run(base_cmd + ["chat", query, "请用中文解释主要证据和限制。"], cwd=package_root, env=env, text=True, capture_output=True, timeout=120)
    return {
        "answer_returncode": answer.returncode,
        "answer_stdout_prefix": answer.stdout[:240],
        "html_returncode": html_run.returncode,
        "html_exists": html_path.exists(),
        "html_has_svg": html_path.exists() and "<svg" in html_path.read_text(encoding="utf-8"),
        "figures_returncode": fig_run.returncode,
        "figure_files": sorted(str(path) for path in figure_dir.glob("*.png")),
        "figure_png_valid": all(path.read_bytes().startswith(b"\x89PNG") for path in figure_dir.glob("*.png")),
        "chat_returncode": chat_run.returncode,
        "chat_stdout_len": len(chat_run.stdout),
        "chat_stdout_prefix": chat_run.stdout[:240],
        "stderr": (answer.stderr + html_run.stderr + fig_run.stderr + chat_run.stderr)[-1000:],
    }


async def _validate_mcp(package_root: Path, project_root: Path, env_file: str | None, output_dir: Path) -> dict[str, Any]:
    from mcp import ClientSession
    from mcp.client.stdio import StdioServerParameters, stdio_client

    output_dir.mkdir(parents=True, exist_ok=True)
    env = {"PYTHONPATH": str(package_root / "src")}
    args = ["-m", "pxfquery.mcp_server"]
    if env_file:
        args.extend(["--env-file", str(Path(env_file).resolve())])
    server = StdioServerParameters(command=sys.executable, args=args, env=env)
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            names = [tool.name for tool in tools.tools]
            answer = await session.call_tool("pxfquery_parse_answer", {"text": "What pathways are affected by doxorubicin in A549 cells?", "top_n": 5})
            answer_payload = json.loads(answer.content[0].text)
            figures = await session.call_tool(
                "pxfquery_render_figures",
                {
                    "text": "What pathways are affected by doxorubicin in A549 cells?",
                    "output_dir": str(output_dir / "figures"),
                    "top_n": 5,
                    "figure_format": "png",
                },
            )
            figure_payload = json.loads(figures.content[0].text)
            chat = await session.call_tool(
                "pxfquery_l5_chat",
                {
                    "text": "What pathways are affected by doxorubicin in A549 cells?",
                    "message": "请用中文解释主要证据和限制。",
                    "top_n": 5,
                },
            )
            chat_payload = json.loads(chat.content[0].text)
            return {
                "tools": names,
                "answer_schema": answer_payload.get("schema_version"),
                "has_evidence_contract": bool(answer_payload.get("evidence_contract")),
                "figure_count": len(figure_payload.get("files", [])),
                "figure_png_valid": all(Path(path).read_bytes().startswith(b"\x89PNG") for path in figure_payload.get("files", [])),
                "chat_schema": chat_payload.get("schema_version"),
                "chat_answer_len": len(chat_payload.get("answer", "")),
            }


def _validate_deepseek_chat(source_path: Path, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    data = json.loads(source_path.read_text(encoding="utf-8"))
    row = next(item for item in data["records"] if item.get("evidence_dossier"))
    pxf = PxFQuery()
    qdata = pxf.read.query(row["query"])
    qdata.uns["evidence_dossier"] = row["evidence_dossier"]
    qdata.uns["result"] = row["evidence_dossier"]
    pxf.tl.answer(qdata)
    pxf.tl.chat(qdata, "请用中文解释主要证据和限制。", print_response=False)
    result = {
        "query": row["query"],
        "chat_history_len": len(pxf.get.chat_history(qdata)),
        "answer_len": len(pxf.get.chat(qdata)),
        "answer_preview": pxf.get.chat(qdata)[:240],
        "provider_status": pxf.settings.llm_provider_status(),
    }
    (output_dir / "deepseek_chat_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def _compact_report(report: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": report["schema_version"],
        "datasets": {
            key: {k: value for k, value in stats.items() if k not in {"sample_outputs", "source"}}
            for key, stats in report["datasets"].items()
        },
        "entrypoints": report["entrypoints"],
        "failure_count": len(report["failures"]),
        "elapsed_seconds": report.get("elapsed_seconds"),
    }


def _load_env_file(path: str | os.PathLike[str]) -> None:
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ[key.strip()] = value.strip()


def _require(condition: Any, message: str) -> None:
    if not condition:
        raise AssertionError(message)


if __name__ == "__main__":
    raise SystemExit(main())
