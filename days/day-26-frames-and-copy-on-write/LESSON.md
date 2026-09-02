---
day: 26
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 26 — Frames, the str dtype, and Copy-on-Write"
ids: ["PD-01"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 22
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 26 — Frames, the `str` dtype, and Copy-on-Write

**Phase 4 · Pandas 3.0 · Module 4 · opens the phase** · `PD-01` Series, DataFrame, Copy-on-Write and the
`str` dtype, with the plan's named example: **the chained-assignment trap, reproduced live, then fixed
with `.loc`.**

> **Yesterday:** the copy-against-view question in NumPy, and the module that closed Module 3 — an array
> that never touched its caller's memory.
> **Today:** the same question, one layer up. A pandas frame is columns of NumPy-and-Arrow data with
> labels bolted on, and pandas 3.0 changed two things about it that make most existing pandas advice
> wrong: text is now `str` instead of `object`, and every result behaves like a copy. Then the trap that
> the second change turns from a silent wrong answer into a warning you can see.
> **Tomorrow:** the same frame, read from a CSV, a JSON file and a Parquet file — typed at read time
> rather than fixed afterwards.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The shopping list has lived on the back of an envelope on the fridge door for years. Four lines: the
item, how many, what it costs. It works because everybody in the flat can read handwriting and nobody
has ever needed to explain what the second column means.

This week somebody types it into a spreadsheet on the shared laptop, and two things change straight
away.

The first is that every column now has to be **one kind of thing**. The counts column holds numbers. If
somebody types `two` into it, the spreadsheet does not quietly cope the way the envelope did — the cell
goes left-aligned like text, and the total at the bottom stops counting that row. On the envelope, "2"
and "two" were the same instruction to a human. In the spreadsheet they are different kinds of thing,
and the difference is the entire point: a column that is definitely numbers can be added up.

The second change is about copies. Somebody wants to see just the things that cost more than a pound,
so they filter the sheet. They edit one of the rows they can see. Then they clear the filter — and the
edit is not there. It went into the filtered view, which was never the sheet.

That second one is the mistake this day exists for, and it is worth being precise about why it is
nasty. Nothing failed. No message appeared. The number changed on screen exactly as expected, the
person walked away satisfied, and the list was wrong. The way you find out is three days later, when
somebody asks why the flat has been buying two milk since Tuesday.

Everything today is those two changes, in pandas, with the same four-line list.

---

## §2 The map

Twenty-two parts in five sections. Section 1 is what the two objects are. Section 2 is the dtype that
changed in pandas 3.0. Section 3 is the copying rule that changed with it. Section 4 is the trap the two
of them meet in — the plan's named example. Section 5 builds the module and its test.

**Every part uses the same four-line shopping list**: `item`, `need`, `price`, with `"  Milk "` spelled
with a capital and two stray spaces, because that one messy value is what half the day is about.

### `parts/01-the-two-objects/` — what a Series and a DataFrame actually are

| Part | What it answers | Level |
|---|---|---|
| [1.1](parts/01-the-two-objects/1.1-a-column-with-labels.md) — A column with labels | What a Series is, and why the labels travel with the values | foundation |
| [1.2](parts/01-the-two-objects/1.2-the-index-is-not-a-row-number.md) — The index is not a row number | The one misunderstanding that causes most beginner pandas bugs | foundation |
| [1.3](parts/01-the-two-objects/1.3-a-table-of-columns.md) — A table of columns | What a DataFrame is: columns first, rows second, and why that order matters | foundation |
| [1.4](parts/01-the-two-objects/1.4-one-dtype-per-column.md) — One dtype per column | Why the type belongs to the column and not to the table or the cell | working |
| [1.5](parts/01-the-two-objects/1.5-reading-a-frame-before-you-touch-it.md) — Reading a frame first | `dtypes`, `info`, `shape`, `head` — the four questions to ask before any work | working |

### `parts/02-the-str-dtype/` — the pandas 3.0 change that makes old advice wrong

| Part | What it answers | Level |
|---|---|---|
| [2.1](parts/02-the-str-dtype/2.1-text-used-to-be-object.md) — Text used to be `object` | What `object` dtype was, what it cost, and why it lasted so long | foundation |
| [2.2](parts/02-the-str-dtype/2.2-str-the-dtype-pandas-3-infers.md) — `str`, the dtype pandas 3.0 infers | What you now get for a text column, and what changed with it | working |
| [2.3](parts/02-the-str-dtype/2.3-the-storage-behind-it.md) — The storage behind it | `python` against `pyarrow` storage, measured | working |
| [2.4](parts/02-the-str-dtype/2.4-dtypes-equals-object-finds-nothing.md) — `dtypes == object` finds nothing | The migration bug: every existing "find the text columns" snippet now returns an empty list | production |
| [2.5](parts/02-the-str-dtype/2.5-the-missing-value-in-a-text-column.md) — The missing value | `NaN` against `pd.NA`, and why a text column's blank is not a float any more | working |

### `parts/03-copy-on-write/` — every result is independent of what it came from

| Part | What it answers | Level |
|---|---|---|
| [3.1](parts/03-copy-on-write/3.1-every-result-behaves-like-a-copy.md) — Every result behaves like a copy | The rule, stated once, that the rest of the day depends on | foundation |
| [3.2](parts/03-copy-on-write/3.2-the-copy-that-has-not-happened-yet.md) — The copy that has not happened yet | Why "behaves like a copy" is not "is a copy", and what that buys you | working |
| [3.3](parts/03-copy-on-write/3.3-the-question-that-stopped-mattering.md) — The question that stopped mattering | Yesterday's view-or-copy question, and why pandas 3.0 retired it | working |
| [3.4](parts/03-copy-on-write/3.4-to-numpy-and-the-read-only-array.md) — `to_numpy` and the read-only array | Where the frame ends and NumPy begins, and the flag that guards the seam | production |

### `parts/04-chained-assignment/` — the plan's named example, reproduced and fixed

| Part | What it answers | Level |
|---|---|---|
| [4.1](parts/04-chained-assignment/4.1-the-write-that-vanished.md) — The write that vanished | The trap, run live: the assignment that changed nothing | foundation |
| [4.2](parts/04-chained-assignment/4.2-two-brackets-two-calls.md) — Two brackets, two calls | Why `frame["a"][0] = x` is two operations and the second one is orphaned | working |
| [4.3](parts/04-chained-assignment/4.3-loc-the-single-step.md) — `.loc`, the single step | The fix, and why one bracket pair is a different operation and not a tidier one | working |
| [4.4](parts/04-chained-assignment/4.4-settingwithcopy-is-gone.md) — `SettingWithCopyWarning` is gone | What replaced it, and why the replacement is called an `Error` but is a warning | production |
| [4.5](parts/04-chained-assignment/4.5-the-filtered-frame-that-warned-nobody.md) — The filtered frame | The version of the trap that still says nothing at all, and how to catch it | production |

### `parts/05-the-module/` — the shape that makes all of it reusable

| Part | What it answers | Level |
|---|---|---|
| [5.1](parts/05-the-module/5.1-the-shopping-list-module.md) — `src/setu/frames.py` | Four functions, one contract: check, return new, never write to the caller's | production |
| [5.2](parts/05-the-module/5.2-asserting-the-schema.md) — Asserting the schema | Collect every problem and raise once, rather than one problem per re-run | production |
| [5.3](parts/05-the-module/5.3-the-test-that-can-go-red.md) — The test that can go red | How to assert on a frame, and the one word that takes six tests down | production |

---

## §3 Setup — run this

```bash
mkdir -p days/day-26-frames-and-copy-on-write/lab
touch src/setu/frames.py tests/test_frames.py
uv add pandas==3.0.5 pyarrow==25.0.1
uv run python -c "import pandas as pd; import pyarrow; print(pd.__version__, pyarrow.__version__)"
```

Expected: `3.0.5 25.0.1`. If either prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Why `pyarrow` is not optional today.** pandas 3.0 makes Arrow-backed storage the default behind the new
`str` dtype, so a pandas installed without it behaves differently from every transcript in this day
([2.3](parts/02-the-str-dtype/2.3-the-storage-behind-it.md)). It is added on the day it is first used,
not up front, which is why it appears here and not on Day 20.

Confirm the two things this day's parts assume about your install:

```bash
uv run python -c "
import pandas as pd
print('str dtype  :', pd.Series(['milk', 'bread']).dtype)
print('CoW gone?  :', hasattr(pd.errors, 'SettingWithCopyWarning'))
print('replacement:', hasattr(pd.errors, 'ChainedAssignmentError'))
"
```

Expected: `str`, `False`, `True`. The second line is the one that surprises people — the warning class
every pandas tutorial written before 2026 talks about has been **removed**, not deprecated
([4.4](parts/04-chained-assignment/4.4-settingwithcopy-is-gone.md)).

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your reps.

**`src/setu/frames.py`** — [5.1](parts/05-the-module/5.1-the-shopping-list-module.md) walks through the
whole module and [5.2](parts/05-the-module/5.2-asserting-the-schema.md) walks through its check.

- `SCHEMA` — the column-name-to-dtype-name dictionary, and the single source of truth for what a
  shopping list is. Day 27 hands this same object to `read_csv`.
- `SchemaError(ValueError)` — the project exception, inheriting from the right built-in.
- `assert_schema(frame)` — collects every problem, raises once, returns the frame it was given.
- `normalise(frame)` — strips and case-folds `item`, returns a new frame.
- `restock(frame, minimum)` — raises every count up to `minimum`, returns a new frame.
- `total(frame)` — the list's cost, converted to a plain Python float at the boundary.
- `TODO(me)`: write the module docstring's contract block yourself — the three promises every function
  makes, in your own words. [5.1](parts/05-the-module/5.1-the-shopping-list-module.md) names them; do
  not copy its sentences.
- `TODO(me)`: add a fifth function, `cheapest(frame, n)`, returning the `n` cheapest rows as a new
  frame. It must go through `assert_schema` and must not use a single square bracket to write anything.
  Decide for yourself what it does when `n` is larger than the frame, and write the decision in the
  docstring.
- `TODO(me)`: decide whether `assert_schema` should reject an **empty** frame that has the right columns
  and dtypes. Write one sentence of justification in a comment either way. There is a defensible answer
  in both directions and the sentence is the deliverable.

**`tests/test_frames.py`** — [5.3](parts/05-the-module/5.3-the-test-that-can-go-red.md) walks through
the whole file.

- One test per promise: the schema's `str`, the same-object return, the message fragments, the
  no-mutation guarantee, the plain float.
- `TODO(me)`: write the tests for your `cheapest` — at least one that asserts the caller's frame is
  untouched, and at least one that asserts on the returned frame with
  `pd.testing.assert_frame_equal`.
- `TODO(me)`: break the module in a **third** way of your own — not `"object"` in `SCHEMA`, and not the
  one in 5.3's check-yourself. Watch what goes red, then record the mutation and the number of failures
  in a `# Seen to fail:` comment block at the bottom of the file. If nothing goes red, you have found a
  gap in the suite, which is worth more than the test you were going to write.

**`lab/chained.py`** — the plan's named example, reproduced live and then fixed. This one is a script
rather than a module, because its whole job is to be run and watched.

- Build the four-line list, attempt the change with `frame["need"][0] = 3`, print the frame afterwards,
  and show that nothing moved ([4.1](parts/04-chained-assignment/4.1-the-write-that-vanished.md)).
- Do the same change with `.loc` and show that it landed
  ([4.3](parts/04-chained-assignment/4.3-loc-the-single-step.md)).
- Do the **silent** version — filter to the rows over a pound, write to the filtered frame — and show
  that the original is unchanged and that nothing was printed at all
  ([4.5](parts/04-chained-assignment/4.5-the-filtered-frame-that-warned-nobody.md)).
- `TODO(me)`: run the file once with `-W error::FutureWarning` and once without, and write a comment at
  the top saying which of the three cases changed behaviour and which did not. The answer is the
  difference between a warning and silence, and it is the single most useful thing to know about this
  trap.

---

## §5 The eval that must be able to fail

`tests/test_frames.py` is RED until `src/setu/frames.py` exists, which is the starting condition rather
than a problem. Write these two first, because they are the two that people leave out and they are the
two that catch this day's bugs:

```python
def test_schema_says_str_not_object() -> None:
    """pandas 3.0 infers `str` for text; a schema saying `object` matches nothing."""
    assert fr.SCHEMA["item"] == "str"
    assert str(shopping_list()["item"].dtype) == fr.SCHEMA["item"]


def test_normalise_leaves_the_caller_frame_alone() -> None:
    """The no-mutation promise, checked on the object the caller still holds."""
    shop = shopping_list()
    out = fr.normalise(shop)
    assert out is not shop
    assert out["item"].tolist() == ["milk", "bread", "eggs", "rice"]
    assert shop["item"].tolist() == ["  Milk ", "bread", "eggs", "rice"]
```

**The mutation to watch.** Change one word in `src/setu/frames.py` — `"item": "str"` to
`"item": "object"`, which is the value that line would have held before pandas 3.0 — and run the suite.
Six tests go red from one word. Change it back and all twelve go green.
[5.3](parts/05-the-module/5.3-the-test-that-can-go-red.md) has the transcript and explains why the
failure count is six rather than one.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)). The build brief
asks you for a third mutation of your own choosing, and that one matters more than the two given here.

---

## §6 Request budget

**Zero.** No model calls, no network at run time, no API keys, no cost. Everything today is pandas,
pyarrow, pytest and a four-line shopping list typed into the file.

The one thing that costs anything is the install: `uv add pandas==3.0.5 pyarrow==25.0.1` downloads
roughly 60 MB of wheels once, and pyarrow is most of it. After that the day is offline. The
documentation URLs in §8 are the only network the day asks for, and they are read rather than called.

---

## §7 Traps

**Assuming a text column is `object`.** Every "select the text columns" snippet written before pandas
3.0 — `frame.dtypes == object`, `select_dtypes(include="object")` — now matches nothing at all, and
matching nothing is not an error. It is an empty list and a pipeline that quietly skips a stage
([2.4](parts/02-the-str-dtype/2.4-dtypes-equals-object-finds-nothing.md)).

**Reading a pandas answer written before 2026.** Most of the internet's pandas advice is about a version
where `SettingWithCopyWarning` existed, `copy=True` was a thing you passed, and text was `object`. The
advice is not stale in a small way; on this day's three subjects it is wrong in the specific sense of
producing different behaviour ([4.4](parts/04-chained-assignment/4.4-settingwithcopy-is-gone.md)).

**Two square brackets on the left of an `=`.** `frame["need"][0] = 3` is two calls, and the write goes
into the object the first call returned, which nobody holds
([4.2](parts/04-chained-assignment/4.2-two-brackets-two-calls.md)). One pair of brackets and a `.loc` is
not a tidier version of the same thing — it is a different operation
([4.3](parts/04-chained-assignment/4.3-loc-the-single-step.md)).

**Writing to a frame you got from a filter.** This is the same trap with the warning removed: the
filtered frame is a real, independent frame, so writing to it is legal, succeeds, and changes nothing
you care about ([4.5](parts/04-chained-assignment/4.5-the-filtered-frame-that-warned-nobody.md)).

**Treating the index as a row number.** It is a label. After a filter the labels are whatever survived,
so `.loc[0]` and "the first row" are different questions and sometimes different rows
([1.2](parts/01-the-two-objects/1.2-the-index-is-not-a-row-number.md)).

**Comparing frames with `==` inside an `assert`.** It builds a frame of booleans and then raises
`ValueError: The truth value of a DataFrame is ambiguous`, which is an error in the test rather than a
failing test ([5.3](parts/05-the-module/5.3-the-test-that-can-go-red.md)).

**`isinstance(x, float)` on a value that came out of pandas.** `np.float64` is a subclass of `float`, so
the check passes on exactly the value you were trying to catch. `type(x) is float` is the one that means
it — the same trap as yesterday, one library along
([Day 25, 5.1](../day-25-copy-view-and-the-gate/parts/05-the-gate/5.1-the-eval.md)).

**Expecting `7.67`.** The list totals `7.669999999999999`, because `1.15` and `0.32` are not storable in
binary. That is not a pandas fact, it is a float fact
([Day 20, 2.3](../day-20-arrays-and-dtypes/parts/02-dtypes/2.3-floats-nan-and-precision.md)), and
`pytest.approx` is the fix.

---

## §8 Verify before you code

Fetched and read on the day of writing — read them again today rather than trusting this list, because
this is the one module in the plan whose subject changed under a major version:

- **Copy-on-Write** — the page this day's sections 3 and 4 expand, including *"Copy-on-Write is now the
  default with pandas 3.0"* and the definition of chained assignment as *"a technique where an object is
  updated through two subsequent indexing operations"*:
  <https://pandas.pydata.org/docs/user_guide/copy_on_write.html>
- **What's new in 3.0.0** — the release notes for the two changes this day is about, the `str` dtype and
  the removal of `SettingWithCopyWarning`:
  <https://pandas.pydata.org/docs/whatsnew/v3.0.0.html>
- **Text data types** — what `str` is, what `object` was, and the storage options behind it:
  <https://pandas.pydata.org/docs/user_guide/text.html>
- **Working with missing data** — `pd.NA` against `NaN`, and which one a `str` column uses:
  <https://pandas.pydata.org/docs/user_guide/missing_data.html>
- **Indexing and selecting data** — the `.loc` reference, and the section on why chained indexing is a
  different operation from a single call:
  <https://pandas.pydata.org/docs/user_guide/indexing.html>
- **`pandas.DataFrame.assign`** — the method the module's transforms are built on:
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html>
- **`pandas.testing.assert_frame_equal`** — the comparison the tests use instead of `==`:
  <https://pandas.pydata.org/docs/reference/api/pandas.testing.assert_frame_equal.html>

---

## §9 Say it in an interview

A pandas frame is a dictionary of columns, each column one dtype, with a shared index of labels bolted
across them — and almost every beginner bug comes from thinking the index is a row number when it is a
label. pandas 3.0 changed two things that make most existing pandas advice wrong. Text columns are now
`str` instead of `object`, so every snippet that finds text columns by comparing dtypes against `object`
now silently matches nothing, which is worse than an error because a pipeline just skips a stage. And
Copy-on-Write became the default, which means every result you get out of a frame behaves like an
independent copy — the copy is lazy, so you do not pay for it until somebody writes — and that in turn
killed the chained-assignment trap. `frame["need"][0] = 3` is two calls: the first returns a column, the
second writes into that column, and under Copy-on-Write that column is nobody's, so the write lands in
an object that is thrown away. It used to be a `SettingWithCopyWarning`; that class has been removed and
`ChainedAssignmentError` replaces it, which despite the name inherits from `Warning`, so it does not
stop the program. The fix is `.loc[row, column] = value`, one call on the frame itself. The version that
still says nothing is writing to a frame you got from a filter — that is a legitimate independent frame,
so the write succeeds and changes nothing you keep. In my own code I put every transform behind a schema
check that names every problem at once, return a new frame every time, and test the promise by asserting
the caller's frame is unchanged after every call.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, `tests/test_frames.py` is green, you have watched
it go red for at least three different reasons and can name each one, and `lab/chained.py` reproduces
the trap and its fix in one run. Done is defined by understanding and by green checks — never by elapsed
time (Principle 17).
