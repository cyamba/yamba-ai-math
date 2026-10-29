# ETH-C02. Weighted counting: the weight enumerator $Z_F(q)$, Max-Ones and exact-weight #SAT

| Field | Value |
| --- | --- |
| Category | Counting |
| Source items | "YMB-ETH-03: q-series lifting, subexponential partition function $Z_F(q)$ for weighted #k-SAT" |
| Status | **Solved conditionally at bounded density** (SR-07, Cor. B); **open at arbitrary density** |
| Depends on the upstream theorem | Yes (Theorem C.1) |
| Score (I/B/T/L/Lean) | 3 / 2 / 4 / 3 / 4, composite **3.0** |
| Subresults | [SR-07](../subresults/SR-07-graded-counting-bounded-density.md); Lean `Graded.weight_identity` |

## Statement

$Z_F(q)=\sum_{x\in\mathrm{SAT}(F)}q^{|x|}=\sum_wc_w(F)q^w$. For $m\le Dn$ all $c_w$ are computable in
$2^{O_{k,D}(n/\sqrt{\log n})}$ by grading the variables with a unary tensor $(1,V)$ in the
bounded-density network (SR-07). The source's interpolation plan ($n+1$ evaluations of "the
deformed 378 algorithm") is not needed, and its exponent $n\log\log n/\log n$ is wrong.

## Open part

At arbitrary density the preprint's network sums the original variables inside variable-group
tensors and already uses $V$ for the parity lift. Show that Theorem C.1 holds over
$(\mathbb Z/2^P)[V,W]/(V^\ell,W^{n+1})$ (a second passive variable), or find another grading.

## The partition-counting remark

The source's "bonus" (restricted integer partitions via binary-encoded weights) needs adders,
hence $\Theta(n\log n)$ variables for numbers of $\log n$ bits: not covered by linear encodings.

## Closest work

Preprint Appendix C (level T, read in full; R039).

## Smallest falsifier

A family of dense formulas where the two-variable contraction provably needs precision
$\omega(s)$ would block the extension.

## Resource boundary

One agent to check Appendix C with two passive variables; one critic.
