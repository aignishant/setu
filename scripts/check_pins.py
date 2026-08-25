"""Compare this project's pins against the live package index.

    uv run python scripts/check_pins.py            # human table
    uv run python scripts/check_pins.py --markdown  # rows for docs/PINS_DS.md
    uv run python scripts/check_pins.py --json      # machine-readable

Exit status: 0 when every pin matches the index, 1 when anything drifted.
"""

from __future__ import annotations

import json
import re
import sys
import time
import tomllib
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path

from packaging.version import InvalidVersion, Version

ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = ROOT / ".pins-cache.json"
CACHE_TTL_SECONDS = 6 * 60 * 60
USER_AGENT = "setu-pins/1.0 (learning project)"
TIMEOUT_SECONDS = 10

# name[extras] == version, stopping at the ';' that begins an environment marker (part 2.3).
PIN = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)(?:\[[A-Za-z0-9,._-]+\])?\s*==\s*([^\s;]+)")

SIMPLE_ACCEPT = "application/vnd.pypi.simple.v1+json"


@dataclass
class Pin:
    name: str
    pinned: str | None  # None when the dependency is not exactly pinned
    current: str | None = None
    yanked: bool = False  # the release the index currently offers is withdrawn
    error: str | None = None
    # PEP 592 singles out `==` as the one specifier that still installs a yanked file, and `==` is
    # this project's entire pinning style - so "is OUR release withdrawn" is a separate question
    # from "is the index's latest withdrawn", and it is the dangerous one (part 2.2).
    pinned_yanked: bool = False
    from_cache: bool = False
    spec: str = ""

    @property
    def drift(self) -> str:
        """'unpinned' | 'error' | one of classify()'s verdicts."""
        if self.pinned is None:
            return "unpinned"
        if self.error is not None or self.current is None:
            return "error"
        return classify(self.pinned, self.current)

    @property
    def is_finding(self) -> bool:
        """True when this row is something a human has to act on - the exit code (part 2.3)."""
        return self.drift != "none" or self.pinned_yanked


@dataclass
class Report:
    pins: list[Pin] = field(default_factory=list)
    requests_made: int = 0


# --- reading what we actually pinned -------------------------------------------------------


def read_pins(pyproject_path: str) -> list[Pin]:
    """Parse pyproject.toml and return one Pin per declared dependency."""
    doc = tomllib.loads(Path(pyproject_path).read_text(encoding="utf-8"))

    specs = list(doc["project"].get("dependencies", []))
    for group in doc.get("dependency-groups", {}).values():
        # Every group, not just `dev` - hard-coding `dev` breaks the day a `docs` group appears.
        # A group entry may be a table ({include-group = "..."}), which a regex cannot read.
        specs += [s for s in group if isinstance(s, str)]

    pins: list[Pin] = []
    for spec in specs:
        match = PIN.match(spec)
        if match is None:
            # A specifier that is not an exact pin is a floating dependency, and reporting it is
            # half this tool's job (Principle 4).
            pins.append(Pin(name=spec, pinned=None, spec=spec))
        else:
            pins.append(Pin(name=match.group(1), pinned=match.group(2), spec=spec))
    return pins


# --- reading the truth from the index ------------------------------------------------------


def _get_json(url: str, accept: str | None = None) -> dict:
    """One GET, with the two things politeness requires: a name and a deadline."""
    headers = {"User-Agent": USER_AGENT}
    if accept is not None:
        headers["Accept"] = accept
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
        return json.load(response)


def release_is_yanked(name: str, version: str) -> bool:
    """Is this exact release withdrawn? Yanking is per file, so ask about the set (part 2.2)."""
    doc = _get_json(f"https://pypi.org/pypi/{name}/{version}/json")
    return any(bool(f["yanked"]) for f in doc["urls"])


def fetch_current(name: str) -> tuple[str, bool]:
    """Return (latest_stable_version, is_yanked) for one package.

    Raises on failure. The CALLER decides what a failure means, not this function.
    """
    doc = _get_json(f"https://pypi.org/simple/{name}/", accept=SIMPLE_ACCEPT)

    parsed: list[Version] = []
    for raw in doc["versions"]:
        try:
            parsed.append(Version(raw))
        except InvalidVersion:
            continue  # a version PEP 440 cannot read is not one uv would pick either
    stable = [v for v in parsed if not v.is_prerelease]
    if not stable:
        raise LookupError(f"{name} has published no stable release")

    newest = str(max(stable))
    return newest, release_is_yanked(name, newest)


# --- deciding, with no network in sight -----------------------------------------------------


def classify(pinned: str, current: str) -> str:
    """'none' | 'patch' | 'minor' | 'MAJOR' | 'BACKWARDS' - see part 4.2.

    Pure: inputs in, verdict out. That is what makes it testable without PyPI.
    """
    p, c = Version(pinned), Version(current)
    # Most specific condition first, the same rule that orders `except` clauses (part 2.3).
    if p == c:
        return "none"
    if c < p:
        return "BACKWARDS"  # the index went backwards: our pin was probably yanked
    if c.major != p.major:
        return "MAJOR"
    if c.minor != p.minor:
        return "minor"
    return "patch"


# --- the cache, so a re-run is instant and polite --------------------------------------------


def load_cache() -> dict:
    """Entries older than the TTL are never returned - the expiry is on the READ path (part 2.3)."""
    if not CACHE_PATH.exists():
        return {}
    try:
        data = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}  # a corrupt cache is a cache miss, never a crash
    now = time.time()
    return {k: v for k, v in data.items() if now - v.get("fetched", 0) < CACHE_TTL_SECONDS}


def save_cache(cache: dict) -> None:
    CACHE_PATH.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


# --- rendering ------------------------------------------------------------------------------

STATUS = {
    "none": "current",
    "patch": "patch drift",
    "minor": "minor drift",
    "MAJOR": "MAJOR drift",
    "BACKWARDS": "BACKWARDS",
    "unpinned": "NOT PINNED",
    "error": "ERROR",
}


def _note(pin: Pin) -> str:
    if pin.error:
        return pin.error
    notes = []
    if pin.pinned_yanked:
        notes.append("PINNED RELEASE IS YANKED")
    if pin.yanked:
        notes.append("index's latest is yanked")
    return "; ".join(notes)


def render_table(report: Report) -> str:
    rows = [("package", "pinned", "index", "status", "note")]
    rows += [
        (pin.name, pin.pinned or "-", pin.current or "?", STATUS[pin.drift], _note(pin))
        for pin in report.pins
    ]
    widths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]
    lines = [
        "  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)).rstrip() for row in rows
    ]
    lines.insert(1, "  ".join("-" * w for w in widths))
    return "\n".join(lines)


def render_markdown(report: Report) -> str:
    lines = ["| Package | Pinned | Index | Status |", "|---|---|---|---|"]
    for pin in report.pins:
        note = _note(pin)
        status = STATUS[pin.drift] + (f" - {note}" if note else "")
        lines.append(f"| {pin.name} | {pin.pinned or '-'} | {pin.current or '?'} | {status} |")
    return "\n".join(lines)


def render_json(report: Report) -> str:
    payload = {
        "verified": time.strftime("%Y-%m-%d"),
        "requests_made": report.requests_made,
        "drifted": [p.name for p in report.pins if p.is_finding],
        "pins": [asdict(p) | {"drift": p.drift} for p in report.pins],
    }
    return json.dumps(payload, indent=2, sort_keys=True)


# --- the run --------------------------------------------------------------------------------


def check(pins: list[Pin], *, use_cache: bool = True) -> Report:
    """Fill in every pin from the index. One failure may never lose the run (part 2.3)."""
    cache = load_cache() if use_cache else {}
    report = Report(pins=pins)

    for pin in pins:
        if pin.pinned is None:
            continue

        entry = cache.get(pin.name)
        if entry is not None and entry.get("pinned") == pin.pinned:
            pin.current = entry["current"]
            pin.yanked = entry["yanked"]
            pin.pinned_yanked = entry["pinned_yanked"]
            pin.from_cache = True
            continue

        # The try is INSIDE the loop. That is the whole lesson: package three failing must not
        # cost you the answers for packages four to sixty.
        try:
            current, yanked = fetch_current(pin.name)
            report.requests_made += 2
            if current == pin.pinned:
                pinned_yanked = yanked
            else:
                pinned_yanked = release_is_yanked(pin.name, pin.pinned)
                report.requests_made += 1
        except urllib.error.HTTPError as exc:
            # HTTPError is a SUBCLASS of URLError, so it must be caught first - swap these two
            # and a 404 is reported as a network failure, which is worse than a crash.
            pin.error = f"http {exc.code}"
            continue
        except urllib.error.URLError as exc:
            pin.error = f"network: {exc.reason}"
            continue
        except (KeyError, LookupError, ValueError) as exc:
            pin.error = f"index: {exc}"
            continue

        pin.current, pin.yanked, pin.pinned_yanked = current, yanked, pinned_yanked
        cache[pin.name] = {
            "fetched": time.time(),
            "pinned": pin.pinned,
            "current": current,
            "yanked": yanked,
            "pinned_yanked": pinned_yanked,
        }

    if use_cache:
        save_cache(cache)
    return report


def main(argv: list[str]) -> int:
    as_json = "--json" in argv
    as_markdown = "--markdown" in argv
    use_cache = "--refresh" not in argv

    unknown = [a for a in argv if a not in ("--json", "--markdown", "--refresh")]
    if unknown:
        print(f"unknown argument(s): {unknown}", file=sys.stderr)
        print(__doc__, file=sys.stderr)
        return 2

    report = check(read_pins(str(ROOT / "pyproject.toml")), use_cache=use_cache)

    # Data on stdout, chatter on stderr - that is what makes a tool pipeable (part 3.3).
    if as_json:
        print(render_json(report))
    elif as_markdown:
        print(render_markdown(report))
    else:
        print(render_table(report))

    cached = sum(1 for p in report.pins if p.from_cache)
    print(
        f"{len(report.pins)} pins - {cached} from cache - {report.requests_made} requests",
        file=sys.stderr,
    )

    findings = [p for p in report.pins if p.is_finding]
    if findings:
        # The text is a courtesy; the exit status is the tool's real output (part 2.3).
        print(f"findings: {', '.join(p.name for p in findings)}", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
