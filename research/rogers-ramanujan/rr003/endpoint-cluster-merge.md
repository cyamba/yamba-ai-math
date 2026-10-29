# RR003 direct gap–cluster merge and universal author argument

**Proposed proved endpoint formulation; author-only assurance.** The gap–C
endpoint and cluster base are established in [Kurşungöz, Theorem 7](https://arxiv.org/html/1808.01432).
This direct merge is an independently derived expression of the endpoint,
not the missing U–C bridge. Its novelty and precise equivalence to all
source move descriptions are unverified. There is no additional critic
round: both scheduled challenges are already preserved. The preceding
obstacle interpreter remains frozen with its finite checks and unproved
conformance lemma; it is not silently promoted by this argument.

## Atom bounds

A close pair in a gap partition has form
P_(2r)=(3r+1,3r+2) or P_(2r+1)=(3r+3,3r+3), r>=0.
They cannot overlap: any three parts in overlapping close pairs lie in an
interval of length at most two, violating the distance-two rule. Splitting
all close pairs leaves an ordered word of singles and pairs. Singles are
at least two apart when consecutive. Put

    L(2r)=3r-1,       R(2r)=3r+4,
    L(2r+1)=3r,       R(2r+1)=3r+6.

A single s immediately before P_l is compatible exactly when s<=L(l);
a single immediately after is compatible exactly when s>=R(l).
Consecutive pair atoms P_l,P_m are compatible exactly when m>=l+2.
These statements follow by checking the adjacent sum and the two triples
straddling that boundary. Consecutive singles are compatible when separated
by at least two. All these atom conditions together imply the full gap
conditions: triples touching a pair are covered by its boundary, and triples
of singles span at least four. Also L(l+2)=L(l)+3,
R(l+2)=R(l)+3, each increment of L is one or two, and

    R(l)-3 = L(l+1)+1.

## Actual maps

For a literal gap partition read its atoms in increasing order. Let single
s_i have i earlier singles and q_i earlier pairs, numbering from zero.
Let pair P_(l_j) have j earlier pairs and z_j earlier singles. Define

    mu_i = s_i-3q_i-2i-1,
    nu_j = l_j-2j-z_j,
    a = number of singles, b = number of pairs.

For the reverse, consume the ascending nonnegative vectors mu,nu in their
order. With i singles and j pairs already emitted, the next potential
single value is S=mu_i+3j+2i+1, and the next potential pair level is
l=nu_j+2j+i. If one list is exhausted take from the other. Otherwise emit
the single exactly when S<=L(l+1); emit P_l otherwise. Increment the
respective counter and repeat. The decision is a literal formula; no
enumeration, matching, saved trace or hidden table is present.

## The inverse data are valid C

For successive singles with h intervening pairs, their value difference
is at least 3h+2. For h=0 this is their separation by two. For h>=1 use
the left bound at the first intervening pair, the right bound at the last,
R-L>=5, and levels rising by at least two between intervening pairs. Thus
mu_(i+1)-mu_i>=0. Before the first single, q pairs have levels at least
0,2,...,2q-2, so that single is at least 3q+1; hence mu_0>=0.

For successive pairs with h intervening singles, their level difference
is at least h+2. For h=0 this is the pair boundary. For h>=1 the singles
span at least 2(h-1), so L(m)-R(l)>=2h-2. If m-l<=h+1, the fact that each
increment of L is at most two and R(l)-L(l)>=5 would instead give
L(m)-R(l)<=2(h+1)-5=2h-3, a contradiction. Thus nu is ascending. If h
singles precede the first pair, L(l)>=2h-1, while L(l)<=2l-1 for l>=0;
therefore l>=h and nu_0>=0. Empty lists need no first-entry argument.
All vectors have the exact lengths a,b including zeros.

## The merge always returns a valid gap partition

Emitted levels are nonnegative. Successive singles are separated by
2+mu difference+3 times the intervening pair count, at least two.
Successive pair levels differ by 2+nu difference+the intervening single
count, at least two. For an adjacent single–pair boundary, the single's
selection rule immediately before that pair gives exactly s<=L(l).
For an adjacent pair–single boundary, the pair's selection rule was
S>L(l+1), where the eventual single has value S+3. By the displayed
identity this means S+3>=R(l). Thus every atom boundary is compatible.
All parts are positive, and the atom bounds prove full validity.

## Unique reconstruction, including nonadjacent competing atoms

Consider the atom word of any valid gap partition and its recovered C.
At any residual step suppose both types remain. If the next atom is a
single but the next pair occurs after h>=1 singles, its actual level is
l+h. The last of those singles is at least S+2(h-1), and is at most
L(l+h). Since L increases by at most two per level, this implies
S<=L(l+h)-2(h-1)<=L(l+1). The merge therefore selects the correct single.
If the next atom is a pair and the next single occurs after h>=1 pairs,
the single's actual value is S+3h and the last such pair has level at
least l+2(h-1). Its right bound yields
S+3h>=R(l)+3(h-1), hence S>=R(l)-3=L(l+1)+1. The merge correctly selects
the pair. Induction recovers the entire original word and values.
Conversely the merge's formulas make extraction return each given
coordinate of mu,nu exactly. These prove both inverse identities for every
weight, rather than assuming equality of generating functions.

## Weight, termination, cost and limitations

Every pair has weight 3(l_j+1). The extracted coordinates satisfy

    |mu| = sum_i s_i -3 sum_i q_i -a^2,
    3|nu| =3 sum_j l_j -3b(b-1)-3 sum_j z_j.

Every single–pair combination has exactly one order, so
sum_i q_i+sum_j z_j=ab. Substitution gives
|A|=a^2+3ab+3b^2+|mu|+3|nu| exactly. Extraction scans the input once.
Merge consumes one coordinate at every step and emits a single or pair,
so both algorithms terminate without an unbounded search. Arithmetic is
on O(log(N+2))-bit integers; literal validity checks and scans take
O((N+1)log(N+2)) bit work and O((N+1)log(N+2)) auxiliary bits, within the
preferred bounds. The formalization of this proof and separate semantic
review of this formulation remain outstanding. Its being an endpoint
cannot establish U–C coverage or a complete residue–gap bijection.

## Discovery, selection and learning

The useful change of representation is a sequence of intrinsic singles
and pairs with numerical boundary energies. Its advantage is a threshold
whose two branches are disjoint and exhaustive, and a closed inverse with
no moving-atom history. It is an endpoint expression inside the existing
cluster route, not a third candidate for the missing bridge. The original
complete KR1 objective and success criterion are unchanged.

Decisive obligation: prove the merge decision from nonadjacent next atoms,
not just verify adjacent move examples. The two inequalities above supply
that argument. Next justified step: freeze and verify literal maps, then
seek an equally intrinsic atomization on U. Workflow hypothesis,
**unvalidated**: deriving energy-adjusted coordinates from the inverse can
turn adjustment rules into a directly provable merge. No broader harness
success-rate claim follows.
