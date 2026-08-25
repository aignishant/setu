"""Day 2: prove the gate is a gate, and that the budget rule is mechanical."""

from __future__ import annotations

import os
import shutil
import subprocess
import tomllib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PROVIDER_KEYS = ("GEMINI_API_KEY", "GROQ_API_KEY", "OPENROUTER_API_KEY", "OPENAI_API_KEY")
REQUIRED_FAMILIES = ("E", "F", "I", "UP", "B", "SIM")

# This test runs ./m check, and ./m check runs this test. Today the recursion cannot happen -
# gate one refuses the unparseable probe file and `set -e` stops the script before pytest - but
# that safety is an accident of gate ORDER, not a property of the test. Reorder the gates and the
# inner run reaches pytest, which spawns another gate, forever. The sentinel makes the base case
# explicit instead of emergent: the child run knows it is the child and declines to have children.
GATE_PROBE = "SETU_GATE_PROBE"


def _pyproject() -> dict:
    return tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))


def test_ruff_config_selects_the_six_families() -> None:
    """Principle 4: the rule set is a pin too. See part 1.2."""
    select = _pyproject()["tool"]["ruff"]["lint"]["select"]

    missing = [family for family in REQUIRED_FAMILIES if family not in select]
    assert not missing, f"[tool.ruff.lint].select is missing rule families: {missing}"


def test_markers_are_declared_and_strict() -> None:
    """An undeclared marker must be an error, not a new category. Part 3.3."""
    pytest_config = _pyproject()["tool"]["pytest"]["ini_options"]
    declared = " ".join(pytest_config["markers"])

    for marker in ("live", "slow"):
        assert f"{marker}:" in declared, f"marker {marker!r} is not declared in pyproject.toml"

    # Both halves matter, and this is the half people leave out. Declaring the markers only
    # documents them: without --strict-markers a MISSPELLED marker is silently accepted as a
    # brand-new one, so `@pytest.mark.liv` creates a category nothing deselects and the test it
    # guards runs in CI making live calls. Declaration says what exists; the flag makes anything
    # else an error at collection time instead of a surprise on the bill.
    assert "--strict-markers" in pytest_config["addopts"], (
        "markers are declared but --strict-markers is not in addopts, so a typo still passes"
    )


def test_the_gate_refuses_broken_code() -> None:
    """./m check must exit non-zero when the tree is broken. Part 4.1."""
    if os.environ.get(GATE_PROBE) == "1":
        pytest.skip("this run IS the gate spawned by the outer copy of this test")

    bash = shutil.which("bash")
    if bash is None:
        pytest.skip("./m needs bash; not on this PATH")

    broken = ROOT / "src" / "setu" / "_gate_probe.py"
    try:
        broken.write_text("def broken(\n", encoding="utf-8")
        result = subprocess.run(
            [bash, "m", "check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            # OneDrive cannot hardlink into uv's cache, and a gate that failed for THAT reason
            # would pass this test for the wrong reason entirely.
            env=os.environ | {"UV_LINK_MODE": "copy", GATE_PROBE: "1"},
        )
        assert result.returncode != 0, "./m check passed with an unparseable file in src/setu/"
        # Not just "it failed" - it failed FOR THIS REASON. A test that only checks the exit code
        # would stay green if the gate broke for an unrelated reason, which is the exact failure
        # this whole day is about (part 3.1).
        assert "_gate_probe" in result.stdout + result.stderr, (
            f"the gate refused, but never named the broken file:\n{result.stdout}{result.stderr}"
        )
    finally:
        # In `finally`, always: one failed run must not leave the repository broken - which is the
        # bug this test exists to catch, one level up.
        broken.unlink(missing_ok=True)


def test_ci_holds_no_provider_keys() -> None:
    """Principle 5, as a test rather than as a promise. Part 5.3."""
    if os.environ.get("CI") != "true":
        pytest.skip("not running in CI; this asserts about the build machine, not your laptop")

    # Names only. Printing a value here would put a live credential into a public build log,
    # which is a worse outcome than the thing being tested.
    present = [name for name in PROVIDER_KEYS if os.environ.get(name)]
    assert not present, f"provider keys are set in CI: {present}"
