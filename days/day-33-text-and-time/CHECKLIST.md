# Day 33 — Definition of done

`PD-11` text data with the `.str` accessor · `PD-12` date and time, `Timedelta`, resampling.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints one item where there were four
spellings, a refusal, a parsed column at the resolution you asked for, and a week nobody shopped in:

```bash
uv run python -c "
import pandas as pd
from setu.textdate import TextDateError, by_period, extract_field, normalise_item, parse_time

receipts = pd.DataFrame({
    'item': pd.Series(['Milk', 'milk ', 'MILK', 'milk'], dtype='str'),
    'paid_at': pd.Series([
        '2026-03-01 08:12:30',
        '2026-03-04 19:40:05',
        '2026-03-18 11:05:00',
        '2026-03-19 18:22:47',
    ], dtype='str'),
    'price': [1.15, 1.15, 1.20, 1.20],
})

clean = normalise_item(receipts, 'item')
print('spellings :', receipts['item'].nunique(), '->', clean['item'].nunique())

try:
    extract_field(clean['item'], r'(?P<shop>shop-\d+)', 'shop', min_match_rate=0.9)
except TextDateError as e:
    print('refused   :', str(e).splitlines()[0])

timed = parse_time(clean, 'paid_at', fmt='%Y-%m-%d %H:%M:%S', tz='UTC')
print('dtype     :', timed['paid_at'].dtype)

weekly = by_period(timed, 'paid_at', freq='W', value='price', how='sum')
print('weeks     :', len(weekly), 'rows -- expected 3, one of them empty')
print(weekly.to_dict())
"
```

The spelling count must go from 4 to 1, the pattern that matches nothing must be **refused** rather
than returning blanks, the parsed dtype must state its resolution and its timezone, and the weekly
result must contain the week nobody shopped in. If any of those fails, sections 2, 3, 4 or 6 have
not landed.

---

## Setup

- [ ] Ran `./m scaffold 33` and created `src/setu/textdate.py` and `tests/test_textdate.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5` and `numpy.__version__` is `2.5.2`
- [ ] If either has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Ran the §3 warm-up and got **4 spellings, 2 after `lower()`, 1 after `strip().lower()`**
- [ ] Saw the `TypeError` from subtracting one text date from another
- [ ] Can say why lower-casing alone left the flat's bug exactly as broken as it was
- [ ] Confirmed nothing was installed today — everything came from Day 26

## Section 1 — the `.str` accessor

- [ ] **1.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say in one sentence why a column has no `.lower()` when every value in it does
- [ ] **1.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say what a blank does to `.str.contains` used as a filter
- [ ] **1.3** read · ran its check-yourself · answered its question out loud
- [ ] Recorded my own `str` against `object` measurement, on my own machine

## Section 2 — cleaning names

- [ ] **2.1** read · ran its check-yourself · answered its question out loud
- [ ] **2.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say what `.str.replace('.', '')` does under each setting of `regex=`
- [ ] **2.3** read · ran its check-yourself · answered its question out loud
- [ ] Can name the row that `contains('milk')` matches and should not
- [ ] **2.4** read · ran its check-yourself · answered its question out loud
- [ ] Recorded the rows lost **and** the money lost by the unnormalised join, and can say why the
      two percentages differ

## Section 3 — pulling text apart

- [ ] **3.1** read · ran its check-yourself · answered its question out loud
- [ ] Can say why a column of lists is a dead end rather than an inconvenience
- [ ] **3.2** read · ran its check-yourself · answered its question out loud
- [ ] **3.3** read · ran its check-yourself · answered its question out loud
- [ ] Can say why the named capture group is the version worth keeping
- [ ] **3.4** read · ran its check-yourself · answered its question out loud
- [ ] Watched a pattern match nothing, return a full-length column of blanks, and raise **nothing**

## Section 4 — the `.dt` accessor

- [ ] **4.1** read · ran its check-yourself · answered its question out loud
- [ ] Saw a date format where sorting the text gives the wrong order
- [ ] **4.2** read · ran its check-yourself · answered its question out loud
- [ ] Can say what `errors="coerce"` converts a loud failure into
- [ ] **4.3** read · ran its check-yourself · answered its question out loud
- [ ] Checked for myself which day of the week `.dt.dayofweek == 0` is, rather than assuming
- [ ] **4.4** read · ran its check-yourself · answered its question out loud
- [ ] Printed the resolution of a parsed column on **my** machine and can say what it is
- [ ] **4.5** read · ran its check-yourself · answered its question out loud
- [ ] Saw the real error from comparing a naive timestamp with an aware one

## Section 5 — arithmetic on time

- [ ] **5.1** read · ran its check-yourself · answered its question out loud
- [ ] **5.2** read · ran its check-yourself · answered its question out loud
- [ ] Saw `.dt.days` report `1` for a 47-hour gap
- [ ] **5.3** read · ran its check-yourself · answered its question out loud
- [ ] Added one month to 31 January and can say what the answer was and why

## Section 6 — resampling

- [ ] **6.1** read · ran its check-yourself · answered its question out loud
- [ ] **6.2** read · ran its check-yourself · answered its question out loud
- [ ] Ran the frequency aliases myself and recorded which ones this pandas accepts
- [ ] **6.3** read · ran its check-yourself · answered its question out loud
- [ ] Got **different row counts** from `groupby` and `resample` on the same file
- [ ] Can say what `0` means and what a blank means for a week nobody shopped in
- [ ] **6.4** read · ran its check-yourself · answered its question out loud
- [ ] Ran the same resample with `label="left"` and `label="right"` and compared the tables
- [ ] **6.5** read · ran its check-yourself · answered its question out loud
- [ ] Can say which of `rolling` and `resample` a "weekly spend" metric actually means

## Section 7 — the module

- [ ] **7.1** read · ran its check-yourself · answered its question out loud
- [ ] **7.2** read · ran its check-yourself · answered its question out loud

## Build brief

- [ ] `src/setu/textdate.py` exists with `TEXT_DTYPE`, `TIME_FORMAT` and `MIN_MATCH_RATE` as
      module constants
- [ ] `TextDateError` subclasses `ValueError`; no fourth exception family was invented
- [ ] `normalise_item` asserts the dtype **before** any `.str` call and returns a new frame
- [ ] `extract_field` raises when the match rate is below the floor, and names the rate in the
      message
- [ ] `parse_time` passes an explicit `format=`, surfaces failures, and asserts the resolution
- [ ] `by_period` makes the caller name the empty-bucket policy
- [ ] `TODO(me)`: fixed `clean_key` and stated its guarantee in the docstring
- [ ] `TODO(me)`: added `time_report` with the comment on why the failed *share* is the alert
- [ ] `TODO(me)`: added `guard_freq` with the comment on why the input row count predicts nothing
- [ ] `lab/the_week_that_was_not_there.py` runs and prints three weekly totals with their row counts
- [ ] `TODO(me)`: added the empty-month case and said which answer a chart should use
- [ ] `TODO(me)`: ran it with both `label=` settings and recorded both

## Tests

- [ ] `tests/test_textdate.py` has three **fixtures**: messy text, an unparseable timestamp, an
      empty week
- [ ] There is a test asserting each fixture has the property it exists for
- [ ] The trailing-space test asserts the fixture **has** a trailing space before the normalising
- [ ] There is a test that a pattern matching nothing is refused
- [ ] `pytest.raises` is used with `match=` on a fragment rather than a whole sentence
- [ ] The resample test asserts the row count **including** the empty bucket
- [ ] **Break it (1):** removed the dtype assertion and watched **one** test go red
- [ ] **Break it (2):** dropped the explicit `format=` and watched a **different** one go red
- [ ] **Break it (3):** let the empty-bucket policy default and watched the row-count test go red
- [ ] **Break it (4):** changed `MIN_MATCH_RATE` from `0.99` to `0.1` and watched the suite stay
      **green**
- [ ] Can explain what (4) proves about the difference between a bug and a policy change
- [ ] `TODO(me)`: wrote the tests for the fixed `clean_key`
- [ ] `TODO(me)`: added the normalise-twice property test with its comment
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:`
      block

## The gate

- [ ] `uv run ruff format days/day-33-text-and-time/ src/setu/textdate.py tests/test_textdate.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 33` passes
- [ ] `./m check` is green
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 33` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-11` and `PD-12` and quotes my own unmatched-spend share from
      `2.4` and my own resolution from `4.4`
