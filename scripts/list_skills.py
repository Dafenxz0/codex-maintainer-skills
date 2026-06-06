#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for skill_file in sorted(root.glob("*/SKILL.md")):
        metadata = _frontmatter(skill_file)
        name = metadata.get("name", skill_file.parent.name)
        description = metadata.get("description", "")
        print(f"{name}: {description}")
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
