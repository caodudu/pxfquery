from __future__ import annotations

import os
import sys
import time
from pathlib import Path


def _load_env(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main() -> int:
    workspace = Path(__file__).resolve().parents[3]
    if str(workspace / "script") not in sys.path:
        sys.path.insert(0, str(workspace / "script"))
    _load_env(workspace / ".env")

    from PxFquery import PxFquery

    pxf = PxFquery()
    pxf.load_data_dir(str(workspace / "output/store/gsea_anndata"))
    pxf.enable_resolver(
        index_dir=str(workspace / "output/store/query_index"),
        provider="minimax",
        model=os.getenv("MINIMAX_MODEL", "MiniMax-M2.7"),
        summary_include_numbers=False,
    )

    cases = [
        {
            "id": "C1_exact_genetic",
            "q": "In A549, what pathways are affected by EGFR knockdown?",
            "expect_pert_type": ("xpr", "sh"),
            "expect_hit": ("EXACT", "PROXY_CELL", "PROXY_PERT", "PROXY_BOTH"),
        },
        {
            "id": "C2_disease_context",
            "q": "In non-small cell lung carcinoma, what happens if EGFR is suppressed?",
            "expect_pert_type": ("xpr", "sh"),
            "expect_hit": ("PROXY_CELL", "PROXY_BOTH", "NOT_FOUND", "EXACT"),
        },
        {
            "id": "C3_drug_query",
            "q": "In A549, what pathways change after erlotinib treatment?",
            "expect_pert_type": ("cp",),
            "expect_hit": ("EXACT", "PROXY_PERT", "PROXY_CELL", "PROXY_BOTH", "NOT_FOUND"),
        },
        {
            "id": "C4_drug_generic",
            "q": "In A549, what pathways are affected by an EGFR inhibitor?",
            "expect_pert_type": ("cp",),
            "expect_hit": ("EXACT", "PROXY_PERT", "PROXY_CELL", "PROXY_BOTH", "NOT_FOUND"),
        },
    ]

    ok = 0
    for c in cases:
        try:
            t0 = time.perf_counter()
            res = pxf._resolver.resolve_and_query(c["q"], top_n=10, summarize=False)  # type: ignore[attr-defined]
            dt = time.perf_counter() - t0
            meta = getattr(res, "resolver_meta", {}) or {}
            pt = meta.get("pert_type")
            hit = meta.get("hit_level")
            pass_pt = pt in c["expect_pert_type"]
            pass_hit = hit in c["expect_hit"]
            passed = pass_pt and pass_hit
            ok += int(passed)
            print(
                f"[{c['id']}] pass={passed} time={dt:.3f}s pert_type={pt} hit={hit} "
                f"selected_source={meta.get('selected_source')}"
            )
            if not pass_pt:
                print(f"  expected pert_type in {c['expect_pert_type']}")
            if not pass_hit:
                print(f"  expected hit in {c['expect_hit']}")
        except Exception as e:
            print(f"[{c['id']}] pass=False error={type(e).__name__}: {e}")

    print(f"passed {ok}/{len(cases)}")
    return 0 if ok == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(main())
