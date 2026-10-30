# Reflected major comparison and arithmetic energy

29 October 2026. Registry role: Mathematician, `GOLDBACH-ENERGY-012`, author stage. Two candidates are proved below relative to explicitly named classical inputs, pending distinct review: the exact major-comparison reduction, and the energy bound under a selected zero-free strip, with that strip supplied on a stated small-radical class. General H retains the zero-free hypothesis. The reduction uses the definition of the comparison, independently of PAIRING-011. No full Guo/LWW theorem, actual-prime theorem, Goldbach conclusion or novelty is imported.

## Parameters, arithmetic coefficients and assurance of inputs

Let H tend to infinity, `L=log H`, `H/L^B<=X=MN<=H`, up to fixed endpoint constants, and `M,N>=H^{1/5-o(1)}`. Write `V0=X^{1/5}`, `Z=exp(L^{3/4})`, and `R_Z(n)=1_(P^-(n)>Z)`, with R_Z(1)=1. Let I_M,I_N be arbitrary subintervals of the respective dyads. For fixed `|v|<=L^{2B}` the actual coefficients are

\[
 \alpha_m=\mu(m)R_Z(m)\mathbf1_{(m,H)=1}m^{iv},\qquad
 \beta_n=c_{V0}(n)R_Z(n)\mathbf1_{(n,H)=1}n^{iv},
 \quad c_{V0}(n)=\sum_{d\mid n,\ d>V0}\Lambda(d).
\]

They vanish outside I_M,I_N. Their bounds are 1 and O(L), since `c_V0(n)<=log n`. Their roles are kept: no exchange turns an arbitrary bounded coefficient into the Mobius coefficient.

The marking primes are the fixed disjoint eligible bands from MOMENTS-010, avoiding H, with masses V_i and `V_mark=prod_i V_i`. Their one-per-group product b is selected by fixed real smooth eta(b/Y), supported in [1,4]. They are eventually units modulo every k<=L^{A0}; the long sifted variables are units there too. At each fixed k and fixed characters psi modulo q=kH and omega modulo k set `psi2=psi*omega` and

\[
 B_\xi(t)=\frac1{YV_{\rm mark}}\sum_b\eta(b/Y)e(-\lambda b/Y)\xi(b)b^{it},
\quad M_\xi(t)=M^{-1}\sum_m\alpha_m\xi(m)m^{it},
\quad N_\xi(t)=N^{-1}\sum_n\beta_n\xi(n)n^{it}. \tag{1}
\]

The uniform ranges are `|lambda|<=2L^{A0}`, `|t|<=T0=L^{B1}`, and the same statements after conjugation/sign reversal of the displayed phases. Every Gram family below fixes psi once; psi2 is fixed in that energy family as well.

The smooth determinant cutoff in Q_maj is denoted capital Psi below, to distinguish it from a character psi.

Imported number-theoretic bounds are precisely these inspected primary statements:

* Published MSTT Lemma 3.9(ii), as recorded in `primary-inputs.md`: for fixed alpha in (0,1], any precision P, `q<=log^P W`, `1<=r<=W`, all characters modulo q, and `|t|<=W`, its weighted Mobius sum has a supremum over **subintervals** of `[W^alpha,2W^alpha]`, bounded by `W^{alpha/2}log^{-P}W`.
* The inspected Heath-Brown primary introduction's ordinary Burgess r=2 bound for primitive nonprincipal characters at arbitrary modulus: an interval of length T has sum `O_epsilon(T^{1/2}q^{3/16+epsilon})`.
* Iwaniec's inspected original Theorem 2 is used only for the small-radical specialization below, with its exact width and possible real exception.

Their theorem statements, not their complete published proofs, were inspected in the primary PDFs and independently checked where recorded. The author-provided [Koukoulopoulos primary book, Theorem 11.1 and definition (11.3), printed page 111](https://www.dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf), was also visually inspected by the root for primitive nonprincipal entire continuation and the completed functional equation, with the conjugate character at 1-s. Standard order/growth and Hadamard factorization of that completed function remain explicitly declared classical background; this is not a full book or Hadamard-proof audit. The needed local zero count/logarithmic-derivative and Perron consequences are reconstructed below. Ordinary polynomial mean values used here have elementary proofs; no stronger mean-value theorem or Polya-Vinogradov input is imported.

## Candidate 1: exact major-comparison reduction

**Proved, pending review.** For the full H-fold pullback comparison Q_maj of PAIRING-011, a uniform energy bound

\[
 \mathcal E(\psi,\psi_2):=\frac1{\phi(H)}\sum_{\chi\bmod H}
     \int_{|t|\le T0}|B_{\chi\psi_2}(t)M_{\chi\psi}(t)
                                  N_{\chi\psi}(t)|^2dt
          \ll_A L^{-A}/H \tag{2}
\]

at sufficiently large fixed precision implies `|Q_maj|<<_D HY L^{-D}`. The comparison scale before logarithmic costs is `YX^2 mathcal E`. This assertion estimates no energy by itself.

### Units, fiber characters and classwise Cauchy

Reduction `G=(Z/kH Z)^* -> (Z/H Z)^*` is surjective, even when k and H share primes. At each prime dividing H, any unit residue lifts to its higher prime-power modulus; primes of k absent from H can be assigned a unit residue independently by CRT. Its kernel K_f has size

\[
 r_f=\phi(kH)/\phi(H)
       =k\prod_{p\mid k,\ p\nmid H}(1-1/p)\le k. \tag{3}
\]

Every character of this kernel extends to G. To see this without a cyclic-modulus assumption, adjoin one element g at a time to a subgroup already carrying a character; if g has quotient order d, choose a d-th root of the assigned value at g^d. The resulting character on the generated subgroup is well-defined. Iterate to G.

Choose these extensions psi_eta once, independently of the class a modulo H. In the fiber of a choose a unit representative a_tilde. Expanding `w -> e(h a_tilde w/(kH))` on K_f gives coefficients c_(a,eta), of modulus at most one, and hence

\[
 e(hu/(kH))=\sum_{\eta\in\widehat K_f}
      c_{a,\eta}\psi_\eta(\widetilde a)^{-1}\psi_\eta(u)
          \quad(u=a\pmod H). \tag{4}
\]

The coefficients depend on a. For arbitrary class-indexed X_(a,eta), use **before Parseval**

\[
 \sum_a\left|\sum_\eta c_{a,\eta}
          \psi_\eta(\widetilde a)^{-1}X_{a,\eta}\right|^2
       \le k\sum_\eta\sum_a|X_{a,\eta}|^2. \tag{5}
\]

Thus no class-dependent coefficient is relabeled as one global twist. Additive marking phases `e(-hb/k)` and its a-side conjugate expand in characters modulo k, with total absolute coefficient mass at most k on each side. Coarse accounting of (5), its at most k extensions and these two marking sums costs at most k^4. Only after (5) does character orthogonality modulo H give energies with long twist psi_eta and marking twist psi_eta*omega.

### Two Mellin variables at the natural scale

Write `u1=bmn`, `u2=ars`, and `kappa=X/H`. Their normalized values `u_i/(YX)` lie in [1,16]. In the rational arc `phi=h/k+lambda/Y`, the phase is

\[
 e(h(u_1-u_2)/(kH))e(-h(b-a)/k)
 e(\lambda(u_1-u_2)/(HY))e(-\lambda(b-a)/Y),
\]

and the cutoff is `Psi((u1-u2)/(HY))`. For a fixed smooth varpi equal to one on [1,16], with compact support inside (0,infinity), put

\[
 F_\lambda(l,l')=\varpi(e^l)\varpi(e^{l'})
   \Psi(\kappa(e^l-e^{l'}))
   e(\lambda\kappa(e^l-e^{l'})).
\]

Its support in l,l' is fixed and its derivatives cost only fixed powers of `L^{A0}`, because kappa<=1. In particular there is no positive power of H/X. With the ordinary two-dimensional Fourier transform,

\[
 F_\lambda(l,l')=\int_{\mathbb R^2}\widehat F_\lambda(s,t)
                                   e^{isl}e^{itl'}\,ds\,dt. \tag{6}
\]

At `l=log(u1/(YX))`, `l'=log(u2/(YX))`, the first product has frequency s and the conjugated second product has frequency -t. These are two separate variables; positivity or convolution structure is not assumed. Integration by parts yields, for a fixed B0 and every fixed j, bounds by a fixed logarithmic factor times

\[
 (1+|s|/L^{B0})^{-j}(1+|t|/L^{B0})^{-j}. \tag{7}
\]

Choose fixed B1>B0 sufficiently large. Truncation to `|s|,|t|<=L^{B1}` has arbitrarily small logarithmic error by increasing j.

For clarity, let S_a(s,omega) be the normalized product sum of the b,m,n side in residue a modulo H, with normalization `1/(Y V_mark MN)`, the marking phases `e(-lambda b/Y)omega(b)`, the additive product phase `e(hu1/(kH))`, and frequency `(u1/(YX))^{is}`. After (4)-(5), Parseval gives the squared norm of each extended class sum as

\[
 \frac1{\phi(H)}\sum_\chi
       |B_{\chi\psi_\eta\omega}(s)M_{\chi\psi_\eta}(s)
                                     N_{\chi\psi_\eta}(s)|^2.
\]

The omitted `(YX)^{-is}` has modulus one. Cauchy in the residue a, followed by `2ab<=a^2+b^2`, bounds the bilinear expression from (6) by these energies at s and -t. The marginals of `|Fhat|` have logarithmically bounded suprema, so integration in the other variable leaves (2), with fixed logarithmic costs. Every extension is held fixed inside its energy argument and subsequent Gram family.

The normalized product sums have scale YMN=YX. The rational-arc displacement has measure `d lambda/Y`. Thus the exact prefactor is

\[
 (YX)^2/Y=YX^2. \tag{8}
\]

One may partition the union of arcs into measurable disjoint pieces of its rational-arc cover. Enlarging pieces only after taking absolute values gives at most `O(L^{2A0})` arcs, lambda-length `O(L^{A0})`, and k^4<=L^{4A0}. The transform integrals add fixed logarithmic costs. This handles overlaps without falsely counting the union as an exact sum of overlapping integrals.

For tails, a product coefficient at u is bounded by `C_K L tau_3(u)/(YX)` and its squared norm is `O_K(L^{10}/(YX))`. Each H-residue has `O(YX/H+1)` terms. Pointwise class Cauchy therefore gives, uniformly at **all** real frequencies,

\[
 \phi(H)^{-1}\sum_\chi|BMN|^2
         \ll_K L^{B+10}/H. \tag{9}
\]

Here `sum_{n<=W}tau_3(n)^2<<W log^8(2W)` follows from `tau_3^2<=tau_9`; a pair of prime-exponent distributions admits a nonnegative 3-by-3 contingency matrix, proving the coefficient inequality. Equation (7) with (9) bounds the discarded tails. Consequently (2) with `A=D+O(A0+B1+B)` gives `|Q_maj|<<YX^2 L^{-D}/H<=HY L^{-D}`. Fixed endpoint constants in X only alter fixed constants and the bounded number of terms per H-class.

## Candidate 2: arithmetic energy with an explicit zero-free input

For fixed A0,A1,C1,C2 define ZF to mean: every primitive nonprincipal character of conductor `q*|kH`, `k<=L^{A0}`, `q*>L^{A1}`, has no zero in

\[
 \Re s\ge1-C_1\log L/L,\qquad |\Im s|\le L^{C_2}. \tag{10}
\]

**Proved relative to the named classical inputs, pending review.** For each requested energy precision A there are fixed C1,C2 such that ZF implies (2), uniformly in the specified arithmetic coefficients, intervals, lambda and fixed twists. For general H this is conditional on (10). For `rad(H)<=L^C`, with fixed C, choosing `A1>A0+C` establishes (10) from the inspected Iwaniec theorem and therefore gives (2) on that class without the selected-strip hypothesis as an additional assumption. This is not a claim about all H or about actual primes.

### Elementary mean values and sparse points

We will use two elementary estimates. First, for coefficients supported on n<=4H, orthogonality and pointwise Cauchy give

\[
 \sum_{\chi\bmod H}\int_{-T}^T
       |\sum_n a_n\chi(n)\psi(n)n^{it}|^2dt
          \le8T\phi(H)\sum_n|a_n|^2. \tag{11}
\]

Each unit residue has at most four terms; a fixed endpoint enlargement only changes this fixed number. For support n<=H there is at most one term per unit residue. Second, for any polynomial of length W,

\[
 \int_{-T}^T|\sum_{n\le W}a_n n^{it}|^2dt
       \ll(T+W\log(2W))\sum_n|a_n|^2. \tag{12}
\]

Indeed an off-diagonal integral is at most `2/|log(m/n)|<=2W/|m-n|`; its absolute row sum is O(W log(2W)), and `2|a_m a_n|<=|a_m|^2+|a_n|^2` proves (12). No imported ordinary mean-value theorem is needed.

For one-spaced real points t_j, disjoint radius-one-half intervals and the identity for the derivative of |F|^2 give

\[
 \sum_j|F(t_j)|^2\le\int|F|^2
                  +2(\int|F|^2)^{1/2}(\int|F'|^2)^{1/2}, \tag{13}
\]

over the range enlarged by one. Select a maximum of |BMN| in each unit interval for each character, and split even/odd intervals. Each family P has one-spaced points for each fixed chi; their sum bounds the original integral. All later estimates treat each family separately.

### Sparse exceptional marking values

Fix a large precision A_s and let E consist of points in P with `|B|>L^{-A_s}`. Put `j=floor(L/log(16Y))`. The polynomial B^j has support at most H and squared coefficient norm

\[
 \sum_u|c_u^{(j)}|^2
       \le(j!)^K(\sum_b|c_b|^2)^j
       \le(j!)^K(C_B^2/(16Y))^j. \tag{14}
\]

Choose a fixed C_B to cover eta and V_mark. In each band the j prime factors of u, including repetitions, have at most j! assignments to the ordered slots; this proves (14) without assuming all primes distinct. The character is evaluated at the product u, not raised to its j-th power. Apply (11),(13) to B^j; its derivative inserts log u<=L. As `(16Y)^j<=H<(16Y)^{j+1}`,

\[
 |E|\le L^{2jA_s}C L(T0+1)16Y C_B^{2j}(j!)^K,
 \qquad |E|\le\exp(L^{0.9}) \tag{15}
\]

eventually. In fact its logarithm is `O_(K,A_s)(L^{1-a_K}log L)`, and the strict fixed inequality a_K>0.1 absorbs it. Constants and thresholds can depend on the fixed band exponents.

Outside E, the squared coefficient norm of M*N is `O(L^5/X)`. Equations (11),(13), and `X>=H/L^B`, bound the bulk by

\[
 \sum_{P\setminus E}|BMN|^2
       \ll \frac{\phi(H)}H L^{-2A_s+B_1+B+8}. \tag{16}
\]

No arithmetic coefficient cancellation is needed for this bulk step.

### Same- and distinct-character Gram rows

For a fixed long twist psi, take sparse points `(chi_r,t_r)` in E and set `xi_r=chi_r psi` modulo q=kH. For a polynomial of length W on `(W,8W]`, a fixed smooth majorant w0 on `[W/2,16W]` and Hilbert-space duality give

\[
 \sum_r|\sum_n a_n\xi_r(n)n^{it_r}|^2
       \le\|a\|_2^2\max_r\sum_s|G_{rs}|,
 \quad G_{rs}=\sum_n w_0(n)\xi_r(n)\overline{\xi_s(n)}n^{i(t_r-t_s)}.
                                                               \tag{17}
\]

Cauchy on the coefficient vector followed by the absolute Hermitian row-sum bound proves (17). Its use keeps psi fixed. If twists were changed with r, distinct chi could give identical xi and the next nonprincipal argument would fail.

On the diagonal, G is O(W). For the same character and tau=t_r-t_s, expand the unit indicator over d|rad(q). Euler summation of `w0(dm)m^{i tau}` has error O(1+|tau|). Two integrations by parts in the integral give `O((W/d)(1+|tau|)^{-2})`. Thus

\[
 |G_{rs}|\ll W(1+|\tau|)^{-2}\log L+	au(q)(1+|\tau|).
\]

Here `sum_{d|q}1/d<<log log q`: primes up to log q use the Mertens upper product, and the remaining product is bounded by the logarithmic divisor budget. One-spacing gives total same-character row `O(W log L+T0^2 tau(q))`. The second term is o(W) at every length used below.

For distinct chi the quotient is nonprincipal because psi is fixed. If induced by primitive xi* of conductor q*>1, its exact missing-prime expansion is

\[
 \sum_{n\le y}\xi(n)=\sum_{d|q_1}\mu(d)\xi^*(d)
                  \sum_{m\le y/d}\xi^*(m),
 \quad q_1=\prod_{p|q,\ p\nmid q^*}p.
\]

Burgess r=2 and `tau(q)=H^{o(1)}` therefore give a prefix bound

\[
 \max_{y\le16W}|\sum_{n\le y}\xi(n)|
       \ll_\epsilon W^{1/2}H^{3/16+\epsilon+o(1)}.
\]

Partial summation of the smooth weight and phase costs O(1+T0). Hence the distinct-character row is at most

\[
 |E|L^{O(1)}W^{1/2}H^{3/16+\epsilon+o(1)}=o(W) \tag{18}
\]

whenever W has a fixed power margin above H^{3/8}. This uses only the inspected arbitrary-modulus r=2 theorem, not a stronger mean-value variant or a Polya-Vinogradov input.

Take eta0=1/40 and fix epsilon<eta0/8. Using coefficient squared norms `O(1/M)`, `O(L^8/M^3)` and `O(L^2/N)` in (17) gives respectively

\[
 \begin{array}{ll}
 M\ge H^{3/8+\eta_0}:&\sum_E|M|^2\ll\log L,\\
 &\sum_E|M|^6\ll L^9,\\
 N\ge H^{1/2+2\eta_0}:&\sum_E|N|^2\ll L^2\log L.
 \end{array} \tag{19}
\]

The middle line uses W=M^3>=H^{3/5-o(1)}, hence the margin in (18) is stronger. The coefficients of M^3 are at most tau_3(u)/M^3 and have the stated norm by `tau_3^2<=tau_9`. Its character is still xi at the product u. The last line likewise has W=N>=H^{0.55}, more than enough for Burgess. The factor exp(L^{0.9}) in (15) and all missing-prime factors are absorbed by these fixed negative powers.

### Small-conductor sifted Mobius input in the actual interval range

For a primitive character xi* of conductor at most L^{A1}, apply the exact MSTT interval statement directly. At a dyadic length D0>=H^{1/12}, choose `W_*=D0^{R_*}`, `alpha=1/R_*`, r=1, with fixed R_* sufficiently large for the requested frequency ceiling. Its free input precision P covers both the conductor ceiling and the desired logarithmic saving. It gives the weighted sum with `1/sqrt n` on every subinterval of `[D0,2D0]`. Partial summation against the **real** factor sqrt n removes this coefficient at cost O(sqrt D0), giving

\[
 \sup_{I\subset[D0,2D0],\ |u|\le H^{C_t}}
       |\sum_{n\in I}\mu(n)\xi^*(n)n^{iu}|
       \ll D0 L^{-P'} . \tag{20}
\]

For instance `R_*>12(C_t+1)` suffices for the frequency range. The phase is not differentiated. No unsupported conversion of a full-dyad estimate to arbitrary translated intervals is used.

The prime-by-prime identity

\[
 \mu(n)R_Z(n)=\sum_{d|n,\ P^+(d)\le Z}\mu(n/d)
\]

then gives the same arbitrary logarithmic saving at M>=H^{1/6}, including subintervals. For d<=sqrt M, use (20) at D0=M/d>=H^{1/12} and sum the smooth reciprocal mass O(log Z). For larger d the integer count is O(M/d), even near 2M. Rankin at exponent 1/log Z gives reciprocal tail

\[
 \ll\log Z\exp(-\log M/(2\log Z))
       \ll L^{3/4}e^{-cL^{1/4}}.
\]

The Euler-product bound here follows from Mertens and the bounded change from p^{-1} to p^{-1+1/log Z}. Removing the H-unit indicator on Z-rough support costs at most `O(M omega(H)/Z)`. On the original support, the imprimitive character equals xi*: the primes of k are below Z, and H-units exclude all remaining missing primes. This proves for every fixed P'

\[
 \sup_{|t|\le T0+1}|M_{\chi\psi}(t)|\ll L^{-P'}
            \quad\text{if }\operatorname{cond}(\chi\psi)\le L^{A1}. \tag{21}
\]

It includes principal inducing character, through the actual Mobius input. For fixed psi there are at most L^{2A1} such chi: the inducing primitive character determines the character chi on units, and its possible conductors/characters have that elementary total bound. Ordinary mean value (12) on B*N, whose coefficient squared norm is O_K(L^5/(YN)), gives `int|BN|^2<<_K L^6`. The extra logarithm from (12) is retained. Taking P' sufficiently large proves energy `O_A(L^{-A}/H)` from all these small conductors, using `H/phi(H)<<log L`.

### Perron prime sums from the selected strip

We spell out the classical L-function consequences used for large conductors. From the foundational completed-L Hadamard product and functional equation one obtains

\[
 N(t+1)-N(t-1)\ll\log(q^*(|t|+3)),\quad
 \frac{L'}L(s,\xi^*)=
       \sum_{|\gamma-\Im s|\le1}\frac1{s-\rho}
           +O(\log(q^*(|\Im s|+3))) \tag{22}
\]

for 1/2<=Re s<=2 away from zeros. Here is a derivation of the needed form. Jensen in a fixed disk centered at 2+it bounds nearby completed-L zeros by O(log(q*(|t|+3))). The lower bound at the center follows from the absolutely convergent Euler product; the upper bound in that disk follows from the functional equation, Stirling, and polynomial growth in a fixed strip. Subtract the Hadamard logarithmic derivatives at s and 2+it. Zeros with vertical distance above one contribute an absolutely convergent sum bounded by the preceding local count times a summable inverse-square tail. The nearby zeros remain explicitly, and the gamma factor contributes O(log(q*(|t|+3))). This proves (22). These steps use the stated structural completed-L theory; no unproved zero-free assertion is inserted into them.

For a primitive nonprincipal inducer satisfying (10), put `u=t+v`, `|u|<=L^{C3}`, where `C3=max(B1,2B)+1`, and choose `C2>=C3+2`. Set `c=1+1/L`, `sigma0=1-C1 log L/(2L)`, `T=L^{C2}-L^{C3}-1`. On the contour between c and sigma0, at height at most T after twisting, every nearby zero in (22) is horizontally separated by at least `C1 log L/(2L)`. Since q*<=HL^{A0}, (22) gives `|L'/L|<<L^2` after a fixed threshold.

Truncated Perron for `F(s)=-(L'/L)(s-iu,xi*)` yields, uniformly for `H^{1/6}<=y<=H`,

\[
 \sum_{n\le y}\Lambda(n)\xi^*(n)n^{iu}
   =\frac1{2\pi i}\int_{c-iT}^{c+iT}F(s)y^s\frac{ds}s
          +O(yL^2/T+\log y). \tag{23}
\]

The truncation kernel follows by integrating z^s/s and closing past its pole: its error is bounded by `z^c min(1,(T|log z|)^{-1})`. Use a half-integer endpoint with the same integer sum; in the near-y range harmonic summation with `Lambda(n)<=log n` gives the displayed error, and the far tail uses `sum log(n)n^{-1-1/L}<<L^2`. Thus integer and near-integer endpoints are covered without a relative short-interval prime theorem.

Shift to sigma0. There is no zero pole by (10), no principal pole because the inducer is nonprincipal, and sigma0>1/2 eventually. The vertical contribution is `O(y^{sigma0}L^3)` and the horizontals `O(yL^2/T)`. Since `log y>=L/6`, `y^{sigma0}<=yL^{-C1/12}`. Passing to an imprimitive character modulo kH changes prime-power coefficients only at primes dividing kH, of total `O(L^2)`. We conclude

\[
 \sum_{n\le y}\Lambda(n)\xi(n)n^{iu}
       \ll yL^{3-C1/12}+yL^{3-C2}+O(L^2). \tag{24}
\]

This is never applied to a principal inducer. An ordinary width c/log q would not give arbitrary logarithmic saving at these lengths; (10) is the exact conditional input.

For N, expand the actual long-prime-factor coefficient:

\[
 N_\xi(t)=N^{-1}\sum_{k'<2N/V0}R_Z(k')\mathbf1_{(k',H)=1}
       \xi(k')(k')^{iu}
       \sum_{\ell\in I_{k'},\ \ell>V0}
             \Lambda(\ell)R_Z(\ell)\mathbf1_{(\ell,H)=1}
                                 \xi(\ell)\ell^{iu}. \tag{25}
\]

Here I_k' is the original supported n interval divided by k', intersected with `(V0,infinity)`. Its endpoints are between V0 and 2N, its ratio is at most two, and V0>=H^{1/6}, 2N<=H eventually. Dropping the inner sifting/unit restrictions costs O(Z+L): each prime has at most one power in a ratio-two interval, the small-prime logarithmic sum is O(Z), and prime divisors of H have total logarithm at most L. After the k' sum this costs O((Z+L)/V0), negligible at every fixed logarithmic precision. Differences of endpoint bounds (24), not a relative estimate in the interval's own length, control every I_k'. Summing their harmonic k' costs O(L).

Thus, choosing C1,C2 sufficiently large in terms of any requested D_N and C3,

\[
 \sup_{|t|\le T0+1}|N_{\chi\psi}(t)|\ll L^{-D_N}
           \quad\text{if }\operatorname{cond}(\chi\psi)>L^{A1}.
                                                               \tag{26}
\]

For example `C1>=12(D_N+10)`, `C2>=max(D_N+10,C3+2)` suffice. All endpoint, imprimitive, prime-power and smooth restriction costs have been retained.

### Assembly and order of constants

Choose A_s large enough to make (16) smaller than the requested energy. Large-conductor exceptional points satisfy (26). If `M>=H^{3/8+eta0}`, (19) bounds their sum by `O_K(L^{-2D_N}log L)`. Otherwise `N>=H^{5/8-eta0}/L^B>=H^{1/2+2eta0}` eventually. Holder gives

\[
 \sum_E|BMN|^2
 \ll_K\sup_E|N|^{2/3}
            (\sum_E|M|^6)^{1/3}(\sum_E|N|^2)^{2/3}
       \ll_K L^{6-2D_N/3}. \tag{27}
\]

Divide by phi(H), whose reciprocal is O(log L/H). Taking D_N sufficiently large proves (2) from these points. The bulk is (16); small conductors are (21). The two sparse point families cover the original integral.

One noncircular choice is: fix A0,B,B1,K,bands and the desired energy A; choose A1 as the selected conductor cutoff; take `A_s=A+B1+B+30`, and `D_N=3(A+B1+B+A1+30)`; choose C3 as above and then C1,C2 as after (26); finally choose the freely available MSTT precision for (21). Burgess epsilon is a fixed small fraction of eta0. All constants and thresholds may depend on these fixed data. One fixed zero-free width only proves the precisions it supports; no claim of all precisions from one fixed C1 is made.

### The primary-established small-radical class

Suppose `rad(H)<=L^C`. The original inspected Iwaniec theorem has

\[
 \vartheta^{-1}=4\cdot10^4\{
       \log\operatorname{rad}(q^*)+
       (\ell\log(2\ell))^{3/4}\},\qquad
 \ell=\log(q^*(|t|+3)),
\]

and any nonprincipal exception in `Re s>1-vartheta` is a real character with a real simple zero. For every `q*|kH`, k<=L^{A0}, its radical is at most L^{A0+C}, its size at most HL^{A0}, and ell<=2L at the required fixed height. Thus `vartheta>>L^{-3/4}(log L)^{-3/4}`, which strictly dominates `C1 log L/L` for every fixed C1.

A real primitive character has conductor at most eight times its radical: its odd-prime character factors through the prime because the higher unit kernel has odd prime-power order, and its 2-primary real character factors through modulus eight. Therefore choosing fixed `A1>A0+C` excludes every possible real primitive exception above L^{A1}, eventually. The desired closed rectangle (10) lies strictly inside the printed open region. Conductors 1 and 2 are below the cutoff and are treated by (21), not by this nonprincipal theorem. This deduction covers all conductors dividing kH, including extra odd primes of k; it is not limited to powers of two.

Accordingly the selected strip, then (2), and then the comparison bound of Candidate 1 hold on this small-radical class from the inspected classical statements and the proof above. General H remains conditional on (10). The original Iwaniec theorem statement, not its full proof, was visually inspected as recorded in `iwaniec-primary-statement.md` and `source-provenance.json`; this qualification is retained.

## Limits and next arithmetic interface

This report proves no zero-free assertion for general H. Its small-conductor branch depends essentially on the actual Mobius coefficient, not arbitrary bounded arrays. Every sparse Gram family has fixed twists; mixing class-dependent fiber coefficients or changing psi between points would invalidate that argument. The transform and energy normalizations are those displayed, including 1/Y arc measure and YX^2 prefactor.

The candidates are independent analytic statements about Q_maj and its arithmetic energy, pending main review and finite normalization checks. Combining them with PAIRING-011 is a subsequent use of that stage's actually accepted scope, not part of the definition of the analytic reduction. Even an accepted combination leaves Type-I/decomposition, eventual weight removal and an actual-prime theorem. The original polynomial-rough lower margin, h=1 prime boundary and nonzero centers remain. The source has close prior conditional framing; novelty is unverified, and no Goldbach proof or demonstrated breakthrough is claimed.
