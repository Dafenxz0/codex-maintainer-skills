# PR Risk Rubric

## Severity

- `critical` - likely security issue, data loss, irreversible migration, or system-wide breakage
- `high` - likely user-visible regression in a common path
- `medium` - plausible regression in a narrower path or missing important verification
- `low` - maintainability, docs, or minor behavior ambiguity

## Merge Readiness

- `ready` - behavior is clear, tested, and low risk
- `ready with follow-up` - acceptable now, but a non-blocking task should be tracked
- `needs changes` - concrete correctness, security, compatibility, or test gap blocks merge
- `needs maintainer decision` - tradeoff is product/API policy rather than code correctness

## High-Risk Surfaces

- Authentication and authorization
- Secrets, credentials, tokens, and logs
- File paths, archives, uploads, and downloads
- Public APIs, CLI flags, and config formats
- Database migrations and persistent storage
- Dependency upgrades with transitive security or compatibility impact
- Concurrency, caching, retries, and idempotency
