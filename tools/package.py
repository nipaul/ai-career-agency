#!/usr/bin/env python3
"""Build upload-ready zip files for claude.ai and the Claude desktop app.

Usage:
    python tools/package.py            # writes dist/*.zip
    python tools/package.py --list     # also prints every entry

Outputs
    dist/career-agency-plugin.zip
        The whole plugin. Upload with  Customize > Plugins > Add > Upload plugin.
        Contains one .claude-plugin/plugin.json at the top level.
    dist/job-tailored-resume-skill.zip
        Just the skill, for  Customize > Skills > Upload skill  (claude.ai needs code execution turned on).
        The skill folder itself is the top level of the archive: job-tailored-resume/SKILL.md.

Works on Windows, macOS and Linux (standard library only). Never packages personal data: only files under the
paths below are included, and anything matching EXCLUDE is skipped.
"""
import fnmatch
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
SKILL = ROOT / "skills" / "job-tailored-resume"

PLUGIN_INCLUDE = [".claude-plugin", "skills", "README.md", "LICENSE", "CHANGELOG.md"]
EXCLUDE_NAMES = {"__pycache__", ".DS_Store", "Thumbs.db", ".git", "private", ".career-agency"}
# Mirrors the personal-data and per-application patterns in .gitignore; the *.example.* templates are fine.
EXCLUDE_PATTERNS = ["career-inventory.md", "profile.json", "keywords.json", "spec.json", "job-posting.txt",
                    "Fit Brief.md", "Outreach.md", "*.local.md", ".env", ".env.*", "preview*.png",
                    "*.pyc", "*.docx", "*.pdf"]


def wanted(path: Path) -> bool:
    if any(part in EXCLUDE_NAMES for part in path.parts):
        return False
    return not any(fnmatch.fnmatch(path.name, pat) for pat in EXCLUDE_PATTERNS)


def files_under(base: Path):
    if base.is_file():
        yield base
        return
    for p in sorted(base.rglob("*")):
        if p.is_file() and wanted(p.relative_to(ROOT)):
            yield p


def write_zip(out: Path, entries):
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for src, arcname in entries:
            info = zipfile.ZipInfo.from_file(src, arcname)  # forward slashes, original mtime
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, src.read_bytes())
    return out


def main():
    plugin_entries = []
    for item in PLUGIN_INCLUDE:
        for f in files_under(ROOT / item):
            plugin_entries.append((f, f.relative_to(ROOT).as_posix()))
    skill_entries = [(f, ("job-tailored-resume/" + f.relative_to(SKILL).as_posix()))
                     for f in files_under(SKILL)]

    plugin_zip = write_zip(DIST / "career-agency-plugin.zip", plugin_entries)
    skill_zip = write_zip(DIST / "job-tailored-resume-skill.zip", skill_entries)

    # Self-check: the shapes claude.ai and the desktop app require.
    with zipfile.ZipFile(plugin_zip) as z:
        names = z.namelist()
        assert names.count(".claude-plugin/plugin.json") == 1, "plugin zip needs exactly one .claude-plugin/plugin.json"
        assert any(n.startswith("skills/job-tailored-resume/SKILL.md") for n in names)
    with zipfile.ZipFile(skill_zip) as z:
        names = z.namelist()
        assert "job-tailored-resume/SKILL.md" in names, "skill zip must have <skill-name>/SKILL.md at the top level"
        assert all(n.startswith("job-tailored-resume/") for n in names), "every entry must sit inside the skill folder"
        leaked = [n for n in names if n.endswith(("career-inventory.md", "profile.json"))]
        assert not leaked, f"personal data files in package: {leaked}"

    for z in (plugin_zip, skill_zip):
        print(f"wrote {z.relative_to(ROOT)}  ({z.stat().st_size / 1024:.0f} KB)")
        if "--list" in sys.argv:
            with zipfile.ZipFile(z) as zf:
                for n in zf.namelist():
                    print("   ", n)


if __name__ == "__main__":
    main()
