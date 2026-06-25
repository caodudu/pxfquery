Executing the CyHex checking stage for T-032
Now verify each asset symlink and check non-empty content
All 5 assets resolve to readable paths. A-004 symlink resolves to the T-013 `4_artifact/` directory but the actual files are nested under `2_persist/` and `5_table/`. Wait — looking at the A-004 symlink target more carefully: it points to `4_artifact/` inside T-013, which is the top-level directory containing `2_persist/`, `5_table/`, `3_document/`, etc. But the `required` path in `asset_rule.yaml` says `4_artifact/` for A-004, and the protocol Step 1 references D-003 and D-005 which live in different subdirectories. The symlink needs to actually reach the sub-files. Let me verify the actual paths match what A-
Good — A-004 symlink resolves to `4_artifact/`, and the files are inside `4_artifact/2_persist/` and `4_artifact/5_table/`. Since the symlink points to `4_artifact/`, the protocol text saying D-003 and D-005 are "inside" A-004 is accurate — the execute AI reads the symlinked directory and finds files within. There's no path mismatch.

Now check the `3_execution/` directory structure and the action prompt consistency. Let me also verify non-empty status of A-003
A-003 contains real 19-file bundle with `cp_func_ad.h5ad` at 105M. Not empty shells.

`3_execution/` is empty (as expected — execute stage hasn't begun). The CyHex protocol says `3_execution/` should be set up with step folders when execution happens. Step folders don't need to exist at the checking stage — the protocol's `output:` block lists `3_execution/run_stability_guard.py`, `3_execution/stability_guard_validation.json`, `3_execution/pxfquery_T-032_repaired/` as targets for the execute AI to create.

Now check consistent inclusion of all assets in the latest action prompt
The latest action prompt (`0858`) contains all registered assets, all steps, all guard semantics, and all deliverables. The action prompt is consistent with the current `protocol.md` and `asset_rule.yaml`. No regeneration needed — the check prompt (`0901`) already correctly points to `0858_action_prompt.md` as the `[required]` file.

Now I have verified everything. No repairs needed. The key observations to report are:

1. A-004 symlink is correct even though it resolves to `4_artifact/` — the D-003 and D-005 files are inside subdirectories of that path and the execute AI reads them with relative paths.
2. A-001's `reverse.py` (8.8KB) and `utils.py` (2.9KB) have real content with the `cosine_similarity_matrix` zero-denominator epsilon-fill that A-004 documents as the bug to fix.
3. `3_execution/` is empty — appropriate for checking stage.
4. No blocker — all 5 assets have non-empty content and are readable via symlinks.
5. The protocol has concrete, executable Steps grounded in assets, and a clear list of 11 deliverables.

I also notice a minor inconsistency: the CyHex protocol says `3_execution/` step folders should follow `§14` pattern (e.g. `01_xxx/`, `02_xxx/`), but the protocol doesn't explicitly create them. The execute prompt will auto-create them. Let me verify none of the steps actually require pre-existing folders.

The checking confirms no configuration gaps. I now report the evidence.

---

### 一、我准备如何遵守 CyHex

- **实际使用的文件与目录：**
  - CyHex 系统协议：`/Users/dudu/.cyhex/protocols/cyhex_protocol.md`（v2.11, matched=true）
  - 项目协议：`1_project_init/1_project_protocol/`（0_overview, 1_goal, 2_rule, 3_environment）
  - 任务工作目录：`.../goal_deterministic_query_engines_v1/task_reverse_stability_guard_v1/`
  - 资产（通过 symlink）：A-001（T-024 workspace）、A-002（T-026 loader）、A-003（T-021/D-004 19-file bundle）、A-004（T-013 artifacts）、A-005（project protocol）
  - `3_execution/` → 执行阶段写入脚本和修复后的 `pxfquery-T-032` workspace
  - `4_artifact/` → 交付产物（guard_warnings.json, positive_control_candidates.json, meta.json, 两份 HTML 报告, registry.yaml）
  - `5_report/` → completion.md 和 repair_log.md

- **执行期 API 调用：**
  - 无持久化 job 需求（这是一个短运行 demo，不需要 durable_jobs）
  - 异常时 `POST .../stage_incident` 上报

- **禁止目录：** `../2_project_asset/1_raw_material/`, `/Users/dudu/Documents/3_Project/8_functional_query`, 所有上游 artifact 目录（T-024/T-026/T-021/T-013），`6_project_deliverable/`, `2_protocol/`

- **触发 blocked.md 的条件：** A-001 的 `reverse.py`/`utils.py` 需要实质修复但执行 AI 无法完成；`cp_func_ad.h5ad` 不可读；conda env `pxfquery` 不存在或不可用；修复后的 `pxfquery-T-032` 无法在 editable install 后通过 import 验证

### 二、我准备如何达成任务目标

**目标重申：** 在 PxFquery 反向查询路径中加入数值稳定防护层，检测并显式处理零范数行、零范数目标向量、NaN/Inf 行、空矩阵和无匹配 term 等异常情况，同时保证正常反向查询（HALLMARK_APOPTOSIS + HALLMARK_MYC_TARGETS_V1, MCF7, cp）的排名不受影响，输出可序列化的防护警告和正控候选结果。

**基于实际资产的执行计划：**
1. 阅读 A-001 的 `utils.py`, `reverse.py`, `core.py`, `data/loader.py` → 定位 `cosine_similarity_matrix` 的 `1e-10` epsilon-fill 路径和 `build_target_vector` 的无匹配返回全零的路径
2. 阅读 A-002 的 `loader_validation.json` → 确认矩阵形状/列名/dtype
3. 复制 A-001 的 `src/` 到 `3_execution/pxfquery_T-032_repaired/` → 替换 `cosine_similarity_matrix` 为带 GuardEvent 的版本，扩展 `build_target_vector` 以返回匹配状态，在 `ReverseResult` 上加 `.warnings` 聚合器
4. editable install 到 `pxfquery` conda env → `pip install -e .`
5. 运行 `run_stability_guard.py`，一次执行完成 Scenario A（正控反向查询, 105M cp_func_ad.h5ad）和 Scenario B（合成异常输入矩阵）→ 输出 JSON 证据
6. 写 validation JSON、两份 HTML 报告、completion.md
7. 登记到 `4_artifact/registry.yaml`

**为什么现在可执行：** 5 个资产全部通过 symlink 可达且非空；`cp_func_ad.h5ad`（105M）已确认存在；conda env 在项目协议中已定义；A-004 提供了精确的 bug 定位（cosine_similarity_matrix 零分母 1e-10 填充）；protocol steps 每步都有具体文件/操作/输出目标

### 三、检查与修复

- **发现的问题：** 无。配置阶段产物完整且一致。
- **修复：** 无需修复。
- **空壳/占位检查：** `3_execution/` 当前为空 → 正常，执行阶段写入。A-003 下有 19 个文件（含 3 个 h5ad 共 265M, 105M/96M/64M），非空壳。A-001 下 reverse.py（8.8KB）、utils.py（2.9KB）、core.py（15.6KB），均非空。A-002 下 `loader_validation.json` 有非零内容。A-004 下 D-003/D-005 有非零 CSV/MD 内容。A-005 下 4 个 md 文件均非空。
- **操作提示词路径：** `2_protocol/0_prompt/2026-06-23_0858_action_prompt.md`，与当前 protocol/asset_rules 一致，无需重新生成。
- **阻断项：** 无。

检查完成。请确认：检查通过，开始执行 / 提出修改意见
