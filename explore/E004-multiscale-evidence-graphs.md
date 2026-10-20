---
id: E004
title: "Query-sensitive multiscale compression of evidence graphs"
status: seed
category: attention-geometry
tags: [spectral-graphs, multiscale, attention, sparsification]
---

# Query-sensitive multiscale compression of evidence graphs

## Question

Can an evidence graph be compressed at several scales while retaining the relations needed to answer a specified query? The opportunity is to replace repeated dense token interaction with a cheaper operator whose approximation target is explicit.

## Known foothold

[Graph Sparsification by Effective Resistances](https://epubs.siam.org/doi/10.1137/080734029) provides a rigorous foundation for approximating undirected graph Laplacian quadratic forms. [Structured state space duality](https://arxiv.org/abs/2405.21060) demonstrates that useful sequence computations can be reorganized through matrix structure. Neither result licenses substituting a Laplacian sparsifier for general directed, input-dependent softmax attention.

## Proposed gap

**Novelty status: NOT VERIFIED.** Design a restricted attention layer operating as a positive diffusion or regularized graph solve, then derive which query answers survive elimination and sparsification. Compare query-aware coarse graphs with global spectral compression. Schur complements, algebraic multigrid, graph pooling, and graph transformers are close prior art.

## Mathematical setup

Use a weighted undirected evidence graph with Laplacian L and answer signal x = (L + λI)⁻¹b, λ > 0. A query reads a linear functional aᵀx. Coarsening uses a specified restriction/prolongation pair; retained fine nodes represent query anchors and fragile relations. Only later add learned weights, with positivity and conditioning constraints made explicit.

## Unproved theorem targets

1. **Unproved:** Bound query-answer error for a combination of approximate elimination and spectral sparsification in terms of λ, operator error, and the query's energy norm. Determine when this is substantially sharper than a global Euclidean bound.
2. **Unproved:** For a hierarchical graph family, exhibit a query-preserving coarse representation with lower end-to-end cost than the specified dense diffusion implementation, including construction and update costs.

## Counterexample or obstruction

A single low-weight edge may carry the only logically decisive fact. Preserving diffusion energy need not preserve symbolic entailment or directed relational composition. Constructing the coarse graph per query may cost more than solving the original problem.

## Minimal falsification experiment

Generate hierarchical graphs containing both smooth diffusion labels and brittle path-existence labels. Compare dense solves, global sparsification, query-aware compression, and exact graph algorithms. Reject semantic generality immediately if gains occur only for smooth labels; retain that restricted result if useful.

## Success and cost metrics

Query functional error, classification margin preservation, brittle-relation failures, graph construction time, amortization threshold, retained edges, peak memory, and measured solve latency.

## Next artifact

A restricted operator definition and one adversarial bridge-edge counterexample before any transformer implementation.
