#!/usr/bin/env python3
"""Copy the files in shared/ into each skill that needs them.

Skills must be self-contained (the skill-only zips contain one skill folder), so shared text is copied, not linked.
shared/ is the source of truth.

Usage:
    python tools/sync_shared.py          # write the copies
    python tools/sync_shared.py --check  # exit 1 if any copy is missing or differs (used by tests and CI)
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"

# source (under shared/) -> (destination under each skill, skills that carry it)
SYNC = {
    "common.md": ("references/common.md", ["job-fit", "outreach-blurbs", "generate-resume"]),
    "posting-analysis.md": ("references/posting-analysis.md", ["job-fit", "outreach-blurbs", "generate-resume"]),
    "templates/career-inventory.example.md": ("templates/career-inventory.example.md",
                                               ["job-fit", "outreach-blurbs", "generate-resume"]),
    "templates/profile.example.json": ("templates/profile.example.json",
                                        ["job-fit", "outreach-blurbs", "generate-resume"]),
}


def targets():
    for src, (dest, skills) in SYNC.items():
        for skill in skills:
            yield SHARED / src, SKILLS / skill / dest


def main(check: bool) -> int:
    bad = []
    for src, dst in targets():
        want = src.read_bytes()
        if dst.exists() and dst.read_bytes() == want:
            continue
        bad.append(dst)
        if not check:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(want)
    for dst in bad:
        print(("out of date: " if check else "wrote: ") + dst.relative_to(ROOT).as_posix())
    if check and bad:
        print("run: python tools/sync_shared.py")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
