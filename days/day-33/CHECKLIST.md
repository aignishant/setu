# Day 33 — CHECKLIST

**IDs covered:** PD-11, PD-12 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-33/lab/accessors.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the eleven-part accessor report including two measured ratios, then all frame tests green.

## Setup

- [ ] `./m start 33` and `./m scaffold 33` run
- [ ] `days/day-33/lab/accessors.py` created
- [ ] No new packages installed

## PD-11 — the `.str` accessor

- [ ] Saw `Series.lower()` raise, and can say why the namespace exists
- [ ] Confirmed `.str.len()` gives `<NA>` for a missing value, not `0`
- [ ] Saw `.str.contains()` **without** `na=` produce `<NA>` in the mask
- [ ] Confirmed that mask then raises when used for indexing
- [ ] Used `split(expand=True)` to get columns, and `.str[0]` to index elements
- [ ] Used `str.extract` with **named** groups; noted it returns strings
- [ ] Passed `regex=` explicitly on a `replace`
- [ ] Ran `why_it_is_fast_now()`; recorded the ratio: ______× and the memory difference
- [ ] Ran `the_apply_temptation()`; recorded the ratio: ______×
- [ ] Can state the rule: if an accessor method exists, use it

## PD-12 — the `.dt` accessor and time

- [ ] Confirmed **microsecond** resolution (pandas 3.0) and parsed `1500-01-01`
- [ ] Saw `dayfirst=` change the interpretation of `12/06/2017`
- [ ] Used `errors="coerce"` and **counted** the resulting `NaT` values
- [ ] Used `.dt.year`, `.dt.quarter`, `.dt.day_name`, `.dt.to_period('M')`
- [ ] Can say what a `Period` is that a timestamp is not
- [ ] Compared `pd.Timedelta(days=30)` with `pd.DateOffset(months=1)`
- [ ] Localised and converted a timezone; saw naive-vs-aware comparison raise
- [ ] Resampled with `ME` and `W`, and checked the **current** frequency aliases in the docs
- [ ] Saw upsampling create gaps; used `ffill` and understood why `bfill` is forbidden

## The leak

- [ ] Ran `rolling_and_the_leak()` and **read all three printed rows**
- [ ] Can say exactly which rows `center=True` uses at index 1
- [ ] Can state the safe shape in one line
- [ ] Connected it to Day 97's `TimeSeriesSplit`

## Build brief

- [ ] `extract_pattern` — **TODO(me)**: named groups required, collision check, dtype cast, no-match raise
- [ ] `parse_dates_strictly` — **TODO(me)**: `max_coercion=0.0` default, names bad values
- [ ] `add_time_parts` — **TODO(me)**: refuses a non-datetime column
- [ ] `causal_rolling` — **TODO(me)**: trailing + `shift(1)`, group-aware, **no `center=` parameter**
- [ ] Can defend the decision to omit `center=` entirely

## Tests that must be able to fail

- [ ] `test_extract_adds_named_groups` — green
- [ ] `test_extract_rejects_unnamed_groups` / `test_extract_rejects_a_column_collision` — green
- [ ] `test_extract_does_not_mutate` — green
- [ ] `test_extract_raises_when_nothing_matches` — green
- [ ] `test_parse_dates_refuses_silent_coercion` — green
- [ ] **Removed the bad value from the message, watched it go red, restored it** ← do not skip
- [ ] `test_parse_dates_allows_an_explicit_tolerance` — green
- [ ] `test_parse_dates_clean_input_passes` — green
- [ ] `test_time_parts_added` — green
- [ ] `test_time_parts_refuses_a_non_datetime_column` — green
- [ ] `test_time_parts_rejects_an_unknown_part` — green
- [ ] `test_causal_rolling_never_sees_the_current_row` — green ← **today's real assessment**
- [ ] **Removed the `.shift(1)`, saw row 2 become 2.5 instead of 1.5, restored it** ← do not skip
- [ ] `test_causal_rolling_matches_a_hand_computed_window` — green
- [ ] `test_causal_rolling_does_not_bleed_across_groups` — green
- [ ] **Applied `rolling` before the `groupby`, watched group b use group a's data, fixed it** ← do not skip
- [ ] `test_causal_rolling_has_no_center_parameter` — green
- [ ] `test_causal_rolling_rejects_a_bad_window` — green
- [ ] `test_no_bfill_on_time_columns_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why do `.str` and `.dt` live behind accessors instead of on the Series directly?
- [ ] What does `.str.contains()` return for a missing value, and what breaks next?
- [ ] Why is `.str` faster in pandas 3.0 than it was in 2.x?
- [ ] Why must you count coercions when parsing dates?
- [ ] What is the difference between `Timedelta` and `DateOffset`?
- [ ] Why is `bfill` on a time series leakage rather than a convenience?
- [ ] Explain the `center=True` leak using the three printed rows
- [ ] Why is omitting `center=` from the signature better than documenting that it is unsafe?

## Commit

- [ ] `./m check && ./m done 33` succeeded
