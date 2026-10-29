# Dated discovery notes — 25 October 2026, Europe/Stockholm

All notes are local. Older RR006/RR007 ledgers remain closed. This notebook
records discovery rather than a transcript or a claim of independent proof.

1. Reading the external code exposed two separate issues: its loop is over
   size five, not six, and its success print confuses 42 at five with 65
   through five. Its global used set also means the listed moves are not a
   standalone local map with an intrinsic inverse.
2. A literal determinant permutation is part of the object. In particular,
   n=6 e51 has two positive T6 occurrences. Removing that copy tag changes
   the cancellation problem. The complete raw inventory is retained.
3. Candidate family1 allows arbitrary one-label relocation and row-block
   reorder, stronger than simply sliding the final corner. It already has
   an exact Hall obstruction at five. Candidate family2 v1 adds reading-word
   recuts but still fails the same component. Both failures are saved.
4. The obstruction's triangle sends (14/25/3) to (135/24). It moves three
   labels and swaps the inversion contributions of edges 34 and 45. This
   suggested a bounded three-label relocation family, frozen before n=6.
   It gives complete finite matching at six. That success does not give a
   structural inverse; no promotion from matching to proof was made.
5. A direct hook demotion from T51 has only a two-source ambiguity when the
   arm prefix, last corner and leg form a full chain. The two literal T6
   copies absorb exactly this ambiguity and have entrywise inverses.
6. Splitting T42 overlaps the hook image exactly when x<_P b and not x<_P a.
   The a<_P x branch rotates to (uvw/ax/b); the incomparable branch rotates
   to (uvb/wx/a). The target inequalities t<_P z versus z incomparable t
   make their inverse languages disjoint. This gives Theorem A, with no
   global used set. Its second rotation needs n>=6: n=5 would place x below
   b in column two and violate the column rule. This boundary is explicit.
7. The exact Hall pair at six admits a conditional universal triangle rule.
   Requiring c<v<b and both c,b incomparable with v makes one removed graph
   inversion balance one added inversion. It recovers its labels directly
   from either target shape. Its 321 images cannot overlap Theorem A's two
   languages because their required inequalities contradict a<_P c or b∥v.
8. Exhaustive checks find 151 structural sources and recognize exactly 151
   images, versus 3,980 total negative sources. The remaining 3,829 are a real
   gap. An unrestricted finite matching is a useful existence diagnostic but
   cannot replace their intrinsic component classification.

No higher-dimensional Ferrers volume identity was used as a cancellation
proof. The successful geometric clue is specific: a three-label routing
cycle with two explicitly balanced incomparable-edge crossings. A global
Ferrers-solid cut/glue invariant remains an idea, not an established result.
