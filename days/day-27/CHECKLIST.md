# Day 27 — CHECKLIST

**IDs covered:** PD-02 · **Principles served:** 1, 7, 9

## Demo command

```bash
uv run python days/day-27/lab/reading.py
uv run python -m pytest tests/test_io.py -v
```

Expected: the six-part reading report including a measured CSV-vs-Parquet table, then all tests green.

## Setup

- [ ] `./m start 27` and `./m scaffold 27` run
- [ ] `pyarrow` present in `pyproject.toml` (came in on Day 26)
- [ ] `days/day-27/lab/reading.py` created

## PD-02 — inference vs declaration

- [ ] Ran `inference_guesses_wrong()` and **saw `0012` become `12`**
- [ ] Saw one `"N/A"` turn a numeric column into text
- [ ] Saw a date column stay a string
- [ ] Fixed all three with `dtype=`, `parse_dates=`, `na_values=`
- [ ] Confirmed `.dt.year` works only after `parse_dates`
- [ ] Can explain why an integer column with a missing value becomes `float64`
- [ ] Used nullable `Int64` and can state how it differs from `int64`
- [ ] Used `usecols=` and can say what it saves on a wide export
- [ ] Used `chunksize=` and confirmed it returns an **iterator**

## Formats

- [ ] Ran `formats_compared()`; recorded **your** numbers:
  - csv: write ______s · read ______s · ______ MiB
  - parquet: write ______s · read ______s · ______ MiB
- [ ] Confirmed `back_parquet.dtypes.equals(original.dtypes)` is **True**
- [ ] Can state why CSV cannot do that
- [ ] Saw `to_csv` without `index=False` produce a stray index column

## Build brief

- [ ] `read_table` — **TODO(me)**: dispatch by suffix, apply the spec, UTF-8, validates parquet dtypes
- [ ] `write_table` — **TODO(me)**: `index=False`, creates parents, **atomic** (reuses Day 16)
- [ ] `read_in_chunks` — **TODO(me)**: lazy, covers every row
- [ ] `check_schema` — **TODO(me)**: reports **every** problem at once
- [ ] `infer_spec` — **TODO(me)**: captures a validated schema for reuse
- [ ] Can explain how `infer_spec` + `check_schema` implement Principle 9

## Tests that must be able to fail

- [ ] `test_read_preserves_leading_zeros` — green ← **today's real assessment**
- [ ] **Dropped the `spec` → `dtype=` pass-through, watched it go red, fixed it** ← do not skip
- [ ] `test_read_without_a_spec_still_works` — green
- [ ] `test_csv_round_trip_has_no_unnamed_column` — green
- [ ] **Removed `index=False`, watched `Unnamed: 0` appear, restored it** ← do not skip
- [ ] `test_parquet_round_trips_dtypes_exactly` — green, including nullable `Int64`
- [ ] `test_write_is_atomic` — green (all three assertions)
- [ ] `test_unsupported_suffix_is_rejected` — green
- [ ] `test_chunked_reading_is_lazy` — green
- [ ] `test_chunks_cover_every_row` — green (ragged final chunk, fourth time)
- [ ] `test_check_schema_reports_every_problem_at_once` — green
- [ ] **Made it raise on the first problem, watched it go red, fixed it** ← do not skip
- [ ] `test_check_schema_passes_a_correct_frame` — green
- [ ] `test_infer_then_check_is_a_fixed_point` — green

## Provenance (Principle 9)

- [ ] Any dataset you downloaded today has a row in `data/raw/SOURCE.md`
- [ ] That row names the URL, the licence, and the date pulled

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Describe the leading-zeros bug and why it surfaces far from its cause
- [ ] Name the three predictable ways inference guesses wrong
- [ ] Why can `int64` not hold a missing value, and what are your two options?
- [ ] What is the difference between `Int64` and `int64`?
- [ ] Why does Parquet not need a `dtype=` argument?
- [ ] What happens if you round-trip a CSV three times without `index=False`?
- [ ] How do `infer_spec` and `check_schema` work together as a workflow?

## Commit

- [ ] `./m check && ./m done 27` succeeded
