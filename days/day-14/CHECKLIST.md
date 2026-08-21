# Day 14 — CHECKLIST

**IDs covered:** PY-16 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-14/lab/decorators.py
uv run python -m pytest tests/test_decorators.py -v
```

Expected: the seven-part decorator report, then **eleven green tests**.

## Setup

- [ ] `./m start 14` and `./m scaffold 14` run
- [ ] Files created: `days/day-14/lab/decorators.py`, `src/setu/decorators.py`, `tests/test_decorators.py`
- [ ] No new packages installed

## PY-16 — the mechanism

- [ ] Wrote the **desugared** version (`greet = shout(greet)`) before using `@`
- [ ] Can state the one-line definition of a decorator without hesitating
- [ ] Confirmed `*args, **kwargs` is why a wrapper can wrap anything
- [ ] Saw `__name__` become `'wrapper'` without `functools.wraps`
- [ ] Saw `__name__` and `__doc__` preserved with it
- [ ] Found the original via `__wrapped__`
- [ ] Built a decorator **with arguments** and can explain why it needs three layers
- [ ] Stacked two decorators and confirmed the bottom one is applied first
- [ ] Stored state on the wrapper object rather than in a global
- [ ] Saw `try/finally` keep the timing when the wrapped call raised

## Build brief

- [ ] `timed` — **TODO(me)**: `functools.wraps`, `perf_counter`, `try/finally`, logs at DEBUG, re-raises
- [ ] `retry` — **TODO(me)**: three layers, explicit `exceptions` tuple, hard cap, no trailing sleep, chains the cause
- [ ] `memoize` — **TODO(me)**: caches by arguments, exposes `cache_clear()` and `cache_info()`
- [ ] Read `functools.lru_cache` **after** writing `memoize`, and noted the differences in your commit message
- [ ] Used `logging`, never `print`, inside `src/setu/`

## Tests that must be able to fail

- [ ] All eleven were red before you implemented the TODOs
- [ ] `test_timed_preserves_identity` — green
- [ ] **Removed `@functools.wraps`, watched it go red, restored it** ← do not skip
- [ ] `test_timed_returns_the_value` — green
- [ ] `test_timed_logs_even_when_the_call_raises` — green
- [ ] **Replaced `try/finally` with a plain call, watched it go red, restored it** ← do not skip
- [ ] `test_retry_succeeds_on_third_attempt` — green
- [ ] `test_retry_cap_is_hard` — green
- [ ] `test_retry_does_not_swallow_unlisted_exceptions` — green ← **today's most important test**
- [ ] **Widened the filter to `except Exception`, watched it go red, narrowed it back** ← do not skip
- [ ] `test_retry_sleeps_between_but_not_after` — green (exactly two delays for three attempts)
- [ ] `test_retry_preserves_identity` — green
- [ ] `test_memoize_calls_the_function_once_per_distinct_argument` — green
- [ ] `test_memoize_cache_clear` — green
- [ ] `test_memoize_rejects_unhashable_arguments` — green

## Budget

- [ ] LLM calls today: **0**
- [ ] Real seconds slept in tests: **0**

## Understanding check — answer out loud

- [ ] Write `@d` as a plain assignment
- [ ] What exactly does `functools.wraps` copy, and what breaks without it?
- [ ] Why does a decorator with arguments need three nested functions?
- [ ] In a stack of two decorators, which runs first and which is outermost?
- [ ] Why must a timing decorator use `finally`?
- [ ] Why is retrying a `TypeError` actively harmful on a free tier?
- [ ] Why must `memoize` raise on unhashable arguments instead of skipping the cache?

## Commit

- [ ] `./m check && ./m done 14` succeeded
