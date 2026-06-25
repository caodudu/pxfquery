# T-064 Minimal Delivery Recovery Prompt

You are recovering T-064 after `deliver_interrupted`.

Work only inside:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor`

Do not modify predecessor tasks. Do not send messages to existing CLI sessions. Do not rewrite task protocol files. Do not rerun implementation or redesign work.

## Recovery Objective

Verify the existing T-064 delivery QA result and finish the delivery QA stage cleanly.

## Files to check

- `5_report/delivery_qa.md`
- `5_report/completion.md`
- `4_artifact/registry.yaml`
- `4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md`
- `4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml`
- `4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv`
- `4_artifact/3_document/execution_report_v20260625.html`
- `4_artifact/3_document/result_report_v20260625.html`

## Required checks

1. Confirm `delivery_qa.md` contains a green/pass verdict or equivalent deliverable-ready conclusion.
2. Confirm registry and completion are consistent with the five registered artifact/report files.
3. Confirm the three core deliverables and two HTML reports exist and are non-empty.
4. Do not create new design content unless a listed report is missing.

## If checks pass

Optionally write `5_report/delivery_recovery_verification_20260625.md` with a concise summary.
End with a `Completed` response stating that T-064 is deliverable and no repair is needed.

## If checks fail

Repair only task-local missing report/registry/completion inconsistencies. If repair cannot complete, write `5_report/blocked.md` and end with `Blocked`.
