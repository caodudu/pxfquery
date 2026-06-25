# Delivery QA: T-060 reverse_query_core_repair_m1

## Verdict
red_return

## Checks Performed
- Confirmed CyHex local API is running and reports app version `1.2.19`, matching the task metadata.
- Checked task-local delivery structure without scanning predecessor task contents or project raw assets.
- Confirmed required repair fixture, repair manifest, provenance report, positive demo JSON, no-hit/error JSON, ranking CSV, and HTML reports exist under `4_artifact/`.
- Confirmed `3_execution/` contains process artifacts only: generation/evidence scripts, CLI smoke stdout, fixture summary, and checklist.
- Checked `4_artifact/registry.yaml`, `5_report/completion.md`, and both HTML reports for internal consistency.
- Escalated from green-pass because the registered core package path is not a task-local delivered package.

## Repairs Made
- Rewrote this QA report into the required delivery-QA shape.
- Added `5_report/handoff_ai_use.md` to preserve downstream handoff context and the red-return reason.

## Remaining Issues
- Core deliverable `T-060/D-001` is registered as `4_artifact/1_package/pxfquery`, but that path is a symlink to the predecessor T-044 package skeleton outside this task:
  `/Users/dudu/Documents/3_Project/12_PxFquery/4_phase_development/goal_m1_python_package_v2/task_package_skeleton_m1/4_artifact/1_package/pxfquery`.
- Within the T-060 task directory, no task-local reverse query package source files were found under `4_artifact/1_package/pxfquery`; `find` only reports the symlink itself.
- Because the task contract requires T-060 to deliver the reverse query package code as the same-layer replacement for T-049, this cannot be repaired by delivery metadata alone.

## Execute Revision Required
yes

## Next Action
execute_revision
