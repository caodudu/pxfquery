# 生信论文模板拆解：DTVF (GENES-02693)

**DOI:** 10.3390/genes15091170 | **年份:** 2024 | **交付形态:** web server + tool + model

**题名:** A User-Friendly Tool for Virulence Factor Prediction Based on ProtT5 and Deep Transfer Learning Models

**结构指标（据 T012 全文统计）：** Intro 864字 | Methods 1472字 | Results 1039字 | Discussion 475字 | 图6 | Results段落26

---

## 一、介绍写作逻辑

### 问题锚定方式
从"致病因子的生物信息学鉴定"这个应用问题切入。不是讲深度学习理论，而是讲"pathogens evade immune systems → need to find virulence factors → bioinformatics problem"。

### Gap 构建链条
1. 毒力因子对揭示病原机制和药物发现很关键（生物学意义）。
2. 鉴定 VF 是生信领域的重要问题（问题定性）。
3. 暗示现有方法不够好，提出 DTVF：ProtT5 + dual-channel LSTM/CNN + attention。
4. 强调 novelty：首次将 ProtT5 与双通道深度学习结合用于 VF 预测。

### Genes 典型套路
- T005 评价："引言充分回顾领域发展，方法部分详细描述模型数学公式"。
- 864字 Intro 平衡了领域回顾和技术铺垫。
- 结构完整，适合 Genes 对 computational tool 论文的标准要求。

---

## 二、结果写作逻辑

### 段落结构分析（26个 Results 段，1039字）
1. **数据集描述段**: 用的什么基准数据集，规模多大。
2. **模型性能段**: 核心指标（accuracy/precision/recall/AUC等）。
3. **与 SOTA 对比段**: 和已有模型比，DTVF 好在哪里。
4. **超参数分析段**: Optuna 搜索过程和最优配置。
5. **消融实验/分析段**: 每个模块的贡献。
6. **案例/可视化段**: 示例预测结果。

### 段落间推进方式
- 经典的"数据→性能→对比→分析→案例"五段式。
- 每段用一个表或一张图支撑，不给没有图表的 claim。

### 结果包装策略
- 1039字结果段很少，但26个段落说明每段都很短——靠图表支撑内容，文字只是图表的说明。
- 对比表是主力证据（与现有方法比所有指标）。

---

## 三、图摆放逻辑

| 图 | 推测类型 | 所在段落位置 | 回答什么 |
|----|--------|------------|---------|
| Figure 1 | 模型架构图 | 方法段后、结果段前 | DTVF 的 ProtT5+LSTM/CNN+Attention 架构 |
| Figure 2 | 性能指标表/ROC | 性能结果段 | 主要预测指标 |
| Figure 3 | 与 SOTA 对比表/图 | 对比段 | 比别的方法好多少 |
| Figure 4 | 超参数搜索可视化 | 超参数分析段 | Optuna search 结果 |
| Figure 5 | 消融分析 | 消融段 | 每个模块的贡献 |
| Figure 6 | Web 界面截图/案例 | 案例段或末段 | 用户可以怎么用 |

### 图摆放策略
- 架构图→性能→对比→消融→案例，从"是什么"到"多好"到"为什么好"到"怎么用"。
- 6张图对应6个子结论，每个图带一个表或一段分析。

---

## 四、可模仿要点

1. **架构图必备**: Figure 1 的模型架构图展示方法全貌，这是 computational tool 论文的标配。
2. **对比表撑场**: 与多个方法对比所有指标，即使优势不大也列出数据。
3. **超参数搜索加分**: Optuna 等工具做超参数优化让方法看起来更完整。
4. **Web UI 包装**: 即使只做了一个简单的 web 界面，也能标榜"user-friendly tool"。
5. **弱点警示（T005 指出）**: 没有命令行/API/代码仓库，只在单数据集验证。PxFquery 应避免这些缺陷。