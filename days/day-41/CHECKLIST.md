# Day 41 — CHECKLIST · **PHASE 5 GATE**

**IDs covered:** VIZ-08 · **Principles served:** 1, 5, 7, 10 · **Artifact:** the figure pack

## Demo command

```bash
uv run python days/day-41/lab/interactive.py
uv run python scripts/figure_pack.py
uv run python -m pytest -q
```

Expected: the seven-part Plotly report with measured file sizes, then the pack builds in under 30
seconds, then the **whole** suite green.

## Setup

- [ ] `./m start 41` and `./m scaffold 41` run
- [ ] `uv add "plotly==<your pin>"` — exact-pinned, drift logged
- [ ] Files created: `days/day-41/lab/interactive.py`, `scripts/figure_pack.py`
- [ ] Did **not** install `kaleido`; can explain why

## VIZ-08 — Plotly

- [ ] Used both `plotly.express` and `graph_objects`; confirmed they produce the same object type
- [ ] Know what a **trace** is and why it makes click-to-toggle work
- [ ] Built a hover chart (case 1) and can say what a static version would need
- [ ] Built a range slider (case 2)
- [ ] Built a 12-series toggle chart (case 3)
- [ ] Ran `the_costs()`; recorded standalone ______ KiB vs CDN ______ KiB
- [ ] Compared against a Matplotlib SVG of the same chart
- [ ] Applied `symbol=` and the house `PALETTE` to a Plotly chart
- [ ] Can state the three cases where interactivity earns its weight
- [ ] Can state the default, and why

## Build brief

- [ ] `interactive_scatter` — **TODO(me)**: house palette, symbol alongside colour, 50k cap
- [ ] `write_interactive` — **TODO(me)**: CDN by default, returns the size
- [ ] `assert_pack_is_publishable` — **TODO(me)**: every lint, every panel, one message

## The figure pack (the gate artifact)

- [ ] `scripts/figure_pack.py` written
- [ ] `apply_house_style()` called **once**, in `main()`
- [ ] One figure via `grid(4, 2)`; every panel drawn onto its supplied `ax`
- [ ] Panel 1 — distribution, histogram, log-x, n and bins in the title
- [ ] Panel 2 — the same variable as an ECDF
- [ ] Panel 3 — `grouped_box` with points overlaid and n on the ticks
- [ ] Panel 4 — `mean_with_ci`, zero-based, error measure labelled
- [ ] Panel 5 — multi-series line using `distinct_styles`
- [ ] Panel 6 — scatter with `trend=True` and r reported
- [ ] Panel 7 — correlation heatmap, masked, diverging, fixed limits
- [ ] Panel 8 — dumbbell, sorted by change
- [ ] `assert_accessible_axes` run on **every** panel
- [ ] `assert_honest_bar` run on the bar panels
- [ ] Heatmap findings printed; script exits non-zero if a leak is found
- [ ] Saved to `reports/figures/phase5_pack.{svg,png}`
- [ ] Runs in **under 30 seconds**
- [ ] **No new plotting code was needed inside the script**

## Tests that must be able to fail

- [ ] `test_interactive_scatter_uses_shape_as_well_as_colour` — green
- [ ] `test_interactive_scatter_uses_the_house_palette` — green
- [ ] **Dropped `color_discrete_sequence`, watched it go red, restored it** ← do not skip
- [ ] `test_interactive_scatter_refuses_too_many_points` — green
- [ ] `test_write_interactive_defaults_to_the_small_file` — green
- [ ] `test_write_interactive_rejects_a_bad_suffix` — green
- [ ] `test_pack_check_passes_compliant_panels` — green
- [ ] `test_pack_check_reports_every_failing_panel` — green (both indices in one message)
- [ ] **Made it raise on the first failure, watched it go red, collected them all instead** ← do not skip
- [ ] `test_figure_pack_script_exists_and_runs` — green
- [ ] `test_figure_pack_produced_both_formats` — green
- [ ] `test_figure_pack_has_eight_panels` — green

## The human check

- [ ] **Opened the PNG and looked at it.** Would you put it in a report?
- [ ] Converted it to greyscale (or printed it) and confirmed every panel still reads
- [ ] Every panel has a title stating a finding, not just the variables
- [ ] No panel needs you standing next to it to be understood

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are the three cases where interactivity earns its weight?
- [ ] What does Plotly cost you, in file size and in reach?
- [ ] Why does this project not install `kaleido`?
- [ ] What is a trace, and why does it matter for the legend?
- [ ] Why do the Day 40 accessibility rules still apply to an interactive chart?
- [ ] Why must `apply_house_style()` be called once rather than per panel?
- [ ] Why is the figure pack a **script with an exit code** rather than a notebook?
- [ ] What would it mean if a panel needed new plotting code inside `figure_pack.py`?

## PHASE 5 GATE

- [ ] `scripts/figure_pack.py` runs clean in one command
- [ ] Eight panels, both formats, over 5 KB each
- [ ] Every panel passes `assert_accessible_axes`
- [ ] Every bar panel passes `assert_honest_bar`
- [ ] Heatmap findings printed; no leak present
- [ ] The PNG is legible in greyscale — **verified by looking, not assumed**
- [ ] `src/setu/style.py` is the only module touching global rcParams
- [ ] Layering test still green (`plots` is layer 2, `style` is layer 1)
- [ ] `./m check` green; CI green on a push
- [ ] `./m done 41` succeeded and `./m status` shows Phases 0–5 complete
