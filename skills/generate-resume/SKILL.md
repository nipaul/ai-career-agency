---
name: generate-resume
description: "Builds a tailored resume (.docx + .pdf) and optional cover letter from a job posting, using only the user's verified career inventory, with a fact guard that flags any unverified number. Use whenever the user shares a job description or posting URL and wants a resume or cover letter for it."
---

# Generate resume

You act as the user's career agent and build a resume (and, on request, a cover letter) that reads as if it was
written for this posting, while staying strictly truthful and consistent across versions. Recruiters compare
versions and interviewers probe every number.

Fit assessment and outreach messages are separate skills (`job-fit`, `outreach-blurbs`).

## Bundled files

Paths are relative to this skill's folder. Use the skill's base directory when running scripts.

| File | Purpose |
|---|---|
| `references/common.md` | **Read first.** Finding the user's data, posting checks, output folder, truthfulness rules |
| `references/posting-analysis.md` | Reading the posting, archetypes and section order |
| `references/playbook.md` | Length, bullet craft, profile formula, titles, ATS rules, pre-ship checks |
| `references/cover-letter.md` | Cover letter template |
| `scripts/build_docx.py` | Builds the .docx (and .pdf) from a JSON spec |
| `scripts/check_resume.py` | Fact guard (every metric must trace to the inventory) and keyword coverage |
| `templates/resume-spec.example.json` | Example spec for `build_docx.py` |
| `templates/career-inventory.example.md`, `templates/profile.example.json` | Blank annotated inventory and profile |

## Output switches

| Switch | Produces |
|---|---|
| (none) or `r` | Resume (.docx + .pdf) |
| `cl` | Cover letter (.docx + .pdf) |
| `r cl` or `all` | Both |

With `cl` alone, if a resume for this posting already exists in its folder, read it and keep the story and numbers
consistent with it.

## Workflow

1. **Set up.** Follow `references/common.md` (find the data or run first-run setup, get the posting, run the
   posting checks, reuse the posting folder). Read the inventory in full, including section 0 (decisions), then
   `references/posting-analysis.md` and `references/playbook.md`. The scripts need `python-docx`, LibreOffice
   (`soffice`) and poppler (`pdfinfo`, `pdftoppm`); install anything missing. If LibreOffice can't be installed
   (some sandboxes), build the .docx only, deliver it, and say plainly that the PDF step was unavailable.
2. **Analyze the posting**, or reuse `keywords.json` and `Fit Brief.md` if `job-fit` already ran for this posting.
   Settle on:
   - the archetype, level and page budget
   - the top 5 outcomes the role exists to deliver
   - must-have and nice-to-have keywords, written to `keywords.json` (skip if it already exists)
   - the title to use for each role (fixed by the inventory), plus any required role-summary line
   - whether the posting requires a degree. If it does, include EDUCATION.
3. **Map evidence to requirements.** For each top outcome and must-have, find the strongest inventory bullets,
   using the tags to scan quickly. Anything with no evidence is a gap: don't stretch a bullet to cover it, and
   mention it to the user in the final reply.
4. **Write the resume spec** as JSON for `build_docx.py` (the format is documented at the top of the script, and
   `templates/resume-spec.example.json` shows a complete one). Follow the archetype's section order and the bullet
   craft rules. Mark key phrases and numbers with `**bold**`.
5. **Build, check and look at it:**
   ```bash
   python3 ${CLAUDE_SKILL_DIR}/scripts/build_docx.py spec.json "<out>.docx" --pdf --profile "<data folder>/profile.json"
   python3 ${CLAUDE_SKILL_DIR}/scripts/check_resume.py "<out>.docx" --inventory "<data folder>/career-inventory.md" --keywords keywords.json
   pdftoppm -png -r 60 "<out>.pdf" preview   # then view page 1
   ```
   `${CLAUDE_SKILL_DIR}` is this skill's folder in Claude Code and Cowork. In chat on claude.ai the skill is copied
   into the sandbox, so use the path relative to this file, `scripts/build_docx.py`.
   Then fix three kinds of problems:
   - **UNVERIFIED metrics:** every number must trace to the inventory. Remove the number or correct it.
   - **Must-have coverage under about 80%:** reword a bullet only where it stays true.
   - **Pages over budget:** use the trimming order in the playbook, section 3.

   Look at page 1 before you hand anything over. Layout problems (an orphaned role header, a lonely last line) only
   show up visually.
6. **Cover letter** (if requested): follow `references/cover-letter.md`, built with the same script, and run the
   fact guard on it too.
7. **Deliver** the files (see `references/common.md` for folder and naming), then reply in chat with:
   - where the files are and which version is newest
   - the must-have keyword coverage and any real gaps the resume doesn't cover
   - any posting problems (stale, closed, truncated)
   - any inventory decision that shaped the resume, if it matters
   - what to run next if useful: `outreach-blurbs` (and `job-fit` if no brief exists)

Follow the truthfulness and inventory-update rules in `references/common.md`.
