# Security policy

## Reporting a vulnerability

Please report security problems privately through GitHub:
**Security tab > Report a vulnerability** on this repository. Don't open a public issue for them.

I aim to acknowledge reports within a few days. This is a small personal project, so fixes are made on a
best-effort basis.

## Scope

This repository contains a Claude plugin: instructions (`SKILL.md`, references) and two local Python scripts
(`build_docx.py`, `check_resume.py`) that run in your own sessions. Relevant reports include:

- a script reading or writing files outside the folders you point it at
- anything that could leak the contents of a user's `career-inventory.md` or `profile.json`
- a packaging change that would put personal data into the upload zips

## Your data

Never put real personal data in issues, pull requests, examples or tests. If you accidentally commit some,
tell me and I'll help remove it from history.
