# Next iteration of the `eth` set: where to start

Fresh-session entry point, written at the end of iteration 1 (2026-10-29). Read this, then
[RANKING.md](RANKING.md). The upstream theorem is still an **unverified claim**
([SOURCE.md](SOURCE.md)); check [NR-002](../../novelty_radar/NR-002-eth-refutations.md) for news of
the working group's report before relying on anything conditional.

## State at hand-off

* 37 problems, ranked; 9 subresults; the Lean certificate in [`lean/verification.json`](lean/verification.json)
  (rebuild with `python3 verify.py` in `lean/`, Lean toolchain from `lean-toolchain` on `PATH`).
* Tier 1 has three program contracts; ETH001 pins its completion statement in
  [targets/ETH001.md](targets/ETH001.md).
* Exact small cases of CP(Q, R) up to $Q=6$ are in
  [`experiments/results/`](experiments/results/); larger cases need structure (see the notes at
  the end of RANKING.md).
* A draft article ([articles/](articles/README.md)) awaits the operator's decision; it must not
  be posted or submitted from a session.

## First moves

1. Merge state: confirm that the branch `eth-consequences-iter1` has been merged into `main`, and
   start new work on a fresh branch in its own worktree (root `CLAUDE.md`).
2. Read the last ten lines of [meta/session-log.md](../../meta/session-log.md) and append one line
   for the iteration's workflow decision.
3. Plan the flagship program and inspect the assignment:

   ```sh
   python3 -m harness plan programs/eth-point-dependent-designs.json
   python3 -m harness packet programs/eth-point-dependent-designs.json
   ```

   A packet is an unexecuted task until a researcher supplies its result
   ([programs/contract.md](../../programs/contract.md)).
4. Give the construction and lower-bound tracks of ETH001 their first packets independently,
   before either sees the other's answer; keep the critic separate from both.
5. Under the pinned target, every proved claim declares `target_relation` and `scope_delta`;
   small-case data are `empirical`.

## Do not

* claim an exponent improvement without a Lean-checked design lemma, a re-derived cost account
  and the critic's acceptance;
* treat a method-level barrier as a barrier for all algorithms;
* cite a source in a subresult without a reading-list entry and inspection level.
