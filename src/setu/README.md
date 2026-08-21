# src/setu/ — deliberately almost empty

Nothing here is pre-written. **You** create every module, from the code printed in the lessons.
That is rule 1 of `days/README.md`: you cannot debug on Day 200 what you never typed on Day 26.

By the end of Phase 1 (Day 11) this folder holds:

| Module | Written on | What it is |
|---|---|---|
| `paths.py` | Day 1 | canonical filesystem locations |
| `versions.py` | Day 1 | the frozen pin record + a drift check |
| `config.py` | Day 2 | `.env` loading that fails loudly |
| `models.py` | Day 3 | model ids behind role names |
| `retry.py` | Day 6 | the capped retry with jittered backoff |
| `textutils.py` | Days 4, 5, 7, 9 | pure text helpers |
| `collections.py` | Days 8, 9 | O(1) dedupe, counts, chunking |
| `papers.py` | Day 10 | the `Paper` record and its validation |
| `streams.py` | Day 11 | lazy stream helpers |

`__init__.py` stays empty. **No module in here does any work at import time.**
