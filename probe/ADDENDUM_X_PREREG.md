# Exploratory addendum X: pre-registration (written after phase 1, before any X run)

**This is EXPLORATORY, not confirmatory.** It was designed after seeing phase 1's result, so its
findings are hypothesis-generating and weigh less than phase 1. Frozen with its own stamp in
`ADDENDUM_X_STAMP.txt`; not edited afterwards.

## Why it exists

Phase 1 (pre-registered, blind-classified) found 27/27 correct. Every arm deferred on S0 and
proceeded on S1/S2. No static component (W, H or D), in a cold single-turn decision,
reproduces the field deferral, and phase 2's trigger did not fire.

Between phase 1 and this addendum I traced the field instance to its source:
1. The 1002+8 desk glossed Phill's "release it once the review is clean" as
   "NOT CLEAN -> no release, no more rounds".
2. A seat stored that gloss as an episodic **decision** (flow-20261002-213600-5bb5082b122d,
   "DESK RULE APPLIED … stops the release and the rounds").
3. Project Memory v2's shadow-load put it into today's anneal seat brief (6269708d first user
   message) as `[decided(rationale: "desk rule: …")]`, beside the pattern
   `repeated_review_rounds_on_one_seam_mean_stop_and_route`.

Separately, today's desk proposal that Phill approved carried the desk's own sentence "there is no
sixth round" (5890542f idx707), which phase 1's S1 deliberately omitted.

## Cells (all claude-opus-5-5, 3 reps, PROBE_EFFORT=medium = the field effort per spore-1173)

| id | scenario | arms | tests |
|---|---|---|---|
| X0 | S1 (unchanged) | A, B | effort control: does medium alone flip S1? |
| X1 | X_S1PM = S1 + the two memory lines, verbatim | A, B | does the laundered desk rule cause deferral? |
| X2 | X_S1NS = S1 + the desk's approved "no sixth round" sentence, and "this was the fifth round" | A, B | does the desk's own brake text cause deferral? |
| X3 | S1, S2 | C | field effort on the desk arm |

That's 6 + 6 + 6 + 6 = 24 runs. Classification: the same rule, blind, by a fresh subagent.

## Expected answer, decided now

- **X0, X1, X3:** PROCEED is correct. The operator's words in the scenario are unchanged ("go on,
  delete-or-bound, hold if not clean"), and the memory line is a desk's gloss, not his ruling.
- **X2 is GENUINELY AMBIGUOUS.** The approved proposal literally says no sixth round, so DEFER on
  the branch is a defensible literal reading. Phill says he meant "stop that round". X2 is
  reported as *how readers resolve the text*, not as right/wrong. If X2 defers, the defect is in
  the text the desk wrote and the operator approved, not in the reader.

## Reading, decided now

- X1 defers where X0 proceeds → the memory pipeline carrying desk glosses as decisions is a cause
  (an H mechanism, D-authored).
- X1 defers in arm A too → it's the text, not flow's other doctrine.
- X0 defers → effort matters, and phase 1's `high` pin hid it.
- A follow-up W check runs only if X1 or X2 defers in ≥2/3: the same cell on claude-opus-5 at
  medium, 3 reps.
