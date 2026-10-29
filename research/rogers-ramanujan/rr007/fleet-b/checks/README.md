# Distinct critic evidence

These Python 3 standard-library scripts are exact copies of the raw RR007
critic pilots. Run them from the repository root only within an authorized
computation budget. Their literal bound is fixed at 12. They write their
compact result JSON into an existing `.runs/rr007/` directory; create that
directory first in a fresh checkout.

- `critic_b_independent.py` independently generates the B1/B2/B3 literal
  domains and imports no author or legacy executable.
- `critic_b_stockhofe12.py` independently generates literal U/B domains and
  calls only the actual RR003 endpoint and its definition-only dependency.
- `critic_b_evidence_hashes.json` records matching raw/canonical SHA-256
  hashes for the scripts and the saved pilot results.

The saved results are finite evidence. The universal ordinary arguments,
assurance scope and inspected-source limitation are in `../review-1.md`
and `../stockhofe-review.md`. No high-weight legacy tests or new full
bijection are part of this evidence.
