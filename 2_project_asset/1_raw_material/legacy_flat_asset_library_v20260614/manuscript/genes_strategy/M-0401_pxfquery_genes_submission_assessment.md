# PxFquery 投 Genes 快速可行性评估

## 一句话结论

有可能投 Genes，但不建议按“我开发了一个药物/基因功能查询 agent”直接投。更快、更像 Genes 的写法是：

> 基于 LINCS L1000 扰动数据和功能基因集评分，构建一个 gene/drug-to-function 的可复现生信工作流，并用具体疾病/药物基因场景验证其可以识别药物相关功能通路和候选扰动。

也就是说，论文主角应该是 **functional genomics / perturbation response / drug-gene functional interpretation**，PxFquery 是方法工具。

## 当前项目资产

项目位置：

`D:\Projects\7_rush\3_functional_query\1_claude\workspace`

现有核心内容：

- `xpr/sh/cp` 三类 LINCS 扰动矩阵，功能层面为 91 个 gene sets
- 正向查询：perturbation -> functional pathway changes
- 反向查询：functional target -> candidate perturbations
- 药物索引：约 5,314 个 PubChem 命中的化合物，含结构近邻
- 基因索引：约 25,036 个简化基因条目，含 GenePT 语义近邻
- 细胞系索引：约 240 个 LINCS cell lines，带 lineage/disease/subtype 层次树
- 功能索引：50 个 Hallmark + 41 个 3CA/MPS gene sets
- resolver：支持自然语言解析、exact/proxy 命中、证据汇总

这些资产对 Genes 来说是有生信含量的，尤其是 LINCS perturbation、gene function、biological pathway、drug-gene response 这条线。

## 当前直接投稿的风险

如果按“agent/tool paper”直接投，风险较高：

1. 生物学发现不足  
   目前报告更多是系统能力验证，不是围绕一个明确疾病/药物问题给出新发现。

2. LLM 稳定性还不够  
   已有稳定性报告显示 LLM intent 解析成功率为 6/9。对论文来说，这会被审稿人抓住。

3. 评估集太小  
   当前主 suite 只有 3-4 个 query，mock matrix test 只有 7 个 case。作为工具论文不够。

4. drug query 还不是最强  
   最新报告里 “EGFR inhibitor” 这类泛化药物描述有 NOT_FOUND 场景，说明药物自然语言查询还需要补强。

5. 它更像工程原型，不像完整 manuscript story  
   Genes 快稿通常是问题窄、结果清楚、验证简单完整。当前项目需要一个清晰 biological use case。

## 更快的改法

### 推荐包装 1：NSCLC / EGFR perturbation functional response

题目方向：

> A LINCS-Based Perturbation-to-Function Workflow Reveals EGFR-Related Functional Programs in Non-Small Cell Lung Cancer

为什么适合：

- 你已有 A549 + EGFR knockdown 的 exact evidence。
- cellline tree 里 lung cancer / NSCLC 覆盖很完整。
- Genes 接受 gene function、functional genomics、bioinformatics。
- 题目窄，审稿人容易理解。

需要补强：

- 系统跑 NSCLC 相关细胞系中 EGFR/xpr/sh 证据。
- 汇总 EGFR knockdown/overexpression 或邻近基因扰动的功能通路。
- 加外部文献或数据库验证，例如 EGFR/KRAS/MYC/MTOR/OXPHOS 等通路解释。
- 把 resolver 作为 workflow interface，而不是论文主角。

### 推荐包装 2：Drug-gene functional response retrieval for cancer cell lines

题目方向：

> PxFquery: A LINCS-Based Bioinformatics Workflow for Querying Drug- and Gene-Induced Functional Programs in Cancer Cell Lines

为什么适合：

- 保留工具名。
- 主题仍是 drug/gene-induced functional programs。
- 可以作为 Application Note 风格的短文。

风险：

- 如果没有足够 benchmark，仍然会被当工具论文严格审。
- 比推荐包装 1 更慢一点。

### 推荐包装 3：Reverse query for pathway-targeted perturbation discovery

题目方向：

> Functional Target-to-Perturbation Querying Identifies Candidate Compounds and Genes for Modulating Cancer Pathways

为什么适合：

- 反向查询更像“候选药物/基因发现”。
- 和 druggable genes / candidate perturbations 靠得近。

风险：

- 需要更多验证，尤其候选 compound 是否合理。
- 如果结果只是表格，会显得浅。

## 最推荐的快速投稿路线

选择包装 1。

主线：

1. 背景：NSCLC 中 EGFR 是核心驱动基因，但不同扰动形式和细胞背景下的功能通路响应需要系统化查询。
2. 方法：LINCS L1000 + GSEA functional score matrix + PxFquery exact/proxy evidence retrieval。
3. 结果：
   - 数据资源覆盖：xpr/sh/cp、cell lines、gene/drug/function index
   - EGFR perturbation in A549/NSCLC 的功能响应
   - EGFR 邻近基因或相关 ligand/receptor 的 proxy evidence
   - NSCLC cell-line proxy 检索是否能稳定回到合理细胞系
   - 与已知 EGFR biology 的一致性
4. 讨论：该工作流如何帮助 drug-gene functional interpretation。

这样写最快，因为它把工具评估压缩成一个生物学案例，不需要证明 agent 对所有领域都强。

## 最小补强清单

要让它更像能投的稿件，至少补以下结果：

1. 一个主 case study  
   建议 NSCLC/EGFR。不要同时铺太多疾病。

2. 一张 workflow 图  
   Input: perturbation/cell/function query -> indexes -> exact/proxy retrieval -> functional score output -> evidence summary。

3. 一张数据覆盖图或表  
   xpr/sh/cp observation counts、cell lines、genes、drugs、functional terms。

4. 一张 EGFR case 结果图  
   A549 EGFR knockdown 的 top activated/suppressed pathways。

5. 一张 proxy evidence 图  
   EGFR 邻近扰动和 NSCLC proxy cell lines 的 evidence bundle。

6. 一个小 benchmark  
   例如 20-30 个 curated queries，报告 exact/proxy/not_found、latency、LLM-free fast path vs LLM path。

7. 降低 LLM 依赖  
   投稿时最好突出 deterministic index + fast parser，把 LLM 作为 optional natural-language layer。否则审稿人会担心不稳定。

## 当前投 Genes 的可能性判断

| 形态 | 可能性 | 速度 | 评价 |
|---|---:|---:|---|
| 直接投 agent/tool | 中低 | 慢 | 容易被要求严格 benchmark |
| 改成 LINCS functional genomics workflow | 中高 | 中等偏快 | 比较贴 Genes |
| 改成 NSCLC/EGFR 生物学 case + workflow | 高一些 | 最快 | 推荐 |
| 改成泛化 drug discovery platform | 中 | 慢 | 需要更多验证 |

## 最实际建议

如果目标是“毕业快点”，不要追求把 PxFquery 讲成很大的 agent 平台。建议把稿件定位为：

> A LINCS-based perturbation-to-function bioinformatics workflow for interpreting EGFR-related functional responses in NSCLC.

然后把 PxFquery 作为实现该 workflow 的工具。这样最符合 Genes 快稿画像：问题窄、功能基因组学明确、数据公开、结果可复现、审稿人容易判断。

