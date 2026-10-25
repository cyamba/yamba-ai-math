# Christopher Yamba fiber-splitting approach: restricted progress

2026-10-25. Local, unpublished research checkpoint. **Full KR1 remains open.**

Christopher supplied the fiber-splitting/extra-dimension intuition. His exact
wording is preserved in the canonical [idea record](../ideas/CY-KR1-FIBER-001.md).
This attempt derives formulas from it; it does not establish their novelty.

## What the intuition becomes mathematically

A coarse output U does not have to remain the final output. Route its
different preimages to different valid outputs of the original weight, with
an inverse that can recognize the route. An extra direction can hold the
route during construction; its information must survive in the final
unmarked partition. Merely appending a tag solves an enlarged problem.
Different fibers must also receive disjoint outputs, and full KR1 requires
exhausting the target. These are separate obligations.

For the pictured ordinary tableaux the distinct outputs are
T1=((1,2),(3,4),(5)) -> ((1,2),(3),(4),(5)) and
T2=((1,2),(3,5),(4)) -> ((1,2,5),(3,4)). The output shape remembers the
branch. This local repair already existed in prior work. The explicit
predecessor rule in [the proof](proof-candidate.md) resolves arbitrary fiber
sizes for the ordinary family (2,2,1^r), r>=1, onto a precisely recognized
subset. It is not the graph-weighted P-tableau cancellation theorem.

## New restricted KR1 extension

The baseline is the exact reviewed **H3** map in saved checkpoint
ef7bfe0895c8648f6d8e4679b6c24dc09635f2c9, whose Phase 2 result is based on
5cbc2440aab896d3f7de9e45bba2bac027f9c5cb. It is distinct from Argon's
later rr004 implementation at 97d6561. No old assignments were silently
replaced, and no closed evidence files were edited.

Write

    C=(4,0,(x,x+t,x+t+y,x+t+y+z),()),  x,t,y,z>=0.

Its weight is 16+4x+3t+2y+z. This attempt adds **all x,t,z** for
**y=2, y=3 and y=4**, with actual U outputs and exact inverses, disjoint from H3.

Examples at the first points of these infinite slabs:

    y=2: (0,0,2,2)  -> U=(10,9,1),   weight 20.
    y=3: (0,0,3,3)  -> U=(8,8,6),    weight 22.
    y=4: (0,0,4,4)  -> U=(12,9,3),   weight 24.

The formulas use column multiplicities and reversible carries rather than
free labels or a finite apex matching. [Y2 proof](proof-candidate.md),
[Y3 proof for x>=1](y3-proof-candidate.md),
[repaired Y3 boundary proof](y3-repair-proof.md), and
[distinct semantic review](semantic-review.md) give the exact arguments.
The x=0 portion of the first Y3 proof is refuted and superseded explicitly.
The [Y4 proof](y4-proof-candidate.md) adds fourteen disjoint languages;
its delicate boundaries avoid the retained map's mandatory one/three cells.

A further encoding covers y=5..17 whenever

    x >= 3*ceil((2y+4)/3),  with arbitrary t,z.

It encodes y by the number of 10s and x modulo 3 by the number of 6s. The
common width funds the marker weight. The final coherent implementation
is `y4_extension.ExtensionV4`, with H3 supplied as a module. It excludes
alternate funded y=2/3/4 targets in its inverse as well as its forward map.
Together with retained H3, this covers every x,t,z for y=0,1,2,3,4 or y>=18.

**Assurance:** ordinary mathematical proofs with distinct semantic review,
conditional on the reviewed H3 baseline. These new statements have no Lean
certificate. **Novelty: unverified.** No complete KR1 theorem is claimed.

## What checking established

All earlier 3498 assignments through weight 40 remain unchanged. The new
slabs add 202 y2, 156 y3 and 118 y4 states, giving 3974 mapped states out of 5461
total C/U objects cumulatively through 40. The inverse recognizes exactly
those 3974 targets; endpoint maps to actual gap/residue partitions also
roundtrip. These counts measure a finite prefix, not a fraction of the
infinite problem and not a proof of the infinite claims.

There are 1980 distinct checked parameter-grid outputs for each of the three new slabs,
5400 initial funded-band checks, 405 first-composition checks, 378 final
funded-composition checks, 351 final Y4-composition funded checks, and 20
large-parameter stress cases across y2/y3/y4.
All are discovery/regression evidence, not held-out validation. Their exact
scopes and hashes are in [first-result.json](first-result.json),
[composition-result.json](composition-result.json), and
[y3-repair-result.json](y3-repair-result.json), and [y4-result.json](y4-result.json).
A critic separately checked 47 small y2 boundary cases. Root math subprocess time totaled 9.581 seconds;
the critic used 0.88 seconds. Memory was not measured. No paid providers,
installations, broad fleet, publication or push occurred.

Engineering verification: 95 repository unit tests passed (final run: 2.445 seconds),
and `scripts/check_repository.py` passed. Those checks do not certify math.

## Failures retained

* A naive ordinary-tableau rule applied to a general P is refuted by
  h=(1,2,4,4,5): ((1,2),(3,5),(4)) is valid, but ((1,2,5),(3,4)) is not.
* A naive even-x Y3 encoding collides with Y2 at weight 24; see the frozen
  second proof. A dimension erased on flattening cannot repair that.
* The first full-Y3 proposal is refuted at weight 22:
  new C=(4,0,(0,0,3,3),()) and old C=(3,0,(2,5,6),()) both give
  U=(12,6,3,1). The old f1 third-12 language had been omitted in the
  exclusion argument. V3 keeps that old assignment and routes the new
  source to (8,8,6). The rejected V2 files remain frozen as failure evidence.

## Next precise work

1. In a new bounded attempt, attack y=5..17 with
   x<3*ceil((2y+4)/3). The variables t,z remain unbounded. Try a finite
   state carry rule with intrinsic image recognition; do not expand a
   lookup table or reassign retained outputs without a coherent proof.
   An untested next candidate for y=5, even x=2q>=2, is
   U=10,9,8^q,6,3^t,1^(z+1). Its weight is correct; exclusion,
   exact recognition and composition have NOT received a new review/check.
2. Separately handle missing b>0 sectors. The first still-unmapped source
   in the checked prefix is C=(3,1,(0,0,0),(0)), **weight 21**.
3. Prove general-a coverage and exhaustion, then compare with closest
   published constructions before any full-bijection or novelty claim.
4. For the separate P-tableau problem, encode poset comparisons and graph
   inversion changes in the fiber state; ordinary order is insufficient.

Related primary literature: the inspected abstract of Garsia–Milne,
[Method for constructing bijections for classical partition identities](https://pmc.ncbi.nlm.nih.gov/articles/PMC319275/)
(1981), presents the involution-principle route to partition bijections.
It is relevant prior art for rerouting; abstract inspection does not prove
that this particular new restricted encoding is new or equivalent.

The [canonical TODO](../TODO.md)
has the next action and its short session-start/natural-pause review rule.

## Reproduce the final restricted check

From this checkout with Python3.11+, using the exact saved H3 repository:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 research/rogers-ramanujan/fiber-splitting-20261025/check_y4.py \
  --h3-root /private/tmp/yamba-ai-math-phase2-review-20261025 \
  --output /private/tmp/kr1-fiber-check-repeat.json
```

No claim of a self-contained replacement for that baseline is made. Its
commit identity is given above; restore that checkout before replay if it
has been removed. Do not accidentally substitute Argon's other bridge.
The [illustration](fiber-progress.png) is explanatory, not proof evidence.
