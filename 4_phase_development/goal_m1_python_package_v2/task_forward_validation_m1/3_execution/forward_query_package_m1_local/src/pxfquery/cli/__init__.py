from __future__ import annotations

import argparse
import json

from pxfquery.core import PxFquery


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    subparsers = parser.add_subparsers(dest="command", required=True)

    forward = subparsers.add_parser("forward")
    forward.add_argument("--perturbation", required=True)
    forward.add_argument("--cell-line", required=True)
    forward.add_argument("--matrix", required=False)
    forward.add_argument("--manifest", required=False)
    forward.add_argument("--fixture-root", required=False)
    forward.add_argument("--matrix-type", default="xpr")
    forward.add_argument("--top-k", type=int, default=20)
    forward.add_argument("--compact", action="store_true")

    args = parser.parse_args(argv)
    if args.command == "forward":
        query = PxFquery(matrix_path=args.matrix, manifest_path=args.manifest, fixture_root=args.fixture_root, matrix_type=args.matrix_type)
        result = query.pert2func(args.perturbation, args.cell_line, matrix_type=args.matrix_type, top_k=args.top_k)
        print(json.dumps(result, indent=None if args.compact else 2, sort_keys=False))
        return 0 if result.get("found") or result.get("error") is None else 2
    return 2
