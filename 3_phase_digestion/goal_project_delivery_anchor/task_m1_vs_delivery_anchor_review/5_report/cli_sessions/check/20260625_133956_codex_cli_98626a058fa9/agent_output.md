我会按 Green Check 处理：只核对任务配置是否足够执行，并写入执行前 handoff，不进入 M1 评审本体，也不生成后续 prompt。先补读被快照截断的协议段，确认交付物、写入边界和停止条件是否具体。
协议和 asset rule 是一致的：16 个输入都来自当前注册资产，执行步骤是评审/归类，不要求跑代码、联网或重算数据。接下来我只写检查 handoff，结论可以保持 green_check。
CyHex 本地 API 返回版本 1.2.20，与任务 meta 一致；没有发现需要修复的配置矛盾。我现在写入 `5_report/handoff_check_before_exec.md`，供后续执行 AI 直接按边界和停止条件操作。
检查 handoff 已写入。最后我会快速读回文件，确认结构符合指定模板且没有误写到交付物目录。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_m1_vs_delivery_anchor_review`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不改 predecessor artifacts、package code、project protocol、`6_project_deliverable/`；不读未来 prompt；不联网；不执行 M1 验证或重算数据
- 执行阶段必须先读的文件：A-001 至 A-016 的注册资产，优先从 M1 四个证据文件开始，再读 T-062/T-063/T-064 anchors
- 触发 `5_report/blocked.md` 的条件：必需资产不可读、协议/资产规则无法一致、需要未注册 predecessor 上下文、需要运行测试/修代码/原始数据分析/联网才能判断

### 二、我准备如何达成任务目标
- 目标：检查 M1 是否满足交付 anchor，明确分类为 full milestone、deterministic kernel/substrate 或 partial milestone，并列出 capability gap、scope shrinkage、下一 milestone 边界
- 4-8 步执行策略：先抽取 M1 claims；建立 T-062 package checklist；单独检查 T-063 resolver/LLM；单独检查 T-064 evidence routing；逐项赋 controlled status；给出总体分类；识别未批准降级；产出 YAML/CSV/中文报告/HTML/registry/completion
- 保守起步/试跑建议：先对 A-001 至 A-004 做小型 evidence inventory，再解析 YAML/JSON/CSV 顶层结构，确认受控标签可用后进入完整评审
- 预期交付物和验收信号：`4_artifact/2_persist/*.yaml|*.md`、`4_artifact/5_table/*.csv`、`4_artifact/3_document/*.html`、`4_artifact/registry.yaml`、`5_report/completion.md`；验收信号是每项 capability 有状态、证据说明、总体分类和下一 milestone 建议

### 三、检查与修复
- 资产预检结论：16 个注册资产全部 ok；CyHex API 可用，版本 `1.2.20`
- 计划质量结论：通过；步骤、输入、输出、停止条件和成本风险都足够具体
- 修复了什么：未修复任何配置，保持 `green_check`
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_m1_vs_delivery_anchor_review/5_report/handoff_check_before_exec.md` 是否已写：已写入并读回确认
- 是否避免调用下游 prompt 生成：是，未调用任何 `/prompt/generate*` endpoint
- 剩余阻断：无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
