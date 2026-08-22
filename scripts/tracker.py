#!/usr/bin/env python
"""Regenerate docs/TRACKER.md from docs/CURRICULUM_INDEX_DS.md + what is on disk.

Single source of truth for the day list is the curriculum index; this script never
invents a day. Status is read from the filesystem and the checklists, so the tracker
cannot drift from reality.

Under plan v2.0.0 a day counts as written only when it has the hub *and* a non-empty
parts/ directory (Principle 16, plan Part 11). A day still carrying only its v1.0.0
single-file lesson is reported as legacy, which is what makes the regeneration visible.

    uv run python scripts/tracker.py            # rewrite docs/TRACKER.md
    uv run python scripts/tracker.py --summary  # one-line progress, no file written
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "CURRICULUM_INDEX_DS.md"
TRACKER = ROOT / "docs" / "TRACKER.md"
DAYS = ROOT / "days"

PHASE_RE = re.compile(r"^##\s+Phase\s+(\d+)\s+·\s+(.+?)\s+·\s+Days?\s+([\d–—-]+)\s*$")
ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(\w+)\s*\|\s*$")


@dataclass
class Day:
    number: int
    title: str
    ids: str
    kind: str
    phase: int
    phase_name: str
    written: bool = False
    has_checklist: bool = False
    complete: bool = False
    open_boxes: int = 0
    folder: str = ""
    parts: int = 0
    legacy: bool = False


@dataclass
class Phase:
    number: int
    name: str
    span: str
    days: list[Day] = field(default_factory=list)


def parse_index() -> list[Phase]:
    """Read the curriculum index and return its phases in order."""
    if not INDEX.exists():
        sys.exit(f"missing {INDEX} - the tracker has nothing to track")

    phases: list[Phase] = []
    current: Phase | None = None

    for line in INDEX.read_text(encoding="utf-8").splitlines():
        header = PHASE_RE.match(line)
        if header:
            current = Phase(int(header.group(1)), header.group(2), header.group(3))
            phases.append(current)
            continue
        if current is None:
            continue
        row = ROW_RE.match(line)
        if row:
            current.days.append(
                Day(
                    number=int(row.group(1)),
                    title=row.group(2).replace("**", ""),
                    ids=row.group(3) or "—",
                    kind=row.group(4),
                    phase=current.number,
                    phase_name=current.name,
                )
            )
    return phases


def find_folder(number: int) -> Path | None:
    """Day 0 lives in day-00-setup; every other day is day-NN."""
    candidates = [DAYS / f"day-{number:02d}", DAYS / f"day-{number}"]
    if number == 0:
        candidates.insert(0, DAYS / "day-00-setup")
    return next((p for p in candidates if p.is_dir()), None)


def inspect(day: Day) -> Day:
    """Fill in on-disk status for one day."""
    folder = find_folder(day.number)
    if folder is None:
        return day
    day.folder = folder.relative_to(ROOT).as_posix()
    day.parts = len(list((folder / "parts").glob("*.md"))) if (folder / "parts").is_dir() else 0
    day.legacy = (folder / "_legacy" / "LESSON.md").is_file()
    # v2.0.0: a hub without parts/ is not a written day.
    day.written = (folder / "LESSON.md").is_file() and day.parts > 0
    checklist = folder / "CHECKLIST.md"
    day.has_checklist = checklist.is_file()
    if day.has_checklist:
        text = checklist.read_text(encoding="utf-8")
        day.open_boxes = len(re.findall(r"^- \[ \]", text, flags=re.M))
        ticked = len(re.findall(r"^- \[x\]", text, flags=re.M | re.I))
        day.complete = day.open_boxes == 0 and ticked > 0
    return day


def badge(day: Day) -> str:
    if day.complete:
        return "✅ done"
    if day.written and day.has_checklist:
        return "📄 written"
    if day.written:
        return "⚠️ no checklist"
    if day.legacy:
        return "🗃️ legacy"
    return "⬜ pending"


def build(phases: list[Phase]) -> tuple[str, dict[str, int]]:
    day_zero = inspect(
        Day(0, "Toolchain, skeleton, and the ./m script", "—", "setup", 0, "Foundry")
    )
    for phase in phases:
        phase.days = [inspect(d) for d in phase.days]

    all_days = [day_zero] + [d for p in phases for d in p.days]
    stats = {
        "total": len(all_days),
        "written": sum(d.written for d in all_days),
        "complete": sum(d.complete for d in all_days),
        "legacy": sum(d.legacy and not d.written for d in all_days),
        "parts": sum(d.parts for d in all_days),
    }
    stats["pending"] = stats["total"] - stats["written"]
    pct = 100 * stats["written"] / stats["total"]

    out: list[str] = [
        "---",
        "name: tracker",
        "plan: setu",
        f"generated: \"{date.today().isoformat()}\"",
        "generator: scripts/tracker.py",
        "---",
        "",
        "# 📊 TRACKER — Project Setu",
        "",
        "> **Do not edit this file by hand.** It is regenerated by `./m tracker` "
        "(and automatically by `./m done N`) from `docs/CURRICULUM_INDEX_DS.md` "
        "plus what is actually on disk.",
        "",
        "> **Plan v2.0.0.** A day counts as *written* only when it has a hub **and** a non-empty "
        "`parts/` directory (Principle 16 · plan Part 11). Days marked 🗃️ legacy still carry their "
        "v1.0.0 single-file lesson at `days/day-NN/_legacy/LESSON.md` and are workable from it "
        "until they are regenerated.",
        "",
        "## Progress",
        "",
        "| | Count | Of total |",
        "|---|---|---|",
        f"| 📄 Days written in the v2.0.0 shape | **{stats['written']}** | {pct:.1f}% |",
        f"| 📚 Sub-topic documents in `parts/` | **{stats['parts']}** | — |",
        f"| ✅ Days completed (checklist fully ticked) | **{stats['complete']}** |"
        f" {100 * stats['complete'] / stats['total']:.1f}% |",
        f"| 🗃️ Legacy days awaiting regeneration | **{stats['legacy']}** |"
        f" {100 * stats['legacy'] / stats['total']:.1f}% |",
        f"| ⬜ Never written | **{stats['pending'] - stats['legacy']}** |"
        f" {100 * (stats['pending'] - stats['legacy']) / stats['total']:.1f}% |",
        f"| Total days in plan | {stats['total']} | (Day 0 + Days 1–240) |",
        "",
        "```",
        f"written  {bar(stats['written'], stats['total'])}  "
        f"{stats['written']}/{stats['total']}",
        f"complete {bar(stats['complete'], stats['total'])}  "
        f"{stats['complete']}/{stats['total']}",
        f"legacy   {bar(stats['legacy'], stats['total'])}  "
        f"{stats['legacy']}/{stats['total']}",
        "```",
        "",
        "**Legend:** ✅ done (checklist fully ticked) · 📄 written (hub + `parts/` + checklist) · "
        "⚠️ no checklist · 🗃️ legacy (v1.0.0 lesson only, needs regenerating) · "
        "⬜ pending (never written)",
        "",
        "## By phase",
        "",
        "| Phase | Module | Theme | Days | Written | Parts | Done |",
        "|---|---|---|---|---|---|---|",
    ]

    zero_written = int(day_zero.written)
    out.append(
        f"| 0 | — | Foundry (incl. Day 0 setup) | 0–3 | "
        f"{zero_written + sum(d.written for d in phases[0].days)}/4 | "
        f"{day_zero.parts + sum(d.parts for d in phases[0].days)} | "
        f"{int(day_zero.complete) + sum(d.complete for d in phases[0].days)}/4 |"
    )
    for phase in phases[1:]:
        module = f"M{phase.number}" if 1 <= phase.number <= 27 else "—"
        n = len(phase.days)
        out.append(
            f"| {phase.number} | {module} | {phase.name} | {phase.span} | "
            f"{sum(d.written for d in phase.days)}/{n} | "
            f"{sum(d.parts for d in phase.days)} | "
            f"{sum(d.complete for d in phase.days)}/{n} |"
        )

    out += ["", "## Every day", ""]
    out += [
        "### Phase 0 · Foundry · Days 0–3",
        "",
        "| Day | Title | IDs | Kind | Status | Parts | Open boxes |",
        "|---|---|---|---|---|---|---|",
        row(day_zero),
    ]
    out += [row(d) for d in phases[0].days]
    out.append("")

    for phase in phases[1:]:
        out += [
            f"### Phase {phase.number} · {phase.name} · Days {phase.span}",
            "",
            "| Day | Title | IDs | Kind | Status | Parts | Open boxes |",
            "|---|---|---|---|---|---|---|",
        ]
        out += [row(d) for d in phase.days]
        out.append("")

    out += [
        "## Next up",
        "",
    ]
    pending = [d for d in all_days if not d.written]
    if pending:
        nxt = pending[:10]
        out.append("The next ten days to write, in order:")
        out.append("")
        out += [
            f"- **Day {d.number}** — {d.title} `({d.ids})`"
            + ("  ·  🗃️ has a v1.0.0 lesson to mine" if d.legacy else "")
            for d in nxt
        ]
    else:
        out.append("Every day is written. 🎉")
    out.append("")
    return "\n".join(out), stats


def bar(done: int, total: int, width: int = 40) -> str:
    filled = round(width * done / total)
    return "█" * filled + "░" * (width - filled)


def row(day: Day) -> str:
    title = day.title if len(day.title) <= 78 else day.title[:75] + "…"
    boxes = str(day.open_boxes) if day.has_checklist else "—"
    parts = str(day.parts) if day.parts else "—"
    return (
        f"| {day.number} | {title} | {day.ids} | {day.kind} | "
        f"{badge(day)} | {parts} | {boxes} |"
    )


def main() -> int:
    phases = parse_index()
    content, stats = build(phases)
    if "--summary" in sys.argv:
        print(
            f"Setu: {stats['written']}/{stats['total']} days in the v2.0.0 shape "
            f"({stats['parts']} sub-topic docs), {stats['complete']} completed, "
            f"{stats['legacy']} legacy to regenerate, "
            f"{stats['pending'] - stats['legacy']} never written."
        )
        return 0
    TRACKER.write_text(content + "\n", encoding="utf-8")
    print(f"wrote {TRACKER.relative_to(ROOT)} - {stats['written']}/{stats['total']} written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
