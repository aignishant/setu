#!/usr/bin/env python
"""Enforce the plan's Part 11 depth contract on a day folder.

A day is written when it is a hub plus one document per subtopic (Principle 16), each taken from
zero prior knowledge through to production (Principle 18), with no clock anywhere (Principle 17).
This script is the machine-readable half of that contract: it cannot judge whether an explanation
is good, but it can refuse a day that has no parts, a numbering gap, a missing required section, a
code block nobody walked through, a time estimate, a dead cross-part link, a part loose outside its
section folder, a day or section folder whose name does not say what is inside it, or a hub that
quietly went back to teaching.

Since plan v2.3.0 it also refuses the two shapes left behind by the retired v2.2.0 paper format:
a papers/ directory inside a day folder, and a leftover `kind:` or `paper:` key in a part's
frontmatter. A source is now cited inline, in the sentence that needs it, by title, year, identifier
and URL (Principle 19 retired, Part 11.4).

Since plan v2.4.0 it also enforces the size contract of Part 11.7 - three to five parts a day, and
ceilings on the prose words in a part, in a day and in a hub - plus the merged "The idea, through a
story" section and the new "The code you write" section (Part 11.4). A day is checked against the
contract version stamped in its own hub, so a day written before the amendment is not retroactively
broken; from CUTOVER_DAY onward a hub must carry the current stamp.

    uv run python scripts/depth_check.py          # every day that has a parts/ directory
    uv run python scripts/depth_check.py 4        # just day 4
    uv run python scripts/depth_check.py 4 5 6    # several days

Exit code 0 means every checked day satisfies the contract. Anything else is a failure list.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAYS = ROOT / "days"
PLAN = ROOT / "docs" / "00_MASTER_PLAN_DS_GENAI.md"
INDEX = ROOT / "docs" / "CURRICULUM_INDEX_DS.md"

# The one place the plan's version is written down. Every hub's frontmatter is checked against it
# and so is the curriculum index, so a version bump is one edit here plus the documents themselves.
PLAN_VERSION = "v2.4.0"

# Plan v2.4.0 sized a day to one sitting and reshaped the part contract. Days written before it are
# valid days, not broken ones, so each day is judged against the contract stamped in its own hub -
# and from this day number onward, only the current stamp is accepted. Below it, either stamp passes
# and the older one selects the older section list.
CUTOVER_DAY = 33
LEGACY_VERSION = "v2.3.0"

# The index is the day list every other tool reads: the tracker builds from it, ./m brief projects
# from it, and a day is written against it. It is generated from the plan's Part 4 and Part 5, so
# when the plan moves and the index does not, every one of those tools is quietly wrong. Comparing
# the two version stamps would only catch a forgotten edit to a stamp; these checks compare the
# content, so the stamp means something.
PLAN_PHASE_RE = re.compile(r"^\|\s*\*\*(\d+)\*\*\s*\|\s*(\d+)[–—-](\d+)\s*\|", re.M)
INDEX_PHASE_RE = re.compile(r"^##\s+Phase\s+(\d+)\s+·\s+.+?·\s+Days?\s+(\d+)[–—-](\d+)\s*$", re.M)
MATRIX_ID_RE = re.compile(r"^\|\s*([A-Z]{2,4}-\d+)\s", re.M)
ANY_ID_RE = re.compile(r"[A-Z]{2,4}-\d+")

KEBAB = r"[a-z0-9]+(?:-[a-z0-9]+)*"

# parts/<NN>-<slug>/<section>.<subtopic>-<kebab-slug>.md
#   ->  "parts/02-the-split/2.3-why-the-split-comes-first.md"
PART_NAME_RE = re.compile(rf"^(\d+)\.(\d+)-({KEBAB})\.md$")

# A section folder is the zero-padded section number, a hyphen, then a short slug naming what the
# section covers - 01-toolchain, 02-skeleton, 03-m-script (plan v2.1.0, Part 11.2). A bare 01/
# forces the reader to open a file to find out what section 1 is about.
SECTION_DIR_RE = re.compile(rf"^(\d{{2}})-({KEBAB})$")

# A day folder carries the same kind of label: day-<NN>-<slug>, e.g. day-00-setup, day-01-pins.
# Since plan v2.4.0 the number may be followed by a single lowercase letter - day-33a-<slug>,
# day-33b-<slug> - which marks one sitting of a subject too large for one day (Part 11.7). The
# number is still the plan's day; the letter is only the split.
DAY_DIR_RE = re.compile(rf"^day-(\d{{2}})([a-z]?)-({KEBAB})$")

# The ten required sections of a part document, in order (plan Part 11.4). Section 1 is the
# frontmatter, checked separately; these are the nine that appear in the body. There are two lists
# because v2.4.0 merged "the story" and "the idea in plain language" into one section and added
# "the code you write"; a day is checked against the one its hub is stamped for.
_ONE_LINE = ("one-line answer", re.compile(r"^#{2,3}\s.*one[- ]line answer", re.I | re.M))
_WHY_SETU = ("why Setu needs it", re.compile(r"^#{2,3}\s.*why setu needs it", re.I | re.M))
_MECHANISM = ("the mechanism", re.compile(r"^#{2,3}\s.*mechanism", re.I | re.M))
_LINE_BY_LINE = (
    "line by line",
    re.compile(r"^#{2,3}\s.*line by line|^\*\*Line by line:?\*\*", re.I | re.M),
)
_BREAKS = ("when it breaks", re.compile(r"^#{2,3}\s.*when it breaks", re.I | re.M))
_PRODUCTION = ("in production", re.compile(r"^#{2,3}\s.*in production", re.I | re.M))
_CHECK = ("check yourself", re.compile(r"^#{2,3}\s.*check yourself", re.I | re.M))

PART_SECTIONS_V23 = [
    _ONE_LINE,
    ("the story", re.compile(r"^#{2,3}\s.*the story", re.I | re.M)),
    ("the idea in plain language", re.compile(r"^#{2,3}\s.*idea in plain language", re.I | re.M)),
    _WHY_SETU,
    _MECHANISM,
    _LINE_BY_LINE,
    _BREAKS,
    _PRODUCTION,
    _CHECK,
]

PART_SECTIONS_V24 = [
    _ONE_LINE,
    # "The idea, through a story" - one section since v2.4.0. The pattern accepts any heading that
    # names both halves, so a day may title it for its own subject without inventing a new contract.
    (
        "the idea, through a story",
        re.compile(r"^#{2,3}\s.*\bidea\b.*\bstory\b|^#{2,3}\s.*\bstory\b.*\bidea\b", re.I | re.M),
    ),
    _WHY_SETU,
    _MECHANISM,
    _LINE_BY_LINE,
    ("the code you write", re.compile(r"^#{2,3}\s.*code you write", re.I | re.M)),
    _BREAKS,
    _PRODUCTION,
    _CHECK,
]

# A v2.4.0 part that still carries the old pair as separate headings is an unfinished migration: it
# would otherwise pass, because "the idea, through a story" can match neither and the merge is the
# whole point of the amendment.
SPLIT_STORY_RE = re.compile(r"^#{2,3}\s.*idea in plain language", re.I | re.M)

# The size contract, plan Part 11.7. Prose words are counted with code fences removed, because a
# fence is read at a different speed; the code ceiling is what stops a part hiding its bulk inside
# one. These are hard ceilings - the targets that sit under them live in the plan, not here.
MAX_PARTS_PER_DAY = 6
MAX_PART_WORDS = 1300
MAX_PART_CODE_LINES = 150
MAX_DAY_WORDS = 4500
MAX_HUB_WORDS = 800

PART_FRONTMATTER_KEYS = [
    "day",
    "part",
    "title",
    "ids",
    "level",
    "prerequisites",
    "prev",
    "next",
]

# Plan v2.3.0 retired the paper document, so these two keys are no longer part of the contract. A
# file that still carries one was written against v2.2.0 and never migrated - which is worth saying
# out loud, because a stale `paper: none` reads like a promise the format no longer makes.
RETIRED_KEYS = {"kind", "paper"}

# Principle 18: every part declares where it leaves the reader.
LEVELS = {"foundation", "working", "production"}

# Principle 17: a day is a unit of subject, not a unit of time. Nothing in a day folder may
# suggest a duration or a pace - not "takes 20 minutes", not "reading_minutes", not "Day 3 of 4".
TIME_BANS = [
    (
        re.compile(
            r"^\s*(reading_minutes|duration|time_estimate|minutes|est_time)\s*:", re.I | re.M
        ),
        "a duration field in frontmatter",
    ),
    (
        re.compile(r"\b\d+\s*[-–]?\s*\d*\s*(minutes?|mins?|hours?|hrs?)\b(?!\s*(of |the ))", re.I),
        "a time estimate in the prose",
    ),
    (re.compile(r"\*\*Time:?\*\*", re.I), "a **Time:** line"),
    (re.compile(r"should take (about |around |roughly )?\w+", re.I), "a 'should take ...' pace"),
]

HUB_FRONTMATTER_KEYS = [
    "day",
    "phase",
    "phase_name",
    "title",
    "ids",
    "principles",
    "kind",
    "plan_version",
    "parts",
    "generated",
    "status",
    "lab_scaffolded",
    "commit",
]

# The twelve required hub sections (plan Part 11.4). Frontmatter and the yesterday/today/tomorrow
# blockquote are checked separately; these ten are the numbered headings.
HUB_SECTIONS = [
    (1, "The story"),
    (2, "The map"),
    (3, "Setup"),
    (4, "Build brief"),
    (5, "The eval"),
    (6, "Request budget"),
    (7, "Traps"),
    (8, "Verify before you code"),
    (9, "Say it in an interview"),
    (10, "Done when"),
]

# Fences whose contents are error output or a bare check command - they need no walkthrough.
NO_WALKTHROUGH_LANGS = {"", "text", "console", "traceback", "mermaid", "json", "toml", "yaml"}

# Headings under which a code block is evidence, not teaching, so no walkthrough is required.
EXEMPT_HEADINGS = re.compile(r"when it breaks|check yourself|verify|request budget", re.I)


@dataclass
class Report:
    day: int
    failures: list[str] = field(default_factory=list)
    parts: int = 0
    contract: str = PLAN_VERSION
    words: int = 0
    # The folder this report is about. One day number can be several folders since v2.4.0, so the
    # printed line names the folder rather than only the number.
    label: str = ""

    @property
    def ok(self) -> bool:
        return not self.failures

    def fail(self, where: str, message: str) -> None:
        self.failures.append(f"{where}: {message}")


def frontmatter(text: str) -> dict[str, str] | None:
    """Return the YAML-ish frontmatter as a flat dict, or None when there is none."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def body(text: str) -> str:
    """The document with its frontmatter removed, so heading checks cannot match inside it."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4 :]
    return text


FENCE_BLOCK_RE = re.compile(r"^(`{3,})[^\n]*\n.*?^\1\s*$", re.M | re.S)


def prose_words(text: str) -> int:
    """Words outside code fences, with frontmatter already stripped by the caller.

    Fences are removed rather than counted because a code block is read at a different speed from
    a sentence, and sizing the two separately is the honest way to measure a document (plan Part
    11.7). Table pipes and heading hashes are left in: they are a rounding error at this scale, and
    stripping them would make the number harder to reproduce by hand with `wc -w`.
    """
    return len(FENCE_BLOCK_RE.sub("", text).split())


def code_lines(text: str) -> int:
    """Lines inside code fences, not counting the two fence markers themselves.

    This is the ceiling that stops a part moving its bulk into a fence to duck the word count.
    """
    return sum(max(0, len(m.group(0).splitlines()) - 2) for m in FENCE_BLOCK_RE.finditer(text))


def day_contract(folder: Path, number: int, report: Report) -> str:
    """Which version of the part contract this day is judged against.

    A day carries its own stamp in the hub's frontmatter, so amending the plan does not
    retroactively break days written to the previous contract (plan Part 11.9). From CUTOVER_DAY
    onward only the current stamp is accepted, and a day past it still carrying the old one is
    reported as unmigrated rather than quietly passed.
    """
    hub = folder / "LESSON.md"
    stamped = ""
    if hub.is_file():
        stamped = (frontmatter(hub.read_text(encoding="utf-8")) or {}).get("plan_version", "")
        stamped = stamped.strip('"')

    if number >= CUTOVER_DAY and stamped == LEGACY_VERSION:
        report.fail(
            "LESSON.md",
            f"stamped plan_version {LEGACY_VERSION}, but the size contract applies from day "
            f"{CUTOVER_DAY} - this day predates plan {PLAN_VERSION} and needs rewriting to it "
            "(three to five parts, the merged 'idea through a story' section, and 'the code you "
            "write'; plan Part 11.7 and 11.9)",
        )
        return LEGACY_VERSION
    if stamped == LEGACY_VERSION:
        return LEGACY_VERSION
    return PLAN_VERSION


def find_days(number: int) -> list[Path]:
    """Every folder belonging to one day number, in reading order.

    Day folders are day-<NN>-<slug> (plan v2.1.0), so the slug is free text and the number is the
    only stable handle. Since v2.4.0 one number may resolve to several folders - day-33a-<slug>
    and day-33b-<slug> are the two sittings of one subject (Part 11.7) - so this returns a list and
    each folder is checked as a day in its own right. The older unslugged day-<NN> and day-<N>
    forms still resolve, so a folder written before the amendment is found and then reported as a
    naming failure, never as a missing day.
    """
    slugged = sorted(p for p in DAYS.glob(f"day-{number:02d}*-*") if p.is_dir())
    if slugged:
        return slugged
    bare = [p for p in (DAYS / f"day-{number:02d}", DAYS / f"day-{number}") if p.is_dir()]
    return bare


def unexplained_code_blocks(text: str) -> list[int]:
    """Line numbers of code fences that no 'Line by line' walkthrough follows.

    Walks the document once, tracking the current heading. A fence is exempt when its language
    carries no logic (plain output, a diagram, a config dump) or when it sits under a heading
    whose job is showing evidence rather than teaching.
    """
    lines = text.splitlines()
    offenders: list[int] = []
    heading = ""
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line
            i += 1
            continue
        fence = re.match(r"^(`{3,})(\w*)\s*$", line)
        if not fence:
            i += 1
            continue

        # A fence may be longer than three backticks so it can contain a shorter one - which
        # is how a lesson shows the contents of a Markdown file. The closing fence must be at
        # least as long as the opening one, so a nested block cannot end the outer one.
        ticks = len(fence.group(1))
        closing = re.compile(rf"^`{{{ticks},}}\s*$")
        lang = fence.group(2).lower()
        start = i
        i += 1
        while i < len(lines) and not closing.match(lines[i]):
            i += 1
        i += 1  # step over the closing fence

        if lang in NO_WALKTHROUGH_LANGS or EXEMPT_HEADINGS.search(heading):
            continue

        # Look ahead for a walkthrough before the next fence or the next heading of the same rank.
        j = i
        explained = False
        while j < len(lines):
            nxt = lines[j]
            if re.search(r"line by line", nxt, re.I):
                explained = True
                break
            if re.match(r"^`{3,}\w", nxt) or nxt.startswith("## "):
                break
            j += 1
        if not explained:
            offenders.append(start + 1)
    return offenders


def check_part(path: Path, day: int, report: Report) -> tuple[int, int] | None:
    """Validate one parts/<NN>-<slug>/ document. Returns its (section, subtopic) numbers."""
    contract = report.contract
    where = f"parts/{path.parent.name}/{path.name}"
    match = PART_NAME_RE.match(path.name)
    if not match:
        report.fail(where, "filename must be <section>.<subtopic>-<kebab-slug>.md")
        return None
    section, subtopic = int(match.group(1)), int(match.group(2))

    # The folder's own name is validated once per day in check_day; here we only ask whether the
    # number it starts with agrees with the number in the filename.
    folder = path.parent.name
    folder_match = SECTION_DIR_RE.match(folder)
    if folder_match and int(folder_match.group(1)) != section:
        report.fail(
            where,
            f"lives in parts/{folder}/ but its number says section {section} - "
            f"it belongs in parts/{section:02d}-<slug>/",
        )

    text = path.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail(where, "no YAML frontmatter")
    else:
        missing = [k for k in PART_FRONTMATTER_KEYS if k not in meta]
        if missing:
            report.fail(where, f"frontmatter missing {', '.join(missing)}")
        if meta.get("day") not in {str(day), f'"{day}"'}:
            report.fail(where, f"frontmatter day is {meta.get('day')!r}, expected {day}")
        if meta.get("part", "").strip('"') != f"{section}.{subtopic}":
            report.fail(where, f"frontmatter part should be {section}.{subtopic}")
        level = meta.get("level", "").strip('"').lower()
        if level and level not in LEVELS:
            report.fail(where, f"level is {level!r}, must be one of {sorted(LEVELS)}")
        for stale in sorted(RETIRED_KEYS & meta.keys()):
            report.fail(
                where,
                f"frontmatter still carries {stale}: - the paper format was retired in plan "
                "v2.3.0, and a source is now cited inline in the part that needs it (Part 11.4)",
            )

    content = body(text)
    required = PART_SECTIONS_V24 if contract == PLAN_VERSION else PART_SECTIONS_V23
    seen_at: list[int] = []
    for name, pattern in required:
        found = pattern.search(content)
        if not found:
            report.fail(where, f"missing required section: {name}")
        else:
            seen_at.append(found.start())
    if len(seen_at) == len(required) and seen_at != sorted(seen_at):
        report.fail(where, "required sections are out of contract order (plan Part 11.3)")

    if contract == PLAN_VERSION and SPLIT_STORY_RE.search(content):
        report.fail(
            where,
            "still has a separate 'the idea in plain language' heading - plan v2.4.0 merged the "
            "story and the idea into one section, 'The idea, through a story' (Part 11.4)",
        )

    for line_no in unexplained_code_blocks(content):
        report.fail(where, f"code block at line {line_no} has no 'Line by line' walkthrough")

    if contract == PLAN_VERSION:
        words = prose_words(content)
        report.words += words
        if words > MAX_PART_WORDS:
            report.fail(
                where,
                f"{words} prose words, ceiling is {MAX_PART_WORDS} (plan Part 11.7). Delete prose "
                "the worked example already says, or split the part - never cut the failure text, "
                "the production section or the keyboard step to fit",
            )
        lines = code_lines(content)
        if lines > MAX_PART_CODE_LINES:
            report.fail(
                where,
                f"{lines} lines of code, ceiling is {MAX_PART_CODE_LINES} (plan Part 11.7)",
            )

    check_no_clocks(text, where, report)
    check_links(path, where, report)
    return section, subtopic


def check_links(path: Path, where: str, report: Report) -> None:
    """Every relative Markdown link in a part must resolve to a file that exists.

    Cross-section links go up a level (../01/1.5-<slug>.md) and are easy to get wrong, so a
    dead link here is a routine mistake rather than an exotic one. External links are skipped;
    this cannot check the internet.
    """
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for target in re.findall(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)", text):
        if target.startswith(("http://", "https://", "/")):
            continue
        if not (path.parent / target).resolve().is_file():
            report.fail(where, f"dead link: {target}")


def check_no_clocks(text: str, where: str, report: Report) -> None:
    """Principle 17: no time estimates anywhere in a day folder.

    Content is never trimmed to fit a schedule, so no document may imply one. Two things are
    stripped before the scan, both because they are not prose and cannot state a pace:

    - Code fences, since a real command may legitimately mention a timeout.
    - Markdown link targets and any bare .md filename, since a part's filename carries its number
      and slug. A part such as 6.2-min-and-max-are-a-range-check.md reads as "2-min" to the duration
      pattern, so every document linking to it - and its neighbours' prev:/next: frontmatter - would
      fail on a filename the hub's §2 map mandates.

    Link *text* is deliberately left in - "[takes 20 minutes](x.md)" is still a clock, and so is a
    duration field in frontmatter, which is a key rather than a filename.
    """
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    prose = re.sub(r"\]\([^)]*\)", "]()", prose)
    prose = re.sub(r"[\w./-]+\.md\b", "", prose)
    for pattern, description in TIME_BANS:
        hit = pattern.search(prose)
        if hit:
            snippet = hit.group(0).strip().replace("\n", " ")
            report.fail(where, f"{description} ({snippet!r}) - a day has no clock (Principle 17)")


def check_numbering(numbers: list[tuple[int, int]], report: Report) -> None:
    """Sections start at 1 and are contiguous; so are the subtopics inside each section."""
    if not numbers:
        return
    sections = sorted({s for s, _ in numbers})
    if sections[0] != 1:
        report.fail("parts/", f"section numbering starts at {sections[0]}, must start at 1")
    expected = list(range(1, len(sections) + 1))
    if sections != expected:
        report.fail("parts/", f"section numbering has a gap: {sections} (expected {expected})")
    for section in sections:
        subs = sorted(sub for s, sub in numbers if s == section)
        if subs != list(range(1, len(subs) + 1)):
            report.fail(
                "parts/", f"section {section} subtopics are {subs}, expected 1..{len(subs)}"
            )


def check_hub(folder: Path, day: int, part_count: int, report: Report) -> None:
    hub = folder / "LESSON.md"
    if not hub.is_file():
        report.fail("LESSON.md", "missing - every day needs a hub")
        return

    text = hub.read_text(encoding="utf-8")
    meta = frontmatter(text)
    if meta is None:
        report.fail("LESSON.md", "no YAML frontmatter")
    else:
        missing = [k for k in HUB_FRONTMATTER_KEYS if k not in meta]
        if missing:
            report.fail("LESSON.md", f"frontmatter missing {', '.join(missing)}")
        declared = meta.get("parts", "").strip('"')
        if declared.isdigit() and int(declared) != part_count:
            report.fail(
                "LESSON.md", f"frontmatter says parts: {declared}, parts/ holds {part_count}"
            )
        stamped = meta.get("plan_version", "").strip('"')
        # day_contract has already reported a day past the cutover that is still on the old stamp;
        # this only has to reject a stamp that is neither the current contract nor the legacy one.
        if stamped not in {PLAN_VERSION, LEGACY_VERSION}:
            report.fail("LESSON.md", f"plan_version must be {PLAN_VERSION}")

    content = body(text)
    for number, name in HUB_SECTIONS:
        if not re.search(rf"^##\s*§{number}\b", content, re.M):
            report.fail("LESSON.md", f"missing section §{number} ({name})")

    if not re.search(r"^>\s*\*\*Yesterday", content, re.M | re.I):
        report.fail("LESSON.md", "missing the yesterday / today / tomorrow blockquote")

    if re.search(r"line by line", content, re.I):
        report.fail("LESSON.md", "the hub must not teach - move the walkthrough into a part")

    if report.contract == PLAN_VERSION:
        words = prose_words(content)
        if words > MAX_HUB_WORDS:
            report.fail(
                "LESSON.md",
                f"{words} prose words, ceiling is {MAX_HUB_WORDS} (plan Part 11.7). The hub "
                "orients and assembles; the teaching belongs in the parts",
            )

    check_no_clocks(text, "LESSON.md", report)
    check_links(hub, "LESSON.md", report)

    linked = set(re.findall(rf"parts/(\d{{2}}-{KEBAB}/[\w.\-]+\.md)", content))
    on_disk = {
        f"{d.name}/{f.name}"
        for d in (folder / "parts").iterdir()
        if d.is_dir()
        for f in d.glob("*.md")
    }
    for name in sorted(on_disk - linked):
        report.fail("LESSON.md", f"§2 map does not link parts/{name}")


def check_day(number: int) -> list[Report]:
    """Every folder for this day number, each checked as a day in its own right.

    A day split into lettered sittings (plan v2.4.0, Part 11.7) is several folders, and each one
    must satisfy the whole contract on its own - a letter is not half a day.
    """
    folders = find_days(number)
    if not folders:
        report = Report(day=number)
        report.fail("days/", f"no folder for day {number}")
        return [report]
    return [check_day_folder(number, folder) for folder in folders]


def check_day_folder(number: int, folder: Path) -> Report:
    report = Report(day=number, label=folder.name)

    if not DAY_DIR_RE.match(folder.name):
        report.fail(
            f"days/{folder.name}/",
            "day folders are day-<NN>-<slug> - e.g. day-01-pins - optionally with a single "
            "lowercase letter after the number for a lettered sitting, e.g. day-33a-text-accessors "
            "(plan v2.4.0, Part 11.7). The slug names the day's subject, so days/ can be read "
            "without opening a hub",
        )

    if (folder / "papers").is_dir():
        report.fail(
            "papers/",
            "the paper document was retired in plan v2.3.0 - delete this directory and cite the "
            "source inline, by title, year, identifier and URL, in the part that needs it "
            "(Part 11.4)",
        )

    report.contract = day_contract(folder, number, report)

    parts_dir = folder / "parts"
    if not parts_dir.is_dir():
        report.fail("parts/", "missing - a day with no parts/ is not written (plan Part 11.1)")
        return report

    loose = sorted(parts_dir.glob("*.md"))
    for stray in loose:
        report.fail(
            f"parts/{stray.name}",
            "loose in parts/ - every part lives in its section folder, e.g. parts/01/",
        )

    for entry in sorted(parts_dir.iterdir()):
        if entry.is_dir() and not SECTION_DIR_RE.match(entry.name):
            report.fail(
                f"parts/{entry.name}/",
                "section folders are <NN>-<slug> - the zero-padded section number, a hyphen, and "
                "a short kebab-case name for what the section covers (01-toolchain, 02-skeleton). "
                "A bare 01/ says nothing about its contents",
            )

    files = sorted(
        (f for d in parts_dir.iterdir() if d.is_dir() for f in d.glob("*.md")),
        key=lambda f: (f.parent.name, f.name),
    )
    if not files:
        report.fail("parts/", "empty - no section folders holding part documents")
        return report

    report.parts = len(files)
    if report.contract == PLAN_VERSION and len(files) > MAX_PARTS_PER_DAY:
        report.fail(
            "parts/",
            f"{len(files)} parts, ceiling is {MAX_PARTS_PER_DAY} and the target is three to five "
            f"(plan Part 11.7). A subject this size is split into lettered sittings - "
            f"day-{number:02d}a-<slug>, day-{number:02d}b-<slug> - never crammed into one day",
        )

    numbers = [n for f in files if (n := check_part(f, number, report)) is not None]
    check_numbering(numbers, report)

    check_hub(folder, number, len(files), report)

    if report.contract == PLAN_VERSION and report.words > MAX_DAY_WORDS:
        report.fail(
            "parts/",
            f"{report.words} prose words across the day, ceiling is {MAX_DAY_WORDS} "
            "(plan Part 11.7) - split the day into lettered sittings",
        )

    if not (folder / "CHECKLIST.md").is_file():
        report.fail("CHECKLIST.md", "missing")
    return report


def between(text: str, start: str, stop: str) -> str:
    """The slice of `text` from the line starting `start` to the line starting `stop`."""
    head = text.split(start, 1)
    return head[1].split(stop, 1)[0] if len(head) > 1 else ""


def check_index() -> list[str]:
    """Repo-level: does the curriculum index still agree with the plan it was generated from?

    Not per-day, so it runs once rather than inside check_day. Three questions, in the order
    that makes a failure diagnosable: is the stamp current, do the phase day-ranges match, and
    does every curriculum ID the matrices define actually reach a day.
    """
    problems: list[str] = []
    if not INDEX.is_file() or not PLAN.is_file():
        return ["docs/: the plan or the curriculum index is missing"]

    plan_text = PLAN.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8")

    meta = frontmatter(index_text) or {}
    stamped = meta.get("plan_version", "").strip('"')
    if stamped != PLAN_VERSION:
        problems.append(
            f"docs/CURRICULUM_INDEX_DS.md: plan_version is {stamped or 'missing'}, "
            f"plan is {PLAN_VERSION} - regenerate the index or correct the stamp"
        )

    plan_phases = {
        int(m.group(1)): (int(m.group(2)), int(m.group(3)))
        for m in PLAN_PHASE_RE.finditer(between(plan_text, "## Part 5", "## Part 6"))
    }
    index_phases = {
        int(m.group(1)): (int(m.group(2)), int(m.group(3)))
        for m in INDEX_PHASE_RE.finditer(index_text)
    }
    for phase in sorted(set(plan_phases) | set(index_phases)):
        if plan_phases.get(phase) != index_phases.get(phase):
            problems.append(
                f"docs/CURRICULUM_INDEX_DS.md: phase {phase} spans "
                f"{index_phases.get(phase, 'nothing')} but plan Part 5 says "
                f"{plan_phases.get(phase, 'nothing')}"
            )

    plan_ids = set(MATRIX_ID_RE.findall(between(plan_text, "## Part 4", "## Part 5")))
    index_ids = set(ANY_ID_RE.findall(index_text))
    # One-directional on purpose: the index also carries ADR- deliverable IDs that the matrices
    # never define, and those are not a fault. An ID the matrices define but no day claims is.
    orphaned = sorted(plan_ids - index_ids)
    if orphaned:
        problems.append(
            f"docs/CURRICULUM_INDEX_DS.md: {len(orphaned)} plan IDs reach no day - "
            f"{', '.join(orphaned[:8])}{' …' if len(orphaned) > 8 else ''}"
        )
    return problems


def written_days() -> list[int]:
    """Every day that has attempted the v2.0.0 shape, so an unwritten day is not a failure."""
    found: list[int] = []
    for folder in sorted(DAYS.glob("day-*")):
        if not (folder / "parts").is_dir():
            continue
        digits = re.search(r"day-(\d+)", folder.name)
        if digits:
            found.append(int(digits.group(1)))
    return sorted(found)


def main(argv: list[str]) -> int:
    requested = [int(a) for a in argv if a.isdigit()]
    # The index check is repo-level, so it runs on a full sweep and not when one day was named.
    index_problems = [] if requested else check_index()

    days = requested or written_days()
    if not days:
        print("no day has a parts/ directory yet - nothing to check")
        return 1 if index_problems else 0

    reports = [r for d in days for r in check_day(d)]
    failed = [r for r in reports if not r.ok]

    for report in reports:
        name = report.label or f"day {report.day}"
        if report.ok:
            size = f"{report.words} words" if report.contract == PLAN_VERSION else report.contract
            print(f"OK   {name:<38}  {report.parts} parts, {size}")
        else:
            print(f"FAIL {name:<38}  {len(report.failures)} problems")
            for failure in report.failures:
                print(f"       - {failure}")

    if index_problems:
        print()
        print(f"FAIL curriculum index  {len(index_problems)} problems")
        for problem in index_problems:
            print(f"       - {problem}")

    print()
    if failed:
        print(f"depth contract: {len(reports) - len(failed)}/{len(reports)} day folders pass")
        return 1
    if index_problems:
        print(f"depth contract: all {len(reports)} checked days pass, but the index disagrees")
        return 1
    print(f"depth contract: all {len(reports)} checked days pass")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
