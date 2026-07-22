#!/usr/bin/env bash
# Render a signature HTML at @2x in headless Chrome and pixel-diff it against the
# Figma reference render.
#
#   ./scripts/qa-diff.sh signature-2-v4.html qa/ref/figma-1-2282@2x.png 600 488
#
# Image URLs are rewritten from the GitHub Pages host to the local preview server
# so the diff reflects the assets in this working tree, not what is deployed.
set -euo pipefail

HTML="${1:?usage: qa-diff.sh <html> <reference.png> <width@1x> <height@1x>}"
REF="${2:?}"
W="${3:?}"
H="${4:?}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CHROME="$(ls -d "$HOME"/.cache/puppeteer/chrome-headless-shell/mac_arm-*/chrome-headless-shell-mac-arm64/chrome-headless-shell | sort -V | tail -1)"

# whichever preview port is actually up (launch.json has moved between ports)
BASE="${PREVIEW_BASE:-}"
if [ -z "$BASE" ]; then
  for p in 8765 8907; do
    if curl -s -o /dev/null --max-time 1 "http://localhost:$p/"; then BASE="http://localhost:$p"; break; fi
  done
fi
[ -n "$BASE" ] || { echo "no preview server on 8765/8907 — start it, or set PREVIEW_BASE" >&2; exit 1; }
OUT="$ROOT/qa/out"
mkdir -p "$OUT"

NAME="$(basename "$HTML" .html)"
STAGED="$ROOT/qa/out/$NAME.staged.html"

# point assets at the local server, and strip the preview page chrome so the
# screenshot is the signature and nothing else
sed -e "s#https://chife-mod.github.io/Eplug_Gmail_Signature#$BASE#g" \
    -e "s|<body[^>]*>|<body style=\"margin:0;padding:0;background:#FFFFFF;\">|" \
    "$ROOT/$HTML" > "$STAGED"

"$CHROME" \
  --headless --disable-gpu --hide-scrollbars --no-sandbox \
  --force-device-scale-factor=2 \
  --default-background-color=FFFFFFFF \
  --window-size="$W,$H" \
  --virtual-time-budget=8000 \
  --screenshot="$OUT/$NAME.png" \
  "$BASE/qa/out/$NAME.staged.html" >/dev/null 2>&1

python3 "$ROOT/scripts/qa-diff.py" "$OUT/$NAME.png" "$ROOT/$REF" "$OUT/$NAME.diff.png"
