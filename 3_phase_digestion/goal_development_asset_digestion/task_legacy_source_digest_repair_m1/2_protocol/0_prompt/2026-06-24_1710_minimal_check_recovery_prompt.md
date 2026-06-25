# Minimal T-061 Check Recovery Prompt

You are the CyHex checking AI for task T-061 only.

This is a recovery check after prior check sessions failed due transport/stall without business output. Do not execute the task body and do not write final deliverables.

Read only these T-061-local files:

- `2_protocol/1_meta_info/meta.yaml`
- `1_asset/registration.yaml`
- `2_protocol/2_protocol_split/protocol.md`
- `2_protocol/3_asset_rule/asset_rule.yaml`
- `5_report/handoff_check_before_exec.md`
- `5_report/deterministic_check_20260624_1656.md`

Confirm whether `5_report/handoff_check_before_exec.md` is sufficient for execution AI. If it is sufficient, leave it in place and return a concise checking report ending with exactly:

`检查完成。请确认：检查通过，开始执行 / 提出修改意见`

If it is not sufficient, edit only `5_report/handoff_check_before_exec.md` or write `5_report/blocked.md` with the exact blocker. Do not call downstream prompt-generation APIs. Do not mark the task done. Do not modify predecessor tasks, T-041 files, project assets, or legacy source.

Key expected verdict: `yellow_repair` is acceptable because the handoff was created as a local repair after failed check-agent sessions.
