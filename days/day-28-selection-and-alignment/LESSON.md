---
day: 28
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 28 — loc, iloc, boolean masks, reindexing and alignment"
ids: ["PD-03", "PD-04"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P8 leakage is the enemy", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 24
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 28 — `loc`, `iloc`, boolean masks, reindexing and alignment

**Phase 4 · Pandas 3.0 · Module 4** · `PD-03` indexing and selection · `PD-04` reindexing and
alignment, with the plan's named example: **two series with different indexes added — the NaNs are
the lesson.**

> **Yesterday:** getting a typed frame in, from four different stores, with `dtype=` and
> `parse_dates=` stated at read time rather than repaired afterwards.
> **Today:** getting things back out of it. There are exactly two ways to name a row — by the label
> it carries or by the position it currently sits in — and pandas keeps them apart on purpose.
> Everything else follows from that one distinction: how you filter, how you write, and what happens
> when two frames meet and their labels do not agree.
> **Tomorrow:** why you should almost never walk a frame row by row, measured on a million rows, and
> how to sort and rank instead.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The shopping list is on the fridge. Four lines: milk, bread, eggs, rice.

Somebody at the shop rings up and asks about one of them, and there are two ways they can say which.
They can say "how many eggs", which works wherever the eggs are on the list. Or they can say "what's
the third one", which is quicker and means the same thing right now.

Then somebody adds tea to the top of the list, because that is where the space was.

"How many eggs" still gets you eggs. "What's the third one" now gets you bread. Nobody did anything
wrong; the two ways of pointing were never the same thing, and one of them survives the list changing
while the other does not.

That is the first half of the day, and the second half is what happens when there are **two** lists.

Two people in the flat write lists without telling each other. One has milk, bread, eggs and rice.
The other has milk, eggs and tea. Somebody adds them up, and the answer has *five* lines — more than
either list started with — and three of them are blank.

The blanks are the interesting part. Milk is on both lists, so milk has an answer. Bread is on one
list only, and the honest answer for bread is not "one" and not "zero" — it is that nobody knows
whether the second person needed bread or simply did not think about it. A blank line does not say
which.

So the day has one idea running through it, and it is not really about pandas. **A label is a promise
about what a row is; a position is only a fact about where it happens to be.** Keep the labels and
the computer can tell you when two things do not line up. Throw them away and it will happily add the
milk to the rice and never mention it.

The thing to watch for all day: almost nothing here raises an exception. Yesterday's failures were
mostly errors you could read. Today's are mostly **plausible wrong answers** — an empty frame, a
write that vanished, a total that is two per cent low. The skill being built is knowing which single
number to check after each operation.

---

## §2 The map

Six sections. The first three are `PD-03`, taking things out of one frame. The next two are `PD-04`,
what happens when two frames meet. The last is where both meet the project's code.

| Section | What it means |
|---|---|
| **1.x** | **Label and position** — the two ways to name a row, and where they disagree |
| **2.x** | **Masks** — a comparison makes a column, and that column selects rows |
| **3.x** | **Writing** — putting a selection on the left of an `=`, safely |
| **4.x** | **Alignment** — two labelled things meeting, and the `NaN`s that result |
| **5.x** | **Reindexing** — taking control of the index instead of accepting the union |
| **6.x** | **The module** — every operation paired with the check that makes its failure loud |

### Section 1 — label and position

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [Two ways to say "that row"](parts/01-label-and-position/1.1-two-ways-to-say-that-row.md) | Why are there two accessors? | `foundation` |
| 1.2 | [`loc`, by label](parts/01-label-and-position/1.2-loc-by-label.md) | What comes back, and what shape is it? | `foundation` |
| 1.3 | [`iloc`, by position](parts/01-label-and-position/1.3-iloc-by-position.md) | When is position the right question? | `working` |
| 1.4 | [Rows and columns at once](parts/01-label-and-position/1.4-rows-and-columns-at-once.md) | What the comma does | `working` |
| 1.5 | [The slice that includes its end](parts/01-label-and-position/1.5-the-slice-that-includes-its-end.md) | Why `loc` disagrees with all of Python | `working` |

### Section 2 — masks

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [A comparison makes a column](parts/02-masks/2.1-a-comparison-makes-a-column.md) | What does `price > 1` actually return? | `foundation` |
| 2.2 | [Selecting with a mask](parts/02-masks/2.2-selecting-with-a-mask.md) | How does the mask find its rows? | `working` |
| 2.3 | [`&`, `\|`, `~` and the brackets](parts/02-masks/2.3-and-or-not-and-the-brackets.md) | Why not `and`, and why the brackets? | `working` |
| 2.4 | [`isin`, `between`, and the readable ones](parts/02-masks/2.4-isin-between-and-the-readable-ones.md) | How do you write a long condition? | `working` |
| 2.5 | [The mask that matched nothing](parts/02-masks/2.5-the-mask-that-matched-nothing.md) | What does an empty result mean? | `production` |

### Section 3 — writing

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [Assigning through `loc`](parts/03-writing/3.1-assigning-through-loc.md) | Why does one spelling of a write vanish? | `working` |
| 3.2 | [The new column that was a mask](parts/03-writing/3.2-the-new-column-that-was-a-mask.md) | When is a flag better than a filter? | `working` |
| 3.3 | [`where`, `mask`, and the write that was not](parts/03-writing/3.3-where-mask-and-the-write-that-was-not.md) | How do you blank values without dropping rows? | `production` |

### Section 4 — alignment

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [Two lists, different items](parts/04-alignment/4.1-two-lists-different-items.md) | The plan's named example | `foundation` |
| 4.2 | [Alignment is automatic](parts/04-alignment/4.2-alignment-is-automatic.md) | What happens when the labels merely reorder? | `working` |
| 4.3 | [The `NaN` that changed the dtype](parts/04-alignment/4.3-the-nan-that-changed-the-dtype.md) | Why did my integers become floats? | `working` |
| 4.4 | [The index is the join key](parts/04-alignment/4.4-the-index-is-the-join-key.md) | What is alignment, really? | `production` |
| 4.5 | [Turning alignment off](parts/04-alignment/4.5-turning-alignment-off.md) | When is dropping the labels right? | `production` |

### Section 5 — reindexing

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [`reindex` — say the index you want](parts/05-reindexing/5.1-reindex-say-the-index-you-want.md) | How do you choose the shape? | `working` |
| 5.2 | [`fill_value`, `method`, and the gap](parts/05-reindexing/5.2-fill-value-method-and-the-gap.md) | What goes in the blanks? | `working` |
| 5.3 | [Duplicate labels](parts/05-reindexing/5.3-duplicate-labels.md) | What breaks when a label repeats? | `production` |
| 5.4 | [`align`, and the boundary](parts/05-reindexing/5.4-align-and-the-boundary.md) | How do you pick the join type? | `production` |

### Section 6 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [`src/setu/select.py`](parts/06-the-module/6.1-the-select-module.md) | Where does each check belong? | `production` |
| 6.2 | [The test that can go red](parts/06-the-module/6.2-the-test-that-can-go-red.md) | How do you test what a function does *not* do? | `production` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-28-selection-and-alignment/lab
touch src/setu/select.py tests/test_select.py
uv run python -c "import pandas as pd; print(pd.__version__)"
```

Expected: `3.0.5`. If it prints something else, stop and log it in `docs/CHANGELOG_PLAN_DS.md` before
continuing (Principle 4, Principle 14).

**Nothing is installed today.** Everything comes from Day 26's `uv add pandas==3.0.5 pyarrow==25.0.1`.

Build the day's frame, which is the same four rows Days 26 and 27 used, with one change that makes
the whole day visible:

```bash
uv run python -c "
import pandas as pd
shop = pd.DataFrame(
    {
        'item': pd.Series(['milk', 'bread', 'eggs', 'rice'], dtype='str'),
        'need': [2, 1, 6, 1],
        'price': [1.15, 1.40, 0.32, 2.05],
        'aisle': pd.Series(['07', '03', '07', '11'], dtype='str'),
    }
).set_index('item')
print(shop)
print()
print('index name :', shop.index.name)
print('index      :', shop.index.tolist())
print('is unique? :', shop.index.is_unique)
"
```

**The change is `set_index('item')`.** Until now the frame's rows were numbered `0, 1, 2, 3`, where
every label happens to equal its own position — and on such a frame `loc` and `iloc` agree about
everything, which hides the entire subject
([1.1](parts/01-label-and-position/1.1-two-ways-to-say-that-row.md)). A frame with a meaningful index
is where today's ideas become visible.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/select.py`** — [6.1](parts/06-the-module/6.1-the-select-module.md) walks through the whole
module.

- `SHELF` — the reference index, as a tuple, and the single source of truth for what a shopping list's
  rows are ([5.1](parts/05-reindexing/5.1-reindex-say-the-index-you-want.md)).
- `SelectionError(ValueError)` — for a selection that did not do what it promised. Import Day 26's
  `SchemaError` rather than redefining it.
- `assert_unique_index(frame)` — the precondition everything else assumes, with the offending labels
  named ([5.3](parts/05-reindexing/5.3-duplicate-labels.md)).
- `rows_for(frame, items)` — `loc` with a list, every unknown label collected and reported at once.
- `dear_items(frame, threshold)` — a mask. **No emptiness check**, and the docstring says why
  ([2.5](parts/02-masks/2.5-the-mask-that-matched-nothing.md)).
- `flag(frame, threshold)` — `assign` with lambdas, returning a new frame
  ([3.2](parts/03-writing/3.2-the-new-column-that-was-a-mask.md)).
- `restock(frame, minimum)` — a `.loc` assignment, **with the write confirmed to have landed**
  ([3.1](parts/03-writing/3.1-assigning-through-loc.md)).
- `onto_shelf(counts)` — `reindex` onto `SHELF`, refusing to drop an item the shelf does not know.
- `combine(mine, theirs, join)` — `align` with the join type stated, the dtype converted back to
  `int64` ([5.4](parts/05-reindexing/5.4-align-and-the-boundary.md)).
- `TODO(me)`: add `cheapest(frame, n)` returning the `n` cheapest rows. It must go through
  `assert_unique_index`, must not use a single square bracket to write anything, and must decide what
  it does when `n` is larger than the frame. Write the decision in the docstring. Sorting properly is
  tomorrow's subject; solve it with what section 1 and 2 gave you.
- `TODO(me)`: `dear_items` currently has no check. Decide whether it should **log** when it returns
  nothing — not raise, log — and write one sentence of justification as a comment either way. There is
  a defensible answer in both directions.
- `TODO(me)`: `combine` checks both indexes for duplicates but `dear_items` and `flag` do not. Decide
  whether to add a single entry point that checks once, or to leave each function responsible, and
  write the reason down. [6.1](parts/06-the-module/6.1-the-select-module.md)'s production section has
  an opinion; disagree with it if you can say why.

**`tests/test_select.py`** — [6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md) walks through
the whole file.

- Three kinds of assertion: what each function returns, **what it does not do** (the caller's frame is
  unchanged), and what it refuses (`pytest.raises` with `match=`).
- One test asserting that `dear_items` may return **nothing**, and that the empty frame keeps its
  columns and dtypes.
- One test asserting `combine`'s result is `int64`, because that proves no blank survived the
  alignment ([4.3](parts/04-alignment/4.3-the-nan-that-changed-the-dtype.md)).
- `TODO(me)`: write the tests for your `cheapest` — at least one asserting the caller's frame is
  untouched, and at least one using `pd.testing.assert_frame_equal` on the result.
- `TODO(me)`: add the **empty-input** sweep. Run every public function against a zero-row frame and
  assert what happens. Some should return empty; decide whether any should raise, and record the
  decision. This is the case that never occurs in development.
- `TODO(me)`: break the module a **second** way of your own — not the `.loc` mutation in 6.2. Watch
  what goes red, then record the change and the failure count in a `# Seen to fail:` comment at the
  bottom of the file. If nothing goes red, you have found a gap in the suite.

**`lab/two_lists.py`** — the plan's named example, made visible. A script, because its job is to be
run and looked at.

- Build the two shopping lists from [4.1](parts/04-alignment/4.1-two-lists-different-items.md), add
  them, and print the result **with its length and dtype**.
- Print the same addition four more ways: with `fill_value=0`, with both sides reindexed onto `SHELF`,
  with `align(join="inner")`, and with `.to_numpy()` on both sides.
- `TODO(me)`: add a sixth line that reverses one Series' index order **without changing its values**,
  and print the labelled addition next to the `to_numpy()` one. The two answers differ and neither
  raises ([4.2](parts/04-alignment/4.2-alignment-is-automatic.md)). Write a comment at the top saying
  which is correct and how you would have noticed if you had only had the second.

---

## §5 The eval that must be able to fail

`tests/test_select.py` is RED until `src/setu/select.py` exists. Write these two first, because they
catch the two bugs this day exists to prevent:

```python
def test_restock_writes_through_loc_and_the_write_lands(shop: pd.DataFrame) -> None:
    out = sel.restock(shop, 3)
    assert out["need"].tolist() == [3, 3, 6, 3]
    assert shop["need"].tolist() == [2, 1, 6, 1]


def test_combine_result_is_int64_not_float64() -> None:
    """Alignment promotes to float64; the module converts back, which proves no blank survived."""
    mine = pd.Series([2, 1], index=["milk", "bread"], name="need")
    theirs = pd.Series([1, 3], index=["milk", "tea"], name="need")
    assert (sel.combine(mine, theirs).dtypes == "int64").all()
```

The first has **two** assertions and the second one matters more: a chained-assignment version of
`restock` returns a frame that passes the first line and fails the second. The second test asserts a
**dtype** in order to prove something about *values* — that `fill_value=0` really removed every blank
([4.3](parts/04-alignment/4.3-the-nan-that-changed-the-dtype.md)).

**The mutation to watch.** In `src/setu/select.py`, change `out.loc[below, "need"] = minimum` to
`out[below]["need"] = minimum` and run the suite. One test goes red — and read *what* stopped it:
the module's own `SelectionError: restock did not take effect`, raised inside the function. pandas'
`ChainedAssignmentError` appears too, as a **warning**, which on its own would have let the bug ship.
[6.2](parts/06-the-module/6.2-the-test-that-can-go-red.md) has the full transcript.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)). The build
brief asks for a second mutation of your own, and that one matters more than the given one.

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, and nothing installed.

Everything today runs on the four-row shopping list and two short Series, typed into the file. There
is no benchmark data to generate and nothing to download — today is the cheapest day of the phase.
The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **Using `iloc` when you mean "that row".** A position changes meaning whenever the data changes, and
  it never raises ([1.1](parts/01-label-and-position/1.1-two-ways-to-say-that-row.md)).
- **`loc["a":"b"]` includes `b`.** It is the one slice in Python that does
  ([1.5](parts/01-label-and-position/1.5-the-slice-that-includes-its-end.md)).
- **A backwards `loc` slice returns an empty frame**, with no error, when the index is unsorted
  ([1.5](parts/01-label-and-position/1.5-the-slice-that-includes-its-end.md)).
- **`df.loc["x"]["col"]`** builds a whole `object` row and throws it away — and on the left of an `=`
  it silently does nothing ([1.4](parts/01-label-and-position/1.4-rows-and-columns-at-once.md)).
- **`and` between two masks raises**, and so does a correctly-written `&` with the brackets left out.
  Same message, two causes ([2.3](parts/02-masks/2.3-and-or-not-and-the-brackets.md)).
- **`&` between a numeric column and a number is legal arithmetic**, so a missing bracket can return a
  confident wrong answer with no error at all
  ([2.3](parts/02-masks/2.3-and-or-not-and-the-brackets.md)).
- **A comparison against a missing value is always `False`**, so a mask and its opposite do not add up
  to the whole frame ([2.1](parts/02-masks/2.1-a-comparison-makes-a-column.md)).
- **`isin` with the wrong type matches nothing**, silently — and can never tell you that a value you
  asked for was absent ([2.4](parts/02-masks/2.4-isin-between-and-the-readable-ones.md)).
- **`sum()` of an empty column is `0.0` and `mean()` is `nan`.** A zero total is indistinguishable
  from a real one ([2.5](parts/02-masks/2.5-the-mask-that-matched-nothing.md)).
- **Filtering then writing changes the copy, not the original — and does not warn**, because the
  filtered frame has a name ([3.1](parts/03-writing/3.1-assigning-through-loc.md)).
- **`where` and `mask` return; they do not modify.** A bare call is a line that does nothing
  ([3.3](parts/03-writing/3.3-where-mask-and-the-write-that-was-not.md)).
- **Adding two Series can give a result longer than both**, and one missing label turns every integer
  in the column into a float ([4.1](parts/04-alignment/4.1-two-lists-different-items.md),
  [4.3](parts/04-alignment/4.3-the-nan-that-changed-the-dtype.md)).
- **Same labels in a different order still align** — which is right, and means `to_numpy()` on both
  sides gives a different, silent answer ([4.2](parts/04-alignment/4.2-alignment-is-automatic.md)).
- **`a > b` raises where `a + b` aligns.** The comparison operators refuse; the method forms do not
  ([4.2](parts/04-alignment/4.2-alignment-is-automatic.md)).
- **`reindex` drops labels you did not ask for**, silently, so a stale reference list is a filter
  ([5.1](parts/05-reindexing/5.1-reindex-say-the-index-you-want.md)).
- **A duplicated index multiplies an alignment** — including an `inner` one — rather than raising
  ([5.3](parts/05-reindexing/5.3-duplicate-labels.md),
  [5.4](parts/05-reindexing/5.4-align-and-the-boundary.md)).

**The pattern behind almost all of these:** yesterday's failures were exceptions you could read.
Today's are **plausible wrong answers**. After every operation on this day there is exactly one number
worth checking — usually the row count — and checking it is the whole skill.

---

## §8 Verify before you code

Fetched on the day of writing. Read the argument lists rather than trusting any lesson, this one
included.

- **Indexing and selecting data** —
  <https://pandas.pydata.org/docs/user_guide/indexing.html> — the user guide for section 1 and 2.
  Read its "different choices for indexing" table and its warning about chained assignment.
- **`DataFrame.loc`** — <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html> —
  read the list of allowed inputs, which is longer than section 1 covers, and the warning under the
  slice entry: *"Note that contrary to usual python slices, both the start and the stop are
  included"*. That is
  [1.5](parts/01-label-and-position/1.5-the-slice-that-includes-its-end.md) stated by the
  documentation itself.
- **`DataFrame.reindex`** —
  <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html> — check `fill_value`,
  `method` and the note that `method` requires a monotonic index.
- **`DataFrame.align`** — <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html> —
  the four `join` values, and confirm for yourself that it returns a **tuple**.
- **Copy-on-Write** — <https://pandas.pydata.org/docs/user_guide/copy_on_write.html> — the page
  pandas' own `ChainedAssignmentError` links to. Section 3 is the practical half of it.

---

## §9 Say it in an interview

> A pandas row has two handles: the label it carries, and the position it currently sits in. `loc`
> takes labels and `iloc` takes positions, and they are separate because a label can itself be a
> number — so `df[7]` would be genuinely ambiguous. I use `loc` for almost everything, because a
> position is a fact about the frame's current arrangement rather than about the row, so positional
> code silently changes meaning when the data changes upstream.
>
> The thing that follows from that is index alignment. Any operation between two labelled objects
> matches by label first, so the result's index is the union of the two and non-overlapping labels
> become `NaN`. That has three consequences people get caught by: the result can be **longer** than
> either input; the dtype gets promoted from `int64` to `float64`, because `NaN` is a float and a
> NumPy integer column has no missing marker; and it happens even when the lengths match and the
> labels are merely in a different order — which is the dangerous case, because there is no `NaN` to
> warn you. Stripping the labels with `to_numpy()` to "fix" that is deleting the evidence, not
> fixing the join.
>
> So in practice I treat the index as a join key. I check `is_unique` at the boundary, normalise the
> key once at load, and use `align` with an explicit `join=` rather than letting `+` pick the outer
> default. And because almost every failure here is a plausible wrong answer rather than an
> exception — an empty filter, a write that landed on a copy, a join that grew — I assert the row
> count after each step, and I check that a write actually landed rather than trusting that it did.

---

## §10 Done when

Every box in [CHECKLIST.md](CHECKLIST.md) is ticked, `./m depth 28` passes, and `./m check` is green.

Not when a number of sittings have passed. A part is finished when you can answer its *Check
yourself* question out loud without scrolling up, and the day is finished when you can say — without
looking — which of today's operations fail loudly and which fail quietly, and what single number you
check after each of the quiet ones.
