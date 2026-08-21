# Day 26 — CHECKLIST

**IDs covered:** PD-01 · **Principles served:** 2, 4, 7, 13

## Demo command

```bash
uv run python days/day-26/lab/cow_demo.py
uv run python -m pytest tests/test_frames.py -v
```

Expected: the chained-assignment block shows **all scores still 1.0**, the `.loc` block shows 100.0,
then seven green tests.

## Setup

- [ ] `./m start 26` and `./m scaffold 26` run
- [ ] `uv add "pandas==<your pinned 3.x>" "pyarrow"` — appears in `pyproject.toml` and `uv.lock`
- [ ] Version pinned from **your** Day-1 verify run; any difference from `3.0.5` logged in `docs/CHANGELOG_PLAN_DS.md`
- [ ] `pd.__version__` confirmed to start with `3.`
- [ ] Read and understood why `pyarrow` is the one unpinned package in this plan

## Copy-on-Write

- [ ] Ran `chained_assignment_does_nothing()` and saw **all four scores still 1.0**
- [ ] Confirmed **no warning and no exception** was printed
- [ ] Ran `loc_assignment_works()` and saw row `b` and row `d` become 100.0
- [ ] Ran `a_slice_is_now_yours_alone()` and saw the parent untouched
- [ ] Can describe the "two bracket pairs then `=`" shape without looking
- [ ] Wrote the house rule somewhere you will see it: **assignment goes through `.loc`**

## The `str` dtype

- [ ] `df.dtypes` shows `str` for `paper`, not `object`
- [ ] The legacy `df.dtypes == "object"` check returned an **empty** list
- [ ] `select_dtypes(include="str")` returned `["paper"]`
- [ ] Set a `None` into a `str` column via `.loc` and counted it with `.isna().sum()`
- [ ] Can name two concrete benefits of the Arrow-backed string dtype

## The other 3.0 changes

- [ ] Parsed `1500-01-01` successfully and saw microsecond resolution in the dtype
- [ ] Understood that `inplace=True` chaining is possible but is **not** this project's style
- [ ] Know that `copy=` keywords are now inert and should be deleted, not reasoned about

## Build brief

- [ ] `src/setu/frames.py` created
- [ ] `text_columns` read and understood
- [ ] `set_where` — **TODO(me) implemented**: uses `.loc`, mutates in place, raises `KeyError` on a bad column
- [ ] `normalise_text_columns` — **TODO(me) implemented**: returns a new frame, reuses `setu.textutils.normalise_whitespace` rather than reimplementing it
- [ ] Each function's docstring states clearly whether it mutates or returns new

## Tests that must be able to fail

- [ ] All seven tests were red before the TODOs were implemented
- [ ] `test_text_columns_finds_str_dtype` — green
- [ ] `test_legacy_object_check_would_have_failed` — green (understood *why* this test exists)
- [ ] `test_set_where_actually_changes_the_frame` — green, including the row-0-untouched assertion
- [ ] `test_set_where_rejects_a_missing_column` — green
- [ ] `test_normalise_text_does_not_mutate_the_caller` — green
- [ ] `test_normalise_text_collapses_whitespace` — green
- [ ] `test_no_chained_assignment_anywhere_in_src` — green
- [ ] **Pasted a chained assignment into a file under `src/setu/`, watched the guard go red, removed it** ← do not skip

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What exactly happens, step by step, when you run `df["a"][mask] = 1` under Copy-on-Write?
- [ ] Why is a silent no-op worse than an exception?
- [ ] Why did `SettingWithCopyWarning` exist, and why is its removal an improvement rather than a loss?
- [ ] What replaced `df.dtypes == "object"`, and why did the old idiom stop working?
- [ ] Name two ways the Arrow-backed string dtype pays off later in this plan
- [ ] Why is `set_where` allowed to mutate while `normalise_text_columns` is not?
- [ ] How does today's mutation test relate to Day 4's `test_dedupe_does_not_mutate_its_input`?

## Freshness (Principle 13)

- [ ] Checked <https://pandas.pydata.org/docs/whatsnew/> for anything newer than your pinned version
- [ ] Any contradiction with this lesson recorded as an addendum, not patched silently

## Commit

```bash
./m check
./m done 26
```

- [ ] `./m done 26` succeeded
