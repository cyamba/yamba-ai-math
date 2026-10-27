import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import openai_math_watch as watch  # noqa: E402

CONTENTS = """**3 manuscripts covering 2 result families.**

**001. First <i>result</i>.** Proves a partition identity. ([Lean](lean/docs/001.md))

&emsp;[Paper](preprints/x.pdf)

**002. Second result.** Bounds edit distance.
"""


class ParseTests(unittest.TestCase):
    def test_parse_contents(self):
        parsed = watch.parse_contents(CONTENTS)
        self.assertEqual((parsed["manuscripts"], parsed["families_total"]), (3, 2))
        self.assertEqual(parsed["families"]["001"]["title"], "First result")
        self.assertTrue(parsed["families"]["001"]["lean"])
        self.assertFalse(parsed["families"]["002"]["lean"])
        self.assertNotIn("Lean", parsed["families"]["001"]["summary"])

    def test_diff_and_interests(self):
        old = {"families": {"001": {"title": "First result", "lean": False},
                            "003": {"title": "Gone", "lean": False}},
               "history_sections": ["October 6, 2026"]}
        current = watch.parse_contents(CONTENTS)
        current["history_sections"] = ["October 26, 2026", "October 6, 2026"]
        changes = watch.diff(old, current)
        self.assertEqual(changes["added"], ["002"])
        self.assertEqual(changes["removed"], ["003"])
        self.assertEqual(changes["newly_formalized"], ["001"])
        self.assertEqual(changes["new_history_sections"], ["October 26, 2026"])
        interests = [{"id": "partitions", "keywords": ["partition"]}, {"id": "bio", "keywords": ["edit distance"]}]
        self.assertEqual(watch.interest_matches(current["families"], interests), {"001": ["partitions"], "002": ["bio"]})


class StateTests(unittest.TestCase):
    def test_recorded_state_is_consistent(self):
        state = json.loads((ROOT / "references" / "openai-math-watch.json").read_text(encoding="utf-8"))
        baseline = state["baseline"]
        self.assertEqual(len(baseline["families"]), baseline["families_total"])
        for number in state["watched_families"]:
            self.assertIn(number, baseline["families"])
        self.assertEqual(len({rule["id"] for rule in state["interests"]}), len(state["interests"]))

    def test_report_runs_against_fixture(self):
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "CONTENTS.md").write_text(CONTENTS, encoding="utf-8")
            state = json.loads((ROOT / "references" / "openai-math-watch.json").read_text(encoding="utf-8"))
            text = watch.report(state, watch.read_checkout(Path(directory)))
        self.assertIn("Removed families", text)


if __name__ == "__main__":
    unittest.main()
