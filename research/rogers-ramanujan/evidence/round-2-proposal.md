# RR002 round 2 — frozen local column straightening candidate

Author: root/mathematician. Status: **conjecture** for injectivity; no
inverse or full bridge is claimed. Frozen before automated tests of this
candidate. Hand calculations at N<=8 informed its design; weights 9..30
are the next falsification interval, not previously evaluated for it.

## Exact algorithm R2

Input W is first encoded losslessly as U: conjugate column heights h,
then F(5q+r)=9q+s_r with s=(0,1,3,6,8). Sort U ascending to get p.
Empty input returns empty. Keep the total N fixed throughout.

Repeat, with the following strict priority:

1. Scan adjacent pairs left to right for the first (x,y) with y-x<=1
   and (x+y)%3 !=0. If (x+y)%9 belongs to {1,3,6,8}, replace this pair
   by (x-1,y+1); otherwise replace it by the singleton (x+y).
2. Only if no bad pair exists, scan triples left to right for the first
   (x,y,z) with z-x<=2. If y=z, replace it by (x-1,y-1,z+2), deleting
   zero entries. Otherwise replace it by (x,y+z).
3. Sort ascending after each replacement and restart with step 1.
4. If neither defect exists, return p.

No global family enumeration, ranking, arbitrary tie choice, history
field or counting identity enters this algorithm. It is defined by a
fixed finite set of arithmetic rules and one residue guard.
Default execution retains only the current partition and a step count.
Optional full traces are diagnostic evidence outside the proposed map's
quadratic-space implementation; their measured storage is counted in
the experiment budget. This instrumentation distinction does not alter
the rewrite rules or their priority.

## Universal partial argument to be reviewed

Every update preserves the total. A pair spread never has x=1: the only
possible defective pair beginning with one is (1,1), whose sum two does
not take that branch. Triple spreading deletes zeros explicitly.

Let E(p)=sum(p_i^2). Pair merging raises E by 2xy; pair spreading by
2(y-x)+2; merging the last two triple entries by 2yz; equal-top triple
spreading by 2(y-x)+6. These are positive. Since E<=N^2, the algorithm
terminates in at most N^2/2 rewrites. When it stops, the literal A
conditions hold. Sorting and full scans must be charged; a unary
implementation fits the contracted quartic work/quadratic space target.

Thus the candidate is a total weight-preserving W->A normalization if
this argument is sound. **Injectivity and a recoverable inverse remain
the decisive unproved obligations.** The known A<->C parametrization
would turn a successful new W<->A construction into the required W<->C
bridge; it must not be assumed to repair any collision in R2.

## Acceptance and rejection

Enumerate the actual W and A sets independently. Check every image,
weight, collisions and missing images through N=30. Retain the smallest
failing fibre with its exact two traces. A collision refutes R2 and every
deterministic composition through its output, but not the whole finite
local-rule class. Finite success alone cannot accept R2 as a bijection:
an explicit inverse and a universal argument are still required.

## Recorded first falsifier and frozen finite-family extension

The first automated check refuted the exact algorithm above at N=8:
W=(4,2) and W=(8) both reach A=(3,5). The first input's U is (3,3,1,1).
In ascending order, (1,1,3,3)->(2,3,3)->(3,5): the defective pair (2,3)
has priority over the plateau triple. The second input passes through
(4,4), which spreads to the same result. This invalidates the proposed
inverse, despite a strict energy measure.

Before a second-family run, freeze the following **16** profiles. Four
Boolean switches specify the entire family; there are no learned tables
or further choices after evaluation:

* `plateau_first`: if true, process the leftmost defective triple with
  y=z before any bad pair; otherwise retain the original pair-first
  priority. Fallback after pairs is always the leftmost bad triple.
* `residue_guard`: if true, retain conditional pair spreading; otherwise
  merge every defective pair.
* `plateau_spread`: if true, retain (x-1,y-1,z+2) for y=z; otherwise
  replace that triple by (x,y+z).
* `merge_upper`: for y!=z, choose (x,y+z) if true, or (x+y,z) if false.

Switch order in profile IDs is the order above. The original R2 is
`0111`. Profiles 0000..1111 are each specified by the same finite program;
the choice is not input-dependent. Every allowed update has the same
strict energy increase (lower-pair merging adds 2xy), so totality and
weight preservation have the same proposed universal argument.

This extension is exploration **inside the second author proposal
stage**, before its critic dispatch. It is informed by the stated N=8
failure; it is not an independent held-out replication of the original
proposal. Freeze all profiles before testing any of them. A profile with
no counterexample through thirty remains unproved. Refuting all sixteen
needs an exact witness for each; it does not refute unlisted priorities,
other arithmetic updates or a general structural bridge.

This is the last construction review round under RR002. Do not start a
third review/repair round or a full Lean/exposition increment if it fails.
