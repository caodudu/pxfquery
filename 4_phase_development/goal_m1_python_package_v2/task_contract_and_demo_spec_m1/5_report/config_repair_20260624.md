T042 config repair note
=======================

Reason:
The initial Codex configuration session failed before writing task configuration files. The session log ended with `Unsupported content type`; `protocol.md`, `registration.yaml`, and `asset_rule.yaml` remained template/empty.

Repair performed:
- Registered selected T007 and T013 artifacts as T042 input assets.
- Wrote a task-specific protocol for the M1 contract/demo-spec task.
- Wrote asset rules that forbid raw project assets, direct legacy-root reads, and failed T024-T040 route inputs.

Scope:
This repair only edits T042 local configuration files and report notes. It does not approve the failed session, does not mark the task done, and does not modify upstream completed artifacts.

Next expected CyHex step:
Retry or re-enter the configuration/check flow using the repaired task files.
