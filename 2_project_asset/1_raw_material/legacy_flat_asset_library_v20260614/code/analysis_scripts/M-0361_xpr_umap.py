import os
import sys
import anndata as ad
import scanpy as sc
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sc.settings.figdir = '/public/home/caojun/project/RUSH/3_work/output/picture'
sc.settings.set_figure_params(figsize=(8, 8))

xpr_func_ad = sc.read_h5ad('/public/home/caojun/project/RUSH/3_work/output/store/gsea_anndata/xpr_func_ad.h5ad')
#xpr_func_ad.layers['score'] = xpr_func_ad.X.copy() 
#xpr_func_ad.layers['score_clip'] = np.clip(xpr_func_ad.layers['score'],-10,10)
#xpr_func_ad.X = xpr_func_ad.layers['score_clip'].copy()
#sc.tl.pca(xpr_func_ad, svd_solver='arpack')
#sc.pp.neighbors(xpr_func_ad, n_neighbors=10, n_pcs=20)
#sc.tl.umap(xpr_func_ad)
#xpr_func_ad.write('/public/home/caojun/project/RUSH/3_work/output/store/gsea_anndata/xpr_func_ad.h5ad')



xpr_func_ad.X = xpr_func_ad.layers['score_clip'].copy()
#sc.tl.pca(xpr_func_ad, svd_solver='arpack')
sc.pp.neighbors(xpr_func_ad, n_neighbors=15, metric='cosine', use_rep='X')#n_pcs=20)
sc.tl.umap(xpr_func_ad)
xpr_func_ad.write('/public/home/caojun/project/RUSH/3_work/output/store/gsea_anndata/xpr_func_ad.h5ad')




sc.pl.umap(xpr_func_ad,
           color=['cell_iname',],# 'pert_id', 'cmap_name'],
           color_map='inferno',
           save="_umap_xpr_gsea_all.pdf",
           #layer='counts'
           )
 