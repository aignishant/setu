"""How Setu reads configuration. Nothing below knows a file exists.

Every later day imports from here rather than reading `.env` itself. The rule this module exists
to enforce is one line long: **code reads the environment, never the file** — so the same code
runs unchanged on a laptop with a `.env`, in CI with no secrets at all, and on a host where the
values arrive from a secret manager.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

# Called once, at import, as close to the entry point as possible. In production there is no
# .env file and this is a no-op - which is exactly why the rest of the module reads os.environ.
load_dotenv()

# A tuple, not a list: this is a constant, and immutability makes that visible.
# All five are required by the Phase 0 gate. A database connection string is a credential in
# exactly the same sense as an API key - it just happens to carry a password inside a URL.
REQUIRED = (
    "GEMINI_API_KEY",
    "GROQ_API_KEY",
    "OPENROUTER_API_KEY",
    "SUPABASE_DB_URL",
    "MONGODB_URI",
)

_HELP = "days/day-03-keys-and-budget/parts/01-secrets/1.2-dotenv-and-os-environ.md"

# The only values a "true" may take. bool("false") is True, because a non-empty string is truthy,
# and that is the single most common environment-variable bug in existence.
_TRUTHY = frozenset({"1", "true", "yes", "on"})


def require(name: str) -> str:
    """Return an environment variable, failing loudly and immediately when it is absent."""
    try:
        return os.environ[name]
    except KeyError:
        # Re-raise something that says what to DO. A bare KeyError says what is missing; this
        # says how to fix it. `from None` drops the chained traceback, which adds nothing here
        # and pushes the useful message away from where people look.
        raise RuntimeError(
            f"{name} is not set. Copy .env.example to .env and fill it in - see {_HELP}"
        ) from None


def optional(name: str) -> str | None:
    """Return an environment variable, or None when absence is a state to branch on."""
    value = os.environ.get(name)
    # `or None` collapses missing and empty to one answer. An empty variable is a real and common
    # state - a .env line with nothing after the `=` - and treating "" as present buys you an
    # authentication failure where you wanted a clear absence.
    return value or None


def flag(name: str, *, default: bool = False) -> bool:
    """Read a boolean from the environment, explicitly. Never `bool()` on the raw string."""
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    return raw.strip().lower() in _TRUTHY


def which_keys_are_present() -> dict[str, bool]:
    """Report presence by NAME only. Never returns or logs a value (part 1.1).

    Every diagnostic in this project reports presence this way, so that a screenshot of a
    terminal is never a leak.
    """
    return {name: bool(os.environ.get(name)) for name in REQUIRED}


def missing_keys() -> list[str]:
    """The names of the required variables that are not set, in declaration order."""
    return [name for name, present in which_keys_are_present().items() if not present]
