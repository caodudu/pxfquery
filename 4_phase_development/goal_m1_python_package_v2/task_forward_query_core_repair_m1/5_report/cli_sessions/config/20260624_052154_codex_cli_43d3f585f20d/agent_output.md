I’ll configure this as a yellow-expand case because seven predecessors are selected and T-048 has no AI-use handoff. I’ll keep the read set narrow: only the listed handoffs/registries/meta files, plus T-048 completion if needed for the incident summary.
T-042 gives the hard contract: the key inputs are the API contract YAML and demo cases YAML, especially DEMO-001 `EGFR/A549/xpr`. I’m now selecting the fixture, skeleton, loader, hardening, and incident-reference artifacts that execution will need without opening their raw deliverables.
The base implementation source should come from T-044’s skeleton, while T-043’s fixture is useful context but not enough for the required positive demo. I’m checking the loader and hardening handoffs next so the repair protocol can require compatibility with the existing resource-loading API.
T-046 provides the documented fixture loader API and smoke evidence; T-047 is optional hardening rather than the base route. I’ll read T-045 as index-health context and T-048 only as the failed-reference incident, then write the configuration.
The incident is explicit: T-048 failed because the required `EGFR/A549/xpr` positive case is absent from the loader-exposed fixture rows. I’m going to configure T-059 to create a task-local synthetic/repair substrate with honest provenance, then implement and prove the forward query against T-042 without mutating upstream artifacts.
I’m writing the three configuration files now. The asset registry will point to predecessor artifacts only; the repair fixture/manifest is configured as an execution output, not pre-registered as an input.
Configuration files are written. I’ll do a light syntax check on the YAML and a targeted readback of the headers so the final report is based on the actual files, not just the patch.
The readback matches the intended configuration. One YAML parse check returned cleanly but without printed output through `conda run`, so I’ll rerun it with the environment’s Python binary directly for an explicit confirmation.
Verdict: `yellow_expand`

Reason: seven predecessors were selected, and T-048 lacked `handoff_ai_use.md`, so I used the allowed yellow-expand fallback `5_report/completion.md` for the incident summary.

Files read:
- CyHex `/api/version`
- T-042 to T-047: listed `meta.yaml`, `handoff_ai_use.md`, `registry.yaml`
- T-048: `meta.yaml`, `registry.yaml`, `completion.md`

Predecessors read:
- T-042, T-043, T-044, T-045, T-046, T-047, T-048

Assets selected/registered:
- Registered 15 assets in `1_asset/registration.yaml`
- Required: T-042 contract/demo, T-043 manifest/fixture/schema/sample records, T-044 skeleton/import smoke, T-046 loader/API/smoke, T-048 blocked completion report
- Optional: T-047 hardened loader code and gap list
- Intentionally not used: T-048 `4_artifact/` outputs, T024-T040 blocked assets, `2_project_asset/`
- Planned web: none

Files written/revised:
- [protocol.md](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/2_protocol/2_protocol_split/protocol.md)
- [asset_rule.yaml](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/2_protocol/3_asset_rule/asset_rule.yaml)
- [registration.yaml](/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_forward_query_core_repair_m1/1_asset/registration.yaml)

Validation:
- `registration.yaml` and `asset_rule.yaml` parsed successfully as YAML.
- No downstream prompt endpoint was called.
- No task execution, artifact delivery, web search, or status change was performed.

配置完成。请确认：配置通过 / 提出修改意见
