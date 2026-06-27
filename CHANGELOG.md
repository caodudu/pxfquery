# Changelog

## 0.4.0 - 2026-06-27

- Current package source is organized as five inspectable internal folders: `l1_nlu`, `l2_routing`, `l3_execution`, `l4_evidence`, and `l5_presentation`.
- `src/pxfquery/` root contains only thin entrypoints: `__init__.py` and `__main__.py`.
- `PxFQuery` is the only public top-level class.
- `PxFQuery` exposes a scanpy-style user interface: `read.query`, `pp.parse`, `tl.route`, `tl.execute`, `tl.assemble`, `get.result`, and `get.answer`.
- Biological results are not fabricated before resource-backed retrieval exists.
