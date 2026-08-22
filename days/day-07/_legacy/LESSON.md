---
day: 7
phase: 1
phase_name: "Python foundations (Module 1)"
title: "Strings — methods, split/join, and formatting"
ids: ["PY-06"]
principles: ["P1 build daily", "P2 from scratch before library", "P7 evals before features"]
kind: lab
plan: setu
plan_version: "v1.0.0"
generated: "2026-08-21"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 7 — Strings: methods, split/join, and formatting

**Phase 1 · Module 1** · ID: **PY-06** (string basics, inbuilt methods, splitting and joining, formatting)

> **Yesterday:** loops and the capped retry.
> **Today:** the text primitives. Every phase after Phase 13 is a text project — tokenisation on
> Day 117, chunking on Day 164, prompt assembly on Day 168 — and all three are `split` and `join`
> wearing costumes.
> **Tomorrow:** lists, tuples, sets and dictionaries.

```bash
./m start 7 && ./m scaffold 7
```

**Time:** 80 minutes. **Request budget:** 0 model calls.

---

## §1 The story

A string is a sequence of characters, and it is **immutable** (Day 4). That single fact explains
almost everything about how you work with them:

- No string method changes a string. Every one returns a new one. If you ignore the return value,
  nothing happened.
- Building a string by repeated `+=` in a loop creates a new object every iteration. For a few
  hundred pieces it is fine; for a few hundred thousand it is slow enough to notice. `"".join(parts)`
  allocates once.

The second idea today is the one that pays off longest: **`split` and `join` are inverses, and almost
every text task is a `split`, a transform, and a `join`.** Cleaning whitespace is
`" ".join(text.split())`. Tokenisation on Day 117 is a smarter split. Chunking on Day 164 is a split
with overlap. Prompt assembly on Day 168 is a join with separators. You are learning the shape now
and refilling it four times later.

---

## §2 Setup — run this

```bash
mkdir -p days/day-07/lab
touch days/day-07/lab/strings.py
```

`src/setu/textutils.py` exists from Day 4 and grows today. No new packages.

---

## §3 PY-06 — the methods worth knowing

`days/day-07/lab/strings.py`:

```python
"""PY-06: the string methods this project actually uses, and why."""

from __future__ import annotations


def inspection() -> None:
    title = "Attention Is All You Need"
    print(f"{len(title)=}")
    print(f"{title[0]=} {title[-1]=} {title[:9]=} {title[-4:]=}")
    print(f"{title.lower()=}")
    print(f"{title.startswith('Attention')=}  {title.endswith('.')=}")
    print(f"{'All' in title=}   <- substring test, not a method")
    print(f"{title.find('All')=}  {title.find('nope')=}   <- -1, not an exception")
    print(f"{title.count('e')=}")


def cleaning() -> None:
    messy = "\t  Deep   Learning\n\n for  NLP  \n"
    print(f"\n{messy!r}")
    print(f"{messy.strip()!r}          <- ends only; inner runs survive")
    print(f"{' '.join(messy.split())!r}  <- the one you want")
    print(f"{messy.replace('  ', ' ')!r} <- fails on three spaces")


def splitting_and_joining() -> None:
    row = "2017,Attention Is All You Need,Vaswani"
    fields = row.split(",")
    print(f"\n{fields=}")
    print(f"{row.split(',', maxsplit=1)=}   <- stop after the first")
    print(f"{row.rsplit(',', maxsplit=1)=}  <- from the right")

    year, name, author = fields
    print(f"{year=} {name=} {author=}   <- unpacking a known-length split")

    print(f"\n{' | '.join(fields)=}")
    print(f"{''.join(['a', 'b', 'c'])=}")

    doc = "line one\nline two\r\nline three"
    print(f"{doc.splitlines()=}   <- handles \\n and \\r\\n")


def formatting() -> None:
    name, score, n = "bert", 0.8734, 1234567
    print(f"\n{name=} {score=}")
    print(f"  fixed:     {score:.2f}")
    print(f"  percent:   {score:.1%}")
    print(f"  padded:    |{name:>10}|{name:<10}|{name:^10}|")
    print(f"  thousands: {n:,}")
    print(f"  repr:      {name!r}")
    print(f"  expr:      {score * 100:.1f}")


def raw_and_multiline() -> None:
    print(f"\n{r'C:\Users\nisha'=}   <- raw: backslashes are literal")
    prompt = """Answer using only the context below.
If the answer is not in the context, say so.

Context: {context}"""
    print(f"\n{prompt[:40]=}")


if __name__ == "__main__":
    inspection()
    cleaning()
    splitting_and_joining()
    formatting()
    raw_and_multiline()
```

**Line by line — the parts that are not obvious:**

- `title[-4:]` — negative indexing counts from the end; `[-4:]` is the last four characters. Slices
  never raise on out-of-range, unlike single-index access.
- `'All' in title` — the `in` operator does substring testing. Use it; `.find(...) != -1` is noisier.
- `.find('nope')` returns **`-1`**, not an exception. `.index()` is the twin that raises. Pick
  deliberately: `-1` is a value you can forget to check, and `-1` is a **valid index**, so
  `title[title.find('nope')]` silently returns the last character. That is a real bug.
- `messy.strip()` — removes whitespace from **both ends only**. The three spaces between `Deep` and
  `Learning` survive. People assume otherwise constantly.
- `' '.join(messy.split())` — `split()` with **no argument** splits on any run of whitespace and drops
  empty pieces; `join` reassembles with single spaces. Two calls, no regex. Compare with
  `.replace('  ', ' ')`, which turns three spaces into two.
- `split(',', maxsplit=1)` — stop after the first separator. Essential when the last field may itself
  contain the separator; `rsplit` is the same from the right, which is how you peel a file extension.
- `year, name, author = fields` — unpacking. Raises `ValueError` if the count is wrong, which is
  **good**: a malformed row fails loudly instead of shifting every column by one.
- `splitlines()` — handles `\n`, `\r\n` and `\r`. Use it instead of `split("\n")`, or Windows CSVs
  will leave a `\r` glued to your last field. That is a genuinely common data-cleaning bug.
- `{score:.2f}` / `{score:.1%}` / `{n:,}` — format specs after the colon: fixed decimals, percentage
  (multiplies by 100 for you), thousands separators.
- `{name:>10}` `{name:<10}` `{name:^10}` — right, left, centre in a 10-character field. This is how
  Day 1's version table lined up.
- `{name!r}` — `repr`, so quotes and escapes are visible. **Every debug print should use `!r`.**
- `r'C:\Users\nisha'` — a raw string; `\n` stays two characters instead of becoming a newline.
  Windows paths and regex patterns are the two places you need this.
- The triple-quoted `prompt` — this is exactly the shape of every prompt template from Day 153 onward.

---

## §4 Build brief

Extend `src/setu/textutils.py`:

```python
def truncate(text: str, limit: int, suffix: str = "…") -> str:
    """TODO(me): shorten to at most `limit` characters INCLUDING the suffix.

    truncate("abcdefgh", 5) -> "abcd…"   (5 characters total)
    truncate("abc", 5)      -> "abc"     (unchanged, no suffix)
    Raise ValueError if limit is shorter than the suffix.
    """
    raise NotImplementedError


def slugify(text: str) -> str:
    """TODO(me): lowercase, non-alphanumerics to single hyphens, no leading/trailing hyphen.

    "  Attention Is All You Need!  " -> "attention-is-all-you-need"
    Standard library only. No regex needed - split/join is enough.
    """
    raise NotImplementedError


def split_sentences(text: str) -> list[str]:
    """TODO(me): naive sentence split on . ! ? - stripped, no empties.

    This is DELIBERATELY naive. Day 117 replaces it with a real tokeniser and you
    will compare the two. Note in your commit message one case this gets wrong.
    """
    raise NotImplementedError
```

- `truncate` — the "including the suffix" requirement is the whole exercise. Getting it to exactly
  `limit` characters is where the off-by-one lives.
- `slugify` — you use it on Day 227 to name scraped files. Doing it without regex forces you to
  actually use `split`/`join` rather than reaching for a pattern you half-remember.
- `split_sentences` — being asked to note what it gets wrong is the point (Principle 2). "Dr. Smith
  went to Washington." is one sentence and this will say two. Knowing *why* your naive version fails
  is what makes Day 117's real tokeniser mean something.

---

## §5 The eval that must be able to fail

Add to `tests/test_textutils.py`:

```python
def test_truncate_total_length_includes_suffix():
    out = tu.truncate("abcdefgh", 5)
    assert len(out) == 5, f"got {out!r} of length {len(out)}"
    assert out.endswith("…")


def test_truncate_leaves_short_text_alone():
    assert tu.truncate("abc", 5) == "abc"


def test_truncate_at_exact_limit_is_unchanged():
    assert tu.truncate("abcde", 5) == "abcde"


def test_truncate_rejects_impossible_limit():
    with pytest.raises(ValueError):
        tu.truncate("abcdefgh", 0)


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("  Attention Is All You Need!  ", "attention-is-all-you-need"),
        ("C++ & Rust", "c-rust"),
        ("---already--hyphenated---", "already-hyphenated"),
        ("2017", "2017"),
    ],
)
def test_slugify(raw, expected):
    assert tu.slugify(raw) == expected


def test_split_sentences_strips_and_drops_empties():
    assert tu.split_sentences("One. Two!  Three?  ") == ["One", "Two", "Three"]
```

**Line by line:**

- `test_truncate_total_length_includes_suffix` — the failure message prints the actual value, so a red
  test tells you what you got instead of only that you were wrong.
- `test_truncate_at_exact_limit_is_unchanged` — the boundary. An implementation that always truncates
  passes the first test and fails this one. **Every length-limit function needs its exact-boundary
  twin.**
- `@pytest.mark.parametrize(("raw", "expected"), [...])` — a tuple of names with a list of tuples,
  giving four independent cases.
- `"---already--hyphenated---"` — the collapse-and-trim case, which a naive `replace(" ", "-")` fails.
- `"2017"` — digits survive. A slugify that strips everything non-alphabetic loses it.

```bash
uv run python -m pytest tests/test_textutils.py -q
```

---

## §6 Request budget

| Resource | Spent today |
|---|---|
| LLM calls | **0** |

---

## §7 Traps

- **Discarding a string method's return value.** `text.strip()` alone does nothing. (Day 4, again.)
- **`.replace("  ", " ")` to clean whitespace.** Fails on three spaces. `" ".join(text.split())`.
- **`.split("\n")` on real-world text.** Use `.splitlines()` or a Windows `\r` rides along.
- **Unchecked `.find()`.** It returns `-1`, which is a *valid index*, so the bug is silent.
- **`+=` in a big loop.** Collect into a list and `join` once.
- **Assuming `strip()` touches the middle.** Ends only.
- **Windows paths without `r"..."`.** `"C:\new"` contains a newline.
- **Trusting a naive sentence splitter.** It will be wrong. Know *how* wrong before Day 117.

---

## §8 Verify before you code

Written **2026-08-21**:

- <https://docs.python.org/3/library/stdtypes.html#string-methods> — confirm `split()`'s no-argument
  behaviour and the `maxsplit` signature.
- <https://docs.python.org/3/library/string.html#format-specification-mini-language> — the full
  format-spec grammar behind `:.2f`, `:>10` and `:,`.

---

## §9 Say it in an interview

> "Strings are immutable, so every method returns a new one — which means the most common text bug is
> calling `.strip()` and throwing the result away. For cleaning I use `' '.join(text.split())` rather
> than chained replaces, because bare `split()` collapses any run of whitespace and drops empties in
> one pass. And I use `.splitlines()` rather than splitting on `\n`, because otherwise a carriage
> return rides along on every Windows-authored file and shows up glued to the last field three
> transformations later."

---

## §10 Done when

Tick [`CHECKLIST.md`](CHECKLIST.md), then `./m check && ./m done 7`.
