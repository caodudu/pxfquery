from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="PxFquery resolver MVP demo")
    parser.add_argument("--provider", default="minimax", choices=["minimax", "siliconflow"])
    parser.add_argument("--model", default=None)
    parser.add_argument("--query", default="In A549, what pathways are affected by EGFR knockdown?")
    parser.add_argument("--data-dir", default="output/store/gsea_anndata")
    parser.add_argument("--index-dir", default="output/store/query_index")
    args = parser.parse_args()

    workspace = Path(__file__).resolve().parents[3]
    package_root = workspace / "script"
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))

    # Load .env manually (simple parser) so this demo works without extra deps.
    env_path = workspace / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

    from PxFquery import PxFquery

    pxf = PxFquery()
    pxf.load_data_dir(str(workspace / args.data_dir))
    pxf.enable_resolver(
        index_dir=str(workspace / args.index_dir),
        provider=args.provider,
        model=args.model or ("MiniMax-M2.7" if args.provider == "minimax" else "Qwen/Qwen2.5-72B-Instruct"),
    )

    result = pxf.query(args.query, top_n=10)
    print("=== QUERY ===")
    print(args.query)
    print("=== RESULT TYPE ===")
    print(type(result).__name__)
    if hasattr(result, "resolver_meta"):
        print("=== RESOLVER META ===")
        print(result.resolver_meta)
    if hasattr(result, "summary"):
        print("=== SUMMARY ===")
        summary = str(result.summary)
        try:
            print(summary)
        except UnicodeEncodeError:
            print(summary.encode("utf-8", errors="replace").decode("utf-8", errors="replace"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
