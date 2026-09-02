# Day 27 — Definition of done

`PD-02` Reading and writing: CSV, JSON, Parquet, SQL — typed at read time.
Nothing here is ticked because a duration passed. Every box is a thing that happened.

**The demo command** — the day is not done until this prints a table with `07` in it:

```bash
uv run python -c "
from setu.loaders import load
for name in ['shopping.csv', 'shopping.parquet', 'shop.db']:
    frame = load(f'data/{name}')
    print(f'{name:18}', frame['aisle'].tolist(), str(frame['bought'].dtype))
"
```

---

## Setup

- [ ] Ran `./m scaffold 27` and created `src/setu/loaders.py` and `tests/test_loaders.py`
- [ ] Confirmed `pandas.__version__` is `3.0.5` and `pyarrow.__version__` is `25.0.1`
- [ ] Confirmed `sqlite3.sqlite_version` is `3.37.0` or higher, so `STRICT` tables exist
- [ ] If any of the three has moved: logged it in `docs/CHANGELOG_PLAN_DS.md` and stopped (Principle 14)
- [ ] Wrote `data/shopping.csv` with the hub's §3 command and looked at the raw text, not a frame
- [ ] Confirmed nothing was installed today — pandas and pyarrow came from Day 26, `sqlite3` is stdlib

## Section 1 — the CSV

- [ ] **1.1** read · ran its check-yourself · answered its out-loud question
- [ ] Saw with my own eyes that `data/shopping.csv` is 129 bytes and contains no type information
- [ ] **1.2** read · ran its check-yourself · answered its out-loud question
- [ ] **1.3** read · ran its check-yourself · answered its out-loud question
- [ ] Watched `07` become `7`, then tried `astype(str)` and saw that it gives `"7"` and not `"07"`
- [ ] **1.4** read · ran its check-yourself · answered its out-loud question
- [ ] **1.5** read · ran its check-yourself · answered its out-loud question
- [ ] **1.6** read · ran its check-yourself · answered its out-loud question
- [ ] **1.7** read · ran its check-yourself · answered its out-loud question
- [ ] Reproduced the comma-inside-a-value failure **both ways** — the silent reshape and the `ParserError`

## Section 2 — JSON

- [ ] **2.1** read · ran its check-yourself · answered its out-loud question
- [ ] **2.2** read · ran its check-yourself · answered its out-loud question
- [ ] **2.3** read · ran its check-yourself · answered its out-loud question
- [ ] Wrote the same frame with every `orient` and looked at all six files as raw text
- [ ] **2.4** read · ran its check-yourself · answered its out-loud question

## Section 3 — Parquet

- [ ] **3.1** read · ran its check-yourself · answered its out-loud question
- [ ] **3.2** read · ran its check-yourself · answered its out-loud question
- [ ] **3.3** read · ran its check-yourself · answered its out-loud question
- [ ] Built the half-million-row file and ran the size-and-speed table **on my own machine**
- [ ] Recorded my own numbers next to the lesson's, and can explain why compression bought so little
- [ ] **3.4** read · ran its check-yourself · answered its out-loud question
- [ ] Read a Parquet footer with `pq.ParquetFile(...).metadata` and found the three wanted columns' bytes

## Section 4 — SQL

- [ ] **4.1** read · ran its check-yourself · answered its out-loud question
- [ ] Built `data/shop.db` from nothing and read its schema back out of `sqlite_master`
- [ ] Saw `IntegrityError: NOT NULL constraint failed` — the refusal no file format can make
- [ ] Reproduced the missing-`commit()` case and watched the row vanish with no error
- [ ] **4.2** read · ran its check-yourself · answered its out-loud question
- [ ] Confirmed `aisle` arrives as `str` with **no** `dtype=` anywhere, and that `bought` does not
- [ ] **4.3** read · ran its check-yourself · answered its out-loud question
- [ ] Ran the f-string search with `milk' OR '1'='1` and counted the rows it returned
- [ ] Ran the same value through `params=` and confirmed it returned none
- [ ] **4.4** read · ran its check-yourself · answered its out-loud question
- [ ] Let `to_sql` create a table, then read the schema it invented and found the `index` column
- [ ] Watched `STRICT` refuse the value that a plain table accepted

## Section 5 — the module

- [ ] **5.1** read · ran its check-yourself · answered its out-loud question
- [ ] **5.2** read · ran its check-yourself · answered its out-loud question
- [ ] Measured the peak memory of the whole-file read against the chunked read, on my own machine
- [ ] Saw that the two totals agree to the penny and are **not** the same float, and can say why
- [ ] Iterated a chunked reader twice and watched the second pass return zero rows, silently
- [ ] **5.3** read · ran its check-yourself · answered its out-loud question

## The build

- [ ] `src/setu/loaders.py` has `SCHEMA`, `DATES`, and `COLUMNS` **derived** from the other two
- [ ] It reuses Day 26's `SchemaError` and `assert_schema` rather than redefining either
- [ ] `load_csv`, `load_parquet` and `load_sql` all return a frame with identical dtypes
- [ ] `load_sql` uses a `mode=ro` connection and `closing()`, and binds every value with `params=`
- [ ] `load()` dispatches on the suffix and its error names the formats it does know
- [ ] `iter_csv` and `total_in_chunks` never hold more than one chunk
- [ ] `to_shopping_list` narrows to three columns and hands the result to Day 26's `assert_schema`
- [ ] `TODO(me)`: wrote `load_json` and justified my `orient` choice in its docstring
- [ ] `TODO(me)`: added the `since` bound parameter to `load_sql` without building SQL by formatting
- [ ] `TODO(me)`: decided about an explicit `format=` override and wrote the reason down as a comment
- [ ] `lab/four_ways.py` prints the four stores' dtypes read naively and read properly
- [ ] `TODO(me)`: added the third row — repaired-afterwards — and compared **values**, not just dtypes

## The tests

- [ ] `tests/test_loaders.py` builds its own input in `tmp_path` and reads no committed file
- [ ] One test per store's round trip, including the CSV one that asserts a **failure**
- [ ] The chunked-total test uses `pytest.approx`, and I can say why `==` would be wrong
- [ ] `uv run pytest tests/test_loaders.py -q` is green
- [ ] **Break it:** deleted `dtype=SCHEMA` from `load_csv`, ran the suite, watched **four** go red
- [ ] Read all four failures, and can explain why the **SQL** test failed when only the CSV changed
- [ ] Put the argument back and confirmed the suite is green again
- [ ] `TODO(me)`: wrote the round-trip test for `load_json` and kept it even where it surprised me
- [ ] `TODO(me)`: added the empty-frame test and recorded what the dtypes actually were
- [ ] `TODO(me)`: broke the module a **second** way of my own and recorded it in a `# Seen to fail:` block

## The gate

- [ ] `uv run ruff format days/day-27-reading-and-writing/ src/setu/loaders.py tests/test_loaders.py`
- [ ] `uv run ruff check` is clean, with no new `noqa`
- [ ] `./m depth 27` passes
- [ ] `./m check` is green
- [ ] Deleted the generated benchmark files under `data/` — they are reproducible from a seed
- [ ] `./m tracker` run, so `docs/TRACKER.md` and `days/INDEX.md` include this day

## Budget

- [ ] **Zero.** No model calls, no API keys, no network at run time, nothing installed. Confirmed.

## Commit

- [ ] Every box above is ticked
- [ ] `./m done 27` — refuses unless the checklist is ticked and `./m check` is green
- [ ] The commit message names `PD-02` and says which store surprised me most
