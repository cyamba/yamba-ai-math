# RR003 critical independent computations

These are portable copies of the two separately authored critic scripts
that actually ran during RR003. Only repository-root resolution and the
round-two reference to the sibling first script were changed. Exact original
execution hashes and portable-copy hashes are in provenance.json. Reviews
and original execution receipts refer to the original hashes, not these
copies. They retain ordinary Python assertions; run without `-O`.
No third critic challenge is implied by reproducing saved computations.

From the repository root, under an authorized fresh resource budget:

    python3 research/rogers-ramanujan/rr003/reproduction/critic1.py
    python3 research/rogers-ramanujan/rr003/reproduction/critic2.py

The RR003 meter refuses to extend the original deadline. This record does
not authorize resetting its ledger, adding a review round, or treating
reproduction as independent semantic review of later author revisions.
Bulk stdout and source-bound execution receipts remain ignored in .runs/rr003.

The separate middle_source.py file is an author verification-only enumerator
for the attributed positive two-cut family. It is not a critic script or
an endpoint algorithm. Its frozen pilot checks actual weights<=12; the
larger check uses actual weights<=30, with normalized middle state<=23 so
actual L stays<=30. Coefficient agreement does not supply a branch bijection.
