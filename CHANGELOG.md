# Changelog

## 0.1.2 - 2026-06-27

CyHex task: `T-125 task_ms7_public_api_single_class_v012`

- Narrowed the public top-level API contract to one class: `PxFQuery`.
- Enforced `pxfquery.__all__ == ["PxFQuery"]`.
- Moved provider registration and provider inspection behind `PxFQuery` methods in public docs.
- Rewrote README around the single class entrypoint.
- Preserved `v0.1.0` and `v0.1.1` as historical tags.

## 0.1.1 - 2026-06-27

CyHex task: `T-124 task_ms7_version_governance_v011`

- Added explicit version governance for the public package.
- Published `pxfquery.__version__`.
- Established a one-version-per-CyHex-task release rule.
- Added release documentation under `docs/releases/`.
- Preserved `v0.1.0` as a Git tag before this version bump.

## 0.1.0 - 2026-06-27

CyHex task range: `T-117` through `T-123`

- Initial private GitHub package export.
- Added package source, route contract, parser, resolver, deterministic engines, CLI, API, provider check, MS7 corpus fixture, and tests.
- Validated with the MS7 recovery package evidence set.
