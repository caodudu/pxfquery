"""
build_gene_index.py
===================
构建基因查询索引：
  中间产物（一次性）：
    output/store/genePT/gene_embedding_m3_filtered.npz   (33791×3072 float32)
    output/store/genePT/gene_names_m3_filtered.csv        (33791 行)
  完整索引：
    output/store/query_index/gene_index.json
      格式：{lowercase_symbol: {symbol, gene_type, in_matrix}}
    output/store/query_index/gene_neighbors.json
      格式：{symbol: [[neighbor_symbol, cosine_int], ...]}
  简化索引（--step simplify 生成，从完整索引派生）：
    output/store/query_index/gene_index_simple.json
      格式：{UPPERCASE_SYMBOL: type_code}
      类型码：pc=protein_coding, mir=miRNA, snr=snRNA, misc=misc_RNA
      不含 lncRNA、伪基因等；resolver 查询前需 .upper()
    output/store/query_index/gene_neighbors_simple.json
      格式与 gene_neighbors.json 相同，但排除 lncRNA query 基因

运行：
  python script/word_new/3_gene_index/build_gene_index.py [--step extract|index|neighbors|simplify|all] [--demo]

--demo：使用极小子集（extract 取 500 基因，neighbors 取前 50 行），用于验证逻辑是否正确。
"""

import argparse
import gzip
import json
import pickle
import re
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd

# ── 路径配置（相对于 workspace/ 运行）────────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parents[3]

INPUT_M3_PICKLE = WORKSPACE / "input" / "genePT" / "GenePT_gene_protein_embedding_model_3_text.pickle"
INPUT_GTF       = WORKSPACE / "input" / "genePT" / "gencode.v49.annotation.gtf.gz"
INPUT_GENE_INFO = WORKSPACE / "input" / "cmap" / "gene_info_beta.csv"
INPUT_XPR       = WORKSPACE / "output" / "store" / "gsea_anndata" / "xpr_func_ad.h5ad"
INPUT_SH        = WORKSPACE / "output" / "store" / "gsea_anndata" / "sh_func_ad.h5ad"

# 中间产物放 output/store/genePT/（input/ 只读）
OUTPUT_NPZ      = WORKSPACE / "output" / "store" / "genePT" / "gene_embedding_m3_filtered.npz"
OUTPUT_NAMES    = WORKSPACE / "output" / "store" / "genePT" / "gene_names_m3_filtered.csv"

OUTPUT_INDEX    = WORKSPACE / "output" / "store" / "query_index" / "gene_index.json"
OUTPUT_NEIGHBORS = WORKSPACE / "output" / "store" / "query_index" / "gene_neighbors.json"
OUTPUT_INDEX_SIMPLE    = WORKSPACE / "output" / "store" / "query_index" / "gene_index_simple.json"
OUTPUT_NEIGHBORS_SIMPLE = WORKSPACE / "output" / "store" / "query_index" / "gene_neighbors_simple.json"
LOG_PATH        = WORKSPACE / "report" / "3_gene_index.md"

# 简化版保留的类型 → 短码
TYPE_SHORT = {
    "protein_coding": "pc",
    "miRNA":          "mir",
    "snRNA":          "snr",
    "misc_RNA":       "misc",
}

PAT_NUCLEOTIDE = re.compile(r"^[ACGTN]{4,8}$")
TOP_N = 50


# ── 共用数据加载 ─────────────────────────────────────────────────────────────

def get_valid_matrix_genes() -> set[str]:
    """从 xpr/sh h5ad 读取 cmap_name，过滤无效条目。"""
    xpr = ad.read_h5ad(INPUT_XPR)
    sh  = ad.read_h5ad(INPUT_SH)
    all_genes = (
        set(xpr.obs["cmap_name"].dropna().unique())
        | set(sh.obs["cmap_name"].dropna().unique())
    )
    return {
        g for g in all_genes
        if re.match(r"^[A-Za-z]", g)        # 必须字母开头（过滤 -666 等）
        and not PAT_NUCLEOTIDE.match(g)      # 排除 shRNA guide 序列
        and "_" not in g                     # 排除实验对照/复合构建体
        and "/" not in g
    }


def get_gencode_name2type() -> dict[str, str]:
    """从 Gencode v49 GTF 解析 gene_name → gene_type。"""
    name2type: dict[str, str] = {}
    with gzip.open(INPUT_GTF, "rt") as f:
        for line in f:
            if line.startswith("#"):
                continue
            parts = line.split("\t")
            if parts[2] != "gene":
                continue
            attrs = parts[8]
            gn = re.search(r'gene_name "([^"]+)"', attrs)
            gt = re.search(r'gene_type "([^"]+)"', attrs)
            if gn and gt:
                name2type[gn.group(1)] = gt.group(1)
    return name2type


# ── Step 0：model-3 pickle 过滤提取 → npz ─────────────────────────────────

def step_extract(demo: bool = False, verbose: bool = True) -> None:
    """
    加载 model-3 pickle，过滤到 (Gencode v49 ∪ 有效矩阵基因) ∩ model-3。
    保存为 npz + gene_names csv。
    demo=True 时只取 500 个基因（快速验证逻辑）。
    已存在且非 demo 则跳过。
    """
    if OUTPUT_NPZ.exists() and OUTPUT_NAMES.exists() and not demo:
        if verbose:
            names = pd.read_csv(OUTPUT_NAMES, header=None)[0].tolist()
            print(f"[extract] 已存在，跳过。gene_names: {len(names)}")
        return

    if verbose:
        print("[extract] 加载 model-3 pickle...", flush=True)

    with open(INPUT_M3_PICKLE, "rb") as f:
        m3: dict[str, list] = pickle.load(f)

    gc_name2type = get_gencode_name2type()
    valid_genes  = get_valid_matrix_genes()
    gc_names     = set(gc_name2type.keys())
    target       = sorted((gc_names | valid_genes) & set(m3.keys()))

    if demo:
        target = target[:500]
        if verbose:
            print(f"[extract][DEMO] 截取前 500 个基因（共 {len(target)} 个）")

    if verbose:
        print(f"[extract] model-3 总: {len(m3)}, 过滤后目标: {len(target)}", flush=True)

    matrix = np.array([m3[g] for g in target], dtype=np.float32)

    OUTPUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(OUTPUT_NPZ, data=matrix)
    pd.Series(target).to_csv(OUTPUT_NAMES, index=False, header=False)

    if verbose:
        print(f"[extract] 保存 npz: {matrix.shape}")
        print(f"[save] {OUTPUT_NPZ}")
        print(f"[save] {OUTPUT_NAMES}")


# ── Step 1：gene_index.json ──────────────────────────────────────────────────

def step_index(verbose: bool = True) -> None:
    """
    构建 lowercase(symbol) → {symbol, gene_type, in_matrix} 索引。

    gene_type 来自 Gencode v49 GTF（protein_coding / lncRNA / miRNA 等），
    in_matrix 标记该基因是否在 xpr/sh 矩阵中有实验数据。
    来自 gene_info_beta 但不在 Gencode 的基因，gene_type 为 null。

    优先级（处理重名冲突）：
      1. 有效矩阵基因（in_matrix=True，直接有数据）
      2. Gencode v49（规范 symbol + gene_type）
      3. gene_info_beta（补充 LINCS 基因）
    """
    gc_name2type = get_gencode_name2type()
    valid_genes  = get_valid_matrix_genes()
    gi_symbols   = set(pd.read_csv(INPUT_GENE_INFO)["gene_symbol"].dropna().unique())

    index: dict[str, dict] = {}
    conflicts = 0

    def add(symbols, get_type_fn, in_matrix_fn, label):
        nonlocal conflicts
        added = 0
        for sym in symbols:
            key = sym.lower()
            if key not in index:
                index[key] = {
                    "symbol": sym,
                    "gene_type": get_type_fn(sym),
                    "in_matrix": in_matrix_fn(sym),
                }
                added += 1
            else:
                conflicts += 1
        if verbose:
            print(f"[index] {label}: {len(list(symbols))} 个 → 新增 {added} 条", flush=True)

    # 优先级 1：有效矩阵基因
    add(
        sorted(valid_genes),
        lambda g: gc_name2type.get(g),
        lambda _: True,
        "有效矩阵基因（优先级1）",
    )
    # 优先级 2：Gencode v49
    add(
        sorted(gc_name2type.keys()),
        lambda g: gc_name2type.get(g),
        lambda g: g in valid_genes,
        "Gencode v49（优先级2）",
    )
    # 优先级 3：gene_info_beta
    add(
        sorted(gi_symbols),
        lambda g: gc_name2type.get(g),
        lambda g: g in valid_genes,
        "gene_info_beta（优先级3）",
    )

    OUTPUT_INDEX.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, separators=(",", ":"))

    if verbose:
        n_in_matrix = sum(1 for v in index.values() if v["in_matrix"])
        type_counts: dict[str, int] = {}
        for v in index.values():
            t = v["gene_type"] or "unknown"
            type_counts[t] = type_counts.get(t, 0) + 1
        top_types = sorted(type_counts.items(), key=lambda x: -x[1])[:8]
        print(f"[index] 最终条目: {len(index)}, in_matrix: {n_in_matrix}, 冲突跳过: {conflicts}")
        print(f"[index] gene_type top-8: {top_types}")
        print(f"[save] {OUTPUT_INDEX}")


# ── Step 2：gene_neighbors.json ──────────────────────────────────────────────

def step_neighbors(demo: bool = False, verbose: bool = True) -> None:
    """
    对 filtered npz 中每个基因，计算与「有效矩阵基因候选池」的余弦相似度，
    取 top-50，压缩存储为 [[symbol, cosine×100], ...]。

    demo=True 时只处理前 50 行，快速验证输出格式是否正确。
    """
    if not OUTPUT_NPZ.exists():
        raise FileNotFoundError(f"先运行 --step extract，缺少 {OUTPUT_NPZ}")

    gene_names = pd.read_csv(OUTPUT_NAMES, header=None)[0].tolist()
    matrix = np.load(OUTPUT_NPZ)["data"].astype(np.float32)   # (N, 3072)
    N = len(gene_names)

    valid_genes = get_valid_matrix_genes()

    # 候选池：有效矩阵基因 ∩ filtered names
    name2idx  = {g: i for i, g in enumerate(gene_names)}
    cand_genes = [g for g in gene_names if g in valid_genes]
    cand_idx   = [name2idx[g] for g in cand_genes]
    C = len(cand_idx)
    cand_pos   = {gi: li for li, gi in enumerate(cand_idx)}  # global_idx → local_idx

    if verbose:
        print(f"[neighbors] 嵌入矩阵: {matrix.shape}")
        print(f"[neighbors] 候选池（矩阵∩filtered）: {C}")
        print(f"[neighbors] 有效矩阵基因 NOT in filtered: {len(valid_genes) - C}")

    # 余弦相似度：先 L2 归一化，再做点积
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    normed = matrix / norms                      # (N, 3072)，单位向量
    cand_normed = normed[cand_idx]               # (C, 3072)
    cand_gene_arr = np.array(cand_genes)

    process_range = range(0, min(50, N) if demo else N)
    if demo and verbose:
        print(f"[neighbors][DEMO] 只处理前 {min(50, N)} 行")

    BATCH = 1000
    neighbors: dict[str, list] = {}

    for batch_start in range(process_range.start, process_range.stop, BATCH):
        batch_end  = min(batch_start + BATCH, process_range.stop)
        sims = normed[batch_start:batch_end] @ cand_normed.T   # (B, C)

        for local_i, global_i in enumerate(range(batch_start, batch_end)):
            sim_row = sims[local_i].copy()

            # 排除自身
            if global_i in cand_pos:
                sim_row[cand_pos[global_i]] = -1.0

            top_idx = np.argpartition(sim_row, -min(TOP_N, C))[-min(TOP_N, C):]
            top_idx = top_idx[np.argsort(-sim_row[top_idx])]

            nbrs = [
                [cand_gene_arr[ci], round(float(sim_row[ci]) * 100)]
                for ci in top_idx
                if sim_row[ci] > 0
            ]
            neighbors[gene_names[global_i]] = nbrs

        if verbose and (batch_end % 5000 == 0 or batch_end == process_range.stop):
            print(f"  [{batch_end}/{process_range.stop}] done", flush=True)

    OUTPUT_NEIGHBORS.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_NEIGHBORS, "w", encoding="utf-8") as f:
        json.dump(neighbors, f, ensure_ascii=False, separators=(",", ":"))

    if verbose:
        n_with = sum(1 for v in neighbors.values() if v)
        avg = sum(len(v) for v in neighbors.values()) / len(neighbors) if neighbors else 0
        print(f"[neighbors] 条目: {len(neighbors)}, 有近邻: {n_with}, 平均近邻数: {avg:.1f}")
        if neighbors:
            sample_key = next(iter(neighbors))
            print(f"[neighbors] 样例 {sample_key}: {neighbors[sample_key][:3]}")
        print(f"[save] {OUTPUT_NEIGHBORS}")


# ── Step 3：简化索引 ──────────────────────────────────────────────────────────

def step_simplify(verbose: bool = True) -> None:
    """
    从完整 gene_index.json / gene_neighbors.json 派生两个简化版本：

    gene_index_simple.json
      - key: UPPERCASE symbol（resolver 查询前需 .upper()）
      - value: 类型短码（pc/mir/snr/misc）
      - 只保留 protein_coding, miRNA, snRNA, misc_RNA 四类
      - 去除 lncRNA、伪基因、snoRNA、TEC 等

    gene_neighbors_simple.json
      - 格式同 gene_neighbors.json
      - 排除 lncRNA query 基因（~3472 条）
      - 近邻列表不变（候选池本就几乎全是蛋白编码基因）
    """
    if not OUTPUT_INDEX.exists():
        raise FileNotFoundError(f"先运行 --step index，缺少 {OUTPUT_INDEX}")
    if not OUTPUT_NEIGHBORS.exists():
        raise FileNotFoundError(f"先运行 --step neighbors，缺少 {OUTPUT_NEIGHBORS}")

    with open(OUTPUT_INDEX, encoding="utf-8") as f:
        idx_full = json.load(f)
    with open(OUTPUT_NEIGHBORS, encoding="utf-8") as f:
        nbrs_full = json.load(f)

    # ── gene_index_simple：只保留 TYPE_SHORT 中的类型 ──
    index_simple: dict[str, str] = {}
    for v in idx_full.values():
        short = TYPE_SHORT.get(v["gene_type"])
        if short is not None:
            index_simple[v["symbol"]] = short   # uppercase key

    if verbose:
        from collections import Counter
        cnt = Counter(index_simple.values())
        print(f"[simplify] gene_index_simple: {len(index_simple)} 条")
        for code in ("pc", "mir", "snr", "misc"):
            print(f"  {code}: {cnt.get(code, 0)}")

    OUTPUT_INDEX_SIMPLE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_INDEX_SIMPLE, "w", encoding="utf-8") as f:
        json.dump(index_simple, f, ensure_ascii=False, separators=(",", ":"))
    print(f"[save] {OUTPUT_INDEX_SIMPLE}")

    # ── gene_neighbors_simple：排除 lncRNA query 基因 ──
    sym2type = {v["symbol"]: v["gene_type"] for v in idx_full.values()}
    neighbors_simple = {
        sym: nbrs
        for sym, nbrs in nbrs_full.items()
        if sym2type.get(sym) != "lncRNA"
    }

    if verbose:
        excluded = len(nbrs_full) - len(neighbors_simple)
        avg = sum(len(v) for v in neighbors_simple.values()) / len(neighbors_simple) if neighbors_simple else 0
        print(f"[simplify] gene_neighbors_simple: {len(neighbors_simple)} 条（排除 lncRNA {excluded} 条）")
        print(f"  平均近邻数: {avg:.1f}")

    with open(OUTPUT_NEIGHBORS_SIMPLE, "w", encoding="utf-8") as f:
        json.dump(neighbors_simple, f, ensure_ascii=False, separators=(",", ":"))
    print(f"[save] {OUTPUT_NEIGHBORS_SIMPLE}")


# ── 日志写入 ─────────────────────────────────────────────────────────────────

def write_log(steps_run: list[str], start_time: float, demo: bool) -> None:
    import datetime

    elapsed = time.time() - start_time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    demo_note = "（DEMO 模式，小规模验证）" if demo else ""
    stats = []

    if OUTPUT_NPZ.exists():
        data = np.load(OUTPUT_NPZ)["data"]
        stats.append(f"- `gene_embedding_m3_filtered.npz`: {data.shape[0]}×{data.shape[1]} float32")

    if OUTPUT_INDEX.exists():
        idx = json.loads(OUTPUT_INDEX.read_text(encoding="utf-8"))
        n_in_matrix = sum(1 for v in idx.values() if v.get("in_matrix"))
        stats.append(f"- `gene_index.json`: {len(idx)} 条，其中 in_matrix={n_in_matrix}")

    if OUTPUT_NEIGHBORS.exists():
        nbrs = json.loads(OUTPUT_NEIGHBORS.read_text(encoding="utf-8"))
        n_with = sum(1 for v in nbrs.values() if v)
        avg = sum(len(v) for v in nbrs.values()) / len(nbrs) if nbrs else 0
        stats.append(f"- `gene_neighbors.json`: {len(nbrs)} 个基因，{n_with} 有近邻，平均 {avg:.1f} 个")

    log = f"""# 3_gene_index 运行分析报告 {demo_note}

**时间**: {now}
**执行步骤**: {', '.join(steps_run)}
**总耗时**: {elapsed:.1f}s

---

## 输出统计

{chr(10).join(stats)}

---

## 数据规模参考

| 集合 | 数量 |
|------|------|
| model-3 原始基因 | 133736 |
| Gencode v49 基因 | 77078 |
| 有效矩阵基因（过滤后）| 7966 |
| 提取目标（gc∪matrix ∩ m3）| 33791 |
| 近邻候选池（矩阵∩m3）| 7396 |
| 无嵌入矩阵基因 | 570 |

---

## 读取约定

- gene_index：`gene_index[user_input.lower()]` → `{{symbol, gene_type, in_matrix}}`
- gene_neighbors：`gene_neighbors[symbol]` → `[[gene, cosine_int], ...]`，`cosine = cosine_int / 100`
- 近邻已按 cosine 降序排列

---

## 异常与备注

（如有运行异常在此补充）
"""

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(log, encoding="utf-8")
    print(f"[log] {LOG_PATH}")


# ── 主入口 ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Build gene query index")
    parser.add_argument(
        "--step",
        choices=["extract", "index", "neighbors", "simplify", "all"],
        default="all",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="小规模验证：extract 取 500 基因，neighbors 取前 50 行",
    )
    args = parser.parse_args()

    t0 = time.time()
    steps_run = []

    if args.demo:
        print("=" * 50)
        print("DEMO 模式：小规模验证，不覆盖正式产物")
        print("=" * 50)

    if args.step in ("extract", "all"):
        print("=" * 50)
        print("STEP 0: model-3 过滤提取 → npz")
        print("=" * 50)
        step_extract(demo=args.demo)
        steps_run.append("extract")

    if args.step in ("index", "all"):
        print("=" * 50)
        print("STEP 1: gene_index.json")
        print("=" * 50)
        step_index()
        steps_run.append("index")

    if args.step in ("neighbors", "all"):
        print("=" * 50)
        print("STEP 2: gene_neighbors.json（余弦 top-50）")
        print("=" * 50)
        step_neighbors(demo=args.demo)
        steps_run.append("neighbors")

    if args.step in ("simplify", "all"):
        print("=" * 50)
        print("STEP 3: 简化索引（gene_index_simple + gene_neighbors_simple）")
        print("=" * 50)
        step_simplify()
        steps_run.append("simplify")

    write_log(steps_run, t0, args.demo)
    print(f"\n完成。总耗时 {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
