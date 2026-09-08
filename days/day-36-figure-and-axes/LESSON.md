---
day: 36
phase: 5
phase_name: "Visualisation (Module 5)"
title: "Day 36 — Matplotlib: figure, axes, and the object API"
ids: ["VIZ-01"]
principles: ["P1 build daily", "P2 from scratch before library", "P3 one concept one day", "P4 pin everything", "P5 zero budget", "P6 the notebook is a scratchpad", "P7 evals before features", "P10 interview-ready artifacts", "P16 depth over density", "P17 no clocks", "P18 zero to production", "P20 plain language"]
kind: lab
plan: setu
plan_version: "v2.3.0"
parts: 21
generated: "2026-09-08"
status: not-started
lab_scaffolded: false
commit: ""
---

# Day 36 — Matplotlib: figure, axes, and the object API

**Phase 5 · Visualisation · Module 5** · `VIZ-01` matplotlib: the figure, the axes, and the object
API.

**The phase gate (Day 41):** an eight-chart figure pack, legible in greyscale and safe for
colour-blind readers.

> **Yesterday:** the phase closed. Where pandas stops, what Polars and DuckDB do instead, one
> benchmark careful enough to claim something, and the five criteria the dataset had to pass.
> **Today:** a new phase and a different kind of output. Two objects — the sheet of paper and the box
> drawn on it — and the reason every chart in this project will be built by naming them rather than
> by letting a module guess which one you meant.
> **Tomorrow:** the same two objects, but everything written on them — labels, ticks, legends,
> annotation — and the question of which chart type was honest in the first place.

> **Read this hub first**, then work through `parts/` in order. No time estimate here or anywhere — a
> day is a unit of subject, not of hours (Principle 17).

---

## §1 The story

Four people share a flat and they have been keeping the shopping receipts for a month. Somebody
finally types the numbers up. Four aisles, four weeks:

```text
aisle        week 1   week 2   week 3   week 4    total
dairy          4.60     5.75     4.60     6.90    21.85
bakery         2.80     1.40     2.80     2.80     9.80
produce        6.30     7.10     5.40     8.20    27.00
household      3.50     0.00     9.20     1.10    13.80
every week    17.20    14.25    22.00    19.00    72.45
```

Twenty numbers. Somebody says: put that on the fridge so we can all see it.

So they get out a sheet of paper. They draw a box on the sheet, and inside the box they draw four
bars — one per aisle, tallest for produce. Then they draw a second box underneath, and inside that
one a line going up and down for the four weekly totals.

At the end there is one sheet of paper, with two boxes on it, and something drawn inside each box.

Now notice what happened while the pen was moving. Nobody labelled *the sheet of paper*. The words
"pounds spent" went next to a box. The tick marks went along the edge of a box. The little heading
"what each aisle cost" went above a box. The sheet did exactly two jobs: it decided how big the
picture was, and it held the boxes.

That is the whole idea, and it is the reason this day exists as its own day.

Because there is a way of drawing with this library where you never mention the sheet or the box.
You say "draw bars", and something appears. It works. It keeps working right up until the moment
there are two sheets on the fridge and you write on "the sheet" — and the writing lands on the one
you were not looking at. That failure does not look like a bug. It looks like a chart that came out
with somebody else's title on it, in a test that passes when it runs alone and fails when the whole
suite runs, in an order nobody chose.

So the day is one sentence long, and the rest of it is why. **Name the sheet and name the box, every
time, and nothing can ever draw somewhere you did not ask it to.**

---

## §2 The map

Six sections, all of them `VIZ-01`. The first three build the mental model and the habit; the last
three are what makes it survive a real figure and a real test suite.

| Section | What it means |
|---|---|
| **1.x** | **The two objects** — figure, axes, axis, and the artists on them |
| **2.x** | **The state machine** — the `plt.` interface, and exactly where it stops working |
| **3.x** | **The object API** — `fig, ax = plt.subplots()`, and everything you do with that `ax` |
| **4.x** | **Many axes** — more than one panel on one sheet |
| **5.x** | **Getting it out** — backends, saving, and the figures nobody closed |
| **6.x** | **The module** — the day's rules as code, and a chart tested without looking at it |

### Section 1 — the two objects

| Part | Title | What it answers | Level |
|---|---|---|---|
| 1.1 | [The paper and the frame drawn on it](parts/01-the-two-objects/1.1-the-paper-and-the-frame.md) | What a figure is, what an axes is, and which one you label | `foundation` |
| 1.2 | [Axes, axis, and the word everybody trips on](parts/01-the-two-objects/1.2-axes-is-not-axis.md) | One letter, two completely different objects | `foundation` |
| 1.3 | [Everything you can see is an artist](parts/01-the-two-objects/1.3-everything-is-an-artist.md) | Why every drawn thing has a `get_`/`set_` pair | `foundation` |

### Section 2 — the state machine

| Part | Title | What it answers | Level |
|---|---|---|---|
| 2.1 | [The figure you never named](parts/02-the-state-machine/2.1-the-figure-you-never-named.md) | Where the figure came from when you did not make one | `foundation` |
| 2.2 | [`gca`, and the axes you did not choose](parts/02-the-state-machine/2.2-gca-and-the-axes-you-did-not-choose.md) | The current figure is a global variable in a module | `working` |
| 2.3 | [Where `plt.plot` stops working](parts/02-the-state-machine/2.3-where-plt-plot-stops-working.md) | Four places it breaks, and the rule that replaces it | `production` |

### Section 3 — the object API

| Part | Title | What it answers | Level |
|---|---|---|---|
| 3.1 | [`fig, ax = plt.subplots()`](parts/03-the-object-api/3.1-fig-ax-subplots.md) | The one line the whole project starts every chart with | `foundation` |
| 3.2 | [Drawing on an axes](parts/03-the-object-api/3.2-drawing-on-an-axes.md) | `bar`, `plot`, `scatter` — and why the return value matters | `working` |
| 3.3 | [The setter names, and how to find one](parts/03-the-object-api/3.3-the-setter-names.md) | Finding a method you do not know, without searching the web | `working` |
| 3.4 | [`ax.set` — the one-call form](parts/03-the-object-api/3.4-ax-set-the-one-call-form.md) | Four lines into one, and what it cannot do | `working` |
| 3.5 | [The `ax` parameter](parts/03-the-object-api/3.5-the-ax-parameter.md) | The signature every drawing function in this project has | `production` |

### Section 4 — many axes

| Part | Title | What it answers | Level |
|---|---|---|---|
| 4.1 | [A grid of axes](parts/04-many-axes/4.1-a-grid-of-axes.md) | `subplots(2, 2)` gives an array, and its shape surprises people | `working` |
| 4.2 | [The axes you forgot to use](parts/04-many-axes/4.2-the-axes-you-forgot-to-use.md) | The empty panel, and why the grid shape is a decision | `working` |
| 4.3 | [Shared axes, and the comparison that becomes possible](parts/04-many-axes/4.3-shared-axes.md) | Four panels with four different y ranges is four charts, not one | `production` |
| 4.4 | [Constrained layout, and the label that overlapped](parts/04-many-axes/4.4-constrained-layout.md) | Three layout settings, measured rather than eyeballed | `production` |

### Section 5 — getting it out

| Part | Title | What it answers | Level |
|---|---|---|---|
| 5.1 | [Backends, and the script with no window](parts/05-getting-it-out/5.1-backends-and-the-script-with-no-window.md) | Why `Agg` comes before `import pyplot`, and what CI needs | `working` |
| 5.2 | [`savefig`, `dpi`, and `bbox_inches`](parts/05-getting-it-out/5.2-savefig-dpi-and-bbox-inches.md) | The same figure saved four ways, in bytes and in pixels | `working` |
| 5.3 | [Vector or raster — which file to write](parts/05-getting-it-out/5.3-vector-or-raster.md) | PNG, SVG, PDF — what scales, what does not, what it costs | `production` |
| 5.4 | [The figures you never closed](parts/05-getting-it-out/5.4-the-figures-you-never-closed.md) | The warning after twenty, and the memory after two hundred | `production` |

### Section 6 — the module

| Part | Title | What it answers | Level |
|---|---|---|---|
| 6.1 | [`src/setu/figures.py`](parts/06-the-module/6.1-the-figures-module.md) | Where does each of the day's rules live? | `production` |
| 6.2 | [Testing a chart without looking](parts/06-the-module/6.2-testing-a-chart-without-looking.md) | Asserting on objects, because CI cannot see the picture | `production` |

**The running example is the flat's fridge chart** — four aisles, four weeks, twenty numbers, drawn
as two panels on one sheet. Every part of this day picks it up.

---

## §3 Setup — run this

```bash
mkdir -p days/day-36-figure-and-axes/lab
touch src/setu/figures.py tests/test_figures.py
uv run python -c "import matplotlib; print(matplotlib.__version__, matplotlib.get_backend())"
```

Expected: `3.11.1` and whatever backend your machine reports. If the version prints something else,
stop and log it in `docs/CHANGELOG_PLAN_DS.md` before continuing (Principle 4, Principle 14).

**Nothing is installed today.** `matplotlib==3.11.1` arrived on Day 34, for `DataFrame.plot`
([Day 34, 6.5](../day-34-categories-and-describe/parts/06-the-quality-report/6.5-built-in-plotting-the-fastest-look.md)).
Today is the library itself rather than pandas' wrapper over it.

Confirm the two facts the whole day rests on — the sheet holds boxes, and the boxes are what you
write on:

```bash
uv run python -c "
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(6, 4))
print('a bare figure holds :', fig.axes)
ax = fig.add_subplot()
print('after add_subplot   :', fig.axes)
print('the figure has a title method:', hasattr(fig, 'suptitle'))
print('the axes has one too         :', hasattr(ax, 'set_title'))
ax.bar(['dairy', 'bakery', 'produce', 'household'], [21.85, 9.80, 27.00, 13.80])
print('artists on the axes :', len(ax.containers[0]), 'bars')
print('x tick labels       :', [t.get_text() for t in ax.get_xticklabels()])
plt.close(fig)
"
```

Expected: an empty list, then a list with one axes in it, then four bars and four aisle names. **The
figure started with nothing on it**, which is the sentence section 1 is built on
([1.1](parts/01-the-two-objects/1.1-the-paper-and-the-frame.md)).

Every code block in this day starts with `matplotlib.use("Agg")` before `import matplotlib.pyplot`.
[5.1](parts/05-getting-it-out/5.1-backends-and-the-script-with-no-window.md) is where that stops
being a ritual and becomes a reason.

One warning about section 5: [5.4](parts/05-getting-it-out/5.4-the-figures-you-never-closed.md)
deliberately opens hundreds of figures to make the leak measurable. Save every image the day
produces into `days/day-36-figure-and-axes/lab/`, and keep them out of the commit unless the
checklist asks for one.

---

## §4 Build brief

**One module, one test file, one lab script.** The parts explain every line; none of them does your
reps.

**`src/setu/figures.py`** — [6.1](parts/06-the-module/6.1-the-figures-module.md) walks through the
whole module. Day 37 will import from it, so its shape is a decision that lasts the phase.

- `FIGSIZE`, `DPI` and `BACKEND` — the day's policy, pinned as module constants (Principle 4).
- `FigureError(ValueError)` — for a figure that leaves the module in a state the phase gate would
  reject. Import the earlier days' exceptions rather than inventing a seventh family.
- `new_figure(rows, cols, **kwargs)` — always `squeeze=False` and always `layout="constrained"`, so
  the caller's indexing never depends on the grid's shape
  ([4.1](parts/04-many-axes/4.1-a-grid-of-axes.md),
  [4.4](parts/04-many-axes/4.4-constrained-layout.md)).
- `spend_by_aisle(spend, ax=None) -> Axes` — the flat's bar chart, following the `ax=None` contract
  from [3.5](parts/03-the-object-api/3.5-the-ax-parameter.md) and returning the axes.
- `weekly_total(weeks, totals, ax=None) -> Axes` — the second panel, same contract.
- `save(fig, path, dpi=DPI) -> Path` — saves, **closes the figure**, and returns the path
  ([5.4](parts/05-getting-it-out/5.4-the-figures-you-never-closed.md)).
- **As given, `quick_look(frame)` calls `plt.bar` and closes nothing**, so it draws onto whichever
  axes happens to be current and leaks a figure per call
  ([2.3](parts/02-the-state-machine/2.3-where-plt-plot-stops-working.md)).
- `TODO(me)`: fix `quick_look`. Make it take and return an axes, leak nothing, and state in the
  docstring what is guaranteed about the figure count after it returns.
- `TODO(me)`: add `panel_pack(charts, rows, cols)` that assembles the phase gate's eight-chart
  figure and **refuses** a grid too small for the charts given. Say in a comment why refusing beats
  silently dropping the last one.
- `TODO(me)`: add a `greyscale_check(fig)` stub that Day 37 will fill in. Leave the body raising
  `NotImplementedError`, and write in a comment exactly what it will have to measure and why a
  colour name is not enough.

**`tests/test_figures.py`** — [6.2](parts/06-the-module/6.2-testing-a-chart-without-looking.md)
walks through the whole file. Nobody can look at the picture in CI, so every assertion is on an
object.

- A fixture that closes every figure after each test, and a test that proves the fixture works.
- The five assertions that carry the day: the title, x label and y label are non-empty; the bar
  heights equal the data that went in; the panel count equals the grid asked for; a bar chart's y
  axis starts at zero; and the file `save` wrote exists and is non-empty.
- `pytest.raises` with `match=` on a fragment, for `FigureError`.
- `TODO(me)`: write the tests for your fixed `quick_look`, including one that asserts the open
  figure count is unchanged after calling it fifty times.
- `TODO(me)`: add a test that `new_figure(1, 1)` and `new_figure(2, 3)` both return an array of the
  same number of dimensions, and say in a comment which bug that catches.
- `TODO(me)`: break the module a **second** way of your own — not the label removal and not the
  `squeeze`. Watch what goes red, then record the change and the failure count in a
  `# Seen to fail:` comment. **If nothing goes red, that is the more interesting result** — say
  which test should have caught it and why it did not.

**`lab/the_fridge_chart.py`** — the day's picture, made runnable.

- Build the two-panel fridge chart from the module's functions and save it to `lab/fridge.png`.
- Print the panel count, both panels' y limits, and the saved file's size in bytes.
- `TODO(me)`: draw the same two panels with `sharey=True` and without, save both, and record which
  aisle looks different between them. Say in a comment which version you would put on the fridge
  ([4.3](parts/04-many-axes/4.3-shared-axes.md)).
- `TODO(me)`: save the figure as PNG, SVG and PDF, record the three file sizes, and say in a comment
  which one you would attach to an email and which one you would send to a print shop
  ([5.3](parts/05-getting-it-out/5.3-vector-or-raster.md)).

---

## §5 The eval that must be able to fail

`tests/test_figures.py` is RED until `src/setu/figures.py` exists. Write these two first, because
they are the two that carry the day:

```python
def test_every_chart_is_labelled() -> None:
    fig, axs = new_figure(1, 1)
    ax = spend_by_aisle({"dairy": 21.85, "bakery": 9.80}, ax=axs[0, 0])
    assert ax.get_title(), "a chart with no title is a decoration"
    assert ax.get_xlabel()
    assert ax.get_ylabel()
    plt.close(fig)


def test_a_bar_chart_starts_at_zero() -> None:
    fig, axs = new_figure(1, 1)
    ax = spend_by_aisle({"dairy": 21.85, "bakery": 21.40}, ax=axs[0, 0])
    assert ax.get_ylim()[0] == 0
    plt.close(fig)
```

**The first test is the one that makes the phase gate possible.** Eight charts that each need a
human to check they are labelled is not a gate; one assertion that runs on all eight is.

**The second test is the one nobody writes, and it is a correctness test rather than a style one.**
A bar chart encodes a value as a length, so an axis that does not start at zero makes two nearly
equal numbers look like a landslide. Tomorrow's
[Day 37, 2.4](../day-37-labels-and-chart-choice/parts/02-ticks-and-limits/2.4-the-axis-that-started-above-zero.md)
measures exactly how much of a landslide. Delete this test and that distortion ships.

**The mutations to watch.** Three, and they behave differently:

1. Drop the `set_ylabel` call in `spend_by_aisle`. **One test goes red** — the labelling one — and
   the picture still looks fine, which is the point.
2. Return the figure instead of the axes from `spend_by_aisle`. **A different single test goes red**,
   and it is not an obvious one: everything still draws, and the failure is an `AttributeError`
   several lines later.
3. Remove `squeeze=False` from `new_figure`. **One test goes red** — the grid-shape one — and only
   for the `1, 1` case, because every other shape is unaffected.

And one that **no correctness test can catch**: change `FIGSIZE` from `(6, 4)` to `(3, 2)`. Every
test stays green, every chart still draws, and every label in the phase's figure pack is now too
small to read. The defences are a test asserting the constant's value and a review that treats a
figure size as part of the output rather than as a detail.

**Green is not the finish.** A suite whose failures nobody has watched is a suite nobody has checked
([Day 2, 3.1](../day-02-quality-gate/parts/03-pytest/3.1-the-test-that-can-go-red.md)).

---

## §6 Request budget

**Zero.** No model calls, no API keys, no network at run time, nothing installed — `matplotlib`
arrived on Day 34.

The disk budget is a handful of images in `days/day-36-figure-and-axes/lab/`, none of them larger
than a few hundred kilobytes. The one deliberately expensive block is
[5.4](parts/05-getting-it-out/5.4-the-figures-you-never-closed.md), which opens hundreds of figures
in a loop to make the leak measurable; it releases the memory when the process ends, and the point
of the exercise is watching it not release it before then.

The documentation URLs in §8 are the only network the day asks for, and they are read rather than
called.

---

## §7 Traps

- **You label the box, not the sheet.** `fig.suptitle` and `ax.set_title` are different objects'
  methods and land in different places
  ([1.1](parts/01-the-two-objects/1.1-the-paper-and-the-frame.md)).
- **"Axes" is one panel and "axis" is one edge of it**, and the plural of the second is spelled the
  same as the first ([1.2](parts/01-the-two-objects/1.2-axes-is-not-axis.md)).
- **`ax.set_xaxis(...)` does not exist**, and Python's suggestion for the typo points at a getter
  that will not help ([1.2](parts/01-the-two-objects/1.2-axes-is-not-axis.md)).
- **`plt.bar` creates a figure and an axes behind your back**, so a script that never makes one
  still has one ([2.1](parts/02-the-state-machine/2.1-the-figure-you-never-named.md)).
- **The current figure is a global variable**, so a title can land on a figure you are not looking
  at ([2.2](parts/02-the-state-machine/2.2-gca-and-the-axes-you-did-not-choose.md)).
- **Under `pytest`, test order decides which figure is current**, so a state-machine chart makes a
  suite that passes alone and fails together
  ([2.3](parts/02-the-state-machine/2.3-where-plt-plot-stops-working.md)).
- **`plt.subplots()` returns a tuple**, and unpacking it wrongly gives an error two lines later
  rather than on the line that caused it ([3.1](parts/03-the-object-api/3.1-fig-ax-subplots.md)).
- **`ax.set(...)` cannot take an argument that needs more than one value**, so `set_xticks` with
  labels and a rotation has to stay its own call
  ([3.4](parts/03-the-object-api/3.4-ax-set-the-one-call-form.md)).
- **A drawing function that makes its own figure cannot be put into a grid**, which is why every one
  of them takes `ax=None` and returns the axes
  ([3.5](parts/03-the-object-api/3.5-the-ax-parameter.md)).
- **`plt.subplots(1, 3)` gives a one-dimensional array and `plt.subplots(2, 3)` gives a
  two-dimensional one**, so the same indexing code breaks when the grid changes shape
  ([4.1](parts/04-many-axes/4.1-a-grid-of-axes.md)).
- **An unused panel in a grid is drawn as an empty box**, not omitted
  ([4.2](parts/04-many-axes/4.2-the-axes-you-forgot-to-use.md)).
- **Four panels with four different y ranges are four charts, not one comparison**, and the reader
  is not told ([4.3](parts/04-many-axes/4.3-shared-axes.md)).
- **Without a layout setting, a long y label is drawn outside the figure** and simply disappears
  from the saved file ([4.4](parts/04-many-axes/4.4-constrained-layout.md)).
- **`matplotlib.use` has to come before `import matplotlib.pyplot`**, because the backend is chosen
  when pyplot loads ([5.1](parts/05-getting-it-out/5.1-backends-and-the-script-with-no-window.md)).
- **`bbox_inches="tight"` changes the saved figure's size**, so a pack of figures saved that way is
  no longer a consistent size ([5.2](parts/05-getting-it-out/5.2-savefig-dpi-and-bbox-inches.md)).
- **`dpi` changes the pixel dimensions and not the layout**, so a low-dpi save shrinks the text
  relative to nothing ([5.2](parts/05-getting-it-out/5.2-savefig-dpi-and-bbox-inches.md)).
- **A scatter of a million points is a vector file with a million objects in it**, and it will not
  open ([5.3](parts/05-getting-it-out/5.3-vector-or-raster.md)).
- **A figure is not garbage-collected when the variable goes out of scope**, because pyplot keeps a
  reference to it ([5.4](parts/05-getting-it-out/5.4-the-figures-you-never-closed.md)).

**The pattern behind the day.** Almost none of these raises. The state machine draws a chart; the
unshared axes draw four charts; the missing label draws a chart with a blank edge; the leaked figure
draws every chart perfectly and then runs the machine out of memory an hour later. Every one of them
produces a picture that looks like a picture — which is why the module names the figure and the
axes explicitly, returns the axes rather than the figure, closes what it opens, and is tested by
asking the objects what they contain rather than by looking.

---

## §8 Verify before you code

Fetched on the day of writing, 2026-09-08. Read the argument lists rather than trusting any lesson,
this one included.

- **Quick start guide** — <https://matplotlib.org/stable/users/explain/quick_start.html> — the
  library's own figure-and-axes diagram, and its own statement of the object API against the
  `pyplot` interface.
- **The figure** — <https://matplotlib.org/stable/users/explain/figure/figure_intro.html> — what a
  figure owns, and what it does not.
- **`matplotlib.pyplot.subplots`** —
  <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html> — read the defaults
  for `squeeze`, `sharex`, `sharey` and `layout`, and what each one returns.
- **`matplotlib.axes.Axes`** — <https://matplotlib.org/stable/api/axes_api.html> — the full list of
  setters, which is the list [3.3](parts/03-the-object-api/3.3-the-setter-names.md) teaches you to
  search rather than memorise.
- **Backends** — <https://matplotlib.org/stable/users/explain/figure/backends.html> — what `Agg` is
  and why a script wants it.
- **`Figure.savefig`** —
  <https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.savefig> — read what
  `dpi`, `bbox_inches` and `transparent` actually change.

---

## §9 Say it in an interview

> Matplotlib has two objects that matter and one word that trips everybody up. A **figure** is the
> sheet of paper: it owns the size and it holds the panels. An **axes** is one panel drawn on it —
> the box with data inside — and it is what you actually label, because a title, an x label and tick
> marks all belong to a panel rather than to the sheet. The word that trips people is that "axes"
> with an s is one panel, while an "axis" is a single edge of that panel, so a figure with two
> panels has two axes and four axis objects.
>
> There are two ways to drive it, and I only use one. The `pyplot` interface keeps a current figure
> and a current axes in module-level state, so `plt.bar` creates a figure if none exists and
> `plt.title` writes on whichever one is current. That is fine in a notebook cell and it fails in
> four places that matter: inside a function that another function also draws in, in a loop that
> builds several charts, under pytest where test order decides which figure is current, and in any
> notebook cell that gets re-run. So every chart I write starts `fig, ax = plt.subplots()`, and
> every function that draws takes `ax=None`, creates one only if it was given none, and returns the
> axes. That signature is the thing that makes charts composable — it is what lets the same function
> draw standalone and into a panel of a grid without knowing which it is doing.
>
> A couple of details I would mention because they bite in production. `plt.subplots` squeezes its
> return value by default, so a one-row grid comes back one-dimensional and a two-row grid
> two-dimensional, and the indexing code that worked for one breaks for the other — I pass
> `squeeze=False` so the shape is always the same. Panels that are meant to be compared need shared
> axes, because four panels with four different y ranges are four separate charts and the reader is
> not told. And pyplot holds a reference to every figure it creates, so a figure is not collected
> when its variable goes out of scope: a service that renders charts on request and does not call
> `close` will warn after twenty and run out of memory eventually. My save function closes the
> figure it saved, and that is not tidiness, it is the fix.
>
> Testing charts is the part people assume is impossible. It is not, as long as you stop trying to
> look at the picture. In CI I assert on the objects: the title, the x label and the y label are
> non-empty; the bar heights match the data that went in; the number of panels matches the grid I
> asked for; a bar chart's y axis starts at zero; the saved file exists and is not empty. Those
> catch the failures that actually happen. Image comparison exists and I would avoid it — it goes
> red when a font version changes, which trains people to ignore it.

---

## §10 Done when

Every box in [`CHECKLIST.md`](CHECKLIST.md) is ticked and `./m check` is green.

Not when a duration has elapsed. A part is finished when you can answer its *Check yourself* question
out loud without scrolling, and the day is finished when `./m done 36` accepts it — which it will
refuse to do while any box is unticked (Principle 17).
