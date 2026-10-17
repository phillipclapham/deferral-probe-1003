#!/bin/sh
# Check every relative-path hash in the stamp files against the files in probe/.
# Expected: every line OK except probe/PREREGISTRATION.md, which carries the one-line
# redaction described in WITHHELD.md. The stamps' absolute-path lines name files that
# are withheld (WITHHELD.md gives their hashes).
cd "$(dirname "$0")/probe" || exit 1
for s in *_STAMP.txt; do grep -E '^[0-9a-f]{64}  [^/]' "$s"; done | shasum -a 256 -c
echo
echo "Re-running the pre-registered phase Z analysis:"
python3 fisher_z.py
