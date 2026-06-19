import os
import sys
import anndata as ad
import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import re
import random
import string
import pickle
import gseapy as gp

# 1. 输入数据
data_id = sys.argv[1]

tt_ad = sc.read_h5ad(f'/public/home/caojun/project/RUSH/3_work/output/store/cp_split/cp_split_{data_id}.h5ad')
tt_ad.var_names = tt_ad.var['gene_symbol'].astype(str).values.copy()
tt_ad.var_names_make_unique()
tmp_p = '/public/home/caojun/project/RUSH/3_work/output/store/tmp'

tmp_p = '/public/home/caojun/project/RUSH/3_work/output/store/tmp'

# 构造表达矩阵
tt_exp = pd.DataFrame(tt_ad.X, index=tt_ad.obs_names, columns=tt_ad.var_names)

# 基因集文件路径
merged_gmt_p = '/public/home/caojun/project/RUSH/3_work/input/genesets/merged.gmt'

# 输出路径
all_res_p = '/public/home/caojun/project/RUSH/3_work/output/store/gsea_res'
all_res = {}


for dd in list(tt_ad.obs_names):

    try:
        # 排序样本的表达值，生成排名文件
        sub_rank = tt_exp.loc[dd, :].sort_values(ascending=False)

        # 生成唯一的文件名
        letters = string.ascii_letters
        rnd = random.Random()  # 创建独立随机生成器
        file_id = ''.join(rnd.choice(letters) for _ in range(16))
        sub_rank_p = f'{tmp_p}/sub_rank_{file_id}.rnk'

        # 保存排序后的基因表达值为 .rnk 文件
        sub_rank.to_csv(sub_rank_p, sep="\t", header=None)

        # 执行 GSEA 分析
        gsea_results_ = gp.prerank(
            rnk=sub_rank_p,          # 排名文件路径
            gene_sets=merged_gmt_p,   # 基因集的GMT文件
            outdir=None,              # 不保存文件，返回结果
            permutation_num=1000     # 默认置换次数
        )

        # 获取 GSEA 分析结果
        res_ = gsea_results_.res2d
        res_.index = res_['Term'].values.copy()

        # 保存每个样本的 GSEA 结果
        all_res[dd] = res_.copy()

        # 删除临时文件
        os.remove(sub_rank_p)

    except BaseException:

        # 删除临时文件（如果存在）
        try:
            if 'sub_rank_p' in locals() and isinstance(sub_rank_p, str) and os.path.exists(sub_rank_p):
                os.remove(sub_rank_p)
        except BaseException:
            pass

        # 用 all_res 里任意一个成功结果当模板，然后指定列赋值
        if len(all_res) > 0:
            any_key = next(iter(all_res.keys()))
            template = all_res[any_key].copy()

            if 'NES' in template.columns:
                template['NES'] = 0
            if 'FDR q-val' in template.columns:
                template['FDR q-val'] = 1

            all_res[dd] = template
        else:
            # 如果一个成功的都没有，只能给最小可用结构
            res_0 = pd.DataFrame({'Term': [], 'NES': [], 'FDR q-val': []})
            res_0.index = res_0['Term'].values.copy()
            all_res[dd] = res_0

with open(f'{all_res_p}/cp_gsea_res_{data_id}.pkl' ,'wb') as f:
    pickle.dump(all_res, f)


print(f"Saved GSEA results for {data_id} to {all_res_p}/cp_gsea_res_{data_id}.pkl")
