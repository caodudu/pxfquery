from __future__ import annotations

import argparse
import json
import os
import sys

from .core import PxFquery


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    subparsers = parser.add_subparsers(dest="command", required=True)

    forward = subparsers.add_parser("forward")
    forward.add_argument("--perturbation", "-p", required=True)
    forward.add_argument("--cell-line", "-c", required=True)
    forward.add_argument("--matrix", "-m", default=os.environ.get("PXFQUERY_MATRIX_PATH"))
    forward.add_argument("--matrix-type", "-t", default=os.environ.get("PXFQUERY_MATRIX_TYPE", "xpr"))
    forward.add_argument("--top-k", type=int, default=20)
    forward.add_argument("--compact", action="store_true")

    info = subparsers.add_parser("info")
    info.add_argument("--detail", action="store_true")

    args = parser.parse_args(argv)

    if args.command == "info":
        print("pxfquery 0.1.0")
        if args.detail:
            print("M1 forward query core; matrix types: xpr, sh, cp")
        return 0

    if args.command == "forward":
        if not args.matrix:
            result = {
                "error": "NoMatrixLoaded",
                "message": "No functional matrix is loaded. Provide --matrix or PXFQUERY_MATRIX_PATH.",
                "query_type": "system",
            }
            _print_json(result, args.compact)
            return 1
        try:
            query = PxFquery(args.matrix, matrix_type=args.matrix_type)
            result = query.pert2func(args.perturbation, args.cell_line, args.matrix_type, args.top_k)
        except FileNotFoundError as exc:
            result = {"error": "FileNotFound", "message": str(exc), "query_type": "system"}
            _print_json(result, args.compact)
            return 1
        _print_json(result, args.compact)
        if result.get("error") in {"PerturbationNotFound", "ContextNotFound"}:
            return 2
        if result.get("error"):
            return 1
        return 0

    return 1


def _print_json(result: dict, compact: bool) -> None:
    if compact:
        print(json.dumps(result, separators=(",", ":"), ensure_ascii=False))
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
