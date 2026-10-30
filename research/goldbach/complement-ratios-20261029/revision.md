# Moving complement-ratio averaging: reviewed revision

29 October 2026. Registry role: Mathematician, `GOLDBACH-RATIOS-007`, revision stage. This record accepts the separate critic and finite-check results from the populated revise packet. Frozen inputs remain unchanged:

| Input | SHA256 |
| --- | --- |
| `statement.md` | `dbd7f89da164cf2dba56a9b6ef877d083e936d3caee912e70390218e0a6a6699` |
| `closest-work.md` | `95e4c94980157c3faf2530aab65d30d91a1b06c03f19b8f3857e6d862a130f71` |
| `survey.md` | `56933082bc0c3a30d16e3df466b1591fdd2557987f070bbecd1833ad73079bf6` |

**Proved, with separate agent review:** frozen equations (1)-(11), including their complete-sum, completion, mass, frequency, discrepancy and normalized bounded-variation statements. The recombination with a leading mass needs the explicit mean-times-mass-error term given below. Assurance is a self-contained elementary argument plus separate mathematical review, supported by bounded exact computations. It is not formal verification or external peer review. Inference usage and monetary cost are unknown.

**Unverified:** any prime-weighted, prescribed-list, selected-endpoint or high-moment extension; the changed major-arc estimate from SECTORS-006; a Goldbach lower bound, demonstrated breakthrough or novelty.

## Accepted estimates with their quantifiers

Let `H>=2`, `U,V>=2`, and let the population consist of primitive integer positions `P=(u,v)` with

\[
 U\le u\le16U,\qquad V\le v\le2V,\qquad (uv,H)=1.
\]

Keep literal closed endpoints and all rounding errors. Put `r_P=-v^{-1}/u mod 1`, `x_P=H r_P mod 1`, let N0 be the actual population size, and let S be the sum of `e(k x_P)` for a nonzero integer k. Define

\[
 \tau_H=2^{\omega(H)},\qquad
 \kappa_b(H)=\zeta(2)^{-1}\prod_{\ell\mid H}\frac{\ell-1}{\ell+1}.
\]

The elementary fourth-moment collision proof and unit-scaling orbit give, for every `m>=2` and integer h,a,

\[
 |K_m(h,a)|\le C(m)m^{3/4}(h,a,m)^{1/4},\qquad
 C(m)=\left(2\tau_3(m)m/\phi(m)\right)^{1/4}.
\]

Even m, nonunit frequencies, and zero complete frequencies are allowed in this finite input. Its proof uses the at-most-two fibers of the three-factor linear map, prime-power allocations of a product divisible by m, and an orbit of size `phi(m/g)` for `g=(h,a,m)`. For every fixed eta>0, `C(m)<<_eta m^eta`.

For every admitted u the reviewed interval completion is

\[
 S_u=\frac Vu\frac{\phi(H)}H c_u(k)
 +O\!\left(\tau_H C(u)u^{3/4}(k,u)^{1/4}\log(2u)\right).
\]

The constant here is absolute. The expansion includes every `d|rad(H)`, including empty intervals `[V/d,2V/d]` for `d>2V`. Since u is coprime to H, `-kH d^{-1}` has gcd with u equal to `(k,u)`, and its complete Ramanujan center is `c_u(k)`. This is a complete-frequency identity, not an equality of incomplete sums with different unit multipliers. The integer interval cardinality differs from V/d by O(1), uniformly including empty intervals. No small-H or unit-k hypothesis is added.

Summing u gives, for each fixed eta>0,

\[
 S=V\frac{\phi(H)}H
       \sum_{U\le u\le16U,\ (u,H)=1}\frac{c_u(k)}u
 +O_\eta\!\left(\tau_H\sigma_{-3/4}(|k|)
                         U^{7/4+\eta}\log(2U)\right),
\]

and consequently

\[
 |S|\ll_\eta V\tau(|k|)
 +\tau_H\sigma_{-3/4}(|k|)U^{7/4+\eta}\log(2U).
\]

The Ramanujan main term is essential when u divides k. The bounds sum the actual common-factor cost; they never assume `(k,u)=1`. The independent mass calculation gives

\[
 N_0=M+O(E),\qquad
 M=15UV\kappa_b(H),\qquad
 E=\tau_H(U+V)\log(2U).
\]

It counts v coprime to uH at fixed u and then expands `phi(u)/u`, avoiding a squared `tau_H` error. The local factor depending on H is retained.

Let H tend to infinity, with `U` and `V` comparable, up to fixed positive multiplicative constants, to `H^a` and `H^b`, respectively. Require fixed `a,b>0` and `b>3a/4`. For every fixed A>0, uniformly over `1<=|k|<=H^A`,

\[
 N_0>0\text{ eventually},\qquad
 \frac{|S|}{N_0}\ll H^{-\gamma+o(1)},\qquad
 \gamma=\min\{a,b-3a/4\}>0.
\]

For every fixed positive slack this notation gives the corresponding weakened power with a parameter-dependent constant. It supplies no numerical threshold or specified effective constant. The factors `tau_H`, `tau(|k|)`, `sigma_{-3/4}(|k|)` and `kappa_b(H)^{-1}` are uniformly subpower in this polynomial-frequency range. Zero k and arbitrary enormous frequencies are excluded from this cancellation conclusion. In particular, making k a multiple of every admitted u would make every phase one and is outside the claimed uniform range in general.

For N0>0 let D be the circular interval discrepancy of the x_P, using a consistent half-open convention. The reviewed Fejer argument yields, for each integer `J>=2`,

\[
 D\ll J^{-1/2}+\sum_{1\le k<J}\frac{|S(H,k;U,V)|}{kN_0}.
\]

Choosing J comparable to `H^{2 gamma}` uses a fixed polynomial-frequency exponent sufficiently large for this choice and gives `D<<H^{-gamma+o(1)}`. When U,V are comparable to `sqrt(H)`, gamma is 1/8 and J is comparable to `H^{1/4}`. This is a genuine limited unweighted cancellation result. It does not cover boxes failing the displayed exponent condition. For finite empty populations, neither S/N0 nor D is defined; only the raw finite sums and mass formulas are used.

## Explicit normalization correction for test functions

Let g be a right-continuous periodic function of bounded variation and put `mu_g=integral_0^1 g(t)dt`. The accepted normalized assertion is

\[
 \left|N_0^{-1}\sum_Pg(x_P)-\mu_g\right|
       \le \operatorname{Var}(g)D,\qquad N_0>0,
\]

with the usual interval convention in its Stieltjes proof. In particular constant functions have zero normalized error. The identity

\[
 \sum_Pg(x_P)-M\mu_g
 =\left(\sum_Pg(x_P)-N_0\mu_g\right)+(N_0-M)\mu_g
\]

therefore gives the explicit unnormalized bound

\[
 \boxed{\left|\sum_Pg(x_P)-M\mu_g\right|
 \le N_0\operatorname{Var}(g)D+|N_0-M|\,|\mu_g|.}
\]

Inserting the mass estimate makes the second term `O(E |mu_g|)`. In the polynomial box regime the resulting error is

\[
 O\!\left(N_0\operatorname{Var}(g)H^{-\gamma+o(1)}
                  +E|\mu_g|\right).
\]

Both costs must be retained for H-dependent g. A constant `g_H=H^{100}` has variation zero but incurs exactly `H^{100}|N0-M|` when N0 is replaced by M. Thus variation does not control this second cost. If N0=0, do not introduce a normalized discrepancy; the raw leading-mass comparison is simply `M|mu_g|`, equal to the mass-error contribution `|N0-M||mu_g|` in that case. No nonempty finite-population assumption is hidden by division.

## Finite evidence and corrected refuted assertions

The independent final check reports no failures at the declared finite inputs. It checked complete moments for moduli 2 through 18, 2,108 unit-orbit cases, 2,695 collision eliminations, and 29,240 inputs to the linear map. It checked 1,960 exact inverse-interval Mobius expansions and 132 Fourier completions, retaining 470 empty divisor intervals and 133 nonunit-k cases. The primitive-position branch used 60 domains, 300 frequency-grouping comparisons, 1,148 complements and 960 fixed-u mass checks. Six populations were empty and were kept unnormalized. The checker source hash is `498798fd996b211cf5d1f1b3bea47b101fcc720061d9b2133c1a9d5df92e28af`.

These computations check finite identities and hypotheses. Numerical error-scale ratios are diagnostics; they do not certify asymptotic constants, a limiting exponent, a prime-list estimate or Goldbach.

For accurate epistemic labeling, the **refuted assertions** are the following omitted-hypothesis or equality claims. Their counterexample calculations themselves are true:

1. Dropping `(u,H)=1` while retaining the unit-based frequency simplification is invalid: `u=2,H=2,k=1` gives actual complete sum +1 but the proposed Ramanujan center -1.
2. Equal coefficient gcds do not imply equal incomplete inverse sums: the recorded `u=3,k=1` short-interval examples at H=2 and H=4 give distinct `zeta_3` and `zeta_3^2` values.
3. Omitting v-coprimality changes the population and its sum: the recorded `u=3,H=2,V=2` example changes from 0 to -1.

None contradicts the accepted statements, which retain these hypotheses and only use unit-invariance of the complete Ramanujan sum and uniform bounds for incomplete sums.

## Priority, scope and the next arithmetic obligation

The inspected source appendix suggests the elementary finite input, and the argument here reconstructs it. No full Lue-Wang-Wu theorem, prescribed-modulus root average or enlarged-range version is imported. The separately inspected [Blomer-Risager-Shparlinski introduction, equation (1.4)](https://arxiv.org/html/2411.17823v3) records the stronger classical square-root Weil bound with gcd and divisor factors. Modular-inverse averaging by such methods is established methodology. This result is a scoped specialization with a self-contained weaker input; novelty remains unverified. Its exact filtered consequences are not claimed as audited consequences of those external theorems.

The measure here has no actual-prime coefficients, prescribed prime lists, selected endpoint weights or path moments. Marginal equidistribution of `H r_P` does not supply their joint distribution. In particular the denominator-H prime major-arc contribution of SECTORS-006 remains unestimated, and the polynomial-label and h=1 prime-boundary issues of LABELS-005 remain.

A distinct next bounded arithmetic obligation is joint projective-line and complement-ratio distribution on the actual determinant-H root families, with their prescribed list and endpoint constraints. It must state the true local density, populated family size, frequency or variation cost, modulus dependence and error before being used in a norm or moment estimate. Thin projective-line populations cannot be assumed to have the same relative discrepancy as the aggregate population. The present unweighted marginal estimate is useful finite input for testing such a statement, not a proof of it or of actual-prime cancellation. No original F lower margin, Goldbach proof or demonstrated breakthrough is established; the research goal remains open.
