# Changelog

## 0.2.0 - 2026-06-27

- Refactored the public package surface around the MS8 input-kernel-output product model.
- Added `PxFQueryAnswer` as the human-readable answer object returned by `PxFQuery.ask(...)`.
- Kept `PxFQuery.query(...)` as the structured dictionary compatibility layer.
- Added `pxf.resources.status()`, `pxf.resources.use(...)`, `pxf.resources.use_manifest(...)`, and `pxf.resources.download(...)` as the resource-pack management surface.
- Updated CLI `pxfquery query` to print a readable answer by default, with `--json` for structured output.
- Rewrote README and data asset docs around biomedical natural-language questions, resource packs, evidence, and limitations.
- Documented that the real resource-pack-backed query kernel remains a later MS8 implementation layer.

## 0.1.5 - 2026-06-27

- Corrected the data input contract to the real flat 19-file `standard_resources/` layout.
- Expanded default asset registration to include matrices, query indexes, metadata tables, and provenance.
- Updated README and data asset docs so examples no longer use invented `matrices/` or `indexes/` subfolders.

## 0.1.4 - 2026-06-27

- Reworked the recommended public workflow around a single `PxFQuery` client.
- Added runtime data asset registration by root or manifest.
- Added `PxFQuery.ask(...)` as the README query entry point.
- Updated README to show concrete query output instead of interface concepts.
- Added asset-registration test coverage.

## 0.1.3 - 2026-06-27

- Added a lightweight query work object for stepwise parse/route/resolve execution.
- Corrected README ordering so LLM/provider registration happens before provider-dependent checks or query execution.
- Added provider-first workflow test coverage.
- Kept `PxFQuery` as the only top-level public class while preserving one-step convenience methods for scripts.

## 0.1.2 - 2026-06-27

- Narrowed the public top-level API contract to one class: `PxFQuery`.
- Enforced `pxfquery.__all__ == ["PxFQuery"]`.
- Moved provider registration and provider inspection behind `PxFQuery` methods in public docs.
- Rewrote README around the single class entrypoint.
- Preserved `v0.1.0` and `v0.1.1` as historical tags.

## 0.1.1 - 2026-06-27

- Added explicit version governance for the public package.
- Published `pxfquery.__version__`.
- Established a one-version-per-release discipline.
- Added release documentation.
- Preserved `v0.1.0` as a Git tag before this version bump.

## 0.1.0 - 2026-06-27

- Initial private GitHub package export.
- Added package source, route contract, parser, resolver, deterministic engines, CLI, API, provider check, corpus fixture, and tests.
- Validated with the initial recovery package evidence set.
