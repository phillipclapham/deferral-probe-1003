#!/usr/bin/env python3
"""Phase Z analysis, frozen with ADDENDUM_Z_PREREG.md before any Z run.

One-sided Fisher exact test on DEFER counts (ASK and PROCEED both count as not-DEFER), for each
pre-registered contrast, plus Holm-Bonferroni across the two PRIMARY contrasts and, separately,
across the two SECONDARY ones. Reads runs/manifest.jsonl + classify/labels_Z.jsonl.
"""
import json
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def fisher_greater(a, n1, c, n2):
    """P(X >= a) for X = defers in group 1, under the hypergeometric null with margins fixed."""
    k, n = a + c, n1 + n2
    return sum(comb(k, x) * comb(n - k, n1 - x) for x in range(a, min(k, n1) + 1)) / comb(n, n1)


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i])
    adj, running = [0.0] * len(ps), 0.0
    for rank, i in enumerate(order):
        running = max(running, min(1.0, (len(ps) - rank) * ps[i]))
        adj[i] = running
    return adj


# (label, group expected to defer MORE, group expected to defer LESS); cells = (model, arm, scenario)
PRIMARY = [
    ("W: opus-5-5 vs opus-5, bare, memory lines",
     ("claude-opus-5-5", "A", "X_S1PM"), ("claude-opus-5", "A", "X_S1PM")),
    ("H: bare vs pre-10:29 flow, opus-5-5, memory lines",
     ("claude-opus-5-5", "A", "X_S1PM"), ("claude-opus-5-5", "Bm", "X_S1PM")),
]
SECONDARY = [
    ("patch: pre-10:29 vs current flow, memory lines",
     ("claude-opus-5-5", "Bm", "X_S1PM"), ("claude-opus-5-5", "B", "X_S1PM")),
    ("patch: pre-10:29 vs current flow, no-sixth-round",
     ("claude-opus-5-5", "Bm", "X_S1NS"), ("claude-opus-5-5", "B", "X_S1NS")),
]

if __name__ == "__main__":
    man = {json.loads(l)["run_id"]: json.loads(l) for l in open(ROOT / "runs/manifest.jsonl")}
    lab = {json.loads(l)["run_id"]: json.loads(l) for l in open(ROOT / "classify/labels_Z.jsonl")}
    cells = {}
    for rid, m in man.items():
        if m["phase"] != "Z":
            continue
        key = (m["model"], m["arm"], m["scenario"])
        d, n = cells.get(key, (0, 0))
        cells[key] = (d + (lab[rid]["label"] == "DEFER"), n + 1)
    print("| model | arm | scenario | DEFER / n |\n|---|---|---|---|")
    for k in sorted(cells):
        print(f"| {k[0]} | {k[1]} | {k[2]} | {cells[k][0]} / {cells[k][1]} |")
    for name, fam in (("PRIMARY", PRIMARY), ("SECONDARY", SECONDARY)):
        ps = [fisher_greater(*cells[hi], *cells[lo]) for _, hi, lo in fam]
        print(f"\n{name} (one-sided Fisher exact; Holm within family; threshold adj p < 0.05)")
        for (label, hi, lo), p, pa in zip(fam, ps, holm(ps)):
            print(f"- {label}: {cells[hi][0]}/{cells[hi][1]} vs {cells[lo][0]}/{cells[lo][1]}"
                  f"  p={p:.4f}  Holm-adj={pa:.4f}  -> {'SUPPORTED' if pa < 0.05 else 'not supported'}")
