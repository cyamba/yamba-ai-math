# RR005 round one: intrinsic unit and triple chains

**Proposed proved structural reduction; separate review pending.** Complete
KR1 is unresolved. Novelty status: NOT VERIFIED. This is a U–C construction
attempt with a missing residual-root bijection, not a completed bridge.
Definitions are the literal RR002 U and C domains, including terminal drops,
empty input and exact-length zero-padded vectors. No RR003 author-only
endpoint or other premise is used.

## 1. Unit chains on U

Let R1_U append a column 1 and sort. This always stays in U: if nonempty,
the old bottom height was at most four, and inserting height one preserves
all drops. L1_U removes one 1 exactly when the result is literal U.
These are partial inverses, with weight changes +1 and -1.

The root domain D_U (no L1_U predecessor) consists exactly of:

* U with no ones, including empty;
* U with exactly one 1 whose smallest other column is 9.

Indeed, two ones permit removal; a sole one with no other column does too.
For a sole one with next decoded height h, validity gives h<=5 and removal
is forbidden exactly when h=5, that is, the next column is 9.

Repeated L1_U lowers weight and gives a unique D_U root plus count n1.
Applying R1_U n1 times reconstructs the original, without a saved trace.

## 2. Unit chains on C

Define R1_C by these disjoint exhaustive cases:

1. a>0: increase only mu's last entry by one.
2. a=b=0: return (1,0,(0,),()).
3. a=0,b>0,nu_1>=1: return (1,b,(0,),nu-(1,...,1)).
4. a=0,b>0,nu_1=0: return (2,b-1,(0,0),nu_(2:)).

All vectors remain ascending and nonnegative. Cases 2–3 give a=1,mu=0;
case 4 gives a=2,mu=(0,0); case 1 gives a last mu strictly greater than
its predecessor (use predecessor zero for a=1). Thus their images are
disjoint. The inverse L1_C lowers a strictly excessive last mu; otherwise
it sends a=1,mu=0 to (0,b,(),nu+1), including b=0; or sends a=2,mu=00
to (0,b+1,(),(0,nu)). Other C have no predecessor.

Case 3 changes Q by 3b+1 and 3|nu| by -3b. In case 4,
Q(2,b-1)=3b^2+1 and the removed nu entry is zero. Cases 1–2 are immediate.
Every R1_C therefore adds one, and the displayed inverses recover all
coordinates exactly, including zero padding.

The root domain D_C is exactly:

* a=0, arbitrary b,nu;
* a=2, mu=(k,k), k>=1, arbitrary b,nu;
* a>=3, mu's final two entries equal, arbitrary b,nu.

Repeated L1_C terminates by weight and yields a unique root and n1.

## 3. Triple chains on D_U

Define R3_U on the whole D_U:

* On a root with no ones, append a column 3.
* On a root with one 1 and smallest other column 9, replace one 9 and
  the 1 by 10 and 3, and sort.

Both branches add three and produce D_U objects with no ones. Appending
height two preserves drops because the old bottom height was <=4.
In the second branch, heights 5 and 1 are replaced by 6 and 2. Any height
above the removed 5 is at most 9, or an intervening height 6 already exists.
Inserting 6 subdivides a valid gap or raises the top by one; removing the
last 5 leaves a bottom gap 6-2=4. If another 5 remains the gap is smaller.
No terminal gap exceeds four.

Intrinsic inverse L3_U: for a D_U object with no ones and at least one 3,
first remove one 3 if the result is literal U. Otherwise try replacing one
10 and one 3 by 9 and 1, accepting exactly when the result belongs to D_U.
If neither test succeeds there is no predecessor. This is at most two
literal tests, not a search or a transcript. The second case's image has
exactly one 3 and all other heights >=5; removing the 3 has invalid
terminal height. Hence it cannot overlap the first case. Reversing its
replacement recovers exactly the original multiplicities. Conversely each
accepted inverse reconstructs the original by its specified forward branch.
Inputs with a one cannot be images. Thus both inverse identities hold on
the stated images, and R3_U is total and injective on D_U.

## 4. Triple chains on D_C

Define R3_C by these disjoint domain cases:

1. a=b=0: return (0,1,(),(0,)).
2. b>0 (any allowed a): increase only nu's last entry by one.
3. b=0,a=2,mu=(k,k),k>=1: return (3,0,(0,k-1,k-1),()).
4. b=0,a>=3: increase the last three mu entries by one.

These cases exhaust D_C. They preserve its conditions, add three and
remain literal C. The only non-immediate weight calculation is case 3:
9+2(k-1) = (4+2k)+3. Case 4 keeps ascending order and the final equality.

Images are disjoint. Case 1 is a=0,b=1,nu=0; case 2 has its last nu
strictly above the preceding one (zero when b=1); case 3 is a=3,b=0,
mu_1=0; case 4 has b=0,a>=3 and the first of its last three entries
strictly greater than the preceding entry (zero for a=3).

L3_C reverses precisely those tests: case 1 returns empty; case 2 lowers
the final nu; case 3 returns (2,0,(mu_2+1,mu_2+1),()); case 4 lowers
the final three mu entries. No other D_C object has a predecessor.
Both compositions recover every coordinate by these disjoint tests.

## 5. Universal normal forms and the missing bridge

Let E_U and E_C be the respective D domains with no L3 predecessor.
On either full domain, first strip L1 to its D root, then strip L3 to
its E root. Each successful step strictly lowers nonnegative weight.
Return (root,n1,n3). Reconstruction first applies R3 n3 times, then R1
n1 times. Partial-inverse identities prove both normal-form round trips
on the entire literal domains, not by equal counting. The exact weight is

    |input| = |root| + n1 + 3*n3.

A weight-preserving explicit bijection psi:E_U <-> E_C would therefore
supply a full U–C bijection by preserving n1,n3. **No such psi is supplied.**
The reduction is sufficient for a chain-respecting full construction; it
does not claim every possible KR1 bijection respects these chosen chains.
There is no proof that the residual problem is easier.

Source/destination root tests, R/L operations and normalization are intrinsic.
At most N successful lowers occur. Direct literal height validation and
sorting require at most O((N+1)^2 log(N+2)) bit work per step using simple
lists, giving a conservative quartic unary-work bound overall and quadratic
auxiliary bits. No diagnostic traces count as map output. Root matching's
complexity remains unknown.

## 6. A coherent infinite restricted correspondence

Choose only two root matches: empty <-> (0,0,(),()) and
(6) <-> (2,0,(1,1),()). Both are literal E roots of the same weight.
These are fixed structural base cases, not a lookup indexed by weight.
Their full chains are intrinsically disjoint by the normal-form theorem.
This defines a restricted bijection on all U consisting of ones and threes,
or ones and threes and exactly one six; the inverse accepts exactly the
two stated E_C roots after stripping. For t>=1,s>=0, in particular,

    U=(6,3^t,1^s) <-> (3,0,(t-1,t-1,t-1+s),()).

For t=0 the image is (2,0,(1,1+s),()). Thus (6,3) corresponds to the
previously omitted zero-increment a=3 core and (6,3,1) to mu=(0,0,1).
This is a proposed restricted map only, not a forced global matching.

These choices replace earlier partial assignments where they disagree;
they are not overlaid with them. For example (6,3,3) now lies on the
(6) chain and maps to a=3,mu=(1,1,1), whereas the RR003 restricted map
assigned it a=0,b=2,nu=0. No RR003 theorem is refuted by this alternative.

Smallest useful falsifiers: an R/L branch overlap, invalid terminal drop,
failure of a normal-form round trip, or a root accepted outside the two
declared matches. Full coverage already fails if any further E_U/E_C root
is left unsupported; the next task is a uniform root match, not more finite
coefficient agreement. Frozen tests are exposed implementation checks.

## Attribution and inspection

The exact U representation and C weight retain RR002's Andrews–Keith and
Kurşungöz attribution. These proofs use only literal definitions and
elementary arithmetic. No endpoint theorem or global counting identity is
a premise. On 2026-10-24 the author reinspected the statements of
[Andrews–Keith Theorem 6](https://arxiv.org/html/2203.05202v2) and
[Mizuno Theorem 1.1](https://arxiv.org/html/2609.09653v3); their full proofs
were not freshly audited. They do not establish the missing constructive
root match or its novelty. No Lean certificate has been run.
