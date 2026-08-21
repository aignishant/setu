---
day: 5
phase: 1
phase_name: "Python foundations (Module 1)"
title: "Operators, precedence, and conditionals"
ids: ["PY-03", "PY-04"]
principles: ["P1 build daily", "P7 evals before features"]
kind: lab
plan: setu
plan_version: "v1.0.0"
generated: "2026-08-21"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 5 — Operators, precedence, and conditionals

**Phase 1 · Module 1** · IDs: **PY-03** (operators, precedence), **PY-04** (conditionals, truthiness)

> **Yesterday:** objects, and the mutable/immutable split.
> **Today:** `is` vs `==` — which is yesterday's lesson wearing an operator — plus precedence, and
> the truthiness rule that will bite you on Day 26 with a DataFrame.
> **Tomorrow:** loops, and the capped retry that every agent loop in Phase 21 is shaped like.

```bash
./m start 5 && ./m scaffold 5
```

**Time:** 75 minutes. **Request budget:** 0 model calls.

---

## §1 The story

Yesterday you learned that a variable is a label on an object, and that two labels can point at one
object. Today that fact grows an operator.

- `==` asks: **do these two objects have the same value?**
- `is` asks: **are these two labels pointing at the same object?**

Those are different questions, and Python will happily answer either. The trap is that for small
integers and short strings, CPython caches objects — so `a = 256; b = 256; a is b` is `True`, and
`a = 257; b = 257; a is b` is `False`. Same code shape, different answer, because of an
implementation detail you should never build on.

**The rule is simple and it has exactly one exception:** use `==` for values. Use `is` only for
singletons — `None`, `True`, `False`.

The second half of today is **truthiness**: what Python considers true when you write `if x:`. Empty
things are false. Zero is false. `None` is false. Everything else is true — *unless the object's
class says otherwise*, which is where pandas comes in, because a DataFrame refuses to answer the
question at all and raises instead. That refusal is a feature, and knowing why on Day 5 saves you
twenty minutes on Day 26.

---

## §2 Setup — run this

```bash
mkdir -p days/day-05/lab
touch days/day-05/lab/operators.py
```

`src/setu/textutils.py` and its test file already exist from Day 4 — today extends both.
No new packages.

---

## §3 PY-03 — `is` vs `==`, and precedence

`days/day-05/lab/operators.py`:

```python
"""PY-03: identity, equality, and the order operations actually happen in."""

from __future__ import annotations


def identity_vs_equality() -> None:
    a, b = 256, 256
    c, d = 257, 257
    print(f"{a == b=}  {a is b=}   <- small ints are cached")
    print(f"{c == d=}  {c is d=}   <- and 257 is not. never rely on this.")

    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    print(f"\n{x == y=}  {x is y=}   <- equal values, two objects")
    print(f"{x == z=}  {x is z=}   <- one object, two labels")


def the_only_correct_use_of_is() -> None:
    value = None
    print(f"\n{value is None=}   <- correct")
    print(f"{value == None=}   <- works, but a class could lie about __eq__")


def precedence() -> None:
    print(f"\n{2 + 3 * 4=}          <- * before +")
    print(f"{(2 + 3) * 4=}")
    print(f"{2 ** 3 ** 2=}         <- ** is RIGHT associative: 2**(3**2)")
    print(f"{-2 ** 2=}             <- ** binds tighter than unary minus")
    print(f"{True or False and False=}  <- and before or")
    print(f"{(True or False) and False=}")


def short_circuit() -> None:
    def loud(name: str, value: bool) -> bool:
        print(f"    evaluated {name}")
        return value

    print("\nand: stops at the first falsy")
    loud("A", False) and loud("B", True)
    print("or: stops at the first truthy")
    loud("C", True) or loud("D", True)


if __name__ == "__main__":
    identity_vs_equality()
    the_only_correct_use_of_is()
    precedence()
    short_circuit()
```

**Line by line:**

- `a, b = 256, 256` — tuple unpacking; two assignments on one line. `a is b` prints `True` because
  CPython pre-allocates small integers. `257` is outside that cache. **This is not a language rule.**
  It is a detail of one implementation, and the point of showing it is so you never write code that
  depends on it.
- `x == y` is `True` while `x is y` is `False` — two distinct lists holding equal values. This is
  Day 4's diagram with operators attached.
- `value == None` — works, but a class can override `__eq__` to return anything. `is None` compares
  identity against the one and only `None` object and cannot be fooled.
- `2 ** 3 ** 2` is `512`, not `64` — `**` is the one arithmetic operator that groups **right to
  left**. Write the brackets.
- `-2 ** 2` is `-4` — `**` binds tighter than the unary minus, so it reads as `-(2**2)`. This one
  costs people real time in statistics code on Day 60.
- `and` before `or` — the same precedence relationship as `*` before `+`. When in doubt, bracket; a
  bracket costs two characters and saves a bug.
- `loud("A", False) and loud("B", True)` — **`B` never prints.** `and` stops at the first falsy value
  and returns it. `or` stops at the first truthy one. That is **short-circuiting**, and it is not a
  performance trick — it is the reason `if user is not None and user.name:` is safe. Reverse those
  two clauses and you get an `AttributeError`.

---

## §4 PY-04 — truthiness

Add to the same file:

```python
def truthiness() -> None:
    falsy = [False, None, 0, 0.0, "", [], {}, set(), ()]
    for value in falsy:
        assert not value, f"{value!r} should be falsy"
    print(f"\nall falsy: {[repr(v) for v in falsy]}")

    truthy = ["0", "False", [0], {0: 0}, -1, 0.1]
    for value in truthy:
        assert value, f"{value!r} should be truthy"
    print(f"all truthy: {[repr(v) for v in truthy]}")


def the_pandas_trap() -> None:
    print("\n-- what breaks on Day 26 --")
    print("  if df:            -> ValueError: truth value of a DataFrame is ambiguous")
    print("  if len(df):       -> correct: 'does it have rows'")
    print("  if not df.empty:  -> clearer: says what you mean")
```

**Line by line:**

- The `falsy` list — memorise this set. **Empty containers, zero, empty string, `None`, `False`.**
  That is all of it.
- `"0"` and `"False"` are **truthy** — they are non-empty strings. Every value read from a file, an
  environment variable, or a CSV arrives as a string, so `if os.environ["DEBUG"]:` is `True` when
  `DEBUG=0`. That is a real bug in real code.
- `[0]` is truthy — a list with one element. The element being falsy is irrelevant; the container is
  non-empty.
- `assert not value, f"..."` — `assert` with a message. Useful inside a script for a claim you want
  checked at runtime. It is **not** a substitute for a test: `python -O` strips asserts entirely.
- The pandas note — a DataFrame's `__bool__` raises deliberately, because "is this dataframe true?"
  has three plausible answers (has rows? all values true? any value true?) and guessing would be
  worse than refusing. Day 26 meets this for real.

### The safe-guard pattern

```python
def summarise(text: str | None) -> str:
    if not text:
        return "(empty)"
    return text.strip()[:40]
```

- `if not text:` catches `None` **and** `""` in one branch. Two error cases, one guard.
- Returning early keeps the happy path unindented. Every function you write from here on should look
  like this: guards first, work last.

---

## §5 Build brief

Extend `src/setu/textutils.py`:

```python
def is_blank(text: str | None) -> bool:
    """TODO(me): True for None, empty, and whitespace-only. False otherwise.

    Use truthiness, not a chain of == comparisons.
    """
    raise NotImplementedError


def first_non_blank(*candidates: str | None) -> str | None:
    """TODO(me): return the first candidate that is not blank, else None.

    'Longest common bug': do NOT use `or` alone - '   ' is truthy.
    """
    raise NotImplementedError
```

- `*candidates` — collects any number of positional arguments into a tuple. You meet `*args` formally
  on Day 10 (PY-10); today just use it.
- `first_non_blank` is the exact shape of a config-fallback helper you will reuse on Day 172 when the
  provider router picks the first available key.

---

## §6 The eval that must be able to fail

Add to `tests/test_textutils.py`:

```python
import pytest

from setu import textutils as tu


@pytest.mark.parametrize("value", [None, "", "   ", "\n\t "])
def test_is_blank_true(value):
    assert tu.is_blank(value) is True


@pytest.mark.parametrize("value", ["a", " a ", "0", "False"])
def test_is_blank_false(value):
    assert tu.is_blank(value) is False


def test_first_non_blank_skips_whitespace_only():
    assert tu.first_non_blank(None, "   ", "found", "later") == "found"


def test_first_non_blank_returns_none_when_all_blank():
    assert tu.first_non_blank(None, "", "  ") is None
```

**Line by line:**

- `assert tu.is_blank(value) is True` — `is True`, not `== True`. This asserts the function returns
  the actual boolean, not something merely truthy. A function annotated `-> bool` that returns `1`
  passes an `== True` check and fails this one, correctly.
- `"0"` and `"False"` in the false list — the string trap from §4, tested.
- `test_first_non_blank_skips_whitespace_only` — a naive `a or b or c` returns `"   "`, because
  whitespace is truthy. **This is the test that catches the obvious wrong answer**, which is what a
  good test is for.

```bash
uv run python -m pytest tests/test_textutils.py -q
```

---

## §7 Request budget

| Resource | Spent today |
|---|---|
| LLM calls | **0** |

---

## §8 Traps

- **`is` for value comparison.** Works for small ints by accident, fails for large ones. Use `==`.
- **`== None`.** Use `is None`.
- **Assuming `-2 ** 2` is `4`.** It is `-4`.
- **Assuming `2 ** 3 ** 2` is `64`.** It is `512`.
- **Reversing a short-circuit guard.** `if user.name and user is not None:` raises. Order matters.
- **`if s:` on a config string.** `"0"` is truthy. Compare explicitly when the value came from text.
- **`if df:` on a DataFrame.** Raises. Use `len(df)` or `not df.empty`.
- **Relying on `assert` for validation in shipped code.** `python -O` removes it. Raise instead.

---

## §9 Verify before you code

Written **2026-08-21**:

- <https://docs.python.org/3/reference/expressions.html#operator-precedence> — the full precedence
  table. Bookmark it; nobody memorises the middle rows.
- <https://docs.python.org/3/library/stdtypes.html#truth-value-testing> — the authoritative falsy list.

---

## §10 Say it in an interview

> "`is` compares identity, `==` compares value, and the only correct use of `is` is against
> singletons like `None`. People get away with `is` on small integers because CPython caches them,
> which makes it a bug that passes its own smoke test. And truthiness has one edge that shows up
> constantly in real code: any non-empty string is truthy, so a config flag read as `'0'` from an
> environment variable is `True`. I guard with `if not text:` because it catches `None` and empty in
> one branch, and I test the return with `is True` so a function that returns a truthy non-boolean
> doesn't slip through."

---

## §11 Done when

Tick [`CHECKLIST.md`](CHECKLIST.md), then `./m check && ./m done 5`.
