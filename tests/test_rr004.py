"""RR004 evidence-integrity, literal-boundary and honest-completion checks."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / 'research/rogers-ramanujan/checks'
sys.path.insert(0, str(CHECKS))
import rr004_verify as first
import rr004_finite_certificate as finite


class RR004Tests(unittest.TestCase):
    def test_changed_or_missing_frozen_evidence_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'proof.md'
            source.write_text('frozen argument')
            freeze = root / 'freeze.json'
            freeze.write_text(json.dumps({'source_sha256': {
                'proof.md': hashlib.sha256(source.read_bytes()).hexdigest()}}))
            first.check_freeze(root=root, freeze_path=freeze)
            source.write_text('changed argument')
            with self.assertRaisesRegex(AssertionError, 'frozen source changed'):
                first.check_freeze(root=root, freeze_path=freeze)
            source.unlink()
            with self.assertRaises(OSError):
                first.check_freeze(root=root, freeze_path=freeze)

    def test_invalid_columns_are_rejected_before_diagnostic_charge(self):
        for u in ((9,), (10,), (10, 1), (11,), (3, 6), (True,), (0,)):
            with self.subTest(u=u), self.assertRaises(ValueError):
                finite.candidate_pair_charge(u, {})
        self.assertEqual(finite.candidate_pair_charge((), {}), 0)
        with self.assertRaises(KeyError):
            finite.candidate_pair_charge((8,), {})

    def test_certificate_reports_failure_class_without_bijection_claim(self):
        report = finite.verify()
        self.assertEqual(report['full_bijection'], 'unresolved')
        self.assertEqual(report['candidate_maps'], 'absent')
        self.assertEqual(report['maximum_source_weight'], 10)
        self.assertEqual(report['source_count'], len(set(finite.WITNESSES)))
        self.assertEqual(report['diagonal_cases'], [
            {'e22': -1, 'b_333': -1, 'rejected': True},
            {'e22': 0, 'b_333': 1, 'rejected': False}])
        negative = [w for w in report['witnesses'] if w['forced_b'] < 0]
        self.assertEqual(negative, [{'U': (6, 3, 1), 'weight': 10, 'forced_b': -1}])

    def test_optimized_cli_keeps_completion_failure_and_existing_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'evidence.json'
            command = [sys.executable, '-O', str(CHECKS / 'rr004_finite_certificate.py'),
                       '--require-bijection', '--output', str(output)]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            original = output.read_bytes()
            report = json.loads(original)
            self.assertEqual(report['full_bijection'], 'unresolved')
            self.assertIn('required_completion_failure', report)
            repeated = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(repeated.returncode, 0)
            self.assertIn('refusing to overwrite evidence', repeated.stderr)
            self.assertEqual(output.read_bytes(), original)

    def test_small_literal_domain_check_cannot_trigger_larger_sweep(self):
        report = first.verify(12)
        self.assertEqual(report['map_pilot'], 'not_applicable_no_candidate_maps')
        self.assertEqual(report['weight30_sweep'], 'not_run_no_viable_map_candidate')
        self.assertEqual(report['cases'][0]['actual_U'], 1)
        self.assertEqual(report['cases'][0]['actual_C'], 1)
        for bad in (0, 9, 13, 30, True):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                first.verify(bad)


if __name__ == '__main__':
    unittest.main()
