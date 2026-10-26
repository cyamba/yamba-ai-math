# Argon rerouting proposals: exact failures and a capacity obstruction

Date: 2026-10-26. Source: the user-provided Argon PDF, especially pages 3 to 6
and 9 to 15. Literal implementation audited: `rr004_multidim_cones.py` at
research base `2ccf9c5`. Novelty is not verified.

## Verdict

Argon's distinct-head cone idea is a valid coordinate device for a selected
family once the required head assignments and exclusions are proved. It does
not yield a general KR1 map. The advertised surgical changes collide with
existing higher-sector images at weights 25 or 31, before the known weight-41
obstruction. This failure persists even if cone validity and exclusion from
all lower-sector images are proved.

The script [probe_repair.py](probe_repair.py) checks the following explicit
witnesses without modifying any current maps. Its passing status means the
proposed preservation repairs are refuted, not that a KR1 bijection passed.

## Five occupied proposed destinations

Write a cluster as `(a,b,mu,nu)`. Each row has distinct proposed and existing
sources of the displayed common weight. The candidate target is a valid U
partition, and the unchanged current reconstruction of the existing source
is exactly that target.

| Proposed source | Proposed new target | Existing source already owning target | Weight |
| --- | --- | --- | --- |
| `(5,0,(0,1,1,2,2),())` | `(10,9,9,3)` | `(4,0,(0,0,5,10),())` | 31 |
| `(5,0,(0,1,1,2,2),())` | `(9,8,8,6)` | `(3,1,(0,2,2),(2,))` | 31 |
| `(5,0,(0,0,0,0,0),())` | `(9,8,8)` | `(4,0,(0,3,3,3),())` | 25 |
| `(5,0,(0,1,1,5,5),())` | `(10,10,9,8)` | `(4,0,(2,5,7,7),())` | 37 |
| `(5,0,(0,1,2,6,7),())` | `(10,10,9,9,3)` | `(3,1,(1,2,2),(5,))` | 41 |

Thus retaining all existing other assignments while installing any listed
proposal fails injectivity. This does not rule out a coordinated remapping
of a larger family, but such a remapping needs a fresh global proof.

There is also a source-transcription error on PDF page 3. The literal table
maps the apex `(5,0,(0,1,1,2,2),())` to `(18,10,3)`, not `(19,12)`. The old
operator trace then sends this to `(19,12,6)`, `(19,12,6,3)`, and finally the
known weight-41 collision `(19,12,6,3,1)`.

## Theorem 1: offsets cannot separate two full octants sharing a head

Fix a head multiplicity tuple `(z,y,x)`. For any two tail offsets
`alpha,beta` in N^3, the full translated tail octants

`alpha + N^3` and `beta + N^3`

intersect. Consequently, assigning different base tail offsets to two source
apexes with the same head cannot make their *full unbounded* increment
images disjoint.

**Proof.** Let `gamma_i=max(alpha_i,beta_i)` coordinatewise. Then
`gamma-alpha` and `gamma-beta` belong to N^3, so `gamma` belongs to both
translated octants. Because the six allowed column values are distinct,
the two resulting column partitions are identical. Distinct source apexes
remain distinct source clusters, so a claimed injection fails. This proves
the statement. It does not exclude restricted or partitioned tail domains.

## Theorem 2: the proposed unique-head compiler is impossible by weight 55

Consider all head labels `(z,y,x)` with `0<=z<=3`, `y` in `{1,2}`, `x>=0`,
and `x+z>=1`. A candidate target is

`(10^z,9^y,8^x,6^c6,3^c3,1^c1)`.

If `x=0`, require a positive tail `c6+c3+c1>=1`. Suppose each higher-sector
cluster apex gets a distinct head label, with a nonnegative tail offset,
and the assigned target has the same weight as that apex. Then no such
assignment exists even for all apexes of weight at most 55 in the single
source sector `a=3,b=2`.

**Proof.** The relevant apex subfamily is

`A(r,u,v)=(3,2,(0,r,r),(u,v))`,

where `r` belongs to `{0,1,2}` and `0<=u<=v`. These are indeed octant apexes:
`d1=d3=q2=0`, and the residual difference is `r`. Their weights are

`wt(A)=39+2r+3(u+v)`.

At weight at most 55 there are 12 choices `(u,v)` for `r=0` (sum at most 5),
9 for `r=1` (sum at most 4), and 9 for `r=2` (sum at most 4), giving 30
distinct source apexes. In general the number of ascending pairs of sum
at most `s` is `sum_{t=0}^s (floor(t/2)+1)`, giving those exact counts.

For `x>=1`, the number of head labels with weight at most 55 is

`sum_{z=0}^3 sum_{y=1}^2 max(0,floor((55-10z-9y)/8)) = 23`.

For `x=0`, there are six additional labels (`z=1,2,3` and `y=1,2`), all
admitting minimum positive tail weight 1 at this bound. Thus there are only
29 head labels that could possibly support a target of weight at most 55.
This count generously includes heads reserved by every other sector.
Nonnegative tail offsets cannot reduce head weight. A weight-preserving
assignment of the 30 apexes into these 29 labels contradicts the pigeonhole
principle. This proves the theorem.

By Theorem 1, allowing two of these apexes to reuse a head with different
base tail offsets does not fix the proposed full-octant compiler. This is
an obstruction to that precise compiler architecture, not to general KR1
bijections or to more elaborate partitions of a head's tail domain.

The parent investigation additionally develops a stronger fixed-alphabet
capacity theorem. I independently checked its proposed witness: the `2^k`
ascending vectors with binary successive differences, at `a=3,b=k,mu=0`,
are distinct source apexes of weight at most
`M(k)=(9k^2+21k+18)/2`. For `k=128`, `M=75081` and
`2^128 > 75082^6`. Thus even the much larger collection of all partitions
on six fixed positive column values has insufficient cumulative capacity
for all source apexes. The complete general proof is recorded separately
by the parent investigation.

## Other limitations in the supplied argument

- Exact U validity requires the terminal decoded height to be **less than
  5**, not merely nonzero modulo 5. Within the proposed cone, the positive
  shorter tail does force terminal height in `{1,2,3,4}`, so this particular
  argument can be repaired. The general invariant stated in the PDF is too
  weak.
- Counting six symbols in an ordinary input tuple takes linear time in its
  length. Argon's inverse is not O(1) for that representation. It can be
  constant time only when six multiplicities are already supplied.
- The elementary modulo-9 head-weight identity is correct. It provides
  neither a head assignment nor coverage/injectivity of a global map.
- Disjointness from lower sectors and the special `a=3,b=0` sector does not
  imply disjointness from all remaining higher sectors, as the table shows.
- The parent investigation's cone proof author audits membership and
  lower-image exclusion separately. None of this note assumes its result.

## Reproduce

From the repository root:

```sh
python3 research/partitions/argon-2026-10-26/probe_repair.py
```

The [saved report](repair_probe.json) records exact witnesses and counts.
Only explicit candidate targets and a small head/source count at weight 55
are checked; no broad KR1 enumeration or altered construction is used.
