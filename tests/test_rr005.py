"""RR005 domain/evidence safeguards; finite checks do not certify KR1."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
CHECKS = ROOT / 'research/rogers-ramanujan/checks'
sys.path.insert(0, str(CHECKS))
import kr1
import rr005_chains as chains
import rr005_verify as verifier


class RR005Tests(unittest.TestCase):
    def test_stale_or_missing_frozen_proof_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root/'proof.md'
            source.write_text('fixed claim')
            (root/'round-1-freeze.json').write_text(json.dumps({'source_sha256': {
                'proof.md':hashlib.sha256(source.read_bytes()).hexdigest()}}))
            with patch.object(verifier, 'ROOT', root), patch.object(verifier, 'PHASE', root):
                verifier.check_freeze()
                source.write_text('new claim')
                with self.assertRaisesRegex(AssertionError, 'frozen source changed'):
                    verifier.check_freeze()
                source.unlink()
                with self.assertRaises(OSError):
                    verifier.check_freeze()

    def test_restricted_correspondence_rejects_unmatched_roots(self):
        # Weight eight is in both full domains but outside the two selected chains.
        with self.assertRaisesRegex(ValueError, 'restricted correspondence'):
            chains.partial_u_to_c((8,))
        with self.assertRaisesRegex(ValueError, 'restricted correspondence'):
            chains.partial_c_to_u(kr1.ClusterData(2,0,(2,2),()))
        for root in ((9,), (10,), (True,), [1]):
            with self.subTest(root=root), self.assertRaises(ValueError):
                chains.split_u(root)
        with self.assertRaises(ValueError):
            chains.join_u(chains.NormalForm((3,),0,0))
        for n in (-1, True, 1.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                chains.NormalForm((),n,0)

    def test_optimized_completion_gate_and_evidence_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            for script in ('rr005_verify.py','rr005_six_verify.py'):
                with self.subTest(script=script):
                    output = Path(directory)/(script+'.json')
                    command = [sys.executable,'-O',str(CHECKS/script),
                               '--require-bijection','--output',str(output)]
                    first = subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
                    self.assertEqual(first.returncode,2,first.stdout+first.stderr)
                    saved = output.read_bytes()
                    report = json.loads(saved)
                    self.assertEqual(report['full_KR1'],'unresolved')
                    self.assertIn('completion_failure',report)
                    second = subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
                    self.assertNotEqual(second.returncode,0)
                    self.assertIn('refusing to overwrite evidence',second.stderr)
                    self.assertEqual(saved,output.read_bytes())


if __name__ == '__main__':
    unittest.main()
