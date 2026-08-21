# Day 40 — CHECKLIST

**IDs covered:** VIZ-07 · **Principles served:** 1, 4, 7, 10

## Demo command

```bash
uv run python days/day-40/lab/styling.py
uv run python -m pytest tests/test_style.py -v
```

Expected: the seven-part styling report including measured luminance gaps, then all style tests green.

## Setup

- [ ] `./m start 40` and `./m scaffold 40` run
- [ ] Files created: `days/day-40/lab/styling.py`, `src/setu/style.py`, `tests/test_style.py`
- [ ] No new packages installed

## VIZ-07 — the constraints

- [ ] Can state the two accessibility constraints and roughly who they affect
- [ ] Can state the single rule that solves both
- [ ] Ran `rcparams_are_global()` and saw a global change affect a later figure
- [ ] Used `plt.rc_context` and confirmed it restores on exit
- [ ] Can name the three palette kinds and what each is for
- [ ] Can say what goes wrong when you mismatch palette kind to data kind

## Measuring, not guessing

- [ ] Ran `greyscale_test()` and recorded the smallest luminance gap per palette
- [ ] Can explain why the luminance formula weights green most heavily
- [ ] Ran `colour_alone_is_not_enough()` and compared both panels
- [ ] Used `markevery` so markers identify rather than obscure
- [ ] Ran `perceptually_uniform_colormaps()`
- [ ] Can say **two** specific things wrong with `jet`
- [ ] Ran `emphasis_by_desaturation()`; can state the "colour is scarce" rule
- [ ] Know the minimum text sizes for a projected chart

## Build brief

- [ ] `src/setu/style.py` created with `PALETTE` (Wong), `SEQUENTIAL`, `DIVERGING`, `BANNED_COLORMAPS`
- [ ] `apply_house_style` — **TODO(me)**: called once, from the entry point only
- [ ] `style_context` — **TODO(me)**: scoped `rc_context`
- [ ] `luminance` — **TODO(me)**
- [ ] `assert_greyscale_legible` — **TODO(me)**: names both colours and the gap
- [ ] `assert_accessible_axes` — **TODO(me)**: colour-only series and banned colormaps, all problems at once
- [ ] `distinct_styles` — **TODO(me)**: colour + linestyle + marker, refuses above 12
- [ ] **No plotting function calls `apply_house_style`**

## Tests that must be able to fail

- [ ] `test_luminance_matches_known_values` — green
- [ ] **Swapped the R and B coefficients, watched the green/blue assertion go red, fixed it** ← do not skip
- [ ] `test_palette_is_greyscale_legible` — green
- [ ] `test_greyscale_check_rejects_two_similar_colours` — green
- [ ] `test_greyscale_check_names_the_gap` — green
- [ ] `test_palette_has_at_least_eight_colours` — green
- [ ] `test_style_context_is_scoped` — green
- [ ] `test_style_context_restores_on_exception` — green
- [ ] **Replaced `rc_context` with direct assignment, watched both scoping tests go red, reverted** ← do not skip
- [ ] `test_distinct_styles_are_mutually_distinguishable` — green
- [ ] `test_distinct_styles_vary_more_than_colour` — green
- [ ] `test_distinct_styles_refuses_an_unreadable_count` — green
- [ ] `test_accessible_axes_passes_a_styled_chart` — green
- [ ] `test_accessible_axes_rejects_colour_only` — green ← **today's real assessment**
- [ ] `test_accessible_axes_allows_a_single_series` — green
- [ ] `test_accessible_axes_rejects_banned_colormaps` — five green cases
- [ ] `test_accessible_axes_accepts_viridis` — green
- [ ] `test_accessible_axes_reports_every_problem` — green
- [ ] `test_no_global_style_calls_in_src` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What are the two accessibility constraints, and what single rule addresses both?
- [ ] Why is red-versus-green the worst possible pairing?
- [ ] Why must a library function never call `sns.set_theme()`?
- [ ] What does `rc_context` guarantee that direct assignment does not?
- [ ] Name the three palette kinds and a use for each
- [ ] Why are two colours with equal luminance a problem?
- [ ] Give two concrete reasons `jet` distorts data
- [ ] Why grey the context and accent one series, rather than use eight colours?

## Commit

- [ ] `./m check && ./m done 40` succeeded
