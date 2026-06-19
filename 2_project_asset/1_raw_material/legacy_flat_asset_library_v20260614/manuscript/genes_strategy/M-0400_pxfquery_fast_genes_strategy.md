# PxFquery 按 Genes 快稿生态的投稿策略

## 直接结论

目标不是把 PxFquery 写成“严肃完整工具论文”，而是把它写成 Genes 最近快稿里常见的 **bioinformatics Article**：

> 一个具体疾病/细胞背景下，基于 LINCS 扰动数据的 gene/drug-to-function 查询与功能通路解释。

工具是 PxFquery，主角是 **EGFR/NSCLC functional response** 或类似的具体功能基因组学案例。

## 为什么这个策略更像 Genes 快稿

最近 100 篇里，`Received -> Accepted <= 20 天` 的文章有 27 篇。抽查快稿 PDF 首页后，快稿里大量是普通 `Article`，不是必须 Short Communication。

快稿里出现过的相近形态包括：

- `Differential Gene Expression ... Identifies Antiviral Responses ...`，20 天接收
- `An Integrative Network Analysis Framework ... Autism Spectrum Disorder`，13 天接收
- `... Transcriptome Analysis`，16 天接收
- `Genome-Wide Identification and Expression Profiling ... Gene Family ...`，17-19 天接收
- `Multi-Omics Reveals ... Networks ...`，16 天接收

这些稿件共同点不是机制特别深，而是：

- 数据公开或流程标准
- 题目具体
- 结果能落到 genes/pathways/networks
- 生信分析链条完整
- 不把工具本身吹成大平台

## 你的项目应该怎么改口径

不要主打：

> We developed an AI agent for querying drug-gene functions.

改成：

> We developed a LINCS-based perturbation-to-function workflow to interpret drug- and gene-induced functional programs in cancer cell lines, with EGFR perturbation in NSCLC as a case study.

中文理解：

> 我们构建了一个基于 LINCS 扰动数据的功能通路查询工作流，并用 NSCLC/EGFR 案例展示其能解释药物/基因扰动引起的功能程序变化。

## 最快主线

### 题目候选 1

**A LINCS-Based Perturbation-to-Function Workflow Reveals EGFR-Related Functional Programs in Non-Small Cell Lung Cancer**

优点：最像 Genes 的 functional genomics/bioinformatics。

### 题目候选 2

**PxFquery: A Bioinformatics Workflow for Querying Drug- and Gene-Induced Functional Programs from LINCS Perturbation Data**

优点：保留工具名，但仍然把 functional programs 放在主语位置。

### 题目候选 3

**Integrative Querying of Gene and Drug Perturbation Signatures Identifies Functional Pathway Responses in Cancer Cell Lines**

优点：更泛化，但可能比题目 1 慢一点。

## 最小结果包

为了快，不建议做大而全 benchmark。最小结果包应是：

1. Workflow 图  
   Natural query / gene / drug / cell line -> index resolver -> exact/proxy evidence -> pathway scores。

2. 数据覆盖表  
   三类扰动：xpr、sh、cp；240 cell lines；91 functional terms；drug/gene/cell/function indexes。

3. 主案例：A549 / NSCLC / EGFR knockdown  
   展示 top activated 和 top suppressed pathways。

4. Proxy evidence 展示  
   EGFR 相关邻近基因、NSCLC 相关细胞系、exact/proxy hit levels。

5. 小型 query panel  
   20-30 个问题足够。统计 exact/proxy/not_found、耗时、是否需要 LLM。

6. 负例说明  
   说明泛化药物描述如 “EGFR inhibitor” 可能受 drug alias/BRD 映射限制，避免被审稿人抓住说 hallucination。

## 快速写法重点

Results 不要写成“系统功能很多”。建议写成四段：

1. Construction of a perturbation-to-function query resource
2. Index-assisted exact and proxy retrieval of gene/drug perturbations
3. EGFR perturbation reveals interpretable functional programs in NSCLC models
4. Query panel evaluation demonstrates fast and traceable retrieval

## 当前最大短板

最该补的是 **case study 结果图**，不是继续完善 agent。

现在已有工程和索引，但缺少 manuscript 级别的：

- EGFR/NSCLC 主图
- pathway response heatmap/bar plot
- evidence bundle 表
- 小 query panel 统计

这些比继续优化自然语言能力更重要。

## 实际投稿判断

按当前形态直接投：不建议。

按 EGFR/NSCLC functional genomics workflow 改写：有机会，而且比纯 agent 更快。

按 Genes 最近快稿生态看，最像快稿的不是“AI agent”，而是：

> network analysis / transcriptome-like functional analysis / gene-to-pathway interpretation / genome-scale query workflow

