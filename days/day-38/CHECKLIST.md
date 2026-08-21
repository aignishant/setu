# Day 38 — CHECKLIST

**IDs covered:** VIZ-04 · **Principles served:** 1, 2, 7

## Demo command

```bash
uv run python days/day-38/lab/seaborn_api.py
uv run python -m pytest tests/test_plots.py -v
```

Expected: the seven-part Seaborn report, then all plot tests green with no leaked figures.

## Setup

- [ ] `./m start 38` and `./m scaffold 38` run
- [ ] `uv add "seaborn==<your pin>"` — exact-pinned, drift logged
- [ ] `days/day-38/lab/seaborn_api.py` created

## VIZ-04 — the two APIs

- [ ] Ran `axes_level_composes()` and confirmed `returned is axes[0]`
- [ ] Ran `figure_level_does_not()` and saw a `FacetGrid` with its **own** figure
- [ ] Can name three axes-level and three figure-level functions from memory
- [ ] Can state the rule this project adopts, and why

## Statistical transforms

- [ ] Ran `the_statistical_transform()` and counted the error-bar artists
- [ ] Can say what `errorbar=("ci", 95)` computes, and which earlier day you built it on
- [ ] Can state the difference between a CI and an SD in one sentence
- [ ] Used `hue=` for a second categorical
- [ ] Used `order=` explicitly, and know what happens without it
- [ ] Ran `long_form_is_required()`; can say which Day-32 function reshapes for Seaborn
- [ ] Used `regplot` and can say what statistical claim it makes

## Faceting

- [ ] Ran `faceting_by_hand()` with `sharey=True`
- [ ] Can explain what goes wrong **without** shared limits
- [ ] Used `zip(..., strict=True)`

## Build brief

- [ ] `facet` — **TODO(me)**: axes-level `plot_fn`, shared limits by default, n in titles, panel cap, hides unused
- [ ] `grouped_box` — **TODO(me)**: box + strip overlay, n on tick labels, rejects tiny categories
- [ ] `mean_with_ci` — **TODO(me)**: calls `assert_honest_bar`, labels the error measure
- [ ] Can explain why `facet` **raises** above 12 panels instead of drawing them

## Tests that must be able to fail

- [ ] `test_facet_makes_one_panel_per_group` — green
- [ ] `test_facet_titles_include_n` — green
- [ ] `test_facet_shares_limits_by_default` — green ← **today's real assessment**
- [ ] **Set `sharey=False` internally, watched the limits diverge and the test go red, fixed it** ← do not skip
- [ ] `test_facet_can_unshare_when_asked` — green
- [ ] `test_facet_refuses_too_many_panels` — green (the count appears in the message)
- [ ] `test_facet_hides_unused_panels` — green
- [ ] `test_facet_respects_ordered_categorical` — green
- [ ] **Sorted groups alphabetically, saw `high, low, medium`, fixed it** ← do not skip
- [ ] `test_grouped_box_overlays_the_raw_points` — green
- [ ] `test_grouped_box_annotates_n` — green
- [ ] `test_grouped_box_rejects_a_tiny_category` — green
- [ ] `test_mean_with_ci_draws_error_bars` — green
- [ ] `test_mean_with_ci_axis_includes_zero` — green (Day 37's lint, running automatically)
- [ ] `test_mean_with_ci_label_names_the_error_measure` — green
- [ ] `test_mean_with_ci_rejects_an_unknown_error` — green
- [ ] `test_no_figure_level_seaborn_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What is the difference between an axes-level and a figure-level Seaborn function?
- [ ] Why does that difference decide whether a chart can go in a figure pack?
- [ ] What does `sns.barplot` compute that a plain bar chart does not?
- [ ] CI, SD, SE — what does each describe, and why must the label say which?
- [ ] Why does Seaborn need long-form data?
- [ ] What goes wrong when facet panels autoscale independently?
- [ ] What statistical assumption does `regplot` make?
- [ ] Why does `grouped_box` overlay the raw points?

## Commit

- [ ] `./m check && ./m done 38` succeeded
