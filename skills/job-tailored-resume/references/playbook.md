# Resume playbook — how to tailor

Read this after the career inventory, before choosing evidence. It covers reading the posting, picking a
layout, bullet craft, length, and the pre-ship checks.

## 1. Read the posting like a hiring manager

Pull out, in your own notes (not the resume):
- **Role archetype** (table below) and **level** (Associate / Senior / Staff / Principal / Lead / Director).
- **Top 5 outcomes** the role exists to deliver (for example "own release-to-adoption for the billing platform").
- **Must-have** qualifications vs **nice-to-have**: years, domain, platform, people management.
- **Exact vocabulary** the posting uses. It will be screened by ATS and by a recruiter skimming for the same
  words. Prefer the posting's wording when it describes something the candidate truly did: if it says
  "go-to-market", don't write "GTM motion"; if it says "LLM evaluation", use "evals" only alongside it.
- **Company context**: product, customers, stack, stage. If the posting is a URL, fetch it. If company context
  would sharpen the summary and a quick search is available, one lookup is fine.

## 2. Archetypes → base layout

| Archetype | Typical signals | Section order | Lead with |
|---|---|---|---|
| AI Product Manager | "AI/ML products", "LLM", "agents", "evals" | Profile → Career Highlights → Experience → Hands-on AI Projects → Skills → Certs | AI launches and pilots, evaluation work, hands-on builds |
| Technical PM / TPM | "technical", "APIs", "platform", "dependencies", "SDLC" | Profile → Career Highlights → Experience → Projects (optional) → Skills → Certs | Delivery at scale, observability, cross-team dependencies, CI/CD |
| Product Manager (core / growth) | "customer insights", "roadmap", "metrics", "growth" | Profile → Career Highlights → Experience → Skills → Certs | Growth metrics, adoption, revenue, engagement |
| Product Owner / Agile | "backlog", "user stories", "Scrum", "UAT" | Profile → Selected PO Highlights (5 labeled bullets) → Experience → Skills → Certs | Backlog ownership, release scope, team size |
| Outbound / GTM PM, Product Lead | "enablement", "positioning", "field", "customer programs" | Profile → Career Highlights → Experience → Skills → Certs | Customer programs, launches, case studies, partners, training |
| Solutions Architect | "architecture", "pre-sales", "integration" | Tagline under name → Career Highlights → Core Skills → Experience → Certs | Architecture and modernization, reference architectures |
| Engineering leader | "engineering manager", "director of engineering" | Profile → Core Competencies → Experience → Technical Skills → Education | Team sizes, hybrid orgs, platform scale, reliability |

Hybrid postings are common (for example "Technical Product Manager – AI"): pick the archetype that matches the
**title**, then pull the second archetype's strongest evidence into Career Highlights.

## 3. Length

Default rule (override it if the inventory's section 0 states a different preference):
- Associate / mid-level / senior PM, TPM, PO: **2 pages max**.
- Staff, Principal, Lead, Director, Architect: **up to 3 pages**.
- Either way, page 1 must stand alone: name, contact, profile, highlights and the most recent role.

Ways to fit, in this order:
1. Drop the weakest bullet per role.
2. Condense older roles to 2–3 bullets.
3. Drop the early-career entry unless it adds depth the posting wants.
4. Trim Skills to what the posting cares about.
5. Fold Education into one "EDUCATION & CERTIFICATIONS" section.
6. Merge bullets.

Never shrink fonts or margins below the template, and never drop a required role-summary line (section 6).
One page of this template holds about 550–600 words: plan roughly 1,100 words for 2 pages and 1,650 for 3.

**Stranded headers:** if a role's title and org line land alone at the bottom of a page, set `"break_before": true`
on that role in the spec. Don't delete content to work around it.

## 4. Bullet craft

- Shape: **bold action + object**, how, measurable result. Example:
  "**Owned end-to-end delivery** of the checkout migration, enabling **120,000** monthly orders and **$2M annual savings**."
- Bold the lead verb phrase and the key metric. Bold sparingly elsewhere: two or three bold spans per bullet at most.
- 3–5 bullets for the most relevant roles, 2–3 for the rest. Order bullets inside each role by relevance to the
  posting, not chronology.
- Reword an inventory bullet to echo the posting's language **only where it is still true**. "Coordinated
  cross-functional delivery" can become "orchestrated execution across Sales, Engineering and Support" only if the
  inventory supports those groups.
- Spell out an acronym once if the posting does (First Call Resolution (FCR)).
- No first person, no "responsible for", no buzzword stacks.

## 5. Profile / summary (3–4 lines)

Formula: who the candidate is for *this* role + 2 proof points + what they want to do next that matches the
posting's mission. Name the domain and level the posting uses. Example for a technical PM role:

"Technical product manager building AI-assisted patient-access features in healthcare. Led a zero-downtime
migration of 120,000 monthly bookings and an API program adopted by 60 partners. Hands-on builder who turns new
capability into shipped, measured outcomes."

(That example uses the fictional persona in `templates/career-inventory.example.md`. Always draw real
proof points from the user's own inventory.)

## 6. Titles and role-summary lines

- Titles are fixed in the inventory: use them as given, even when the posting uses different words. Never upgrade
  seniority ("Senior", "Principal", "Lead") beyond what is listed.
- If the inventory's section 0 says a role's content must mention other roles the candidate played, put that in a
  one-line `summary` under the org line. Tune its wording to the posting, but never drop it.
- For a Product Owner posting, lead that role's bullets with backlog ownership. For an engineering or TPM
  posting, lead with the engineering-team work.
- List the most recent role first. On PM/TPM resumes, a side or part-time role can be kept to 2–3 bullets.

## 6a. Hands-on projects section

If the inventory has a projects section with an approved short form, start from it and keep the candidate's wording.
Tailor by choosing and ordering bullets, not by rewriting them. Respect any naming rules recorded in section 0
(for example "describe the project generically on resumes; name it only in cover letters"). Default length is
three bullets; this section is optional on 2-page resumes and is the first thing to drop when space runs out.

## 7. ATS hygiene

The template is single-column, no tables or text boxes, real bullets, standard headings. Keep it that way.
Section headings in caps as in the template: PROFILE, CAREER HIGHLIGHTS, PROFESSIONAL EXPERIENCE,
HANDS-ON PROJECTS, SKILLS, CERTIFICATIONS, EDUCATION (or EDUCATION & CERTIFICATIONS).

**Education:** include it whenever the posting mentions a degree. Automated screens drop resumes that have no
education section. Include it on 3-page resumes regardless.

## 8. Before shipping, check

1. `check_resume.py` shows no UNVERIFIED metrics (or each one is traced and added to the inventory with a source).
2. Must-have keyword coverage ≥ 80%, with every miss explained in the fit brief as a real gap or a truthful synonym.
3. Page count matches the length rule; render the PDF and look at page 1.
4. Titles and dates match the inventory exactly, and any required role-summary lines are present.
5. Keyword coverage is a wording check, not proof. A phrase that matches inside an unrelated context
   (for example "customer success" inside "customer success stories") doesn't count as evidence; say so in the brief.
