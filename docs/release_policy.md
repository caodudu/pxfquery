# Release Policy

PxFquery versions are task-scoped.

## Rules

1. One CyHex task owns one package version.
2. One task should change one direction only.
3. Every public package change must bump `src/pxfquery/_version.py`.
4. Every version must have:
   - a GitHub commit
   - a Git tag
   - a `CHANGELOG.md` entry
   - a `docs/releases/vX.Y.Z-*.md` note
   - test output
5. Old versions are never overwritten or relabeled.
6. GitHub is the primary review window for source changes.

## Version Owner Map

| Version | CyHex task | Git tag | Status |
| --- | --- | --- | --- |
| 0.1.0 | T-117 through T-123 | v0.1.0 | preserved |
| 0.1.1 | T-124 | v0.1.1 | preserved |
| 0.1.2 | T-125 | v0.1.2 | preserved |
| 0.1.3 | T-126 | v0.1.3 | current |
