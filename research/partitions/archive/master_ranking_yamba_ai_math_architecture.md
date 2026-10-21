# Master Strategy: Integer Partition Breakthroughs & `yamba-ai-math` Agentic Architecture

## 1. Comparative Ranking of Open Partition Problems

To maximize our chances of securing a publishable, verifiable breakthrough using an AI-driven mathematical harness (combining empirical computation, Lean 4 formalization, and LaTeX/TikZ exposition), we evaluate the six problems across four dimensions:
*   **Scientific Impact (1–10):** Prestige and breadth of consequences across combinatorics, number theory, and representation theory.
*   **Overall Difficulty (1–10):** Resistance of the general problem to known human methods.
*   **AI-Agent Tractability (1–10):** How well the problem decomposes into finite computational search, symbolic algebra (SageMath), SAT/SMT solving, and inductive Lean 4 formalization.
*   **Breakthrough Yield Rank:** Our strategic ordering of where we can realistically extract a novel theorem, family verification, or explicit construction first.

| Yield Rank | Problem Name | Source Text | Impact | Difficulty | AI Tractability | Why It Ranks Here for Our AI Pipeline |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **#1 (Best)** | **$e$-Positivity & Schur-Positivity in $(P, \omega)$-Partitions** | Stanley (*EC Vol. 1 & 2*) | 8.5 / 10 | 7.0 / 10 | **9.5 / 10** | Highly discrete and finite-checkable. Agents can systematically search unit-interval orders/posets up to $n=14$, discover new $e$-positive families or minimal counterexamples, and construct explicit sign-reversing involutions. |
| **#2** | **Bijective Proofs for Rogers-Ramanujan-Type Identities** | Andrews & Eriksson | 8.0 / 10 | 7.5 / 10 | **9.0 / 10** | Finding a bijection between two equinumerous partition sets for $n \le 25$ can be framed as a structured graph-matching / cellular automaton ruleset synthesis problem—ideal for genetic/LLM code evolution and Lean 4 finite/inductive verification. |
| **#3** | **Combinatorial cranks & Ranks for Partition Congruences** | Andrews & Eriksson | 8.5 / 10 | 8.0 / 10 | **8.0 / 10** | Searching for linear/nonlinear combinations of partition statistics (cranks/ranks) that divide $p(An+B)$ into $m$ equinumerous classes is a pure symbolic/algebraic search problem where AI agents excel at pattern detection. |
| **#4** | **Plane Partitions Under Exotic Symmetry & Boundary Classes** | Stanley (*EC Vol. 2*) | 7.5 / 10 | 8.0 / 10 | **7.5 / 10** | Guessing closed-form product formulas (via Krattenthaler's `Rate` or LLL lattice reduction) and proving them via Lindström–Gessel–Viennot determinant evaluations is highly automatable once a new boundary class is defined. |
| **#5** | **Kronecker Coefficients Positivity ($g(\lambda, \mu, \nu) > 0$)** | Stanley (*EC Vol. 2*) | 10 / 10 | 9.8 / 10 | **6.0 / 10** | The "Holy Grail" of algebraic combinatorics. While the general problem is too vast, restricting to 3-row shapes or hook-plus-two-row shapes yields tractable sub-problems for polytope/hive rule synthesis. |
| **#6** | **Asymptotic Parity & Density Distribution of $p(n) \pmod m$** | Andrews & Eriksson | 9.5 / 10 | 9.9 / 10 | **3.5 / 10** | Relies heavily on deep analytic number theory, $L$-functions, and Deligne-type bounds on modular forms rather than discrete combinatorial constructions. Least suited for direct constructive/bijective discovery. |

---

## 2. Top Three Recommended Targets for Our Immediate Collaboration

Based on the ranking above, here are the **three problems** you and I should immediately tackle together, generate initial empirical/symbolic results right here, and then hand off to your **Claude Code / Codex** environment on dedicated branches:

1.  **Target Alpha (`branch: feat/poset-e-positivity`):** *Stanley–Stembridge $e$-Positivity & Schur-Positivity for Restricted Poset Families.*
    *   **Our Angle:** Attack a specific, unproved sub-class of $(3+1)$-free posets (e.g., spiders, $K$-chains, or specific unit interval orders) and use an agentic loop to synthesize an explicit **sign-reversing involution** on ribbon tableaux, proving $e$-positivity and formalizing the involution in Lean 4.
2.  **Target Beta (`branch: feat/rr-bijection-synthesis`):** *Algorithmic Bijection Synthesis for Higher-Modulus Rogers-Ramanujan Identities (e.g., Kanade–Russell or Göllnitz–Gordon companions).*
    *   **Our Angle:** Take a known $q$-series identity lacking a clean direct bijection (or a recently conjectured Kanade–Russell identity), compute exact partition tables for $n \le 30$, and train an evolutionary/symbolic agent to discover a local Ferrers-diagram transformation rule (generalizing Bressoud/Garsia-Milne), complete with automated TikZ Ferrers diagram visualizations.
3.  **Target Gamma (`branch: feat/generalized-crank-search`):** *Automated Discovery of Combinatorial Cranks for Higher Prime Power Partition Congruences.*
    *   **Our Angle:** Use symbolic regression and modular arithmetic agents to search the space of partition statistics (bg-rank, $M_2$-rank, Dyson rank variants) on overpartitions or $k$-regular partitions to find an explicit statistic that splits $p_{\text{restricted}}(An+B)$ into $m$ equal residue classes.

---

## 3. Upgrading `github.com/cyamba/yamba-ai-math`

To transform `yamba-ai-math` into a premier autonomous mathematical discovery engine capable of taking a `(Problem Markdown)` $\longrightarrow$ `(Customized Agentic Fleet & Harness)` $\longrightarrow$ `(Verified Lean 4 Proof + Publication-Ready LaTeX/TikZ PDF)`, we should architect the repository around a **Branch-Per-Problem Determinism Model**.

### 3.1 Proposed Repository Directory Structure

```text
yamba-ai-math/
├── .claude/
│   ├── commands/
│   │   ├── init-problem-branch.md     # Slash command: /project:init-problem-branch
│   │   ├── run-fleet-cycle.md         # Slash command: /project:run-fleet-cycle
│   │   └── compile-paper.md           # Slash command: /project:compile-paper
│   └── agents/                        # Sub-agent system prompts & tool permissions
│       ├── 01_explorer_sage.md
│       ├── 02_conjecturer_symbolic.md
│       ├── 03_redteam_falsifier.md
│       ├── 04_lean4_formalizer.md
│       └── 05_exposition_tikz.md
├── harness/
│   ├── orchestrator.py                # State machine managing Blackboard & agent handoffs
│   ├── tools/
│   │   ├── sage_runner.py             # Dockerized SageMath / SymPy execution sandbox
│   │   ├── sat_smt_bridge.py          # Z3 / Kissat wrapper for finite bijection/involution search
│   │   ├── oeis_query.py              # Local/API OEIS sequence matcher
│   │   └── lean_repl_bridge.py        # Interactive Lean 4 / Mathlib4 tactic feedback loop
│   └── schemas/
│       └── blackboard_state.json      # Shared mathematical memory schema
├── problems/                          # The 6 Problem Markdown specs we are generating today
│   ├── 01_rogers_ramanujan_bijections.md
│   ├── 02_partition_congruence_cranks.md
│   ├── 03_partition_parity_density.md
│   ├── 04_kronecker_coefficients.md
│   ├── 05_plane_partition_symmetries.md
│   └── 06_poset_quasisymmetric_positivity.md
├── workspace/                         # Populated dynamically per Git branch
│   ├── data/                          # Empirical JSON/CSV tables generated by Explorer
│   ├── conjectures/                   # Candidate theorems & falsification logs
│   ├── lean/                          # Lean 4 project (lakefile.lean, Mathlib4 dependencies)
│   └── paper/                         # LaTeX source, TikZ generators, compiled PDF
└── playbooks/
    ├── bijective_synthesis.yaml
    ├── positivity_involution.yaml
    └── modular_crank_search.yaml
```

---

### 3.2 The `(Problem) -> (Agentic Fleet Topology & Harness)` Pipeline

Instead of using a generic chat loop, `yamba-ai-math` should map each problem class to a specific **Multi-Agent Graph Topology** coordinated via a shared `blackboard_state.json`.

```
                  +---------------------------------------+
                  |   PROBLEM SPECIFICATION (.md file)    |
                  +-------------------+-------------------+
                                      |
                                      v
                  +---------------------------------------+
                  |     HARNESS ROUTER & ORCHESTRATOR     |
                  |  Selects Topology (Bijective / Poset) |
                  +-------------------+-------------------+
                                      |
          +---------------------------+---------------------------+
          |                           |                           |
          v                           v                           v
+-------------------+       +-------------------+       +-------------------+
|  AGENT 1: SAGE    |       | AGENT 2: SYMBOLIC |       | AGENT 3: RED-TEAM |
|  EMPIRICAL ENGINE |------>| CONJECTURER / SAT |<----->|   FALSIFIER       |
| (Generates tables,|       | (Synthesizes maps,|       | (Hunts counter-   |
|  posets, q-series)|       |  involutions,LLL) |       |  examples n=1..30)|
+-------------------+       +---------+---------+       +-------------------+
                                      |
                         [Survives Falsification!]
                                      |
                                      v
                            +-------------------+
                            | AGENT 4: LEAN 4   |
                            | FORMALIZER        |
                            | (Mathlib4 proofs, |
                            |  decide/omega/ind)|
                            +---------+---------+
                                      |
                           [Zero 'sorry' tokens!]
                                      |
                                      v
                            +-------------------+
                            | AGENT 5: SCRIBE & |
                            | VISUALIZER        |
                            | (LaTeX + Python   |
                            |  TikZ Young/Poset)|
                            +-------------------+
```

#### The 5 Specialized Agent Roles in the Fleet:
1.  **`Explorer-Sage` (Empirical Generator):**
    *   *Tools:* SageMath (`sage.combinat.partition`, `sage.combinat.posets`, `sage.combinat.sf`), Python, OEIS API.
    *   *Role:* Generates exact partition sets, Ferrers diagrams, poset Hasse diagrams, and symmetric function expansions for $n \le 25$. Outputs structured JSON artifacts to `workspace/data/`.
2.  **`Conjecturer-Symbolic` (The Synthesizer):**
    *   *Tools:* Z3 SMT Solver, `FunSearch`-style evolutionary Python mutation, LLL lattice reduction.
    *   *Role:* For bijections or sign-reversing involutions, it formulates the search as either a bipartite matching constraint problem (Z3) or evolves a Python function `def phi(partition): ...` scored by how many target constraints it satisfies across $n \le 18$.
3.  **`RedTeam-Falsifier` (Adversarial Critic):**
    *   *Tools:* Property-based testing (`Hypothesis`), extremal combinatorics heuristics.
    *   *Role:* Attempts to break every conjectured formula or bijection produced by `Conjecturer-Symbolic` on edge-case partitions (e.g., all 1s, hooks, self-conjugate shapes, $n = 20..35$). A conjecture cannot advance to Lean 4 until it survives 10,000 adversarial checks.
4.  **`Formalizer-Lean4` (Verification Engine):**
    *   *Tools:* Lean 4 (`lake build`), `Mathlib.Combinatorics.Young.YoungDiagram`, `Mathlib.Data.Nat.PartEnat`, `aesop`, `decide`.
    *   *Role:* Translates the surviving Python bijection or algebraic identity into Lean 4 definitions. Uses computational reflection (`by decide`) to prove finite base cases ($n \le 20$) automatically, and structural induction for general theorems.
5.  **`Exposition-TikZ-Scribe` (Publication Architect):**
    *   *Tools:* `pdflatex`, `ytableau`, `tikz-cd`, Python-to-TikZ script generators.
    *   *Role:* Reads the verified `blackboard_state.json` and Lean 4 files, writes a rigorous mathematical exposition, and executes Python scripts that automatically emit TikZ code for Ferrers diagrams, Young tableaux, Hasse diagrams, and bijective arrow flows.

---

### 3.3 The Claude Code Branch-Per-Problem Playbook

To execute this cleanly in **Claude Code**, you can add a custom slash command `.claude/commands/run-problem-branch.md` so that launching a research campaign is a single command:

1.  **Branch Initialization:**
    ```bash
    git checkout -b research/prob-06-poset-epositivity
    claude "/project:init-problem-branch problems/06_poset_quasisymmetric_positivity.md"
    ```
2.  **Automated Playbook Phases (enforced by a Git pre-commit/stage gate):**
    *   **Gate 1 (`DATA_READY`):** `Explorer-Sage` must populate `workspace/data/baseline_tables.json` with verified small-$n$ examples and sanity checks against known theorems.
    *   **Gate 2 (`CONJECTURE_LOCKED`):** `Conjecturer-Symbolic` and `RedTeam-Falsifier` iterate in a sub-agent loop until a Python implementation of the bijection/involution/crank achieves **100% accuracy** on all test cases in `baseline_tables.json`.
    *   **Gate 3 (`LEAN_VERIFIED`):** `Formalizer-Lean4` creates `workspace/lean/MainTheorem.lean`. The harness runs `lake build` in a loop, feeding compiler errors back to the agent until exit code `0` is achieved with zero `sorry` axioms on the core theorems (or clearly isolated lemmas).
    *   **Gate 4 (`PAPER_COMPILED`):** `Exposition-TikZ-Scribe` generates `workspace/paper/main.tex`, compiles all TikZ figures (Ferrers diagrams, lattice paths, poset Hasse diagrams), runs `latexmk -pdf`, and checks the rendered PDF pages for visual layout and mathematical clarity.