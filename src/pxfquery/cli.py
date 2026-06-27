from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from pxfquery import PxFQuery
from pxfquery.llm import DEFAULT_PROVIDER, provider_check
from pxfquery.query import parse, query, run_corpus, summarize_records, write_jsonl


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    sub = parser.add_subparsers(dest="command", required=True)

    parse_cmd = sub.add_parser("parse")
    parse_cmd.add_argument("text", nargs="?")
    parse_cmd.add_argument("--corpus")
    parse_cmd.add_argument("--jsonl")
    parse_cmd.add_argument("--provider-mode", default="disabled", choices=["real", "disabled", "fallback"])

    query_cmd = sub.add_parser("query")
    query_cmd.add_argument("text")
    query_cmd.add_argument("--provider-mode", default="disabled", choices=["real", "disabled", "fallback"])
    query_cmd.add_argument("--json", action="store_true")

    corpus_cmd = sub.add_parser("run-corpus")
    corpus_cmd.add_argument("--corpus", required=True)
    corpus_cmd.add_argument("--family", action="append", default=[])
    corpus_cmd.add_argument("--provider-mode", default="disabled", choices=["real", "disabled", "fallback"])
    corpus_cmd.add_argument("--jsonl")
    corpus_cmd.add_argument("--summary")

    provider_cmd = sub.add_parser("provider-check")
    provider_cmd.add_argument("--provider", default=DEFAULT_PROVIDER)
    provider_cmd.add_argument("--mode", default="real", choices=["real", "disabled", "fallback"])
    provider_cmd.add_argument("--prompt", default="Return JSON with key ms7_provider_check and value ok.")
    provider_cmd.add_argument("--timeout", type=float, default=20.0)
    provider_cmd.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    if args.command == "parse":
        if args.corpus:
            records = []
            for record in run_corpus(args.corpus, provider_mode=args.provider_mode):
                records.append({"case_id": record["case_id"], "intent": record["intent"]})
            if args.jsonl:
                with Path(args.jsonl).open("w", encoding="utf-8") as fh:
                    for record in records:
                        fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
            print(json.dumps({"total": len(records), "records": records}, ensure_ascii=False, indent=2))
            return 0
        if not args.text:
            parser.error("parse requires text or --corpus")
        print(json.dumps(parse(args.text, provider_mode=args.provider_mode), ensure_ascii=False, indent=2))
        return 0
    if args.command == "query":
        if args.json:
            payload = query(args.text, provider_mode=args.provider_mode)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            client = PxFQuery(provider_mode=args.provider_mode)
            print(client.ask(args.text))
        return 0
    if args.command == "run-corpus":
        records = run_corpus(args.corpus, families=args.family, provider_mode=args.provider_mode)
        summary = summarize_records(records)
        if args.jsonl:
            write_jsonl(records, args.jsonl)
        if args.summary:
            Path(args.summary).write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0 if summary["failed"] == 0 else 1
    if args.command == "provider-check":
        result = provider_check(provider=args.provider, mode=args.mode, prompt=args.prompt, timeout=args.timeout).to_dict()
        print(json.dumps(result, ensure_ascii=False, indent=2 if args.json else None))
        return 0 if args.mode != "real" or result["real_provider_success"] else 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
