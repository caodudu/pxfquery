# Python package milestone — Protocol

## Objective

Build a runnable PxFquery Python package milestone from existing digestion, MVP review, and precomputed-data understanding outputs. The milestone must produce real package code, tests, demo evidence, and Chinese HTML reports rather than only planning text.

## Upstream Boundary

- T-007 defines the current interpretation of PxFquery development state.
- T-013 defines current MVP pass/fail evidence and missing capabilities.
- T-014 defines the precomputed data landscape and can support a fast demo fixture route.
- T-021 is the later standard-resource route. Package development must not block entirely on T-021; standard-resource integration waits for it.

## Task Strategy

1. Freeze a package/API/resource/test contract.
2. Produce a small demo fixture from T014/T013 so development can start immediately.
3. Build importable package core.
4. Implement deterministic forward/reverse query APIs.
5. Repair index/resolver compatibility enough for milestone claims.
6. Build regression tests and a demo.
7. Integrate T021 standard resources as a separate enhancement when ready.
8. Produce a package milestone report with claim boundaries.

## Fast-Pass Policy

Use `fast_pass_permission: green` for these new tasks. Green only authorizes CyHex to pass review checkpoints automatically; incidents, failures, interruptions, or capability problems must not be auto-approved.
