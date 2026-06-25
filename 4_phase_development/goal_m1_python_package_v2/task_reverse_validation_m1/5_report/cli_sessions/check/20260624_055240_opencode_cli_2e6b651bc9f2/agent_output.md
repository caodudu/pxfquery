Now let me do a quick content sanity check on the key assets:
### 一、我准备如何遵守 CyHex
- **本 task 实际路径:** `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_reverse_validation_m1`
- **允许写入目录:** `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为:** 不读 `2_project_asset/`；不修改任何前序 task 产出；不跳过后继 prompt 生成；不改 acceptance criteria
- **执行阶段必须先读的文件:** `1_asset/registration.yaml` (6 个资产均已 `ok`)
- **触发 `blocked.md` 的条件:** 资产不可索引 / 无法 import / loader 无法加载 / 协议与资产不可调和 / 需要 `2_project_asset/`

### 二、我准备如何达成任务目标
- **复述目标:** 独立验证 M1 reverse query 实现，重新运行 T-042 reverse demo，输出结构化 pass/fail 报告及完整溯源记录
- **执行策略 (8 步):**
  1. 检查 package symlink 目标并记录版本
  2. 通过 M1FixtureLoader (需显式传 `fixture_root`) 加载 fixture，确认 shape、target columns、cell line 覆盖
  3. 运行正向 demo: `activate=APOPTOSIS, suppress=MYC_TARGETS_V1, cell_line=A549, top_n=3`
  4. 运行 5 种 error/no-hit case 并与 A-005 对照
  5. 对比 ranking 输出与 A-006 的 CSV
  6. 运行 CLI reverse 接口做 smoke test
  7. 写结构化 JSON 验证报告
  8. 注册所有交付物到 `4_artifact/registry.yaml`
- **保守起步:** 先做 step 1–2（inspect + load fixture），确认基座正常后再跑 query
- **预期交付物:** JSON 报告 (`4_artifact/2_persist/`)、CSV 比对表 (`4_artifact/5_table/`)、HTML 执行报告、`5_report/completion.md`、`4_artifact/registry.yaml`
- **验收信号:** 清晰的 pass/fail 裁决，不允许模糊或灰色表述

### 三、检查与修复
- **资产预检结论:** ✅ 6/6 assets `ok`，全部 symlink 正确，fixture 文件完整，h5ad 可读 (15×9)，`reverse_query` 函数调用通过，M1FixtureLoader 加载正常（需显式 `fixture_root`）
- **计划质量结论:** ✅ 满足 8 条执行计划质量标准；步骤明确、有保守起步、有停止条件
- **修复了什么:** 无 — 配置完整无需修复
- **`handoff_check_before_exec.md`:** ✅ 已写入 `5_report/handoff_check_before_exec.md`
- **是否避免调用下游 prompt 生成:** ✅ 未调用任何 `/prompt/generate*` 端点
- **剩余阻断:** 无

### ⚠️ 关键执行提示（非阻断）
1. **`M1FixtureLoader` 必须传 `fixture_root` 参数** — loader 不会根据 manifest 的 `fixture_package_root` 自动推导，硬编码为 `fixture_package_m1` 子目录
2. **Package 是 symlink** 指向 T-044，溯源记录中需要注明
3. **`reverse_query` API 签名** 是 `reverse_query(matrix, activate, suppress, cell_line, ...)`，不接收 `fixture` 对象

检查完成。请确认：**检查通过，开始执行**
