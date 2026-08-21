# Day 61 — CHECKLIST

**IDs covered:** ST-05 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-61/lab/shape.py
uv run python -m pytest tests/test_stats.py -v
```

Expected: the eight-part report ending with the kurtosis/tails table, then all stats tests green.

## Setup

- [ ] `./m start 61` and `./m scaffold 61` run
- [ ] `days/day-61/lab/shape.py` created
- [ ] No new packages installed

## ST-05 — the moments

- [ ] Ran `same_centre_same_spread_different_shape()` and read the `|z|>4` column
- [ ] Computed skew and kurtosis **by hand** from standardised deviations
- [ ] Confirmed the first two moments are always 0 and 1
- [ ] Can say why the third moment is signed and the fourth is not
- [ ] Confirmed scipy and pandas skew **disagree**, and know why
- [ ] Know that scipy's kurtosis is **excess** by default, and what a normal scores

## Sign and thresholds

- [ ] Ran `what_the_sign_means()` and confirmed skew and mean−median agree in sign
- [ ] Can say why skew is comparable across variables and the raw gap is not
- [ ] Ran `rules_of_thumb_are_rough()` and **read the whole table**
- [ ] Recorded max |skew| from a symmetric population at n=20: ______
- [ ] Can say why "skew = 0.6, therefore skewed" is not a conclusion at small n

## The transform

- [ ] Ran `the_log_transform()`; recorded skew before ______ and after ______
- [ ] Can say why a lognormal becomes exactly normal
- [ ] Can name four real variables that are multiplicative
- [ ] Confirmed `np.log(0)` is `-inf` and `log1p(0)` is `0`
- [ ] Compared six transforms and their resulting skews
- [ ] Know when Box-Cox is unusable and what replaces it
- [ ] Can state the leakage rule for a fitted transform
- [ ] Read `when_not_to_transform()` and can name all three consequences

## Kurtosis

- [ ] Ran `kurtosis_is_about_tails()` and **read the table**
- [ ] Confirmed the uniform has a flat peak **and** negative excess kurtosis
- [ ] Can say which column kurtosis tracks, and which it does not
- [ ] Can state why "peakedness" is the wrong mental model

## Build brief

- [ ] `shape` — **TODO(me)**: `kurtosis_excess` key, labels, small-n warning, refuses below interval
- [ ] `suggest_transform` — **TODO(me)**: fits nothing, reason names the skew value
- [ ] `apply_transform` — **TODO(me)**: reuses `fitted` rather than refitting, does not mutate
- [ ] `skew_stability` — **TODO(me)**: vectorised simulation
- [ ] Can explain why the output key is named `kurtosis_excess`

## Tests that must be able to fail

- [ ] `test_symmetric_data_has_near_zero_skew` — green
- [ ] `test_right_skew_is_positive` / `test_left_skew_is_negative` — green
- [ ] `test_normal_has_near_zero_excess_kurtosis` — green
- [ ] **Switched to raw kurtosis, watched it go red at 3.0, reverted** ← do not skip
- [ ] `test_heavy_tails_have_positive_excess_kurtosis` — green
- [ ] `test_uniform_has_negative_excess_kurtosis` — green
- [ ] `test_small_samples_get_a_warning` / `test_large_samples_get_no_warning` — green
- [ ] `test_shape_is_refused_below_interval` — two green cases
- [ ] `test_shape_needs_three_values` — green
- [ ] `test_skew_is_unstable_at_small_n` — green
- [ ] `test_skew_stabilises_as_n_grows` — green
- [ ] `test_skew_stability_is_reproducible` — green
- [ ] `test_log_transform_reduces_right_skew` — green
- [ ] `test_suggest_recommends_none_when_symmetric` — green
- [ ] `test_suggest_recommends_log1p_for_positive_right_skew` — green
- [ ] `test_suggest_avoids_log_when_negatives_are_present` — green
- [ ] `test_suggest_does_not_recommend_log_for_left_skew` — green
- [ ] **Mapped "skewed → log" unconditionally, watched two tests go red, fixed it** ← do not skip
- [ ] `test_log1p_handles_zero` — green
- [ ] `test_log1p_rejects_negatives_and_counts_them` — green
- [ ] `test_transform_does_not_mutate_its_input` — green
- [ ] `test_fitted_params_are_reused_not_refitted` — green ← **today's real assessment**
- [ ] **Ignored the `fitted` argument and refitted, watched all three assertions go red, fixed it** ← do not skip
- [ ] `test_fitted_params_are_json_serialisable` — green
- [ ] `test_unknown_transform_raises` / `test_none_transform_is_the_identity` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What do the third and fourth moments measure, and why is only one signed?
- [ ] Why must a kurtosis value always come with its convention?
- [ ] Why is skewness comparable across variables when mean−median is not?
- [ ] Why are the |skew| thresholds unreliable at small n?
- [ ] Why `log1p` rather than `log`?
- [ ] Why does a log transform make left skew worse?
- [ ] What are the three consequences of transforming a target?
- [ ] Why is refitting a transform on the test set leakage?

## Commit

- [ ] `./m check && ./m done 61` succeeded
