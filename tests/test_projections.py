"""Prove the generated context files are projections, not summaries.

`./m brief NN` and `days/INDEX.md` are allowed to stand in for reading the plan, the curriculum
index and the day tree only because every line in them is copied from one of those files. That
claim is the entire safety argument - a summary could quietly invent a requirement the plan does
not contain, and under Principle 7 that would be a silent failure. So the claim gets a test that
can go RED: change day_brief.py to paraphrase a matrix row instead of copying it, and
`test_every_brief_table_row_exists_verbatim_in_a_source` fails.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

PLAN = ROOT / "docs" / "00_MASTER_PLAN_DS_GENAI.md"
INDEX = ROOT / "docs" / "CURRICULUM_INDEX_DS.md"
PARTS_INDEX = ROOT / "days" / "INDEX.md"

# A written day with curriculum IDs, neighbours on both sides, and a phase - the shape that
# exercises every branch of the brief. Day 11 is the Phase 1 gate.
SAMPLE_DAY = 11


def _brief(day: int = SAMPLE_DAY) -> str:
    from day_brief import build

    return build(day)


def _source_lines() -> set[str]:
    """Every line of every file the brief is allowed to copy from."""
    lines: set[str] = set()
    for path in (PLAN, INDEX):
        lines.update(line.strip() for line in path.read_text(encoding="utf-8").splitlines())
    return lines


def test_every_brief_table_row_exists_verbatim_in_a_source() -> None:
    """The core claim. A row the brief prints but no source file contains is a hallucination."""
    sources = _source_lines()
    # Rows the brief builds itself - the column headers it adds so a projected row renders as a
    # table, and the part manifests it projects from frontmatter rather than from these two files.
    own = re.compile(r"^\|\s*(ID|Day|Part)\s*\||^\|[\s|:-]+\|$|^\|\s*[\d.]+\s*\|\s*\w+\s*\|")

    invented = [
        line
        for line in _brief().splitlines()
        if line.startswith("|") and not own.match(line) and line.strip() not in sources
    ]
    assert not invented, f"the brief printed rows that exist in no source file: {invented}"


def test_the_brief_carries_the_days_real_ids() -> None:
    """A brief that quietly drops an ID would send the day off to teach the wrong subject."""
    row = next(
        line
        for line in INDEX.read_text(encoding="utf-8").splitlines()
        if re.match(rf"^\|\s*{SAMPLE_DAY}\s*\|", line)
    )
    expected = re.findall(r"[A-Z]{2,4}-\d+", row)
    assert expected, "the sample day should cite at least one curriculum ID"

    brief = _brief()
    missing = [i for i in expected if i not in brief]
    assert not missing, f"day {SAMPLE_DAY} cites {expected} but the brief omitted {missing}"


def test_the_brief_never_smuggles_in_the_depth_contract() -> None:
    """Part 11 is judgement, not a lookup. If it ever lands in the brief, someone will read the
    projection instead of the contract, which is the one substitution that is not allowed."""
    brief = _brief()
    assert "## Part 11" not in brief
    assert len(brief) < 40_000, "the brief has grown into a document; it is meant to be a filter"


def test_the_brief_refuses_a_day_outside_the_plan() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "day_brief.py"), "999"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "not in" in (result.stdout + result.stderr)


@pytest.mark.parametrize("column", ["Part", "Level", "Title", "IDs"])
def test_parts_index_is_generated_and_complete(column: str) -> None:
    """days/INDEX.md must exist and describe every written part, or step 3 of the day-setu skill
    silently starts re-explaining ideas that are already taught."""
    assert PARTS_INDEX.is_file(), "days/INDEX.md is missing - run ./m tracker"
    text = PARTS_INDEX.read_text(encoding="utf-8")
    assert column in text

    on_disk = len(list((ROOT / "days").glob("day-*/parts/*/*.md")))
    indexed = len(re.findall(r"^\|\s*\d+\.\d+\s*\|", text, re.M))
    assert indexed == on_disk, (
        f"index lists {indexed} parts, the tree has {on_disk} - run ./m tracker"
    )


def test_index_check_catches_a_plan_that_moved() -> None:
    """The depth sweep's repo-level check must be able to fail. It found a real v1.0.0 stamp on
    2026-08-30; this proves it would find the next one."""
    import depth_check

    assert depth_check.check_index() == [], "the curriculum index currently disagrees with the plan"

    original = depth_check.PLAN_VERSION
    try:
        depth_check.PLAN_VERSION = "v9.9.9"
        problems = depth_check.check_index()
    finally:
        depth_check.PLAN_VERSION = original
    assert problems, "a moved plan version must be reported, not passed over"
    assert "plan_version" in problems[0]
