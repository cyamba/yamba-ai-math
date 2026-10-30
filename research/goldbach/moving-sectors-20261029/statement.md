# Moving-target sectors: exact conjugacy and quantitative counts

29 October 2026. Registry role: Mathematician, `GOLDBACH-SECTORS-006`. This statement uses the populated harness packet and source survey. It gives two bounded candidate results: an exact finite-operator conjugacy, and elementary point-count/edge estimates after that conjugacy. Separate review is pending. No source cancellation theorem, Goldbach proof, breakthrough, or novelty claim is asserted.

The inspected [Lue-Wang-Wu equations (4.18)-(4.28)](https://arxiv.org/html/2610.20242v1) motivate the change of coordinates. Their full analytic theorem remains unverified as a dependency here. The proofs below establish their own finite identities, not a moving-target extension of that theorem.

## 1. Exact sector conjugacy for the whole centered kernel

Let H>=2 be an integer, eventually an even Goldbach target. Let Omega=[U,16U] times [V,2V], with U,V>0. First restrict to primitive integer positions P=(u,v) with gcd(u,H)=1. The residue

\[
c(P)=v u^{-1}\pmod H,\qquad0\le c<H
\]

is then well-defined. On the c sector define

\[
T_c(u,v)=\left(u,\frac{v-cu}{H}\right),\qquad
T_c^{-1}(u,w)=(u,cu+Hw).
\]

Its determinant is 1/H. Its image domain is exactly the parallelogram

\[
\Omega'_c=\{(u,w):U\le u\le16U,\ V\le cu+Hw\le2V\}. \tag{1}
\]

The map is a bijection from integer points in that sector to integer points in (1) with u coprime to H. Because gcd(u,H)=1,

\[
\gcd(u,cu+Hw)=\gcd(u,w),
\]

so primitivity is equivalent in both directions. Different sector images are kept as separate copies indexed by c; forgetting the sector index would lose the inverse map.

### The Fourier integral makes cross-sector blocks vanish

Let M1 be any measurable subset of the unit circle, and let e(x)=exp(2*pi*i*x). Define its full H-fold pullback

\[
M_H=\{\theta\in\mathbb R/\mathbb Z:H\theta\in M_1\}.
\]

For every integer k, splitting into the H inverse branches proves

\[
\boxed{\int_{M_H}e(k\theta)\,d\theta=
 \begin{cases}
 0,&H\nmid k,\\
 \displaystyle\int_{M_1}e((k/H)\phi)\,d\phi,&H\mid k.
 \end{cases}} \tag{2}
\]

Indeed the branch sum contains H^(-1)*sum_{j=0}^{H-1}e(jk/H). It is zero in the first case and one in the second. There is no extra 1/H factor in the second case, and meas(M_H)=meas(M1). Keeping only one inverse branch would invalidate the zero in (2).

For endpoints P=(u,v), Q=(u',v') and a common first-coordinate divisor D, set t=det(P,Q)/D, an integer. On the present restricted space D is automatically coprime to H. If the sector residues are c,c', write P'=T_cP and Q'=T_c'Q. Then

\[
t=H\frac{\det(P',Q')}{D}
                    +(c'-c)\frac{uu'}D. \tag{3}
\]

The integer uu'/D is a unit modulo H. Consequently H divides t exactly when c=c'. The exact edge condition t=H*(b-a) has no cross-sector edges. More significantly, its major-arc comparison

\[
\int_{M_H}e\big(\theta(t-H(b-a))\big)\,d\theta
\]

also vanishes whenever c differs from c', by (2). Thus the **whole centered bracket**, rather than just its exact-edge part, is block diagonal.

Inside one sector, t=H*t' with t'=det(P',Q')/D an integer, and the bracket becomes exactly

\[
\mathbf1_{t'=b-a}-\int_{M_1}e\big(\phi(t'-b+a)\big)\,d\phi. \tag{4}
\]

Choose the moving-target smooth cutoff as psi_H(t/Y)=psi_1(t/(H*Y)). It likewise becomes psi_1(t'/Y). This is an explicit definition of the candidate centered operator. If another analytic decomposition uses different arcs or a different cutoff, it must prove agreement with these choices before using the conjugacy. The arc pullback is not an imported arithmetic estimate.

This choice also changes the arithmetic major-arc problem. An arc around zero in M1 pulls back to arcs centered at every j/H, with widths divided by H. For j coprime to H their reduced denominator is H. More generally an arc centered at a/k pulls back to centers (a+j*k)/(H*k), whose reduced denominators can involve H. When H is of the ambient size, these are large-denominator arcs outside the inspected fixed-shift small-denominator regime. Equality of total measure is not an estimate for the prime exponential sums on them. Retaining the ordinary small-denominator arcs instead does not give the cross-sector zero in (2). Thus (6) concerns the deliberately defined pullback-centered operator, not a major-arc part already controlled for the original Goldbach calculation.

For example, with H=2, frequency k=1, and M1 a symmetric interval of radius eta<1/2, the complete pullback gives zero. Keeping only its branch around zero instead gives sin(pi*eta)/pi, which is nonzero. This tests why the full pullback is essential.

### Lists, measures, complements, and adjoints

Retain any finite first-coordinate prime-list admissibility, including shared D and unshared a,b, and all weights depending only on those lists and the first coordinates. The map changes neither first coordinate nor list. In particular a state measure sigma=product V_i^(-(J+1)), the source damping factor, list permutations, and the factors d0/D and eta(a/Y)eta(b/Y) are preserved exactly. List primes dividing H cannot occur in an admissible unit-first-coordinate state. The original normalizing V_i are retained; replacing them by group masses with those primes deleted would be a separate renormalization to account for.

On each sector the pullback of functions is an isometry for the discrete state measure. No Lebesgue Jacobian is inserted into a counting-space norm. If P has an integral complement C=(r,s) with u*s-v*r=1, then

\[
C'=(Hr,s-cr)
\]

is an integral complement to P'=T_cP. Thus their complement ratios satisfy

\[
r_{P'}=H r_P\pmod1. \tag{5}
\]

Good-state conditions for the moving operator must use H*r_P; they then agree exactly with coefficient-one conditions on P'. Multiplication by H preserves Haar measure on the circle, but this fact alone does not prove arithmetic equidistribution of complement ratios among the sector roots.

List symmetrization and these diagonal good-state projections preserve sectors. The unchanged state measures mean that adjoints still reverse transitions with the same joint list weight and conjugate the kernel. Combining (2)-(5) gives the exact unitary direct-sum identity

\[
\boxed{\mathcal U A_H^{\rm unit}\mathcal U^{-1}
       =\bigoplus_{c\ ({\rm mod}\ H)} A_{1,c}^{\Omega'_c,\rm unit-first}.} \tag{6}
\]

All factors and projections must be the ones just specified. Adjoint products and every finite moment transform by the same unitary. In particular the operator norm on the left is the maximum of the block norms, rather than their sum; there is no automatic H loss in (6). There is also no cancellation estimate in the identity.

### A justified both-coordinate restriction for a candidate Goldbach decomposition

For actual prime summands p<H, excluding p dividing H costs at most omega(H) counts, or omega(H)*log H with prime logarithmic weights. For von Mangoldt input, the total weight of powers with prime base dividing H is at most omega(H)*log H too. Multiplying the exact Vaughan decomposition by 1_(n,H)=1 is compatible with its multiplicative sums: every factor of a product coprime to H is itself coprime to H. The restrictions can be carried in the corresponding factor coefficients without an analytic assumption.

In such a deliberately restricted decomposition, the factors m,r,n,s are units modulo H. Every selected label dividing H-mn or H-rs is also a unit, since gcd(H-mn,H)=gcd(mn,H)=1. For the positions P=(Dbm,s), Q=(Dar,n), both coordinates are therefore units. Only c in (Z/H)^times occur. This is a derived property of that restricted construction, not a claim about arbitrary supplied coefficient arrays.

There is a useful primitivity check for original small labels. Suppose all list primes are below Z, all coefficient factors m,r,n,s are Z-rough and coprime to H, b>1, gcd(a,b)=1, and the nonzero centered kernel has |t/H|<=C*Y<Z. By (2), a nonzero centered bracket has H dividing t. If a prime ell divided both coordinates of P, it could not divide Db, because s is Z-rough. Hence ell divides m and s, ell>Z, and ell does not divide H. Since ell divides t, it then divides t/H. The size condition forces t=0. But t=bmn-ars=0 is impossible: b would divide a*r*s, whereas gcd(b,a*r*s)=1. Thus P is primitive; the same proof applies to Q. This establishes primitivity for these nonzero kernel terms without bounding H*(b-a) by Z.

This check uses the full centered support and original small-label/sift separation. It does not solve the polynomial-label problem from LABELS-005, where those labels exceed Z. Nor does it show that every other choice of comparison kernel has the same support.

### Geometry and discarded endpoints

The area of each parallelogram (1) is 15*U*V/H, and each vertical slice has width V/H. For 0<=c<H its smallest axis-parallel bounding rectangle has height (V+15*c*U)/H, with area ratio 1+15*c*U/V. Thus replacing thin sectors by bounding rectangles may create a large loss. The exact domain should be retained.

Positions with gcd(u,H)>1 are not covered by this map. Their mass need not be small in an arbitrary abstract state space. The small discarded prime-input cost above is available only if the coprimality restriction is carried through the actual multiplicative decomposition as stated. If that has not been done, (6) is a compressed-operator identity, not a statement about the full original Goldbach problem.

## 2. Quantitative counts and an actual post-conjugacy estimate

Here are elementary estimates, independent of any claimed source cancellation theorem. Let U,V>=2, B=min(16U,2V), and tau_H=2^omega(H). Define

\[
\kappa_u(H)=\frac1{\zeta(2)}\prod_{\ell\mid H}\frac{\ell}{\ell+1}.
\]

For each residue c modulo H, let N_c count primitive integer positions in Omega with gcd(u,H)=1 and v congruent to c*u modulo H. Equivalently it counts their transformed primitive positions in (1). Uniformly in H and c,

\[
\boxed{N_c=\frac{15UV}{H}\kappa_u(H)
 +O\left(\left(U+\frac{\tau_H V}{H}\right)\log(2B)
                    +B+\frac{UV}{HB}\right).} \tag{7}
\]

**Proof.** Apply the exact identity 1_gcd(u,v)=1=sum_{g|u,g|v}mu(g). Only g coprime to H contribute. For fixed g<=B, scale u=g*u0,v=g*v0. The congruence remains v0=c*u0 modulo H. Inclusion-exclusion over prime divisors of H counts u0 in [U/g,16U/g] coprime to H as

\[
15U\phi(H)/(gH)+O(\tau_H).
\]

For every such u0, the number of v0 in [V/g,2V/g] in the required class is V/(gH)+O(1). Bounding the error from this last O(1) by the total number of u0, which is O(U/g+1), gives a fixed-g count

\[
\frac{15UV\phi(H)}{g^2H^2}
 +O\left(\frac{\tau_H V}{gH}+\frac Ug+1\right).
\]

Sum these errors over g<=B. Extending the main sum to infinity costs O(UV/(HB)), and

\[
\frac{\phi(H)}H\sum_{(g,H)=1}\frac{\mu(g)}{g^2}
  =\frac1{\zeta(2)}\prod_{\ell\mid H}\frac{\ell}{\ell+1}.
\]

This proves (7), including interval-endpoint rounding errors. □

The estimate is a genuine moving-H count after the conjugacy, but its per-sector relative error can be large when V/H is small. In particular its U*log(2B) term divided by the main scale UV/H is of order H*log(2B)/V before local-density factors. For Type II boxes with V around sqrt(H), this bound does not give a relative asymptotic for each sector. It cannot be presented as uniform thin-sector root averaging.

A direct aggregate count is better than summing that error over sectors. Let N_both count primitive positions in Omega whose two coordinates are both coprime to H. Put

\[
\kappa_b(H)=\frac1{\zeta(2)}\prod_{\ell\mid H}\frac{\ell-1}{\ell+1}.
\]

The same Möbius expansion, now counting both scaled intervals coprime to H, gives

\[
\boxed{N_{\rm both}=15UV\kappa_b(H)
 +O\left(\tau_H(U+V)\log(2B)+\tau_H^2B+\frac{UV}{B}\right).} \tag{8}
\]

For each g the two interval counts have errors O(tau_H); multiplying and summing yields the first two displayed errors. The main coefficient is (phi(H)/H)^2*sum_{(g,H)=1}mu(g)/g^2, which is exactly kappa_b(H). The reciprocal-square tail gives the last error. This proves (8).

The density is consistent with the sector geometry:

\[
\frac{\phi(H)}H\kappa_u(H)=\kappa_b(H).
\]

Thus phi(H) unit sectors, each with transformed area 15UV/H and density kappa_u(H), have the correct aggregate leading mass. These densities may depend substantially on H and must not be replaced by a fixed parity constant.

For example, if H tends to infinity and H^delta<=U,V<=H^C for fixed positive delta,C, (8) gives a relative aggregate asymptotic. The standard elementary divisor bounds give tau_H=H^o(1), while the local product kappa_b(H) is H^(-o(1)); the displayed error divided by its main term tends to zero. This conclusion concerns position counts, not list-constrained complement-ratio moments. It needs no new prime-distribution input.

One additional exact-edge estimate is uniform even in a thin sector. Fix a primitive P', fixed D,a,b and determinant det(P',Q')=D*(b-a). All integer solutions Q' differ by integer multiples of P'. Since P'_1>=U and Q'_1 lies in [U,16U], there are at most 17 such Q', independently of H. List divisibility and the parallelogram restriction can only reduce this count. This gives a concrete bound for the exact-edge part for a fixed label transition. The major-arc comparison involves many nonexact determinants; this count does not control its cancellation or the full summed list operator.

## What the calculation removes and what it leaves

The candidate full pullback removes the moving determinant coefficient exactly on the unit-first-coordinate state space, including its centered comparison and adjoints. Properly carrying a prime-input coprimality restriction can give both-unit positions, and original small-label/sift separation then restores primitivity for nonzero centered terms. The two elementary counts and the exact-edge bound are actual quantitative consequences, not assumed cancellation.

No target-uniform bound on the centered coefficient-one operator over these H-dependent parallelograms has been proved. The aggregate point count does not average the inverse/complement ratios, prescribed prime-list lines, or high moments appearing in the source's root-averaging argument. Using its existing congruence-count theorem with an added modulus H would leave its inspected range when H is the Goldbach target; no enlarged-range theorem is imported here. A proof exploiting the aggregate both-unit structure without paying that full modulus would be genuinely additional arithmetic work.

The original polynomial-label moment-height, small-K and root-range deficits from LABELS-005 also remain. This conjugacy does not remove the h=1 prime boundary or justify zero bias on polynomial-rough complements. The work is a finite geometric reduction with explicit counts, not a Goldbach proof or a demonstrated breakthrough. The precise next estimate is a uniform centered-operator or root-moment bound on the exact unit-sector domains, with its true H and list-modulus dependence, while retaining the actual prime-input structure.
