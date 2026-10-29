import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_repository import operator_specific_lines  # noqa: E402


class OperatorNeutralSkillsTest(unittest.TestCase):
    def write(self, root: Path, relative: str, text: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_repository_shared_skills_are_operator_neutral(self):
        self.assertEqual(operator_specific_lines(ROOT), [])

    def test_flags_hardcoded_drive_link_and_owner_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, ".agents/skills/x/SKILL.md",
                       "ok\nInbox: https://drive.google.com/drive/folders/abc\nWhen Christopher asks\n")
            found = operator_specific_lines(root)
            self.assertEqual(len(found), 2)
            self.assertTrue(found[0].startswith(".agents/skills/x/SKILL.md:2:"))

    def test_ignores_untracked_local_configuration(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write(root, ".agents/local/yamba-post.json",
                       '{"YAMBAPOST_INBOX_FOLDER_ID": "https://drive.google.com/x"}')
            self.assertEqual(operator_specific_lines(root), [])


if __name__ == "__main__":
    unittest.main()
