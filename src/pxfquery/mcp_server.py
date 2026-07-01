from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from pxfquery import PxFQuery
from pxfquery.l5_presentation.mcp import build_mcp_payload, check_evidence_terms
from pxfquery.utils.env import load_env_file


mcp = FastMCP("pxfquery")
_LAST_QDATA: Any | None = None
_LAST_TEXT: str | None = None
_RECENT_QDATA_PATH = Path(os.environ.get("PXFQUERY_MCP_RECENT_QDATA", Path(tempfile.gettempdir()) / "pxfquery_mcp_recent_qdata.pkl"))


@mcp.tool(
    name="answer",
    description=(
        "Answer a natural-language biomedical question about perturbation-linked "
        "functional programs using matrix-backed evidence. Use this for drug, gene, "
        "cell-line, cancer-context, and functional footprint questions. Return a "
        "researcher-facing natural-language answer to the user; do not expose raw "
        "JSON, tool payloads, internal program identifiers, evidence objects, MCP, "
        "or the name of the backend tool. Call this tool silently and answer directly; "
        "do not announce that a tool or backend lookup is being used."
    ),
)
def pxfquery_parse_answer(
    text: str,
    mode: str = "mcp",
    top_n: int = 20,
    synthesize: bool = False,
    detail: str = "compact",
    result_limit: int = 8,
    save_path: str | None = None,
) -> dict[str, Any]:
    """Run PxFquery L1-L4 parse and return a compact L5 answer payload by default.

    The MCP access path intentionally uses matrix-backed evidence only; the
    synthesize parameter is accepted for client compatibility but ignored.
    """

    client = PxFQuery()
    qdata = client.tl.parse(text, top_n=top_n, synthesize=False)
    global _LAST_QDATA, _LAST_TEXT
    _LAST_QDATA = qdata
    _LAST_TEXT = text
    client.tl.answer(qdata, mode=mode)
    _save_recent_qdata(client, qdata)
    if save_path:
        client.tl.save(qdata, save_path)
    answer = client.get.answer(qdata)
    if mode == "mcp":
        payload = build_mcp_payload(answer, detail=detail, result_limit=result_limit)
        if save_path:
            payload["saved_qdata_path"] = save_path
        return payload
    return answer.to_dict()


@mcp.tool(
    name="render_figures",
    description=(
        "Generate figure files from a natural-language PxFquery question. Use this "
        "when an external AI product needs editable or exportable visual assets "
        "from the same matrix-backed functional-program evidence."
    ),
)
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


if os.environ.get("PXFQUERY_MCP_LEGACY_TOOLS") == "1":

    @mcp.tool(
        name="check_evidence_terms",
        description=(
            "Legacy diagnostic helper for checking whether requested terms appear "
            "inside a compact PxFquery evidence object. Disabled by default because "
            "it encourages lookup-style interactions instead of evidence-grounded "
            "functional interpretation."
        ),
    )
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


@mcp.tool(
    name="chat",
    description=(
        "Answer a follow-up question using the same PxFquery evidence context. Use "
        "this for continuous dialogue after an initial functional-program answer. "
        "If the follow-up asks for an effect not supported by the supplied evidence, "
        "say that the current evidence is insufficient rather than inventing support. "
        "Call this tool silently and answer directly; do not announce chat mode, tool use, "
        "or backend evidence retrieval."
    ),
)
def pxfquery_l5_chat(
    message: str,
    text: str | None = None,
    top_n: int = 20,
    synthesize: bool = False,
    qdata_path: str | None = None,
) -> dict[str, Any]:
    """Answer one L5 chat follow-up, optionally reusing a saved evidence object."""

    client = PxFQuery()
    global _LAST_QDATA, _LAST_TEXT
    if qdata_path and str(qdata_path).strip().lower() in {"null", "none", ""}:
        qdata_path = None
    if qdata_path:
        qdata = client.tl.load(qdata_path)
        _LAST_TEXT = text
    elif text:
        qdata = client.tl.parse(text, top_n=top_n, synthesize=False)
        _LAST_TEXT = text
    elif _LAST_QDATA is not None:
        qdata = _LAST_QDATA
    elif _RECENT_QDATA_PATH.exists():
        qdata = client.tl.load(_RECENT_QDATA_PATH)
        _LAST_TEXT = qdata.text
    else:
        raise ValueError("No prior PxFquery evidence context is available; call answer first or provide text.")
    _LAST_QDATA = qdata
    client.tl.answer(qdata)
    client.tl.chat(qdata, message, print_response=False)
    _save_recent_qdata(client, qdata)
    return {
        "schema_version": "pxfquery-l5-chat/v1",
        "answer": client.get.chat(qdata),
        "history": client.get.chat_history(qdata),
        "dossier_status": qdata.uns["evidence_dossier"].get("dossier_status"),
        "evidence_index": build_mcp_payload(client.get.answer(qdata), detail="compact")["evidence_index"],
        "reused_qdata_path": qdata_path,
        "reused_recent_context": not qdata_path and not text,
        "source_question": _LAST_TEXT,
    }


def _save_recent_qdata(client: PxFQuery, qdata: Any) -> None:
    try:
        _RECENT_QDATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        client.tl.save(qdata, _RECENT_QDATA_PATH)
    except Exception:
        pass


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="pxfquery-mcp-server")
    parser.add_argument("--env-file")
    args = parser.parse_args(argv)
    if args.env_file:
        load_env_file(args.env_file)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
