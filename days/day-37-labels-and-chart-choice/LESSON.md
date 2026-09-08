---
day: 37
phase: 5
phase_name: "Visualisation (Module 5)"
title: "Day 37 — Customising charts; choosing the right chart type"
ids: ["VIZ-02", "VIZ-03"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 24
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 37 — Customising charts; choosing the right chart type

**Phase 5 · Visualisation · Module 5** · `VIZ-02` customising: labels, ticks, legends, annotation,
saving · `VIZ-03` chart-type selection.

**The phase gate (Day 41):** an eight-chart figure pack, legible in greyscale and safe for
colour-blind readers.

> **Yesterday:** two objects — the sheet and the box — and the habit of naming both, so that nothing
> can ever draw somewhere you did not ask it to.
> **Today:** everything written on the box, and then the harder question underneath it. Labels,
> ticks, legends, annotation and the greyscale test are `VIZ-02`. Then `VIZ-03`: the flat's bar
> chart is arithmetically correct and tells the reader something false, and a box plot of the same
> four columns does not.
> **Tomorrow:** seaborn — statistical plots and faceting, and what it does to the tidy frame you
> hand it.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Somebody in the flat gets tired of arguing about the shopping and makes a chart.

Twelve weeks of receipts, four columns on the till slip — bakery, dairy, produce and household — and
a bar for each. It takes about six lines. The bars come out clean and blue and roughly the right
heights, and it looks like the sort of thing that settles an argument.

They send a screenshot to the group chat.

The first reply is: **"22 what?"**

The second is: "is that the whole twelve weeks or one week?"

The third is: "which bar is household, the third or the fourth?"

The chart is not wrong. Every bar is exactly as tall as the arithmetic says it should be. It is
simply that the person who made it already knew what the numbers were, and the picture never says.
The tallest bar is 21.64, and 21.64 could be pounds, could be items, could be a percentage, could be
a twelve-week total, could be a weekly average.

That is the first half of the day, and it is the easy half: a label, a unit, a title that states the
finding rather than restating the axes, ticks you can read, a legend in the right order, and a save
that does not cut the y label off. Every one of those is a small fix, and together they are the
difference between a picture and a chart.

The second half is not a presentation problem. Somebody fixes all of it — proper labels, pounds on
the axis, everything — and sends it again, and now the chart is beautifully readable and still says
something false.

Household and produce come out at almost the same height. About twenty-one pounds each. So the flat
agrees that produce and cleaning things cost about the same and moves on.

They do not cost about the same. Produce is around twenty-two pounds every single week, quietly.
Household is about five pounds one week and about thirty-seven the next, because the big shop for
cleaning things happens fortnightly. The average of five and thirty-seven is twenty-one, and the bar
is twenty-one, and **twenty-one is a number that never once appeared on a receipt.**

The bar chart did not lie about the arithmetic. It lied about what the arithmetic described, because
a bar of a mean quietly claims the mean describes the column. A box plot of the same four columns
gives it away instantly: three narrow boxes and one that fills the chart.

So the day has one shape running through both halves. **The first half is what a chart must say
before anybody can read it. The second half is what a chart claims whether or not you meant it to.**
And the second one is the one that ends up in a decision.

---

## §2 The map

Eight sections. Sections 1 to 5 are `VIZ-02` — the five things you write on a chart and the file you
save it to. Sections 6 and 7 are `VIZ-03` — how a reader's eye actually works, and which chart
claims what. Section 8 is where both meet the project's code.

| Section | What it means |
|---|---|
| **1.x** | **Labels** — the three strings without which a chart is a decoration |
| **2.x** | **Ticks and limits** — where the numbers on the edges come from, and the axis that lied |
| **3.x** | **Legends** — naming the series, and the legend that came from nowhere |
| **4.x** | **Annotation** — writing on the chart itself, and the two coordinate systems |
| **5.x** | **Saving for print** — the greyscale test, and getting the file out intact |
| **6.x** | **What the eye compares** — why some encodings are read and others are guessed |
| **7.x** | **Choosing the chart** — the bar that lied, the box plot that did not, and the table |
| **8.x** | **The module** — the day's rules as code, and a test that can actually go red |

### Section 1 — labels

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [The chart that never said what the numbers were](parts/01-labels/1.1-the-chart-that-never-said-what-the-numbers-were.md) | "22 what?" — and why the maker could not see it | `foundation` |
| 1.2 | [The unit the label owes you](parts/01-labels/1.2-the-unit-the-label-owes-you.md) | The three questions a y label has to answer | `working` |
| 1.3 | [A title that states the finding](parts/01-labels/1.3-a-title-that-states-the-finding.md) | Caption or finding — and which one survives being pasted | `production` |

### Section 2 — ticks and limits

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [Where the ticks go](parts/02-ticks-and-limits/2.1-where-the-ticks-go.md) | Locator and formatter — the two jobs behind one number | `foundation` |
| 2.2 | [The formatter, and the thousands separator](parts/02-ticks-and-limits/2.2-the-formatter-and-the-thousands-separator.md) | Turning `21.64` into `£21.64`, and why a draw is needed first | `working` |
| 2.3 | [The labels that overlapped](parts/02-ticks-and-limits/2.3-the-labels-that-overlapped.md) | Rotate, or use fewer ticks — measured rather than guessed | `working` |
| 2.4 | [The axis that started above zero](parts/02-ticks-and-limits/2.4-the-axis-that-started-above-zero.md) | Pixel ratio against value ratio, and the rule that follows | `production` |

### Section 3 — legends

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [The legend comes from the label](parts/03-legends/3.1-the-legend-comes-from-the-label.md) | Where the words in a legend actually come from | `foundation` |
| 3.2 | [Where the legend sits](parts/03-legends/3.2-where-the-legend-sits.md) | `loc`, `bbox_to_anchor`, and the legend that covered the data | `working` |
| 3.3 | [The series nobody could name](parts/03-legends/3.3-the-series-nobody-could-name.md) | Direct labelling, and the legend whose order was wrong | `production` |

### Section 4 — annotation

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [The one number worth writing on](parts/04-annotation/4.1-the-one-number-worth-writing-on.md) | When to label every bar, and when that ruins it | `working` |
| 4.2 | [`annotate`, and the two coordinate systems](parts/04-annotation/4.2-annotate-and-the-two-coordinate-systems.md) | Data space, axes fraction, figure fraction | `working` |
| 4.3 | [The reference line](parts/04-annotation/4.3-the-reference-line.md) | The cheapest way to turn a chart into a decision | `production` |

### Section 5 — saving for print

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [The greyscale test you can run](parts/05-saving-for-print/5.1-the-greyscale-test-you-can-run.md) | A measurement, not an opinion, about a printed chart | `working` |
| 5.2 | [Hatch and marker instead of colour](parts/05-saving-for-print/5.2-hatch-and-marker-instead-of-colour.md) | The second channel, and what it costs | `production` |
| 5.3 | [`dpi`, and the label that got cut off](parts/05-saving-for-print/5.3-dpi-and-the-label-that-got-cut-off.md) | Four saves, four pixel sizes, one missing label | `production` |

### Section 6 — what the eye compares

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [Position, length, and angle](parts/06-what-the-eye-compares/6.1-position-length-and-angle.md) | The ordering behind every chart-choice rule | `foundation` |
| 6.2 | [The pie chart question](parts/06-what-the-eye-compares/6.2-the-pie-chart-question.md) | When a pie is defensible, and the tell when it is not | `working` |

### Section 7 — choosing the chart

| Part | Title | What it answers | Level |
|---|---|---|---|
| 7.1 | [The bar that lied](parts/07-choosing-the-chart/7.1-the-bar-that-lied.md) | Twenty-one pounds, which never appeared on a receipt | `working` |
| 7.2 | [The box plot that did not](parts/07-choosing-the-chart/7.2-the-box-plot-that-did-not.md) | Box, line, whiskers, fliers — and the one tall box | `working` |
| 7.3 | [Line, scatter, and what each claims](parts/07-choosing-the-chart/7.3-line-scatter-and-what-each-claims.md) | The segment drawn across a gap that has no data | `working` |
| 7.4 | [The decision table](parts/07-choosing-the-chart/7.4-the-chart-decision-table.md) | Five questions, five charts, and what each one hides | `production` |

### Section 8 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 8.1 | [`src/setu/charts.py`](parts/08-the-module/8.1-the-charts-module.md) | Where does each of the day's rules live? | `production` |
| 8.2 | [The test that can go red](parts/08-the-module/8.2-the-test-that-can-go-red.md) | Asserting a unit, a baseline and a grey separation | `production` |

**The running example is twelve weeks of the flat's shopping** — four aisles, one seed, and a
household column that alternates between about £5 and about £37. Every part of this day picks it up,
and section 7 is where that alternation becomes the point.

---

## §3 Setup — run this

```bash
mkdir -p days/day-37-labels-and-chart-choice/lab
touch src/setu/charts.py tests/test_charts.py
uv run python -c "import matplotlib; print(matplotlib.__version__)"
```

Expected: `3.11.1`. If it prints something else, stop and log it in `docs/CHANGELOG_PLAN_DS.md`
before continuing (Principle 4, Principle 14).

**Nothing is installed today.** `matplotlib==3.11.1` arrived on Day 34 and Day 36 is the library
itself; today is what you write on it.

Confirm the one fact the second half of the day rests on — that two nearly equal bars can describe
two completely different columns:

```bash
uv run python -c "
import numpy as np
import pandas as pd


def weekly_spend() -> pd.DataFrame:
    rng = np.random.default_rng(37)
    columns = {}
    steady = [('bakery', 9.0, 1.5), ('dairy', 18.0, 2.0), ('produce', 22.0, 2.5)]
    for aisle, centre, spread in steady:
        columns[aisle] = np.round(rng.normal(centre, spread, 12), 2)
    household = np.empty(12)
    household[0::2] = rng.normal(5.0, 1.0, 6)
    household[1::2] = rng.normal(37.5, 3.0, 6)
    columns['household'] = np.round(household, 2)
    return pd.DataFrame(columns, index=pd.RangeIndex(1, 13, name='week'))


spend = weekly_spend()
print('means :', spend.mean().round(2).to_dict())
print('stdevs:', spend.std().round(2).to_dict())
print('household min/max:', spend['household'].min(), spend['household'].max())
"
```

Expected: **produce and household with almost the same mean, and wildly different spreads** — and a
household column whose minimum and maximum are nowhere near its own average. Those three lines are
[7.1](parts/07-choosing-the-chart/7.1-the-bar-that-lied.md) and
[7.2](parts/07-choosing-the-chart/7.2-the-box-plot-that-did-not.md) in advance. Record your own
numbers; the seed is fixed, so they should match this page's, and if they do not, that is worth
knowing before section 7.

Every code block in this day starts with `matplotlib.use("Agg")` before `import matplotlib.pyplot`,
for the reason [Day 36, 5.1](../day-36-figure-and-axes/parts/05-getting-it-out/5.1-backends-and-the-script-with-no-window.md)
gives. Save every image into `days/day-37-labels-and-chart-choice/lab/`.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/charts.py`** — [8.1](parts/08-the-module/8.1-the-charts-module.md) walks through the
whole module. It **imports from Day 36's `src/setu/figures.py`** rather than duplicating it, and it
fills in the `greyscale_check` stub that day deliberately left empty.

- `MIN_GREY_SEPARATION`, `PRINT_DPI` and `BAR_BASELINE` — the day's policy, as module constants.
- `ChartError(ValueError)` — for a chart that would leave the module unreadable. Import the earlier
  days' exceptions rather than inventing an eighth family.
- `label_axes(ax, *, title, xlabel, ylabel)` — **keyword-only, all three required**, and it raises
  on an empty string ([1.2](parts/01-labels/1.2-the-unit-the-label-owes-you.md), and
  [Day 10, 1.5](../day-10-functions/parts/01-the-signature/1.5-keyword-only-and-positional-only.md)).
- `money_axis(ax, axis="y")` — the `£{x:,.2f}` formatter from
  [2.2](parts/02-ticks-and-limits/2.2-the-formatter-and-the-thousands-separator.md).
- `bars(labels, values, ax=None)` — forces the baseline to zero
  ([2.4](parts/02-ticks-and-limits/2.4-the-axis-that-started-above-zero.md)) and applies hatches
  from a fixed cycle ([5.2](parts/05-saving-for-print/5.2-hatch-and-marker-instead-of-colour.md)).
- `greyscale_separation(fig)` — saves to an in-memory PNG, converts it to grey, and returns the
  smallest gap between the grey levels the series collapse to
  ([5.1](parts/05-saving-for-print/5.1-the-greyscale-test-you-can-run.md)).
- **As given, `quick_bar(series, ax=None)` passes the column name as the title and `""` as the y
  label**, so it produces exactly the chart the group chat could not read
  ([1.1](parts/01-labels/1.1-the-chart-that-never-said-what-the-numbers-were.md)).
- `TODO(me)`: fix `quick_bar` so that no chart can leave this module without a unit in its y label,
  and state that guarantee in the docstring.
- `TODO(me)`: add `spread(frame, ax=None)`, drawing the box plot beside the bar chart of means. Say
  in a comment why the two belong on one figure rather than in two files
  ([7.1](parts/07-choosing-the-chart/7.1-the-bar-that-lied.md),
  [7.2](parts/07-choosing-the-chart/7.2-the-box-plot-that-did-not.md)).
- `TODO(me)`: add `guard_series_count(n)` that refuses more series than the hatch cycle can
  distinguish. Say in a comment why that limit is a property of the encoding rather than of
  matplotlib.

**`tests/test_charts.py`** — [8.2](parts/08-the-module/8.2-the-test-that-can-go-red.md) walks
through the whole file. It builds on Day 36's approach: assert on the objects, because CI cannot see
the picture ([Day 36, 6.2](../day-36-figure-and-axes/parts/06-the-module/6.2-testing-a-chart-without-looking.md)).

- The `plt.close("all")` fixture, reused from Day 36's suite rather than rewritten.
- The five assertions that carry the day: every returned axes has a non-empty title, x label and y
  label; a money chart's y label contains `£`; a bar chart's y axis starts at zero; the grey
  separation is at least `MIN_GREY_SEPARATION`; and the tick label strings match the expected
  format after a draw.
- `pytest.raises` with `match=` on a fragment, for `ChartError` on an empty label.
- `TODO(me)`: write the tests for your fixed `quick_bar`, including one asserting that a y label
  with no unit in it is refused.
- `TODO(me)`: add a test that `greyscale_separation` **goes down** when the hatches are removed, and
  say in a comment why a test that only checks the passing case would not have caught a regression
  here.
- `TODO(me)`: break the module a **second** way of your own — not the baseline and not the hatch
  cycle. Watch what goes red, then record the change and the failure count in a `# Seen to fail:`
  comment. **If nothing goes red, that is the more interesting result** — say which test should have
  caught it and why it did not.

**`lab/the_bar_that_lied.py`** — the day's argument, made runnable.

- Build `weekly_spend()` with the day's seed, then draw two panels on one figure: the four means as
  bars, and the four columns as box plots.
- Print the four means, the four standard deviations, and household's minimum and maximum.
- Save the figure to `lab/means_and_spread.png` and print its grey separation.
- `TODO(me)`: add error bars to the bar panel and say in a comment what they fix and what they do
  not.
- `TODO(me)`: run the greyscale check on the figure with and without hatching, record both numbers,
  and say which of the two you would put in a printed report
  ([5.2](parts/05-saving-for-print/5.2-hatch-and-marker-instead-of-colour.md)).

---

## §5 The eval that must be able to fail

`tests/test_charts.py` is RED until `src/setu/charts.py` exists. Write these two first, because they
are the two that carry the day:

```python
def test_a_money_chart_says_what_the_unit_is() -> None:
    fig, axs = new_figure(1, 1)
    ax = bars(["produce", "household"], [22.04, 21.64], ax=axs[0, 0])
    money_axis(ax)
    label_axes(ax, title="Produce and household cost the same on average", xlabel="aisle", ylabel="pounds spent per week (£)")
    assert "£" in ax.get_ylabel()
    plt.close(fig)


def test_hatching_improves_greyscale_separation() -> None:
    plain = greyscale_separation(_four_series(hatched=False))
    hatched = greyscale_separation(_four_series(hatched=True))
    assert hatched > plain
    assert hatched >= MIN_GREY_SEPARATION
```

**The first test is the one that answers the group chat.** "22 what?" is a test failure, not a
matter of taste, and the assertion is one line long.

**The second test is the one nobody writes, and it is the phase gate in miniature.** A test that
only asserts the *current* figure passes the greyscale threshold goes green forever, including after
somebody removes the hatching and the four series collapse to two greys. Asserting that hatching
*improves* the number is what makes the check load-bearing
([5.2](parts/05-saving-for-print/5.2-hatch-and-marker-instead-of-colour.md)).

**The mutations to watch.** Three, and they behave differently:

1. Remove `ylim(bottom=0)` from `bars`. **One test goes red** — the baseline one — and every chart
   still draws, looks fine, and exaggerates every comparison
   ([2.4](parts/02-ticks-and-limits/2.4-the-axis-that-started-above-zero.md)).
2. Drop the hatch cycle. **A different single test goes red** — the greyscale one — and nothing
   changes on a colour screen at all, which is exactly why the check exists.
3. Make `ylabel` optional in `label_axes`. **One test goes red** — the unit one — and the
   `ChartError` test does not notice, because its fixture passes an empty string rather than
   omitting the argument.

And one that **no correctness test can catch**: lower `MIN_GREY_SEPARATION` until the current figure
passes. Every test stays green, every chart still draws, and the phase gate's greyscale criterion
now means nothing. The defences are a test asserting the constant's value and a review that treats a
threshold change as a threshold change.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed — `matplotlib`
arrived on Day 34.

The disk budget is a handful of images in `days/day-37-labels-and-chart-choice/lab/`, plus the
in-memory PNGs the greyscale check writes and discards. Section 5 saves the same figure several ways
to compare file sizes and pixel dimensions; none of them is large, and the comparison is the point.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **A number with no unit is not information**, and the person who made the chart is the one person
  who cannot see that ([1.1](parts/01-labels/1.1-the-chart-that-never-said-what-the-numbers-were.md)).
- **A y label has to answer three questions** — what is measured, in what unit, over what period —
  and answering two of them still leaves the reader guessing
  ([1.2](parts/01-labels/1.2-the-unit-the-label-owes-you.md)).
- **A title that restates the axes has said nothing**, and a title that states the finding survives
  being pasted into a document with no surrounding text
  ([1.3](parts/01-labels/1.3-a-title-that-states-the-finding.md)).
- **`set_xticks` and `set_xticklabels` as two calls can get out of step**, and the labels then attach
  to the wrong positions silently ([2.1](parts/02-ticks-and-limits/2.1-where-the-ticks-go.md)).
- **Tick label text does not exist until the figure is drawn**, so reading it back before
  `fig.canvas.draw()` returns empty strings
  ([2.2](parts/02-ticks-and-limits/2.2-the-formatter-and-the-thousands-separator.md)).
- **Rotating overlapping labels treats the symptom**, and fewer ticks usually treats the cause
  ([2.3](parts/02-ticks-and-limits/2.3-the-labels-that-overlapped.md)).
- **A bar chart with a truncated y axis exaggerates every comparison in it**, and the exaggeration
  is measurable in pixels ([2.4](parts/02-ticks-and-limits/2.4-the-axis-that-started-above-zero.md)).
- **`ax.legend()` with no labelled artist warns rather than raising**, and the warning is easy to
  miss ([3.1](parts/03-legends/3.1-the-legend-comes-from-the-label.md)).
- **A legend can cover the data it is describing**, and the default position does not know where
  your data is ([3.2](parts/03-legends/3.2-where-the-legend-sits.md)).
- **A legend whose order does not match the drawing order maps the wrong name to the wrong series**
  ([3.3](parts/03-legends/3.3-the-series-nobody-could-name.md)).
- **Labelling every value on a busy chart hides the finding among the data**
  ([4.1](parts/04-annotation/4.1-the-one-number-worth-writing-on.md)).
- **An annotation placed in data coordinates moves when the limits change**, and one placed in axes
  fraction does not ([4.2](parts/04-annotation/4.2-annotate-and-the-two-coordinate-systems.md)).
- **A hard-coded reference line ages**, because the mean, the target or the threshold it drew moves
  with the data ([4.3](parts/04-annotation/4.3-the-reference-line.md)).
- **Four distinguishable colours can become two greys when printed**, and nothing on screen tells
  you ([5.1](parts/05-saving-for-print/5.1-the-greyscale-test-you-can-run.md)).
- **Hatching is ugly at small sizes and expensive in vector output**, which is a real cost rather
  than a reason not to use it
  ([5.2](parts/05-saving-for-print/5.2-hatch-and-marker-instead-of-colour.md)).
- **`bbox_inches="tight"` makes the saved figure's size unpredictable**, so a pack of figures saved
  that way is no longer consistent
  ([5.3](parts/05-saving-for-print/5.3-dpi-and-the-label-that-got-cut-off.md)).
- **The eye reads position accurately, length well, and angle badly**, which is the whole reason the
  chart-choice rules exist ([6.1](parts/06-what-the-eye-compares/6.1-position-length-and-angle.md)).
- **A pie chart whose labels are doing all the work is a table wearing a circle**
  ([6.2](parts/06-what-the-eye-compares/6.2-the-pie-chart-question.md)).
- **A bar of a mean claims the mean describes the column**, and error bars help without fixing it
  ([7.1](parts/07-choosing-the-chart/7.1-the-bar-that-lied.md)).
- **A box plot cannot show two clumps as two clumps**, so it is honest about spread and quiet about
  shape ([7.2](parts/07-choosing-the-chart/7.2-the-box-plot-that-did-not.md)).
- **A line chart over a gappy index draws a straight segment across the gap**, inventing data that
  was never measured ([7.3](parts/07-choosing-the-chart/7.3-line-scatter-and-what-each-claims.md)).

**The pattern behind the day.** Sections 1 to 5's failures make a chart **hard to read**, and every
one of them is visible to anybody who looks. Sections 6 and 7's failures make a chart **easy to read
and wrong**, and none of them is visible at all — the bars are the right height, the labels are
correct, the file saves cleanly, and the conclusion is false. That asymmetry is why the module
forces a unit into every label, pins the bar baseline to zero, measures the grey separation instead
of trusting the palette, and why the decision table in
[7.4](parts/07-choosing-the-chart/7.4-the-chart-decision-table.md) names, for every chart, the thing
it hides.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Text in matplotlib** — <https://matplotlib.org/stable/users/explain/text/text_intro.html> —
  titles, axis labels, and the objects each of them is.
- **Tick locators and formatters** —
  <https://matplotlib.org/stable/gallery/ticks/tick-locators.html> and
  <https://matplotlib.org/stable/gallery/ticks/tick-formatters.html> — the two jobs
  [2.1](parts/02-ticks-and-limits/2.1-where-the-ticks-go.md) separates, with every built-in listed.
- **Legend guide** — <https://matplotlib.org/stable/users/explain/axes/legend_guide.html> — where
  handles and labels come from, and what `loc` and `bbox_to_anchor` do together.
- **Annotations** — <https://matplotlib.org/stable/users/explain/text/annotations.html> — read the
  table of `xycoords` values for yourself.
- **`Axes.boxplot`** —
  <https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html> — confirm what the
  whiskers default to before you explain them to anyone.
- **Choosing colormaps** — <https://matplotlib.org/stable/users/explain/colors/colormaps.html> — the
  library's own section on perceptual uniformity and greyscale conversion.

---

## §9 Say it in an interview

> There are two separate jobs in "make this chart better", and I keep them separate because only one
> of them is a matter of taste. The first is making it readable: a y label that says what is
> measured, in what unit, over what period; a title that states the finding rather than restating
> the axes; ticks formatted the way the reader thinks about the number; a legend in the same order
> as the series; and a save that does not crop the label off. Those are cheap, and I put the
> important ones in code rather than in a review checklist — the function that labels a chart takes
> title, xlabel and ylabel as required keyword-only arguments and raises on an empty string, so a
> chart that does not say what its numbers are cannot leave the module.
>
> The one in that list that is not cosmetic is the axis baseline. A bar chart encodes a value as a
> length, so if the axis starts above zero the lengths no longer stand in the right ratio — two
> numbers a few per cent apart can be drawn as a landslide, and you can measure the exaggeration in
> pixels. A line chart encodes position rather than length, so it does not have to start at zero.
> That is a testable rule, so it is a test: every bar chart the module produces has its lower y
> limit asserted to be zero.
>
> The second job is chart choice, and that is where the real errors live, because the failure mode
> is a chart that is perfectly readable and still wrong. The example I use is four columns of weekly
> spending where two of them have almost the same mean: one is steady at about twenty-two every
> week, and the other alternates between about five and about thirty-seven because the big shop
> happens fortnightly. Their means are within a pound of each other, so the bar chart says they cost
> the same, and the average of the second one is a number that never appeared on a single receipt. A
> bar of a mean quietly claims the mean describes the column. A box plot of the same four columns
> shows it immediately — three narrow boxes and one that fills the chart. Error bars help and do not
> fix it, because they are still a summary.
>
> The other thing I would mention is accessibility, because it is checkable rather than aspirational.
> Four series distinguished only by colour can collapse to two greys when the chart is printed or
> read by someone with the commoner kinds of colour blindness. So I add a second channel — hatching
> on bars, line style and markers on lines — and I test it: render the figure to an image, convert
> it to grey, and assert the separation between the series' grey levels. The test that matters is
> not "the current figure passes the threshold", because that goes green forever; it is "hatching
> improves the separation", which goes red the day somebody removes it.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 37` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
