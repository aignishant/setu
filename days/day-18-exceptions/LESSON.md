---
day: 18
phase: 2
phase_name: "Advanced Python (Module 2)"
title: "Day 18 — Exceptions and custom error types"
ids: ["PY-22"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 19
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 18 — Exceptions and custom error types

**Phase 2 · Advanced Python · Module 2** · `PY-22` `try`/`except`/`else`/`finally` and custom exceptions.
The plan's named example is **`class RateLimited(Exception)` — the one every provider call raises later**,
and by the end of today it exists in `src/setu/errors.py` with the attribute a retry loop needs.

> **Yesterday:** how the files you have been writing find each other — imports, packages, `__init__.py`,
> and the layer rule that says `errors.py` may import nothing of ours.
> **Today:** what `raise` actually does, which type to raise, how to design a family of your own, and the
> handler shapes that hide bugs.
> **Tomorrow:** typing, dataclasses, Pydantic v2 and concurrency — where `ExceptionGroup` stops being
> trivia and starts arriving from `asyncio.TaskGroup`.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

You are at the post office counter with a parcel.

Everything today happens at that counter.

- **The clerk weighs it and it is over the limit.** She stops. She does not take your money, print the
  label, or put it in the bag — every step that had not happened yet does not happen — and she hands the
  parcel back with a reason.
- **Three different things can go wrong**, and they are not the same kind of wrong: the parcel is too
  heavy, the form has no address, or the system is down. You repack, you write, or you go home. Nobody is
  helped by "there was a problem".
- **There is a rhythm to the counter**: weigh it, say so if it failed, print the label if it did not, and
  clear the counter whatever happened. Four jobs, not two — and printing the label is not part of
  "weighing", which matters the day the printer jams.
- **Somebody wedged the shutter open** so it would stop sliding down, and it stayed open at closing time
  and through the fire drill. The wedge does not know the difference between the shutter falling and the
  shutter being brought down on purpose.
- **The slip she hands back has the weight and the limit on it**, not just the word "rejected", because
  otherwise you are back at the counter twice.
- **The problems sheet is grouped, not alphabetical** — parcel problems here, system problems there — so a
  trainee can be told two rules instead of seven, and the sheet can grow a row without retraining anybody.
- **The card machine's slip says "try again in 30 seconds"**, and thirty is a number you can act on. The
  branch that prints "please try again later" throws that number away between the till and the customer.
- **The counter's own sentences have not changed in twenty years** while the scales, the printer and the
  card machine were all replaced twice. The clerk translates. She does not shout "E-04" over the counter.
- **The problems tray is counted, not read**, and for a month it held one genuinely bad parcel a day and
  two forms the clerk had filled in wrongly herself. The number stayed normal, so nobody looked.
- **Two ways to get a parcel into the last van**: walk out, check there is room, walk back for the parcel,
  walk out again and find it full — or carry the parcel out once and try.
- **The day book said "card machine — 14:20" for months** and was useless when somebody finally had to
  work out why. The receipt the machine printed was on the counter for four seconds, every time.
- **The Bristol round came back with three problems at once**, and the driver handed over all three slips
  clipped together rather than the first one he found.
- **And somebody asks whether a parcel has arrived for them, and it has not.** Nobody writes an incident
  report. *Not yet* is an answer; *no address on this parcel* is the absence of one.

One thing before any code: **exceptions are not a separate language feature.** An exception is an object
([Day 4](../day-04-objects/parts/01-objects/1.1-identity-type-value.md)) of a class
([Day 12](../day-12-classes/parts/01-the-blank-form/1.1-a-class-is-a-blank-form.md)) in an inheritance
tree ([Day 13](../day-13-inheritance-and-abstraction/parts/01-inheritance/1.3-the-mro.md)), and `with` was
already `try` / `finally` ([Day 16](../day-16-files-and-context-managers/parts/04-context-managers/4.2-try-finally-is-what-with-is.md)).
What is new is the control flow, and the judgement about who should be told what.

---

## §2 The map

**What the section numbers mean today.** One ID, so the sections follow the plan's `lab (1 ID)` split —
mechanism, then behaviour, then design, then production use. **1.x** is the machinery: raising, catching,
and the four clauses. **2.x** is the hierarchy: which type, and how to translate between them. **3.x** is
designing your own family, which is today's build. **4.x** is the handler shapes that separate a codebase
you can debug from one you cannot.

### Section 1 — raising and catching

| Part | What it answers | Level |
|---|---|---|
| [1.1 What raising does](parts/01-raising-and-catching/1.1-what-raising-does.md) | Where does the rest of the function go? | `foundation` |
| [1.2 `try` / `except`, and catching by type](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md) | Why did my second `except` never run? | `foundation` |
| [1.3 `else` and `finally`](parts/01-raising-and-catching/1.3-else-and-finally.md) | Why is moving one line into `else` a bug fix? | `working` |
| [1.4 The bare `except`](parts/01-raising-and-catching/1.4-the-bare-except.md) | Why can I not stop this with Ctrl-C? | `working` |
| [1.5 What the object carries](parts/01-raising-and-catching/1.5-the-exception-object.md) | What is in an exception besides its message? | `working` |

### Section 2 — the hierarchy

| Part | What it answers | Level |
|---|---|---|
| [2.1 Catching catches subclasses](parts/02-the-hierarchy/2.1-catching-catches-subclasses.md) | How does one clause catch fifteen types? | `foundation` |
| [2.2 Which built-in to raise](parts/02-the-hierarchy/2.2-which-built-in-to-raise.md) | `TypeError` or `ValueError`? | `working` |
| [2.3 `raise ... from`](parts/02-the-hierarchy/2.3-raise-from-and-the-chain.md) | What are those two sentences in a traceback? | `working` |
| [2.4 Re-raising](parts/02-the-hierarchy/2.4-re-raising.md) | What does a bare `raise` do that `raise error` does not? | `production` |

### Section 3 — your own

| Part | What it answers | Level |
|---|---|---|
| [3.1 One base class per project](parts/03-your-own/3.1-one-base-class-per-project.md) | When is a custom exception worth defining? | `working` |
| [3.2 An exception that carries data](parts/03-your-own/3.2-an-exception-that-carries-data.md) | How does the retry delay reach the retry loop? | `production` |
| [3.3 The message is an interface](parts/03-your-own/3.3-the-message-is-an-interface.md) | What does a good message say? | `production` |
| [3.4 Translating at the boundary](parts/03-your-own/3.4-translate-at-the-boundary.md) | Which exceptions should never escape my module? | `production` |

### Section 4 — in anger

| Part | What it answers | Level |
|---|---|---|
| [4.1 The `except` that was too wide](parts/04-in-anger/4.1-the-except-that-was-too-wide.md) | How does a typo become "a bad row"? | `production` |
| [4.2 Ask forgiveness or ask permission](parts/04-in-anger/4.2-eafp-and-lbyl.md) | Why is checking first not safer? | `production` |
| [4.3 `logging.exception`](parts/04-in-anger/4.3-logging-exception.md) | What does `log.error(f'{e}')` throw away? | `production` |
| [4.4 `pytest.raises`](parts/04-in-anger/4.4-pytest-raises.md) | How do you test a refusal? | `production` |
| [4.5 `ExceptionGroup` and `except*`](parts/04-in-anger/4.5-exception-groups.md) | What happens when three things fail at once? | `production` |
| [4.6 When not to raise](parts/04-in-anger/4.6-when-not-to-raise.md) | Is "not found" an error? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language itself plus `logging`, `json` and `traceback` from
the standard library, and `pytest`, which is already a development dependency. Module 2 is still the
language; the first new dependency is Day 19.

```bash
mkdir -p tests notebooks
touch src/setu/errors.py tests/test_errors.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-18-scratch.ipynb

# yesterday's layer rule decides where errors.py sits - check it is still green first
uv run python -m pytest tests/test_layout.py -q

# the twelve facts the day is built on, before any part names them
uv run python -c "
def weigh(g):
    if g > 2000:
        raise ValueError('too heavy for this counter')
    return g

try:
    weigh(5000)
except ValueError as error:
    kept = error
print('1 raising stops the function :', repr(kept), '<- part 1.1')
print('2 the as-name is gone now    :', 'error' in dir(), '<- part 1.2')
print('3 str loses the type         :', f'{kept}', '| repr keeps it:', f'{kept!r}', '<- part 1.5')
def f():
    try:
        return 'returned'
    finally:
        print('4 finally runs on every path :', end=' ')
print(f'{f()} - even past a return <- part 1.3')
print('5 a bare except catches exit :', not issubclass(SystemExit, Exception), '<- part 1.4')
print('6 catching catches subclasses:', issubclass(FileNotFoundError, OSError), '<- part 2.1')
print('7 the tree, one branch       :', ' -> '.join(c.__name__ for c in FileNotFoundError.__mro__[:-1]), '<- part 2.1')
try:
    int('heavy')
except ValueError as e:
    print('8 what int() raises          :', type(e).__name__, '|', e, '<- part 2.2')
try:
    try:
        int('heavy')
    except ValueError:
        raise RuntimeError('wrapped')
except RuntimeError as e:
    print('9 chaining is automatic      : cause', e.__cause__, '| context', type(e.__context__).__name__, '<- part 2.3')
try:
    open('no-such-file.txt')
except OSError as e:
    print('10 exceptions carry data     :', e.errno, e.filename, '<- part 3.2')
g = ExceptionGroup('two failed', [ValueError('a'), KeyError('b')])
print('11 groups hold several       :', len(g.exceptions), 'inside; isinstance ValueError is', isinstance(g, ValueError), '<- part 4.5')
print('12 the raising twin exists   : find gives', 'ab'.find('z'), 'where index() raises <- part 4.6')
"

# the two rules that catch today's headline mistakes, read from the installed linter
uv run ruff rule E722
uv run ruff rule B012
```

Expected from the twelve-fact block on 2026-09-02:

```
1 raising stops the function : ValueError('too heavy for this counter') <- part 1.1
2 the as-name is gone now    : False <- part 1.2
3 str loses the type         : too heavy for this counter | repr keeps it: ValueError('too heavy for this counter') <- part 1.5
4 finally runs on every path : returned - even past a return <- part 1.3
5 a bare except catches exit : True <- part 1.4
6 catching catches subclasses: True <- part 2.1
7 the tree, one branch       : FileNotFoundError -> OSError -> Exception -> BaseException <- part 2.1
8 what int() raises          : ValueError | invalid literal for int() with base 10: 'heavy' <- part 2.2
9 chaining is automatic      : cause None | context ValueError <- part 2.3
10 exceptions carry data     : 2 no-such-file.txt <- part 3.2
11 groups hold several       : 2 inside; isinstance ValueError is False <- part 4.5
12 the raising twin exists   : find gives -1 where index() raises <- part 4.6
```

**Line 2 is worth a second look.** The name `error` bound by `as` no longer exists after the block, which
is why line 1 had to save it as `kept` ([1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md)).

| What | Where it comes from | Part |
|---|---|---|
| `raise`, stack unwinding, reading a traceback | language | [1.1](parts/01-raising-and-catching/1.1-what-raising-does.md) |
| `try` / `except`, type matching, tuples of types | language | [1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md) |
| `else`, `finally`, `B012` | language + `ruff` | [1.3](parts/01-raising-and-catching/1.3-else-and-finally.md) |
| `BaseException`, `SystemExit`, `KeyboardInterrupt`, `E722` | language + `ruff` | [1.4](parts/01-raising-and-catching/1.4-the-bare-except.md) |
| `args`, `__traceback__`, `add_note`, *PEP 678* | language | [1.5](parts/01-raising-and-catching/1.5-the-exception-object.md) |
| `traceback.format_exception` | standard library | [1.5](parts/01-raising-and-catching/1.5-the-exception-object.md) |
| inheritance and the MRO | already met on [Day 13](../day-13-inheritance-and-abstraction/parts/01-inheritance/1.3-the-mro.md) | [2.1](parts/02-the-hierarchy/2.1-catching-catches-subclasses.md) |
| the built-in exception tree | standard library | [2.2](parts/02-the-hierarchy/2.2-which-built-in-to-raise.md) |
| `__cause__`, `__context__`, *PEP 3134* | language | [2.3](parts/02-the-hierarchy/2.3-raise-from-and-the-chain.md) |
| bare `raise`, log-and-re-raise | language | [2.4](parts/02-the-hierarchy/2.4-re-raising.md) |
| `__init__`, `super()`, `__str__` | already met on [Day 15](../day-15-constructors-and-dunders/parts/03-the-dunders/3.2-repr-and-str.md) | [3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md) |
| `pickle`, and why `args` must replay | standard library | [3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md) |
| the leaf-module rule | already decided on [Day 17](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md) | [3.1](parts/03-your-own/3.1-one-base-class-per-project.md) |
| `logging`, `exc_info`, `%s` arguments | standard library | [4.3](parts/04-in-anger/4.3-logging-exception.md) |
| `pytest.raises`, `match=`, `caught.value` | `pytest==9.1.1` | [4.4](parts/04-in-anger/4.4-pytest-raises.md) |
| `ExceptionGroup`, `except*`, *PEP 654* | language | [4.5](parts/04-in-anger/4.5-exception-groups.md) |
| `dict.get`, `str.find`, sentinels | standard library | [4.6](parts/04-in-anger/4.6-when-not-to-raise.md) |

---

## §4 Build brief

**One new module and one test file.** `src/setu/errors.py` is the project's exception family — the first
module deliberately designed as a **leaf**: it imports nothing of ours, and everything else may import it
([Day 17, 4.4](../day-17-modules-and-packages/parts/04-the-project/4.4-designing-the-public-surface.md)).

**1. `src/setu/errors.py`** — the family, and one function that translates.

```python
"""Every exception this project raises on purpose.

A LEAF module: it imports nothing from setu, so everything may import it and no
cycle can start here (Day 17, part 4.4). Keep it that way.
"""

from __future__ import annotations


class SetuError(Exception):
    """Base class for everything this project raises deliberately.

    Inherits from Exception, NOT from a built-in like ConnectionError, so that
    existing handlers elsewhere do not catch our exceptions by accident
    (part 3.1).
    """


class ConfigError(SetuError):
    """A required setting is missing or unusable."""

    # TODO(me): carry the variable NAME, never its value (part 3.3 - a secret in
    # a message reaches every log sink there is, Principle 11). Give it a
    # `variable` attribute and a __str__ that names it, and say in a comment
    # which of part 3.3's four questions each part of the message answers.


class ProviderError(SetuError):
    """A model provider could not serve the request."""


class RateLimited(ProviderError):
    """A provider asked us to slow down, and said for how long."""

    def __init__(self, provider: str, retry_after: float) -> None:
        # TODO(me): super().__init__ with the FIELDS, not a formatted message,
        # so args replays through cls(*args) and this survives pickling when the
        # work moves into a process pool (part 3.2). Then store both as
        # attributes with the names a retry loop will type.
        raise NotImplementedError

    def __str__(self) -> str:
        # TODO(me): the readable sentence, computed from the attributes so it
        # cannot drift out of step with them. Include the number (part 3.3).
        raise NotImplementedError


def retry_delay(error: Exception, *, default: float = 5.0) -> float:
    """How long to wait before retrying, from the exception itself.

    This is the function Day 6's retry loop and Day 14's @retry should have been
    calling all along, instead of guessing (part 3.2).
    """
    # TODO(me): if it is a RateLimited, return its retry_after. Otherwise return
    # the default. Do NOT parse the message (part 3.3's third failure), and do
    # NOT use hasattr as a stand-in for the type check - say in a comment why
    # isinstance is the right question here (part 2.1).
    raise NotImplementedError
```

**2. `src/setu/manifest.py`** — the translation from [3.4](parts/03-your-own/3.4-translate-at-the-boundary.md),
which is where `errors.py` gets used rather than merely defined.

```python
"""Load a JSONL manifest, or raise ManifestError. Never leaks json or OSError."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from setu.errors import SetuError


class ManifestError(SetuError):
    """The manifest could not be loaded, or is not usable."""

    # TODO(me): carry `path` and an optional `line`. A missing file has no line;
    # a malformed record does. Decide what __str__ says in each case and write
    # the decision in the docstring.


def load_manifest(path: Path) -> list[dict[str, Any]]:
    """Return the records. Raises ManifestError and nothing else."""
    # TODO(me): two translations, both `from error` (part 2.3):
    #
    #   - OSError around the read           -> ManifestError(path)
    #   - json.JSONDecodeError around ONE   -> ManifestError(path, number)
    #     json.loads, inside the loop
    #
    # Catch those two NARROW types and nothing wider - an AttributeError from a
    # typo of ours must travel (part 3.4). enumerate(..., start=1), because
    # json's own message always says "line 1" whatever line it was.
    raise NotImplementedError
```

**3. Decide, in writing, what `retry_delay` does with a `RateLimited` whose `retry_after` is absurd.**
Two sentences in the docstring. A provider that says "retry in 3600 seconds" is asking you to block for an
hour; capping it is a policy, and so is not capping it. An undecided answer is the one that surprises
somebody at midnight.

**4. Reproduce the eight traps in the notebook, then throw the notebook away.** In
`notebooks/day-18-scratch.ipynb`, in this order:

- Return `None` on failure instead of raising, and read where the error surfaces
  ([1.1](parts/01-raising-and-catching/1.1-what-raising-does.md)).
- Write `except Exception:` above `except ValueError:` and watch the second never run
  ([1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md)).
- Put a `return` inside a `finally` and watch an exception vanish
  ([1.3](parts/01-raising-and-catching/1.3-else-and-finally.md)).
- Catch `sys.exit(3)` with a bare `except:` and check the process exit code
  ([1.4](parts/01-raising-and-catching/1.4-the-bare-except.md)).
- Raise inside a handler with and without `from`, and read both middle sentences
  ([2.3](parts/02-the-hierarchy/2.3-raise-from-and-the-chain.md)).
- Log and swallow, then log and re-raise, and compare what the caller gets
  ([2.4](parts/02-the-hierarchy/2.4-re-raising.md)).
- Pickle an exception whose `super().__init__` got a formatted string
  ([3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md)).
- Catch an `ExceptionGroup` with a plain `except ValueError:` and watch it not match
  ([4.5](parts/04-in-anger/4.5-exception-groups.md)).

**The notebook is not committed** (Principle 6); the two modules and their tests are.

**5. Add `errors` and `manifest` to `LAYERS` in `src/setu/layout.py`.** `errors` is layer 0 — a leaf.
`manifest` imports it, so it is not. Yesterday's test is what will tell you if you get it backwards.

---

## §5 The eval that must be able to fail

Create `tests/test_errors.py`. Every test runs offline, writes only to `tmp_path`
([Day 2, 3.2](../day-02-quality-gate/parts/03-pytest/3.2-fixtures-and-tmp-path.md)), and belongs in
`./m check`.

```python
"""Day 18: what an exception family must promise, and what a handler must not do."""

from __future__ import annotations

import json
import pickle

import pytest

from setu.errors import ConfigError, ProviderError, RateLimited, SetuError, retry_delay
from setu.manifest import ManifestError, load_manifest


def test_every_error_is_a_setu_error() -> None:
    """Part 3.1: the base class is worthless if something forgets to inherit."""
    # TODO(me): assert issubclass for each of ConfigError, ProviderError,
    # RateLimited, ManifestError. One line each, and this is the test that
    # catches a new exception class defined under the wrong parent.
    raise NotImplementedError


def test_rate_limited_is_a_provider_error_but_not_a_connection_error() -> None:
    """Part 2.1: where you attach it decides who catches it."""
    # TODO(me): two asserts. The second one - NOT a ConnectionError - is the
    # one that documents a deliberate decision rather than an accident.
    raise NotImplementedError


def test_rate_limited_carries_the_delay() -> None:
    """Part 3.2: the number the retry loop needs."""
    # TODO(me): pytest.raises with `as caught`, then assert on
    # caught.value.retry_after and caught.value.provider. Assert the ATTRIBUTES,
    # not the message (part 4.4).
    raise NotImplementedError


def test_rate_limited_survives_a_round_trip() -> None:
    """Part 3.2: exceptions cross process boundaries, and args must replay."""
    # TODO(me): pickle.loads(pickle.dumps(error)) and assert retry_after
    # survived. This is the test that fails if super().__init__ was handed a
    # formatted string - and it is the only one that would.
    raise NotImplementedError


def test_str_is_readable_and_names_the_number() -> None:
    """Part 3.3: the message a human reads at 3am."""
    # TODO(me): assert the provider name and the number both appear in str().
    # A loose assertion on purpose - part 3.3 says do not freeze the wording.
    raise NotImplementedError


def test_config_error_never_contains_the_value() -> None:
    """Part 3.3, Principle 11: a secret in a message reaches every log sink."""
    # TODO(me): build a ConfigError for a variable whose value is 'sk-secret',
    # and assert that string is NOT in str(error) or repr(error). If your design
    # never receives the value, say so in a comment - that is a better answer
    # than a passing assertion.
    raise NotImplementedError


def test_retry_delay_reads_the_exception() -> None:
    """Part 3.2: the guess replaced by an instruction."""
    # TODO(me): retry_delay(RateLimited('groq', 30.0)) == 30.0, and
    # retry_delay(ValueError('x')) == the default.
    raise NotImplementedError


def test_retry_delay_does_not_parse_the_message() -> None:
    """Part 3.3: the message is not an API."""
    # TODO(me): build a plain ProviderError whose message says 'retry in 30s'
    # and assert retry_delay returns the DEFAULT, not 30. A version written with
    # a regex passes every other test in this file.
    raise NotImplementedError


def test_load_manifest_reports_the_files_line_number(tmp_path) -> None:
    """Part 3.4: json always says line 1, whatever line it was."""
    # TODO(me): a file whose SECOND line is malformed. Assert caught.value.line
    # is 2. Then assert the json message says line 1 - both are true, and the
    # comment should say why.
    raise NotImplementedError


def test_load_manifest_keeps_the_cause(tmp_path) -> None:
    """Part 2.3: `from error`, or the position is gone."""
    # TODO(me): assert isinstance(caught.value.__cause__, json.JSONDecodeError).
    # A translation written without `from` fails only this test.
    raise NotImplementedError


def test_load_manifest_never_leaks_a_json_exception(tmp_path) -> None:
    """Part 3.4: the module's promise, made executable."""
    # TODO(me): pytest.raises(ManifestError) for a malformed file AND for a
    # missing one. Say in a comment why this is not the same assertion as the
    # test above.
    raise NotImplementedError


def test_a_bug_is_not_translated(tmp_path, monkeypatch) -> None:
    """Part 3.4: catching Exception at a boundary turns our bugs into data problems."""
    # TODO(me): monkeypatch something inside load_manifest to raise
    # AttributeError, and assert it escapes as an AttributeError rather than as
    # a ManifestError. This is the test that fails the day somebody widens the
    # except clause to Exception.
    raise NotImplementedError


def test_the_handler_does_not_swallow(tmp_path) -> None:
    """Part 2.4: the only test that can see a missing `raise`."""
    # TODO(me): pytest.raises around a load of a malformed file. Every test
    # about return values passes for a version that catches and returns [].
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_errors.py -v
```

Then implement, then **break each one on purpose**:

- Make `RateLimited` inherit from `ConnectionError` instead of `ProviderError`. **Two tests go red**, and
  say out loud which existing handlers in a real codebase would silently start catching it.
- Pass a formatted string to `super().__init__`. **Only the pickle test goes red** — every value assertion
  still passes, which is why that test exists.
- Delete `__str__`. The readable-message test goes red and everything else stays green; read what
  `str(error)` becomes.
- Write `retry_delay` with a regular expression over the message. `test_retry_delay_does_not_parse_the_message`
  goes red and `test_retry_delay_reads_the_exception` stays green.
- Drop `from error` in `load_manifest`. **Only the cause test goes red.** The line number is still right,
  which is what makes the omission easy to merge.
- Change `enumerate(...)` to start at 0. The line-number test goes red by one, which is the whole reason
  it asserts a number rather than "a line number exists".
- Widen `except json.JSONDecodeError` to `except Exception`. `test_a_bug_is_not_translated` goes red and
  nothing else notices.
- Put the variable's **value** in `ConfigError`'s message. One test goes red, and it is the only thing
  standing between a secret and every log sink you have (Principle 11).
- **Break it and watch every test stay GREEN** — make `load_manifest` catch `ManifestError` at the end and
  `return []`, **and** delete `test_the_handler_does_not_swallow`. Every remaining test passes: the file
  loads, the good path is unchanged, and every caller now believes a malformed manifest was empty.
  Restore the test, watch it go red, and say out loud what it was protecting.

That last item is the most important line in this section. Every other test asserts something about an
exception that was raised; only one asserts that it got out.

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — nothing today leaves your machine |
| New packages | **0** — Module 2 is still the language |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |
| Disk | a few kilobytes in `tmp_path`, deleted by `pytest` |

Today is the day that makes tomorrow's budget *enforceable*. `retry_delay` is what turns a guessed sleep
into the number the provider actually asked for — and a retry loop that guesses too short is the single
easiest way to spend a day's free-tier allowance before lunch
([3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md)).

---

## §7 Traps

- **`raise` abandons the rest of the function, cleanup included** —
  [1.1](parts/01-raising-and-catching/1.1-what-raising-does.md).
- **Returning `None` on failure moves the error away from its cause** —
  [1.1](parts/01-raising-and-catching/1.1-what-raising-does.md).
- **A `print` in an error path is a note to somebody who is not reading** —
  [1.1](parts/01-raising-and-catching/1.1-what-raising-does.md).
- **`raise "a string"` is a `TypeError`: exceptions must derive from `BaseException`** —
  [1.1](parts/01-raising-and-catching/1.1-what-raising-does.md).
- **A broad `except` above a narrow one makes the narrow one dead code, silently** —
  [1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md).
- **The name bound by `as` is deleted at the end of the block** —
  [1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md).
- **A wide `try` makes the handler's claim false for most of its contents** —
  [1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md).
- **Matching on the message text freezes the wording forever** —
  [1.2](parts/01-raising-and-catching/1.2-try-except-and-catching-by-type.md).
- **Success work left in the `try` gets caught by the failure handler** —
  [1.3](parts/01-raising-and-catching/1.3-else-and-finally.md).
- **A `return` inside `finally` discards the exception in flight (`ruff` B012)** —
  [1.3](parts/01-raising-and-catching/1.3-else-and-finally.md).
- **A `finally` that raises replaces the real error as the headline** —
  [1.3](parts/01-raising-and-catching/1.3-else-and-finally.md).
- **`finally` does not run when the process is killed** —
  [1.3](parts/01-raising-and-catching/1.3-else-and-finally.md).
- **A bare `except:` catches Ctrl-C, so a loop cannot be stopped (`ruff` E722)** —
  [1.4](parts/01-raising-and-catching/1.4-the-bare-except.md).
- **A bare `except:` turns `sys.exit(3)` into exit code 0** —
  [1.4](parts/01-raising-and-catching/1.4-the-bare-except.md).
- **`sys.exit()` works by raising, which is why it is catchable at all** —
  [1.4](parts/01-raising-and-catching/1.4-the-bare-except.md).
- **`str(error)` loses the type; two different bugs log identically** —
  [1.5](parts/01-raising-and-catching/1.5-the-exception-object.md).
- **`__notes__` does not exist until `add_note` is called once** —
  [1.5](parts/01-raising-and-catching/1.5-the-exception-object.md).
- **Keeping exception objects keeps every frame's locals alive** —
  [1.5](parts/01-raising-and-catching/1.5-the-exception-object.md).
- **`KeyError` is not an `IndexError`; they are siblings** —
  [2.1](parts/02-the-hierarchy/2.1-catching-catches-subclasses.md).
- **`UnicodeDecodeError` is a `ValueError`, so `except ValueError` catches encoding failures** —
  [2.1](parts/02-the-hierarchy/2.1-catching-catches-subclasses.md).
- **Inheriting from a built-in enrols you in everybody else's handlers** —
  [2.1](parts/02-the-hierarchy/2.1-catching-catches-subclasses.md).
- **`raise Exception(...)` forces every caller to catch broadly** —
  [2.2](parts/02-the-hierarchy/2.2-which-built-in-to-raise.md).
- **`NotImplemented` is a value; `NotImplementedError` is the class** —
  [2.2](parts/02-the-hierarchy/2.2-which-built-in-to-raise.md).
- **`ValueError` where `TypeError` belonged sends the investigation to the data** —
  [2.2](parts/02-the-hierarchy/2.2-which-built-in-to-raise.md).
- **Raising inside a handler without `from` labels the cause as coincidence** —
  [2.3](parts/02-the-hierarchy/2.3-raise-from-and-the-chain.md).
- **`from None` hides the position information you will want** —
  [2.3](parts/02-the-hierarchy/2.3-raise-from-and-the-chain.md).
- **`raise error` adds a frame to the traceback that nothing caused** —
  [2.4](parts/02-the-hierarchy/2.4-re-raising.md).
- **A bare `raise` outside a handler is `RuntimeError: No active exception to reraise`** —
  [2.4](parts/02-the-hierarchy/2.4-re-raising.md).
- **Log-and-swallow returns `None` and moves the failure somewhere unrelated** —
  [2.4](parts/02-the-hierarchy/2.4-re-raising.md).
- **A custom exception that forgets to inherit cannot be raised** —
  [3.1](parts/03-your-own/3.1-one-base-class-per-project.md).
- **A class that nobody catches separately is a message, not a type** —
  [3.1](parts/03-your-own/3.1-one-base-class-per-project.md).
- **A formatted message in `super().__init__` makes the exception un-picklable** —
  [3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md).
- **Keyword-only constructor parameters break the `cls(*args)` rebuild** —
  [3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md).
- **With fields in `args` and no `__str__`, the log line is a tuple** —
  [3.2](parts/03-your-own/3.2-an-exception-that-carries-data.md).
- **A secret in a message reaches every log sink, tracker and ticket** —
  [3.3](parts/03-your-own/3.3-the-message-is-an-interface.md).
- **A message without the value cannot be searched for in a million rows** —
  [3.3](parts/03-your-own/3.3-the-message-is-an-interface.md).
- **Code that parses a message breaks on a wording improvement** —
  [3.3](parts/03-your-own/3.3-the-message-is-an-interface.md).
- **Leaking a dependency's exception puts it in your public interface** —
  [3.4](parts/03-your-own/3.4-translate-at-the-boundary.md).
- **Translating a bug reports a typo as a data problem** —
  [3.4](parts/03-your-own/3.4-translate-at-the-boundary.md).
- **Re-wrapping your own exception adds a traceback layer and no information** —
  [3.4](parts/03-your-own/3.4-translate-at-the-boundary.md).
- **`except Exception` counts your bugs as bad rows, and the number looks normal** —
  [4.1](parts/04-in-anger/4.1-the-except-that-was-too-wide.md).
- **A broad handler makes a function's failure path untestable** —
  [4.1](parts/04-in-anger/4.1-the-except-that-was-too-wide.md).
- **A broad handler in a loop reports an outage as bad data** —
  [4.1](parts/04-in-anger/4.1-the-except-that-was-too-wide.md).
- **`if exists()` then act still needs the handler — the gap is real** —
  [4.2](parts/04-in-anger/4.2-eafp-and-lbyl.md).
- **A duplicated condition in the caller drifts from the one in the callee** —
  [4.2](parts/04-in-anger/4.2-eafp-and-lbyl.md).
- **A check that is not the operation cannot guarantee the operation** —
  [4.2](parts/04-in-anger/4.2-eafp-and-lbyl.md).
- **`log.error(f'{e}')` records no traceback at all** —
  [4.3](parts/04-in-anger/4.3-logging-exception.md).
- **`log.exception` outside a handler prints `NoneType: None`** —
  [4.3](parts/04-in-anger/4.3-logging-exception.md).
- **An f-string in a log message makes one issue per value in a tracker** —
  [4.3](parts/04-in-anger/4.3-logging-exception.md).
- **A `pytest.raises` block with two statements makes the second dead** —
  [4.4](parts/04-in-anger/4.4-pytest-raises.md).
- **`match=` anchored to the whole message turns rewording into a breaking change** —
  [4.4](parts/04-in-anger/4.4-pytest-raises.md).
- **`caught` is an `ExceptionInfo`; the exception is `caught.value`** —
  [4.4](parts/04-in-anger/4.4-pytest-raises.md).
- **`except ValueError:` does not catch an `ExceptionGroup` of `ValueError`s** —
  [4.5](parts/04-in-anger/4.5-exception-groups.md).
- **`except*` runs every matching clause, not the first** —
  [4.5](parts/04-in-anger/4.5-exception-groups.md).
- **`return`, `break` and `continue` are `SyntaxError`s inside `except*`** —
  [4.5](parts/04-in-anger/4.5-exception-groups.md).
- **A group with one member hides the day there are two** —
  [4.5](parts/04-in-anger/4.5-exception-groups.md).
- **A function that falls off the end returns `None` and told nobody** —
  [4.6](parts/04-in-anger/4.6-when-not-to-raise.md).
- **A sentinel that could be a real value is a bug waiting** —
  [4.6](parts/04-in-anger/4.6-when-not-to-raise.md).
- **A returned error code can be ignored; an exception cannot** —
  [4.6](parts/04-in-anger/4.6-when-not-to-raise.md).

---

## §8 Verify before you code

Fetched **2026-09-02**. Today is the language plus three standard-library modules and `pytest`, so the
language reference, the library reference and the PEPs are the authority:

- <https://docs.python.org/3/library/exceptions.html> — the full built-in exception tree as an indented
  list, plus what each one means. Worth reading front to back once.
- <https://docs.python.org/3/tutorial/errors.html> — the tutorial's chapter, which is where `else`,
  `finally`, chaining and exception groups are each shown in about ten lines.
- <https://docs.python.org/3/reference/compound_stmts.html#the-try-statement> — the language reference's
  exact rules for clause order, `else`, `finally`, and `except*`.
- <https://peps.python.org/pep-3134/> — *PEP 3134 — Exception Chaining and Embedded Tracebacks* (2005),
  which added `__cause__` and `__context__` and the two sentences a traceback prints.
- <https://peps.python.org/pep-0654/> — *PEP 654 — Exception Groups and except\** (2021), the design of
  `ExceptionGroup` and why `except*` runs every matching clause.
- <https://peps.python.org/pep-0678/> — *PEP 678 — Enriching Exceptions with Notes* (2022), the reason
  `add_note` exists rather than re-wrapping with a longer message.
- <https://docs.python.org/3/library/logging.html> — `logging`, `exc_info`, and why the message takes
  `%s` arguments rather than being pre-formatted.
- <https://docs.python.org/3/library/traceback.html> — `format_exception`, and what `logging` is doing
  for you.
- <https://docs.pytest.org/en/stable/reference/reference.html#pytest-raises> — `pytest.raises`, `match=`,
  and `ExceptionInfo`.

---

## §9 Say it in an interview

> "`raise` stops the current function immediately — the rest of it does not run, including cleanup unless
> it is in a `finally` — and hands the exception to the caller, and that repeats outward until something
> catches it or the process exits non-zero. So the first design rule I follow is that a function either
> does its job or raises: returning `None` on failure moves the error away from its cause, and the
> traceback you eventually get is about a `NoneType` in a function that did nothing wrong. Catching is by
> type, and it catches subclasses, so clause order is semantics rather than style — a broad clause above a
> narrow one makes the narrow one dead code with no warning. I keep the `try` around the smallest thing
> that can fail and catch the narrowest type that fits, because the alternative is that a typo of mine
> becomes 'a bad row' in a report that looks completely normal — that is the mistake I have actually been
> bitten by, and the tell is a pipeline whose skipped-row count never changes. `except Exception` gets
> exactly one place per process, at the boundary, where it logs the traceback and turns the failure into a
> status code; a bare `except:` gets none, because it also catches `KeyboardInterrupt` and `SystemExit` and
> makes a long job impossible to stop. For my own exceptions I define one base class per project that
> inherits from `Exception` — not from a built-in, because subclassing `ConnectionError` silently enrols
> you in every existing handler for it — and then subclass by how the caller will respond rather than by
> what went wrong. Exceptions carry data: a rate limit exception has `retry_after` and `provider` as
> attributes, so the retry loop reads a number instead of guessing or parsing a sentence, and I pass those
> fields to `super().__init__` so `args` replays through `cls(*args)` and the thing still pickles when the
> work moves into a process pool. At a module boundary I translate the exceptions my dependencies raise
> into my own, always with `raise ... from error` so the cause is in the traceback — but only the expected
> ones; a bug of mine travels untouched, because wrapping an `AttributeError` in a domain error sends the
> investigation to the data instead of the code. And on the testing side, the test that earns its keep is
> the one asserting an exception *escapes*: a handler that catches and forgets to re-raise passes every
> test about return values, and `pytest.raises` around the failing call is the only thing that can see it."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, `src/setu/errors.py` is a
leaf that yesterday's layer test accepts, `RateLimited` survives a pickle round trip with its
`retry_after` intact, `load_manifest` reports the file's line number and never leaks a `json` exception,
and you have **watched the whole suite stay green through a handler that swallows** — in §5 — not when a
particular amount of time has passed. Then:

```bash
./m done 18
```

Tomorrow is typing, dataclasses, Pydantic v2 and concurrency — the phase gate. `RateLimited` gets a type
signature, `TriageResult` becomes a Pydantic model, and `asyncio.TaskGroup` starts handing you the
`ExceptionGroup` that [4.5](parts/04-in-anger/4.5-exception-groups.md) was written for.
