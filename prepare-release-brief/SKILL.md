---
name: prepare-release-brief
description: Prepare maintainer release briefs from git history, diffs, changelogs, package metadata, or pull request lists. Use when Codex is asked to draft release notes, summarize changes since a tag, identify release risk, build a maintainer checklist, check version bumps, or create upgrade notes for an open-source project.
---

# Prepare Release Brief

## Workflow

1. Determine the release range: explicit git range, previous tag to `HEAD`, or user-provided PR/commit list.
2. Run `scripts/commit_digest.py <range>` when a local git repo and range are available.
3. Inspect package metadata, changelog, docs, tests, migrations, and public API changes touched in the range.
4. Read `references/release-brief-template.md` for the recommended output structure.
5. Separate user-facing changes from maintainer-only work.
6. Call out release blockers, risky changes, missing tests, migration needs, and follow-up issues.

## Versioning Guidance

- Recommend patch for bug fixes and internal hardening.
- Recommend minor for new features, new public APIs, and compatible behavior additions.
- Recommend major for breaking API changes, removed behavior, migration requirements, or incompatible config changes.
- Mark the recommendation as uncertain when the public contract is not clear from the repository.

## Output Rules

- Keep release notes crisp and user-facing.
- Do not list every commit unless the user asks for a raw changelog.
- Mention uncertainty and verification gaps explicitly.
- Include commands run and ranges inspected when the user needs auditability.
