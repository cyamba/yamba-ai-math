# RR004 result — a reviewed obstruction, complete KR1 unresolved

**Complete explicit KR1 bijection: NOT ACHIEVED.**
**Novelty status: NOT VERIFIED.** Work is local; no push or publication.
RR004 is closed after its two authorized critic rounds. A fresh investigation
needs its own authorization, contract and ledger; neither RR003 nor RR004
has spare review rounds to reuse.

## Governing objective and assurance

The objective remains explicit weight-preserving mutually inverse algorithms
between partitions with parts 1,3,6,8 modulo nine and ascending positive gap
partitions: distance-two gaps at least three, and adjacent difference at
most one implies sum divisible by three. Include weight zero.
Completion still requires universal validity, weight, termination, both
inverse proofs, executable full endpoint composition and separate semantic
review. Lean certification and exposition remain subsequent obligations.
No objective, proof standard, attribution or success criterion was relaxed.

| Claim | Status and assurance |
| --- | --- |
| No full U-C bijection with a fixed signed height-transition sum for b | **Proved**, written universal argument supported by the [first separate review](round-1-review.md); ordinary manual-review assurance |
| No weight-preserving injection from the fourteen listed U objects, maximum weight ten, into C with that b formula | **Proved**, [finite written proof](round-2-proposal.md) supported by the [second separate review](round-2-review.md); not formally certified |
| Executable transcription of obstruction witnesses and small literal domains | **Empirical/exact computation**, checked through weight twelve; supports transcription, not a constructive KR1 theorem |
| Full intrinsic U-C decomposition and full residue-gap bijection | **Unverified/unresolved**; no candidate maps or universal coverage argument obtained |
| Newness or general workflow benefit | **Unverified**; no fresh external prior-work audit or controlled workflow evaluation |

The same distinct critic profile performed both rounds; this is separate
semantic review, not a claim of independent errors. No final RR003
author-only component was imported as an accepted premise. Earlier RR003
assurance distinctions remain unchanged.

## What the obstruction says

Write the literal decoded column heights as h_1>=...>=h_l>0 and
h_(l+1)=0. The attempted intrinsic statistic was

    b(U) = sum_i e(h_i,h_(i+1)),

with fixed arbitrary real signed charges on height transitions, including
repetitions and the terminal zero. Charges may depend on both full
heights but not on the rest of the input, index or weight.
Even an added initial-height potential telescopes into the same class.

Fourteen exact U objects force e(1,0)=e(1,1)=e(2,1)=e(2,2)=0,
e(2,0)=e(3,1)=1 and e(3,2)=-1. Therefore the valid source
U=(6,3,1), weight ten, would have b=-1. The full finite argument
uses target capacities and injectivity alone. It assumes no global
counting identity and does not assert a minimal witness set.

This **refutes only the fixed-transition recovery class**. Context,
run multiplicity, marking or cancellation remain possible.
The originally omitted U=(6,3) and C=(3,0,(0,0,0),()) are traced,
but no global matching between them was selected. Restricted old
assignments remain replaceable by a coherent full construction.

## Execution and validation

The [contract](contract.md) and [pre-run reflection](pre-run.md) were saved
before mathematical verification. Both proposals and executable dependencies
were frozen before their checks. The inverse/coverage gate produced an
exact obstruction, so broad implementation stopped early; no weight-thirty
sweep or recursive-route pivot occurred. See the [revision record](round-1-revision.md).

The author certificate and the first critic independently regenerated small
literal domains through twelve. The second critic independently checked
all nine frozen inputs and used exact rational elimination: 224
capacity-admissible b assignments, zero consistent real-charge solutions.
This is a finite algebraic check of the scoped impossibility argument,
not a formal proof-checker run. The critic's first auxiliary script had
a transcription error; its failed script and receipt are preserved beside
the corrected successful run. [Portable script copies](reproduction/README.md)
retain hashes and failure provenance.

All **95 repository tests passed**, including five RR004 regressions for
stale/missing frozen evidence, malformed literal inputs, negative-witness
reporting, optimized-Python completion failure and refusal to overwrite
evidence. The required repository checker and program planner are recorded
in the [verification summary](verification-summary.json).
The complete-bijection flag deliberately returns exit **2**.

Exact timing, cumulative computation, RSS and artifact totals are in
[execution.json](execution.json). The meter checks local child peak RSS
after exit; it does not reserve OS memory or measure model RSS.
Conservative bootstrap/maintenance charges are distinguished from measured
child invocation time. Raw receipts remain in ignored .runs/rr004.
No new dependencies, providers, external messages or user-file deletions.

## Next unresolved lemma and learning

Construct a context-sensitive intrinsic U-C extraction and reconstruction
for arbitrary a,b, returning ascending exact-length zero-padded mu,nu,
with weight Q=a^2+3ab+3b^2, disjoint exhaustive coverage, termination and
both inverse identities. A useful first foothold must specify the extra
recoverable context that avoids the finite transition-charge obstruction.
No such corrected construction is supplied here.

The first reflection tweak was applied as an inverse-statistic gate;
the second reserved criticism for the claims actually retained. Observed:
a scoped failure received criticism before broad coding. **Workflow
benefits remain unvalidated**; one attempt supplies no causal comparison
or general increase in discovery success. Preserve all earlier failures.

CY-KR1-001 and CY-KR1-002 remain PENDING; no human feedback was returned
and no Drive delivery was performed. Continue from [NEXT_SESSION.md](NEXT_SESSION.md).
