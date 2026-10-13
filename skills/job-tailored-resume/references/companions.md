# Companion documents

All three use the same facts as the resume, and nothing new. Write them after the resume is final so the story
is consistent.

## 1. Fit & gap brief (`Fit Brief.md`, also summarized in chat)

Purpose: the candidate reads this before applying and before the interview. Be candid; it is for them, not the
employer.

```
# <Company> — <Role>: fit brief
**Match:** <Strong / Good / Stretch>, with one sentence why. **Recommendation:** apply cold / apply with referral / direct note to the hiring manager / skip.
**Posting status:** date posted, and whether it's still open or truncated (if you checked).
**Archetype & length used:** <e.g. Technical PM, 2 pages>   **Role framing:** <which roles led, and how any required role-summary lines were worded>

## What they're really hiring for
3–5 bullets in plain language.

## Where the candidate is strong (evidence → requirement)
| Requirement | Best evidence | Where it appears in the resume |

## Gaps and how to handle them
| Gap | Severity (blocker / moderate / minor) | Honest framing or adjacent evidence | Prep before interview |

## Keyword coverage
Must-have X% · Nice-to-have Y% · Missing: ... (each marked "gap" or "deliberately omitted")

## Inventory decisions that mattered
Any section 0 decision that shaped this application (for example a title or figure a recruiter may ask about),
and how to explain it.

## Interview prep: 3 stories to have ready
STAR outlines drawn from the inventory, mapped to the posting's top outcomes.
```

## 2. Cover letter (`.docx` + `.pdf`, built with the same script)

- Under one page; 3–4 short paragraphs, about 250–350 words. Use `"contact": true` in the header, then a date line,
  "Dear Hiring Manager," (or a name if known), body paragraphs, and "Sincerely," followed by the candidate's name
  (from `profile.json`).
- P1: the role, the company, and one specific reason this team (from the posting or company context).
- P2: the strongest proof for the role's #1 outcome, with a number.
- P3: second proof for the #2 outcome, plus hands-on evidence if relevant.
- P4: short close: what they would do in the first months, and an invitation to talk.
- Spec: a single section `{"title": null, "type": "paragraphs", "items": [...]}`. Bold nothing, or at most one phrase.

## 3. Recruiter / hiring-manager outreach (`Outreach.md`)

Two variants, both under 120 words:
- **LinkedIn connection note** (≤300 characters): role name + one proof point + ask.
- **Email / InMail**: subject line, 3 short sentences (why them, best proof, ask for 15 minutes), sign-off with the
  candidate's LinkedIn.

Plain, warm, specific. No "I hope this finds you well".
