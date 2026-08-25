# Day 6 — CHECKLIST

**IDs covered:** `PY-05` · **Principles served:** 1, 2, 3, 5, 6, 7, 11, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 6` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_retry.py -v && ./m check
```

Expected: eleven passing tests (two of them parametrised), all finishing in milliseconds because the
sleep is injected — and a green gate.

---

## Section 1 — how iteration actually works

- [ ] Read [1.1 — what a `for` loop actually does](parts/01-iteration/1.1-what-a-for-loop-actually-does.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — `range` is lazy](parts/01-iteration/1.2-range-is-lazy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — `enumerate`, `zip`, and the silent truncation](parts/01-iteration/1.3-enumerate-and-zip.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — `while`, and the loop with no promise](parts/01-iteration/1.4-while-and-the-loop-with-no-promise.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote the desugared loop — `iter`, `next`, `except StopIteration` — and got identical output
- [ ] Confirmed `iter(items) is iter(items)` is `False` for a list and `iter(g) is g` is `True` for a generator
- [ ] **Looped a generator twice and got an empty second pass**, with no error
- [ ] Compared `readlines()` against iterating the handle, and can say which one holds the file
- [ ] Triggered `TypeError: 'NoneType' object is not iterable` and found the bug on the line *above*
- [ ] Got a `NameError` from reading a loop variable after an empty loop
- [ ] Printed `sys.getsizeof(range(n))` at three sizes and saw one number
- [ ] Confirmed `999_999 in range(1_000_000)` is instant, and that the same on a list is not
- [ ] Wrote `range(5, 0, -1)`, noticed `0` was missing, and fixed it to `range(5, -1, -1)`
- [ ] Reproduced the `range(1, len(rows) - 1)` bug and can say why the `- 1` was wrong
- [ ] Built contiguous chunks with `range(0, n, size)` and confirmed no overlap and no gap
- [ ] Found the one legitimate `range(len(x))` in the three examples, and the cleaner form for the other two
- [ ] **Watched `zip` drop rows silently**, then made it raise with `strict=True`
- [ ] Confirmed a truncating `zip` also **consumed** an item from the longer iterator
- [ ] Used `enumerate(x, start=1)` and confirmed nothing was skipped
- [ ] Wrote `zip(*rows)` and understood it as a transpose
- [ ] Wrote a `while` loop with all three parts — progress, cap, failure exit
- [ ] Used `time.monotonic()` for a deadline and can say why not `time.time()`
- [ ] Confirmed `0.1` added ten times is not `1.0`, and can say what that does to `while x != 1.0:`

## Section 2 — leaving a loop early

- [ ] Read [2.1 — `break` and which loop it leaves](parts/02-control-flow/2.1-break-and-which-loop-it-leaves.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — `continue` and the skipped increment](parts/02-control-flow/2.2-continue-and-the-skipped-increment.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — `for ... else`](parts/02-control-flow/2.3-for-else.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — mutating while iterating](parts/02-control-flow/2.4-mutating-while-iterating.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Confirmed a `break` in an inner loop leaves the outer loop running
- [ ] Wrote the second `break` and saw it fire on **every** outer pass, not only after a match
- [ ] Wrote all three exits from a nested loop — flag, function + `return`, restructure
- [ ] **Reproduced the leftover-variable bug**: an empty inner group reporting the previous group's match
- [ ] Wrote the `while` + `continue` hang (with a safety counter), and moved the increment to fix it
- [ ] Moved a `continue` above and below an accumulator and got two means differing by two thirds
- [ ] Wrote a guard-clause loop with three counted rejection reasons and a reconciliation line
- [ ] Confirmed a `for ... else` runs on an **empty** iterable
- [ ] Confirmed `break` skips the `else` and does **not** skip a `finally`
- [ ] Moved an `else` in by four spaces and watched it attach to the `if` instead of the loop
- [ ] **Removed from a list while iterating and watched a row survive** — with a `visited` list as the witness
- [ ] Got `RuntimeError: dictionary changed size during iteration`, and the `Set` variant
- [ ] Confirmed changing dict **values** during iteration does not raise
- [ ] Wrote all three fixes — rebuild, iterate a copy, iterate backwards — and got the same result
- [ ] Wrote `for row in rows: row = clean(row)` and confirmed it does nothing

## Section 3 — the capped retry

- [ ] Read [3.1 — why the cap comes first](parts/03-capped-retry/3.1-why-the-cap-comes-first.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — the capped retry from scratch](parts/03-capped-retry/3.2-the-capped-retry-from-scratch.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — which errors are worth retrying](parts/03-capped-retry/3.3-which-errors-are-retryable.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Computed the amplification table and can state the number for three attempts at four layers
- [ ] Ran an uncapped loop against a permanently-failing fake and watched it spend the whole call budget
- [ ] Ran the capped version and confirmed it spent exactly `max_attempts` calls
- [ ] Wrote a `while a != 3` cap with a step of 2 and watched it never fire — then switched to `>=`
- [ ] Wrote a loop with **both** bounds: an attempt cap and a `monotonic` deadline
- [ ] Confirmed the two bounds report **different** outcomes, and can say what each tells an operator
- [ ] Injected the sleep function and recorded the delays instead of waiting
- [ ] Confirmed the delay list has **one fewer** entry than there were failures
- [ ] Read a traceback with `raise ... from` and one without, and can say what the second loses
- [ ] Called the retry with `max_attempts=0` and got a `ValueError`, not a silent failure
- [ ] Wrote `is_retryable` as a **function**, not as `except` clauses
- [ ] Classified all eight cases including `401` and `KeyError`, and wrote the reasoning down
- [ ] Watched a broad `except Exception` retry a `400` three times and hide the real message
- [ ] Used a bare `raise` to re-raise, and can say why not `raise exc`
- [ ] Ran the idempotency-key demo and watched a retry produce two charges without one

## Section 4 — what a loop costs

- [ ] Read [4.1 — the accidental quadratic](parts/04-loop-cost/4.1-the-accidental-quadratic.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — the loop you should not write](parts/04-loop-cost/4.2-the-loop-you-should-not-write.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Ran the ratio test at three sizes** and watched one column converge on 2 and the other on 4
- [ ] Can say which number means linear and which means quadratic, without looking
- [ ] Timed `+=` string building against `"".join`, then **doubled `N`** and watched the ratio change
- [ ] Timed `list.insert(0, x)` against `deque.appendleft`
- [ ] Replaced a nested-loop join with a dict index and watched the **speedup itself grow** with `n`
- [ ] Confirmed the correctness tests pass against the quadratic implementation
- [ ] Timed the dot product three ways in pure Python and confirmed all three are within ~2×
- [ ] Can name the two per-item costs a Python loop pays that compiled code does not
- [ ] Named three loops in your own code that should **stay** loops, and why for each

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/retry.py`
- [ ] Implemented `backoff_delay` — with the comment explaining the ceiling
- [ ] Implemented `is_retryable` — with the written reasoning, including the `401` decision
- [ ] Implemented `call_with_retry` — and all five properties in its `TODO` are true
- [ ] Created `src/setu/loops.py`
- [ ] Implemented `chunked` — **streaming**, with no `list(items)` anywhere
- [ ] Implemented `first_matching` — with the comment saying which of the three shapes you chose and why
- [ ] Reproduced all four story loops in `notebooks/day-06-scratch.ipynb`
- [ ] The notebook is **not** committed; the understanding graduated to `src/setu/` (Principle 6)
- [ ] `uv run ruff check src/ tests/` passes, including `B007` and `E722`

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_retry.py -v` **before** implementing and watched every test fail
- [ ] Implemented `test_succeeds_first_time_makes_exactly_one_call` — asserting the **call count**
- [ ] Implemented `test_succeeds_after_retries_and_stops_there` — asserting **two** delays, not three
- [ ] Implemented the parametrised `test_never_exceeds_the_cap`
- [ ] Implemented `test_exhaustion_chains_the_original_error` — asserting `__cause__`
- [ ] Implemented `test_a_non_retryable_error_is_not_retried` — asserting `calls == 1`
- [ ] Implemented the parametrised `test_a_nonsense_cap_is_rejected`
- [ ] Implemented `test_backoff_grows_and_is_capped` — many draws per attempt, with the seeding decision written down
- [ ] Implemented `test_is_retryable_classifies_the_table`
- [ ] Implemented `test_chunked_tiles_without_gaps_or_overlap`
- [ ] Implemented `test_chunked_does_not_consume_the_whole_iterable`
- [ ] Implemented `test_first_matching_stops_early` — counting predicate calls
- [ ] **Break it, watch it go red, fix it —** removed the sleep guard, saw only the delay-count assertion fail. Restored it.
- [ ] **Break it, watch it go red, fix it —** dropped `from last_error`, saw only the chaining test fail, and read both tracebacks. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `is_retryable` return `True` always, saw two tests fail for different reasons. Restored it.
- [ ] **Break it, watch it go red, fix it —** rewrote the loop as `while True` with a forgotten increment, **watched the cap test hang**, killed it, and can say why `for ... in range()` makes that impossible. Restored it.
- [ ] **The one that matters most —** added `list(items)` to the top of `chunked`, watched the tiling test **still pass** and only the streaming test go red, and can say why a correctness test cannot see a streaming bug
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today — every service was a fake that counted its own calls
- [ ] **0** network requests — nothing today left the machine
- [ ] **$0** spent (Principle 5)
- [ ] Can say why building the cap against a fake **before** a real endpoint is the point

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] The four steps a `for` loop takes, using `iter`, `next` and `StopIteration`
- [ ] Why looping a list twice works and looping a generator twice does not
- [ ] What a `range` object stores, and why its size does not depend on its length
- [ ] The four things the exclusive upper bound buys, and the one place it bites
- [ ] What `zip` does on unequal lengths, and why that default is dangerous for evaluation code
- [ ] Two things `enumerate` can do that `range(len(x))` cannot
- [ ] The three things every `while` loop needs, and which one the polling story was missing
- [ ] Why a deadline uses `time.monotonic()`
- [ ] Exactly what `break` leaves and what it does not
- [ ] The three ways out of a nested loop, and which one usually removes the nesting
- [ ] Where `continue` jumps to in each loop type, and why only one of them can hang
- [ ] The placement rule that prevents both of `continue`'s failure modes
- [ ] When a loop's `else` clause runs, and the three exits that skip it
- [ ] Why removing from a list during iteration skips items, in terms of what the iterator holds
- [ ] Why a dict raises where a list does not
- [ ] The five decisions every retry loop makes
- [ ] Retry amplification in one sentence, with the number for three attempts at four layers
- [ ] The retry loop's twelve lines, and which decision each implements
- [ ] Why the sleep is skipped on the last attempt, and what `raise ... from` preserves
- [ ] The one question that decides whether a failure is retryable, with three codes on each side
- [ ] Why a timeout on a `POST` is neither, and what makes it safe
- [ ] Five operations that look constant inside a loop and are not
- [ ] The ratio test in one sentence, and what number means what
- [ ] The two per-item costs a Python loop pays that compiled code does not
- [ ] Three situations where vectorising would be the wrong fix

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `src/setu/retry.py`, `src/setu/loops.py` and `tests/test_retry.py` staged
- [ ] `notebooks/day-06-scratch.ipynb` does **not** appear in `git status` (Principle 6)
- [ ] `uv run ruff format days/day-06-loops/ src/ tests/` has run
- [ ] `uv run python scripts/depth_check.py 6` passes
- [ ] `./m done 6` ran green and created the commit
