"""Day 1: prove the pins are pins, and that drift classification is right."""

from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

# name[extras]==version, and nothing else. A range, a ~=, or a bare name is not a pin.
EXACT_PIN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*(\[[A-Za-z0-9,._-]+\])?==[^,;\s]+$")


def all_specs() -> list[str]:
    doc = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    specs = list(doc["project"].get("dependencies", []))
    for group in doc.get("dependency-groups", {}).values():
        specs += [s for s in group if isinstance(s, str)]
    return specs


def test_every_dependency_is_exactly_pinned() -> None:
    """Principle 4: no ranges anywhere. See part 1.2."""
    specs = all_specs()
    assert specs, "pyproject.toml declares no dependencies at all - nothing was pinned"

    loose = [s for s in specs if not EXACT_PIN.match(s)]
    # The offending specs go IN the message: a failure that does not say which one is a failure
    # you will resent at eleven at night (part 3.1 of Day 2, learned here first).
    assert not loose, f"not pinned with ==: {loose}"


def test_python_requirement_is_exact() -> None:
    """requires-python is ==3.12.* - patches yes, a minor jump no. Part 3.1."""
    doc = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    requires = doc["project"]["requires-python"]

    # `==3.12.*` admits 3.12.0 through 3.12.99 and refuses 3.13. `>=3.12` admits an interpreter
    # nobody has tested this project against, which is the same class of mistake as `>=` on a
    # dependency: a future release decides for you.
    assert re.fullmatch(r"==3\.\d+\.\*", requires), (
        f"requires-python is {requires!r}, which does not pin the minor version"
    )


def test_classify_detects_a_major_bump() -> None:
    """The pure decision function from part 4.2, tested without a network."""
    from check_pins import classify

    assert classify("3.0.5", "4.0.0") == "MAJOR", "a major bump must not be reported as ordinary"
    assert classify("3.0.5", "3.1.0") == "minor"
    assert classify("3.0.5", "3.0.6") == "patch"
    assert classify("3.0.5", "3.0.5") == "none"
    # The index's latest being OLDER than our pin is not drift - it usually means the release we
    # pinned was yanked, and `==` is the specifier that still installs it (PEP 592, part 2.2).
    assert classify("3.0.5", "3.0.4") == "BACKWARDS"


@pytest.mark.live
def test_pins_match_the_index() -> None:
    """Hits PyPI. Skipped by default; this is Principle 13 as a test.

    It carries `live` because it makes real network calls: `./m check` runs on every commit and
    in CI, and a gate that reaches the internet is a gate that fails when the internet does.
    """
    from check_pins import check, read_pins

    report = check(read_pins(str(ROOT / "pyproject.toml")))

    unreachable = [p.name for p in report.pins if p.error]
    assert not unreachable, f"could not reach the index for: {unreachable}"

    # MAJOR and BACKWARDS fail; minor and patch do not. The threshold is deliberate: a minor or
    # patch release is additive or a fix, so the honest response is to read the notes and pin it
    # this week - a decision, not an emergency. A MAJOR bump means behaviour was removed and
    # Principle 14 says an addendum comes BEFORE the pin moves; BACKWARDS means our pinned
    # release probably no longer exists. Those two are the ones worth waking a test up for.
    serious = [
        f"{p.name}: pinned {p.pinned}, index has {p.current} ({p.drift})"
        for p in report.pins
        if p.drift in ("MAJOR", "BACKWARDS")
    ]
    assert not serious, f"pins needing an amendment before they move: {serious}"

    withdrawn = [f"{p.name}=={p.pinned}" for p in report.pins if p.pinned_yanked]
    assert not withdrawn, f"pinned to a YANKED release: {withdrawn}"
