

I'll execute the CyHex checking stage. Let me start with the mandatory protocol read and all required
Good, CyHex checked. Now read all required current
Now let me check if the prompt includes the protocol,
Good, the prompt is complete and consistent with the current protocol and asset rules. Now let me spot-check the existence and non-emptiness of the required
The globs don't expand in the script — let
Found the scope note file at a different path. Let
The file name is `genes_bioinformatics_deliverable_catalog_scope_note_v20260618.md` (not `artifact_deliverable`). Let me check the registered path
Good, the file exists with nonzero content. The registration.yaml path for A-007 references `genes_bioinformatics_artifact_deliverable_catalog_scope_note_v20260618.md` but the actual filename is `genes_bioinformatics_deliverable_catalog_scope_note_v20260618.md`. The D-001 registry in T012 uses the correct filename: `genes_bioinformatics_deliverable_catalog_scope_note_v20260618.md`. So the registration.yaml has an incorrect filename for A-007. Same issue for A-008:
A-008 is correct. Let me also verify A
A-009 also correct. Now I know the A-007 path in registration.yaml and asset_rule.yaml has an incorrect filename — it says `genes_bioinformatics_artifact_deliverable_catalog_scope_note` but the real file is `genes_bioinformatics_deliverable_catalog_scope_note`. Let me also
All 9 required assets exist and have nonzero content. Now I need to fix the A-007 path bug (wrong filename in both registration.yaml and asset_rule.yaml). Let me also check the 
Good, `3_execution/` is empty which is expected before execution. Now let me also check `4_artifact/` to see what already
Now I need to fix the A-007 filename in registration.yaml and asset_rule.yaml. Let me
Prompt regenerated. Now let me also fix the task name in meta.yaml — the task is called "
Now let me verify the final state of all configuration files
