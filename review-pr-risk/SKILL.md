---
name: review-pr-risk
description: Review pull requests like an open-source maintainer. Use when Codex is asked to inspect PR diffs, branches, patches, or proposed changes and report behavioral regressions, API compatibility risks, security concerns, missing tests, release impact, documentation gaps, and merge readiness.
---

# Review PR Risk

## Workflow

1. Inspect the changed files and infer the public surface affected by the PR.
2. Read nearby tests, docs, changelog, package metadata, and call sites before judging risk.
3. Read `references/risk-rubric.md` when assigning severity or merge readiness.
4. Prioritize concrete bugs over style preferences.
5. Verify whether tests cover the changed behavior; run focused tests when feasible.
6. Produce findings first, then open questions, then a merge recommendation.

## Review Posture

- Prefer specific file and line references when available.
- Avoid blocking on cosmetic issues unless they obscure correctness or maintainability.
- Call out compatibility risk for public APIs, config formats, CLIs, serialized data, database migrations, and dependency constraints.
- Treat security, auth, permissions, secret handling, path traversal, injection, and unsafe deserialization as high-scrutiny areas.
- If the PR is low risk, say so clearly and identify the remaining verification gap.

## Output

Use this shape unless the user asks for inline comments:

```text
Findings:

Open questions:

Test coverage:

Release impact:

Merge recommendation:
```
