I’ll stay inside the T-064 task directory and run targeted parse/content checks only on the listed local artifacts. If they pass, I’ll add the optional recovery verification note and close with the verified file list.
`rg` is not installed in this environment, so I’m switching to direct file checks and lightweight parsers. I’ll avoid broad repository reads and only touch the named T-064 files.
The local file set is present, and `completion.md` already records the execute-stalled repair context plus acceptance evidence. I’m now doing the mechanical checks: route terms, YAML parsing/keys, CSV parsing and scenario range, and registry contents.
One check failed narrowly: the YAML parses, but two required contract sections are not present under the exact protocol names `llm_fields` and `threshold_policy`. I’m inspecting only that contract and the registry shape, then I’ll patch the missing local contract fields without changing the design scope.
The registry already registers the three deliverables, but it describes the contract as an 8-field schema while the recovery protocol requires two additional top-level contract sections. I’m going to add those sections to the YAML and update the registry/completion wording to match the repaired contract, keeping edits local to the listed files.
The missing concepts are already partially present under older names (`thresholds` and diagnostic LLM fields), so the repair is a schema-alias/normalization patch: add protocol-named `llm_fields` and `threshold_policy` sections rather than inventing new content.
I’m editing three local files now: the metadata contract gets the two protocol-named sections, the registry note gets aligned to that contract, and completion gets one acceptance line naming the two repaired sections.
The contract now has the protocol-named sections. I’m making the reporting files reflect that normalization so the artifact registry and completion evidence are internally consistent.
`completion.md` is a richer report than the short version I first saw, but it was missing an explicit repair note. I’m adding that repair context and tightening the contract acceptance text.
The local repair note is now in place. I’m rerunning the full recovery check set before deciding whether to write the optional verification summary.
The YAML checks now pass, but the CSV parse fails on illegal quoting at line 11. This is one of the listed local artifacts, so I’m inspecting only the malformed lines and will repair CSV quoting without changing scenario content.
The malformed CSV has unescaped quotes in scenario descriptions such as `"a549"` inside an unquoted field. I’m checking whether Ruby can recover it with liberal parsing; if it can, I’ll use that parse to normalize the CSV safely.
Liberal parsing recovered 29 rows with the expected 12 columns, so this is a formatting repair rather than content reconstruction. I’m normalizing the CSV with proper quoting, then I’ll rerun strict parsing.
The CSV has been normalized from the recovered 29-row parse. I’m running the strict verification again now.
Strict CSV parsing now passes. The remaining failure is registry coverage: it registers the three core deliverables but not the two accepted HTML reports listed for verification, so I’m adding those report entries to `registry.yaml`.
I’m adding minimal registry records for the existing execution and result HTML reports. This is metadata registration only; I’m not changing report content.
The registry now includes the two report artifacts. I’m updating the completion evidence to avoid saying only the three core deliverables are registered when the reports are now included too.
I’ve completed the local repairs that the checks exposed. I’m running the full verification again and will only add the optional recovery note if everything passes.
All required checks pass now. I’m adding the optional recovery verification summary with the exact pass evidence, then I’ll do one final parse check.
The recovery verification note is written. I’m doing one last strict check over the listed artifacts plus the new verification file so the final response can be definitive.
Completed.

Verified:
- `4_artifact/2_persist/evidence_routing_route_taxonomy_v20260625.md`
- `4_artifact/2_persist/evidence_routing_metadata_contract_v20260625.yaml`
- `4_artifact/5_table/evidence_routing_stress_test_mapping_v20260625.csv`
- `4_artifact/3_document/execution_report_v20260625.html`
- `4_artifact/3_document/result_report_v20260625.html`
- `4_artifact/registry.yaml`
- `5_report/completion.md`

Also added:
- `5_report/execute_recovery_verification_20260625.md`

Strict YAML/CSV parsing passed, and the CSV contains 29 rows from `SC-001` through `SC-029`.
