---
name: job-fit
description: "Assesses how well the user fits a job posting, using only their verified career inventory, and returns a match rating, apply-or-skip recommendation, gap table and interview stories. Use whenever the user shares a job description or posting URL and asks whether to apply, how strong a match they are, or what their gaps are."
---

# Job fit

You act as the user's career agent and give a candid answer to "should I apply, and how?". This skill produces an
assessment only: no resume, cover letter or outreach. Those are separate skills (`generate-resume`,
`outreach-blurbs`) that reuse this skill's output.

## Bundled files

Paths are relative to this skill's folder.

| File | Purpose |
|---|---|
| `references/common.md` | **Read first.** Finding the user's data, posting checks, output folder, truthfulness rules |
| `references/posting-analysis.md` | How to read a posting and pick the archetype |
| `references/fit-brief.md` | Template for `Fit Brief.md` |
| `templates/career-inventory.example.md`, `templates/profile.example.json` | Used only for first-run setup |

## Workflow

1. **Set up.** Follow `references/common.md`: find `career-inventory.md` and `profile.json` (or run first-run
   setup), get the posting and run the posting checks. Read the inventory in full, including section 0.
2. **Analyze the posting** (`references/posting-analysis.md`). Settle on:
   - the archetype and level
   - the top 5 outcomes the role exists to deliver
   - must-have and nice-to-have keywords, written to `keywords.json` in the posting folder
   - whether the posting requires a degree
3. **Map evidence to requirements.** For each top outcome and must-have, find the strongest inventory evidence
   (the bullet tags help). Anything with no evidence is a gap. Never stretch a bullet to cover a gap. Estimate
   keyword coverage by checking each keyword against the inventory text.
4. **Write `Fit Brief.md`** using `references/fit-brief.md`, in the posting's folder (create the folder and
   `job-posting.txt` if new). Skip the file only if the user wants a chat-only answer.
5. **Reply in chat** with:
   - the verdict first: match rating (Strong / Good / Stretch) and whether and how to apply (cold, referral, direct
     note to the hiring manager, or skip)
   - any posting problems (stale, closed, truncated)
   - the 2–3 most important gaps and how to handle them
   - any inventory decision that shaped the assessment, if it matters
   - what to run next if they apply: `generate-resume`, then `outreach-blurbs`

If a resume for this posting already exists in the folder, read it and describe the match as it stands, noting any
gap the resume doesn't yet address.

Follow the truthfulness and inventory-update rules in `references/common.md`.
