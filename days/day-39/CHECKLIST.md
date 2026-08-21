# Day 39 — CHECKLIST

**IDs covered:** VIZ-05, VIZ-06 · **Principles served:** 1, 7, 8

## Demo command

```bash
uv run python days/day-39/lab/distributions.py
uv run python -m pytest tests/test_plots.py -v
```

Expected: the ten-part report ending with the pairplot panel count, then all plot tests green.

## Setup

- [ ] `./m start 39` and `./m scaffold 39` run
- [ ] `days/day-39/lab/distributions.py` created
- [ ] No new packages installed

## VIZ-05 — distributions

- [ ] Ran `bin_width_changes_the_story()` and **looked at all four panels**
- [ ] Confirmed `bins=3` hides the bimodality entirely
- [ ] Used `np.histogram_bin_edges(..., bins="fd")` and know what it computes from
- [ ] Ran `four_views_of_the_same_data()`
- [ ] Confirmed the **box plot cannot show two modes** — its one serious blind spot
- [ ] Ran `kde_invents_density()` and saw the KDE extend below zero on count data
- [ ] Ran `log_scale_for_skew()`; used **log bins**, not just a log axis
- [ ] Ran `ecdf_has_no_bins()`; can say why an ECDF has nothing to tune
- [ ] Filled in the five-row table from §1 from memory

## VIZ-06 — relationships

- [ ] Ran `scatter_and_overplotting()`; can name two fixes and one non-fix
- [ ] Ran `the_correlation_heatmap()` and found **all three planted problems** before the printout
- [ ] Identified which is leakage and which is multicollinearity
- [ ] Can explain how `citations_per_page` is built and why that makes it a leak
- [ ] Read `why_the_mask_and_the_colormap_matter()` and can justify each of the five settings
- [ ] Ran `correlation_is_only_linear()`; saw r ≈ 0 for a perfect parabola
- [ ] Ran `pairplot_is_for_exploring()`; noted it is figure-level (Day 38)

## Build brief

- [ ] `distribution` — **TODO(me)**: five kinds, `fd` bins, log-x does both, n and bins in the title
- [ ] `correlation_heatmap` — **TODO(me)**: masked, diverging, fixed limits, returns `findings`
- [ ] `assert_no_leaky_features` — **TODO(me)**: names every offender **and** the diagnostic question
- [ ] `scatter` — **TODO(me)**: auto-hexbin above 5000, reports r when a trend is drawn
- [ ] Can explain why the leak check is an assertion rather than a habit

## Tests that must be able to fail

- [ ] `test_distribution_title_reports_n_and_bins` — green
- [ ] `test_distribution_supports_every_kind` — five green cases
- [ ] `test_distribution_rejects_an_unknown_kind` / `..._tiny_sample` — green
- [ ] `test_log_x_sets_both_scale_and_bins` — green
- [ ] `test_log_x_rejects_non_positive_values` — green
- [ ] `test_heatmap_uses_a_fixed_symmetric_scale` — green
- [ ] **Removed `vmin`/`vmax`, watched it go red, restored them** ← do not skip
- [ ] `test_heatmap_finds_the_leak` — green ← **today's real assessment**
- [ ] **Lowered the threshold so everything was flagged, watched the `noise` assertion go red, fixed it** ← do not skip
- [ ] `test_heatmap_finds_collinear_features` — green
- [ ] `test_heatmap_findings_without_a_target` — green
- [ ] `test_heatmap_findings_are_json_serialisable` — green
- [ ] `test_heatmap_drops_non_numeric_columns` — green
- [ ] `test_heatmap_needs_two_numeric_columns` — green
- [ ] `test_assert_no_leaky_features_raises_and_names_everything` — green
- [ ] `test_assert_no_leaky_features_passes_clean_data` — green
- [ ] `test_scatter_switches_to_hexbin_above_the_threshold` — green
- [ ] `test_scatter_with_trend_reports_r` — green
- [ ] `test_scatter_rejects_non_numeric` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] Name each distribution chart's blind spot
- [ ] Why does a histogram's message depend on a parameter you chose?
- [ ] Why is a KDE wrong for count data?
- [ ] What is an ECDF, and why is it the most honest distribution chart?
- [ ] Why must a correlation heatmap use a diverging colormap and fixed limits?
- [ ] Explain the difference between a leak and multicollinearity, using the two you found
- [ ] Why is `r ≈ 0.97` with the target a warning rather than good news?
- [ ] Why is the heatmap a screen and not a verdict?

## Commit

- [ ] `./m check && ./m done 39` succeeded
