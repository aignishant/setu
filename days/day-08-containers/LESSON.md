---
day: 8
phase: 1
phase_name: "Python foundations (Module 1)"
title: "Day 8 — Lists, tuples, sets, dictionaries, and view objects"
ids: ["PY-07", "PY-08"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P16 depth over density", "P17 no clocks", "P18 zero to production"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 13
generated: "2026-08-25"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 8 — Lists, tuples, sets, dictionaries, and view objects

**Phase 1 · Python foundations · Module 1** · `PY-07` (lists and tuples) and `PY-08` (sets,
dictionaries, and dict view objects). The plan's named examples for these IDs are *why a coordinate is
a tuple and a to-do list is a list* and *de-duplicating 10 000 arXiv IDs in O(n) instead of O(n²) —
timed, both ways*, and both are built today.

> **Yesterday:** a string is code points rather than bytes, and a normaliser is six deliberate steps
> that turn nine spellings of one title into one key.
> **Today:** where those keys go. Four containers, three questions that choose between them, and the
> measurement that turns "a set is faster" from a belief into a number.
> **Tomorrow:** comprehensions — the same building, said in one line.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

A wedding needs two things at the door: a queue, and a coat check.

The queue is a painted line on the floor. Joining the back costs nothing. Taking somebody off the
front means everybody else shuffles up, which nobody notices with five people and takes longer than
the wedding with five hundred.

The coat check is a rail of numbered hooks. Handing in a coat and getting it back are both instant,
however many coats there are, because the ticket number says which hook. But nobody can tell you
which coat arrived third, because the coats were never arranged by arrival — they were arranged by
ticket.

Neither of those is better than the other. They are good at opposite things, and choosing wrongly
does not produce an error. It produces a very slow evening, or a coat rail that cannot answer the
question you turned out to need.

That is today. Four containers, each fast at some things and useless at others, and four bugs that
come entirely from picking one for a property it does not have.

Four bugs from four different files, all in the same week.

```text
queue.pop(0)                            # eleven minutes before the first job is processed
audit_copy = records[:]                 # the audit log shows the state after the change
top = list(set(ranked))[:20]            # twenty arbitrary papers, different every run
config = {**DEFAULTS, **site_config}    # the database section lost three of its four keys
```

The first is a list used as a queue, so every `pop(0)` shifts two hundred thousand pointers. The
second is a shallow copy, so the "backup" shares its dictionaries with the original. The third is a set
used where order mattered, so the ranking is gone and — because string hashing is randomised per
process — it is gone differently each run. The fourth is a shallow merge, so a nested section is
replaced rather than merged, and a connection timeout silently becomes "wait forever".

None of them raises. Every one of them is the same mistake: **a container was chosen for one property
and used for another.**

That is what today is about, and it reduces to three questions you ask before choosing:

- **Do I need a value per item?** → a dict.
- **Do I need order?** → not a set.
- **Do I need membership tests?** → not a list.

Everything else — why `append` is free and `insert(0, …)` is not, why a set cannot hold a list, why
`keys()` supports `&`, why `dict.fromkeys` deduplicates while keeping order — falls out of how these
four structures are actually built. And the day ends with the measurement that makes the choice
concrete: the same four lines, one word apart, timed at three sizes, with the ratio converging on 4
and on 2.

```mermaid
flowchart LR
    S1["§1 sequences<br/>list · slice · tuple · unpack · sort"] --> S2["§2 sets and dicts<br/>hash tables · algebra · views · merge"]
    S2 --> S3["§3 dedup<br/>10 000 IDs, timed both ways"]
    style S1 fill:#1f6feb,color:#fff
    style S3 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** Two IDs, so one section per ID plus a synthesis: **1.x** is
`PY-07` — the ordered sequences, how they are built and what that costs; **2.x** is `PY-08` — the hash
tables and the views onto them; **3.x** is where both meet, in the deduplication the plan names for
this day. Both containers rest on a published design — CPython's `listsort.txt` for the sort and
*PEP 456* for the hash — and each is cited inside the part that leans on it,
[1.5](parts/01-sequences/1.5-sort-sorted-and-key.md) and
[2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md).

### Section 1 — the ordered sequences (`PY-07`)

| Part | What it answers | Level |
|---|---|---|
| [1.1 A list is a dynamic array](parts/01-sequences/1.1-a-list-is-a-dynamic-array.md) | Why is `append` free and `pop(0)` not? | `foundation` |
| [1.2 Slicing, and the copy you did not notice](parts/01-sequences/1.2-slicing-and-the-copy-you-missed.md) | What exactly does `records[:]` copy? | `working` |
| [1.3 A tuple is a record](parts/01-sequences/1.3-a-tuple-is-a-record.md) | Why is a coordinate a tuple and a to-do list a list? | `working` |
| [1.4 Unpacking and `*rest`](parts/01-sequences/1.4-unpacking-and-star-rest.md) | Why is `a, b = b, a` safe without a temporary? | `working` |
| [1.5 `sort` vs `sorted`, `key=`, stability](parts/01-sequences/1.5-sort-sorted-and-key.md) | How do you sort by two fields in opposite directions? | `production` |

### Section 2 — the hash tables (`PY-08`)

| Part | What it answers | Level |
|---|---|---|
| [2.1 A set is a hash table](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md) | Why does membership not slow down as the set grows? | `foundation` |
| [2.2 Set algebra](parts/02-sets-and-dicts/2.2-set-algebra.md) | Which four operators replace which four nested loops? | `working` |
| [2.3 A dict is ordered now](parts/02-sets-and-dicts/2.3-a-dict-is-ordered-now.md) | What exactly does the ordering guarantee promise? | `foundation` |
| [2.4 `get`, `setdefault`, `defaultdict`, `Counter`](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md) | Which of the five modify the dict, and when? | `working` |
| [2.5 View objects are windows](parts/02-sets-and-dicts/2.5-view-objects-are-windows.md) | Why does a captured `keys()` show later changes? | `production` |
| [2.6 Merging dicts](parts/02-sets-and-dicts/2.6-merging-dicts.md) | Why did the nested config section lose three keys? | `working` |

### Section 3 — deduplication, where both sections meet

| Part | What it answers | Level |
|---|---|---|
| [3.1 Ten thousand identifiers, timed](parts/03-dedup/3.1-ten-thousand-ids-timed.md) | What ratio proves a function is quadratic? | `production` |
| [3.2 Order-preserving dedup](parts/03-dedup/3.2-order-preserving-dedup.md) | Which one-liner deduplicates *and* keeps the ranking? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language plus `collections`, `operator`, `sys`, `time`,
`random` and `subprocess` from the standard library.

```bash
mkdir -p src/setu tests notebooks
touch src/setu/containers.py tests/test_containers.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-08-scratch.ipynb

# the two facts the day rests on, before any part states them (parts 1.1, 2.1)
uv run python -c "import sys; d=[]; s=[sys.getsizeof(d)]; [ (d.append(i), s.append(sys.getsizeof(d))) for i in range(20) ]; print('list grows in jumps:', sorted(set(s)))"
uv run python -c "print('set order differs per process:', list({'nlp','vision','audio','robotics'}))"

# run that second command twice and compare the two lines (part 2.1)

# the rule that catches today's headline bug
uv run ruff rule B007
```

| What | Where it comes from | Part |
|---|---|---|
| `sys.getsizeof`, `collections.deque` | standard library | [1.1](parts/01-sequences/1.1-a-list-is-a-dynamic-array.md) |
| `copy.deepcopy`, slice assignment | standard library, language | [1.2](parts/01-sequences/1.2-slicing-and-the-copy-you-missed.md) |
| `typing.NamedTuple` | standard library | [1.3](parts/01-sequences/1.3-a-tuple-is-a-record.md) |
| `*rest` unpacking, `zip(*rows)` | language | [1.4](parts/01-sequences/1.4-unpacking-and-star-rest.md) |
| `sorted`, `key=`, `operator.itemgetter`, `heapq.nlargest` | builtins, standard library | [1.5](parts/01-sequences/1.5-sort-sorted-and-key.md) |
| `hash`, `frozenset`, `PYTHONHASHSEED` | builtins, environment | [2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md) |
| `&`, `\|`, `-`, `^`, `isdisjoint` | language, builtins | [2.2](parts/02-sets-and-dicts/2.2-set-algebra.md) |
| `dict.fromkeys`, `collections.OrderedDict` | builtins, standard library | [2.3](parts/02-sets-and-dicts/2.3-a-dict-is-ordered-now.md) |
| `defaultdict`, `Counter` | standard library | [2.4](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md) |
| `keys()`, `values()`, `items()` | builtins | [2.5](parts/02-sets-and-dicts/2.5-view-objects-are-windows.md) |
| `\|`, `{**a, **b}`, `update` | language, builtins | [2.6](parts/02-sets-and-dicts/2.6-merging-dicts.md) |
| `time.perf_counter`, `random.seed` | standard library | [3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md) |

---

## §4 Build brief

One module, and it is the one Day 9 rewrites as comprehensions and Day 11 rewrites as generators.

**1. `src/setu/containers.py`** — the container helpers, each with its complexity in its docstring.

```python
"""Container helpers whose complexity class is part of their contract.

Every function here states its cost in its docstring. If you cannot state the
cost, you have not finished designing it (day 8, part 3.1).
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Any, TypeVar

T = TypeVar("T")
K = TypeVar("K", bound=Hashable)


def dedup_preserving_order(items: Iterable[T]) -> list[T]:
    """Distinct items in first-seen order. O(n), one pass.

    Part 3.2 gives a one-liner for this. Write that one-liner, and add a comment
    saying WHY it preserves order - the reason is a language guarantee, not luck.
    """
    # TODO(me): one line. Then answer in a comment: what does it require of the
    # items, and what would you do if they were dicts?
    raise NotImplementedError


def dedup_by(items: Iterable[T], key: Callable[[T], K], keep: str = "first") -> list[T]:
    """Distinct items by `key(item)`, keeping the first or the last occurrence. O(n).

    Part 3.2: 'first' and 'last' are different requirements, not preferences.
    """
    # TODO(me): decide what `keep` values you accept and what an unknown one does
    # BEFORE writing the body (day 5, part 2.1's exhaustiveness). Both branches
    # must preserve first-seen POSITION - work out why that is not automatic.
    raise NotImplementedError


def reconcile(left: Iterable[K], right: Iterable[K]) -> dict[str, set[K]]:
    """Both directions of difference plus the overlap. O(n + m).

    Returns {"left_only": ..., "right_only": ..., "both": ...}. Part 2.2 explains
    why reporting only the symmetric difference is half a result.
    """
    # TODO(me): three set operations. Do NOT write a loop.
    raise NotImplementedError


def group_by(items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Group items by key, preserving within-group order. O(n).

    Part 2.4 gives four ways to write this. Pick one and say why in a comment -
    and if you pick defaultdict, return a PLAIN dict (part 2.4's hazard).
    """
    # TODO(me): one loop, one lookup per item.
    raise NotImplementedError


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge `override` into `base`, returning a NEW dict.

    Part 2.6 names FOUR decisions this has to make. Write all four in this
    docstring before writing the body. The decisions are the deliverable.
    """
    # TODO(me): the four decisions, then about fifteen lines. Do not mutate `base`.
    raise NotImplementedError


def snapshot_keys(mapping: dict[K, Any]) -> set[K]:
    """A STABLE set of the mapping's keys, unaffected by later changes.

    Part 2.5: the one-word difference between this and a live view.
    """
    # TODO(me): one line, and the annotation already tells you which one.
    raise NotImplementedError


def top_n(items: Sequence[T], n: int, key: Callable[[T], Any]) -> list[T]:
    """The n highest items by `key`, with a deterministic tie-break. O(n log n).

    Part 1.5: a sort feeding a report needs a TOTAL key or the output is
    non-deterministic. Part 3.1 mentions a cheaper option for small n - name it
    in a comment and say why you did or did not use it.
    """
    # TODO(me): the tie-break is the exercise, not the sort.
    raise NotImplementedError
```

**2. Build the benchmark yourself.** `src/setu/benchmark.py` with a `ratio_test(fn, sizes, make_input)`
that runs a function at several sizes and returns the consecutive ratios
([3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md)). It must generate the input **outside** the timed
region, take the **minimum** of several runs, and pin the random seed (Principle 4). You will import
this on Day 9, Day 11 and Day 20.

**3. Reproduce all four story bugs in the notebook, then throw the notebook away.** In
`notebooks/day-08-scratch.ipynb`: time `list.pop(0)` against `deque.popleft()` at two sizes; make an
"audit copy" with `[:]` and watch it change; print `list(set(...))` in two separate processes and
compare; and merge a nested config shallowly and count the keys that vanished. **The notebook is not
committed** (Principle 6); `src/setu/containers.py` and its tests are.

---

## §5 The eval that must be able to fail

Create `tests/test_containers.py`. Everything runs offline; the ratio test is marked slow.

```python
"""Day 8: prove the container choices rather than assuming them."""

from __future__ import annotations

import pytest

from setu.benchmark import ratio_test
from setu.containers import (
    dedup_by,
    dedup_preserving_order,
    deep_merge,
    group_by,
    reconcile,
    snapshot_keys,
    top_n,
)


def test_dedup_preserves_first_seen_order() -> None:
    """Part 3.2: the property `set` throws away."""
    # TODO(me): assert the exact output list for a ranked input, not just its
    # length. A length assertion passes for set() too, which is the whole point.
    raise NotImplementedError


def test_dedup_is_linear_not_quadratic() -> None:
    """Part 3.1: the only test that can go red for a complexity bug."""
    # TODO(me): use ratio_test at n, 2n, 4n and assert every ratio is under 3.
    # A list-based implementation gives about 4. Mark this @pytest.mark.slow
    # (day 2, part 3.3) and say in a comment why 3 and not 2.
    raise NotImplementedError


@pytest.mark.parametrize("keep", ["first", "last"])
def test_dedup_by_keeps_the_right_occurrence(keep: str) -> None:
    """Part 3.2: two correct implementations that disagree."""
    # TODO(me): two records sharing a key and DIFFERING in another field, so the
    # two modes give visibly different answers. Assert the position too.
    raise NotImplementedError


def test_dedup_by_rejects_an_unknown_keep() -> None:
    # TODO(me): whatever your build-brief decision was. If it silently defaults,
    # this test asserts that and the comment defends it.
    raise NotImplementedError


def test_reconcile_reports_both_directions() -> None:
    """Part 2.2: reporting only the symmetric difference is half a result."""
    # TODO(me): assert all three keys, including that "both" is non-empty.
    raise NotImplementedError


def test_group_by_returns_a_plain_dict() -> None:
    """Part 2.4: a defaultdict that escapes grows when anyone probes it."""
    # TODO(me): assert type(result) is dict, then probe a missing key and assert
    # len() did not change. That second assertion is the one that catches it.
    raise NotImplementedError


def test_deep_merge_keeps_sibling_keys() -> None:
    """Part 2.6: the shallow merge that lost three of four keys."""
    # TODO(me): a nested section where the override sets ONE field. Assert the
    # other three survive - and assert the shallow `{**a, **b}` version does NOT,
    # so the test proves there was a bug to fix.
    raise NotImplementedError


def test_deep_merge_does_not_mutate_its_inputs() -> None:
    """Part 1.2: a function that edits its caller's data has a contract nobody reads."""
    # TODO(me): assert the base dict is unchanged AFTER the merge, including its
    # nested sections. Use `is` on a nested dict to check what is shared.
    raise NotImplementedError


def test_deep_merge_raises_on_a_shape_mismatch() -> None:
    """Part 2.6, decision 3: a dict where a scalar was expected."""
    # TODO(me): assert TypeError and that the message names the key.
    raise NotImplementedError


def test_snapshot_keys_is_not_a_live_view() -> None:
    """Part 2.5: the audit log that recorded post-change state."""
    # TODO(me): snapshot, mutate the dict, assert the snapshot did not change.
    # Then assert that mapping.keys() DID - both halves, or the test proves nothing.
    raise NotImplementedError


def test_top_n_is_deterministic_across_tie_breaks() -> None:
    """Part 1.5: a sort feeding a report needs a total key."""
    # TODO(me): build input with several equal scores, shuffle it with a PINNED
    # seed, and assert the same output for two different shuffles. A key without
    # a tie-break fails this.
    raise NotImplementedError


def test_top_n_with_n_larger_than_the_input() -> None:
    # TODO(me): decide what n > len(items) does, and assert it.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_containers.py -v
```

Then implement, then **break each one on purpose**:

- Change `dedup_preserving_order` to `list(set(items))` → **the order test goes red and the linearity
  test still passes.** Both are correct implementations of "deduplicate"; only one is correct here.
- Change it to the `seen = []` loop → **the order test still passes and only the ratio test goes red.**
  Sit with that pair: the two tests catch disjoint bugs and neither can catch the other's.
- Make `group_by` return the `defaultdict` directly → the plain-dict test goes red on the **second**
  assertion, not the first. Read why.
- Make `deep_merge` shallow → the sibling-keys test goes red **and** the mutation test may still pass.
  A merge can be wrong without mutating anything.
- Remove the tie-break from `top_n` → the determinism test goes red **intermittently**, depending on the
  shuffle. Pin a second seed and make it fail reliably; a flaky test for a real bug is still a bug.

That second item is today's meeting of
[Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md) with
[3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md): **a correctness test cannot see a complexity bug
and a complexity test cannot see a correctness bug.** You need both, and most codebases have only the
first.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — every input is generated locally |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |

[3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md)'s benchmark runs locally and the only subprocess is
a second Python interpreter printing a set, used to show that hash randomisation differs between
processes ([2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md)).

---

## §7 Traps

- **`list.pop(0)` and `insert(0, x)` shift every element** — use a `deque` —
  [1.1](parts/01-sequences/1.1-a-list-is-a-dynamic-array.md).
- **A list of a million integers is far more than eight megabytes** — the integers are separate objects
  — [1.1](parts/01-sequences/1.1-a-list-is-a-dynamic-array.md).
- **`deque` indexing in the middle is O(n)** — it is a queue, not a sequence —
  [1.1](parts/01-sequences/1.1-a-list-is-a-dynamic-array.md).
- **`records[:]` copies the list and shares the elements** —
  [1.2](parts/01-sequences/1.2-slicing-and-the-copy-you-missed.md).
- **`items[:] = other` mutates in place; `items = other` rebinds** —
  [1.2](parts/01-sequences/1.2-slicing-and-the-copy-you-missed.md).
- **A strided slice assignment must match length exactly** —
  [1.2](parts/01-sequences/1.2-slicing-and-the-copy-you-missed.md).
- **`(3)` is an integer; the comma makes the tuple** —
  [1.3](parts/01-sequences/1.3-a-tuple-is-a-record.md).
- **`(1, [2])` is unhashable** — immutability must go all the way down —
  [1.3](parts/01-sequences/1.3-a-tuple-is-a-record.md).
- **Building a tuple with `t = t + (x,)` in a loop is quadratic** —
  [1.3](parts/01-sequences/1.3-a-tuple-is-a-record.md).
- **`*rest` is always a list, even from a tuple** —
  [1.4](parts/01-sequences/1.4-unpacking-and-star-rest.md).
- **Unpacking targets bind left to right**, so `i, v[i] = 1, 99` uses the new `i` —
  [1.4](parts/01-sequences/1.4-unpacking-and-star-rest.md).
- **A failed unpack of a generator leaves it partially consumed** —
  [1.4](parts/01-sequences/1.4-unpacking-and-star-rest.md).
- **`list.sort()` returns `None`** — [1.5](parts/01-sequences/1.5-sort-sorted-and-key.md).
- **One `None` in a sort key raises, at the end of the job** —
  [1.5](parts/01-sequences/1.5-sort-sorted-and-key.md).
- **`sorted(["10", "9"])` puts `"10"` first and does not raise** —
  [1.5](parts/01-sequences/1.5-sort-sorted-and-key.md).
- **A sort without a tie-break is non-deterministic when the input order is** —
  [1.5](parts/01-sequences/1.5-sort-sorted-and-key.md).
- **`{}` is an empty dict; the empty set is `set()`** —
  [2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md).
- **`{1, True, 1.0}` has one element** —
  [2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md).
- **Set order is randomised per process** — never let it reach an output —
  [2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md).
- **A mutable object with a custom `__hash__` becomes unreachable when it changes** —
  [2.1](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md).
- **`known | some_list` raises; `known.union(some_list)` does not** —
  [2.2](parts/02-sets-and-dicts/2.2-set-algebra.md).
- **`set().union("abc")` adds three characters** —
  [2.2](parts/02-sets-and-dicts/2.2-set-algebra.md).
- **`&` binds tighter than `|`** — [2.2](parts/02-sets-and-dicts/2.2-set-algebra.md).
- **`result = result | batch` in a loop is quadratic; `result |= batch` is not** —
  [2.2](parts/02-sets-and-dicts/2.2-set-algebra.md).
- **Deleting and re-inserting a dict key moves it to the end; updating does not** —
  [2.3](parts/02-sets-and-dicts/2.3-a-dict-is-ordered-now.md).
- **`dict.fromkeys(keys, [])` shares one list across every key** —
  [2.3](parts/02-sets-and-dicts/2.3-a-dict-is-ordered-now.md).
- **JSON round-trips turn non-string keys into strings, silently** —
  [2.3](parts/02-sets-and-dicts/2.3-a-dict-is-ordered-now.md).
- **`d.get(k, default)` returns a stored `None`, not the default** —
  [2.4](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md).
- **`d.setdefault(k, expensive())` runs `expensive()` on every call** —
  [2.4](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md).
- **Reading `d[k]` on a `defaultdict` inserts the key** —
  [2.4](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md).
- **`Counter` subtraction drops zero and negative counts** —
  [2.4](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md).
- **A view is live, not a snapshot** —
  [2.5](parts/02-sets-and-dicts/2.5-view-objects-are-windows.md).
- **`d.keys()[0]` raises** — a view is iterable, not a sequence —
  [2.5](parts/02-sets-and-dicts/2.5-view-objects-are-windows.md).
- **`values()` is not set-like, and `items()` only when the values are hashable** —
  [2.5](parts/02-sets-and-dicts/2.5-view-objects-are-windows.md).
- **Every dict merge is shallow** — a nested section is replaced, not merged —
  [2.6](parts/02-sets-and-dicts/2.6-merging-dicts.md).
- **`config = defaults.update(overrides)` is `None`** —
  [2.6](parts/02-sets-and-dicts/2.6-merging-dicts.md).
- **A merged dict shares its nested values with the originals** —
  [2.6](parts/02-sets-and-dicts/2.6-merging-dicts.md).
- **A single timing tells you nothing; the ratio does** —
  [3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md).
- **Generating the input inside the timed region measures the wrong thing** —
  [3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md).
- **Switching from list to set can turn a working dedup into `TypeError: unhashable`** —
  [3.1](parts/03-dedup/3.1-ten-thousand-ids-timed.md).
- **A fast dedup on unnormalised keys is a fast wrong answer** —
  [3.2](parts/03-dedup/3.2-order-preserving-dedup.md).
- **`{r[key]: r for r in records}` keeps the LAST record at the FIRST one's position** —
  [3.2](parts/03-dedup/3.2-order-preserving-dedup.md).

---

## §8 Verify before you code

Written **2026-08-25**. The language reference and the standard library docs are the authority:

- <https://docs.python.org/3/tutorial/datastructures.html> — the tutorial chapter covering all four
  containers, worth reading start to finish once.
- <https://wiki.python.org/moin/TimeComplexity> — **the cost table for every list, set and dict
  operation.** Sections 1 and 2 of today are a subset of this page; read the whole thing.
- <https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset> — the set operations, with
  the operator/method distinction stated explicitly.
- <https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects> — views, in the language's
  own words, including which are set-like.
- <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict> — and the note recording that
  insertion order became a guarantee in 3.7.
- <https://docs.python.org/3/library/collections.html> — `deque`, `defaultdict`, `Counter`,
  `OrderedDict`, each with a "when to use this" paragraph.
- <https://docs.python.org/3/howto/sorting.html> — the official Sorting HOWTO: `key=`, stability, and
  the decorate-sort-undecorate idiom.
- <https://docs.python.org/3/library/heapq.html#heapq.nlargest> — the cheaper top-N that
  [1.5](parts/01-sequences/1.5-sort-sorted-and-key.md) mentions.
- <https://docs.python.org/3/using/cmdline.html#envvar-PYTHONHASHSEED> — hash randomisation, and why it
  exists.

---

## §9 Say it in an interview

> "The four containers are the same three questions: do I need a value per item, do I need order, and
> do I need membership tests. A list is a dynamic array of pointers with spare capacity at the end, so
> indexing and appending are O(1) and anything at the front shifts everything — which is why a queue
> built on `pop(0)` is quadratic and `collections.deque` is O(1) at both ends. A set and a dict are
> hash tables: they compute a number from the value and go straight to a slot, so membership does not
> slow down as they grow. That speed is the same property as the two costs — elements must be hashable,
> because the hash must not change while the item is stored, and there is no order, because a slot is
> not a position. For strings the hash is randomised per process as a denial-of-service defence, so a
> report built by iterating a set comes out differently every run. Dicts are the exception: since 3.7
> insertion order is a language guarantee, which is why `list(dict.fromkeys(items))` is the
> order-preserving deduplicator and why a dict with ignored values is Python's ordered set. The
> mistakes I look for in review are a list used for membership, which is the accidental quadratic; a
> `[:]` copy treated as a backup when it shares the elements; a set used where order mattered; and a
> dict merge treated as deep when every form of it is shallow, so a nested config section gets
> replaced rather than merged. And the way I settle any of those arguments is to time it at n, 2n and
> 4n and read the ratio — 2 is linear, 4 is quadratic, the seconds are machine-specific and the ratio
> is not."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, and you have **watched the
ratio column converge on 4 and on 2 with your own hands** — not read that it would — not when a
particular amount of time has passed. Then:

```bash
./m done 8
```

Tomorrow is comprehensions: the same grouping, filtering and building written in one line, including
the two `if`s that look identical and mean completely different things.
