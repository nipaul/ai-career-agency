<!--
CAREER INVENTORY — EXAMPLE (fictional person, fictional employers, fictional numbers)

Copy this file to your private data folder as `career-inventory.md` and replace everything with your
own verified facts. Your real inventory must NEVER be committed to a public repo.

Why this file exists: it is the single source of truth. A tailored resume may select, reorder and
rephrase what is written here, but may not add a metric, employer, title, date, team size or
technology that is not here. `check_resume.py` enforces that by looking up every number in the
text between the INVENTORY START / END markers below.

Tips
- Write bullets the way you would defend them in an interview. If you cannot explain a number, do not list it.
- Put the tags in brackets at the start of each bullet. They let the agent scan quickly. Invent your own tags;
  keep the legend in section 2 up to date.
- When you decide how a fact should appear (a title, a figure you refuse to use), record it in section 0.
  Decisions always beat older resumes.
-->

<!-- INVENTORY START -->
## Jordan Avery — Career Inventory (single source of truth)

Everything a tailored resume, cover letter or outreach note says about Jordan must trace back to this
inventory. Bullets can be reworded, reordered, merged or trimmed, but **no new metrics, employers,
titles, dates, team sizes, customers or technologies** may be introduced. If a job posting asks for
something not here, it is a gap: mention it in the fit brief, don't paper over it in the resume.

Sources: resumes 2024–2026, performance reviews, LinkedIn recommendations, personal GitHub. (List yours.)

---

### 0. Decisions

Decisions you have made about facts that differ between older resumes. These override everything else.

| # | Item | Decision |
|---|------|----------|
| D1 | Harbor Health title | Always **"Senior Product Manager"**. Role content must also say Jordan served as **Product Owner** for the Patient Access team. |
| D2 | Brightline start date | **Mar 2016**. Never use the 2015 date from the old consulting version. |
| D3 | Cost-savings figure | **$2M annual savings**. The older "$3M" came from a forecast, never use it. |
| D4 | Years of experience | **Don't state a total-years figure** anywhere; the dates on the resume show it. |
| D5 | Side project name | Describe as "an AI-native scheduling assistant" on resumes; name it only in cover letters or interviews. |

---

### 1. Contact & identity

- Name: **Jordan Avery** · Portland, OR area
- Email jordan.avery@example.com · Mobile 555-0100
- LinkedIn https://www.linkedin.com/in/jordan-avery-example · GitHub https://github.com/jordan-avery-example
- Education: Bachelor of Science (Computer Science)
- Career arc: software engineering → technical product management.

---

### 2. Roles (reverse chronological)

Tags: [AI] [GROW] growth/adoption · [TPM] delivery/program · [LEAD] people leadership · [DATA] analytics ·
[ARCH] architecture/integration · [GTM] go-to-market · [PO] backlog/agile · [ENG] hands-on engineering

Each role lists its **Title** (fixed, or a list of "Approved titles" to pick from), its **Org line**
(exactly as it should print) and a bullet bank.

#### 2.1 Senior Product Manager — Harbor Health Systems
- Title: **"Senior Product Manager"** (D1). Include on every resume.
- Required in the role content: Jordan **also served as Product Owner** for the Patient Access team (one-line `summary`).
- Org line: `Harbor Health Systems | Full-time | Portland, OR, USA | Jun 2021 – Present`
- Context: regional health system, Patient Access team, online scheduling and intake across 40 clinics. Vendors: two staffing partners.

Bullet bank:
- [GROW][AI] Launched an AI-assisted appointment-reminder flow that cut no-shows by **18%** across 40 clinics within two quarters.
- [TPM][ARCH] Owned end-to-end delivery of the scheduling-platform migration, moving **120,000** monthly bookings with zero downtime.
- [PO] Owned and prioritized the product backlog — epics, user stories, acceptance criteria and release scope — for a team of **8** engineers.
- [DATA] Built a funnel dashboard on the data warehouse that exposed a **22%** drop-off at insurance verification and guided the fix.
- [GTM] Ran pilot programs with **5** clinics, then rolled out to the rest with train-the-trainer sessions.

#### 2.2 Technical Product Manager — Brightline Software
- Approved titles: "Technical Product Manager"; "Product Manager, Platform"
- Org line: `Brightline Software | Seattle, WA, USA | Mar 2016 – May 2021` (D2)

Bullet bank:
- [ARCH][ENG] Defined the public API roadmap and shipped v2 of the REST API, adopted by **60** partner integrations.
- [GROW] Lifted self-serve activation from **31%** to **44%** by redesigning onboarding.
- [LEAD] Managed a **4-person** offshore QA team and a **3-person** support-tooling group.

#### 2.3 Early career (2010 – 2016)
- Title: **"Software Engineer"**. Show as one line under an EARLY CAREER heading; drop it first when space is tight.
- Org line: `Cedar & Co | Austin, TX | 2010 – 2016`

Bullet bank:
- [ENG] Built internal reporting tools in C# and SQL used by **200+** staff.

---

### 3. Career-highlight lines (pre-approved summaries)

- Product manager with a technical background, shipping AI-assisted patient-access features in healthcare.
- Led a zero-downtime platform migration of 120,000 monthly bookings and an API program adopted by 60 partners.
- Raised self-serve activation from 31% to 44% and cut appointment no-shows by 18%.

---

### 4. Personal & hands-on projects

Use these to prove hands-on depth. Describe client work generically; never name clients.

- **Scheduling assistant** (personal, 2026) — a small LLM-powered assistant that proposes meeting times from calendar free/busy data. React, TypeScript, Node. (D5: unnamed on resumes.)
- **Open-source CLI** (public) — command-line tool that lints OpenAPI specs for breaking changes.

---

### 5. Skills (pick and order to match the posting)

- **Product:** roadmaps, discovery, experimentation, OKRs, backlog ownership, release planning.
- **Technical:** REST APIs, SQL, TypeScript, Python, CI/CD, cloud basics.
- **AI:** LLM prompting, evaluation basics, AI-assisted development.
- **Industries:** healthcare, developer platforms.

---

### 6. Certifications

- Example Institute — Product Management Certificate (2023)

---

### 7. Third-party proof (for cover letters / outreach — paraphrase, don't overquote)

- Former manager, Harbor Health (name): praised the migration for finishing "on time and without patient impact".
- Peer PM, Brightline (name): "strong product sense with the technical depth to back it up".
<!-- INVENTORY END -->
