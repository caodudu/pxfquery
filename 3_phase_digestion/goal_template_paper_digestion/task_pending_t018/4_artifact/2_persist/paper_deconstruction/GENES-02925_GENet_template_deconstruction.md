# 生信论文模板拆解：GENet (GENES-02925)

**DOI:** 10.3390/genes15070938 | **年份:** 2024 | **交付形态:** software tool + model + algorithm

**题名:** A Graph-Based Model Leveraging Histone Marks and Transcription Factors for Enhanced Gene Expression Prediction

**结构指标（据 T012 全文统计）：** Intro 2003字 | Methods 0字 | Results 1895字 | Discussion 1895字 | 图4 | Results段落48

**⚠ 注意:** Methods 字数为0是 T012 自动统计未识别章节标题导致的，不代表论文没有 Methods 部分。需用人工核对确认章节标题识别问题。

---

## 一、介绍写作逻辑

### 问题锚定方式
从"理解基因表达调控机制是基因组学核心目标"这个宏大命题切入。然后迅速落地：虽然 TSS 附近的 DNA 序列提供了有价值的信息，但仅靠周围序列不够准确预测基因表达。

### Gap 构建链条
1. 基表达调控是大问题（领域价值锚定）。
2. DNA sequence near TSS 提供了 insights（已有方法基础）。
3. 但"recent methods suggest that analyzing only the surrounding DNA may not suffice"（限制指出）。
4. 需要整合更多信息——histone marks + transcription factors（自己的路径）。
5. 提出 GENet：graph-based model 整合组蛋白标记和转录因子信息。

### Genes 典型套路
- 2003字 Intro 是 5 篇中最长的。可能因为 graph model + 多来源特征整合需要更长的背景铺垫。
- 用了"从大到小"的漏斗结构：大领域问题 → 已有什么方法 → 还有什么不足 → 我的方案。
- 明确说出了自己的特征来源（histone marks + TFs），让读者一看就知道创新点在哪。

---

## 二、结果写作逻辑

### 段落结构分析（48个 Results 段，1895字）
1. **特征工程/数据描述段**: histone marks 和 TF 数据的来源和预处理。
2. **图模型构建效果**: graph 结构的设计和节点特征表示效果。
3. **基因表达预测性能**: 核心指标展示。
4. **与基线方法对比**: 和只用序列或只用一种特征的模型对比。
5. **生物学解释段**: 模型学到的重要特征（哪些 histone marks/TFs 贡献最大）的解读。

### 段落间推进方式
- 特征→模型→预测→对比→解释，从计算到生物学的叙事链路。
- 48段/1895字说明每段较短，密集排列子结论。

### 结果包装策略
- 1895字 Results + 1895字 Discussion（两者字数相同，可能是 T012 边界切分问题，但说明 Discussion 被认真写了）。
- Graph-based model 自带"看起来高级"的感觉。

---

## 三、图摆放逻辑

| 图 | 推测类型 | 所在段落位置 | 回答什么 |
|----|--------|------------|---------|
| Figure 1 | 图模型架构/框架图 | 方法段后 | 图的节点、边、特征如何定义 |
| Figure 2 | 预测性能指标 | 性能结果段 | 基因表达预测的准确率 |
| Figure 3 | 与基线对比 | 对比段 | 比纯序列方法好多少 |
| Figure 4 | 特征贡献/生物学解释 | 解释段 | 哪些组蛋白标记和 TF 最重要 |

### 图摆放策略
- 4 张图对 48 个段，平均每 12 段配 1 张图。
- 模型架构→性能→对比→生信注释，标准的"方法好看→结果可靠→优于别人→有意义"四段式。

---

## 四、可模仿要点

1. **Long Intro 可以接受**: 2003字 Intro 说明 Genes 接受较长背景叙述，尤其是方法涉及多来源特征时。
2. **"DNA序列不够，需要XX信息"是经典 Gap 句式**: 指出已有方法的输入不全，然后补充新信息类型。
3. **Graph-based 模型自带高级感**: 图结构比纯 MLP/CNN 看起来更有设计思量。
4. **生物学解释做出口**: 不只是报性能指标，还要说明模型学到了什么生物学上可解释的模式。
5. **⚠ Methods 边界注意**: T012 统计未识别 Methods 章节，提醒我们在写 PxFquery 论文时要用明确的章节标题（如 "## 2. Materials and Methods"），方便自动统计和同行定位。