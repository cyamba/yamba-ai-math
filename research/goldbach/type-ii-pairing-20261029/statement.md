# Signed cofactor square and the reflected Type-II difference

29 October 2026. Registry role: Mathematician, `GOLDBACH-PAIRING-011`, author stage. Two bounded candidates are derived below, pending distinct review: the signed-cofactor enlargement with quantitative overlap bounds, and the specified quadratic raw-minus-comparison estimate. The accepted MOMENTS-010 revision, including its common-state normalization and original-box qualifications, is used. No estimate of Q_maj, prime parity theorem, Goldbach proof, breakthrough or novelty is asserted.

The pinned Guo source and [Lue-Wang-Wu sections 4.6-4.7](https://arxiv.org/html/2610.20242v1) supply closer prior framing. Their full theorem and conditional transport are not imported. The argument below states the arithmetic interfaces, including one-edge positive bad-state replacement, rather than treating an endpoint moment as that replacement.

## Definitions and choices

Let `x=MN`, `L=log x`, `M,N>=x^delta`, and `x<=H<=x L^B` for fixed positive delta and fixed B>=0. Coefficients alpha_m,beta_n are complex, supported on subintervals of `[M,2M)` and `[N,2N)`, bounded by L^C, Z-rough and coprime to H. Take, for example, `Z=exp(L^0.24)`. More generally require that all chosen band primes lie below Z and every nonempty selected-product block has Y=o(Z). The fixed bands, eligible primes avoiding H, reciprocal masses V_i, J,R and order of precision choices are those of MOMENTS-010. K and band exponents stay fixed before x tends to infinity.

Let A be the products of one eligible prime per group, represented uniquely by disjointness. Write `V=prod_i V_i`, `p_min=min union Pi_i`. Choose a **real nonnegative** smooth dyadic partition eta, supported in [1,4], with bounded cutoffs and bounded overlap. For a fixed Y use eta(a/Y). Choose a fixed **real even** smooth psi equal to one on [-4,4], supported in `[-C_psi,C_psi]`. This plateau is part of this theorem: arbitrary compact support alone would not identify the raw quadratic form. Since a,b in [Y,4Y], the raw normalized determinant lies in [-3,3].

Let M1 be the denominator/width union defined in MOMENTS-010, `M_H={theta:H theta in M1}`, and put

\[
 t=bmn-ars,\qquad
 J_H(t;a,b)=\psi(t/(HY))\int_{M_H}e(\theta(t-H(b-a)))\,d\theta.
\]

The H-fold branch character sum gives exactly

\[
 J_H(t;a,b)=\mathbf1_{H\mid t}\psi(t/(HY))
             \int_{M_1}e(\phi(t/H-b+a))\,d\phi. \tag{1}
\]

There is no factor 1/H in the nonzero branch and `|M_H|=|M1|<<L^{3A0}/Y`. Define

\[
 A_h=V^{-1}\sum_{a,m,n:H-mn=ah}\eta(a/Y)\alpha_m\beta_n,
 \qquad Q_{\rm all}=\sum_{h\in\mathbb Z\setminus\{0\}}|A_h|^2,
\]

and

\[
 Q_{\rm maj}=V^{-2}\sum_{a,b,m,n,r,s}\eta(a/Y)\eta(b/Y)
       \alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s}
       J_H(bmn-ars;a,b). \tag{2}
\]

All coefficient supports remain their separate product supports. In particular no indicator `mn<H` is put inside this signed operator or into Q_maj.

## Candidate 1: support, cofactor square and overlap bounds

**Author proof, pending separate review.** The positive-argument selected-divisor expansion and its all-integer upper-bound square are valid, with overlap error `O_(K,rho)(x L^{2C}/p_min)`. Both raw and comparison absolute quadratic arrays are `O_(K,rho)(xY L^{C_1+3A0})` for a fixed exponent C1 depending on C; their parts with `(a,b)>1` save a factor `1/p_min`. These statements are uniform over the given H range.

### The positive target and the signed enlargement

Let omega_i count **distinct** eligible group primes and omega=sum_i omega_i, and set

\[
 W(w)=\prod_i\frac{\omega_i(w)\rho^{\omega_i(w)-1}}{V_i},
\]

with a zero factor when omega_i=0. It is uniformly bounded for fixed K,rho, since `sup_{j>=1}j rho^{j-1}` is finite and V_i have a uniform positive lower bound. For w=H-mn>=1 and w=ah with `(a,h)=1`,

\[
 \mu(w)=(-1)^K\mu(h),\qquad\omega(w)=K+\omega(h).
\]

Thus selecting one distinct divisor in each group gives the exact expansion with the additional restriction `(a,h)=1`. Removing that restriction costs only pairs with `p^2|H-mn` for an eligible p. Indeed

\[
 V^{-1}\sum_{a\mid w}\rho^{\omega(w/a)}\le W(w),
\]

because `omega(w/a)>=omega(w)-K`. For fixed m, each eligible p is coprime to m by Z-roughness, so `p^2|H-mn` selects one residue of n modulo p^2. Here `p^2=x^{o(1)}<N` eventually. Summing over m,n and p gives `O(x sum_p p^{-2})=O(x/p_min)`, with the coefficient factor L^{2C}. The eta cutoff only changes a fixed constant. No assertion about Mobius values at negative arguments occurs.

After this overlap error, the positive-argument dyadic target is

\[
 T_Y=(-1)^K\sum_{h\ge1}\mu(h)\rho^{\omega(h)}A_h.
\]

Only `1<=h<=H/Y` contribute. Consequently

\[
 |T_Y|^2\le\lfloor H/Y\rfloor Q_+
       \le(H/Y)Q_{\rm all},\qquad Q_+=\sum_{h\ge1}|A_h|^2. \tag{3}
\]

The second inequality adds nonnegative squares with negative h. A zero cofactor is impossible on the present support: mn=H contradicts `(mn,H)=1` for H>1. If this unit assumption is omitted, H=2,m=1,n=2,a=3 already gives a zero cofactor; deleting it would lose a genuine square term. This is a finite support witness, not a counterexample to (3) with its hypotheses.

Expanding Q_all keeps the two integer divisibilities and the equality of their quotients:

\[
 a\mid H-mn,\quad b\mid H-rs,\quad
 (H-mn)/a=(H-rs)/b\ne0. \tag{4}
\]

For `(a,b)=1`, (4) is equivalent to

\[
 bmn-ars=H(b-a). \tag{5}
\]

To prove the reverse implication, reduce `b(H-mn)=a(H-rs)` modulo a and b, then divide the resulting integer quotients. Zero is excluded by the same support. For shared primes (5) alone is insufficient: H=2,a=b=3,m=n=r=s=1 satisfies it but gives quotient 1/3. All shared raw terms below are therefore bounded from (4), not from an unjustified replacement by (5).

### A uniform elementary divisor-square bound

For any integer a coprime to H with `a=x^{o(1)}`, uniformly in the residue H modulo a,

\[
 \sum_{1\le k\le4x,\ k=H\ ({\rm mod}\ a)}\tau(k)^2
          \ll (x/a)L^3. \tag{6}
\]

Here is an elementary derivation sufficient for the present range. Prime by prime, `(e+1)^2<=binom(e+3,3)`, so `tau(k)^2<=tau_4(k)`. In every four-factor representation one factor is largest; the product d of the other three is at most `(4x)^{3/4}`. Thus the left side is at most four times

\[
 \sum_{d\le(4x)^{3/4}}\tau_3(d)
       \#\{k\le4x:d\mid k,\ k=H\pmod a\}.
\]

Only `(d,a)=1` contribute, because `(a,H)=1`. Their count is `4x/(ad)+O(1)`. The elementary sums `sum_{d<=T}tau_3(d)/d<<log^3(2T)` and `sum_{d<=T}tau_3(d)<<T log^2(2T)` give `(x/a)L^3+x^{3/4}L^2`. The second term is absorbed since every selected a is subpolynomial. This proves (6) without assuming a translated divisor-square theorem.

For fixed a,b in the selected block, Cauchy on the actual common integer h in (4), with `k=H-ah`, `l=H-bh`, bounds the absolute product-divisor count by

\[
 \sum_h\tau(H-ah)\tau(H-bh)\ll (x/\sqrt{ab})L^3
                                      \ll(x/Y)L^3, \tag{7}
\]

where each factor is retained only in its positive product support k,l<=4x. This works for either sign of h. The proof uses the positive product range rather than enlarging divisor arguments to size H, so it has no unnecessary factor H/x.

There are O(Y^2) integer product pairs a,b in the block. Those sharing a prime number at most

\[
 O\!\left(Y^2\sum_{p\ge p_{\min}}p^{-2}\right)=O(Y^2/p_{\min}).
\]

For a prescribed p, count multiples of p in [Y,4Y]; if the block contains p its number is O(Y/p), including endpoint rounding. Uniqueness of group-product representation prevents multiplicity. With eta bounded, coefficients L^{4C} and fixed V^{-2}, (7) gives

\[
 Q_{\rm raw,abs}\ll_K xY L^{4C+3},\qquad
 Q_{\rm raw,shared,abs}\ll_K xY L^{4C+3}/p_{\min}. \tag{8}
\]

For the comparison, (1) enforces `bk-al=0 mod H`. Each a,b is a unit modulo H. At fixed k, l is in one residue modulo H, in an interval of length O(H) from the cutoff, and k,l<=4x with H>=x. There are O(1) such l, and conversely O(1) k at fixed l. Therefore `2tau(k)tau(l)<=tau(k)^2+tau(l)^2` gives an O(xL^3) count for fixed a,b. Multiply by `|M_H|<<L^{3A0}/Y` and the same pair counts to obtain

\[
 Q_{\rm maj,abs}\ll_K xY L^{4C+3+3A_0},\qquad
 Q_{\rm maj,shared,abs}\ll_K xY L^{4C+3+3A_0}/p_{\min}. \tag{9}
\]

Equations (8)-(9) justify removing or restoring shared a,b at every fixed logarithmic precision. They do not assign cofactor integrality to a shared determinant solution.

## Candidate 2: the actual quadratic difference

**Author proof, pending separate review.** For every fixed A>0, after choosing the fixed precision parameters as described below,

\[
 \boxed{|Q_{\rm all}-Q_{\rm maj}|\ll_A xY L^{-A}
                                      \ll_A HY L^{-A}.} \tag{10}
\]

This is an estimate of the difference with the explicitly defined complete-pullback comparison. Q_maj itself is not estimated here.

### The accepted moment in the precise present range

MOMENTS-010 is used in its accepted revision, not its broader unqualified normalizer sentence. Eligible groups are used throughout the ambient alphabet, with unchanged good tests and original-box cutoffs. No full-band ambient power is equated to an eligible one through unit endpoints alone. The input can be oriented M<=N by exchanging both coefficient arrays and their identical support/sifting hypotheses before constructing the operator.

The accepted proof extends from H comparable to x to `x<=H<=xL^B` by the following explicit checks. The omitted reciprocal mass still has log H=O(L). ROOTS-008 remains uniform since H<=x^2 eventually, and with `U=d0YM,V=N` its aspect saving follows from M<=N. The relative height is `O(1+UV/H)<=O(d0Y)`, and every moving boundary coefficient `(H/(UV))z2` is bounded on contributing positions. Thus the same boundary/error calculation uses no positive H loss. All eligible masses and constants remain uniform. For any requested E the accepted moment consequently gives

\[
 D_{\rm unit}:=\sum_{P\in\Omega\ {m primitive},\ (P_1P_2,H)=1}
       \langle u_P,(BB^*)^R u_P\rangle
       \ll UV L^{-2RE},\quad U=d_0YM,\ V=N, \tag{11}
\]

for the ambient labelled coefficient-one operator B, with selected unit roots and the specified good projections. This is the ambient power, not a power with intermediate unit projections and not a full trace. Its root measure and density remain those of MOMENTS-010.

### Endpoint function, primitivity and exact kernel identification

For a position P, let G(P1) be its full eligible-band part. Set

\[
 f(P)=\overline{\alpha_{P_1/G(P_1)}}\,\beta_{P_2}
\]

when G(P1) is squarefree, has exactly m distinct primes in each group and the coefficient supports hold; set f=0 otherwise. It is independent of list ordering and is supported on both-unit coordinates. On the ambient labelled space each such original endpoint occupies its unique sector. At

\[
 P=(Dbm,s),\quad Q=(Dar,n),
\]

Z-roughness ensures `G(P1)=Db`, `G(Q1)=Da`, and

\[
 \overline{f(P)}f(Q)=
      \alpha_m\overline{\alpha_r}\beta_n\overline{\beta_s}. \tag{12}
\]

The conjugation is essential for complex coefficients. All endpoint damping equals one, because their eligible omega is exactly Km.

Both raw and comparison endpoint pairs are primitive automatically on this support, after the shared a,b terms have been removed. If a prime l divides Dbm and s, it exceeds Z, divides m and s, and avoids D and H. It divides `t=bmn-ars`; (1) or the raw relation gives H|t. Also t is nonzero: otherwise b divides ars, impossible since `(b,ars)=1` and b>1. Thus l divides the nonzero integer t/H, whose absolute value is at most C_psi Y<Z. This is a contradiction. The other endpoint is identical. The proof uses the nonzero **normalized** determinant and applies to comparison terms, not just exact edges.

The full-pullback kernel vanishes unless the unit endpoints share their slope class modulo H. In its sector image, `det(P',Q')/D=t/H`, and the centered brace is exactly that of the accepted coefficient-one B. The specified plateau makes the raw cutoff one on (5). These facts identify the desired disjoint quadratic array with the corresponding signed pairings. No positivity mask `mn<H` is introduced into B or f.

The endpoint norm has no logarithmic exponent growing with K or J. Indeed `sup|f|<=L^{2C}`. For each fixed ordered full list of product G, available positions are O(UV/G), since its coefficient quotient is at least M. Consequently

\[
 \|f\|^2\ll UVL^{4C}
      \left(\prod_iV_i^{-m}\right)
            \sum_{\rm ordered\ distinct\ lists}\frac1G
       \le UVL^{4C}. \tag{13}
\]

The last sum is bounded by `prod_i(sum_{p in Pi_i}1/p)^m`. Ordered tuples are retained on both sides, so no factorial is omitted or added.

### Localization and the ambient Gram pairing

Partition unit endpoints by sector `c=P2/P1 mod H` and real-slope cells of width `w=H/(d0 Y M^2)`. The kernel cutoff implies

\[
 |P_2/P_1-Q_2/Q_1|\ll w,
\]

so only O(1) neighboring cells within a sector interact. Every occupied sector, hence every cell, contains O(d0Y) endpoints. To see this choose a lattice-primitive P0 there. Its determinant with another point is an integer multiple of H, of absolute size O(UV), so there are `O(1+UV/H)` possibilities. For one determinant, lattice solutions differ by an integer multiple of P0; the first-coordinate range admits O(1) such shifts. Since `UV/H<=d0Y` and d0Y tends to infinity, the claimed count follows without an H factor.

Let f_j be f in one cell and g_j its possible target cells. The restricted matrix `(<u_P,(BB*)^R u_Q>)` is positive semidefinite. Its trace d_j bounds its largest eigenvalue. Thus

\[
 \langle f_j,(BB^*)^Rf_j\rangle
       \le C d_0Y (\sup|f|)^2 d_j.
\]

Spectral Holder in the ambient space and then Holder over cells give

\[
 |\langle f,Bf\rangle|
 \ll\|f\|^{2-1/R}
       \left(Cd_0Y(\sup|f|)^2\sum_j d_j\right)^{1/(2R)}.
\]

There is bounded overlap in the g_j supports, and `sum_j d_j<=D_unit`. With (11)-(13),

\[
 |\langle f,Bf\rangle|
       \ll UV L^{-E+4C}(d_0Y)^{1/(2R)}
       \ll_K d_0Yx L^{-E+4C}. \tag{14}
\]

The retained root factor is harmless because `log(d0Y)=O_K(L^{0.21})` and `R` is of order sqrt L. No pointwise deletion of projections or full-trace inference occurs. The Gram trace already includes the actual list-fiber norms; it is not a sum over artificially normalized u_P.

### Independent positive one-edge replacement for bad endpoints

Let K0 be the same eligible physical operator before its good-state projections, with list symmetrization retained. Removal is bounded by the two positive absolute one-edge forms with the source or target failing goodness, after `|f(P)f(Q)|<=L^{4C}` and damping at most one. This step cannot be deduced from (11).

Here is its arithmetic proof. Expand a single physical edge, relative to its unit source root, before any memory. It uses exactly J+2 distinct eligible primes per group in the union of its endpoint lists. There are `exp(o(L))` choices of relative target and prime data; their prescribed modulus has `log S=O_K(L^{0.21})`. The ROOTS-008 unit-root theorem and the same original-box/good-test boundary partition as MOMENTS-010 replace each positive form by its independent-line model with total error `O_D(UV L^{-D})` for any fixed D. Kernel absolute values are fixed functions of the integer relative determinant and prime data, not oscillatory functions of the real root. Only the controlled box and intrinsic bad-state indicators remain. The H range checks preceding (11) apply unchanged.

In the independent model the union-prime probability/normalizer mass is at most

\[
 \prod_i\left(\sum_{p\in\Pi_i}\frac1{V_i(p+1)}\right)^{J+2}\le1.
\]

For fixed complete source lists the bad-ratio measure is `O_K(exp(-cL^{0.1}))`, by the explicit good tests proved in MOMENTS-010. At fixed real root and selected primes, the exact reduced determinant gives O(1) relative targets. The comparison permits O(Y) reduced determinants, each O(1) targets, multiplied by `|M_H|<<L^{3A0}/Y`. All list averages have mass one. Hence the source-bad main is bounded by `UV L^{4C+3A0}exp(-cL^{0.1})`. Reverse the edge and apply the same argument to its adjoint for a bad target. This uses the actual symmetric joint list weights and retained original boxes, not an arbitrary root-dependent projection. We obtain

\[
 |\langle f,K_0f\rangle-\langle f,Bf\rangle|
 \ll_{D,K} UV\{L^{4C+3A_0}e^{-cL^{0.1}}+L^{-D}\}. \tag{15}
\]

This separately proves the positive absolute replacement and true row/column target counts needed to remove goodness.

### Artificial shared lists and exact reassembly

For one dyadic shared block define `B_d0=<f,K0 f>`. Since f is list-order invariant, its outside list symmetrizations disappear in this pairing. Its state weight times fresh-edge normalization is `prod_i V_i^{-(J+2)}`. Dividing its kernel d0/D by d0 gives the exact identity of weights

\[
 \frac1D\prod_i V_i^{-(J+2)}
       =\left(\prod_{i,h\le J}\frac1{p_{i,h}V_i}\right)V^{-2}.
                                                               \tag{16}
\]

Each shared coordinate is therefore an ordered harmonic draw of mass one. Summing over all dyadic D blocks counts each ordered tuple exactly once. It adds neither J! nor J+1. Fix coprime a,b, and let w(a,b) be the probability that the J draws per group are distinct and avoid the two unshared primes from that group. Let Delta(a,b) denote its coefficient array with the brace `1_(t=H(b-a))-J_H(t;a,b)`, including the eta factors. The exact reassembly is

\[
 \sum_{d_0}B_{d_0}/d_0
       =V^{-2}\sum_{(a,b)=1}w(a,b)\Delta(a,b). \tag{17}
\]

Primitivity and coefficient supports impose no further restrictions on these draws, by the earlier automatic-primitivity argument and Z-roughness. A union bound over collisions and forbidden endpoint primes gives uniformly

\[
 0\le1-w(a,b)\le C_K(J+1)^2
       \max_{i,p}(pV_i)^{-1}\ll_K(J+1)^2/p_{\min}. \tag{18}
\]

This probability concerns the sum over all D blocks; the mass in one block need not be near one. Equations (8)-(9) show that replacing w by one in (17) costs `O_A(xY L^{-A})` at every fixed precision. They also restore the shared a,b terms, with their **correct raw cofactor conditions**.

There are O_K(L) dyadic D blocks. For each, (14)-(15), with `UV=d0Yx`, give

\[
 |B_{d_0}|/d_0\ll_K xY
       \{L^{-E+4C}+L^{-D}+L^{4C+3A_0}e^{-cL^{0.1}}\}.
\]

Choose E>A+4C+3 first and D>A+3, then the accepted moment precision, A0 and K, and finally fixed band exponents and the limit in x. All remaining constants, including B and cutoff constants, are fixed. Summing blocks, applying (17)-(18), and using (8)-(9) proves (10). No cancellation or positivity is asserted for Q_maj.

## Assurance, source relationship and next boundary

The two candidate proofs are exposed for independent review. The sensitive interfaces are the signed cofactor/AP divisor count, plateau normalization, comparison congruence, ambient endpoint localization, positive bad-edge replacement and the ordered harmonic reassembly. Failure of any interface invalidates (10); no source-wide H2' assumption is used to conceal it.

The pinned Guo source already has the nonnegative signed-square and ambient restricted-Gram architecture. This reconstruction is not a novelty claim and does not validate its other conditional analytic inputs. The moment dependency is the accepted MOMENTS-010 eligible model in its corrected scope; its modest H-range extension was checked explicitly above. There is no equality of different full-band and eligible ambient powers.

Even acceptance of (10) leaves the comparison Q_maj, its major-energy/character-sum analysis, Type-I and decomposition interfaces, eventual weight removal, and an actual-prime theorem. The original polynomial-rough lower margin, nonzero centers and h=1 prime boundary remain. No Goldbach proof or demonstrated breakthrough follows from this Type-II difference.
