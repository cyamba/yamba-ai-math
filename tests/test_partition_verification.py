"""Synthetic protocol tests: failed/missing evidence must never become success."""

import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from research.partitions.verify_all import run_suite


class PartitionVerificationTests(unittest.TestCase):
    def run_fixture(self, *, failed_stage=None, missing=None, failed_certificate=None,
                    changed=False, unavailable=False):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        calls = []

        def fake_runner(command, **kwargs):
            index = len(calls)
            calls.append(command)
            if unavailable and index == 3:
                raise FileNotFoundError("synthetic missing Lean dependency")
            if "--output" in command:
                path = Path(command[command.index("--output") + 1])
                name = path.stem
                if name != missing:
                    path.write_text(json.dumps({
                        "status": "failed" if name == failed_certificate else "passed",
                        "sha256": {"synthetic.lean": "fixture"}, "axioms": {},
                    }))
            return subprocess.CompletedProcess(command, 1 if index == failed_stage else 0,
                                                "Synthetic verification protocol fixture")

        snapshots = 0

        def snapshotter(_):
            nonlocal snapshots
            snapshots += 1
            return {"synthetic.lean": "changed" if changed and snapshots > 1 else "fixture"}

        return run_suite(root, root / "artifacts", runner=fake_runner,
                         snapshotter=snapshotter), calls

    def test_all_required_stages_and_records_are_needed(self):
        report, calls = self.run_fixture()
        self.assertEqual(report["status"], "passed")
        self.assertEqual(len(calls), 4)
        self.assertEqual(report["h3_status"], "incomplete")
        self.assertIsNone(report["final_h3_declaration"])

    def test_failed_repository_check_does_not_skip_certificate_checks(self):
        report, calls = self.run_fixture(failed_stage=0)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(len(calls), 4)

    def test_missing_dependency_prevents_success(self):
        report, _ = self.run_fixture(unavailable=True)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["certificates"]["mathlib"]["status"], "failed")

    def test_zero_exit_without_certificate_prevents_success(self):
        report, _ = self.run_fixture(missing="std")
        self.assertEqual(report["status"], "failed")

    def test_failed_certificate_with_zero_process_exit_prevents_success(self):
        report, _ = self.run_fixture(failed_certificate="mathlib")
        self.assertEqual(report["status"], "failed")

    def test_source_change_during_checks_prevents_success(self):
        report, _ = self.run_fixture(changed=True)
        self.assertEqual(report["status"], "failed")
        self.assertFalse(report["source_unchanged_during_checks"])


if __name__ == "__main__":
    unittest.main()
