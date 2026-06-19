from pxfquery import PxFquery

pxf = PxFquery()
pxf.load_data("xpr", "output/store/gsea_anndata/xpr_func_ad.h5ad")
pxf.load_llm(api_key="sk-...", base_url="...", model="...")

# 正向查询
result = pxf.pert2func("EGFR", cell_line="A549")
pxf.plot(result)

# 自然语言
result = pxf.query("A549里敲掉EGFR会影响哪些通路")