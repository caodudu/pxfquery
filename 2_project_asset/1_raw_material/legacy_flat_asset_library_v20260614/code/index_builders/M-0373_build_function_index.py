"""
build_function_index.py — 构建功能基因集查询索引

输入:  output/store/gsea_anndata/xpr_func_ad.h5ad  （取 var_names，91 个）
输出:  output/store/query_index/function_index.json

function_index.json 结构:
{
  "var_names":  [...],          // 91 个精确 var 名（与 h5ad 一致）
  "meta": {
    "<var_name>": {
      "source":  "hallmark" | "3ca_mps",
      "label":   "<人类可读名>",
      "mp_id":   <int>          // 仅 3ca_mps 有
    }
  },
  "aliases": {
    "<lowercase_alias>": "<var_name>",
    ...
  }
}

运行:
  cd workspace/
  python script/word_new/5_function_index/build_function_index.py
"""

import json
import re
from pathlib import Path

import anndata as ad

# ── 路径 ──────────────────────────────────────────────────────────────────────
WORKSPACE   = Path(__file__).resolve().parents[3]
H5AD        = WORKSPACE / "output" / "store" / "gsea_anndata" / "xpr_func_ad.h5ad"
OUTPUT_DIR  = WORKSPACE / "output" / "store" / "query_index"
OUTPUT_JSON = OUTPUT_DIR / "function_index.json"


# ── 解析 var_name → (source, label, mp_id) ───────────────────────────────────

def parse_hallmark(var_name: str) -> dict:
    """HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION → label='Epithelial Mesenchymal Transition'"""
    raw = var_name[len("HALLMARK_"):]        # strip prefix
    # 保留缩写大写：G2M, E2F, MYC, WNT, UV, TGF, IL2, IL6, ROS, TNFA, PI3K, AKT, MTORC1, KRAS
    words = raw.split("_")
    label_words = []
    for w in words:
        # 已经是全大写缩写 / 数字+字母（V1, V2, DN, UP）→ 原样保留
        if w in {"G2M", "E2F", "MYC", "WNT", "UV", "TGF", "ROS", "TNFA",
                  "PI3K", "AKT", "IL2", "IL6", "MTORC1", "KRAS", "DNA",
                  "DN", "UP", "V1", "V2", "UPR"}:
            label_words.append(w)
        else:
            label_words.append(w.capitalize())
    label = " ".join(label_words)
    return {"source": "hallmark", "label": label}


def parse_mp(var_name: str) -> dict:
    """'MP1  Cell Cycle - G2/M' → {source:'3ca_mps', label:'Cell Cycle - G2/M', mp_id:1}"""
    m = re.match(r"^MP(\d+)\s+(.*)", var_name.strip())
    if not m:
        return {"source": "3ca_mps", "label": var_name.strip()}
    mp_id = int(m.group(1))
    label = m.group(2).strip()
    # 修正已知 typo：Cylce → Cycle
    label = label.replace("Cylce", "Cycle")
    return {"source": "3ca_mps", "label": label, "mp_id": mp_id}


def parse_var(var_name: str) -> dict:
    if var_name.startswith("HALLMARK_"):
        return parse_hallmark(var_name)
    elif var_name.startswith("MP"):
        return parse_mp(var_name)
    else:
        return {"source": "unknown", "label": var_name.strip()}


# ── 别名构建 ──────────────────────────────────────────────────────────────────

# 手工维护的缩写/常见写法 → 精确 var_name
# 仅覆盖「自动生成不到的」或「用户极常用的」情形
CURATED_ALIASES: dict[str, str] = {
    # --- MSigDB Hallmark ---
    "emt":                          "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION",
    "epithelial mesenchymal transition": "HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION",
    "g2m":                          "HALLMARK_G2M_CHECKPOINT",
    "g2/m":                         "HALLMARK_G2M_CHECKPOINT",
    "g2/m checkpoint":              "HALLMARK_G2M_CHECKPOINT",
    "e2f":                          "HALLMARK_E2F_TARGETS",
    "e2f targets":                  "HALLMARK_E2F_TARGETS",
    "myc":                          "HALLMARK_MYC_TARGETS_V1",
    "myc targets":                  "HALLMARK_MYC_TARGETS_V1",
    "p53":                          "HALLMARK_P53_PATHWAY",
    "tp53":                         "HALLMARK_P53_PATHWAY",
    "p53 pathway":                  "HALLMARK_P53_PATHWAY",
    "oxphos":                       "HALLMARK_OXIDATIVE_PHOSPHORYLATION",
    "oxidative phosphorylation":    "HALLMARK_OXIDATIVE_PHOSPHORYLATION",
    "upr":                          "HALLMARK_UNFOLDED_PROTEIN_RESPONSE",
    "unfolded protein response":    "HALLMARK_UNFOLDED_PROTEIN_RESPONSE",
    "ifn alpha":                    "HALLMARK_INTERFERON_ALPHA_RESPONSE",
    "ifn-alpha":                    "HALLMARK_INTERFERON_ALPHA_RESPONSE",
    "interferon alpha":             "HALLMARK_INTERFERON_ALPHA_RESPONSE",
    "ifn gamma":                    "HALLMARK_INTERFERON_GAMMA_RESPONSE",
    "ifn-gamma":                    "HALLMARK_INTERFERON_GAMMA_RESPONSE",
    "interferon gamma":             "HALLMARK_INTERFERON_GAMMA_RESPONSE",
    "nfkb":                         "HALLMARK_TNFA_SIGNALING_VIA_NFKB",
    "nf-kb":                        "HALLMARK_TNFA_SIGNALING_VIA_NFKB",
    "tnfa":                         "HALLMARK_TNFA_SIGNALING_VIA_NFKB",
    "tnf-alpha":                    "HALLMARK_TNFA_SIGNALING_VIA_NFKB",
    "tgf beta":                     "HALLMARK_TGF_BETA_SIGNALING",
    "tgfb":                         "HALLMARK_TGF_BETA_SIGNALING",
    "tgf-beta":                     "HALLMARK_TGF_BETA_SIGNALING",
    "wnt":                          "HALLMARK_WNT_BETA_CATENIN_SIGNALING",
    "wnt signaling":                "HALLMARK_WNT_BETA_CATENIN_SIGNALING",
    "beta catenin":                 "HALLMARK_WNT_BETA_CATENIN_SIGNALING",
    "mtorc1":                       "HALLMARK_MTORC1_SIGNALING",
    "mtor":                         "HALLMARK_MTORC1_SIGNALING",
    "pi3k":                         "HALLMARK_PI3K_AKT_MTOR_SIGNALING",
    "pi3k akt mtor":                "HALLMARK_PI3K_AKT_MTOR_SIGNALING",
    "akt":                          "HALLMARK_PI3K_AKT_MTOR_SIGNALING",
    "ros":                          "HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY",
    "reactive oxygen species":      "HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY",
    "kras up":                      "HALLMARK_KRAS_SIGNALING_UP",
    "kras dn":                      "HALLMARK_KRAS_SIGNALING_DN",
    "kras signaling up":            "HALLMARK_KRAS_SIGNALING_UP",
    "kras signaling down":          "HALLMARK_KRAS_SIGNALING_DN",
    "inflammation":                 "HALLMARK_INFLAMMATORY_RESPONSE",
    "inflammatory response":        "HALLMARK_INFLAMMATORY_RESPONSE",
    "dna repair":                   "HALLMARK_DNA_REPAIR",
    "hypoxia":                      "HALLMARK_HYPOXIA",
    "glycolysis":                   "HALLMARK_GLYCOLYSIS",
    "fatty acid metabolism":        "HALLMARK_FATTY_ACID_METABOLISM",
    "fatty acid":                   "HALLMARK_FATTY_ACID_METABOLISM",
    "cholesterol":                  "HALLMARK_CHOLESTEROL_HOMEOSTASIS",
    "androgen response":            "HALLMARK_ANDROGEN_RESPONSE",
    "estrogen response":            "HALLMARK_ESTROGEN_RESPONSE_EARLY",
    "estrogen":                     "HALLMARK_ESTROGEN_RESPONSE_EARLY",
    "notch":                        "HALLMARK_NOTCH_SIGNALING",
    "hedgehog":                     "HALLMARK_HEDGEHOG_SIGNALING",
    "apoptosis":                    "HALLMARK_APOPTOSIS",
    "angiogenesis":                 "HALLMARK_ANGIOGENESIS",
    "myogenesis":                   "HALLMARK_MYOGENESIS",
    "coagulation":                  "HALLMARK_COAGULATION",
    "complement":                   "HALLMARK_COMPLEMENT",
    "xenobiotic":                   "HALLMARK_XENOBIOTIC_METABOLISM",
    "peroxisome":                   "HALLMARK_PEROXISOME",
    "protein secretion":            "HALLMARK_PROTEIN_SECRETION",
    "il2 stat5":                    "HALLMARK_IL2_STAT5_SIGNALING",
    "il6 jak stat3":                "HALLMARK_IL6_JAK_STAT3_SIGNALING",
    "jak stat":                     "HALLMARK_IL6_JAK_STAT3_SIGNALING",
    "mitotic spindle":              "HALLMARK_MITOTIC_SPINDLE",
    # --- 3CA MPS ---
    "cell cycle g2/m":              "MP1  Cell Cycle - G2/M",
    "cell cycle g1/s":              "MP2  Cell Cycle - G1/S",
    "g1/s":                         "MP2  Cell Cycle - G1/S",
    "chromatin":                    "MP4  Chromatin ",
    "stress":                       "MP5 Stress ",
    "mp6 hypoxia":                  "MP6 Hypoxia",
    "proteasome":                   "MP8 Proteasomal degradation",
    "proteasomal degradation":      "MP8 Proteasomal degradation",
    "translation":                  "MP11 Translation initiation",
    "translation initiation":       "MP11 Translation initiation",
    "emt i":                        "MP12 EMT-I",
    "emt ii":                       "MP13 EMT-II",
    "emt iii":                      "MP14 EMT-III ",
    "emt iv":                       "MP15 EMT IV",
    "mes":                          "MP16 MES (glioma)",
    "respiration":                  "MP21 Respiration",
    "glutathione":                  "MP38 Glutathione",
    "metal response":               "MP39 Metal-response",
    "platelet":                     "MP34 Platelet-activation",
    "platelet activation":          "MP34 Platelet-activation",
    "cilia":                        "MP24 Cilia",
    "senescence":                   "MP19 Epithelial Senescence",
    "epithelial senescence":        "MP19 Epithelial Senescence",
    "alveolar":                     "MP31 Alveolar",
    "skin pigmentation":            "MP32 Skin-pigmentation",
    "pigmentation":                 "MP32 Skin-pigmentation",
    "immunoglobulin":               "MP36 IG",
    "ig":                           "MP36 IG",
}


def build_auto_aliases(var_names: list[str], meta: dict) -> dict[str, str]:
    """从 label 自动生成 lowercase → var_name 映射（不覆盖已有 curated）。"""
    auto: dict[str, str] = {}
    for vn in var_names:
        label = meta[vn]["label"].strip().lower()
        if label and label not in auto:
            auto[label] = vn
        # 对 hallmark：去掉 "hallmark " 前缀如果出现在 label 里（不会，已处理）
        # 额外：normalized var_name 本身（保留给精确回查）
        norm_vn = vn.strip().lower()
        if norm_vn not in auto:
            auto[norm_vn] = vn
    return auto


# ── 主流程 ────────────────────────────────────────────────────────────────────

def main():
    print(f"[input]  {H5AD}")

    # Step 1：从 h5ad 读取 91 个 var_names（最权威来源）
    adata = ad.read_h5ad(H5AD, backed="r")
    var_names: list[str] = list(adata.var_names)
    print(f"[var_names] {len(var_names)} gene sets loaded from h5ad")

    # Step 2：构建 meta
    meta: dict[str, dict] = {}
    for vn in var_names:
        meta[vn] = parse_var(vn)

    # 统计来源
    n_hallmark = sum(1 for v in meta.values() if v["source"] == "hallmark")
    n_mps      = sum(1 for v in meta.values() if v["source"] == "3ca_mps")
    print(f"[meta]   hallmark={n_hallmark}  3ca_mps={n_mps}")

    # Step 3：构建 aliases
    aliases: dict[str, str] = {}

    # 先放自动生成（低优先级）
    auto = build_auto_aliases(var_names, meta)
    aliases.update(auto)

    # 再放 curated（高优先级，可覆盖 auto）
    # 验证 curated targets 全部存在
    valid_set = set(var_names)
    for alias_key, target in CURATED_ALIASES.items():
        if target not in valid_set:
            print(f"  [WARN] curated alias '{alias_key}' → '{target}' NOT in var_names")
        else:
            aliases[alias_key.lower()] = target

    print(f"[aliases] {len(aliases)} entries total "
          f"(auto={len(auto)}, curated added/overrode={len(CURATED_ALIASES)})")

    # Step 4：写 JSON
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        "var_names": var_names,
        "meta":      meta,
        "aliases":   dict(sorted(aliases.items())),
    }
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    size_kb = OUTPUT_JSON.stat().st_size / 1024
    print(f"\n[output] {OUTPUT_JSON}  ({size_kb:.1f} KB)")

    # Step 5：打印摘要
    print("\n=== 功能条目列表 ===")
    print(f"{'idx':>4}  {'source':<10}  {'label'}")
    print("-" * 70)
    for i, vn in enumerate(var_names, 1):
        m = meta[vn]
        src = m["source"]
        lbl = m["label"]
        print(f"  {i:>2}.  {src:<10}  {lbl}")

    print("\n=== 别名样例（curated，前 20 条）===")
    curated_items = list(CURATED_ALIASES.items())[:20]
    for alias, target in curated_items:
        print(f"  '{alias}' → '{target}'")

    print("\n[done]")


if __name__ == "__main__":
    main()
