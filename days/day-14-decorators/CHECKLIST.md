# Day 14 — CHECKLIST

**IDs covered:** `PY-16` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 11, 12, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 15, in [`parts/`](parts/)

> `./m done 14` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_decorators.py -v && ./m check
```

Expected: eleven tests plus the two parametrised documentation rows passing, then a green gate.

---

## Setup

- [ ] Created `src/setu/decorators.py` and `tests/test_decorators.py`
- [ ] Ran `uv run python -c "from setu.loaders import LOADERS; print(sorted(LOADERS))"` **before** writing anything
- [ ] Ran the six-fact setup block in the hub's §3 and can say what each of the six lines proved
- [ ] Read `uv run ruff rule B023` and `uv run ruff rule B008` from the installed linter
- [ ] Confirmed no new package was added today — Module 2 is still the language

---

## Section 1 — functions as values

- [ ] Read [1.1 — a function is a value](parts/01-functions-as-values/1.1-a-function-is-a-value.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — a function that returns a function](parts/01-functions-as-values/1.2-a-function-that-returns-a-function.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — the wrapper written by hand](parts/01-functions-as-values/1.3-the-wrapper-written-by-hand.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — the `@` sign is two lines](parts/01-functions-as-values/1.4-the-at-sign-is-two-lines.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Put three functions in a list and called each one in a loop, with no brackets anywhere in the list
- [ ] Confirmed `desk is collect` is `True` after `desk = collect`
- [ ] Ran `del collect` and confirmed `desk` still works and still reports `__name__` as `collect`
- [ ] Triggered `TypeError: 'str' object is not callable` by putting `collect('folder')` in the list
- [ ] Built two functions from one factory and printed `__closure__[0].cell_contents` for each
- [ ] Built three functions in a `for` loop with a `lambda` and watched all three report the last value
- [ ] Wrote a wrapper by hand, with no `@`, and rebound the name with `collect = signed_in(collect)`
- [ ] Deleted `return wrapper` and read `TypeError: 'NoneType' object is not callable`
- [ ] Confirmed by hand and by `@` give byte-for-byte identical output
- [ ] Put a `print` in a decorator's body and watched it fire **at import**, before `module loaded`

---

## Section 2 — writing a decorator

- [ ] Read [2.1 — `*args` and `**kwargs`](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `functools.wraps`](parts/02-writing-a-decorator/2.2-functools-wraps.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — returning the value](parts/02-writing-a-decorator/2.3-returning-the-value.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — `@timed`](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — stacking and the order](parts/02-writing-a-decorator/2.5-stacking-and-the-order.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrapped a zero-argument, a one-argument and a keyword-only function with **one** decorator
- [ ] Triggered `got an unexpected keyword argument` by leaving `**kwargs` off the wrapper
- [ ] Triggered `takes 1 positional argument but 2 were given` by writing `job(args, kwargs)` without the stars
- [ ] Watched a wrapper that names `count` override the wrapped function's own default — **no error**
- [ ] Registered two functions in a dict keyed on `__name__` with no `wraps` and counted **one** entry
- [ ] Ran `help()` on a decorated function and got `wrapper(*a, **k)`
- [ ] Compared `inspect.signature` with and without `wraps`
- [ ] Reached the original through `__wrapped__` and called it
- [ ] Deleted `return` from a wrapper and watched `.upper()` fail three lines away
- [ ] Wrote `return print(...)` in a wrapper and confirmed it still returns `None`
- [ ] Timed the same fast function with `time.time()` and `perf_counter()` and read both resolutions
- [ ] Put `@timed` on a function that raises and confirmed the timing line **still printed**
- [ ] Put `@timed` on a generator function and read the `0.0000s` before the generator was drained
- [ ] Ran `@timed` over `@retry` and `@retry` over `@timed` and read the two different logs
- [ ] Put a cache above and below a timer and watched one arrangement hide the second call entirely

---

## Section 3 — decorators with arguments

- [ ] Read [3.1 — `@retry(3)`](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — backoff, jitter, which errors](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — the retry that made it worse](parts/03-decorators-with-arguments/3.3-the-retry-that-made-it-worse.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Named the three layers out loud and said what each one captures
- [ ] Wrote `@retry` with no brackets and printed the function object that came back
- [ ] Then called `.upper()` on it and read `'function' object has no attribute 'upper'`
- [ ] Removed the last-attempt `raise` and watched three failures return `None`
- [ ] Used `@retry(0)` and confirmed the function was **never called**
- [ ] Printed a fixed schedule, a doubling schedule and a jittered schedule side by side
- [ ] Ran the same seed twice and got identical waits, then a different seed and got different ones
- [ ] Added up the total wait for five attempts and compared it to a realistic caller's budget
- [ ] Ran `catching=Exception` and `catching=TimeoutError` against a `KeyError` and counted the calls
- [ ] Timed a retry with a real `time.sleep` against one with an injected `sleep`
- [ ] Appended to a list inside a retried function and counted **three** entries for one call
- [ ] Rewrote it with a `visit_id` and confirmed the count is **one**
- [ ] Wrote down which of Day 13's loader methods `@retry` is safe on, and why

---

## Section 4 — the toolkit

- [ ] Read [4.1 — a decorator on a method](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — `functools.cache` and its trap](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — when a decorator is wrong](parts/04-the-toolkit/4.3-when-a-decorator-is-wrong.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `args[0]` inside a wrapper on a method and confirmed it is the instance
- [ ] Confirmed `Desk.collect is Desk.collect` is `True` — **one** wrapper for the whole class
- [ ] Watched a counter in a decorator count 1, 2, 3 across **two different instances**
- [ ] Put `@classmethod` under a plain decorator and read `'classmethod' object is not callable`
- [ ] Cached a method by argument only and watched one instance receive another instance's answer
- [ ] Passed a list to a `@cache`d function and read `TypeError: unhashable type: 'list'`
- [ ] Appended to a cached list and confirmed the next caller sees the change, with `is` proving why
- [ ] Deleted the only reference to an instance used with a cached method and confirmed it stayed alive
- [ ] Changed a source-of-truth dict after caching and watched `cache_info()` report a healthy hit
- [ ] Stacked three empty decorators and counted the frames in the traceback
- [ ] Wrote a decorator that edits an argument and broke it with a keyword call

---

## Build

- [ ] `src/setu/decorators.py` exists with `timed` and `retry` and **nothing else**
- [ ] `timed` uses `functools.wraps`, `*args, **kwargs`, `perf_counter` and `try` / `finally`
- [ ] `retry` validates `attempts` **in the factory**
- [ ] `retry` builds its `random.Random(seed)` **inside the wrapper**
- [ ] `retry`'s `catching` has **no default**
- [ ] `retry` takes `sleep` as a parameter, defaulting to `time.sleep`
- [ ] `retry` re-raises on the final attempt **before** computing a wait
- [ ] `retry`'s docstring names the precondition: only on calls that are safe to repeat
- [ ] Decorated `TextLoader.load` with `timed` from outside, without editing `src/setu/loaders/`
- [ ] Said in a comment how many wrapper objects that created for a thousand instances
- [ ] Reproduced all six traps in `notebooks/day-14-scratch.ipynb`
- [ ] Confirmed the notebook is **not** committed (Principle 6)

---

## Tests

- [ ] `tests/test_decorators.py` exists and every test failed before any implementation
- [ ] `test_timed_returns_the_functions_value` asserts the **value**, not truthiness
- [ ] `test_timed_lets_the_exception_through` passes
- [ ] `test_timed_keeps_the_name_and_the_signature` asserts `__name__`, `__doc__` **and** the signature
- [ ] `test_retry_stops_at_the_cap` asserts **both** that it raises and that the count is exactly 3
- [ ] `test_retry_returns_as_soon_as_it_works` asserts a count of 1
- [ ] `test_retry_does_not_catch_what_it_was_not_told_to` asserts a count of 1
- [ ] `test_retry_waits_longer_each_time` asserts the shape, not the values
- [ ] `test_retry_is_reproducible_from_its_seed` passes twice in a row
- [ ] `test_retry_does_not_sleep_after_the_last_attempt` asserts `len(waits) == attempts - 1`
- [ ] `test_retry_refuses_a_nonsense_attempt_count` has no `def` and no `@` in it
- [ ] The whole suite runs with **no real sleeping**
- [ ] **Break it, watch it go red, fix it** — drop `return` in `timed` → only the value test goes red
- [ ] **Break it, watch it go red, fix it** — `except Exception: pass` instead of `finally` → only the exception test goes red
- [ ] **Break it, watch it go red, fix it** — remove `functools.wraps` → the name test goes red
- [ ] **Break it, watch it go red, fix it** — copy `__name__` across by hand → the **signature** assertion is still red
- [ ] **Break it, watch it go red, fix it** — drop the last-attempt `raise` → `pytest.raises` red, the count green
- [ ] **Break it, watch it go red, fix it** — move `Random(seed)` into the factory → only the reproducibility test goes red
- [ ] **Break it, watch it go red, fix it** — compute the wait before the final `raise` → the sleep-count test goes red
- [ ] **Break it and watch every test stay GREEN** — widen `catching` to `Exception` and delete its test.
      Everything passes. Restore the test, watch it go red, and say what it was protecting.

---

## Budget

- [ ] **0** LLM calls made today
- [ ] **0** network requests made today
- [ ] **0** seconds of real sleeping in the test suite
- [ ] $0 spent (Principle 5)

---

## Commit

- [ ] `uv run ruff format days/day-14-decorators/ src/ tests/`
- [ ] `./m check` green
- [ ] `./m depth 14` reports no failures
- [ ] `./m done 14`
