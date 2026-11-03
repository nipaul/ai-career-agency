"""Layout tests for the split skills. Run from the repo root:  python -m unittest discover -s tests -v"""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import sync_shared  # noqa: E402

SKILLS = ROOT / "skills"
EXPECTED = {"job-fit", "outreach-blurbs", "generate-resume", "job-tailored-resume"}


def skill_dirs():
    return sorted(p for p in SKILLS.iterdir() if p.is_dir())


class Layout(unittest.TestCase):
    def test_expected_skills_exist(self):
        self.assertEqual({p.name for p in skill_dirs()}, EXPECTED)

    def test_folder_name_matches_frontmatter_name(self):
        for sd in skill_dirs():
            text = (sd / "SKILL.md").read_text(encoding="utf-8")
            m = re.match(r"---\nname: (\S+)\ndescription: \"(.+)\"\n---\n", text)
            self.assertIsNotNone(m, f"{sd.name}: bad frontmatter")
            self.assertEqual(m.group(1), sd.name)

    def test_shared_copies_are_in_sync(self):
        for src, dst in sync_shared.targets():
            self.assertTrue(dst.exists(), f"missing {dst}")
            self.assertEqual(src.read_bytes(), dst.read_bytes(), f"{dst} differs; run tools/sync_shared.py")

    def test_referenced_files_exist(self):
        # Every `references/...`, `scripts/...`, `templates/...` path named in a SKILL.md must exist in that skill.
        for sd in skill_dirs():
            text = (sd / "SKILL.md").read_text(encoding="utf-8")
            for rel in set(re.findall(r"`((?:references|scripts|templates)/[\w./-]+)`", text)):
                self.assertTrue((sd / rel).exists(), f"{sd.name}/SKILL.md names missing file {rel}")


if __name__ == "__main__":
    unittest.main()
