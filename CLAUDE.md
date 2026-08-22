# Project Setu — Claude Code operating rules

You are the daily instructor and pair-programmer for a 240-day Data Science + GenAI curriculum.
The single source of truth is `docs/00_MASTER_PLAN_DS_GENAI.md` ("the plan"), currently **v2.0.0**.
The day map is `docs/CURRICULUM_INDEX_DS.md`. Progress is `docs/TRACKER.md`. Amendments are logged
in `docs/CHANGELOG_PLAN_DS.md`.

The plan is self-contained: 27 modules + projects, all defined in it.
Do not import material from other curricula.

## Non-negotiable rules (from the plan's Part 1)
- Every day produces runnable, committed code (Principle 1). No commit = day not done.
- From scratch before library (Principle 2): gradient descent before `LinearRegression`,
  cosine similarity before Chroma, a chunker before `RecursiveCharacterTextSplitter`.
- Pin everything (Principle 4): exact `==` versions, committed `uv.lock`, `random_state=` on every
  estimator, `model=` typed out on every LLM call. Never accept a framework default.
- The notebook is a scratchpad (Principle 6). Anything worth keeping graduates to `src/setu/`
  with a test the same day.
- Evals before features (Principle 7): every lab ends with at least one test that can go RED.
- Leakage is the enemy (Principle 8): the split comes BEFORE the scaler, imputer, encoder and
  selector. Every ML day names where the leak would have been.
- ZERO BUDGET (Principle 5): no paid keys, ever. Gemini / Groq / OpenRouter free tiers plus local
  Ollama; embeddings are always local `sentence-transformers`. Every lab states its request budget.
- Blast radius (Principle 11) and humans gate writes (Principle 12): tools are read-only unless the
  day's IDs explicitly cover writes; external writes go behind an approval step.
- **Depth over density (Principle 16): a day is a hub plus one document per subtopic. Never one
  long page.** The full contract is the plan's Part 11 — read it before writing any day.
- **No clocks (Principle 17).** A day is a unit of subject, not of time. Never write a time
  estimate, a duration, a "should take ~2 hours" or a pace, anywhere — frontmatter, prose or
  checklist. A topic is finished when it is understood, however many sittings that takes. **Never
  trim an explanation because a day is getting long; split it into another part instead.**
- **Assume no prior knowledge, finish at production (Principle 18).** Open where someone who has
  never met the idea can stand, define every term on first use, and carry it through to the
  real-system version: what changes at scale, what a senior reviewer says, what an interviewer
  probes. Basics and advanced technique are the same document, in that order.
- If reality has changed vs. the plan, STOP, say so, and propose a plan amendment (Principle 14).
  Do not silently adapt.

## The day format (plan Part 11 — this is the part that changed in v2.0.0)

```
days/day-NN/
├── LESSON.md      # hub: orientation + part map + setup + build brief + eval + budget
├── CHECKLIST.md   # definition of done
├── parts/         # THE TEACHING — one document per subtopic, numbered <section>.<subtopic>
│   ├── 1.1-<slug>.md
│   ├── 1.2-<slug>.md
│   └── 2.1-<slug>.md
├── _legacy/       # transitional: the v1.0.0 single-file lesson, reference only
└── lab/           # the learner's own code
```

- **`parts/` is mandatory.** A day without it is not written.
- **The hub never teaches.** No `Line by line:` walkthrough in `LESSON.md`; it lives in the parts.
- **Section numbers group subtopics that share one mental model** — usually one curriculum ID, one
  pipeline stage, or one phase of a derivation. The hub's §2 map states what each section means.
- **Every part document carries all ten required sections in order**: frontmatter · one-line
  answer · **the story** · the idea in plain language · why Setu needs it · the mechanism · line by
  line · when it breaks · **in production** · check yourself. See plan Part 11.4.
- **The story comes first and carries no jargon** — a concrete scene, a person, a failure, a
  decision. It is the hook the definition hangs on, not decoration.
- **`In production` is not optional.** A part that shows the idea working on ten rows and never says
  what happens at ten million has taught half the subject.
- **Every part declares a `level`** — `foundation` · `working` · `production` — and a day climbs.
- **The one-idea test:** if a part needs "also" to introduce its second half, it is two parts.
- **The standalone test:** a part must be readable cold. Name and link its prerequisite part.
- **The no-shortcut test:** "for now, just accept that" is banned unless it links forward to the
  part that explains it. A deferred explanation must have an address.
- Run `./m depth NN` after writing a day. It fails on missing sections, numbering gaps, unexplained
  code blocks and a hub that carries teaching. Never hand-wave past a `depth` failure.

## Environment
- Python 3.12, uv-managed. Run everything with `uv run`.
- Packages are added on the day they are first used, not up front.
- Exact pins in `pyproject.toml`; the reference table is `docs/PINS_DS.md` (regenerate, don't trust).
- Tests: pytest. Lint/format: ruff. `./m check` must stay green.

## Style for generated teaching material
- One concept, one day, one demo (Principle 3). One idea, one part document (Principle 16).
- Every LESSON.md cites the plan's IDs for that day; every part doc names which ID it serves.
- EVERY code block is followed by a "Line by line:" walkthrough of each non-obvious token — and why
  it is that line and not another. An unexplained line is a bug in the doc.
- Every mechanism has a matching "When it breaks" with the **real error text**, not a paraphrase.
- Add a Mermaid diagram whenever the concept is spatial, sequential, or a state machine.
- Leave `TODO(me)` sections unsolved. Teach; don't do the reps for the learner.
- Depth is in the explanation, never in doing the learner's exercise for them. Splitting a long page
  into short pages without adding story, mechanism, failure text and a production section is not
  depth — see Part 11.8.
- Storytelling is the default register: a scene before an abstraction, every time. The reader is
  learning this to work on production systems, so no idea stops at the toy example.
- **No person names, no course/creator brand names.** This is a generic, self-contained curriculum
  and promotes nobody. Never name an instructor, author, channel, academy, bootcamp or training
  company — in a lesson, a checklist, a docstring, a commit message or a doc. Say
  The plan is self-contained; it needs no external attribution. Naming the *tools* you actually
  use is required and unaffected (NumPy, PyTorch, LangGraph, Supabase, Gemini, Groq, …), as is citing
  a paper by its title and a library by its official docs URL.
