---
day: 9
phase: 1
phase_name: "Python foundations (Module 1)"
title: "List and dictionary comprehensions"
ids: ["PY-09"]
principles: ["P1 build daily", "P3 one concept one day", "P7 evals before features"]
kind: lab
plan: setu
plan_version: "v1.0.0"
generated: "2026-08-21"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 9 — List and dictionary comprehensions

**Phase 1 · Module 1** · ID: **PY-09**

> **Yesterday:** the four containers and the O(1) membership rule.
> **Today:** the syntax for building one container from another — and, more importantly, the
> discipline for knowing when *not* to.
> **Tomorrow:** functions, scope, and your first properly-structured `src/setu/` module.

```bash
./m start 9 && ./m scaffold 9
```

**Time:** 70 minutes. **Request budget:** 0 model calls.

---

## §1 The story

Almost every data operation is the same three moves: **take a collection, keep some of it, change
each item.** Filter and map. You will do it a hundred times before Day 240.

Written as a loop it is four lines with an accumulator and an `append`. Written as a comprehension it
is one line that reads left-to-right as a sentence:

```python
[clean(t) for t in titles if t]
#  ↑ what you get   ↑ source        ↑ keep only these
```

Read it as: *"clean(t), for each t in titles, where t is truthy."* Once that reads as a sentence
rather than as punctuation, you will find loops that only build a list slightly annoying to write.

There is a second, quieter reason comprehensions matter here. A comprehension creates a **new**
container and cannot accidentally mutate the source. Day 4's mutation bug is structurally impossible
inside one. When your Day-8 `unique` function needs to not touch the caller's list, a comprehension
is the shape that makes that free rather than careful.

**And the discipline.** A comprehension is for one filter and one transform. The moment you need two
conditions with different actions, or a `try`, or a running total, the loop is *clearer* and clearer
wins. There is no prize for one-lining. Nested triple comprehensions are how you write code that you
cannot read three weeks later.

---

## §2 Setup — run this

```bash
mkdir -p days/day-09/lab
touch days/day-09/lab/comprehensions.py
```

`src/setu/collections.py` and `textutils.py` grow today. No new packages.

---

## §3 PY-09 — the four forms

`days/day-09/lab/comprehensions.py`:

```python
"""PY-09: list, dict, set and generator comprehensions - and where the line is."""

from __future__ import annotations

import sys


def the_translation() -> None:
    titles = ["  Attention  ", "", "BERT", "   ", "GPT"]

    result = []
    for title in titles:
        if title.strip():
            result.append(title.strip().lower())
    print(f"\nloop:          {result}")

    result = [t.strip().lower() for t in titles if t.strip()]
    print(f"comprehension: {result}")


def all_four_forms() -> None:
    years = [2017, 2018, 2018, 2019]

    print(f"\nlist:      {[y + 1 for y in years]}")
    print(f"set:       {{y % 2 for y in years}} -> {({y % 2 for y in years})}")
    print(f"dict:      {({y: y - 2000 for y in years})}   <- later keys overwrite earlier")

    gen = (y + 1 for y in years)
    print(f"generator: {gen}")
    print(f"           consumed once -> {list(gen)}, then empty -> {list(gen)}")


def conditions() -> None:
    values = [4, -1, 0, 9, -3]

    print(f"\nfilter (no else):     {[v for v in values if v > 0]}")
    print(f"transform (with else): {[v if v > 0 else 0 for v in values]}")
    print(f"both:                  {[v * 2 if v > 5 else v for v in values if v != 0]}")


def nesting() -> None:
    pages = [["a", "b"], ["c"], [], ["d", "e"]]

    flat = [token for page in pages for token in page]
    print(f"\nflatten: {flat}   <- outer loop first, same order as nested for")

    grid = [[f"{r}{c}" for c in "xy"] for r in range(2)]
    print(f"nested:  {grid}   <- inner comprehension builds each row")


def memory() -> None:
    listcomp = [i for i in range(100_000)]
    genexp = (i for i in range(100_000))
    print(f"\nlist  : {sys.getsizeof(listcomp):>9,} bytes")
    print(f"genexp: {sys.getsizeof(genexp):>9,} bytes   <- holds a recipe, not the items")
    print(f"sum via generator: {sum(i for i in range(100_000)):,}")


def when_not_to() -> None:
    print("\nUse a loop when you need any of:")
    for reason in (
        "a try/except around the transform",
        "two conditions with different actions",
        "a running total or other state between items",
        "logging or a side effect",
        "more than about 80 characters on one line",
    ):
        print(f"  - {reason}")


if __name__ == "__main__":
    the_translation()
    all_four_forms()
    conditions()
    nesting()
    memory()
    when_not_to()
```

**Line by line:**

- `[t.strip().lower() for t in titles if t.strip()]` — the whole translation. `append` becomes the
  expression at the front; `if` moves to the back. Note `t.strip()` is computed twice here; §4's
  build brief asks you to avoid that.
- `{y % 2 for y in years}` — **braces with one expression** is a set comprehension. Deduplicated by
  construction.
- `{y: y - 2000 for y in years}` — **braces with a colon** is a dict comprehension. `2018` appears
  twice in `years`, and the later one silently wins. That is normal dict behaviour and it is a real
  source of quiet data loss when you build a lookup from a column with duplicates.
- `(y + 1 for y in years)` — **round brackets** make a generator expression. It computes nothing until
  iterated, and it is **consumed once**: the second `list(gen)` is empty. This trips everyone once.
  Day 11 covers generators properly.
- `[v for v in values if v > 0]` — the `if` at the **end** filters: items can be dropped.
- `[v if v > 0 else 0 for v in values]` — an `if/else` at the **front** is a conditional *expression*,
  part of the transform. Nothing is dropped; every item is transformed. **These are two different
  features that look similar**, and mixing them up is the most common comprehension error.
- `[token for page in pages for token in page]` — flattening. The `for` clauses appear in the **same
  order as nested loops**: outer first. Reading it right-to-left is why it confuses people; read the
  `for`s left to right and it is just an indentation-free nested loop.
- `sys.getsizeof` — the generator is a fixed small size regardless of range. It holds a recipe, not
  results. `sum(i for i in range(100_000))` never builds a list at all.
- `when_not_to` — read the five reasons out loud. They are the day's actual judgement content.

---

## §4 Build brief

Extend `src/setu/collections.py`:

```python
def group_by_first_letter(words: Iterable[str]) -> dict[str, list[str]]:
    """TODO(me): {first letter (lowercased): [words starting with it]}.

    Blank/whitespace-only entries are skipped. Order within each group is input order.
    A dict comprehension alone cannot do this - think about why, then choose.
    """
    raise NotImplementedError


def invert(mapping: dict[H, T]) -> dict[T, list[H]]:
    """TODO(me): {value: [keys that had it]}. Values may repeat, so each maps to a list."""
    raise NotImplementedError
```

And in `src/setu/textutils.py`:

```python
def clean_all(titles: Iterable[str | None]) -> list[str]:
    """TODO(me): normalise whitespace on each, drop the ones that end up blank.

    Reuse normalise_whitespace and is_blank - do NOT reimplement them.
    Compute each cleaned value ONCE (the §3 example carelessly computes it twice).
    """
    raise NotImplementedError
```

- `group_by_first_letter` is the exercise's point: a dict comprehension builds one entry per source
  item, so it cannot **accumulate** into a list. This is a case for a loop with `setdefault` — the
  discipline from §1, applied.
- `clean_all` computing each value once is the small craft detail. `walrus` (`:=`) is one way; a loop
  is another; a helper generator is a third. Any is fine — pick one and be able to defend it.

---

## §5 The eval that must be able to fail

Add to `tests/test_collections.py`:

```python
from setu.collections import group_by_first_letter, invert


def test_group_by_first_letter():
    assert group_by_first_letter(["apple", "avocado", "Banana", "  ", "cherry"]) == {
        "a": ["apple", "avocado"],
        "b": ["Banana"],
        "c": ["cherry"],
    }


def test_group_by_first_letter_preserves_input_order():
    assert group_by_first_letter(["zebra", "zulu", "zen"])["z"] == ["zebra", "zulu", "zen"]


def test_group_by_first_letter_of_empty():
    assert group_by_first_letter([]) == {}


def test_invert_collects_duplicate_values():
    assert invert({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}
```

And to `tests/test_textutils.py`:

```python
def test_clean_all_drops_blanks_and_normalises():
    assert tu.clean_all(["  a  b ", None, "   ", "c"]) == ["a b", "c"]


def test_clean_all_calls_normalise_once_per_item(monkeypatch):
    calls = []
    original = tu.normalise_whitespace

    def counting(text):
        calls.append(text)
        return original(text)

    monkeypatch.setattr(tu, "normalise_whitespace", counting)
    tu.clean_all(["  a  ", "  b  ", "   "])
    assert len(calls) == 3, f"normalise_whitespace ran {len(calls)} times for 3 items"
```

**Line by line:**

- `test_group_by_first_letter` — lowercased key, original casing preserved in the value (`"Banana"`).
  Two requirements in one assertion, and a naive `word[0]` fails the first.
- `test_group_by_first_letter_preserves_input_order` — a dict-of-sets implementation passes the
  membership check and fails this. Order is part of the contract.
- `test_invert_collects_duplicate_values` — a naive `{v: k for k, v in d.items()}` loses `"a"`,
  because `1` appears twice and the later key wins. **That is §3's silent-overwrite lesson, tested.**
- `test_clean_all_calls_normalise_once_per_item` — monkeypatches the helper with a counting wrapper.
  A double-computing implementation gives 6 and fails with a message that says so. This is how you
  test "how many times" rather than "what result", and you will reuse the pattern on Day 169 to count
  model calls.

```bash
uv run python -m pytest -q
```

---

## §6 Request budget

| Resource | Spent today |
|---|---|
| LLM calls | **0** |

---

## §7 Traps

- **Confusing the two `if` positions.** `if` at the end filters; `if/else` at the front transforms.
- **A dict comprehension over duplicate keys.** Silent data loss. Group into lists instead.
- **Reusing a generator expression.** Consumed once, then empty. Wrap in `list()` if you need it twice.
- **Computing the same expression twice** in the transform and the filter.
- **Flattening with the `for` clauses reversed.** Outer loop first, same as nested loops.
- **Nesting three deep** because it fits on one line. It fits; it does not read.
- **A comprehension with a side effect** (appending elsewhere, printing). Use a loop; a comprehension
  is for building a value.
- **Building a huge list to feed straight into `sum`/`max`/`any`.** Pass a generator expression.

---

## §8 Verify before you code

Written **2026-08-21**:

- <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions> — including the nested form.
- <https://docs.python.org/3/reference/expressions.html#displays-for-lists-sets-and-dictionaries> —
  the precise evaluation order of multiple `for` and `if` clauses.

---

## §9 Say it in an interview

> "Comprehensions are filter-and-map in one line, and the version I care about is that they build a
> new container, so they can't accidentally mutate the source. The two things people get wrong are
> the `if` position — trailing `if` filters, leading `if/else` transforms — and building a lookup with
> a dict comprehension over a column that has duplicates, where later entries silently overwrite
> earlier ones and you lose rows with no error. I group into lists for that. And I stop using them the
> moment I need a try/except or state between items; there's no prize for one-lining something a
> four-line loop says more clearly."

---

## §10 Done when

Tick [`CHECKLIST.md`](CHECKLIST.md), then `./m check && ./m done 9`.
