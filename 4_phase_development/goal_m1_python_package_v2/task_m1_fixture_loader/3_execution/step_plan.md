# T-046 Execution Step List

Generated: 2026-06-24

1. Preflight selected assets and package layout.
   - Operation: inspect A-001 manifest, A-002 fixture file list, A-003 expected-shapes table, and the existing M1 package skeleton.
   - Expected evidence: notes identifying the fixture contract and implementation target.
   - Dependency: none.

2. Implement the fixture loader.
   - Operation: add a task-local package artifact following the existing `src/pxfquery` layout, with public loader APIs in `pxfquery.data.loader`.
   - Expected evidence: reusable Python code under `4_artifact/1_package/`.
   - Dependency: step 1.

3. Run smoke validation.
   - Operation: execute a small script through the project `pxfquery` conda environment, loading A-001/A-002 and checking observed structure against A-003.
   - Expected evidence: command log plus CSV/JSON/Markdown smoke evidence.
   - Dependency: step 2.

4. Promote documentation and reports.
   - Operation: write API notes, execution/result HTML reports, registry entries, and completion report.
   - Expected evidence: accepted deliverables under `4_artifact/` and `5_report/completion.md`.
   - Dependency: step 3.
