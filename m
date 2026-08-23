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
    [ -n "$D" ] || { echo "no lesson written yet for day $DAY"; exit 1; }
    echo "-> open $D/LESSON.md"
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
  scaffold N     create days/day-NN/lab/
  check          ruff + ruff format + offline pytest
USAGE
    ;;
esac
