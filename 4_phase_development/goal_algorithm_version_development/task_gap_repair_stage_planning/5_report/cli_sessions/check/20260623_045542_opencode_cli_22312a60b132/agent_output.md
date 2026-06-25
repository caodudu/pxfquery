

I'll execute the CyHex checking stage prompt.
Now read the CyHex protocol checking section and all current
Now let me verify each registered asset's symlink resolves to a real file/directory with nonzero content.
The symlinks have broken relative paths. The `ln` commands used relative paths from the `1_asset` directory, but those don't resolve correctly. Let me check the actual links and fix them
The symlinks are relative paths from `1_asset/`, but all the cross-references need `..` segments relative to the task root level. The problem is: from `1_asset/` path, `../../../` goes up to `goal_algorithm_version_development/` level, but these relative paths should go up 3 levels from `1_asset` to reach project root. Let me verify:

`1_asset/` is at depth 5 from project root. `../../../` from there is depth 2, which is `goal_algorithm_version_development/`. But the assets are in sibling goals at project-depth 4. The symlinks need to account for this correctly.

Let me compute the right number of `..` for each:
- Project protocol `1_project_init/1_project_protocol/` is at depth 3 from root. From `1_asset/`: need `../../../../1_project_init/..` — that's 4 up.
- T-013 files need to go up 3 from `1_asset` to project root, then down to `4_phase_development/goal_algorithm_function_review/...`. Currently uses `../../goal_algorithm_function_review/...` which would be `4_phase_development/task_gap_repair_stage_planning/1_asset/goal_algorithm_function_review/...` — wrong.

Let me fix all symlinks with absolute target paths (via the `ln
Now let me re-verify all assets resolve correctly:
All 13 symlinks pass. The prompt verification had a PATH issue with grep — let me also verify the prompt does contain "self-PATCH" and check the relative paths in asset_rule.yaml resolve
Good, the prompt does contain that line. Now let me also verify that the relative paths in asset_rule.yaml resolve correctly from the `2_protocol/3_asset_rule/` directory
The relative paths in `asset_rule.yaml` are wrong. From `2_protocol/3_asset_rule/`:
- `../../` = task root level (task_gap_repair_stage_planning)
- `../../../` = goal level (goal_algorithm_version_development)
- So `../../goal_algorithm_function_review/` resolves to `task_gap_repair_stage_planning/goal_algorithm_function_review` — doesn't exist

The correct paths need more `..`:
- `../../../` needs to be `../../../../../` to reach project root
- `../../goal_algorithm_function_review/` should be `../../../../../4_phase_development/goal_algorithm_function_review/`

Let me fix
Prompt regenerated. Now let me verify the new prompt
Now let me also verify the `3_execution/` step folder structure. The protocol has 8 steps — the checking rules say I should create or update the step subfolders if CyHex protocol
---

## Checking Report

### 一、我准备如何遵守 CyHex

- **实际使用的文件和目录:**
  - Task path: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_algorithm_version_development/task_gap_repair_stage_planning`
  - CyHex protocol: `~/.cyhex/protocols/cyhex_protocol.md`
  - Action prompt: `2_protocol/0_prompt/2026-06-23_0504_action_prompt.md`
  - 13 registered assets via `1_asset/` symlinks (all verified non-empty and readable)
  - 8 execution step folders under `3_execution/` for organized execution

- **执行中需要调用的 API:**
  - `POST /api/.../artifacts/auto_register` — 交付物登记（若API可用）
  - `POST /api/.../stage_incident` — 出现阻塞时上报
  - `POST /api/.../durable_jobs` — 如有长时间运行需求

- **禁止目录/操作:**
  - `/Users/dudu/Documents/3_Project/8_functional_query` — 历史源根
  - `6_project_deliverable/` — 最终交付物
  - `2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614/` — 只读迁移资产
  - `goal_algorithm_function_review/` — T-013产物只读
  - `3_phase_digestion/` — T-007/T-012产物只读
  - 不得自行 PATCH task status → done

- **触发 `5_report/blocked.md` 的条件:**
  - T-013 失败清单或能力状态矩阵不可读
  - T-007 开发状态报告不可读
  - 某个缺口的根因无法从现有证据判断
  - 包代码结构混乱到无法规划合理修改路径
  - prompt/协议/资产规则与文件系统矛盾

### 二、我准备如何达成任务目标

**目标复述:** 基于T-013走查发现的4个缺口（CAP-03索引不可用、CAP-05未命中误报、CAP-06反向查询数值问题、CAP-07 NL resolver阻断），结合T-007的开发状态理解和T-012的Genes论文措辞模式，产出分阶段修复计划（只规划不执行）。

**执行计划（8步）:**
1. 读T-013缺口清单→整理每个缺口的技术根因和修复方向
2. 读T-007开发状态→补充代码/索引/数据层面背景
3. 读T-012措辞库→提取Genes论文中可参照的描述模式
4. 读包代码/设计文档/索引目录→确认每个缺口涉及的具体文件
5. 制定每个缺口的具体修复方案（目标/范围/产出/验收标准）
6. 组织为分阶段G-006任务建议（先CAP-03/07阻塞层，再CAP-05行为层，最后CAP-06论文级打磨）
7. 为每阶段映射Genes论文措辞框架
8. 产出3份交付物：规划报告、任务建议表、Genes措辞对照

**预期产出:** 3个文件写入 `4_artifact/` + `5_report/completion.md`

### 三、检查与修复

**发现的问题与修复:**
1. **资产软链接路径错误** — 配置阶段创建的13个symlink使用了错误的相对路径。已修复为绝对路径，全部13个资产通过非空验证。
2. **asset_rule.yaml 相对路径错误** — required/optional/forbidden/non_modifiable中所有跨goal/跨phase的相对路径均少了两层 `..`。已全部修正为 `../../../../../` 前缀。

**无空壳占位资产** — 全部13个资产均指向实际存在的非空文件或非空目录。symlink通过绝对路径验证，asset_rule中修正后的相对路径均可从 `2_protocol/3_asset_rule/` 解析。

**重新生成后的 action prompt 路径:** `2_protocol/0_prompt/2026-06-23_0504_action_prompt.md`

**T-023 protocol 可行性确认:**
- Objective 明确且有边界：做规划，不做执行
- 8个 Steps 层层递进：证据整理→背景补充→措辞提取→代码确认→方案制定→阶段组织→措辞对齐→报告产出
- 3个 Deliverables 具体可测，有文件路径和格式
- 13个输入资产全部可用，覆盖缺口证据（T-013）、开发背景（T-007）、论文模式（T-012）、技术参考（包代码/设计文档/索引）
- Failure Stop 覆盖了可预见的阻断场景
- 无剩余阻断。

检查完成。请确认：检查通过，开始执行 / 提出修改意见
