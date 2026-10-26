# A fixed finite column alphabet cannot carry all cluster apexes

**Status:** written proof, supported by [separate semantic review](review-round1.md). No Lean certification
or novelty claim. This concerns Argon's proposed fixed-support head compiler,
not the truth of the Kanade-Russell identity.

## Objects

A cluster is C=(a,b,mu,nu), where a,b are nonnegative integers and mu,nu are
ascending nonnegative integer tuples of lengths a,b. Its weight is

    wt(C)=a^2+3ab+3b^2+sum(mu)+3 sum(nu).

For a>=3 its octant coordinates are the last three successive mu differences,
with the middle difference decomposed as 3q+r. An apex has d1=d3=q=0.
This agrees with the literal reduction in rr004_multidim_cones.py.

Let S be any fixed finite set of positive integer column weights, |S|=m.
A target is a multiset of weights from S. Imposing the additional U-validity
conditions can only decrease the target count.

## Theorem

There is no weight-preserving injection from all cluster apexes with a>=3 into
multisets supported on S. Consequently no such injection exists from the full
higher-sector cluster domain. In particular, the six-weight support
S={1,3,6,8,9,10} cannot receive every apex, regardless of the head-registry
algorithm or allowed tail offsets.

## Proof

Fix k>=1. For each binary vector epsilon=(epsilon_1,...,epsilon_k), set

    a=3, b=k, mu=(0,0,0),
    nu_j=epsilon_1+...+epsilon_j  (1<=j<=k).

These are valid ascending increment tuples and apexes. The vector epsilon is
recovered by successive nu differences, so the construction gives 2^k distinct
apexes. Their weights satisfy

    wt(C)=9+9k+3k^2+3 sum_j nu_j
         <= M(k):=(9k^2+21k+18)/2,

because sum nu_j<=k(k+1)/2. The numerator is always even.

Every multiset supported on S and of weight at most M has each of its m
multiplicities between 0 and M. Thus there are at most (M+1)^m such targets.
A weight-preserving injection would force

    2^k <= (M(k)+1)^m

for every k. This is impossible. Here is an elementary quantified comparison:
M(k)+1<=25k^2 for k>=1. Set r=2m+1 and choose an integer
k>25^m r^r. Then k>=r and

    2^k >= binomial(k,r)
        = product_{i=0}^{r-1} (k-i)/(r-i)
        >= (k/r)^r
        > 25^m k^(2m)
        >= (M(k)+1)^m.

The product inequality follows from k>=r. The case m=0 is immediate because
positive-weight clusters have no target. This contradicts injectivity. QED.

## Explicit six-weight witness bound

Taking k=128 gives 2^128 distinct apexes of weights at most 75,081, while the
number of all six-weight target multisets up to that weight is at most

    75082^6 = 179149250616921445983301071424
             < 2^128
             = 340282366920938463463374607431768211456.

No enumeration of those 2^128 objects is needed. This is a finite pigeonhole
proof with exact integer arithmetic, rather than empirical growth evidence.

## Consequences and limits

Argon's distinct-head rule remains valid for a family that actually admits an
injective assignment to distinct heads with correct weights. What fails is the
proposed universal supply of such assignments in the fixed six-weight alphabet.
Even allowing multiple offsets per head cannot evade this cardinality bound.

An unrestricted construction must use a growing column alphabet, a different
representation or some other unbounded information capacity. The theorem does
not prohibit a general KR1 bijection into the actual U, whose column alphabet
is unbounded. It also does not invalidate any already proved restricted sector.
