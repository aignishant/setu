# Day 37 — CHECKLIST

**IDs covered:** VIZ-02, VIZ-03 · **Principles served:** 1, 7, 10

## Demo command

```bash
uv run python days/day-37/lab/customising.py
uv run python -m pytest tests/test_plots.py -v
```

Expected: the eleven-part report ending with the chart chooser, then all plot tests green.

## Setup

- [ ] `./m start 37` and `./m scaffold 37` run
- [ ] `days/day-37/lab/customising.py` created
- [ ] No new packages installed

## VIZ-02 — customising

- [ ] Wrote a title that states the **finding**, not the axes
- [ ] Used a `FuncFormatter` and put the units in the **axis label**
- [ ] Compared rotated labels with `barh` and can say which is the fix
- [ ] Used `set_yscale("log")` and stated it in the label
- [ ] Used `ax.grid(alpha=...)` with `set_axisbelow(True)`
- [ ] Added an `annotate` with an arrow pointing at the finding
- [ ] Used `legend(frameon=False)` and tried direct labelling once
- [ ] Can state the readability bar: a stranger reads it with no caption

## VIZ-03 — choosing

- [ ] Ran `the_truncated_axis()` and **looked at both panels**
- [ ] Can explain why truncation is dishonest on a bar and often right on a line
- [ ] Ran `the_bar_of_means()` and confirmed the two means are nearly identical
- [ ] Confirmed group B is **bimodal** and that only the histogram revealed it
- [ ] Can say what a bimodal group usually means in practice
- [ ] Ran `dual_axes_are_almost_always_wrong()`; can name two honest alternatives
- [ ] Read the seven chart-chooser rules **out loud**
- [ ] Can recall at least five from memory

## Build brief

- [ ] `annotate_point` — **TODO(me)**: point-offset, refuses off-screen points
- [ ] `apply_units` — **TODO(me)**: `FuncFormatter`, never rescales the data
- [ ] `assert_honest_bar` — **TODO(me)**: detects the value axis from patch geometry
- [ ] `distribution_panel` — **TODO(me)**: hist/box/violin, reports n per group
- [ ] `dumbbell` — **TODO(me)**: sorted by change size, rejects duplicates
- [ ] Can explain why making the honest chart easy beats warning about the dishonest one

## Tests that must be able to fail

- [ ] `test_apply_units_formats_the_ticks` — green
- [ ] **Removed the `fig.canvas.draw()`, saw empty labels, understood why** ← do not skip
- [ ] `test_apply_units_does_not_change_the_data` — green
- [ ] `test_apply_units_rejects_a_bad_axis` — green
- [ ] `test_annotate_point_adds_text` — green
- [ ] `test_annotate_point_refuses_an_offscreen_point` — green
- [ ] `test_honest_bar_passes_when_zero_is_included` — green
- [ ] `test_honest_bar_rejects_a_truncated_axis` — green ← **today's real assessment**
- [ ] `test_honest_bar_checks_the_x_axis_for_horizontal_bars` — green
- [ ] `test_honest_bar_ignores_the_wrong_axis_for_horizontal_bars` — green
- [ ] **Checked `y` unconditionally, watched the horizontal test go red; then checked both axes, watched the other go red; then detected the axis from the patch** ← do not skip
- [ ] `test_honest_bar_raises_when_there_are_no_bars` — green
- [ ] `test_distribution_panel_draws_one_series_per_group` — green
- [ ] `test_distribution_panel_reports_n_per_group` — green
- [ ] `test_distribution_panel_rejects_a_tiny_group` / `..._unknown_kind` — green
- [ ] `test_dumbbell_sorts_by_change_size` — green
- [ ] `test_dumbbell_rejects_duplicate_categories` — green
- [ ] No figures leaked (the autouse fixture stayed green)

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Why must a bar chart's value axis start at zero, and why is a line chart different?
- [ ] Describe the bar-of-means failure using the numbers you printed
- [ ] What does a bimodal distribution usually mean about the group?
- [ ] Why are dual y-axes almost always dishonest?
- [ ] When is a pie chart acceptable?
- [ ] Why must a log scale be stated in the axis label?
- [ ] Why does `assert_honest_bar` need to work out which axis carries the value?
- [ ] Why does a distribution chart need `n` displayed?

## Commit

- [ ] `./m check && ./m done 37` succeeded
