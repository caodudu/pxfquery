"""
build_cellline_enrich.py — 用 Cellosaurus API 补充细胞系 lineage/disease 信息

输入:  input/cellline_meta_sub.csv  (240 行，82 个 unknown lineage)
输出:  output/table/cellline_meta_enriched.csv  (不覆盖原文件)

补充策略：
  - cell_lineage == 'unknown' 的细胞系 → 查 Cellosaurus
  - 拿到 site（组织来源）和 disease（疾病名）
  - 新增列：cellosaurus_site, cellosaurus_disease, cellosaurus_category
  - lineage/disease/subtype 原列保留不变（enriched 列另存）

运行：
  cd workspace/
  python script/word_new/4_cellline_index/build_cellline_enrich.py

  --demo 模式（只跑前5个 unknown，验证 API）：
  python script/word_new/4_cellline_index/build_cellline_enrich.py --demo
"""

import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

# ── 路径 ────────────────────────────────────────────────────────────────────
WORKSPACE   = Path(__file__).resolve().parents[3]
INPUT_CSV   = WORKSPACE / "input" / "cellline_meta_sub.csv"
OUTPUT_DIR  = WORKSPACE / "output" / "table"
OUTPUT_CSV  = OUTPUT_DIR / "cellline_meta_enriched.csv"

DELAY = 0.3   # 秒，Cellosaurus API 限速保守值


# ── Cellosaurus 查询 ──────────────────────────────────────────────────────────
def query_cellosaurus(name: str) -> dict | None:
    """
    查询单个细胞系名，返回 {site, disease, category} 或 None（未命中）。

    site: str      组织来源，如 "Lung"
    disease: str   疾病名（取第一个），如 "Lung adenocarcinoma"
    category: str  细胞系类型，如 "Cancer cell line" / "Transformed cell line"
    """
    q = urllib.parse.quote(f'id:"{name}"')
    url = (
        f"https://api.cellosaurus.org/search/cell-line"
        f"?q={q}&format=json&fields=id,ac,sy,di,ca,derived-from-site&nbresults=1"
    )
    try:
        with urllib.request.urlopen(url, timeout=15) as r:
            d = json.loads(r.read())
    except Exception:
        return None

    cells = d.get("Cellosaurus", {}).get("cell-line-list", [])
    if not cells:
        return None

    cl = cells[0]
    diseases = [x["label"] for x in cl.get("disease-list", [])]
    sites    = [s["site"]["value"] for s in cl.get("derived-from-site-list", [])]
    category = cl.get("category", "")

    return {
        "site":     sites[0] if sites else "",
        "disease":  diseases[0] if diseases else "",
        "category": category,
    }


# ── 主流程 ────────────────────────────────────────────────────────────────────
def main(demo: bool = False):
    print(f"[input]  {INPUT_CSV}")
    df = pd.read_csv(INPUT_CSV)

    # 去掉重复列
    if "cell_iname.1" in df.columns:
        df = df.drop(columns=["cell_iname.1"])

    # 新增列（若已存在则保留，重跑时断点续传）
    for col in ["cellosaurus_site", "cellosaurus_disease", "cellosaurus_category"]:
        if col not in df.columns:
            df[col] = ""

    # 只查 lineage == unknown 的行
    targets = df[df["cell_lineage"] == "unknown"].copy()
    print(f"[info]   unknown lineage: {len(targets)} 行")

    if demo:
        targets = targets.head(5)
        print(f"[demo]   只跑前 5 行")

    total = len(targets)
    hit = 0

    for i, (idx, row) in enumerate(targets.iterrows()):
        name = row["cell_iname"]

        # 断点续传：已有结果则跳过
        if pd.notna(df.at[idx, "cellosaurus_site"]) and df.at[idx, "cellosaurus_site"] != "":
            print(f"  [{i+1}/{total}] {name}: skip (already have data)")
            continue

        result = query_cellosaurus(name)

        if result:
            df.at[idx, "cellosaurus_site"]     = result["site"]
            df.at[idx, "cellosaurus_disease"]  = result["disease"]
            df.at[idx, "cellosaurus_category"] = result["category"]
            hit += 1
            print(f"  [{i+1}/{total}] {name}: site={result['site']!r}  disease={result['disease']!r}")
        else:
            df.at[idx, "cellosaurus_site"]     = "NOT_FOUND"
            df.at[idx, "cellosaurus_disease"]  = "NOT_FOUND"
            df.at[idx, "cellosaurus_category"] = "NOT_FOUND"
            print(f"  [{i+1}/{total}] {name}: not found")

        # 每 10 条保存一次（断点续传）
        if (i + 1) % 10 == 0 and not demo:
            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            df.to_csv(OUTPUT_CSV, index=False)
            print(f"  [checkpoint] saved {i+1} rows")

        time.sleep(DELAY)

    # 最终保存
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_CSV, index=False)

    print(f"\n[result] hit {hit}/{total} unknown cells")
    print(f"[output] {OUTPUT_CSV}")

    # 简单统计：补充后 unknown 剩多少
    if not demo:
        still_unknown = (
            (df["cell_lineage"] == "unknown") &
            (df["cellosaurus_site"].isin(["", "NOT_FOUND"]))
        ).sum()
        print(f"[info]   补充后仍无 site 信息: {still_unknown} 行")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true", help="只跑前5个 unknown 验证 API")
    args = parser.parse_args()
    main(demo=args.demo)
