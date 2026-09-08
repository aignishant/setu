---
day: 30
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 30 — Missing data, and why the imputer lives in the pipeline"
ids: ["PD-07"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 22
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 30 — Missing data, and why the imputer lives in the pipeline

**Phase 4 · Pandas 3.0 · Module 4** · `PD-07` missing data — `NA`, `fillna`, `dropna`, `interpolate`
— with the plan's named example: **why the median goes in the pipeline, not the dataframe**
(Principle 8).

> **Yesterday:** two ways of not making pandas decide something per row — vectorising instead of
> looping, and deciding a tie instead of letting the sort algorithm decide it.
> **Today:** the empty box. What it is, how to find it, why it is empty, and the three things you can
> do about it — none of which is free, and one of which is a correctness bug that produces no error.
> **Tomorrow:** `groupby` — split, apply, combine — which is the tool today's group-wise fill was
> borrowing in advance.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The flat does the shop on a Saturday and pins the receipt to the fridge so the money can be split on
Sunday. This Saturday the receipt came out of a pocket in two pieces, and the tear went straight
through the line with the eggs on it.

Somebody types the list up anyway and leaves that one box empty. Six eggs, aisle seven, who paid —
all of it is there. Just not what they cost.

On Sunday somebody adds up the column and gets four pounds sixty. Nobody blinks, because four pounds
sixty is a perfectly believable Saturday shop. Somebody else works out the average price of a thing
and gets one pound fifty-three. Also believable. One of those numbers treated the missing egg price
as nothing, and the other treated it as not there, and **nobody made either of those decisions**.

That is the whole day, and it is worth saying what makes it different from the days before it. A
missing value does not crash anything. There is no traceback, no warning, no red text. Every function
you call has already decided what to do about the blank, quietly and reasonably, and the number that
comes out is plausible. **The failure mode of this subject is a believable answer**, which is why it
gets its own day and why the day has more "when it breaks" sections without an error message than any
day so far.

Then it gets worse in an interesting way. Suppose the tear was not random. Suppose the frozen-aisle
receipts fade because the kiosk prints on thin paper, so the missing prices are all frozen things,
and frozen things are dearer. Now throwing away the blank lines does not just lose data — it makes
the shop look cheaper than it was. The blanks were not scattered; they were *selected*, and deleting
them was a selection too.

And then the last turn, which is the one the plan names. To fill the blanks you need a number — say,
the middle price of the sheet. If you work that number out from the whole year and then hide the last
six months to test yourself on, the number you wrote into the first six months was computed partly
from the six months you were supposed to be hiding. You have not looked at the hidden half. You have
still cheated, and the only way to see it is to change one line in the hidden half and watch the
visible half move.

So: an empty box is a decision waiting to be made. Today is about making it on purpose, writing down
what you decided, and doing it in an order that does not lie to you about how well it worked.

---

## §2 The map

Seven sections, and they are in the order you would actually work: understand the blank, find it,
ask why it is there, then the three things you can do — drop, fill, or fill in a way that leaks —
and finally the module.

| Section | What it means |
|---|---|
| **1.x** | **What missing means** — the value that means "no value", and its four spellings |
| **2.x** | **Finding it** — the mask, the profile, and the blank that was never blank |
| **3.x** | **Why it is missing** — the question that decides everything you are allowed to do next |
| **4.x** | **Dropping** — deleting rows, deleting columns, and what each choice costs |
| **5.x** | **Filling** — a constant, a group, a neighbour, a line between two points |
| **6.x** | **The leak** — the plan's named example, and the discipline that prevents it |
| **7.x** | **The module** — the rules written down, and a test that can actually go red |

### Section 1 — what missing means

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [The price nobody wrote down](parts/01-what-missing-means/1.1-the-price-nobody-wrote-down.md) | What is a blank, and what does each function do with it? | `foundation` |
| 1.2 | [`NaN`, the number not equal to itself](parts/01-what-missing-means/1.2-nan-the-number-not-equal-to-itself.md) | Why does `price == NaN` find nothing? | `foundation` |
| 1.3 | [`None` is not what gets stored](parts/01-what-missing-means/1.3-none-is-not-what-gets-stored.md) | You typed `None`; what went in? | `foundation` |
| 1.4 | [`pd.NA`, and the answer that is unknown](parts/01-what-missing-means/1.4-pd-na-and-the-answer-unknown.md) | The nullable dtypes and three-valued logic | `working` |
| 1.5 | [One column, one dtype, one kind of blank](parts/01-what-missing-means/1.5-one-dtype-one-kind-of-blank.md) | `NaN`, `NaT`, `<NA>` — which one, and why | `working` |

### Section 2 — finding it

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [`isna` and `notna`](parts/02-finding-it/2.1-isna-and-notna.md) | How do you point at the blanks? | `foundation` |
| 2.2 | [Counting the blanks](parts/02-finding-it/2.2-counting-the-blanks.md) | The one-line profile you run on every table | `working` |
| 2.3 | [The blank that was not blank](parts/02-finding-it/2.3-the-blank-that-was-not-blank.md) | Zero missing values and an average of −248 | `production` |

### Section 3 — why it is missing

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [Three reasons a line is blank](parts/03-why-it-is-missing/3.1-three-reasons-a-line-is-blank.md) | Which blanks can be fixed by arithmetic, and which cannot | `working` |
| 3.2 | [The blank that is itself a signal](parts/03-why-it-is-missing/3.2-the-blank-that-is-itself-a-signal.md) | When emptiness is the best feature you have | `production` |

### Section 4 — dropping

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [`dropna`, and the rows that left](parts/04-dropping/4.1-dropna-and-the-rows-that-left.md) | Why did one line survive out of four? | `foundation` |
| 4.2 | [`how`, `thresh` and `subset`](parts/04-dropping/4.2-how-thresh-and-subset.md) | Dropping on the fields that actually matter | `working` |
| 4.3 | [Dropping the column instead](parts/04-dropping/4.3-dropping-the-column-instead.md) | One fact about everyone, or everything about most | `production` |

### Section 5 — filling

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [`fillna` is a claim](parts/05-filling/5.1-fillna-is-a-claim.md) | What a fill does to the mean, the spread and the correlations | `working` |
| 5.2 | [A different fill for each column](parts/05-filling/5.2-a-different-fill-for-each-column.md) | One value per column, and one per group | `working` |
| 5.3 | [`ffill`, `bfill`, and the order you depend on](parts/05-filling/5.3-ffill-bfill-and-the-order-you-depend-on.md) | Filling from a neighbour, and what a neighbour requires | `working` |
| 5.4 | [`interpolate`, and the line between two points](parts/05-filling/5.4-interpolate-and-the-line-between-two-points.md) | The gap filled smoothly — by row, or by time? | `production` |

### Section 6 — the leak

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [The median that saw the test set](parts/06-the-leak/6.1-the-median-that-saw-the-test-set.md) | The plan's named example, demonstrated in one line | `production` |
| 6.2 | [Fit on train, transform on both](parts/06-the-leak/6.2-fit-on-train-transform-on-both.md) | The two operations that make the leak hard to write | `production` |
| 6.3 | [The imputer you write yourself](parts/06-the-leak/6.3-the-imputer-you-write-yourself.md) | The object, before you meet the library one | `production` |

### Section 7 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 7.1 | [`src/setu/missing.py`](parts/07-the-module/7.1-the-missing-module.md) | Where does each of the day's rules live? | `production` |
| 7.2 | [The test that can go red](parts/07-the-module/7.2-the-test-that-can-go-red.md) | How do you test a bug that never raises? | `production` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-30-missing-data/lab
touch src/setu/missing.py tests/test_missing.py
uv run python -c "import pandas as pd; import numpy as np; print(pd.__version__, np.__version__)"
```

Expected: `3.0.5 2.5.2`. If either prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Nothing is installed today.** Everything comes from Day 26's `uv add pandas==3.0.5
pyarrow==25.0.1`.

Confirm the one behaviour every part of this day rests on:

```bash
uv run python -c "
import numpy as np
import pandas as pd
print('NaN == NaN        :', np.nan == np.nan)
print('pd.NA == pd.NA    :', pd.NA == pd.NA)
print('None == None      :', None is None)
print('isna finds all    :', pd.isna(np.nan), pd.isna(pd.NA), pd.isna(None), pd.isna(pd.NaT))
s = pd.Series([1.15, 1.40, None, 2.05])
print('len vs count      :', len(s), s.count())
print('sum vs mean       :', s.sum(), round(s.mean(), 4))
print('sum of all-blank  :', pd.Series([None, None], dtype='float64').sum())
"
```

Expected: `False` on the first line, `<NA>` on the second, and `4.6 1.5333` on the sums. **The last
line printing `0.0` is the single most important default on the day** — a column that failed to load
entirely sums to a confident zero
([1.1](parts/01-what-missing-means/1.1-the-price-nobody-wrote-down.md)).

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/missing.py`** — [7.1](parts/07-the-module/7.1-the-missing-module.md) walks through the
whole module.

- `REQUIRED` and `MAX_DROP_SHARE` — the day's two policy decisions, as module constants.
- `ImputationError(ValueError)` — for a fill that could not be learned or applied as promised. Import
  Day 28's `SelectionError` rather than defining a fifth exception meaning "this frame is wrong".
- `profile(frame)` — rows, values, blanks, share, dtype, **returned not printed**
  ([2.2](parts/02-finding-it/2.2-counting-the-blanks.md)).
- `require_complete(frame, columns)` — raises, naming the columns and the first offending rows
  ([2.1](parts/02-finding-it/2.1-isna-and-notna.md)).
- `blank_rate_by(frame, column, by)` — evidence about *why*, ranked by spread, with **no verdict**
  ([3.1](parts/03-why-it-is-missing/3.1-three-reasons-a-line-is-blank.md)).
- `drop_incomplete(frame, required, max_loss)` — refuses above the loss share, logs the empty-row and
  incomplete-row counts separately ([4.2](parts/04-dropping/4.2-how-thresh-and-subset.md)).
- `MedianImputer` — `fit` learns, `transform` applies, the flag is written before the fill, and
  "not fitted" raises ([6.3](parts/06-the-leak/6.3-the-imputer-you-write-yourself.md)).
- `fill_by_group(frame, column, by, min_group)` — group median with a global fallback and a minimum
  group size ([5.2](parts/05-filling/5.2-a-different-fill-for-each-column.md)).
- `carry_forward(frame, column)` — **as given, this calls `ffill` on the whole frame: no sort, no
  group, no limit.** It fills one flat's blank from another flat's meter reading
  ([5.3](parts/05-filling/5.3-ffill-bfill-and-the-order-you-depend-on.md)).
- `TODO(me)`: fix `carry_forward`. Give it `by`, `order` and `limit`, make all three required, and
  make it raise if the ordering column has blanks in it. Then write one sentence in the docstring
  saying what each of the three protects against.
- `TODO(me)`: `MedianImputer` has no `save`/`load`. Add them, with a `schema_version` in the payload
  ([6.3](parts/06-the-leak/6.3-the-imputer-you-write-yourself.md) sketches the shape). Then answer in
  a comment: what breaks if `add_indicator` is not written into the file?
- `TODO(me)`: add `sentinel_report(frame, suspects)` — given a list of suspicious values per column,
  report how many of each appear. [2.3](parts/02-finding-it/2.3-the-blank-that-was-not-blank.md)
  argues for the range check as the second line of defence; decide whether your version does both,
  and say why in the docstring.

**`tests/test_missing.py`** — [7.2](parts/07-the-module/7.2-the-test-that-can-go-red.md) walks
through the whole file.

- A fixture, not a module-level frame, with the blanks in known places.
- The four kinds of assertion: the **value** a function returns, what it does **not** change, what it
  **refuses**, and where a learned number **came from**.
- The leak test: fit on train, change a row in the held-back half, assert the learned value did not
  move. **Write this one first.**
- `TODO(me)`: write the tests for your fixed `carry_forward`, and delete the `xfail` marker when they
  pass. `strict=True` will tell you when.
- `TODO(me)`: add the round-trip test for `save`/`load` — save, load, transform the same frame with
  both objects, assert the results are identical.
- `TODO(me)`: break the module a **second** way of your own — not the swapped flag lines and not the
  leaking `fit`. Watch what goes red, then record the change and the failure count in a
  `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say which
  test should have caught it and why it did not.

**`lab/why_it_is_missing.py`** — the day's argument, made runnable on data where you know the truth.

- Build the three cases from
  [3.1](parts/03-why-it-is-missing/3.1-three-reasons-a-line-is-blank.md) from the day's seed, and
  print the true mean, the mean after dropping, and the per-group means for each.
- Print the blank-rate-by-group report for each case, so you can see which cases the diagnostic
  catches and which it does not.
- `TODO(me)`: add a fourth case of your own where the blank rate is flat across every visible column
  and the answer is still biased. Say in a comment what that proves about the diagnostic.
- `TODO(me)`: for case B, compare a global median fill against a group median fill, and report how
  much of the bias each one removes. Record both numbers.

---

## §5 The eval that must be able to fail

`tests/test_missing.py` is RED until `src/setu/missing.py` exists. Write these two first, because
they are the two that carry the day:

```python
def test_fit_does_not_see_rows_it_was_not_given() -> None:
    """The learned median must not move when a held-back row changes."""
    train = pd.DataFrame({"price": [1.0, None, 2.0, 3.0]})
    test = pd.DataFrame({"price": [10.0, 11.0, None, 12.0]})

    learned_before = dict(MedianImputer(["price"]).fit(train).values_)
    test.loc[3, "price"] = 1000.0

    assert MedianImputer(["price"]).fit(train).values_ == learned_before


def test_indicator_counts_the_blanks_that_were_there_before_the_fill(shop) -> None:
    blanks_before = int(shop["price"].isna().sum())
    assert blanks_before == 1, "the fixture must contain a blank"
    out = MedianImputer(["price"]).fit(shop).transform(shop)
    assert out["price_was_missing"].sum() == blanks_before
```

**`dict(...)` around `values_` is the point of the first one.** Without the copy you compare a
dictionary to itself and the test passes whatever `fit` does — the same class of mistake as Day 29's
fixture that had no tie in it.

**The assertion on `blanks_before` is the point of the second one.** Without it, a fixture edit that
removed the blank would make the real assertion `0 == 0` and the test would go on passing while
guarding nothing.

**The mutations to watch.** Three, and they behave differently:

1. In `MedianImputer.transform`, swap the two lines so the flag is computed after the fill. **One
   test goes red**, with `assert 0 == 1`. Nothing else notices, and the column is now useless
   ([3.2](parts/03-why-it-is-missing/3.2-the-blank-that-is-itself-a-signal.md)).
2. In `MedianImputer.fit`, change `strategy` to the mean. **The value assertions go red**, which is
   correct — the fill value is part of the contract, not an implementation detail.
3. Change `fit` to take the whole dataset rather than the training frame. **Only the leak test goes
   red.** Delete that test and this bug ships silently, which is the argument for writing it.

And one that **no correctness test can catch**: change `drop_incomplete`'s `max_loss` from `0.02` to
`0.9`. Every test stays green, every function still works, and the pipeline will now silently discard
most of a bad batch. The defences are a test asserting the constant's value and a review that treats
a policy change as a policy change.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed.

The largest thing the day builds in memory is the twenty-thousand-row series in
[5.1](parts/05-filling/5.1-fillna-is-a-claim.md) and the ten-thousand by twenty block in
[4.1](parts/04-dropping/4.1-dropna-and-the-rows-that-left.md) — under two megabytes each. Nothing is
written to disk except the module, the tests and the lab script.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **A blank is not a zero and not an empty string.** `sum` skips it, `mean` skips it *and* shrinks
  the divisor, `len` counts the row anyway
  ([1.1](parts/01-what-missing-means/1.1-the-price-nobody-wrote-down.md)).
- **A column of nothing but blanks sums to `0.0`** — a confident number indistinguishable from a
  column of genuine zeroes ([1.1](parts/01-what-missing-means/1.1-the-price-nobody-wrote-down.md)).
- **`NaN == NaN` is `False`**, so `df[df["x"] == None]` returns no rows, with no error
  ([1.2](parts/01-what-missing-means/1.2-nan-the-number-not-equal-to-itself.md)).
- **`if series.isna():` raises** `ValueError: The truth value of a Series is ambiguous`. You meant
  `.any()` or `.all()` ([2.1](parts/02-finding-it/2.1-isna-and-notna.md)).
- **A count of blanks is meaningless without the row count.** 404 of 500 is a broken column; 516 of
  500 000 is fine ([2.2](parts/02-finding-it/2.2-counting-the-blanks.md)).
- **`df.info()` prints and returns `None`.** It cannot be asserted on, logged or diffed
  ([2.2](parts/02-finding-it/2.2-counting-the-blanks.md)).
- **A sentinel is not a blank.** `-999` in a price column gives zero missing values and an average of
  −248 ([2.3](parts/02-finding-it/2.3-the-blank-that-was-not-blank.md)).
- **`na_values=[-999]` applies to every column** unless you pass the dictionary form, and it will
  erase a legitimate −999 elsewhere ([2.3](parts/02-finding-it/2.3-the-blank-that-was-not-blank.md)).
- **A flat blank rate is not proof the blanks are random**, because the cause may be the missing value
  itself ([3.1](parts/03-why-it-is-missing/3.1-three-reasons-a-line-is-blank.md)).
- **Computing the missingness flag after the fill gives a column of `False`**, silently
  ([3.2](parts/03-why-it-is-missing/3.2-the-blank-that-is-itself-a-signal.md)).
- **`dropna()` deletes rows, not blanks.** Twenty columns at five per cent blank each leaves about
  thirty-five per cent of the rows ([4.1](parts/04-dropping/4.1-dropna-and-the-rows-that-left.md)).
- **`df.dropna()` on its own line does nothing.** You have to assign the result
  ([4.1](parts/04-dropping/4.1-dropna-and-the-rows-that-left.md)).
- **`how` and `thresh` cannot be combined** — `TypeError` — and `thresh=2` means "keep rows with at
  least two real values", not "drop rows with two or more blanks"
  ([4.2](parts/04-dropping/4.2-how-thresh-and-subset.md)).
- **`dropna(subset=["typo"])` raises `KeyError`; `fillna({"typo": 0})` does not.** Two methods, two
  conventions ([4.2](parts/04-dropping/4.2-how-thresh-and-subset.md),
  [5.2](parts/05-filling/5.2-a-different-fill-for-each-column.md)).
- **`dropna(axis="columns")` makes the output schema depend on the batch**
  ([4.3](parts/04-dropping/4.3-dropping-the-column-instead.md)).
- **`df.fillna(0)` fills the text columns too**, and turns a `str` column into `object`
  ([5.1](parts/05-filling/5.1-fillna-is-a-claim.md)).
- **A mean fill leaves the mean alone and shrinks everything else** — the spread, and every
  correlation the column had ([5.1](parts/05-filling/5.1-fillna-is-a-claim.md)).
- **A group-wise fill leaves a group with no values untouched**, with no error
  ([5.2](parts/05-filling/5.2-a-different-fill-for-each-column.md)).
- **`ffill` has no concept of a group and no concept of a date.** It copies from the row physically
  above ([5.3](parts/05-filling/5.3-ffill-bfill-and-the-order-you-depend-on.md)).
- **`interpolate()` spaces the fill by row position, not by time.** `method="time"` is one word and
  is not the default ([5.4](parts/05-filling/5.4-interpolate-and-the-line-between-two-points.md)).
- **A trailing gap silently becomes a forward fill** under `interpolate`, and reports no blanks left
  ([5.4](parts/05-filling/5.4-interpolate-and-the-line-between-two-points.md)).
- **`fillna(df.median())` cannot run on one row** — it fills a blank with a blank
  ([6.2](parts/06-the-leak/6.2-fit-on-train-transform-on-both.md)).

**The pattern behind the day.** Every trap above except three produces **no error at all**. That is
the difference between this day and the four before it: Day 26's chained assignment warned, Day 27's
bad dtype was visible in `dtypes`, Day 29's slow loop was slow. Here the wrong answer looks exactly
like the right one, so the defence is not a check you run afterwards — it is an order you work in.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Working with missing data** — <https://pandas.pydata.org/docs/user_guide/missing_data.html> — the
  table of which sentinel goes with which dtype, and the statement that `NA`'s behaviour is still
  experimental and can change without warning.
- **`DataFrame.dropna`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html> — the signature is
  keyword-only after `self`; read the `thresh` description, which is where "cannot be combined with
  how" is stated.
- **`DataFrame.fillna`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html> — note that `value` is
  required and everything after it is keyword-only, and read what `limit` counts.
- **`DataFrame.interpolate`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html> — the default is
  `method="linear"`, documented as *"Ignore the index and treat the values as equally spaced"*, and
  `limit_area` takes `None`, `"inside"` or `"outside"`.
- **`read_csv`** — <https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html> — find
  `na_values` and `keep_default_na`, and read the list of strings pandas already treats as blank.

---

## §9 Say it in an interview

> A missing value in pandas is a real value that means "there is no value", and which one you get
> depends on the column's dtype — `NaN` in a float column, `NaT` in a datetime column, `<NA>` in the
> nullable ones. The thing that trips people is that `NaN` is defined to compare unequal to
> everything including itself, so comparing to it finds nothing and returns an empty result with no
> error; you find blanks with `isna`. Everything downstream has already decided what to do about
> them: `sum` skips them, so it behaves as if they were zero, while `mean` skips them and shrinks the
> divisor. A column that is entirely blank sums to zero, which is a confident number that looks
> exactly like a column of genuine zeroes.
>
> Before doing anything about a blank I want to know why it is there, because that decides what I am
> allowed to do. If the blanks landed at random, dropping the rows costs sample size and nothing
> else. If they depend on some other column I can see — frozen items go missing more often, and
> frozen items are dearer — then dropping is biased and the fix is to work within that column's
> groups. And if they depend on the value that is gone, no arithmetic on the table recovers it; that
> needs new data or an assumption I state out loud. You can gather evidence for the first two by
> comparing the blank rate across every other column, but a flat rate is not proof, because the third
> case is invisible by construction.
>
> Then the practical part. `dropna` deletes rows rather than blanks, and it gets brutal as a table
> gets wider — twenty columns at five per cent missing each leaves about a third of the rows — so I
> pass `subset=` with the fields that are genuinely required rather than accepting the default.
> Filling is a claim: it leaves the mean where it was, shrinks the standard deviation, and weakens
> every correlation the column had, so I keep a boolean column recording where the blanks were,
> computed before the fill, and often that flag is a better feature than the filled values.
>
> The part I would not compromise on is the order. The split comes before the imputer, because a fill
> value is computed from data, so computing it over the whole dataset writes a summary of the test set
> into the training rows. The way to demonstrate it takes one line: change a value in the held-back
> half and watch the number that gets written into a training row move. That is why the imputer is a
> `fit`/`transform` object rather than a function — `fit` sees the training rows and stores the
> values, `transform` applies them to anything, including a single row at serving time. If a cleaning
> step cannot run on one row, it is not a cleaning step, it is a batch summary, and it will have to
> be rewritten before anything ships.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 30` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
