"""
build_cellline_tree.py — 细胞系查询索引构建

输入: input/cellline_meta_sub.csv
输出: output/store/query_index/cellline_tree.json

JSON 结构：
  {
    "tree":  { lineage: { disease: { subtype: [cell_iname, ...] } } },
    "cell_index": { lowercase_name: canonical_cell_iname },
    "meta":  { cell_iname: { lineage, disease, subtype } }
  }

用途（对应 resolver.py 的命中优先级）：
  L1 EXACT       — cell_index 精确匹配
  L2 PROXY_CELL  — meta 反查 → tree 找同 subtype 细胞系
  L3 PROXY_CELL  — meta 反查 → tree 找同 disease 细胞系
  L4 PROXY_CELL  — meta 反查 → tree 找同 lineage 细胞系

运行：
  cd workspace/
  python script/word_new/4_cellline_index/build_cellline_tree.py
"""

import json
import re
from collections import defaultdict
from pathlib import Path

import pandas as pd

# ── 路径 ────────────────────────────────────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parents[3]   # .../workspace
INPUT_CSV  = WORKSPACE / "input" / "cellline_meta_sub.csv"
OUTPUT_DIR = WORKSPACE / "output" / "store" / "query_index"
OUTPUT_JSON = OUTPUT_DIR / "cellline_tree.json"


# ── 工具函数 ─────────────────────────────────────────────────────────────────
def normalize_key(name: str) -> str:
    """小写 + 合并连续空白，用于 cell_index 键。"""
    return re.sub(r"\s+", " ", name.strip().lower())


# ── 主流程 ────────────────────────────────────────────────────────────────────
def main():
    print(f"[input]  {INPUT_CSV}")

    # 1. 读取 CSV
    df = pd.read_csv(INPUT_CSV)
    print(f"[data]   shape={df.shape}, columns={df.columns.tolist()}")

    # cell_iname.1 与 cell_iname 重复，丢弃
    if "cell_iname.1" in df.columns:
        df = df.drop(columns=["cell_iname.1"])

    # 填充缺失值
    for col in ["cell_lineage", "primary_disease", "subtype"]:
        df[col] = df[col].fillna("unknown")

    # 2. 构建 tree: lineage → disease → subtype → [cell_iname]
    tree: dict[str, dict[str, dict[str, list[str]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(list))
    )
    meta: dict[str, dict[str, str]] = {}

    for _, row in df.iterrows():
        cname    = row["cell_iname"]
        lineage  = row["cell_lineage"]
        disease  = row["primary_disease"]
        subtype  = row["subtype"]

        tree[lineage][disease][subtype].append(cname)
        meta[cname] = {"lineage": lineage, "disease": disease, "subtype": subtype}

    # 3. 构建 cell_index: lowercase(name) → canonical cell_iname
    cell_index: dict[str, str] = {}
    alias_conflicts: list[str] = []

    def add_entry(key: str, canonical: str):
        k = normalize_key(key)
        if not k:
            return
        if k in cell_index and cell_index[k] != canonical:
            alias_conflicts.append(f"  '{k}' → '{cell_index[k]}' vs '{canonical}' (kept first)")
            return
        cell_index[k] = canonical

    for _, row in df.iterrows():
        cname = row["cell_iname"]
        add_entry(cname, cname)                        # 主名本身

        alias_raw = row.get("cell_alias", None)
        if pd.notna(alias_raw) and str(alias_raw).strip():
            for alias in str(alias_raw).split("|"):    # 分隔符为 |
                add_entry(alias.strip(), cname)

    # 4. 转换为普通 dict（JSON 可序列化）
    tree_plain = {
        lin: {
            dis: dict(sub_dict)
            for dis, sub_dict in dis_dict.items()
        }
        for lin, dis_dict in tree.items()
    }

    result = {
        "tree": tree_plain,
        "cell_index": cell_index,
        "meta": meta,
    }

    # 5. 写入 JSON
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # 6. 统计报告
    n_cells      = len(df)
    n_lineages   = len(tree_plain)
    n_diseases   = sum(len(v) for v in tree_plain.values())
    n_subtypes   = sum(len(sv) for v in tree_plain.values() for sv in v.values())
    n_index      = len(cell_index)
    size_kb      = OUTPUT_JSON.stat().st_size / 1024

    print(f"\n[tree]")
    print(f"  cell lines : {n_cells}")
    print(f"  lineages   : {n_lineages}")
    print(f"  diseases   : {n_diseases}")
    print(f"  subtypes   : {n_subtypes}")
    print(f"\n[cell_index]")
    print(f"  entries    : {n_index}  (cell_iname + aliases)")

    if alias_conflicts:
        print(f"  conflicts  : {len(alias_conflicts)}")
        for msg in alias_conflicts:
            print(msg)

    print(f"\n[output] {OUTPUT_JSON}  ({size_kb:.1f} KB)")
    print("[done]")


if __name__ == "__main__":
    main()
