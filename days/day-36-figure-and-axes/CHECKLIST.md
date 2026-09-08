# Day 36 — Definition of done

`VIZ-01` matplotlib: the figure, the axes, and the object API.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints two labelled panels on one figure, a
bar chart whose axis starts at zero, a saved file, and **no** figures left open:

```bash
uv run python -c "
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from setu.figures import new_figure, save, spend_by_aisle, weekly_total

AISLES = {'dairy': 21.85, 'bakery': 9.80, 'produce': 27.00, 'household': 13.80}
WEEKS = [1, 2, 3, 4]
WEEKLY = [17.20, 14.25, 22.00, 19.00]

fig, axs = new_figure(2, 1)
top = spend_by_aisle(AISLES, ax=axs[0, 0])
bottom = weekly_total(WEEKS, WEEKLY, ax=axs[1, 0])

print('panels      :', len(fig.axes))
print('grid shape  :', axs.shape)
print('top labels  :', repr(top.get_title()), repr(top.get_xlabel()), repr(top.get_ylabel()))
print('bar baseline:', top.get_ylim()[0])
print('bar heights :', [round(b.get_height(), 2) for b in top.containers[0]])

path = save(fig, Path('days/day-36-figure-and-axes/lab/fridge.png'))
print('saved       :', path, path.stat().st_size, 'bytes')
print('open figures:', len(plt.get_fignums()))
"
```

There must be **two** panels, the grid shape must be `(2, 1)` rather than `(2,)`, all three label
strings must be non-empty, the bar baseline must be `0.0`, the bar heights must equal the data that
went in, the file must exist and be non-empty, and the open-figure count must be **0**. If any of
those fails, sections 3, 4, 5 or 6 have not landed.

---

## Setup

- [ ] Ran `./m scaffold 36` and created `src/setu/figures.py` and `tests/test_figures.py`
- [ ] Confirmed `matplotlib.__version__` is `3.11.1`
- [ ] If it has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Confirmed nothing was installed today — `matplotlib` arrived on Day 34
- [ ] Ran the §3 warm-up and saw a **bare figure hold no axes**
- [ ] Recorded what `matplotlib.get_backend()` says on my machine before I set it

## Section 1 — the two objects

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say, without the word "matplotlib", what the sheet does and what the box does
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say how many axes and how many axis objects a two-panel figure has
- [ ] **1.3** read · ran its check-yourself · answered its question out loud
- [ ] Changed one bar's height after drawing it, and left the others untouched

## Section 2 — the state machine

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] Called `plt.bar` with no figure in sight and then found the figure it made
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Made a title land on the **wrong** figure, on purpose, and can say why
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced at least two of the four places the state machine breaks
- [ ] Can say what `plt.subplots` still uses the state machine for

## Section 3 — the object API

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say what `ax.bar` returns and why it is worth keeping
- [ ] **3.3** read · ran its check-yourself · answered its question out loud
- [ ] Listed the `set_` methods on an axes myself and counted them
- [ ] **3.4** read · ran its check-yourself · answered its question out loud
- [ ] Saw the real error from passing `ax.set` a keyword it does not know
- [ ] **3.5** read · ran its check-yourself · answered its question out loud
- [ ] Wrote one function with the `ax=None` signature and called it both ways

## Section 4 — many axes

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw `subplots(1, 3)` and `subplots(2, 3)` return arrays of **different** dimensionality
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] **4.3** read · ran its check-yourself · answered its question out loud
- [ ] Printed the four y limits with and without `sharey`, and can name the aisle that changed
      appearance
- [ ] **4.4** read · ran its check-yourself · answered its question out loud
- [ ] Measured the y label's bounding box under all three layout settings, rather than eyeballing it

## Section 5 — getting it out

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say why `matplotlib.use` must come **before** `import matplotlib.pyplot`
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Saved one figure four ways and recorded the four file sizes and pixel dimensions
- [ ] **5.3** read · ran its check-yourself · answered its question out loud
- [ ] Can say which format I would email and which I would send to a print shop, and why
- [ ] **5.4** read · ran its check-yourself · answered its question out loud
- [ ] Reproduced matplotlib's open-figure warning myself and recorded its exact text
- [ ] Watched memory grow across a loop of figures that were never closed

## Section 6 — the module

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say why this project asserts on objects rather than comparing images

## Build brief

- [ ] `src/setu/figures.py` exists with `FIGSIZE`, `DPI` and `BACKEND` as module constants
- [ ] `FigureError` subclasses `ValueError`; no seventh exception family was invented
- [ ] `new_figure` always passes `squeeze=False` and `layout="constrained"`
- [ ] `spend_by_aisle` and `weekly_total` both take `ax=None` and **return the axes**
- [ ] `save` closes the figure it saved and returns the path
- [ ] `TODO(me)`: fixed `quick_look` and stated the figure-count guarantee in its docstring
- [ ] `TODO(me)`: added `panel_pack` with the refusal, and the comment on why refusing beats
      dropping
- [ ] `TODO(me)`: left `greyscale_check` as a stub with a comment naming what it must measure
- [ ] `lab/the_fridge_chart.py` runs and prints the panel count, both y limits and the file size
- [ ] `TODO(me)`: saved the two-panel chart with and without `sharey` and named the aisle that
      changed
- [ ] `TODO(me)`: saved PNG, SVG and PDF and recorded the three sizes with my choice for each use

## Tests

- [ ] `tests/test_figures.py` has a fixture that closes every figure after each test
- [ ] There is a test proving that fixture actually works
- [ ] The labelling test asserts the title, x label **and** y label are non-empty
- [ ] There is a test that the bar heights equal the data that went in
- [ ] There is a test that a bar chart's y axis starts at zero
- [ ] There is a test that the saved file exists and is non-empty
- [ ] `pytest.raises` is used with `match=` on a fragment rather than a whole sentence
- [ ] **Break it (1):** dropped `set_ylabel` and watched **one** test go red while the picture still
      looked fine
- [ ] **Break it (2):** returned the figure instead of the axes and watched a **different** one go
      red
- [ ] **Break it (3):** removed `squeeze=False` and watched the grid-shape test go red for `(1, 1)`
      only
- [ ] **Break it (4):** changed `FIGSIZE` to `(3, 2)` and watched the suite stay **green**
- [ ] Can explain what (4) proves about what a test suite can and cannot defend
- [ ] `TODO(me)`: wrote the tests for the fixed `quick_look`, including the fifty-call figure count
- [ ] `TODO(me)`: added the grid-dimensionality test with its comment
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate

- [ ] `uv run ruff format days/day-36-figure-and-axes/ src/setu/figures.py tests/test_figures.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 36` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day
- [ ] `lab/fridge.png` exists and I have actually looked at it

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 36` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `VIZ-01` and quotes **my own** four saved-file sizes from `5.2` and
      the figure count at which matplotlib warned me in `5.4`
