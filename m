#!/usr/bin/env bash
# Project Setu daily driver. Replaces `make` (not installed on Windows).
set -euo pipefail

DAY="${2:-}"
pad() { printf "%02d" "$1"; }

# Day folders are days/day-<NN>-<slug> (plan v2.1.0), so the slug is free text and the number is
# the only stable handle - glob on it. The unslugged forms still resolve so an older folder is not
# suddenly invisible; ./m depth is what complains about the name.
daydir() {
  local n d
  n="$(pad "$1")"
  for d in days/day-"$n"-*; do
    [ -d "$d" ] && { echo "$d"; return; }
  done
  if [ -d "days/day-$n" ]; then echo "days/day-$n"
  elif [ -d "days/day-$1" ]; then echo "days/day-$1"
  else echo ""; fi
}

case "${1:-help}" in
  start)
    [ -z "$DAY" ] && { echo "usage: ./m start <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no lesson written yet for day $DAY"; exit 1; }
    echo "-> open $D/LESSON.md"
    ;;
  scaffold)
    [ -z "$DAY" ] && { echo "usage: ./m scaffold <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || {
      echo "no folder for day $DAY yet - write the day first (/day-setu $DAY)."
      echo "day folders are named days/day-$(pad "$DAY")-<slug>, never bare days/day-$(pad "$DAY")."
      exit 1
    }
    mkdir -p "$D/lab"
    echo "-> created $D/lab"
    ;;
  parts)
    [ -z "$DAY" ] && { echo "usage: ./m parts <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no lesson written yet for day $DAY"; exit 1; }
    for S in "$D"/parts/*/; do
      [ -d "$S" ] || continue
      echo "$(basename "$S")"
      for F in "$S"*.md; do [ -f "$F" ] && echo "    $(basename "$F")"; done
    done
    ;;
  depth)
    if [ -n "$DAY" ]; then uv run python scripts/depth_check.py "$DAY"
    else uv run python scripts/depth_check.py; fi
    ;;
  tracker)
    uv run python scripts/tracker.py
    ;;
  check)
    uv run ruff check .
    uv run ruff format --check .
    # pytest exits 5 when it collected nothing. Until the first day writes a test that is the
    # honest state of the repo, not a failure - but it is said out loud, because a silently
    # empty test run is exactly how Principle 7 rots. Every other exit code is still fatal.
    set +e
    uv run python -m pytest -q -m "not live"
    PYTEST=$?
    set -e
    if [ "$PYTEST" -eq 5 ]; then
      echo "WARN pytest collected no tests yet (Principle 7: every lab ends with one that can go RED)"
    elif [ "$PYTEST" -ne 0 ]; then
      exit "$PYTEST"
    fi
    uv run python scripts/depth_check.py
    echo "OK all green"
    ;;
  status)
    uv run python scripts/tracker.py --summary 2>/dev/null \
      || git log --oneline --grep='^day-' -1 --pretty='last completed: %s'
    ;;
  done)
    [ -z "$DAY" ] && { echo "usage: ./m done <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no day folder for $DAY"; exit 1; }
    C="$D/CHECKLIST.md"
    if grep -q '^- \[ \]' "$C"; then
      echo "FAIL unticked boxes remain in $C"
      grep -n '^- \[ \]' "$C"
      exit 1
    fi
    "$0" check
    git add -A && git commit -m "day-$(pad "$DAY"): complete"
    echo "OK day $DAY committed"
    ;;
  *)
    cat <<'USAGE'
usage: ./m <command> [day]

  start N        point at day N's lesson
  parts N        list day N's sections and their part documents
  scaffold N     create the lab/ folder inside day N's folder
  depth [N]      run the depth contract over day N, or every written day
  tracker        regenerate docs/TRACKER.md from the index and what is on disk
  check          ruff + ruff format + offline pytest + the depth contract
  status         one-line progress
  done N         refuse unless the checklist is ticked and check is green, then commit
USAGE
    ;;
esac
