# T-064 Minimal Execute Recovery Prompt

You are recovering T-064 after an `execute_stalled` OpenCode session. Work only inside:

`/Users/dudu/Documents/3_Project/12_PxFquery/3_phase_digestion/goal_project_delivery_anchor/task_evidence_routing_anchor`

Do not modify predecessor tasks. Do not send messages to existing CLI sessions. Do not rewrite protocol files. Do not reread large predecessor assets unless a listed T-064 artifact is missing.

## Recovery Objective

Verify that the task-local repaired deliverables satisfy the T-064 protocol, then finish the execute stage with a concise Completed response.

## Files to verify

- `4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md`
- `4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml`
- `4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv`
- `4_artifact/3_document/execution_report_v20260625.html`
- `4_artifact/3_document/result_report_v20260625.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

## Required checks

1. Confirm the taxonomy defines all six route types: exact-hit, proxy-hit, no-hit, ambiguous-hit, context-missing, transfer/suggestion.
2. Confirm the metadata contract YAML parses and defines route_type, query_context, perturbation_resolution, function_response, confidence, proxy_chain, diagnostics, suggestions, llm_fields, and threshold_policy.
3. Confirm the stress-test mapping CSV parses and has 29 data rows from SC-001 through SC-029.
4. Confirm registry.yaml parses and registers the accepted artifacts.
5. Confirm completion.md states the repair context and acceptance evidence.

## If checks pass

Do not create new design content. Optionally add `5_report/execute_recovery_verification_20260625.md` summarizing the checks. End with a `Completed` response listing the verified files.

## If checks fail

Repair only missing or obviously malformed T-064-local files listed above. If repair cannot be completed, write `5_report/blocked.md` and end with `Blocked`.
