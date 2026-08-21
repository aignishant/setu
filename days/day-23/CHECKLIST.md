# Day 23 — CHECKLIST

**IDs covered:** NP-06, NP-07 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-23/lab/ufuncs.py
uv run python -m pytest tests/test_arrays.py -v
```

Expected: the ten-part report including a measured argsort-vs-argpartition ratio, then all tests green.

## Setup

- [ ] `./m start 23` and `./m scaffold 23` run
- [ ] `days/day-23/lab/ufuncs.py` created
- [ ] No new packages installed

## NP-06 — ufuncs

- [ ] Confirmed `+` **is** `np.add`
- [ ] Used `.reduce`, `.accumulate`, `.outer` on a ufunc
- [ ] Know that `np.add.reduce` is `np.sum`
- [ ] Used `out=` and can say what it saves on a large array
- [ ] Used `where=` and know why `out` must be initialised, not `np.empty`
- [ ] Learned the **safe-division idiom** (`out=` + `where=`) as a unit
- [ ] Used `np.errstate` with `"raise"` and know when you would want it
- [ ] Confirmed `argmin` returns a flattened index; used `np.unravel_index`
- [ ] Used `np.unique(return_counts=True)`, `np.bincount`, `np.isin`, `np.count_nonzero`

## NP-07 — sorting and searching

- [ ] Can state the difference between `sort` and `argsort` in one sentence
- [ ] Used `argsort` indices to reorder a **different** array
- [ ] Compared `argsort(x)[::-1]` with `argsort(-x)` on tied values and saw the difference
- [ ] Can explain why the negation version preserves stability
- [ ] Used `kind='stable'` explicitly once
- [ ] Ran the `argpartition` benchmark; recorded the ratio: ______×
- [ ] Can state what `argpartition` guarantees and what it does **not**
- [ ] Used `np.searchsorted`, `np.flatnonzero`, `np.argwhere`
- [ ] Used `np.lexsort` and confirmed the **last** key is primary
- [ ] Connected `lexsort` back to Day 15's `Paper.__lt__`

## Build brief

- [ ] `safe_divide` — **TODO(me)**: `out=` + `where=`, no inf, no nan, **no warning**, broadcasts
- [ ] `top_k` — **TODO(me)**: both methods, identical results, NaN last, validates k
- [ ] `value_counts` — **TODO(me)**: `np.unique` + `lexsort`, JSON-serialisable output
- [ ] `running_stats` — **TODO(me)**: no Python loop for `cummean`
- [ ] Can explain why keeping both `top_k` methods is a design decision, not duplication

## Tests that must be able to fail

- [ ] `test_safe_divide_returns_fill_not_inf` — green
- [ ] `test_safe_divide_emits_no_warning` — green
- [ ] **Implemented it as divide-then-patch, watched the warning test go red, switched to `out=`/`where=`** ← do not skip
- [ ] `test_safe_divide_broadcasts_a_scalar` — green
- [ ] `test_top_k_is_descending` — green
- [ ] `test_top_k_ties_break_by_lower_index` — green
- [ ] `test_both_methods_agree_with_each_other` — two green cases ← **today's real assessment**
- [ ] `test_both_methods_agree_when_there_are_many_ties` — green
- [ ] **Returned `argpartition(...)[:k]` unsorted, watched the ties test go red, sorted the candidates** ← do not skip
- [ ] `test_top_k_puts_nan_last` — green
- [ ] **Removed the NaN handling, saw NaN become the top hit, restored it** ← do not skip
- [ ] `test_top_k_larger_than_the_array` / `test_top_k_rejects_zero` — green
- [ ] `test_value_counts_orders_by_count_then_value` — green
- [ ] `test_value_counts_returns_json_serialisable_types` — green
- [ ] `test_running_stats` / `test_running_stats_on_empty` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is a ufunc, and what do `out=` and `where=` buy you?
- [ ] Write the safe-division idiom from memory
- [ ] Why does `argsort` return indices rather than values, and why does that matter for retrieval?
- [ ] Why does reversing a stable sort change the tie order, and what do you do instead?
- [ ] What does `argpartition` guarantee, and what must you do afterwards?
- [ ] Where does NaN land in an ascending sort, and what happens when you negate?
- [ ] Which `lexsort` key is primary?
- [ ] Draw the retrieval diagram from §1 and name three later days that use it

## Commit

- [ ] `./m check && ./m done 23` succeeded
