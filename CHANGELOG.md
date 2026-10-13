# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.1.0] - 2026-10-13

### Added
- `job-tailored-resume` skill: tailored resume (.docx + .pdf), cover letter, fit and gap brief, and outreach notes
  from a job posting.
- Fact guard (`check_resume.py`): every metric in a document must trace to the user's career inventory.
- Keyword coverage check against the posting's must-have and nice-to-have terms.
- First-run setup that builds a career inventory from the user's existing resumes.
- Annotated example inventory, profile and resume spec using fictional data.
- Setup guide for Claude Code, the Claude desktop app (Chat and Cowork) and claude.ai, including where the career
  inventory lives on each surface, a first-run check and troubleshooting.
- `tools/package.py`: builds `career-agency-plugin.zip` and `job-tailored-resume-skill.zip` for upload. Its
  exclusions mirror the personal-data patterns in `.gitignore`.
- Unit tests for the fact guard, keyword coverage and an end-to-end build (`python -m unittest discover -s tests`).
- Security tooling: Dependabot (pip, GitHub Actions), CI, CodeQL, `SECURITY.md`, `CODEOWNERS`, and a pinned
  `requirements.txt`. Workflow actions are pinned to commit SHAs.

### Changed
- Fact guard matches numbers as whole tokens, so "8%" is no longer accepted because the inventory says "18%".
  Emails, URLs and phone numbers in the contact line are no longer treated as metrics.
- `build_docx.py` parses its arguments with `argparse` and reports a missing LibreOffice or a malformed contact
  entry with a clear message.
- Skill script paths use `${CLAUDE_SKILL_DIR}` so they resolve in Claude Code and Cowork, and fall back to relative
  paths in claude.ai chat.
- Skill falls back to a .docx-only delivery when LibreOffice is unavailable in the sandbox.
