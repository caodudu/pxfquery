# M1 Python Package Milestone Report — T-053

**Generated:** 2026-06-24  
**Task:** T-053 m1_python_package_milestone  
**Objective:** Aggregate T-050 forward validation, T-051 reverse validation, and T-052 package assembly into a single M1 milestone deliverable.

---

## Overall Verdict: **PASS**

All three evidence gates are green. No missing evidence. All predecessor tasks completed with PASS verdicts.

| Evidence Stream | Source Task | Verdict | Checks | Key Assets |
|----------------|-------------|---------|--------|------------|
| Forward Validation | T-050 | PASS | 11/11 | A-001, A-002 |
| Reverse Validation | T-051 | PASS | 42/42 | A-003, A-004, A-005 |
| Package Assembly | T-052 | PASS | 9/9 (acceptance) | A-006 through A-012 |

---

## Final Package Location & Version

| Attribute | Value |
|-----------|-------|
| Package name | `pxfquery` |
| Version | `0.1.0` |
| Package source path | `1_asset/assembled_package_source/` (symlink to T-052 `4_artifact/1_package/`) |
| Install method | `pip install -e .` (editable install) |
| Build system | hatchling |
| CLI entry point | `pxfquery = pxfquery.cli:main` |

### Package Structure
```
4_artifact/1_package/
├── pyproject.toml
├── README.md
└── src/pxfquery/
    ├── __init__.py        (version 0.1.0, exports PxFquery)
    ├── core.py            (PxFquery class wiring)
    ├── cli/               (forward, reverse, info subcommands)
    │   ├── __init__.py
    │   └── __main__.py
    ├── query/
    │   ├── __init__.py
    │   ├── forward.py     (forward_query from T-059)
    │   └── reverse.py     (reverse_query from T-060)
    ├── data/
    │   ├── __init__.py
    │   ├── loader.py      (base loader)
    │   └── m1_loader.py   (M1FixtureLoader)
    ├── index/             (cellline, drug, function, gene indexes)
    │   ├── __init__.py
    │   ├── cellline_index.py
    │   ├── drug_index.py
    │   ├── function_index.py
    │   └── gene_index.py
    ├── llm/               (prompt templates)
    │   ├── __init__.py
    │   └── prompts.py
    └── viz/               (visualization)
        ├── __init__.py
        └── plots.py
```

---

## Evidence Summary

### Forward Validation (T-050) — 11/11 PASS
- **Loader:** `pxfquery.data.m1_loader.M1FixtureLoader` (`synthetic_repair` provenance)
- **Positive:** `pert2func("EGFR", "A549", matrix_type="xpr")` → found:true, top_activated (4), top_suppressed (3)
- **No-hit:** `pert2func("UNKNOWN_GENE_XYZ999", "A549")` → structured `PerturbationNotFound` error, no traceback
- **Reference match:** Structural keys match reference (excluding `_evidence` harness field)
- **CLI:** `pxfquery forward --perturbation EGFR --cell-line A549` → exit 0, valid JSON

### Reverse Validation (T-051) — 42/42 PASS
- **Loader:** `pxfquery.data.m1_loader.M1FixtureLoader` (`reverse_repair_manifest_m1_1`)
- **Ranking method:** Cosine similarity (target vector: +1 activate, -1 suppress)
- **Positive:** `func2pert(activate=["HALLMARK_APOPTOSIS"], suppress=["HALLMARK_MYC_TARGETS_V1"], cell_line="A549")` → found:true, top-3: THTPA (1.0), SCD (0.999959), TP53 (0.999541)
- **Error cases:** NoMatrixLoaded, ProgramNotFound, ContextNotFound, LowConfidenceResult, EmptyTarget — all structured properly
- **CLI:** `pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549` → exit 0, valid JSON

### Package Assembly (T-052) — 9/9 Acceptance Criteria PASS
- `pip install -e .` succeeds
- `import pxfquery; print(__version__)` → 0.1.0
- `pxfquery info` → valid JSON with package name, version, matrix_types
- `pxfquery forward --help` → shows all options
- `pxfquery reverse --help` → shows all options
- Forward demo → found:true (EGFR/A549/xpr)
- Reverse demo → found:true (HALLMARK_APOPTOSIS + MYC_TARGETS_V1 / A549)
- All output JSON well-formed per T-042 contract
- No query logic reimplemented — all from predecessor imports

---

## Layered Asset Map

See `4_artifact/5_table/layered_asset_map_v20260624_061117.csv` for full mapping.

| Layer | Predecessor | Assets | Description |
|-------|-------------|--------|-------------|
| 1 — Skeleton | T-044 | (CLI wiring via A-010) | Base CLI structure, index modules |
| 2 — Forward Impl | T-059 | (internal) | forward_query logic, M1FixtureLoader |
| 3 — Reverse Impl | T-060 | (internal) | reverse_query logic |
| 4 — Package Assembly | T-052 | A-006 to A-012 | Assembled package, demos, smoke test |
| 5 — Forward Validation | T-050 | A-001, A-002 | 11-check forward validation |
| 6 — Reverse Validation | T-051 | A-003, A-004, A-005 | 42-check reverse validation |

---

## Demo Commands

See `4_artifact/2_persist/demo_commands_v20260624_061117.md` for full reference.

```bash
# Info
pxfquery info

# Forward query
pxfquery forward --perturbation EGFR --cell-line A549 --manifest <path> --fixture-root <path>

# Reverse query
pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549 --manifest <path> --fixture-root <path>
```

---

## Known Gaps

See `4_artifact/5_table/known_gaps_v20260624_061117.md` for full report.

7 low-severity gaps identified, all expected for M1 milestone:
- Synthetic fixture validation (not real LINCS data)
- No wheel/distribution build tested
- Minimal demo scope (1-2 test cases per query direction)
- 1 zero-norm candidate skipped in reverse query

No missing evidence or failed evidence streams.

---

## Deliverables

| Deliverable | Path | Status |
|------------|------|--------|
| Milestone report | `4_artifact/3_document/milestone_report_v20260624_061117.md` | produced |
| Evidence index | `4_artifact/2_persist/evidence_index_v20260624_061117.json` | produced |
| Layered asset map | `4_artifact/5_table/layered_asset_map_v20260624_061117.csv` | produced |
| Known gap report | `4_artifact/5_table/known_gaps_v20260624_061117.md` | produced |
| Demo commands | `4_artifact/2_persist/demo_commands_v20260624_061117.md` | produced |
| Completion report | `5_report/completion.md` | produced |

All predecessor artifacts preserved. No modifications to T-050, T-051, or T-052 directories.
