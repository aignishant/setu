---
day: 27
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 27 — Reading and writing: CSV, JSON, Parquet, SQL — typed at read time"
ids: ["PD-02"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 22
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 27 — Reading and writing: CSV, JSON, Parquet, SQL

**Phase 4 · Pandas 3.0 · Module 4** · `PD-02` the four stores a dataset arrives in, and the plan's
named example: **`dtype=` and `parse_dates=` at read time beat five `astype` calls later.**

> **Yesterday:** what a frame *is* — Series, DataFrame, the `str` dtype and Copy-on-Write — with the
> shopping list typed by hand in Python, where the types were never in doubt.
> **Today:** the same shopping list, arriving from outside. A CSV, a JSON file, a Parquet file and a
> database table, and the question every one of them forces: who decides what each column's type is?
> The answer ranges from "nobody, so pandas guesses" to "the table, before a single row went in", and
> the whole day is spent measuring what that difference costs.
> **Tomorrow:** having got the frame in and typed, the two ways of picking things out of it — `loc`
> and `iloc`, boolean masks, and the alignment that puts `NaN` where two indexes disagree.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The shopping list has been typed into the shared laptop, and now it has to get from there to
everywhere else.

That turns out to mean four different things, because four different people each saved it the way
they knew how. One saved it as plain text with commas between the values, which opens in anything.
One exported it from an app, so it arrived as nested brackets with the aisle and the shelf tucked
inside each item. One had heard that a particular format is smaller and faster and used that. And the
list on the phone was never a file at all; it lives inside the app, in a store that was told what
each column holds before anybody typed anything into it.

Four copies of one shopping list. Open all four and you get four slightly different tables.

The differences are small and they all come from the same place. The shop's aisle signs are two
digits — aisle `07` — and only some of these four copies remember that the leading zero is part of
the label rather than a number that happens to start with a zero. The date somebody bought the milk
is a date in some of them and a piece of text in others. The blank where nobody has bought the eggs
yet means "not yet" to a person and something else to each of the four.

Nobody made a mistake. The copies differ because **most of these formats have nowhere to write down
what a column is**, so whoever opens the file has to decide, and different openers decide
differently.

Here is the idea the whole day turns on. There is a moment when the file becomes a table, and at that
moment somebody chooses the type of every column. If you do not make that choice, something else
makes it for you — and then you spend the afternoon converting columns back, which never fully works,
because by then the leading zero is gone and no conversion can bring it back.

So: say what you mean at the door. It is one argument, at the one place where it still helps.

---

## §2 The map

Five sections, and they are in order of **how much each store knows about itself** — from a format
that records nothing to one that refuses data that does not fit. Read them in order; the comparison
is the lesson, and each section is an answer to the one before it.

| Section | What it means |
|---|---|
| **1.x** | **The CSV** — the format that has no types in it, and the seven arguments that make up for that |
| **2.x** | **JSON** — the format with a shape but no schema, and how a tree becomes a rectangle |
| **3.x** | **Parquet** — the format that writes the types into the file, measured against the CSV |
| **4.x** | **SQL** — the store that declares its types *first* and can refuse a bad row |
| **5.x** | **The module** — one loader behind all four, the file too big for memory, and the test |

### Section 1 — the CSV

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [A CSV has no types in it](parts/01-the-csv/1.1-a-csv-has-no-types-in-it.md) | Why does anything need to decide? | `foundation` |
| 1.2 | [`read_csv` and what it guessed](parts/01-the-csv/1.2-read-csv-and-what-it-guessed.md) | What does pandas do with a file that says nothing? | `foundation` |
| 1.3 | [When the guess is wrong — the aisle that lost its zero](parts/01-the-csv/1.3-when-the-guess-is-wrong.md) | What does a wrong guess actually destroy? | `working` |
| 1.4 | [`dtype=` at read time beats five `astype` calls later](parts/01-the-csv/1.4-dtype-at-read-time.md) | The plan's named example | `working` |
| 1.5 | [`parse_dates` and the date that stayed text](parts/01-the-csv/1.5-parse-dates-and-the-date-that-stayed-text.md) | Why do dates need their own argument? | `working` |
| 1.6 | [`na_values` and the blank](parts/01-the-csv/1.6-na-values-and-the-blank.md) | What counts as missing, and who decided? | `working` |
| 1.7 | [`to_csv`, and what it throws away](parts/01-the-csv/1.7-to-csv-and-what-it-throws-away.md) | What does writing one cost you? | `production` |

### Section 2 — JSON

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [Nested by nature — why JSON is not a table](parts/02-json/2.1-nested-by-nature.md) | Why is a tree not a rectangle? | `foundation` |
| 2.2 | [`json_normalize` — flattening the tree](parts/02-json/2.2-json-normalize.md) | How does a nested record become columns? | `working` |
| 2.3 | [`orient` — six ways to write the same frame](parts/02-json/2.3-orient-six-ways-to-write-a-frame.md) | Which one, and why does it matter? | `working` |
| 2.4 | [JSON Lines — one record per line](parts/02-json/2.4-json-lines.md) | Why does the format change at scale? | `production` |

### Section 3 — Parquet

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [Columns on disk, with types](parts/03-parquet/3.1-columns-on-disk-with-types.md) | What is stored differently? | `foundation` |
| 3.2 | [The round trip that keeps dtypes](parts/03-parquet/3.2-the-round-trip-that-keeps-dtypes.md) | What comes back unchanged? | `working` |
| 3.3 | [The size and the speed, measured](parts/03-parquet/3.3-the-size-and-the-speed-measured.md) | How much smaller and faster, really? | `working` |
| 3.4 | [Column pruning — three columns out of forty](parts/03-parquet/3.4-column-pruning.md) | Why can Parquet read part of a file when a CSV cannot? | `production` |

### Section 4 — SQL

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [A table that knows its own types](parts/04-sql/4.1-a-table-that-knows-its-types.md) | What can a table do that no file can? | `foundation` |
| 4.2 | [`read_sql` and the connection](parts/04-sql/4.2-read-sql-and-the-connection.md) | Why do the dtypes arrive correct — and the date not? | `working` |
| 4.3 | [`params=`, not f-strings](parts/04-sql/4.3-params-not-f-strings.md) | Why does the value never go in the query string? | `working` |
| 4.4 | [`to_sql`, and what SQLite invents](parts/04-sql/4.4-to-sql-and-what-sqlite-invents.md) | What does a write decide on your behalf? | `production` |

### Section 5 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [`src/setu/loaders.py` — one frame, four stores](parts/05-the-module/5.1-the-loaders-module.md) | Where does the knowledge live? | `production` |
| 5.2 | [The file that does not fit](parts/05-the-module/5.2-the-file-that-does-not-fit.md) | How do you add up a file bigger than memory? | `production` |
| 5.3 | [`tests/test_loaders.py` — the round trip that must survive](parts/05-the-module/5.3-the-round-trip-test.md) | How do you stop the fix being tidied away? | `production` |

---

## §3 Setup — run this

```bash
mkdir -p days/day-27-reading-and-writing/lab
touch src/setu/loaders.py tests/test_loaders.py
uv run python -c "import pandas, pyarrow, sqlite3; print(pandas.__version__, pyarrow.__version__, sqlite3.sqlite_version)"
```

Expected: `3.0.5 25.0.1` and a SQLite version of `3.37.0` or higher. If pandas or pyarrow prints
something else, stop and log it in `docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4,
Principle 14).

**Nothing is installed today.** `pandas==3.0.5` and `pyarrow==25.0.1` arrived on Day 26, and `sqlite3`
is in the Python standard library — there is no database server, no port and no password, because a
SQLite database is one ordinary file ([4.1](parts/04-sql/4.1-a-table-that-knows-its-types.md)). That
is what lets this day teach SQL under Principle 5's zero budget.

The SQLite version matters for one thing only: `STRICT` tables arrived in 3.37.0, and
[4.4](parts/04-sql/4.4-to-sql-and-what-sqlite-invents.md) uses them.

Build the day's four copies of the shopping list before you start:

```bash
uv run python -c "
from pathlib import Path
import pandas as pd
Path('data').mkdir(exist_ok=True)
Path('data/shopping.csv').write_text(
    'item,need,price,aisle,bought\n'
    'milk,2,1.15,07,2026-08-30\n'
    'bread,1,1.40,03,2026-08-30\n'
    'eggs,6,0.32,07,\n'
    'rice,1,2.05,11,2026-08-24\n',
    encoding='utf-8',
)
print(Path('data/shopping.csv').read_text(encoding='utf-8'))
"
```

Four lines and a header. **Every part of this day uses these same four rows**, so that no part asks
you to learn a second example in order to follow the first. The half-million-row version is built in
[3.3](parts/03-parquet/3.3-the-size-and-the-speed-measured.md), where it is needed.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/loaders.py`** — [5.1](parts/05-the-module/5.1-the-loaders-module.md) walks through the
whole module, and [5.2](parts/05-the-module/5.2-the-file-that-does-not-fit.md) adds its two streaming
functions.

- `SCHEMA`, `DATES`, `COLUMNS` — the day's arguments turned into constants, with `COLUMNS` **derived**
  from the other two rather than typed out.
- `LoadError(ValueError)` — the module's exception. Reuse Day 26's `SchemaError` rather than
  redefining it.
- `load_csv`, `load_parquet`, `load_sql` — one reader per store, all returning the same frame. Notice
  how many arguments each one needs; that count is the day's whole argument.
- `load(path)` — dispatch on the suffix, with an error message that lists the formats it does know.
- `iter_csv`, `total_in_chunks` — the streaming pair from
  [5.2](parts/05-the-module/5.2-the-file-that-does-not-fit.md).
- `to_shopping_list(frame)` — narrow the five loaded columns to the three Day 26's schema promises,
  then hand it to Day 26's `assert_schema`.
- `TODO(me)`: write `load_json`. Section 2 gives you `json_normalize` and the `orient` choice; decide
  for yourself which `orient` the module should *write*, and put one sentence of justification in the
  docstring. There is a defensible answer in more than one direction and the sentence is the
  deliverable.
- `TODO(me)`: `load_sql` currently takes an optional `aisle`. Add an optional `since` date as well,
  as a **second bound parameter**, and make sure the query still has exactly one `read_sql` call in
  it. If you find yourself building the `WHERE` clause with an f-string, re-read
  [4.3](parts/04-sql/4.3-params-not-f-strings.md).
- `TODO(me)`: decide whether `load()` should accept an explicit `format=` override rather than always
  trusting the suffix. Write the decision as a comment either way — a `.txt` file containing CSV is a
  real thing that arrives, and so is a `.csv` file containing tab-separated values.

**`tests/test_loaders.py`** — [5.3](parts/05-the-module/5.3-the-round-trip-test.md) walks through the
whole file.

- One test per promise: the declared dtypes, the aisle's leading zero, the lossless Parquet round
  trip, the **lossy** CSV round trip asserted with `pytest.raises`, the SQL types, the dispatcher's
  refusal, and the chunked total compared with `pytest.approx`.
- `TODO(me)`: write the round-trip test for your `load_json`. Decide first whether you expect it to be
  lossless, then write the test that proves you were right — and if you were wrong, keep the test and
  change the claim rather than the other way round.
- `TODO(me)`: add a test for the **empty frame**. Write a CSV with a header and no rows, load it, and
  assert what the dtypes are. This is the case that breaks first in real ingestion and the one the
  given suite does not cover.
- `TODO(me)`: break the module in a **second** way of your own — not the `dtype=SCHEMA` deletion in
  5.3. Watch what goes red, then record the change and the failure count in a `# Seen to fail:`
  comment at the bottom of the file. If nothing goes red, you have found a gap in the suite, which is
  worth more than the test you were about to write.

**`lab/four_ways.py`** — the plan's named example, made visible. A script rather than a module,
because its job is to be run and looked at.

- Write the four-line list into all four stores, then read each one back with **no arguments at all**,
  and print the dtypes of each side by side.
- Then read all four again with the arguments the module uses, and print the same table.
- `TODO(me)`: add a third row to that table — the same four stores read naively, then repaired
  afterwards with `astype`. Print the `aisle` column's *values*, not only its dtype. The plan's
  example claims that reading correctly beats repairing afterwards; this script is where you find out
  whether that is a preference or a fact.

---

## §5 The eval that must be able to fail

`tests/test_loaders.py` is RED until `src/setu/loaders.py` exists, which is the starting condition
rather than a problem. Write these two first, because they are the two that catch this day's bugs:

```python
def test_the_aisle_keeps_its_leading_zero(csv_path: Path) -> None:
    """The one column inference destroys, and the reason dtype= is not optional."""
    assert ld.load_csv(csv_path)["aisle"].tolist() == ["07", "03", "07", "11"]


def test_csv_round_trip_is_not_lossless(csv_path: Path, tmp_path: Path) -> None:
    """A CSV written and read back without dtype= loses the aisle. This is the day's point."""
    original = ld.load_csv(csv_path)
    target = tmp_path / "again.csv"
    original.to_csv(target, index=False)
    naive = pd.read_csv(target)
    assert str(naive["aisle"].dtype) == "int64"
    with pytest.raises(AssertionError, match="aisle"):
        pd.testing.assert_frame_equal(original, naive)
```

The first asserts the **values**, not the dtype, because a column cast back to text after the zero is
gone has the right dtype and the wrong data. The second asserts that a comparison **fails**, which
looks like a mistake until you realise it is the only way to stop a known limitation being quietly
forgotten.

**The mutation to watch.** Delete `dtype=SCHEMA` from `load_csv` — one argument, the kind of thing
somebody removes while tidying — and run the suite. **Four tests go red, and the fourth is about the
database**, which was never touched. [5.3](parts/05-the-module/5.3-the-round-trip-test.md) has the
transcript and explains why a broken CSV loader reaches a store two steps away.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)). The build
brief asks for a second mutation of your own, and that one matters more than the given one.

---

## §6 Request budget

**Zero.** No model calls, no API keys, no cost, and no network at run time.

Every store used today is local: files under `data/`, and a SQLite database that is itself a file.
Nothing is installed — pandas and pyarrow arrived on Day 26 and `sqlite3` ships with Python — so
today does not even download a wheel.

The largest thing the day makes is the half-million-row benchmark file in
[3.3](parts/03-parquet/3.3-the-size-and-the-speed-measured.md), about 13.5 MB as CSV, plus the
forty-column file in [3.4](parts/03-parquet/3.4-column-pruning.md), about 57 MB. Both are generated
from a seed, both live under `data/`, and neither is committed. Delete them when the day is done.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **Reading a CSV with no arguments and trusting the result.** It works, it never raises, and it is
  wrong about the aisle every single time ([1.3](parts/01-the-csv/1.3-when-the-guess-is-wrong.md)).
- **Repairing with `astype` after the read.** `astype(str)` on a column that has already become
  `int64` gives you `"7"`, not `"07"`. **The zero is gone at the read**, and no later call brings it
  back ([1.4](parts/01-the-csv/1.4-dtype-at-read-time.md)).
- **Putting a date column in `dtype=`.** Dates are parsed, not converted, and they need
  `parse_dates=` instead. Naming a column in both is a conflict
  ([1.5](parts/01-the-csv/1.5-parse-dates-and-the-date-that-stayed-text.md)).
- **A comma inside a value.** Depending on which row it is in, the file either raises `ParserError`
  or silently shifts every column one place to the left
  ([1.1](parts/01-the-csv/1.1-a-csv-has-no-types-in-it.md)).
- **Assuming `usecols=` makes a CSV read fast.** It roughly halves it, and no more, because the
  bytes still have to be read and the commas still have to be counted
  ([3.4](parts/03-parquet/3.4-column-pruning.md)).
- **`with con:` on a `sqlite3` connection.** It commits; it does **not** close. That is not what the
  same syntax does for a file ([4.2](parts/04-sql/4.2-read-sql-and-the-connection.md)).
- **Forgetting `con.commit()`.** The rows are silently discarded when the connection closes, and
  `COUNT(*)` says zero with no error anywhere
  ([4.1](parts/04-sql/4.1-a-table-that-knows-its-types.md)).
- **`params="milk"`** — a bare string is a sequence of four characters, so you get "the statement uses
  1, and there are 4 supplied". The trailing comma in `("milk",)` is the fix
  ([4.3](parts/04-sql/4.3-params-not-f-strings.md)).
- **Letting `to_sql` create the table.** You get a column named `index` that nobody asked for, a date
  stored as text, and no constraints at all
  ([4.4](parts/04-sql/4.4-to-sql-and-what-sqlite-invents.md)).
- **`if_exists="replace"` on a table somebody has indexed.** It drops the table, so the index and
  every constraint go with it. `"delete_rows"` is what was meant
  ([4.4](parts/04-sql/4.4-to-sql-and-what-sqlite-invents.md)).
- **Iterating a chunked reader twice.** The second pass yields nothing, with no error at all
  ([5.2](parts/05-the-module/5.2-the-file-that-does-not-fit.md)).
- **Finishing a chunked read with `pd.concat`.** You now hold the whole frame, which is the thing
  chunking existed to avoid ([5.2](parts/05-the-module/5.2-the-file-that-does-not-fit.md)).

**The pattern behind almost all of these**, and the thing to carry out of the day: on Day 26 the
failures were exceptions. Today most of them are **plausible wrong answers**. Nothing raises, the
frame prints beautifully, and one column is quietly different from what you meant.

---

## §8 Verify before you code

Fetched on the day of writing. Read the argument lists rather than trusting any lesson, this one
included.

- **`pandas.read_csv`** — <https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html> — the
  argument list this day's section 1 is a tour of. Note in particular that `dtype` says *"Use `str`
  or `object` together with suitable `na_values` settings to preserve and not interpret dtype"*, and
  that `engine=` has three values of which only `pyarrow` is multithreaded.
- **`pandas.read_sql`** — <https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html> — read
  the `con` entry carefully: *"If a DBAPI2 object, only sqlite3 is supported"*, and *"The user is
  responsible for engine disposal and connection closure"*, which is
  [4.2](parts/04-sql/4.2-read-sql-and-the-connection.md)'s whole point about who closes what. The
  `params` entry points at PEP 249's `paramstyle`, which is why the placeholder is `?` here and
  `%(name)s` elsewhere.
- **`DataFrame.to_sql`** — <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html>
  — check `index` (**default `True`**) and the four `if_exists` values. Confirm for yourself that
  `delete_rows` exists, because most material written about pandas predates it and tells you to use
  `replace`.
- **Datatypes In SQLite** — <https://www.sqlite.org/datatype3.html> — the five storage classes, and
  §2.2 confirming there is no date type: dates are stored as ISO 8601 text, Julian day numbers or
  Unix time, and you choose which.
- **STRICT Tables** — <https://www.sqlite.org/stricttables.html> — added in SQLite 3.37.0
  (2021-11-27). Two paragraphs, and it is the fix for everything
  [4.4](parts/04-sql/4.4-to-sql-and-what-sqlite-invents.md) demonstrates about type affinity.

---

## §9 Say it in an interview

> A dataset arrives in one of about four shapes, and they differ in one thing that matters more than
> anything else: how much the store knows about itself. A CSV knows nothing — it is text, so every
> reader guesses, and two readers can guess differently about the same file. JSON knows a little; it
> has four types and a shape, but no schema, and it is a tree rather than a table. Parquet writes the
> types into the file and stores each column separately, so a round trip is lossless and reading
> three columns out of forty reads three columns out of forty. A database table is the only one that
> declared its types before any data existed, so it is the only one that can refuse a bad row.
>
> That ranking decides how I write the read. With a CSV I pass `dtype=` and `parse_dates=` and
> `usecols=` at read time rather than repairing afterwards, because repairing does not work: an aisle
> code like `07` read as an integer is `7`, and `astype(str)` gives me `"7"`. The zero was destroyed
> at the read and no later call brings it back. With Parquet I pass `columns=` and nothing else.
> With SQL I bind values with `params=` rather than formatting them into the query — which is a
> correctness fix before it is a security one, because the first thing it saves me from is a customer
> named O'Brien.
>
> Then I put all of that behind one loader module, so that the knowledge lives in one file instead of
> at every call site, and I write a round-trip test for each store. One of those tests asserts that
> the CSV round trip **fails**, because it does, and a limitation that is not pinned by a test gets
> tidied away by somebody who thinks the argument is clutter.

---

## §10 Done when

Every box in [CHECKLIST.md](CHECKLIST.md) is ticked, `./m depth 27` passes, and `./m check` is green.

Not when a number of sittings have passed. A part is finished when you can answer its *Check
yourself* question out loud without scrolling up, and the day is finished when you can say what each
of the four stores knows about itself — and what it costs you when it knows nothing.
