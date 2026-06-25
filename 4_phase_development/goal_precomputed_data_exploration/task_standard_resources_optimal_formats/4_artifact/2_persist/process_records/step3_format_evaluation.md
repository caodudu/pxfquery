# T-021 Step 3: Optimal Format Evaluation

**Generated:** 2026-06-23

## 1. Float Precision: float64 → float32

**Conclusion: float32 is lossless for practical purposes.**

| Metric | cp | sh | xpr |
|---|---|---|---|
| Rank correlation (mean) | 1.000000 | 1.000000 | 1.000000 |
| Rank correlation (min) | 1.000000 | 1.000000 | 1.000000 |
| Top 5% overlap (mean) | 100.0% | 100.0% | 100.0% |
| Bottom 5% overlap (mean) | 100.0% | 100.0% | 100.0% |
| Max abs difference | ~0.00025 | ~0.00025 | ~0.00025 |
| Mean abs difference | ~3×10⁻⁶ | ~3×10⁻⁶ | ~3×10⁻⁶ |

## 2. Storage Format Comparison (cp example)

| Format | Size | Compatible? |
|---|---|---|
| h5ad float64 (original) | 569.43 MB | Yes (orig) |
| h5ad float32 | 105.11 MB | Yes |
| parquet zstd | 99.21 MB | No (no AnnData) |
| feather zstd | 66.14 MB | No (no AnnData) |
| Table split (CSV + NPY) | 85.60 MB | No (needs package change) |

## 3. Table-Split Feasibility

The pxfquery `DataLoader` class exclusively uses `anndata.read_h5ad`. Splitting the AnnData into separate perturbation_meta.csv, function_meta.csv, and score.parquet would require rewriting the package code. **Not recommended.**

## 4. Metadata Consolidation

- Cell line: M-0234 (enriched, deduplicated from M-0093/M-0184)
- Compound: M-0235 (enriched, deduplicated from M-0099/M-0188)
- Cell line info: M-0185 (beta detailed annotations)
- Compound info: M-0186 (beta detailed annotations)
- Gene info: M-0187 (beta gene annotations)

## 5. Query Index Compactness

All 9 existing JSON indexes are already in optimal compact format:
- Drug neighbors: BRD- prefix stripped, Tanimoto as int×100
- Gene neighbors: cosine as int×100, sorted descending
- JSON is the only format pxfquery index loaders support

## 6. Function Index Status

- `function_index.json`: **MISSING** in legacy migration
- Must be rebuilt: 50 HALLMARK + 41 3CA MPS = 91 terms
- Use matrix `var` names as source of truth

## Decision Summary

| Resource | Optimal Format | Rationale |
|---|---|---|
| Functional matrices | h5ad float32 | 82% size reduction, perfect precision, compatible with pxfquery |
| Query indexes | JSON | Already compact, only format supported by pxfquery index loaders |
| Metadata | CSV | Small (<5 MB), human-readable, pandas-compatible |

See also: `4_artifact/2_persist/process_records/step3_format_evaluation.json`