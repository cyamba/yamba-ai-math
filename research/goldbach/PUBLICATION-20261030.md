# Publishing the paused Goldbach research record

The user authorized committing, pushing, opening a PR and merging this research on30 October2026. This publication preserves a paused investigation. It does not announce a Goldbach proof or verified breakthrough.

The [handoff](HANDOFF-20261030.md) is an immutable snapshot written before the research was committed. Its statement that the outputs were untracked describes that moment. After this change is committed, the selected research records and programs are versioned. Ignored .runs inputs and prepared packets remain local; their identities and primary source links are documented in the provenance records.

Historical files have not been normalized or rewritten to make checks pass. The scoped Git attributes preserve their original bytes, including mixed line endings and documented frozen formatting defects. Run:

```sh
python research/goldbach/checks/verify_frozen_artifacts.py
```

This verifies artifact identity, not mathematical validity or novelty. The CI workflow runs it alongside the existing repository checks. The focused tests exercise changed line endings, missing files and rejected paths outside the repository.

Current local validation is recorded separately from the historical checkpoint results. On the latest upstream checkout, the full Windows suite encountered pre-existing Unix resource-module, path, symlink and frozen-checkout issues. The Goldbach tests and repository/contracts checks passed. The PR's clean Ubuntu runs are the relevant additional integration check; do not relabel the Windows suite green.

The [deferred publication YambaPost](publication/NEXT_PUBLICATION-20261030.md) records the updated PDF, LaTeX, YambaCode News and christopheryamba.com work for the next intentional session. The mathematical goal remains paused. A separate [free coding starter](../../docs/tutorials/free-ai-coding-starter.md) supplies the requested beginner lesson without requiring Claude Code access.
