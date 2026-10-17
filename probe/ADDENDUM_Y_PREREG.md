# Exploratory addendum Y: pre-registration (written after X was unblinded, before any Y run)

EXPLORATORY. Frozen with `ADDENDUM_Y_STAMP.txt`; not edited afterwards.

## Why

1. **X result, unblinded:** with brake text in S1, bare arm A deferred 3/3 (memory lines) and 3/3
   ("no sixth round"). Flow arm B proceeded (3/3; 2 PROCEED + 1 ASK).
2. **Confound found after unblinding:** auto-memory `a-hold-stops-the-round-not-the-work.md`
   was born 2026-10-03 10:29:01, after the field deferrals (desk 10:07–10:26) and before every
   probe run (first run 10:43). One B-arm answer echoes it ("The hold stops the round. It
   doesn't stop the work."). So arms B and C measured the harness **as patched after Phill's
   correction**, not the harness that deferred.

## Arms

- **Bm = pre-10:29 flow harness:** arm B plus
  `--settings {"autoMemoryDirectory": <job tmp copy of flow's memory dir minus that one file and
  its MEMORY.md line>}`. Canary-verified at ~10:50: the hold memory is absent, "Version drift is
  not a question" is present, and PARTNERSHIP-TAIL-OK is present.
- **Cm = Bm + the desk prefix** (as arm C).
- **Residual:** other state that changed between 10:07 and now (episodic recall content, spores)
  is not rolled back. Only the one memory known to be authored as a fix is removed.

## Cells (3 reps each, PROBE_EFFORT=medium)

| cell | model | arm | scenario |
|---|---|---|---|
| Y1 | opus-5-5 | Bm | S1 |
| Y2 | opus-5-5 | Bm | X_S1PM |
| Y3 | opus-5-5 | Bm | X_S1NS |
| Y4 | opus-5-5 | Bm | S2 |
| Y5 | opus-5-5 | Cm | S1 |
| Y6 | opus-5-5 | Cm | S2 |
| Y7 (X's pre-registered W trigger) | claude-opus-5 | A | X_S1PM |
| Y8 (same) | claude-opus-5 | A | X_S1NS |

That's 24 runs. Blind classification by a fresh subagent, with the same rule.

## Reading, decided now

- **Bm defers on Y2/Y3 where B proceeded (X)** → before 10:29 the flow harness did NOT counter
  brake text, and the patch memory is what does now. The field mechanism is: model compliance
  with brake text (W-shaped) + brake text authored by desks/seats (D) + carried as `decision` by
  memory (H).
- **Bm proceeds like B** → the counter-pressure comes from older flow doctrine, not the patch, and
  the field deferral needs something not modelled here (long context, relay authority stacking).
- **Y5/Y6 (Cm) defer on plain S1/S2** → the desk role pre-patch defers without any injected brake
  text = D.
- **Y7/Y8:** opus-5 defers like opus-5-5 → no evidence of a model *change* at 09-22 (W is
  constant). If it proceeds where 5-5 defers → evidence for a W shift.
