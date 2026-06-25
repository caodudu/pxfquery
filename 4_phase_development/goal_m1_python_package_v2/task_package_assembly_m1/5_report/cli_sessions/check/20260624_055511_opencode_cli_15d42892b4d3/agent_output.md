Now I have a clear picture of all assets and the task configuration. Let me identify two issues that need repair:

1. **Asset name mismatch**: A-014 in the registration YAML has `reverse_repair_manifest.yam` (missing trailing "l" — ".yam" instead of ".yaml"), but the prompt says it was truncated. Let me check the actual registration file.
All 15 assets verified ok. No file-level anomalies. The registration `reverse_repair_manifest.yam` truncation in prompt display was just visual truncation — actual file is `.yaml`. The configuration is clean and ready for green check.
Good, now I understand the M1FixtureLoader interface. Let me write the handoff report.
### 一、我准备如何遵守 CyHex
- **本 task 路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_assembly_m1`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为**: `2_project_asset/`, T-024–T-040, T-048/T-049, 修改 predecessor 目录, 修改 `2_protocol/` 或 `1_asset/`
- **执行阶段必须先读的文件**: `1_asset/registration.yaml` (确定源码来源), 本 handoff 报告
- **触发 blocked.md 的条件**: fixture h5ad 与 M1FixtureLoader 不兼容; manifest 引用不存在的文件; `func2pert` 接线发现接口缺失; 结构性 pip 安装失败

### 二、我准备如何达成任务目标
**复述目标**: 从 T-044 骨架 + T-059 核心逻辑 + T-060 反向 fixture 组装可安装 pxfquery 包, 含 CLI forward/reverse/info 子命令, 跑通两个 demo。

**9 步执行策略**:
1. 建目录 `4_artifact/1_package/src/pxfquery/`
2. 用 A-015 pyproject.toml (已含 `[project.scripts]`)
3. 复制 A-004~A-009 模块树到 `src/pxfquery/`
4. 重写 `core.py` 的 `func2pert()` → 委托给 `query/reverse.reverse_query()`
5. 复制 A-002/A-003 CLI (T-044 版, 含 reverse/info)
6. 写入 `__init__.py` (export `PxFquery`, `__version__`)
7. `pip install -e .`
8. 烟雾测试: import + info + --help
9. forward/reverse demo 并收集证据

**保守起步**: 先跑 `pxfquery info` (不加载矩阵即可验证 CLI). 全部通过后再跑 demo。

**预期交付物**: `4_artifact/1_package/` (包源码), `4_artifact/2_import_smoke/smoke_test_*.txt`, forward/reverse JSON, execution/result HTML 报告, CLI help 文本。

**验收信号**: `pip install -e .` 成功; `import pxfquery`; `pxfquery info` 返回 JSON; forward demo 返回 `found: true` (EGFR/A549/xpr); reverse demo 返回 `found: true` (MYC_TARGETS_V1/A549)

### 三、检查与修复
- **资产预检结论**: ✅ 全部 15 个资产 ok, symlink 一致, 无 missing 无 empty
- **计划质量结论**: ✅ protocol 有 12 步具体操作, 含输入/输出/停止条件, 可执行
- **修复了什么**: 无 — 配置完整一致, 直接 green check
- **handoff_check_before_exec.md**: ✅ 已写入 `5_report/handoff_check_before_exec.md`
- **是否避免调用下游 prompt 生成**: ✅ 未调用任何 `/prompt/generate*` 端点
- **剩余阻断**: 无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
