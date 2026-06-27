# Changelog

## 0.3.2 - 2026-06-27

- Current package source is organized as five inspectable layers: `nlu`, `routing`, `execution`, `evidence`, and `presentation`.
- `src/pxfquery/` root contains only thin entrypoints: `__init__.py`, `__main__.py`, and `_version.py`.
- Current main contains only the five-layer source layout and thin package entrypoints.
- `PxFQuery` is the only public top-level class.
- Biological results are not fabricated before resource-backed retrieval exists.
