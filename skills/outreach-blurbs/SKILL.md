---
name: outreach-blurbs
description: "Writes short, truthful outreach messages for a job posting (LinkedIn connection note, email or InMail to a recruiter or hiring manager, referral ask, and follow-up), using only the user's verified career inventory. Use whenever the user wants to message a recruiter, hiring manager or contact about a role, ask for a referral, or follow up on an application."
---

# Outreach blurbs

You act as the user's career agent and write the short messages that get a reply. This skill produces
`Outreach.md` only; it doesn't build a resume or assess fit (see `generate-resume` and `job-fit`).

## Bundled files

Paths are relative to this skill's folder.

| File | Purpose |
|---|---|
| `references/common.md` | **Read first.** Finding the user's data, posting checks, output folder, truthfulness rules |
| `references/posting-analysis.md` | How to read a posting (used only when no brief exists yet) |
| `references/outreach-templates.md` | Message types, length limits, tone, `Outreach.md` layout |
| `templates/career-inventory.example.md`, `templates/profile.example.json` | Used only for first-run setup |

## Workflow

1. **Set up.** Follow `references/common.md`: find the data (or run first-run setup), get the posting, run the
   posting checks, and reuse the posting folder. If the posting is closed, use the closed-posting wording in
   `references/outreach-templates.md`.
2. **Reuse earlier work.** If the folder has a `Fit Brief.md`, `keywords.json` or a resume, read them and pick the
   same best proof point they use. Otherwise do a light analysis (`references/posting-analysis.md`, top 3 outcomes
   only) and pick the strongest inventory evidence for the #1 outcome.
3. **Ask who it's for** only if unclear: recruiter, hiring manager, an existing contact for a referral, or a
   follow-up after applying. If the user names a person, use their name and role; never invent a name or a
   shared connection.
4. **Write the messages** from `references/outreach-templates.md`. By default give the LinkedIn note and the
   email/InMail for the audience asked about; give the other types when the user asks for "all" or a full set.
5. **Check the facts.** Every number and claim must come from the inventory. Keep the proof point identical to the
   one used in any existing resume.
6. **Save** `Outreach.md` in the posting folder (version suffix if one exists), and reply in chat with the
   messages themselves so the user can copy them straight away.

Follow the truthfulness and inventory-update rules in `references/common.md`.
