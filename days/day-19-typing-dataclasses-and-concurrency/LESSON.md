---
day: 19
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 19 — Typing, dataclasses, Pydantic v2, and concurrency"
ids: ["PY-23", "PY-24"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P11 blast radius", "P14 amend the plan first", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: gate
plan: setu
plan_version: "v2.3.0"
parts: 26
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 19 — Typing, dataclasses, Pydantic v2, and concurrency

**Phase 2 · Advanced Python · Module 2 · THE PHASE GATE** · `PY-23` typing, dataclasses and Pydantic v2
basics; `PY-24` concurrency — threads, processes, `asyncio`. The plan's named examples are **`TriageResult`
as a Pydantic model — the contract reused from Day 172 to Day 240** and **20 HTTP fetches, sequential
versus `asyncio.gather`, timed**. Both exist by the end of today, and the phase gate —
**`Paper` hierarchy + custom exceptions + async fetcher, tested** — is demonstrated rather than described.

> **Yesterday:** what `raise` does, which type to raise, and how to design an exception family of your
> own — including `RateLimited`, which carries the number a retry loop needs.
> **Today:** the annotations you have been writing since Day 10 finally get read — by `dataclasses`, by a
> type checker, and by Pydantic — and then concurrency, ending with the phase gate.
> **Tomorrow:** Phase 3 and NumPy. A different world, where these Python foundations are assumed.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The post office counter, one more time — and today it is the paperwork and the queue.

- **The form has small grey words under each box**: *in grams, whole numbers*. Nobody at the counter
  enforces them. They are printed on the paper, not built into it, and for years the only thing that read
  them was a person.
- **Then the office got a scanner**, and it began flagging the boxes that did not match the words. Nothing
  about the form changed. Something started reading it.
- **The forms used to be typed one at a time**, and there were three versions in circulation that were
  nearly the same. A template fixed that: you give it the headings, it prints the boxes.
- **One box on the template was set up wrong** — a starting value that turned out to be one shared box
  every form pointed at, so the first customer's "books" appeared on the second customer's form.
- **The template got three settings**: ink not pencil, no margins, and headings filled in by name — after
  somebody swapped two columns in the layout and three hundred forms were quietly wrong.
- **The template prints boxes and does not read them.** A form arriving from the agency with "quite heavy"
  in the weight box is a perfectly well-formed form.
- **So the office put a person on the door**, and the surprise was the other half of her job: a weight
  typed as text becomes a number before it reaches the tray.
- **When she refuses a form** she clips a slip to it with a line per problem, so the sender fixes all
  three and comes back once instead of three times.
- **She works in both directions now** — the outgoing tray too — so one person knows what the depot's date
  format is and what the customer is allowed to see.
- **Then the queue.** People waiting for the depot to answer, and people waiting for cash to be counted:
  the same length of queue, and completely different problems.
- **Four clerks and one till key**, so exactly one is at the till at any moment — and the other three can
  all be on hold at once, because being on hold is not work.
- **One ledger, and two clerks reading it a second apart**, both adding to the number they read, and £15
  vanishing with no record anywhere.
- **A second counter** solved the counting, and every parcel now has to be *carried* there and back, which
  for the pallet of catalogues costs more than the weighing.
- **A ticket rail** replaced the queue: one clerk, forty tickets, and one way to break it — somebody hands
  her a shoebox of coins to count and the whole room stops.
- **A new clerk writes the ticket and never rings the depot.** The rail looks busy. A rail of tickets is
  what a busy day looks like.
- **The depot rang to complain** about forty calls in a minute, so the rail got four hooks — and a clock,
  because a call nobody answers holds a hook forever.
- **And the inspector arrives once a year** with a list, and asks to see the fire drill *working*, with
  somebody holding a door shut.

One thing before any code: **the two halves of today are the same idea twice.** In the morning, an
annotation is inert until something reads it — and then `dataclasses` and Pydantic read it. In the
afternoon, a program is sequential until something overlaps it — and whether overlapping helps depends
entirely on whether it was waiting or working.

---

## §2 The map

**What the section numbers mean today.** This is a `gate` day, so the plan's split is *one acceptance
criterion per part* for §5 — and the first four sections are the two IDs it rests on. **1.x** and **2.x**
are `PY-23`'s first half: annotations, and the library that reads them to generate code. **3.x** is
`PY-23`'s second half: the library that reads them to validate data. **4.x** is `PY-24` entire. **5.x** is
the gate: the criteria, the build, and the tests.

### Section 1 — type hints

| Part | What it answers | Level |
|---|---|---|
| [1.1 A hint is a note, not a rule](parts/01-type-hints/1.1-a-hint-is-a-note.md) | Does Python check `grams: int`? | `foundation` |
| [1.2 The vocabulary](parts/01-type-hints/1.2-the-vocabulary.md) | `list[str]` or `Iterable[str]`? | `foundation` |
| [1.3 `X \| None`](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md) | What does `Optional` actually mean? | `working` |
| [1.4 The type checker](parts/01-type-hints/1.4-the-type-checker.md) | What does it catch that a test does not? | `production` |

### Section 2 — dataclasses

| Part | What it answers | Level |
|---|---|---|
| [2.1 What `@dataclass` writes](parts/02-dataclasses/2.1-what-dataclass-writes.md) | Which three methods do you stop writing? | `foundation` |
| [2.2 `field(default_factory=…)`](parts/02-dataclasses/2.2-default-factory.md) | Why does `tags: list = []` refuse to compile? | `working` |
| [2.3 `frozen`, `slots`, `kw_only`](parts/02-dataclasses/2.3-frozen-slots-kw-only.md) | What does `frozen=True` buy you? | `working` |
| [2.4 `__post_init__`](parts/02-dataclasses/2.4-post-init.md) | Where does validation go? | `working` |
| [2.5 A dataclass is not a validator](parts/02-dataclasses/2.5-not-a-validator.md) | Why is this not enough at a boundary? | `production` |

### Section 3 — Pydantic v2

| Part | What it answers | Level |
|---|---|---|
| [3.1 The model that refuses](parts/03-pydantic/3.1-the-model-that-refuses.md) | What happens that a dataclass does not do? | `working` |
| [3.2 `ValidationError`](parts/03-pydantic/3.2-validationerror.md) | How do you show a user four problems at once? | `working` |
| [3.3 Coercion and `strict`](parts/03-pydantic/3.3-coercion-and-strict.md) | Why is `500.0` accepted and `500.5` not? | `production` |
| [3.4 `model_dump` and the boundary](parts/03-pydantic/3.4-model-dump-and-the-boundary.md) | Which dump can `json.dumps` handle? | `production` |
| [3.5 `TriageResult`](parts/03-pydantic/3.5-triage-result.md) | What does one model class do three times? | `production` |

### Section 4 — concurrency

| Part | What it answers | Level |
|---|---|---|
| [4.1 Waiting is not working](parts/04-concurrency/4.1-waiting-is-not-working.md) | Which kind of slow is this? | `foundation` |
| [4.2 The GIL](parts/04-concurrency/4.2-the-gil.md) | Why do threads not help arithmetic? | `working` |
| [4.3 Threads](parts/04-concurrency/4.3-threads.md) | Where did the £15 go? | `production` |
| [4.4 Processes](parts/04-concurrency/4.4-processes.md) | What does a worker process cost? | `production` |
| [4.5 `asyncio`](parts/04-concurrency/4.5-asyncio-one-thread.md) | How does one thread serve forty people? | `working` |
| [4.6 `async def`, `await`](parts/04-concurrency/4.6-async-await.md) | What do you get without the `await`? | `working` |
| [4.7 `asyncio.gather`](parts/04-concurrency/4.7-gather-and-twenty-fetches.md) | Twenty fetches — how much faster, really? | `production` |
| [4.8 Timeouts and `TaskGroup`](parts/04-concurrency/4.8-timeouts-and-taskgroup.md) | What happens to the siblings? | `production` |
| [4.9 Choosing](parts/04-concurrency/4.9-choosing.md) | Which of the three, and when none? | `production` |

### Section 5 — the gate

| Part | What it answers | Level |
|---|---|---|
| [5.1 The gate as a list](parts/05-the-gate/5.1-the-gate-as-a-list.md) | What exactly is Phase 2 asking for? | `production` |
| [5.2 The async fetcher](parts/05-the-gate/5.2-the-async-fetcher.md) | What are the four things besides `gather`? | `production` |
| [5.3 Testing async code](parts/05-the-gate/5.3-testing-async-code.md) | How do you test it with no plugin? | `production` |

---

## §3 Setup — run this

**Today adds the day's one new package.** Pydantic is the first dependency since Day 3, and Module 2's
last: Phase 3 opens with NumPy tomorrow.

```bash
# THE PIN. Plan Part 2 recorded 2.13.4 on 2026-08-21; PyPI on 2026-09-02 says 2.13.5.
# That is patch drift, which docs/PINS_DS.md says to pin and log in CHANGELOG_PLAN_DS.md.
uv add pydantic==2.13.5

# httpx is needed only for part 4.7's measurement and part 5.2's fetcher. It is already
# in the plan's forward table at 0.28.1 (Part 2, "Extras").
uv add httpx==0.28.1

mkdir -p tests notebooks
touch src/setu/models.py src/setu/fetcher.py tests/test_models.py tests/test_fetcher.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-19-scratch.ipynb

# yesterday's errors module must already exist - today's fetcher raises from it
uv run python -c "from setu.errors import RateLimited, SetuError; print('errors ok')"

# the twelve facts the day is built on, before any part names them
uv run python -c "
import asyncio, os, sys, time
from dataclasses import dataclass

print('1 a hint is a note      :', end=' ')
def weigh(g: int) -> int:
    return g * 2
print(repr(weigh('heavy')), '<- part 1.1')

@dataclass
class P:
    pid: int
    grams: int = 0
print('2 dataclass writes 3    :', [n for n in ('__init__','__repr__','__eq__') if n in vars(P)], '<- part 2.1')
print('3 and checks nothing    :', P('seven', 'heavy'), '<- part 2.5')

from pydantic import BaseModel, Field, ValidationError
class M(BaseModel):
    pid: int
    grams: int = Field(gt=0)
print('4 pydantic converts     :', M(pid='7741', grams='500'), '<- part 3.1')
try:
    M(pid='x', grams=-1)
except ValidationError as e:
    print('5 and refuses, all of it:', [(x['loc'][0], x['type']) for x in e.errors()], '<- part 3.2')

print('6 cores on this machine :', os.cpu_count(), '<- part 4.4')
print('7 the GIL switch interval:', sys.getswitchinterval(), '<- part 4.2')
w0, c0 = time.perf_counter(), time.process_time()
time.sleep(0.2)
print(f'8 waiting: cpu/wall     : {(time.process_time()-c0)/(time.perf_counter()-w0):.2f} <- part 4.1')
w0, c0 = time.perf_counter(), time.process_time()
sum(i*i for i in range(2_000_000))
print(f'9 working: cpu/wall     : {(time.process_time()-c0)/(time.perf_counter()-w0):.2f} <- part 4.1')

async def wait(n):
    await asyncio.sleep(0.2)
    return n
async def main():
    s = time.perf_counter()
    r = await asyncio.gather(*(wait(i) for i in range(10)))
    return time.perf_counter() - s, r
el, r = asyncio.run(main())
print(f'10 10 waits of 0.2s took: {el:.2f}s <- part 4.7')
print('11 a group is not its members:', isinstance(ExceptionGroup('g', [ValueError()]), ValueError), '<- part 4.8')
import httpx
print('12 httpx has both clients:', hasattr(httpx, 'Client'), hasattr(httpx, 'AsyncClient'), '<- part 5.2')
"

# the two rules that catch today's headline mistakes, read from the installed linter
uv run ruff rule B006
uv run ruff rule RUF006
```

Expected from the twelve-fact block on 2026-09-02. **Lines 6 and 7 differ by machine**, and lines 8 to 10
vary a little with load:

```
1 a hint is a note      : 'heavyheavy' <- part 1.1
2 dataclass writes 3    : ['__init__', '__repr__', '__eq__'] <- part 2.1
3 and checks nothing    : P(pid='seven', grams='heavy') <- part 2.5
4 pydantic converts     : pid=7741 grams=500 <- part 3.1
5 and refuses, all of it: [('pid', 'int_parsing'), ('grams', 'greater_than')] <- part 3.2
6 cores on this machine : 4 <- part 4.4
7 the GIL switch interval: 0.005 <- part 4.2
8 waiting: cpu/wall     : 0.00 <- part 4.1
9 working: cpu/wall     : 1.00 <- part 4.1
10 10 waits of 0.2s took: 0.21s <- part 4.7
11 a group is not its members: False <- part 4.8
12 httpx has both clients: True True <- part 5.2
```

**Lines 3 and 4 are the whole of the morning**, side by side: the same annotations, ignored by one tool
and enforced by the other. **Lines 8 and 9 are the whole of the afternoon**: the same two seconds of slow,
and completely different answers about what to do about it.

| What | Where it comes from | Part |
|---|---|---|
| annotations, `__annotations__`, `inspect.signature` | language | [1.1](parts/01-type-hints/1.1-a-hint-is-a-note.md) |
| `list[str]`, `X \| None`, `Any`, *PEP 585*, *PEP 604* | language | [1.2](parts/01-type-hints/1.2-the-vocabulary.md) |
| `Iterable`, `Sequence`, `Mapping` | `collections.abc` | [1.2](parts/01-type-hints/1.2-the-vocabulary.md) |
| narrowing with `is None` | language | [1.3](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md) |
| `mypy`, `--strict`, `# type: ignore[code]` | **not pinned** — a one-off `uv run --with` | [1.4](parts/01-type-hints/1.4-the-type-checker.md) |
| `@dataclass`, `fields`, `asdict`, `astuple` | standard library | [2.1](parts/02-dataclasses/2.1-what-dataclass-writes.md) |
| `field(default_factory=, repr=, compare=, init=)` | standard library | [2.2](parts/02-dataclasses/2.2-default-factory.md) |
| the mutable default argument | already met on [Day 4](../day-04-objects/parts/03-identity-trap/3.1-the-mutable-default-argument.md) | [2.2](parts/02-dataclasses/2.2-default-factory.md) |
| `__slots__` | already met on [Day 12](../day-12-classes/parts/02-attribute-lookup/2.3-slots-and-a-million-objects.md) | [2.3](parts/02-dataclasses/2.3-frozen-slots-kw-only.md) |
| `__hash__` and `__eq__` together | already met on [Day 15](../day-15-constructors-and-dunders/parts/03-the-dunders/3.4-hash-and-the-broken-set.md) | [2.3](parts/02-dataclasses/2.3-frozen-slots-kw-only.md) |
| `BaseModel`, `Field`, `ConfigDict` | `pydantic==2.13.5` | [3.1](parts/03-pydantic/3.1-the-model-that-refuses.md) |
| `ValidationError.errors()`, `loc`, `type` | `pydantic==2.13.5` | [3.2](parts/03-pydantic/3.2-validationerror.md) |
| lax and strict validation | `pydantic==2.13.5` | [3.3](parts/03-pydantic/3.3-coercion-and-strict.md) |
| `model_validate_json`, `model_dump`, `model_json_schema` | `pydantic==2.13.5` | [3.4](parts/03-pydantic/3.4-model-dump-and-the-boundary.md), [3.5](parts/03-pydantic/3.5-triage-result.md) |
| `StrEnum` | standard library, 3.11+ | [3.5](parts/03-pydantic/3.5-triage-result.md) |
| `time.perf_counter`, `time.process_time` | standard library | [4.1](parts/04-concurrency/4.1-waiting-is-not-working.md) |
| the GIL, `sys.getswitchinterval`, *PEP 703* | language | [4.2](parts/04-concurrency/4.2-the-gil.md) |
| `threading`, `Lock`, `ThreadPoolExecutor` | standard library | [4.3](parts/04-concurrency/4.3-threads.md) |
| `ProcessPoolExecutor`, pickling, `spawn` | standard library | [4.4](parts/04-concurrency/4.4-processes.md) |
| `if __name__ == "__main__":` | already met on [Day 17](../day-17-modules-and-packages/parts/01-the-module/1.4-the-name-that-changes.md) | [4.4](parts/04-concurrency/4.4-processes.md) |
| `asyncio.run`, the event loop, coroutines | standard library | [4.5](parts/04-concurrency/4.5-asyncio-one-thread.md) |
| generators, and why a coroutine is one | already met on [Day 11](../day-11-iterators-and-generators/parts/02-generators/2.1-yield-the-function-that-pauses.md) | [4.5](parts/04-concurrency/4.5-asyncio-one-thread.md) |
| `async def`, `await`, `async with`, `to_thread` | language | [4.6](parts/04-concurrency/4.6-async-await.md) |
| `gather`, `return_exceptions`, `Semaphore` | standard library | [4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md) |
| `httpx.Client` and `httpx.AsyncClient` | `httpx==0.28.1` | [4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md) |
| `asyncio.timeout`, `CancelledError`, `TaskGroup` | standard library | [4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md) |
| `ExceptionGroup` and `except*` | already met on [Day 18](../day-18-exceptions/parts/04-in-anger/4.5-exception-groups.md) | [4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md) |
| `RateLimited` and `retry_after` | already built on [Day 18](../day-18-exceptions/parts/03-your-own/3.2-an-exception-that-carries-data.md) | [5.2](parts/05-the-gate/5.2-the-async-fetcher.md) |
| `pytest.raises`, `recwarn` | `pytest==9.1.1` | [5.3](parts/05-the-gate/5.3-testing-async-code.md) |

---

## §4 Build brief

**Two new modules, and the phase gate.** `src/setu/models.py` is `TriageResult`;
`src/setu/fetcher.py` is the async fetcher. Both import `src/setu/errors.py` from yesterday and add
themselves to `LAYERS` in `src/setu/layout.py`
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**1. `src/setu/models.py`** — the plan's named contract
([3.5](parts/03-pydantic/3.5-triage-result.md) explains every line).

```python
"""The contracts that cross a boundary. Reused from Day 172 to Day 240."""

from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class Label(StrEnum):
    """The categories a triage decision may use. Values are the WIRE format."""

    BUG = "bug"
    FEATURE = "feature"
    QUESTION = "question"


class TriageResult(BaseModel):
    """What a model must return, checked."""

    # TODO(me): frozen=True and extra="forbid", and say in a comment what each
    # one protects against (parts 2.3 and 3.1). The second is the one that turns
    # a renamed field from a silent default into a rejection.
    model_config = ConfigDict()

    label: Label
    # TODO(me): confidence, a float in 0..1 inclusive (part 3.5). Decide ge/le
    # versus gt/lt and say why in a comment.
    # TODO(me): reason, a str with BOTH a min_length and a max_length. The
    # minimum is the one people forget; say what it stops.
    # TODO(me): tags, a list[str] with a default_factory (part 2.2).


def schema_for_prompt() -> dict:
    """The JSON Schema to hand a provider's structured-output mode (part 3.5)."""
    # TODO(me): one call. Then say in a comment which three jobs this one class
    # is now doing, and why that is worth more than the sum of them.
    raise NotImplementedError
```

**2. `src/setu/fetcher.py`** — the gate's third criterion
([5.2](parts/05-the-gate/5.2-the-async-fetcher.md) explains every line).

```python
"""Fetch many URLs concurrently, within a limit, reporting what it spent."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable, Iterable
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Budget:
    """What one run spent. Principle 5: every lab states its request budget."""

    requests: int = 0
    failures: int = 0
    concurrent_peak: int = 0
    _in_flight: int = field(default=0, repr=False)

    def start(self) -> None:
        # TODO(me): count the request, increment in-flight, and update the peak.
        # No lock: asyncio is one thread and there is no await in here (part 4.5).
        # Say that in a comment - it is the reason this is safe.
        raise NotImplementedError

    def finish(self, ok: bool) -> None:
        # TODO(me): decrement, and count a failure when not ok.
        raise NotImplementedError


async def fetch_all(
    get: Callable[[str], Awaitable[Any]],
    urls: Iterable[str],
    *,
    limit: int = 4,
    timeout: float = 10.0,
) -> tuple[list[Any], Budget]:
    """Fetch every url with at most `limit` in flight. Returns (results, budget).

    `get` is injected so the tests never touch a network (Principle 5).
    """
    # TODO(me): four things, and all four are compulsory (part 5.2):
    #
    #   1. asyncio.Semaphore(limit), created HERE not at module level
    #   2. asyncio.timeout INSIDE the semaphore - outside it, queued tasks time
    #      out before they ever start, which is part 5.2's second failure
    #   3. budget.finish() in a FINALLY, or a timeout leaves the count drifting
    #   4. gather(..., return_exceptions=True), so one failure keeps the rest
    #
    # Catch NOTHING. The exception travels out and gather turns it into a value
    # (Day 18, part 2.4). And do NOT retry - say in the docstring why that
    # belongs to the caller.
    raise NotImplementedError
```

**3. Decide, in writing, what `limit` should default to.** Two sentences in the docstring. The plan's
Part 2.1 gives the free tiers' shapes — "tens of RPM" for Gemini, "tight tokens-per-minute" for Groq — and
the default is a promise you are making on behalf of every caller who does not pass one (Principle 5). A
number chosen because it looked reasonable is the one that gets you blocked.

**4. Reproduce the ten traps in the notebook, then throw the notebook away.** In
`notebooks/day-19-scratch.ipynb`, in this order:

- Call a function annotated `-> int` with a string and watch it work
  ([1.1](parts/01-type-hints/1.1-a-hint-is-a-note.md)).
- Write `-> dict` on a function with a `return None` in it, then run `mypy` over it
  ([1.3](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md), [1.4](parts/01-type-hints/1.4-the-type-checker.md)).
- Write `tags: list[str] = []` in a dataclass and read the refusal
  ([2.2](parts/02-dataclasses/2.2-default-factory.md)).
- Put a list in a `frozen=True` dataclass, append to it, and try to hash it
  ([2.3](parts/02-dataclasses/2.3-frozen-slots-kw-only.md)).
- Build a Pydantic model from a dictionary of strings and print the types
  ([3.3](parts/03-pydantic/3.3-coercion-and-strict.md)).
- Hand `model_dump()` to `json.dumps` with a `datetime` field
  ([3.4](parts/03-pydantic/3.4-model-dump-and-the-boundary.md)).
- Time eight sleeps and eight loops with a thread pool, and compare the two ratios
  ([4.1](parts/04-concurrency/4.1-waiting-is-not-working.md)).
- Run the eight-thread ledger with a `time.sleep(0)` in the middle, three times
  ([4.3](parts/04-concurrency/4.3-threads.md)).
- Call an `async def` without awaiting it and check `bool()` on the result
  ([4.6](parts/04-concurrency/4.6-async-await.md)).
- Catch a `TaskGroup` failure with `except ValueError:` and read the tree
  ([4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md)).

**The notebook is not committed** (Principle 6); the two modules and their tests are.

**5. Write the phase decision record.** Principle 10 asks for one ADR per phase. One page, in
`docs/adr/`: what Module 2 chose and why — a base exception class rather than built-ins, `src/` layout,
Pydantic at boundaries and dataclasses inside, and the concurrency default. It is the document you would
defend in an interview, and §9 below is its first draft.

---

## §5 The eval that must be able to fail

Create `tests/test_models.py` and `tests/test_fetcher.py`. Every test runs offline, makes **zero**
requests, and belongs in `./m check`.

```python
"""Day 19: the contract must refuse, and the fetcher must respect its limit."""

from __future__ import annotations

import asyncio
import json

import pytest
from pydantic import ValidationError

from setu.errors import RateLimited
from setu.fetcher import fetch_all
from setu.models import Label, TriageResult


def test_a_good_reply_parses() -> None:
    """Part 3.5: the happy path, so a file of only-rejections cannot pass vacuously."""
    # TODO(me): model_validate_json on a well-formed reply. Assert label is
    # Label.BUG AND that it compares equal to the string 'bug' - the StrEnum
    # payoff, and the thing that breaks if somebody uses a plain Enum.
    raise NotImplementedError


def test_an_invented_label_is_rejected() -> None:
    """Part 3.5: the most common model failure."""
    # TODO(me): label='urgent'. Assert the error type is 'enum'. Assert on the
    # CODE, not the message (part 3.2).
    raise NotImplementedError


def test_a_confidence_of_95_is_rejected() -> None:
    """A model answering in percent, which happens."""
    # TODO(me): confidence=95. Without ge/le this is silently accepted and every
    # downstream threshold is wrong in the confident direction.
    raise NotImplementedError


def test_an_empty_reason_is_rejected() -> None:
    """Part 3.5: min_length is the bound people forget."""
    raise NotImplementedError


def test_a_renamed_field_is_rejected() -> None:
    """Part 3.1: extra='forbid', or a default silently replaces the answer."""
    # TODO(me): send 'certainty' instead of 'confidence'. Assert
    # 'extra_forbidden'. With the default extra='ignore' this test cannot exist.
    raise NotImplementedError


def test_the_result_cannot_be_edited() -> None:
    """Part 2.3: frozen, so nothing downstream adjusts a score."""
    raise NotImplementedError


def test_every_constraint_reaches_the_schema() -> None:
    """Part 3.5: the same class constrains the provider."""
    # TODO(me): model_json_schema(), then assert the confidence bounds and
    # additionalProperties=False are in it. This is the test that fails when
    # somebody moves a constraint into __post_init__-style code instead.
    raise NotImplementedError


def test_it_round_trips() -> None:
    """Part 3.4: what serialises must parse back."""
    # TODO(me): model_validate_json(x.model_dump_json()) == x.
    raise NotImplementedError


def test_the_fetcher_returns_one_result_per_url() -> None:
    """Part 4.7: gather promises ARGUMENT order, not completion order."""
    # TODO(me): a fake get that sleeps LONGER for earlier urls, so completion
    # order differs from argument order. Assert the results are in argument
    # order - a version using as_completed passes every other test here.
    raise NotImplementedError


def test_the_fetcher_never_exceeds_its_limit() -> None:
    """Part 5.2: the semaphore, proved by a counter rather than by a clock."""
    # TODO(me): 20 urls, limit=4, assert budget.concurrent_peak == 4. NOT a
    # timing assertion (part 5.3).
    raise NotImplementedError


def test_a_failure_comes_back_as_a_value() -> None:
    """Part 4.7: return_exceptions, so one bad url does not lose nineteen."""
    # TODO(me): one url raises RateLimited. Assert the OTHER results survived,
    # that results[i] is a RateLimited, and that its retry_after is intact
    # (Day 18, part 3.2).
    raise NotImplementedError


def test_a_slow_url_times_out_and_the_others_survive() -> None:
    """Part 4.8: the timeout, inside the semaphore."""
    # TODO(me): one url sleeps far longer than the timeout. Assert exactly one
    # TimeoutError and that every other result is fine.
    raise NotImplementedError


def test_the_budget_is_accurate_after_failures() -> None:
    """Part 5.2: finish() in a finally, or the counts drift."""
    # TODO(me): a mix of good, raising and slow urls. Assert requests equals the
    # url count and failures equals the bad count. A version without the finally
    # passes every other test in this file.
    raise NotImplementedError


def test_the_fetcher_makes_no_real_requests() -> None:
    """Principle 5: the whole suite has a request budget of zero."""
    # TODO(me): assert `httpx` is not imported by setu.fetcher - reuse Day 17's
    # internal_imports, or assert on the module's __dict__. Say in a comment why
    # dependency injection is what makes this assertion possible.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_models.py tests/test_fetcher.py -v
```

Then implement, then **break each one on purpose**:

- Change `label: Label` to `label: str`. **Only the invented-label test goes red**, and the schema test
  goes red too — say out loud which of those you would have noticed in review.
- Drop `ge=0.0, le=1.0`. Only the confidence test goes red, and `95` becomes a valid confidence.
- Drop `min_length=1`. Only the empty-reason test goes red.
- Change `extra="forbid"` to `"ignore"`. Only the renamed-field test goes red, and the model silently
  substitutes a default for the model's real answer.
- Remove `frozen=True`. Only the edit test goes red.
- Move `asyncio.timeout` **outside** the semaphore. **The limit test still passes**, and under enough URLs
  every queued task times out before starting — the failure that looks like an outage at the provider.
- Remove the `finally` around `budget.finish`. Only the budget-after-failures test goes red; the peak
  becomes larger than the limit, and the limit test may still pass on a fast machine.
- Change `return_exceptions=True` to the default. Two tests go red, and the message is the first
  exception rather than anything about the other nineteen.
- Replace `gather` with a loop of `await`s. **Only the limit test can see it** — every result is correct,
  in order, and it is twenty times slower.
- **Break it and watch every test stay GREEN** — replace the semaphore with nothing, **and** delete
  `test_the_fetcher_never_exceeds_its_limit`. Every remaining test passes: the results are right, the
  failures are values, the budget adds up, and the first real run fires two hundred requests at a provider
  that allows tens per minute. Restore the test, watch it go red, and say what it was protecting
  (Principle 5).

That last item is the most important line in this section. Every other test asserts something about the
answers; only one asserts something about what the answers cost.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — part 4.7's HTTP benchmark runs against a server started on `127.0.0.1` in the same process, and every test injects a fake `get` |
| New packages | **2** — `pydantic==2.13.5`, `httpx==0.28.1` |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |
| Disk | a few kilobytes in `tmp_path`, deleted by `pytest` |

Today is the day the budget becomes **enforceable rather than aspirational**. `Budget` in
[5.2](parts/05-the-gate/5.2-the-async-fetcher.md) is a returned value, so from Day 172 every fetch can
state its request count without anybody remembering to; and the semaphore is where the free tiers'
published limits (plan Part 2.1) live in code rather than in somebody's memory.

**On the pin.** Plan Part 2 recorded `pydantic==2.13.4` on 2026-08-21 and PyPI says `2.13.5` today. That
is patch drift, which `docs/PINS_DS.md` says to pin and log in `docs/CHANGELOG_PLAN_DS.md` — not a
Principle 14 stop. `httpx==0.28.1` is unchanged from the plan's table.

---

## §7 Traps

- **A hint is stored and never checked; `weigh("heavy")` runs** —
  [1.1](parts/01-type-hints/1.1-a-hint-is-a-note.md).
- **An annotation naming an undefined class is a `NameError` at import** —
  [1.1](parts/01-type-hints/1.1-a-hint-is-a-note.md).
- **A bare `tuple` or `list` says almost nothing** —
  [1.2](parts/01-type-hints/1.2-the-vocabulary.md).
- **`list[str]` on a parameter refuses a generator the code handles fine** —
  [1.2](parts/01-type-hints/1.2-the-vocabulary.md).
- **One `Any` disables checking for everything downstream of it** —
  [1.2](parts/01-type-hints/1.2-the-vocabulary.md).
- **`Optional[X]` means "may be None", never "may be omitted"** —
  [1.3](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md).
- **`if not value:` treats an empty collection as missing; use `is None`** —
  [1.3](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md).
- **`-> dict` on a function that returns `None` misleads every caller** —
  [1.3](parts/01-type-hints/1.3-optional-and-the-none-you-forgot.md).
- **A bare `# type: ignore` silences the next mistake on that line too** —
  [1.4](parts/01-type-hints/1.4-the-type-checker.md).
- **A checker cannot see past `Any`, so external data is unchecked** —
  [1.4](parts/01-type-hints/1.4-the-type-checker.md).
- **A field with no annotation is not a field — one colon decides** —
  [2.1](parts/02-dataclasses/2.1-what-dataclass-writes.md).
- **A dataclass with `__eq__` has `__hash__ = None` and cannot go in a set** —
  [2.1](parts/02-dataclasses/2.1-what-dataclass-writes.md).
- **A generated `__repr__` prints every field, including the API key** —
  [2.1](parts/02-dataclasses/2.1-what-dataclass-writes.md), [2.2](parts/02-dataclasses/2.2-default-factory.md).
- **`default_factory=list()` is not callable; it is `list`** —
  [2.2](parts/02-dataclasses/2.2-default-factory.md).
- **A factory returning a module-level object shares it anyway** —
  [2.2](parts/02-dataclasses/2.2-default-factory.md).
- **An instance of your own class as a default is hashable, so it is accepted and shared** —
  [2.2](parts/02-dataclasses/2.2-default-factory.md).
- **`frozen=True` is shallow: a list field is still mutable and still unhashable** —
  [2.3](parts/02-dataclasses/2.3-frozen-slots-kw-only.md).
- **`slots=True` only works if the whole inheritance chain has it** —
  [2.3](parts/02-dataclasses/2.3-frozen-slots-kw-only.md).
- **A frozen class cannot inherit from an unfrozen one** —
  [2.3](parts/02-dataclasses/2.3-frozen-slots-kw-only.md).
- **A computed field without `init=False` accepts and discards a caller's value** —
  [2.4](parts/02-dataclasses/2.4-post-init.md).
- **Computing before validating turns your message into a `ZeroDivisionError`** —
  [2.4](parts/02-dataclasses/2.4-post-init.md).
- **A subclass's `__post_init__` skips the parent's validation without `super()`** —
  [2.4](parts/02-dataclasses/2.4-post-init.md).
- **`frozen=True` blocks assignment from inside `__post_init__`** —
  [2.4](parts/02-dataclasses/2.4-post-init.md).
- **A dataclass accepts `Parcel(pid="seven", grams="heavy")` happily** —
  [2.5](parts/02-dataclasses/2.5-not-a-validator.md).
- **A dataclass field annotated as a model holds the raw dictionary** —
  [2.5](parts/02-dataclasses/2.5-not-a-validator.md).
- **A `BaseModel` constructor is keyword-only** —
  [3.1](parts/03-pydantic/3.1-the-model-that-refuses.md).
- **`dict()`, `json()`, `parse_obj()` are Pydantic v1 and are deprecated** —
  [3.1](parts/03-pydantic/3.1-the-model-that-refuses.md).
- **`extra="ignore"` is the default, so a renamed field becomes a silent default** —
  [3.1](parts/03-pydantic/3.1-the-model-that-refuses.md).
- **`errors()[0]` throws away the other three problems** —
  [3.2](parts/03-pydantic/3.2-validationerror.md).
- **`loc` is a tuple; `str(loc)` shows a user parentheses and quotes** —
  [3.2](parts/03-pydantic/3.2-validationerror.md).
- **`500.5` is refused for an `int` — losslessness, not strictness** —
  [3.3](parts/03-pydantic/3.3-coercion-and-strict.md).
- **A number is not coerced to a string; coercion is not symmetric** —
  [3.3](parts/03-pydantic/3.3-coercion-and-strict.md).
- **`strict=True` on a settings model rejects every environment variable** —
  [3.3](parts/03-pydantic/3.3-coercion-and-strict.md).
- **`json.dumps(model_dump())` raises on a `datetime` field** —
  [3.4](parts/03-pydantic/3.4-model-dump-and-the-boundary.md).
- **A secret needs `Field(exclude=True)` or `SecretStr`, not a remembered argument** —
  [3.4](parts/03-pydantic/3.4-model-dump-and-the-boundary.md).
- **Re-validating inside your own program costs two passes and tells you nothing** —
  [3.4](parts/03-pydantic/3.4-model-dump-and-the-boundary.md).
- **A new required field breaks every record written before today** —
  [3.5](parts/03-pydantic/3.5-triage-result.md).
- **Threads make CPU-bound code very slightly slower** —
  [4.1](parts/04-concurrency/4.1-waiting-is-not-working.md).
- **`process_time` reports zero for a program that only sleeps** —
  [4.1](parts/04-concurrency/4.1-waiting-is-not-working.md).
- **The GIL does not make threads safe** —
  [4.2](parts/04-concurrency/4.2-the-gil.md).
- **Lowering `setswitchinterval` makes threads dramatically slower** —
  [4.2](parts/04-concurrency/4.2-the-gil.md).
- **A read-modify-write can be interrupted, and the naive version passes its tests** —
  [4.3](parts/04-concurrency/4.3-threads.md).
- **A lock held across I/O serialises the whole pool** —
  [4.3](parts/04-concurrency/4.3-threads.md).
- **`start()` and `join()` in one loop is the sequential version** —
  [4.3](parts/04-concurrency/4.3-threads.md).
- **An exception in a raw thread prints and the exit code stays 0** —
  [4.3](parts/04-concurrency/4.3-threads.md).
- **A lambda cannot be sent to a worker process** —
  [4.4](parts/04-concurrency/4.4-processes.md).
- **No `if __name__ == "__main__":` gives `BrokenProcessPool` on Windows and macOS** —
  [4.4](parts/04-concurrency/4.4-processes.md).
- **Module-level state is invisible between parent and worker** —
  [4.4](parts/04-concurrency/4.4-processes.md).
- **Sending a large argument costs more than the work** —
  [4.4](parts/04-concurrency/4.4-processes.md).
- **`time.sleep` in a coroutine blocks every other coroutine** —
  [4.5](parts/04-concurrency/4.5-asyncio-one-thread.md).
- **`asyncio.run` inside a running loop is a `RuntimeError`** —
  [4.5](parts/04-concurrency/4.5-asyncio-one-thread.md).
- **A blocking client makes async code sequential with no error** —
  [4.5](parts/04-concurrency/4.5-asyncio-one-thread.md).
- **A coroutine object is truthy, so `if result:` cannot see a missing `await`** —
  [4.6](parts/04-concurrency/4.6-async-await.md).
- **The "never awaited" warning points at the wrong file** —
  [4.6](parts/04-concurrency/4.6-async-await.md).
- **`with` where `async with` was needed does not mention `async`** —
  [4.6](parts/04-concurrency/4.6-async-await.md).
- **`gather` re-raises the first failure and discards the good results** —
  [4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md).
- **`gather` does not limit concurrency; ten thousand means ten thousand** —
  [4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md).
- **A coroutine can only be awaited once** —
  [4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md).
- **A client per request is slower than one shared client** —
  [4.7](parts/04-concurrency/4.7-gather-and-twenty-fetches.md).
- **A bare `except:` swallows `CancelledError` and makes a task unstoppable** —
  [4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md).
- **A timeout cannot interrupt a coroutine that never awaits** —
  [4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md).
- **`except ValueError:` does not catch a `TaskGroup`'s `ExceptionGroup`** —
  [4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md).
- **Cleanup outside a `finally` is skipped on cancellation** —
  [4.8](parts/04-concurrency/4.8-timeouts-and-taskgroup.md).
- **Nesting a process pool over a threaded library multiplies workers** —
  [4.9](parts/04-concurrency/4.9-choosing.md).
- **The timeout outside the semaphore times out requests never sent** —
  [5.2](parts/05-the-gate/5.2-the-async-fetcher.md).
- **A fetcher that retries spends the caller's budget without asking** —
  [5.2](parts/05-the-gate/5.2-the-async-fetcher.md).
- **`pytest` does not run `async def` tests without a plugin** —
  [5.3](parts/05-the-gate/5.3-testing-async-code.md).
- **A timing assertion cannot tell concurrent from merely fast** —
  [5.3](parts/05-the-gate/5.3-testing-async-code.md).

---

## §8 Verify before you code

Fetched **2026-09-02**. Two pinned libraries and a lot of standard library, so the library reference, the
PEPs and the two projects' own documentation are the authority:

- <https://docs.python.org/3/library/typing.html> — the typing vocabulary, and the deprecation notes
  saying which `typing.X` names moved to built-ins or `collections.abc`.
- <https://peps.python.org/pep-0585/> — *PEP 585 — Type Hinting Generics In Standard Collections* (2020),
  which is why `list[str]` replaced `typing.List[str]`.
- <https://peps.python.org/pep-0604/> — *PEP 604 — Allow writing union types as X | Y* (2019).
- <https://docs.python.org/3/library/dataclasses.html> — `@dataclass`, every flag, `field()`, `InitVar`,
  and the `__post_init__` ordering.
- <https://docs.pydantic.dev/latest/> — Pydantic v2's own documentation. Check any tutorial you read
  against it: `model_` prefixes are v2, `parse_obj` is v1.
- <https://docs.pydantic.dev/latest/concepts/conversion_table/> — exactly which conversions lax and strict
  modes allow, per type. This is the page [3.3](parts/03-pydantic/3.3-coercion-and-strict.md) is a
  summary of.
- <https://docs.python.org/3/library/asyncio.html> — the whole asyncio reference, including the "Running
  Blocking Code" section that `to_thread` belongs to.
- <https://docs.python.org/3/library/asyncio-task.html> — `run`, `gather`, `create_task`, `timeout`,
  `TaskGroup`, and the cancellation rules.
- <https://docs.python.org/3/library/concurrent.futures.html> — `ThreadPoolExecutor` and
  `ProcessPoolExecutor`, and the note about what must be picklable.
- <https://peps.python.org/pep-0703/> — *PEP 703 — Making the Global Interpreter Lock Optional in CPython*
  (2023), for what the GIL is and where it is going.
- <https://www.python-httpx.org/async/> — `httpx`'s async client, and the reasons to reuse one.

---

## §9 Say it in an interview

> "Type hints are not enforced — the interpreter stores them in `__annotations__` and ignores them, so a
> function annotated `int` will happily take a string. What makes them worth writing is that other things
> read them: a type checker before the code runs, which catches wrong arguments at the **call site**
> rather than three frames away and, more usefully, unhandled `None`; and libraries that read them at run
> time. `dataclasses` reads them to generate `__init__`, `__repr__` and `__eq__`, which removes a class of
> bug where a hand-written `__eq__` forgets a field — and it deliberately does **not** check types, which
> is fine for records my own code builds and useless for data arriving from outside. That is where
> Pydantic goes: at the boundary, one model per external interface, converting where conversion is
> lossless — `'500'` becomes `500`, `500.5` is refused rather than truncated — and reporting **every**
> problem rather than the first, with a stable error code per field that I branch on instead of the
> message. Inside the program I use plain dataclasses, because re-validating data I just constructed costs
> time and tells me nothing. For concurrency the first thing I do is measure, not choose: processor time
> over wall time. Near zero means the program is waiting, and threads or asyncio help — threads for a
> handful because they are simpler, asyncio for hundreds because a coroutine costs a few hundred bytes
> where a thread costs a stack. Near one means it is working, and only processes help, because the GIL
> means one thread runs Python bytecode at a time; though the honest answer there is usually to move the
> loop into NumPy, which releases the GIL and is often a hundred times faster rather than four. The
> failure I have actually been bitten by is adding threads to something CPU-bound: no faster, and now it
> can race. On the async side, the shapes that matter are a semaphore, because `gather` has no throttle
> and will happily open ten thousand connections; a timeout **inside** the semaphore, because outside it
> you time out requests you never sent; `return_exceptions=True`, so one bad URL does not discard
> nineteen good results; and bookkeeping in a `finally`, because cancellation is the path that skips
> cleanup. And I test it with an injected fake client and assertions on recorded state — the peak
> in-flight count, the result types — never on elapsed time, because a timing assertion is flaky on a
> shared runner and cannot tell concurrent from merely fast."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, and **all twelve of
[5.1](parts/05-the-gate/5.1-the-gate-as-a-list.md)'s gate criteria are demonstrated by a test that has
been made to go red at least once**. Specifically: `TriageResult` refuses an invented label, a confidence
of 95, an empty reason and a renamed field; the fetcher's recorded peak equals its limit; a slow URL times
out while the others survive; the budget is accurate after failures; and you have **watched the whole
suite stay green with the semaphore removed** — in §5 — not when a particular amount of time has passed.
Then:

```bash
./m done 19
```

**That closes Phase 2 and Module 2.** Tomorrow is Day 20 and NumPy — arrays, vectorisation, and a world
where the loop you were about to write is one function call. Everything from Days 4 to 19 is assumed from
here: objects, containers, functions, iterators, classes, exceptions, modules, types and concurrency are
the language you will now write ML in rather than the subject.
