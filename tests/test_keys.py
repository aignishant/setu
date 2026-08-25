"""Day 3: prove the secrets are handled safely and the budget rules are mechanical."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REQUIRED_VARS = (
    "GEMINI_API_KEY",
    "GROQ_API_KEY",
    "OPENROUTER_API_KEY",
    "SUPABASE_DB_URL",
    "MONGODB_URI",
)

# Anything long, unbroken and secret-shaped, inside quotes, anywhere in the history.
SECRET_SHAPED = re.compile(r"[\"'][A-Za-z0-9_\-]{32,}[\"']")
CREDENTIAL_SUFFIXES = (".env", ".pem", ".key", ".p12", ".pfx")


def _git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False)


def test_env_example_lists_every_variable_with_no_values() -> None:
    """The shape is committed; the values never are. Part 1.1."""
    lines = (ROOT / ".env.example").read_text(encoding="utf-8").splitlines()
    assignments = {}
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        name, _, value = stripped.partition("=")
        assignments[name.strip()] = value.strip()

    missing = [name for name in REQUIRED_VARS if name not in assignments]
    assert not missing, f".env.example does not list: {missing}"

    # A placeholder that is a real key is exactly how these get committed. The failure names the
    # variable and never the value - printing it here would put the secret in a CI log.
    filled = [name for name, value in assignments.items() if value]
    assert not filled, f".env.example has non-empty values for: {filled}"


def test_no_credential_is_tracked_or_was_ever_committed() -> None:
    """Part 1.1: git is the authority, not .gitignore."""
    # .gitignore is a claim. Ask git itself whether it would ignore the file.
    assert _git("check-ignore", "-q", ".env").returncode == 0, "git would NOT ignore .env"

    tracked = _git("ls-files").stdout.splitlines()
    leaked = [p for p in tracked if p.endswith(CREDENTIAL_SUFFIXES) and p != ".env.example"]
    assert not leaked, f"credential-shaped files are TRACKED: {leaked}"

    # Deleting a committed key does nothing: it is still in the previous commit and in every
    # clone. So the honest question is not "is it in the tree" but "was it EVER committed".
    history = _git("rev-list", "--all", "--objects", "--", *CREDENTIAL_SUFFIXES).stdout
    ever = [line.split(maxsplit=1)[-1] for line in history.splitlines() if " " in line]
    ever = [p for p in ever if p != ".env.example"]
    assert not ever, f"credential-shaped files exist in git HISTORY - revoke, do not delete: {ever}"


def test_classify_distinguishes_a_daily_limit_from_a_per_minute_one() -> None:
    """The pure decision function from part 4.2, tested with no network."""
    from gate import classify

    # A daily limit clears tomorrow. Retrying it is five and a half hours of achieving nothing.
    retryable, wait = classify(429, "Quota exceeded: Generate requests per day (RPD)")
    assert retryable is False, "a DAILY 429 must not be retried"
    assert wait is None

    # A per-minute limit with the server's own instruction. The server's number always wins.
    retryable, wait = classify(429, "Rate limit reached, please try again in 3s")
    assert retryable is True
    assert wait == 3.0, "the server's retry hint must be parsed, not guessed at"

    # A 429 with no hint is still retryable - the caller falls back to jittered backoff.
    retryable, wait = classify(429, "Too Many Requests")
    assert retryable is True
    assert wait is None

    assert classify(503, "upstream unavailable")[0] is True, "a 5xx is transient"
    assert classify(401, "invalid api key")[0] is False, "a 401 does not improve with time"
    assert classify(404, "no such model")[0] is False


@pytest.mark.live
def test_every_required_door_answers() -> None:
    """The Phase 0 gate, as a test. Skipped by default; never runs in CI.

    It carries `live` because every assertion here costs a real request against a real free-tier
    allowance, using credentials that deliberately do not exist on a build runner (Day 2, part
    3.3). `./m check` runs on every commit and in CI; a door check inside it would spend quota
    dozens of times a day and go red on a network hiccup that has nothing to do with the commit.
    """
    from gate import run_all

    results = run_all()
    closed = [f"{r.name} ({r.status}: {r.detail})" for r in results if r.blocks_the_phase]
    assert not closed, f"required doors did not answer: {closed}"
