---
day: 7
phase: 1
phase_name: "Python foundations (Module 1)"
title: "Day 7 — Strings: code points, methods, and f-strings"
ids: ["PY-06"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P6 the notebook is a scratchpad", "P7 evals before features", "P16 depth over density", "P17 no clocks", "P18 zero to production"]
kind: lab
plan: setu
plan_version: "v2.2.0"
parts: 14
generated: "2026-08-25"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 7 — Strings: code points, methods, and f-strings

**Phase 1 · Python foundations · Module 1** · `PY-06` — string basics, methods, `split`/`join`, and
f-string formatting. The plan's named example for this ID is *normalising 500 messy paper titles with
one chained expression*, and that normaliser is today's deliverable.

> **Yesterday:** a `for` loop is `iter` plus `next`, `break` leaves one loop, and the capped retry is
> the shape every agent loop reuses.
> **Today:** a string is a sequence of code points rather than bytes, slicing never raises, the method
> vocabulary does most of the work, and an f-string is compiled rather than parsed.
> **Tomorrow:** lists, tuples, sets, dictionaries and view objects — where today's normalised keys go
> to be deduplicated.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Two strings that will not compare equal.

```text
>>> print(expected)
Attention Is All You Need
>>> print(actual)
Attention Is All You Need
>>> expected == actual
False
```

An hour disappears here, and it is one of at least six different bugs it could be. A trailing space,
invisible in `print`. A non-breaking space pasted from a web page, which renders identically to an
ordinary one. A `\r` left behind by a Windows line ending. An `é` written as one code point on one
side and as `e` plus a combining accent on the other. A `ﬁ` ligature from a PDF extractor. A Cyrillic
`А` standing in for a Latin one.

None of them raises. All of them look like the string being fine.

That is what makes text different from the subjects of the last three days. An operator bug produces a
wrong number; a loop bug produces a wrong count; a **text** bug produces something that *looks
correct on screen* and is not the same value. The tools that resolve it are unglamorous and take one
day to learn:

- **`repr`, not `print`** — the quotes are the whole difference
  ([3.3](parts/03-formatting/3.3-repr-and-the-debugging-f-string.md)).
- **Decode at the boundary** — a file contains bytes, and which encoding you read them with is a
  decision ([1.1](parts/01-text/1.1-a-string-is-code-points.md)).
- **Normalise deliberately** — one named function, six steps, each throwing away a specific kind of
  difference ([4.1](parts/04-normalising/4.1-the-title-normaliser.md)).
- **Methods before regex** — most of what people reach for `re` to do is a `split`, a `strip` or a
  `removeprefix` ([4.3](parts/04-normalising/4.3-methods-before-regex.md)).

By the end of today you will have a `normalise_title` that turns nine spellings of one paper into one
key. Tomorrow that key goes into a set and the duplicates disappear — and the quality of the dedup is
entirely the quality of the normaliser.

```mermaid
flowchart LR
    S1["§1 text<br/>code points · slicing · escapes"] --> S2["§2 methods<br/>strip · split/join · replace · find"]
    S2 --> S3["§3 formatting<br/>f-strings · the spec · !r · injection"]
    S3 --> S4["§4 normalising<br/>500 messy titles, end to end"]
    style S1 fill:#1f6feb,color:#fff
    style S4 fill:#238636,color:#fff
```

---

## §2 The map

**What the section numbers mean today.** One ID, so the sections follow the plan's `lab` split from
mechanism to production use: **1.x** is what a string *is* — code points, positions, literals; **2.x**
is the method vocabulary, one part per family; **3.x** is formatting, from what an f-string compiles
to through to where it must not be used; **4.x** is the pipeline that puts all of it together on real
data.

### Section 1 — what a string is

| Part | What it answers | Level |
|---|---|---|
| [1.1 A string is code points, not bytes](parts/01-text/1.1-a-string-is-code-points.md) | Why is `len("café")` 4 but its encoded length 5? | `foundation` |
| [1.2 Indexing and slicing](parts/01-text/1.2-indexing-and-slicing.md) | Why does `s[i]` raise and `s[a:b]` never? | `foundation` |
| [1.3 Escapes and raw strings](parts/01-text/1.3-escapes-and-raw-strings.md) | Why does `"C:\data\new"` contain a newline? | `foundation` |

### Section 2 — the method vocabulary

| Part | What it answers | Level |
|---|---|---|
| [2.1 Normalising: `strip`, `lower`, `casefold`](parts/02-methods/2.1-normalising-strip-and-case.md) | Why is `lower()` the wrong function for comparison? | `working` |
| [2.2 `split` and `join`](parts/02-methods/2.2-split-and-join.md) | What are the three differences between `split()` and `split(sep)`? | `working` |
| [2.3 `replace` and `removeprefix`](parts/02-methods/2.3-replace-and-removeprefix.md) | How does `"scientific"` become `"scienti"`? | `working` |
| [2.4 `find` vs `index` vs `in`](parts/02-methods/2.4-find-index-and-in.md) | Why is `-1` the most dangerous sentinel in Python? | `working` |

### Section 3 — formatting

| Part | What it answers | Level |
|---|---|---|
| [3.1 What an f-string compiles to](parts/03-formatting/3.1-what-an-f-string-compiles-to.md) | Why can a template from a config file not be an f-string? | `working` |
| [3.2 The format spec](parts/03-formatting/3.2-the-format-spec.md) | What is the difference between `round(x, 2)` and `f"{x:.2f}"`? | `working` |
| [3.3 `!r`, `=`, and the debugging f-string](parts/03-formatting/3.3-repr-and-the-debugging-f-string.md) | Which one line ends the story's hour? | `working` |
| [3.4 When not to use an f-string](parts/03-formatting/3.4-when-not-to-use-an-f-string.md) | Why is interpolation into SQL structurally unsafe? | `production` |

### Section 4 — the normaliser, end to end

| Part | What it answers | Level |
|---|---|---|
| [4.1 The title normaliser, from scratch](parts/04-normalising/4.1-the-title-normaliser.md) | What are the six steps, and why in that order? | `production` |
| [4.2 Unicode normalisation](parts/04-normalising/4.2-unicode-normalisation.md) | How can two strings render identically and have different lengths? | `production` |
| [4.3 Methods before regex](parts/04-normalising/4.3-methods-before-regex.md) | Where exactly is the boundary between a pattern and a fixed string? | `production` |

---

## §3 Setup — run this

**No new packages today.** Everything is the language plus `unicodedata`, `re`, `sqlite3`,
`subprocess`, `pathlib`, `dis` and `decimal` from the standard library. Module 1 is the language before
any library (Principle 2), and `re` appears only in
[4.3](parts/04-normalising/4.3-methods-before-regex.md) — after four parts arguing that most of what
people use it for is a method call.

```bash
mkdir -p src/setu tests notebooks data
touch src/setu/text.py tests/test_text.py

# a scratchpad for today - the notebook is never the deliverable (P6)
touch notebooks/day-07-scratch.ipynb

# the character-dump reflex, before any part tells you to have it (part 3.3)
uv run python -c "s='caf\u00e9'; print(repr(s), len(s), [f'U+{ord(c):04X}' for c in s])"

# the same word, decomposed - different length, identical rendering (part 4.2)
uv run python -c "s='cafe\u0301'; print(repr(s), len(s), [f'U+{ord(c):04X}' for c in s])"

# the two rules that catch today's silent bugs
uv run ruff rule E713
uv run ruff rule RUF001
```

| What | Where it comes from | Part |
|---|---|---|
| `encode`, `decode`, `ord`, `chr` | builtins | [1.1](parts/01-text/1.1-a-string-is-code-points.md) |
| `slice` objects, `tempfile`, `pathlib` | builtins, standard library | [1.2](parts/01-text/1.2-indexing-and-slicing.md) |
| `str.maketrans`, `str.translate` | builtins | [2.3](parts/02-methods/2.3-replace-and-removeprefix.md) |
| `partition`, `rpartition`, `startswith` with a tuple | builtins | [2.4](parts/02-methods/2.4-find-index-and-in.md) |
| `dis` | standard library | [3.1](parts/03-formatting/3.1-what-an-f-string-compiles-to.md) |
| `decimal.Decimal` | standard library | [3.2](parts/03-formatting/3.2-the-format-spec.md) |
| `sqlite3`, `subprocess`, `re.escape` | standard library | [3.4](parts/03-formatting/3.4-when-not-to-use-an-f-string.md) |
| `unicodedata.normalize`, `.name`, `.combining` | standard library | [4.2](parts/04-normalising/4.2-unicode-normalisation.md) |
| `re.compile`, `re.VERBOSE`, named groups | standard library | [4.3](parts/04-normalising/4.3-methods-before-regex.md) |

---

## §4 Build brief

One module, and it is the one every later text day imports.

**1. `src/setu/text.py`** — the normaliser and its neighbours.

```python
"""Text normalisation for Setu.

Every function here builds a COMPARISON KEY, not a display string. Callers keep
the raw value alongside the key (day 7, part 4.1).
"""

from __future__ import annotations

import unicodedata

KEY_VERSION = 1
"""Bump this when normalise_title changes, so stored keys can be re-computed."""

PUNCTUATION_MAP = str.maketrans(
    {
        "\u201c": '"',
        "\u201d": '"',
        "\u2018": "'",
        "\u2019": "'",
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
        "\u2009": " ",
        "\u200b": "",
    }
)

TRAILING_PUNCTUATION = ".,;:"


def normalise_title(raw: str) -> str | None:
    """A comparison key for a paper title, or None when there is no title.

    Six steps, in the order part 4.1 justifies. Write the docstring listing them
    BEFORE writing the body - the decisions are the deliverable, not the code.
    """
    # TODO(me): the six steps. Two of the orderings matter; say which in a comment.
    raise NotImplementedError


def show(text: str) -> str:
    """repr(text) plus every non-ASCII code point in it (part 3.3).

    The helper you reach for when two strings look identical and are not.
    """
    # TODO(me): two lines. Decide whether to report duplicates once or every time,
    # and say why.
    raise NotImplementedError


def strip_accents(text: str) -> str:
    """Drop combining marks: 'cafe' from 'café' (part 4.2).

    Decompose FIRST - on a composed string there is nothing to filter.
    """
    # TODO(me): normalize then filter. Then answer in a comment: what does this
    # do to 'Straße', and is that a bug?
    raise NotImplementedError


def collapse_whitespace(text: str) -> str:
    """Any run of any whitespace becomes one space; the ends are trimmed.

    One expression, two method calls, no regex (parts 2.2 and 4.3).
    """
    # TODO(me): one line.
    raise NotImplementedError


def strip_bracketed_suffix(text: str) -> str:
    """Remove ONE trailing (...) or [...] group. Deliberately NOT in normalise_title.

    Part 4.1 explains why this is a separate, caller-visible decision.
    """
    # TODO(me): use rfind and guard its -1 (part 2.4). A title that is entirely a
    # bracketed group must not become empty - decide what it becomes instead.
    raise NotImplementedError


def truncate_bytes(text: str, limit: int) -> str:
    """The longest prefix of `text` whose UTF-8 encoding is at most `limit` bytes.

    Part 1.1: slicing the encoded form can cut a character in half.
    """
    # TODO(me): you cannot slice the bytes and decode. Work out why, then work out
    # what you CAN do, and write the reasoning in a comment.
    raise NotImplementedError
```

**2. Build the messy fixture yourself.** In `data/`, create `titles_messy.txt` with at least twenty
lines: the nine variants from [4.1](parts/04-normalising/4.1-the-title-normaliser.md), plus a
decomposed accent, a `ﬁ` ligature, a full-width form, a Cyrillic homoglyph, a zero-width space, a
trailing `\r`, and at least three genuinely *different* papers. **The last group is the important
one** — a normaliser that collapses everything is not a normaliser, and without distinct papers in
the fixture your tests cannot prove it does not.

**3. Reproduce the story in the notebook, then throw the notebook away.** In
`notebooks/day-07-scratch.ipynb`: take two visually identical titles, spend two minutes with `print`
getting nowhere, then resolve it in one line with `f"{title=}"`. Then do it again with a decomposed
accent, where `repr` is *also* not enough and you need `!a` or a code-point dump. **The notebook is not
committed** (Principle 6); `src/setu/text.py` and its tests are.

---

## §5 The eval that must be able to fail

Create `tests/test_text.py`. Everything runs offline and belongs in `./m check`.

```python
"""Day 7: prove the normaliser's decisions rather than eyeballing its output."""

from __future__ import annotations

import pytest

from setu.text import (
    collapse_whitespace,
    normalise_title,
    show,
    strip_accents,
    strip_bracketed_suffix,
    truncate_bytes,
)

SAME_PAPER = [
    "  Attention Is All You Need  ",
    "ATTENTION IS ALL YOU NEED",
    "Attention\u00a0Is All You Need",
    "Attention  Is\tAll\nYou Need",
    "\u201cAttention Is All You Need\u201d",
    "Attention Is All You Need.",
    "Attention Is All You Need\r",
]

DIFFERENT_PAPERS = [
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "Deep Residual Learning for Image Recognition",
    "Attention Is Not All You Need",
]


def test_all_variants_collapse_to_one_key() -> None:
    """Part 4.1: the property the whole function exists for."""
    # TODO(me): assert len({normalise_title(t) for t in SAME_PAPER}) == 1.
    # This is the headline test; write it first and watch it fail.
    raise NotImplementedError


def test_distinct_papers_stay_distinct() -> None:
    """Part 4.1: a normaliser that collapses everything is not a normaliser."""
    # TODO(me): assert the three different papers produce three different keys,
    # and that none of them equals the SAME_PAPER key. Without this test, an
    # over-aggressive normaliser passes the test above perfectly.
    raise NotImplementedError


@pytest.mark.parametrize("blank", ["", "   ", "\t\n", "\u200b"])
def test_a_blank_title_is_none_not_empty_string(blank: str) -> None:
    """Part 4.1: an empty key would make every untitled paper collide."""
    # TODO(me): assert normalise_title(blank) is None. Use `is`, not ==
    # (day 5, part 1.4).
    raise NotImplementedError


def test_composed_and_decomposed_accents_match() -> None:
    """Part 4.2: the bug no amount of stripping or casefolding fixes."""
    # TODO(me): "caf\u00e9" and "cafe\u0301" must produce the same key. Assert the
    # RAW strings are unequal first - otherwise the test proves nothing.
    raise NotImplementedError


def test_ligature_and_fullwidth_forms_are_folded() -> None:
    """Part 4.2: why NFKC rather than NFC."""
    # TODO(me): "identi\ufb01cation" and "identification"; "\uff21\uff22\uff23" and "ABC".
    raise NotImplementedError


def test_homoglyphs_do_NOT_match() -> None:
    """Part 4.2: normalisation must not merge different letters."""
    # TODO(me): Cyrillic "\u0410ttention" and Latin "Attention" must produce
    # DIFFERENT keys. Then answer in a comment: is that the behaviour we want,
    # and what would we do instead if it is not?
    raise NotImplementedError


def test_collapse_whitespace_handles_every_kind() -> None:
    """Part 2.2: tabs, newlines, non-breaking and zero-width."""
    # TODO(me): one input containing all of them. Assert the exact output, not
    # just that it has no double spaces.
    raise NotImplementedError


def test_strip_accents_decomposes_first() -> None:
    """Part 4.2: on a composed string there is nothing to filter."""
    # TODO(me): assert strip_accents("caf\u00e9") == "cafe". Then add the "Stra\u00dfe"
    # case with whatever your build-brief comment decided.
    raise NotImplementedError


def test_strip_bracketed_suffix_is_not_greedy() -> None:
    """Part 4.1: it removes ONE trailing group and leaves internal ones alone."""
    # TODO(me): "Attention (Revised) Considered" must be untouched. And a title
    # that is entirely a bracketed group must not become empty.
    raise NotImplementedError


def test_truncate_bytes_never_produces_invalid_utf8() -> None:
    """Part 1.1: slicing encoded text can cut a character in half."""
    # TODO(me): for limits 1..20 on a title containing a multi-byte character,
    # assert the result re-encodes to at most `limit` bytes AND round-trips
    # through encode/decode without raising.
    raise NotImplementedError


def test_show_reveals_an_invisible_character() -> None:
    """Part 3.3: the helper that ends the story's hour."""
    # TODO(me): assert "00A0" appears in show("a\u00a0b") and does not appear in
    # show("a b").
    raise NotImplementedError
```

Run them and watch every one fail before you write a line:

```bash
uv run python -m pytest tests/test_text.py -v
```

Then implement, then **break each one on purpose**:

- Change `casefold()` to `lower()` → the variant-collapse test **still passes**, because the fixture is
  English. Add `"STRASSE"`/`"Straße"` to `SAME_PAPER` and watch it go red. **The test only catches what
  the fixture contains.**
- Remove the NFKC step → the accent test and the ligature test go red, and the headline
  collapse test still passes. Read which ones fail and which do not.
- Move the `casefold()` before the `translate` → everything still passes. Now work out whether that
  ordering is actually safe, and write the answer in a comment. (It is; two of the six orderings matter
  and this is not one of them. Being able to say *which* is the point.)
- Make `normalise_title` also strip bracketed suffixes → the collapse test passes and
  **`test_distinct_papers_stay_distinct` goes red**, because two of the fixture papers differ only by
  a suffix. That is the over-aggressive-normaliser failure, caught.
- Make `normalise_title` return `""` instead of `None` → the blank test goes red four times, once per
  parametrised case.

That fourth item is today's most important line. A normaliser is judged by **two** properties that pull
in opposite directions — variants must collapse and distinct records must not — and a test suite with
only the first is how an over-aggressive normaliser reaches production
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

| Resource | Today |
|---|---|
| LLM API calls | **0** — no model is called on this day |
| Network requests | **0** — the fixture is one you write by hand |
| Free-tier quota | none consumed |
| Cost | **$0** (Principle 5) |

[3.4](parts/03-formatting/3.4-when-not-to-use-an-f-string.md) uses `sqlite3` in memory and
`subprocess` with `echo`; neither leaves the machine. The SQL-injection demonstration is against a
database created and destroyed in the same process.

---

## §7 Traps

- **`len("café")` is 4 and its UTF-8 length is 5** — any byte-sized limit checked against a character
  count is wrong — [1.1](parts/01-text/1.1-a-string-is-code-points.md).
- **`errors="ignore"` turns a loud failure into silent data loss** —
  [1.1](parts/01-text/1.1-a-string-is-code-points.md).
- **Decoding with the wrong encoding often does not raise** —
  [1.1](parts/01-text/1.1-a-string-is-code-points.md).
- **`open()` without `encoding=` reads differently on Windows** —
  [1.1](parts/01-text/1.1-a-string-is-code-points.md).
- **`b"abc"[0]` is `97`, an integer** — [1.1](parts/01-text/1.1-a-string-is-code-points.md).
- **`s[i]` raises and `s[a:b]` never does** — a short row gives an empty field, not an error —
  [1.2](parts/01-text/1.2-indexing-and-slicing.md).
- **Consuming a string by re-slicing it is quadratic** —
  [1.2](parts/01-text/1.2-indexing-and-slicing.md).
- **`"C:\data\new"` contains a newline, a tab and one surviving backslash** —
  [1.3](parts/01-text/1.3-escapes-and-raw-strings.md).
- **Forgetting `r` breaks a regex containing `\b` and not one containing `\d`** —
  [1.3](parts/01-text/1.3-escapes-and-raw-strings.md).
- **A raw string cannot end with a backslash** — [1.3](parts/01-text/1.3-escapes-and-raw-strings.md).
- **`title.strip()` on its own line does nothing** —
  [2.1](parts/02-methods/2.1-normalising-strip-and-case.md).
- **`strip("https://")` removes a character SET and eats the `s` of `sci-hub`** —
  [2.1](parts/02-methods/2.1-normalising-strip-and-case.md).
- **`lower()` leaves German `ß` alone; `casefold()` does not** —
  [2.1](parts/02-methods/2.1-normalising-strip-and-case.md).
- **`title()` turns `"it's"` into `"It'S"`** — [2.1](parts/02-methods/2.1-normalising-strip-and-case.md).
- **`"".split()` is `[]` and `"".split(",")` is `[""]`** —
  [2.2](parts/02-methods/2.2-split-and-join.md).
- **`split("; ")` silently merges records when the spacing is inconsistent** —
  [2.2](parts/02-methods/2.2-split-and-join.md).
- **`join` is a method on the separator, and will not convert non-strings** —
  [2.2](parts/02-methods/2.2-split-and-join.md).
- **`replace` is global**, so a `.pdf` in the middle of a title disappears too —
  [2.3](parts/02-methods/2.3-replace-and-removeprefix.md).
- **Two chained `replace` calls are not two independent substitutions** —
  [2.3](parts/02-methods/2.3-replace-and-removeprefix.md).
- **`s[len(prefix):]` without a `startswith` guard chops any string** —
  [2.3](parts/02-methods/2.3-replace-and-removeprefix.md).
- **`"abc".replace("", "-")` inserts between every character** —
  [2.3](parts/02-methods/2.3-replace-and-removeprefix.md).
- **`find` returns `-1`, and `-1` is a valid Python index** —
  [2.4](parts/02-methods/2.4-find-index-and-in.md).
- **`"abc".find("")` is `0`** — a computed empty needle always "matches" —
  [2.4](parts/02-methods/2.4-find-index-and-in.md).
- **`"aaa".count("aa")` is `1`** — counts are non-overlapping —
  [2.4](parts/02-methods/2.4-find-index-and-in.md).
- **`f"{template}"` does not re-interpret braces inside `template`** —
  [3.1](parts/03-formatting/3.1-what-an-f-string-compiles-to.md).
- **A `str.format` template from an untrusted source can read your objects' attributes** —
  [3.1](parts/03-formatting/3.1-what-an-f-string-compiles-to.md).
- **`round(0.1, 2)` prints `0.1`; `f"{0.1:.2f}"` prints `0.10`** —
  [3.2](parts/03-formatting/3.2-the-format-spec.md).
- **A width without a precision does not truncate**, so one long value breaks a table —
  [3.2](parts/03-formatting/3.2-the-format-spec.md).
- **`{x:.1%}` multiplies by 100** — doing it by hand as well gives 8560% —
  [3.2](parts/03-formatting/3.2-the-format-spec.md).
- **`print` hides trailing whitespace; `repr` does not** —
  [3.3](parts/03-formatting/3.3-repr-and-the-debugging-f-string.md).
- **A `__repr__` that raises, is slow, or prints a secret is a production hazard** —
  [3.3](parts/03-formatting/3.3-repr-and-the-debugging-f-string.md).
- **Interpolating into SQL, a shell, a path or HTML is an injection** —
  [3.4](parts/03-formatting/3.4-when-not-to-use-an-f-string.md).
- **`Path` joining does not stop `..`** — resolve, then check containment —
  [3.4](parts/03-formatting/3.4-when-not-to-use-an-f-string.md).
- **An f-string in a logging call formats even when the level is disabled** —
  [3.4](parts/03-formatting/3.4-when-not-to-use-an-f-string.md).
- **A normaliser that returns `""` makes every untitled record collide** —
  [4.1](parts/04-normalising/4.1-the-title-normaliser.md).
- **Character substitutions must come before token-level splits** —
  [4.1](parts/04-normalising/4.1-the-title-normaliser.md).
- **Two visually identical strings can have different lengths** —
  [4.2](parts/04-normalising/4.2-unicode-normalisation.md).
- **NFKC is lossy: `x²` becomes `x2`** — [4.2](parts/04-normalising/4.2-unicode-normalisation.md).
- **No normalisation form merges a Cyrillic `А` with a Latin `A`** —
  [4.2](parts/04-normalising/4.2-unicode-normalisation.md).
- **An index normalised differently from its queries is worse than no normalisation** —
  [4.2](parts/04-normalising/4.2-unicode-normalisation.md).
- **A pattern built from unescaped input is broken or dangerous** —
  [4.3](parts/04-normalising/4.3-methods-before-regex.md).
- **An optional regex group that did not match is `None`, not `""`** —
  [4.3](parts/04-normalising/4.3-methods-before-regex.md).
- **`re.match` anchors at the start; `re.search` does not** —
  [4.3](parts/04-normalising/4.3-methods-before-regex.md).
- **Nested quantifiers backtrack catastrophically** — a denial of service on user input —
  [4.3](parts/04-normalising/4.3-methods-before-regex.md).

---

## §8 Verify before you code

Written **2026-08-25**. Today is the language and the standard library, so the reference is the
authority:

- <https://docs.python.org/3/library/stdtypes.html#string-methods> — every method on this page, with
  the exact semantics of `split`, `strip` and `partition`. Read the whole list once; it is shorter
  than you expect and you will use most of it.
- <https://docs.python.org/3/howto/unicode.html> — the official Unicode HOWTO, which is the best
  single explanation of [1.1](parts/01-text/1.1-a-string-is-code-points.md) and
  [4.2](parts/04-normalising/4.2-unicode-normalisation.md) anywhere.
- <https://docs.python.org/3/library/string.html#format-specification-mini-language> — the format spec
  grammar. [3.2](parts/03-formatting/3.2-the-format-spec.md) reproduces it; this is authoritative.
- <https://docs.python.org/3/reference/lexical_analysis.html#f-strings> — f-strings defined as
  grammar, including what changed in 3.12.
- <https://docs.python.org/3/library/unicodedata.html> — `normalize`, `name`, `combining`,
  `is_normalized`.
- <https://unicode.org/reports/tr15/> — Unicode Annex 15, the normalisation forms in their own words.
  Skim the summary table; it is the source
  [4.2](parts/04-normalising/4.2-unicode-normalisation.md) is paraphrasing.
- <https://docs.python.org/3/library/re.html#re.VERBOSE> — and the "Regular Expression HOWTO" linked
  from that page, which is the right first read on `re`.
- <https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders> — parameter binding, in the
  standard library's own words.
- `uv run ruff rule E713`, `uv run ruff rule RUF001` — read from the linter you have installed.

---

## §9 Say it in an interview

> "A Python string is a sequence of Unicode code points, not bytes — `encode` and `decode` are the
> only ways between the two, and each needs an encoding, which is why `len('café')` is 4 while its
> UTF-8 length is 5. That difference is behind a whole family of bugs: a byte-sized database column
> checked against a character count, text truncated at a byte boundary producing an invalid sequence,
> and every `UnicodeDecodeError`, which always means the reader's encoding is wrong — `errors='ignore'`
> converts a loud failure into silent data loss. So I decode at the boundary, work in `str` throughout,
> and encode on the way out. The methods do most of the work: `' '.join(text.split())` collapses any run
> of any whitespace including the exotic ones, `casefold` rather than `lower` for a comparison key
> because `lower` leaves German `ß` alone, `removeprefix` rather than `replace` because `replace` is
> global, and `partition` rather than `find` because `find` returns `-1` and `-1` is a valid index, so
> an unchecked result produces plausible garbage instead of an error. For debugging, `repr` rather than
> `print` — `f'{value=}'` shows the expression and the quoted value in one token, which is how you find
> a trailing space in four seconds instead of an hour, and `!a` is what finds an invisible non-breaking
> space. The hard case is Unicode normalisation: `é` can be one code point or `e` plus a combining
> accent, so two strings render identically, have different lengths, and compare unequal —
> `unicodedata.normalize` fixes that, NFC for storage and NFKC for a comparison key because it also
> folds ligatures and full-width forms, at the cost of being lossy. What it will not fix is a Cyrillic
> `А` standing in for a Latin one, because those genuinely are different letters; that needs a script
> check. And the rule I hold to on formatting is that an f-string is fine when a human reads the
> result and dangerous when something else parses it — SQL gets bound parameters, shells get argument
> lists, paths get `pathlib` plus a containment check, and logging gets `%s` args so the formatting is
> deferred."

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `./m check` is green, and your normaliser
satisfies **both** properties — the variants collapse to one key *and* the three genuinely different
papers stay three — not when a particular amount of time has passed. Then:

```bash
./m done 7
```

Tomorrow is containers: lists, tuples, sets, dictionaries and view objects — where today's keys go into
a set, and where the plan's example is de-duplicating ten thousand identifiers in O(n) instead of
O(n²), timed both ways.
