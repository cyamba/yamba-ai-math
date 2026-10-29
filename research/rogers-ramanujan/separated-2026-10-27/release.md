# Supporting contribution publication follow-up

On 27 October 2026, Christopher explicitly authorized pushing this work to a
remote PR and merging it. This supersedes the initial local-only scope for this
publication action. Original contracts and verification receipts remain historical
records of the earlier investigation.

Publication base: main at `b44c5ba4bdc531c426ca9355c00166382b85b6f0`.
Only the changes from local commits `17cb19a` and `c62c54b`, plus this
publication context, are carried onto that base. Older unmerged draft branches
are not included as dependencies.

The separated-family theorem, proof and mathematical review are unchanged.
Disposition: reviewed supporting contribution; zero global KR1 obligations
closed by this entry. Novelty remains unverified and no new Lean claim is made.
The existing positive cut-word research package retains its scope and records.

Fresh validation on the publication base is recorded below. GitHub's PR checks
and merge result are the authoritative remote execution record.

- `python3 -m unittest discover -s tests -v`: all 110 tests pass (3.352s).
  This is the current main suite plus eight new regressions; the original
  115-test receipt belongs to the earlier PR16-based investigation.
- `python3 scripts/check_repository.py`: passes, including shared skill checks.
- `python3 research/rogers-ramanujan/separated-2026-10-27/audit.py --maximum 60`:
  all restricted assertions pass over 55,403 cluster inputs. The unrestricted
  compiler remains refuted; the audit's success is not a full-bijection claim.
- Original executable-dependency hashes and the separately reviewed proof hash
  match. Added prose has no em dashes; the diff has no whitespace errors.
