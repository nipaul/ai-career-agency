#!/usr/bin/env python3
"""Two deterministic checks on a finished resume or cover letter.

1. Fact guard: every metric-like token (percentages, $ amounts, counts like 2,500+,
   1.5M, <2 weeks, 12-member) in the document must appear somewhere in
   the user's career inventory (career-inventory.md). Anything that doesn't is printed as UNVERIFIED so it
   can be removed or traced back to a source before the file goes out.
2. Keyword coverage (optional): given a JSON list of keywords/phrases pulled from the
   job posting, report which appear in the document (case-insensitive).

Usage:
    python check_resume.py out.docx --inventory /path/to/career-inventory.md [--keywords keywords.json]

If --inventory is omitted, the inventory is looked up in $CAREER_AGENCY_HOME, ./ and ~/.career-agency/.
If the file has <!-- INVENTORY START --> / <!-- INVENTORY END --> markers, only the text between
them counts as evidence; otherwise the whole file does.

keywords.json: ["assistant", "roadmap", "A/B testing", ...]  or
               {"must_have": [...], "nice_to_have": [...]}
"""
import json
import os
import re
import sys
from pathlib import Path

METRIC = re.compile(
    r"(?:[$<~]?\d[\d,]*(?:\.\d+)?\s?(?:%|\+|[KMB]\b|MM\b|x\b)?\+?)"
)


def find_inventory(explicit=None):
    """Resolve the career inventory file or exit with a clear message."""
    if explicit:
        path = Path(explicit).expanduser()
        if not path.is_file():
            sys.exit(f"inventory not found: {path}")
        return path
    candidates = []
    home = os.environ.get("CAREER_AGENCY_HOME")
    if home:
        candidates.append(Path(home).expanduser() / "career-inventory.md")
    candidates += [Path.cwd() / "career-inventory.md", Path.home() / ".career-agency" / "career-inventory.md"]
    for c in candidates:
        if c.is_file():
            return c
    sys.exit("career inventory not found: pass --inventory <path> or set CAREER_AGENCY_HOME")


# Contact details are not achievements: drop emails, URLs and phone numbers before looking for metrics.
NOT_METRICS = re.compile(
    r"\S+@\S+|https?://\S+|www\.\S+"
    r"|\(?\d{3}\)?[\s.-]\d{3,4}[\s.-]\d{4}|\d{3}-\d{4}"
)


def doc_text(path):
    from docx import Document  # imported here so the pure functions below can be used (and tested) without it
    d = Document(path)
    return "\n".join(p.text for p in d.paragraphs)


def norm(s):
    """Lower-case; drop thousands separators and the space in '20 %' / '1.5 M' so '2,500+' == '2500+'."""
    s = re.sub(r"(?<=\d),(?=\d)", "", s.lower())
    return re.sub(r"(?<=\d)\s+(?=[%+]|[kmb]|mm|x)", "", s)


def in_inventory(core, inv):
    """True if `core` appears in `inv` as a whole number: '8%' must not match inside '18%', or '12' inside '120000'."""
    pat = r"(?<![\d.])" + re.escape(core) + r"(?!\d|\.\d)"
    return re.search(pat, inv) is not None


def metric_tokens(text):
    toks = set()
    for m in METRIC.finditer(NOT_METRICS.sub(" ", text)):
        tok = m.group(0).strip()
        digits = re.sub(r"\D", "", tok)
        if not digits:
            continue
        # ignore years, phone fragments and single small digits that are just list counts
        if re.fullmatch(r"(19|20)\d\d", tok):
            continue
        if len(digits) <= 1 and not re.search(r"[%$+KMB]", tok):
            continue
        toks.add(tok)
    return toks


def fact_guard(text, inventory):
    raw = Path(inventory).read_text(encoding="utf-8")
    m = re.search(r"<!-- INVENTORY START -->(.*)<!-- INVENTORY END -->", raw, re.S)
    inv = norm(m.group(1) if m else raw)  # the inventory (between markers, if present) is the only evidence
    unverified = []
    for tok in sorted(metric_tokens(text)):
        core = norm(tok).rstrip("+")
        if not in_inventory(core, inv):
            unverified.append(tok)
    return unverified


def coverage(text, kw):
    groups = kw if isinstance(kw, dict) else {"keywords": kw}
    report = {}

    def found(w):
        # whole-word / whole-phrase match, case-insensitive ("AI" won't match "said"),
        # tolerant of simple endings and hyphen/space variants ("stakeholders", "instrumented",
        # "consumer facing" for "consumer-facing")
        pat = re.escape(w).replace(r"\-", r"[-\s]?").replace(r"\ ", r"[-\s]")
        return re.search(r"(?<![A-Za-z0-9])" + pat + r"(?:s|es|ed|d|ing)?(?![A-Za-z0-9])", text, re.I) is not None

    for g, words in groups.items():
        hit = [w for w in words if found(w)]
        miss = [w for w in words if not found(w)]
        report[g] = {"covered": hit, "missing": miss,
                     "pct": round(100 * len(hit) / max(1, len(words)))}
    return report


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    path = sys.argv[1]
    inventory = find_inventory(sys.argv[sys.argv.index("--inventory") + 1] if "--inventory" in sys.argv else None)
    text = doc_text(path)
    unv = fact_guard(text, inventory)
    print("FACT GUARD:", "all metrics trace to the career inventory" if not unv else "")
    for u in unv:
        print(f"  UNVERIFIED metric not found in the career inventory: {u}")
    if "--keywords" in sys.argv:
        kw = json.loads(Path(sys.argv[sys.argv.index("--keywords") + 1]).read_text(encoding="utf-8"))
        rep = coverage(text, kw)
        for g, r in rep.items():
            print(f"KEYWORDS [{g}] {r['pct']}% covered")
            if r["missing"]:
                print("  missing:", ", ".join(r["missing"]))
    words = len(text.split())
    print(f"WORD COUNT: {words}")


if __name__ == "__main__":
    main()
