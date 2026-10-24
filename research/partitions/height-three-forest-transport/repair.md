# P014 round two: digit repair and direct Hall verification

**Construction refuted if the retained neighborhood certificate verifies.**
Round one is complete: all four development cases passed representation,
comparison and inverse checks. The fork grammar diagnostically saturates both
size-seven cases and the new size-eight boundary case, but has a two-to-one
Hall deficiency on `h=(3,5,5,7,7,7,8,8)`. No P014 held-out case has been run.

The sole repair is exactly the predeclared maximum-insertion digit step:
change one digit by `+1` for epsilon one or `-1` for epsilon zero, reconstruct
the tree list, and toggle epsilon. All other coordinates, marks, component
sets and compositions stay fixed. Tom's insertion bijection gives validity
and exact inverse; the one-unit inversion change compensates for epsilon.
This remains a partial symmetric relation, with no universal selector claim.

The two negative Hall states are

```text
h            = (3,5,5,7,7,7,8,8)
parents      = (3,5,4,6,7,0,8,0)
compositions = ((1,3),(4)) or ((3,1),(4))
marks        = (1,1)
epsilon      = 0
inversion    = degree = 3
```

Their component words `1,3,4,6` and `2,5,7,8` are increasing, so all
insertion digits are zero. Marks are minimal as well. A degree-preserving
epsilon-zero step must decrease a digit or mark, which is impossible.
Therefore the repair adds no neighbor to either state. If the old complete
neighborhood is the one recorded positive state, the same Hall deficiency
persists in the repaired grammar without any large search.

Round two will verify precisely that finite certificate, under a fresh copy
of the same resource limits. It will rebuild the recorded states, check the
actual full signed type/statistic, enumerate every old and repaired primitive
from the two negatives, compare the union with the advertised positive set,
verify inverse membership and check `2>1`. It will not repeat complete
development enumeration, lock a selector, run held-out cases or count any
unrun case as a success. This is a narrower falsification than the originally
possible full second search, justified by the already decisive certificate.
The two fresh held-out vectors remain untested and unexposed by outcomes.

The verifier is an engineering addition to the executed round-one source;
the mathematical grammar, development data and single permitted repair are
unchanged. Preserve the round-one source snapshot and receipt. A new frozen
round-two verification specification pins that receipt before the check.
No third repair or substantial Lean work follows a verified deficiency.
