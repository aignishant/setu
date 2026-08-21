# Day 21 — CHECKLIST

**IDs covered:** NP-03 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-21/lab/indexing.py
uv run python -m pytest tests/test_arrays.py -v
```

Expected: the six-part indexing report ending with the leakage demonstration, then all tests green.

## Setup

- [ ] `./m start 21` and `./m scaffold 21` run
- [ ] `days/day-21/lab/indexing.py` created
- [ ] No new packages installed

## NP-03 — indexing modes

- [ ] Confirmed `a[0]` returns a NumPy scalar, not a Python `int`
- [ ] Used `m[1, 2]` and can say why `m[1][2]` is worse
- [ ] Confirmed `m[:, 1]` drops a dimension and `m[:, 1:2]` keeps it
- [ ] Confirmed an out-of-range **slice** is empty but an out-of-range **index** raises
- [ ] Used `...` (Ellipsis) at least once
- [ ] Used fancy indexing with a list of positions
- [ ] Built a boolean mask and counted it with `.sum()`
- [ ] Combined conditions with `&` **and the required brackets**
- [ ] Saw `and` on arrays raise `ValueError`, and connected it to Day 5
- [ ] Used `np.where` in both its two-branch and one-argument forms

## The view trap

- [ ] Wrote to a slice and watched the **parent change**
- [ ] Confirmed `view.base is a` and `copy.base is None`
- [ ] Used `np.shares_memory` and know why it beats checking `.base`
- [ ] Confirmed basic indexing → view, fancy/boolean → copy
- [ ] Ran `assignment_through_indexing()` and can explain the `__getitem__` / `__setitem__` asymmetry
- [ ] Ran `the_leakage_shape()` and saw `data` modified through `train`
- [ ] Can state the Day 79 rule this sets up

## Build brief

- [ ] `is_view_of` — **TODO(me)**, uses `np.shares_memory`
- [ ] `safe_split` — **TODO(me)**: shuffles indices not data, returns copies, validates the fraction
- [ ] `top_k_indices` — **TODO(me)**: descending, ties by lower index, handles k > n
- [ ] `clip_outliers` — **TODO(me)**: returns new, passes NaN through, validates bounds
- [ ] Noted that `top_k_indices` **is** Day 155's retrieval primitive

## Tests that must be able to fail

- [ ] `test_a_slice_is_a_view` / `test_a_copy_is_not_a_view` / `test_boolean_indexing_returns_a_copy` — green
- [ ] `test_split_returns_independent_arrays` — green ← **today's real assessment**
- [ ] **Returned `values[:n]` from `safe_split`, watched it go red, fixed it** ← do not skip
- [ ] `test_split_does_not_modify_the_source` — green
- [ ] **Used `rng.shuffle(values)`, watched it go red, switched to shuffling indices** ← do not skip
- [ ] `test_split_sizes_and_completeness` — green
- [ ] `test_split_is_reproducible_and_actually_shuffles` — green
- [ ] `test_split_rejects_impossible_fractions` — four green cases
- [ ] `test_split_rejects_a_single_row` — green
- [ ] `test_top_k_is_descending` — green
- [ ] `test_top_k_breaks_ties_by_lower_index` — green
- [ ] **Wrote `argsort(x)[::-1]`, watched the tie test go red, fixed it** ← do not skip
- [ ] `test_top_k_larger_than_the_array` / `test_top_k_rejects_zero` — green
- [ ] `test_clip_does_not_modify_the_caller` — green
- [ ] `test_clip_clamps_both_ends` — green
- [ ] `test_clip_passes_nan_through` — green
- [ ] **Hand-rolled clip with `np.where`, watched NaN get clamped, switched to `np.clip`** ← do not skip
- [ ] `test_clip_rejects_inverted_bounds` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Which indexing operations return a view and which return a copy?
- [ ] Why does fancy indexing have to copy?
- [ ] How do you check, definitively, whether two arrays share memory?
- [ ] Why does reading `a[mask]` copy while assigning to `a[mask]` writes back?
- [ ] Describe the leakage bug this enables, and the Day 79 rule that prevents it
- [ ] Why must you write `(a > 1) & (a < 5)` with brackets?
- [ ] Why does a hand-rolled `np.where` clip mishandle NaN?

## Commit

- [ ] `./m check && ./m done 21` succeeded
