# Day 8 — CHECKLIST

**IDs covered:** `PY-07`, `PY-08` · **Principles served:** 1, 2, 3, 4, 6, 7, 8, 16, 17, 18
**Hub:** [`LESSON.md`](LESSON.md) · **Parts:** 13, in [`parts/`](parts/)

> `./m done 8` refuses to commit while any box below is unticked. Ticking a box you did not do costs
> you the only thing the gate was protecting — see
> [Day 0, 3.3](../day-00-setup/parts/03-m-script/3.3-the-done-gate.md).
>
> **No time budget on this day.** Done is this list, ticked honestly, and `./m check` green.

## Demo command

```bash
uv run python -m pytest tests/test_containers.py -v && ./m check
```

Expected: twelve passing tests (one parametrised twice), including the pair that catch disjoint bugs —
the order test and the ratio test — and a green gate.

---

## Section 1 — the ordered sequences (`PY-07`)

- [ ] Read [1.1 — a list is a dynamic array](parts/01-sequences/1.1-a-list-is-a-dynamic-array.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.2 — slicing and the copy you missed](parts/01-sequences/1.2-slicing-and-the-copy-you-missed.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.3 — a tuple is a record](parts/01-sequences/1.3-a-tuple-is-a-record.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.4 — unpacking and `*rest`](parts/01-sequences/1.4-unpacking-and-star-rest.md), ran its check-yourself, answered its out-loud question
- [ ] Read [1.5 — sort, sorted, key and stability](parts/01-sequences/1.5-sort-sorted-and-key.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Timed `list.pop(0)` against `deque.popleft()`** and watched the ratio, not the seconds
- [ ] Timed `list.insert(0, x)` against `append`
- [ ] Watched a list's `getsizeof` grow in jumps, and can say what the spare capacity buys
- [ ] Estimated the memory of a million-integer list including the integers themselves
- [ ] Confirmed `deque` indexing in the middle is not O(1), and used `maxlen` for a sliding window
- [ ] Confirmed `copy is not records` **and** `copy[0] is records[0]` in the same breath
- [ ] **Reproduced the audit-log bug**: a `[:]` "backup" that changed with the original
- [ ] Timed shallow copy, explicit rebuild and `deepcopy` on the same nested data
- [ ] Built new records with `{**r, ...}` instead of mutating, and confirmed nothing was shared
- [ ] Saw `items[:] = other` mutate and `items = other` rebind, with an alias as the witness
- [ ] Triggered the extended-slice length `ValueError`
- [ ] Confirmed `(3)` is an integer and `(3,)` is a tuple
- [ ] Hit the missing-comma error in a `sqlite3` parameter binding, or reproduced its shape
- [ ] Confirmed `(1, [2])` is unhashable, and can say which part is to blame
- [ ] Wrote a `NamedTuple` and confirmed it is still a tuple, still hashable, still unpacks, still equal
- [ ] Used all three star placements: `first, *rest`, `*init, last`, `first, *mid, last`
- [ ] Confirmed a starred target absorbs zero items without an error
- [ ] Confirmed `*rest` gives a **list** and a starred parameter gives a **tuple**
- [ ] **Predicted `i, v[i] = 1, 99` before running it** — and was wrong, or can explain why not
- [ ] Failed an unpack of a generator and confirmed it was left partially consumed
- [ ] Saw `x = papers.sort()` produce `None`
- [ ] Counted the `key=` calls and confirmed it is once per element, not per comparison
- [ ] Sorted by a tuple key with mixed directions, and by two passes, and got the same answer
- [ ] Confirmed stability by sorting on one field and watching ties keep their input order
- [ ] Made a sort raise on a `None`, then fixed it with a key that gives `None` a position
- [ ] Confirmed `sorted(["10", "9"])` does **not** raise and is still wrong

## Section 2 — the hash tables (`PY-08`)

- [ ] Read [2.1 — a set is a hash table](parts/02-sets-and-dicts/2.1-a-set-is-a-hash-table.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.2 — set algebra](parts/02-sets-and-dicts/2.2-set-algebra.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.3 — a dict is ordered now](parts/02-sets-and-dicts/2.3-a-dict-is-ordered-now.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.4 — get, setdefault, defaultdict, Counter](parts/02-sets-and-dicts/2.4-get-setdefault-and-counter.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.5 — view objects are windows](parts/02-sets-and-dicts/2.5-view-objects-are-windows.md), ran its check-yourself, answered its out-loud question
- [ ] Read [2.6 — merging dicts](parts/02-sets-and-dicts/2.6-merging-dicts.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Timed `in` on a list and a set at three sizes** and watched the set column stay flat
- [ ] Confirmed `hash(42) == hash(42.0)` and can say why that is required
- [ ] Confirmed `{1, True, 1.0}` has one element
- [ ] **Ran the same set literal in two separate processes and got two orders**
- [ ] Pinned `PYTHONHASHSEED` and watched the order become stable
- [ ] Built a class with a mutable `__hash__` and made a member unreachable
- [ ] Confirmed `{}` is a dict and `set()` is the empty set
- [ ] Replaced a nested-loop reconciliation with one set operation, and got the same answer
- [ ] Used all four operators and all three comparisons, including `isdisjoint`
- [ ] Watched `known | some_list` raise and `known.union(some_list)` succeed
- [ ] **Watched `set().union("abc")` add three characters**
- [ ] Confirmed `a | b & c` differs from `(a | b) & c`
- [ ] Compared `accumulated |= batch` against `rebuilt = rebuilt | batch` in a loop
- [ ] Confirmed a dict preserves insertion order, that updating keeps the slot, and that **delete-plus-reinsert does not**
- [ ] Confirmed plain-dict equality ignores order and `OrderedDict` equality does not
- [ ] Used `move_to_end`, and can name the only two things `OrderedDict` still does
- [ ] **Reproduced the `dict.fromkeys(keys, [])` shared-list bug** and fixed it with a comprehension
- [ ] Ran all five missing-key tools on the same key and recorded which ones grew the dict
- [ ] **Reproduced the `defaultdict` read that inserts**, then fixed it with `in`
- [ ] **Watched `setdefault(k, expensive())` run the factory on a cache hit**
- [ ] Confirmed `Counter[missing]` returns `0` without inserting
- [ ] Used `most_common`, `total`, and `Counter` subtraction — and saw zero counts dropped
- [ ] Confirmed `Counter.update` **adds** rather than replaces
- [ ] Confirmed a view costs the same regardless of the dict's size
- [ ] **Captured a view, mutated the dict, and watched the "snapshot" change**
- [ ] Wrote a schema check as `required - row.keys()` with no conversion
- [ ] Confirmed `values() & set` raises and `items() & items()` works only for hashable values
- [ ] Confirmed deleting during iteration raises and changing a **value** does not
- [ ] **Reproduced the config merge that lost three keys**
- [ ] Confirmed a merged dict shares its nested values with the originals, and mutated a module constant through one
- [ ] Saw `d.update(...)` return `None`
- [ ] Listed the colliding keys with `a.keys() & b.keys()` **before** merging

## Section 3 — deduplication

- [ ] Read [3.1 — ten thousand ids, timed](parts/03-dedup/3.1-ten-thousand-ids-timed.md), ran its check-yourself, answered its out-loud question
- [ ] Read [3.2 — order-preserving dedup](parts/03-dedup/3.2-order-preserving-dedup.md), ran its check-yourself, answered its out-loud question

**Proof, not belief:**

- [ ] **Ran the plan's example: 10 000 ids, both ways, timed** — and the two implementations were asserted equal first
- [ ] Watched the list ratio converge on **4** and the set ratio on **2**
- [ ] Watched the **speedup column grow**, and can say why that proves a complexity difference and not a constant factor
- [ ] Projected both to 1,000,000 and 10,000,000 items and wrote the numbers down
- [ ] Varied the duplicate rate and confirmed it changes the list version's cost
- [ ] Deliberately put data generation **inside** the timed region and watched the difference vanish
- [ ] Compared all four dedup forms and recorded which preserve order
- [ ] Ran `list(set(...))` in two processes and compared
- [ ] Deduplicated **by a field**, both first-wins and last-wins, and got different answers
- [ ] Confirmed `dict.fromkeys` on a list of dicts raises, and can say why
- [ ] Used a dict as an ordered set: add, remove, membership, order
- [ ] Logged `len(items) - len(deduped)` and a `Counter` of the repeated keys

---

## Build brief — the reps that are yours

- [ ] Created `src/setu/containers.py`, with a complexity stated in every docstring
- [ ] Implemented `dedup_preserving_order` — one line, with the comment on **why** it preserves order
- [ ] Implemented `dedup_by` — with the `keep` decision made before the body was written
- [ ] Implemented `reconcile` — three set operations, **no loop**
- [ ] Implemented `group_by` — one lookup per item, returning a **plain** dict
- [ ] Implemented `deep_merge` — with **all four decisions** written in the docstring first
- [ ] Implemented `snapshot_keys`
- [ ] Implemented `top_n` — with the tie-break, and the comment on `heapq.nlargest`
- [ ] Created `src/setu/benchmark.py` with `ratio_test`
- [ ] `ratio_test` generates input **outside** the timed region, takes the **minimum** of several runs, and pins the seed
- [ ] Reproduced all four story bugs in `notebooks/day-08-scratch.ipynb`
- [ ] The notebook is **not** committed; the understanding graduated to `src/setu/` (Principle 6)
- [ ] `uv run ruff check src/ tests/` passes

## The eval — it must be able to fail

- [ ] Ran `uv run python -m pytest tests/test_containers.py -v` **before** implementing and watched every test fail
- [ ] Implemented `test_dedup_preserves_first_seen_order` — asserting the exact list, not its length
- [ ] Implemented `test_dedup_is_linear_not_quadratic` — marked slow, with the comment on the threshold
- [ ] Implemented the parametrised `test_dedup_by_keeps_the_right_occurrence` — asserting position too
- [ ] Implemented `test_dedup_by_rejects_an_unknown_keep`
- [ ] Implemented `test_reconcile_reports_both_directions`
- [ ] Implemented `test_group_by_returns_a_plain_dict` — with the probe-then-check-len assertion
- [ ] Implemented `test_deep_merge_keeps_sibling_keys` — **including that the shallow version fails**
- [ ] Implemented `test_deep_merge_does_not_mutate_its_inputs` — using `is` on a nested dict
- [ ] Implemented `test_deep_merge_raises_on_a_shape_mismatch`
- [ ] Implemented `test_snapshot_keys_is_not_a_live_view` — **both halves**
- [ ] Implemented `test_top_n_is_deterministic_across_tie_breaks` — with pinned seeds
- [ ] Implemented `test_top_n_with_n_larger_than_the_input`
- [ ] **Break it, watch it go red, fix it —** replaced the dedup with `list(set(items))`; the order test went red and the ratio test passed. Restored it.
- [ ] **The one that matters most —** replaced it with the `seen = []` loop; **the order test passed and only the ratio test went red**, and can say why neither test can catch the other's bug
- [ ] **Break it, watch it go red, fix it —** returned the `defaultdict` from `group_by`, and saw the **second** assertion fail, not the first. Restored it.
- [ ] **Break it, watch it go red, fix it —** made `deep_merge` shallow, and noted the mutation test still passed. Restored it.
- [ ] **Break it, watch it go red, fix it —** removed the tie-break from `top_n`, saw it fail **intermittently**, then pinned a second seed to make it fail reliably. Restored it.
- [ ] `./m check` is green

## Budget

- [ ] **0** LLM API calls today
- [ ] **0** network requests — every input was generated locally
- [ ] **$0** spent (Principle 5)

## Understand it out loud

Say each to an empty room, in your own words, without re-reading:

- [ ] What a list holds in memory, and why `append` is O(1) and `pop(0)` is O(n)
- [ ] What a `deque` gives you and what it gives up
- [ ] Exactly what `items[:]` copies and what it does not
- [ ] A situation where a shallow copy is right and one where it is wrong
- [ ] The difference between `items[:] = other` and `items = other`
- [ ] The list/tuple distinction in terms of **meaning** rather than mutability
- [ ] What immutability buys, and why `(1, [2])` cannot be a dict key
- [ ] What `*rest` collects, its type, and the minimum length of the source
- [ ] Why `a, b = b, a` needs no temporary, in terms of evaluation order
- [ ] What `list.sort()` returns and why
- [ ] What "stable" means, and how it makes a two-pass sort work
- [ ] The sort key for "score descending, title ascending"
- [ ] Why `in` on a set does not slow down as the set grows
- [ ] The two things that property costs you, and why string hashing is randomised
- [ ] The four set operators and the sentence each answers
- [ ] Why `known | some_list` raises and why that strictness is worth having
- [ ] Exactly what the dict ordering guarantee promises, update versus reinsert
- [ ] The two things `OrderedDict` still does
- [ ] The five missing-key tools, and which modify the dict
- [ ] Why `setdefault(k, expensive())` saves nothing, and why `if d[k]:` on a defaultdict is a bug
- [ ] What a view object holds, and why `keys()` is set-like and `values()` is not
- [ ] The one-word fix for both live-view hazards
- [ ] The three ways to merge dicts, which mutate, and what "shallow" costs
- [ ] Two of the four decisions a deep merge has to make
- [ ] The ratio you expect for a linear function and for a quadratic one
- [ ] Three things that spoil a benchmark
- [ ] The one-liner for an order-preserving dedup, and why it works
- [ ] The three questions that pick a container

## Commit

- [ ] `git status --porcelain` read **before** staging
- [ ] `src/setu/containers.py`, `src/setu/benchmark.py` and `tests/test_containers.py` staged
- [ ] `notebooks/day-08-scratch.ipynb` does **not** appear in `git status` (Principle 6)
- [ ] `uv run ruff format days/day-08-containers/ src/ tests/` has run
- [ ] `uv run python scripts/depth_check.py 8` passes
- [ ] `./m done 8` ran green and created the commit
