from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_repository", ROOT / "scripts" / "check_repository.py")
check_repository = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_repository)

ENTRY = "- 2026-10-29 | claude | math | Decompose the stalled lemma | why: rr004/result.md | check: glue reviewed"


def problems(*lines: str) -> list[str]:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "session-log.md"
        text = "# Log\n\nFormat notes may mention | pipes.\n\n## Entries\n\n" + "\n".join(lines) + "\n"
        path.write_bytes(text.encode("utf-8"))
        return check_repository.session_log_problems(path)


class SessionLogTests(unittest.TestCase):
    def test_tracked_log_is_valid(self):
        self.assertEqual(check_repository.session_log_problems(ROOT / "meta" / "session-log.md"), [])

    def test_well_formed_and_closed_entries_pass(self):
        self.assertEqual(problems(ENTRY, ENTRY + " -> kept (2026-11-02)"), [])

    def test_malformed_overlong_and_excess_entries_fail(self):
        self.assertTrue(problems("- yesterday we decided many things"))
        self.assertTrue(problems(ENTRY.replace("| math |", "| bench |")))
        self.assertTrue(problems(ENTRY + " " + "x" * 300))
        self.assertTrue(problems(*[ENTRY] * 41))

    def test_missing_log_fails(self):
        self.assertTrue(check_repository.session_log_problems(ROOT / "meta" / "no-such-log.md"))


if __name__ == "__main__":
    unittest.main()
