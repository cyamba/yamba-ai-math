# Direct character margin: the fixed-gap attempt and its first failed estimate

29 October 2026. Actual registry Mathematician, GOLDBACH-DIRECT-021 propose stage. There is one candidate mechanism: retain the actual prime and rough-semiprime transforms, then seek a one-sided parity-weighted nonprincipal remainder smaller than the negative principal term. The desired fixed-gap inequality is **unverified**. Its first attempted absolute-value estimate is **refuted for every sufficiently large power of two**, by the actual arithmetic marginals and Parseval, as proved below. This is a limitation of that attempted estimate, not a limitation of every signed-character argument and not a Goldbach breakthrough.

Assurance of the new deductions is a complete elementary author argument relative to ordinary PNT, pending the distinct critic. No proof assistant or external human review was used. PNT is an imported established dependency: its primary statement and inspection are recorded in CENTERED-018, `research/goldbach/centered-polynomial-energy-20261029/statement.md`, under classical inputs, citing Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 8.1, printed page 84/PDF page 95 of the [author-provided book](https://www.dms.umontreal.ca/~koukoulo/documents/publications/primes.pdf#page=95). That source proof was not freshly audited here. The asymptotic derivation specific to the present semiprimes is supplied below. Novelty is unverified; the identities and norm obstruction are elementary consequences of orthogonality and PNT.

The actual packet, original prompt, continuation revision, switching bilinear model test, LABELS005 revision, and actual PRINCIPAL019 and RECOMBINE020 revisions were read. No inference from a positive composite-input energy to an original prime count is made. This stage did execute one bounded transient Python helper, disclosed in section 7. No extra worker, supplement, paid call, publication, external message or goal-completion action occurred. Token and billed usage are unknown.

## 1. Exact objects and the genuine sufficient inequality

Let H=2^ell with integer ell>=3, L=log H, z=floor(H^(1/3)), and G=(Z/HZ)^*, of order h=phi(H)=H/2. Define actual sets

\[
 P=\{p:z<p<H,\ p\text{ prime}\},\qquad
 S=\{pq:z<p\le q,\ p,q\text{ prime},\ pq<H\}.
 \tag{1}
\]

In S, pq is an integer counted once, including p=q. Unique factorization makes this unambiguous. Write p_0=|P| and s_0=|S|. Both sets consist of odd H-units. For every character chi modulo H put

\[
 P_\chi=\sum_{p\in P}\chi(p),\qquad
 S_\chi=\sum_{s\in S}\chi(s).
 \tag{2}
\]

These sums are unnormalized. Put

\[
 D_H=(p_0^2-s_0^2)/h,\qquad
 R_H=\frac1h\sum_{\chi\ne\chi_0}\chi(-1)
                   (|S_\chi|^2-|P_\chi|^2).
 \tag{3}
\]

The actual fixed-gap target attempted here is

\[
 \exists\kappa\in(0,1),\ \exists\ell_0,\quad
 \forall\ell\ge\ell_0:\qquad R_H\le(1-\kappa)D_H.
 \tag{G-open}
\]

There is no assumption that R_H is nonpositive or has zero center. The principal computation below gives D_H~c_*H/L^2 with c_*=2(1-(log 2)^2)>0. Thus (G-open) would yield the genuine original signed margin T(H)<=-kappa D_H<0 on every sufficiently large power of two. Neither (G-open) nor any sufficient replacement is proved in this stage. An unknown threshold would not by itself settle all even Goldbach targets or the finitely many smaller powers of two.

The task, objects and resource boundary are therefore explicit: the actual sets (1), no synthetic prime substitution, a uniform pointwise error at H/L^2, one pair round with at most two mechanisms and no added round. The obstruction tested is loss of chi(-1) cancellation when controlling the actual convolution. The first falsifier is an asymptotic lower bound for the attempted unsigned error itself, not a favorable finite sign pattern.

## 2. Orthogonality, support and exact reflection

**Proved elementary identity.** For A contained in the H-units represented by integers in (0,H), define A_chi=sum_(a in A)chi(a). Orthogonality gives

\[
 \frac1h\sum_\chi\chi(-1)|A_\chi|^2
 =\sum_{a,b\in A}1_{-a b^{-1}=1\pmod H}
 =\#\{(a,b)\in A^2:a+b=H\}.
 \tag{4}
\]

The first equality follows by expanding chi(-1)chi(a)overline(chi(b)); the congruence is a+b=0 modulo H. Since 0<a,b<H, their sum lies strictly between 0 and 2H and the only possible multiple is H. Every chi(-1) is real and is +1 or -1.

Every integer a in the original rough-pair population has at most two prime factors with multiplicity: each admitted factor is at least z+1>H^(1/3), so three factors have product greater than H. The unit 1 and every a<=z are excluded. Thus the two possible types are exactly P and S. Reflection pairs mixed P,S and S,P terms with signs -1 and +1. Consequently, with ordered counts and squares retained,

\[
 T(H)=SS(H)-PP(H)=-D_H+R_H.
 \tag{5}
\]

There is no midpoint correction: H/2 is divisible by 2 and is not rough for ell>=3. Strict cutoff equality and upper endpoints have been retained in (1). No squareful or nonunit error is discarded. Powers of two are essential for every admitted prime to be an H-unit under these definitions; no formula here is silently extended to general even H.

## 3. Exact semiprime convolution and its principal size

The actual, cutoff-coupled convolution is

\[
 S_\chi=\sum_{z<p\le\sqrt{H-1}}\chi(p)
                   \sum_{p\le q<H/p\atop q\ {m prime}}\chi(q)
 =\frac12\sum_{p,q>z\atop p,q\ {m prime},\ pq<H}\chi(p)\chi(q)
       +\frac12\sum_{p>z\atop p\ {m prime},\ p^2<H}\chi(p)^2.
 \tag{6}
\]

Distinct factors have two ordered representations in the middle expression, and squares have one. The last term repairs squares exactly. This is not an untruncated product of two common prime sums. In particular, normalization cannot turn (6) into an independent probability convolution without proving that the actual product cutoff and its endpoint weights permit it.

**Proved PNT consequence.** As ell tends to infinity,

\[
 p_0=(1+o(1))H/L,\qquad s_0=(\log2+o(1))H/L,
 \quad D_H=(c_*+o(1))H/L^2.
 \tag{7}
\]

Here all o(1) quantities are along the specified powers of two. To prove the second assertion, let pi_<(x) count primes strictly less than x. Exact least-factor enumeration gives

\[
 s_0=\sum_{z<p\le\sqrt{H-1}}
                    \{\pi_<(H/p)-\pi(p)+1\}.
 \tag{8}
\]

The contribution of pi(p) and 1 in absolute value is O(H/L^2)+O(sqrt(H)/L), using pi(sqrt H)=O(sqrt H/L). It is o(H/L). The arguments H/p are all at least sqrt H, so the ordinary PNT relative error is uniformly o(1). Therefore

\[
 s_0=(1+o(1))H\sum_{z<p\le\sqrt{H-1}}
                                  \frac1{p\log(H/p)}+o(H/L).
 \tag{9}
\]

For completeness, real partial summation with pi(x)=(1+o(1))x/log x, uniformly for x>=z, replaces this prime sum by

\[
 \int_z^{\sqrt H}\frac{dx}{x\log x\log(H/x)}+o(1/L)
 =\frac1L\int_{\log z/L}^{1/2}\frac{dt}{t(1-t)}+o(1/L)
 =\frac{\log2+o(1)}L.
 \tag{10}
\]

One can check the error directly: for f(x)=1/[x log(H/x)], both endpoint terms |(pi(x)-li(x))f(x)| are o(1/L^2), and the error integral is bounded by the uniform PNT relative error times O(1/L), because log x and log(H/x) are comparable to L on this range. Strict endpoint changes cost O(1/zL), which is o(1/L). The floor cutoff has log z/L tending to 1/3. The antiderivative is log(t/(1-t)), whose change from 1/3 to 1/2 is log2. This proves s_0. PNT also gives p_0=pi_<(H)-pi(z)~H/L. Squaring and using h=H/2 proves the principal term in (7).

No additive prime-pair asymptotic is used. Repeated-factor corrections in (6) are exact, and their cardinality O(sqrt H/L) is already below the main marginal scale. Equations (7) assert no pointwise value for PP or SS.

## 4. Attempt the fixed-gap estimate: the first unsigned bound is false

The first attempted sufficient estimate for (G-open) is to keep the genuine convolution (6), use endpoint character cancellation or a norm estimate, and then majorize the signed remainder by

\[
 R_H\le W_H:=\frac1h\sum_{\chi\ne\chi_0}
                         \big||S_\chi|^2-|P_\chi|^2\big|.
 \tag{11}
\]

To reach (G-open) this route would need W_H<=(1-kappa)D_H, or at least W_H=O(H/L^2) with a sufficiently small constant. **That load-bearing inequality is refuted on the actual P and S for all sufficiently large powers of two.**

Indeed, support below H makes the residue representatives injective, so Parseval gives

\[
 \frac1h\sum_{\chi\ne\chi_0}|P_\chi|^2=p_0-p_0^2/h,
 \qquad
 \frac1h\sum_{\chi\ne\chi_0}|S_\chi|^2=s_0-s_0^2/h.
 \tag{12}
\]

Taking the absolute value only after summing their difference proves the exact lower bound

\[
 W_H\ge|s_0-p_0+D_H|.
 \tag{13}
\]

By (7), eventually p_0>s_0 and p_0-s_0>D_H. Consequently

\[
 W_H\ge p_0-s_0-D_H
       =(1-\log2+o(1))H/L,
 \qquad
 \frac{W_H}{D_H}\ge(1+o(1))\frac{L}{2(1+\log2)}\longrightarrow\infty.
 \tag{14}
\]

The quantifiers are strong: for every fixed C>0, there is ell_C such that every ell>=ell_C satisfies W_H>C D_H and W_H>C H/L^2. This is a complete asymptotic falsifier of the specific unsigned estimate (11), with no numerical threshold claimed. It is not merely a finite failure of a zero-centered statement. It does not assert R_H is large or positive, because the chi(-1) signs in R_H are absent in W_H.

This also identifies precisely what prevents an import of the earlier nonprincipal energy. The true nonprincipal marginal energies in (12) are of order H/L. They cannot both have an all-precision small total energy at the present normalization. CENTERED018 concerns a different label-averaged product family with its own coefficients, normalization, phase ranges and retained principal term. Applying its bound to either energy in (12) would contradict the exact arithmetic support calculation.

## 5. Keeping the bilinear difference still loses one logarithm

There is a second way to perform the norm step inside this same mechanism. Let f=1_S-1_P and g=1_S+1_P on G. Then

\[
 |S_\chi|^2-|P_\chi|^2
   =\operatorname{Re}\{\widehat f(\chi)
                                  \overline{\widehat g(\chi)}\}.
\]

The genuine sets P and S are disjoint. Exact nonprincipal Parseval and Cauchy therefore give

\[
 |R_H|\le C_H:=
 \left[(p_0+s_0)-(s_0-p_0)^2/h\right]^{1/2}
 \left[(p_0+s_0)-(s_0+p_0)^2/h\right]^{1/2}.
 \tag{15}
\]

Using (7),

\[
 C_H=(1+\log2+o(1))H/L,\qquad
 C_H/D_H=(1+o(1))L/[2(1-\log2)].
 \tag{16}
\]

Equation (15) is valid; the hoped-for deduction C_H<=(1-kappa)D_H is false eventually. This establishes a precise failure of the proposed norm proof, not a lower bound for R_H. Even hypothetical individual bounds |P_chi|,|S_chi|<<_A H/L^A for every fixed A would not repair this inference: summing squared individual bounds over h characters gives O_A(H^2/L^(2A)), and the exact normalized energies remain (12). For each fixed A this individual upper bound is compatible with those energies. No arbitrary signed restriction of a small norm is used.

Preserving chi(-1) through expansion of (6) restores the actual constraints pq+rs=H in the semiprime contribution, and a+b=H in the prime contribution, by (4). At present there is no proved contraction/correlation estimate for the difference that gains the required logarithm with its one-sided constant. Assigning a favorable sign after Cauchy would be the first unjustified step. The genuine remaining arithmetic input is cancellation between the even- and odd-character energy differences, not another bound for the unsigned energies.

## 6. Small exact controls of additional tempting inferences

These are controls within the same character mechanism, not asymptotic refutations of (G-open).

At H=8, z=2, P={3,5,7}, S is empty, PP=2 and SS=0. Hence D_H=9/4, T=-2 and R_H=1/4>0. At H=32, z=3, P={5,7,11,13,17,19,23,29,31}, S={25}, PP=2 and SS=0. Hence D_H=5 and R_H=3. Thus an assertion R_H<=0 for every ell>=3 is false. These witnesses do not refute eventual nonpositivity, an eventual nonzero-centered fixed gap, or the possibility of a correctly retained local main term.

A probability-convolution shortcut for (6) also has an actual finite obstruction. At H=16, z=2, P={3,5,7,11,13} and S={9,15}. The real even character chi_8, equal to +1 on residues 1,7 modulo 8 and -1 on 3,5, has P_chi=-3 and S_chi=2. Therefore

\[
 |S_\chi|/s_0=1>3/5=|P_\chi|/p_0.
 \tag{17}
\]

If the actual normalized semiprime measure were the multiplicative convolution of the normalized full prime measure with a probability measure, every normalized character coefficient would contract, contradicting (17). This rules out that exact finite identity at H=16, the first power of two with S nonempty. It does not rule out a differently weighted convolution, an approximate relation with a proved error, or any eventual asymptotic contraction. In particular, (17) is not substituted for the genuinely sufficient target (G-open).

## 7. Bounded helper disclosure and handoff

One transient Python 3.11.17 helper was executed through PowerShell, with no written helper artifact. It enumerated exactly the seven targets H=2^ell for ell=3,...,9, computed the integer cube-root cutoff by a loop, sieved smallest prime factors, and listed actual P and S with squares retained. It then counted PP and SS by set membership and searched characters using the decomposition n=(-1)^a*5^j modulo H. Character values in that exploratory search used double-precision complex exponentials; no floating result is used in any proof here. The execution tool reported approximately 0.310 seconds. A separate read-only version query reported Python 3.11.17.

Its count output, reproduced here for provenance, was:

| H | z | p_0 | s_0 | PP | SS | R_H |
| --- | --- | --- | --- | --- | --- | --- |
| 8 | 2 | 3 | 0 | 2 | 0 | 1/4 |
| 16 | 2 | 5 | 2 | 4 | 0 | -11/8 |
| 32 | 3 | 9 | 1 | 2 | 0 | 3 |
| 64 | 4 | 16 | 4 | 8 | 0 | -1/2 |
| 128 | 5 | 28 | 5 | 6 | 0 | 375/64 |
| 256 | 6 | 51 | 16 | 14 | 0 | 553/128 |
| 512 | 8 | 93 | 23 | 20 | 2 | 439/32 |

The exact witnesses in section 6 are independently checkable by their displayed lists and real-character values, without trusting that helper. The asymptotic obstruction (14) has no computational dependency. No unbounded scan or finite-to-infinite inference is made.

The complete transient helper source was the following. Its final output also contained floating character values; those were exploratory suggestions only, and (17) is proved exactly above.

```python
from math import isqrt
from cmath import exp,pi
for ell in range(3,10):
 H=2**ell
 z=0
 while (z+1)**3<=H:z+=1
 spf=list(range(H))
 for p in range(2,isqrt(H-1)+1):
  if spf[p]==p:
   for n in range(p*p,H,p):
    if spf[n]==n:spf[n]=p
 P=[n for n in range(z+1,H) if spf[n]==n]
 S=[n for n in range(z+1,H) if spf[n]>z and spf[n]!=n and spf[n//spf[n]]==n//spf[n]]
 PP=sum(H-p in P for p in P); SS=sum(H-s in S for s in S)
 prin=(len(S)**2-len(P)**2)/(H//2)
 # theta-normalized pointwise contraction, search first exact vanishing P via real chars
 order=H//4; logs={};x=1
 for j in range(order):logs[x]=(0,j);logs[(-x)%H]=(1,j);x=x*5%H
 bad=[]
 for a in range(2):
  for k in range(order):
   if a==0 and k==0:continue
   pc=sum((-1)**(a*logs[n][0])*exp(2j*pi*k*logs[n][1]/order) for n in P)
   sc=sum((-1)**(a*logs[n][0])*exp(2j*pi*k*logs[n][1]/order) for n in S)
   if abs(sc)*len(P)>abs(pc)*len(S)+1e-7:bad.append((a,k,pc,sc))
 print({'H':H,'z':z,'P':len(P),'S':len(S),'PP':PP,'SS':SS,'T':SS-PP,'principal':prin,'remainder':SS-PP-prin,'contraction_first_bad':bad[:1]})
 if H<=32: print('sets',P,S)
```

The helper comment about a vanishing prime transform describes an exploratory intention; the code actually tests normalized contraction for all enumerated nonprincipal characters, without requiring a vanishing transform. No vanishing-transform claim is used.

The next review question is whether (14) and (15) have preserved their normalization and actual disjoint supports, and whether the explicit finite controls have stayed in their finite scope. The next substantive proof obligation, if this route is continued later under authorization, is a signed even-minus-odd correlation bound for the actual truncated convolution (6) and actual prime transform, sufficient for (G-open) after the nonzero main term is retained. This stage supplies no such bound. The original F_alpha route would still require its prime margin to exceed the reviewed uniform triple upper bound; no estimate here replaces that requirement. The full original pointwise objective, global novelty and breakthrough classification remain unestablished.
