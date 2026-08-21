# Day 22 — CHECKLIST

**IDs covered:** NP-04, NP-05 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-22/lab/broadcasting.py
uv run python -m pytest tests/test_arrays.py -v
```

Expected: the nine-part report ending with the attention reshape round-trip, then all tests green.

## Setup

- [ ] `./m start 22` and `./m scaffold 22` run
- [ ] `days/day-22/lab/broadcasting.py` created
- [ ] No new packages installed

## NP-04 — broadcasting

- [ ] Can state the rule in one sentence, including the right-to-left alignment
- [ ] Saw `(3,4) + (4,)` succeed and `(3,4) + (3,)` fail — and read the error message
- [ ] Fixed the failure with `[:, None]`
- [ ] Used `np.broadcast_shapes` to check before computing
- [ ] Saw the **zero stride** in a broadcast view and know why it is read-only
- [ ] Confirmed `axis=0` collapses rows and `axis=1` collapses columns
- [ ] Can state the mnemonic: *the axis you name is the one that disappears*
- [ ] Used `keepdims=True` and know when it saves you a `[:, None]`
- [ ] Wrote pairwise distances with `[:, None, :] - [None, :, :]`
- [ ] Computed the memory of the `(n, n, d)` intermediate at n=5000 and understood the warning
- [ ] Know that `.flat` / `ndenumerate` / row iteration are for **debugging only**

## NP-05 — reshaping

- [ ] Used `reshape` with `-1`
- [ ] Saw `reshape` return a view, and saw a mismatched element count raise
- [ ] Confirmed `ravel` can be a view and `flatten` always copies
- [ ] Confirmed `.T` is a view sharing memory
- [ ] Used `[:, None]`, `[None, :]`, `expand_dims`, `squeeze`
- [ ] Used `concatenate` and `stack` and can say exactly how they differ
- [ ] Used `split` and `array_split` and know which allows ragged parts
- [ ] Ran `the_attention_reshape()` and confirmed the round-trip
- [ ] Noted that those two lines are Day 143's multi-head attention

## Build brief

- [ ] `standardise` — **TODO(me)**: broadcasting only, returns `(out, means, stds)`, handles zero variance
- [ ] `apply_standardisation` — **TODO(me)**: uses pre-computed statistics, validates shapes
- [ ] `pairwise_distances` — **TODO(me)**: chunked, exact-zero diagonal, symmetric
- [ ] `batch` — **TODO(me)**: ragged final batch, validates size
- [ ] Can explain how `standardise`'s **signature** prevents leakage

## Tests that must be able to fail

- [ ] `test_standardise_produces_zero_mean_unit_std` — green
- [ ] `test_standardise_does_not_modify_the_input` — green
- [ ] `test_standardise_handles_a_constant_column` — green
- [ ] **Removed the zero-variance guard, saw `inf`/`nan`, restored it** ← do not skip
- [ ] `test_apply_uses_train_statistics_not_test_statistics` — green ← **today's real assessment**
- [ ] **Made `apply_standardisation` recompute its own statistics, watched it go red, fixed it** ← do not skip
- [ ] `test_apply_rejects_a_shape_mismatch` — green
- [ ] `test_pairwise_distances_are_correct` — green
- [ ] `test_pairwise_diagonal_is_exactly_zero` — green
- [ ] **Removed the negative clamp before `sqrt`, watched the diagonal go non-zero (or NaN), fixed it** ← do not skip
- [ ] `test_pairwise_is_symmetric` — green
- [ ] `test_pairwise_chunking_matches_the_unchunked_result` — green
- [ ] `test_batch_sizes_and_completeness` — green (ragged final batch, third time)
- [ ] `test_batch_empty_returns_nothing` / `test_batch_rejects_zero_size` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the broadcasting rule, including which end alignment starts from
- [ ] Why does `(3,4) + (3,)` fail, and what is the one-token fix?
- [ ] What does a zero stride mean, and why is a broadcast view read-only?
- [ ] Broadcasting makes the stretch free — what is still *not* free?
- [ ] What is the difference between `ravel` and `flatten`, and which earlier day is that?
- [ ] What is the difference between `concatenate` and `stack`?
- [ ] Why does `standardise` return its statistics instead of just the transformed array?
- [ ] Why can a pairwise diagonal come out non-zero, and what is the fix?

## Commit

- [ ] `./m check && ./m done 22` succeeded
