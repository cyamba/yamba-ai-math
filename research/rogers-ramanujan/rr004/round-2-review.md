# RR004 round-two separate semantic review

**Verdict: supported**, for the strengthened finite injection obstruction.
Reviewed 2026-10-24; completed 15:44 UTC (17:44 Stockholm), within the
10-minute second-review allocation. This is the final authorized critic
round, using the same separate `rr004_critic` profile. No subagents,
external retrieval, providers, dependencies or external messages were used.

## Exact statement and assurance

Let S be the fourteen distinct literal U objects in the frozen proposal:
`(1)`, `(1,1)`, `(1,1,1)`, `(3)`, `(3,1)`, `(3,3)`, `(3,3,3)`,
`(1^7)`, `(3,1^4)`, `(3,3,1)`, `(6,1)`, `(6,1,1,1)`, `(6,3)`,
and `(6,3,1)`. Their largest weight is ten; decoded heights are in
`{1,2,3}`, with valid ordering, repeated heights and terminal drops.
C has nonnegative integer `a,b`, ascending nonnegative vectors of exact
lengths `a,b`, and weight `a^2+3ab+3b^2+|mu|+3|nu|`.

**Proved, separate written semantic review; not formally certified:**
there exist no weight-preserving injection `Phi:S -> C` and fixed real
signed height-transition charges whose sum, including repetitions and
the terminal transition to zero, is the b coordinate of every `Phi(U)`.
The statement also excludes an added initial-height potential absorbed
by telescoping. It does not exclude contextual or multiplicity-dependent
statistics or general U-C decompositions.

## Logical audit

The proof is complete without the first-round asymptotic diagonal lemma.
Its finite diagonal deductions are valid. At weights one and two every
C has b=0; the sources `(1)` and `(1,1)` therefore give `e(1,0)=0` and
`e(1,1)=0`. At weight three, `(1,1,1)` occupies the sole b=0 target,
forcing `e(2,0)=1`. At weight four, `(3,1)` forces `e(2,1)=0`.
At weight six, `(3,3)` has b=`e(2,2)+1`, an integer in `{0,1}`,
so the real charge `e(2,2)` is exactly -1 or 0. The former makes
`(3,3,3)` have b=-1 at weight nine; hence `e(2,2)=0`.

At weight seven the three listed b=0 sources are distinct and saturate
all three actual b=0 targets. Injectivity alone forces `(6,1)` to use
the sole b=1 target, so `e(3,1)=1`. At weight nine `(3,3,3)` and
`(6,1,1,1)` are distinct b=1 sources and saturate the only two targets
with positive b. Thus `(6,3)` has b=0, forcing `e(3,2)=-1`.
The literal source `(6,3,1)` then has b=-1, contradiction.

These are capacity arguments within individual weights, requiring no
surjectivity, equality of global U/C counts or assignments to the rest
of U. Nonnegativity and integrality of actual C coordinates justify each
case split. No RR003 author-only component is a premise.

## Findings (no blocking defects; no mathematical disagreement)

1. **Supported scope; informational boundary.** The finite proof is strictly
   stronger than the first claim with respect to the required source and
   injection hypotheses. It excludes the specified fixed statistic, with
   no need for arbitrary repetition counts. The proposal correctly makes
   no claim of a minimal witness set, weight threshold or broader
   impossibility. Such claims would require new proofs.
2. **Supported assurance; informational boundary.** This is a reviewed
   impossibility argument for one recovery mechanism. It supplies no U-C
   maps, full KR1 endpoint composition, universal constructive bijection,
   formal proof certificate or novelty evidence. These boundaries are
   accurately stated in the proposal and executable certificate.

## Independent finite validation

All **nine** source hashes in `round-2-freeze.json` matched. The independent
script imports no author math/check module. It regenerates actual C
vectors directly from their definition and validates every source's height
transitions. The computed b capacities `(b=0,b=1)` are:
`1:(1,0)`, `2:(1,0)`, `3:(1,1)`, `4:(2,0)`, `6:(3,1)`,
`7:(3,1)`, `9:(5,2)`, `10:(6,2)`.

As a second check beyond transcribing the written deductions, it forms
the seven-transition incidence matrix of all fourteen sources. It
exhaustively considers their **2,048** possible integer b assignments,
retains the **224** assignments satisfying literal target capacities,
and uses exact `Fraction` Gaussian elimination. **Zero** retained
assignments admit real charges. Exact rational elimination is sufficient
because the linear coefficients and right-hand sides are rational:
real consistency and rational consistency coincide. This is a finite
algebraic supplement to the written semantic proof, not a floating-point
search, a formal proof-checker run or a complete KR1 acceptance test.

First command, retained with its failed script and receipt:

```sh
python3 research/rogers-ramanujan/checks/rr004_meter.py critic2-independent -- python3 .runs/rr004/critic2_independent.py
```

The first run exited 1 because the critic's auxiliary explicit formula
for `(3,1^4)` incorrectly included an extra `e(2,0)` term. This was a
critic-script transcription error, not a proposal defect. The independent
linear-consistency check had completed, but that run is not claimed as
passing. Its script and receipt remain unchanged.

Corrected command:

```sh
python3 research/rogers-ramanujan/checks/rr004_meter.py critic2-independent-v2 -- python3 .runs/rr004/critic2_independent_v2.py
```

The corrected diagnostic uses `e(2,1)+3*e(1,1)+e(1,0)`; the run passed,
exit 0. Script SHA-256:
`22852a6a758fd7c1d22fc24f2e131adddab795712c2704c31a4ea0e2b6f8612a`.
Successful output: `.runs/rr004/critic2-independent-result.json`;
receipt: `.runs/rr004/critic2-independent-v2.json`.
Failed receipt: `.runs/rr004/critic2-independent.json`.

Metered child elapsed: **0.10011483400012366 seconds** failed, then
**0.10201362500083633 seconds** passed; total second-review computation
**0.20212845900096 seconds**. Maximum recorded child RSS:
**19,349,504 bytes**. Shared cumulative computation after the successful
run: **15.400449917011429 seconds**, including the conservative setup
charge and other recorded runs. RSS is checked after execution, without
an OS reservation; model resource usage is not measurable by the meter.

## Remaining obligation

A context-sensitive intrinsic extraction/reconstruction must still
recover `a,b`, ordered zero-padded `mu,nu`, exact quadratic core weight,
disjoint exhaustive coverage, termination and both inverse identities.
This review supplies no selected global image for the omitted weight-nine
core. The complete original KR1 objective remains **unverified/unresolved**;
Lean certification and exposition remain subsequent obligations.
**Novelty status: NOT VERIFIED.** No further review round is authorized.
