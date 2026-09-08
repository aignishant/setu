---
day: 34
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 34 — Categorical dtype and describe() as a data-quality report"
ids: ["PD-13", "PD-14"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 23
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 34 — Categorical dtype and `describe()` as a data-quality report

**Phase 4 · Pandas 3.0 · Module 4** · `PD-13` categorical dtype ·
`PD-14` descriptive statistics and built-in plotting.

> **Yesterday:** the two columns a join depends on — the text key typed four ways, and the date that
> was text — and the accessors that make each of them into what it claimed to be.
> **Today:** what those columns cost to store, and what they will tell you about themselves if you
> ask. A column holding three words two hundred thousand times can hold them once. And the summary
> table everyone prints and nobody reads is, row by row, a list of findings.
> **Tomorrow:** the phase closes. Where pandas stops, what Polars and DuckDB do instead, one honest
> benchmark, and the gate: a clean, typed, joined dataset with an `audit()` and no chained
> assignment anywhere.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The flat has kept its shopping list for a year.

It started as four lines on the back of an envelope — milk, bread, eggs, rice — with a note next to
each saying which part of the shop it comes from. Milk is dairy. Bread is bakery. Rice is dry goods.
Somebody typed it up, and then kept typing it up, week after week, and now there is a file with a
couple of hundred thousand lines in it.

Somebody opens the file to add up the year's spending, and the laptop takes a noticeable moment. That
is odd, because the numbers are only prices and there are not that many of them.

So they look at the file properly. Four columns and a price. One of them is the part of the shop, and
it contains **three different words**. Only three. Written out, in full, two hundred and forty
thousand times.

Nobody would do that on paper. On paper you write the three words once at the top and put a tick in
a column. The file writes out "dry goods" — nine letters — eighty thousand separate times, because
nothing ever told it not to. That is the first half of the day, and the fix is one word long and has
a trap in it: telling pandas a column is one of a fixed set of labels is also telling it that
anything outside that set is an error, and that the order of the set means something. Both of those
turn out to be useful. Both of them bite.

The second half starts from the same file and asks a different question. Somebody prints the summary
table — the one with count, mean, min, max and the three middle numbers — because that is what you do
with a new file. It scrolls past. Nobody reads it.

But read it. The `count` on the price column is a few hundred short of the row count, which means a
few hundred prices were never written down. The `max` is two hundred and sixty, on a file where
nothing costs more than four, which means somebody typed pence into a pounds column. The `min` on
the quantity is `-1`, which is not a quantity. And the size column has one distinct value on every
row, because a backfill went wrong in June and overwrote it — a column that never changes carries no
information at all, and it will sit in a model six months from now doing nothing while looking like
a feature.

Every one of those is in the table. Nobody read the table.

So the day has one shape running through both halves. **A column knows things about itself, and
neither of the two questions worth asking is expensive.** What does it cost to store? And what does
it say when you look at it? The first has a one-word answer with three traps. The second has an
eight-number answer that nobody reads, and turning it into an `audit()` that returns findings
instead of a table is the whole point — because a finding can fail a test, and a table cannot.

---

## §2 The map

Seven sections. Sections 1 to 4 are `PD-13` — the repeated word, the dtype that fixes it, the order
it accidentally has, and the four ways it quietly reverts. Sections 5 and 6 are `PD-14` — the eight
numbers, and reading them as findings. Section 7 is where both meet the project's code, and where
the phase gate's named artifact gets built.

| Section | What it means |
|---|---|
| **1.x** | **The repeated word** — the same short word stored a quarter of a million times |
| **2.x** | **The `category` dtype** — codes plus categories: what it is, what it saves, what it is not |
| **3.x** | **Order** — when the order of the labels means something, and how to say so |
| **4.x** | **The traps** — the four ways a categorical column quietly becomes text again |
| **5.x** | **`describe`** — the eight numbers, and what changes for text |
| **6.x** | **The quality report** — reading those numbers as findings, not as a formality |
| **7.x** | **The module** — `audit()`, and a test that can actually go red |

### Section 1 — the repeated word

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [The same short word, over and over](parts/01-the-repeated-word/1.1-the-same-short-word-over-and-over.md) | Three distinct words, two hundred thousand copies | `foundation` |
| 1.2 | [What `memory_usage` actually counts](parts/01-the-repeated-word/1.2-what-memory-usage-actually-counts.md) | Why `deep=True` changes the answer by a factor | `working` |

### Section 2 — the `category` dtype

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [Two arrays instead of one](parts/02-the-category-dtype/2.1-two-arrays-instead-of-one.md) | Codes and categories — the whole mechanism | `foundation` |
| 2.2 | [`astype("category")`, and the saving measured](parts/02-the-category-dtype/2.2-astype-category-and-the-saving-measured.md) | The number, and the arithmetic that makes it believable | `working` |
| 2.3 | [The code width, and where the saving stops](parts/02-the-category-dtype/2.3-the-code-width-and-where-the-saving-stops.md) | The point at which a category costs *more* than text | `production` |
| 2.4 | [A category is not a text column](parts/02-the-category-dtype/2.4-a-category-is-not-a-text-column.md) | What still works, what raises, and where `.cat` replaces `.str` | `working` |

### Section 3 — order

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [Nominal and ordinal — two kinds of label](parts/03-order/3.1-nominal-and-ordinal.md) | Why `large, medium, small` is the wrong sort | `foundation` |
| 3.2 | [`CategoricalDtype` — the order written down](parts/03-order/3.2-categoricaldtype-the-order-written-down.md) | Declaring the list, and what falls outside it | `working` |
| 3.3 | [Comparing and sorting an ordered category](parts/03-order/3.3-comparing-and-sorting-an-ordered-category.md) | The comparison that works, and the one that raises | `production` |

### Section 4 — the traps

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [The value that is not a category](parts/04-the-traps/4.1-the-value-that-is-not-a-category.md) | Writing a new label into a closed set | `working` |
| 4.2 | [The category that nobody used](parts/04-the-traps/4.2-the-category-that-nobody-used.md) | The empty group, and when it is the finding | `working` |
| 4.3 | [The operation that gave back text](parts/04-the-traps/4.3-the-operation-that-gave-back-text.md) | Six calls that undo the conversion, measured | `production` |
| 4.4 | [`concat`, `merge`, and the dtype that went back to text](parts/04-the-traps/4.4-concat-and-the-dtype-that-went-back-to-text.md) | Two frames whose category lists disagree | `production` |

### Section 5 — `describe`

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [Eight numbers for a column](parts/05-describe/5.1-eight-numbers-for-a-column.md) | What each one is, in a sentence, including `std`'s divisor | `foundation` |
| 5.2 | [`describe` on text, and what changes](parts/05-describe/5.2-describe-on-text-and-what-changes.md) | `count`, `unique`, `top`, `freq` — and the tie | `working` |
| 5.3 | [`include`, `exclude`, and the column left out](parts/05-describe/5.3-include-exclude-and-the-column-left-out.md) | The default that silently hides nine columns | `working` |

### Section 6 — the quality report

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [`count` is a missing-value report](parts/06-the-quality-report/6.1-count-is-a-missing-value-report.md) | The subtraction nobody does | `working` |
| 6.2 | [`min` and `max` are a range check](parts/06-the-quality-report/6.2-min-and-max-are-a-range-check.md) | The cheapest impossible-value test there is | `working` |
| 6.3 | [The quartiles, and the tail they hide](parts/06-the-quality-report/6.3-the-quartiles-and-the-tail.md) | `mean` far from `50%`, `max` far from `75%` | `production` |
| 6.4 | [The column that never changes](parts/06-the-quality-report/6.4-the-column-that-never-changes.md) | `std == 0`, and the feature that does nothing | `production` |
| 6.5 | [Built-in plotting — the fastest look](parts/06-the-quality-report/6.5-built-in-plotting-the-fastest-look.md) | `.plot()` as a check, not as a chart you ship | `working` |

### Section 7 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 7.1 | [`src/setu/audit.py`](parts/07-the-module/7.1-the-audit-module.md) | The phase gate's named artifact, function by function | `production` |
| 7.2 | [The test that can go red](parts/07-the-module/7.2-the-test-that-can-go-red.md) | Testing a finding count, a dtype and a memory ratio | `production` |

**The running example is the flat's year of shopping** — the same four items, three aisles and three
pack sizes, in a file of 240 000 lines built from one seed. Every part of this day picks it up.

---

## §3 Setup — run this

```bash
mkdir -p days/day-34-categories-and-describe/lab
touch src/setu/audit.py tests/test_audit.py
uv add matplotlib==3.11.1
uv run python -c "import pandas as pd, numpy as np, matplotlib; print(pd.__version__, np.__version__, matplotlib.__version__)"
```

Expected: `3.0.5 2.5.2 3.11.1`. If any of the three prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**One package is installed today**, and only for
[6.5](parts/06-the-quality-report/6.5-built-in-plotting-the-fastest-look.md): `matplotlib`, because
`DataFrame.plot` is `PD-14`'s second half and it has no drawing engine of its own. Days 36 to 41 are
the real treatment; today it is a check you run, not a chart you ship.

Confirm the two facts the whole day rests on — the size of the repetition, and the summary nobody
reads:

```bash
uv run python -c "
import numpy as np
import pandas as pd

rng = np.random.default_rng(34)
ITEMS = ['milk', 'bread', 'eggs', 'rice']
AISLES = {'milk': 'dairy', 'bread': 'bakery', 'eggs': 'dairy', 'rice': 'dry goods'}
item = rng.choice(ITEMS, 240_000)
aisle = pd.Series([AISLES[i] for i in item], dtype='str')

as_text = aisle.memory_usage(deep=True)
as_cat = aisle.astype('category').memory_usage(deep=True)
print('distinct values :', aisle.nunique(), 'in', len(aisle), 'rows')
print('as text  (bytes):', as_text)
print('as category     :', as_cat)
print('ratio           :', round(as_text / as_cat, 1), 'x')

need = pd.Series(rng.integers(1, 4, 240_000))
need.iloc[7] = -1
print()
print(need.describe().to_dict())
"
```

Expected: **three distinct values in 240 000 rows**, a category column many times smaller than the
text one, and a `describe()` whose `min` is `-1` on a column of quantities. Those two blocks are the
two halves of the day. The exact ratio depends on your machine's pointer size, so record **your**
number rather than this page's ([2.2](parts/02-the-category-dtype/2.2-astype-category-and-the-saving-measured.md)).

One warning about sections 2 and 4: both build the 240 000-row frame several times to measure
memory before and after. Neither is slow; both are there because the numbers are the argument.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/audit.py`** — [7.1](parts/07-the-module/7.1-the-audit-module.md) walks through the whole
module. This is the artifact the Phase 4 gate names by name, so Day 35 closes the phase on it.

- `ITEMS`, `AISLES`, `SIZES` — the day's label lists, sorted, written once, at module level.
- `SIZE_DTYPE` — an **ordered** `CategoricalDtype` built from `SIZES`
  ([3.2](parts/03-order/3.2-categoricaldtype-the-order-written-down.md)).
- `MAX_MISSING_SHARE` and `MAX_CATEGORY_RATIO` — the day's two policy numbers.
- `AuditError(ValueError)` — for a frame that fails a check the module refuses to pass. Import the
  earlier days' exceptions rather than inventing a fifth family.
- `categorise(frame, columns, dtypes)` — returns a new frame, asserts the resulting dtype, and
  refuses a column whose ratio of distinct values to rows makes the conversion a loss
  ([2.3](parts/02-the-category-dtype/2.3-the-code-width-and-where-the-saving-stops.md)).
- `audit(frame)` — returns a **frame of findings**, one row per check, with columns `column`,
  `check`, `value` and `passed`. Built from `describe`, `count`, `nunique`, `std` and
  `memory_usage`. It returns; it does not print.
- **As given, `audit` calls `describe()` with its default `include`**, so every text and categorical
  column is silently absent from the report it claims to be
  ([5.3](parts/05-describe/5.3-include-exclude-and-the-column-left-out.md)).
- `TODO(me)`: fix `audit` so that no column can be missing from its own report, and state that
  guarantee in the docstring.
- `TODO(me)`: add `memory_report(frame)` returning the per-column bytes before and after
  categorising. Say in a comment why the ratio is the number worth reporting rather than the total.
- `TODO(me)`: add `constant_columns(frame)`. Say in a comment why `std == 0` and `nunique == 1` are
  not the same test, and which one catches the flat's failed backfill
  ([6.4](parts/06-the-quality-report/6.4-the-column-that-never-changes.md)).

**`tests/test_audit.py`** — [7.2](parts/07-the-module/7.2-the-test-that-can-go-red.md) walks through
the whole file.

- Four fixtures: a clean frame, the corrupted year file, a frame with an unused category, and a
  frame whose two halves have different `categories` — plus a test asserting each has the property
  it exists for.
- The three assertions that carry the day: the finding count, the dtype after `categorise`, and the
  memory ratio.
- `pytest.raises` with `match=` on a fragment, for `AuditError`.
- `TODO(me)`: write the tests for your fixed `audit`, including one asserting that a frame of only
  text columns still produces a non-empty report.
- `TODO(me)`: add a property test — categorising twice gives the same dtype as categorising once —
  and say in a comment what class of bug that catches and what class it cannot.
- `TODO(me)`: break the module a **second** way of your own — not the dtype assertion and not the
  ratio guard. Watch what goes red, then record the change and the failure count in a
  `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say
  which test should have caught it and why it did not.

**`lab/the_column_that_did_nothing.py`** — the day's most expensive failure, made runnable.

- Build the flat's year file with the day's seed, then corrupt it deliberately: a few hundred blank
  prices, one price typed in pence, one negative quantity, and a `size` column overwritten to a
  single value from June onwards.
- Print `describe(include="all")` and, next to it, the findings `audit()` would produce.
- `TODO(me)`: add the memory before and after categorising every text column, and say in a comment
  which single column carries most of the saving and why.
- `TODO(me)`: run it once with the corruption applied before the categorising and once after, and
  record both. Say which order the pipeline should use and what the other order silently drops.

---

## §5 The eval that must be able to fail

`tests/test_audit.py` is RED until `src/setu/audit.py` exists. Write these two first, because they
are the two that carry the day:

```python
def test_a_text_only_frame_still_gets_a_report(text_only) -> None:
    assert text_only.select_dtypes("number").empty, "the fixture must have no numeric column"
    findings = audit(text_only)
    assert not findings.empty
    assert set(findings["column"]) == set(text_only.columns)


def test_a_column_too_distinct_to_categorise_is_refused(nearly_unique) -> None:
    with pytest.raises(AuditError, match=r"ratio"):
        categorise(nearly_unique, ["reference"], {"reference": "category"})
```

**The assertion on the fixture is the point of the first one.** Without a numeric-free fixture, the
test passes whether or not `include="all"` is being passed — the same vacuity Days 29, 31, 32 and 33
each found in their own suites
([Day 33, 7.2](../day-33-text-and-time/parts/07-the-module/7.2-the-test-that-can-go-red.md)).

**The second test is the one nobody writes.** "Always convert text to category" is the lesson people
take away, and it is false past a certain ratio of distinct values to rows — at which point the
conversion costs memory rather than saving it
([2.3](parts/02-the-category-dtype/2.3-the-code-width-and-where-the-saving-stops.md)). Delete this
test and the module happily makes every file bigger.

**The mutations to watch.** Three, and they behave differently:

1. Drop the dtype assertion in `categorise`. **One test goes red** — the ordered-dtype one — and
   every other test passes, because every other fixture would be converted correctly anyway.
2. Use `astype("category")` instead of `SIZE_DTYPE`. **A different single test goes red**, and it is
   the sorting one; nothing about the memory or the finding count changes at all.
3. Remove the ratio guard. **One test goes red** — the refusal — and the memory-ratio test does not
   notice, because its fixture is well within the limit.

And one that **no correctness test can catch**: change `MAX_MISSING_SHARE` from `0.01` to `0.9`.
Every test stays green, every function still works, and a file that is nine-tenths blank now passes
its audit. The defences are a test asserting the constant's value and a review that treats a policy
change as a policy change.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero model calls, zero API keys, zero network at run time.** One package installed:
`matplotlib==3.11.1`, pinned, for
[6.5](parts/06-the-quality-report/6.5-built-in-plotting-the-fastest-look.md) only.

The largest thing the day builds is the 240 000-row frame, rebuilt several times across sections 2
and 4 to measure memory before and after — tens of megabytes, and the point of the exercise, because
the argument for the `category` dtype is a measurement rather than an opinion. Every chart in 6.5 is
written to `lab/` through the `Agg` backend; nothing opens a window.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **`memory_usage()` without `deep=True` counts the pointers, not the text they point at**, so the
  number that matters is the one nobody prints
  ([1.2](parts/01-the-repeated-word/1.2-what-memory-usage-actually-counts.md)).
- **`astype("category")` sorts the categories alphabetically**, whatever order the values appeared
  in ([2.1](parts/02-the-category-dtype/2.1-two-arrays-instead-of-one.md)).
- **The code array widens as the category count grows**, so a column with tens of thousands of
  distinct values can cost more as a category than it did as text
  ([2.3](parts/02-the-category-dtype/2.3-the-code-width-and-where-the-saving-stops.md)).
- **`.str` on a categorical column works and returns text**, which quietly undoes the conversion in
  the middle of a pipeline ([2.4](parts/02-the-category-dtype/2.4-a-category-is-not-a-text-column.md)).
- **Sorting an unordered category sorts the labels alphabetically**, so `large` comes before
  `medium` ([3.1](parts/03-order/3.1-nominal-and-ordinal.md)).
- **A value outside the declared `categories` becomes blank, silently**, so a typo in a label list
  deletes rows' values without deleting the rows
  ([3.2](parts/03-order/3.2-categoricaldtype-the-order-written-down.md)).
- **Comparing an unordered category with `<` raises**, and that error is the lucky version
  ([3.3](parts/03-order/3.3-comparing-and-sorting-an-ordered-category.md)).
- **Assigning a new label into a categorical column raises rather than growing the list**
  ([4.1](parts/04-the-traps/4.1-the-value-that-is-not-a-category.md)).
- **A category nobody used still appears in `value_counts()` with a zero**, and whether that is a
  bug or the finding depends on the question
  ([4.2](parts/04-the-traps/4.2-the-category-that-nobody-used.md)).
- **`.apply`, `.map`, `.fillna` with a non-category and a comparison against a string can each
  return text**, so the memory saving evaporates mid-pipeline
  ([4.3](parts/04-the-traps/4.3-the-operation-that-gave-back-text.md)).
- **`concat` of two frames whose category lists differ gives `object`**, and so does a `merge` on a
  categorical key whose dtypes do not match exactly
  ([4.4](parts/04-the-traps/4.4-concat-and-the-dtype-that-went-back-to-text.md)).
- **`describe()`'s `std` divides by `n - 1`, not `n`**, so it disagrees with NumPy's default
  ([5.1](parts/05-describe/5.1-eight-numbers-for-a-column.md)).
- **`describe()` on a mixed frame silently drops every non-numeric column**, so the report you read
  is not a report on the file ([5.3](parts/05-describe/5.3-include-exclude-and-the-column-left-out.md)).
- **`top` on a tie picks one value and says nothing about the tie**
  ([5.2](parts/05-describe/5.2-describe-on-text-and-what-changes.md)).
- **`count` is the non-blank count, not the row count**, and the difference is the missing-value
  report ([6.1](parts/06-the-quality-report/6.1-count-is-a-missing-value-report.md)).
- **A `max` far outside the plausible range is a unit error, not an outlier**, and treating it as an
  outlier hides it ([6.2](parts/06-the-quality-report/6.2-min-and-max-are-a-range-check.md)).
- **A mean that moved while the median did not is a tail**, and averaging it into a report is how a
  single bad row changes a headline number
  ([6.3](parts/06-the-quality-report/6.3-the-quartiles-and-the-tail.md)).
- **A constant column breaks a model silently rather than loudly**, and `describe()` shows it as
  `std` of zero on every run ([6.4](parts/06-the-quality-report/6.4-the-column-that-never-changes.md)).
- **`DataFrame.plot` opens a window unless the backend says otherwise**, which is why every example
  today sets `Agg` first
  ([6.5](parts/06-the-quality-report/6.5-built-in-plotting-the-fastest-look.md)).

**The pattern behind the day.** Sections 1 to 4's failures are about **what a column costs**;
sections 5 and 6's are about **what a column is telling you**. Almost none of them raises. The
conversions that revert leave a perfectly good column with the wrong dtype, and the findings in
`describe()` are printed in full and simply not read — which is why the module returns findings
rather than a table, asserts the dtype after every conversion, and refuses a conversion that would
cost more than it saves.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Categorical data** — <https://pandas.pydata.org/docs/user_guide/categorical.html> — the user
  guide's own treatment, including the section on operations that return `object` and the note on
  `union_categoricals`.
- **`pandas.CategoricalDtype`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html> — read what `ordered`
  changes and what happens to a value outside `categories`.
- **`DataFrame.describe`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html> — confirm for
  yourself what `include` defaults to and what the datetime columns get.
- **`DataFrame.memory_usage`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html> — read what
  `deep` actually changes, and for which dtypes it changes nothing.
- **Chart visualisation** — <https://pandas.pydata.org/docs/user_guide/visualization.html> — the
  built-in plotting the second half of `PD-14` names, and what it delegates to matplotlib.
- **matplotlib backends** — <https://matplotlib.org/stable/users/explain/figure/backends.html> — why
  `Agg` is what a script wants.

---

## §9 Say it in an interview

> A text column that only ever holds a handful of distinct values is storing the same word over and
> over. The `category` dtype replaces it with two arrays: a small integer code per row, and the list
> of labels those codes point into. On a column with three distinct values and a couple of hundred
> thousand rows that is a large saving, and the way I make the claim believable is to decompose it —
> the codes' `nbytes` plus the categories' own bytes should add up to what `memory_usage(deep=True)`
> reports, and if it does not I have measured the wrong thing.
>
> The part people miss is that it is not free and it is not always a win. The code array widens as
> the number of categories grows, so past a certain ratio of distinct values to rows the categorical
> version costs more than the text it replaced. And the dtype reverts easily: `.str` on it, `.apply`,
> a `fillna` with a value outside the list, a `concat` with a frame whose category list is different
> — each of those hands back `object`, silently, in the middle of a pipeline. So the conversion goes
> at a known boundary and the dtype gets asserted after it, not assumed.
>
> The other thing a category buys is an order, and that one is a correctness feature rather than a
> memory one. Small, medium, large sorts alphabetically as large, medium, small, which is wrong in
> every chart and every group-by. Declaring an ordered `CategoricalDtype` fixes that, and it also
> closes the set: a value outside the declared list becomes null rather than being added, which
> catches a typo in a label at the moment it happens rather than three joins later.
>
> On the statistics side, the thing I actually do is read `describe()` as a list of findings rather
> than as a formality. `count` against the row count is the missing-value report. `min` and `max`
> are the cheapest impossible-value check there is — a maximum of two hundred and sixty on a column
> where nothing costs more than four is a unit error, not an outlier. A mean far from the median is
> a tail, so a headline average is being moved by a handful of rows. And a standard deviation of
> zero is a column that never changes, which will sit in a model doing nothing while looking like a
> feature. The reason I wrap all of that in an `audit()` that returns a frame of findings rather
> than printing a table is simple: a finding can fail a test in CI, and a table can only scroll past.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 34` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
