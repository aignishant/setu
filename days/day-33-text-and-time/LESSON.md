---
day: 33
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 33 — The .str and .dt accessors; resampling"
ids: ["PD-11", "PD-12"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 26
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 33 — The `.str` and `.dt` accessors; resampling

**Phase 4 · Pandas 3.0 · Module 4** · `PD-11` text data with the `.str` accessor ·
`PD-12` date and time, `Timedelta`, resampling.

> **Yesterday:** two tables meeting, and the four answers to "what about the rows that did not
> match" — plus the two shapes one table can be in, and the four operations that convert between
> them.
> **Today:** the two columns yesterday's join depended on and neither of us checked. The key was
> text, typed four ways by four people. The date was text that looked like a date. Both have an
> accessor — a doorway with its own set of methods — and both have a way of being quietly wrong that
> no error message ever mentions.
> **Tomorrow:** the same columns again, but asking what they cost to store, and reading
> `describe()` as a list of findings rather than a formality.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Four people share a flat, and they take turns doing the shopping. Whoever goes types what they
bought into the shared file on their phone, with what it cost and when they paid.

One of them types `Milk`. One types `milk` and, because the phone keyboard adds a space after a
word, ends up with `milk ` — the space is there, it just does not show. One has caps lock on and
types `MILK`. One types `milk`.

At the end of the month somebody wants a simple answer: how much did we spend on milk? They open the
file, ask for everything in small letters first, because that would obviously fix it — and the thing
they type, the thing anybody would type, does not work. It does not give a wrong answer and it does
not quietly do nothing. It stops, and says the column does not have that.

That is the first half of the day, and it ends somewhere unpleasant. Lower-casing fixes three of the
four spellings and leaves the fourth exactly as broken as it was, because `milk ` and `milk` are
different values and nothing on the screen tells you which is which. Join the file to the price
sheet with that column as the key and you lose the rows quietly — the sum still prints, still looks
plausible, and is wrong by whatever the invisible space was worth.

The second half is the same shape of trouble wearing a different coat. The `paid_at` column looks
like a date. It sorts, it prints, it has a year in it. It is text. So `max()` gives you the
alphabetically last string, `-` between two of them raises, and the question "what did we spend each
week" has no answer at all, because there is no week — a week is something you have to build.

And when you do build it, one more decision is waiting. Group the receipts by week and the weeks
nobody shopped in are simply absent from the answer. Resample by week and those weeks appear, with a
zero in them. Neither is wrong. One of them says *we spent nothing* and the other says *nothing
happened*, and a chart drawn from the first has a gap where the second has a floor.

So the day has one shape running through both halves. **A column of text is not text, and a column
that looks like time is not time, until somebody says so out loud.** The accessor is how you say it,
and the price of not saying it is a number that is quietly wrong rather than an error that stops
you.

---

## §2 The map

Seven sections. Sections 1 to 3 are `PD-11` — text: what the accessor is, cleaning a key with it,
and pulling a value out of a string. Sections 4 to 6 are `PD-12` — time: making a timestamp,
doing arithmetic on it, and grouping by a bucket of it. Section 7 is where both meet the project's
code.

| Section | What it means |
|---|---|
| **1.x** | **The `.str` accessor** — what it is, what a blank does to it, and the dtype underneath |
| **2.x** | **Cleaning names** — four spellings into one value, and what it costs not to |
| **3.x** | **Pulling text apart** — splitting a value, and extracting a piece with a pattern |
| **4.x** | **The `.dt` accessor** — turning text into timestamps, and what a timestamp is made of |
| **5.x** | **Arithmetic on time** — subtracting, `Timedelta`, and the month that is not thirty days |
| **6.x** | **Resampling** — grouping by a key made of time, and the buckets that were empty |
| **7.x** | **The module** — the day's rules as code, and a test that can actually go red |

### Section 1 — the `.str` accessor

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [The column that has no `.lower()`](parts/01-the-str-accessor/1.1-the-column-that-has-no-lower.md) | Why the obvious line raises, and where the methods actually live | `foundation` |
| 1.2 | [The blank that came back blank](parts/01-the-str-accessor/1.2-the-blank-that-came-back-blank.md) | What a missing value does to every `.str` result | `working` |
| 1.3 | [The dtype under the text, measured](parts/01-the-str-accessor/1.3-the-dtype-under-the-text.md) | `str` against `object`, and what the difference costs | `production` |

### Section 2 — cleaning names

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [Four spellings of milk](parts/02-cleaning-names/2.1-four-spellings-of-milk.md) | The two chained calls that fix the flat's actual bug | `foundation` |
| 2.2 | [`replace`, and the pattern you did not know you wrote](parts/02-cleaning-names/2.2-replace-and-the-regex-default.md) | What a `.` in a replacement means, and to which setting | `working` |
| 2.3 | [`contains`, `startswith`, and the mask](parts/02-cleaning-names/2.3-contains-startswith-and-the-mask.md) | Turning a text test into rows, and what a blank does to it | `working` |
| 2.4 | [The mismatch that costs rows](parts/02-cleaning-names/2.4-the-mismatch-that-costs-rows.md) | The same join before and after normalising, in rows and in money | `production` |

### Section 3 — pulling text apart

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [`split`, and the list that ended up in a cell](parts/03-pulling-text-apart/3.1-split-and-the-list-in-a-cell.md) | Why a column of lists is a dead end | `foundation` |
| 3.2 | [`expand`, and the columns you get](parts/03-pulling-text-apart/3.2-expand-and-the-columns-you-get.md) | A split whose piece count varies is a schema you do not control | `working` |
| 3.3 | [`extract`, and the capture group](parts/03-pulling-text-apart/3.3-extract-and-the-capture-group.md) | Naming the piece you want instead of counting to it | `working` |
| 3.4 | [The pattern that matched nothing](parts/03-pulling-text-apart/3.4-the-pattern-that-matched-nothing.md) | All blanks, no error — and the assertion that catches it | `production` |

### Section 4 — the `.dt` accessor

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [Text that looks like a date is not a date](parts/04-the-dt-accessor/4.1-text-that-looks-like-a-date.md) | What sorts wrong, what raises, and what `.dt` says | `foundation` |
| 4.2 | [`to_datetime`, `format`, and `errors`](parts/04-the-dt-accessor/4.2-to-datetime-format-and-errors.md) | The one conversion, and the two arguments you always pass | `working` |
| 4.3 | [The fields inside a timestamp](parts/04-the-dt-accessor/4.3-the-fields-inside-a-timestamp.md) | Year, month, day of week — views of one number | `working` |
| 4.4 | [The resolution pandas 3 picks](parts/04-the-dt-accessor/4.4-the-resolution-pandas-3-picks.md) | Microseconds, not nanoseconds — and everywhere that bites | `production` |
| 4.5 | [Naive, aware, and the hour that moved](parts/04-the-dt-accessor/4.5-naive-aware-and-the-hour-that-moved.md) | A timestamp with a missing column, and the comparison that raises | `production` |

### Section 5 — arithmetic on time

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [Subtracting two timestamps](parts/05-arithmetic-on-time/5.1-subtracting-two-timestamps.md) | The gap is a `Timedelta`, not a number | `foundation` |
| 5.2 | [`Timedelta`, and the units you have to name](parts/05-arithmetic-on-time/5.2-timedelta-and-its-units.md) | Why `.dt.days` on a gap of forty-seven hours is `1` | `working` |
| 5.3 | [Offsets, and the month that is not thirty days](parts/05-arithmetic-on-time/5.3-offsets-and-the-month-that-is-not-thirty-days.md) | Adding "one month" to 31 January | `production` |

### Section 6 — resampling

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [The index that has to be time](parts/06-resampling/6.1-the-index-that-has-to-be-time.md) | Why resampling asks for the index, and what `on=` does instead | `foundation` |
| 6.2 | [`resample` — the group-by you did not have to write](parts/06-resampling/6.2-resample-the-groupby-you-did-not-write.md) | The same operation, spelled two ways, and the aliases that changed | `working` |
| 6.3 | [The bucket that was empty](parts/06-resampling/6.3-the-bucket-that-was-empty.md) | "Nobody shopped" against "we do not know" | `working` |
| 6.4 | [`label`, `closed`, and which side the edge belongs to](parts/06-resampling/6.4-label-closed-and-the-edge.md) | Two defaults that move every number on an axis | `production` |
| 6.5 | [`rolling` is not `resample`](parts/06-resampling/6.5-rolling-is-not-resample.md) | One row per week, or one window per row | `production` |

### Section 7 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 7.1 | [`src/setu/textdate.py`](parts/07-the-module/7.1-the-textdate-module.md) | Where does each of the day's rules live? | `production` |
| 7.2 | [The test that can go red](parts/07-the-module/7.2-the-test-that-can-go-red.md) | Testing a unique count, a parse failure and a row count | `production` |

**The running example is the flat's shared shopping file** — eight receipts, four items typed eight
ways, and a `paid_at` column that is text. Every part of this day picks up that same file.

---

## §3 Setup — run this

```bash
mkdir -p days/day-33-text-and-time/lab
touch src/setu/textdate.py tests/test_textdate.py
uv run python -c "import pandas as pd; import numpy as np; print(pd.__version__, np.__version__)"
```

Expected: `3.0.5 2.5.2`. If either prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Nothing is installed today.** Everything comes from Day 26's `uv add pandas==3.0.5
pyarrow==25.0.1`.

Confirm the two facts the whole day rests on — the invisible space, and the text that is not a time:

```bash
uv run python -c "
import pandas as pd
item = pd.Series(['Milk', 'milk ', 'MILK', 'milk'], dtype='str')
print('spellings          :', item.nunique())
print('after lower()      :', item.str.lower().nunique())
print('after strip+lower  :', item.str.strip().str.lower().nunique())
paid = pd.Series(['2026-03-01 08:12:30', '2026-03-11 18:22:47'], dtype='str')
print('dtype of paid_at   :', paid.dtype)
try:
    print(paid.max() - paid.min())
except TypeError as e:
    print('subtracting text   :', e)
"
```

Expected: **4 spellings, 2 after lower-casing, 1 after stripping and lower-casing** — and a
`TypeError` on the subtraction. Those three numbers are the entire first half of the day
([2.1](parts/02-cleaning-names/2.1-four-spellings-of-milk.md)), and that exception is the entire
second half ([4.1](parts/04-the-dt-accessor/4.1-text-that-looks-like-a-date.md)).

One warning about section 2 and section 3: both build a larger frame with a seeded generator to
measure what the mismatch costs and what `.str.extract` costs. Neither is slow; both are there
because the numbers are the argument.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/textdate.py`** — [7.1](parts/07-the-module/7.1-the-textdate-module.md) walks through the
whole module.

- `TEXT_DTYPE`, `TIME_FORMAT` and `MIN_MATCH_RATE` — the day's three policy decisions, as module
  constants.
- `TextDateError(ValueError)` — for a column that arrived in a state the module refuses to work on.
  Import Day 28's `SelectionError`, Day 31's `GroupingError` and Day 32's `JoinError` rather than
  defining a fourth family of exception.
- `normalise_item(frame, column)` — asserts the dtype **before** any `.str` work
  ([1.3](parts/01-the-str-accessor/1.3-the-dtype-under-the-text.md)), then strips and lower-cases,
  and returns a new frame ([2.1](parts/02-cleaning-names/2.1-four-spellings-of-milk.md)).
- `extract_field(series, pattern, name, min_match_rate)` — raises when the share of values the
  pattern matched falls below the floor
  ([3.4](parts/03-pulling-text-apart/3.4-the-pattern-that-matched-nothing.md)).
- `parse_time(frame, column, fmt, tz)` — `to_datetime` with an explicit `format=`, failures
  surfaced rather than coerced, and the resolution asserted
  ([4.2](parts/04-the-dt-accessor/4.2-to-datetime-format-and-errors.md),
  [4.4](parts/04-the-dt-accessor/4.4-the-resolution-pandas-3-picks.md)).
- `by_period(frame, time_column, freq, value, how)` — a resample whose empty-bucket policy the
  caller has to name ([6.3](parts/06-resampling/6.3-the-bucket-that-was-empty.md)).
- `clean_key(frame, column)` — **as given, this lower-cases and nothing else.** No strip, no dtype
  assertion, so `'milk '` survives it and the join still loses the row.
- `TODO(me)`: fix `clean_key`. Make it delegate to `normalise_item`, and state in the docstring what
  is guaranteed about the returned column's values.
- `TODO(me)`: add `time_report(frame, column)` returning the span, the resolution, the timezone and
  the share of values that failed to parse. Say in a comment why the failed share is the number
  worth alerting on rather than the count.
- `TODO(me)`: add a `guard_freq` check to `by_period` that refuses a frequency finer than the data's
  own spacing, and answer in a comment why the input's row count does not predict the output's
  ([6.3](parts/06-resampling/6.3-the-bucket-that-was-empty.md)).

**`tests/test_textdate.py`** — [7.2](parts/07-the-module/7.2-the-test-that-can-go-red.md) walks
through the whole file.

- Three fixtures: a messy text frame, a frame with one timestamp that will not parse, and a frame
  with a week nobody shopped in — plus a test asserting each has the property it exists for.
- The three assertions that carry the day: the unique-item count after normalising, the count of
  values that failed to parse, and the resampled row count **including** the empty week.
- `pytest.raises` with `match=` on a fragment, for `TextDateError`.
- `TODO(me)`: write the tests for your fixed `clean_key`, including one that asserts a trailing
  space cannot survive it.
- `TODO(me)`: add a property test — normalising twice gives the same answer as normalising once —
  and say in a comment what class of bug that catches and what class it cannot.
- `TODO(me)`: break the module a **second** way of your own — not the dtype assertion and not the
  match rate. Watch what goes red, then record the change and the failure count in a
  `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say
  which test should have caught it and why it did not.

**`lab/the_week_that_was_not_there.py`** — the day's most expensive failure, made runnable.

- Build the flat's receipts with one week deliberately empty, using the day's seed.
- Print the weekly total three ways: `groupby` on `.dt.isocalendar().week`, `resample("W").sum()`,
  and `resample("W").mean()`. Show the differing row counts side by side.
- `TODO(me)`: add the same three answers for a month with no shopping at all, and say in a comment
  which of the three a chart should be drawn from and why.
- `TODO(me)`: run it once with `label="left"` and once with `label="right"` and record both. Say
  which of the two a report's "week commencing" column actually means.

---

## §5 The eval that must be able to fail

`tests/test_textdate.py` is RED until `src/setu/textdate.py` exists. Write these two first, because
they are the two that carry the day:

```python
def test_a_trailing_space_cannot_survive_normalising(messy) -> None:
    assert messy["item"].str.endswith(" ").any(), "the fixture must have a trailing space"
    out = normalise_item(messy, "item")
    assert out["item"].nunique() == 4
```

```python
def test_a_pattern_that_matches_nothing_is_refused(messy) -> None:
    with pytest.raises(TextDateError, match=r"match rate"):
        extract_field(messy["item"], r"(?P<shop>\bshop-\d+)", "shop", min_match_rate=0.9)
```

**The assertion on the fixture is the point of the first one.** Without a trailing space in the
fixture, the test passes whether or not `.str.strip()` is being called — the same vacuity Days 29,
31 and 32 each found in their own suites
([Day 32, 6.2](../day-32-joining-and-reshaping/parts/06-the-module/6.2-the-test-that-can-go-red.md)).

**The second test is the one nobody writes.** A regular expression that matches nothing returns a
column of blanks and raises nothing at all, so every shape check, every dtype check and every row
count still passes ([3.4](parts/03-pulling-text-apart/3.4-the-pattern-that-matched-nothing.md)).
Delete this test and that bug ships in silence.

**The mutations to watch.** Three, and they behave differently:

1. Remove the dtype assertion from `normalise_item`. **One test goes red** — the one whose fixture
   has an `object` column — and every other test passes, because every other fixture is already
   `str`.
2. Drop the explicit `format=` in `parse_time`. **A different single test goes red**, and it is the
   day-first one; every ISO-formatted fixture parses identically either way.
3. Remove the empty-bucket policy from `by_period` and let it default. **One test goes red** — the
   row-count one — and no total changes, because summing a missing week and summing a zero week
   give the same number.

And one that **no correctness test can catch**: change `MIN_MATCH_RATE` from `0.99` to `0.1`. Every
test stays green, every function still works, and a pattern that finds a tenth of the rows now
passes silently. The defences are a test asserting the constant's value and a review that treats a
policy change as a policy change.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed.

The largest things the day builds are the seeded frames in
[2.4](parts/02-cleaning-names/2.4-the-mismatch-that-costs-rows.md) and
[3.4](parts/03-pulling-text-apart/3.4-the-pattern-that-matched-nothing.md), each a few hundred
thousand rows — tens of megabytes, and the point of the exercise, because the argument for cleaning
at the boundary is a measurement rather than an opinion. Nothing is written to disk except the
module, the tests and the lab script.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **A column is not a string, so it has no string methods.** The methods live behind `.str`, and
  the error names the column rather than the mistake
  ([1.1](parts/01-the-str-accessor/1.1-the-column-that-has-no-lower.md)).
- **`.str` never changes the column it was called on.** A line that calls `.str.lower()` and assigns
  nothing has done nothing at all
  ([1.1](parts/01-the-str-accessor/1.1-the-column-that-has-no-lower.md)).
- **A blank stays blank through every `.str` call**, so a filter built from `.str.contains` reads
  "unknown" as "no" and rows leave a report without anybody choosing to drop them
  ([1.2](parts/01-the-str-accessor/1.2-the-blank-that-came-back-blank.md)).
- **`dtypes == object` finds nothing in pandas 3**, so the check that used to catch a slow text
  column no longer does ([1.3](parts/01-the-str-accessor/1.3-the-dtype-under-the-text.md)).
- **Lower-casing fixes three of the flat's four spellings and leaves the fourth**, because a
  trailing space is invisible in every printout
  ([2.1](parts/02-cleaning-names/2.1-four-spellings-of-milk.md)).
- **`.str.replace` treats its pattern according to `regex=`**, so a `.` or a `(` means something you
  did not intend the moment that setting changes
  ([2.2](parts/02-cleaning-names/2.2-replace-and-the-regex-default.md)).
- **`.str.contains("milk")` also matches `buttermilk`**, so a filter that looks right over-counts
  ([2.3](parts/02-cleaning-names/2.3-contains-startswith-and-the-mask.md)).
- **An unnormalised key loses rows in a join with no error and no warning**, and the money lost is
  not proportional to the rows lost
  ([2.4](parts/02-cleaning-names/2.4-the-mismatch-that-costs-rows.md)).
- **`.str.split()` without `expand=True` puts a list in every cell**, and a column of lists is
  `object`, so nothing vectorised works on it again
  ([3.1](parts/03-pulling-text-apart/3.1-split-and-the-list-in-a-cell.md)).
- **A split whose piece count varies gives a different number of columns on different files**, so
  the schema is a function of the data ([3.2](parts/03-pulling-text-apart/3.2-expand-and-the-columns-you-get.md)).
- **A pattern that matches nothing returns blanks, not an error**, and every shape check still
  passes ([3.4](parts/03-pulling-text-apart/3.4-the-pattern-that-matched-nothing.md)).
- **Text that looks like a date sorts as text**, and for any format that is not year-first that
  order is wrong ([4.1](parts/04-the-dt-accessor/4.1-text-that-looks-like-a-date.md)).
- **`to_datetime` without `format=` guesses per value**, so one ambiguous row can change how a
  whole column is read ([4.2](parts/04-the-dt-accessor/4.2-to-datetime-format-and-errors.md)).
- **`errors="coerce"` turns every unparseable value into a blank**, which converts a loud failure
  into a quiet one ([4.2](parts/04-the-dt-accessor/4.2-to-datetime-format-and-errors.md)).
- **pandas 3 defaults to microsecond resolution, not nanosecond**, so a round trip through Parquet
  or a `concat` with an older frame can change a column's dtype
  ([4.4](parts/04-the-dt-accessor/4.4-the-resolution-pandas-3-picks.md)).
- **Comparing a naive timestamp with an aware one raises**, and the fix is a decision about which
  one was wrong ([4.5](parts/04-the-dt-accessor/4.5-naive-aware-and-the-hour-that-moved.md)).
- **A difference between two timestamps is a `Timedelta`, not a number**, and `.dt.days` truncates,
  so a gap of forty-seven hours counts as one day
  ([5.2](parts/05-arithmetic-on-time/5.2-timedelta-and-its-units.md)).
- **Adding `Timedelta("30 days")` is not adding a month**, and the two answers differ in every month
  of the year ([5.3](parts/05-arithmetic-on-time/5.3-offsets-and-the-month-that-is-not-thirty-days.md)).
- **`resample` needs a time index or an explicit `on=`**, and the error names the index rather than
  the column ([6.1](parts/06-resampling/6.1-the-index-that-has-to-be-time.md)).
- **The single-letter frequency aliases have changed in pandas 3**, so code that ran last year now
  warns or raises ([6.2](parts/06-resampling/6.2-resample-the-groupby-you-did-not-write.md)).
- **`resample` invents rows for periods with no data and `groupby` does not**, so the two give
  different row counts from the same file
  ([6.3](parts/06-resampling/6.3-the-bucket-that-was-empty.md)).
- **`.sum()` on an empty bucket is `0` and `.mean()` is blank**, and the difference between them is
  the difference between "nobody shopped" and "we do not know"
  ([6.3](parts/06-resampling/6.3-the-bucket-that-was-empty.md)).
- **`label=` and `closed=` decide which edge a bucket is named for and which side owns a boundary
  value**, so switching them shifts every point on a chart
  ([6.4](parts/06-resampling/6.4-label-closed-and-the-edge.md)).
- **`rolling(7)` and `resample("W")` answer different questions** and produce different row counts,
  and a metric definition usually means one of them specifically
  ([6.5](parts/06-resampling/6.5-rolling-is-not-resample.md)).

**The pattern behind the day.** Sections 1 to 3's failures are about **what a value actually is**;
sections 4 to 6's are about **what a bucket actually contains**. Almost none of them raises. They
hand you a column with the right dtype, the right length and no blanks — which is why the module
asserts the dtype before it works, measures the share a pattern matched, refuses to guess a date
format, and makes the caller name what an empty bucket means.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Working with text data** — <https://pandas.pydata.org/docs/user_guide/text.html> — the user
  guide's own treatment of `.str`, including the table of every method and the note on what the
  `str` dtype changed.
- **`Series.str.replace`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html> — read what `regex`
  defaults to in this version rather than remembering what it defaulted to in the last one.
- **Time series and date functionality** —
  <https://pandas.pydata.org/docs/user_guide/timeseries.html> — the guide's own treatment of
  `to_datetime`, offsets, resampling and the frequency alias table.
- **`pandas.to_datetime`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html> — read the defaults for
  `format`, `errors`, `dayfirst` and `utc`, and what the ISO 8601 fast path requires.
- **`DataFrame.resample`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html> — confirm for
  yourself what `label`, `closed` and `origin` default to for a weekly frequency.
- **Regular expression operations** — <https://docs.python.org/3/library/re.html> — the syntax
  every `.str` method with a `pattern` argument actually uses.

---

## §9 Say it in an interview

> A column of text is not a piece of text, so it has none of the string methods. They live behind
> the `.str` accessor, which applies the ordinary Python method to every value and hands back a new
> column — nothing is changed in place. The part worth being precise about is that this is where
> keys get cleaned, and cleaning a key is not cosmetic: `Milk`, `milk`, `MILK` and `milk ` are four
> distinct values, a join on them silently keeps only the rows that matched exactly, and the money
> you lose is not proportional to the rows you lose, because the rows that fail to match are never a
> random sample. So the normalisation goes at the boundary, once, with an assertion on the dtype
> before it runs and a match-rate check after.
>
> The same argument applies to anything I pull out of text with a pattern. A regular expression that
> matches nothing does not raise — it returns a column of nulls with the right name, the right
> length and the right dtype, and every shape check downstream passes. So an extract is always
> followed by an assertion on the share of rows it actually matched, and that share is the thing I
> alert on rather than the count.
>
> Dates are the same problem with a different surface. A column that looks like a date is text until
> somebody converts it, and the conversion has two arguments I always pass: an explicit `format`, so
> that one ambiguous row cannot change how the whole column is read, and `errors` left at raise
> rather than coerce, because coercing turns a loud failure into a column of blanks. In pandas 3 the
> default resolution is microseconds rather than nanoseconds, which matters when frames of different
> resolutions meet in a concat or a Parquet round trip, so the parse asserts the resolution too. And
> a timestamp with no timezone is a timestamp with a missing column: I store UTC and convert at the
> edge, because comparing a naive and an aware timestamp raises, and that exception is the lucky
> version of the bug.
>
> Resampling is group-by on a key that does not exist in the data and has to be manufactured, and
> the thing that surprises people is the row count. `groupby` on a week number gives you the weeks
> that occurred; `resample` gives you every week in the range, including the ones nobody shopped in.
> Neither is wrong, but summing an empty bucket gives zero and averaging it gives null, and a chart
> drawn from the first has a floor where the second has a gap. So the function I write makes the
> caller say which one they meant, and the test asserts the row count rather than only the totals —
> because a missing week and a zero week add up to exactly the same number.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 33` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
