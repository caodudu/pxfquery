# Legacy Flat Asset Library Dedup Record

Date: 2026-07-20

Asset directory:

`/Users/dudu/Documents/3_Project/12_PxFquery/2_project_asset/1_raw_material/legacy_flat_asset_library_v20260614`

Reason:

This T002-derived flat legacy asset library contained hash-identical large files under two material-number ranges. The duplicate copies were replaced with relative symlinks to preserve path compatibility while removing duplicated storage.

Size change:

- Before deduplication: about 6.9G.
- After deduplication: about 4.6G.

Replacements:

| Replaced path | Symlink target | Verified SHA256 |
|---|---|---|
| `data/functional_matrices/M-0199_cp_func_ad.h5ad` | `M-0105_cp_func_ad.h5ad` | `db0bdb7af15fc75703a739b56ecdc7c6fc8f255d5f063ec97459836626b8130d` |
| `data/functional_matrices/M-0200_sh_func_ad.h5ad` | `M-0106_sh_func_ad.h5ad` | `e4fa7516e7d61c6a2db2211c02a4382ba07349f181e8dc04541d3b2e4f5f909b` |
| `data/functional_matrices/M-0201_xpr_func_ad.h5ad` | `M-0107_xpr_func_ad.h5ad` | `0fc84d0384f4cc6bbb4d74f33602e15892516af2a4191f716c79ce8e119a97a2` |
| `results/gsea_tables/M-0236_cp_gsea_100terms.csv` | `M-0114_cp_gsea_100terms.csv` | `e01f9f41ff1cf0c5fc860417480b7a9a2226b0c4b94b61fd7a0c1880ce08d987` |
| `results/gsea_tables/M-0237_sh_gsea_100terms.csv` | `M-0115_sh_gsea_100terms.csv` | `3355ef58985b50c38f99bb9c539107981bc2669343648bbd59d4dd9ef2b2906f` |
| `results/gsea_tables/M-0238_xpr_gsea_100terms.csv` | `M-0116_xpr_gsea_100terms.csv` | `8d1b4cae50df8453ed082d33e7491f542882bfb27885feb21f5d3247f607cc82` |

Notes:

- Only hash-identical duplicate files were replaced.
- The retained entity files are the lower-numbered material IDs.
- The replacement links are relative symlinks, so the library remains relocatable within P012.
