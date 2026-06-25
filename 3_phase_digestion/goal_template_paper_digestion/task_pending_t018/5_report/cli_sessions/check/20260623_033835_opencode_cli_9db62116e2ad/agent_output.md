

I notice the task name has already been updated to "生信论文模板拆解" in meta.yaml (from the previous round). Let me
All files are in good shape. Now I need to verify that every required asset file physically resolves. Let me also read the task format reference to ensure the asset_rule.yaml format is correct, since the
The asset_rule.yaml format follows the recommended format from the reference. The required section uses the extended form with `id`, `path`, and `reason` — the reference explicitly allows this ("Allowed list item forms"). The configuration is valid.

Now let me verify all required asset files resolve with a targeted
The relative path resolution in bash fails because `..` in the path doesn't collapse as expected from T-018's directory. Let me use canonical absolute
All 9 required assets exist and are non-empty. Now I need to verify the prompt file path listed in the checking prompt matches expectations — it references `2026-06-23_0319_action_prompt.md` which is the regenerated one. Also, let me verify the action prompt includes updated content by spot-checking the scope note path
The regenerated prompt reflects the corrected path. Everything checks out. Let me also verify `3_execution/` exists and the step folders are appropriate — but the prompt says 3_execution/ is empty and protocol.md doesn't have numbered steps that need specific subfolders. I should create them
---

## 检查报告

### 一、我准备如何遵守 CyHex

**实际使用的文件和目录：**
- Task 根目录：`3_phase_digestion/goal_template_paper_digestion/task_pending_t018/`
- 项目协议：`1_project_init/1_project_protocol/`（0_overview, 1_goal, 2_rule, 3_environment）
- 项目状态：`1_project_init/3_project_state/state.yaml`, `current_state.md`
- 行动提示词：`2_protocol/0_prompt/2026-06-23_0319_action_prompt.md`
- 资产登记：`1_asset/registration.yaml`（9 项资产，来自 T-012 前序任务）
- 资产规则：`2_protocol/3_asset_rule/asset_rule.yaml`
- 执行目录：`3_execution/`（已按 Steps 创建 8 个子文件夹）
- 产出目录：`4_artifact/2_persist/paper_deconstruction/`、`4_artifact/2_persist/`、`4_artifact/3_document/`
- 前序资产源：`task_genes_bioinformatics_deliverable_catalog/4_artifact/2_persist/`（只读）

**执行中会调用的 API：**
- 执行完成后：`POST /api/projects/12_PxFquery/tasks/goal_template_paper_digestion/task_pending_t018/artifacts/auto_register`（登记交付物）
- 遇阻断：`POST .../stage_incident`（异常上报）

**禁止目录：**
- `../../../../8_functional_query/` — 遗留源码根
- `../../../6_project_deliverable/` — 最终交付物目录（消化阶段不涉入）

**触发 blocked.md 的条件：**
- MDPI 官网无法访问（5 篇论文 A-010~A-014 不可达）
- 任一 required 本地资产文件不可读

### 二、我准备如何达成任务目标

**目标复述：** 对 T-012 D-013 中 5 篇 Genes 论文，逐篇拆解"介绍怎么写、结果怎么组织、图怎么放在哪个段落后"，输出 5 篇 MD 拆解 + 1 个 HTML 总汇总，作为 PxFquery 的 Genes 风格写作参考模板。

**执行计划（8 步，对齐 protocol.md Steps）：**
1. 读 D-013 → 确认 5 篇论文的列表、DOI、MDPI URL、结构指标和后续重点
2. 读 5 篇 T012 catalog records → 获交付物归类、验证状态、弱点、短语模式
3. 读 A-007(scope) + A-008(synthesis) + A-009(phrases) → Genes 写作基线
4. 逐篇 webfetch MDPI → 分析简介 gap 构建逻辑、结果段落结构和子结果序列、图编号与位置关系
5. 写 5 篇拆解 MD → `4_artifact/2_persist/paper_deconstruction/`
6. 写 HTML 总汇总 → `4_artifact/2_persist/`
7. 写 `4_artifact/registry.yaml` + `5_report/completion.md`
8. 生成两份 HTML 报告 → `4_artifact/3_document/`

**可执行性：** 9 项 local required 资产已逐一验证存在且非空（最小 2.2KB，最大 12.7KB）。5 个 MDPI URL 作为 optional 资产清晰可查。Step 明确、可操作、产出路径具体。Agent 具备 webfetch/read/write/bash 全部所需能力。

### 三、检查与修复

**发现问题：** 无。上次检查阶段已修复的 A-007 路径错误（文件名 `artifact_deliverable_catalog_scope_note` → `deliverable_catalog_scope_note`）已在新 prompt 中验证一致。

**修复操作：** 无新增修复。

**验证清单：**
- task status: `active`, sub_status: `checking` ✓
- 9 required assets 存在、非空 ✓
- protocol Steps 可达成 Objective ✓
- Deliverables 非空、有具体文件路径 ✓
- prompt `0319` 与当前 protocol/asset_rule 一致 ✓
- `3_execution/` 已按 8 个 Steps 创建子文件夹 ✓
- 工具能力匹配（webfetch/read/write/bash） ✓

**行动提示词路径：** `2_protocol/0_prompt/2026-06-23_0319_action_prompt.md`（上次修复后已重新生成，无需再次重新生成。）

**剩余阻断：** 无

---

**检查完成。请确认：检查通过，开始执行 / 提出修改意见**
