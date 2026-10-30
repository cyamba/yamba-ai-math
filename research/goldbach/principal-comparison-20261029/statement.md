# The actual positive comparison and its central principal term

29 October 2026. Registry Mathematician, `GOLDBACH-PRINCIPAL-019`, propose stage. Two candidates are proved below, pending the distinct critic: exact positivity and monotonicity of the actual comparison on its label-independent coefficient class; and its central-arc principal asymptotic with an all-precision nonprincipal remainder. A consequence is a positive lower bound for the actual fractional comparison on this particular polynomial prime-factor input. The raw-minus-major estimate and pointwise prime boundary remain unproved.

Assurance is a complete author argument using the actual reviewed CENTERED-018 revision and its named classical inputs, not formal verification, external peer review or a new audit of their published proofs. No mathematical experiment, helper run, new source search, paid inference, publication or outside action occurred. Usage is unknown. No novelty, Goldbach proof, breakthrough classification or full-goal completion is claimed.

## Exact family and accepted input

Let H=2^ell grow, L=log H, alpha in [3/10,1/3), delta=1/4,

\[
 T=\sqrt{H/6},\quad X=T^2=H/6,\quad Y=H/3,
 \quad I=[T,(1+\delta)T].
\]

Let P_I denote the primes in I, including either endpoint if prime. Let eta be fixed, real, nonzero, smooth, between zero and one, and compactly supported in (2,5/2). The selected-label set P consists of unit primes in (H^alpha,H), and

\[
 V_H=\sum_{a\in P}1/a=\log(1/\alpha)+o(1)>0.
\]

Every active label satisfies `2H/3<a<5H/6`, and the long primes are odd, hence all factors are H-units. The actual coefficients in this stage are

\[
 \alpha_m=-\mathbf1_{m\in P_I},\qquad
 \beta_n=(\log n)\mathbf1_{n\in P_I}.              \tag{1}
\]

These are the changed polynomial-factorwise prime arrays of BOUNDARY-017/CENTERED-018. They are not the accepted small-sift arrays of ENERGY-012. The inherited threshold may be the CENTERED-018 `V0=X^(1/5)` or BOUNDARY-017 `V0=(7T^2/8)^(1/5)`. Each is below I and gives c_V0(n)=log n on its prime support; equality of the inherited thresholds or of the full Vaughan interfaces is not asserted.

All products mn lie in `[T^2,25T^2/16]`, hence below H and strictly inside the honest product dyad `(7T^2/8,7T^2/4)`. There is no joint product or positivity mask. Ordered prime factorizations remain separate, including the single representation of a square.

The actual accepted CENTERED-018 revision SHA256 is `a45b012cbd701675ce6746f060bedd7777f5075ca8cb96ab3fd903b5d40407d3`, with positive distinct review `3a014cd1b9f78a36b81b05b9e38076e33807f8bd30080145927e54cf1e44caa2`. It supplies, at k=1 with trivial fixed twists, for every fixed A,B,C>0,

\[
 \frac1{\varphi(H)}\sum_{\chi\ne\chi_0}
  \int_{|t|\le L^B}
    |B_{\chi,\lambda}(t)M_\chi(t+v)N_\chi(t+v)|^2dt
       \ll H^{-1}L^{-A},                           \tag{2}
\]

uniformly for every real lambda and |v|<=L^C. Here

\[
 B_{\chi,\lambda}(t)=\frac1{YV_H}\sum_{a\in P}
          \eta(a/Y)e(-\lambda a/Y)\chi(a)a^{it},
\]
\[
 M_\chi(t)=-T^{-1}\sum_{m\in P_I}\chi(m)m^{it},\qquad
 N_\chi(t)=T^{-1}\sum_{n\in P_I}(\log n)\chi(n)n^{it}. \tag{3}
\]

The revision retains the exact half-integer endpoint argument and clean prime sets. We use only v=0 of (2), and import no other modulus, twist or product rectangle. Its effective ordinary PNT input is the inspected classical estimate `pi(x)=li(x)+O(x exp(-c sqrt(log x)))`; real partial summation gives its weighted-prime counterpart. Primary-statement assurance, including Iwaniec for the nonprincipal theorem, is as recorded in 018. Root administrative integration is not a mathematical input in place of this actual reviewed proof.

## Candidate 1: positivity of the actual form

Let Psi be the real even cutoff equal to one on [-4,4]. For any measurable set M of the circle, define t=bmn-ars and the actual comparison

\[
 Q_M=\frac1{V_H^2}\sum_{a,b,m,n,r,s}
  \eta(a/Y)\eta(b/Y)\alpha_m\overline{\alpha_r}
       \beta_n\overline{\beta_s}\mathbf1_{H\mid t}
       \Psi(t/(HY))
       \int_M e\!\left(\phi(t/H-b+a)\right)d\phi. \tag{4}
\]

This is the already pulled-back form. There is no additional 1/H or 1/a. The original full pullback has exactly its branch-count cancellation as in the accepted 017 argument.

**Proved, pending review.** On this actual coefficient class,

\[
 Q_M=\frac1{\varphi(H)V_H^2}\sum_{\chi\bmod H}\int_M
 \left|\sum_{a,m,n}\eta(a/Y)\alpha_m\beta_n\chi(amn)
       e\!\left(\phi a(mn/H-1)\right)\right|^2d\phi.
 \tag{5}
\]

Consequently Q_M>=0 and Q_(M')>=Q_M whenever M is contained in M' up to null sets. This statement concerns the complete form on the specified input; it does not assert positive semidefiniteness of the general label-dependent configuration kernel, or positivity of its fractional compression on arbitrary vectors.

### Exact proof and the scope of relabeling

All products are positive and less than H, and a,b<4Y. Thus `|bmn-ars|<4HY` for every contributing pair, so Psi is identically one throughout (4). This check precedes its removal.

Swap the two independently summed labels a and b. Their real eta weights are symmetric, and the arithmetic coefficients do not depend on either label. The resulting congruence is `amn=brs mod H` and the phase becomes

\[
 \phi\{a(mn/H-1)-b(rs/H-1)\}.                    \tag{6}
\]

Since every factor is an H-unit, exact multiplicative orthogonality expresses the congruence as

\[
 \mathbf1_{amn\equiv brs\ (H)}
  =\varphi(H)^{-1}\sum_\chi\chi(amn)\overline{\chi(brs)}.
\]

Substituting this and (6), and factoring the two finite sums, proves (5) with precisely its coefficient conjugations. Equivalently,

\[
 Q_M=V_H^{-2}\int_M\sum_{c\in(\mathbb Z/H)^\times}
   \left|\sum_{amn\equiv c\ (H)}\eta(a/Y)\alpha_m\beta_n
               e\!\left(\phi a(mn/H-1)\right)\right|^2d\phi.
 \tag{7}
\]

Both formulas retain equal-label and repeated-product terms. They need no coprimality of a and b beyond their individual H-units. Positivity and monotonicity follow from the pointwise nonnegative integrand.

The arithmetic input can be complex in this algebraic identity provided it remains independent of a with the displayed Cartesian supports. A joint label/cofactor projection would instead leave the coefficients with the wrong label after the swap, and the square argument would not follow. Likewise a nonconstant Psi outside its plateau would remain a coupled factor. These are exact hypotheses doing substantive work, not a generic configuration-kernel positivity theorem.

## Candidate 2: the central principal main term

Fix A0>0, put Lambda=L^A0 and

\[
 M_0=\{\|\phi\|\le\Lambda/Y\}.
\]

For large H this is one interval about zero in the circle. Let M_1 be the accepted major-arc union with this fixed logarithmic cutoff. Its q=1 arc contains M_0, and the elementary union bound gives

\[
 |M_1|=m_{\rm arc}\ll L^{3A0}/Y.                 \tag{8}
\]

For example the original radius `2L^A0/Y` used in the moment definition contains this chosen half-radius central interval. No other major arc is estimated by the following central computation.

Define the continuum function

\[
 A(\lambda)=\int_2^{5/2}\eta(u)
       \int_1^{5/4}\int_1^{5/4}
           e\!\left(\lambda u(rs/6-1)\right)\,dr\,ds\,du,
 \quad J_\eta=\int_{\mathbb R}|A(\lambda)|^2d\lambda. \tag{9}
\]

**Proved, pending review.** J_eta is finite and strictly positive, and

\[
 \boxed{\displaystyle
 Q_0:=Q_{M_0}
   =\left(\frac{2J_\eta}{9}+O_{\alpha,\eta,A0}(L^{-1})\right)
                 \frac{HY}{V_H^2L^4}.}             \tag{10}
\]

The nonprincipal part of Q_0 is `O_D(HY L^(-D))` for every fixed D, relative to the actual accepted (2). The principal term in (10) is derived directly from three separate prime sums. It is not the compact energy center from 018 identified by assertion with a comparison or an unknown prime-pair count.

### Exact rescaling and prefactor

Put phi=lambda/Y in (5) and define

\[
 P_\chi(\lambda)=\frac1{YV_H X}\sum_{a,m,n}
  \eta(a/Y)\alpha_m\beta_n\chi(amn)
       e\!\left(\lambda(a/Y)(mn/H-1)\right).       \tag{11}
\]

Since dphi=dlambda/Y, the exact formula is

\[
 Q_0=YX^2\left\{\frac1{\varphi(H)}\sum_\chi
               \int_{-\Lambda}^{\Lambda}|P_\chi(\lambda)|^2d\lambda\right\}.
 \tag{12}
\]

In particular the unaveraged character sum has prefactor YX^2/phi(H); neither the arc Jacobian nor the full V_H has been lost.

### Common-product Mellin separation and nonprincipal saving

On the support, q=amn/(YX) is in `[2,125/32]`. Choose a fixed smooth w compactly supported in (1,5), equal to one on that interval. Put

\[
 F_\lambda(q)=w(q)e(\lambda q/6),\quad
 \widehat F_\lambda(t)=\int_0^\infty F_\lambda(q)q^{-it}\,dq/q.
\]

Fourier inversion in log q gives `F_lambda(q)=(2pi)^(-1)integral hatF_lambda(t)q^(it)dt`. Separating the marking phase e(-lambda a/Y) therefore proves the exact absolutely convergent identity

\[
 P_\chi(\lambda)=\frac1{2\pi}\int_{\mathbb R}
  \widehat F_\lambda(t)(YX)^{-it}
        B_{\chi,\lambda}(t)M_\chi(t)N_\chi(t)\,dt. \tag{13}
\]

The own-triple phase is exactly the one in (11), not e(lambda mn/H) without its label. Integration by parts in log q gives, for every fixed j,

\[
 |\widehat F_\lambda(t)|\le C_w,\quad
 |\widehat F_\lambda(t)|\le C_j(1+|\lambda|)^j(1+|t|)^{-j},\quad
 \|\widehat F_\lambda\|_1\le C(1+|\lambda|)^2.     \tag{14}
\]

The first bound is uniform in lambda since |e|=1; the other bounds use the fixed compact support and its derivatives.

Choose a fixed frequency cutoff R=L^B with B>A0+2. For the retained part of (13), weighted Cauchy and the first and third bounds in (14) give

\[
 \frac1{\varphi(H)}\sum_{\chi\ne\chi_0}|P^{\rm ret}_\chi(\lambda)|^2
 \le C(1+\Lambda)^2\frac1{\varphi(H)}\sum_{\chi\ne\chi_0}
     \int_{|t|\le R}|B_{\chi,\lambda}(t)M_\chi(t)N_\chi(t)|^2dt.
 \tag{15}
\]

Apply (2) with this B and an arbitrarily high fixed saving. After integration over lambda, the loss is at most L^(3A0). It is paid by selecting the precision in (2) higher before H grows.

For the tail, character averaging must precede any loss of its 1/H. Exact B orthogonality gives, for every real t,lambda,

\[
 \frac1{\varphi(H)}\sum_\chi|B_{\chi,\lambda}(t)|^2
    =\frac1{Y^2V_H^2}\sum_{a\in P}\eta(a/Y)^2
    \ll\frac1{HV_H^2}.                            \tag{16}
\]

Only a=b survives because distinct selected integers are below H. Trivial normalized long bounds are |M_chi|<<1 and |N_chi|<<L at every frequency, so the all-character mean of their product with B is at most `CL^2/(HV_H^2)`. Hilbert-space triangle inequality in the normalized character sum then gives

\[
 \left(\frac1{\varphi(H)}\sum_\chi|P^{\rm tail}_\chi(\lambda)|^2\right)^{1/2}
       \le\frac{CL}{\sqrt H V_H}
                     \int_{|t|>R}|\widehat F_\lambda(t)|dt.
 \tag{17}
\]

By (14) the last integral is at most `C_j(1+Lambda)^j R^(1-j)`. Since B>A0, choosing fixed j sufficiently large makes it smaller than every requested fixed negative power of L, uniformly for |lambda|<=Lambda. Integrating (17) over lambda retains the 1/H, with only fixed logarithmic losses. There is no individual-character bound followed by an unnormalized count of phi(H) characters.

Combining retained and tail pieces, and then multiplying by YX^2 in (12), proves

\[
 Q_{0,{\rm np}}\ll_D HY L^{-D}\quad\text{for every fixed }D>0. \tag{18}
\]

Only the k=1, trivial-twist, v=0 case of the actual 018 theorem was needed. All transform heights, derivative orders and precision choices are fixed before H grows. No noncentral arc or other arithmetic array has been imported.

### Principal model on the growing lambda interval

At chi_0 all character values on the support are one. The effective ordinary PNT used in 018, with real partial summation, replaces the three prime sums by the exact density model

\[
 D_H(\lambda)=-\frac1{V_H}\int_2^{5/2}\eta(u)
       \int_1^{5/4}\int_1^{5/4}
       \frac{e(\lambda u(rs/6-1))}{\log(Yu)\log(Tr)}\,dr\,ds\,du.
 \tag{19}
\]

The missing log(Ts) in the denominator is intentional: beta_n=log n cancels the prime-density logarithm in the s variable. The negative sign is the actual alpha coefficient. The density factors Y,T,T cancel those in (11), leaving precisely 1/V_H.

Here is uniform error accounting. On each fixed scaled support, partial summation of the inspected PNT error against a test of bounded variation costs its size plus total variation, times `exp(-c' sqrt L)` after normalization by its scale. The log-weighted prime version follows by one additional real partial summation, absorbing fixed logarithms into a smaller c'. With two variables held fixed, the phase and its derivative in the remaining scaled variable are O(1+|lambda|), uniformly on this box; eta has fixed derivatives. Telescope the three replacements, using bounded normalized true prime masses or density masses for the remaining factors. Endpoint primes contribute at most a fixed power of L divided by T or Y. Thus for every fixed K,

\[
 \sup_{|\lambda|\le\Lambda}|P_{\chi_0}(\lambda)-D_H(\lambda)|
       \ll_K L^{-K}.                             \tag{20}
\]

All phase costs are fixed powers of L on this lambda range, so effective PNT absorbs them. Hard endpoints in r,s are handled as bounded-variation jumps; no short-interval or AP prime theorem is used. Both true and model sums are O(1/(V_H L^2)) by positivity of their absolute coefficients. Consequently (20) gives arbitrary fixed logarithmic accuracy in their squared lambda integrals after paying the interval length 2Lambda. This is not an unproved compact-time limit extended to a growing interval.

The exact logarithms in (19) are retained until the integrable tail is controlled. Write kappa=rs/6-1. Throughout the box,

\[
 -5/6\le\kappa\le-71/96<0.
\]

Repeated integration by parts in u is uniform in r,s because eta is smooth and compactly supported and kappa stays away from zero. It gives, for every fixed j,

\[
 |A(\lambda)|\le C_j(1+|\lambda|)^{-j},\qquad
 |D_H(\lambda)|\le\frac{C_j}{V_H L^2}(1+|\lambda|)^{-j}. \tag{21}
\]

Moreover the u derivatives, of each fixed order, of
`L^2/(log(Yu)log(Tr))-2`
are O(1/L), uniformly in r,s. The same integration by parts therefore gives the stronger weighted expansion

\[
 D_H(\lambda)=-\frac{2A(\lambda)}{V_H L^2}
    +O_j\left(\frac{(1+|\lambda|)^{-j}}{V_H L^3}\right).
 \tag{22}
\]

This decay justifies both the logarithm expansion and removal of the lambda cutoff in squared integrals; a uniform unweighted O(L^-3) error on a growing interval would not suffice. In particular,

\[
 \int_{\mathbb R}|D_H(\lambda)|^2d\lambda
      =\frac{4J_\eta}{V_H^2L^4}+O\!\left(\frac1{V_H^2L^5}\right).
 \tag{23}
\]

The tails outside |lambda|<=Lambda are smaller than every requested fixed logarithmic power by choosing j in (21) large. Also J_eta>0: A is continuous and `A(0)=(integral eta)delta^2>0`, while (21) makes its square integrable. No unknown pointwise triple count occurs in this continuum constant.

Equations (18)-(23) and (12) first give the all-precision exact-density representation

\[
 Q_0=\frac{YX^2}{\varphi(H)}\int_{\mathbb R}|D_H(\lambda)|^2d\lambda
             +O_D(HY L^{-D}).                     \tag{24}
\]

Finally phi(H)=H/2 and X=H/6, so `YX^2/phi(H)=HY/18`. Substitution of (23) gives factor `4/18=2/9`, proving (10). The full V_H normalization remains explicit; replacing it by its positive limit is optional.

### A consequence for this actual fractional comparison

BOUNDARY-017's exact integer compression applies on these same positive supports. The sole integer cofactor is h=1, with actual amplitude

\[
 C_1=-V_H^{-1}\sum_{m,n\in P_I,\ a=H-mn\in P}
                     \eta(a/Y)\log n.
\]

There is no assumption that this sum is nonempty at a prescribed H. Its honest upper bound, using at most one a for each ordered m,n, is

\[
 |C_1|\le V_H^{-1}\#P_I\sum_{n\in P_I}\log n
                 \ll H/(V_H L).                  \tag{25}
\]

Let f_frac be the actual remaining fractional-cofactor input. The c=1 sector contains no fractional states, so for the full major comparison

\[
 Q_{M_1}=m_{\rm arc}|C_1|^2+Q_{\rm frac}(f).
 \tag{26}
\]

The label-independent square identity makes Q_(M_1)>=Q_0. From (8),(25),

\[
 m_{\rm arc}|C_1|^2
   \ll \frac{H^2L^{3A0-2}}{V_H^2Y}
      =o\!\left(\frac{HY}{V_H^2L^4}\right).       \tag{27}
\]

Indeed their ratio is O(L^(3A0+2)/H), since Y=H/3. Thus (10),(26),(27) prove the new actual-input conclusion

\[
 \boxed{\displaystyle Q_{\rm frac}(f)
      \ge\left(\frac{2J_\eta}{9}+o(1)\right)
                         \frac{HY}{V_H^2L^4}>0.}   \tag{28}
\]

This lower bound is specific to the actual factorable prime arrays and the full major set considered here. It is not a generic fractional-kernel positivity theorem or an asymptotic for Q_(M_1), whose other arcs were not evaluated. It updates the earlier unknown-sign status only on this precise input, through the proved complete-form positivity and central lower bound.

## Failure cases, scope and remaining original problem

Label independence, H-units and the Psi plateau are necessary for the exact square derivation offered here. A joint label/cofactor mask cannot be inserted into (5) as if relabeling preserved it. A character average with a factor allowed to be a nonunit would also need a different orthogonality formula. The nonprincipal estimate is used only in its proved power-of-two, k=1, trivial-twist scope. Its principal term cannot be put into (2): the positive contribution computed in (10) is an exact obstruction to doing so. A dyadic reciprocal normalizer would change the formulas, and r=s remains one ordered product representation.

The finite nonprincipal transport and its tails now connect the actual centered energy to the central additive comparison with its correct YX^2 prefactor. The principal continuum term is proved independently by effective ordinary PNT, rather than equated with a prime-pair main term. Positivity permits the central lower bound to survive adding the other major arcs, despite their unevaluated arithmetic.

The total signed difference is still
`Q_raw-Q_(M_1)=|C_1|^2-Q_(M_1)`.
Neither (10) nor (28) proves a sufficiently small estimate for it or a positive lower bound for C_1. The raw boundary may be empty; the comparison has genuine fractional states and can remain positive regardless. Assuming the missing difference estimate to infer C_1>0 would be circular here. Even such a nonempty raw block would count prime a plus the composite Vaughan product mn, not two prime summands. Polynomial-sieve Type I, the remaining minor comparison and the original correctly centered rough prime margin remain separate.

The next exact mathematical obligation is a bound for that raw-minus-full-major remainder, or a rigorous account of its failure, on the actual polynomial arrays while retaining (10)'s nonzero principal term. No estimate of the original Goldbach R/E0/H0 or F pointwise margin, global novelty, demonstrated breakthrough or goal completion is established by this stage.
