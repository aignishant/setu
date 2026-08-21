# Day 7 — CHECKLIST

**IDs covered:** PY-06 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-07/lab/strings.py
uv run python -m pytest tests/test_textutils.py -q
```

Expected: the string report, then all tests green (Days 4, 5 and 7).

## Setup

- [ ] `./m start 7` and `./m scaffold 7` run
- [ ] `days/day-07/lab/strings.py` created
- [ ] No new packages installed

## PY-06 — methods

- [ ] Ran all five demo functions
- [ ] Used negative indexing and slicing; confirmed slices don't raise out of range
- [ ] Used `in` for substring testing rather than `.find(...) != -1`
- [ ] Confirmed `.find()` returns `-1` — and can explain why that is a *silent* bug source
- [ ] Confirmed `.strip()` leaves inner whitespace alone
- [ ] Confirmed `" ".join(text.split())` beats `.replace("  ", " ")` on three spaces
- [ ] Used `maxsplit` and `rsplit` at least once each
- [ ] Unpacked a split into named variables and know why a wrong count raising is good
- [ ] Used `.splitlines()` and know what `\r` does to a `.split("\n")`

## Formatting

- [ ] Used `:.2f`, `:.1%`, `:,` and the `>`/`<`/`^` alignment specs
- [ ] Used `!r` in a debug print
- [ ] Used a raw string for a Windows path
- [ ] Wrote a triple-quoted multi-line template and noted it is Day 153's prompt shape

## Build brief

- [ ] `truncate` — **TODO(me) implemented**, total length includes the suffix
- [ ] `slugify` — **TODO(me) implemented**, standard library only, no regex
- [ ] `split_sentences` — **TODO(me) implemented**, deliberately naive
- [ ] Wrote in your commit message **one concrete case `split_sentences` gets wrong**

## Tests that must be able to fail

- [ ] All were red before you implemented the TODOs
- [ ] `test_truncate_total_length_includes_suffix` — green
- [ ] `test_truncate_leaves_short_text_alone` — green
- [ ] `test_truncate_at_exact_limit_is_unchanged` — green ← the boundary case
- [ ] **Made `truncate` always truncate, watched the boundary test go red, fixed it** ← do not skip
- [ ] `test_truncate_rejects_impossible_limit` — green
- [ ] `test_slugify` — four green parametrised cases including `"C++ & Rust"` and `"2017"`
- [ ] `test_split_sentences_strips_and_drops_empties` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why does no string method modify the string it was called on?
- [ ] Why is `" ".join(text.split())` better than chained `.replace()` calls?
- [ ] Why is an unchecked `.find()` result dangerous specifically?
- [ ] What does `.splitlines()` handle that `.split("\n")` does not?
- [ ] When would you reach for `rsplit` over `split`?
- [ ] Name three later days that are `split` → transform → `join` in disguise
- [ ] What does your naive `split_sentences` get wrong, and what will replace it?

## Commit

- [ ] `./m check && ./m done 7` succeeded
