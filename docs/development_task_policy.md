# Development Task Policy

PxFquery releases are reviewed from this private GitHub repository, but every externally visible package change must remain tied to a local CyHex task in the project workspace.

## Required Release Linkage

Every version must have:

- one scoped CyHex task;
- one source change direction;
- one version bump;
- one immutable Git tag;
- README, CHANGELOG, and docs updates when the public interface or demo flow changes;
- real test or smoke-command evidence recorded in the corresponding CyHex task directory.

Current task/version anchors:

| Version | CyHex task | Git tag | Purpose |
| --- | --- | --- | --- |
| 0.1.0 | T-123 | v0.1.0 | MS7 recovery package baseline |
| 0.1.1 | T-124 | v0.1.1 | Version governance |
| 0.1.2 | T-125 | v0.1.2 | Single-class public API |
| 0.1.3 | T-126 | v0.1.3 | scverse-style workflow API |

## Public API Rule

The package-facing public API baseline is:

```python
from pxfquery import PxFQuery
```

Scattered top-level function imports are not part of the public contract. Provider registration and query workflows should hang from the `PxFQuery` client unless a later CyHex task deliberately changes the API and records the migration.

The recommended workflow order is:

```python
pxf = PxFQuery()
pxf.settings.register_llm(...)
q = pxf.read.query(text)
pxf.pp.parse(q)
pxf.tl.resolve(q)
result = pxf.get.result(q)
```

## Anchor Digestion Rule

Legacy tasks, draft assets, stress corpora, previous delivery files, and user-review anchors can be used as reference inputs only after they are digested into a scoped task or reference asset. A downstream task must record:

- the source anchor;
- the audited reusable claims;
- the unsafe or non-reusable claims;
- how the downstream task is allowed to use the asset.

Directly copying old deliverables forward as success evidence is forbidden.
