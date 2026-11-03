# Common rules for every career-agency skill

> Generated copy. The source is `shared/common.md` in the repository; edit that file and run
> `python tools/sync_shared.py`. Do not edit this copy by hand.

The user applies to many roles and wants each application to be consistent, truthful and tailored. The core idea is
to **select and phrase rather than invent**. The user's career inventory holds every fact they have approved: roles,
titles, dates, metrics, projects, skills and certifications. Section 0 of the inventory records decisions about facts
that differ between older resumes; those decisions always win.

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

**If no inventory exists, run first-run setup instead of the task:**
1. Ask for the user's existing resumes (PDF, .docx or pasted text), and any LinkedIn export or performance notes.
2. Draft `career-inventory.md` following `templates/career-inventory.example.md`: same sections, the INVENTORY
   START / END markers, tagged bullet banks, a decisions table.
3. Walk the user through every number, title and date and ask them to confirm each. Where two resumes disagree,
   ask which is right and record the answer as a decision in section 0. Never resolve a conflict yourself.
4. Write `profile.json` from `templates/profile.example.json`.
5. Save both files to the folder the user chooses (suggest `~/.career-agency/`), and remind them to keep that
   folder private. Never write personal data into this plugin's folder.

## Inputs: the job posting

The posting can come in any form:
- pasted text
- a URL (fetch it with WebFetch; if the page is blocked or empty, ask the user to paste the text)
- a PDF, .txt or .docx attachment
- a file in the user's jobs folder

If only a company and title are given, ask for the posting text. Work tailored to a guess isn't tailored.

Check the posting before investing in it:
- **Truncated.** Screenshots and "Read more" captures often stop partway through, with no Qualifications section,
  for example. If so, look for the full posting with WebFetch or WebSearch, using the job number, company and
  title. Use it only if its visible text matches what the user gave you, and say where the rest came from.
- **Stale or closed.** Note the posting date. If it's more than about 6 weeks old, or a quick check shows it closed,
  say so first, in the chat reply and at the top of any written brief. The user may still want the work, but
  should know first.
- **Page clutter.** Captured job pages often include sidebars such as "skills of previous hires", "similar jobs"
  or match widgets. Ignore those; only the job description itself defines requirements.

## Output files and where they go

Each posting gets **one folder**, named `<Company> - <Role>` with the posting's title shortened to something
readable, for example `Acme - Senior PM (Payments)`. Every skill, on every run for that posting, uses the same folder:
- **New posting:** create the folder and save `job-posting.txt` in it (the text as received).
- **Folder already exists** (a re-run, or a different skill run after another): check its contents first and
  reuse it. Never overwrite a file the user may have edited or sent. Save a new version with a suffix instead
  (`... (Acme) v2.docx`, then `v3`), and say in chat which version is newest.

Files the skills write there (`<Name>` comes from `profile.json`):
- `<Name> - <Role> (<Company>).docx` and `.pdf`: the resume (generate-resume)
- `<Name> - Cover Letter (<Company>).docx` and `.pdf` (generate-resume)
- `Fit Brief.md` and `keywords.json` (job-fit)
- `Outreach.md` (outreach-blurbs)
- `job-posting.txt`

Put the folder under the user's `jobs_folder` from `profile.json`. If that isn't set, ask once where applications
should be saved and offer to record the answer in `profile.json`. If the host can't write to the user's computer,
send the files in chat. When running as a test or eval with an explicit output directory, save the files directly
there and don't create the subfolder.

**Reusing earlier work.** If the folder already holds a `Fit Brief.md`, `keywords.json` or a resume for this
posting, read them and keep the story, keywords and numbers consistent with them instead of re-deriving.
`keywords.json` has the shape `{"must_have": [...], "nice_to_have": [...]}`.

## Truthfulness rules

These rules exist because one invented number, discovered in an interview or a background check, costs more than
any keyword match gains.
- Use the title the inventory gives for each role, with dates exactly as listed. Where the inventory says a role's
  content must mention other roles the user played, include that line wherever roles are described, so a reader
  sees the full scope behind one title.
- Metrics must appear in the inventory. You may round down or omit a number. Never round up, combine two numbers,
  or move a metric to a different role.
- Tools and technologies must be ones the inventory names. If the posting wants a technology the inventory doesn't
  list, that is a gap. Name it, and if relevant point out adjacent strengths.
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

If the user edits a generated document and the edit changes a fact or wording they clearly prefer, ask whether to
carry it into the inventory.
