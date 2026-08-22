# Day 81 — CHECKLIST

**IDs covered:** FE-06 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-81/lab/encoding.py
uv run python -m pytest tests/test_features.py -v
```

Expected: the nine-part report ending with the encoding-choice table, then all feature tests green.

## Setup

- [ ] `./m start 81` and `./m scaffold 81` run
- [ ] `days/day-81/lab/encoding.py` created
- [ ] No new packages installed

## FE-06 — the three encodings

- [ ] Can say what a linear model actually does with an integer-coded nominal variable
- [ ] Built one-hot columns and confirmed exactly one 1 per row
- [ ] Can say when `drop_first=True` is required and when it is harmful
- [ ] Can state the **unseen-category trap** and name the sklearn fix
- [ ] Ran `cardinality_is_the_problem()`; recorded the width at 5,000 categories: ______
- [ ] Can name **two** reasons one-hot fails at that width
- [ ] Confirmed ordinal encoding reads the **dtype's** order (Day 34)
- [ ] Can say why an unordered categorical's codes must not be used

## The leak

- [ ] Ran `target_encoding_the_naive_way()` on data with **no** real effect
- [ ] Recorded the leaked correlation: ______ and the cross-validated R²: ______
- [ ] Can explain in one sentence where the leak comes from
- [ ] Ran `why_the_split_alone_does_not_fix_it()`
- [ ] Recorded train correlation ______ vs test correlation ______
- [ ] Can say what the split fixes and what it does **not**
- [ ] Can name four things inside train that are misled by the remaining leak

## The fix

- [ ] Ran `out_of_fold_encoding()` on the same data
- [ ] Confirmed the correlation dropped to near zero
- [ ] Can explain the out-of-fold rule in one sentence
- [ ] Ran `smoothing_protects_rare_categories()`
- [ ] Recorded the rare category's raw mean ______ and smoothed ______
- [ ] Can state the smoothing weight formula and what `k` controls
- [ ] Can say where `k` must be tuned, and where it must not
- [ ] Read the six-row encoding-choice table

## Build brief

- [ ] `choose_encoding` — **TODO(me)**: level-aware, refuses ordinal on an unordered dtype
- [ ] `fit_encoder` — **TODO(me)**: records the category list, smoothed target means
- [ ] `apply_encoder` — **TODO(me)**: **raises** on a width mismatch, never fits
- [ ] `target_encode_out_of_fold` — **TODO(me)**: a row's own target never used
- [ ] `assert_no_target_leak` — **TODO(me)**: reuses Day 39, asks the diagnostic question
- [ ] Can explain why a width mismatch raises rather than warns

## Tests that must be able to fail

- [ ] `test_one_hot_for_few_nominal_categories` — green
- [ ] `test_target_encoding_for_high_cardinality` — green
- [ ] `test_ordinal_requires_an_ordered_dtype` — green
- [ ] `test_ordinal_accepts_an_ordered_dtype` — green
- [ ] `test_rare_categories_are_warned_about` / `test_the_reason_names_a_number` — green
- [ ] `test_one_hot_produces_a_stable_column_set` — green
- [ ] `test_an_unseen_category_encodes_as_all_zeros` — green
- [ ] `test_a_missing_category_in_test_still_gets_its_column` — green
- [ ] **Used `pd.get_dummies` on test directly, watched the width change, fixed it** ← do not skip
- [ ] `test_ordinal_uses_the_dtype_order_not_alphabetical` — green (`[2, 0, 1]`)
- [ ] `test_target_encoding_requires_a_target` — green
- [ ] `test_smoothing_pulls_rare_categories_toward_the_global_mean` — green
- [ ] `test_no_smoothing_returns_the_raw_mean` — green
- [ ] `test_naive_target_encoding_leaks` — green ← **today's real assessment, leg 1**
- [ ] `test_out_of_fold_encoding_does_not_leak` — green ← **leg 2**
- [ ] `test_out_of_fold_preserves_a_real_signal` — green ← **leg 3**
- [ ] **Made the encoder return a constant; watched leg 2 pass and leg 3 go red** ← do not skip
- [ ] `test_out_of_fold_beats_naive_on_the_same_data` — green
- [ ] `test_out_of_fold_is_aligned_to_the_index` — green
- [ ] `test_out_of_fold_rejects_bad_arguments` — green
- [ ] `test_train_mappings_are_applied_not_refitted` — green
- [ ] `test_apply_refuses_to_see_a_target` — green
- [ ] `test_apply_rejects_a_missing_column` / `test_apply_does_not_mutate` — green
- [ ] `test_the_spec_is_json_serialisable` — green
- [ ] `test_the_leak_tripwire_fires` — green, diagnostic question present
- [ ] `test_the_tripwire_allows_an_honest_feature` — green
- [ ] `test_the_tripwire_reuses_day_39` — green
- [ ] `test_no_naive_target_encoding_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does a linear model assert when given an integer-coded nominal variable?
- [ ] When does `drop_first` help and when does it hurt?
- [ ] Describe the unseen-category trap and both directions it breaks in
- [ ] Where exactly does naive target encoding get the answer from?
- [ ] Why is fitting on train alone insufficient?
- [ ] State the out-of-fold rule in one sentence
- [ ] What does smoothing protect against, and what does `k` trade off?
- [ ] Why does the test suite need a third leg?

## Commit

- [ ] `./m check && ./m done 81` succeeded
