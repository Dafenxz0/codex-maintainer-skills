---
name: triage-oss-issue
description: Triage open-source GitHub issues into maintainer-ready summaries. Use when Codex is asked to inspect a bug report, feature request, support question, reproduction notes, logs, screenshots, or issue thread and produce severity, labels, missing information, duplicate/search hints, reproduction steps, and a concise maintainer response.
---

# Triage OSS Issue

## Workflow

1. Classify the issue as `bug`, `feature`, `docs`, `support`, `security`, `performance`, or `question`.
2. Extract environment details, affected versions, expected behavior, actual behavior, reproduction steps, logs, and linked issues.
3. Identify missing information that blocks maintainer action.
4. Search the local repo for related docs, tests, error strings, APIs, and previous fixes before recommending labels.
5. Read `references/label-taxonomy.md` when label selection is needed.
6. Produce a maintainer note with: summary, likely component, severity, confidence, labels, next action, and a response draft.

## Output

Use this shape unless the user asks otherwise:

```text
Summary:

Classification:

Severity:

Suggested labels:

Evidence:

Missing information:

Recommended next action:

Maintainer response draft:
```

## Triage Rules

- Treat security-looking reports conservatively and recommend private disclosure when exploit details, credentials, tokens, or vulnerable versions appear.
- Do not promise fixes or timelines.
- Prefer asking for one precise missing artifact over a broad "please provide more info".
- If reproduction is weak, propose the smallest reproduction request that would unblock debugging.
- If the issue is likely a duplicate, give search terms and candidate files rather than asserting a duplicate without evidence.
