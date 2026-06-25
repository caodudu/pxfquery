# PxFquery Algorithm Package Downgrade Rules

Generated: 2026-06-25

## Purpose

These rules prevent future PxFquery package milestones from silently shrinking into deterministic lookup only. They apply when reviewing or configuring milestones that claim package delivery, resolver behavior, LLM-assisted behavior, proxy routing, natural-language or semi-structured query entry, or user-facing transfer/fallback behavior.

## Hard Distinction: Runtime Fallback Is Not Scope Downgrade Approval

A runtime fallback is an implemented behavior used after a primary path fails or is unavailable. It is acceptable only when the output clearly records the trigger, the fallback path, the evidence status, and the limits of the result.

A scope downgrade is a milestone-level change that removes, optionalizes, defers, or replaces a required capability. A fallback path does not authorize a scope downgrade. For example:

- A deterministic parser fallback after an LLM timeout may be valid runtime behavior.
- The same deterministic parser cannot be counted as delivery of required LLM-assisted parsing unless the milestone explicitly accepts fallback-only behavior.
- A direct structured API query may be valid for low-level tests.
- The same direct API query cannot replace a required resolver-mediated user entry layer without explicit user approval.

## Actions That Require Explicit User Approval

The following actions are downgrades when the capability is part of the milestone scope:

1. Removing forward or reverse query behavior from an algorithm-package milestone.
2. Treating biological context as an ignored label rather than a retrieval constraint or proxy basis.
3. Replacing exact/proxy/not-found evidence routing with unlabeled score lookup.
4. Marking resolver-mediated natural-language or semi-structured entry as optional after the milestone required it.
5. Replacing required proxy routing with exact-only deterministic lookup.
6. Counting LLM endpoint connectivity as full LLM-assisted parsing or summarization.
7. Removing LLM-assisted parsing/summarization because manuscript claims should be conservative.
8. Accepting fallback-only behavior as primary delivery.
9. Deferring transparent evidence metadata.
10. Using legacy reports or planned behavior as current delivery evidence without a current run, artifact, or registered accepted source.

Approved downgrades must be labeled `deferred-user-approved` or otherwise recorded with the approving user decision, date, reason, and expected follow-up. Unapproved downgrades must be labeled `downgraded` or `deferred-not-approved`.

## Capability-Specific Stop Rules

- Forward query absent: package milestone is blocked or failed unless the milestone is explicitly not an algorithm package milestone.
- Reverse query absent: package milestone is partial at best and usually blocked for package delivery.
- Not-found route unsafe: user-facing delivery is failed, because false positives are worse than a transparent no-hit result.
- Proxy route absent when required: milestone is blocked or downgraded; exact-only success does not satisfy proxy delivery.
- Resolver cannot start or dispatch when required: milestone is blocked; direct function calls may support lower-level evidence but not resolver delivery.
- LLM required but only connectivity is shown: milestone is partial or evidence-insufficient, not delivered.
- Metadata absent: evidence-aware retrieval claims are not accepted.
- Standard resources incompatible or unavailable: current package delivery is blocked until a registered resource basis is available.

## Manuscript Claim Restraint

The project should avoid overstating PxFquery as a broad AI-agent platform or claiming stable natural-language performance without evidence. This restraint affects manuscript wording and external positioning. It does not reduce software delivery scope when a milestone explicitly includes resolver, LLM-assisted behavior, proxy routing, transfer behavior, or user-facing query entry.

## Required Review Record

Every future package milestone review should state:

- which capabilities were in scope;
- evidence used for each capability;
- classification label for each capability;
- whether any fallback path was exercised;
- whether any required capability was downgraded or deferred;
- whether downgrade or deferral had explicit user approval;
- whether claims are limited to the demonstrated behavior.
