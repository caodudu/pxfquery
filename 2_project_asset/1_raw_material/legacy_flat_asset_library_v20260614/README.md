# Legacy Flat Asset Library v20260614

This library is the T-002 first-pass migration output. It uses a flat asset-type layout: first-level folders are asset types; second-level folders are asset groups. Legacy paths are provenance only.

Large files are symlink placeholders in this first pass. After human layout acceptance, run `replace_symlinks_with_copies_v20260614.sh` to convert them into hard copies.

## Asset Types

- `background/`
- `code/`
- `data/`
- `results/`
- `reports/`
- `manuscript/`
- `history/`
- `provenance/`
