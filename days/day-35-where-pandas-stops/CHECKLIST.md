# Day 35 — Definition of done

`PD-15` where pandas stops — Polars and DuckDB, benchmarked. **This is the Phase 4 gate.**
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints three tools agreeing on one answer,
with the machine they ran on named, and the five gate criteria checked:

```bash
uv run python -c "
import duckdb
import polars as pl
from setu.bench import BenchError, flat_receipts, gate_report, machine, same_answer, time_it

print('machine:', machine())

frame = flat_receipts(200_000)
question = (
    frame.loc[frame['need'] > 1]
    .groupby('aisle', observed=True)['price']
    .sum()
    .sort_values(ascending=False)
)
lazy = (
    pl.from_pandas(frame)
    .lazy()
    .filter(pl.col('need') > 1)
    .group_by('aisle')
    .agg(pl.col('price').sum())
    .sort('price', descending=True)
)
sql = duckdb.sql(
    \"SELECT aisle, sum(price) AS price FROM frame WHERE need > 1 GROUP BY aisle ORDER BY price DESC\"
).df()

same_answer(question, lazy.collect(), sql)
print('three tools agree')

seconds, checksum = time_it(lambda: frame.loc[frame['need'] > 1].groupby('aisle', observed=True)['price'].sum())
print('pandas  :', round(seconds, 4), 's   checksum', checksum)

report = gate_report(frame)
print(report.to_string(index=False))
print('failed criteria:', int((~report['passed']).sum()))
"
```

`same_answer` must not raise, the machine line must name the core count and each library's thread
count, the timing must come with a checksum beside it, and the gate report must have a row per
criterion. If any of those fails, sections 4 or 6 have not landed.

---

## Setup

- [ ] Ran `./m scaffold 35` and created `src/setu/bench.py` and `tests/test_bench.py`
- [ ] `uv add polars==1.43.2 duckdb==1.5.5` and both pins are in `pyproject.toml` and `uv.lock`
- [ ] Confirmed `pandas.__version__` is `3.0.5`, `polars.__version__` is `1.43.2`,
      `duckdb.__version__` is `1.5.5`
- [ ] If any has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 thread-count check and **recorded my own numbers** — cores, Polars threads, DuckDB
      threads
- [ ] Can say why a benchmark that omits those numbers is measuring hardware
- [ ] Chose a scratch directory outside the repository for every Parquet file today

## Section 1 — where pandas stops

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw a real out-of-memory failure on **my** machine, and recorded its message
- [ ] Measured my own bytes-per-row, rather than using a rule of thumb
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] Know which of read / filter / group / sort dominates on my machine at one million rows
- [ ] **1.3** read · ran its check-yourself · answered its question out loud
- [ ] Can name the shape of problem each of the three answers is right for

## Section 2 — Polars

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say what replaces `.loc` and alignment, and what that costs
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Printed a bare `pl.col(...)` expression and saw that it computed nothing
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Read a real `explain()` output and pointed at the projection and predicate pushdown in it
- [ ] **2.4** read · ran its check-yourself · answered its question out loud
- [ ] Checked the Polars answer against the pandas answer **before** looking at any timing
- [ ] Found one concrete null-semantics difference between the two, by running it

## Section 3 — DuckDB

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say what each of `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY` does
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] Measured the memory to check the "no copy" claim rather than repeating it
- [ ] **3.3** read · ran its check-yourself · answered its question out loud
- [ ] Ran a query over a file larger than the memory limit I set, and watched it complete
- [ ] Watched pandas fail on the same file, and recorded the error

## Section 4 — the benchmark

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Can list, without scrolling, four things a fair benchmark has to hold fixed
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say why the minimum is the honest statistic and the mean is not
- [ ] **4.3** read · ran its check-yourself · answered its question out loud
- [ ] Ran the benchmark myself and wrote **my own** table, with my machine named above it
- [ ] Recorded any size that would not build, rather than leaving the row blank
- [ ] **4.4** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced at least one of the three lying benchmarks and watched it produce a plausible
      wrong number

## Section 5 — the recommendation

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] `TODO(me)`: wrote **my own** recommendation, naming a threshold, the measurement behind it,
      and the condition under which it would be wrong
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Measured one `.to_pandas()` conversion myself and can quote its cost

## Section 6 — the gate

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] Can state all five criteria and one way each of them can be false
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Ran the clean-and-typed assertions against my own Phase 4 dataset
- [ ] **6.3** read · ran its check-yourself · answered its question out loud
- [ ] Ran the row count, the match rate and the total, and all three held
- [ ] **6.4** read · ran its check-yourself · answered its question out loud
- [ ] Tried the grep and found at least one false positive or false negative myself
- [ ] Wrote the source-frame-unchanged test, and it passes
- [ ] **6.5** read · ran its check-yourself · answered its question out loud
- [ ] Ran the inventory and recorded which of days 26–35's modules and tests exist on disk

## Build brief

- [ ] `src/setu/bench.py` exists with `SIZES`, `REPEATS` and `WARMUP` as module constants
- [ ] `BenchError` subclasses `ValueError`; no sixth exception family was invented
- [ ] `flat_receipts` is seeded, and two calls with the same seed give identical frames
- [ ] `time_it` returns the time **and** the checksum together
- [ ] `same_answer` runs before any timing is reported, and raises when the tools disagree
- [ ] `gate_report` returns a frame of findings, in Day 34's `audit()` shape
- [ ] `TODO(me)`: fixed `time_it` — minimum, warm-up, and a docstring saying what the number measures
- [ ] `TODO(me)`: added `machine()` and put it in the report, with the comment on why
- [ ] `TODO(me)`: added `guard_size` using my own measured bytes-per-row, with the comment on where
      that number came from
- [ ] `lab/three_tools_one_question.py` runs, asserts agreement first, then prints the table
- [ ] `TODO(me)`: added the cold-cache condition and said whether I could actually get one
- [ ] `TODO(me)`: wrote my recommendation into the file's docstring

## Tests

- [ ] `tests/test_bench.py` has four **fixtures**: clean, unnormalised key, `object` column,
      lossy join
- [ ] There is a test asserting each fixture has the property it exists for
- [ ] There is one test per gate criterion — five in total
- [ ] The disagreement test uses `pytest.raises` with `match=` on a fragment
- [ ] The chained-assignment test asserts the **source frame is unchanged** after the pipeline
- [ ] **Break it (1):** removed the warm-up from `time_it` and watched the suite stay **green**
      unless I had written the test the build brief asks for
- [ ] **Break it (2):** used `describe()`'s default `include` in `gate_report` and watched the
      every-column test go red
- [ ] **Break it (3):** dropped the dtype assertion and watched a **different** single test go red
- [ ] **Break it (4):** changed `REPEATS` from `7` to `1` and watched the suite stay **green**
- [ ] Can explain what (1) and (4) together prove about what a test suite can and cannot defend
- [ ] `TODO(me)`: wrote the tests for the fixed `time_it`
- [ ] `TODO(me)`: added the every-column gate-report test
- [ ] `TODO(me)`: broke the gate a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate — Phase 4 closed

- [ ] The dataset is **clean**: every text key normalised at the boundary
- [ ] The dataset is **typed**: declared dtypes, ordered categories where the order means something,
      timestamps parsed with an explicit format and a known resolution, and no `object` column
- [ ] The dataset is **joined**, with the row count, the match rate and a total all asserted
- [ ] `audit()` exists, returns findings, and covers **every** column
- [ ] **No chained assignment anywhere** — checked by the source-frame-unchanged test, not by grep
      alone
- [ ] Every criterion that failed has a named re-run plan, with its own `docs/TRACKER.md` row
- [ ] Wrote down what the benchmark does **not** claim, in my own words

## The check

- [ ] `uv run ruff format days/day-35-where-pandas-stops/ src/setu/bench.py tests/test_bench.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 35` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day
- [ ] Every Parquet file built today is deleted from the scratch directory

## Budget

- [ ] **Zero model calls, zero API keys, zero network at run time.** Two pinned installs:
      `polars==1.43.2`, `duckdb==1.5.5`. Confirmed.
- [ ] Every large file was written outside the repository, and none of them is in `git status`

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 35` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-15`, says the phase is closed, and quotes **my own** benchmark
      table's headline row and the row count at which the ranking changed
