---
id: ETH-B03
source: new (this program)
category: exponent-frontier
status: TOP OPEN PROBLEM. M_0-form settled up to constants (proved, Lean core); general rows open
novelty: NOT VERIFIED
---

# ETH-B03: Routing rigidity beyond `M_0`, the only visible route past `sqrt(log n)`

## Setting

Auxiliary coordinates `u = (a_u, d_u) in [r]^Q x [r]^Q`, `D = r^{2Q}`. At node `t` the coordinate `w` is
*allowed* for row `u` iff `a_w(t) = d_u(t)`; let `N_{t,u}` be the forbidden coordinates. A **design of degree
`R-1` with `c` measurements** is a `c`-dimensional space `Rs` (row space of the measurement matrix `C`) and rows

`P_u(T) in Q[T]^D`, `deg P_u <= R-1`, `P_u(0) = e_u`, with `P_u(t)|_{N_{t,u}} in Rs|_{N_{t,u}}` for `t = 1..Q`.

The algorithm's exponent is `n [ (R/Q) log(Q/R) + tau log D + 1/r ]` with `c/D = eps <= 2 tau / r`.
Define `eps*(Q,R,r)` = least achievable `c / D`.

The preprint uses the **`M_0` form** `P_u(T) = ((I - M_0) e_u)^T + sum_w M_0[u,w] prod_{s in E_{u,w}} (1 - T/s) e_w`,
which requires `M_0[u,w] != 0 => Ham(d_u, a_w) <= R-1` and gives `c = rank(I - M_0)`.

## What is now known

| Statement | Status | Evidence |
| --- | --- | --- |
| `M_0` form, *any* matrix (commutative or not): `rank(I - M_0) >= D Pr[Bin(Q,1/2) >= ceil((Q+R)/2)]^2 ~ D e^{-R^2/Q}` (even `r`) | **proved; Lean core** (`RoutingRigidity.lean`) | product-set zero block; [checks/routing_product_set_bound.py](../checks/routing_product_set_bound.py) |
| `M_0` form, commutative swap algebra achieves `~ D e^{-R^2/(2Q)}` | **established** (preprint construction, sharp tail) | |
| Hence for the `M_0` form `log(1/eps*) = kappa R^2 / Q` with `kappa in [1/2, 1]` asymptotically | **proved** | |
| Smallest case `(Q,R,r) = (3,2,2)`: commutative optimum 10, certified lower bound 8, non-commutative completion of rank 9 | **empirical** (rank 9: 3 of 8 runs converge to `sigma_10 ~ 1e-14` with bounded entries); LB 8 **proved** by CP-SAT triangular block | [checks/routing_minrank_*.py](../checks/) |
| General polynomial rows: `eps* >= 4^{-R}` (even `r`; odd `r`: `(floor(r/2) ceil(r/2)/r^2)^R`) | **proved** (fixed node set `S_0` of size `R` on which every pair in a block is forbidden; Lagrange at `S_0` puts `e_u|_T` in `Rs|_T`) | this file, Sec. "Proof of the 4^{-R} bound" |
| General rows: is `eps* = 2^{-Theta(R)}` achievable for `R << sqrt(Q)`? | **OPEN** | ALS on `(3,2,2)` inconclusive (does not even recover known `c = 9`) |

### Proof of the `4^{-R}` bound

Fix `S_0 subset [Q]`, `|S_0| = R`, and a symbol split `X ⊔ Y = [r]`. Let `T = {u : a_u(t) in X, d_u(t) in Y
for t in S_0}`, `|T| = D (|X||Y|/r^2)^R >= D 4^{-R} (1 - o(1))`. For `u, w in T` and `t in S_0`,
`a_w(t) in X`, `d_u(t) in Y`, so `w in N_{t,u}`: `P_u(t)[w] = rho_{u,t}[w]` with `rho_{u,t} in Rs`. Lagrange
interpolation of the degree-`(R-1)` polynomial `P_u(.)[w]` at `S_0` gives
`delta_{uw} = P_u(0)[w] = sum_{t in S_0} lambda_t rho_{u,t}[w]`. The vector `sigma_u = sum lambda_t rho_{u,t}`
lies in `Rs` and restricts to `e_u` on `T`. Hence `dim Rs >= |T|`. QED.

## Why this is the top problem

If general rows reach `eps* = 2^{-O(R)}`, take `R ~ log log n`, `Q ~ log n / log r`,
`r ~ log n / (log log n)^3`, `tau ~ (log log n)^3 / (log n)^2`: the exponent becomes `O(n (log log n)^3 / log n)`, a polynomial-in-`log n`
improvement over Theorem 1 and the first algorithm beyond the `sqrt(log n)` scale
(the interpolation template is stuck at `rho(n)`, [ETH-B01](ETH-B01-sqrt-log-barrier.md)). If instead `eps* >= e^{-O(R^2/Q)}` holds for general rows too, the
barrier covers the whole replacement-form template and the field must change the recovery step.

## Concrete sub-problems for a fleet

1. **(Exact small cases.)** Compute `eps*` exactly for general rows at `(Q,R,r) in {(3,2,2), (4,2,2), (3,2,3)}`.
   The problem is bilinear (rows times `Rs`); use Groebner bases over `Q` or exhaustive search over `Rs`
   spanned by `{0, +-1}` vectors (which the algorithm needs anyway for bounded measurements).
2. **(Certify the 10 to 9 improvement.)** Turn the numerical rank-9 completion into an exact rational one, or
   certify existence by alpha-theory after fixing coordinates. The reduced form is a `32 x 64` partial
   matrix (only rows with `Ham(d_u, a_u) >= 2` constrain). Scripts: `routing_rank9_probe.py`,
   `routing_rank9_sparsify.py`.
3. **(Improve the lower bound.)** Find any argument for general rows that uses more than one fixed node set,
   e.g. a polynomial-method or rank argument over the joint `(u, t)` structure. Target: `eps* >= e^{-c R^2/Q}`.
4. **(Constructions.)** Node-dependent row spaces: let `rho_{u,t}` vary with `t` (the `M_0` form keeps it
   constant). Natural candidates: rows built from *different* polynomials `f_t` at different nodes, or
   non-commutative products of routing permutations `sigma(a,d) = (d, pi_d(a))` with eigenvalue-1 mass
   larger than the swap's on the relevant subspaces.
5. **(Integrality.)** Any construction must also give `Rs` an integral basis of small `l_1` norm, since
   measurement values must range over a set of size `D^{O(1)}`.

Resources: tiny instances run in seconds to minutes on 2 CPU cores; `(4,2,2)` has `D = 256`.
