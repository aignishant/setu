# Day 29 — CHECKLIST

**IDs covered:** PD-05, PD-06 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-29/lab/vectorise.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the ladder timings with measured slowdown factors, then all tests green.

## Setup

- [ ] `./m start 29` and `./m scaffold 29` run
- [ ] `days/day-29/lab/vectorise.py` created
- [ ] No new packages installed

## PD-05 — the ladder

- [ ] Ran `the_ladder()`; recorded **your** slowdown factors:
  - apply(axis=1): ______× · itertuples: ______× · iterrows: ______×
- [ ] Confirmed all five approaches produced **identical** results
- [ ] Can explain why a dataframe being columnar makes row iteration slow
- [ ] Ran `iterrows_also_destroys_dtypes()` and saw `int16` become a boxed Python int
- [ ] Confirmed `itertuples` preserves dtypes
- [ ] Can recite the seven-rung ladder, or at least the top three and the bottom two
- [ ] Understands that `apply(axis=1)` is **not** vectorised

## Conditionals without apply

- [ ] Used `np.where` for two branches
- [ ] Used `np.select` for many branches and know that **first match wins**
- [ ] Used `.map` with a dict and **checked `.isna().sum()` afterwards**
- [ ] Used `pd.cut` and noticed it returns a categorical
- [ ] Read the four conditions under which `apply(axis=1)` is defensible

## PD-06 — sorting and ranking

- [ ] Multi-key sorted with a direction per key
- [ ] Used `kind='stable'` and can say when it matters
- [ ] Used `nlargest` and can say why it beats `sort_values().head(k)`
- [ ] Confirmed `sort_values` puts NaN **last** by default
- [ ] Ran `ranking_and_ties()` and **read all five output lines**
- [ ] Can describe what each of the five methods does in one phrase
- [ ] Used `rank(pct=True)`
- [ ] Ran `top_k_per_group()` and can explain why it uses `method='first'`

## Build brief

- [ ] `add_derived` — **TODO(me)**: new frame, refuses to overwrite, validates the index
- [ ] `bucketise` — **TODO(me)**: `np.select`, ordered categorical, NaN stays NaN, validates the spec
- [ ] `top_n_per_group` — **TODO(me)**: `rank(method='first')`, preserves the index
- [ ] `rank_column` — **TODO(me)**: validates the method name against all five
- [ ] No `.apply(axis=1)` anywhere in `src/setu/`

## Tests that must be able to fail

- [ ] `test_add_derived_returns_a_new_frame` — green
- [ ] `test_add_derived_refuses_to_overwrite` — green
- [ ] `test_add_derived_rejects_a_misaligned_result` — green
- [ ] `test_bucketise_assigns_the_right_buckets` — green
- [ ] `test_bucketise_keeps_nan_as_nan` — green
- [ ] `test_bucketise_result_is_ordered_categorical` — green
- [ ] `test_bucketise_rejects_bad_specs` — three green cases
- [ ] `test_bucketise_is_vectorised` — green
- [ ] **Rewrote `bucketise` with `.apply`, watched the timing test go red, reverted** ← do not skip
- [ ] `test_top_n_per_group` — green
- [ ] `test_top_n_per_group_preserves_the_index` — green
- [ ] `test_top_n_per_group_is_deterministic_with_ties` — green ← **today's real assessment**
- [ ] **Switched to `method='min'`, watched it return four rows for n=2, reverted** ← do not skip
- [ ] `test_top_n_per_group_handles_a_small_group` — green
- [ ] `test_rank_column_rejects_an_unknown_method` — green
- [ ] `test_rank_methods_differ` — three green cases

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why is `iterrows` slow — name all three reasons, not just "loops are slow"
- [ ] Why does `iterrows` destroy your dtypes?
- [ ] Why is `apply(axis=1)` not the vectorised option people think it is?
- [ ] When does `np.select` order matter?
- [ ] What must you check after every `.map`?
- [ ] Describe all five `rank` methods and give a use for each
- [ ] Why does top-n-per-group need `method='first'` specifically?

## Commit

- [ ] `./m check && ./m done 29` succeeded
