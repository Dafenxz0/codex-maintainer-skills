# Label Taxonomy

Use these labels as suggestions, not as hard requirements.

## Type

- `type: bug` - confirmed or plausible defect
- `type: feature` - new capability or enhancement
- `type: docs` - documentation, examples, guides
- `type: support` - usage help or environment-specific setup
- `type: question` - unclear request or conceptual question
- `type: security` - vulnerability or sensitive disclosure path

## Status

- `needs reproduction` - missing minimal reproduction
- `needs info` - missing version, environment, logs, or expected behavior
- `needs maintainer review` - enough detail for a maintainer decision
- `blocked` - waiting on upstream, dependency, or external system

## Severity

- `severity: critical` - data loss, security exposure, service-wide outage
- `severity: high` - common workflow broken, no practical workaround
- `severity: medium` - broken edge case or workaround exists
- `severity: low` - polish, docs, papercut, rare scenario

## Component

Prefer existing repository labels. If none exist, suggest component labels such as
`component: cli`, `component: api`, `component: docs`, `component: tests`,
`component: build`, or `component: dependencies`.
