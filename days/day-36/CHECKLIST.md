# Day 36 — CHECKLIST

**IDs covered:** VIZ-01 · **Principles served:** 1, 6, 7

## Demo command

```bash
uv run python days/day-36/lab/anatomy.py
uv run python -m pytest tests/test_plots.py -v
```

Expected: the six-part anatomy report, then all plot tests green with **no leaked figures**.

## Setup

- [ ] `./m start 36` and `./m scaffold 36` run
- [ ] `uv add "matplotlib==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-36/lab/anatomy.py`, `src/setu/plots.py`, `tests/test_plots.py`
- [ ] `matplotlib.use("Agg")` placed **before** the pyplot import

## VIZ-01 — the object model

- [ ] Ran `the_state_machine_trap()` and saw the title land on the second figure
- [ ] Can state in one sentence why the state machine fails inside a function
- [ ] Used `fig, ax = plt.subplots()` and inspected both objects
- [ ] Unpacked `line, = ax.plot(...)` and know why the comma is there
- [ ] Inspected `ax.lines` and confirmed the artists are attached to the Axes
- [ ] Built a 2×2 grid; confirmed `axes` is a **NumPy array** and used `.flat`
- [ ] Can list three figure-level and three axes-level operations from memory
- [ ] Layered several artists on one Axes and used `zorder` once
- [ ] Saved both PNG and SVG; can say when each is right
- [ ] Ran `the_leak()` and saw 30 figures held open

## Build brief

- [ ] `new_axes` — **TODO(me)**: the single entry point for project defaults
- [ ] `line` — **TODO(me)**: optional `ax=`, labels from columns, legend only when >1 series, reports all missing columns
- [ ] `bar` — **TODO(me)**: horizontal option, sorts descending, respects ordered categoricals, rejects duplicates
- [ ] `save` — **TODO(me)**: `tight_layout`, both formats, **closes the figure**, creates parents
- [ ] `grid` — **TODO(me)**: always a flat list, never squeezed
- [ ] **No function in `plots.py` calls `plt.show()` or `plt.savefig()`**
- [ ] Every plotting function **returns the Axes**

## Tests that must be able to fail

- [ ] `test_new_axes_returns_a_figure_and_axes` — green
- [ ] `test_line_labels_the_axes_from_the_columns` — green
- [ ] `test_line_draws_one_artist_per_series` — green
- [ ] `test_legend_only_when_there_are_several_series` — green
- [ ] `test_line_reports_every_missing_column` — green (both names in the message)
- [ ] `test_functions_compose_onto_a_caller_supplied_axes` — green ← **makes Day 41 possible**
- [ ] **Made `line` ignore the `ax=` argument and build its own, watched it go red, fixed it** ← do not skip
- [ ] `test_bar_rejects_duplicate_categories` — green
- [ ] `test_bar_sorts_descending_by_default` — green
- [ ] `test_bar_respects_an_ordered_categorical` — green
- [ ] **Sorted the ordered categorical by value, watched it go red, fixed it** ← do not skip
- [ ] `test_save_writes_both_formats_and_closes` — green
- [ ] **Removed the `plt.close` from `save`, watched the autouse fixture catch it, restored it** ← do not skip
- [ ] `test_save_creates_parent_directories` / `test_save_rejects_an_unknown_format` — green
- [ ] `test_grid_always_returns_a_flat_list` — four green cases including 1×1 and 1×3
- [ ] `test_no_plt_show_or_savefig_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the hidden state in the pyplot API, and where exactly does it bite?
- [ ] What is a Figure, what is an Axes, and which operations belong to each?
- [ ] Why does `ax.plot()` return a list?
- [ ] Why does every plotting function return the Axes instead of showing the chart?
- [ ] Why does every plotting function accept an optional `ax=`?
- [ ] Why test `ax.lines` rather than compare rendered images?
- [ ] What happens if you forget `plt.close(fig)` in a loop over 500 groups?
- [ ] Why must `matplotlib.use("Agg")` come before the pyplot import?

## Commit

- [ ] `./m check && ./m done 36` succeeded
