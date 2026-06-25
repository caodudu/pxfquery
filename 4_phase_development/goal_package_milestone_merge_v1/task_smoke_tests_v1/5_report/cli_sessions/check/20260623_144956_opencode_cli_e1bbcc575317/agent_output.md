

I'll execute this checking stage. Let me read all relevant files in parallel.
Now let me verify each required asset has real content (not just empty shells) and check T
All asset paths resolve. But I need to verify whether each output bundle actually contains the runnable script mentioned:
Key finding: T-030's `3_execution/` is empty (no `run_reverse_demo.py` at all), and T-033 has neither deliverable. This is consistent with the protocol's `UNMET_DEPENDENCY` handling — the protocol correctly accounts for this. 

Now let me verify the action prompt consistency. The prompt faithfully reproduces the protocol - good. Task status is `active` with sub_status `checking`. Let me check whether `3_execution/` step folders need creating per CyHex §14.
Now let me regenerate the prompt to reflect updated step folders.
All checks pass. Configuration is executable. Let me write the final report.

### 一、我准备如何遵守 CyHex

- **实际路径与目录**:
  - 任务根: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_package_milestone_merge_v1/task_smoke_tests_v1`
  - 输入路径: 通过 `1_asset/*` symlink 指向的 T-029/T-030/T-031/T-032/T-033 `4_artifact/` 目录
  - 产出路径: `4_artifact/5_table/`、`4_artifact/3_document/`、`4_artifact/registry.yaml`、`5_report/completion.md`、`5_report/repair_log.md`
  - 执行路径: `3_execution/{01_inventory,02_smoke_runs,03_consolidate}/`（已创建）
- **实际 API 调用（执行阶段）**:
  - `POST /api/projects/12_PxFquery/tasks/goal_package_milestone_merge_v1/task_smoke_tests_v1/artifacts/auto_register`（交付物登记）
  - `POST .../stage_incident`（如遇失败 / 缺能力 / 配置不一致）
  - `POST .../durable_jobs`（如某些脚本运行超过合理时长时使用 — 黑盒 smoke 不预期需要）
- **禁止目录**: `2_project_asset/`、`6_project_deliverable/`、`8_functional_query`、所有上游 `4_artifact/`（T-024 / T-025 / T-026 / T-027 / T-028 / T-021 / T-013）。T-035 仅读取，不修改上游 artifact。
- **触发 `5_report/blocked.md` 的条件**:
  - pxfquery conda 环境不可用且无法安装
  - T-029 / T-031 / T-032 的脚本存在但完全无法 import pxfquery（属于上游故障，T-035 在自身范围内只能 repair 到 T-035-repaired 本地副本，超出则上报 `config_mismatch`）
  - 任意非可选 predecessor 在脚本可跑的情况下 exit code ≠ 0 且 bad stderr

### 二、我准备如何达成任务目标

- **目标复述**: 对 deterministic query engine 链（T-029 forward engine、T-030 reverse engine、T-031 no-hit guard、T-032 stability guard、T-033 resolver）做 black-box smoke test，把每个 predecessor 的可运行脚本在 pxfquery conda 环境下重新执行一次，捕获 stdout / stderr / exit_code 实际输出，写入 `4_artifact/5_table/pxfquery_T035_smoke_results.json`，并产出中文 HTML 两份报告 + completion 报告。
- **执行计划（按 protocol Steps 编号）**:
  1. **01_inventory**: 读取每个 predecessor 的 `4_artifact/registry.yaml`，列出实际可执行入口（`forward_engine.py` / `test_no_hit_guard.py` / `test_positive_control.py` / `run_stability_guard.py`），对 T-030 / T-033 验证是否存在 `run_reverse_demo.py` / resolver entrance。
  2. **02_smoke_runs**: 在 `pxfquery` conda env 下顺序执行每个已发现入口，每条命令用 `subprocess.run` 捕获 stdout / stderr / exit code / elapsed；输出落到 `4_artifact/5_table/` 下各自的 per-task JSON（`pxfquery_T035_smoke_{T029}
