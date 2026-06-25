我会按配置阶段处理，只读取允许的前置索引/报告文件，先确认 CyHex 服务版本，再从 T-007/T-041 的 registry/meta 中选出该任务真正需要登记的输入资产。T-041 会只作为失败背景，不作为权威来源。
T-007 的 handoff 缺失，registry 只给出了源图谱 artifact 但没有直接暴露包源码路径；这触发 yellow_expand。我会只打开 T-007 的核心源图谱和必要 completion，用来确定该登记哪个输入资产；T-041 只核对失败状态和不采用其产物。
已定位到 T-007 的权威源图谱明确列出的 migrated package source：`2_project_asset/.../code/pxfquery_package/`。接下来我会写入协议、资产规则和注册表，只登记 T-007 源图谱与这个包源码目录；T-041 的产物会被明确列为不可依赖。
配置文件已写入。我再做一次轻量校验，确认三个 YAML/Markdown 文件的关键结构和路径没有明显写错；这不是执行任务本体，也不会读取源码目录内容。
校验时我看到 `asset_rule.yaml` 里用父目录表达“禁止广泛扫描”可能和已登记的 A-002 子目录产生歧义。我会把这条改成“未登记项目资产路径”，避免执行阶段把 A-002 误判为禁止输入。
Verdict: `yellow_expand`

Files actually read:
- `GET http://localhost:47291/api/version`
- T-007 `2_protocol/1_meta_info/meta.yaml`
- T-007 `4_artifact/registry.yaml`
- T-007 `4_artifact/2_persist/pxfquery_development_source_map_v20260617.md`
- T-007 `5_report/completion.md`
- T-041 `2_protocol/1_meta_info/meta.yaml`
- T-041 `4_artifact/registry.yaml`
- T-041 `5_report/completion.md`

Predecessor tasks read:
- T-007: used as trusted source map authority.
- T-041: read only to confirm failed/context status and intentionally not reuse outputs.

Assets selected and registered:
- `A-001`: T-007/D-001 source map.
- `A-002`: migrated PxFquery package-source directory from T-007 source map.
- T-041 artifacts: intentionally not registered or used.
- Planned web evidence: none.

Files written/revised:
- [protocol.md](/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/2_protocol_split/protocol.md)
- [asset_rule.yaml](/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml)
- [registration.yaml](/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_development_asset_digestion/task_legacy_source_digest_repair_m1/1_asset/registration.yaml)

No downstream prompt endpoint was called. No task execution, web search, artifact deliverable writing, or task status update was performed.

配置完成。请确认：配置通过 / 提出修改意见
