# RR003 recursive extension: arbitrary ones with a separated core

**Proposed proved restricted theorem, author-only assurance.** This extends
the frozen zero/one/two-one repair inside mechanism B. It adds a concrete
infinite arbitrary-multiplicity family; it does not solve arbitrary residue
part insertion or receive a third critic challenge. Established Glaisher
and the attributed cluster endpoint retain their credits. Novelty is
unverified, and full KR1 success remains absent.

## Actual domain, forward rule and inverse

Keep all earlier small-charge inputs. Also accept three ones with empty
core. For t>=4 ones, let C=(a,b,mu,nu) be the intrinsic cluster data of the
three-divisible Glaisher core. Accept when mu is empty or mu_1>=t, and
nu is empty or nu_1>=2. These are explicit separation hypotheses, not
assumed properties of every source core. Map this source to

    C'=(a+2,b,(0,t-4,mu_1-4,...,mu_a-4),nu-(2,...,2))

and merge to the gap partition. All vectors are ascending and nonnegative:
mu_1-4>=t-4>=0 and nu_1-2>=0. Empty lists and equality are allowed.
Three ones with empty core map to (1,2).

Inverse: first try the frozen small-charge inverse; then recognize (1,2)
as three ones. Otherwise require a'>=2 and mu'_1=0. Recover

    t=mu'_2+4,
    C=(a'-2,b,mu'_(3:)+4,nu'+2).

Merge this C and require every part to be divisible by three. Inverse
Glaisher recovers the core residue partition; prepend t ones. Failed
intrinsic recognition is unsupported, not a fallback to enumeration.

## Universal proof and image separation

Adding two singleton coordinates changes Q by 4a+6b+4. The mu change is
t-4-4a, and the change in 3|nu| is -6b. The total change is exactly t.
Validity and termination follow from literal C validity and the proved
cluster merge. The inverse takes the first two coordinates, which are
intrinsically distinguished even when equal zeros occur; removing two
entries from a sorted sequence leaves exactly the original tail.
Adding four and two restores the original vectors. Conversely the
recognized inverse automatically meets mu_min>=t and nu_min>=2; its
all-three check is precisely the source-core condition. Thus both inverse
identities and weight preservation hold for arbitrary size in this domain.

The new image has a'>=2 and mu'_1=0. Every old small-charge image with
at least two singles has minimum mu at least two, since its core is
three-divisible and only its last coordinate was raised. Old images
arising from a=0 have just one single. The t=0 image is three-divisible,
whose nonempty mu has minimum at least two. The three-one empty-core
image (1,2) has no singles and a non-three pair; it is in none of these
other images. Therefore all branches are disjoint. No image assignment
from the earlier successful restricted repair was changed.

This covers the all-ones axis for every t. It also covers unbounded a,b
and t with nonempty cores: start with the all-parameter three-divisible
family in three-divisible-foothold.md and translate every part upward by
3s. This changes mu by +3s and nu by +2s. Taking s large enough ensures
the displayed separation hypotheses for any prescribed t>=4.
The construction's conservative bit-work and auxiliary-space bounds stay
quadratic in unary weight N; the complete-map complexity is still unknown.

## Precise obstruction to the tempting unrestricted rule

An alternative would add only one singleton, insert t-1 anywhere in the
sorted vector mu-2 and subtract one from nu, whose entries are large enough
for every three-divisible core. Its cost is t, but charge recovery fails:
core (6),t=1 and core (3),t=4 both give C'=(2,0,(0,3),()) and gap (1,6).
The residue sources are (1,6) and (1,1,1,1,3), of weight seven. This is an
exact algebraic collision, not a swept computational assertion. The fixed
second coordinate in the separated-core rule retains t and avoids that
particular ambiguity. It does not prove that the separation hypotheses
can simply be removed. The earlier cost-three two-branch collision at
weight nine remains preserved in third-one-obstruction.md.

## Next lemma and learning

Unresolved: mixed cores with t>=3 outside these hypotheses, especially a
first mu smaller than t or a first nu equal to one, and all larger residue
parts congruent to one or eight modulo nine. A complete recursive adapter
must cover them disjointly and recover the branch without a transcript.
The leading U–C global decomposition is still an alternative route; none
of these partial constructions is declared the governing objective.

Decisive obligation proved here: store an arbitrary charge count in an
intrinsic coordinate while preserving core data and old images. The next
step is to challenge the boundary cases rather than erase the hypotheses.
Workflow hypothesis, **unvalidated**: allocating a recoverable coordinate
can prevent information loss exposed by a simpler insertion, at the cost
of a narrower structural domain. No general discovery-rate claim follows.
