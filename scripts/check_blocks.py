"""Parse every Python block in days/ and report the ones that are not Python.

    uv run python scripts/check_blocks.py

Exit status: 0 when every block parses, 1 when any block does not. This proves the blocks are
syntactically Python; it does not run them, and therefore proves nothing about whether they work.
"""

from __future__ import annotations

import ast
import re
import sys
import warnings
from collections.abc import Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Three backticks, built rather than typed: a literal fence inside a Python string inside a
# Markdown lesson is the nesting problem this whole file is about (part 2.3).
FENCE = chr(96) * 3

# f-string AND raw string: the `f` half interpolates FENCE, the `r` half stops Python eating `\s`
# before the regex engine sees it. `(?:...)` is non-capturing so findall returns bodies, not pairs.
# `(.*?)` is non-greedy or the first fence would swallow every block to the last one. re.M makes
# ^/$ match at line boundaries; re.S makes `.` cross newlines. Drop either and you silently get
# zero matches.
BLOCK = re.compile(rf"^{FENCE}(?:python|py)\s*$(.*?)^{FENCE}\s*$", re.M | re.S)


def iter_blocks(text: str) -> Iterator[tuple[int, str]]:
    """Yield (line number of the fence in the file, block body) for every python block."""
    for match in BLOCK.finditer(text):
        # The fence's own line, so the report points at the file rather than at an offset inside
        # a block the reader cannot see. This became worth doing the day the script became a gate.
        fence_line = text.count("\n", 0, match.start()) + 1
        yield fence_line, match.group(1)


def python_blocks(text: str) -> list[str]:
    """Every fenced python/py block in one document, in order."""
    return [body for _, body in iter_blocks(text)]


def check_file(path: Path) -> list[str]:
    """Every parse failure in one document, already formatted for printing."""
    failures = []
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()
    for number, (fence_line, block) in enumerate(iter_blocks(text), start=1):
        try:
            # ast.parse raises SyntaxError and EXECUTES NOTHING, which is what makes it safe to
            # point at a lesson whose examples start a server or delete a file.
            #
            # Warnings are suppressed, not failures: a lesson may deliberately show code the
            # parser dislikes but still accepts. Day 7's 1.3 prints "C:\data\reports" precisely
            # to demonstrate an invalid escape sequence, and that block is correct as written.
            # This gate answers one question - does it parse - and a warning is not an answer to it.
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                ast.parse(block)
        except SyntaxError as exc:
            # Catch the specific failure. A bare `except:` would also swallow KeyboardInterrupt
            # (E722, part 1.2).
            where = fence_line + (exc.lineno or 0)
            failures.append(f"{rel}:{where}: block {number}: {exc.msg}")
    return failures


def main() -> int:
    bad: list[str] = []
    files = 0
    for path in sorted((ROOT / "days").rglob("*.md")):
        files += 1
        bad.extend(check_file(path))

    for failure in bad:
        print(failure)
    print(f"{files} documents - unparseable python blocks: {len(bad)}")
    # The exit code, so this can join a gate. A checking tool that only prints is one people stop
    # reading (part 2.2).
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
