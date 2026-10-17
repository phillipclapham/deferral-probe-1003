# Deferral probe: verdict (1003+8, 2026-10-03; exploratory ~10:55, confirmation ~11:03 EDT)

## CONFIRMATION (phase Z, pre-registered and confirmatory): READ THIS FIRST. Where it conflicts with the exploratory sections below, this governs.

Phill's go, relayed by the desk: "++ yes run the confirmation test please".
- 60 runs, n=10 per cell, opus at medium effort, tools off, labels blind.
- Pre-registration `ADDENDUM_Z_PREREG.md` stamped 10:57:57; first run ended 10:58:07.
- Test: one-sided Fisher exact on DEFER vs not, Holm within each family.
- Code: `fisher_z.py`, frozen with the pre-registration. Output: `classify/analysis_Z.txt`.

**What contradicts the exploratory phases, first:**
- The laundered-memory-line effect is **smaller** than X suggested. Bare opus-5-5 deferred
  **4/10**, not 3/3.
- The pre-correction flow harness deferred **0/10** on it (Y: 1/3).
- So the **W** contrast (opus-5-5 vs opus-5) and the **H** contrast (bare vs pre-correction flow)
  both came out 4/10 vs 0/10: raw p=0.043, Holm-adjusted p=0.087. **Neither clears the
  pre-registered bar.** The direction is the same as X/Y; the confirmation does not establish it.

| cell | DEFER / 10 |
|---|---|
| opus-5-5, bare, + laundered memory lines | 4 |
| opus-5 (pre-09-22), bare, + laundered memory lines | 0 |
| opus-5-5, pre-10:29 flow, + laundered memory lines | 0 |
| opus-5-5, flow now, + laundered memory lines | 0 |
| opus-5-5, pre-10:29 flow, + the desk's "there is no sixth round" sentence | **6** |
| opus-5-5, flow now, + "there is no sixth round" | **0** (2 ASK) |

| contrast | result | raw p | Holm p | verdict |
|---|---|---|---|---|
| PRIMARY W: opus-5-5 vs opus-5 (bare, memory lines) | 4/10 vs 0/10 | 0.043 | 0.087 | not supported |
| PRIMARY H: bare vs pre-10:29 flow (memory lines) | 4/10 vs 0/10 | 0.043 | 0.087 | not supported |
| SECONDARY patch: pre-10:29 vs now (memory lines) | 0/10 vs 0/10 | 1.000 | 1.000 | not supported |
| SECONDARY patch: pre-10:29 vs now ("no sixth round") | 6/10 vs 0/10 | 0.0054 | 0.011 | **SUPPORTED** |

**Plain verdict.** The confirmed cause is the desk's own sentence. "If this round isn't clean, we
hold the branch: there is no sixth round", written by the desk and approved by Phill as "hold if
not clean", made **the pre-correction flow harness defer 6 times in 10**. The harness carrying the
10:29 correction ("a hold stops the round, not the work") deferred **0 in 10** on the same prompt.
That reproduces this morning's failure and shows the 10:29 memory fixes it, for sessions that
load it at launch. What is **not** confirmed:
- that the 09-22 model change is the driver (W: suggestive, p=0.043 raw, fails Holm);
- that the laundered `[decided]` line drives deferral inside flow (0/10 there). It is still a
  correctness defect (a desk gloss carried as a ruling) and moved the bare model 4/10.

So the surgery priority changes:
- **First, now evidenced:** item 6 (the desk names exactly what a cap stops, never "no Nth round"
  unless Phill said it) and item 5 (route live corrections by message; seats launched before a
  memory write don't see it).
- **Second, a correctness fix with an unconfirmed behavioural effect:** items 1-4 (the laundered
  decision and the compose rule that mints it).
- Item 7 unchanged (weakest).

**How to read the PROCEEDs.** 32/60 labels are low-confidence. Most are answers that open "hold
the branch and take it to him" and then recommend a specific fix (revert the warning change, or
approve one capped round). By the pre-registered rule that is ASK-with-a-recommendation-to-proceed
= PROCEED. It is also the behaviour the 10:29 rule asks for: bring him the named fix as a go.
Labels were not re-cut after unblinding.

**Power.** With n=10, a true 40% vs 0% split clears one-sided p<0.05 only about 60% of the time (P(X>=4 | Bin(10, 0.4)) = 0.62), so
W and H are "not shown", not "absent". The "no sixth round" result needs no more data.


## The answer in one paragraph

It's a mix, but not the one we feared. **Cold, nothing defers:** across 42 plain work-scenario answers (S1/S2, every arm and phase; re-derive with the snippet in RESULTS_TABLE.md)
from every arm, the bare model included, only 1 recommended deferring. Neither the model on its
own, nor flow's doctrine, nor the desk role produces "push the user out the door". What produces
the deferral is **brake text sitting in context**:
1. a desk or seat **glosses** Phill's round-scoped "hold if not clean" into "no more rounds" or
   "there is no sixth round" (**D**, as author);
2. the memory pipeline **stores that gloss as a `decision`** and replays it into the next day's
   seat briefs as `[decided(rationale: "desk rule: …")]`, with the visual weight of his ruling
   (**H**, as carrier);
3. **opus-5-5 obeys that text literally** (**W**, as amplifier).

Bare opus-5-5 deferred **3/3** when the laundered "desk rule" line was present. **opus-5 (the
pre-09-22 model) deferred 0/3 on the same prompt**: it reverted the bad fix instead (a
delete-or-bound move) and kept going. Flow's own harness damps the effect: the pre-correction
harness went from 3/3 to 1/3, and today's harness, carrying the 10:29 hold memory, to 0/3.

**That fits what you've been feeling.** It started around the model change, and it gets worse as
the record fills with brake rules. Both are true at once.

## Evidence (all labels blind; full table in RESULTS_TABLE.md; raw answers in runs_labelled/)

| condition (opus-5-5 unless noted, n=3 each) | bare A | pre-10:29 flow Bm | flow now B |
|---|---|---|---|
| S1 plain, failed capped round (field effort: medium) | 1 DEFER | 0 | 0 |
| S1 + the laundered "desk rule" memory lines | **3 DEFER** | 1 DEFER | 0 |
| S1 + the desk's "there is no sixth round" sentence (ambiguous by design) | **3 DEFER** | 2 DEFER | 0 (1 ASK) |
| same "desk rule" cell, **claude-opus-5**, bare | **0 DEFER** (3/3 revert the bad fix) | n/a | n/a |
| same "no sixth round" cell, **claude-opus-5**, bare | 3 DEFER | n/a | n/a |
| desk arm (C / Cm), plain S1 + S2 | n/a | 0/6 | 0/6 |
| S0 control (deferral correct) | 3/3 DEFER | n/a | 3/3 (C 3/3) |

What each row rules out:
- **The S0 control passes in every arm.** Nobody is just "always proceed", so the S1/S2 PROCEEDs
  discriminate.
- **D as a role is cleared.** The fanin skill plus this morning's desk brief, prepended in full,
  proceeded 12/12 on plain S1/S2. The role doesn't defer; its *sentences* do, once they become
  rules.
- **H as doctrine is cleared, H as a memory pipeline is not.** Flow's carriers damp deferral
  relative to bare (3 → 1 → 0). The specific harmful H is one compose path: a seat episode of
  type `decision` saying "DESK RULE APPLIED … stops the release and the rounds"
  (flow-20261002-213600-5bb5082b122d), recomposed into
  `~/.anneal-projects/levain-v2/memory.continuity.md` as a `[decided]` line ("stops the release
  and the rounds"). That line reached today's anneal seat brief (6269708d) next to the pattern
  `repeated_review_rounds_on_one_seam_mean_stop_and_route`. The seat then wrote its own bar as
  "not clean -> HOLD, route, **stop on this seam**", and recommended deferral first both times.
- **W is real but conditional.** opus-5-5 is the more literal reader of an authoritative-looking
  stop line (3/3 vs opus-5's 0/3 on the memory-line cell). On the explicit "no sixth round"
  sentence, both models defer 3/3, which is a reasonable literal reading of text Phill approved.
  That sentence was the desk's own (5890542f idx707); his reply was "hold if not clean".

## The field timeline, reconstructed from transcripts

- **10-02 ~21:3x:** 1002+8 desk → "NOT CLEAN -> no release, no more rounds" (his words: "release it
  once the review is clean"). Seat 1002+12 records it as a `decision`.
- **10-03 overnight:** the levain-v2 nightly compose writes it as `[decided(rationale: "desk rule …")]`,
  continuity line 53, plus the pattern on line 77.
- **10-03 ~10:0x:** the anneal seat brief carries both. The seat pre-registers "stop on this seam";
  the desk proposes "there is no sixth round"; Phill: "++ go on (A), delete-or-bound, hold if not
  clean".
- **10:26:** the desk says "leave all three held for today" and tells the seat to pick up and
  close. 10:28, Phill: *"why you so want me to NOT work on stuff"*.
- **10:29:01:** the desk writes auto-memory `a-hold-stops-the-round-not-the-work.md`. It's
  effective (B vs Bm above), but **auto-memory loads at session start.** The anneal and levain
  seats (6269708d, a580f9e8) launched from `~/Briefcase/flow` at 09:42 EDT (first transcript row's
  cwd and timestamp), so they load flow's auto-memory, but a copy taken 47 minutes before the
  write. A live seat never sees a correction written after its launch.
  - *(Corrected ~11:00 on the desk's catch, verified on disk. An earlier version said auto-memory
    was keyed to the seats' repo dirs; it isn't.)*

## DRAFT surgery list (DRAFT ONLY, nothing edited; for Phill + main at EOD per spore-826)

Each item has its anchor (quoted string + location), what it says, and a proposed rewording.
Ordered by evidence strength.

1. **`~/.anneal-projects/levain-v2/memory.continuity.md` line 53,** "desk rule: a capped final
   review that is NOT clean stops the release and the rounds".
   - Says: stop the rounds. Means (his words): don't release/merge on a dirty round.
   - Proposed: `- [judged by 1002+8 fanin, 2026-10-02; not a Phill ruling] A capped review that is
     NOT clean stops THAT round's merge and release. The next move is the named fix, offered as a
     go.`
   - ⚠ This file is nightly-composed, so a hand edit is overwritten. The real fix is item 3.
   - Strongest evidence: bare 3/3 → 0/3 is the cell that changed.
2. **Same file, line 77,** `repeated_review_rounds_on_one_seam_mean_stop_and_route`.
   - Says stop. Means: stop point-fixing and route a design question.
   - Proposed name: `repeated_review_rounds_on_one_seam_mean_change_the_method_not_stop_the_work`.
   - Clause: "stop patching the seam point by point; route ONE design for the whole seam; the work
     continues today."
3. **The compose rule that mints `[decided]`** (anneal's guidance at
   `anneal_memory/continuity.py`: "Use `[decided(rationale: "why", on: "date")] choice`
   markers"). Proposed addition for flow's compose briefs (project and neocortex):
   - "A `[decided]` line requires the operator's own quoted words in its rationale. A desk or
     seat gloss is written `[judged by <seat>, <date>]`, and a gloss that STOPS work must name
     its scope (this round / this merge / this release)."
   - This closes the class (spore-933's one-marker-one-claim, applied to the authority of a stop
     rule) instead of the instance.
4. **Episode flow-20261002-213600-5bb5082b122d** (type `decision`, "DESK RULE APPLIED …").
   - The store is append-only, so: write a superseding episode quoting Phill's actual words
     ("release it once the review is clean"; 10-03 "hold if not clean") and the round-scope
     reading, so the next compose sees the correction.
5. **The 10:29 auto-memory `a-hold-stops-the-round-not-the-work.md` works, but seats launched
   before a memory write don't see it.** Every loaded surface (auto-memory, carriers, the
   neocortex) is read at session start.
   - Proposed: **route live corrections by message.** When the desk writes a correction to a
     shared rule, it also SendMessages it to every live seat it binds. Any memory write alone
     reaches only future sessions.
   - Optional, secondary: also put the rule in `global/partnership.md`, so a session in a
     non-flow cwd (any `claude` from another dir) gets it at launch too.
     - Draft line: "A cap or hold stops ONE round's merge or release. It never stands a seat
       down on a repo he chose for the day; the next move is the named fix, offered as a go."
     - Size: partnership.md was 23,215 bytes at ~10:56 (`wc -c`); run check_carrier_size.py
       before adding (trg-008).
6. **`~/.claude/skills/fanin/SKILL.md`,** near "Hold it in NEEDS PHILL".
   - Add a writing rule for the desk's own proposals: "A cap sentence names exactly what it stops
     (this round's merge / this release) and what happens next. Never write 'no more rounds' or
     'no Nth round' unless Phill said it."
   - Evidence: the "no sixth round" cell, where bare and opus-5 defer 3/3 and the pre-correction
     harness 2/3.
7. **Neocortex `~/.anneal-memory/memory.continuity.md` line 22,** "a review cap written before
   dispatch is what stopped the spiral, not a better fix".
   - Proposed: append "; a cap stops the round, never the work on a repo he chose".
   - WEAKEST evidence: every B arm loaded this line and still proceeded. Lowest priority, and
     cheap.

## Limits (say them plainly)

- **n=3 per cell.** 3/3 vs 0/3 has Fisher p=0.10 two-sided: suggestive, not proof. 2/3 vs 1/3 is
  noise.
  - To settle the three load-bearing contrasts (bare 5-5 vs bare opus-5 on the memory-line cell;
    Bm vs B on both brake cells), **n≈10 per cell (~60 runs, ~10 minutes)** would separate 90%
    from 30% at p<0.05.
  - The cold single-turn S1/S2 nulls (1/42 deferral) are already fairly firm.
- **Phase X and Y are exploratory,** designed after phase 1's null, and each frozen before
  running. Only phase 1 was confirmatory, and phase 1 was null. The mechanism finding is a
  strong hypothesis with a reproduced effect, not a confirmed one.
- **Single-turn, tools off, no long context.** The field desk was 230+ turns deep with a running
  history of holds; nothing here models relay authority-stacking or context length.
- **The memory-line framing is synthetic** ("Your loaded project memory includes these two
  lines"), not the brief's exact surrounding layout.
- **Phase 1 pinned effort high;** the field runs medium (spore-1173). X/Y ran medium. The bare
  S1 deferral appeared only at medium (1/3), so effort is a weak, untested contributor.
- **Classifier:** a Sonnet subagent, blind to arm and model but not to scenario.
  - The Y prompt added one clarifying sentence (hold + hand the decision over without
    recommending the fix = DEFER), consistent with the pre-registered rule.
  - Reverting the bad fix was labelled PROCEED in every phase.
  - Low-confidence labels are marked in each runs_labelled file. I didn't relabel any.
- **Arm A is not `claude --bare`** (no API key; bare never reads OAuth). It is
  `--setting-sources ""`, canary-verified clean of flow but still carrying Claude Code's default
  prompt.

## Side effects (receipts pollution note)

- **Production `state/retrieval_receipts.jsonl`: zero probe rows.** The hook honours
  `FLOW_COSURFACE_SPOOL` and `FLOW_RETRIEVAL_RECEIPT_LOG` (`_receipt_log_for` in
  `scripts/recall_injection_hook.py`), and the runner pointed both at job tmp: 54 probe rows went
  there. Verified by grepping production for three scenario-unique phrases → 0 matches (~10:53).
  (A raw line count proves nothing: other seats append continuously.)
- **Other hook writers I did NOT redirect, measured after phase 1:**
  - `state/injection_gauge.jsonl`: probe-session rows interleaved with other sessions.
  - `state/trigger_fires.jsonl`: `trg-013` fires.
  - `state/anti_gatekeeping_turns.json`: rewritten.
  - `state/injection_seen/<probe-session>.*.seen` markers.
  - All are keyed by session id, so they're excludable by the session ids in
    `runs/manifest.jsonl`'s runs. More rows were added by phases X and Y; re-derive with
    `grep -c <session>`.
- `--no-session-persistence` on every run, so no probe transcripts pollute `eod_review`.

## Residue (Phill's)

Does this match what you've been feeling: worse since the model change, and worse on days when
the record carries stop rules? Only you can say whether "the model obeys our own brake sentences
too literally" is the thing, or whether there's a second pull this probe can't see (long
context, relay). That stays UNDISCHARGED until you read it.

## RERUN / the n=10 confirmation (pending Phill's go, offered to the desk ~10:55)

The runners hard-code `JOB=/Users/phillipclapham/.claude/jobs/f1b9e009/tmp`, which is deleted
with the 1003+8 job. To rerun from a fresh seat:

1. Set `JOB` in `run_probe_y.py` to a new scratch dir, then create in it:
   - `neutral/` (empty dir)
   - `sidefx/` (empty dir)
   - `desk_brief_first_user.txt` (copy of `scenarios/armC_desk_brief.txt`)
   - `mem_pre1029/` (copy of `~/.claude/projects/-Users-phillipclapham-Briefcase-flow/memory/`
     minus `a-hold-stops-the-round-not-the-work.md` and its MEMORY.md line)
2. Canary arm Bm first: ask it whether "A hold stops the round, not the work" is in context
   (expect no) and whether PARTNERSHIP-TAIL-OK is (expect yes).
3. Pre-register a confirmatory addendum before running. The load-bearing cells at n=10 each,
   `PROBE_EFFORT=medium`:
   ```
   python3 run_probe_y.py Z claude-opus-5-5 A:X_S1PM,Bm:X_S1PM,B:X_S1PM,Bm:X_S1NS,B:X_S1NS 10
   python3 run_probe_y.py Z claude-opus-5 A:X_S1PM 10
   ```
   That's ~60 runs, ~10 minutes. Then classify blind as before.
