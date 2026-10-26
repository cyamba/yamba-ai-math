# PR15 revision 2: mathematical audit and corrections

Date: 2026-10-26. Base: 97d6561a855ea4aac4fb89c03a6fb543c9edd56e.
Author attribution remains Christopher Yamba; original collaborator remains Antigravity.
This revision was prepared by Codex with a separate critic reviewing the constructions.
It is not an external peer review or a novelty audit.

## Review findings

1. **Refuted old Phi221 formula:** for h=(2,2,4,5,5),
   T=((1,4),(2,5),(3,)) has graph weight 1; candidate 2 has weight 2.
   The corrected exact definition selects the first ordered candidate that
   is a valid target AND has equal graph weight. It selects candidate 4 here.
   Python already used that acceptance rule; the published formula did not.
   All 42 n=5 Hessenberg vectors are exhaustively checked for coverage,
   validity, equal weight and collisions. The complete routing is not Lean checked.
2. **Correct beta recovery:** zero-based sigma maps determinant row to column,
   beta[sigma[i]]=cols[i]-i+sigma[i]. The decreasing key order tau IS sigma.
   Both directions now explicitly recover columns, sigma and signs through n=6,
   with n=1 included. The written proof covers all n and completes nonnegativity,
   partition size and mutual-inverse arguments; it is not formalized in Lean.

## Further research and preserved counterexample

Full KR1 roundtrips pass 5,461 states for 0<=N<=40. The current implementation
uses a finite 82-entry apex table. Coordinate reduction gives 85 reached cluster
apexes including 3 special a=3,b=0 apexes; the old figure of 78 was stale.

At N=41 two distinct clusters have the same column image:

- Higher: (a=5,b=0,mu=(0,1,2,6,7),nu=()).
- Lower: (a=2,b=2,mu=(5,5),nu=(0,1)).
- Common U=(19,12,6,3,1); decompose_full returns the lower cluster.

This refutes the all-weight extension of the current rules. Nine further cluster
states at N=41 lack apex assignments. A known higher apex (18,10,3) proceeds by
+6 to (19,12,6), +3 to (19,12,6,3), and +1 to the collision image.
Adding missing apexes alone cannot repair the known-orbit overlap.

The restricted a=3,b=0 sector separately passes 4,491 states through N=60.
This is positive finite evidence, not a proof on its infinite domain.

A useful next target is a signature invariant preventing the three operators
from entering the lower-sector image, followed by a unique inverse. The general
6D cone statement remains a conjecture: the existing explanation does not fully
prove all terminal and lower-image exclusions. No general KR1 bijection is claimed.

## Assurance and checks

- Exact Python suites and five review regressions pass.
- Full repository suite: 100 tests pass; repository integrity check passes.
- Independent critic found the two principal repairs consistent with the code;
  additional scope corrections cover the n6 rotation hypotheses and cascade.
- Existing Lean files are unchanged. Their historical verification record is
  retained; all listed source hashes were checked for correspondence.
- Fresh Lean verification could not run: Lean 4.34.0 / lake is not installed.
- PDF rebuilt with pdflatex and visually inspected; no overfull boxes after layout repair.
- Website Astro production build passes (49 pages). Publication PR remains draft.
- New finite reports live beside this note. Run Python without -O; verifier CLIs
  reject optimized execution because their exact checks use assertions.

Commands (repository root):

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
python3 research/partitions/checks/multidimensional_ferrers.py
python3 research/rogers-ramanujan/checks/rr004_multidim_cones.py
python3 research/rogers-ramanujan/checks/rr004_extension_probe.py
python3 research/partitions/lean/verify.py  # requires pinned Lean 4.34.0
```

The finite evidence reports are not general proofs. Artifact hashes record content
and provenance, not mathematical truth, novelty or legal priority.
