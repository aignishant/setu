# Day 28 — CHECKLIST

**IDs covered:** PD-03, PD-04 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-28/lab/selecting.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the nine-part selection report including the all-NaN alignment bug, then all tests green.

## Setup

- [ ] `./m start 28` and `./m scaffold 28` run
- [ ] `days/day-28/lab/selecting.py` created
- [ ] No new packages installed

## PD-03 — the two selectors

- [ ] Can state the `.loc` / `.iloc` rule including inclusive vs exclusive slicing
- [ ] Changed one slice endpoint and **saw the row count differ**
- [ ] Sliced columns by label with `df.loc[:, 'a':'b']`
- [ ] Ran `when_the_index_is_integers()` and saw `loc` and `iloc` disagree
- [ ] Saw `df[0]` raise, and can explain why `[]` on a DataFrame means columns
- [ ] Built a boolean mask and confirmed it carries the frame's index
- [ ] Used `&` with brackets; saw `and` raise
- [ ] Confirmed `.between` is inclusive on **both** ends
- [ ] Used `.isin` and `.query` at least once each
- [ ] Re-confirmed Day 26's rule: assignment goes through `.loc`

## PD-04 — the index

- [ ] Ran `alignment_is_automatic()` and saw the union-with-NaN result
- [ ] Used `.add(other, fill_value=0)` as the explicit form
- [ ] Confirmed label order does not matter
- [ ] Ran `the_silent_reset_index_bug()` and **saw four NaN from two three-element inputs**
- [ ] Used `reindex` with and without `fill_value`
- [ ] Confirmed a duplicate index label makes `loc` return a **DataFrame**
- [ ] Checked `index.is_unique` and `index.is_monotonic_increasing`
- [ ] Can say why a sorted index makes `.loc` slicing faster
- [ ] Ran `the_leakage_shape()` and can explain why preserving the index is correct there

## Build brief

- [ ] `select` — **TODO(me)**: `.loc` only, names every missing column, validates the mask's index, returns a copy
- [ ] `assert_unique_index` — **TODO(me)**: names the duplicates and the count
- [ ] `align_frames` — **TODO(me)**: common index, same order, raises on empty overlap with numbers
- [ ] `split_by_mask` — **TODO(me)**: preserves indices, complete partition, rejects NaN masks
- [ ] Can explain why a foreign boolean mask is dangerous rather than merely wrong

## Tests that must be able to fail

- [ ] `test_select_by_columns` — green
- [ ] `test_select_reports_every_missing_column` — green
- [ ] `test_select_with_a_boolean_mask` — green
- [ ] `test_select_rejects_a_misaligned_mask` — green ← **today's real assessment**
- [ ] **Dropped the mask-index validation, watched it go red, restored it** ← do not skip
- [ ] `test_select_returns_an_independent_frame` — green (ADR-001)
- [ ] `test_assert_unique_index_passes` / `test_assert_unique_index_names_the_duplicates` — green
- [ ] `test_align_restricts_to_the_intersection` — green
- [ ] `test_align_puts_both_sides_in_the_same_order` — green
- [ ] `test_align_raises_on_the_reset_index_bug` — green
- [ ] **Removed the empty-intersection check, watched it return two empty frames instead of raising, restored it** ← do not skip
- [ ] `test_split_by_mask_preserves_indices` — green
- [ ] `test_split_by_mask_is_a_complete_partition` — green (all three assertions)
- [ ] `test_split_parts_are_independent` — green
- [ ] `test_split_rejects_a_mask_with_missing_values` — green
- [ ] `test_alignment_footgun_is_documented` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] State the `.loc` / `.iloc` rule, including the slice-endpoint difference
- [ ] Why is `df[0]` ambiguous, and what does pandas do instead?
- [ ] Describe what happens when you add two Series with partially overlapping labels
- [ ] Describe the `reset_index` bug and why it produces no error
- [ ] Why is a boolean mask from another frame dangerous?
- [ ] What does a duplicate index label do to `.loc`?
- [ ] Why does the train/test example deliberately keep its original index?

## Commit

- [ ] `./m check && ./m done 28` succeeded
