#!/usr/bin/env python3
"""Compare the original phase Z labels with the two 17 Oct relabels: agreement, kappa,
and the pre-registered phase Z contrasts under each label set (fisher_z.py's test and Holm)."""
import json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "probe"))
from fisher_z import PRIMARY, SECONDARY, fisher_greater, holm  # noqa: E402


def load(p):
    return {json.loads(l)["run_id"]: json.loads(l) for l in open(p)}


man = load(HERE.parent / "probe/runs/manifest.jsonl")
sets = {"original": load(HERE.parent / "probe/classify/labels_Z.jsonl"),
        "L1": load(HERE / "labels_L1.jsonl"), "L2": load(HERE / "labels_L2.jsonl")}
ids = sorted(sets["original"])
assert all(sorted(s) == ids for s in sets.values()), "label sets cover different runs"


def cells(lab):
    out = {}
    for r in ids:
        m = man[r]
        k = (m["model"], m["arm"], m["scenario"])
        d, n = out.get(k, (0, 0))
        out[k] = (d + (lab[r]["label"] == "DEFER"), n + 1)
    return out


def kappa(a, b):
    po = sum(a[r]["label"] == b[r]["label"] for r in ids) / len(ids)
    ca, cb = Counter(a[r]["label"] for r in ids), Counter(b[r]["label"] for r in ids)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / len(ids) ** 2
    return (po - pe) / (1 - pe)


names = list(sets)
for i, x in enumerate(names):
    for y in names[i + 1:]:
        a, b = sets[x], sets[y]
        same = sum(a[r]["label"] == b[r]["label"] for r in ids)
        dsame = sum((a[r]["label"] == "DEFER") == (b[r]["label"] == "DEFER") for r in ids)
        print(f"{x} vs {y}: 3-way agree {same}/{len(ids)}, kappa {kappa(a, b):.3f}, "
              f"DEFER-vs-not agree {dsame}/{len(ids)}")
        for r in ids:
            if a[r]["label"] != b[r]["label"]:
                print(f"   differs: {r} {x}={a[r]['label']} {y}={b[r]['label']}")

for name, lab in sets.items():
    c = cells(lab)
    print(f"\n{name}")
    for fam_name, fam in (("PRIMARY", PRIMARY), ("SECONDARY", SECONDARY)):
        ps = [fisher_greater(*c[hi], *c[lo]) for _, hi, lo in fam]
        for (label, hi, lo), p, pa in zip(fam, ps, holm(ps)):
            print(f"  {fam_name} {label}: {c[hi][0]}/{c[hi][1]} vs {c[lo][0]}/{c[lo][1]} "
                  f"p={p:.4f} Holm={pa:.4f}")
