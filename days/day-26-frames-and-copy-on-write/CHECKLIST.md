# Day 26 — CHECKLIST

**IDs covered:** `PD-01` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 10, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 22, in [`parts/`](parts/) · **Kind:** lab

> `./m done 26` refuses to commit while any box below is unticked. Ticking a box you did not do costs you
> the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **This day opens a module on a library that changed under a major version.** Most of what is written
> about pandas describes the version before this one, so the boxes below that say "ran it and saw the
> output myself" are the only ones that mean anything. Do not tick one because a part said it would
> happen.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python days/day-26-frames-and-copy-on-write/lab/chained.py \
  && uv run pytest tests/test_frames.py -v \
  && ./m depth 26 \
  && ./m check
```

Expected: the trap reproduced and then fixed in one run, twelve or more tests passing, a green depth
report for day 26, then a green gate.

---

## Setup

- [ ] Ran `./m scaffold 26` and created `src/setu/frames.py` and `tests/test_frames.py`
- [ ] Ran `uv add pandas==3.0.5 pyarrow==25.0.1` and committed the changed `uv.lock`
- [ ] Confirmed `pd.__version__` is `3.0.5` and `pyarrow.__version__` is `25.0.1`
- [ ] If either has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the three-line probe in §3 and saw `str`, `False`, `True` with my own eyes
- [ ] Typed the four-line shopping list — `"  Milk "` with the capital and the two spaces — and used the
      same one for every part today

---

## Section 1 — the two objects

- [ ] Read [1.1 — a column with labels](parts/01-the-two-objects/1.1-a-column-with-labels.md), ran its check-yourself, answered its out-loud question
- [ ] Can say what a Series is without using the word "column"
- [ ] Read [1.2 — the index is not a row number](parts/01-the-two-objects/1.2-the-index-is-not-a-row-number.md), ran its check-yourself, answered its out-loud question
- [ ] Filtered the list, looked at the surviving index labels, and can say why they are not `0, 1, 2`
- [ ] Read [1.3 — a table of columns](parts/01-the-two-objects/1.3-a-table-of-columns.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — one dtype per column](parts/01-the-two-objects/1.4-one-dtype-per-column.md), ran its check-yourself, answered its out-loud question
- [ ] Put a string into the `need` column, printed `dtypes`, and recorded what the whole column became
- [ ] Read [1.5 — reading a frame first](parts/01-the-two-objects/1.5-reading-a-frame-before-you-touch-it.md), ran its check-yourself, answered its out-loud question
- [ ] Ran `info()` on the list and can say what each of its lines is telling me

---

## Section 2 — the `str` dtype

- [ ] Read [2.1 — text used to be object](parts/02-the-str-dtype/2.1-text-used-to-be-object.md), ran its check-yourself, answered its out-loud question
- [ ] Can say what `object` dtype actually stored, and why that cost what it cost
- [ ] Read [2.2 — `str`, the dtype pandas 3.0 infers](parts/02-the-str-dtype/2.2-str-the-dtype-pandas-3-infers.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — the storage behind it](parts/02-the-str-dtype/2.3-the-storage-behind-it.md), ran its check-yourself, answered its out-loud question
- [ ] Measured `python` against `pyarrow` storage on my own machine and recorded both numbers
- [ ] Read [2.4 — `dtypes == object` finds nothing](parts/02-the-str-dtype/2.4-dtypes-equals-object-finds-nothing.md), ran its check-yourself, answered its out-loud question
- [ ] **Ran the old snippet and watched it return an empty list**, rather than reading that it would
- [ ] Read [2.5 — the missing value](parts/02-the-str-dtype/2.5-the-missing-value-in-a-text-column.md), ran its check-yourself, answered its out-loud question
- [ ] Can say what `!=` returns when one side is `pd.NA`, and what that does to a filter

---

## Section 3 — Copy-on-Write

- [ ] Read [3.1 — every result behaves like a copy](parts/03-copy-on-write/3.1-every-result-behaves-like-a-copy.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — the copy that has not happened yet](parts/03-copy-on-write/3.2-the-copy-that-has-not-happened-yet.md), ran its check-yourself, answered its out-loud question
- [ ] Can say what "lazy" buys, and name the moment the copy actually happens
- [ ] Read [3.3 — the question that stopped mattering](parts/03-copy-on-write/3.3-the-question-that-stopped-mattering.md), ran its check-yourself, answered its out-loud question
- [ ] Said out loud how yesterday's NumPy view-or-copy question differs from this one, and why pandas
      could retire it while NumPy cannot
- [ ] Read [3.4 — `to_numpy` and the read-only array](parts/03-copy-on-write/3.4-to-numpy-and-the-read-only-array.md), ran its check-yourself, answered its out-loud question
- [ ] Tried to write into the array `to_numpy()` returned and recorded the exact error text

---

## Section 4 — the chained-assignment trap (the plan's named example)

- [ ] Read [4.1 — the write that vanished](parts/04-chained-assignment/4.1-the-write-that-vanished.md), ran its check-yourself, answered its out-loud question
- [ ] **Reproduced the trap myself** and recorded the exact `ChainedAssignmentError` text
- [ ] Read [4.2 — two brackets, two calls](parts/04-chained-assignment/4.2-two-brackets-two-calls.md), ran its check-yourself, answered its out-loud question
- [ ] Can name, in order, the two calls `frame["need"][0] = 3` actually makes
- [ ] Read [4.3 — `.loc`, the single step](parts/04-chained-assignment/4.3-loc-the-single-step.md), ran its check-yourself, answered its out-loud question
- [ ] **Fixed the trap with `.loc`** and watched the change land in the original frame
- [ ] Read [4.4 — `SettingWithCopyWarning` is gone](parts/04-chained-assignment/4.4-settingwithcopy-is-gone.md), ran its check-yourself, answered its out-loud question
- [ ] Checked `hasattr(pd.errors, "SettingWithCopyWarning")` myself and can say why the replacement is
      called an `Error` but does not stop the program
- [ ] Read [4.5 — the filtered frame that warned nobody](parts/04-chained-assignment/4.5-the-filtered-frame-that-warned-nobody.md), ran its check-yourself, answered its out-loud question
- [ ] **Ran the silent version** and confirmed that nothing at all was printed

---

## Section 5 — the module

- [ ] Read [5.1 — `src/setu/frames.py`](parts/05-the-module/5.1-the-shopping-list-module.md), ran its check-yourself, answered its out-loud question
- [ ] Can state the module's three promises without looking
- [ ] Read [5.2 — asserting the schema](parts/05-the-module/5.2-asserting-the-schema.md), ran its check-yourself, answered its out-loud question
- [ ] Can say why the dtype loop needs its `continue`, and what the function would do without it
- [ ] Ran the `python -O` demonstration and can say why `assert` is not a validator
- [ ] Read [5.3 — the test that can go red](parts/05-the-module/5.3-the-test-that-can-go-red.md), ran its check-yourself, answered its out-loud question
- [ ] Wrote `assert out == shop` on purpose once, and recorded the `truth value ... is ambiguous` text

---

## Build

- [ ] `src/setu/frames.py` exists with `SCHEMA`, `SchemaError`, `assert_schema`, `normalise`, `restock`
      and `total`
- [ ] `SCHEMA["item"]` is `"str"` and I can say what it would have been on pandas 2.x and why that
      matters
- [ ] `TODO(me)`: wrote the module docstring's contract block in my own words, not copied from 5.1
- [ ] `TODO(me)`: wrote `cheapest(frame, n)`, with its out-of-range behaviour decided and documented
- [ ] `TODO(me)`: wrote the one-sentence justification for how `assert_schema` treats an empty frame
- [ ] No function in the module writes to its argument, and I checked rather than assumed
- [ ] No single square bracket appears on the left of an `=` anywhere in the module

---

## The lab script

- [ ] `lab/chained.py` reproduces the vanished write, prints the frame afterwards, and shows nothing moved
- [ ] It then does the same change with `.loc` and shows that it landed
- [ ] It runs the silent filtered-frame version and shows that nothing was printed
- [ ] `TODO(me)`: ran it with `-W error::FutureWarning` and without, and wrote the difference in a
      comment at the top of the file

---

## Tests

- [ ] `tests/test_frames.py` has one test per promise the module makes
- [ ] Watched the whole suite go RED before the module existed, and can say what the failure was
- [ ] **Mutation 1:** changed `SCHEMA["item"]` to `"object"`, ran the suite, recorded how many went red
- [ ] Can say why that one word took down more than one test
- [ ] **Mutation 2:** made `normalise` edit its argument instead of returning a new frame, and confirmed
      the no-mutation test caught it
- [ ] **Mutation 3 (mine):** picked my own break, watched it go red, and recorded it in the
      `# Seen to fail:` block
- [ ] `TODO(me)`: wrote the tests for `cheapest`, including one using `pd.testing.assert_frame_equal`
- [ ] Every float comparison uses `pytest.approx`, and I can say why `== 7.67` fails on correct code
- [ ] `uv run ruff format days/day-26-frames-and-copy-on-write/` is clean, because ruff formats Python
      inside Markdown too

---

## Budget

- [ ] **Request budget: zero.** No model calls, no API keys, no paid anything (Principle 5)
- [ ] Confirmed the only network today was the wheel download and the §8 documentation pages

---

## Commit

- [ ] `./m depth 26` passes with no failures
- [ ] `./m check` is green
- [ ] `./m tracker` re-run so `docs/TRACKER.md` and `days/INDEX.md` include day 26
- [ ] Committed with the day number in the message — no commit means the day is not done (Principle 1)
