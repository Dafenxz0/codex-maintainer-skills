#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="List skills included in this pack.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    skills = []
    for skill_file in sorted(root.glob("*/SKILL.md")):
        metadata = _frontmatter(skill_file)
        skills.append(
            {
                "name": metadata.get("name", skill_file.parent.name),
                "description": metadata.get("description", ""),
                "path": str(skill_file.parent.relative_to(root)),
            }
        )

    if args.json:
        print(json.dumps(skills, indent=2))
    else:
        for skill in skills:
            print(f"{skill['name']}: {skill['description']}")
    return 0


def _frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return {}

    values: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            break
        key, separator, value = line.partition(":")
        if separator:
            values[key.strip()] = value.strip()
    return values


if __name__ == "__main__":
    raise SystemExit(main())
