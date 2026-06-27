# Release Policy

PxFquery versions are source releases.

## Rules

1. One release should change one direction clearly.
2. Public behavior changes must be documented in `README.md` and `CHANGELOG.md`.
3. Every public package change must bump `src/pxfquery/_version.py`.
4. Every version must have a GitHub commit, a Git tag, and test output.
5. Old versions are never overwritten or relabeled.
6. Source installation is the project workflow.

## Version Map

| Version | Git tag | Status |
| --- | --- | --- |
| 0.1.0 | v0.1.0 | preserved |
| 0.1.1 | v0.1.1 | preserved |
| 0.1.2 | v0.1.2 | preserved |
| 0.1.3 | v0.1.3 | preserved |
| 0.1.4 | v0.1.4 | current |
