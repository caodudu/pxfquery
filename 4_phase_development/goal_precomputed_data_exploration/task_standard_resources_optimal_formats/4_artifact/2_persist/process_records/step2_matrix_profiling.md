# T-021 Step 2: Matrix Profiling & Duplicate Verification

**Generated:** 2026-06-23

## Canonical Set Selection

Two vintage pairs exist in `functional_matrices/`:
- M-0105~M-0107 (canonical)
- M-0199~M-0201 (duplicate)

### Verification Results

| Pair | Canonical | Duplicate | MD5 Match | Identical? |
|---|---|---|---|---|
| cp | M-0105 (n=201,014) | M-0199 | Yes | Yes |
| sh | M-0106 (n=189,365) | M-0200 | Yes | Yes |
| xpr | M-0107 (n=132,464) | M-0201 | Yes | Yes |

All vintage pairs are byte-identical. **Selected M-0105~M-0107** as canonical.

## Matrix Profiles

### cp (Compound) — M-0105
| Property | Value |
|---|---|
| File size | 569.43 MB |
| n_obs | 201,014 |
| n_vars | 91 |
| X dtype | float64 |
| X range | [-10.0, 10.0] |
| X mean | −0.098 |
| X std | 1.74 |
| Nonzero fraction | 1.00 (dense) |
| Unique cell lines | 229 |
| Unique perturbations | 34,413 |
| Cell line examples | A375, HEPG2, PC3, A549 |

### sh (shRNA) — M-0106
| Property | Value |
|---|---|
| File size | 533.24 MB |
| n_obs | 189,365 |
| n_vars | 91 |
| X dtype | float64 |
| X range | [-10.0, 10.0] |
| X mean | −0.204 |
| X std | 1.41 |
| Nonzero fraction | 1.00 (dense) |
| Unique cell lines | 22 |
| Unique perturbations | 27,920 |

### xpr (ORF) — M-0107
| Property | Value |
|---|---|
| File size | 370.31 MB |
| n_obs | 132,464 |
| n_vars | 91 |
| X dtype | float64 |
| X range | [-10.0, 10.0] |
| X mean | −0.086 |
| X std | 1.12 |
| Nonzero fraction | 1.00 (dense) |
| Unique cell lines | 26 |
| Unique perturbations | 13,466 |

### Var Names (consistent across all 3):
- 50 HALLMARK terms (start with "HALLMARK_")
- 41 3CA MPS terms (start with "MP" + number)
- Sample: HALLMARK_ADIPOGENESIS, HALLMARK_APOPTOSIS, ..., MP39 Metal-response, MP40 PDAC-related, MP41 Unassigned

## Estimates

- Float64 raw memory per CP matrix (X only): ~139.6 MB
- Float32 raw memory per CP matrix (X only): ~69.8 MB
- Total canonical float64 raw memory: ~450.2 MB (X only)
- Total canonical float32 raw memory: ~225.1 MB (X only)

See also: `4_artifact/2_persist/process_records/step2_matrix_profiling.json`