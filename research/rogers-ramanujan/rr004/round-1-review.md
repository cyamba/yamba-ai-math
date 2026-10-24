# RR004 round-one separate semantic review

**Verdict: supported**, for the exact fixed-transition obstruction only.
Reviewed 2026-10-24; completed 15:39 UTC (17:39 Stockholm), within the
12-minute critic allocation. Reviewer is the distinct `rr004_critic` profile;
this separation does not guarantee independent model errors. No subagents,
external retrieval, providers, dependencies or external messages were used.

## Formal statement and assurance

Let U consist of descending tuples `(F(h_1),...,F(h_l))` with positive
integer heights, `h_(l+1)=0`, and `0 <= h_i-h_(i+1) < 5`, where
`F(5q+r)=9q+(0,1,3,6,8)[r]`. Include the empty tuple. Let C consist
of all `(a,b,mu,nu)` with nonnegative integer `a,b`, ascending
nonnegative vectors of exactly those lengths, and weight
`a^2+3ab+3b^2+|mu|+3|nu|`.

**Proved, separate written semantic review; not formally certified:**
there is no weight-preserving bijection U to C for which the second
coordinate satisfies `b(U)=sum_i e(h_i,h_(i+1))` for fixed arbitrary
real signed charges on allowed height transitions. Charges may depend
on full heights and include repetitions and the terminal transition,
but cannot depend on index, total weight or other input context.

The frozen argument is complete for that statement. For every positive
height h, the unit-step path `h,h-1,...,1,0` gives a valid source. Repeating
the initial h adds `m*F(h)` weight and `m*e(h,h)` pair count. Actual target
coordinates satisfy `0 <= b <= sqrt(N/3)`. Since `F(h)>0`, either sign of
a nonzero diagonal charge violates one bound for sufficiently large m;
thus all diagonal charges are zero. This universal argument, rather than
a finite sweep, is essential.

At weights 1, 3 and 4, the literal fibers then force respectively
`e(1,0)=0`, `e(2,0)=1`, and `e(2,1)=0`. The complete four-object U
fiber at weight 7 has three objects already assigned b=0, while C has
exactly one positive-b object. Therefore `e(3,1)=1`. At weight 9, the
objects `(3,3,3)` and `(6,1,1,1)` already occupy the only two positive-b
targets; hence `(6,3)` has b=0 and `e(3,2)=-1`. The valid source
`(6,3,1)` then has b=-1, contradiction. Each use of target multiplicity
is licensed by weight preservation plus bijectivity on the finite weight
fiber. No global counting identity is assumed.

## Findings (no blocking defects)

1. **Supported claim; informational scope restriction.** The contradiction
   excludes the exact fixed transition-additive statistic and also an added
   initial-height potential. Indeed, with `p(0)=0`, its telescoping
   differences can be absorbed into the charges. It does not exclude
   context, multiplicity, marking, lookahead or other nonlocal recovery.
   The proposal states these restrictions correctly. A claim excluding
   general U-C decompositions would require a different argument.
2. **Supported assurance; informational evidence boundary.** The frozen
   script and the independent regeneration below check executable finite
   transcriptions. Neither is a bijection implementation, a proof of the
   universal diagonal lemma, a completed KR1 pilot, or evidence of novelty.
   The proposal maintains these boundaries correctly. Lean certification,
   endpoint composition and the full original KR1 proof gate remain open.

## Independent checks and resources

Read the contract, frozen proposal, freeze manifest, author verifier and
meter, together with the governing role and audit instructions. All four
source SHA-256 hashes in `round-1-freeze.json` matched their frozen values.
No RR003 author-only mathematical component was used as a premise.

Independent script `.runs/rr004/critic1_independent.py` imports no author
math/check module. It enumerates U directly by descending height paths
and C directly by the quadratic weight and exact-length ascending vectors.
It regenerated weights 0 through 12, checked empty/zero objects, every
small U list and positive-b C fiber used by the proof, both weight-nine
witnesses, the negative-b weight-ten witness and the omitted C core.
All passed. Descriptive `(U,C,positive-b C)` counts at proof weights:
`1:(1,1,0)`, `3:(2,2,1)`, `4:(2,2,0)`, `7:(4,4,1)`,
`9:(7,7,2)`, `10:(8,8,2)`.

Executed once from the canonical repository root:

```sh
python3 research/rogers-ramanujan/checks/rr004_meter.py critic1-independent -- python3 .runs/rr004/critic1_independent.py
```

Exit 0; metered child elapsed **0.04210837499704212 seconds**;
peak child RSS **18,120,704 bytes**. Shared cumulative computation after
this run: **15.14245904100244 seconds**, including the precharged setup
allowance. Meter receipt: `.runs/rr004/critic1-independent.json`;
full independent output: `.runs/rr004/critic1-independent-result.json`.
Script SHA-256:
`36f6346157dbe03541baa49df4c7576684f212d2f75e8d8db0b57a57e9837543`.
RSS is checked after execution, not reserved by the OS; model resources
are not measurable by this meter. No completion tests or engineering
checks are claimed by this semantic review.

## Remaining mathematical obligation

Construct and prove an intrinsically recoverable, context-sensitive U-C
decomposition with exact zero-padded coordinates, quadratic core weight,
disjoint exhaustive coverage, termination and both inverse identities.
The obstruction selects no global image for `(6,3)` or for
`(3,0,(0,0,0),())`. Complete KR1 remains **unverified/unresolved**;
novelty remains **NOT VERIFIED**.
