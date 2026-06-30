from __future__ import annotations

import argparse
from typing import Any

from mcp.server.fastmcp import FastMCP

from pxfquery import PxFQuery
from pxfquery.l5_presentation.mcp import build_mcp_payload, check_evidence_terms
from pxfquery.utils.env import load_env_file


mcp = FastMCP("pxfquery")


@mcp.tool()
def pxfquery_parse_answer(
    text: str,
    mode: str = "mcp",
    top_n: int = 20,
    synthesize: bool = False,
    detail: str = "compact",
    result_limit: int = 8,
    save_path: str | None = None,
) -> dict[str, Any]:
    """Run PxFquery L1-L4 parse and return a compact L5 answer payload by default."""

    client = PxFQuery()
    qdata = client.tl.parse(text, top_n=top_n, synthesize=synthesize)
    client.tl.answer(qdata, mode=mode)
    if save_path:
        client.tl.save(qdata, save_path)
    answer = client.get.answer(qdata)
    if mode == "mcp":
        payload = build_mcp_payload(answer, detail=detail, result_limit=result_limit)
        if save_path:
            payload["saved_qdata_path"] = save_path
        return payload
    return answer.to_dict()


@mcp.tool()
def pxfquery_render_figures(text: str, output_dir: str, top_n: int = 20, figure_format: str = "png") -> dict[str, Any]:
    """Run PxFquery L1-L4 parse and write L5 figure files."""

    client = PxFQuery()
    qdata = client.tl.parse(text, top_n=top_n)
    client.tl.answer(qdata)
    client.tl.figures(qdata, output_dir=output_dir, format=figure_format)
    return {
        "schema_version": "pxfquery-l5-figures/v1",
        "output_dir": output_dir,
        "figure_format": figure_format,
        "files": qdata.uns["figure_outputs"],
        "dossier_status": qdata.uns["evidence_dossier"].get("dossier_status"),
    }


@mcp.tool()
def pxfquery_check_evidence_terms(
    text: str,
    terms: list[str],
    top_n: int = 20,
    synthesize: bool = False,
    qdata_path: str | None = None,
) -> dict[str, Any]:
    """Check whether specific terms appear in the compact evidence object without returning full L4 JSON."""

    client = PxFQuery()
    qdata = client.tl.load(qdata_path) if qdata_path else client.tl.parse(text, top_n=top_n, synthesize=synthesize)
    client.tl.answer(qdata)
    return check_evidence_terms(client.get.answer(qdata), terms)


@mcp.tool()
def pxfquery_l5_chat(
    text: str,
    message: str,
    top_n: int = 20,
    synthesize: bool = False,
    qdata_path: str | None = None,
) -> dict[str, Any]:
    """Answer one L5 chat follow-up, optionally reusing a saved evidence object."""

    client = PxFQuery()
    qdata = client.tl.load(qdata_path) if qdata_path else client.tl.parse(text, top_n=top_n, synthesize=synthesize)
    client.tl.answer(qdata)
    client.tl.chat(qdata, message, print_response=False)
    return {
        "schema_version": "pxfquery-l5-chat/v1",
        "answer": client.get.chat(qdata),
        "history": client.get.chat_history(qdata),
        "dossier_status": qdata.uns["evidence_dossier"].get("dossier_status"),
        "evidence_index": build_mcp_payload(client.get.answer(qdata), detail="compact")["evidence_index"],
        "reused_qdata_path": qdata_path,
    }


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="pxfquery-mcp-server")
    parser.add_argument("--env-file")
    args = parser.parse_args(argv)
    if args.env_file:
        load_env_file(args.env_file)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
