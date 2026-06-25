from __future__ import annotations

import argparse
import json
import os

from pxfquery.core import PxFquery


def _emit(result: dict, compact: bool) -> None:
    print(json.dumps(result, separators=(",", ":") if compact else None, indent=None if compact else 2))


def _load_query(matrix: str | None, manifest: str | None, fixture_root: str | None, matrix_type: str) -> PxFquery:
    path = matrix or os.environ.get("PXFQUERY_MATRIX_PATH")
    if manifest:
        return PxFquery(manifest_path=manifest, fixture_root=fixture_root, matrix_type=matrix_type)
    if not path:
        raise FileNotFoundError("--matrix is required when PXFQUERY_MATRIX_PATH is not set")
    return PxFquery(matrix_path=path, matrix_type=matrix_type)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pxfquery")
    subparsers = parser.add_subparsers(dest="command", required=True)

    forward = subparsers.add_parser("forward")
    forward.add_argument("--perturbation", "-p", required=True)
    forward.add_argument("--cell-line", "-c", required=True)
    forward.add_argument("--matrix", "-m")
    forward.add_argument("--manifest")
    forward.add_argument("--fixture-root")
    forward.add_argument("--matrix-type", "-t", default="xpr", choices=["xpr", "sh", "cp"])
    forward.add_argument("--top-k", type=int, default=20)
    forward.add_argument("--compact", action="store_true")

    reverse = subparsers.add_parser("reverse")
    reverse.add_argument("--activate", action="append", default=[])
    reverse.add_argument("--suppress", action="append", default=[])
    reverse.add_argument("--cell-line", "-c", required=True)
    reverse.add_argument("--matrix", "-m")
    reverse.add_argument("--manifest")
    reverse.add_argument("--fixture-root")
    reverse.add_argument("--matrix-type", "-t", default="xpr", choices=["xpr", "sh", "cp"])
    reverse.add_argument("--top-n", type=int, default=10)
    reverse.add_argument("--compact", action="store_true")

    info = subparsers.add_parser("info")
    info.add_argument("--detail", action="store_true")

    args = parser.parse_args(argv)
    try:
        if args.command == "info":
            _emit({"package": "pxfquery", "version": "0.1.0", "matrix_types": ["xpr", "sh", "cp"]}, False)
            return 0
        query = _load_query(args.matrix, args.manifest, args.fixture_root, args.matrix_type)
        if args.command == "reverse":
            result = query.func2pert(args.activate, args.suppress, args.cell_line, args.matrix_type, args.top_n)
        else:
            result = query.pert2func(args.perturbation, args.cell_line, args.matrix_type, args.top_k)
        _emit(result, args.compact)
        return 0 if result.get("found", False) else 2 if "error" in result or result.get("found") is False else 0
    except FileNotFoundError as exc:
        _emit({"error": "FileNotFound", "message": str(exc), "query_type": "system"}, getattr(args, "compact", False))
        return 1
    except ValueError as exc:
        _emit({"error": "InvalidMatrix", "message": str(exc), "query_type": "system"}, getattr(args, "compact", False))
        return 1
    except Exception as exc:  # pragma: no cover
        _emit({"error": "InternalError", "message": str(exc), "query_type": "system"}, getattr(args, "compact", False))
        return 4
