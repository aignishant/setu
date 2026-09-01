---
day: 13
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 13 — Inheritance, polymorphism, encapsulation, abstraction"
ids: ["PY-14", "PY-15"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P9 data has provenance", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 14
generated: "2026-09-01"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 13 — Inheritance, polymorphism, encapsulation, abstraction

**Phase 2 · Advanced Python · Module 2** · `PY-14` inheritance and polymorphism, `PY-15`
encapsulation and abstraction with `abc`. The plan's named examples are **`BaseLoader` → `PDFLoader`,
`HTMLLoader`** and **an ABC that refuses to instantiate until `.load()` is implemented**, and by the
end of today both exist in `src/setu/loaders/`.

> **Yesterday:** how to make a type of your own — what it holds, where the values live, and what
> makes an object worth writing at all.
> **Today:** how one type can start from another, why one loop can handle three of them, what a class
> keeps to itself, and how a base class refuses to be built half-finished.
> **Tomorrow:** decorators — `@timed` and `@retry(3)`, the two you will reuse in every later phase.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Somebody sends you the same recipe three times in one week, three different ways.

```text
Monday    a photo of a page
Wednesday typed into a message
Friday    a link
```

Everything today is in that week.

- **You say the same four words each time** — *"read me the recipe"* — and somebody works out how.
  You do not learn a new instruction per format, and when a fourth kind arrives on Sunday you say the
  same four words again.
- **Two thirds of the job is the same every time**: note where it came from, write down the date. It
  is written once on a shared sheet, and each format adds only its own step.
- **A person covering the counter for a week** must be usable exactly as the regular person was. When
  the cover asks "what encoding is it in?" before reading, or refuses a photo, or hands back a note
  instead of a list, they have broken a promise nobody wrote down and everybody relied on.
- **The kitchen has one good pair of scissors**, and the answer is a pot on the counter that everyone
  reaches into — not a pair screwed to every drawer. Buying a better pair should be one visit, not
  eleven.
- **The counter has a menu facing out, a clipboard facing in, and a closed drawer.** Nothing is
  locked. The three levels are legible, and reaching past one is a decision rather than an accident.
- **Two people on different shifts each keep a pad** headed *today's code*. If it is one pad, the
  second note wipes out the first and nobody can work out why. Printing the shift's name at the top of
  each pad costs nothing and makes the collision impossible.
- **The count on the board must equal the length of the list.** Somebody tidying crosses a line off
  the list and does not touch the number, and now both look right and one of them is wrong.
- **A source form with the "how to read one" box empty does not get filed.** It is refused at the
  desk, in front of the person who can still say what goes in it — not two weeks later, a hundred and
  twelve recipes into a batch.
- **And the neighbour turns up with a hand-written card**, having registered nothing, and it works
  immediately. The counter never asked for identification; it asked whether the thing could be read.

The day ends with the card pinned above the pigeonholes: six lines saying what every source must
provide and what every source gets. That card is `BaseLoader`, and the reason it is six lines rather
than nine is the last thing this day teaches.

```mermaid
flowchart LR
    S1["§1 inheritance<br/>one form from another"] --> S2["§2 polymorphism<br/>one name, three answers"]
    S2 --> S3["§3 encapsulation<br/>what a class keeps"]
    S3 --> S4["§4 abstraction<br/>the base that refuses"]
    style S1 fill:#1f6feb,color:#fff
    style S4 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** Two IDs, so the plan's `lab (2 IDs)` split: **1.x** and
**2.x** are `PY-14` — the machinery of inheritance, then the reason anybody builds a hierarchy;
**3.x** and **4.x** are `PY-15` — what a class keeps to itself, then how a base class states and
enforces what it requires. Section 4 is also the day's build.

### Section 1 — inheritance

| Part | What it answers | Level |
|---|---|---|
| [1.1 One form that starts from another](parts/01-inheritance/1.1-one-form-that-starts-from-another.md) | What decides whether one class should inherit from another? | `foundation` |
| [1.2 `super()`, and the `__init__` that has to run twice](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md) | Why is a subclass's `name` attribute missing? | `working` |
| [1.3 The MRO — what Python actually searches](parts/01-inheritance/1.3-the-mro.md) | With two parents, which class does `super()` reach? | `production` |
| [1.4 Overriding, and the method that broke its parent's promise](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md) | What does Python check about an override? | `working` |
| [1.5 Composition over inheritance](parts/01-inheritance/1.5-composition-over-inheritance.md) | Which one lets a test pass a fake? | `production` |

### Section 2 — polymorphism

| Part | What it answers | Level |
|---|---|---|
| [2.1 One name, three behaviours](parts/02-polymorphism/2.1-one-name-three-behaviours.md) | What changes when a fourth kind arrives? | `foundation` |
| [2.2 Duck typing, and the `isinstance` check you did not need](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md) | What does Python check when you call a method? | `working` |
| [2.3 Liskov in plain words](parts/02-polymorphism/2.3-liskov-in-plain-words.md) | Which four rules make a subclass safe to substitute? | `production` |

### Section 3 — encapsulation

| Part | What it answers | Level |
|---|---|---|
| [3.1 Public, `_protected`, `__private`](parts/03-encapsulation/3.1-public-protected-private.md) | Does Python have private attributes? | `foundation` |
| [3.2 Name mangling, and the attribute that vanished](parts/03-encapsulation/3.2-name-mangling.md) | Why is the attribute called `_Base__token`? | `working` |
| [3.3 The invariant](parts/03-encapsulation/3.3-the-invariant.md) | What is hiding state actually for? | `production` |

### Section 4 — abstraction

| Part | What it answers | Level |
|---|---|---|
| [4.1 `abc.ABC` and `@abstractmethod`](parts/04-abstraction/4.1-abc-and-abstractmethod.md) | When does an incomplete class fail, and what does the message say? | `working` |
| [4.2 `BaseLoader` → `TextLoader`, `HTMLLoader`](parts/04-abstraction/4.2-the-loader-family.md) | What does adding a fourth format cost? | `production` |
| [4.3 `Protocol` versus ABC](parts/04-abstraction/4.3-protocol-versus-abc.md) | When do you require nothing at all? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `abc` and `typing` from the standard
library. Module 2 is still the language; the first new dependency is Phase 3.

```bash
mkdir -p src/setu/loaders tests notebooks
touch src/setu/loaders/__init__.py src/setu/loaders/base.py
touch src/setu/loaders/text.py src/setu/loaders/html.py
touch tests/test_loaders.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-13-scratch.ipynb

# yesterday's Paper must already exist - loaders produce them, never redefine them
uv run python -c "from setu.paper import Paper; print('Paper ok')"

# the six facts the day is built on, before any part names them
uv run python -c "
from abc import ABC, abstractmethod

class Base:
    def __init__(self, name): self.name = name
    def describe(self): return f'{self.name} ({type(self).__name__})'

class Child(Base):
    pass

print('1 child gets the parent method:', Child('x').describe(), '<- part 1.1')

class A:
    def who(self): return 'A'
class B(A):
    def who(self): return 'B'
class C(A):
    def who(self): return 'C'
class D(B, C): pass
print('2 the search order            :', [c.__name__ for c in D.__mro__], '<- part 1.3')

class Typo(Base):
    def descrbe(self): return 'mine'
print('3 a misspelled override       :', Typo('x').describe(), '<- part 1.4')

class Mangled:
    def __init__(self): self.__token = 1
print('4 two underscores store       :', sorted(vars(Mangled())), '<- part 3.2')

class Abstract(ABC):
    @abstractmethod
    def load(self): ...
try:
    Abstract()
except TypeError as e:
    print('5 an abstract class refuses   :', e, '<- part 4.1')

from typing import Protocol, runtime_checkable
@runtime_checkable
class Loadable(Protocol):
    def load(self): ...
class Stranger:
    def load(self): return []
print('6 structural typing           :', isinstance(Stranger(), Loadable), '<- part 4.3')
"

# the two rules that catch today's headline mistakes, read from the installed linter
uv run ruff rule B024
uv run ruff rule B027
```

| What | Where it comes from | Part |
|---|---|---|
| `class Child(Parent)`, `__mro__`, `issubclass` | language, built-ins | [1.1](parts/01-inheritance/1.1-one-form-that-starts-from-another.md), [1.3](parts/01-inheritance/1.3-the-mro.md) |
| `super()` | language | [1.2](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md) |
| overriding, `typing.override` | language, standard library | [1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md) |
| composition, held collaborators | design | [1.5](parts/01-inheritance/1.5-composition-over-inheritance.md) |
| `isinstance`, `type(x) == cls` | built-ins | [2.2](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md) |
| `_name`, `__name`, name mangling, `co_names` | language | [3.1](parts/03-encapsulation/3.1-public-protected-private.md), [3.2](parts/03-encapsulation/3.2-name-mangling.md) |
| `abc.ABC`, `@abstractmethod` | standard library | [4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md) |
| `typing.Protocol`, `@runtime_checkable` | standard library | [4.3](parts/04-abstraction/4.3-protocol-versus-abc.md) |
| `io.StringIO` as a fake reader | already met on [Day 11](../day-11-iterators-and-generators/parts/04-the-gate/4.2-the-streaming-reader.md) | [4.2](parts/04-abstraction/4.2-the-loader-family.md) |
| `Paper`, and validation at construction | already built on [Day 12](../day-12-classes/parts/03-the-paper-object/3.2-validation-in-init.md) | [4.2](parts/04-abstraction/4.2-the-loader-family.md) |
| `pytest.mark.parametrize` | already met on [Day 2](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md) | [1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md), [4.2](parts/04-abstraction/4.2-the-loader-family.md) |

---

## §4 Build brief

**One new package**, `src/setu/loaders/`, holding the family. `src/setu/paper.py` is imported and not
changed.

**1. `src/setu/loaders/base.py`** — the contract and nothing else
([4.2](parts/04-abstraction/4.2-the-loader-family.md) explains every line of it).

```python
"""What every loader must provide, and what they all get."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol

from setu.paper import Paper


class Reader(Protocol):
    """Anything that can hand back its whole contents as text (part 4.3).

    io.StringIO satisfies this, and so does an open file, and so does a
    four-line fake in a test. None of them inherits from anything of ours.
    """

    def read(self) -> str: ...


class LoaderError(Exception):
    """Every loader raises this or a subclass. Part 2.3, rule 3."""


class BaseLoader(ABC):
    """A source of Papers.

    Subclasses implement load(). Everything else is provided.

    The contract for load(), which abc cannot enforce (part 4.1):
        returns:  list[Paper], possibly empty. NEVER None.
        raises:   LoaderError, or a subclass. Nothing else.
        promises: calling it twice is safe and gives the same answer.
    """

    def __init__(self, name: str, reader: Reader) -> None:
        # TODO(me): two assignments. `reader` is HELD, not inherited (part 1.5),
        # and it gets one underscore (part 3.1). Say in a comment what a test can
        # do because of that choice.
        raise NotImplementedError

    @abstractmethod
    def load(self) -> list[Paper]:
        """Return every Paper this source can produce. See the class docstring."""

    def describe(self) -> str:
        # TODO(me): one line. Use type(self).__name__, not the literal class
        # name - part 1.1 shows why one method then reports three types.
        raise NotImplementedError
```

**2. `src/setu/loaders/text.py` and `src/setu/loaders/html.py`** — one format each.

```python
"""One format each, one method each, the same signature."""

from __future__ import annotations

from setu.loaders.base import BaseLoader, LoaderError, Reader
from setu.paper import Paper


class TextLoader(BaseLoader):
    """One title per line."""

    def __init__(self, name: str, reader: Reader, *, source: str = "manual") -> None:
        # TODO(me): super().__init__ FIRST (part 1.2), then your own field.
        # `source` is keyword-only and has a default: part 2.3 rule 1 says a
        # subclass may accept more and never demand more.
        raise NotImplementedError

    def load(self) -> list[Paper]:
        # TODO(me): one Paper per non-empty line, with source=self.source so
        # provenance survives (P9). Return [] for an empty reader - never None.
        # Wrap whatever the reader raises in LoaderError, or the caller's single
        # `except` misses it and the batch dies (part 2.3, rule 3).
        raise NotImplementedError


class HTMLLoader(BaseLoader):
    """Titles inside a tag. Methods before regex - day 7, part 4.3."""

    def __init__(self, name: str, reader: Reader, *, tag: str = "h2") -> None:
        # TODO(me): same shape as above. No html library today; Phase 3 brings
        # a real parser, and the point is that adding it changes nothing here.
        raise NotImplementedError

    def load(self) -> list[Paper]:
        # TODO(me): same three rules. Then read your two load() methods side by
        # side and move anything identical UP to the base - but only if it is
        # genuinely identical (part 1.5 on the base class that grew).
        raise NotImplementedError
```

**3. `src/setu/loaders/__init__.py`** — the registry and the caller.

```python
"""Where a new format plugs in, and the loop that never changes."""

from __future__ import annotations

from setu.loaders.base import BaseLoader, LoaderError, Reader
from setu.loaders.html import HTMLLoader
from setu.loaders.text import TextLoader
from setu.paper import Paper

LOADERS: dict[str, type[BaseLoader]] = {
    ".txt": TextLoader,
    ".html": HTMLLoader,
}


def load_all(loaders: list[BaseLoader]) -> tuple[list[Paper], list[str]]:
    """Load from every loader. Return the papers AND the failures.

    Does not stop at the first failure: one bad source must not lose the good
    ones (day 12, part 3.2's bulk-loading rule).
    """
    # TODO(me): one loop, one try, one `except LoaderError`. No isinstance
    # anywhere (part 2.1). Collect failures with loader.describe() in the
    # message so a log line identifies which source failed.
    raise NotImplementedError
```

**4. Reproduce the five traps in the notebook, then throw the notebook away.** In
`notebooks/day-13-scratch.ipynb`, in this order:

- Write a subclass `__init__` **without** `super().__init__(...)` and read the `AttributeError`
  ([1.2](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md)). Then move the `super()`
  call to the last line and use a parent field above it — same message, different cause.
- Build the diamond from [1.3](parts/01-inheritance/1.3-the-mro.md) and print `__mro__`. Then remove
  one `super()` call from the chain and see which step disappears.
- Misspell an overridden method name and confirm the base's version runs with no error
  ([1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md)).
- Store `self.__x` in a base and the same name in a child, and print `vars()`
  ([3.2](parts/03-encapsulation/3.2-name-mangling.md)).
- Put `@abstractmethod` on a class whose base line is **not** `ABC`, and watch it instantiate anyway
  ([4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md)).

**The notebook is not committed** (Principle 6); `src/setu/loaders/` and its tests are.

**5. Decide, in writing, whether `Reader` should be a `Protocol` or an ABC.** Write two sentences in
the `Reader` docstring saying which you chose and why
([4.3](parts/04-abstraction/4.3-protocol-versus-abc.md) has the table). Either answer can be
defended; an undecided one cannot.

---

## §5 The eval that must be able to fail

Create `tests/test_loaders.py`. Every one runs offline and belongs in `./m check`.

```python
"""Day 13: the same contract, asserted against every member of the family."""

from __future__ import annotations

import io

import pytest

from setu.loaders import LOADERS, load_all
from setu.loaders.base import BaseLoader, LoaderError
from setu.paper import Paper


class RaisingReader:
    """A reader that fails. Four lines, no mocking library (part 2.2)."""

    def read(self) -> str:
        raise OSError("file gone")


def make(cls, text):
    """Build any loader over an in-memory reader. No disk, no network."""
    # TODO(me): one line. io.StringIO(text) is the fake (part 1.5), and this
    # helper is why every test below is two lines long.
    raise NotImplementedError


def test_base_loader_cannot_be_instantiated() -> None:
    """Part 4.1: the abstract base refuses, and says which method is missing."""
    # TODO(me): pytest.raises(TypeError, match="load"). Assert on the MESSAGE -
    # it naming 'load' is what tells the next loader author what to write.
    raise NotImplementedError


@pytest.mark.parametrize("cls", list(LOADERS.values()))
def test_every_loader_returns_a_list_of_papers(cls) -> None:
    """Part 1.4: the return-shape contract, for every member of the family."""
    # TODO(me): assert isinstance(result, list) AND that every item is a Paper.
    # A new loader has to pass this before it goes in LOADERS.
    raise NotImplementedError


@pytest.mark.parametrize("cls", list(LOADERS.values()))
def test_every_loader_returns_an_empty_list_for_empty_input(cls) -> None:
    """Never None - part 1.4's most common violation."""
    # TODO(me): assert result == [], NOT `assert not result`. The second passes
    # for None too, which is the value this test exists to reject.
    raise NotImplementedError


@pytest.mark.parametrize("cls", list(LOADERS.values()))
def test_every_loader_raises_only_loader_error(cls) -> None:
    """Part 2.3, rule 3: the caller has one handler, so one exception family."""
    # TODO(me): build with RaisingReader() and pytest.raises(LoaderError).
    # A loader that lets the OSError through fails here - and would take down
    # load_all in production.
    raise NotImplementedError


@pytest.mark.parametrize("cls", list(LOADERS.values()))
def test_every_loader_is_safe_to_call_twice(cls) -> None:
    """The promise in the base's docstring, made executable."""
    # TODO(me): call load() twice, assert the results are equal. A loader that
    # iterates its reader passes the first and fails the second - day 11 part
    # 1.3 is why, and this is that bug wearing a class.
    raise NotImplementedError


@pytest.mark.parametrize("cls", list(LOADERS.values()))
def test_every_loader_sets_provenance(cls) -> None:
    """Principle 9: every Paper must be able to say where it came from."""
    # TODO(me): assert every returned Paper has a non-None source. This is the
    # test that catches a loader built by copying another and not editing it.
    raise NotImplementedError


def test_load_all_keeps_the_good_papers_when_one_loader_fails() -> None:
    """One bad source must not lose the others."""
    # TODO(me): one working loader and one with RaisingReader. Assert the good
    # papers survive AND that failures has exactly one entry naming the bad one.
    raise NotImplementedError


def test_a_stranger_class_is_not_a_baseloader_and_still_works() -> None:
    """Part 2.2: load_all takes anything with load(), not just our subclasses."""
    # TODO(me): a four-line class with a load() returning one Paper, not
    # inheriting from anything. Assert isinstance(x, BaseLoader) is False AND
    # that load_all still collects its paper. Then say in a comment what an
    # isinstance gate in load_all would have cost.
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_loaders.py -v
```

Then implement, then **break each one on purpose**:

- Remove `ABC` from `BaseLoader`'s base line. **`test_base_loader_cannot_be_instantiated` goes red
  and nothing else does** — which is the whole point of
  [4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md)'s inert-decorator failure.
- Let `TextLoader.load` return `None` for an empty reader. The empty-list test goes red; the
  list-of-papers test goes red too. **Two tests for one edit** means they test different promises.
- Delete the `try`/`except` wrapping the reader in one loader. The `only LoaderError` test goes red
  for that loader alone, and the parametrised name in the failure tells you which.
- Move `super().__init__(...)` to the **last** line of a loader's `__init__` and use `self.name`
  above it. Every test for that loader goes red with an `AttributeError`.
- Rename `load` to `laod` in one loader. **It fails at construction with a `TypeError` naming
  `load`** — not silently, as it did on
  [1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md), because the base is abstract
  now. Sit with that difference before restoring it.
- **Make `load` iterate `self._reader` one line at a time instead of calling `read()`.** Every test still
  passes **except** `safe_to_call_twice`. Do not restore it until you can say why the other six were
  green.

That last item is the most important line in this section. Six green tests over a real defect is
exactly what Principle 7 exists to prevent, and the one that caught it is the one that asserts a
promise nobody would have thought to test.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — nothing today leaves your machine |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |

Every loader is tested against `io.StringIO`, so nothing touches a disk either. That is the held
reader from [1.5](parts/01-inheritance/1.5-composition-over-inheritance.md) doing its job, and it is
why `./m check` stays offline
([Day 2, 5.3](../day-02-quality-gate/parts/05-ci/5.3-caching-and-never-spending-a-quota.md)).

---

## §7 Traps

- **Inheriting from `dict` or `list` gives your class forty methods you did not want** —
  [1.1](parts/01-inheritance/1.1-one-form-that-starts-from-another.md).
- **A base class that is instantiable can end up in the list by accident** —
  [1.1](parts/01-inheritance/1.1-one-form-that-starts-from-another.md).
- **A subclass's `__init__` replaces the parent's completely** —
  [1.2](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md).
- **`AttributeError` on a subclass instance usually means a missing `super().__init__()`** —
  [1.2](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md).
- **`super().__init__(self, ...)` supplies the instance twice** —
  [1.2](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md).
- **The no-argument `super()` only works inside a class body** —
  [1.2](parts/01-inheritance/1.2-super-and-the-init-that-runs-twice.md).
- **`super()` is the next class in the MRO, not the parent** —
  [1.3](parts/01-inheritance/1.3-the-mro.md).
- **One class that skips `super()` truncates the whole cooperative chain** —
  [1.3](parts/01-inheritance/1.3-the-mro.md).
- **`class C(A, B)` where `B(A)` cannot be linearised and fails at import** —
  [1.3](parts/01-inheritance/1.3-the-mro.md).
- **Python checks nothing about an override — not the signature, not the return, not the name** —
  [1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md).
- **A misspelled override silently leaves the base's version running** —
  [1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md).
- **An override returning `None` fails in the caller, three frames away** —
  [1.4](parts/01-inheritance/1.4-overriding-and-the-broken-promise.md).
- **Inheriting for reuse gives you the parent's whole public surface** —
  [1.5](parts/01-inheritance/1.5-composition-over-inheritance.md).
- **A behaviour that is inherited cannot be faked in a test** —
  [1.5](parts/01-inheritance/1.5-composition-over-inheritance.md).
- **A hierarchy that grows a level per behaviour is composition asking to happen** —
  [1.5](parts/01-inheritance/1.5-composition-over-inheritance.md).
- **A branch chain reappears as an `isinstance` chain and is no better** —
  [2.1](parts/02-polymorphism/2.1-one-name-three-behaviours.md),
  [2.2](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md).
- **A branch with no `else` returns `None` for the kind nobody handled** —
  [2.1](parts/02-polymorphism/2.1-one-name-three-behaviours.md).
- **`type(x) == Cls` rejects a perfectly good subclass** —
  [2.2](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md).
- **A `hasattr` guard turns a loud failure into a silently empty result** —
  [2.2](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md).
- **Duck typing matches the method's name, not its meaning** —
  [2.2](parts/02-polymorphism/2.2-duck-typing-and-isinstance.md).
- **A subclass demanding an extra argument breaks every base caller** —
  [2.3](parts/02-polymorphism/2.3-liskov-in-plain-words.md).
- **A subclass raising a new exception type escapes every existing handler** —
  [2.3](parts/02-polymorphism/2.3-liskov-in-plain-words.md).
- **`raise NotImplementedError` in a concrete subclass means the hierarchy is upside down** —
  [2.3](parts/02-polymorphism/2.3-liskov-in-plain-words.md).
- **One underscore enforces nothing at all** —
  [3.1](parts/03-encapsulation/3.1-public-protected-private.md).
- **A method returning the object's own list hands out a way to mutate it** —
  [3.1](parts/03-encapsulation/3.1-public-protected-private.md),
  [3.3](parts/03-encapsulation/3.3-the-invariant.md).
- **Two underscores rename rather than hide, and only inside a class body** —
  [3.2](parts/03-encapsulation/3.2-name-mangling.md).
- **A subclass setting `self.__x` does not override the parent's `__x`** —
  [3.2](parts/03-encapsulation/3.2-name-mangling.md).
- **Two stored fields that must agree will eventually disagree** —
  [3.3](parts/03-encapsulation/3.3-the-invariant.md).
- **Constructor validation is bypassed by the next assignment** —
  [3.3](parts/03-encapsulation/3.3-the-invariant.md).
- **`@abstractmethod` without an `ABC` base does nothing at all** —
  [4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md).
- **`@abstractmethod` above `@property` fails at import with a message about `__isabstractmethod__`** —
  [4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md).
- **`abc` checks names and never behaviour** —
  [4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md).
- **A loader that iterates its reader works once and returns nothing the second time** —
  [4.2](parts/04-abstraction/4.2-the-loader-family.md).
- **A base class larger than its children has become the program** —
  [4.2](parts/04-abstraction/4.2-the-loader-family.md).
- **`isinstance` against a `Protocol` needs `@runtime_checkable` and checks names only** —
  [4.3](parts/04-abstraction/4.3-protocol-versus-abc.md).
- **A `Protocol` enforces nothing at run time** —
  [4.3](parts/04-abstraction/4.3-protocol-versus-abc.md).

---

## §8 Verify before you code

Fetched **2026-09-01**. Today is the language and two standard-library modules, so the language
reference and the PEPs are the authority:

- <https://docs.python.org/3/tutorial/classes.html#inheritance> — the tutorial's treatment of
  inheritance, `isinstance`, `issubclass` and multiple inheritance, which is
  [1.1](parts/01-inheritance/1.1-one-form-that-starts-from-another.md).
- <https://docs.python.org/3/library/functions.html#super> — `super()`, including the sentence that
  it returns a proxy delegating to a parent **or sibling** class, which is the wording
  [1.3](parts/01-inheritance/1.3-the-mro.md) is built on.
- <https://www.python.org/download/releases/2.3/mro/> — *The Python 2.3 Method Resolution Order*
  (2003), still the canonical explanation of C3 linearisation and of why the naive order was
  replaced.
- <https://docs.python.org/3/tutorial/classes.html#private-variables> — the tutorial's own statement
  that there is no true private, plus the name-mangling rule, which is
  [3.1](parts/03-encapsulation/3.1-public-protected-private.md) and
  [3.2](parts/03-encapsulation/3.2-name-mangling.md).
- <https://docs.python.org/3/library/abc.html> — `ABC`, `ABCMeta`, `abstractmethod`, and the note
  about decorator ordering that [4.1](parts/04-abstraction/4.1-abc-and-abstractmethod.md)'s failure
  section demonstrates.
- <https://peps.python.org/pep-0544/> — *Protocols: Structural subtyping (static duck typing)*
  (2017), which added `Protocol` and `@runtime_checkable`, and is
  [4.3](parts/04-abstraction/4.3-protocol-versus-abc.md).
- <https://docs.python.org/3/library/typing.html#typing.Protocol> — the current API, including the
  warning that a run-time protocol check looks only at the presence of methods.
- `uv run ruff rule B024` and `uv run ruff rule B027` — the two `bugbear` rules about abstract base
  classes: a class inheriting `ABC` with no abstract methods, and an empty method on an ABC that is
  not marked abstract. Read them from the linter you have installed.

---

## §9 Say it in an interview

> "Inheritance is the strongest coupling the language offers, so I use the 'is-a' test before I use
> it: a subclass has to be usable anywhere the base is, without the caller knowing which it got. That
> is the substitution rule, and in practice it means a subclass may accept more and promise more but
> never less — no extra required argument, no returning `None` where a list was promised, and no new
> exception types, because the caller's `except` was written against the base. The one that catches
> people is that Python checks *none* of this: an override with a completely different signature
> imports fine, and a misspelled override silently leaves the base's version running, so the defences
> are a documented contract on the base and one parametrised test that runs the same assertions
> against every subclass. `super()` is worth being precise about too — it is the next class in the
> MRO, not the parent, which only matters once mixins are involved, and then it matters a lot: one
> class that does not call `super()` truncates the chain and the missing behaviour is impossible to
> find. For anything that is not genuinely an 'is-a', I compose: the object *holds* its collaborator
> and takes it in `__init__`, which is what makes the offline test possible, because you can pass a
> fake. And duck typing is why that fake needs no base class at all — Python looks up the method on
> the object, so most `isinstance` checks are refusing objects that would have worked. On the
> abstraction side, an abstract base class earns its place by refusing to be built: a subclass
> missing `load` fails at construction with a message naming the method, rather than raising
> `NotImplementedError` half way through a batch. It checks names and not behaviour, so the contract
> still lives in the docstring. And when I am describing something I *accept* rather than something I
> build — a reader that might be a file, a `StringIO` or a test double — that is a `Protocol`, because
> nobody else's class is ever going to inherit from mine."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green,
`src/setu/loaders/` holds a base that refuses to be instantiated and two loaders that pass the same
six parametrised tests, and you have **watched six tests stay green through a real defect** — the
reader iterated instead of read, in §5 — not when a particular amount of time has passed. Then:

```bash
./m done 13
```

Tomorrow is decorators: `@timed` and `@retry(3)`, built from the closures of Day 10 and reused in
every phase after this one. The loaders are the first thing they wrap.
