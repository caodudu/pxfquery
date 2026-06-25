

I'll execute this CyHex configuration prompt for T-064 `evidence_routing_anchor`. Let me start by reading the predecessor task files as specified
Now let me read the key handoff/registry content from T-007 and T-013 that are most relevant to this task. I need to read the handoff_ai_use.md files (missing for T-007 and T-013, so I need to use completion.md as yellow_expand). Let me also check T-013's failure/missing capability list since it directly relates to
Now let me also read the key deliverable handoff pack from T-058 and the T-013 failure/missing capability list, as these are most directly relevant to defining evidence-routing routes. Let me also check the T-007 development state report
Now I have sufficient understanding from all predecessor tasks. Let me now write the three configuration files. I have a clear picture of:

- Evidence routing routes needed: exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion
- Predecessor evidence about current gaps (no-hit fuzzy matching false-positives, missing function_index.json, always_llm instability)
- Predecessor evidence about what works (deterministic 7/7 matrix, hybrid_fast, resolver proxy logic)
- T-021 standard resources (rebuilding function_index.json)
- T-058 stress-test scenarios for future validation
All three files written. Now producing the final evidence report.

---

**Verdict:** `green_config`

**Files actually read:**
- T-007: `meta.yaml`, `registry.yaml`, `completion.md`, `pxfquery_development_state_report_v20260617.md`, `pxfquery_development_gap_and_risk_list_v20260617.md`
- T-013: `meta.yaml`, `registry.yaml`, `completion.md`, `pxfquery_t013_failure_missing_capability_list_v20260618.md`
- T-021: `meta.yaml`, `registry.yaml`, `completion.md`
- T-058: `meta.yaml`, `handoff_ai_use.md`, `registry.yaml`, `completion.md`, `stress_test_development_handoff_pack_v20260624.md` (partial to §4 for scenario cross-walk)

**Predecessor tasks actually read:** T-007, T-013, T-021, T-058 (all 4 `must`-gate predecessors)

**Assets selected:**
- A-001: T-007/D-002 development state report (routing behavior, gaps)
- A-002: T-013/D-005 failure/missing capability list (no-hit risk, resolver blocked)
- A-003: T-021/D-001 standard resource guide (canonical index/matrix reference)
- A-004: T-058/D-001 stress test handoff pack (29 scenarios for mapping)
- A-005: T-007/D-005 gap and risk list (LLM stability, latency, NOT_FOUND patterns)

**No missing assets, planned-web assets, or intentionally unused assets.**

**Files written:**
- `2_protocol/2_protocol_split/protocol.md` — full protocol with 6 route types, 5 inputs, 4 execution steps, 8 acceptance criteria
- `2_protocol/3_asset_rule/asset_rule.yaml` — 5 required assets, 3 output paths, modifiable/non-modifiable scoped
- `1_asset/registration.yaml` — 5 registered predecessor assets with source paths

**Confirmation:** No downstream prompt endpoint was called. No implementation, no delivery artifacts, no task status change.

配置完成。请确认：配置通过 / 提出修改意见
