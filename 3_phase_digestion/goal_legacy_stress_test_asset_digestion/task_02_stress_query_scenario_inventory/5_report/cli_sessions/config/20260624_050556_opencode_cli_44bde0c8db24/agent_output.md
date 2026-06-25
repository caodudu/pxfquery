Now I have sufficient context from T-007 to configure the task. T-041 is still active, so it will be omitted as instructed. No web search is needed — the stress-test scenarios can be derived from T-007's documented gaps, risks
## 最终证据报告

| 项目 | 内容 |
|---|---|
| **判定** | `green_config` |
| **阶段** | 仅 green_config，未触发 yellow_expand / red_block |

### 已读文件

- T-007 `2_protocol/1_meta_info/meta.yaml` — 确认任务状态 done
- T-007 `5_report/handoff_ai_use.md` — 缺失（已通过 registry + completion 补偿）
- T-007 `4_artifact/registry.yaml` — 选取 D-002/D-003/D-004/D-005/D-006
- T-007 `5_report/completion.md` — 确认交付物和主要发现
- T-007 `4_artifact/2_persist/pxfquery_development_state_report_v20260617.md` — 理解查询机制
- T-007 `4_artifact/2_persist/pxfquery_development_gap_and_risk_list_v20260617.md` — 提取压力测试场景
- T-007 `4_artifact/2_persist/pxfquery_development_phase_handoff_v20260617.md` — 具体查询示例
- T-007 `4_artifact/2_persist/pxfquery_development_source_map_v20260617.md` — 确认资产位置
- 项目资产 `M-0239` — 验证报告权威路由
- 项目资产 `M-0243` — 已知风险清单
- 项目资产 `M-0257` — 确定性矩阵测试 7/7

### 前置任务

- **T-007**: 已读，选取 5 个 D-level 资产 + 3 个 M-level 项目资产
- **T-041**: 确认 active/executing，按要求省略

### 资产选择

| 状态 | 数量 | 来源 |
|---|---|---|
| 已注册 | 8 (A-001 ~ A-008) | T-007 交付物 5 个 + 项目资产 3 个 |
| 已省略 | T-041 全部 | 任务活跃中，不可用 |
| 缺失 | T-007 handoff_ai_use.md | 已通过 registry + completion 补偿 |
| web 计划中 | 0 | 不需要，信息充足 |

### 已写文件

- `1_asset/registration.yaml` — 注册 8 个输入资产
- `2_protocol/2_protocol_split/protocol.md` — 完整执行协议
- `2_protocol/3_asset_rule/asset_rule.yaml` — 资产规则

### 确认

- 未调用下游 prompt 端点
- 未执行任务本体
- 未写交付物

---

配置完成。请确认：配置通过 / 提出修改意见
