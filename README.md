# AI Career Agency

**An AI-native career agency for your terminal, desktop app and browser.** It tailors resumes, cover letters, fit
briefs and outreach notes to any job posting, using only facts you have verified.

Think of a talent agent for an actor. You supply the real credits. The agent reads each casting call, picks the
credits that fit, and writes the pitch, but never invents a role you didn't play. This plugin works the same way:
you keep a **career inventory** of verified facts, and the agent tailors from it. It cannot add a number that
isn't in your inventory, and a script checks that before anything ships.

> **v0.1** ships one agent: `job-tailored-resume`. More skills for the agency may follow.

## What you get per job posting

| Output | What it is |
|---|---|
| Resume | `.docx` + `.pdf`, single-column and ATS-friendly, tailored to the posting's language |
| Cover letter | `.docx` + `.pdf`, under one page, consistent with the resume |
| Fit brief | A candid match rating, gaps, keyword coverage and interview stories (`Fit Brief.md`) |
| Outreach | A LinkedIn note and a short email for the recruiter or hiring manager (`Outreach.md`) |

Ask for the whole package or only part: `r` (resume), `cl` (cover letter), `fit` (should I apply?), `out` (outreach).

---

## Setup

Setup has two parts, and the second is the one people skip:

1. **Install the plugin** (the agent and its tools). Same for everyone.
2. **Give the agent your career inventory** (your private facts). *Where* it lives depends on where you use Claude.

### Which surface should I use?

An analogy helps here. Picture where your agent works:

| Where you use Claude | The analogy | Where your inventory lives |
|---|---|---|
| **Claude Code** (terminal, IDE, desktop Code tab) | Your **own workshop**. The agent works at your desk, with your files on your disk. | A folder on your computer (`~/.career-agency/` or any folder you point to) |
| **Claude desktop app, Cowork tab** | A **desk with one folder handed over**. The agent sees only the folder you choose for the task. | The folder you choose when you start a task |
| **Claude desktop app Chat tab, or claude.ai in the browser** | A **visiting agent with a briefcase that's emptied every night**. Its sandbox keeps no files between sessions, so you bring your papers each time. | A **Project's knowledge** (best), or files you attach to the chat |

If you are unsure, use the **browser or desktop Chat tab with a Project**: nothing to install on your computer.

### Before you start

- A **paid Claude plan** (Pro, Max, Team or Enterprise). Plugins and skills aren't available on Free.
- **Code execution turned on** (claude.ai and the desktop app): **Settings > Capabilities > "Code execution and file
  creation"**. The skill builds your .docx and .pdf by running scripts, so it needs this.
- **Team or Enterprise:** an Owner may need to enable code execution and Skills in **Admin settings > Capabilities**,
  and may control which plugin sources you can add.

---

### Part 1: Install the plugin

Pick **one** route. Once installed from claude.ai, the desktop app or Claude Code, the plugin is saved to your
account and also appears in the others (Claude Code syncs it the next time you start a session signed in to the
same account).

#### Route A: add this repository as a marketplace (recommended; updates are easy)

**claude.ai in the browser, or the Claude desktop app** (Chat and Cowork tabs):

1. Open **Customize** in the left sidebar, then **Plugins**.
2. Select **Add**, then **Add marketplace**.
3. Enter `nipaul/ai-career-agency` and confirm.
4. Find **career-agency** in the list (open **Discover** if it isn't shown) and select **Add** or **Install**.
5. Open the plugin and check its **Skills** tab lists `job-tailored-resume`.

To pick up new versions later, open the marketplace and select **Check for updates**, or turn on **Sync
automatically**.

**Claude Code** (one step, Claude Code 2.1.275 or later):

```
/plugin install career-agency --marketplace nipaul/ai-career-agency
```

Or in two steps, which works on every version:

```
/plugin marketplace add nipaul/ai-career-agency
/plugin install career-agency@ai-career-agency
```

Then run `/reload-plugins` (or restart Claude Code).

#### Route B: upload a zip (works with no GitHub at all)

Use this if you don't want to use GitHub, the repository isn't reachable from your network, or you want to install
a copy you have modified.

1. Get the zip. Either download `career-agency-plugin.zip` from a [release](https://github.com/nipaul/ai-career-agency/releases), or build it yourself
   from a clone of this repository:
   ```
   python tools/package.py
   ```
   This writes `dist/career-agency-plugin.zip` and `dist/job-tailored-resume-skill.zip`.
2. In claude.ai or the desktop app: **Customize > Plugins > Add > Upload plugin**, and choose
   `career-agency-plugin.zip`.

#### Route C: skill only (no plugin)

If your organization blocks plugin uploads but allows skills:

1. Turn on code execution (see *Before you start*).
2. **Customize > Skills > Upload skill** (or **Settings > Capabilities > Skills > Upload skill**), and choose
   `job-tailored-resume-skill.zip` from `python tools/package.py`.
3. Turn the skill on in the list.

The zip must contain the skill folder itself at the top level (`job-tailored-resume/SKILL.md`). The packaging script
guarantees that. If you zip it by hand, zip the folder, not the files inside it.

> **Private repository?** For a marketplace you add yourself, public GitHub repositories work directly. For a
> private one, connect your GitHub account when the dialog asks and give the Claude GitHub App access to the
> repository.

---

### Part 2: Give the agent your career inventory

Your inventory is two small files:

| File | What it holds |
|---|---|
| `career-inventory.md` | Verified roles, titles, dates, metrics, projects, skills, and your decisions |
| `profile.json` | Your name, contact line, and where to save applications |

**You don't have to write them by hand.** On first run the agent notices you have no inventory, asks for your
existing resumes (PDF, Word or pasted text), drafts the inventory, and walks you through confirming every number,
title and date. Annotated starter files with fictional data are in
[`skills/job-tailored-resume/templates/`](skills/job-tailored-resume/templates/) if you'd rather fill them in
yourself.

#### Setup for browser and desktop Chat (Project knowledge)

1. Create a **Project** (left sidebar, **Projects**, **New project**), for example "Job search". Keep it
   **private to you**: anything in project knowledge is visible to everyone the project is shared with.
2. Start a chat in that Project, attach your current resumes, and say:
   > Set up my career inventory from these resumes.
3. Answer the confirmation questions. When it finishes, the agent hands you `career-inventory.md` and
   `profile.json` as files.
4. **Download both and keep them somewhere private** (a private Git repository or an encrypted folder). That is
   your **master copy**.
5. Add both files to the Project's **knowledge**. That is a **mirror** the agent reads in every chat in the Project.

From then on, every chat in that Project can use them. Edit the master copy, then re-upload to the Project, so the
two never drift apart.

Why this routing: the chat sandbox starts empty each session. The agent reads your two files from project
knowledge, copies them into the sandbox, and builds your documents there.

#### Setup for Cowork (a connected folder)

1. Put `career-inventory.md` and `profile.json` in a folder on your computer (for example `~/career-data/`).
2. When you start a Cowork task, choose that folder.
3. Ask: *"Tailor my resume for this job"* and share the posting. The agent finds the files in the folder.

#### Setup for Claude Code (a folder on disk)

Put the files in `~/.career-agency/`, or in any folder and point to it with an environment variable:

```bash
# macOS / Linux (add to ~/.zshrc or ~/.bashrc)
export CAREER_AGENCY_HOME="$HOME/career-data"
```

```powershell
# Windows PowerShell (persists for your user; open a new terminal afterwards)
setx CAREER_AGENCY_HOME "C:\Users\you\career-data"
```

The skill and its scripts look in this order: a folder you name in the conversation, `$CAREER_AGENCY_HOME`, the
current directory, then `~/.career-agency/`.

> **Never commit your inventory to a public repository.** It holds personal details. This repo's `.gitignore`
> blocks `career-inventory.md` and `profile.json` so they can't land here by accident; give your own data folder
> the same protection.

---

### Part 3: Use it

Describe the task, or pick the skill yourself. Type `/` in the message box and choose
**`career-agency:job-tailored-resume`** (Claude Code: `/career-agency:job-tailored-resume`).

Examples:

```
Tailor my resume for this role: <paste the job posting or a URL>
```
```
fit: is this worth applying to? <posting>
```
```
r cl  <posting>          (resume and cover letter only)
```

Where your files end up:

| Surface | Output |
|---|---|
| Browser / desktop Chat | Delivered in the chat as downloadable files, plus a short verdict (match rating, gaps) |
| Cowork | Saved in your connected folder under `<Company> - <Role>/`, and shown in the task |
| Claude Code | Saved under the `jobs_folder` in `profile.json`, or the current directory |

Each posting gets one folder named `<Company> - <Role>`. Re-runs create `v2`, `v3` files instead of overwriting
anything you may have edited or sent.

### Check that it works

1. **Customize > Plugins** lists *career-agency*, and its **Skills** tab shows `job-tailored-resume`.
2. **Customize > Skills** shows the skill toggled on.
3. Type `/` in a chat and `career-agency:job-tailored-resume` appears in the menu.
4. Say *"Set up my career inventory"* with no files attached. The agent should ask for your resumes. That
   confirms the skill loaded.

### Troubleshooting

| Symptom | Likely cause and fix |
|---|---|
| Plugins or Skills missing from **Customize** | You're on the Free plan, or your organization has them off. Ask an Owner. |
| Skill upload is rejected | The zip has `SKILL.md` at its root instead of inside `job-tailored-resume/`, or the folder name doesn't match the skill name. Rebuild with `python tools/package.py`. |
| Plugin upload is rejected | The archive must contain exactly one `.claude-plugin/plugin.json`. Use the packaged zip. |
| The agent builds nothing, or says it can't run scripts | Turn on **Code execution and file creation** in Settings > Capabilities. |
| *"Career inventory not found"* | The agent can't see your files. In chat, add them to the Project's knowledge or attach them; in Cowork, choose the folder that holds them; in Claude Code, set `CAREER_AGENCY_HOME`. |
| You get a .docx but no .pdf | The sandbox couldn't install LibreOffice. The agent tells you; open the .docx and use **Save as PDF**. |
| `UNVERIFIED metric` in the output | Working as intended: the number isn't in your inventory. Remove it, or add it to the inventory with a source if it's true. |
| The plugin doesn't show up in Claude Code | Run `/reload-plugins`. Plugins you install *from* the Claude Code command line stay on that machine and aren't added to your claude.ai account. |
| New version not showing | Open the marketplace and select **Check for updates**. |

### Update or remove

- **Update:** marketplace installs update from their source (**Check for updates**, or **Sync automatically**).
  Zip installs: upload the new zip.
- **Remove:** **Customize > Plugins**, open the plugin, its menu, **Remove**. Your inventory is never touched,
  because it lives outside the plugin.

---

## How it keeps you honest

- **Select and phrase, never invent.** The agent may reorder, merge and reword your bullets to echo the posting. It
  may not add a metric, employer, title, date, team size or technology.
- **Fact guard.** `check_resume.py` extracts every metric-like token from the finished document and looks it up in
  your inventory. Anything missing is reported as `UNVERIFIED` and must be fixed before delivery.
- **Gaps are named, not hidden.** If the posting asks for something you haven't done, the fit brief says so and
  suggests honest framing and interview prep.
- **Decisions beat old resumes.** When two of your resumes disagree (a title, a date, a figure), you record the
  winner once in section 0 of the inventory, and every future document follows it.

## Your data stays yours

Your inventory lives **outside** this plugin and is never part of this repo, so updating or removing the plugin
never touches it.

| Surface | Master copy (you edit) | Copy the agent reads |
|---|---|---|
| Claude Code | `~/.career-agency/` or `$CAREER_AGENCY_HOME` | the same folder |
| Cowork | a folder on your computer | the folder you connect to the task |
| Browser / desktop Chat | a private folder or private Git repository | a **mirror** in your Project's knowledge |

A plugin or skill you add yourself isn't reviewed by Anthropic, and its instructions and scripts run in your
sessions. Everything here is plain text and Python you can read before installing.

## Repository layout

```
.claude-plugin/
  plugin.json            plugin manifest (name: career-agency)
  marketplace.json       makes this repo addable as a marketplace
skills/job-tailored-resume/
  SKILL.md               the workflow
  references/            playbook (tailoring rules) and companion-document templates
  scripts/               build_docx.py, check_resume.py
  templates/             example inventory, profile and resume spec (fictional data)
tools/package.py         builds the upload zips in dist/
```

## Develop and test locally

```bash
# Build a sample resume from the fictional data
cd skills/job-tailored-resume
python3 scripts/build_docx.py templates/resume-spec.example.json /tmp/sample.docx --pdf \
  --profile templates/profile.example.json
python3 scripts/check_resume.py /tmp/sample.docx --inventory templates/career-inventory.example.md
```

Run the tests (needs `pip install python-docx` for the end-to-end case):

```bash
python -m unittest discover -s tests -v
```

Add a made-up number to the spec (for example "grew revenue 73%") and re-run the check: it will be flagged.

Try the plugin from a local clone before publishing changes:

```
/plugin marketplace add ./path/to/ai-career-agency        # Claude Code
claude plugin validate .                                   # checks manifests and skill frontmatter
python tools/package.py                                    # builds dist/*.zip for claude.ai / desktop
```

## Contributing

Issues and pull requests are welcome. Please never include real personal data in examples, tests or issues.

## License

[MIT](LICENSE)
