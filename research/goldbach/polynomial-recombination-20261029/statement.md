# Exact polynomial Vaughan recombination and the first prime-margin obstruction

29 October 2026. Actual registry Mathematician, GOLDBACH-RECOMBINE-020, propose stage. Two bounded candidates are given: the exact polynomial-sifted decomposition with every prime-power/profile correction, and a refutation of a profilewise one-sided transfer from the positive balanced composite term to the original prime count. Both await the distinct critic. The original pointwise prime margin is not proved.

Assurance is a complete elementary author derivation using the accepted local identities and the reviewed continuation upper bound, not formal verification or external peer review. Usage is unknown. No new source search, numerical search, experiment, paid call, publication or external message was performed. All frozen 008-019 evidence is unchanged. PRINCIPAL-019 is parallel author work, not an accepted input here.

## Exact target and accepted inputs

Let H be even, L=log H, alpha in [3/10,1/3), z=H^alpha, and \(R_z(n)=1_{P^-(n)>z}\), with \(R_z(1)=1\). Let nu count distinct prime factors and Omega count prime factors with multiplicity. The polynomial roughness indicator is completely multiplicative.

Among actual prime summands p with q=H-p>1 and R_z(q)=1, let R count prime q, E0 count squarefree semiprime q, and H0 count squarefree three-prime q. All these are unweighted ordered-summand counts. The three-factor count H_alpha also includes nonsquarefree triples. Define

\[
 G_\rho(w)=1_{H-w>1}\mu(H-w)R_z(H-w)
                  \nu(H-w)\rho^{\nu(H-w)-1},\qquad 0<\rho<1.
 \tag{1}
\]

The value is zero if nu=0. On the admitted squarefree complement profiles its values are -1, 2rho, -3rho^2. Since four prime factors exceeding z have product greater than H, the exact LABELS-005 identities are

\[
 Z_\rho=\sum_{p\text{ prime}}G_\rho(p)
       =-R+2\rho E_0-3\rho^2H_0,
 \qquad R=-3Z_{1/4}+3Z_{1/2}-Z_{3/4},
 \tag{2}
\]
\[
 F_0=R+H_0=-\frac{17}3Z_{1/4}+\frac{25}3Z_{1/2}
                                      -\frac{11}3Z_{3/4}.
 \tag{3}
\]

Here F0 is the squarefree odd-complement count. The full odd-complement count is \(F=F_0+(H_\alpha-H_0)=R+H_\alpha\). Thus \(R=F-H_\alpha=F_0-H_0\) exactly; nu and Omega are not interchanged. The nonsquarefree complement population is at most \(H/(z-1)\), by summing \(H/r^2\) over integers r>z, so its count is \(o(H/L^2)\).

The accepted continuation revision states: there are absolute effective but numerically unspecified C,N0 such that every even H>=N0 and every epsilon in [0,1/30], alpha=1/3-epsilon, satisfy

\[
 H_\alpha(H)\le \omega_{>H^\alpha}(H)
        +C\mathfrak S(H)\frac H{L^2}
                          (\varepsilon+1/L)^2,\qquad
 \omega_{>H^\alpha}(H)\le3.
 \tag{4}
\]

The exceptional prime summands dividing H are counted globally once. Write \(A_H=\mathfrak S(H)H/L^2\). For fixed epsilon, (4) gives limsup H_alpha/A_H<=C epsilon^2. Epsilon must be fixed before H tends to infinity; neither C nor a pointwise lower margin has a numerical value here. This is an accepted upper bound, not a pointwise asymptotic.

The actual accepted TYPEI-013 revision supplies its exact Vaughan convolution identity. Its subpolynomial Type-I estimate is not imported after changing the sieve to R_z. COFACTORS-015 and BOUNDARY-017 distinguish the positive selected composite-variable block from the original prime summand. CENTERED-018 revision SHA256 a45b012cbd701675ce6746f060bedd7777f5075ca8cb96ab3fd903b5d40407d3 supplies only its exact balanced k=1 prime-factor energy on H=2^ell, with trivial fixed twists, arbitrary real marking lambda and common |v|<=L^C for fixed C. Its principal term is retained, with an explicit positive asymptotic only on fixed compact time intervals at v=lambda=0. No full signed comparison or prime-count main term is imported.

## Candidate 1: exact polynomial decomposition and complete cancellation table

**Proved, pending distinct review.** Let J=(y,t], y<t<=2y, t<H, where y is comparable to H, and put U=V0=y^(1/5). For all sufficiently large H, U,V0<z<y. The same algebra works for y>=H/L^B with each fixed B. For any bounded test function g on positive integers less than H, including g=G_rho, the polynomial Vaughan terms satisfy

\[
 \sum_{w\in J}\Lambda(w)R_z(w)g(w)=T_1(g)+T_3(g),\qquad T_2(g)=0,
 \tag{5}
\]
\[
 T_1(g)=\sum_{w\in J}R_z(w)(\log w)g(w),
\]
\[
 T_3(g)=\sum_{\substack{m>U,\ n>V0\\ mn\in J}}
           \mu(m)R_z(m)(\log n)R_z(n)g(mn).
 \tag{6}
\]

These are exact equalities before any rectangle split. The shifted arithmetic test, positivity endpoint and product dyad remain in g(mn) and the displayed condition; no joint cutoff is inserted into a factorable operator by assertion.

### Derivation

The elementary convolution identity is

\[
 \Lambda=\Lambda_{\le V0}+\mu_{\le U}*\log
          -\mu_{\le U}*\Lambda_{\le V0}*1
          +\mu_{>U}*\Lambda_{>V0}*1.
 \tag{7}
\]

Indeed \(\log=1*\Lambda\), \(\mu*1=\delta_1\), and the last three terms equal Lambda_>V0 after cancellation. On w>y the first term vanishes. Since R_z is completely multiplicative, it distributes exactly to every convolution factor.

If d<=U and R_z(d)=1, then d=1: every nontrivial such d has a prime divisor at most d<z. Thus only d=1 survives in T1. In T2, any ell with Lambda(ell) nonzero has a prime-power base at most ell<=V0<z, so R_z(ell)=0. Consequently T2 is identically zero, not merely small.

On R_z(n)=1, every prime-power divisor ell>1 of n exceeds z>V0. Hence

\[
 c_{V0}(n)=\sum_{\ell\mid n,\ \ell>V0}\Lambda(\ell)
          =\sum_{\ell\mid n}\Lambda(\ell)=\log n.
 \tag{8}
\]

Moreover rough m,n>1 automatically exceed U,V0. Therefore the coefficient of a fixed rough w>1 in T3 is

\[
 a_3(w)=\sum_{\substack{d\mid w\\1<d<w}}\mu(d)\log(w/d)
       =\Lambda(w)-\log w.
 \tag{9}
\]

The last equality includes d=w with its zero log1 term and uses mu*log=Lambda. It is an exact arithmetic coefficient identity for every bounded g, not a statistical independence statement.

### All profiles with Omega<=3

Write a=log r, b=log s, c=log u; distinct letters in a row denote distinct primes, all exceeding z. The coefficients are before multiplication by the common g(w).

| Original variable w | T1 coefficient | Individual T3 divisor contributions | Total T3 | T1+T3 |
| --- | --- | --- | --- | --- |
| r | a | none | 0 | a |
| r*s, r!=s | a+b | m=r gives -b; m=s gives -a | -(a+b) | 0 |
| r^2 | 2a | m=r gives -a; m=r^2 has mu=0 | -a | a |
| r*s*u, all distinct | a+b+c | single-prime m give -(b+c)-(a+c)-(a+b); two-prime m give c+b+a | -(a+b+c) | 0 |
| r^2*s, r!=s | 2a+b | m=r gives -(a+b); m=s gives -2a; m=r*s gives +a | -(2a+b) | 0 |
| r^3 | 3a | m=r gives -2a; higher repeated m have mu=0 | -2a | a |

There are no four-factor profiles on w<=H. A repeated prime product contributes one ordered factorization at m=n=r, whereas distinct r,s contribute both orders. For a distinct triple, m equal to a product of two primes is one integer divisor, not two ordered decompositions of that divisor. These multiplicities explain every entry of the table.

Thus all non-prime-power composites cancel identically in (5). Squares and cubes retain precisely their von Mangoldt weight log r, to be removed when returning to actual primes. No composite original variable becomes a surviving prime contribution just because its complement is prime.

### Both corrections back to actual prime p

Let

\[
 Q_{\rm small}(g)=
  \sum_{\substack{r\le z,\ r\text{ prime},\ j\ge1\\r^j\in J}}
                     (\log r)g(r^j),\qquad
 Q_{\rm high}(g)=
  \sum_{\substack{r\text{ prime},\ j\ge2\\r^j\in J}}
                     (\log r)g(r^j).
 \tag{10}
\]

Then exactly

\[
 \sum_{\substack{p\in J\\p\text{ prime}}}(\log p)g(p)
     =T_1(g)+T_3(g)+Q_{\rm small}(g)-Q_{\rm high}(g).
 \tag{11}
\]

The first correction restores prime powers with small base deleted by R_z. The second removes all higher powers, including large bases. In the ratio-two interval J, there is at most one power of each fixed base: consecutive powers have ratio at least2 and the lower endpoint is open. Thus \(|Q_{\rm small}|\le\|g\|_\infty\sum_{r\le z}\log r=O(\|g\|_\infty zL)\), an elementary sufficient bound. The usual absolute bound \(|Q_{\rm high}|\ll\|g\|_\infty\sqrt y\log^2(2y)\) follows by counting bases and exponents.

Because y>z, Q_small contains no prime term. It cancels exactly the small-base part of Q_high. Equivalently,

\[
 \sum_{p\in J}(\log p)g(p)
       =T_1(g)+T_3(g)-Q_{\rm rough\,high}(g),
\quad
 Q_{\rm rough\,high}
       =\sum_{\substack{r>z,\ r\text{ prime},\ j\ge2\\r^j\in J}}
                    (\log r)g(r^j).
 \tag{12}
\]

Only squares and cubes can occur in Q_rough_high. Keeping both corrections in (11) makes clear why merely restoring small bases is insufficient.

Multiplication throughout by \(1_{(w,H)=1}\) is legal and keeps (5)-(12) exact. Restoring original prime summands p dividing H costs at most \(\|g\|_\infty\sum_{p\mid H}\log p\le\|g\|_\infty L\). On prime summands, gcd(H-p,H)=gcd(p,H), so this also restores the missing complement units. No estimate for all nonunit composite inputs is inferred from that small prime-summand cost; the exact recombination is performed first.

For fixed rho in the three-node set, G_rho is uniformly bounded, since its nonzero complement has at most three factors. All displayed correction bounds are o(H/L^K) for every fixed K when y is comparable to H. For y>=H/L^B, the same is true with constants depending on fixed B. Covering p>=H/L^B by disjoint dyads uses O_B(log L) intervals; the errors remain negligible. The omitted small prime summands p<=H/L^B cost at most O(H/L^B) unweighted. Choose B>2 for o(H/L^2). In particular restricting p itself to p>z loses at most O(z)=o(H/L^2); this is distinct from restricting the complement q.

### Exact logarithmic-to-unweighted passage

For the signed test g=G_rho define
\(S_g(u)=\sum_{y<p\le u}(\log p)g(p)\). Then partial summation gives exactly

\[
 \sum_{y<p\le t}g(p)
     =\frac{S_g(t)}{\log t}
       +\int_y^t\frac{S_g(u)}{u(\log u)^2}\,du.
 \tag{13}
\]

Thus a signed weighted estimate must be endpoint-uniform, or its variation must be controlled, before division by log H. A weighted error o(H/L) gives o(H/L^2) after this formula on comparable dyads; an unsifted signed o(H/L) unweighted result from another coefficient family is not the required conclusion. The negligible corrections above remain negligible after (13). Squareful-complement losses are at most O(H/(z-1)) unweighted, or O(LH/(z-1)) logarithmically weighted, and hence are also below the prime-pair scale.

### What actually remains after the valid CENTERED-018 estimate

For clarity define the explicit rough-profile correlations

\[
 C_{\rho,k}(J)=
   \sum_{\substack{w\in J,\ R_z(w)=1\\\Omega(w)=k}}
                           (\log w)G_\rho(w),\qquad k=1,2,3.
 \tag{14}
\]

Let P2,P3 denote the sums in Q_rough_high with exponent2,3 respectively. The complete coefficient table proves the exact relations

\[
 T_1(G_\rho)=C_{\rho,1}+C_{\rho,2}+C_{\rho,3},\qquad
 T_3(G_\rho)=-C_{\rho,2}-C_{\rho,3}+P2+P3,
\]
\[
 \sum_{p\in J}(\log p)G_\rho(p)=C_{\rho,1}.
 \tag{15}
\]

These formulas identify and cancel the composite correlations, rather than posit a new dispersion bound containing the unknown prime count. In particular the entire T3 has zero coefficient at every prime w. Its balanced prime-by-prime rectangle is a piece of C_rho,2, with the square convention in the table; triple profiles also occur in other rectangles of the full convolution.

CENTERED-018 proves an all-precision nonprincipal character-energy saving for exactly one balanced prime-factor family, with its actual phases and center retained. It does not evaluate the linear shifted T3 sum, its signed fractional comparison, all its rectangles or T1. Even a complete evaluation of that one composite rectangle would supply a term canceled by the corresponding part of T1 in (15), not an extra positive prime contribution. The prime part of T1 remains unmeasured; estimating the full T1 requires the actual two-sided rough correlation

\[
 \sum_{w\in J}R_z(w)(\log w)
       \mu(H-w)R_z(H-w)h_\rho(H-w),
 \tag{16}
\]

together with its explicitly enumerated composite pieces in (15), at endpoint-uniform weighted precision o(H/L) if one seeks o(A_H) information after deweighting. This is the original signed rough-pair correlation with all original-variable profiles retained, not an accepted subpolynomial Type-I estimate. Its product/complement restrictions are not removed by the complete multiplicativity of R_z. No bound for (16) of that precision is supplied by the accepted stages.

The same coefficient cancellation applies independently to each complement profile and to each of the three rho nodes. On original prime w, (2)-(3) still control which complement profiles survive. The odd signed reflection identity in the original bridge, the adapted Z interpolation and the original prime p margin therefore have not been replaced by an assertion about composite w=mn.

## Candidate 2: first exact falsifier of a one-sided composite-center transfer

**Refuted inference, with a complete profile counterexample:** a positive selected prime-by-prime cofactor contribution cannot be carried into a nonnegative original-prime margin profile by profile after Vaughan recombination. The smallest factor-count obstruction is Omega(w)=2. Distinct semiprimes cancel already between T1 and T3; squares also require the higher-power correction. This is not a counterexample to actual primes, the accepted energy theorem or Goldbach.

Here is a concrete one-sided claim that such a profilewise transfer would require. For a nonnegative localization b(w), define

\[
 R_b(H)=\sum_{\substack{p\text{ prime}\\H-p\text{ prime}>z}}b(p),
\quad
 B_b(H)=\frac1{V_H}
    \sum_{\substack{r,s\in I\text{ prime}\\a=H-rs\text{ prime}}}
        b(rs)\eta(a/Y)\log s,
 \tag{17}
\]

with the exact balanced I,Y and full normalizer of 018. A claimed transfer of a positive multiple of the retained selected composite contribution, with no signed compensation, would assert \(R_b(H)\ge cB_b(H)\) for some c>0 uniformly over such localizations. Both quantities have the intended unweighted prime-pair scale when the respective macroscopic populations have their natural density: the log s in B is part of its actual Vaughan coefficient, not an extra prime-pair log weight.

The claim is false for every c>0. Take H=128, alpha=3/10, r=s=5, w=25, a=103 and b(w)=1 when w=25 and0 otherwise. Then 5>128^(3/10), since \(5^{10}>128^3\), and 103 is prime (none of2,3,5,7 divides it). The balanced interval \(I=[\sqrt{128/6},(5/4)\sqrt{128/6}]\) contains5. All coordinates are H-units. Moreover \(a/Y=309/128\) lies strictly between2 and5/2; choose an admissible smooth eta positive at this point. Thus

\[
 R_b(128)=0,\qquad
 B_b(128)=\eta(309/128)\log5/V_{128}>0.
 \tag{18}
\]

There is one ordered r=s factorization. The normalization V_128 is positive because, for example,5 lies in its prime group. The original p=25 is composite, so the left side is zero independently of any uncertainty about other prime pairs at H=128.

The exact cancellation can be checked without a numerical search. In the honest original dyad J=(16,32], U=V0=16^(1/5)<z, the single w=25 profile with nonnegative test b(w) times the prime-complement indicator contributes \(2\log5\) to T1, \(-\log5\) to T3 and \(-\log5\) through the removal of the higher power. Its final prime contribution is0. For each G_rho, q=103 has coefficient -1 independent of rho; multiplying all three entries by -1 leaves the same exact cancellation. The positive selected cofactor amplitude in (18) therefore cannot change this recombined coefficient.

This finite profile is a coefficient witness, not a replacement of the full arrays by an arbitrary localized version of 018. The energy theorem is used only in its accepted actual scope. The witness disproves the proposed profilewise nonnegative transfer; it does not disprove a possible unlocalized global inequality R>=cB whose proof would need additional arithmetic information. No asymptotic counterexample to a global prime theorem is asserted.

### Why the available upper bound and nonzero centers do not repair the inference

At the original target scale the accepted sufficient margin remains \(F>H_\alpha\). Bound (4) would suffice if a genuinely derived one-sided estimate for the recombined F exceeded its right side by a positive multiple of A_H, for one fixed epsilon. No such lower estimate has been derived here. Stating it again is not a new theorem or an estimate furnished by the principal energy.

There is an exact algebraic model of the missing implication. For large A_H take an integer K<=A_H with K>0, and set abstract profile counts R=H0=H_alpha=0, E0=K and no squareful population. Then all interpolation identities hold,

\[
 Z_{1/4}=K/2,\quad Z_{1/2}=K,\quad Z_{3/4}=3K/2,
\quad R=F=0.
 \tag{19}
\]

The triple upper bound is satisfied, all three signed observables have nonzero centers, and the available rough-population upper bound of order A_H is satisfied. The exact prime reconstruction and odd reconstruction both vanish. This profile model is not a model of the actual distribution of primes or a denial of 018. It shows that the proved profile identities, nonzero centers as such and a small triple upper bound contain no algebraic positive margin. The centered energy adds no bound for the unmeasured linear prime cell by the support calculation (15). An actual pointwise value or one-sided error bound for the correctly recombined signed observable is the genuinely missing arithmetic information.

A proposed comparison main term could change this situation only if its exact link to the recombined original prime observable and its signed fractional/minor remainder were proved with the required sign and o(A_H) size. No theorem from parallel PRINCIPAL-019 is assumed, and no positive comparison term is used to bound an uncontrolled signed remainder. The first new arithmetic estimate is a target-uniform, parity-sensitive estimate of that recombined original-prime observable, including the full T1 and composite cancellation accounting above. It cannot be replaced by the already accepted nonprincipal energy saving on composite w.

## Review questions and limits

The distinct critic should check the exact survival d=1/T2=0, c_V0=log n, every repeated-factor coefficient and both prime-power corrections; then check that (18) refutes precisely the localized/profilewise transfer, without implying an actual global prime counterexample. The log-weighted-to-unweighted endpoint formula and the fixed-epsilon use of the accepted triple bound must remain visible.

Candidate1 is an exact finite algebraic recombination with scale-correct correction bounds. Candidate2 refutes a particular attempted one-sided transfer and gives a precise profile model of the remaining gap; it does not prove a positive original prime margin. All original k/twist/rectangle limits of 018 remain. Closest-work novelty, a substantive global breakthrough classification, the original pointwise margin and Goldbach remain unverified or unresolved. No goal completion is asserted or authorized.
