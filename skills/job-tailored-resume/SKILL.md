---
name: job-tailored-resume
description: "Runs the full application package for a job posting by chaining the job-fit, generate-resume and outreach-blurbs skills. Use whenever the user shares a job description or posting URL and wants everything at once: fit verdict, tailored resume and cover letter, and outreach notes."
---

# Job-tailored application package

This is a thin orchestrator. It holds no logic of its own; each step is a separate skill with its own instructions.
Use the individual skills when the user wants only one outcome.

Switches (anywhere in the user's message, alone or combined; plain words work too):

| Switch | Runs |
|---|---|
| (none) or `all` | `job-fit`, then `generate-resume` (resume + cover letter), then `outreach-blurbs` |
| `fit` | `job-fit` only |
| `r` | `generate-resume`, resume only |
| `cl` | `generate-resume`, cover letter only |
| `out` | `outreach-blurbs` only |

## Steps

1. Invoke the `job-fit` skill. It finds the user's data, checks the posting, and writes `Fit Brief.md` and
   `keywords.json` in the posting folder. Show the verdict. If the recommendation is "skip", say so and ask whether
   to continue before spending effort on documents.
2. Invoke `generate-resume`. It reuses the posting folder, `keywords.json` and `Fit Brief.md`.
3. Invoke `outreach-blurbs`. It reuses the same folder and the same proof point as the resume.
4. Finish with one chat summary: verdict, posting problems, the 2–3 main gaps, and where the files are.

All three skills share one posting folder and never overwrite existing files (they add `v2`, `v3`).
