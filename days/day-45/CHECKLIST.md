# Day 45 — CHECKLIST

**IDs covered:** DB-05 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-45/lab/joins.py
uv run python -m pytest tests/test_db.py -v
SETU_LIVE=1 uv run python -m pytest tests/test_db.py -m live -v
```

Expected: the nine-part join report ending with a passing SQL-vs-pandas assertion, then all tests green.

## Setup

- [ ] `./m start 45` and `./m scaffold 45` run
- [ ] `sql/004_seed_authors.sql` written and applied
- [ ] No new packages installed

## DB-05 — the four joins

- [ ] Ran `the_four_joins()`; recorded INNER ____ LEFT ____ RIGHT ____ FULL ____
- [ ] Can explain each difference from the data
- [ ] Computed `LEFT − INNER` and can say what that number diagnoses
- [ ] Used the **anti-join** idiom and can write it from memory
- [ ] Can say why `RIGHT JOIN` is legal but discouraged

## The two silent failures

- [ ] Ran `the_silent_loss()` and named the paper that would have vanished
- [ ] Ran `the_where_that_undoes_a_left_join()` and saw the two counts differ
- [ ] Can explain **why** a right-table `WHERE` condition drops the NULL rows
- [ ] Ran `the_fan_out()`; recorded the inflated sum ______ vs the true sum ______
- [ ] Can say why fan-out is more dangerous than loss
- [ ] Ran `two_fixes_for_the_fan_out()`; both matched the true total
- [ ] Can say why `EXISTS` is the better habit for a filter

## Details that decide answers

- [ ] Ran `aggregate_across_the_join()`
- [ ] Confirmed `count(child.col)` gives 0 and `count(*)` gives 1 for a childless parent
- [ ] Wrote a self-join with aliases and a strict inequality
- [ ] Compared `UNION` and `UNION ALL`; can say which to default to and why
- [ ] Ran `sql_and_pandas_agree()`; the frame assertion passed
- [ ] Used `validate="one_to_many"` in the pandas merge

## Build brief

- [ ] `join_report` — **TODO(me)**: full accounting, **one** round trip
- [ ] `safe_join_query` — **TODO(me)**: names expected, actual, difference, and the remedy
- [ ] `anti_join` — **TODO(me)**: `NOT EXISTS`, bounded
- [ ] `aggregate_without_fan_out` — **TODO(me)**: `EXISTS` not `JOIN`, allowlisted aggregate
- [ ] Can explain why `join_report` must be one query on a paused free tier

## Tests that must be able to fail

- [ ] `test_inner_join_silently_drops_unmatched_rows` — green
- [ ] `test_left_join_keeps_them` — green
- [ ] `test_a_where_condition_undoes_a_left_join` — green ← **today's real assessment**
- [ ] **Moved the condition from `ON` into `WHERE`, watched the counts converge, moved it back** ← do not skip
- [ ] `test_fan_out_inflates_an_aggregate` — green
- [ ] `test_exists_does_not_fan_out` — green
- [ ] `test_count_column_versus_count_star_after_a_left_join` — green
- [ ] **Used `count(*)`, watched the childless paper report 1 instead of 0, fixed it** ← do not skip
- [ ] `test_union_deduplicates_and_union_all_does_not` — green
- [ ] `test_safe_join_query_rejects_a_surprising_count` — green
- [ ] `test_safe_join_query_allows_a_tolerance` — green
- [ ] `test_aggregate_rejects_an_unknown_function` — green
- [ ] `test_no_join_to_a_child_inside_an_aggregate_in_src` — green
- [ ] Live: `test_join_report_detects_loss_and_fan_out` — green
- [ ] Live: `test_join_report_is_one_round_trip` — green
- [ ] **Wrote `join_report` as five separate queries, watched it go red, merged them into one** ← do not skip
- [ ] Live: `test_anti_join_finds_the_unmatched_rows` — green
- [ ] Live: `test_aggregate_without_fan_out_matches_the_unjoined_total` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Name the two silent join failures and which is more dangerous
- [ ] What does `LEFT − INNER` tell you?
- [ ] Write the anti-join idiom from memory
- [ ] Why does a right-table condition in `WHERE` undo a `LEFT JOIN`?
- [ ] Why is `sum()` after a one-to-many join wrong, and give two fixes
- [ ] After a `LEFT JOIN`, why do `count(*)` and `count(child.col)` differ?
- [ ] When do you use `UNION` rather than `UNION ALL`?
- [ ] What does `validate="one_to_many"` protect you from in pandas?

## Commit

- [ ] `./m check && ./m done 45` succeeded
