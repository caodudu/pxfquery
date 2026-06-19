# Algorithm function review — Protocol

This development goal is for evidence-first algorithm function review.

Tasks under this goal should answer whether the existing PxFquery algorithm actually works in the current project environment, which planned functions are already present, which functions fail, and which expected capabilities are missing.

The goal should not repair or redesign algorithm code directly. It should create controlled tests, collect fresh run evidence, and convert confirmed gaps into later development tasks under `goal_algorithm_version_development`.

Expected review areas include:

- package import and environment readiness;
- data and index availability;
- structured forward query from perturbation to function;
- structured reverse query from function target to perturbation;
- resolver behavior for exact hit, proxy hit, and not-found cases;
- natural-language parsing and LLM-dependent behavior, when credentials are available;
- result object schema, evidence labels, ranking stability, and runtime cost;
- missing assets or missing code paths that block the MVP.
