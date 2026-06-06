# Codex Maintainer Skills

A compact skill pack for open-source maintainers using Codex.

The pack focuses on the work that tends to pile up around active repositories:
triaging noisy issues, reviewing pull requests with a maintainer lens, and
preparing release briefs from git history.

## Skills

### `triage-oss-issue`

Turns an issue report into a maintainer-ready triage note with classification,
severity, suggested labels, missing information, and a response draft.

Example prompt:

```text
Use triage-oss-issue to triage this GitHub issue and draft a maintainer reply.
```

### `review-pr-risk`

Reviews a pull request for regressions, public API risk, missing tests, security
concerns, documentation gaps, and merge readiness.

Example prompt:

```text
Use review-pr-risk on this PR diff and tell me if it is safe to merge.
```

### `prepare-release-brief`

Builds release notes, upgrade notes, risk notes, and a maintainer checklist from
a git range or commit list. Includes a small `commit_digest.py` helper for local
git history.

Example prompt:

```text
Use prepare-release-brief for v0.3.0..HEAD and draft release notes.
```

## Install

Copy any skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R triage-oss-issue review-pr-risk prepare-release-brief ~/.codex/skills/
```

On Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse triage-oss-issue,review-pr-risk,prepare-release-brief "$env:USERPROFILE\.codex\skills\"
```

Restart Codex after installing new skills.

## Validate

List the skills included in the pack:

```bash
python scripts/list_skills.py
```

Validate each skill with Codex's skill validator when available:

```bash
python path/to/quick_validate.py triage-oss-issue
python path/to/quick_validate.py review-pr-risk
python path/to/quick_validate.py prepare-release-brief
```

## Design

These skills are intentionally small. They give Codex maintainer-specific
workflow memory without trying to replace human judgment or project policy.

Each skill follows the standard Codex skill structure:

```text
skill-name/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
```

Not every skill needs scripts; most of the value is in clear workflow guidance
and reusable rubrics.

## License

MIT
