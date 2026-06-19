# T-002 扁平化资产库结构说明

生成日期：2026-06-15

## 1. 这次迁移的目的

这次 T-002 的目标不是备份旧目录，也不是把旧 4t / four-stage / archive 结构搬进新项目。

它的目标是：根据 T-001 的语义登记结果，把旧 PxFquery 项目中仍然有用的材料转成一个新的、扁平化的项目资产库，让后续 T-003 可以直接读取新资产库，而不是回到 `/Users/dudu/Documents/3_Project/8_functional_query` 里找旧文件。

旧路径只作为 provenance 记录在 manifest 中，不作为新目录结构。

## 2. 当前迁移状态

当前是第一遍迁移结果：

- 普通资产：已硬拷贝
- 大文件资产：先用软链接占位
- secret 文件：不复制原文，只保留脱敏记录
- 旧协议壳、导航壳、噪音、重复文件：不迁移

统计如下：

| 项目 | 数量 |
|---|---:|
| T-001 registry 总行数 | 411 |
| 已硬拷贝普通资产 | 288 |
| 大文件软链接占位 | 18 |
| secret 脱敏记录 | 1 |
| 不迁移条目 | 104 |
| 新登记资产总数 | 307 |

大文件阈值是 `100MB`。大文件目前不是实体拷贝，而是软链接。你验收目录结构后，再执行：

```bash
3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/2_persist/replace_symlinks_with_copies_v20260614.sh
```

把 18 个软链接替换为硬拷贝。

## 3. 新资产库位置

```text
2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/
```

绝对路径：

```text
/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/
```

## 4. 扁平化规则

本次采用“两层分类”：

```text
资产类型/
  资产组/
```

第一层是资产类型，例如 `code/`、`data/`、`results/`。

第二层是强关联资产组，例如 `code/pxfquery_package/`、`data/query_indexes/`、`results/gsea_tables/`。

注意：代码包内部可能继续有 Python package 自身结构，例如 `code/pxfquery_package/query/resolver.py`。这属于单个资产组内部的代码内容，不是迁移分类层级。迁移分类本身仍是两层。

## 5. 顶层结构

```text
legacy_flat_asset_library_v20260614/
  background/
  code/
  data/
  results/
  reports/
  manuscript/
  history/
  provenance/
  README.md
```

这些顶层目录是新项目资产类型，不是旧项目结构。

## 6. 各目录说明

### background/

用途：保存项目身份、背景、约束、决策和 T-001 消化后的总入口。

结构：

```text
background/
  project_context/
  t001_digest/
```

重点看：

- `background/t001_digest/T001_DIGESTED_CONTEXT.md`

这个文件承接 T-001 对旧项目背景、旧资产结构、权威来源的消化结果。它的作用是替代旧的 MOC、AI_READ_PROTOCOL、checkpoint、目录导航等旧协议壳。

### code/

用途：保存后续开发可能直接用到的旧代码、设计文档、索引构建脚本和分析 notebook。

结构：

```text
code/
  pxfquery_package/
  index_builders/
  analysis_scripts/
  design_docs/
```

重点看：

- `code/pxfquery_package/`：旧 PxFquery 包源码
- `code/index_builders/`：药物、基因、细胞系、function index、resolver 相关构建脚本
- `code/design_docs/`：旧代码设计说明
- `code/analysis_scripts/`：旧分析脚本和 notebook

### data/

用途：保存后续分析、索引重建、功能矩阵读取需要的数据资产。

结构：

```text
data/
  cmap_ad_matrices/
  functional_matrices/
  genept_embeddings/
  metadata_tables/
  query_indexes/
```

重点看：

- `data/cmap_ad_matrices/`：CMAP AD 相关矩阵与元数据
- `data/functional_matrices/`：处理后的 function / GSEA AnnData 矩阵
- `data/genept_embeddings/`：GenePT embedding、gene annotation 等大文件
- `data/metadata_tables/`：compound、cell line、gene metadata
- `data/query_indexes/`：旧 resolver 使用的 query index

其中大文件当前多数是软链接占位。

### results/

用途：保存旧分析结果和可用于验证/写作的结果资产。

结构：

```text
results/
  figures/
  gsea_pickles/
  gsea_tables/
```

重点看：

- `results/gsea_tables/`：大型 GSEA 结果表，目前是软链接占位
- `results/gsea_pickles/`：序列化 GSEA 结果
- `results/figures/`：旧结果图

### reports/

用途：保存旧任务报告、验证报告、上下文卡片等辅助理解材料。

结构：

```text
reports/
  digested_context/
  validation_reports/
```

这些不是旧导航系统本身，而是保留对后续开发、验证有用的报告内容。

### manuscript/

用途：保存投稿、Genes 策略、稿件、参考文献相关资产。

结构：

```text
manuscript/
  genes_strategy/
  manuscript_assets/
  reference_articles/
  submission_context/
```

重点看：

- `manuscript/genes_strategy/`：Genes 时间线、投稿策略、定位分析
- `manuscript/manuscript_assets/`：旧稿件和稿件相关材料
- `manuscript/reference_articles/`：参考论文
- `manuscript/submission_context/`：投稿上下文材料

### history/

用途：保存少量有设计演化价值的历史记录。

结构：

```text
history/
  design_traces/
```

这里的内容只作为历史证据，不作为新项目执行协议。

### provenance/

用途：保存来源、脱敏记录和杂项 provenance。

结构：

```text
provenance/
  misc_useful/
  redacted_secrets/
  migration_manifest_v20260614.json
```

重点看：

- `provenance/migration_manifest_v20260614.json`
- `provenance/redacted_secrets/`

`migration_manifest_v20260614.json` 记录每个 T-001 条目的旧路径、新路径、处理状态和迁移理由。

## 7. 当前软链接占位的大文件

当前共有 18 个大文件软链接，分布如下：

```text
data/functional_matrices/
data/genept_embeddings/
results/gsea_tables/
```

具体包括：

```text
data/functional_matrices/M-0105_cp_func_ad.h5ad
data/functional_matrices/M-0106_sh_func_ad.h5ad
data/functional_matrices/M-0107_xpr_func_ad.h5ad
data/functional_matrices/M-0199_cp_func_ad.h5ad
data/functional_matrices/M-0200_sh_func_ad.h5ad
data/functional_matrices/M-0201_xpr_func_ad.h5ad
data/genept_embeddings/M-0058_gene_attribute_matrix_standardized.txt.gz
data/genept_embeddings/M-0192_GenePT_gene_embedding_ada_text.pickle
data/genept_embeddings/M-0193_GenePT_gene_protein_embedding_model_3_text.pickle
data/genept_embeddings/M-0194_GPT-3-large_homo_sapiens_embedding_3072d.npz
data/genept_embeddings/M-0195_GPT-ada-002_homo_sapiens_embedding_1536d.npz
data/genept_embeddings/M-0197_gene_embedding_m3_filtered.npz
results/gsea_tables/M-0114_cp_gsea_100terms.csv
results/gsea_tables/M-0115_sh_gsea_100terms.csv
results/gsea_tables/M-0116_xpr_gsea_100terms.csv
results/gsea_tables/M-0236_cp_gsea_100terms.csv
results/gsea_tables/M-0237_sh_gsea_100terms.csv
results/gsea_tables/M-0238_xpr_gsea_100terms.csv
```

## 8. 配套登记文件

任务产出的登记和清单文件在：

```text
3_phase_digestion/goal_legacy_asset_migration/task_plan_migration_map/4_artifact/5_table/
```

包括：

```text
migration_manifest_v20260614.json
migration_manifest_v20260614.xlsx
flat_asset_registration_v20260614.json
```

用途：

- `migration_manifest_v20260614.json`：完整迁移明细，包含未迁移条目
- `migration_manifest_v20260614.xlsx`：同一内容的表格版，便于人工查看
- `flat_asset_registration_v20260614.json`：新扁平资产库登记表，给后续任务使用

## 9. 你验收时建议看的点

建议先看这几个位置：

```text
legacy_flat_asset_library_v20260614/README.md
legacy_flat_asset_library_v20260614/background/t001_digest/T001_DIGESTED_CONTEXT.md
legacy_flat_asset_library_v20260614/code/pxfquery_package/
legacy_flat_asset_library_v20260614/data/
legacy_flat_asset_library_v20260614/results/
legacy_flat_asset_library_v20260614/manuscript/genes_strategy/
```

主要判断：

1. 顶层资产类型是否符合你的后续使用习惯。
2. 第二层资产组是否足够清楚。
3. 有没有你认为不该迁移的旧壳内容。
4. 有没有你认为应该迁移但被放进 `not_migrated` 的内容。
5. 大文件软链接位置是否合理。

如果这个结构通过验收，下一步再执行大文件实体拷贝。
