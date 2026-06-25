# Protocol: 生信论文模板拆解

## Objective
对 T-012 交付物 D-013 记录的 5 篇 Genes 生信论文（GENES-02459 OHDLF、GENES-02981 CrossMP、GENES-02693 DTVF、GENES-04451 StrainIQ、GENES-02925 GENet），逐篇拆解其介绍写作逻辑、结果写作逻辑和图摆放逻辑，为 PxFquery 写作提供 Genes 风格的参考模板。目标是对齐 Genes 喜欢的风格和工作量设置，不做 Nature/大 SCI 标准的评判。

## Inputs
- A-001: T012 D-013 重点阅读论文记录 HTML — 获取 5 篇论文的基本信息、DOI、结构指标和后续重点方向
- A-002: T012 D-006 逐篇记录 — OHDLF 的 T012 catalog 记录，含交付物归类、验证证据和表达模式
- A-003: T012 D-006 逐篇记录 — CrossMP 的 T012 catalog 记录
- A-004: T012 D-006 逐篇记录 — DTVF 的 T012 catalog 记录
- A-005: T012 D-006 逐篇记录 — StrainIQ 的 T012 catalog 记录
- A-006: T012 D-006 逐篇记录 — GENet 的 T012 catalog 记录
- A-007: T012 D-001 范围说明 — 了解 T012 的 artifact-deliverable 筛选标准和范围边界
- A-008: T012 D-009 综合分析报告 — 了解 Genes 论文交付物描述模式和写作风格基线
- A-009: T012 D-008 短语库 — 可复用的交付物描述表达模式
- A-010: 原始论文网页 — 从 MDPI 官网逐篇阅读原文，提取介绍/结果/图摆放逻辑

## Steps
1. 读取 T012 D-013 确定 5 篇论文的列表、DOI、各篇结构指标和后续重点。
2. 读取 T012 D-006 中对应 5 篇的逐篇记录（含交付物归类、验证证据、限制和表达模式）。
3. 读取 T012 D-001 和 D-009 确认 Genes 论文交付物描述的总体风格基线。
4. 对每一篇论文，通过 MDPI 官网打开原文，提取：
   - 介绍写作逻辑：如何引出问题、如何构建 gap、如何引导到自己的交付物。
   - 结果写作逻辑：段落结构、每段讲什么、如何安排子结果顺序、如何用图表支撑每个结论。
   - 图摆放逻辑：图与结果段落的对应关系、图类型（流程图/性能表/案例展示/截图等）、每张图回答什么。
5. 每篇写一个独立的中文 MD 拆解文件，按统一模板记录介绍逻辑、结果逻辑和图逻辑。
6. 编写总 HTML 汇总页面，包含 5 篇的交叉对比表、写作模式归纳和 Genes 风格要点总结。
7. 将每篇拆解 MD 放入 4_artifact/2_persist/paper_deconstruction/。
8. 将总 HTML 汇总页面放入 4_artifact/2_persist/。

## Constraints
- 每篇拆解 MD 包含三个核心章节：介绍写作逻辑、结果写作逻辑、图摆放逻辑。
- 拆解目标是"学习 Genes 喜欢的叙述方式"，不是评判论文科学质量或对 PxFquery 的直接启示。
- 不要用 Nature/Bioinformatics 的标准去批评 MDPI 论文。接受 Genes 的叙述惯性，提炼可模仿的模式。
- 只处理 D-013 明确的 5 篇论文，不扩展到 T012 的 103 篇全集。
- 图摆放逻辑需要说明每张图回答什么、放在哪个段落之后、图类型和叙述配合方式。
- 每篇拆解末尾附"可模仿要点"小节，提炼该篇最值得 PxFquery 对标的部分。

## Deliverables
- 5 篇论文各自的拆解 MD：`4_artifact/2_persist/paper_deconstruction/{GENES-ID}_{deliverable_name}_template_deconstruction.md`
- 总 HTML 汇总：`4_artifact/2_persist/paper_deconstruction_summary_v20260623.html`
- 完成报告：`5_report/completion.md`

## Acceptance
- 5 篇拆解 MD 完整，每篇都包含介绍、结果、图三个逻辑分析。
- 总 HTML 汇总包含交叉对比表和 Genes 风格要点归纳。
- 分析语气是"学习模板"而非"评判科学水平"。