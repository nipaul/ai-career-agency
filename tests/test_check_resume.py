"""Tests for the fact guard and keyword coverage. Run from the repo root:  python -m unittest discover -s tests -v"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "job-tailored-resume"
sys.path.insert(0, str(SKILL / "scripts"))

import check_resume as cr  # noqa: E402

INVENTORY = SKILL / "templates" / "career-inventory.example.md"  # contains 18%, 120,000, 60, $2M, 31%, 44%, 40


class FactGuard(unittest.TestCase):
    def unverified(self, text):
        return cr.fact_guard(text, INVENTORY)

    def test_verified_metrics_pass(self):
        self.assertEqual(self.unverified("Cut no-shows by 18% across 40 clinics, moving 120,000 bookings; $2M savings."), [])

    def test_invented_metric_is_flagged(self):
        self.assertEqual(self.unverified("Grew revenue 73%."), ["73%"])

    def test_no_substring_match_inside_larger_number(self):
        # 8% is inside 18%, 12 inside 120,000, 0% inside 40%: none of these may count as verified.
        for text, tok in (("Cut costs 8%.", "8%"), ("Led 12 teams.", "12"), ("Raised 4% growth.", "4%")):
            self.assertIn(tok, self.unverified(text), text)

    def test_thousands_separator_and_plus_suffix(self):
        self.assertEqual(self.unverified("Moved 120000 bookings."), [])
        self.assertIn("2,500+", self.unverified("Served 2,500+ users."))

    def test_contact_details_are_not_metrics(self):
        text = "Email: jane.doe2024@example.com | Mobile: 555-123-4567 | https://linkedin.com/in/jane-77"
        self.assertEqual(self.unverified(text), [])

    def test_years_are_ignored(self):
        self.assertEqual(self.unverified("Jun 2021 – Present"), [])

    def test_only_text_between_markers_counts(self):
        with tempfile.TemporaryDirectory() as d:
            inv = Path(d) / "inv.md"
            inv.write_text("outside 99%\n<!-- INVENTORY START -->inside 55%<!-- INVENTORY END -->", encoding="utf-8")
            self.assertEqual(cr.fact_guard("55%", inv), [])
            self.assertEqual(cr.fact_guard("99%", inv), ["99%"])


class Coverage(unittest.TestCase):
    def test_whole_word_and_variants(self):
        rep = cr.coverage("Shipped consumer facing roadmaps with A/B testing; said hello.",
                          {"must_have": ["consumer-facing", "roadmap", "A/B testing", "AI"]})
        self.assertEqual(rep["must_have"]["missing"], ["AI"])  # "AI" must not match inside "said"
        self.assertEqual(rep["must_have"]["pct"], 75)


class EndToEnd(unittest.TestCase):
    def test_example_spec_builds_and_passes_the_guard(self):
        try:
            import docx  # noqa: F401
        except ImportError:
            self.skipTest("python-docx not installed")
        import build_docx
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "sample.docx"
            build_docx.main([str(SKILL / "templates" / "resume-spec.example.json"), str(out),
                             "--profile", str(SKILL / "templates" / "profile.example.json")])
            text = cr.doc_text(out)
            self.assertIn("Jordan Avery", text)
            self.assertEqual(cr.fact_guard(text, INVENTORY), [])
            # the same document with an invented number must be caught
            text_bad = text + "\nGrew revenue 73%."
            self.assertEqual(cr.fact_guard(text_bad, INVENTORY), ["73%"])


if __name__ == "__main__":
    unittest.main()
