from __future__ import annotations

import argparse
import json
import sys

from pxfquery import PxFQuery
from pxfquery.llm import DEFAULT_PROVIDER, provider_check
from pxfquery.query import parse, query


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    sub = parser.add_subparsers(dest="command", required=True)

    parse_cmd = sub.add_parser("parse")
    parse_cmd.add_argument("text", nargs="?")

    query_cmd = sub.add_parser("query")
    query_cmd.add_argument("text")
    query_cmd.add_argument("--json", action="store_true")

    provider_cmd = sub.add_parser("provider-check")
    provider_cmd.add_argument("--provider", default=DEFAULT_PROVIDER)
    provider_cmd.add_argument("--mode", default="real", choices=["real", "disabled", "fallback"])
    provider_cmd.add_argument("--prompt", default="Return JSON with key pxfquery_provider_check and value ok.")
    provider_cmd.add_argument("--timeout", type=float, default=20.0)
    provider_cmd.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    if args.command == "parse":
        if not args.text:
            parser.error("parse requires text")
        print(json.dumps(parse(args.text), ensure_ascii=False, indent=2))
        return 0
    if args.command == "query":
        if args.json:
            payload = query(args.text)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            client = PxFQuery()
            print(client.ask(args.text))
        return 0
    if args.command == "provider-check":
        result = provider_check(provider=args.provider, mode=args.mode, prompt=args.prompt, timeout=args.timeout).to_dict()
        print(json.dumps(result, ensure_ascii=False, indent=2 if args.json else None))
        return 0 if args.mode != "real" or result["real_provider_success"] else 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
