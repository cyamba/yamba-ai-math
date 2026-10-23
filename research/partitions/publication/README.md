# The beauty of cancellation

A recreational-mathematics feature by Christopher Yamba for Yamba AI Math.
This exposition explains the established Cho–Huh height-two positivity theorem
and the project's completed all-finite-alphabet Lean formalization. It makes
no claim to a new general-height open-problem solution.

- `article.html`: canonical accessible article body, shared by three websites.
- `metadata.json`: title, date, canonical URL and attribution scope.
- `assets/`: two conceptual artworks (hero and portrait cover), three exact
  mathematical diagrams in SVG/PNG, a 30-second silent H.264 video, captions
  and the complete social download.
- `social/`: six 1080 × 1350 carousel images, five editable SVG cards, Facebook
  and Instagram captions, and image descriptions.
- `manifest.json`: exact SHA-256/byte inventory of the released article/media.
- `review.md`: separate semantic and visual review, including the resolved
  missing-glyph finding and final derivative hashes.
- `prompts.md`: prompts and provenance for the built-in image-generation tool.

The final proof declaration is `PartitionH3.height_two_survivor_expansion`
in `../mathlib/PartitionH3/H3.lean`; its natural-coefficient companion is
`PartitionH3.height_two_survivor_expansion_nat`. Verification is recorded in
`../mathlib/verification.json`. This publication work does not change the proof.

The hero and cover are conceptual AI-generated artwork, not literal proof
figures. SVG diagrams and social-card mathematics were authored exactly and
checked visually against the three-vertex example and local signed-array move.
The short video is a silent six-card sequence, five seconds per card, with a
WebVTT transcript. It uses no music, model API fallback or new dependencies.

Publication targets:

- https://www.christopheryamba.com/posts/the-beauty-of-cancellation/
  (also indexed in Blog, News and Math)
- https://news.yambacode.com/the-beauty-of-cancellation/
- https://autodidactic-math-traveler.vercel.app/articles/the-beauty-of-cancellation/

The lead authored the canonical copy, mathematical illustrations, social pack
and personal-site integration. Separate workers integrated YambaCode and Math
Traveler; a distinct critic reviewed mathematical/attribution claims and final
visuals in two bounded rounds. This was a manually coordinated publication task,
not a claim of a harness evaluation win or independent model errors.

The academic LaTeX source remains in its existing editor and was not changed
by this companion feature.
