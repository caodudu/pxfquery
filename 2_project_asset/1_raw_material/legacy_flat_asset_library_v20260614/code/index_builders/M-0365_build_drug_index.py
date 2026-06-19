"""
build_drug_index.py
===================
构建药物查询索引：
  - output/table/cp_meta_enriched.csv        (PubChem 补充 smiles/inchikey/cid)
  - output/store/query_index/drug_index.json  (别名倒排索引)
  - output/store/query_index/drug_neighbors.json (Tanimoto top-50 近邻)

运行：
  python script/word_new/2_cp_index/build_drug_index.py [--step pubchem|fingerprint|index]

依赖：rdkit, pandas, numpy, requests
"""

import argparse
import json
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

# ── 路径配置（相对于 workspace/ 运行）──────────────────────────────────────
WORKSPACE = Path(__file__).resolve().parents[3]  # workspace/
INPUT_CP = WORKSPACE / "input" / "cp_meta_unique.csv"
OUTPUT_ENRICHED = WORKSPACE / "output" / "table" / "cp_meta_enriched.csv"
OUTPUT_INDEX = WORKSPACE / "output" / "store" / "query_index" / "drug_index.json"
OUTPUT_NEIGHBORS = WORKSPACE / "output" / "store" / "query_index" / "drug_neighbors.json"
LOG_PATH = WORKSPACE / "report" / "2_cp_index.md"

PUBCHEM_URL = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/IsomericSMILES,InChIKey/JSON"
PUBCHEM_DELAY = 0.2   # seconds between requests
TOP_N = 50            # top-N neighbors to keep
MORGAN_RADIUS = 2
MORGAN_BITS = 2048


# ── 工具函数 ────────────────────────────────────────────────────────────────

def parse_aliases(aliases_str: str) -> list[str]:
    """分割 aliases 字段，返回非空部分列表。"""
    if pd.isna(aliases_str):
        return []
    return [a.strip() for a in aliases_str.split(";") if a.strip()]


def is_brd_id(s: str) -> bool:
    return bool(re.match(r"^BRD-[A-Z0-9]+$", s, re.IGNORECASE))


def real_names(aliases_str: str) -> list[str]:
    """返回 aliases 中非 BRD-id 的真实名字列表（保留原始大小写）。"""
    return [a for a in parse_aliases(aliases_str) if not is_brd_id(a)]


def query_pubchem(name: str) -> dict:
    """
    查询 PubChem REST API，返回 {"smiles": ..., "inchikey": ..., "cid": ...}。
    查不到返回全 None。
    """
    url = PUBCHEM_URL.format(name=requests.utils.quote(name))
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            props = resp.json()["PropertyTable"]["Properties"][0]
            return {
                "smiles": props.get("IsomericSMILES") or props.get("SMILES"),
                "inchikey": props.get("InChIKey"),
                "cid": props.get("CID"),  # auto-included in response
            }
    except Exception:
        pass
    return {"smiles": None, "inchikey": None, "cid": None}


# ── Step 1 + 2：过滤有真实名字的药物，批量查 PubChem ─────────────────────

def step_pubchem(verbose: bool = True) -> pd.DataFrame:
    """
    读取 cp_meta_unique.csv，过滤有真实名字的药物，查 PubChem 补充 smiles。
    支持断点续传（cp_meta_enriched.csv 已存在时跳过已有 smiles 的行）。

    返回：enriched DataFrame（包含所有有真实名字的药物，smiles 可能为 None）
    """
    df = pd.read_csv(INPUT_CP, index_col=0)

    # 过滤：aliases 里有非 BRD-id 的真实名字
    df["_real_names"] = df["aliases"].apply(real_names)
    named = df[df["_real_names"].apply(len) > 0].copy()
    named["query_name"] = named["_real_names"].apply(lambda x: x[0])  # 第一个真实名字

    if verbose:
        print(f"[filter] total={len(df)}, has_real_name={len(named)} ({len(named)/len(df):.1%})", flush=True)

    # 断点续传：加载已有结果
    if OUTPUT_ENRICHED.exists():
        done = pd.read_csv(OUTPUT_ENRICHED, index_col=0)
        done_brd = set(done[done["smiles"].notna()]["drug"])
        if verbose:
            print(f"[resume] already done with smiles: {len(done_brd)}", flush=True)
    else:
        done = None
        done_brd = set()

    # 查 PubChem（跳过已完成的）
    todo = named[~named["drug"].isin(done_brd)]
    if verbose:
        print(f"[pubchem] need to query: {len(todo)}", flush=True)

    results = []
    for i, (_, row) in enumerate(todo.iterrows()):
        res = query_pubchem(row["query_name"])
        results.append({
            "drug": row["drug"],
            "target": row["target"],
            "moa": row["moa"],
            "aliases": row["aliases"],
            "query_name": row["query_name"],
            "smiles": res["smiles"],
            "inchikey": res["inchikey"],
            "pubchem_cid": res["cid"],
        })

        if (i + 1) % 100 == 0:
            # 合并并 flush
            new_df = pd.DataFrame(results)
            if done is not None:
                combined = pd.concat([done, new_df], ignore_index=True).drop_duplicates("drug")
            else:
                combined = new_df
            combined.to_csv(OUTPUT_ENRICHED)
            done = combined
            done_brd = set(done[done["smiles"].notna()]["drug"])
            if verbose:
                n_ok = new_df["smiles"].notna().sum()
                print(f"  [{i+1}/{len(todo)}] batch done, smiles_ok={n_ok}/{len(new_df)}", flush=True)

        time.sleep(PUBCHEM_DELAY)

    # 最终写入
    if results:
        new_df = pd.DataFrame(results)
        if done is not None:
            combined = pd.concat([done, new_df], ignore_index=True).drop_duplicates("drug")
        else:
            combined = new_df
    else:
        # 全部已完成（断点续传，nothing to do）
        combined = done if done is not None else pd.DataFrame()

    combined.to_csv(OUTPUT_ENRICHED)
    if verbose:
        n_smiles = combined["smiles"].notna().sum()
        print(f"[pubchem] done. smiles found: {n_smiles}/{len(combined)} ({n_smiles/len(combined):.1%})", flush=True)
        print(f"[save] {OUTPUT_ENRICHED}", flush=True)

    return combined


# ── Step 3 + 4 + 5：Morgan 指纹 + Tanimoto 矩阵 + top-50 近邻 ─────────────

def step_fingerprint(verbose: bool = True) -> None:
    """
    读取 cp_meta_enriched.csv，计算 Morgan 指纹，Tanimoto 矩阵，存 drug_neighbors.json。
    """
    if not OUTPUT_ENRICHED.exists():
        raise FileNotFoundError(f"先运行 --step pubchem，缺少 {OUTPUT_ENRICHED}")

    enriched = pd.read_csv(OUTPUT_ENRICHED, index_col=0)
    valid = enriched[enriched["smiles"].notna()].copy()
    if verbose:
        print(f"[fp] valid smiles: {len(valid)}/{len(enriched)}")

    # 计算指纹
    morgan_gen = rdFingerprintGenerator.GetMorganGenerator(radius=MORGAN_RADIUS, fpSize=MORGAN_BITS)
    fps = []
    valid_idx = []
    for i, (_, row) in enumerate(valid.iterrows()):
        mol = Chem.MolFromSmiles(row["smiles"])
        if mol is None:
            continue
        fp = morgan_gen.GetFingerprintAsNumPy(mol)
        fps.append(fp.astype(np.uint8))
        valid_idx.append(i)

    fp_matrix = np.array(fps, dtype=np.float32)  # (N, 2048)
    valid_rows = valid.iloc[valid_idx].reset_index(drop=True)
    N = len(fp_matrix)

    if verbose:
        print(f"[fp] fingerprints computed: {N}")

    # Tanimoto 矩阵（矩阵操作）
    # intersection[i,j] = sum(fp_i & fp_j) = dot product（因为是 0/1）
    # union[i,j] = |fp_i| + |fp_j| - intersection[i,j]
    intersection = fp_matrix @ fp_matrix.T          # (N, N)
    row_sums = fp_matrix.sum(axis=1)                # (N,)
    union = row_sums[:, None] + row_sums[None, :] - intersection
    with np.errstate(invalid="ignore", divide="ignore"):
        tanimoto = np.where(union > 0, intersection / union, 0.0)  # (N, N)
    np.fill_diagonal(tanimoto, 0.0)  # 排除自身

    if verbose:
        print(f"[tanimoto] matrix shape: {tanimoto.shape}, max={tanimoto.max():.3f}")

    # top-50 近邻（紧凑格式：去掉 BRD- 前缀，tanimoto×100 存整数）
    # 读取时：key/brd 补回 "BRD-" 前缀；t/100 还原 tanimoto 值
    neighbors = {}
    for i in range(N):
        brd_i = valid_rows.iloc[i]["drug"]          # 完整 BRD-id，用于 key
        key_i = brd_i[4:]                           # 去掉 "BRD-" 前缀
        top_idx = np.argsort(-tanimoto[i])[:TOP_N]
        nbrs = []
        for j in top_idx:
            if tanimoto[i, j] <= 0:
                continue
            nbrs.append([
                valid_rows.iloc[j]["drug"][4:],     # 邻居 id（去 BRD- 前缀）
                round(int(tanimoto[i, j] * 100)),   # tanimoto×100 整数（0–100）
            ])
        neighbors[key_i] = nbrs

    OUTPUT_NEIGHBORS.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_NEIGHBORS, "w", encoding="utf-8") as f:
        json.dump(neighbors, f, ensure_ascii=False, indent=None, separators=(",", ":"))

    if verbose:
        n_with_nbrs = sum(1 for v in neighbors.values() if v)
        print(f"[neighbors] drugs with neighbors: {n_with_nbrs}/{N}")
        print(f"[save] {OUTPUT_NEIGHBORS}")


# ── Step 6：别名倒排索引 ─────────────────────────────────────────────────

def step_index(verbose: bool = True) -> None:
    """
    读取 cp_meta_enriched.csv，构建别名 → BRD-id 倒排索引，存 drug_index.json。
    key 统一小写，便于查询时 .lower() 匹配。
    """
    if not OUTPUT_ENRICHED.exists():
        raise FileNotFoundError(f"先运行 --step pubchem，缺少 {OUTPUT_ENRICHED}")

    enriched = pd.read_csv(OUTPUT_ENRICHED, index_col=0)

    index: dict[str, str] = {}
    conflicts = 0

    for _, row in enriched.iterrows():
        brd_id = row["drug"]
        for name in real_names(row["aliases"]):
            key = name.lower()
            if key in index and index[key] != brd_id:
                conflicts += 1  # 同一别名对应多个 BRD-id，保留先出现的
            else:
                index[key] = brd_id

    OUTPUT_INDEX.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=None, separators=(",", ":"))

    if verbose:
        print(f"[index] aliases: {len(index)}, conflicts_skipped: {conflicts}")
        print(f"[save] {OUTPUT_INDEX}")


# ── 日志写入 ─────────────────────────────────────────────────────────────

def write_log(steps_run: list[str], start_time: float) -> None:
    """写 report/2_cp_index_log.md。"""
    import datetime

    elapsed = time.time() - start_time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    # 统计信息
    stats = []
    if OUTPUT_ENRICHED.exists():
        df = pd.read_csv(OUTPUT_ENRICHED, index_col=0)
        n_smiles = df["smiles"].notna().sum()
        stats.append(f"- `cp_meta_enriched.csv`: {len(df)} 行，smiles 命中 {n_smiles} ({n_smiles/len(df):.1%})")

    if OUTPUT_INDEX.exists():
        idx = json.loads(OUTPUT_INDEX.read_text(encoding="utf-8"))
        stats.append(f"- `drug_index.json`: {len(idx)} 个别名条目")

    if OUTPUT_NEIGHBORS.exists():
        nbrs = json.loads(OUTPUT_NEIGHBORS.read_text(encoding="utf-8"))
        n_with = sum(1 for v in nbrs.values() if v)
        stats.append(f"- `drug_neighbors.json`: {len(nbrs)} 个药物，{n_with} 个有近邻")

    log = f"""# 2_cp_index 运行日志

**时间**: {now}
**执行步骤**: {', '.join(steps_run)}
**耗时**: {elapsed:.1f}s

## 输出统计

{chr(10).join(stats)}

## 输入

- `input/cp_meta_unique.csv`: 34419 行，80.7% 为 BRD-only

## 输出路径

| 文件 | 路径 |
|------|------|
| 药物元数据增强版 | `output/table/cp_meta_enriched.csv` |
| 别名倒排索引 | `output/store/query_index/drug_index.json` |
| Tanimoto 近邻 | `output/store/query_index/drug_neighbors.json` |
"""

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOG_PATH.write_text(log, encoding="utf-8")
    print(f"[log] {LOG_PATH}")


# ── 主入口 ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Build drug query index")
    parser.add_argument(
        "--step",
        choices=["pubchem", "fingerprint", "index", "all"],
        default="all",
        help="运行指定步骤（默认 all）",
    )
    args = parser.parse_args()

    t0 = time.time()
    steps_run = []

    if args.step in ("pubchem", "all"):
        print("=" * 50)
        print("STEP 1+2: PubChem 查询 SMILES")
        print("=" * 50)
        step_pubchem()
        steps_run.append("pubchem")

    if args.step in ("fingerprint", "all"):
        print("=" * 50)
        print("STEP 3+4+5: Morgan 指纹 + Tanimoto 近邻")
        print("=" * 50)
        step_fingerprint()
        steps_run.append("fingerprint")

    if args.step in ("index", "all"):
        print("=" * 50)
        print("STEP 6: 别名倒排索引")
        print("=" * 50)
        step_index()
        steps_run.append("index")

    write_log(steps_run, t0)
    print(f"\n完成。总耗时 {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
