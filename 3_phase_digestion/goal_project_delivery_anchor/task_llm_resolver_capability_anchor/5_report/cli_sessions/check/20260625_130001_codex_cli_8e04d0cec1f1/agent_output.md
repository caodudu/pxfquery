我会按 green check 处理：只检查配置是否足够执行，不进入任务本体，也不生成后续 prompt。先补齐当前 task 协议中被快照截断的部分，然后写执行前 handoff。
协议和资产规则已经足够具体：9 个步骤、明确禁止项、固定交付路径、13 个必需资产全部预检 OK。接下来只写 `5_report/handoff_check_before_exec.md`，不改协议、不碰交付物目录。
我会把检查结论写成 green handoff，并把执行 AI 的边界、保守起步、停止条件写清楚。这里没有发现需要 Yellow Repair 的配置问题。
handoff 已写入。最后我会快速核对文件结构和关键结论，确保没有误写成执行交付物或遗漏要求的章节。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不读 legacy root、不扫任意 predecessor 文件夹、不写 `6_project_deliverable/`、不实现代码、不跑测试、不调用下游 prompt 生成
- 执行阶段必须先读的文件：当前 task protocol、asset rule、`1_asset/registration.yaml` 中 13 个已注册资产
- 触发 `5_report/blocked.md` 的条件：必需资产缺失、需要越界读取/实现/测试/联网、或会把 LLM/resolver 降级成 deterministic lookup/fallback-only

### 二、我准备如何达成任务目标
- 目标：检查 T-063 是否能交给执行 AI 生成 LLM/resolver capability anchor，而不让执行 AI 猜上下文或扩大范围
- 执行策略：先读注册资产；提取 resolver 需求/缺口/降级规则；定义 M3 resolver 行为；定义 CyHex AI route；定义 exact/proxy/not-found 与 fallback；生成 demo case 和 acceptance matrix；写入指定 artifacts 与报告
- 保守起步/试跑建议：先用 T-062 相关资产做一个 `3_execution/` outline，确认能力类别和状态词表完整后再写正式交付物
- 预期交付物和验收信号：YAML anchor、functional design、acceptance matrix、demo catalog、HTML reports、artifact registry、completion report；验收重点是不声称代码已实现或 LLM 已实测

### 三、检查与修复
- 资产预检结论：13 个 required assets 全部 `ok`
- 计划质量结论：通过，步骤具体，边界、成本、停止条件、交付路径都明确
- 修复了什么：无，未进入 Yellow Repair
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_llm_resolver_capability_anchor/5_report/handoff_check_before_exec.md` 是否已写：已写
- 是否避免调用下游 prompt 生成：已避免
- 剩余阻断：无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
