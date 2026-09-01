---
day: 14
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 14 — Decorators: @timed and @retry"
ids: ["PY-16"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P11 blast radius", "P12 humans gate writes", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 15
generated: "2026-09-01"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 14 — Decorators: `@timed` and `@retry`

**Phase 2 · Advanced Python · Module 2** · `PY-16` decorators. The plan's named examples are
**`@timed` and `@retry(3)` — reused in every later phase**, and by the end of today both exist in
`src/setu/decorators.py` with tests that can go red.

> **Yesterday:** how one class starts from another, why one loop handles three of them, and how a base
> class refuses to be built half-finished.
> **Today:** how to wrap a function in behaviour it does not know about — measuring it, repeating it,
> remembering its answer — without editing a line of it.
> **Tomorrow:** `classmethod`, `staticmethod`, `property` and the dunder methods, which are the
> language's own decorators and its own hooks.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

There is a desk in the lobby of a small office building, and a book on the desk.

You come in for one folder from the third floor. You do not walk straight to the lift; you stop at the
desk, somebody writes your name and the time in the book, and then you go up. On the way back out they
write the time again and hand you the folder.

The office upstairs knows none of this happened. Somebody knocked, they handed over a folder, that was
their whole involvement. The visitor's experience did not change either: they asked for a folder and
they got one.

Everything today is in that lobby.

- **The desk never does the visiting.** It is handed a job and arranges things around it. A job is a
  thing you can hold, describe and give to somebody else.
- **The book adds a second column.** In and out, so a visit has a length, and the odd one stands out.
  That is `@timed`.
- **A second desk at the foot of the stairs** sends you up again if nobody answers, twice, then sends
  you home. That is `@retry(3)`.
- **The badge says VISITOR.** Not your name. The desk knows exactly who you are and did not write it on
  the thing everybody upstairs reads. That is a decorator without `functools.wraps`.
- **The desk hands the folder over at the end.** If it kept it, you would leave with nothing and find
  out in the car park. That is a wrapper that forgot to `return`.
- **Somebody wrote the answer on a sticky note** so they would not have to look it up again. Then
  payroll moved floors, and nobody updated the note. That is `functools.cache`.
- **And there are four desks now**, and a new starter cannot find out what happens when they walk in
  the front door without a guided tour. That is when a decorator is the wrong tool.

One thing is worth saying before any code: nothing today is new machinery. A decorator is a function
that takes a function and returns a function, and you have had all three of those since Day 10. What is
new is one symbol, `@`, and a habit of mind.

---

## §2 The map

**What the section numbers mean today.** One ID, so the plan's `lab (1 ID)` split — mechanism →
behaviour → edge case → failure mode → production use. **1.x** is the ground floor: functions as values,
and the wrapper built by hand before any syntax exists. **2.x** is writing one properly: the four things
a wrapper must get right. **3.x** is the third layer, where the decorator takes an argument, and the
three real-world decisions that come with retrying. **4.x** is the toolkit: on a method, from the
standard library, and when not to reach for one at all.

### Section 1 — functions as values

| Part | What it answers | Level |
|---|---|---|
| [1.1 A function is a value you can hand to somebody else](parts/01-functions-as-values/1.1-a-function-is-a-value.md) | What is the difference between `collect` and `collect()`? | `foundation` |
| [1.2 A function that builds another function](parts/01-functions-as-values/1.2-a-function-that-returns-a-function.md) | How does a returned function remember anything? | `working` |
| [1.3 The wrapper written by hand](parts/01-functions-as-values/1.3-the-wrapper-written-by-hand.md) | What are the four steps of a decorator, with no `@` in sight? | `working` |
| [1.4 The `@` sign is the rebinding you already wrote](parts/01-functions-as-values/1.4-the-at-sign-is-two-lines.md) | What does `@` actually do, and when does it run? | `foundation` |

### Section 2 — writing a decorator

| Part | What it answers | Level |
|---|---|---|
| [2.1 `*args` and `**kwargs` in a wrapper](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md) | How does one wrapper fit every function? | `working` |
| [2.2 The badge that lost your name](parts/02-writing-a-decorator/2.2-functools-wraps.md) | Why does the profiler say every function is called `wrapper`? | `working` |
| [2.3 The decorator that ate the return value](parts/02-writing-a-decorator/2.3-returning-the-value.md) | Why is this function suddenly returning `None`? | `working` |
| [2.4 `@timed`, the first real one](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md) | Which clock, and why `finally`? | `working` |
| [2.5 Stacking, and the order that changes the answer](parts/02-writing-a-decorator/2.5-stacking-and-the-order.md) | In `@a` over `@b`, which runs first? | `production` |

### Section 3 — decorators with arguments

| Part | What it answers | Level |
|---|---|---|
| [3.1 `@retry(3)` — three nested functions](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md) | Why does a decorator with an argument need a third layer? | `working` |
| [3.2 Backoff, jitter, and which errors](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md) | What does a retry cost the service it is retrying? | `production` |
| [3.3 The retry that made it worse](parts/03-decorators-with-arguments/3.3-the-retry-that-made-it-worse.md) | When is repeating a call not safe? | `production` |

### Section 4 — the toolkit

| Part | What it answers | Level |
|---|---|---|
| [4.1 A decorator on a method, and where `self` goes](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md) | How many wrapper objects exist for a class with a thousand instances? | `production` |
| [4.2 `functools.cache` and its trap](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md) | What does a cache keep, and for how long? | `production` |
| [4.3 When a decorator is the wrong tool](parts/04-the-toolkit/4.3-when-a-decorator-is-wrong.md) | What does every decorator cost a reader? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `functools` and `time` from the
standard library. Module 2 is still the language; the first new dependency is Phase 3.

```bash
mkdir -p src/setu tests notebooks
touch src/setu/decorators.py tests/test_decorators.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-14-scratch.ipynb

# yesterday's loaders must already exist - today's decorators go on their methods
uv run python -c "from setu.loaders import LOADERS; print('loaders ok:', sorted(LOADERS))"

# the six facts the day is built on, before any part names them
uv run python -c "
import functools
import time


def collect(what):
    return f'one {what}'


desk = collect
print('1 a function is a value       :', desk is collect, desk.__name__, '<- part 1.1')


def make_greeter(floor):
    def greet():
        return f'floor {floor}'
    return greet


print('2 a factory builds two of them:', make_greeter(3)(), '/', make_greeter(4)(), '<- part 1.2')


def plain(job):
    def wrapper(*a, **k):
        return job(*a, **k)
    return wrapper


@plain
def signed(what):
    '''Fetch it.'''
    return f'one {what}'


print('3 the badge lost its name     :', signed.__name__, '/ doc:', signed.__doc__, '<- part 2.2')
print(
    '4 the two clocks              :',
    time.get_clock_info('time').resolution,
    'vs',
    time.get_clock_info('perf_counter').resolution,
    '<- part 2.4',
)


def retry(attempts):
    def decorator(job):
        @functools.wraps(job)
        def wrapper(*a, **k):
            return job(*a, **k)
        return wrapper
    return decorator


@retry
def oops(what):
    return f'one {what}'


print('5 @retry with no brackets     :', type(oops('folder')).__name__, '<- part 3.1')


@functools.cache
def shopping(name):
    return ['milk']


first = shopping('weekly')
first.append('bread')
print('6 the cache hands out the same:', shopping('weekly'), '<- part 4.2')
"

# the two rules that catch today's headline mistakes, read from the installed linter
uv run ruff rule B023
uv run ruff rule B008
```

Expected from the six-fact block on this machine, on 2026-09-01:

```
1 a function is a value       : True collect <- part 1.1
2 a factory builds two of them: floor 3 / floor 4 <- part 1.2
3 the badge lost its name     : wrapper / doc: None <- part 2.2
4 the two clocks              : 0.015625 vs 1e-07 <- part 2.4
5 @retry with no brackets     : function <- part 3.1
6 the cache hands out the same: ['milk', 'bread'] <- part 4.2
```

| What | Where it comes from | Part |
|---|---|---|
| functions as values, `__name__` | language | [1.1](parts/01-functions-as-values/1.1-a-function-is-a-value.md) |
| closures, `__closure__` | language | [1.2](parts/01-functions-as-values/1.2-a-function-that-returns-a-function.md) |
| the `@` transformation | language, *PEP 318* | [1.4](parts/01-functions-as-values/1.4-the-at-sign-is-two-lines.md) |
| `*args`, `**kwargs` in both directions | already met on [Day 10](../day-10-functions/parts/01-the-signature/1.4-args-and-kwargs.md) | [2.1](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md) |
| `functools.wraps`, `__wrapped__`, `inspect.signature` | standard library | [2.2](parts/02-writing-a-decorator/2.2-functools-wraps.md) |
| `time.perf_counter`, `get_clock_info`, `try`/`finally` | standard library, *PEP 418* | [2.4](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md) |
| the capped retry loop | already built on [Day 6](../day-06-loops/parts/03-capped-retry/3.2-the-capped-retry-from-scratch.md) | [3.1](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md) |
| which errors are retryable | already argued on [Day 6](../day-06-loops/parts/03-capped-retry/3.3-which-errors-are-retryable.md) | [3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md) |
| `random.Random(seed)`, seeded jitter | standard library, Principle 4 | [3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md) |
| `429` and `Retry-After` | already met on [Day 3](../day-03-keys-and-budget/parts/04-rate-budget/4.2-429-and-real-backoff.md) | [3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md) |
| methods are functions on the class | already met on [Day 12](../day-12-classes/parts/01-the-blank-form/1.3-methods-find-their-object.md) | [4.1](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md) |
| `functools.cache`, `lru_cache`, `cache_info` | standard library | [4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md) |
| hashability of arguments | already met on [Day 4](../day-04-objects/parts/02-containers/2.5-hashability.md) | [4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md) |
| the loaders these decorators go on | already built on [Day 13](../day-13-inheritance-and-abstraction/parts/04-abstraction/4.2-the-loader-family.md) | [4.1](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md) |

---

## §4 Build brief

**One new module**, `src/setu/decorators.py`, holding exactly two decorators. `src/setu/loaders/` is
imported and not changed.

**1. `src/setu/decorators.py`** — `timed` first
([2.4](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md) explains every line).

```python
"""Two decorators, reused in every phase after this one."""

from __future__ import annotations

import functools
import random
import time
from collections.abc import Callable


def timed(job: Callable) -> Callable:
    """Report how long `job` took, and hand back whatever it returned.

    The report goes to `print` today. Part 2.4's `In production` says why a
    real one emits a metric instead, and Day 19 is where that changes.
    """
    # TODO(me): @functools.wraps(job) on the wrapper (part 2.2), *args/**kwargs
    # (part 2.1), perf_counter and NOT time.time (part 2.4), and the report in a
    # `finally` so a slow FAILURE is reported too. Say in a comment what the
    # `finally` buys that a line after the call does not.
    raise NotImplementedError


def retry(
    attempts: int,
    *,
    catching: type[BaseException] | tuple[type[BaseException], ...],
    base: float = 0.5,
    factor: float = 2.0,
    jitter: float = 0.25,
    seed: int = 0,
    sleep: Callable[[float], None] = time.sleep,
) -> Callable:
    """Re-run `job` up to `attempts` times, waiting longer after each failure.

    `catching` has NO default on purpose: part 3.2 shows what `Exception`
    costs. `sleep` is injectable so the tests do not take real seconds.
    `seed` is here for the same reason `random_state=` is on every estimator
    from Phase 12 (Principle 4) - a jittered schedule must be reproducible.

    This decorator does NOT make a call safe to repeat. Read part 3.3 before
    putting it on anything that writes.
    """
    # TODO(me): validate `attempts` HERE, in the factory, so a bad config fails
    # at import (part 3.1's last failure). Then three layers: factory,
    # decorator, wrapper.
    #
    # In the wrapper: build `random.Random(seed)` INSIDE it, not in the factory
    # - part 3.2 says why. Loop from 1 to attempts. Return inside the try.
    # Re-raise on the last attempt BEFORE computing a wait. Then compute the
    # wait and call `sleep`.
    raise NotImplementedError
```

**2. Put them on Day 13's loaders**, without editing `src/setu/loaders/`.

```python
"""Decorating something you already wrote, from the outside."""

from __future__ import annotations

import io

from setu.decorators import retry, timed
from setu.loaders.text import TextLoader

# TODO(me): decorate TextLoader.load with timed at the class level - one line,
# `TextLoader.load = timed(TextLoader.load)`. Then say in a comment how many
# wrapper objects that created for a thousand TextLoader instances (part 4.1),
# and whether `@retry` belongs here at all given part 3.3.
loader = TextLoader("weekly", io.StringIO("The Kitchen Table\nWeeknight Bread\n"))
print(loader.load())
```

**3. Reproduce the six traps in the notebook, then throw the notebook away.** In
`notebooks/day-14-scratch.ipynb`, in this order:

- Write a wrapper with no `return` in front of the inner call and watch a decorated function return
  `None` ([2.3](parts/02-writing-a-decorator/2.3-returning-the-value.md)). Then call `.upper()` on the
  result and read where the traceback points.
- Decorate two functions with a decorator that has no `functools.wraps`, register them in a dictionary
  keyed on `__name__`, and count the entries
  ([2.2](parts/02-writing-a-decorator/2.2-functools-wraps.md)).
- Time the same fast function with `time.time()` three times and with `perf_counter()` three times
  ([2.4](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md)).
- Put `@timed` and `@retry(3)` on one function both ways round and read the two logs
  ([2.5](parts/02-writing-a-decorator/2.5-stacking-and-the-order.md)).
- Write `@retry` with no brackets and print what the "function" returns
  ([3.1](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md)).
- Cache a function that returns a list, append to the result, and call it again
  ([4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md)).

**The notebook is not committed** (Principle 6); `src/setu/decorators.py` and its tests are.

**4. Decide, in writing, whether `@retry` may go on any loader method.** Write two sentences in
`retry`'s docstring naming which of Day 13's methods it is safe on and which it is not, and why
([3.3](parts/03-decorators-with-arguments/3.3-the-retry-that-made-it-worse.md) has the argument).
Either answer can be defended; an undecided one cannot.

---

## §5 The eval that must be able to fail

Create `tests/test_decorators.py`. Every one runs offline, spends nothing, and belongs in `./m check`.

```python
"""Day 14: what a decorator must preserve, and what a retry must not do."""

from __future__ import annotations

import inspect

import pytest

from setu.decorators import retry, timed


def make_flaky(fail_times, error=TimeoutError):
    """A function that fails `fail_times` times, then works. Counts its calls."""
    # TODO(me): a closure over a mutable counter (part 1.2). Return the function
    # AND the counter so a test can assert how many calls really happened.
    raise NotImplementedError


def test_timed_returns_the_functions_value() -> None:
    """Part 2.3: a reporting decorator must not change the answer."""
    # TODO(me): assert the decorated function returns exactly what the
    # undecorated one does. NOT `assert result` - that passes for any truthy
    # value and this test exists to reject None.
    raise NotImplementedError


def test_timed_lets_the_exception_through() -> None:
    """Part 2.4: `finally`, not `except`. A slow failure is still a failure."""
    # TODO(me): pytest.raises around a decorated function that raises.
    raise NotImplementedError


def test_timed_keeps_the_name_and_the_signature() -> None:
    """Part 2.2: without wraps, every profiler groups everything as 'wrapper'."""
    # TODO(me): assert __name__, __doc__ AND str(inspect.signature(f)). The
    # signature assertion is the one that catches a missing wraps even when
    # somebody has copied __name__ across by hand.
    raise NotImplementedError


def test_retry_stops_at_the_cap() -> None:
    """Part 3.1: attempts is a cap, and the last one must RAISE."""
    # TODO(me): a function that always fails, retry(3), pytest.raises, and then
    # assert the counter is exactly 3. Both halves matter: an implementation
    # that returns None passes the count and fails the raises.
    raise NotImplementedError


def test_retry_returns_as_soon_as_it_works() -> None:
    """A function that works first time is called once."""
    # TODO(me): make_flaky(0), assert the counter is 1. This is the test that
    # catches a loop that always runs to `attempts`.
    raise NotImplementedError


def test_retry_does_not_catch_what_it_was_not_told_to() -> None:
    """Part 3.2: catching=Exception turns a bug into four bugs."""
    # TODO(me): retry(4, catching=TimeoutError) on a function raising KeyError.
    # Assert the KeyError escapes AND that the counter is 1.
    raise NotImplementedError


def test_retry_waits_longer_each_time() -> None:
    """Part 3.2: backoff. The schedule is the thing worth asserting."""
    # TODO(me): pass sleep=waits.append and assert the recorded list is
    # strictly increasing. Not the exact values - those are the jitter's - the
    # SHAPE.
    raise NotImplementedError


def test_retry_is_reproducible_from_its_seed() -> None:
    """Principle 4: nothing floats, including randomness."""
    # TODO(me): run the same decorated function twice with the same seed and
    # assert the two recorded wait lists are equal. Then say in a comment why
    # the Random must be built inside the wrapper and not in the factory.
    raise NotImplementedError


def test_retry_does_not_sleep_after_the_last_attempt() -> None:
    """Part 3.2: waiting and then giving up is pure waste."""
    # TODO(me): attempts=3, assert len(waits) == 2. Off by one here costs the
    # caller the whole final backoff on every failure.
    raise NotImplementedError


def test_retry_refuses_a_nonsense_attempt_count() -> None:
    """Part 3.1: validation belongs in the factory, so it fails at import."""
    # TODO(me): pytest.raises(ValueError) around retry(0, catching=TimeoutError).
    # Note there is no `def` and no `@` in this test - the factory must fail on
    # its own, before it ever meets a function.
    raise NotImplementedError


@pytest.mark.parametrize("decorator_name", ["timed", "retry"])
def test_both_decorators_are_documented(decorator_name) -> None:
    """A decorator nobody can name is worse than no decorator (part 4.3)."""
    # TODO(me): assert the docstring exists and mentions its precondition.
    # This one looks like box-ticking until part 3.3 - a retry whose docstring
    # does not say 'only on idempotent calls' will be copied onto a write.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_decorators.py -v
```

Then implement, then **break each one on purpose**:

- Delete `return` in front of the inner call in `timed`. **`test_timed_returns_the_functions_value` goes
  red and nothing else does** — which is exactly why that test asserts the value and not truthiness.
- Change `finally:` to `except Exception: pass` in `timed`. The exception test goes red; the value test
  stays green. **Two tests, two different promises.**
- Delete `@functools.wraps(job)`. The name test goes red — and note that if you copy `__name__` across
  by hand, the *signature* assertion is still red, which is why it is there.
- Change `if attempt == attempts: raise` to `pass`. **`test_retry_stops_at_the_cap` goes red on the
  `pytest.raises` half while the call-count half stays green.** Sit with that: the function was called
  the right number of times and returned `None`.
- Move `rng = random.Random(seed)` from the wrapper into the factory. Every test passes on a single
  run and `test_retry_is_reproducible_from_its_seed` goes red — because the second call continues the
  first call's sequence.
- Compute the wait **before** the last-attempt `raise`. `test_retry_does_not_sleep_after_the_last_attempt`
  goes red, and the number it reports is the backoff you were about to charge every caller on every
  failure.
- **Break it and watch every test stay GREEN** — widen `catching` to `Exception` *and* delete
  `test_retry_does_not_catch_what_it_was_not_told_to`. Everything passes. Restore the test, watch it go
  red, and say out loud what the missing test was protecting.

That last item is the most important line in this section. A test suite is only as good as the promises
somebody thought to write down, and `catching=Exception` is a change that no test about timing, naming
or counting can see.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — nothing today leaves your machine |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |

Every test injects `sleep`, so the suite spends no wall-clock time either
([3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md)). A retry decorator
tested with real sleeping is how a fast suite becomes one people skip
([Day 2, 4.1](../day-02-quality-gate/parts/04-the-gate/4.1-what-m-check-actually-runs.md)).

---

## §7 Traps

- **`collect` and `collect()` differ by one character and by everything** —
  [1.1](parts/01-functions-as-values/1.1-a-function-is-a-value.md).
- **`'str' object is not callable` means you called instead of handing over** —
  [1.1](parts/01-functions-as-values/1.1-a-function-is-a-value.md).
- **`return greet()` inside a factory calls it while building it** —
  [1.2](parts/01-functions-as-values/1.2-a-function-that-returns-a-function.md).
- **A closure built in a loop captures the loop variable, not its value** —
  [1.2](parts/01-functions-as-values/1.2-a-function-that-returns-a-function.md).
- **Forgetting `return wrapper` gives `'NoneType' object is not callable`** —
  [1.3](parts/01-functions-as-values/1.3-the-wrapper-written-by-hand.md).
- **A wrapper with a fixed signature can only wrap one shape of function** —
  [1.3](parts/01-functions-as-values/1.3-the-wrapper-written-by-hand.md),
  [2.1](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md).
- **A decorator runs at import, not at call time** —
  [1.4](parts/01-functions-as-values/1.4-the-at-sign-is-two-lines.md).
- **Anything non-callable after `@` fails at the decorator line, at start-up** —
  [1.4](parts/01-functions-as-values/1.4-the-at-sign-is-two-lines.md).
- **A wrapper with `*args` but no `**kwargs` rejects every keyword call** —
  [2.1](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md).
- **Passing `job(args, kwargs)` without the stars sends two objects, not the arguments** —
  [2.1](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md).
- **A wrapper that names a parameter shadows the function's own default, silently** —
  [2.1](parts/02-writing-a-decorator/2.1-args-and-kwargs-in-a-wrapper.md).
- **Without `functools.wraps`, a registry keyed on `__name__` keeps one entry for every handler** —
  [2.2](parts/02-writing-a-decorator/2.2-functools-wraps.md).
- **`help()` and generated API docs go blank on every decorated function** —
  [2.2](parts/02-writing-a-decorator/2.2-functools-wraps.md).
- **`@functools.wraps` without `(job)` fails inside `functools.py`, not in your code** —
  [2.2](parts/02-writing-a-decorator/2.2-functools-wraps.md).
- **A wrapper with no `return` makes every decorated function return `None`** —
  [2.3](parts/02-writing-a-decorator/2.3-returning-the-value.md).
- **`return print(...)` also returns `None`, and survives review more often** —
  [2.3](parts/02-writing-a-decorator/2.3-returning-the-value.md).
- **An `except` with no re-raise turns a crash into a wrong answer** —
  [2.3](parts/02-writing-a-decorator/2.3-returning-the-value.md).
- **`time.time()` has a resolution of about 15.6 ms on Windows and reports `0.000000` for fast work** —
  [2.4](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md).
- **A timing decorator on a generator function measures building the generator** —
  [2.4](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md).
- **Reporting after the call instead of in `finally` reports nothing on the error path** —
  [2.4](parts/02-writing-a-decorator/2.4-timed-the-first-real-one.md).
- **Stacked decorators are applied bottom-up and run top-down** —
  [2.5](parts/02-writing-a-decorator/2.5-stacking-and-the-order.md).
- **A cache above a timer means cache hits are never recorded** —
  [2.5](parts/02-writing-a-decorator/2.5-stacking-and-the-order.md).
- **One layer missing `wraps` loses the name for the whole stack** —
  [2.5](parts/02-writing-a-decorator/2.5-stacking-and-the-order.md).
- **`@retry` without brackets binds the function to `attempts` and raises nothing** —
  [3.1](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md).
- **A retry loop that falls off the bottom returns `None` after every attempt failed** —
  [3.1](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md).
- **`attempts=0` means the function is never called at all** —
  [3.1](parts/03-decorators-with-arguments/3.1-retry-three-a-decorator-that-takes-an-argument.md).
- **`catching=Exception` spends every attempt on errors that can never succeed** —
  [3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md).
- **Module-level `random` makes a wait schedule depend on test order** —
  [3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md).
- **Five attempts of "just half a second" is seven and a half seconds of the caller's budget** —
  [3.2](parts/03-decorators-with-arguments/3.2-backoff-jitter-and-which-errors.md).
- **A timeout does not mean the call failed — only that you did not hear the answer** —
  [3.3](parts/03-decorators-with-arguments/3.3-the-retry-that-made-it-worse.md).
- **Retrying a write without an idempotency key writes it more than once** —
  [3.3](parts/03-decorators-with-arguments/3.3-the-retry-that-made-it-worse.md).
- **A retry inside a transaction reports the aborted-transaction error, not the real one** —
  [3.3](parts/03-decorators-with-arguments/3.3-the-retry-that-made-it-worse.md).
- **A decorator on a method is created once for the class, so its state is shared by every instance** —
  [4.1](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md).
- **`@classmethod` must be outermost or the wrapper tries to call a `classmethod` object** —
  [4.1](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md).
- **Logging `args` on a method logs `self`, which may be enormous or private** —
  [4.1](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md).
- **`functools.cache` requires hashable arguments, so it narrows what the function accepts** —
  [4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md).
- **A cached mutable return is shared, and one caller's `append` changes everybody's copy** —
  [4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md).
- **`@cache` on a method keeps every instance alive for the life of the process** —
  [4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md).
- **Nothing in a cache ever expires, so a changed source of truth goes unnoticed** —
  [4.2](parts/04-the-toolkit/4.2-functools-cache-and-its-trap.md).
- **A decorator that reaches into arguments breaks on keyword calls** —
  [4.3](parts/04-the-toolkit/4.3-when-a-decorator-is-wrong.md).
- **Every wrapper adds a frame to every traceback** —
  [4.3](parts/04-the-toolkit/4.3-when-a-decorator-is-wrong.md).
- **A decorator whose name needs "and" in it is two decorators** —
  [4.3](parts/04-the-toolkit/4.3-when-a-decorator-is-wrong.md).

---

## §8 Verify before you code

Fetched **2026-09-01**. Today is the language and two standard-library modules, so the language
reference and the PEPs are the authority:

- <https://docs.python.org/3/reference/compound_stmts.html#function-definitions> — the language
  reference for `def`, including the decorator grammar and the sentence that defines `@dec` as
  `func = dec(func)`.
- <https://peps.python.org/pep-0318/> — *PEP 318 — Decorators for Functions and Methods* (2003), which
  proposed the `@` syntax and states the readability problem it solves.
- <https://docs.python.org/3/library/functools.html> — `functools`, and specifically `wraps`,
  `update_wrapper`, `cache`, `lru_cache` and `cached_property`.
- <https://docs.python.org/3/library/time.html#time.perf_counter> — `perf_counter`, and
  `get_clock_info`, which is what the setup block above uses to print your machine's resolutions.
- <https://peps.python.org/pep-0418/> — *PEP 418 — Add monotonic time, performance counter, and process
  time functions* (2012), which is why there is more than one clock and what each one guarantees.
- <https://docs.python.org/3/library/inspect.html#inspect.signature> — `inspect.signature`, and the
  paragraph on `__wrapped__` that explains why `wraps` restores the signature.
- <https://docs.python.org/3/whatsnew/3.10.html> — the change that made `staticmethod` objects callable,
  which is why the decorator ordering rule in
  [4.1](parts/04-the-toolkit/4.1-a-decorator-on-a-method.md) is looser than older advice says.

---

## §9 Say it in an interview

> "A decorator is a function that takes a function and returns a function, and `@` is just
> `f = deco(f)` evaluated when the module is imported — so the wrapping happens once, at start-up, and
> anything expensive in the decorator's own body is import-time cost in every process. The wrapper has
> to be `*args, **kwargs`, because it replaces the function at its call site and must accept every call
> the function accepts; it must not name any of the function's parameters, or it silently shadows their
> defaults. Two lines matter more than they look: `functools.wraps`, because without it every profiler
> and error tracker groups everything under `wrapper` and a registry keyed on `__name__` collapses to
> one entry; and `return` in front of the inner call, because without that every decorated function
> returns `None` and you find out from an `AttributeError` on `'NoneType'` in unrelated code. For
> `@timed` I use `perf_counter` rather than `time.time` — the wall clock can jump and on Windows its
> resolution is about fifteen milliseconds — and I put the measurement in a `finally`, because a slow
> failure is the case you actually wanted it for. A decorator that takes an argument is three layers:
> factory, decorator, wrapper, one per thing to capture. On retries the interesting decisions are not
> the loop: which exceptions are worth repeating, exponential backoff with jitter so a hundred clients
> do not line up, an overall deadline rather than only an attempt count, and — the one people miss —
> whether the call is safe to repeat at all, because a timeout means you did not hear the answer, not
> that nothing happened. And I am careful about where they go: a decorator on a method is created once
> for the class, so any state in its closure is shared by every instance, which is how a cache becomes
> a cross-request data leak."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green,
`src/setu/decorators.py` holds a `timed` that reports on the error path and a `retry` whose wait
schedule is reproducible from a seed, and you have **watched a whole test suite stay green through a
real defect** — `catching` widened to `Exception`, in §5 — not when a particular amount of time has
passed. Then:

```bash
./m done 14
```

Tomorrow is `classmethod`, `staticmethod`, `property` and the dunder methods: the decorators the
language ships with, and the hooks that make an object of your own behave like one of Python's.
