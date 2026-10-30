# Factorable coefficients at the protected polynomial boundary

29 October 2026. Registry Mathematician, `GOLDBACH-BOUNDARY-017`, propose stage. Two bounded candidates are proved below, pending the distinct critic: an exact connection from the positive selected-cofactor expression to its actual coefficient input and comparison, and a principal-energy falsifier of one literal polynomial-sift extension, with a target-average normalization audit on the same explicitly different input. The full signed comparison cancellation remains unresolved. No helper code, experiment, new source search, paid inference or external action was performed. Usage is unknown.

Assurance is a complete author derivation using the accepted COFACTORS-015 comparison identity and declared classical PNT/Mertens background, not formal verification, external peer review or a new audit of those classical proofs. The accepted 015 revision SHA256 is `23996d11ed540409153fba0ed62957e472659d0f1082411e9a494671f0fa6d1c`. The actual PAIRING-011, ENERGY-012 and TYPEI-013 interfaces are used only as specified below. Closest-work novelty, the pointwise original prime margin and Goldbach are unestablished.

## Candidate 1: the exact input, its square and the remaining sectors

**Proved, pending review.** The configuration input is genuinely factorable before the cofactor projection. Its h=1 amplitude is an explicit weighted arithmetic convolution, with no damping or oscillation forced merely by factorability. A polynomial-sifted balanced test has a fixed-sign h=1 amplitude. It is a different arithmetic input from the accepted small-sift energy coefficients. In the explicit box below the only positive integer cofactor is 1, and the full raw-minus-comparison form is exactly

\[
 D_H(f)=(1-m_{\rm arc})|C_1(f)|^2-Q_{\rm frac}(f). \tag{1}
\]

Q_frac is a real signed Hermitian form. No nonnegativity or sufficiently small upper bound for it on either actual coefficient input is established here. Thus (1) is not a lower bound for D_H(f) and does not refute a total-difference estimate.

### Exact selected-divisor expansion and damping

Let H be even, alpha in [3/10,1/3), z=H^alpha, and let P contain all unit primes a in (z,H). Use the **full one-group** normalizer

\[
 V_H=\sum_{a\in P}\frac1a=\log(1/\alpha)+o(1)>0. \tag{2}
\]

The error is uniform for H in a fixed comparable range: the harmonic prime estimate gives the full mass, while the unit deletion is O_alpha(1/z), since at most 1/alpha prime divisors of H exceed z. This is not the single-polynomial-dyad mass, which is of order 1/log H. Substituting that dyad normalizer would retain its explicit inverse powers in all following formulas.

Write nu(w) for the number of distinct P-prime divisors of w and R_z(w) for P^-(w)>z, with R_z(1)=1. For a fixed nonnegative selected-label cutoff eta_a and factorable coefficient f(m,n)=alpha_m beta_n, the original positive selected contribution is

\[
 T^+_\rho=\frac1{V_H}\sum_{m,n,\,0<mn<H}
 f(m,n)\mu(H-mn)R_z(H-mn)
 \sum_{\substack{a\in P\\a\mid H-mn}}\eta_a\rho^{\nu(H-mn)-1}.
\]

Selecting a once is an exact finite identity:

\[
 T^+_\rho=-\sum_{h\ge1}\mu(h)R_z(h)\rho^{\nu(h)}C_h^*,\quad
 C_h^*=\frac1{V_H}\sum_{\substack{a,m,n:H-mn=ah\\(a,h)=1}}\eta_a f(m,n).
 \tag{3}
\]

Indeed mu(ah)=-mu(h) when (a,h)=1; if h is nonsquarefree both sides vanish, and if a|h the original mu(ah) is zero. The coprimality condition in (3) therefore cannot be removed algebraically. For general complex coefficients, enlarging the inner sum is not a monotone enlargement of its squared absolute value. PAIRING-011 removes that overlap with a separate small-label estimate; its polynomial-range extension is not assumed here.

The exact damping rho^nu(h) is an outer cofactor factor in (3). Cauchy gives

\[
 |T^+_\rho|^2\le
 \left(\sum_{1\le h\le H/Y}\mu(h)^2R_z(h)\rho^{2\nu(h)}\right)
       \sum_{h\ge1}|C_h^*|^2
 \le (H/Y)\sum_{h\ge1}|C_h^*|^2                 \tag{4}
\]

when eta_a vanishes below Y. This square has no missing rho multiplier inside its factorable input: the damping was retained in the first Cauchy factor. Alternatively it can be retained in a weighted cofactor square, whose input/measure then changes explicitly. At h=1 it is exactly one in either convention. There is no J padding and no artificial factorial/list factor: this is K=1,J=0.

### The true Hilbert measure, multiplicities and conjugation

For positive product supports, the state x=(a,m,n) has measure

\[
 d\mu(x)=\eta_a/V_H
\]

with counting measure on the supported integer pairs m,n; zero-measure labels are omitted. For a specified coefficient family we may take the Cartesian nonzero support `A times supp(alpha) times supp(beta)`; retaining additional zero-input states does not change its quadratic form. Any block mass or eigenvalue below is on the explicitly specified compression, not a larger all-integer state population. The input is exactly f(x)=alpha_m beta_n, independent of a. Let lambda_x=(H-mn)/a. The unrestricted raw kernel K(x,y) is one when lambda_x=lambda_y is a positive integer, zero otherwise. Its form is

\[
 Q_K(f)=\sum_{x,y}\mu_x\mu_y f(x)\overline{f(y)}K(x,y)
        =\sum_{h\ge1}|C_h|^2,
 \quad C_h=V_H^{-1}\sum_{H-mn=ah}\eta_a\alpha_m\beta_n. \tag{5}
\]

The exact square from (3) uses the additional eligibility at both kernel endpoints. We identify it with (5) only in the later box, where the sole integer cofactor is 1 and eligibility is automatic. No general complex-overlap bound has been silently imported.

This is a pushforward of the actual coefficient square, with no extra divisor multiplicity. Collapsing to basic states (a,u) replaces f by the actual convolution

\[
 F_H(u)=\sum_{m n=u}\alpha_m\beta_n.
\]

Thus C_h=V_H^-1 sum_a eta_a F_H(H-ah). The norm of this collapsed input is not automatically the norm before collapse. The latter, which is the Hilbert norm used here, is exactly

\[
 \|f\|_\mu^2=\left(\frac1{V_H}\sum_a\eta_a\right)
          \left(\sum_m|\alpha_m|^2\right)
          \left(\sum_n|\beta_n|^2\right).          \tag{6}
\]

The expansion of (5) has coefficient
`alpha_m*conj(alpha_r)*beta_n*conj(beta_s)`.
The convention is linear in the first argument. If a physical-position operator uses the alternate endpoint order of PAIRING-011, its endpoint function is the corresponding `conj(alpha_m)*beta_s`, as in that accepted proof. This does not change (5), does not drop a conjugation, and does not prove a polynomial-label identification with that different physical operator.

### The full comparison and sector projection

Take labels in [Y,4Y], all units modulo H and less than H, and products 0<mn<H. Let Psi be the accepted real even cutoff, equal to one on [-4,4]. Define t=bmn-ars and

\[
 J(x,y)=\Psi(t/(HY))\int_{\theta:H\theta\in\mathfrak M_1}
                  e(\theta(t-H(b-a)))\,d\theta.
\]

The full pullback identity from 015 gives

\[
 J(x,y)=\mathbf1_{H\mid t}\Psi(t/(HY))
        \int_{\mathfrak M_1}e(\phi(t/H-b+a))\,d\phi,\qquad
 m_{\rm arc}=|\mathfrak M_1|.                       \tag{7}
\]

There is no extra 1/H. The plateau is valid on this whole positive-product support, because |t|<4HY. Let Q_J use the same measure and the same f as (5). The kernel preserves

\[
 c(x)=(H-mn)a^{-1}\pmod H.                         \tag{8}
\]

For integer cofactors 0<h,k<H, unit labels imply `H|t iff H|(k-h)`, hence h=k. Their phase is zero, so the integer compression of J is m_arc K. The c=1 sector contains **exactly** lambda=1, and contains no fractional state, since H-mn and a are both in (0,H). Cross terms from this sector to its complement vanish for both K and J.

Let P_1 be the Hilbert projection onto a+mn=H. The actual arithmetic projection is
`P_1 f=1_(a+mn=H)*alpha_m*beta_n`.
It depends jointly on a,m,n. When the block is nonempty and at least two labels are active, it cannot be an input independent of a on the full Cartesian support: for a fixed contributing m,n only one label satisfies the boundary equation. An empty projection is zero; no nonemptiness is asserted pointwise. Sector invariance allows the decomposition of the form of the original f, but does not permit invoking a factorable-input theorem for P_1f as if it were factorable. Conversely it does permit computing the exact h=1 contribution without replacing f by an arbitrary witness vector.

In a general box other integer h and integer-fractional same-sector cross terms must be retained. If I denotes all integer-cofactor states and F its complement, then

\[
 Q_K-Q_J=(1-m_{\rm arc})\sum_h|C_h|^2
           -2\Re Q_J(f_I,f_F)-Q_J(f_F).             \tag{9}
\]

No sign of the last two terms follows from K's positivity. The specified J is Hermitian; a positive-semidefinite representation for it on this general configuration space has not been proved. The modular c=1 protection removes only its own cross terms.

### Honest balanced boxes and the two coefficient families

Fix a large real T, put delta=1/4, and take both integer intervals

\[
 I=[T,5T/4],\quad y=7T^2/8,\quad t_0=7T^2/4,\quad
 Y=2T^2,\quad 5T^2\le H\le105T^2/16,
 \tag{10}
\]

with H even. Take a fixed smooth eta in [0,1], compactly supported in (2,5/2), and equal to one on [17/8,19/8]. Set eta_a=eta(a/Y). Its active labels lie in (4T^2,5T^2), hence are less than H and greater than H/2. Take all genuine prime labels with that weight and (a,H)=1. There is no additional label normalization besides V_H in (2).

The entire product rectangle lies in `y<mn<=t_0<H`: its products are between T^2 and 25T^2/16, strictly inside the dyad. These are legitimate subintervals of the original [T,2T] variable dyads. There is no product-endpoint mask to project or smooth here. Also y<H/2 and y>=H/log H eventually, X=T^2 is comparable to y and H, and the inherited Vaughan threshold is the **exact** `U=V0=y^(1/5)`. It is less than every m,n in I. A label at least 4T^2 and a positive complement at most H-T^2<=89T^2/16 cannot have integer cofactor at least 2. Thus all integer-cofactor states in (5) have h=1, automatically (a,h)=1. Equations (3)-(5) then connect the actual rough selected target to exactly -C_1, with no overlap error, while (4)'s h sum has only its h=1 atom.

The accepted TYPEI-013 actual arrays at v=0 are

\[
 \alpha^{\rm small}_m=\mu(m)R_Z(m)\mathbf1_{(m,H)=1},\quad
 \beta^{\rm small}_n=c_{V0}(n)R_Z(n)\mathbf1_{(n,H)=1},\quad
 Z=\exp((\log H)^{3/4}).                             \tag{11}
\]

They are genuinely factorable, and their h=1 amplitude is exactly

\[
 C_1^{\rm small}(H)=\frac1{V_H}
  \sum_{\substack{m,n\in I\\a=H-mn\text{ prime}}}
       \eta(a/Y)\mu(m)c_{V0}(n)R_Z(mn)\mathbf1_{(mn,H)=1}.
 \tag{12}
\]

These arrays do **not** have a fixed sign on I. At this scale R_Z permits squarefree semiprimes in I as well as primes: primes r,s in a sufficiently narrow fixed-factor interval about sqrt(T) have product in I and both exceed Z eventually. PNT gives many distinct such r,s, and deleting the O(1) primes dividing H still leaves choices. Their mu(m)=+1, whereas primes m in I have mu(m)=-1. Thus the inference that the existing small sift already makes balanced variables prime is false. No bound for (12) has been established by this stage.

For the explicit prime-factor test define a different, factorwise polynomial projection:

\[
 \alpha^{\rm poly}_m=\alpha^{\rm small}_m R_z(m),\qquad
 \beta^{\rm poly}_n=\beta^{\rm small}_n R_z(n).       \tag{13}
\]

Uniformly for fixed alpha in the stated interval, I lies in `(H^alpha,H^(2alpha))` eventually. An integer in I with least prime factor exceeding H^alpha must be prime, since otherwise it exceeds H^(2alpha). Therefore at v=0 the nonzero entries of (13) are exactly

\[
 \alpha^{\rm poly}_r=-1,\qquad
 \beta^{\rm poly}_s=\log s,
 \quad r,s\in I\text{ prime},\quad (rs,H)=1.         \tag{14}
\]

For prime s>V0, c_V0(s)=log s exactly; all inherited lower-length, small-sift and unit conditions hold. At H=2^k all odd r,s are automatically units, but no prescribed such H is proved to have a contributing triple.

There are two precise statuses for this test. It is still a bounded factorable arithmetic array satisfying the generic small-sift support conditions; a proposed universal polynomial-label difference theorem for that family would have to handle it. It is also the exact array of a **different** completely multiplicative R_z-sifted Vaughan identity, for which the algebraic convolution remains valid. It is not the accepted ENERGY-012 Mobius/long-factor array: its extra R_z factors change that energy, and the existing Type-I/prime-correction analysis cannot be imported. Nor does a signed-form bound for f_small imply the same bound for its product projection f_poly. This distinction is load-bearing, even though projection in m and n here is factorable.

Write f_poly=alpha_poly beta_poly. Its boundary is

\[
 C_1^{\rm poly}(H)=-B_H,\quad
 B_H=\frac1{V_H}\sum_{\substack{r,s\in I\text{ prime}\\a=H-rs\text{ prime}}}
                  \eta(a/Y)\log s\ge0.              \tag{15}
\]

Each contributing triple is automatically a unit triple: a>r,s and `H=a+rs` give gcd(a,H)=gcd(r,H)=gcd(s,H)=1. Multiplicity of ordered r,s is retained. If the intervals coincide, a product rs with r!=s contributes both orders, with total convolution coefficient -log(rs); r=s contributes only -log r. No repeated-label equal-edge deletion is performed.

All other states of this box have fractional cofactors. Let f_F denote the actual restriction to those states, rather than freely chosen added coefficients. The protected-sector identity gives (1) for either small or polynomial input, with

\[
 Q_{\rm frac}(f)=Q_J(f_F).
\]

It is real because J is Hermitian. It is a **signed** form in the present argument, including for the real fixed-sign input (14): real coefficients do not make Fourier kernel entries nonnegative, and no positive-semidefinite proof is supplied. The term is not discarded, assigned a sign or bounded by the isolated raw sector. This completes the exact arithmetic connection without proving cancellation.

## Candidate 2: the principal-energy falsifier and its normalization audit

**Refuted assertion:** the literal all-precision ENERGY-012 conclusion remains valid after its actual small-sift arrays are replaced by (13), with the same definitions of B,M,N, full normalizer and normalized character energy. **Proof, pending review:** a principal-character lower bound below is at least a constant times `1/(H log^4 H)` for every large even H on an explicit member of this family. It contradicts the proposed `O_A(1/(H log^A H))` for A>4, even on powers of two. This is a failure of that specified extension, not of ENERGY-012 with its accepted actual coefficients and not of every nonzero-centered polynomial method.

As an auxiliary normalization audit of the same input, classical PNT/Mertens also prove that for each fixed alpha and the fixed eta above there are arbitrarily large even H in (10) for which

\[
 B_H\gg_{\alpha,\eta}\frac{H}{V_H(\log H)^2},\qquad
 |C_1^{\rm poly}(H)|^2\gg_{\alpha,\eta}
                         \frac{HY}{V_H^2(\log H)^4}. \tag{16}
\]

This is an averaged prime-plus-semiprime witness, with composite original Vaughan variable p=rs. It is not a prime-plus-prime witness, not a conclusion for every H or every power of two, and not a lower bound for the total signed D_H.

### Auxiliary target averaging with the exact normalizer

Let c_eta=integral eta(v)dv>0 and v_alpha=log(1/alpha). Uniformly for H in (10), V_H=v_alpha+o(1). PNT with a fixed smooth cutoff, by ordinary real partial summation, gives

\[
 \#\{r\in I:r\text{ prime}\}\sim\frac{\delta T}{\log T},\quad
 \sum_{s\in I\text{ prime}}\log s\sim\delta T,\quad
 \sum_{a\text{ prime}}\eta(a/(2T^2))\sim\frac{c_\eta T^2}{\log T}.
\]

All the primes here are odd eventually. Each triple a,r,s contributes to exactly one even H=a+rs in (10), and has the unit property just proved. Hence the exact sum followed by these three classical asymptotics yields

\[
 \sum_{\substack{5T^2\le H\le105T^2/16\\H\ {\mathrm{even}}}}B_H
  =(1+o(1))\frac{c_\eta\delta^2}{v_\alpha}
                                  \frac{T^4}{(\log T)^2}. \tag{17}
\]

The number of even targets is `(25/32+o(1))T^2`. Some target therefore has B_H bounded below by a positive constant times `T^2/(v_alpha log^2 T)`. Using H comparable to Y comparable to T^2 proves (16). This argument counts ordered r,s; it needs neither prime-pair asymptotics at a prescribed H nor any independence assumption. The range starts at 5T^2, so the targets selected as T grows are unbounded.

### Full input norm, thin projection and the raw error scale

For every even H in (10), removing prime divisors of H from I deletes only O(1) primes, because each has logarithm comparable to log T. Also no active prime a>H/2 divides even H. Formula (6) and PNT therefore give, uniformly in those H,

\[
 \|f_{\rm poly}\|_\mu^2
  =(1+o(1))\frac{c_\eta\delta^2}{v_\alpha}
                                \frac{T^4}{\log T}. \tag{18}
\]

Let S_1=sum_(x:h=1)mu_x on the **prime-factor Cartesian support** of f_poly, and N_1=||P_1 f_poly||_mu^2. Thus this S_1 counts exactly the contributing ordered prime triples with weight eta_a/V_H. It is not the mass of a larger block containing composite zero-input states. Their exact relationships are

\[
 (\log T)S_1\le B_H\le\log(5T/4)S_1,\qquad
 (\log T)B_H\le N_1\le\log(5T/4)B_H.              \tag{19}
\]

In particular the actual projected arithmetic vector, when nonzero, nearly aligns with the constant rank-one vector: its raw Rayleigh quotient B_H^2/N_1 lies between `S_1*(log T/log(5T/4))^2` and S_1 by (19) and Cauchy. This makes explicit what the fixed sign proves. It does not turn P_1f into a factorable full input.

At the targets furnished by (17), S_1 is at least a constant times H/(V_H L^3). However the endpoint projection is thin. Trivially `B_H<=V_H^-1*(#r primes in I)*(sum_s log s)<<T^2/(V_H log T)`, since eta<=1 and there is at most one a for each r,s. Thus N_1<<T^2/V_H, and from (18)

\[
 \frac{\|P_1f_{\rm poly}\|_\mu^2}{\|f_{\rm poly}\|_\mu^2}
        \ll_{\eta}\frac{\log T}{T^2}.              \tag{20}
\]

At the average-selected targets this ratio is also bounded below by a constant times 1/T^2 from (16),(19),(18). The large configuration eigenvalue and a nonempty block therefore cannot be substituted for its full-input contribution without this projection cost.

For the unnormalized quadratic comparison error scale HYL^(-A), (16) still says the isolated h=1 raw contribution can have size at least `c HY/(V_H^2 L^4)`. The elementary arc-cover estimate is `m_arc<<L^(3A0)/Y=o(1)` for fixed A0 here. If a proposed total estimate `|D_H(f_poly)|<=C_A HYL^(-A)` holds for some A>4, (1) would force at these targets

\[
 Q_{\rm frac}(f_{\rm poly})=(1-m_{\rm arc})B_H^2
                                  +O_A(HYL^{-A}). \tag{21}
\]

Equation (21) is a necessary compensation, not a contradiction: its left side has not been estimated. Conversely a sufficiently small upper bound for it would refute that particular universal total estimate on this explicit input. Neither alternative is proved here. No isolated positive sector is used to lower-bound a signed total.

For the accepted small-sift input there is an additional, earlier possible cancellation:
`C_1^small=C_1^poly+C_1^(small-poly)`.
Its second term has actual composite-variable signs and can cancel the first inside h=1 itself. A theorem for (12) therefore needs to control that actual convolution, while a universal polynomial-label norm/difference argument must additionally retain all fractional sectors. No result from (16) is promoted across either of these missing steps.

### Exact normalized energy and the principal obstruction

Now set `T=sqrt(H/6)` for each even H, not a target average. This lies within (10), since H/T^2=6. Keep M=N_var=T, Y=2T^2=H/3, the full V_H of (2), the inherited V0=y^(1/5), and exactly the prime-factor coefficient arrays (13)-(14). Distinguish the character energy variable from the integer target H. With k=1, take both fixed marking/long twists to be the principal character modulo H, and take v=lambda=0. These choices are permitted in the literal energy definition of ENERGY-012. Put

\[
 B_\chi(t)=\frac1{YV_H}\sum_{a\ {\mathrm{prime}}}\eta(a/Y)\chi(a)a^{it},\quad
 M_\chi(t)=\frac1T\sum_{r\in I\ {\mathrm{prime}}}(-1)\mathbf1_{(r,H)=1}\chi(r)r^{it},
\]
\[
 N_\chi(t)=\frac1T\sum_{s\in I\ {\mathrm{prime}}}(\log s)\mathbf1_{(s,H)=1}\chi(s)s^{it}.
\]

The selected labels are all units since a>H/2. For any height T0=(log H)^B1 from the accepted energy scheme, its formal normalized energy on this changed input is exactly

\[
 \mathcal E_{\rm poly}(H)=\frac1{\varphi(H)}\sum_{\chi\bmod H}
         \int_{|t|\le T0}|B_\chi(t)M_\chi(t)N_\chi(t)|^2\,dt. \tag{22}
\]

There is one fixed twist in each family, no varying twist and no alteration of the prefactors. At the principal chi_0, the PNT estimates already proved, including the O(1) deleted long primes dividing H, give

\[
 B_{\chi_0}(0)=(1+o(1))\frac{c_\eta}{2V_H\log T},\quad
 M_{\chi_0}(0)=-(1+o(1))\frac\delta{\log T},\quad
 N_{\chi_0}(0)=(1+o(1))\delta.                       \tag{23}
\]

All these are real; only M has a negative sign. To get positive measure in t, rather than rely on a single point, fix tau=1/10. After multiplying B(t) by Y^(-it), all its phases have arguments `t log(a/Y)`, with a/Y in (2,5/2). After multiplying M(t),N(t) by T^(-it), their phases have arguments `t log(r/T)` or `t log(s/T)`, with r/T,s/T in [1,5/4]. For |t|<=tau every such argument has absolute value less than pi/3. Positivity of the coefficients of B,-M,N therefore implies

\[
 |B_{\chi_0}(t)|\ge\tfrac12 B_{\chi_0}(0),\quad
 |M_{\chi_0}(t)|\ge\tfrac12|M_{\chi_0}(0)|,\quad
 |N_{\chi_0}(t)|\ge\tfrac12 N_{\chi_0}(0).          \tag{24}
\]

The factors Y^(-it),T^(-it) have modulus one; no differentiation or zero-free theorem is used. The interval [-tau,tau] is inside the fixed growing energy height eventually. Every term of (22) is nonnegative, so retaining its principal term and using (23)-(24) proves

\[
 \mathcal E_{\rm poly}(H)
   \gg_{\alpha,\eta}\frac1{\varphi(H)V_H^2(\log H)^4}
   \ge\frac{c_{\alpha,\eta}}{H(\log H)^4}.         \tag{25}
\]

This holds for every sufficiently large even H in this construction; no unproved target-specific prime triple count was used. It includes powers of two and thus cannot be repaired merely by the accepted small-radical zero-free specialization. Since V_H stays in a fixed positive compact interval, (25) contradicts the stated literal all-A extension for any A>4 as H grows. If a single-dyad reciprocal normalizer were substituted, its inverse would enlarge the principal obstruction, not remove it.

The exact failure is the loss of the small-conductor Mobius cancellation: M_poly has prime-supported coefficients -1, whereas the accepted M_small retains the original Mobius rough array and can have cancellation. Formula (25) concerns a nonnegative normalized energy, so it requires no sign claim for Q_frac and does not infer a lower bound for Q_all-Q_maj. A different centered energy could subtract or retain this principal main part, but it would need an actual nonzero-center arithmetic analysis; none is proposed as proved here.

## Falsifiers, exact failure location and remaining objective

The first false shortcut is that R_Z on the balanced source intervals forces primality; the semiprime construction following (12) disproves it asymptotically. The polynomial projection (13) repairs that support statement but changes the actual energy family. The second false shortcut is that P_1f is factorable: for distinct supported r,s,a, the relation a+rs=H is a joint relation, and (20) records the projection cost rather than hiding it. The third invalid inference would lower-bound D_H by its protected contribution; the exact remaining signed form in (1) is the obstruction to that inference.

Candidate 1 establishes the arithmetic coefficients, positive measure, exact full normalizer, outer damping, conjugation, integer multiplicity and full comparison decomposition. Candidate 2 refutes the literal all-precision zero-centered energy extension on the changed polynomial-sifted family by (25), and its auxiliary average gives an honest witness at the raw error scale. Neither establishes a pointwise original prime count or a universal no-go theorem. Their direct closest context is the accepted 015 cofactor construction and 011-013 coefficient interfaces; a new novelty claim has not been checked.

The first unresolved analytic obligation for the accepted coefficient vector is a bound for (12) together with its complete Q_frac, not a configuration eigenvalue. For the proposed polynomial-sifted vector it is the actual signed compensation or its failure in (21), and a revised energy analysis retaining the proved principal center (25), plus any new polynomial-sieve Type-I transport needed to apply it to the original problem. These are more specific than the old dispersion D and do not assume its unknown h=1 estimate. Target-average prime-plus-semiprime counting does not select every even H. The original R/E0/H0 or F margin, nonzero prime reconstruction center, pointwise Goldbach and breakthrough classification remain open.
