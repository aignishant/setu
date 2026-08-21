# Day 6 — CHECKLIST

**IDs covered:** PY-05 · **Principles served:** 1, 3, 5, 7

## Demo command

```bash
uv run python days/day-06/lab/loops.py
uv run python -m pytest tests/test_retry.py -v
```

Expected: the loop report, then **five green tests in well under a second**.

## Setup

- [ ] `./m start 6` and `./m scaffold 6` run
- [ ] Files created: `days/day-06/lab/loops.py`, `src/setu/retry.py`, `tests/test_retry.py`
- [ ] No new packages installed

## PY-05 — loop mechanics

- [ ] Confirmed `range` is lazy — `type(r).__name__` is `range`, not `list`
- [ ] Confirmed `range` supports `len()` and indexing without materialising
- [ ] Understood start / stop (exclusive) / step, including a negative step
- [ ] Used `enumerate(..., start=1)` rather than `range(len(...))`
- [ ] Used `zip(..., strict=True)` and know what silently happens without `strict`
- [ ] Ran `break_and_continue()` and can state the difference in one sentence each
- [ ] Ran `for_else()` and can say when the `else` block executes

## The capped retry

- [ ] Redrew the retry flowchart from §1 **from memory**
- [ ] `src/setu/retry.py` created with `RetriesExhausted` and `backoff_delay`
- [ ] Understood why `random.uniform` jitter is not optional
- [ ] Understood why `*` makes `attempts` and `sleep` keyword-only
- [ ] Understood why `sleep` is an injected parameter rather than a direct `time.sleep` call
- [ ] `with_retry` — **TODO(me) implemented**

## Tests that must be able to fail

- [ ] All five were red before you implemented `with_retry`
- [ ] `test_returns_immediately_on_success` — green, and `fn` was called exactly once
- [ ] `test_succeeds_on_the_third_attempt` — green, with exactly **two** sleeps
- [ ] `test_cap_is_hard` — green ← **the most important test in the file**
- [ ] **Made the cap off by one (`attempts + 1`), watched it go red, fixed it** ← do not skip
- [ ] `test_original_error_is_chained` — green (uses `raise ... from exc`)
- [ ] `test_backoff_is_bounded_and_non_negative` — six green parametrised cases
- [ ] The whole file runs in **under a second** — no real sleeping

## Budget

- [ ] LLM calls today: **0**
- [ ] Real seconds slept during tests: **0**

## Understanding check — answer out loud

- [ ] When do you choose `while` over `for`, and what obligation does that choice create?
- [ ] What specifically happens to a $0 project when a retry loop is uncapped?
- [ ] Why is jitter necessary, and what goes wrong without it?
- [ ] Why should there be no sleep after the final failed attempt?
- [ ] What does `zip` do without `strict=True`, and which later day does that bite?
- [ ] What does `raise X from exc` preserve that a bare `raise X` loses?
- [ ] Name two later days that reuse today's loop shape, and what changes in each

## Commit

- [ ] `./m check && ./m done 6` succeeded
