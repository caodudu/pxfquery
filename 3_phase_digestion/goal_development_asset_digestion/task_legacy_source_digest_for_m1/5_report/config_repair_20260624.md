T041 config repair note
=======================

Reason:
The initial OpenCode configuration session failed after a model gateway 502 / JSON parse error. It had already written `1_asset/registration.yaml`, but `protocol.md` and `asset_rule.yaml` remained blank templates.

Repair performed:
- Preserved the asset registration written by the failed config session.
- Wrote a focused task protocol for source digestion only.
- Wrote asset rules that allow only the explicit migrated package source and forbid broad project-asset scanning, direct historical-root reads, and failed T024-T040 route inputs.

Scope:
This repair only edits T041 local configuration files and report notes. It does not approve the failed session, does not mark the task done, and does not modify upstream completed artifacts or legacy source files.

Next expected CyHex step:
Retry or re-enter the configuration/check flow using the repaired task files.
