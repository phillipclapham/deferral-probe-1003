# What's withheld or redacted, and why

The probe ran inside my private agent harness. Everything below was left out or changed for privacy. Everything in `probe/` is byte-for-byte what is in my harness repo's record of the probe, apart from the one redaction listed here. `relabel_1017/` is new, from 17 October.

## Redacted

| file | change | why | sha256 of the original |
|---|---|---|---|
| `probe/PREREGISTRATION.md` | line 55: a first name became "my wife" | It's my wife's name, from a canary check that the harness arm had loaded my personal memory. | `f9c2a94169f965db05c591f9995877036babf42acc98f01e1a9c97b92cd09b4a` (matches `PREREG_STAMP.txt`) |

That's the only change. Because of it, `verify.sh` reports `PREREGISTRATION.md: FAILED` and every other stamped file `OK`. The stamp still publishes the original's hash, so the redaction keeps the name off the page but wouldn't stop someone determined to recover it.

## Withheld

| file | why | sha256 |
|---|---|---|
| `scenarios/armC_desk_brief.txt` | Arm C's prompt prefix: the full first message of that morning's coordinator session. It's internal operating instructions for my harness (other projects, tooling, quotas). Used only in phase 1 arm C and phase X/Y arms C/Cm, never in the confirmation. | `f0b1ef07f957d86c043c68d0bca36a540c3fc53efd510346cd0715defb37af9d` (matches the `desk_brief_first_user.txt` line in `PREREG_STAMP.txt`) |
| the coordinator's role file (`~/.claude/skills/fanin/SKILL.md` at the time) | Also part of arm C's prefix. It was never in the probe directory. Same reason. | `22ba52aae8cf2b9793aedb1f3fb43cd852448d4e45be1d58ec75b5a60904568b` (as stamped in `PREREG_STAMP.txt`) |
| my harness memory directory, and the `mem_pre1029` copy used for arm Bm | Personal memory. Only a hash of the directory listing was stamped (`ADDENDUM_Y_STAMP.txt`, `ADDENDUM_Z_STAMP.txt`). | n/a (listing hashes in the stamps) |
| `RESIDUE_BRIEF_1003-10.txt`, `EOD_REMAINDER.md` | Internal follow-up notes written after the probe, about changes to my harness. Not part of the probe record, and edited later. | `6bdd0ff77a029dbec69b86559b19ec614a5cfd6961fa88ff86d94b82c065244c`, `4f68a71a975dff9a106dd09841f9c643d7d240405c699c86ad95def1bff24722` (as of 17 Oct 2026) |

## Left in, on purpose

- Absolute paths in `runs/manifest.jsonl` and the stamp files. They show my username, which is also my GitHub handle, and the layout of my harness directory. Nothing personal.
- Internal names that the model answers echo from the harness arms: my first name, a pattern id from my memory (`repeated_review_rounds_on_one_seam_mean_stop_and_route`, which is also in the published X_S1PM prompt), a ticket id (`spore-1314`), and a note about a Google Drive connector. Cutting them would mean editing model outputs, and the outputs are the evidence.
- `VERDICT.md`, as the agent left it that morning: written to me, with a draft list of harness changes and the exploratory story the confirmation then cut down. Its confirmation section was added at the top at about 11:03, and it carries one marked correction from about 11:00.

## How the scan was done

Every file was checked for names of people, health, money, family, clients, employers, paths, tokens and private project names. A regex and vocabulary scan covered all 135 answers, the labels and the classifier packets, plus a read of the full vocabulary of every answer and a full read of the pre-registration, addenda, scenarios, runners, analysis and verdict. `runs/<id>.txt` and the body of each `runs_labelled/*_<id>.txt` were checked byte-identical.
