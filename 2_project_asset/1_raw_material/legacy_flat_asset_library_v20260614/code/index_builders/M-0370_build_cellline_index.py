"""
build_cellline_index.py — 构建细胞系查询索引

输入:  output/table/cellline_meta_enriched.csv
输出:
  output/store/query_index/cellline_index.json
  output/store/query_index/cellline_neighbors.json

cellline_index.json:
  {"valid_cells": ["A549", "MCF7", ...]}
  — 矩阵里真实存在的所有 cell_iname，用于 L1 精确验证

cellline_neighbors.json:
  {lineage: {disease: {subtype: [cell_iname, ...]}}}
  — LLM 引导式树遍历，每步只看当前层选项

运行：
  cd workspace/
  python script/word_new/4_cellline_index/build_cellline_index.py
"""

import json
from collections import defaultdict
from pathlib import Path

import pandas as pd

# ── 路径 ────────────────────────────────────────────────────────────────────
WORKSPACE    = Path(__file__).resolve().parents[3]
ENRICHED_CSV = WORKSPACE / "output" / "table" / "cellline_meta_enriched.csv"
OUTPUT_DIR   = WORKSPACE / "output" / "store" / "query_index"
INDEX_JSON   = OUTPUT_DIR / "cellline_index.json"
NEIGHBORS_JSON = OUTPUT_DIR / "cellline_neighbors.json"


# ── 清洗规则 ─────────────────────────────────────────────────────────────────

# lineage 合并：把零散的 Cellosaurus 补充节点归入已有 lineage
LINEAGE_MERGE = {
    "brain":            "central_nervous_system",
    "autonomic_ganglia":"central_nervous_system",
    "bone_marrow":      "haematopoietic_and_lymphoid_tissue",
    "peripheral_blood": "haematopoietic_and_lymphoid_tissue",
    "fetal_kidney":     "kidney",
    # 发育相关的正常细胞归入 normal_other
    "blastocyst":       "normal_other",
    "menstrual_fluid":  "normal_other",
    "umbilical_vein":   "normal_other",
    "placenta":         "normal_other",
}

# disease 合并：把 Cellosaurus 补充的孤立 disease 节点归入已有标准名
DISEASE_MERGE = {
    "chronic myelogenous leukemia, bcr-abl1 positive": "leukemia",
}

# 手工修正：元数据明显错误的细胞系，直接指定正确的 (lineage, disease, subtype)
MANUAL_FIX = {
    # HME1 是正常乳腺上皮细胞，disease/subtype 被错误标为 leukemia/AML
    "HME1": ("breast", "normal breast sample", "normal epithelium sample"),
    # OCILY10 是 B 细胞淋巴瘤，lineage 被错误标为 placenta
    "OCILY10": ("haematopoietic_and_lymphoid_tissue", "lymphoma", "b-cell lymphoma"),
}

# subtype 标准化：修复同义不同名
SUBTYPE_NORM = {
    # lung
    "non small cell carcinoma":      "non-small cell lung carcinoma",
    "non small cell lung carcinoma": "non-small cell lung carcinoma",
    "non small cell lung cancer":    "non-small cell lung carcinoma",
    # leukemia AML 同义合并
    "acute myeloid leukemia (aml)":  "acute myelogenous leukemia (aml)",
    # lymphoma
    "lymphoma":                      "b-cell lymphoma",
    # subtype 与 disease 同名（无额外信息）→ carcinoma
    "lung cancer":                   "carcinoma",
    "colon cancer":                  "carcinoma",
    "bone cancer":                   "carcinoma",
}


def normalize(s: str) -> str:
    return str(s).strip().lower() if pd.notna(s) else "unknown"


def effective_fields(row) -> tuple[str, str, str]:
    """返回 (lineage, disease, subtype)，优先用原始字段，unknown 用 Cellosaurus 补充。"""
    name = row["cell_iname"]

    # 手工修正优先级最高
    if name in MANUAL_FIX:
        return MANUAL_FIX[name]

    lin = normalize(row["cell_lineage"])
    dis = normalize(row["primary_disease"])
    sub = normalize(row["subtype"])

    # Cellosaurus 补充
    if lin == "unknown":
        site = str(row.get("cellosaurus_site", "")).strip()
        cel_dis = str(row.get("cellosaurus_disease", "")).strip()
        if site and site not in ("", "NOT_FOUND", "nan"):
            lin = site.lower().replace(" ", "_")
            if cel_dis and cel_dis not in ("", "NOT_FOUND", "nan"):
                dis = cel_dis.lower()

    # lineage 合并
    lin = LINEAGE_MERGE.get(lin, lin)

    # disease 合并
    dis = DISEASE_MERGE.get(dis, dis)

    # subtype 标准化
    sub = SUBTYPE_NORM.get(sub, sub)

    return lin, dis, sub


# ── 主流程 ────────────────────────────────────────────────────────────────────
def main():
    print(f"[input]  {ENRICHED_CSV}")
    df = pd.read_csv(ENRICHED_CSV)
    if "cell_iname.1" in df.columns:
        df = df.drop(columns=["cell_iname.1"])

    # ── cellline_index.json ──────────────────────────────────────────────────
    # 全部 240 个 cell_iname，不管 lineage 是否已知
    valid_cells = sorted(df["cell_iname"].dropna().unique().tolist())
    index_data = {"valid_cells": valid_cells}

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(INDEX_JSON, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print(f"[cellline_index] {len(valid_cells)} cells → {INDEX_JSON}")

    # ── cellline_neighbors.json ──────────────────────────────────────────────
    # 只放能定位 lineage 的细胞系（unknown 且 Cellosaurus 也没查到的跳过）
    tree: dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    skipped = []

    for _, row in df.iterrows():
        lin, dis, sub = effective_fields(row)
        if lin == "unknown":
            skipped.append(row["cell_iname"])
            continue
        tree[lin][dis][sub].append(row["cell_iname"])

    # 转普通 dict
    tree_plain = {
        lin: {
            dis: dict(sub_dict)
            for dis, sub_dict in sorted(dis_dict.items())
        }
        for lin, dis_dict in sorted(tree.items())
    }

    with open(NEIGHBORS_JSON, "w", encoding="utf-8") as f:
        json.dump(tree_plain, f, ensure_ascii=False, indent=2)

    print(f"[cellline_neighbors] → {NEIGHBORS_JSON}")
    print(f"[skipped] {len(skipped)} cells with no lineage info (in index but not in tree)")

    # ── 统计报告 ─────────────────────────────────────────────────────────────
    print("\n=== 树结构统计 ===")
    print(f"{'lineage':<40} {'diseases':>8} {'subtypes':>9} {'cells':>6}")
    print("-" * 68)
    for lin, dis_dict in sorted(tree_plain.items()):
        n_dis  = len(dis_dict)
        n_sub  = sum(len(sd) for sd in dis_dict.values())
        n_cell = sum(len(cells) for sd in dis_dict.values() for cells in sd.values())
        print(f"  {lin:<38} {n_dis:>8} {n_sub:>9} {n_cell:>6}")
    total_cells = sum(
        len(cells)
        for dd in tree_plain.values()
        for sd in dd.values()
        for cells in sd.values()
    )
    print(f"\n  total in tree: {total_cells} cells  |  skipped: {len(skipped)}")

    print("\n=== subtype 层细节（cells > 1 的 disease）===")
    for lin, dis_dict in sorted(tree_plain.items()):
        for dis, sub_dict in sorted(dis_dict.items()):
            n = sum(len(c) for c in sub_dict.values())
            if n <= 1:
                continue
            print(f"\n  [{lin} / {dis}]")
            for sub, cells in sorted(sub_dict.items()):
                print(f"    {sub:<45} {len(cells):>3}  {cells}")

    print("\n[done]")


if __name__ == "__main__":
    main()
