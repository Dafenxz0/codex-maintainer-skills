#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Commit:
    sha: str
    subject: str
    author: str


def collect_commits(git_range: str) -> list[Commit]:
    output = subprocess.check_output(
        ["git", "log", "--pretty=format:%h%x09%an%x09%s", git_range],
        text=True,
        encoding="utf-8",
    )
    commits: list[Commit] = []
    for line in output.splitlines():
        sha, author, subject = line.split("\t", 2)
        commits.append(Commit(sha=sha, author=author, subject=subject))
    return commits


def bucket(subject: str) -> str:
    lowered = subject.lower()
    for prefix, label in (
        ("feat", "features"),
        ("fix", "fixes"),
        ("docs", "docs"),
        ("test", "tests"),
        ("refactor", "internal"),
        ("build", "build"),
        ("ci", "build"),
        ("deps", "dependencies"),
    ):
        if lowered.startswith(prefix + ":") or lowered.startswith(prefix + "("):
            return label
    return "other"


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize commits in a git range.")
    parser.add_argument("range", help="Git range, for example v1.2.0..HEAD")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    commits = collect_commits(args.range)
    if args.json:
        print(json.dumps([asdict(commit) for commit in commits], indent=2))
        return 0

    grouped: dict[str, list[Commit]] = {}
    for commit in commits:
        grouped.setdefault(bucket(commit.subject), []).append(commit)

    for name in sorted(grouped):
        print(f"## {name}")
        for commit in grouped[name]:
            print(f"- {commit.subject} ({commit.sha}, {commit.author})")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
