---
day: 35
phase: 4
phase_name: "Pandas 3.0 (Module 4)"
title: "Day 35 — Where pandas stops: Polars and DuckDB, benchmarked"
ids: ["PD-15"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P7 evals before features", "P10 interview-ready artifacts", "P14 stop when reality has changed", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: gate
plan: setu
plan_version: "v2.3.0"
parts: 21
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 35 — Where pandas stops: Polars and DuckDB, benchmarked

**Phase 4 · Pandas 3.0 · Module 4 · the phase gate** · `PD-15` where pandas stops — an honest
comparison, one benchmark, and a written recommendation.

**The Phase 4 gate criterion, verbatim from the plan:** *a clean, typed, joined dataset + `audit()`
— no chained assignment anywhere.*

> **Yesterday:** what a column costs to store, and the eight numbers it will tell you about itself
> if you ask — turned into an `audit()` that returns findings rather than a table.
> **Today:** the honest question at the end of ten days of pandas. Where does it stop? What do
> Polars and DuckDB do instead, on the same file and the same question? One benchmark, run
> carefully enough to be allowed to claim something. Then the gate: the phase's five criteria, one
> part each.
> **Tomorrow:** a new phase, and a different kind of output. Matplotlib — the figure, the axes, and
> why `plt.plot` is the last thing you should reach for.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

The flat's shopping file has been growing for three years.

For most of that time nothing about it needed thinking about. Somebody opens it, adds up the year,
gets a number. Then one evening somebody opens it and the laptop pauses — not a blink, a pause, the
kind where the fan comes on. They wait. It finishes. They mention it to nobody, because it finished.

Two months later it does not finish. It stops, with a message about memory, and the message is
confusing because the file on disk is smaller than the memory in the machine. That is the first
thing worth understanding today: a file is not the same size once it is a table. Every short word
becomes an object with a pointer to it, every intermediate step makes a second copy, and the
comfortable multiple between "size on disk" and "size in memory" is not two.

So somebody asks the obvious question, and gets the obvious bad answer. Somebody on the internet
says to use a different library, and the different library is genuinely faster, and now the flat has
two dataframe libraries, two null conventions, two sets of error messages and a conversion at every
boundary — to solve a problem that, this particular time, was a column of three repeated words that
nobody had told pandas was a category.

That is the honest shape of this subject and it is why the day is structured the way it is. There
are three real answers to a file that will not fit: read less of it, use a tool built differently,
or stop pretending it is a file and put it in a database. Each is right for a different problem.
Choosing between them is not a matter of taste, and it is not settled by a benchmark somebody else
ran on somebody else's machine — which is why the middle of this day is one measurement, done
carefully enough that it is allowed to claim something, and the end of it is a written
recommendation with the conditions under which it would be wrong.

The last section is a different job. Ten days of pandas produced a promise: a clean, typed, joined
dataset with an `audit()`, and no chained assignment anywhere. That promise is now five checkable
statements, and a gate that nobody can fail is not a gate. So each of the five gets a part, and each
part says exactly how that clause can be false.

---

## §2 The map

Six sections. Sections 1 to 5 are `PD-15` — the wall, the two alternatives, the benchmark, and the
recommendation. Section 6 is the phase gate itself, one part per clause of the criterion, which is
what a `gate` day splits by (plan Part 11.7).

| Section | What it means |
|---|---|
| **1.x** | **Where pandas stops** — the wall, and what is actually hitting it |
| **2.x** | **Polars** — the same question, in a tool with no index and a query planner |
| **3.x** | **DuckDB** — the same question, in SQL, over the file |
| **4.x** | **The benchmark** — one honest measurement, and what it is allowed to claim |
| **5.x** | **The recommendation** — the written answer, and what a second tool costs |
| **6.x** | **The gate** — the Phase 4 criterion, one part per clause |

### Section 1 — where pandas stops

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [The file that did not fit](parts/01-where-pandas-stops/1.1-the-file-that-did-not-fit.md) | Why a file smaller than RAM does not fit in RAM | `foundation` |
| 1.2 | [What actually costs the time](parts/01-where-pandas-stops/1.2-what-actually-costs-the-time.md) | Read, filter, group, sort — measured separately | `working` |
| 1.3 | [The three answers](parts/01-where-pandas-stops/1.3-the-three-answers.md) | Chunk it, change the tool, or use a database | `working` |

### Section 2 — Polars

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [A frame with no index](parts/02-polars/2.1-a-frame-with-no-index.md) | What replaces `.loc`, and what you give up | `foundation` |
| 2.2 | [Expressions instead of brackets](parts/02-polars/2.2-expressions-instead-of-brackets.md) | Why `pl.col("price") > 2` computes nothing | `working` |
| 2.3 | [Lazy, and the query plan you can read](parts/02-polars/2.3-lazy-and-the-query-plan.md) | `scan`, `explain`, `collect` — and pushdown, printed | `working` |
| 2.4 | [The same question, in Polars](parts/02-polars/2.4-the-same-question-in-polars.md) | The answer checked before the timing, and what it costs a team | `production` |

### Section 3 — DuckDB

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [SQL over a file](parts/03-duckdb/3.1-sql-over-a-file.md) | Five keywords, and no loading step at all | `foundation` |
| 3.2 | [Querying a dataframe in place](parts/03-duckdb/3.2-querying-a-dataframe-in-place.md) | Reading a frame by name, and what "no copy" means | `working` |
| 3.3 | [Larger than memory](parts/03-duckdb/3.3-larger-than-memory.md) | The query that completes where pandas raises | `production` |

### Section 4 — the benchmark

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [What a fair benchmark holds fixed](parts/04-the-benchmark/4.1-what-a-fair-benchmark-holds-fixed.md) | The list, each item with the way it goes wrong | `working` |
| 4.2 | [The timing harness](parts/04-the-benchmark/4.2-the-timing-harness.md) | `min` not mean, and a checksum beside every time | `working` |
| 4.3 | [The numbers, measured](parts/04-the-benchmark/4.3-the-numbers-measured.md) | Three tools, three sizes, two conditions, one table | `production` |
| 4.4 | [The benchmark that lied](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md) | Three that followed every rule and were still wrong | `production` |

### Section 5 — the recommendation

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [The written recommendation](parts/05-the-recommendation/5.1-the-written-recommendation.md) | What stays, what moves, at what threshold, and when it is wrong | `production` |
| 5.2 | [The cost of a second tool](parts/05-the-recommendation/5.2-the-cost-of-a-second-tool.md) | Two dtype systems, two null conventions, one conversion, measured | `production` |

### Section 6 — the gate

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [The gate as a list](parts/06-the-gate/6.1-the-five-criteria.md) | Five criteria, each with a stated way of being false | `foundation` |
| 6.2 | [Clean, and typed](parts/06-the-gate/6.2-clean-and-typed.md) | Normalised keys, declared dtypes, parsed times, no `object` | `production` |
| 6.3 | [Joined, and the row count that proves it](parts/06-the-gate/6.3-joined-and-the-row-count.md) | The three assertions a join has to survive | `production` |
| 6.4 | [No chained assignment anywhere](parts/06-the-gate/6.4-no-chained-assignment-anywhere.md) | How you check a whole repository, and why grep is not enough | `production` |
| 6.5 | [The phase, closed](parts/06-the-gate/6.5-the-phase-closed.md) | The inventory, the record, and what the numbers do not claim | `production` |

**The running example is the flat's shopping file, grown up** — the same four items, three aisles
and three pack sizes as Day 34, written to Parquet at three sizes so all three tools read identical
bytes. **The one question, asked of all three:** what did each aisle cost in total, for the lines
where more than one was bought?

---

## §3 Setup — run this

```bash
mkdir -p days/day-35-where-pandas-stops/lab
touch src/setu/bench.py tests/test_bench.py
uv add polars==1.43.2 duckdb==1.5.5
uv run python -c "
import duckdb, pandas as pd, polars as pl
print(pd.__version__, pl.__version__, duckdb.__version__)
"
```

Expected: `3.0.5 1.43.2 1.5.5`. If any of the three prints something else, stop and log it in
`docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Two packages are installed today**, and they are the subject rather than a convenience.

Now confirm the one fact that makes the benchmark non-trivial — the three tools do not default to
the same amount of hardware:

```bash
uv run python -c "
import os
import polars as pl
import duckdb
print('cpu cores        :', os.cpu_count())
print('polars threads   :', pl.thread_pool_size())
print('duckdb threads   :', duckdb.sql('SELECT current_setting(\'threads\') AS t').fetchone()[0])
print('pandas threads   : 1  (for the operations this day measures)')
"
```

On the machine this page was written on: **4 cores, 4 Polars threads, 4 DuckDB threads, 1 for
pandas.** Record your own numbers, because a comparison that does not state them is measuring core
count and calling it a library
([4.1](parts/04-the-benchmark/4.1-what-a-fair-benchmark-holds-fixed.md)).

**A warning about section 1 and section 4.** [1.1](parts/01-where-pandas-stops/1.1-the-file-that-did-not-fit.md)
deliberately builds a frame too large for this machine, and section 4 builds Parquet files of up to
ten million rows. Write every one of them into a scratch directory, not into the repository, and
delete them when the day is done. If a size will not build on your machine, that is a result: record
what happened and say so in your own benchmark table rather than leaving the row blank.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/bench.py`** — [4.2](parts/04-the-benchmark/4.2-the-timing-harness.md) walks through the
harness, and [6.2](parts/06-the-gate/6.2-clean-and-typed.md) to
[6.4](parts/06-the-gate/6.4-no-chained-assignment-anywhere.md) walk through the gate checks.

- `SIZES`, `REPEATS` and `WARMUP` — the benchmark's shape, as module constants, so a run is
  reproducible and a change to it is visible in a diff.
- `BenchError(ValueError)` — for a run whose answers did not agree. Import the earlier days'
  exceptions rather than inventing a sixth family.
- `flat_receipts(rows, seed)` — the day's one dataset, built the same way every time, seeded.
- `time_it(fn, repeats, warmup)` — returns the **minimum** of the repeats and the answer's checksum
  together, so a wrong answer cannot be reported as a fast one
  ([4.2](parts/04-the-benchmark/4.2-the-timing-harness.md)).
- `same_answer(*results)` — normalises each tool's output to a comparable shape and raises
  `BenchError` when they disagree. This runs **before** any timing is reported.
- `gate_report(frame)` — the five Phase 4 criteria as a frame of findings, in the shape Day 34's
  `audit()` established ([6.1](parts/06-the-gate/6.1-the-five-criteria.md)).
- **As given, `time_it` reports the mean rather than the minimum**, and it times the function
  without a warm-up run, so the first call's import and file-cache costs land inside the stopwatch
  ([4.1](parts/04-the-benchmark/4.1-what-a-fair-benchmark-holds-fixed.md)).
- `TODO(me)`: fix `time_it`. Use the minimum, add the warm-up, and say in the docstring what the
  reported number is a measurement *of* — and what it is not.
- `TODO(me)`: add `machine()` returning the core count, the total RAM and each library's default
  thread count, and make `bench_report` include it. Say in a comment why a benchmark table without
  it is not a result.
- `TODO(me)`: add `guard_size(rows)` that refuses a row count this machine cannot hold, using the
  measured bytes-per-row rather than a guess. Say in a comment where that measurement came from.

**`tests/test_bench.py`** — the gate's own eval.

- Fixtures: a small clean frame, a frame with an unnormalised key, a frame with an `object` column,
  and a frame whose join loses rows — plus a test asserting each has the property it exists for.
- The five gate assertions from [6.1](parts/06-the-gate/6.1-the-five-criteria.md), one test each.
- A test that `same_answer` raises when two tools disagree, with `pytest.raises(..., match=...)`.
- The chained-assignment test from
  [6.4](parts/06-the-gate/6.4-no-chained-assignment-anywhere.md): the source frame is unchanged
  after the pipeline runs. This is the only reliable check, and the part says why.
- `TODO(me)`: write the tests for your fixed `time_it`, including one that fails if the warm-up is
  removed. Say in a comment why timing a timing function is harder than it sounds.
- `TODO(me)`: add a test that the gate report contains a row for **every** column of the frame, so a
  silently dropped column cannot pass the gate ([Day 34, 5.3](../day-34-categories-and-describe/parts/05-describe/5.3-include-exclude-and-the-column-left-out.md)).
- `TODO(me)`: break the gate a **second** way of your own. Watch what goes red, then record the
  change and the failure count in a `# Seen to fail:` comment. **If nothing goes red, that is the
  more interesting result** — say which criterion should have caught it and why it did not.

**`lab/three_tools_one_question.py`** — the benchmark, made runnable.

- Build the flat's file at each size in `SIZES`, write it to Parquet under a scratch directory, and
  answer the day's one question in pandas, Polars and DuckDB.
- Assert the three answers agree **before** printing any timing.
- Print the table: tool × size × (read included / read excluded), with the minimum time and the
  checksum, and the machine line above it.
- `TODO(me)`: add a cold-cache condition and say in a comment how you convinced yourself the cache
  was actually cold — and whether you could.
- `TODO(me)`: write your own recommendation, for your own machine, in a docstring at the top of the
  file. Name the threshold, the measurement it rests on, and the condition under which it would be
  wrong ([5.1](parts/05-the-recommendation/5.1-the-written-recommendation.md)).

---

## §5 The eval that must be able to fail

`tests/test_bench.py` is RED until `src/setu/bench.py` exists. Write these two first, because they
are the two that carry the day:

```python
def test_three_tools_that_disagree_are_refused(small) -> None:
    pandas_answer = {"dairy": 10.0, "bakery": 4.0}
    polars_answer = {"dairy": 10.0, "bakery": 4.0}
    duckdb_answer = {"dairy": 10.0, "bakery": 4.5}
    with pytest.raises(BenchError, match=r"disagree"):
        same_answer(pandas_answer, polars_answer, duckdb_answer)


def test_the_pipeline_does_not_change_its_input(messy) -> None:
    before = messy.copy(deep=True)
    gate_report(messy)
    pd.testing.assert_frame_equal(messy, before)
```

**The first test is the one that makes the benchmark honest.** Without it, a tool that returns the
wrong answer quickly wins, and every number in section 4 becomes a measurement of nothing
([4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md)).

**The second test is the whole "no chained assignment anywhere" clause.** You cannot grep for the
pattern reliably — the search has both false positives and false negatives — and Copy-on-Write means
the old warning no longer fires. What is left is asserting that the input frame is unchanged, and
that assertion is worth more than the grep ever was
([6.4](parts/06-the-gate/6.4-no-chained-assignment-anywhere.md)).

**The mutations to watch.** Three, and they behave differently:

1. Remove the warm-up from `time_it`. **No test goes red** unless you wrote the one the build brief
   asks for — which is exactly why it is in the build brief. The benchmark simply becomes wrong.
2. Have `gate_report` use `describe()`'s default `include`. **One test goes red** — the
   every-column one — and every numeric check still passes.
3. Drop the dtype assertion from the clean-and-typed check. **A different single test goes red**,
   and no total moves.

And one that **no correctness test can catch**: change `REPEATS` from `7` to `1`. Every test stays
green, the harness still runs, and the numbers become noise wearing three decimal places. The
defences are a test asserting the constant's value and a review that treats a benchmark's shape as
part of its result.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero model calls, zero API keys, zero network at run time.** Two pinned installs:
`polars==1.43.2` and `duckdb==1.5.5`.

The disk and memory budget is the largest of the phase, and it is deliberate. Section 4 writes
Parquet files at 100 000, 1 000 000 and 10 000 000 rows — a few hundred megabytes in total, all of it
in a scratch directory outside the repository, all of it deleted at the end of the day.
[1.1](parts/01-where-pandas-stops/1.1-the-file-that-did-not-fit.md) deliberately builds a frame that
does not fit and reads the failure; that is a controlled experiment, not an accident, and it is the
one place in the phase where you are asked to make something fail on purpose at that scale.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **A file is not the same size once it is a table**, and the multiple between them is not two
  ([1.1](parts/01-where-pandas-stops/1.1-the-file-that-did-not-fit.md)).
- **pandas is eager**, so every intermediate step is materialised whether or not anything reads it
  ([1.2](parts/01-where-pandas-stops/1.2-what-actually-costs-the-time.md)).
- **"Rewrite it in a faster library" is the third-best answer** to a problem that is often a dtype
  problem or a column-selection problem
  ([1.3](parts/01-where-pandas-stops/1.3-the-three-answers.md), and
  [Day 34, 2.2](../day-34-categories-and-describe/parts/02-the-category-dtype/2.2-astype-category-and-the-saving-measured.md)).
- **Polars has no index**, so everything alignment did for you is now an explicit join key
  ([2.1](parts/02-polars/2.1-a-frame-with-no-index.md)).
- **A Polars expression computes nothing until it is collected**, so timing a lazy query without
  `.collect()` measures the plan and not the work
  ([2.3](parts/02-polars/2.3-lazy-and-the-query-plan.md),
  [4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md)).
- **The two libraries' null semantics differ**, so a filter that keeps blanks in one drops them in
  the other ([2.4](parts/02-polars/2.4-the-same-question-in-polars.md)).
- **DuckDB reading a frame "in place" is not the same as free**, and the claim is worth measuring
  rather than repeating ([3.2](parts/03-duckdb/3.2-querying-a-dataframe-in-place.md)).
- **A DuckDB query that never materialises its rows is not doing the work pandas is doing**, so
  comparing the two as if they were the same operation is a benchmark that lies
  ([4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md)).
- **The three tools default to different thread counts**, so an unstated core count turns a library
  comparison into a hardware comparison
  ([4.1](parts/04-the-benchmark/4.1-what-a-fair-benchmark-holds-fixed.md)).
- **The second run of a query reads a warm file cache**, so run order alone can invert a ranking
  ([4.1](parts/04-the-benchmark/4.1-what-a-fair-benchmark-holds-fixed.md)).
- **A mean over repeats measures the machine's other work**, which is why the minimum is the honest
  statistic ([4.2](parts/04-the-benchmark/4.2-the-timing-harness.md), and
  [Day 25, 4.2](../day-25-copy-view-and-the-gate/parts/04-the-benchmark/4.2-timeit-honestly.md)).
- **A fast wrong answer beats a slow right one on every benchmark that does not check the answer**
  ([4.2](parts/04-the-benchmark/4.2-the-timing-harness.md)).
- **Every extra dataframe library is another dtype system, another null convention and a conversion
  at every boundary**, and that conversion has a measurable cost
  ([5.2](parts/05-the-recommendation/5.2-the-cost-of-a-second-tool.md)).
- **`dtypes == object` finds nothing in pandas 3**, so the old "is this column text" check silently
  passes ([6.2](parts/06-the-gate/6.2-clean-and-typed.md), and
  [Day 33, 1.3](../day-33-text-and-time/parts/01-the-str-accessor/1.3-the-dtype-under-the-text.md)).
- **A left join's row count does not move when nothing matches**, so the count alone does not prove
  a join worked ([6.3](parts/06-the-gate/6.3-joined-and-the-row-count.md)).
- **Grepping for chained assignment has both false positives and false negatives**, and
  Copy-on-Write means the warning that used to catch it no longer fires
  ([6.4](parts/06-the-gate/6.4-no-chained-assignment-anywhere.md)).

**The pattern behind the day.** Sections 1 to 3's failures are about **what a tool is actually
doing**; section 4's are about **what a measurement is allowed to claim**; section 6's are about
**what a criterion means when somebody tries to pass it without meeting it.** None of the three is
caught by reading code. All three are caught by running something and comparing two numbers, which
is what the harness, the answer check and the gate report exist to do.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Scaling to large datasets** — <https://pandas.pydata.org/docs/user_guide/scale.html> — pandas'
  own account of where it stops and what it suggests instead. Read it before reading anyone else's.
- **Polars user guide — concepts** — <https://docs.pola.rs/user-guide/concepts/> — expressions,
  contexts, and the lazy API, in the project's own words.
- **Polars — `LazyFrame.explain`** —
  <https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.explain.html> —
  confirm for yourself what the plan output actually contains in this version.
- **DuckDB — Python API** — <https://duckdb.org/docs/stable/clients/python/overview> — the
  replacement scan that lets a query name a dataframe, and the conversions back out.
- **DuckDB — larger-than-memory execution** —
  <https://duckdb.org/docs/stable/guides/performance/how-to-tune-workloads> — what spilling to disk
  does and what it costs.
- **`timeit`** — <https://docs.python.org/3/library/timeit.html> — read what the standard library
  says about `repeat` and about reporting the minimum.

---

## §9 Say it in an interview

> The first thing I would say is that "pandas is too slow" is usually a diagnosis nobody has made.
> A file that will not load is often a dtype problem — a column of three repeated words stored as
> text, or a float64 that only ever holds small integers — and a query that takes a long time is
> often reading columns nobody uses. So before changing tools I measure the pieces: the read, the
> filter, the group-by and the sort, separately, and I look at `memory_usage(deep=True)` per column.
> Quite often that is the end of the investigation.
>
> When it is genuinely a scale problem, there are three real answers and they suit different shapes.
> Read less — chunking, column projection, a better file format. Change the tool — Polars, which is
> multi-threaded and has a lazy API, so it can push filters and column selections down into the
> file scan instead of materialising everything first. Or stop treating it as a file and put it in a
> database — DuckDB will run SQL straight over Parquet, spill to disk when the working set does not
> fit, and hand the result back as a dataframe.
>
> The comparison itself is the part I would be careful about, because most published benchmarks are
> not measuring what they say. The three tools do not default to the same number of threads, so an
> unstated core count turns a library comparison into a hardware comparison. Timing a lazy Polars
> query without collecting it measures the query planner. Comparing a DuckDB aggregate that never
> materialises rows against a pandas read-then-group is comparing two different amounts of work. And
> the second run of anything reads a warm file cache. So I hold the data, the question and the
> machine fixed, I report the minimum of several repeats rather than the mean, and — this is the one
> people skip — I check that the three tools returned the *same answer* before I report any timing
> at all. A fast wrong answer wins every benchmark that does not do that.
>
> The recommendation that comes out the other end has to name a threshold and the measurement it
> rests on, and it has to name the conditions under which it is wrong. It also has to price the
> other side honestly: a second dataframe library is a second dtype system, a second null
> convention, a second set of error messages, another pin to keep current, and a conversion at every
> boundary between them — and that conversion has a measurable cost you can put next to the speedup.
> Quite often the right answer is one tool used properly rather than two used partly.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

This is a **gate** day, so it closes Phase 4. The gate is not a formality: each of the five criteria
in [6.1](parts/06-the-gate/6.1-the-five-criteria.md) has a stated way of being false and a command
that checks it, and a criterion you cannot fail is a criterion you have not tested. If one fails,
that is the gate working — name the two or three days to re-run and give the re-runs their own
`docs/TRACKER.md` rows.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 35` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
