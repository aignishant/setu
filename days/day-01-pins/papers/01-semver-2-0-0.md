---
day: 1
part: "P1"
title: "The document behind the three numbers — Semantic Versioning 2.0.0"
ids: []
level: working
kind: paper
paper: ["SemVer 2.0.0"]
prerequisites: ["1.1", "1.2"]
prev: "../parts/04-drift/4.2-drift-and-the-amendment-protocol.md"
next: "02-pep-440.md"
---

# The document behind the three numbers: *Semantic Versioning 2.0.0*

## One-line answer

*Semantic Versioning 2.0.0* is a short public specification that converts a three-number label into
a **promise about breakage**, written in the MUST/SHOULD language of a standards document — and its
one structural weakness is that it binds only the people who chose to follow it, which is why
[1.1](../parts/01-versions/1.1-semantic-versioning.md) called it a social convention rather than a
guarantee.

---

## The citation

| Field | Value |
|---|---|
| **Title** | *"Semantic Versioning 2.0.0"* |
| **Version cited** | 2.0.0 — the version number of the specification is itself a semantic version |
| **Identifier** | `SemVer 2.0.0` (the spec has no DOI; its version string is its identifier) |
| **Canonical URL** | <https://semver.org/spec/v2.0.0.html> — fetched 2026-08-25 |
| **Licence** | Creative Commons CC BY 3.0, which is why anyone may implement it |

**What to actually read.** The whole document is a page of eleven numbered clauses; you can read all
of it. If you read only part, read **clause 8** (what a MAJOR bump means), **clause 4** (the
`0.y.z` carve-out that swallows half of PyPI) and **clause 11** (precedence, which is the only
clause with an algorithm in it).

**On authors.** This plan cites documents, never people — a specification is findable by its title
and version, and that is the whole reason a specification has a version.

---

## The story

Before 2010 the question "what number do I publish this as?" had no shared answer. A maintainer who
had rewritten half a library and a maintainer who had fixed a typo both stood at the same prompt and
picked a number that *felt* right. Version 1.0 meant "I am nervous but proud". Version 0.9 meant
"still nervous". Some projects counted upward forever — release 147, then 148 — and some pinned the
number to the year.

The consumers of those packages had a harder problem. A build server that pulled the newest release
each night had exactly one question: *is this one going to break me?* The number in front of it was
the only clue available, and the number meant a different thing for every project it downloaded. So
teams did the only rational thing: they wrote down the exact release that had worked, and never
moved. Software froze at the version where somebody had last had a good day.

Then someone wrote the promise down, gave it a name, and published it under a licence that let
anyone adopt it. Nothing was invented — projects had used major/minor/patch informally for years.
What changed was that the meaning stopped being folklore held privately by each maintainer and
became **one document that a consumer could point at and say: you said this number would be safe.**

That is the entire contribution, and it is worth understanding exactly, because everything Day 1
does with `~=`, `>=` and `==` is an attempt to trade against a promise this document defines.

---

## The idea in plain language

The specification says: a version is not a measure of progress, it is a **claim about
compatibility with your own public API**.

Three ideas do all the work.

**First, the public API is the unit.** The document is explicit that a project using semantic
versioning MUST declare a public API — the functions, classes and behaviour other people are allowed
to depend on. Everything else is private and may change at any moment without a version bump. A
project that never says what its public API is cannot meaningfully version itself, because there is
nothing for the promise to be *about*.

**Second, the change decides the number, not the other way round.** The clauses are written as
obligations on the maintainer:

> "MAJOR version X (X.y.z | X > 0) MUST be incremented if any backward incompatible changes are
> introduced to the public API."

> "Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backward compatible functionality is
> introduced to the public API."

> "Patch version Z (x.y.Z | x > 0) MUST be incremented if only backward compatible bug fixes are
> introduced."

Read them in that direction. You do not decide to "do a 2.0 release" and then look for things to
break; you break something, and the number 2 is imposed on you. **MUST** is standards language — it
is not advice, it is the condition for being allowed to say you follow the spec at all.

**Third, and this is the clause that matters most in practice, none of it applies below 1.0.0:**

> "Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The
> public API SHOULD NOT be considered stable."

A `0.x` release makes **no promise whatsoever**. Not a weakened promise — none. A huge share of the
packages this plan will install spend years at `0.x`, and every specifier you write against one of
them is a bet with no contract behind it. That single clause is the reason
[1.2](../parts/01-versions/1.2-version-specifiers.md) treats `~=` as unsafe on a young package: `~=0.4.1`
allows `0.4.9`, and the document being followed says `0.4.9` may change anything it likes.

---

## Why Setu needs it

- **[1.1](../parts/01-versions/1.1-semantic-versioning.md) taught the shape** — MAJOR.MINOR.PATCH and what
  each position claims. This part is where that claim comes from, so that "a version is a promise"
  stops being something the lesson asserted and becomes something you can go and check.
- **[1.2](../parts/01-versions/1.2-version-specifiers.md) trades against it.** Every specifier is a bet on
  a clause of this document. `>=2.0` bets that clause 8 will be honoured. `~=2.2` bets the same
  thing with a ceiling. `==2.2.1` declines to bet at all — which is what Principle 4 tells you to do
  in an application.
- **[4.1](../parts/04-drift/4.1-the-three-breaking-changes.md) is what happens when the bet loses**: the
  three breaking changes already sitting in this stack, each of which was announced correctly by a
  number that a specifier had already agreed to accept.
- **[the PEP 440 paper](02-pep-440.md) is the other half of the story.** Python does not use this specification;
  it uses PEP 440, which is a different document with different rules. Reading them next to each
  other is the point, and the disagreement between them is not academic — it changes which files
  `uv` will install.
- **Downstream:** the pin bumps you will do for the rest of this plan, and the freshness check on
  Day 1's `4.2`, are both this document being applied by hand, on a schedule.

---

## The mechanism

Ten of the eleven clauses are prose obligations. Clause 11 is different: it is an **algorithm**, and
an algorithm can be implemented and tested. It defines *precedence* — which of two versions is
"newer" — and it is where most naïve implementations go wrong.

The rules, in the spec's order:

1. Compare MAJOR, then MINOR, then PATCH, **numerically**.
2. A version *with* a pre-release (`1.0.0-alpha`) has **lower** precedence than the same version
   without one (`1.0.0`).
3. Two pre-releases are compared field by field, splitting on `.`:
   - numeric fields compare numerically;
   - alphanumeric fields compare in ASCII sort order;
   - a numeric field always ranks **lower** than an alphanumeric one;
   - if all preceding fields are equal, the version with **more** fields wins.
4. Build metadata (`+build.1`) is **ignored entirely** when determining precedence.

From scratch before library (Principle 2) — the whole of clause 11 in one function:

```python
"""Clause 11 of Semantic Versioning 2.0.0, implemented from the specification text."""


def precedence_key(version: str) -> tuple:
    """A sort key implementing SemVer 2.0.0 clause 11. Build metadata is discarded."""
    core, _, pre = version.partition("+")[0].partition("-")
    major, minor, patch = (int(n) for n in core.split("."))
    if not pre:
        return (major, minor, patch, 1, ())
    fields = []
    for field in pre.split("."):
        if field.isdigit():
            fields.append((0, int(field), ""))
        else:
            fields.append((1, 0, field))
    return (major, minor, patch, 0, tuple(fields))


spec_example = [
    "1.0.0",
    "1.0.0-rc.1",
    "1.0.0-beta.11",
    "1.0.0-beta.2",
    "1.0.0-beta",
    "1.0.0-alpha.beta",
    "1.0.0-alpha.1",
    "1.0.0-alpha",
]
for version in sorted(spec_example, key=precedence_key):
    print(version)
```

**Line by line:**

- `version.partition("+")[0]` — build metadata is stripped *first*, before anything else is parsed,
  because clause 10 says it MUST be ignored for precedence. Doing it first means no later line has
  to remember it exists.
- `.partition("-")` — splits `1.0.0-alpha.1` into core `1.0.0` and pre-release `alpha.1`. `partition`
  rather than `split("-")` because it returns a fixed three-tuple even when there is no `-`, so
  `pre` is `""` instead of raising or producing a one-element list.
- `int(n) for n in core.split(".")` — numeric comparison, not string comparison. This is the same bug
  [1.1](../parts/01-versions/1.1-semantic-versioning.md) demonstrated with `sorted(['1.9.0','1.10.0'])`:
  as text, `"1.10.0" < "1.9.0"`, because `1` sorts before `9`.
- `return (major, minor, patch, 1, ())` — the `1` is rule 2 encoded as a number. A release with no
  pre-release sorts **above** one with a pre-release, so the no-pre-release case gets the higher
  flag. The empty tuple keeps every key the same length and type, which is what lets Python compare
  two keys without a `TypeError`.
- `(0, int(field), "")` for a numeric field and `(1, 0, field)` for an alphanumeric one — rule 3's
  "numeric identifiers always have lower precedence than alphanumeric identifiers", encoded in the
  first slot of each field's key. `0` before `1`, so `alpha.1` sorts below `alpha.beta`.
- `int(field)` in slot two — this is why `beta.11` sorts **above** `beta.2`. Compared as text it
  would not: `"11" < "2"`. That single line is the most commonly wrong line in a hand-rolled version
  comparator.
- The two branches keep the tuple shape identical `(int, int, str)` in both cases; if one branch
  returned a two-element tuple, comparing a numeric field against an alphanumeric one would raise.
- `sorted(..., key=precedence_key)` — the list is deliberately written in reverse of the spec's
  documented order, so a correct implementation has to actually reorder it rather than leave it
  alone.

Running it reproduces the specification's own worked example, in the spec's order:

```text
1.0.0-alpha
1.0.0-alpha.1
1.0.0-alpha.beta
1.0.0-beta
1.0.0-beta.2
1.0.0-beta.11
1.0.0-rc.1
1.0.0
```

Two things in that output are worth stopping on. `1.0.0-alpha.1` sorts **below** `1.0.0-alpha.beta`
— a number ranks under a word. And `1.0.0-beta.2` sorts **below** `1.0.0-beta.11` — eleven is more
than two, which is only true if you remembered to parse the field as an integer.

---

## The demo

One project, one feature: **a release gate that refuses a version number which under-claims the
change it carries**. That is the specification's contribution and nothing else — no packaging, no
changelog generation, no git tags, no network.

```text
semver-gate/
├── semver_gate.py        # clauses 8-11, and nothing else
└── test_semver_gate.py   # the spec's own examples, as tests that can go red
```

`semver_gate.py`, in full:

```python
"""Semantic Versioning 2.0.0, clauses 8-11 only: what to bump, and what is newer."""


def precedence_key(version: str) -> tuple:
    """Clause 11. Build metadata is discarded before anything else is parsed (clause 10)."""
    core, _, pre = version.partition("+")[0].partition("-")
    major, minor, patch = (int(n) for n in core.split("."))
    if not pre:
        return (major, minor, patch, 1, ())
    fields = tuple((0, int(f), "") if f.isdigit() else (1, 0, f) for f in pre.split("."))
    return (major, minor, patch, 0, fields)


def next_version(current: str, change: str) -> str:
    """Clauses 8, 9 and 7: the change decides the number, not the maintainer's mood."""
    major, minor, patch = (int(n) for n in current.partition("-")[0].split("."))
    if change == "breaking":
        return f"{major + 1}.0.0"
    if change == "feature":
        return f"{major}.{minor + 1}.0"
    if change == "fix":
        return f"{major}.{minor}.{patch + 1}"
    raise ValueError(f"unknown change kind: {change!r}")


def gate(previous: str, proposed: str, change: str) -> tuple[bool, str]:
    """Refuse a release whose number under-claims the change it carries."""
    required = next_version(previous, change)
    if precedence_key(proposed) < precedence_key(previous):
        return False, f"{proposed} does not follow {previous} (clause 11)"
    if precedence_key(proposed) < precedence_key(required):
        return False, f"a {change} change requires at least {required}, not {proposed} (clause 8)"
    return True, f"{proposed} is a legal successor to {previous}"
```

**Line by line:** — `precedence_key` is the mechanism above, unchanged, so only what is new is
walked through here.

- `next_version(current, change)` — the specification read in its own direction. The input is *what
  kind of change was made*; the output is the number that change obliges you to publish. There is no
  argument for "which number do you want", because clause 8 does not offer one.
- `current.partition("-")[0]` — a pre-release suffix is dropped before parsing the core, so
  `next_version("2.0.0-rc.1", "fix")` reasons about `2.0.0`. The gate is about the release contract,
  and clause 9 says a pre-release is not yet under it.
- `f"{major + 1}.0.0"` — minor and patch reset to zero on a major bump, which is clause 8's second
  sentence. Writing `f"{major + 1}.{minor}.{patch}"` would be the same mistake as calling a rewrite
  `2.4.2`: the number would no longer describe the change.
- `raise ValueError(f"unknown change kind: {change!r}")` — no default branch. A change nobody
  classified must stop the release rather than silently receive a patch bump; a default here is the
  hole every real release process eventually falls through (Principle 4's habit, applied to process
  rather than to pins).
- `gate(...)` returns `(bool, str)` rather than raising — the caller is a release script that wants
  to print the reason, and the reason names the clause. A gate that says "invalid version" teaches
  nobody; one that says `(clause 8)` sends the reader to the document.
- The first check is *ordering*, the second is *magnitude*. They are separate because they fail for
  different reasons: `2.4.0` after `2.4.1` is going backwards, while `2.4.2` for a breaking change is
  going forwards by too little.

`test_semver_gate.py`, in full:

```python
"""The specification's own examples, as tests that can go red."""

from semver_gate import gate, next_version, precedence_key

SPEC_ORDER = [
    "1.0.0-alpha",
    "1.0.0-alpha.1",
    "1.0.0-alpha.beta",
    "1.0.0-beta",
    "1.0.0-beta.2",
    "1.0.0-beta.11",
    "1.0.0-rc.1",
    "1.0.0",
]


def test_clause_11_reproduces_the_specs_own_ordering():
    shuffled = sorted(SPEC_ORDER, reverse=True)
    assert sorted(shuffled, key=precedence_key) == SPEC_ORDER


def test_clause_10_ignores_build_metadata():
    assert precedence_key("1.0.0+build.2") == precedence_key("1.0.0+build.1")


def test_clause_8_a_breaking_change_costs_a_major():
    assert next_version("2.4.1", "breaking") == "3.0.0"
    assert next_version("2.4.1", "feature") == "2.5.0"
    assert next_version("2.4.1", "fix") == "2.4.2"


def test_the_gate_refuses_an_underclaimed_release():
    ok, why = gate("2.4.1", "2.4.2", "breaking")
    assert not ok
    assert "requires at least 3.0.0" in why
```

**Line by line:**

- `SPEC_ORDER` is copied from clause 11 of the document, in the document's order — the test's oracle
  is the specification itself, not this implementation's current behaviour. That is the difference
  between a test and a snapshot.
- `sorted(SPEC_ORDER, reverse=True)` — the input is deliberately scrambled before sorting, so an
  implementation that returns its input unchanged fails. A test that sorts an already-sorted list
  passes for the wrong reason.
- `test_clause_10_ignores_build_metadata` asserts **equality of the keys**, not `not (a > b)`. Clause
  10 says the two versions rank equal, and equal is a stronger claim than "not greater" — this is the
  assertion that goes red against `packaging`, as [When it breaks](#when-it-breaks) shows.
- `test_clause_8_...` checks all three bump kinds in one test because they are one rule read three
  ways; splitting them would suggest they could be true independently.
- `assert "requires at least 3.0.0" in why` — the test pins the *reason*, not just the refusal. A
  gate that refuses everything would pass a `assert not ok` test and be useless.

Run it:

```console
$ uv run --with pytest python -m pytest -q
....                                                                     [100%]
4 passed in 0.04s

$ uv run python -c "
from semver_gate import gate
for prev, proposed, change in [('2.4.1','2.4.2','fix'),('2.4.1','2.4.2','breaking'),('2.4.1','2.5.0','feature'),('2.4.1','2.4.0','fix')]:
    ok, why = gate(prev, proposed, change)
    print(('PASS' if ok else 'FAIL'), why)"
PASS 2.4.2 is a legal successor to 2.4.1
FAIL a breaking change requires at least 3.0.0, not 2.4.2 (clause 8)
PASS 2.5.0 is a legal successor to 2.4.1
FAIL 2.4.0 does not follow 2.4.1 (clause 11)
```

Line two is the specification doing its job: the same number, `2.4.2`, is legal for a fix and illegal
for a breaking change, and nothing about the *string* distinguishes them. The number is a claim about
the change, and only the change can decide it.

**What this demo deliberately leaves out.** A real release tool infers `change` from commit messages
or an API diff, writes the tag, updates a changelog, and refuses to run on a dirty working tree —
none of which is the specification's contribution. The moment `change` is inferred rather than
supplied, the interesting question stops being "what does clause 8 require" and becomes "is the
inference correct", which is a different subject and belongs to a different day.

---

## When it breaks

The interesting failure is not in the implementation above. It is that **Python does not implement
this specification**, and the tool you are pinning with will happily accept a version string this
document defines and give it a different meaning.

```python
from packaging.version import Version

print(Version("1.0.0-alpha.1"))
print(Version("1.0.0-alpha.beta"))
```

The first line prints:

```text
1.0.0a1
```

The second raises:

```text
packaging.version.InvalidVersion: Invalid version: '1.0.0-alpha.beta'
```

Read what just happened. `1.0.0-alpha.1` is a legal SemVer version, and Python's packaging layer did
not reject it — it **rewrote** it to `1.0.0a1`, a PEP 440 pre-release. The string you published and
the string the installer resolves against are not the same string. Meanwhile `1.0.0-alpha.beta` is
equally legal SemVer, and it is simply refused, because PEP 440 has no way to express a pre-release
whose label is a word followed by another word.

The second failure is quieter and worse:

```python
from packaging.version import Version

print(Version("1.0.0+build.2") > Version("1.0.0+build.1"))
```

```text
True
```

Clause 10 of the specification says build metadata MUST be **ignored** when determining precedence —
those two versions are required to rank equal. Python orders them, because in PEP 440 the part after
`+` is a *local version identifier* and it participates in comparison. A release process that puts a
build number after `+` and assumes it cannot affect resolution is relying on a clause of a document
that Python never agreed to.

**The smallest fix:** do not treat a SemVer string and a PEP 440 string as the same kind of object.
If you need SemVer precedence, implement clause 11 as above. If you need to know what `uv` will
install, ask `packaging` — and see [the PEP 440 paper](02-pep-440.md) for the document it is actually obeying.

---

## What did not survive

This specification is unusually durable — 2.0.0 has stood unchanged for over a decade, which almost
nothing in this plan's stack can say. What did not survive is not the text but several of the
assumptions around it.

**The `0.y.z` clause swallowed the ecosystem.** Clause 4 was written as a short initial-development
phase before a project stabilised. In practice a large share of widely-deployed packages live at
`0.x` permanently, some with millions of downloads. The clause is honoured to the letter and
therefore promises nothing, which inverts the document's purpose for a big fraction of the packages
you will actually install. When you meet a `0.x` dependency, the correct reading is not "young
project" but "no contract".

**"Backward incompatible" turned out to be a judgement, not a fact.** The spec does not — cannot —
define which observable behaviours are part of your public API. Is a fixed bug a patch, or a
breaking change for anyone who worked around it? Is a performance regression breaking? Is a changed
error *message*? Every maintainer answers differently and every one of them can claim compliance.
This is precisely why Principle 4 does not trust the number: the number is honest and the definition
underneath it is elastic.

**Python declined it.** The largest fact about this document, from where you are standing, is that
the ecosystem you are pinning in chose a different specification — one that predates semver as an
idea in Python, has different comparison rules, a different pre-release grammar, and normalises
input rather than rejecting it. Learning semver and assuming it governs `pip`, `uv` or PyPI is the
single most common way this document is misapplied. It governs your *reading* of a maintainer's
intent; PEP 440 governs what gets installed.

**Automation moved past hand-application.** The document assumes a human decides the bump. Modern
release tooling derives the number from commit-message conventions or from an API diff instead —
which does not contradict the spec, but does mean that in a real project the number is often
produced by a rule nobody re-examines, and a mislabelled commit silently mislabels a release.

---

## In production

**What a professional does with this document.** They read a dependency's version number as
*evidence about the maintainer*, not as a guarantee about the code — and they check three things
before trusting a range: does the project state a public API at all; is it above `1.0.0`; and does
its changelog show major bumps ever actually happening? A project at `3.14.2` with a history of
majors is making a real promise. A project at `0.9.47` with 400 releases and no `1.0` is not
promising anything, whatever its README says.

**What changes at scale.** In a monorepo with hundreds of internal packages, semver applied
literally causes *version churn*: one breaking change in a core library forces a major bump, which
forces every consumer to bump, which cascades. Large organisations respond by narrowing what counts
as the public API — often to an explicitly exported surface — so that most changes are legally
internal. The specification supports this; it says the public API is whatever you declare it to be.
The failure mode is declaring nothing and then arguing after the fact.

**The review comment a senior engineer leaves.** On a pull request that writes `>=2.0` against a
dependency: *"This trusts clause 8 of a specification the maintainer never signed. What is our plan
for the night 3.0 ships?"* On a pull request that writes `~=0.4.1`: *"That package is at `0.x` —
there is no compatibility promise to be compatible with. Pin it exactly and add it to the freshness
check."*

**The interview question.** *"You depend on a library at 2.4.1 and they release 2.4.2. Do you take
it automatically?"* The shallow answer is "yes, patch releases are safe". The answer that shows you
have read the document is: *the specification obliges them to make it safe, and I have no way to
verify they did; a patch release is a claim by the maintainer, so I take it deliberately, on a
schedule, with a lockfile and a test suite that would notice.* Then the follow-up, which is the real
question: *"and if the library were at 0.4.1?"* — where the correct answer is that there is no
clause to appeal to at all.

---

## Check yourself

Run this now:

```bash
uv run python -c "
from packaging.version import Version
print(Version('1.0.0-alpha.1'), '|', Version('1.0.0+build.2') > Version('1.0.0+build.1'))
"
```

You should see `1.0.0a1 | True` — a legal SemVer string rewritten into a different specification's
grammar, and a comparison that clause 10 says MUST NOT be decided.

**Say this out loud, without scrolling up:** *a package you depend on is at version `0.8.3` and has
just released `0.9.0`. Quote the clause that tells you what that bump promises — and then say what
you are actually going to do about it.*

Next: [PEP 440 — the specification Python actually obeys](02-pep-440.md)
