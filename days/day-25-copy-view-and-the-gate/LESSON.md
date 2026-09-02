---
day: 25
phase: 3
phase_name: "NumPy (Module 3)"
title: "Day 25 — Copy against view, and the module that closes the phase"
ids: ["NP-10"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P11 blast radius", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: gate
plan: setu
plan_version: "v2.3.0"
parts: 19
generated: "2026-09-02"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 25 — Copy against view, and the module that closes the phase

**Phase 3 · NumPy · Module 3 · GATE** · `NP-10` copy vs view, with the plan's named example of **the bug
where `.ravel()` mutated the original and `.flatten()` did not**.

> **Yesterday:** bits, text and the matrix product — packing yes-or-no answers into an integer, and `A @ B`
> written by hand before the library did it.
> **Today:** the question that has been under every day of this phase. When does NumPy hand you a second
> label on the same memory, and when does it hand you your own? Then the module that closes Module 3: a
> stats module that never touches its caller's array and beats a Python loop by fifty times.
> **Tomorrow:** Phase 4 opens with pandas 3.0 — Copy-on-Write, the `str` dtype, and the chained-assignment
> trap, which is today's bug wearing a different hat.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a day
> is a unit of subject, not of hours (Principle 17).

---

## §1 The story

There is a shopping list on the fridge, written on a magnetic pad. Somebody photographs it before going to
the shop, so they have it on their phone.

At the shop they cross things off. Nothing happens to the pad on the fridge, because a photograph is a
picture of the list and not the list.

Now imagine a different flat where, instead of a photograph, there is a small mirror in the hall angled so
that the pad is visible from the front door. Somebody standing at the door reads the list off the mirror.
If they reach round and rub something out, it comes off the pad, because the mirror was never a copy — it
was a way of looking at the same piece of paper from somewhere else.

Both of those are useful. The photograph is safe and costs you a photograph. The mirror is free and shows
you the truth as it changes. What you cannot afford is not knowing which one you are holding — because the
mistake is not visible at the moment you make it. You cross something off, you walk away, and three days
later somebody asks why the shopping list has been missing eggs since Tuesday.

Every operation in NumPy hands you either a photograph or a mirror. Today is about knowing which, every
time, without guessing.

---

## §2 The map

Nineteen parts in five sections. Sections 1 and 2 are the idea and the bug; section 3 builds the module;
sections 4 and 5 measure it and close the phase on it.

### `parts/01-the-decision/` — which operations copy, which alias, and how to find out

| Part | What it answers | Level |
|---|---|---|
| [1.1](parts/01-the-decision/1.1-six-operations-one-question.md) — Sixteen operations, one question | Which NumPy calls give a view and which give a copy — the table for the whole phase | foundation |
| [1.2](parts/01-the-decision/1.2-the-three-probes.md) — The three probes | `base`, `flags.owndata`, `np.shares_memory` — and which one actually answers it | working |
| [1.3](parts/01-the-decision/1.3-writeable-the-flag.md) — `WRITEABLE` | The flag that turns a silent corruption into an exception | working |
| [1.4](parts/01-the-decision/1.4-out-and-aliasing.md) — Aliasing inside one call | What NumPy's ufunc overlap guarantee covers, and what it does not | production |
| [1.5](parts/01-the-decision/1.5-the-api-contract.md) — The API contract | Four function shapes, said in the name, the return type and the docstring | production |

### `parts/02-the-bug/` — the plan's named example, and how to stop it

| Part | What it answers | Level |
|---|---|---|
| [2.1](parts/02-the-bug/2.1-ravel-changed-it-flatten-did-not.md) — `ravel()` changed it, `flatten()` did not | The bug NP-10 names, reproduced, explained and fixed | working |
| [2.2](parts/02-the-bug/2.2-in-a-pipeline.md) — The same bug in a pipeline | Why six stages hide it and the failure surfaces two stages downstream | production |
| [2.3](parts/02-the-bug/2.3-the-defences.md) — The three defences | Copy out, freeze out, or assert — and which one to reach for first | production |

### `parts/03-the-module/` — the gate's code

| Part | What it answers | Level |
|---|---|---|
| [3.1](parts/03-the-module/3.1-the-gate-as-a-list.md) — The gate as a list | Five criteria, each with a stated way of being false | foundation |
| [3.2](parts/03-the-module/3.2-the-stats-module.md) — `src/setu/stats.py` | The module, with its memory contract in the docstring | production |
| [3.3](parts/03-the-module/3.3-one-pass-or-five.md) — One pass or five | Why it gathers into a copy instead of calling five nan-aware reductions | production |
| [3.4](parts/03-the-module/3.4-the-boundary-that-decides.md) — The boundary | The one line where the caller's memory ends and the module's begins | production |

### `parts/04-the-benchmark/` — the number, honestly

| Part | What it answers | Level |
|---|---|---|
| [4.1](parts/04-the-benchmark/4.1-what-fifty-times-is-against.md) — What "fifty times" is against | The same module measured 15× and 133× on the same data. Which is the claim? | working |
| [4.2](parts/04-the-benchmark/4.2-timeit-honestly.md) — `timeit` honestly | `min` not mean, `number` against `repeat`, and what got inside the stopwatch | working |
| [4.3](parts/04-the-benchmark/4.3-the-number-measured.md) — The number, measured | 56× at seven thousand readings — and the size where the loop wins | production |
| [4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md) — The benchmark that lied | Three that followed every rule in 4.2 and were still wrong | production |

### `parts/05-the-gate/` — the eval, the CI question, and the close-out

| Part | What it answers | Level |
|---|---|---|
| [5.1](parts/05-the-gate/5.1-the-eval.md) — `tests/test_stats.py` | One test per criterion, and two of them broken on purpose | production |
| [5.2](parts/05-the-gate/5.2-the-performance-test-in-ci.md) — The performance test in CI | Why a ratio travels better than a time, and where that stops being true | production |
| [5.3](parts/05-the-gate/5.3-the-phase-closed.md) — The phase, closed | The record, and the section that says what the number does not claim | production |

**The running example is the month of step counts** — a 4×7 array of daily totals with one missing reading
on week one's Thursday, the same chart every part of this day picks up.

---

## §3 Setup — run this

```bash
mkdir -p days/day-25-copy-view-and-the-gate/lab
mkdir -p docs/gates
touch src/setu/stats.py tests/test_stats.py
uv run python -c "import numpy; print(numpy.__version__)"
```

Expected: `2.5.2`. If it prints anything else, stop and log it in `docs/CHANGELOG_PLAN_DS.md` before
continuing (Principle 4).

**No new packages today.** NumPy is pinned from day 20, pytest from Module 1, and everything this day uses
— `timeit`, `tracemalloc`, `multiprocessing`, `statistics`, `platform` — is in the standard library.

Confirm the `slow` marker is registered, because [5.1](parts/05-the-gate/5.1-the-eval.md) uses it and the
project runs with `--strict-markers`:

```bash
grep -A 4 "^markers" pyproject.toml
```

Expected to include `"slow: takes more than a few seconds"`.

---

## §4 Build brief

**One module, one test file, one benchmark script, one gate record.**

**`src/setu/stats.py`** — [3.2](parts/03-the-module/3.2-the-stats-module.md) explains every line of it and
[3.4](parts/03-the-module/3.4-the-boundary-that-decides.md) explains where its boundary sits.

- `Summary` — a frozen dataclass carrying `observed`, `expected`, `mean`, `std`, `smallest`, `largest`, with
  `complete` and `spread` as properties.
- `summarise(counts, *, sample=True)` — reads only. Refuses a non-float dtype and refuses fewer than
  `MIN_FOR_SPREAD` readings. Returns plain Python numbers.
- `centre(counts)` — TRANSFORM. New array out, argument untouched.
- `centre_inplace(counts)` — IN PLACE. Returns `None`, raises on a read-only array.
- `freeze(counts)` — WINDOW. Returns a read-only view.
- `TODO(me)`: write the module docstring's `MEMORY CONTRACT` block yourself, listing all four shapes and
  where each one's boundary is. [3.4](parts/03-the-module/3.4-the-boundary-that-decides.md) shows the
  form; do not copy it — write the version for the functions you actually wrote.
- `TODO(me)`: mark the boundary line in `summarise` with a comment saying **when** it is a view and when it
  is a copy. If you cannot say which, [4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md) is the
  part that settles it.

**`lab/baselines.py`** — the loops the gate is measured against, committed so the claim is checkable.

- `loop_five_passes`, `stdlib`, `loop_one_pass`, `loop_tuned` — all four from
  [4.1](parts/04-the-benchmark/4.1-what-fifty-times-is-against.md), all returning the same five values in
  the same order.
- `TODO(me)`: write the docstring on `loop_one_pass` that says it is the committed baseline and must not be
  tuned or worsened. Say why in your own words.

**`lab/bench_stats.py`** — the measurement.

- The curve from [4.3](parts/04-the-benchmark/4.3-the-number-measured.md): every size from 28 to 7,000,000,
  in multiples of seven, one per cent missing at every size.
- `describe_the_input` from [4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md), printed above the
  timings.
- `TODO(me)`: find **your** crossing point — the size where `summarise` overtakes `loop_one_pass` on your
  machine — and write it in a comment at the top of the file.
- `TODO(me)`: decide your gate size from your own curve rather than taking 7,000 from this day, and write
  one sentence saying why you picked it.

**`tests/test_stats.py`** — [5.1](parts/05-the-gate/5.1-the-eval.md) walks through the whole file.

- One test named after each of the five `checked_by` fields in
  [3.1](parts/03-the-module/3.1-the-gate-as-a-list.md), plus the refusals, the in-place function, and the
  memory ceiling.
- `TODO(me)`: pick a **third** mutation of your own — not the two in 5.1 — make it, watch what goes red,
  and record it in the "Seen to fail" comment block. If nothing goes red, you have found a gap in the
  suite, which is the more valuable outcome.

**`docs/gates/phase-03.md`** — [5.3](parts/05-the-gate/5.3-the-phase-closed.md) gives the template.

- `TODO(me)`: write the `WHAT THIS NUMBER DOES NOT SAY` section from **your** measurements. At least four
  lines, and at least three of them should be less flattering than your headline.

---

## §5 The eval that must be able to fail

`tests/test_stats.py` is RED until the module exists, and that is the starting condition rather than a
problem. The two tests to write first, because they are the two people leave out:

```python
@pytest.mark.parametrize("name", ["summarise", "centre", "freeze"])
def test_input_is_never_modified(month, name):
    before = month.copy()
    getattr(stats, name)(month)
    assert np.array_equal(month, before, equal_nan=True)


def test_nothing_returned_aliases_the_input(month):
    assert not np.shares_memory(month, stats.centre(month))
    s = stats.summarise(month)
    for value in (s.mean, s.std, s.smallest, s.largest):
        assert type(value) is float
    assert type(s.observed) is int
```

Then the gate's own assertion, which is a **ratio** and not a time
([5.2](parts/05-the-gate/5.2-the-performance-test-in-ci.md)):

```python
@pytest.mark.slow
def test_beats_the_loop_by_fifty():
    data = gate_data()
    assert data.flags.c_contiguous, "a strided input measures a different code path"
    n = 20
    t_np = min(timeit.repeat(lambda: stats.summarise(data), number=n, repeat=7)) / n
    t_lp = min(timeit.repeat(lambda: loop_one_pass(data), number=n, repeat=7)) / n
    ratio = t_lp / t_np
    assert ratio >= GATE_RATIO, f"{ratio:.1f}x is below the gate's {GATE_RATIO:.0f}x"
```

**Green is not the finish.** Break it on purpose at least twice and watch it fail — 5.1 gives two mutations
with their real output, and the build brief asks you for a third. A suite whose failures nobody has seen is
a suite nobody has checked.

---

## §6 Request budget

**Zero.** No model calls, no network, no API keys, no cost. Everything today is NumPy, the standard library
and a laptop.

The one thing that costs something is time on the processor: the benchmark at seven million readings
allocates about 56 MB and runs for a couple of seconds per repeat, and
[5.2](parts/05-the-gate/5.2-the-performance-test-in-ci.md)'s load experiment saturates every core for a few
seconds. Close anything that matters before running that one, and expect the fans.

---

## §7 Traps

**Comparing arrays with `nan` in them using bare `np.array_equal`.** `nan != nan`, so a correct function
looks like it modified its input. `equal_nan=True` on every comparison
([2.3](parts/02-the-bug/2.3-the-defences.md)).

**Assuming `reshape(-1)` is always a view.** It is a view when the array is contiguous and a silent copy
when it is not, which costs about 30% and is invisible at the call site
([4.4](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md)).

**Using `isinstance(x, float)` to check a value is a plain Python number.** `np.float64` **is** a subclass
of `float`, so that check passes on a NumPy scalar. `type(x) is float` is the one that means it
([5.1](parts/05-the-gate/5.1-the-eval.md)).

**Timing in a loop with a lambda that closes over the loop variable.** Every timing measures the last
function, and the output looks like a clean result rather than a bug
([4.2](parts/04-the-benchmark/4.2-timeit-honestly.md)).

**Generating the test data inside the timed region.** More than half of what you measured can be
`rng.normal` ([4.2](parts/04-the-benchmark/4.2-timeit-honestly.md)).

**Quoting a speedup without its baseline.** The same module measured 15.7× and 133.4× on the same data
([4.1](parts/04-the-benchmark/4.1-what-fifty-times-is-against.md)).

**Reaching for `.copy()` at every function boundary.** It is the correct instinct in the wrong place: six
defensive copies in a six-stage pipeline is six times the data resident
([2.3](parts/02-the-bug/2.3-the-defences.md)), and adding one to `summarise` takes its peak memory from
2.11× to 3.11×.

**`np.asarray(x, dtype=...)` in a function that then writes in place.** It copies only when the dtype does
not already match, so the function modifies its caller on some inputs and not others
([3.4](parts/03-the-module/3.4-the-boundary-that-decides.md)).

---

## §8 Verify before you code

Fetched and read on the day of writing — check them again today rather than trusting this list:

- **Copies and views** — the page this whole day is an expansion of, including the sentence that `reshape`
  "creates a view where possible or a copy otherwise":
  <https://numpy.org/doc/stable/user/basics.copies.html>
- **`numpy.shares_memory`** — the exact probe, its `max_work` parameter, and the warning that the general
  problem is NP-complete: <https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html>
- **`numpy.ndarray.flags`** — `WRITEABLE`, `OWNDATA`, `C_CONTIGUOUS`, and the rule that a view of a locked
  array cannot be made writeable again:
  <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flags.html>
- **`numpy.asarray`** — *"No copy is performed if the input is already an ndarray with matching dtype and
  order"*, and what `copy=False` now raises:
  <https://numpy.org/doc/stable/reference/generated/numpy.asarray.html>
- **`numpy.ravel`** and **`numpy.ndarray.flatten`** — the pair the plan names, one of which copies always
  and one of which copies sometimes:
  <https://numpy.org/doc/stable/reference/generated/numpy.ravel.html> ·
  <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html>
- **`timeit`** — the standard library's own argument for taking the minimum rather than the mean, and the
  note that it disables garbage collection during timing:
  <https://docs.python.org/3/library/timeit.html>
- **`tracemalloc`** — `get_traced_memory()` returning current and peak:
  <https://docs.python.org/3/library/tracemalloc.html>

---

## §9 Say it in an interview

Every NumPy operation gives you back either a view — a second label on the same block of memory — or a
copy, and the whole class of bug here is not knowing which. Slicing and reshaping give views when they can;
boolean and fancy indexing always copy; `ravel` gives a view when the array is contiguous and a copy when
it is not, while `flatten` always copies, and that difference is a real bug people hit. I check with
`np.shares_memory`, not with `base` or `owndata`, because those tell you about ancestry rather than about
overlap. In my own code I put the decision in the function's name and signature — a transform returns a new
array, an in-place function has `_inplace` in its name and returns `None`, an accessor that hands out a
window returns a read-only view — and there is one line in each function where the caller's memory stops
and mine begins, marked with a comment. On the module I built for this, that discipline is tested three
ways: the caller's array is compared before and after every public call, nothing returned shares memory
with the input, and peak memory has a ceiling so a defensive copy somebody adds later turns a test red. It
runs about fifty-six times faster than a one-pass Python loop at seven thousand readings — twenty-two times
faster than a tuned one, thirty-one times at seven million, and slower than the loop below about seventy
readings, which is the kind of thing I would rather say myself than have somebody find out.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked, the tests are green, at least three of them have
been watched to fail for a reason you can name, and `docs/gates/phase-03.md` exists with its limits section
written. Done is defined by understanding and by green checks — never by elapsed time (Principle 17).
