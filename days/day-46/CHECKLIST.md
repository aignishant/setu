# Day 46 — CHECKLIST

**IDs covered:** DB-06 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-46/lab/windows.py
uv run python -m pytest tests/test_db.py -v
```

Expected: the subquery → CTE → window walkthrough, then all db tests green (live ones skipped
unless `SETU_LIVE=1`).

## Setup

- [ ] `./m start 46` and `./m scaffold 46` run
- [ ] `days/day-46/lab/windows.py` created
- [ ] No new packages installed

## DB-06 — the collapse question

- [ ] Can state the one-sentence difference between `GROUP BY` and `OVER (PARTITION BY ...)`
- [ ] Confirmed a window function returns **one row per input row**, not one per group
- [ ] Connected it explicitly to Day 31's `agg` vs `transform` table
- [ ] Wrote each of the four §1 questions as a query: rank within venue, value minus group mean,
      running total, previous row's value

## Subqueries and CTEs

- [ ] Wrote a scalar subquery, an `IN` subquery and a correlated subquery
- [ ] Saw `NOT IN` with a NULL in the subquery return **nothing**, and can explain why
- [ ] Rewrote a nested subquery as a `WITH` chain and can say which you would rather inherit
- [ ] Know when a correlated subquery re-scans the table once per row

## Window functions

- [ ] Used `row_number`, `rank` and `dense_rank`; can state how each treats ties
- [ ] Confirmed `row_number` without a tiebreak is **non-deterministic**
- [ ] Used `lag`/`lead`
- [ ] Wrote an explicit `ROWS BETWEEN` frame
- [ ] Confirmed the **default frame includes the current row**
- [ ] Can state the safe form for a feature, from memory

## The leak

- [ ] Can name the two ways a window function sees the future (§1)
- [ ] Connected both to Day 33's `causal_rolling`
- [ ] Can explain why a partition-wide average computed over the whole table is leakage

## Build brief

- [ ] `rank_within` — **TODO(me)**: `tiebreak` is a **required** parameter, identifiers allowlisted
- [ ] `top_per_group` — **TODO(me)**: CTE + filter, not a correlated subquery
- [ ] `causal_window` — **TODO(me)**: frame ends at `1 PRECEDING`, explicit `ROWS BETWEEN`, no way to include the current row
- [ ] `assert_no_current_row_in_frame` — **TODO(me)**: flags a missing frame clause and unsafe endings, names the fragment
- [ ] Can defend making `tiebreak` required rather than optional

## Tests that must be able to fail

- [ ] `test_window_does_not_collapse_rows` — green
- [ ] `test_rank_variants_differ_on_ties` — green
- [ ] `test_row_number_needs_a_tiebreak_to_be_deterministic` — green
- [ ] `test_not_in_with_a_null_returns_nothing` — green
- [ ] `test_causal_frame_excludes_the_current_row` — green
- [ ] `test_default_frame_includes_the_current_row` — green
- [ ] `test_assert_no_current_row_flags_the_default_frame` — green
- [ ] **Wrote a window with `ORDER BY` and no `ROWS` clause, watched the guard catch it** ← do not skip
- [ ] `test_assert_no_current_row_flags_unsafe_frames` — every parametrised case green
- [ ] `test_assert_no_current_row_allows_a_safe_frame` — green
- [ ] `test_assert_no_current_row_allows_a_query_with_no_window` — green
- [ ] `test_rank_within_requires_a_tiebreak` — green
- [ ] `test_causal_window_has_no_include_current_option` — green
- [ ] **Added an `include_current=` parameter, watched the signature test go red, removed it** ← do not skip
- [ ] `test_top_per_group_is_deterministic` — green
- [ ] `test_causal_window_first_rows_are_null` — green (correct, not a gap to fill)
- [ ] `test_window_matches_pandas_cumcount` — green ← the SQL and pandas answers agree

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does a window function do that `GROUP BY` cannot?
- [ ] Which pandas operation is `OVER (PARTITION BY ...)` the twin of?
- [ ] Why does `NOT IN` with a NULL return no rows?
- [ ] How do `row_number`, `rank` and `dense_rank` differ on ties?
- [ ] What does the default window frame include, and why is that a problem for a feature?
- [ ] Write the leak-free frame clause from memory
- [ ] Why is `tiebreak` a required argument rather than an option?
- [ ] Why is a CTE preferable to a five-level nested subquery, given they compute the same thing?

## Commit

- [ ] `./m check && ./m done 46` succeeded
