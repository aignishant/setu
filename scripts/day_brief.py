#!/usr/bin/env python
"""Project the working set for one day out of the plan, so a day can be written
without loading the plan, the index, the tracker and two neighbouring days whole.

Every line this prints is COPIED VERBATIM from a source file. Nothing is summarised,
paraphrased or generated, and each block names the path it came from, so a claim in
the brief can always be traced back. That is deliberate: under Principle 7 a
hallucinated brief would be a silent failure, and a projection cannot hallucinate.

The day list comes from docs/CURRICULUM_INDEX_DS.md, exactly as scripts/tracker.py
reads it - the two share the parsers so the brief cannot drift from the tracker.

    uv run python scripts/day_brief.py 11        # the brief for day 11
    ./m brief 11                                 # the same thing
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from tracker import PHASE_RE, ROW_RE

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs" / "00_MASTER_PLAN_DS_GENAI.md"
INDEX = ROOT / "docs" / "CURRICULUM_INDEX_DS.md"
DAYS = ROOT / "days"
SRC = ROOT / "src" / "setu"

# A Part 5 phase row: | **1** | 4-11 | M1 | Python foundations | <gate> |
PHASE_ROW_RE = re.compile(r"^\|\s*\*\*(\d+)\*\*\s*\|\s*(\d+)[–—-](\d+)\s*\|")
# A Part 4 matrix row keyed by curriculum ID: | PY-11 <emoji> | topic | example | days |
ID_CELL_RE = re.compile(r"^\|\s*([A-Z]{2,4}-\d+)\s")
# The eight frontmatter keys every part carries (plan Part 11.4).
FRONTMATTER_RE = re.compile(r"^(\w+):\s*(.*)$", re.M)
# How many neighbouring written days to manifest for continuity of voice.
NEIGHBOURS = 2
# A day written but not yet worked through has a full checklist of open boxes - 88 of them on
# Day 10. Printing them all would put back the bulk this brief exists to remove, so the warning
# carries the count, which is the part that decides whether to proceed, and a short sample.
OPEN_BOX_SAMPLE = 5


def slice_between(text: str, start: str, stop: str) -> str:
    """The lines from the heading starting with `start` up to the one starting `stop`."""
    out: list[str] = []
    inside = False
    for line in text.splitlines():
        if line.startswith(start):
            inside = True
        elif inside and line.startswith(stop):
            break
        if inside:
            out.append(line)
    return "\n".join(out)


def find_day(day: int) -> tuple[str, str, list[str], str]:
    """The index row for this day, its phase heading, its IDs and its kind - all verbatim."""
    phase_heading = ""
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        if PHASE_RE.match(line):
            phase_heading = line
        row = ROW_RE.match(line)
        if row and int(row.group(1)) == day:
            raw = row.group(3).strip()
            ids = [] if raw in {"", "—", "-"} else [i.strip() for i in raw.split(",")]
            return phase_heading, line, ids, row.group(4)
    sys.exit(f"day {day} is not in {INDEX.name} - the index is the only day list")


def phase_row(day: int) -> str:
    """The Part 5 row whose day range contains this day: the theme and the phase gate."""
    part5 = slice_between(PLAN.read_text(encoding="utf-8"), "## Part 5", "## Part 6")
    for line in part5.splitlines():
        span = PHASE_ROW_RE.match(line)
        if span and int(span.group(2)) <= day <= int(span.group(3)):
            return line
    return ""


def matrix_rows(ids: list[str]) -> list[tuple[str, str]]:
    """Each requested ID's Part 4 row, tagged with the curriculum heading above it."""
    part4 = slice_between(PLAN.read_text(encoding="utf-8"), "## Part 4", "## Part 5")
    wanted = set(ids)
    hits: list[tuple[str, str]] = []
    heading = ""
    for line in part4.splitlines():
        if line.startswith("### "):
            heading = line
        cell = ID_CELL_RE.match(line)
        if cell and cell.group(1) in wanted:
            hits.append((heading, line))
    found = set()
    for _, line in hits:
        cell = ID_CELL_RE.match(line)
        if cell:
            found.add(cell.group(1))
    for missing in sorted(wanted - found):
        # The index promised an ID the matrices do not define. Say so in the brief rather
        # than printing a short list that silently looks complete.
        hits.append(("", f"| {missing} | NOT FOUND in Part 4 - index and plan disagree | | |"))
    return hits


def day_folder(day: int) -> Path | None:
    folders = sorted(DAYS.glob(f"day-{day:02d}-*"))
    return folders[0] if folders else None


def manifest(day: int) -> list[str]:
    """One written day's part list, from frontmatter only - never a part body."""
    folder = day_folder(day)
    if folder is None or not (folder / "parts").is_dir():
        return []
    lines = [f"`days/{folder.name}/`", "", "| Part | Level | Title | IDs |", "|---|---|---|---|"]
    for path in sorted(folder.glob("parts/*/*.md")):
        text = path.read_text(encoding="utf-8")
        block = text.split("---")[1] if text.startswith("---") else ""
        keys = {k: v.strip().strip('"') for k, v in FRONTMATTER_RE.findall(block)}
        lines.append(
            f"| {keys.get('part', '?')} | {keys.get('level', '?')} "
            f"| {keys.get('title', '?')} | {keys.get('ids', '')} |"
        )
    return lines


def open_boxes(day: int) -> list[str]:
    """Unticked checklist boxes on the previous day - Step 1 must warn before proceeding."""
    folder = day_folder(day)
    if folder is None:
        return []
    checklist = folder / "CHECKLIST.md"
    if not checklist.is_file():
        return []
    lines = checklist.read_text(encoding="utf-8").splitlines()
    return [line for line in lines if line.startswith("- [ ]")]


def build(day: int) -> str:
    phase_heading, row, ids, kind = find_day(day)
    out: list[str] = [
        f"# Day {day} brief",
        "",
        "> Mechanical projection. Every line below is copied verbatim from the file named",
        "> above it - nothing here is generated. Open a part body only when this is not enough.",
        "",
        "## Phase - `docs/CURRICULUM_INDEX_DS.md` + plan Part 5",
        "",
        phase_heading,
        "",
        phase_row(day),
        "",
        f"## This day (`kind: {kind}`) - `docs/CURRICULUM_INDEX_DS.md`",
        "",
        "| Day | Title | IDs | Kind |",
        "|---|---|---|---|",
        row,
        "",
        "## The IDs this day must serve - plan Part 4",
        "",
    ]
    if not ids:
        out += ["_This day cites no curriculum ID (a foundry or portfolio day)._", ""]
    heading_printed = ""
    for heading, line in matrix_rows(ids):
        if heading and heading != heading_printed:
            out += [
                heading,
                "",
                "| ID | Topic | Simple explanation + Setu example | Days |",
                "|---|---|---|---|",
            ]
            heading_printed = heading
        out.append(line)
    out.append("")

    for neighbour in range(day - NEIGHBOURS, day):
        rows = manifest(neighbour)
        if rows:
            out += [
                f"## Already taught - day {neighbour} (frontmatter only, no bodies)",
                "",
                *rows,
                "",
            ]

    stale = open_boxes(day - 1)
    if stale:
        previous = day_folder(day - 1)
        out += [
            f"## WARNING day {day - 1} has {len(stale)} unticked checklist boxes",
            "",
            "Step 1.3 of the day-setu skill: warn and ask before writing this day.",
            f"Full list: `days/{previous.name}/CHECKLIST.md`. First {OPEN_BOX_SAMPLE}:",
            "",
            *stale[:OPEN_BOX_SAMPLE],
            "",
        ]

    modules = sorted(p.name for p in SRC.glob("*.py") if p.stat().st_size)
    out += [
        "## Already in `src/setu/` - build on it, never duplicate it",
        "",
        ("- " + "\n- ".join(modules)) if modules else "_(empty)_",
        "",
    ]
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if not argv or not argv[0].isdigit():
        print("usage: ./m brief <day>", file=sys.stderr)
        return 1
    # Windows consoles default to cp1252 and the plan is full of em-dashes and emoji,
    # so the bytes go out as UTF-8 explicitly rather than through print().
    sys.stdout.buffer.write(build(int(argv[0])).encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
