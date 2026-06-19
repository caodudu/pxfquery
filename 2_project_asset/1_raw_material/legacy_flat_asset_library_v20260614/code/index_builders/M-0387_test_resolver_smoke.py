from __future__ import annotations

import os
import sys
from pathlib import Path


def _load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    package_root = workspace / "script"
    if str(package_root) not in sys.path:
        sys.path.insert(0, str(package_root))

    _load_env(workspace / ".env")

    from PxFquery import PxFquery

    pxf = PxFquery()
    pxf.load_data_dir(str(workspace / "output/store/gsea_anndata"))

    # Smoke check 1: resolver object can be created from local indexes.
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider="minimax",
        model="MiniMax-M2.7",
    )

    # Smoke check 2: non-LLM direct paths still work.
    fwd = pxf.pert2func("EGFR", pert_type="xpr", cell_line="A549", top_n=5, summarize=False)
    assert hasattr(fwd, "found"), "Forward query object missing expected fields"

    rev = pxf.func2pert(
        activate=["HALLMARK_APOPTOSIS"],
        suppress=["HALLMARK_MYC_TARGETS_V1"],
        pert_type="xpr",
        cell_line="A549",
        top_k=5,
        summarize=False,
    )
    assert hasattr(rev, "found"), "Reverse query object missing expected fields"

    print("resolver smoke checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
