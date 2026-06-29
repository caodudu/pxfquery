from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from pxfquery import PxFQuery


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    parser.add_argument("--env-file")
    sub = parser.add_subparsers(dest="command", required=True)

    parse_cmd = sub.add_parser("parse")
    parse_cmd.add_argument("text", nargs="?")

    query_cmd = sub.add_parser("query")
    query_cmd.add_argument("text")
    query_cmd.add_argument("--json", action="store_true")

    answer_cmd = sub.add_parser("answer")
    answer_cmd.add_argument("text")
    answer_cmd.add_argument("--mode", choices=["python", "cli", "html", "mcp"], default="cli")
    answer_cmd.add_argument("--output")

    chat_cmd = sub.add_parser("chat")
    chat_cmd.add_argument("text")
    chat_cmd.add_argument("message")

    figures_cmd = sub.add_parser("figures")
    figures_cmd.add_argument("text")
    figures_cmd.add_argument("--output-dir", required=True)
    figures_cmd.add_argument("--format", choices=["png", "svg"], default="png")

    mcp_cmd = sub.add_parser("mcp-server")
    mcp_cmd.add_argument("--env-file")

    args = parser.parse_args(argv)
    if args.env_file:
        _load_env_file(args.env_file)
    if args.command == "parse":
        if not args.text:
            parser.error("parse requires text")
        client = PxFQuery()
        qdata = client.read.query(args.text)
        client.pp.parse(qdata)
        print(json.dumps(client.get.intent(qdata), ensure_ascii=False, indent=2))
        return 0
    if args.command == "query":
        payload = PxFQuery().query(args.text)
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    if args.command == "answer":
        client = PxFQuery()
        qdata = client.tl.parse(args.text)
        client.tl.answer(qdata, mode=args.mode, output=args.output)
        answer = client.get.answer(qdata)
        if args.mode == "html":
            if args.output:
                print(args.output)
            else:
                print(answer.html)
        elif args.mode == "mcp":
            print(json.dumps(answer.mcp, ensure_ascii=False, indent=2))
        else:
            print(str(answer))
        return 0
    if args.command == "chat":
        client = PxFQuery()
        qdata = client.tl.parse(args.text)
        client.tl.answer(qdata)
        client.tl.chat(qdata, args.message, print_response=True)
        return 0
    if args.command == "figures":
        client = PxFQuery()
        qdata = client.tl.parse(args.text)
        client.tl.answer(qdata)
        client.tl.figures(qdata, output_dir=args.output_dir, format=args.format)
        print(json.dumps(qdata.uns["figure_outputs"], ensure_ascii=False, indent=2))
        return 0
    if args.command == "mcp-server":
        from pxfquery.mcp_server import main as mcp_main

        mcp_args = []
        if args.env_file:
            mcp_args.extend(["--env-file", args.env_file])
        mcp_main(mcp_args)
        return 0
    return 1


def _load_env_file(path: str | os.PathLike[str]) -> None:
    env_path = Path(path)
    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        os.environ[key.strip()] = value.strip()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
