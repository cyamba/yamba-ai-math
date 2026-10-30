"""Meaningful failure checks for frozen artifact identity verification."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parents[1] / "research/goldbach/checks/verify_frozen_artifacts.py"
spec = importlib.util.spec_from_file_location("goldbach_evidence", CHECKER)
checker = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(checker)


class GoldbachEvidenceTests(unittest.TestCase):
    def test_line_ending_change_fails_identity_check(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            artifact = root / "claim.md"
            original = b"frozen\r\n"
            artifact.write_bytes(original)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"files": [{"path": "claim.md", "sha256":
                hashlib.sha256(original).hexdigest()}]}), encoding="utf-8")
            self.assertEqual(checker.verify_manifest(root, manifest), (1, []))
            artifact.write_bytes(b"frozen\n")
            self.assertEqual(checker.verify_manifest(root, manifest)[1],
                             ["hash mismatch: claim.md"])

    def test_dictionary_manifest_and_missing_artifact(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"files": {"missing.md": "0" * 64}}),
                                encoding="utf-8")
            self.assertEqual(checker.verify_manifest(root, manifest),
                             (1, ["missing: missing.md"]))

    def test_parent_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = root / "manifest.json"
            manifest.write_text(json.dumps({"files": {"../outside.md": "0" * 64}}),
                                encoding="utf-8")
            self.assertEqual(checker.verify_manifest(root, manifest)[1],
                             ["outside repository: ../outside.md"])


if __name__ == "__main__":
    unittest.main()
