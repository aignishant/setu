# Day 25 — CHECKLIST

**IDs covered:** `NP-10` · **Principles served:** 1, 2, 3, 4, 5, 6, 7, 10, 11, 16, 17, 18, 20
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 19, in [`parts/`](parts/) · **Kind:** phase gate

> `./m done 25` refuses to commit while any box below is unticked. Ticking a box you did not do costs you
> the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **This is a gate day, so the boxes about failure matter more than the boxes about success.** A green
> suite you have never watched go red is not evidence, and a speedup without its baseline is not a
> measurement. Every box below that says "watch it fail" or "record what it printed" is there because of
> one of those two.
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_stats.py -v && ./m depth 25 && ./m check
```

Expected: fifteen tests in `test_stats.py` passing, a green depth report for day 25, then a green gate.

---

## Setup

- [ ] Confirmed `numpy==2.5.2` is still the pin, with `uv run python scripts/check_pins.py | grep -i numpy`
- [ ] If the index has moved past 2.5.2: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped
      (Principle 14)
- [ ] Ran `./m scaffold 25` and created `src/setu/stats.py` and `tests/test_stats.py`
- [ ] Created `docs/gates/` and `days/day-25-copy-view-and-the-gate/lab/`
- [ ] Confirmed the `slow` marker is registered in `pyproject.toml`, with `grep -A 4 "^markers" pyproject.toml`
- [ ] Wrote the month — a 4×7 `float64` array with `np.nan` at `[0, 3]` — and used the same one all day

---

## Section 1 — the decision

- [ ] Read [1.1 — sixteen operations, one question](parts/01-the-decision/1.1-six-operations-one-question.md), ran its check-yourself, answered its out-loud question
- [ ] Ran the table for myself and recorded which operations surprised me
- [ ] Read [1.2 — the three probes](parts/01-the-decision/1.2-the-three-probes.md), ran its check-yourself, answered its out-loud question
- [ ] Can say why `np.shares_memory` answers the question and `base` and `owndata` do not
- [ ] Read [1.3 — `WRITEABLE`](parts/01-the-decision/1.3-writeable-the-flag.md), ran its check-yourself, answered its out-loud question
- [ ] Saw `assignment destination is read-only` with my own eyes and recorded the exact text
- [ ] Read [1.4 — aliasing inside one call](parts/01-the-decision/1.4-out-and-aliasing.md), ran its check-yourself, answered its out-loud question
- [ ] Ran both directions of the overlapping `out=` and recorded the memory difference
- [ ] Read [1.5 — the API contract](parts/01-the-decision/1.5-the-api-contract.md), ran its check-yourself, answered its out-loud question
- [ ] Wrote down the four function shapes from memory and checked them against the part

---

## Section 2 — the bug

- [ ] Read [2.1 — `ravel()` changed it, `flatten()` did not](parts/02-the-bug/2.1-ravel-changed-it-flatten-did-not.md), ran its check-yourself, answered its out-loud question
- [ ] Reproduced the plan's named bug on my own array, and can say in one sentence why it happens
- [ ] Ran `ravel()` on a **non-contiguous** array and saw that it copied instead
- [ ] Read [2.2 — the same bug in a pipeline](parts/02-the-bug/2.2-in-a-pipeline.md), ran its check-yourself, answered its out-loud question
- [ ] Can name the reason the failure appears two stages after the mistake
- [ ] Read [2.3 — the three defences](parts/02-the-bug/2.3-the-defences.md), ran its check-yourself, answered its out-loud question
- [ ] Saw the `equal_nan` false alarm and know why it fires on correct code

---

## Section 3 — the module

- [ ] Read [3.1 — the gate as a list](parts/03-the-module/3.1-the-gate-as-a-list.md), ran its check-yourself, answered its out-loud question
- [ ] Wrote my own five criteria with a `falsified_by` on each, before writing any module code
- [ ] Read [3.2 — `src/setu/stats.py`](parts/03-the-module/3.2-the-stats-module.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — one pass or five](parts/03-the-module/3.3-one-pass-or-five.md), ran its check-yourself, answered its out-loud question
- [ ] Measured gather-against-skip on my own machine and recorded both the time and the peak memory
- [ ] Recorded what the trade looks like at **one** statistic, not just at five
- [ ] Read [3.4 — the boundary](parts/03-the-module/3.4-the-boundary-that-decides.md), ran its check-yourself, answered its out-loud question
- [ ] Probed every intermediate in `summarise` with `shares_memory` and found the line where it flips
- [ ] Ran the `np.asarray` failure and watched the same function modify its caller on one input and not the other

---

## Section 4 — the benchmark

- [ ] Read [4.1 — what "fifty times" is against](parts/04-the-benchmark/4.1-what-fifty-times-is-against.md), ran its check-yourself, answered its out-loud question
- [ ] Wrote at least two baselines myself and recorded both ratios with their names attached
- [ ] Ran the baseline that forgot the missing readings and saw `agrees=False`
- [ ] Read [4.2 — `timeit` honestly](parts/04-the-benchmark/4.2-timeit-honestly.md), ran its check-yourself, answered its out-loud question
- [ ] Printed all fifteen repeats and recorded my own min, mean and spread
- [ ] Reproduced the late-binding lambda bug and saw two timings agree when they should not have
- [ ] Measured how much of a timing is data generation when the generator is inside the lambda
- [ ] Read [4.3 — the number, measured](parts/04-the-benchmark/4.3-the-number-measured.md), ran its check-yourself, answered its out-loud question
- [ ] Ran the full curve and wrote down **my** crossing point and **my** peak
- [ ] Broke `summarise` into steps and recorded which one is the largest share
- [ ] Read [4.4 — the benchmark that lied](parts/04-the-benchmark/4.4-the-benchmark-that-lied.md), ran its check-yourself, answered its out-loud question
- [ ] Timed a generator expression against a list comprehension and saw the size of the lie
- [ ] Compared a contiguous array against a strided one holding identical values, and recorded the gap
- [ ] Swept the missing fraction and recorded how far the ratio moved

---

## Section 5 — the gate

- [ ] Read [5.1 — the eval](parts/05-the-gate/5.1-the-eval.md), ran its check-yourself, answered its out-loud question
- [ ] Read [5.2 — the performance test in CI](parts/05-the-gate/5.2-the-performance-test-in-ci.md), ran its check-yourself, answered its out-loud question
- [ ] Measured my own headroom above the threshold over at least ten runs
- [ ] Ran the load experiment and recorded which direction my ratio moved
- [ ] Read [5.3 — the phase, closed](parts/05-the-gate/5.3-the-phase-closed.md), ran its check-yourself, answered its out-loud question

---

## Build

- [ ] `src/setu/stats.py` has `Summary`, `summarise`, `centre`, `centre_inplace` and `freeze`
- [ ] `TODO(me)`: wrote the module docstring's `MEMORY CONTRACT` block myself, naming all four shapes
- [ ] `TODO(me)`: marked the boundary line in `summarise` with a comment that says when it is a view
      and when it is a copy
- [ ] `summarise` refuses a non-float dtype with a message naming the dtype it got
- [ ] `summarise` refuses fewer than `MIN_FOR_SPREAD` readings rather than answering
- [ ] `centre_inplace` returns `None` and raises on a read-only array
- [ ] `lab/baselines.py` holds all four loops, each returning the same five values in the same order
- [ ] `TODO(me)`: wrote the docstring on `loop_one_pass` saying it must not be tuned or worsened
- [ ] `lab/bench_stats.py` prints `describe_the_input` above every timing
- [ ] `TODO(me)`: recorded my own crossing point in a comment at the top of `bench_stats.py`
- [ ] `TODO(me)`: chose my gate size from my own curve and wrote one sentence saying why
- [ ] `uv run ruff format days/day-25-copy-view-and-the-gate/ src/setu/stats.py tests/test_stats.py` is clean
- [ ] `uv run ruff check` has no findings I silenced rather than fixed

---

## The eval

- [ ] `tests/test_stats.py` has a test named after each of my five `checked_by` fields
- [ ] `test_input_is_never_modified` is parametrised over every read-only public function
- [ ] `test_nothing_returned_aliases_the_input` uses `type(x) is float`, not `isinstance`
- [ ] `test_summarise_makes_one_copy_not_five` has a docstring accounting for every expected allocation
- [ ] The timing test asserts a **ratio**, not a time, and times its baseline in the same process
- [ ] `uv run python -m pytest tests/test_stats.py -q` is green
- [ ] `uv run python -m pytest tests/test_stats.py -q -m "not slow"` deselects exactly one test
- [ ] **Break it 1:** deleted `view.flags.writeable = False` from `freeze`, watched two tests go red with
      `DID NOT RAISE ValueError`, put it back
- [ ] **Break it 2:** added `counts = counts.copy()` at the top of `summarise`, watched the memory test go
      red with the peak printed in the message, took it out
- [ ] **Break it 3:** `TODO(me)` — my own mutation, what went red, and what it told me. If nothing went
      red, wrote down which criterion has no real test
- [ ] Recorded all three mutations in a "Seen to fail" comment block in the test file

---

## Budget

- [ ] Zero model calls, zero network requests, zero cost — confirmed and stated (Principle 5)
- [ ] Closed anything that matters before running the load experiment in 5.2

---

## Close the day

- [ ] Ran the phase inventory and it prints `phase 3 complete`
- [ ] `docs/gates/phase-03.md` exists, with the gate, the result, the evidence and the limits
- [ ] `TODO(me)`: the `WHAT THIS NUMBER DOES NOT SAY` section has at least four lines, and at least three
      of them are less flattering than the headline
- [ ] Can answer §9's interview paragraph out loud without reading it
- [ ] `./m depth 25` is green
- [ ] `./m check` is green
- [ ] `./m done 25` — committed, with the gate record in the same commit as the module
