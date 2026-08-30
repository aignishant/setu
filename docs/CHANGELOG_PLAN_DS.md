---
name: changelog-plan-ds
plan: setu
---

# 📓 Plan changelog — Project Setu

Principle 14: *if reality changes, the plan is amended first.* Every amendment lands here before any
code or lesson changes. Newest first.

---

## v2.3.0a — 2026-08-30 — the working set, projected

**Not a version bump.** No day, ID, phase, gate, pin, principle or part-contract section changed.
The plan is still v2.3.0 and every hub's `plan_version` stays `v2.3.0`. This entry records
tooling plus the two places in Part 11 that described that tooling and had to be corrected to
stay true.

**Trigger.** A measurement of what one day-writing session actually loads. The read set named by
Step 1 of the day-setu skill — the plan (92 KB), the curriculum index (23 KB), the tracker
(34 KB), and the two neighbouring written days it asks you to read for continuity (485 KB) —
came to **660 KB, about 165 000 tokens**, and the thing it was all for was two rows of the Part 4
matrix and a list of what had already been taught. Part 4 alone is 39% of the plan and holds 230+
ID rows; a day needs two to six of them.

**What was measured before anything was proposed.** Three suspicions were tested and two died.
Overlap between `CLAUDE.md`, Part 11 and the day-setu skill was measured by 8-gram shingle at
**0.7–6.8%** — they are three different compressions, not duplicates, so nothing was deduplicated.
The ~30 KB `LESSON.md` hubs were suspected of teaching, but `depth_check.py` already fails a hub
that teaches and all eleven days pass, so they were left alone.

**The change.**

- `scripts/day_brief.py`, run as `./m brief NN`. Prints one day's working set: its IDs with their
  full Part 4 rows, the phase theme and gate from Part 5, the part manifests of the two previous
  written days, what is already in `src/setu/`, and a warning when the previous day's checklist
  has open boxes. **Every line is copied verbatim from a source file and labelled with the path
  it came from.** It is the plan filtered, not the plan summarised.
- `scripts/parts_index.py`, wired into `./m tracker`, generates `days/INDEX.md`: one row per part
  across every written day, with its `level`, its IDs and a link, plus an inverted
  curriculum-ID-to-parts table. It is projected from the eight frontmatter keys the depth
  contract already mandates, so it cannot disagree with the parts it indexes.
- `./m tracker` now regenerates both files together. Refreshing one without the other is how a
  generated file starts lying.
- Part 11.9 gains the repo-level index check described below; Part 11.9's closing note and the
  companion-file list at the top of the plan now name `days/INDEX.md` and `./m brief`.
- The day-setu skill's Step 1 is rewritten around the brief, with the rule that governs it stated
  explicitly: **a projection may replace a lookup; it may never replace a judgement.** Part 11 is
  still read in full, every time. The brief deliberately does not contain it.

**The lint findings this turned up, each verified before it was believed.**

- A stale `TRACKER.md` at the repository root, 31 KB, tracked by Git. All 24 references in the
  repository point at `docs/TRACKER.md`; `scripts/tracker.py` writes only there. Its legend still
  defined a *written* day the pre-v2.0.0 way and its "Next up" pointed at Day 128. Deleted.
- `docs/CURRICULUM_INDEX_DS.md` was stamped `plan_version: "v1.0.0"`. Its content was checked
  against v2.3.0 and **agrees**: all 30 phase day-ranges match Part 5 and all 303 matrix IDs
  reach a day, which is why v2.0.0–v2.3.0 (document architecture, not the day map) left it
  correct. Stamp corrected to `v2.3.0` and a `verified:` date added beside `generated:`.
- The same file claimed "every day cites ≥1 ID", which is false for the five days that build the
  project rather than teach a topic — Days 1–3 and 239–240. The claim now states the exception.
- `./m depth`, on a full sweep only, now fails when the index disagrees with the plan: phase
  ranges against Part 5, matrix-ID coverage, and the version stamp. It went red on the stamp
  before the stamp was fixed, which is the only reason it is worth having.

**Result.** The same session's read set drops from ~660 KB to ~66 KB, about **165 000 tokens to
16 500 — a 90% cut** — with `CLAUDE.md`, the skill and Part 11 all still loaded whole and
unedited in substance. What was removed was lookup, not judgement.

---

## v2.3.0 — 2026-08-26 — papers out, prose in

**Trigger.** A read-through of the first four written days (0–3) found two problems that no check
could see, and one of them was made worse by v2.2.0.

The first is the writing itself. *The story* section is the one a reader meets before they have any
vocabulary, and several of them opened on scenes a beginner has never been in, used the technical
word before it was defined, and ran sentences together without the punctuation that tells a reader
where to breathe. That is not a small stylistic complaint: a reader who has to decode the prose has
less attention left for the idea, and the idea is the whole point. Nothing in the contract said
anything about the words, so nothing caught it.

The second is `papers/`. v2.2.0 added a whole second class of document — thirteen sections, a
runnable demo, a citation block — beside every day. On Days 1, 4, 7 and 8 that produced six long
documents about specifications, sitting next to parts about version numbers, floating point,
`for` loops and dictionaries. A reader in Phase 1 does not need IEEE 754-2019 taught as a subject in
order to understand why `0.1 + 0.2` is not `0.3`; they need one honest sentence naming the standard,
inside the part that already has their attention. The effort that went into the paper documents was
effort that did not go into the parts. **The plan is amended rather than quietly ignored** (Principle
14), because `./m depth` enforced the paper contract and would otherwise have to be worked around.

**Amendment.**

- **Principle 19 (teach the primary source) is retired.** The `papers/` directory, the paper
  document, its thirteen sections, its demo project, and the `kind:` and `paper:` frontmatter keys
  are all removed from the contract.
- **A source is cited inline instead.** Where a part rests on one dated document, that document is
  named in the sentence that needs it, by **title · year · permanent identifier · canonical URL**,
  and — unchanged from v2.2.0 — **never by author, never "et al.", never by lab**. One or two
  sentences about what the document decided is the whole budget. A part that turns into a summary of
  a specification has stopped teaching its own idea.
- **New Principle 20 — plain language, real scenes.** The words are now part of the contract.
- **The four story rules** (Part 11.4): *ordinary, not clever* — the scene is a shared shopping
  list or a misspelled name, never a trading desk; *one small example, all the way through* — three
  rows, not three million, and the mechanism keeps using whatever the story picked up; *short, common
  words* — the technical term waits for §4, where it is defined; *true, not staged* — the mistake
  people actually make, in the order they actually make it.
- **The prose rules** (Part 11.4): complete sentences, correct punctuation, define on first use, one
  idea per sentence, and a hard rule that **a sentence the reader has to read twice is a defect**.
- **Part frontmatter is now eight keys**: `day`, `part`, `title`, `ids`, `level`, `prerequisites`,
  `prev`, `next`. Hub frontmatter loses `papers`.
- `scripts/depth_check.py` drops every paper check and gains two migration checks: a `papers/`
  directory inside a day folder, and a leftover `kind:` or `paper:` key in a part's frontmatter.
- `scripts/tracker.py` stops counting papers, and `docs/TRACKER.md` loses that row.

**Migration.** Six paper documents were deleted — Day 1 (*Semantic Versioning 2.0.0*, *PEP 440*),
Day 4 (*IEEE 754*), Day 7 (*UAX #15*), Day 8 (`listsort.txt`, *PEP 456*). Every one of them named a
source that the surrounding parts already taught, so the citations moved inline into those parts and
nothing was lost. All 128 part documents dropped their `kind:` and `paper:` keys; all ten hubs moved
to `plan_version: "v2.3.0"` and dropped `papers:`.

Days 4–10 were then rewritten to Principle 20 — every story replaced with an ordinary scene, every
document swept for grammar and punctuation — and Day 10 (`PY-10`, functions and the first
`src/setu/` module) was written for the first time. Days 0–3 keep their teaching; only their
frontmatter, their citations and their hub version changed.

**Explicitly unchanged.** No day, ID, phase boundary, gate, pin, dataset or principle 1–18 is
touched. The 240-day arc and all 276 IDs are identical to v2.2.0. The ten required part sections, the
twelve hub sections, the `<section>.<subtopic>` numbering rule, the folder-naming rule, the `level`
ladder and the no-clocks rule are all identical. This amendment removes a document type and adds a
writing standard; it moves nothing in the curriculum.

---

## v2.2.0 — 2026-08-26 — sources become subjects

**Trigger.** With ten days written, the plan taught ideas that came from named, dated documents and
never said so. Day 4 explained why `0.1 + 0.2` is not `0.3` without naming IEEE 754. Day 7 called
`unicodedata.normalize` without naming the annex that defines the four form names. Day 8 said
"CPython's sort is Timsort" in one sentence of an *In production* section and moved on. That gap
scales badly: from Phase 12 onward almost every subject in this plan — embeddings, transformers,
adapters, retrieval, agent loops — *is* somebody's named result, and a reader who has met only the
library call cannot tell a measured default from an arbitrary one. Nothing in the format asked the
question, so nothing recorded the difference between "there is no paper here" and "nobody looked".

**Amendment.**

- New **Principle 19 — teach the primary source**. Where an idea came from one dated document, that
  document is named, identified, linked **and taught in its own document**, in the day's `papers/`
  directory.
- New **`papers/` directory** beside `parts/`: `days/day-NN-<slug>/papers/<NN>-<slug>.md`, flat and
  numbered from `01` in reading order. A source belongs to the day, not to one section of its
  teaching — several parts across different sections routinely lean on the same document, and adding
  a source to a finished day must never renumber a part.
- **Two new required frontmatter keys on every part**: `kind` (`concept` or `paper`) and `paper`
  (`none`, or a list of identifiers). Neither has a default and neither may be omitted, because a
  missing field cannot be told apart from nobody having checked. `paper: none` is the correct and
  common answer for most Python-fundamentals subtopics.
- **A paper document carries thirteen sections** — the part's ten, plus **the citation** (title,
  year, permanent identifier, canonical URL fetched on the day of writing, and *what to actually
  read*), **the demo**, and **what did not survive**.
- **The demo is a runnable end-to-end mini project implementing that document's one contribution and
  nothing else**: a named folder, every file listed in full with no elisions, one command, and the
  **real** output pasted from an actual run. It closes by naming what it deliberately leaves out.
  Three files is a good size; more than five means it grew a feature the paper did not contribute.
- **Citations name no people.** Title · year · identifier (arXiv, DOI, PEP, RFC, standard annex) ·
  canonical URL. Never an author, never "et al.", never a lab. This extends the existing
  no-person-names rule rather than carving an exception out of it.
- **Specifications, standards and canonical implementation notes count as primary sources.** The
  test is not "was it refereed" but "is there one dated document that decided this, which the reader
  could open" — which is why Day 1 has a paper on PEP 440 and Day 8 has one on CPython's
  `listsort.txt`.
- Hubs gain a **`papers:` count** in frontmatter (`0` is an answer) and, where the day has papers, a
  `### The papers — papers/` block at the end of the §2 map — never mixed into a section's table.
- `scripts/depth_check.py` gains the enforcement: a missing `kind:`/`paper:` key, a `kind` outside
  `concept`/`paper`, a `kind: paper` file inside `parts/`, a paper filename that is not
  `<NN>-<slug>.md` or whose `part:` is not the matching `"PN"`, a gap in the paper numbering, a paper
  declaring `paper: none`, a paper missing one of its thirteen sections or carrying them out of
  order, a hub whose `papers:` count or §2 map disagrees with the directory, and — the check this
  amendment exists for — **a part that cites an identifier its day has no paper for**.
- `scripts/tracker.py` counts papers, so `docs/TRACKER.md` reports them beside the part count.

**Migration.** All 128 existing part documents gained `kind: concept` and `paper: none`; all ten
hubs moved to `plan_version: "v2.2.0"` and gained a `papers:` count. Six papers were written for the
four written days that genuinely rest on primary sources, each with its demo built and run before
its output was pasted:

| Day | Papers |
|---|---|
| 1 | *Semantic Versioning 2.0.0* · *PEP 440* |
| 4 | *IEEE 754* (with the 1991 ACM Computing Surveys survey as its readable companion) |
| 7 | *UAX #15 — Unicode Normalization Forms* |
| 8 | CPython's `listsort.txt` (with the CAV 2015 verification paper) · *PEP 456* and SipHash |

Days 0, 2, 3, 5, 6 and 9 rest on no primary source and say so, in every part's `paper: none`.
`./m depth` passes on all ten days.

**Explicitly unchanged.** No day, ID, phase boundary, gate, pin, dataset or principle 1–18 is
touched. The 240-day arc and all 276 IDs are identical to v2.1.0, the ten required part sections are
identical, and the numbering, folder-naming and no-clocks rules are untouched. Nothing moved out of
`parts/` except the four documents that had been written as paper parts under the first draft of this
amendment, before `papers/` existed.

---

## v2.1.0 — 2026-08-23 — folders that say what is in them

**Trigger.** With two days written, `days/` already read as `day-00-setup/`, `day-01/`, and every
day's `parts/` read as `01/ 02/ 03/ 04/`. Nothing in that tree says what any of it is about. To
find where version specifiers were taught you had to open a hub and read its §2 map — and that is
with 2 of 241 days on disk. At two hundred days it is a wall of numbers, and the numbers are
exactly the thing a reader does not remember.

**Amendment.** Part 11.2 and 11.3 only. Folder names now carry their subject:

- A **day folder** is `days/day-NN-<slug>/` — `day-00-setup`, `day-01-pins`. The slug names the
  day's subject in one to three kebab-case words.
- A **section folder** is `parts/NN-<slug>/` — the zero-padded section number, a hyphen, then one
  to three kebab-case words naming what the section covers: `parts/01-versions/`,
  `parts/02-pypi-index/`, `parts/03-freezing/`, `parts/04-drift/`.
- The slug names what is **inside**, never the position. `01-section-one` and `01-part-a` are bugs.
- **Part filenames are unchanged**: `<section>.<subtopic>-<kebab-slug>.md`. The number before the
  dot must still match the number the folder starts with.
- Cross-section links gain the slug — `../01-versions/1.3-<slug>.md`. Cross-day links become
  `../../../day-NN-<slug>/parts/NN-<slug>/<file>.md`. Same-section links are unchanged.
- **The number stays the handle.** `./m`, `scripts/depth_check.py` and `scripts/tracker.py` locate a
  day by globbing `days/day-NN-*` rather than rebuilding its name, so a slug can be corrected later
  without touching a tool. All three still resolve the old unslugged `day-NN` form, so an old folder
  is reported as a naming failure rather than as a missing day.
- `scripts/depth_check.py` gains two failures: a day folder that is not `day-NN-<slug>`, and a
  section folder that is not `NN-<slug>`. Its dead-link pass already catches a rename whose links
  were not updated.
- `./m` gains the three commands `days/README.md` had been documenting but which did not exist:
  `depth [N]`, `tracker`, and `parts N` (which prints a day's sections and their documents).
  `./m check` now runs the depth contract, as that file already claimed it did. `./m scaffold N`
  now creates `lab/` inside the day's real folder instead of minting a bare `days/day-NN/`.

**Migration.** Both written days were renamed and every link inside them rewritten:

| Was | Now |
|---|---|
| `days/day-00-setup/parts/01…04/` | `parts/01-toolchain/`, `02-skeleton/`, `03-m-script/`, `04-first-commit/` |
| `days/day-01/` | `days/day-01-pins/` |
| `days/day-01/parts/01…04/` | `parts/01-versions/`, `02-pypi-index/`, `03-freezing/`, `04-drift/` |

`./m depth` passes on both days. `docs/TRACKER.md` was regenerated.

**Explicitly unchanged.** No day, ID, phase boundary, gate, pin, dataset, principle, required part
section, hub section or `level` value is touched. The ten-section part contract, the numbering rule
and the no-clocks rule are identical to v2.0.0. This is a folder-naming amendment only — which is
why it is a minor bump and not a major one.

---

## v2.0.0 — 2026-08-22 — the depth contract

**Trigger.** Review of the written days (0–132) found the v1.0.0 single-file lesson format had
failed at scale. Day 127's lesson ran to 40 668 characters and put the entire
derivation of backpropagation under one `##` heading. Days 120–132 average ~38 000 characters. A
reader cannot revisit one subtopic without re-reading its neighbours, and there is no way to tell a
thinly-covered subtopic from a missing one.

**Amendment.**

- New **Principle 16 — depth over density**. A day is taught as a hub plus one document per
  subtopic, never as one long page.
- New **Principle 17 — a day is a unit of subject, not a unit of time**. No document carries a time
  estimate, a duration or a pace; nothing is ever trimmed to fit a schedule. A topic may take one
  sitting or five.
- New **Principle 18 — assume no prior knowledge, finish at production**. Every subtopic opens where
  a reader who has never met the idea can stand and closes with the real-system version of it: what
  changes at scale, what a senior engineer does differently, what a reviewer and an interviewer
  probe. Strong basics and advanced technique are the same document, in that order.
- New **Part 11 — the depth contract**: the three commitments, the folder shape, the
  `<section>.<subtopic>` numbering rule, the **ten** required sections of a part document (adding
  *The story* and a mandatory *In production*), the twelve required sections of a hub, the `level`
  ladder (`foundation → working → production`), splitting by idea boundary rather than length, and
  the seven failure modes this replaces.
- Days become `days/day-NN/{LESSON.md, CHECKLIST.md, parts/, lab/}`, with one folder per
  section inside `parts/` — `parts/01/1.1-<slug>.md`, `parts/02/2.3-<slug>.md` — so a day with
  twenty parts stays navigable.
- New `scripts/depth_check.py` and `./m depth [NN]` enforce the contract mechanically, including a
  hard failure on any time estimate found in a day folder (Principle 17) and on a `level` outside
  the three allowed values.
- `scripts/tracker.py` now reports a part count per day, so a thin day is visible from the progress
  table alone.

**Explicitly unchanged.** No day, ID, phase boundary, gate, pin, dataset or principle 1–15 is
touched. The 240-day arc and all 276 IDs are identical to v1.0.0. This is a documentation-format
and documentation-depth amendment only.

**On the 240 days.** Principle 17 does not shorten or lengthen the plan — it removes the *clock*
from it. Day numbers remain an index into the subject. A day whose subject is large is not
compressed to fit an evening; it is read across as many sittings as it needs, and `./m done N` is
gated on a ticked checklist and green checks, never on elapsed time.

**Migration.** All 133 v1.0.0 lessons were **deleted** on 2026-08-22 (commit `2b290ba`; recoverable
from git history if ever needed). They were not converted, because splitting a shallow page into
shallower pages is not depth — see Part 11.8. Every day is rewritten from the plan, from Day 0
forward, so `days/` refills gradually and `docs/TRACKER.md` reports the real position.

---

## v1.0.0 — 2026-08-21 — initial DS/GenAI plan

240 days, 30 phases (0–29), 27 modules, 276 IDs, 15 operating principles. Stack pins read from live
PyPI on 2026-08-21. Companion documents: `CURRICULUM_INDEX_DS.md`, `PINS_DS.md`,
`CAPSTONE_SETU.md`.
