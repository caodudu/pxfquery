我会按 Green Check 处理：只验证配置可执行性并写交接检查报告，不读取后续 prompt、不生成交付物、不进入任务本体。先确认 CyHex 本地服务状态，再用已有快照和必要的当前任务文件完成 handoff。
CyHex 服务可用，版本与任务配置里的 `1.2.20` 一致。协议正文没有出现需要修复的矛盾：资产预检干净、步骤和交付物足够具体，我会直接写 `handoff_check_before_exec.md`。
我核对了 `registration.yaml`、`asset_rule.yaml` 和协议正文，三者一致：只允许写 `3_execution/`、`4_artifact/`、`5_report/`，并且执行不需要额外搜索或读 legacy root。接下来只写检查交接文件。
检查交接文件已经写入 `5_report/`。我再做一次轻量核对，确认 verdict 和必需章节都在文件里，然后给出最终检查报告。
### 一、我准备如何遵守 CyHex
- 本 task 实际路径：`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor`
- 允许写入目录：`3_execution/`、`4_artifact/`、`5_report/`
- 禁止目录/行为：不写 package 代码，不跑算法测试，不重建资源，不读 legacy root，不写 `6_project_deliverable/`，不调用下游 prompt 生成
- 执行阶段必须先读的文件：当前 protocol、asset registry、asset rule，以及 A-001 到 A-008 注册资产
- 触发 `5_report/blocked.md` 的条件：资产缺失/不足、需要代码实现或测试、需要 raw matrix/web/legacy-root、无法写入规定输出目录、或锚点会把必需 resolver/LLM/proxy 能力降级为可选 lookup

### 二、我准备如何达成任务目标
- 目标：把已注册前置证据整理成 PxFquery 算法包交付锚点，明确能力集、验收词汇、降级规则和里程碑评审 rubric，防止后续任务把目标静默缩成 deterministic lookup。
- 执行策略：读取注册资产；抽取能力/风险/资源依据；建立能力集；写 anchor YAML；写 capability matrix；写 downgrade rules、rubric、classification vocabulary；写中文 Markdown/HTML 摘要；更新 registry 并写 completion report。
- 保守起步/试跑建议：先用 A-004/A-005/A-006 做三类能力骨架试填，验证 YAML/CSV schema 能表达 forward query、resolver/LLM、proxy routing、fallback 和 downgrade。
- 预期交付物和验收信号：目标文件均在 `4_artifact/`，YAML/CSV 可解析，Markdown/HTML 可读，`4_artifact/registry.yaml` 登记所有 reusable outputs，`5_report/completion.md` 说明来源、输出和限制。

### 三、检查与修复
- 资产预检结论：干净，8 个资产均 ok，symlink 同步正常，无 missing/empty/forbidden。
- 计划质量结论：通过，步骤具体，交付物路径明确，包含保守起步、停止条件和成本控制。
- 修复了什么：未修复任何配置，Green Check 直接通过。
- `/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_algorithm_package_delivery_anchor/5_report/handoff_check_before_exec.md` 是否已写：已写。
- 是否避免调用下游 prompt 生成：已避免。
- 剩余阻断：无。

检查完成。请确认：检查通过，开始执行 / 提出修改意见
