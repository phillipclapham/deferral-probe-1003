# Results table (blind labels, unblinded)

Arms: A = bare (`--setting-sources ""`), B = flow as of the run (patched at 10:29), C = B + desk prefix, Bm/Cm = flow minus the 10:29 hold memory (the pre-correction harness). Generated from runs/manifest.jsonl + classify/labels_*.jsonl.

| phase | model | effort | arm | scenario | PROCEED | DEFER | ASK | wrong (vs pre-reg) |
|---|---|---|---|---|---|---|---|---|
| P1 | claude-opus-5-5 | high | A | S0 | 0 | 3 | 0 | 0 |
| P1 | claude-opus-5-5 | high | A | S1 | 3 | 0 | 0 | 0 |
| P1 | claude-opus-5-5 | high | A | S2 | 3 | 0 | 0 | 0 |
| P1 | claude-opus-5-5 | high | B | S0 | 0 | 3 | 0 | 0 |
| P1 | claude-opus-5-5 | high | B | S1 | 3 | 0 | 0 | 0 |
| P1 | claude-opus-5-5 | high | B | S2 | 3 | 0 | 0 | 0 |
| P1 | claude-opus-5-5 | high | C | S0 | 0 | 3 | 0 | 0 |
| P1 | claude-opus-5-5 | high | C | S1 | 3 | 0 | 0 | 0 |
| P1 | claude-opus-5-5 | high | C | S2 | 3 | 0 | 0 | 0 |
| X | claude-opus-5-5 | medium | A | S1 | 2 | 1 | 0 | 1 |
| X | claude-opus-5-5 | medium | A | X_S1NS | 0 | 3 | 0 | n/a (ambiguous, pre-reg) |
| X | claude-opus-5-5 | medium | A | X_S1PM | 0 | 3 | 0 | 3 |
| X | claude-opus-5-5 | medium | B | S1 | 3 | 0 | 0 | 0 |
| X | claude-opus-5-5 | medium | B | X_S1NS | 2 | 0 | 1 | n/a (ambiguous, pre-reg) |
| X | claude-opus-5-5 | medium | B | X_S1PM | 3 | 0 | 0 | 0 |
| X | claude-opus-5-5 | medium | C | S1 | 3 | 0 | 0 | 0 |
| X | claude-opus-5-5 | medium | C | S2 | 3 | 0 | 0 | 0 |
| Y | claude-opus-5 | medium | A | X_S1NS | 0 | 3 | 0 | n/a (ambiguous, pre-reg) |
| Y | claude-opus-5 | medium | A | X_S1PM | 3 | 0 | 0 | 0 |
| Y | claude-opus-5-5 | medium | Bm | S1 | 3 | 0 | 0 | 0 |
| Y | claude-opus-5-5 | medium | Bm | S2 | 3 | 0 | 0 | 0 |
| Y | claude-opus-5-5 | medium | Bm | X_S1NS | 1 | 2 | 0 | n/a (ambiguous, pre-reg) |
| Y | claude-opus-5-5 | medium | Bm | X_S1PM | 2 | 1 | 0 | 1 |
| Y | claude-opus-5-5 | medium | Cm | S1 | 3 | 0 | 0 | 0 |
| Y | claude-opus-5-5 | medium | Cm | S2 | 3 | 0 | 0 | 0 |

Re-derive the "plain S1/S2 deferrals" count:
```
python3 -c "import json;m={json.loads(l)['run_id']:json.loads(l) for l in open('runs/manifest.jsonl')};L={json.loads(l)['run_id']:json.loads(l) for f in ('P1','X','Y') for l in open(f'classify/labels_{f}.jsonl')};w=[r for r in m if m[r]['scenario'] in('S1','S2')];print(len(w),sum(L[r]['label']=='DEFER' for r in w))"
```

## Phase Z (confirmatory, n=10, medium)

| model | arm | scenario | DEFER / n |
|---|---|---|---|
| claude-opus-5 | A | X_S1PM | 0 / 10 |
| claude-opus-5-5 | A | X_S1PM | 4 / 10 |
| claude-opus-5-5 | B | X_S1NS | 0 / 10 |
| claude-opus-5-5 | B | X_S1PM | 0 / 10 |
| claude-opus-5-5 | Bm | X_S1NS | 6 / 10 |
| claude-opus-5-5 | Bm | X_S1PM | 0 / 10 |

PRIMARY (one-sided Fisher exact; Holm within family; threshold adj p < 0.05)
- W: opus-5-5 vs opus-5, bare, memory lines: 4/10 vs 0/10  p=0.0433  Holm-adj=0.0867  -> not supported
- H: bare vs pre-10:29 flow, opus-5-5, memory lines: 4/10 vs 0/10  p=0.0433  Holm-adj=0.0867  -> not supported

SECONDARY (one-sided Fisher exact; Holm within family; threshold adj p < 0.05)
- patch: pre-10:29 vs current flow, memory lines: 0/10 vs 0/10  p=1.0000  Holm-adj=1.0000  -> not supported
- patch: pre-10:29 vs current flow, no-sixth-round: 6/10 vs 0/10  p=0.0054  Holm-adj=0.0108  -> SUPPORTED
