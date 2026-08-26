# Day 7 — CHECKLIST

**IDs covered:** `PY-06` · **Principles served:** 1, 2, 3, 6, 7, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 14, in [`parts/`](parts/)

> `./m done 7` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_text.py -v && ./m check
```

Expected: eleven passing tests (one of them parametrised four times), including the pair that pulls in
opposite directions — variants collapse to one key, distinct papers stay distinct — and a green gate.

---

## Section 1 — what a string is

- [ ] Read [1.1 — a string is code points](parts/01-text/1.1-a-string-is-code-points.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — indexing and slicing](parts/01-text/1.2-indexing-and-slicing.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — escapes and raw strings](parts/01-text/1.3-escapes-and-raw-strings.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Printed `len(s)` and `len(s.encode())` for an ASCII, an accented, a CJK and an emoji string
- [ ] Confirmed `b"abc"[0]` is an `int` and `b"abc"[0:1]` is `bytes`
- [ ] Triggered a real `UnicodeDecodeError` and read the byte and position it names
- [ ] Decoded the same bytes four ways — strict, ignore, replace, and the correct encoding
- [ ] **Watched `errors="ignore"` silently delete a character**, and can say why that is worse than the error
- [ ] Confirmed `"abc" == b"abc"` is `False` with no error
- [ ] Truncated encoded text at a byte boundary and watched the decode raise
- [ ] Confirmed `s[len(s)]` raises and `s[5:99]` does not
- [ ] Built a fixed-width parser and watched a short line produce an empty field, silently
- [ ] Added the length guard and watched the same line raise
- [ ] Timed consuming a string by re-slicing against moving an index
- [ ] Predicted `s[4:1:-1]` and `s[1:4:-1]` before running them
- [ ] Wrote `"C:\data\new"` and saw the `SyntaxWarning`, then dumped its actual characters
- [ ] Confirmed `r"a\n"` and `"a\\n"` are the same string, and that neither is a special type
- [ ] **Watched a non-raw regex containing `\b` match nothing**, with no error

## Section 2 — the method vocabulary

- [ ] Read [2.1 — strip, lower, casefold](parts/02-methods/2.1-normalising-strip-and-case.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — split and join](parts/02-methods/2.2-split-and-join.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — replace and removeprefix](parts/02-methods/2.3-replace-and-removeprefix.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — find, index, in](parts/02-methods/2.4-find-index-and-in.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Wrote `title.strip()` on its own line and confirmed it did nothing
- [ ] Watched `strip("https://")` eat the `s` of `sci-hub`, and fixed it with `removeprefix`
- [ ] Confirmed `"STRASSE".lower() != "Straße".lower()` and that `casefold` fixes it
- [ ] Confirmed `"it's a test".title()` is wrong, and can say why
- [ ] Found a non-breaking space that `strip()` did **not** remove, because it was in the middle
- [ ] Ran the full `split()` versus `split(",")` table and can explain the `""` row
- [ ] Reproduced the author-list bug: inconsistent spacing merging two names into one
- [ ] Reproduced the trailing-separator bug: an empty string counted as an author
- [ ] Used `" ".join(text.split())` to collapse tabs, newlines and non-breaking spaces in one line
- [ ] Got `TypeError` from joining non-strings and read the index it names
- [ ] Watched `replace(".pdf", "")` delete a `.pdf` from the **middle** of a title
- [ ] Watched `replace("arxiv:", "")` turn a doubled prefix into a valid-looking wrong id
- [ ] Ran two chained `replace` calls that fed each other, then fixed it with `translate`
- [ ] Built a `maketrans` table with the three-argument delete form
- [ ] Used `replace(old, new, 1)` and can say when the `count` parameter is the right tool
- [ ] **Watched `find`'s `-1` produce a plausible-looking string instead of an error**
- [ ] Confirmed `index` raises on the same input
- [ ] Rewrote the extraction with `partition` and confirmed it cannot raise
- [ ] Used `startswith` with a tuple instead of a chain of `or`s
- [ ] Confirmed `"aaa".count("aa")` is 1 and `"abc".find("")` is 0

## Section 3 — formatting

- [ ] Read [3.1 — what an f-string compiles to](parts/03-formatting/3.1-what-an-f-string-compiles-to.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — the format spec](parts/03-formatting/3.2-the-format-spec.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — `!r`, `=`, and the debugging f-string](parts/03-formatting/3.3-repr-and-the-debugging-f-string.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.4 — when not to use an f-string](parts/03-formatting/3.4-when-not-to-use-an-f-string.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Disassembled an f-string and a `.format` call, and found where the template lives in each
- [ ] Reproduced the config-template bug: `f"{template}"` printing the braces
- [ ] Fixed it with `.format`, and watched a missing key raise `KeyError`
- [ ] Confirmed an **extra** `format` argument is silently ignored
- [ ] Put an expression, a method call and a conditional expression inside braces
- [ ] Used every field of the format spec at least once: fill, align, sign, width, grouping, precision, type
- [ ] Confirmed `round(0.1, 2)` prints `0.1` and `f"{0.1:.2f}"` prints `0.10`
- [ ] Confirmed banker's rounding on `0.5`, `1.5`, `2.5`
- [ ] Printed `Decimal(2.675)` and can say why `.2f` gives `2.67`
- [ ] Built a table with computed widths using nested braces
- [ ] Removed the precision and watched one long value break every row below it
- [ ] Multiplied by 100 **and** used `:.1%`, and saw 8560%
- [ ] Ran the `str` versus `repr` table and can name three rows where they differ
- [ ] **Ended a "these look identical" investigation with one `f"{value=}"`**
- [ ] Used `!a` to reveal a non-breaking space that `repr` did not
- [ ] Printed a class with no `__repr__` and saw the memory address
- [ ] Ran the SQL-injection demonstration and read the generated statement character by character
- [ ] Confirmed the bound version returns 0 rows for the same malicious input
- [ ] Passed a shell metacharacter through `subprocess.run` with a **list** and watched it stay literal
- [ ] Confirmed `Path` joining does not stop `..`, and used `is_relative_to` on resolved paths
- [ ] Confirmed an f-string in a disabled `log.debug` still evaluated its argument

## Section 4 — the normaliser

- [ ] Read [4.1 — the title normaliser](parts/04-normalising/4.1-the-title-normaliser.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.2 — unicode normalisation](parts/04-normalising/4.2-unicode-normalisation.md), ran its check-yourself, answered its out-loud question
- [ ] Read [4.3 — methods before regex](parts/04-normalising/4.3-methods-before-regex.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Ran the nine messy titles through the pipeline and got **one** key
- [ ] Printed every intermediate stage with `repr` and can justify two of the orderings
- [ ] Swapped the translate and collapse steps and found an input where it matters
- [ ] Confirmed a title that normalises to empty returns `None`, not `""`
- [ ] Wrote `strip_bracketed_suffix` as a **separate** function and can say why
- [ ] Confirmed composed and decomposed `café` have different lengths and render identically
- [ ] Printed `unicodedata.name()` for each character of the decomposed form
- [ ] Confirmed NFC and NFD **both** make them equal, and can say why either works
- [ ] Ran the NFKC table and can name three things it folds that NFC does not
- [ ] Confirmed NFKC turns `x²` into `x2`, and can say when that is wrong
- [ ] **Confirmed no normalisation form merges Cyrillic `А` with Latin `A`**
- [ ] Wrote a script check and used it on the homoglyph title
- [ ] Wrote `strip_accents` and confirmed decomposing first is essential
- [ ] Confirmed `strip_accents("Straße")` leaves the `ß`, and decided whether that is a bug
- [ ] Replaced six regexes with six methods and asserted the results are identical
- [ ] Timed both and can state the direction of the difference
- [ ] Wrote one genuine regex with `VERBOSE`, named groups and a module-level `compile`
- [ ] Handled the optional group being `None` rather than `""`
- [ ] Watched an unescaped `c++` raise `re.error`, then fixed it with `re.escape`
- [ ] **Timed `(a+)+$` at two input lengths four characters apart** and saw the exponential blow-up

## The standard underneath normalisation

Plan v2.3.0 retired the separate paper document, so the annex is cited inside
[4.2](parts/04-normalising/4.2-unicode-normalisation.md), where it is needed.

- [ ] Opened *Unicode Standard Annex #15* at <https://www.unicode.org/reports/tr15/> and found the
      table naming the four normalisation forms

**Proof, not belief:**

- [ ] Printed the code points of both spellings of `é` and watched the lengths differ by one
- [ ] Ran all four forms over `"ﬁ"` and can say which two changed it and which two left it alone
- [ ] Can name which two normalisation forms lose information, and exactly what they lose
- [ ] Can say which form to store and which form to build a dedup key with

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/text.py` with `KEY_VERSION`
- [ ] Implemented `normalise_title` — six steps, with the two load-bearing orderings commented
- [ ] Implemented `show` — with the duplicate-reporting decision written down
- [ ] Implemented `strip_accents` — decompose first, with the `ß` question answered in a comment
- [ ] Implemented `collapse_whitespace` — one line, no regex
- [ ] Implemented `strip_bracketed_suffix` — with the `rfind` sentinel guarded
- [ ] Implemented `truncate_bytes` — with the reasoning about why byte-slicing fails
- [ ] Built `data/titles_messy.txt` with twenty-plus lines
- [ ] The fixture contains a decomposed accent, a ligature, a full-width form, a homoglyph, a zero-width space and a `\r`
- [ ] **The fixture contains at least three genuinely different papers**
- [ ] Reproduced the story in `notebooks/day-07-scratch.ipynb` — two minutes with `print`, four seconds with `=`
- [ ] The notebook is **not** committed; the understanding graduated to `src/setu/` (Principle 6)
- [ ] `uv run ruff check src/ tests/` passes

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_text.py -v` **before** implementing and watched every test fail
- [ ] Implemented `test_all_variants_collapse_to_one_key` — the headline
- [ ] Implemented `test_distinct_papers_stay_distinct` — the counterweight
- [ ] Implemented the parametrised `test_a_blank_title_is_none_not_empty_string` — with `is`, not `==`
- [ ] Implemented `test_composed_and_decomposed_accents_match` — asserting the raw strings are unequal first
- [ ] Implemented `test_ligature_and_fullwidth_forms_are_folded`
- [ ] Implemented `test_homoglyphs_do_NOT_match` — with the comment on whether that is what we want
- [ ] Implemented `test_collapse_whitespace_handles_every_kind` — asserting the exact output
- [ ] Implemented `test_strip_accents_decomposes_first`
- [ ] Implemented `test_strip_bracketed_suffix_is_not_greedy`
- [ ] Implemented `test_truncate_bytes_never_produces_invalid_utf8`
- [ ] Implemented `test_show_reveals_an_invisible_character`
- [ ] **Break it, watch it go red, fix it —** changed `casefold` to `lower`, saw the test **pass**, added the German pair to the fixture, saw it go red. Restored it.
- [ ] **Break it, watch it go red, fix it —** removed the NFKC step, noted **which** tests failed and which did not. Restored it.
- [ ] **Break it, watch it go red, fix it —** moved `casefold` before `translate`, saw everything pass, and worked out why that ordering is safe. Restored it.
- [ ] **The one that matters most —** made `normalise_title` strip bracketed suffixes, watched the collapse test pass and **`test_distinct_papers_stay_distinct` go red**, and can say why a normaliser needs two tests pulling in opposite directions
- [ ] **Break it, watch it go red, fix it —** returned `""` instead of `None`, saw four parametrised failures. Restored it.
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] **0** network requests — the fixture is hand-written and the database is in memory
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] What a `str` holds, what a `bytes` holds, and the only two operations between them
- [ ] Why `len("café")` is 4 while its encoded length is 5, and one bug that causes
- [ ] Why `errors="ignore"` is worse than the exception it silences
- [ ] The one behavioural difference between `s[i]` and `s[a:b]`, and when each is right
- [ ] What the `r` prefix does and at what moment it does it
- [ ] Why forgetting `r` breaks `\b` and not `\d`, and why that makes the rule "always raw"
- [ ] Why `title.strip()` on its own line does nothing
- [ ] The difference between `strip("abc")` and `removeprefix("abc")`
- [ ] The difference between `lower()` and `casefold()`
- [ ] The three differences between `split()` and `split(sep)`, and what each mode is for
- [ ] Why `join` is a method on the separator
- [ ] What `replace` does that `removesuffix` does not, with an input where it matters
- [ ] Why two chained `replace` calls are not two independent substitutions
- [ ] The three answers `find`, `index` and `in` give when absent, and when to use each
- [ ] Why `-1` is specifically dangerous in Python
- [ ] When an f-string is parsed and when a `format` template is parsed
- [ ] The one place you should deliberately not use an f-string, and why
- [ ] The spec for "right-aligned, 12 columns, two decimals, thousands separators"
- [ ] The difference between `round(x, 2)` and `f"{x:.2f}"`
- [ ] Who `str` is for and who `repr` is for, with two bugs `repr` reveals
- [ ] Two rules a custom `__repr__` must obey
- [ ] The one rule for when not to use an f-string, and why it is structural
- [ ] Why parameter binding beats escaping
- [ ] The six steps of the normaliser, and the reason for two of the orderings
- [ ] How two strings can render identically and have different lengths
- [ ] Which normalisation form for storage, which for a key, and what the `K` adds
- [ ] One thing normalisation does not fix, and what to do about it instead
- [ ] The test for whether something is a pattern or a fixed string
- [ ] The four costs of a regex, and the three practices that make a necessary one maintainable

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `src/setu/text.py`, `tests/test_text.py` and `data/titles_messy.txt` staged
- [ ] `notebooks/day-07-scratch.ipynb` does **not** appear in `git status` (Principle 6)
- [ ] `uv run ruff format days/day-07-strings/ src/ tests/` has run
- [ ] `uv run python scripts/depth_check.py 7` passes
- [ ] `./m done 7` ran green and created the commit
