---
day: 9
phase: 1
phase_name: "Python foundations (Module 1)"
title: "Day 9 — List and dict comprehensions"
ids: ["PY-09"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P6 the notebook is a scratchpad", "P7 evals before features", "P16 depth over density", "P17 no clocks", "P18 zero to production"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 10
generated: "2026-08-25"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 9 — List and dict comprehensions

**Phase 1 · Python foundations · Module 1** · `PY-09` — list and dict comprehensions. The plan's named
example for this ID is *the same transform written as a loop and a comprehension; read both aloud*, and
the reading is the exercise: it is what tells you which form belongs.

> **Yesterday:** four containers, three questions that choose between them, and the measurement that
> makes "a set is faster" a number.
> **Today:** the same building, said in one line — plus the four boundaries where the one line is the
> wrong tool, and the one character that decides whether you hold a container or a stream.
> **Tomorrow:** functions, parameters and scope — where today's comprehensions become named, tested
> code in `src/setu/`.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Everybody has written themselves a note in a hurry and found it useless a week later.

> *milk bread eggs 2*

Two eggs? Two of everything? Is "2" a fourth item you have now forgotten? At the moment of writing it
was completely unambiguous, because the whole thought was in your head and the note was only a
prompt. A week on, the note is all that is left, and it is not enough.

Shorthand is a bargain: it saves the writer time and charges the reader. Usually that is a good
bargain, because most notes are read by the person who wrote them, five minutes later. It goes wrong
in exactly one situation — when the reader is somebody else, or is you after you have forgotten.

Today's tool is a very good shorthand for a very common loop. It is worth learning properly and using
often. It is also dense enough that a wrong word in the middle looks exactly like the right one, and
that is what the whole day is really about.

Six lines, all valid Python, all doing something slightly different from what a reader expects.

```text
[x if x > 0 else 0 for x in raw]        # keeps every row
[x for x in raw if x > 0]               # drops rows - and the denominator downstream did not change
[(r, c) for c in cols for r in rows]    # the loops are in the wrong order
{p["doi"]: p for p in papers}           # 10,000 papers in, 9,847 out, silently
[normalise(t) for t in titles if normalise(t)]   # normalise runs twice per title
sum([len(line) for line in handle])     # twenty million integers held to compute one number
```

Not one of them raises. The first two differ by moving five characters and produce lists of different
lengths. The third produces the right pairs in the wrong order. The fourth is a deduplication nobody
decided to perform. The fifth doubles the cost of the most expensive function in the pipeline. The
sixth is the difference between a job that finishes and one the kernel kills.

A comprehension compresses a loop into an expression, and compression is exactly what makes these
mistakes hard to see: the syntax is dense enough that a wrong `if`, a reversed clause order or a pair
of brackets looks like the right one. The whole day is learning to read them precisely —

- **the two `if`s**, which look identical and either filter or transform;
- **the clause order**, which reads outer-to-inner while the expression reads innermost-first;
- **the four containers**, chosen by a colon and a bracket;
- **the four boundaries** where a comprehension cannot go, and where a loop is the correct choice
  rather than a fallback.

The plan's exercise — write it both ways, read both aloud — is the technique that resolves all of it.
"Titles is the stripped title of each paper" is a sentence. If your comprehension is not a sentence, it
is a loop.

```mermaid
flowchart LR
    S1["§1 list comprehensions<br/>the shape · filter · the two ifs · nesting"] --> S2["§2 the other three<br/>dict · set · generator"]
    S2 --> S3["§3 when not to<br/>boundaries · scope · memory"]
    style S1 fill:#1f6feb,color:#fff
    style S3 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** One ID, so the sections follow the plan's `lab` split from
mechanism to production use: **1.x** is the list comprehension and everything its syntax can express;
**2.x** is the same syntax producing the other three results; **3.x** is where it stops being the right
tool — the boundaries, the scoping rule, and the memory decision.

### Section 1 — the list comprehension

| Part | What it answers | Level |
|---|---|---|
| [1.1 The loop and the comprehension, read aloud](parts/01-list-comprehensions/1.1-the-loop-and-the-comprehension.md) | What is the difference, in one spoken sentence each? | `foundation` |
| [1.2 The filter clause](parts/01-list-comprehensions/1.2-the-filter-clause.md) | Why does the filter make a failing conversion safe? | `foundation` |
| [1.3 The two `if`s that look identical](parts/01-list-comprehensions/1.3-the-two-ifs.md) | Which one changes the output length? | `working` |
| [1.4 Nested comprehensions](parts/01-list-comprehensions/1.4-nested-comprehensions.md) | Which `for` clause is the outer loop? | `working` |

### Section 2 — the other three results

| Part | What it answers | Level |
|---|---|---|
| [2.1 Dict comprehensions](parts/02-dict-set-gen/2.1-dict-comprehensions.md) | Why is building an index also a deduplication? | `working` |
| [2.2 Set comprehensions](parts/02-dict-set-gen/2.2-set-comprehensions.md) | What does `{f(x) for x in xs}` collapse that `set(xs)` does not? | `working` |
| [2.3 The generator expression](parts/02-dict-set-gen/2.3-the-generator-expression.md) | What does the parenthesis version give you instead of a tuple? | `production` |

### Section 3 — when the one line is wrong

| Part | What it answers | Level |
|---|---|---|
| [3.1 When a comprehension is the wrong tool](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md) | What does a fourteen-to-one refactor usually delete? | `production` |
| [3.2 Comprehension scope, and the walrus](parts/03-when-not-to/3.2-comprehension-scope.md) | Why does the walrus leak when the loop variable does not? | `production` |
| [3.3 The list you never needed](parts/03-when-not-to/3.3-the-list-you-never-needed.md) | Which one question decides between brackets and parentheses? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language plus `collections`, `itertools`, `tracemalloc`,
`time`, `tempfile` and `pathlib` from the standard library.

```bash
mkdir -p src/setu tests notebooks
touch src/setu/pipeline.py tests/test_pipeline.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-09-scratch.ipynb

# the four brackets, before any part names them (parts 1.1, 2.1, 2.2, 2.3)
uv run python -c "
xs = range(3)
print('[]', [x for x in xs])
print('{}', {x for x in xs})
print('{:}', {x: x for x in xs})
print('()', (x for x in xs), '<- NOT a tuple')
"

# the memory difference the day ends on (part 3.3)
uv run python -c "
import tracemalloc
for label, fn in (('list', lambda: sum([x for x in range(200_000)])), ('gen ', lambda: sum(x for x in range(200_000)))):
    tracemalloc.start(); fn(); _, peak = tracemalloc.get_traced_memory(); tracemalloc.stop()
    print(f'{label}: peak {peak:,} bytes')
"

# the rules that catch today's waste
uv run ruff rule C419
uv run ruff rule C416
```

| What | Where it comes from | Part |
|---|---|---|
| `[expr for x in it]` | language | [1.1](parts/01-list-comprehensions/1.1-the-loop-and-the-comprehension.md) |
| the filter clause | language | [1.2](parts/01-list-comprehensions/1.2-the-filter-clause.md) |
| the conditional expression in the value slot | language | [1.3](parts/01-list-comprehensions/1.3-the-two-ifs.md) |
| multiple `for` clauses, `itertools.chain.from_iterable` | language, standard library | [1.4](parts/01-list-comprehensions/1.4-nested-comprehensions.md) |
| `{k: v for ...}`, `collections.Counter` | language, standard library | [2.1](parts/02-dict-set-gen/2.1-dict-comprehensions.md) |
| `{expr for ...}`, `frozenset` | language, builtins | [2.2](parts/02-dict-set-gen/2.2-set-comprehensions.md) |
| `(expr for ...)`, `next(gen, default)`, `tracemalloc` | language, builtins, standard library | [2.3](parts/02-dict-set-gen/2.3-the-generator-expression.md) |
| `itertools.groupby`, `accumulate`, `defaultdict` | standard library | [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md) |
| the walrus `:=` | language | [3.2](parts/03-when-not-to/3.2-comprehension-scope.md) |
| `itertools.tee`, `sum(1 for ...)` | standard library, builtins | [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md) |
| ruff's `C400`–`C419` | already selected on [Day 2](../day-02-quality-gate/parts/01-linting/1.2-choosing-rule-families.md) | [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md), [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md) |

---

## §4 Build brief

One module, and it is the first one that assembles the previous three days into a pipeline.

**1. `src/setu/pipeline.py`** — the ingestion pipeline, built from
[Day 7's normaliser](../day-07-strings/parts/04-normalising/4.1-the-title-normaliser.md) and
[Day 8's containers](../day-08-containers/parts/03-dedup/3.2-order-preserving-dedup.md).

```python
"""The paper-ingestion pipeline: normalise, filter, deduplicate, index, report.

Every stage here is one comprehension or one loop, and the choice is deliberate
(day 9, part 3.1). Every stage that discards anything reports how much.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, NamedTuple

from setu.text import normalise_title


class StageCounts(NamedTuple):
    """What each stage saw and what it dropped. Part 1.2: a filter is a discard."""

    received: int
    kept: int

    @property
    def dropped(self) -> int:
        return self.received - self.kept


def normalised_keys(titles: Iterable[str]) -> list[str]:
    """The non-empty normalised keys, in first-seen order, calling normalise ONCE per title.

    Part 1.2 shows the double-call trap and part 3.2 the two fixes. Pick one and
    say in a comment which and why.
    """
    # TODO(me): one comprehension. If you use the walrus, choose a name that
    # could not collide with anything else in this module (part 3.2).
    raise NotImplementedError


def dedup_keys(keys: Iterable[str]) -> list[str]:
    """Distinct keys in first-seen order. O(n).

    Day 8 part 3.2 gives the one-liner. Say in a comment why it preserves order.
    """
    # TODO(me): one line.
    raise NotImplementedError


def index_by(records: Iterable[dict[str, Any]], field: str, keep: str = "first") -> dict[str, dict]:
    """A lookup keyed on `field`, keeping the first or the last occurrence.

    Part 2.1: building an index from a non-unique key IS a deduplication, so this
    function must be able to report how many records it dropped. Decide how -
    a second return value, a logged count, or a companion function - before you
    write the body, and say which in the docstring.
    """
    # TODO(me): 'last' is a one-line comprehension; 'first' is not. Work out why.
    raise NotImplementedError


def group_by_year(records: Iterable[dict[str, Any]]) -> dict[int, list[dict]]:
    """Group records by their year, preserving within-group order.

    Part 3.1, boundary 3: this CANNOT be a comprehension. Write the loop, and add
    a comment saying what a comprehension would produce instead.
    """
    # TODO(me): the loop. Return a plain dict if you use a defaultdict
    # (day 8, part 2.4).
    raise NotImplementedError


def parse_years(values: Iterable[str]) -> tuple[list[int], list[tuple[str, str]]]:
    """Parsed years, and the (value, reason) pairs that failed.

    Part 3.1, boundary 1: a comprehension has no `try`, so this is a loop - and
    the failure list is exactly what the comprehension version would have deleted.
    """
    # TODO(me): the loop. Keep the error MESSAGE, not just the value.
    raise NotImplementedError


def stream_lengths(lines: Iterable[str]) -> Iterator[int]:
    """The length of each line, lazily.

    Part 2.3: the annotation says Iterator, so the caller knows it is one-shot.
    """
    # TODO(me): one line, and it is not a list.
    raise NotImplementedError


def summarise(lines: Iterable[str]) -> tuple[int, int]:
    """The total length and the line count, in ONE pass and constant memory.

    Part 3.3: two aggregates over one stream. Two generator passes will not work
    on a one-shot source - work out why, and write the version that does.
    """
    # TODO(me): not a comprehension. Say in a comment why itertools.tee is not
    # the answer here either.
    raise NotImplementedError


def run(raw_titles: Iterable[str]) -> tuple[list[str], list[StageCounts]]:
    """The whole pipeline, with a StageCounts per stage.

    Part 3.1: the counts are the reason this is several one-line stages rather
    than one clever comprehension.
    """
    # TODO(me): normalise -> dedup, with a StageCounts after each. Two
    # comprehensions and two subtractions.
    raise NotImplementedError
```

**2. Rewrite three of yesterday's functions.** Open `src/setu/containers.py` from
[Day 8](../day-08-containers/LESSON.md) and convert `dedup_preserving_order`, `reconcile` and
`snapshot_keys` to comprehensions or one-liners where they are not already. **For each one, run the
existing test suite before and after** — an unchanged green suite is the proof the conversion was
behaviour-preserving. Leave `group_by` and `deep_merge` as loops, and add a one-line comment to each
saying which of [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md)'s boundaries applies.

**3. Reproduce all six story lines in the notebook, then throw the notebook away.** In
`notebooks/day-09-scratch.ipynb`: run the two `if` forms and compare the lengths; write the reversed
clause order and find the wrong pairs; build an index from a duplicated key and count what vanished;
count the calls in the double-`normalise` line; and measure the peak memory of `sum([...])` against
`sum(...)`. **The notebook is not committed** (Principle 6); `src/setu/pipeline.py` and its tests are.

---

## §5 The eval that must be able to fail

Create `tests/test_pipeline.py`. Everything runs offline; the memory test is marked slow.

```python
"""Day 9: prove the comprehension choices rather than assuming them."""

from __future__ import annotations

import pytest

from setu.pipeline import (
    dedup_keys,
    group_by_year,
    index_by,
    normalised_keys,
    parse_years,
    run,
    stream_lengths,
    summarise,
)


def test_normalised_keys_calls_normalise_once_per_title() -> None:
    """Part 1.2: the double-call trap."""
    # TODO(me): monkeypatch or wrap normalise_title with a counter and assert the
    # call count equals len(titles). The RESULT will be right either way, which
    # is exactly why the count is the assertion that matters.
    raise NotImplementedError


def test_normalised_keys_drops_blanks_and_says_how_many() -> None:
    """Part 1.2: a filter is a discard, and a discard is countable."""
    # TODO(me): assert the output AND that the caller can learn the drop count.
    raise NotImplementedError


def test_dedup_preserves_first_seen_order() -> None:
    """Day 8 part 3.2: the property a set throws away."""
    # TODO(me): assert the exact list. A length assertion passes for set() too.
    raise NotImplementedError


@pytest.mark.parametrize("keep", ["first", "last"])
def test_index_by_keeps_the_right_occurrence(keep: str) -> None:
    """Part 2.1: last-wins is one line and first-wins is not."""
    # TODO(me): two records sharing a key and DIFFERING in another field. Assert
    # the surviving record, and assert the key's POSITION is the first one's.
    raise NotImplementedError


def test_index_by_reports_what_it_dropped() -> None:
    """Part 2.1: building an index from a non-unique key is a silent dedup."""
    # TODO(me): whatever your build-brief decision was. This test IS that
    # decision, written down.
    raise NotImplementedError


def test_group_by_year_groups_rather_than_overwrites() -> None:
    """Part 3.1, boundary 3: what a comprehension would have produced instead."""
    # TODO(me): two records in the same year. Assert BOTH are present. Then, in
    # a comment, write what {r['year']: r for r in records} would have given.
    raise NotImplementedError


def test_parse_years_returns_both_the_good_and_the_bad() -> None:
    """Part 3.1, boundary 1: a comprehension has no try, and the failures matter."""
    # TODO(me): a mixed input. Assert the parsed list AND that each failure
    # carries its reason, not just its value.
    raise NotImplementedError


def test_stream_lengths_is_lazy() -> None:
    """Part 2.3: the annotation says Iterator; prove it."""
    # TODO(me): pass a generator whose 100th item would raise, take only the
    # first two, and assert nothing raised. That is the test a list version fails.
    raise NotImplementedError


def test_stream_lengths_is_consumed_once() -> None:
    """Part 2.3: the cost of laziness, asserted rather than assumed."""
    # TODO(me): iterate it fully, then again, and assert the second pass is
    # empty. Then answer in a comment: is that the behaviour we want here?
    raise NotImplementedError


def test_summarise_makes_one_pass_over_a_one_shot_source() -> None:
    """Part 3.3: two generator passes cannot work on a stream."""
    # TODO(me): pass a GENERATOR, not a list. A two-pass implementation returns
    # a count of 0 and does not raise - assert both numbers are right.
    raise NotImplementedError


@pytest.mark.slow
def test_summarise_memory_does_not_grow_with_the_input() -> None:
    """Part 3.3: the memory equivalent of day 8's ratio test."""
    # TODO(me): tracemalloc around summarise at n and 4n; assert the peak ratio
    # is under 2. A materialising implementation gives about 4.
    raise NotImplementedError


def test_run_reports_a_count_for_every_stage() -> None:
    """Part 3.1: the instrumentation a single clever comprehension deletes."""
    # TODO(me): assert received == kept + dropped for every stage, and that the
    # stages chain - each stage's received equals the previous stage's kept.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_pipeline.py -v
```

Then implement, then **break each one on purpose**:

- Rewrite `normalised_keys` as `[normalise_title(t) for t in titles if normalise_title(t)]` → **the
  result is identical and only the call-count test goes red.** That is the whole argument for asserting
  the count.
- Rewrite `index_by(keep="first")` as the last-wins comprehension → the parametrised test goes red for
  one parameter and passes for the other. Read which.
- Rewrite `group_by_year` as `{r["year"]: r for r in records}` → the grouping test goes red, and the
  **shape** of the result still looks plausible. Write down what it returned.
- Rewrite `stream_lengths` to return a list → the consumed-once test goes red **and** the laziness test
  goes red, for two different reasons. Name both.
- Rewrite `summarise` as two generator passes → **the memory test passes and the one-shot test returns a
  count of zero without raising.** Sit with that: the fast, low-memory implementation is silently wrong
  on exactly the input it was built for.

That last item is today's meeting of
[Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md) with
[2.3](parts/02-dict-set-gen/2.3-the-generator-expression.md): **laziness turns a correctness bug into a
plausible number rather than an exception**, and only a test that feeds it a genuine one-shot source can
tell.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — every input is generated locally or read from a scratch file |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |

The memory measurements in [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md) write a
temporary file to the system scratch directory and delete it.

---

## §7 Traps

- **A comprehension used for a side effect builds a list of `None`** —
  [1.1](parts/01-list-comprehensions/1.1-the-loop-and-the-comprehension.md).
- **Parentheses give a generator, not a tuple** —
  [1.1](parts/01-list-comprehensions/1.1-the-loop-and-the-comprehension.md).
- **A comprehension is a snapshot; later changes to the source are not seen** —
  [1.1](parts/01-list-comprehensions/1.1-the-loop-and-the-comprehension.md).
- **The filter runs BEFORE the expression** — which is what makes a guard work —
  [1.2](parts/01-list-comprehensions/1.2-the-filter-clause.md).
- **`[f(x) for x in xs if f(x)]` calls `f` twice per item** —
  [1.2](parts/01-list-comprehensions/1.2-the-filter-clause.md).
- **`isdigit()` rejects negatives and decimals** — a filter is a specification —
  [1.2](parts/01-list-comprehensions/1.2-the-filter-clause.md).
- **A filter is a discard, and an uncounted discard is silent data loss** —
  [1.2](parts/01-list-comprehensions/1.2-the-filter-clause.md).
- **The `if` before the `for` keeps every item; the one after drops items** —
  [1.3](parts/01-list-comprehensions/1.3-the-two-ifs.md).
- **The `else` is mandatory in the value slot and forbidden in the filter** —
  [1.3](parts/01-list-comprehensions/1.3-the-two-ifs.md).
- **Filtering one of two parallel sequences silently misaligns them** —
  [1.3](parts/01-list-comprehensions/1.3-the-two-ifs.md).
- **`for` clauses read left to right as outer to inner** —
  [1.4](parts/01-list-comprehensions/1.4-nested-comprehensions.md).
- **A filter guards the clause it follows; one clause too late is useless** —
  [1.4](parts/01-list-comprehensions/1.4-nested-comprehensions.md).
- **Two `for` clauses is O(n·m) in a syntax compact enough to hide it** —
  [1.4](parts/01-list-comprehensions/1.4-nested-comprehensions.md).
- **Building an index from a non-unique key is a deduplication** —
  [2.1](parts/02-dict-set-gen/2.1-dict-comprehensions.md).
- **A duplicate key keeps the LAST value at the FIRST one's position** —
  [2.1](parts/02-dict-set-gen/2.1-dict-comprehensions.md).
- **Inverting a dict collapses duplicate values and can raise** —
  [2.1](parts/02-dict-set-gen/2.1-dict-comprehensions.md).
- **A missing colon gives a set, not a dict** —
  [2.1](parts/02-dict-set-gen/2.1-dict-comprehensions.md).
- **`{k: [] for k in keys}` is not `dict.fromkeys(keys, [])`** —
  [2.1](parts/02-dict-set-gen/2.1-dict-comprehensions.md).
- **A set comprehension charges hashability loudly and order silently** —
  [2.2](parts/02-dict-set-gen/2.2-set-comprehensions.md).
- **`{normalise(t) for t in titles}` collapses more than `set(titles)` does** —
  [2.2](parts/02-dict-set-gen/2.2-set-comprehensions.md).
- **A generator has no length and no indexing** —
  [2.3](parts/02-dict-set-gen/2.3-the-generator-expression.md).
- **A generator is consumed once, and the second pass is silently empty** —
  [2.3](parts/02-dict-set-gen/2.3-the-generator-expression.md).
- **An exception inside a generator surfaces at the consumer** —
  [2.3](parts/02-dict-set-gen/2.3-the-generator-expression.md).
- **A generator's expression reads enclosing variables at CONSUMPTION time** —
  [2.3](parts/02-dict-set-gen/2.3-the-generator-expression.md).
- **A comprehension has no `try`, so per-item error handling needs a loop** —
  [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md).
- **Grouping is many-to-one and cannot be a comprehension** —
  [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md).
- **`itertools.groupby` needs its input sorted by the same key** —
  [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md).
- **A fourteen-to-one refactor usually deletes the instrumentation** —
  [3.1](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md).
- **A comprehension's loop variable does not leak; the walrus does** —
  [3.2](parts/03-when-not-to/3.2-comprehension-scope.md).
- **The leaked walrus value is the last COMPUTED one, not the last kept** —
  [3.2](parts/03-when-not-to/3.2-comprehension-scope.md).
- **`sum([...])` holds every item to compute one number** —
  [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md).
- **`any([...])` evaluates everything; `any(...)` stops at the first match** —
  [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md).
- **`itertools.tee` buffers what it defers, so two full passes cost the list you avoided** —
  [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md).

---

## §8 Verify before you code

Written **2026-08-25**. The language reference is the authority:

- <https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries> — the
  grammar for all four comprehension forms, including the clause-order rule and the note about the
  first iterable being evaluated in the enclosing scope.
- <https://docs.python.org/3/reference/expressions.html#generator-expressions> — generator expressions
  defined, including when the parentheses may be omitted.
- <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions> — the tutorial's version,
  which is the clearest introduction to nesting.
- <https://peps.python.org/pep-0572/> — the walrus operator, with the section on comprehension scope
  that [3.2](parts/03-when-not-to/3.2-comprehension-scope.md) paraphrases. The rationale is worth
  reading; it is unusually candid about the trade-offs.
- <https://docs.python.org/3/library/itertools.html> — `chain.from_iterable`, `groupby`, `accumulate`,
  `islice`, `tee`, each with a note on when it is the right tool.
- <https://docs.python.org/3/library/tracemalloc.html> — the allocation tracker
  [3.3](parts/03-when-not-to/3.3-the-list-you-never-needed.md) measures with.
- `uv run ruff rule C416`, `C417`, `C419` — the three comprehension rules, read from the linter you have
  installed rather than from memory.

---

## §9 Say it in an interview

> "A comprehension is an expression that builds a collection, so it says what the result *is* rather
> than describing the procedure that accumulates it — and because it is an expression it can go
> anywhere a value goes, which a `for` statement cannot. The syntax is the same for all four results:
> brackets give a list, braces give a set, braces with a colon give a dict, and parentheses give a
> generator rather than a tuple. The two things I read carefully are the `if`s and the clause order. An
> `if` before the `for` is a conditional expression that changes each item's value and keeps every one;
> an `if` after the `for` is a filter that drops items — so one preserves the length and one does not,
> and the `else` is the tell, because it is mandatory in the first and forbidden in the second. That
> matters because filtering one of two parallel sequences silently misaligns them. With two `for`
> clauses, they read left to right as outer to inner, and a filter guards the clause it follows, so a
> guard at the end is too late to protect the inner loop. The filter also runs before the expression,
> which is what lets it protect a conversion that would otherwise raise — but the filter cannot see the
> expression's result, so `[f(x) for x in xs if f(x)]` calls `f` twice and needs a walrus or a nested
> generator. Where I stop using one is the four boundaries: a body that needs a statement like a `try`
> for per-item errors, a side effect, an accumulation like grouping or a running total, or an
> expression that can no longer be read as a single sentence. And the last thing I check is the
> brackets: if the result is consumed once — summed, joined, searched, iterated — the parentheses
> version holds nothing, and for `any` and `all` it also stops at the first decisive item rather than
> evaluating everything."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, and you have **watched an
identical result come from a comprehension that calls its expensive function twice** — the case where
only the call count reveals the bug — not when a particular amount of time has passed. Then:

```bash
./m done 9
```

Tomorrow is functions, parameters, `*args`/`**kwargs` and scope — where the pipeline you built today
gets named, parameterised and tested as your first real `src/setu/` module.
