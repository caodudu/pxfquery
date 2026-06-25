# T-060 Execution Step Checklist

Generated: 2026-06-24

## Step 1: Contract Extraction

- Sub-goal: Extract the reverse API, JSON shape, positive demo, and no-hit/error behavior from registered T-042 assets.
- Operation: Read `1_asset/m1_api_contract.yaml` and `1_asset/m1_demo_cases.yaml`.
- Expected evidence: This checklist plus generated JSON evidence matching the contract.
- Dependency: None.
- Status: complete.

## Step 2: Registered Fixture And Loader Gap Check

- Sub-goal: Confirm whether the selected fixture can satisfy the reverse positive demo.
- Operation: Inspect `1_asset/fixture_package_m1`, `1_asset/m1_fixture_loader_code.py`, and `1_asset/m1_loader_smoke_evidence.csv`.
- Expected evidence: Original fixture lacks `HALLMARK_MYC_TARGETS_V1`; original xpr fixture has no A549 rows.
- Dependency: Step 1.
- Status: complete.

## Step 3: Task-Local Repair Substrate

- Sub-goal: Create a repair fixture and manifest sufficient for the T-042 reverse positive demo.
- Operation: Copy registered fixture sidecars and generate synthetic/repair matrix additions under `4_artifact/2_persist/`.
- Expected evidence: `reverse_repair_fixture_m1_1/`, `reverse_repair_manifest_m1_1.yaml`, and provenance report.
- Dependency: Step 2.
- Status: complete.

## Step 4: Reverse Query Core

- Sub-goal: Deliver deterministic reverse query package code compatible with the T-046 loader shape.
- Operation: Extend the T-044 package skeleton under `4_artifact/1_package/pxfquery/`.
- Expected evidence: importable package exposing `PxFquery.func2pert`, CLI `reverse`, stable cosine ranking, and structured errors.
- Dependency: Step 1 and Step 2.
- Status: complete.

## Step 5: Validation Evidence

- Sub-goal: Run import/compile checks, positive demo, repeatability check, and no-hit/error smoke cases.
- Operation: Execute commands in `/Users/dudu/Softwares/miniconda/bin/conda run -n pxfquery python ...`.
- Expected evidence: JSON evidence files and ranking CSV under `4_artifact/`.
- Dependency: Step 3 and Step 4.
- Status: complete.

## Step 6: Registration And Reports

- Sub-goal: Register all reusable deliverables and write human-facing reports.
- Operation: Update `4_artifact/registry.yaml`, create HTML reports, and replace pending completion report.
- Expected evidence: complete registry, execution report, result report, and `5_report/completion.md`.
- Dependency: Step 5.
- Status: complete.
