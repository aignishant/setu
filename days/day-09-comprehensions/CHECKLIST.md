# Day 9 — CHECKLIST

**IDs covered:** `PY-09` · **Principles served:** 1, 2, 3, 6, 7, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 10, in [`parts/`](parts/)

> `./m done 9` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_pipeline.py -v && ./m check
```

Expected: twelve passing tests (one parametrised twice, one marked slow), including the call-count test
that is the only thing distinguishing a correct implementation from a doubly-expensive one — and a
green gate.

---

## Section 1 — the list comprehension

- [ ] Read [1.1 — the loop and the comprehension](parts/01-list-comprehensions/1.1-the-loop-and-the-comprehension.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — the filter clause](parts/01-list-comprehensions/1.2-the-filter-clause.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — the two `if`s](parts/01-list-comprehensions/1.3-the-two-ifs.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — nested comprehensions](parts/01-list-comprehensions/1.4-nested-comprehensions.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Wrote the plan's exercise: the same transform as a loop and a comprehension, and read both aloud**
- [ ] Asserted the two versions produce identical results
- [ ] Built all four containers with the same syntax and confirmed parentheses give a **generator**
- [ ] Timed the explicit loop, the loop with `append` pre-bound, and the comprehension — and can say where the gap comes from
- [ ] Wrote `[print(x) for x in items]` and looked at what it returned
- [ ] Watched a comprehension raise on a bad value, then fixed it with a filter
- [ ] Confirmed the filter runs **before** the expression, by guarding a conversion
- [ ] Chained two filters where the second depends on the first
- [ ] **Counted the calls in `[f(x) for x in xs if f(x)]`** and saw it double
- [ ] Fixed the double call with a walrus, and again with a nested generator
- [ ] Ran a filter-then-transform and a transform-then-filter and can say which value each tests
- [ ] Computed `len(source) - len(result)` and can say why that line matters
- [ ] Found an input where `isdigit()` drops a valid number
- [ ] **Ran the two `if` forms on the same input and got two different lengths**
- [ ] Computed the mean three ways and found the one that divides by the wrong count
- [ ] Triggered both `SyntaxError`s: an `else` on a filter, and a ternary with no `else`
- [ ] **Zipped a filtered list against an unfiltered one and watched the labels shift**
- [ ] Filtered the **pairs** instead, and confirmed the alignment held
- [ ] Wrote a flattening comprehension and confirmed the clause order matches the nested loops
- [ ] Reversed the clause order and got the same pairs in a different order, with no error
- [ ] Got `NameError` from a clause using a variable bound to its right
- [ ] Placed a guard between two `for` clauses, and again at the end, and saw one raise
- [ ] Distinguished two `for` clauses from a comprehension inside a comprehension
- [ ] Wrote the transpose both ways and compared with `zip(*rows)`

## Section 2 — the other three results

- [ ] Read [2.1 — dict comprehensions](parts/02-dict-set-gen/2.1-dict-comprehensions.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — set comprehensions](parts/02-dict-set-gen/2.2-set-comprehensions.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — the generator expression](parts/02-dict-set-gen/2.3-the-generator-expression.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Built an index from a duplicated key and counted what vanished**
- [ ] Confirmed the surviving value is the **last** and the position is the **first**
- [ ] Kept the first occurrence instead, with `reversed()`
- [ ] Listed the repeated keys with a `Counter`
- [ ] Used all four dict-comprehension shapes: index, transform, filter, invert
- [ ] **Inverted a dict with duplicate values and lost an entry**
- [ ] Tried to invert a dict with list values and got a `TypeError`
- [ ] Wrote the safe inversion with a `defaultdict`, and can say why it cannot be a comprehension
- [ ] Fixed the `dict.fromkeys(keys, [])` shared-list bug with a comprehension
- [ ] Omitted the colon and got a set, then confirmed a set is not subscriptable
- [ ] Compared `set(titles)` against `{normalise(t) for t in titles}` and can say why the counts differ
- [ ] Got `TypeError: unhashable type` from a set comprehension, and fixed it with a tuple **and** with a frozenset
- [ ] **Ran a set comprehension's iteration order in two separate processes and compared**
- [ ] Wrapped it in `sorted()` for display
- [ ] Built a membership lookup with a set comprehension and timed it against a list
- [ ] **Watched a generator expression run nothing at creation**, then produce items on `next()`
- [ ] Confirmed a generator's second pass is empty, with no error
- [ ] Got `TypeError` from `len(gen)` and from `gen[0]`
- [ ] Measured the peak memory of `sum([...])` against `sum(...)`
- [ ] **Counted the calls in `any([...])` versus `any(...)`** and saw the short-circuit
- [ ] Used `next(genexp, None)` as the first-match-or-nothing idiom
- [ ] Consumed a generator with `sum` and watched `max` raise on the empty remainder
- [ ] Confirmed a generator's expression reads enclosing variables at consumption time

## Section 3 — when the one line is wrong

- [ ] Read [3.1 — when a comprehension is wrong](parts/03-when-not-to/3.1-when-a-comprehension-is-wrong.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — comprehension scope and the walrus](parts/03-when-not-to/3.2-comprehension-scope.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.3 — the list you never needed](parts/03-when-not-to/3.3-the-list-you-never-needed.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] Can name all four boundaries and give an example of each
- [ ] Wrote the four responses to a failing conversion: comprehension, filter, sentinel helper, loop
- [ ] **Wrote the loop that collects both the successes and the failures with their reasons**
- [ ] Confirmed a side-effect comprehension allocates a discarded list
- [ ] Split a side-effect loop into a pure comprehension plus a loop for the effect
- [ ] **Tried to group with a comprehension and got the last item instead of the group**
- [ ] Tried it again with the value wrapped in a list, and saw the right *shape* with the wrong data
- [ ] Wrote the `defaultdict` grouping, and used `itertools.groupby` — and saw it split a group on unsorted input
- [ ] Used `itertools.accumulate` for a running total
- [ ] Confirmed a comprehension's loop variable does **not** leak, and that a `for` loop's does
- [ ] Confirmed an enclosing variable is readable inside a comprehension
- [ ] **Watched a walrus target leak, holding the last COMPUTED value rather than the last kept**
- [ ] Wrote the walrus collision bug and confirmed the visible result stayed right
- [ ] Compared the walrus form against the nested-generator form on call count and on leakage
- [ ] Triggered the missing-parentheses `SyntaxError` on a walrus
- [ ] **Measured the peak memory of all five list-versus-generator idiom pairs**
- [ ] Confirmed `len([x for x in xs if p(x)])` and `sum(1 for x in xs if p(x))` agree and differ in memory
- [ ] Computed two aggregates over one stream with a loop, and can say why two generator passes fail
- [ ] Ran `itertools.tee` and can say why it is usually not the answer
- [ ] Read a traceback where the error surfaced at the consumer rather than the producer

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/pipeline.py` with the `StageCounts` named tuple
- [ ] Implemented `normalised_keys` — **one call per title**, with the comment saying which fix and why
- [ ] Implemented `dedup_keys` — one line, with the comment on why order is preserved
- [ ] Implemented `index_by` — with the drop-reporting decision made **before** the body
- [ ] Implemented `group_by_year` — a loop, with the comment naming the boundary
- [ ] Implemented `parse_years` — keeping the error **message**, not just the value
- [ ] Implemented `stream_lengths` — annotated `Iterator`, and not a list
- [ ] Implemented `summarise` — one pass, with the comment on why `tee` is not the answer
- [ ] Implemented `run` — several one-line stages with a `StageCounts` between them
- [ ] Converted three of Day 8's functions, running the existing suite **before and after** each
- [ ] Left `group_by` and `deep_merge` as loops, each with a comment naming its boundary
- [ ] Reproduced all six story lines in `notebooks/day-09-scratch.ipynb`
- [ ] The notebook is **not** committed; the understanding graduated to `src/setu/` (Principle 6)
- [ ] `uv run ruff check src/ tests/` passes, including the `C4` family

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_pipeline.py -v` **before** implementing and watched every test fail
- [ ] Implemented `test_normalised_keys_calls_normalise_once_per_title`
- [ ] Implemented `test_normalised_keys_drops_blanks_and_says_how_many`
- [ ] Implemented `test_dedup_preserves_first_seen_order` — asserting the exact list
- [ ] Implemented the parametrised `test_index_by_keeps_the_right_occurrence` — asserting position too
- [ ] Implemented `test_index_by_reports_what_it_dropped`
- [ ] Implemented `test_group_by_year_groups_rather_than_overwrites` — with the comment recording what a comprehension would give
- [ ] Implemented `test_parse_years_returns_both_the_good_and_the_bad`
- [ ] Implemented `test_stream_lengths_is_lazy` — with the would-raise-at-item-100 generator
- [ ] Implemented `test_stream_lengths_is_consumed_once` — with the comment on whether that is wanted
- [ ] Implemented `test_summarise_makes_one_pass_over_a_one_shot_source` — passing a **generator**
- [ ] Implemented the slow-marked `test_summarise_memory_does_not_grow_with_the_input`
- [ ] Implemented `test_run_reports_a_count_for_every_stage` — asserting the stages chain
- [ ] **The one that matters most —** rewrote `normalised_keys` with the double call, watched **the result stay identical and only the call-count test go red**, and can say why that is the only assertion that could catch it
- [ ] **Break it, watch it go red, fix it —** made `index_by` last-wins for both modes; the parametrised test failed for one parameter only. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `group_by_year` a dict comprehension, wrote down what it returned, and noted the shape still looked right. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `stream_lengths` return a list, and named the two different reasons two tests failed. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `summarise` use two generator passes, saw **the memory test pass and the one-shot test return zero without raising**. Restored it.
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] **0** network requests
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] A loop and its comprehension, read aloud, and the *what* versus *how* difference
- [ ] The three things a comprehension cannot do
- [ ] What parentheses give you instead of a tuple
- [ ] Where the filter `if` goes and in what order the pieces are evaluated
- [ ] Why `[f(x) for x in xs if f(x)]` calls `f` twice, and two ways to fix it
- [ ] Where each `if` goes, what each does to the length, and which requires an `else`
- [ ] Why filtering one of two parallel sequences is dangerous, and what to do instead
- [ ] The rule for the order of `for` clauses, and why the expression's variable order is irrelevant
- [ ] Where a filter goes in a nested comprehension, and what one clause too late does
- [ ] What happens when two items produce the same dict key — which value, which position
- [ ] Why `{k: [] for k in keys}` differs from `dict.fromkeys(keys, [])`
- [ ] What a set comprehension gives you and the two things it charges
- [ ] Why `{normalise(t) for t in titles}` collapses more than `set(titles)`
- [ ] What `(expr for x in items)` produces, and what happens when you create it
- [ ] The three things a generator cannot do, and one case where laziness is a large win
- [ ] The four boundaries where a comprehension is the wrong tool
- [ ] What to look for in a diff that converts a loop into a comprehension
- [ ] Whether a comprehension's loop variable leaks, and what changed between Python 2 and 3
- [ ] What the walrus is for inside a comprehension, and why its leaked value is not the last result
- [ ] The one question that decides between brackets and parentheses
- [ ] Why a loop beats two generator passes when you need two aggregates

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `src/setu/pipeline.py`, `tests/test_pipeline.py` and the edited `src/setu/containers.py` staged
- [ ] `notebooks/day-09-scratch.ipynb` does **not** appear in `git status` (Principle 6)
- [ ] `uv run ruff format days/day-09-comprehensions/ src/ tests/` has run
- [ ] `uv run python scripts/depth_check.py 9` passes
- [ ] `./m done 9` ran green and created the commit
