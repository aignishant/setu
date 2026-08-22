#!/usr/bin/env bash
# Project Setu daily driver. Replaces `make` (not installed on Windows).
set -euo pipefail

DAY="${2:-}"
pad() { printf "%02d" "$1"; }

daydir() {
  local n="$1"
  if [ -d "days/day-$(pad "$n")" ]; then echo "days/day-$(pad "$n")"
  elif [ -d "days/day-$n" ]; then echo "days/day-$n"
  else echo ""; fi
}

case "${1:-help}" in
  start)
    [ -z "$DAY" ] && { echo "usage: ./m start <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no lesson written yet for day $DAY - see docs/TRACKER.md"; exit 1; }
    if [ -f "$D/LESSON.md" ] && [ -d "$D/parts" ]; then
      echo "-> open $D/LESSON.md   (the hub - read its §2 map, then work through parts/ in order)"
      ls "$D/parts" | sed 's|^|     parts/|'
    elif [ -f "$D/_legacy/LESSON.md" ]; then
      echo "!! day $DAY is still on the v1.0.0 single-file format (plan Part 11 not applied yet)."
      echo "-> open $D/_legacy/LESSON.md   -- workable, but regenerate it with /day-setu $DAY"
    else
      echo "no lesson written yet for day $DAY - see docs/TRACKER.md"; exit 1
    fi
    ;;

  parts)
    [ -z "$DAY" ] && { echo "usage: ./m parts <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -d "$D/parts" ] || { echo "day $DAY has no parts/ - it is not written (plan Part 11)"; exit 1; }
    ls "$D/parts"
    ;;

  depth)
    if [ -n "$DAY" ]; then uv run python scripts/depth_check.py "$DAY"
    else uv run python scripts/depth_check.py; fi
    ;;
  scaffold)
    [ -z "$DAY" ] && { echo "usage: ./m scaffold <day>"; exit 1; }
    mkdir -p "days/day-$(pad "$DAY")/lab"
    echo "-> created days/day-$(pad "$DAY")/lab"
    ;;
  check)
    uv run ruff check .
    uv run ruff format --check .
    uv run python -m pytest -q -m "not live"
    uv run python scripts/depth_check.py
    echo "OK all green"
    ;;
  tracker)
    uv run python scripts/tracker.py
    ;;
  status)
    uv run python scripts/tracker.py --summary
    ;;
  done)
    [ -z "$DAY" ] && { echo "usage: ./m done <day>"; exit 1; }
    D="$(daydir "$DAY")"
    [ -n "$D" ] || { echo "no day folder for $DAY"; exit 1; }
    C="$D/CHECKLIST.md"
    if grep -q '^- \[ \]' "$C"; then
      echo "FAIL unticked boxes remain in $C"; grep -n '^- \[ \]' "$C"; exit 1
    fi
    "$0" check
    uv run python scripts/tracker.py
    git add -A && git commit -m "day-$(pad "$DAY"): complete"
    echo "OK day $DAY committed"
    ;;
  *)
    cat <<'USAGE'
usage: ./m <command> [day]

  status         how many days are written / complete
  tracker        regenerate docs/TRACKER.md
  start N        point at day N's hub and list its parts/
  parts N        list day N's sub-topic documents
  depth [N]      check day N (or every written day) against the plan's Part 11 depth contract
  scaffold N     create days/day-NN/lab/
  check          ruff + ruff format + offline pytest + depth contract
  done N         refuse unless checklist ticked and checks green, then commit
USAGE
    ;;
esac
