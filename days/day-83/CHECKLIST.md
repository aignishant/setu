# Day 83 — CHECKLIST · **PHASE 10 GATE**

**IDs covered:** FE-08, FE-09 · **Principles served:** 1, 7, 8, 10 · **Artifact:** a leak-proof pipeline

## Demo command

```bash
uv run python days/day-83/lab/pipeline.py
uv run python scripts/build_features.py
uv run python -m pytest -q
```

Expected: the eight-part report with the two selection scores, then the build script exits 0, then
the whole suite green.

## Setup

- [ ] `./m start 83` and `./m scaffold 83` run
- [ ] Files created: `days/day-83/lab/pipeline.py`, `scripts/build_features.py`
- [ ] No new packages installed

## FE-08 — the selection leak

- [ ] Ran `the_selection_leak()`; recorded the accuracy: ______ (chance is 0.50)
- [ ] Can say why the cross-validation *looked* correct
- [ ] Can say exactly when the leak happened
- [ ] Ran `selection_inside_the_fold()` on identical data; recorded: ______
- [ ] Can state what changed between the two runs
- [ ] Can state the single question that decides where a step goes
- [ ] Ran `selection_methods()`; classified each as target-blind or target-aware
- [ ] Ran `univariate_selection_misses_interactions()`
- [ ] Confirmed XOR features score no better than noise individually
- [ ] Can say what univariate selection is good for, and what it is not
- [ ] Can name the bias in tree importances and the Day-100 alternative

## FE-09 — the pipeline

- [ ] Built a `ColumnTransformer` with different treatment per column group
- [ ] Confirmed a column **silently vanished** under `remainder='drop'`
- [ ] Can say why `remainder` must always be stated
- [ ] Ran `the_pipeline_makes_the_rule_structural()`
- [ ] Can list what is recomputed on every fold, in order
- [ ] Can name all seven fit/apply rules from Days 76–82 it now enforces
- [ ] Read `what_a_pipeline_does_not_fix()` and can name all five gaps

## Build brief

- [ ] `classify_selection_step` — **TODO(me)**
- [ ] `drop_low_variance` — **TODO(me)**: target-blind, `exclude` honoured
- [ ] `drop_correlated` — **TODO(me)**: records **what** each column correlated with
- [ ] `build_preprocessor` — **TODO(me)**: `remainder` explicit, `handle_unknown='ignore'`
- [ ] `build_pipeline` — **TODO(me)**: selection inside
- [ ] `assert_pipeline_is_leak_proof` — **TODO(me)**: catches pre-fitted steps
- [ ] `selection_leak_demo` — **TODO(me)**
- [ ] Can explain why `remainder` is required rather than defaulted

## Tests that must be able to fail

- [ ] `test_target_blind_methods_may_live_outside_the_fold` — three green cases
- [ ] `test_target_aware_methods_must_be_inside_the_pipeline` — three green cases
- [ ] `test_unknown_selection_method_raises` — green
- [ ] `test_constant_columns_are_dropped` / `test_excluded_columns_survive` — green
- [ ] `test_dropping_everything_raises` — green
- [ ] `test_near_duplicates_are_dropped_with_a_reason` — green
- [ ] `test_uncorrelated_columns_all_survive` — green
- [ ] `test_drop_correlated_reuses_the_shared_correlation` — green
- [ ] `test_remainder_must_be_stated_explicitly` — green
- [ ] `test_a_column_in_two_groups_is_refused` — green
- [ ] `test_all_empty_groups_are_refused` — green
- [ ] `test_the_encoder_handles_unknown_categories` — green
- [ ] `test_build_pipeline_rejects_a_non_model` — green
- [ ] `test_selection_goes_inside_the_pipeline` — green
- [ ] `test_selection_on_the_full_dataset_inflates_the_score` — green ← **today's real assessment**
- [ ] `test_selection_inside_the_pipeline_is_honest` — green
- [ ] **Moved the selection outside the pipeline, watched the honest test go red** ← do not skip
- [ ] `test_the_leak_and_the_fix_use_identical_data` — green
- [ ] `test_an_already_fitted_step_is_caught` — green
- [ ] **Fitted a scaler outside and dropped it in, watched the guard catch it** ← do not skip
- [ ] `test_a_clean_pipeline_passes` — green
- [ ] `test_a_bare_function_as_a_step_is_caught` — green
- [ ] `test_the_pipeline_refits_every_step_on_every_fold` — green (5 fits, all partial)
- [ ] `test_the_build_script_exists_and_runs` — green
- [ ] `test_the_manifest_records_every_step` — green
- [ ] `test_the_manifest_records_why_columns_were_dropped` — green
- [ ] `test_phase_10_features_module_is_complete` — green (36 functions)

## The gate artifact

- [ ] `scripts/build_features.py` written and exits 0
- [ ] Reads via `read_table` (Day 27) — typed at read time
- [ ] Runs `prediction_time_check` and **exits non-zero** if a flagged column survives
- [ ] **Splits first** (Day 79), strategy chosen by `choose_split`
- [ ] Target-blind cleaning outside; target-aware steps inside
- [ ] `remainder` stated explicitly
- [ ] `assert_pipeline_is_leak_proof` runs **before** fitting
- [ ] Fits on **train only**; transforms all three sets
- [ ] `assert_no_overlap` and `assert_no_target_leak` both run
- [ ] Manifest saved with steps, split sizes, dropped columns **with reasons**, timestamp
- [ ] Runs in under 60 seconds
- [ ] **No new feature code was needed inside the script**

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does selecting on the full dataset survive cross-validation?
- [ ] What single question decides where a preprocessing step belongs?
- [ ] Why can univariate selection not find an XOR relationship?
- [ ] What does `remainder='drop'` do that you must never let happen silently?
- [ ] What exactly does a Pipeline guarantee on each fold?
- [ ] Name three leaks a pipeline does **not** protect you from
- [ ] How does a pre-fitted step smuggle information in?
- [ ] Why must a dropped column carry a reason?

## PHASE 10 GATE

- [ ] `scripts/build_features.py` runs clean in one command
- [ ] Split happens before any fitted step
- [ ] Every supervised step is inside the pipeline
- [ ] Leak-proof assertion passes before fitting
- [ ] Manifest complete and auditable
- [ ] `test_phase_10_features_module_is_complete` green
- [ ] Every Day 76–82 fit/apply test still green
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 83` succeeded and `./m status` shows Phases 0–10 complete
