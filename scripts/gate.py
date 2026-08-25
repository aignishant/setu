"""Prove every Phase 0 door answers. Prints no secrets, ever.

    uv run python scripts/gate.py

Exit status: 0 when every REQUIRED door answered, 1 otherwise. Optional doors are
reported and never block.
"""

from __future__ import annotations

import os
import random
import re
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass
from urllib.parse import urlsplit

from dotenv import load_dotenv

load_dotenv()

# Every model id is typed out, never left to a framework default (Principle 4). The two that are
# perishable carry the date they were chosen, because "it worked once" is not provenance.
GEMINI_MODEL = "gemini-3.7-flash"
GROQ_MODEL = "llama-3.3-70b-versatile"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
# Chosen on 2026-08-26 from the live catalogue at /api/v1/models, which listed 17 `:free` ids that
# day. PERISHABLE: when this 404s, that is a decision to make from a fresh listing (part 2.3), not
# a patch to apply.
OPENROUTER_MODEL = "google/gemma-4-31b-it:free"
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:3b"  # tag included: `llama3.2` alone is a moving pointer

PROBE_PROMPT = "Reply with the word: ok"


# --- deciding whether a failure is worth another attempt (part 4.2) -------------------------

# Providers word the daily limit differently, so the pattern carries alternatives. This is
# string-matching an error message, which is genuinely fragile - prefer a structured field
# wherever an SDK exposes one, and treat this as the fallback.
DAILY = re.compile(r"per\s*day|RPD|requests per day|Generate requests per day", re.I)
WAIT_HINT = re.compile(r"try again in\s*([0-9.]+)\s*s", re.I)


def classify(status: int, body: str) -> tuple[bool, float | None]:
    """Return (is_retryable, retry_after_seconds). Pure: no network, no clock, no sleeping."""
    if status in (500, 502, 503, 504):
        return True, None  # note 501 is absent: "not implemented" will not become implemented
    if status == 429:
        # The daily check comes FIRST - most specific condition before the general one. Get this
        # backwards and every daily limit is retried as if it were a per-minute one, which is
        # five and a half hours of achieving nothing (part 4.1).
        if DAILY.search(body):
            return False, None
        hint = WAIT_HINT.search(body)
        return True, float(hint.group(1)) if hint else None
    # Default to NOT retrying. 400, 401, 403, 404 - none of these improve with time, and an
    # unrecognised failure is not known to be transient.
    return False, None


class Retryable(Exception):
    """Raised by a caller's classifier when a failure is worth another attempt."""

    def __init__(self, message: str, retry_after: float | None = None) -> None:
        super().__init__(message)
        self.retry_after = retry_after


def with_backoff[T](
    operation: Callable[[], T],
    *,
    attempts: int = 5,
    base: float = 1.0,
    cap: float = 30.0,
) -> T:
    """Call operation, retrying only Retryable failures. Everything else propagates."""
    last: Retryable | None = None
    for attempt in range(1, attempts + 1):
        try:
            return operation()
        except Retryable as exc:
            last = exc
            if attempt == attempts:
                break  # do not sleep after the final attempt
            if exc.retry_after is not None:
                delay, source = exc.retry_after, "server"  # the server's number always wins
            else:
                # Full jitter, UNSEEDED. Two hundred careful clients with an unjittered schedule
                # come back in unison and turn a slow service into a dead one.
                delay = random.uniform(0, min(cap, base * 2 ** (attempt - 1)))
                source = "backoff"
            print(f"  retry {attempt}/{attempts}: waiting {delay:.2f}s ({source})", file=sys.stderr)
            time.sleep(delay)
    raise RuntimeError(f"gave up after {attempts} attempts") from last


# --- one uniform result per door (part 5.1) --------------------------------------------------


@dataclass(frozen=True)
class DoorResult:
    """What one check found. `detail` must never contain a credential."""

    name: str
    required: bool
    present: bool
    answered: bool
    seconds: float
    detail: str

    @property
    def status(self) -> str:
        if self.answered:
            return "OK"
        if not self.present:
            return "ABSENT"  # never configured
        return "FAILED"  # configured, but not working - a different action entirely

    @property
    def blocks_the_phase(self) -> bool:
        return self.required and not self.answered


def timed(name: str, required: bool, env_var: str | None, probe: Callable[[], str]) -> DoorResult:
    """Run one probe, catching everything, and return a uniform result."""
    present = True if env_var is None else bool(os.environ.get(env_var))
    if not present:
        return DoorResult(name, required, False, False, 0.0, f"{env_var} is not set")

    start = time.perf_counter()
    try:
        detail = probe()
        return DoorResult(name, required, True, True, time.perf_counter() - start, detail)
    except Exception as exc:
        # Deliberately broad, and correct HERE and nowhere else: this function's job is to
        # survive every probe so that one door's exotic failure cannot cost you the other five.
        # The class name AND the message - the class alone is too vague, the message alone loses
        # the type, which is often the most diagnostic part.
        return DoorResult(
            name, required, True, False, time.perf_counter() - start, f"{type(exc).__name__}: {exc}"
        )


# --- the probes: one minimal call each, returning a SAFE one-line summary ---------------------
# Every import is inside its probe. A machine with no Mongo driver installed still checks Gemini;
# a missing import becomes one door's FAILED rather than the whole script's crash.


def probe_gemini() -> str:
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    reply = client.interactions.create(model=GEMINI_MODEL, input=PROBE_PROMPT)
    # Truncated and repr'd: truncated so a chatty model cannot flood the report, repr'd so an
    # EMPTY answer is visible rather than looking like a blank column.
    return f"{GEMINI_MODEL} -> {(reply.output_text or '').strip()[:20]!r}"


def probe_groq() -> str:
    from groq import Groq

    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    # Note the shape: messages=[{role, content}], and the text lives at
    # .choices[0].message.content - nothing like Gemini's. Two of the three doors share this
    # shape, which is exactly why people assume all three do.
    completion = client.chat.completions.create(
        messages=[{"role": "user", "content": PROBE_PROMPT}],
        model=GROQ_MODEL,
    )
    text = completion.choices[0].message.content or ""
    return f"{GROQ_MODEL} -> {text.strip()[:20]!r}"


def probe_openrouter() -> str:
    from openai import OpenAI

    client = OpenAI(
        base_url=OPENROUTER_BASE_URL,
        api_key=os.environ["OPENROUTER_API_KEY"],
        timeout=30.0,
    )
    completion = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[{"role": "user", "content": PROBE_PROMPT}],
    )
    text = completion.choices[0].message.content or ""
    return f"{OPENROUTER_MODEL} -> {text.strip()[:20]!r}"


def probe_supabase() -> str:
    import psycopg

    dsn = os.environ["SUPABASE_DB_URL"]

    def connect_once() -> tuple[str, str]:
        try:
            with psycopg.connect(dsn, connect_timeout=15) as conn, conn.cursor() as cur:
                cur.execute("select current_user, current_database()")
                return cur.fetchone()
        except psycopg.OperationalError as exc:
            # A free project PAUSES when idle, and the first connection after that is what wakes
            # it. Narrow, on purpose: this is the opposite choice from `timed`'s broad catch,
            # because here we know exactly which failure is worth another attempt (part 3.1).
            raise Retryable(f"database not answering yet: {exc}") from exc

    user, database = with_backoff(connect_once, attempts=3, base=2.0, cap=10.0)
    # The HOSTNAME only, never the connection string - it carries the password. Reporting
    # current_user states the blast radius of the credential just used (part 1.3).
    return f"host={urlsplit(dsn).hostname} user={user} db={database}"


def probe_mongo() -> str:
    from pymongo import MongoClient

    uri = os.environ["MONGODB_URI"]
    # A short selection timeout, so a missing IP allowlist entry fails FAST rather than
    # mysteriously - a blocked address times out, it is never refused (part 3.2).
    client = MongoClient(uri, serverSelectionTimeoutMS=8000)
    try:
        client.admin.command("ping")
        return f"host={urlsplit(uri).hostname} ping=ok"
    finally:
        # In finally: a gate that leaks a connection pool on every failure eventually exhausts a
        # free tier's connection slots.
        client.close()


def probe_ollama() -> str:
    import json
    import urllib.error
    import urllib.request

    payload = json.dumps({"model": OLLAMA_MODEL, "prompt": PROBE_PROMPT, "stream": False})
    request = urllib.request.Request(
        OLLAMA_ENDPOINT,
        data=payload.encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        # A long timeout: a small model on a laptop CPU is genuinely slow, and RAM is a
        # categorically different ceiling from a rate limit - it does not reset in a minute.
        with urllib.request.urlopen(request, timeout=120.0) as response:
            text = json.load(response)["response"]
    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"the local runner is not answering on {OLLAMA_ENDPOINT} "
            f"- is it running? ({exc.reason})"
        ) from exc
    return f"{OLLAMA_MODEL} -> {text.strip()[:20]!r}"


# (name, required, env_var or None, probe)
DOORS: list[tuple[str, bool, str | None, Callable[[], str]]] = [
    ("gemini", True, "GEMINI_API_KEY", probe_gemini),
    ("groq", True, "GROQ_API_KEY", probe_groq),
    ("openrouter", True, "OPENROUTER_API_KEY", probe_openrouter),
    ("supabase", True, "SUPABASE_DB_URL", probe_supabase),
    ("mongodb", True, "MONGODB_URI", probe_mongo),
    ("ollama", False, None, probe_ollama),
]


def run_all() -> list[DoorResult]:
    """Check every door. Gather failures; never stop at the first.

    This is the OPPOSITE choice from `./m check`, and deliberately so. The gate in Day 2 stops at
    the first failure because its findings are usually consequences of one another - a syntax
    error makes forty tests fail, and the first message is the true one. These six doors are
    independent: a revoked Gemini key tells you nothing about whether Mongo's allowlist is right.
    Stopping early here would mean six runs, and five accounts checked one evening at a time.
    """
    return [timed(name, required, env_var, probe) for name, required, env_var, probe in DOORS]


def report(results: list[DoorResult]) -> int:
    width = max(len(r.name) for r in results)
    print(f"{'door':<{width}}  {'status':<7} {'req':<4} {'secs':>6}  detail")
    print("-" * (width + 40))
    for r in results:
        flag = "yes" if r.required else "opt"
        print(f"{r.name:<{width}}  {r.status:<7} {flag:<4} {r.seconds:>6.2f}  {r.detail}")

    blocked = [r.name for r in results if r.blocks_the_phase]
    calls = sum(1 for r in results if r.present and r.name != "ollama")
    print()
    # Printed EVERY run, including when the number is boring. That is the habit (part 4.3).
    print(f"--- receipt: {calls} live requests, $0 (Principle 5) ---")

    if blocked:
        print(f"\nPHASE 0 INCOMPLETE - required doors closed: {', '.join(blocked)}")
        return 1
    print("\nPHASE 0 GATE: every required door answered.")
    return 0


if __name__ == "__main__":
    sys.exit(report(run_all()))
