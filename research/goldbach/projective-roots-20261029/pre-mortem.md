# Supplemental pre-mortem for the joint root count

29 October 2026. Distinct critic's preparatory check, based only on `brief.md` and earlier reviewed arithmetic. The author's actual statement and proof were not read for this document. This is a separate supplemental dispatch, not execution or acceptance of the main critic stage.

## The proposed local density is plausible under the stated hypotheses

For p coprime to H, a matrix of determinant H modulo p has a nonzero first row. For each such row there are p choices of its second row giving determinant H. A fixed first-row kernel line permits p-1 nonzero row multiples, hence p(p-1) determinant-H matrices out of p(p^2-1). Its complete local density is therefore 1/(p+1).

This argument includes zero entries. The horizontal kernel span(1,0) means u=0 and c_H!=0 modulo p; the determinant then forces v!=0. The vertical kernel span(0,1) means c_H=0 and u!=0, with d_H!=0. Other lines require both first-row entries nonzero. Invertibility of the matrix does not mean all its entries are units.

These complete local counts are compatible with a product of 1/(p+1) and the existing both-unit H density, since the prescribed primes are coprime to H. They do not prove that the canonical complement c_H in [0,u) is jointly distributed with the original coordinates and its real ratio interval. That requires the author's actual incomplete inverse-count argument.

## Small omitted-hypothesis witnesses

1. A proof imposing gcd(u,S)=1 without treating the omitted case loses real prescribed lines. Take H=2, S=3, u=3, v=5. The canonical complement is c_H=2 and d_H=4, giving determinant 2 and first row (0,2) modulo 3. Its kernel is the horizontal line. Both original coordinates are units modulo H and the position is primitive. Thus the u-nonunit case at a prescribed prime is legitimate and cannot be discarded by dividing u modulo S.
2. Coprimality of S and H is essential to the proposed universal line density. If H=3 and S=3, the required u-unit condition forbids u=0 modulo 3. The horizontal kernel is therefore impossible, although a formula assigning it density 1/4 would predict a positive full-interval main term. For an even-target version use H=6, S=3. These examples concern a dropped hypothesis, not the candidate as stated.
3. Arbitrary real intervals cannot support a uniform relative asymptotic without a minimum-main-mass condition. For u>=2 and gcd(u,H)=1, the canonical complement cannot be zero: zero would require u|H. Hence c_H/u>=1/(16U). The interval [0,1/(32U)) contains no ratios at all, while its proposed unfiltered main term is positive and of order V. Such a witness is compatible with a sufficiently large absolute error and does not refute that kind of estimate. It does rule out unconditional relative normalization for every shrinking interval.

## Error-range obligations

The preceding elementary three-quarter Kloosterman completion naturally gives an aggregate error of shape U^(7/4+eta) times subpower and logarithmic factors. Dividing by the position scale UV requires V>U^(3/4) with fixed exponent slack for a power saving. The brief's broad lower and upper polynomial bounds on U,V alone do not imply that aspect condition. An argument using only that completion must retain its actual aspect range, or supply a separate estimate for the complementary range. Failure of this available error to save is not a proof that the true joint count fails there.

The proof must also retain all squarefree divisors of H, including empty residual intervals, and track a possible common-factor frequency cost. Since those divisors and H are units modulo an admitted u, they may simplify a coefficient gcd, but they do not make incomplete sums with different coefficients identical. Prescribed-line completion adds a modulus and frequencies whose full S dependence must be explicit.

Subpolynomial S and radical-divisor factors are eventually subpower in X, uniformly under the brief's polynomial H bound. This only turns an already proved fixed negative power into a useful absolute saving. It does not manufacture that negative power, justify arbitrary aspect ratios, or make an empty thin prescribed population safe to normalize.

## Conditions a successful proof must preserve

The actual proof must check the horizontal and vertical line cases separately; derive the canonical c_H congruences without assuming every row entry is invertible; include zero completed frequencies and their Ramanujan or local main terms; retain consistent endpoint conventions; and state an absolute error before discussing relative asymptotics. Its line density must be derived with the u/v unit restrictions and weighted phi average, rather than copied from a complete matrix count.

Even a successful unweighted joint root estimate would not supply prescribed high path moments, actual-prime cancellation, the changed denominator-H prime major term, or a Goldbach lower bound. No verdict on the forthcoming author argument is given in this preparatory document.
