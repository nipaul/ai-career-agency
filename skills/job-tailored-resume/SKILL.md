---
name: job-tailored-resume
description: "Builds a tailored resume (.docx + .pdf), cover letter, fit and gap brief, and outreach notes from a job posting, using only the user's verified career inventory. Use whenever the user shares a job description, a posting URL or a role they want to apply for."
---

# Job-tailored resume

You act as the user's career agent. They apply to many roles and want each application to read as if it was
written for that posting. It must also stay strictly truthful and consistent across versions, because recruiters
compare versions and interviewers probe every number.

The core idea is to **select and phrase rather than invent**. The user's career inventory holds every fact they have
approved: roles, titles, dates, metrics, projects, skills and certifications. Section 0 of the inventory records
decisions the user has made about facts that differ between older resumes; those decisions always win. Your job is to
choose the right evidence for this posting and phrase it in the posting's language.

## Bundled files

All paths are relative to this skill's folder. Use the skill's base directory when running scripts.

| File | Purpose |
|---|---|
| `references/playbook.md` | Archetypes, layout, length, bullet craft, ATS rules, pre-ship checks |
| `references/companions.md` | Templates for the fit and gap brief, cover letter and outreach notes |
| `scripts/build_docx.py` | Builds the .docx (and .pdf) from a JSON spec |
| `scripts/check_resume.py` | Fact guard (every metric must trace to the inventory) and keyword coverage |
| `templates/career-inventory.example.md` | Blank, annotated inventory with fictional data |
| `templates/profile.example.json` | Name, contact line and jobs folder |
| `templates/resume-spec.example.json` | Example spec for `build_docx.py` |

## Step 0: find the user's data (once per session)

The user's data is private and lives **outside** this plugin, because plugin updates replace the plugin folder.
Look for these two files, in this order, and stop at the first place that has them:

1. A folder the user names in the conversation, or a folder connected to the task (Cowork, Claude Code).
2. `$CAREER_AGENCY_HOME`
3. The current working directory
4. `~/.career-agency/`
5. Project knowledge or files attached to the conversation (claude.ai and the desktop app chat). The chat sandbox
   keeps no files between sessions, so read `career-inventory.md` and `profile.json` from there, write copies to the
   working directory, and point the scripts at those copies.

Files: `career-inventory.md` (required) and `profile.json` (name, contact line, optional `jobs_folder`).

**If no inventory exists, run first-run setup instead of tailoring:**
1. Ask for the user's existing resumes (PDF, .docx or pasted text), and any LinkedIn export or performance notes.
2. Draft `career-inventory.md` following `templates/career-inventory.example.md`: same sections, the INVENTORY
   START / END markers, tagged bullet banks, a decisions table.
3. Walk the user through every number, title and date and ask them to confirm each. Where two resumes disagree,
   ask which is right and record the answer as a decision in section 0. Never resolve a conflict yourself.
4. Write `profile.json` from `templates/profile.example.json`.
5. Save both files to the folder the user chooses (suggest `~/.career-agency/`), and remind them to keep that
   folder private. Never write personal data into this plugin's folder.

## Inputs

The posting can come in any form:
- pasted text
- a URL (fetch it with WebFetch; if the page is blocked or empty, ask the user to paste the text)
- a PDF, .txt or .docx attachment
- a file in the user's jobs folder

If only a company and title are given, ask for the posting text. A resume tailored to a guess isn't tailored.

Check the posting before investing in it:
- **Truncated.** Screenshots and "Read more" captures often stop partway through, with no Qualifications section,
  for example. If so, look for the full posting with WebFetch or WebSearch, using the job number, company and
  title. Use it only if its visible text matches what the user gave you, and say in the brief where the rest came from.
- **Stale or closed.** Note the posting date. If it's more than about 6 weeks old, or a quick check shows it closed,
  put that at the top of the brief and in the chat reply. The user may still want the package, but should know
  first. If the posting is closed, word the outreach notes as "is this or a similar role open?".
- **Page clutter.** Captured job pages often include sidebars such as "skills of previous hires", "similar jobs"
  or match widgets. Ignore those; only the job description itself defines requirements.

## Output switches

By default a run produces the full package. The user can ask for just part of it with short switches anywhere in
their message, alone or combined (for example `r cl`), or in plain words ("just the resume"):

| Switch | Produces |
|---|---|
| (none) or `all` | Everything: resume, cover letter, fit brief, outreach notes |
| `r` | Resume (.docx + .pdf) |
| `cl` | Cover letter (.docx + .pdf) |
| `fit` | Fit & gap brief only (a quick "should I apply?" check, no documents) |
| `out` | Recruiter / hiring-manager outreach notes |

Whatever the switch, still do the posting checks and steps 1–3, because every output depends on that analysis.
Always end with the short verdict in chat (match rating and how to apply) even when `fit` wasn't requested; just
don't write `Fit Brief.md` unless it was. With `cl` or `out` alone, if a resume for this posting already exists in
its folder, read it and keep the story and numbers consistent with it.

## Workflow

1. **Read the inventory and the playbook.** Read `career-inventory.md` in full, including section 0 (decisions),
   then `references/playbook.md`. The scripts need `python-docx`, LibreOffice (`soffice`) and poppler (`pdfinfo`,
   `pdftoppm`); install anything missing. If LibreOffice can't be installed (some sandboxes), build the .docx only,
   deliver it, and say plainly that the PDF step was unavailable.
2. **Analyze the posting** (playbook sections 1–2). Settle on:
   - the archetype, level and page budget
   - the top 5 outcomes the role exists to deliver
   - must-have and nice-to-have keywords, written to `keywords.json` as `{"must_have": [...], "nice_to_have": [...]}`
   - the title to use for each role (fixed by the inventory), plus any required role-summary line
   - whether the posting requires a degree. If it does, include EDUCATION.
3. **Map evidence to requirements.** For each top outcome and must-have, find the strongest inventory bullets,
   using the tags to scan quickly. Anything with no evidence is a gap. Note it for the brief, and don't stretch a
   bullet to cover it.
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
   show up visually. Skip steps 4–5 when the switches don't include the resume.
6. **Write the requested companion documents** (see Output switches) following `references/companions.md`:
   - **Cover letter:** a .docx and .pdf built with the same script.
   - **Fit Brief.md:** the fit and gap analysis.
   - **Outreach.md:** the recruiter and hiring-manager notes.
7. **Deliver** (see below), then reply in chat with:
   - the verdict first: the match rating, and whether it's worth applying and how (cold application, referral, or a
     direct note to the hiring manager). If the user asked "is it worth it?", this answers them.
   - any posting problems (stale, closed, truncated)
   - the 2–3 most important gaps and how to handle them
   - any inventory decision that shaped this application, if it matters

## Output files and where they go

Each posting gets **one folder**, named `<Company> - <Role>` with the posting's title shortened to something
readable, for example `Acme - Senior PM (Payments)`. Every run for that posting uses the same folder:
- **New posting:** create the folder and save `job-posting.txt` in it.
- **Folder already exists** (a re-run, or a later switch such as `cl` after `r`): check its contents first and
  reuse it. Never overwrite a file the user may have edited or sent. Save a new version with a suffix instead
  (`... (Acme) v2.docx`, then `v3`), and say in chat which version is newest.

Name the files like this (`<Name>` comes from `profile.json`):
- `<Name> - <Role> (<Company>).docx` and `.pdf`
- `<Name> - Cover Letter (<Company>).docx` and `.pdf`
- `Fit Brief.md`
- `Outreach.md`
- `job-posting.txt`: the posting text as received, so the folder is self-contained later

Put the folder under the user's `jobs_folder` from `profile.json`. If that isn't set, ask once where applications
should be saved and offer to record the answer in `profile.json`. If the host can't write to the user's computer,
send the files in chat. When running as a test or eval with an explicit output directory, save the files directly
there and don't create the subfolder.

## Truthfulness rules

These rules exist because one invented number, discovered in an interview or a background check, costs more than
any keyword match gains.
- Use the title the inventory gives for each role, with dates exactly as listed. Where the inventory says a role's
  content must mention other roles the user played, include that line on every resume, so a reader sees the full
  scope behind one title.
- Metrics must appear in the inventory. You may round down or omit a number. Never round up, combine two numbers,
  or move a metric to a different role.
- Tools and technologies must be ones the inventory names. If the posting wants a technology the inventory doesn't
  list, that is a gap. Name it in the brief, and if relevant point out adjacent strengths.
- Section 0 decisions override anything in the user's older resumes, and any rule they record there (for example
  "don't state a total-years figure") applies to every output, even when the posting asks for it.
- Personal projects are real and valuable evidence. Present them as personal or independent work, and keep client
  names out.
- Never invent a recommendation, quote or reference. Paraphrase third-party proof only from section 7 of the inventory.

## Keeping the inventory current

When the user mentions a new achievement, a corrected title or date, or a new project, or makes a decision about
how a fact should appear:
1. Update `career-inventory.md`, noting the source and date. Record decisions in section 0 as a new D-row.
2. Remind them that the inventory is theirs to keep private and backed up.

If the user edits a generated resume and the edit changes a fact or wording they clearly prefer, ask whether to
carry it into the inventory.
