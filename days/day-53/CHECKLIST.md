# Day 53 — CHECKLIST

**IDs covered:** APP-02, APP-03 · **Principles served:** 1, 5, 7

## Demo command

```bash
uv run streamlit run days/day-53/lab/widgets.py
uv run python -m pytest tests/test_app.py -v
```

Expected: a seven-section page with a visible query counter, then all app tests green.

## Setup

- [ ] `./m start 53` and `./m scaffold 53` run
- [ ] `days/day-53/lab/widgets.py` created
- [ ] No new packages installed

## APP-02 — widgets

- [ ] Used text, number, select, multiselect, slider (range), date, checkbox, radio
- [ ] Watched the whole value dict re-render on every single change
- [ ] Used a tuple default to get a **range** slider
- [ ] Used `horizontal=True` on a radio; can say when that reads better than a dropdown

## The query counter

- [ ] Clicked the loose query button and watched the counter climb
- [ ] Can state the cost of six widgets above one unconditional query

## Forms

- [ ] Edited four fields inside `st.form` and confirmed **nothing reran**
- [ ] Pressed submit and confirmed **exactly one** query fired
- [ ] Can state what `st.form` changes — and that it is not a layout container
- [ ] Read §4 and can state the **trade-off** in one sentence
- [ ] Know that only `st.form_submit_button` is allowed inside a form

## Upload

- [ ] Uploaded a CSV and guarded with `if uploaded is not None`
- [ ] Read it with `dtype=` and `nrows=`
- [ ] Can say why a human choosing the file does not make it trusted

## APP-03 — layout

- [ ] Used the sidebar for page-wide controls
- [ ] Used `st.columns` with relative widths; used both `with a:` and `a.metric(...)`
- [ ] Used tabs, an expander and a bordered container
- [ ] **Confirmed tab content renders even for tabs you cannot see**
- [ ] Can state what that means for a query placed inside a tab
- [ ] Same for an expander

## Fragments

- [ ] Wrote an `@st.fragment` function
- [ ] Moved its slider and confirmed the page query count **did not change**
- [ ] Can say when to reach for a fragment rather than a form

## Build brief

- [ ] `SearchSpec` — frozen dataclass
- [ ] `validate_spec` — **TODO(me)**: normalises, validates, clamps years, returns a new spec
- [ ] `spec_to_filters` — **TODO(me)**: `"any"` means no clause; values stay values
- [ ] `describe_spec` — **TODO(me)**: omits defaults
- [ ] `check_upload` — **TODO(me)**: suffix, size, path check; takes `(name, size)` not a file
- [ ] `render_search_form` — **TODO(me)**: exactly one form, thin
- [ ] Can explain why `check_upload` takes facts rather than a file object

## Tests that must be able to fail

- [ ] `test_validate_normalises_the_title` — green
- [ ] `test_validate_returns_a_new_spec` — green
- [ ] `test_validate_rejects_an_unknown_venue` / `..._sort_field` — green
- [ ] `test_validate_rejects_reversed_years` — green, both years named
- [ ] `test_validate_rejects_negative_citations` — green
- [ ] `test_validate_clamps_out_of_range_years` — green
- [ ] `test_any_venue_produces_no_clause` — green ← **today's real assessment**
- [ ] **Passed `"any"` through as a value, watched it go red, fixed it** ← do not skip
- [ ] `test_a_named_venue_produces_a_clause` — green
- [ ] `test_an_empty_title_produces_no_clause` — green
- [ ] `test_mongo_filter_passes_the_safety_check` — green
- [ ] `test_filters_never_contain_raw_sql` — green
- [ ] **Stripped quotes from the value instead of binding it, watched it go red, reverted** ← do not skip
- [ ] `test_describe_omits_defaults` / `test_describe_includes_what_was_set` — green
- [ ] `test_upload_accepts_valid_names` — three green cases
- [ ] `test_upload_rejects_bad_suffixes` — four green cases including `papers.csv.exe`
- [ ] `test_upload_rejects_an_oversized_file` — green
- [ ] `test_upload_rejects_a_path_in_the_filename` — four green cases
- [ ] `test_search_functions_are_pure` — green
- [ ] `test_the_search_form_is_a_single_form` — green
- [ ] **Split the inputs across two forms, watched it go red, merged them** ← do not skip
- [ ] `test_no_expensive_work_behind_tabs` — green

## Budget

- [ ] LLM calls today: **0**

## Understanding check — answer out loud

- [ ] What does `st.form` change about the execution model?
- [ ] What can a form **not** do, and when does that make it the wrong choice?
- [ ] Are tabs lazy? What about expanders?
- [ ] What does that mean for where you put a slow query?
- [ ] What does `@st.fragment` re-run, and what does it not?
- [ ] Why is an uploaded file untrusted input? Name two ways it can be hostile
- [ ] Why must `"any"` become the absence of a clause?
- [ ] Why bind a hostile value rather than sanitise it?

## Commit

- [ ] `./m check && ./m done 53` succeeded
