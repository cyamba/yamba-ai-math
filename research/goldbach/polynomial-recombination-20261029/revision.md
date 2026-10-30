# Reviewed polynomial recombination: original-author revision

29 October 2026. Actual GOLDBACH-RECOMBINE-020 original-author revision from the populated revise packet. The distinct critic supports the exact decomposition, all multiplicity profiles, both prime-power corrections and scale accounting. It also supports the finite localized obstruction and abstract profile model, subject to the two P2 clarifications made below. This is the bounded revision in the same authorized pair round, with no new research, source search or experiment. Usage is unknown.

The frozen statement SHA256 is e329f47df803775ca94610809b97630463d176ed73f5f682003a75f63185df9a. The distinct review SHA256 is 8c605c2e28515ace56aa253bdcdf53f305e6372aaafeb7cf7eeddf8769eb53d0. Both remain unchanged. This revision narrows the interpretation of the counterexample and corrects the abstract model's terminology; it does not add an asymptotic counterfamily, a third candidate or a new positive-prime estimate.

Assurance is a complete elementary written author argument with a distinct substantive written-argument audit relative to the named accepted local results. It is not formal verification, external peer review or a fresh audit of the imported classical proofs. No paid call, supplemental worker, publication, external message or goal-completion action occurred.

## Candidate 1 retained: exact recombination and the surviving prime cell

**Proved, supported by the distinct review.** Keep the frozen definitions: H even, alpha in [3/10,1/3), z=H^alpha, a product dyad J=(y,t] with y<t<=2y and t<H, and U=V0=y^(1/5)<z<y. The roughness indicator R_z is completely multiplicative, and g is any bounded test function on positive inputs below H.

The exact Vaughan identity gives

\[
 \sum_{w\in J}\Lambda(w)R_z(w)g(w)=T_1(g)+T_3(g),\qquad T_2(g)=0,
\]
\[
 T_1(g)=\sum_{w\in J}R_z(w)(\log w)g(w),\qquad
 T_3(g)=\sum_{\substack{m>U,n>V0\\mn\in J}}
           \mu(m)R_z(m)(\log n)R_z(n)g(mn).
 \tag{R1}
\]

Indeed, rough d<=U must be1, any nonzero Lambda(ell) with ell<=V0 is deleted by R_z, and every nontrivial prime-power divisor of rough n exceeds V0. Thus c_V0(n)=log n on rough support. The coefficient of rough w in T3 is exactly

\[
 \sum_{\substack{d\mid w\\1<d<w}}\mu(d)\log(w/d)
                     =\Lambda(w)-\log w.
 \tag{R2}
\]

There is no rectangle-factorization assertion about the shifted test g(mn).

There are at most three prime factors with multiplicity on w<=H. For the six possible types r, rs, r^2, rsu, r^2s, r^3, with distinct letters denoting distinct primes and a=log r, b=log s, c=log u, the T3 coefficients are respectively

\[
 0,\quad -(a+b),\quad -a,\quad -(a+b+c),\quad -(2a+b),\quad -2a.
 \tag{R3}
\]

Adding T1 leaves a,0,a,0,0,a, exactly Lambda(w). Unequal prime factors have two ordered factorizations; a square has one. Integer divisors in a triple are counted once, with the Mobius sign at that divisor. The complete table and proof in the frozen statement remain accepted.

Let Q_small restore all powers in J with prime base<=z, and let Q_high remove every power in J with exponent>=2, with each term weighted by its base logarithm times g. Then

\[
 \sum_{\substack{p\in J\\p\text{ prime}}}(\log p)g(p)
       =T_1(g)+T_3(g)+Q_{\rm small}(g)-Q_{\rm high}(g).
 \tag{R4}
\]

Since y>z, Q_small contains no prime term and cancels exactly the small-base part of Q_high. The remaining rough squares and cubes are removed by the higher-power correction. All original-variable composite profiles therefore cancel after full recombination. A prime complement does not turn a composite original variable into a prime summand.

The reviewed losses are retained: Q_small is O(||g||_infinity zL), Q_high is O(||g||_infinity sqrt(y) log^2(2y)); original nonunit prime summands cost at most ||g||_infinity L after recombination; rough squareful complements cost at most H/(z-1) unweighted; and small original prime omissions cost O(z), or O(H/L^B) when using that cutoff with fixed B>2. On the stated macroscopic dyads, and on y>=H/L^B with the recorded dyad costs, these are below the H/L^2 count scale. The exact signed deweighting formula remains

\[
 \sum_{y<p\le t}g(p)
    =\frac{S_g(t)}{\log t}
       +\int_y^t\frac{S_g(u)}{u(\log u)^2}\,du,\qquad
 S_g(u)=\sum_{y<p\le u}(\log p)g(p).
 \tag{R5}
\]

Endpoint-uniform weighted control, including the costs of a later global dyad summation, is required. A single terminal signed estimate cannot replace it.

For the actual G_rho(w)=mu(H-w)R_z(H-w)h_rho(H-w), with H-w>1 and h_rho=nu*rho^(nu-1), let C_(rho,k) be its log-weighted correlation restricted to rough original inputs w with Omega(w)=k. The exact accounting is

\[
 T_1=C_{\rho,1}+C_{\rho,2}+C_{\rho,3},\qquad
 T_3=-C_{\rho,2}-C_{\rho,3}+P2+P3,
 \tag{R6}
\]

where P2,P3 are the rough square/cube base-log corrections. After their removal, C_(rho,1) is the actual prime sum.

The accepted CENTERED-018 result retains its balanced prime-factor, powers-of-two, k=1, trivial-fixed-twist scope, including the stated common polylogarithmic v and arbitrary real marking lambda. It retains its exact principal energy and gives its positive asymptotic only on fixed compact time intervals at v=lambda=0. The support w=rs of that result is composite original input. Its terms occur within the C_(rho,2) part canceled in (R6); its energy bound does not evaluate the linear shifted correlation, all rectangles, T1 or the surviving prime cell. This conclusion preserves the valid result and does not claim that every future use of it is impossible.

The full polynomial Type-I term remains

\[
 \sum_{w\in J}R_z(w)(\log w)\mu(H-w)R_z(H-w)h_\rho(H-w).
 \tag{R7}
\]

It includes original-prime and original-composite cells. The polynomial roughness and shifted endpoint remain actual restrictions. No accepted subpolynomial Type-I estimate is substituted for (R7), and no new dispersion assumption is introduced under another name.

## Candidate 2 clarified: precisely the finite localized claim refuted

**Refuted, in the following finite-H quantifiers only:** fix alpha=3/10 and an admissible smooth eta positive at309/128. There is no c>0 such that

\[
 R_b(H)\ge cB_b(H)
 \tag{R8}
\]

for every admissible finite even H, including H=128, and every nonnegative localization b, where

\[
 R_b(H)=\sum_{\substack{p\text{ prime}\\H-p\text{ prime}>z}}b(p),
\qquad
 B_b(H)=\frac1{V_H}
  \sum_{\substack{r,s\in I\text{ prime}\\a=H-rs\text{ prime}}}
       b(rs)\eta(a/Y)\log s.
 \tag{R9}
\]

Here I,Y,V_H are exactly the balanced parameters and full normalizer used in the frozen statement. Finite admissibility means the displayed prime, roughness, unit, label-support and interval conditions are satisfied. The claim in (R8) includes128 explicitly; it is a universal finite localized/profilewise transfer claim.

The accepted witness is H=128, r=s=5, w=25, a=103 and b=1 at25 and0 elsewhere. We have 5^10>128^3, 103 prime, all coordinates odd H-units, 5 in the balanced interval, a/Y=309/128 in (2,5/2), and V_128>0. Hence

\[
 R_b(128)=0,\qquad
 B_b(128)=\eta(309/128)\log5/V_{128}>0.
 \tag{R10}
\]

There is one ordered square factorization. The dyad (16,32] with U=V0=16^(1/5)<z has this profile's coefficients 2log5 in T1, -log5 in T3 and -log5 upon higher-power removal. Their sum is0. For G_rho the prime complement103 has coefficient -1 at every rho, so the same cancellation holds after multiplication by that sign. This is a coefficient witness, not a substitution of localized arrays into the actual018 theorem.

**The finite witness does not refute either an eventual large-H localized theorem or an unlocalized theorem.** In particular, an assertion quantified only over H>=H0 for some unknown H0, even if uniform over b, is not refuted by this single target. No asymptotic actual-prime counterfamily is asserted. An unlocalized global inequality R>=cB likewise remains outside this refutation and would require additional arithmetic information to prove or disprove.

This resolves P2 finding1 without enlarging the finite evidence.

## Abstract profile model: values, not prescribed arithmetic centers

**Proved algebraic nonimplication, with corrected terminology:** for a large target-scale number A_H, take an integer K with 0<K<=A_H and assign abstract profile counts

\[
 R=H_0=H_\alpha=0,\qquad E_0=K,
\quad
 (Z_{1/4},Z_{1/2},Z_{3/4})=(K/2,K,3K/2).
 \tag{R11}
\]

These are nonzero model observable values. They are not defined as, or identified with, actual arithmetic centers. The profile identities and the retained population/triple upper bounds hold in this model, while both the prime reconstruction and odd reconstruction vanish. Therefore those identities, upper bounds and nonzero observable values alone give no positive prime margin.

The model does not instantiate the prescribed COFACTORS-015 gamma vector or the full arithmetic content of018. In particular, the accepted asymptotic gamma_1~A_H is retained. Assigning R_unit=0 in an abstract model would leave a discrepancy of order A_H from that center; no reviewed small-error estimate excludes it, because the needed dispersion bound is unproved. The positive compact principal energy of018 is also retained as its actual accepted statement, not replaced by a model value. An explicit arithmetic center together with a proved adequately small error could yield information not represented by (R11).

Thus the frozen statement's phrase that this model has “nonzero centers” is superseded by “nonzero model observable values.” It does not show a failure of any theorem prescribing a center and proving a sufficient error bound. This resolves P2 finding2.

## Original prime margin remains the missing arithmetic result

For the actual primes the profile identities remain exact, and the prescribed arithmetic centers retain their separate definitions:

\[
 Z_\rho=-R+2\rho E_0-3\rho^2H_0,\qquad
 R=-3Z_{1/4}+3Z_{1/2}-Z_{3/4},\qquad
 F=R+H_\alpha.
 \tag{R12}
\]

The accepted continuation upper bound retains its exact scope:

\[
 H_\alpha(H)\le \omega_{>H^\alpha}(H)
     +C\mathfrak S(H)H L^{-2}(\varepsilon+1/L)^2,
\quad \omega_{>H^\alpha}(H)\le3,
\quad \alpha=1/3-\varepsilon.
 \tag{R13}
\]

Here C and its effective threshold are numerically unspecified, epsilon is in [0,1/30], and a fixed-epsilon asymptotic is taken with epsilon chosen first. Neither this upper bound nor (R11) supplies a lower margin for F. The needed new arithmetic information is a noncircular, target-uniform one-sided estimate for the correctly recombined original-prime observable at H/log^2 H, retaining the prescribed centers and controlling every signed remainder. It must exceed the triple contamination for one fixed epsilon, or directly reconstruct a positive R.

The original prime cell in (R6) remains unestimated. Full polynomial Type I and signed rough-pair correlation (R7), complete comparison/transport, all actual frequency and rectangle costs, and the original pointwise prime margin remain unresolved. No result from parallel PRINCIPAL-019 is assumed. A further isolated positive composite term does not establish that margin, and an uncontrolled signed fractional/minor remainder is not assigned a favorable sign.

Both critic clarifications are resolved in these new files; the finite conclusions and exact recombination retain their reviewed scope. No Goldbach proof, global impossibility result, novelty, breakthrough classification or goal completion is claimed.
