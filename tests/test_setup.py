"""Day 0: prove the setup is real, not assumed."""

import re
import subprocess
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# name[extras]==version - anything else (>=, ~=, a bare name, a range) is not a pin.
EXACT_PIN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*(\[[A-Za-z0-9,._-]+\])?==[^,;\s]+$")


def _git(*args: str) -> subprocess.CompletedProcess[str]:
    """Run git inside the repo root and hand back the finished process, never raising."""
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_pins_are_exact() -> None:
    """Every dependency in pyproject.toml uses == and not a range (Principle 4)."""
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    specs = list(config["project"].get("dependencies", []))
    for group in config.get("dependency-groups", {}).values():
        specs.extend(s for s in group if isinstance(s, str))

    assert specs, "pyproject.toml declares no dependencies at all - nothing was pinned"
    loose = [s for s in specs if not EXACT_PIN.match(s)]
    assert not loose, f"not pinned with ==: {loose}"


def test_env_file_is_ignored() -> None:
    """.env is ignored BEFORE it exists (Principle 5, part 2.2)."""
    rules = [
        line.strip()
        for line in (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    assert ".env" in rules, ".gitignore has no bare `.env` rule"
    assert ".env.*" in rules, ".gitignore does not ignore `.env.local`, `.env.prod`, ..."
    assert "!.env.example" in rules, ".env.example must be re-included so the shape is committed"

    # The rules are only a claim; git is the authority. Ask it directly.
    assert _git("check-ignore", "-q", ".env").returncode == 0, "git would NOT ignore .env"
    assert _git("check-ignore", "-q", ".env.example").returncode != 0, ".env.example is ignored"


def test_daily_driver_is_executable() -> None:
    """./m exists, is executable, and is in strict mode (part 3.1)."""
    driver = ROOT / "m"
    assert driver.is_file(), "./m does not exist - the daily driver is the day's build brief"

    head = driver.read_text(encoding="utf-8").splitlines()[:5]
    assert head[0] in ("#!/usr/bin/env bash", "#!/bin/bash"), f"bad shebang: {head[0]!r}"
    assert any(line.strip() == "set -euo pipefail" for line in head), "m is not in strict mode"

    # On Windows the filesystem has no exec bit, so the mode Git recorded is the portable truth.
    mode = _git("ls-files", "-s", "--", "m").stdout.split(maxsplit=1)[0]
    assert mode == "100755", f"m is committed as {mode}, not 100755 - run chmod +x m"
