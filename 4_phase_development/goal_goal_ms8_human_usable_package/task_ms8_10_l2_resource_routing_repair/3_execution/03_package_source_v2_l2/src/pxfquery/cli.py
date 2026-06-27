from __future__ import annotations

import argparse
import json
import sys

from pxfquery import PxFQuery


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    sub = parser.add_subparsers(dest="command", required=True)

    parse_cmd = sub.add_parser("parse")
    parse_cmd.add_argument("text", nargs="?")

    query_cmd = sub.add_parser("query")
    query_cmd.add_argument("text")
    query_cmd.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    if args.command == "parse":
        if not args.text:
            parser.error("parse requires text")
        client = PxFQuery()
        qdata = client.read.query(args.text)
        client.pp.parse(qdata)
        print(json.dumps(client.get.intent(qdata), ensure_ascii=False, indent=2))
        return 0
    if args.command == "query":
        if args.json:
            payload = PxFQuery().query(args.text)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            client = PxFQuery()
            print(client.ask(args.text))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
