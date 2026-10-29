# Single reserved refinement notebook

Start 2026-10-24 22:28:48 UTC. Purpose: close the original 3,829-source
gap within frozen routing family 2, preserving the original 151 pairs.
No new family, external call, dependency, or dispatch was introduced.

Discovery sequence, with incomplete domains retained:

1. Common T21111 demotion and first local antecedent: 2,585 sources.
   Hook-before-pair priority has a bounded intrinsic inverse but blocks
   useful hook merges; raw meter output and firsteligible source remain.
2. Move inverse-bubble hook merges before common demotion: 3,169 sources.
   Full remaining 811-source matching extends these prescribed pairs.
3. Skip targets already reserved by original images before choosing
   merge endpoints: 3,214 sources. This became revision_local.py.
4. Middle-arm hook demotion and comparable arm promotions: 3,340;
   outer-arm recuts: 3,385. Entry extraction bounds are 3–36, not a
   tableau-family traversal.
5. Comparable corner and arm exchanges: 3,868, with all 1,273 hooks now
   handled. A second independent finite feasibility check confirms that
   the 112 remaining sources still admit a full family-2 matching after
   all these prescribed image pairs have been removed.
6. Balanced crossing instead of comparable-only routing: 3,938; corner
   promotion: 3,959; later chain changes: 3,964, then 3,971. Exact residual
   witnesses survive in each saved JSON and raw metered stdout.
7. Five fixed balanced slot rotations close the last nine, yielding
   3,980/3,980 and zero failures at 22:41:49 UTC. No mutable matching is
   retained or called by the resulting algorithm.
8. Added the conservative 15-pair equality guard to all prescribed
   layers, making weight preservation explicit rather than relying on
   extending every shortcut argument outside the checked class. Final
   protocol at 22:42:28 UTC remains 3,980/3,980. It also checks all 6,800
   positives, all original 151 pairs, and the frozen moved-label metric.

The hardest conceptual failure was interpreting finite matching as an
inverse rule. The successful repair selects a source only by cuts in
its proposed target and excludes all earlier image languages using
their intrinsic inverses. Strictly decreasing layer number makes this
selection well founded. Cached values are pure results, not ownership.

The remaining scientific limitation is symbolic totality: the layered
injection is proved on its declared domain, while exhaustive enumeration
shows that domain covers the full finite natural-unit-interval class.
No broader theorem or novelty claim is inferred.

Historical source recovery: the preliminary verifier was reverse-edited
into revision-recovered-initial-verifier.py without changing old files;
its SHA256 is 71918602f2f6f8da0fceea5dd1e9af3adce3a230e3ff9ef9eaeea44db8746098,
exactly the preliminary pin. The old structural-initial.py likewise
retains ae58d6ef7ccba8bb09ff8d6e7b6876e7a903588bb39adaaa7f44b10e06828e08.

All quantitative subprocess attempts were routed through the shared
meter, including unsuccessful or merely partial variants. Raw logs live
under .runs/phase2-20261025; the revision freeze records their exact
resource receipt separately from the mathematical result.
