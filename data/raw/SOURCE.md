# data/raw/ — provenance (Principle 9)

Every dataset that lands in this folder gets an entry below **before** it is used.
The files themselves are gitignored; this record is not.

| Dataset | Source URL | Licence | Pulled on | Used from day | Notes |
|---|---|---|---|---|---|
| | | | | | |

**Rules**
- No mystery CSVs. If it has no row here, it does not get used.
- `data/raw/` is downloaded and never edited. `data/processed/` is generated and always reproducible
  from `data/raw/` plus committed code.
- Nothing in here is ever sent to a free-tier model API. Fixtures and public data only.
