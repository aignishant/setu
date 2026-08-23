"""Day 0: prove the setup is real, not assumed."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_pins_are_exact() -> None:
    """Every dependency in pyproject.toml uses == and not a range (Principle 4)."""
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    # TODO(me): collect every dependency specification from the [project] and
    # [dependency-groups] blocks, and assert each one contains "==".
    # Hint: the specs are the quoted strings inside the two list literals.
    raise NotImplementedError


def test_env_file_is_ignored() -> None:
    """.env is ignored BEFORE it exists (Principle 5, part 2.2)."""
    # TODO(me): assert that .gitignore contains a rule matching .env,
    # and that .env.example is re-included.
    raise NotImplementedError


def test_daily_driver_is_executable() -> None:
    """./m exists, is executable, and is in strict mode (part 3.1)."""
    # TODO(me): assert m exists, that its first line is a bash shebang,
    # and that "set -euo pipefail" appears in the first few lines.
    raise NotImplementedError
