---
day: 15
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 15 — classmethod, staticmethod, property, and dunder methods"
ids: ["PY-17", "PY-18"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P9 data has provenance", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 16
generated: "2026-09-01"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 15 — `classmethod`, `staticmethod`, `property`, and dunder methods

**Phase 2 · Advanced Python · Module 2** · `PY-17` the three kinds of method plus `property`, `PY-18`
magic methods. The plan's named examples are **`Paper.from_arxiv_id()` as an alternative constructor**
and **`__repr__`, `__eq__`, `__len__` on `Paper` — and why `__repr__` saves debugging hours**. By the end
of today `src/setu/paper.py` has all of them.

> **Yesterday:** how to wrap a function in behaviour it does not know about — timing it, repeating it,
> remembering its answer — without editing a line of it.
> **Today:** the decorators the language ships with, and the method names Python calls on your behalf,
> so an object of yours behaves like one that came with Python.
> **Tomorrow:** files, `pathlib`, buffering and `with` — which is two more of the dunders you meet today.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Three contacts saved on a phone: your mum, a friend called Sam, and the dentist.

Everything today is on that screen.

- **There are two ways to add one.** Type the name and number into the form, or tap *add to contacts* on
  a message and let the phone fill it in. Same contact either way. That is an alternative constructor.
- **Some questions are about one contact and some are about contacts in general.** *What is Sam's
  number?* needs Sam. *What can a contact hold?* does not, and can be answered on a phone with no
  contacts on it at all.
- **The card of oven temperatures is stuck inside the kitchen cupboard**, not because it is about any
  meal, but because that is where you are standing when you need it. That is a static method, and it is
  the weakest of the three arguments.
- **"Last message: 3 days ago" was never typed by anybody.** It is worked out at the moment you look. So
  is the number of messages — and *that* one is slow enough that somebody wrote it down once and it went
  stale a minute later.
- **The number box will not accept letters.** The rule lives in the box, so it applies however the number
  arrived.
- **Every row in the list said `Contact`**, and nobody could tell which one was Mum. That is a missing
  `__repr__`, and it cost somebody twenty minutes on the phone reading numbers out.
- **Mum is saved twice, under two names, with one number**, and *find duplicates* finds nothing — because
  the tool asked "are these the same entry?" and you asked "are these the same person?"
- **The list is filed alphabetically**, and that is the only reason search is instant. File two entries
  for one person under two letters and being filed is worse than useless.
- **A new phone says "No contacts", not "Contacts app not installed."** Empty and absent are different
  facts.
- **And somebody added six gestures**, each of them a good idea, and now nobody can hand the phone to
  another person and have them use it.

One thing before any code: **none of today is new machinery**. `@classmethod` and `@property` are
decorators, which you built from scratch yesterday, and a dunder method is an ordinary method with a
name Python happens to look for. What is new is a system, and the judgement about how much of it to use.

---

## §2 The map

**What the section numbers mean today.** Two IDs, so the plan's `lab (2 IDs)` split with a synthesis
section. **1.x** and **2.x** are `PY-17` — the three kinds of method, then `property`, which is how a
method stops looking like one. **3.x** is `PY-18` — what a dunder is, and the four every class has an
opinion about whether it wants. **4.x** is the synthesis: the dunders that only make sense as a set, and
the decision about when to stop. Section 4 is also the day's build.

### Section 1 — three kinds of method

| Part | What it answers | Level |
|---|---|---|
| [1.1 The method that receives the class](parts/01-three-kinds-of-method/1.1-the-method-that-gets-the-class.md) | What arrives in the first parameter, and when? | `foundation` |
| [1.2 The second door in — an alternative constructor](parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md) | Why not just add parameters to `__init__`? | `working` |
| [1.3 `staticmethod` — the method that receives nothing](parts/01-three-kinds-of-method/1.3-staticmethod-the-method-that-gets-nothing.md) | When is a module-level function better? | `working` |
| [1.4 `cls` and inheritance](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md) | Why does the subclass get built as the base? | `production` |

### Section 2 — `property`

| Part | What it answers | Level |
|---|---|---|
| [2.1 A property is worked out](parts/02-property/2.1-a-property-is-worked-out.md) | Where does the value live, and when does it run? | `foundation` |
| [2.2 The setter, and validation that cannot be walked round](parts/02-property/2.2-the-setter-and-validation.md) | Why is validating in `__init__` not enough? | `working` |
| [2.3 The property that did real work](parts/02-property/2.3-the-property-that-did-real-work.md) | What do the missing brackets promise a caller? | `production` |
| [2.4 `cached_property`, and the value that stopped being true](parts/02-property/2.4-cached-property-and-the-stale-cache.md) | Where is the cached value stored, and how do you clear it? | `production` |

### Section 3 — the dunders

| Part | What it answers | Level |
|---|---|---|
| [3.1 What a dunder method is](parts/03-the-dunders/3.1-what-a-dunder-method-is.md) | What does Python actually do when it sees `len(x)`? | `foundation` |
| [3.2 `__repr__` and `__str__`](parts/03-the-dunders/3.2-repr-and-str.md) | Which one does a list of your objects use? | `working` |
| [3.3 `__eq__`, and the duplicate that was never caught](parts/03-the-dunders/3.3-eq-and-the-duplicate.md) | What else changes when you define `==`? | `working` |
| [3.4 `__hash__`, and the object that broke the set](parts/03-the-dunders/3.4-hash-and-the-broken-set.md) | Why did defining `__eq__` make my class unhashable? | `production` |
| [3.5 `__len__` and `__bool__`](parts/03-the-dunders/3.5-len-and-bool.md) | What else does adding `__len__` quietly change? | `working` |

### Section 4 — the `Paper` API

| Part | What it answers | Level |
|---|---|---|
| [4.1 Ordering, and `total_ordering`](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md) | Which single comparison does `sorted()` need? | `production` |
| [4.2 The container protocol](parts/04-the-paper-api/4.2-the-container-protocol.md) | What two tests catch a container that contradicts itself? | `production` |
| [4.3 Which dunders, and when to stop](parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md) | What does every extra dunder cost a reader? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `functools` from the standard library.
Module 2 is still the language; the first new dependency is Phase 3.

```bash
mkdir -p src/setu tests notebooks
touch tests/test_paper_api.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-15-scratch.ipynb

# yesterday's decorators must already exist - today's built-ins are the same shape
uv run python -c "from setu.decorators import retry, timed; print('decorators ok')"

# day 12's Paper is what today rebuilds; confirm it is there before touching it
uv run python -c "from setu.paper import Paper; print('Paper ok')"

# the seven facts the day is built on, before any part names them
uv run python -c "
import functools


class Contact:
    kind = 'person'

    def __init__(self, name):
        self.name = name

    @classmethod
    def describe(cls):
        return f'{cls.__name__} stores a {cls.kind}'

    @staticmethod
    def normalise(number):
        return number.replace(' ', '')

    @property
    def shout(self):
        return self.name.upper()


print('1 cls is the class            :', Contact.describe(), '<- part 1.1')
print('2 a staticmethod gets nothing :', Contact.normalise('07700 900111'), '<- part 1.3')
mum = Contact('Mum')
print('3 a property has no brackets  :', mum.shout, '/ stored:', sorted(vars(mum)), '<- part 2.1')


class Bare:
    def __init__(self, n):
        self.n = n


print('4 the default repr            :', [Bare(1)], '<- part 3.2')
print('5 two identical objects       :', Bare(1) == Bare(1), '<- part 3.3')


class Eq:
    def __init__(self, n):
        self.n = n

    def __eq__(self, o):
        return self.n == o.n


print('6 __eq__ removed __hash__     :', Eq.__hash__, '<- part 3.4')
print('7 total_ordering exists       :', functools.total_ordering.__name__, '<- part 4.1')
"

# the two rules that catch today's headline mistakes, read from the installed linter
uv run ruff rule PLW1641
uv run ruff rule B019
```

Expected from the seven-fact block on this machine, on 2026-09-01. The address on line 4 will differ:

```
1 cls is the class            : Contact stores a person <- part 1.1
2 a staticmethod gets nothing : 07700900111 <- part 1.3
3 a property has no brackets  : MUM / stored: ['name'] <- part 2.1
4 the default repr            : [<__main__.Bare object at 0x0000013677B977A0>] <- part 3.2
5 two identical objects       : False <- part 3.3
6 __eq__ removed __hash__     : None <- part 3.4
7 total_ordering exists       : total_ordering <- part 4.1
```

| What | Where it comes from | Part |
|---|---|---|
| `@classmethod`, `cls`, `__self__` | language | [1.1](parts/01-three-kinds-of-method/1.1-the-method-that-gets-the-class.md) |
| alternative constructors, `cls(...)` | design | [1.2](parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md), [1.4](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md) |
| `@staticmethod` | language | [1.3](parts/01-three-kinds-of-method/1.3-staticmethod-the-method-that-gets-nothing.md) |
| `typing.Self`, *PEP 673* | standard library | [1.4](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md) |
| `@property`, `@x.setter`, descriptors | language | [2.1](parts/02-property/2.1-a-property-is-worked-out.md), [2.2](parts/02-property/2.2-the-setter-and-validation.md) |
| `functools.cached_property` | standard library | [2.4](parts/02-property/2.4-cached-property-and-the-stale-cache.md) |
| the data model's special names | language reference | [3.1](parts/03-the-dunders/3.1-what-a-dunder-method-is.md) |
| `repr` vs `str`, `!r` | already met on [Day 7](../day-07-strings/parts/03-formatting/3.3-repr-and-the-debugging-f-string.md) | [3.2](parts/03-the-dunders/3.2-repr-and-str.md) |
| identity comparison as the `==` default | already met on [Day 12](../day-12-classes/parts/02-attribute-lookup/2.4-your-object-and-equality.md) | [3.3](parts/03-the-dunders/3.3-eq-and-the-duplicate.md) |
| hashability, buckets, sets | already met on [Day 4](../day-04-objects/parts/02-containers/2.5-hashability.md) and [Day 8](../day-08-containers/parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md) | [3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md) |
| truthiness and the falsy container | already met on [Day 5](../day-05-operators-and-conditionals/parts/02-conditionals/2.2-truthiness.md) | [3.5](parts/03-the-dunders/3.5-len-and-bool.md) |
| `sorted(key=...)` | already met on [Day 8](../day-08-containers/parts/01-sequences/1.5-sort-sorted-and-key.md) | [4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md) |
| iterable vs iterator | already met on [Day 11](../day-11-iterators-and-generators/parts/01-iterators/1.1-iterable-and-iterator.md) | [4.2](parts/04-the-paper-api/4.2-the-container-protocol.md) |
| `functools.total_ordering`, `collections.abc` | standard library | [4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md), [4.2](parts/04-the-paper-api/4.2-the-container-protocol.md) |
| decorators, and why `@property` is one | already built on [Day 14](../day-14-decorators/parts/01-functions-as-values/1.4-the-at-sign-is-two-lines.md) | all of sections 1 and 2 |

---

## §4 Build brief

**One module rewritten**, `src/setu/paper.py`, and one new one, `src/setu/book.py`.
`src/setu/loaders/` is imported and not changed.

**1. `src/setu/paper.py`** — `Paper`, given the day's four dunders and its second door
([4.3](parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md) walks the finished shape).

```python
"""A paper. Set once at construction; equality and hashing by identifier."""

from __future__ import annotations

import functools
from typing import Self


class Paper:
    """One paper from one source.

    Fields are set in __init__ and never reassigned, which is what makes
    __hash__ safe (part 3.4) and cached_property safe (part 2.4). If you
    later add a setter, say in this docstring which caches it must clear.
    """

    def __init__(self, title: str, year: int, source: str, paper_id: str | None = None) -> None:
        # TODO(me): store into _underscore names, assigning THROUGH the setters
        # you write below where there is one (part 2.2). Validate: a blank
        # title and a year outside 1900..2100 are both refusals, and both
        # raise ValueError with the offending value in the message.
        raise NotImplementedError

    @classmethod
    def from_arxiv_id(cls, arxiv_id: str) -> Self:
        """The plan's named example. Parse, then hand clean values to __init__."""
        # TODO(me): an arXiv id looks like 2301.00001 - the first two digits
        # are the year. Work out title and year, then `return cls(...)`.
        # `cls`, NOT `Paper` - part 1.4 shows what the difference costs.
        # No network: this parses the id, it does not fetch anything (P5).
        raise NotImplementedError

    @classmethod
    def from_row(cls, row: dict[str, str]) -> Self:
        """The database door. Day 226 uses this one."""
        # TODO(me): same shape. One method per input format is the whole point
        # of part 1.2 - resist adding a `kind=` parameter to either of them.
        raise NotImplementedError

    @staticmethod
    def normalise_title(title: str) -> str:
        """Two spellings of one title must normalise to the same string."""
        # TODO(me): reuse day 7's clean_title rather than writing a second one
        # (day 7, part 4.1). Then say in a comment why this is a staticmethod
        # and not a module-level function - part 1.3 argues both sides.
        raise NotImplementedError

    @property
    def title(self) -> str:
        # TODO(me): read-only. Part 3.4: what decides equality must not move.
        raise NotImplementedError

    @property
    def year(self) -> int:
        # TODO(me): read-only as well.
        raise NotImplementedError

    @property
    def age(self) -> int:
        """Derived, cheap, total. Part 2.3's four clauses all apply."""
        # TODO(me): 2026 - self.year. Take the current year as a parameter
        # somewhere rather than calling date.today() in a property - say in a
        # comment which of part 2.3's four clauses that protects.
        raise NotImplementedError

    @functools.cached_property
    def slug(self) -> str:
        """Computed once. Legal only because the title cannot change."""
        # TODO(me): the normalised title, lowercased, hyphen-joined.
        raise NotImplementedError

    def __repr__(self) -> str:
        # TODO(me): type(self).__name__ and the identifying fields only.
        # Part 3.2: this goes in every log line, so no abstract and nothing
        # long. Use !r on the values.
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        # TODO(me): NotImplemented for a non-Paper (part 3.3), then compare
        # the identifier if both have one, and the normalised title and year
        # otherwise. Write down in the docstring which you chose and why -
        # this is a domain decision and an undecided one cannot be defended.
        raise NotImplementedError

    def __hash__(self) -> int:
        # TODO(me): the SAME fields __eq__ uses, as a tuple. Read the two
        # methods side by side before you move on (part 3.4).
        raise NotImplementedError
```

**2. `src/setu/book.py`** — a small collection, to make the container protocol concrete.

```python
"""A collection of Papers that behaves like a built-in one."""

from __future__ import annotations

from collections.abc import Iterator

from setu.paper import Paper


class PaperBook:
    """Papers, deduplicated on the way in.

    Decide ONE meaning for an item and make all four dunders agree
    (part 4.2). Write the decision here before writing the methods.
    """

    def __init__(self, papers: list[Paper]) -> None:
        # TODO(me): store a dict keyed by paper. Deduplication is free now
        # that Paper is hashable (part 3.4) - and COPY the input, or the
        # caller can change the book underneath you (day 4, part 2.3).
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Paper]:
        # TODO(me): return a FRESH iterator every call. Part 4.2's second
        # failure is what happens if you store one.
        raise NotImplementedError

    def __contains__(self, paper: object) -> bool:
        raise NotImplementedError

    def __getitem__(self, index: int) -> Paper:
        raise NotImplementedError

    def __repr__(self) -> str:
        # TODO(me): the COUNT, not the papers. A book of ten thousand must
        # still be printable in a log line (part 3.2).
        raise NotImplementedError
```

**3. Reproduce the seven traps in the notebook, then throw the notebook away.** In
`notebooks/day-15-scratch.ipynb`, in this order:

- Write a `@classmethod` whose first parameter is called `self` and read the `AttributeError`
  ([1.1](parts/01-three-kinds-of-method/1.1-the-method-that-gets-the-class.md)).
- Build a subclass, call an inherited alternative constructor that says `Paper(...)` rather than
  `cls(...)`, and print `type(result).__name__`
  ([1.4](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md)).
- Write a setter that assigns to `self.number` instead of `self._number` and read the `RecursionError`
  ([2.2](parts/02-property/2.2-the-setter-and-validation.md)).
- Cache a property, change the field it was computed from, and read the stale value
  ([2.4](parts/02-property/2.4-cached-property-and-the-stale-cache.md)).
- Assert that two identical objects are equal, with a `__repr__` defined, and read the failure message
  in which both sides look the same ([3.3](parts/03-the-dunders/3.3-eq-and-the-duplicate.md)).
- Define `__eq__` with no `__hash__` and put one in a set
  ([3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md)).
- Add `__len__` to a non-collection and watch `if not paper:` change meaning
  ([3.5](parts/03-the-dunders/3.5-len-and-bool.md)).

**The notebook is not committed** (Principle 6); `src/setu/paper.py`, `src/setu/book.py` and their tests
are.

**4. Decide, in writing, what makes two papers the same.** Write two sentences in `__eq__`'s docstring.
Either answer — the identifier alone, or the normalised title and year — can be defended; an undecided
one cannot ([3.3](parts/03-the-dunders/3.3-eq-and-the-duplicate.md) has the argument, and
[4.3](parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md) has the consequence).

**5. Decide, in writing, whether `Paper` gets a `__lt__`.** One sentence saying yes and which field, or
no and what `key=` callers should use instead
([4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md)).

---

## §5 The eval that must be able to fail

Create `tests/test_paper_api.py`. Every one runs offline, spends nothing, and belongs in `./m check`.

```python
"""Day 15: the promises an object's own API has to keep."""

from __future__ import annotations

import pytest

from setu.book import PaperBook
from setu.paper import Paper


def make(title="The Kitchen Table", year=2019, source="manual", paper_id=None):
    """One place that builds a Paper, so a signature change is one edit."""
    # TODO(me): one line. Every test below goes through this.
    raise NotImplementedError


def test_both_doors_produce_the_same_type() -> None:
    """Part 1.2: an alternative constructor builds the ordinary object."""
    # TODO(me): assert type(Paper.from_arxiv_id('2301.00001')) is Paper.
    raise NotImplementedError


def test_an_alternative_constructor_still_validates() -> None:
    """Part 1.2: no door goes round __init__."""
    # TODO(me): a row with a blank title must raise ValueError from from_row.
    # If it does not, from_row is setting attributes rather than calling cls().
    raise NotImplementedError


def test_a_subclass_gets_itself_back() -> None:
    """Part 1.4: cls, not the class name."""
    # TODO(me): a two-line subclass, then assert isinstance(...) is the
    # SUBCLASS. This is the only assertion that catches a hard-coded name -
    # every field assertion passes on the base.
    raise NotImplementedError


def test_the_title_cannot_be_reassigned() -> None:
    """Part 3.4: what decides equality must not move."""
    # TODO(me): pytest.raises(AttributeError) on paper.title = 'other'.
    # Assert on the message mentioning 'setter' - it is what tells the next
    # reader this was deliberate.
    raise NotImplementedError


def test_the_year_is_validated_on_construction() -> None:
    """Part 2.2: one rule, every route in."""
    # TODO(me): year=1500 raises ValueError, and the message contains 1500.
    raise NotImplementedError


def test_repr_names_the_class_and_omits_long_fields() -> None:
    """Part 3.2: this string goes in every log line."""
    # TODO(me): assert 'Paper(' in repr, that the title is in it, and that
    # len(repr(p)) < 200. The length assertion is the one that survives
    # somebody adding an abstract field later.
    raise NotImplementedError


def test_a_subclass_repr_names_the_subclass() -> None:
    """Part 3.2: type(self).__name__, not a literal."""
    # TODO(me): the same two-line subclass, assert its name is in the repr.
    raise NotImplementedError


def test_two_papers_from_two_sources_are_one_paper() -> None:
    """Part 3.3: the domain decision, made executable."""
    # TODO(me): build the same paper via from_arxiv_id and from_row and
    # assert they are equal. This test is the docstring you wrote in §4,
    # in a form that can go red.
    raise NotImplementedError


def test_a_paper_is_not_equal_to_a_string() -> None:
    """Part 3.3: NotImplemented, not False."""
    # TODO(me): assert (p == 'The Kitchen Table') is False AND that it did
    # not raise. Then say in a comment what returning False from __eq__
    # would have broken that this test cannot see.
    raise NotImplementedError


def test_equal_papers_hash_equal() -> None:
    """Part 3.4: the invariant, stated directly."""
    # TODO(me): for two equal papers assert (a == b) is (hash(a) == hash(b)).
    # Write it as that equivalence, not as two separate assertions - the
    # equivalence is the actual rule.
    raise NotImplementedError


def test_a_set_of_duplicates_holds_one() -> None:
    """Part 3.4: what the hash was for."""
    # TODO(me): three papers, two of them the same, assert len(set) == 2.
    raise NotImplementedError


def test_the_slug_is_stable_across_two_spellings() -> None:
    """Part 2.4 plus day 7: normalising is what makes dedup work."""
    # TODO(me): ' The Kitchen Table ' and 'the kitchen table' produce the
    # same slug.
    raise NotImplementedError


def test_the_book_len_matches_what_it_yields() -> None:
    """Part 4.2, consistency test one."""
    # TODO(me): assert len(list(book)) == len(book).
    raise NotImplementedError


def test_everything_in_the_book_is_in_the_book() -> None:
    """Part 4.2, consistency test two."""
    # TODO(me): assert all(p in book for p in book). Two lines, and it is
    # the only test that catches __iter__ and __contains__ disagreeing.
    raise NotImplementedError


def test_the_book_can_be_iterated_twice() -> None:
    """Part 4.2: __iter__ must build a fresh iterator."""
    # TODO(me): list(book) twice, assert equal and non-empty. An
    # implementation that stores one iterator passes the first and fails
    # the second.
    raise NotImplementedError


@pytest.mark.parametrize("count", [0, 1, 5])
def test_the_book_reprs_at_every_size(count) -> None:
    """Part 3.2: a book of ten thousand must still fit in a log line."""
    # TODO(me): assert the repr is short and contains the count. The zero
    # case is here because an empty collection is the case fixtures never
    # have (part 3.5).
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_paper_api.py -v
```

Then implement, then **break each one on purpose**:

- Change `from_row` to set attributes directly instead of calling `cls(...)`.
  **`test_an_alternative_constructor_still_validates` goes red and nothing else does** — which is why a
  validation test exists per door rather than only on `__init__`.
- Change `from_arxiv_id` to `return Paper(...)`. Only `test_a_subclass_gets_itself_back` goes red. Sit
  with that: every field assertion in the suite still passes.
- Give `title` a setter. `test_the_title_cannot_be_reassigned` goes red — and note that the hash tests
  stay green, because a mutable equality field is a bug no assertion can see until somebody moves one.
- Put the abstract in `__repr__`. The length assertion goes red and the "contains the title" one stays
  green. **Two assertions, one line, two different promises.**
- Delete `__hash__`. `test_a_set_of_duplicates_holds_one` goes red with `TypeError: unhashable type`,
  and so does the book — because the book is a dict keyed by paper.
- Hash the title as well as the identifier. `test_equal_papers_hash_equal` goes red **while everything
  about equality stays green**, which is exactly the bug the invariant test exists for.
- Store one iterator in `PaperBook.__init__` and return it from `__iter__`. Only
  `test_the_book_can_be_iterated_twice` goes red.
- **Break it and watch every test stay GREEN** — make `__iter__` yield papers while `__contains__`
  tests identifier strings, *and* delete `test_everything_in_the_book_is_in_the_book`. Everything
  passes, and `for p in book: assert p in book` is false. Restore the test, watch it go red, and say
  out loud what the missing test was protecting.

That last item is the most important line in this section. A container is a set of promises about what
an item is, and no test about counting, printing or equality can see two of those promises disagreeing.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — `from_arxiv_id` parses an identifier, it does not fetch one |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |

`from_arxiv_id` is the one place today where somebody would reasonably reach for the network. It does
not, and that is deliberate: an alternative constructor that makes a request is a property-style broken
promise ([2.3](parts/02-property/2.3-the-property-that-did-real-work.md)) and it makes every test that
builds a `Paper` need a connection.

---

## §7 Traps

- **A `@classmethod` whose parameter is called `self` still receives the class** —
  [1.1](parts/01-three-kinds-of-method/1.1-the-method-that-gets-the-class.md).
- **Forgetting `@classmethod` fails at the call, naming `cls`** —
  [1.1](parts/01-three-kinds-of-method/1.1-the-method-that-gets-the-class.md).
- **An alternative constructor with no `return` hands back `None`** —
  [1.2](parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md).
- **`cls.__new__(cls)` skips `__init__` and every check in it** —
  [1.2](parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md).
- **An `__init__` with six optional parameters can no longer say what the object requires** —
  [1.2](parts/01-three-kinds-of-method/1.2-from-message-the-second-door-in.md).
- **A `staticmethod` that reaches for `self` gets a `NameError`, not an `AttributeError`** —
  [1.3](parts/01-three-kinds-of-method/1.3-staticmethod-the-method-that-gets-nothing.md).
- **A missing `@staticmethod` works when called on the class and fails when called on an instance** —
  [1.3](parts/01-three-kinds-of-method/1.3-staticmethod-the-method-that-gets-nothing.md).
- **A staticmethod naming its own class ignores a subclass's override** —
  [1.3](parts/01-three-kinds-of-method/1.3-staticmethod-the-method-that-gets-nothing.md).
- **`return Contact(...)` instead of `cls(...)` silently returns the base class** —
  [1.4](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md).
- **A subclass demanding an extra constructor argument breaks every inherited `cls(...)`** —
  [1.4](parts/01-three-kinds-of-method/1.4-cls-and-inheritance.md).
- **Brackets on a property give `'X' object is not callable`** —
  [2.1](parts/02-property/2.1-a-property-is-worked-out.md).
- **A method used as an attribute is always truthy, so the `if` always passes** —
  [2.1](parts/02-property/2.1-a-property-is-worked-out.md).
- **A property named the same as the attribute `__init__` assigns fails inside `__init__`** —
  [2.1](parts/02-property/2.1-a-property-is-worked-out.md).
- **A setter assigning to its own property recurses forever** —
  [2.2](parts/02-property/2.2-the-setter-and-validation.md).
- **Validation in `__init__` alone is bypassed by the next assignment** —
  [2.2](parts/02-property/2.2-the-setter-and-validation.md).
- **One leading underscore prevents accidents, not determined bypass** —
  [2.2](parts/02-property/2.2-the-setter-and-validation.md).
- **A property read three times in a template does its work three times** —
  [2.3](parts/02-property/2.3-the-property-that-did-real-work.md).
- **A property that raises turns every f-string into something needing a `try`** —
  [2.3](parts/02-property/2.3-the-property-that-did-real-work.md).
- **A property with a side effect fires when a debugger renders the object** —
  [2.3](parts/02-property/2.3-the-property-that-did-real-work.md).
- **`cached_property` never invalidates, and the stale value looks plausible** —
  [2.4](parts/02-property/2.4-cached-property-and-the-stale-cache.md).
- **`cached_property` is incompatible with `__slots__`** —
  [2.4](parts/02-property/2.4-cached-property-and-the-stale-cache.md).
- **`cached_property` is silently assignable, unlike a read-only property** —
  [2.4](parts/02-property/2.4-cached-property-and-the-stale-cache.md).
- **A dunder set on an instance is ignored — the lookup is on the type** —
  [3.1](parts/03-the-dunders/3.1-what-a-dunder-method-is.md).
- **You do not choose a dunder's signature; the protocol does** —
  [3.1](parts/03-the-dunders/3.1-what-a-dunder-method-is.md).
- **A list of your objects shows `__repr__`, not `__str__`** —
  [3.2](parts/03-the-dunders/3.2-repr-and-str.md).
- **Writing only `__str__` leaves every debugger, log and test failure useless** —
  [3.2](parts/03-the-dunders/3.2-repr-and-str.md).
- **A `__repr__` that raises makes a whole container unprintable** —
  [3.2](parts/03-the-dunders/3.2-repr-and-str.md).
- **A hard-coded class name in `__repr__` makes subclasses lie** —
  [3.2](parts/03-the-dunders/3.2-repr-and-str.md).
- **Without `__eq__`, an assertion fails with two sides that look identical** —
  [3.3](parts/03-the-dunders/3.3-eq-and-the-duplicate.md).
- **`in`, `remove`, `index` and `count` all change meaning when you define `__eq__`** —
  [3.3](parts/03-the-dunders/3.3-eq-and-the-duplicate.md).
- **Returning `False` rather than `NotImplemented` makes `==` asymmetric** —
  [3.3](parts/03-the-dunders/3.3-eq-and-the-duplicate.md).
- **Defining `__eq__` sets `__hash__` to `None`** —
  [3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md).
- **Hashing more fields than equality compares puts two equal objects in one set** —
  [3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md).
- **Mutating a hashed field leaves an object in a set that cannot find it** —
  [3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md).
- **A subclass that overrides `__eq__` loses `__hash__` again** —
  [3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md).
- **`hash()` of a string differs between processes and must never be stored** —
  [3.4](parts/03-the-dunders/3.4-hash-and-the-broken-set.md).
- **Adding `__len__` changes what `if x:` means** —
  [3.5](parts/03-the-dunders/3.5-len-and-bool.md).
- **`__bool__` must return an actual `bool`** —
  [3.5](parts/03-the-dunders/3.5-len-and-bool.md).
- **`x or default` replaces a real but empty object with the default** —
  [3.5](parts/03-the-dunders/3.5-len-and-bool.md).
- **`sorted` raises about `<` even though you wrote `sorted`** —
  [4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md).
- **`__lt__` gives you `>` by reflection but not `>=`** —
  [4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md).
- **Sorting `(score, object)` tuples fails on the first tie** —
  [4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md).
- **`__eq__` and `__lt__` over different fields make an incoherent order** —
  [4.1](parts/04-the-paper-api/4.1-ordering-and-total-ordering.md).
- **`__iter__` returning a stored iterator works once** —
  [4.2](parts/04-the-paper-api/4.2-the-container-protocol.md).
- **`__getitem__` alone makes an object iterable through the legacy protocol** —
  [4.2](parts/04-the-paper-api/4.2-the-container-protocol.md).
- **`len(x)` and `len(list(x))` disagreeing breaks every caller that trusts the count** —
  [4.2](parts/04-the-paper-api/4.2-the-container-protocol.md).
- **`__getattr__` turns every typo into a silent `None`** —
  [4.3](parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md).
- **An operator whose meaning has to be looked up costs more than it saves** —
  [4.3](parts/04-the-paper-api/4.3-which-dunders-and-when-to-stop.md).

---

## §8 Verify before you code

Fetched **2026-09-01**. Today is the language and one standard-library module, so the language reference
is the authority:

- <https://docs.python.org/3/reference/datamodel.html#special-method-names> — the data model's complete
  list of dunder methods with their required signatures and return types. The single most useful page in
  the documentation for anybody writing classes.
- <https://docs.python.org/3/reference/datamodel.html#object.__hash__> — the paragraph stating that a
  class defining `__eq__` and not `__hash__` has its `__hash__` set to `None`, and the invariant that
  equal objects must hash equally.
- <https://docs.python.org/3/reference/datamodel.html#descriptors> — the descriptor protocol, which is
  what `property`, `classmethod` and `staticmethod` are all built on.
- <https://docs.python.org/3/library/functions.html#property> — `property`, its getter, setter and
  deleter, and the decorator form.
- <https://docs.python.org/3/library/functools.html> — `cached_property` and `total_ordering`, both of
  which say plainly what they cost.
- <https://docs.python.org/3/library/collections.abc.html> — the abstract base classes for containers and
  the table of which methods each one requires and supplies.
- <https://peps.python.org/pep-0673/> — *PEP 673 — Self Type* (2021), the annotation an alternative
  constructor should return.

---

## §9 Say it in an interview

> "The three kinds of method differ only in what arrives in the first parameter: an ordinary method gets
> the instance, a classmethod gets the class, a staticmethod gets nothing. The one that earns its place
> is the classmethod, because `cls(...)` is how you give a class a second way to be built — parse the
> input shape in `from_row` or `from_arxiv_id` and hand clean values to one `__init__`, so the
> constructor's signature still documents what the object requires and every door goes through the same
> validation. And it has to be `cls`, not the class name, or an inherited constructor silently returns
> the base class and nothing fails until somebody calls a subclass-only method a long way away. A
> property is a method you read without brackets, which is a promise: cheap, total, pure, consistent —
> so a property that opens a connection or walks a big list has broken the contract the syntax made,
> and a `cached_property` fixes the cost at the price of never invalidating, which is safe only on an
> object you treat as immutable. On the dunders, the ones I write are `__repr__` on everything, because
> containers, debuggers and pytest failures all show reprs and a missing one costs hours; and `__eq__`
> with `__hash__`, always together, over the same immutable fields — because defining `__eq__` alone
> sets `__hash__` to `None` and that loud failure is standing in for the silent one, where two equal
> objects hash differently and a set quietly keeps both. `__len__` I am careful with, because adding it
> so that `len()` works also decides what `if x:` means, and an object that exists but is empty starts
> reading as absent. Beyond that I stop: an operator a reader has to look up has cost more than the
> characters it saved."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, `src/setu/paper.py` has two
doors, read-only properties and four dunders whose `__eq__` and `__hash__` name the same fields, and you
have **watched a whole test suite stay green through a container that contradicts itself** — `__iter__`
and `__contains__` disagreeing, in §5 — not when a particular amount of time has passed. Then:

```bash
./m done 15
```

Tomorrow is files, `pathlib`, buffering and context managers — and `with` turns out to be two more of
the dunder methods you met today.
