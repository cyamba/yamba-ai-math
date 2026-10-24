# Auxiliary context snapshot mismatch

The root's read-only integrity audit at21:22 UTC found one historical RR007 snapshot mismatch. This is preserved as a deviation, not removed from the evidence.

`.runs/rr007/a-context-hook-pin.json` pins the then-current `fleet-a/context.md` as `ad825acc4475a9b159dc41b858b822e0b711d124fc27ba6cc7a5478fc3b0b02b`. The final author handoff and distinct critic freeze instead pin that file as `98a36ece4428befeaac1c8565d200a96d8b2d5ca65839e9f53759820e0728215`. The final file is not an exact prefix extension of the earlier file, and an exact earlier text was not recovered. The main author says he did not edit it; a notebook update during the context investigator's still-active stage is a plausible explanation, not an established exact diff.

The auxiliary source-hook script and its separate forward/inverse/weight freeze JSON still match their early hashes. All initial canonical input pins, delayed RR006 raw pins, frozen A1–A3/B1–B3 definitions and scripts, final A handoff pins and critic pretrial pins match. No older closed ledger or RR006 evidence was changed.

Assurance consequence: the early auxiliary author pilot supports its unchanged script and explicit freeze JSON. It cannot certify that the entire later context notebook was identical to the early snapshot. The distinct critic separately froze the final notebook, supplied a semantic argument and ran a fresh independent literal pilot12 followed by the explicitly approved unchanged extension30. That later proof and empirical evidence are the basis for the accepted final source-grammar claim. They do not retroactively make the early full-file hash check pass.

Raw records: `.runs/rr007/root-integrity-during-revision.receipt.json` (failed strict comparison), `root-context-snapshot-audit.receipt.json` (prefix investigation), `a-context-hook-pin.json`, `a-author-final-pin.json`, and `fleet-a/critic-a-freeze.json`. No formal assurance or complete immutable provenance is claimed for the early context notebook.
