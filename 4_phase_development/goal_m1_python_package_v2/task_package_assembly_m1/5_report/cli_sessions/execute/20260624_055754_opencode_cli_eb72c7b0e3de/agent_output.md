I'll execute the T-052 package_assembly_m1 task. Let me start by understanding the current state and predecessor assets.
Now let me read the data modules and manifests:
Let me also check the forward fixture structure and what the T-059 package looked like:
Good. Now I need to check the index, ll
Good, I now have full understanding of all assets. Let me execute the assembly.
Now copy pyproject.toml and assemble modules in
Now wire core.py with func2pert delegating to reverse_query:
The pyproject.toml references `README_TASK.md` which doesn't exist in the package dir. Let me fix it:
Package
All smoke tests pass. Now save evidence and run demos:
Now run forward and reverse demos:
Both demos pass. Let me save all evidence:
Now register artifacts and write reports:
Now write the execution report, result report, and completion report:
**T-052 package_assembly_m1 — Execution Complete. All acceptance criteria pass.**

**Summary of what was done:**

1. **Package assembly** — Created `4_artifact/1_package/src/pxfquery/` with `pyproject.toml` (hatchling build, `[project.scripts]` entry) and all modules: `query/` (forward + reverse), `data/` (M1FixtureLoader), `index/`, `llm/`, `viz/`, `cli/` (T-044 wiring with forward/reverse/info subcommands).

2. **Core wiring** — `core.py` `func2pert()` rewired from `NotImplemented` to delegate to `query/reverse.reverse_query()`, enabling the reverse query pipeline.

3. **Install & smoke** — `pip install -e .` succeeded. `import pxfquery`, `pxfquery.info`, `pxfquery --help`, `pxfquery forward --help`, `pxfquery reverse --help` all work.

4. **Forward demo** — `pxfquery forward --perturbation EGFR --cell-line A549` → `found: true` with top_activated (HALLMARK_ADIPOGENESIS +4.03, HALLMARK_APOPTOSIS +2.47) and top_suppressed.

5. **Reverse demo** — `pxfquery reverse --activate HALLMARK_APOPTOSIS --suppress HALLMARK_MYC_TARGETS_V1 --cell-line A549` → `found: true` with 10 top candidates (THTPA similarity 1.0, SCD 0.9999, TP53, BCL2L1, etc.).

**Deliverables produced (7/7):** Package source, import smoke evidence, forward demo JSON, reverse demo JSON, CLI help text, execution report (HTML), result report (HTML) — all registered in `4_artifact/registry.yaml`.
