I’ll execute T-043 inside its task directory only, using the registered T-014/T-021 assets and writing outputs under `3_execution/`, `4_artifact/`, and `5_report/`. I’ll first turn the approved strategy into a concrete checklist, then validate each output before closing.
CyHex is running (`1.2.19`) and the checker’s guidance matches the embedded protocol. The registered assets are present as symlinks, so I’m narrowing the next read to the authority documents/tables and the standard resource bundle structure.
Execution checklist for this task:
1. Confirm allowed inputs and record runtime evidence.
2. Read only A-002/A-004/A-005/A-006 plus relevant A-001/A-003 files to choose stable resource IDs and fixture samples.
3. Generate the fixture package and all required manifest/table/document/report deliverables from real A-001 records.
4. Validate generated files for shape, keys, provenance, and downstream demo adequacy, then register and report completion.
The authority files identify the M1 substrate as the three functional matrices, the query indexes including rebuilt `function_index.json`, and the five standard metadata CSVs. The bundle has the expected 19 files, so I’m now checking exact schemas and selecting linked real records for compact forward/reverse fixtures.
The conda stdin probes returned no visible output, so I’m switching to task-local Python scripts under `3_execution/` for reproducible inspection and generation. That also gives us durable evidence instead of transient terminal output.
I’m about to write the task-local generation script. It will load only `1_asset/t021_standard_resources_bundle` plus the registered T-014/T-021 documents/tables, extract deterministic real rows, and emit all reusable artifacts under `4_artifact/`.
The generation script is in place. I’m running it through the configured `pxfquery` conda environment so H5AD loading and CSV/JSON validation use the project runtime.
The first run failed because the patch landed relative to the repository root rather than the task directory. I’m checking the exact location and will move the script into the allowed task `3_execution/` path before rerunning.
