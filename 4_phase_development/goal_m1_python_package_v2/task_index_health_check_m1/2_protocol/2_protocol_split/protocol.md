# task_index_health_check_m1 — Protocol

## Objective

Check the health of M1-relevant query indexes from T-021 standard resources before real loader hardening (T-047). Verify index schema, readability, required keys, missing fields, and known gaps for forward/reverse demos. Deliver an index health report and machine-readable check summary. Must not rebuild or overwrite authoritative indexes; may only report minimal patch recommendations.

This is an audit/check asset, not a rebuild task. T-045 supports T-047 (resource_loader_hardening_m1) and must not block the fixture-only M1 path.

## Steps

### Step 1 — Load and inspect required core indexes
- Read `cellline_index.json`, `drug_index.json`, `gene_index.json`, `function_index.json` using Python
- Verify each is valid JSON and parseable
- Record file size, top-level type (array/object), and rough element count
- Output: per-index schema summary in `3_execution/step1_core_schema_summary.json`

### Step 2 — Validate M1-required keys for each core index
- cellline_index: check for valid cell line name list
- drug_index: check for drug alias → BRD-id mapping keys
- gene_index: check for gene symbol lookup keys and type annotation
- function_index: check for 91 function terms (50 Hallmark + 41 3CA MPS) and term-to-id mapping
- Report any structural anomalies (null keys, duplicate keys, malformed values)
- Output: `3_execution/step2_key_validation.json`

### Step 3 — Inspect optional neighbor/tree indexes for forward/reverse query fitness
- Read cellline_neighbors.json, cellline_tree.json, drug_neighbors.json, gene_neighbors.json, gene_neighbors_simple.json, gene_index_simple.json
- Verify neighbor graphs have expected edge cardinality (non-empty for major entities)
- Verify cellline_tree is a valid tree structure
- Report any missing or degenerate graphs that would break proxy-matching in forward/reverse queries
- Output: `3_execution/step3_neighbor_health.json`

### Step 4 — Cross-reference index coverage with M1 demo requirements
- Consult T-042 contract or T-042 demo cases for expected entity types (drug, gene, cell line, function term)
- Check whether the indexes cover the entity types needed for forward query (perturbation + context → function) and reverse query (function + context → perturbation)
- Identify index-to-demo gaps: entities present in demo case but missing from index
- Output: `3_execution/step4_coverage_gap.json`

### Step 5 — Generate machine-readable health summary
- Produce `4_artifact/2_persist/index_health_summary.json` with:
  - per-index schema status (valid/invalid/warning)
  - per-index key completeness score
  - per-index size in bytes and element count
  - known gaps list
  - patch recommendations (if any minimal fixes are safe)
- Output: `4_artifact/2_persist/index_health_summary.json`

### Step 6 — Generate human-readable health report
- Produce `4_artifact/2_persist/index_health_report.md` summarizing:
  - which indexes pass, which have warnings, which block M1 use
  - key findings for T-047 (loader hardening)
  - advice on whether fixture path alone is sufficient or real indexes are M1-ready
- Output: `4_artifact/2_persist/index_health_report.md`

### Step 7 — Write gap notes for human review
- Produce `4_artifact/3_document/gap_notes.md` with:
  - human-readable narrative of each gap
  - affected M1 demo case (forward/reverse)
  - severity (blocker / warning / cosmetic)
  - suggested resolution path (e.g. patch index, adjust demo, accept gap)
- Output: `4_artifact/3_document/gap_notes.md`

## Deliverables

| Path | Type | Description |
|------|------|-------------|
| `4_artifact/2_persist/index_health_summary.json` | deliverable | Machine-readable index health summary with per-index schema, key completeness, size, gaps, and patch recommendations |
| `4_artifact/2_persist/index_health_report.md` | deliverable | Human-readable health report with pass/warn/block per index and T-047 handoff advice |
| `4_artifact/3_document/gap_notes.md` | support | Human-readable gap narrative with severity, affected demo case, and resolution path |