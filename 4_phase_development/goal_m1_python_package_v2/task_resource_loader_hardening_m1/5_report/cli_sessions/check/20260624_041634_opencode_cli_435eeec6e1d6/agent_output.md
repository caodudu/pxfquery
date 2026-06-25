I'll execute the CyHex checking prompt. Let me start by trusting the mechanical asset preflight (8/8 OK) and confirm the key inputs are readable, then write the handoff check report.
Let me verify the full manifest and index health summary are complete enough to proceed:
All assets verified — 8/8 ready, manifest complete with full/fixture paths, index health with clear gaps, fixture package with 18 files. No repairs needed. Writing handoff report.
### 一、我准备如何遵守 CyHex

- **任务实际路径**: `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_resource_loader_hardening_m1`
- **允许写入目录**: `3_execution/`, `4_artifact/`, `5_report/`
- **禁止目录/行为**: `2_project_asset/`、前驱任务目录、legacy source root；禁止变异权威索引或标准资源；禁止使用 T-041 输出
- **执行阶段必须先读的文件**: `1_asset/registration.yaml`、`resource_manifest_m1.yaml`(A-001)、`index_health_summary.json`(A-004)、`gap_notes.md`(A-006)
- **触发 blocked.md 的条件**: asset 缺失且无法修复；`t021_standard_resources_bundle/` 空 + fixture 也损坏；需要 `2_project_asset/` 但 phase 不是 digestion；protocol 无法与 asset rule/registry 互洽

### 二、我准备如何达成任务目标

**目标复述**: 硬化 M1 资源加载器，读取真实 manifest 和索引，处理 schema 差异（function_index 非标准结构、gene_index 字段名不一致、cellline_index 扁平包装），field normalization，产出 smoke 结果 + gap list。作为增强资产，不阻塞 M1 fixture 路径。

**执行策略** (8 步):
1. 解析 A-001 manifest + A-004 健康摘要
2. 实现各类型 loader (h5ad/csv/json)，含 unwrap/field normalization
3. fixture 包 smoke test（18 文件）
4. 尝试全量资源加载
5. 汇聚 gap list
6. 产出机器可读 JSON 结果
7. 产出人工可读 MD report
8. 注册 artifact + completion

**保守起步**: 先 fixture smoke test，确认 18 文件可读、shape 匹配 manifest 预期，再碰全量资源。

### 三、检查与修复

- **资产预检结论**: 8/8 OK，symlink 已同步，无 missing/empty/forbidden_scope
- **计划质量结论**: 符合 8 步 concrete plan，每步有输入/预期输出；有保守起步；定义了 stop condition；交付物 concrete 且注册了路径
- **修复了什么**: 无需修复，green check
- `handoff_check_before_exec.md` 是否已写: 已写
- 是否避免调用下游 prompt 生成: 已避免
- 剩余阻断: 无

检查完成。请确认：检查通过，开始执行 / 提出修改意见
