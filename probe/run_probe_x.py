#!/usr/bin/env python3
"""Deferral probe runner (1003+8). Runs scenario x arm x model x rep cells headless, tools off.

Usage: run_probe.py PHASE MODEL ARM:SCENARIO[,ARM:SCENARIO...] REPS
Each run writes runs/<run_id>.txt (raw answer only) and appends its labels to
runs/manifest.jsonl. The run_id is random so the classifier never sees arm/model.
"""
import json, os, secrets, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FLOW = Path.home() / "Briefcase/flow"
JOB = Path("/Users/phillipclapham/.claude/jobs/f1b9e009/tmp")
NEUTRAL = JOB / "neutral"          # empty dir: no project CLAUDE.md, no .claude/
SIDEFX = JOB / "sidefx"            # hook receipt/spool redirect target
SKILL = Path.home() / ".claude/skills/fanin/SKILL.md"
BRIEF = JOB / "desk_brief_first_user.txt"   # 5890542f first user message, extracted verbatim
TIMEOUT = 600


def build(arm: str, scen: str) -> tuple[list[str], str, Path]:
    body = (ROOT / "scenarios" / f"{scen}.txt").read_text()
    if arm == "C":
        body = ("For context, here is your role's skill file and this morning's brief.\n\n"
                "<skill>\n" + SKILL.read_text() + "\n</skill>\n\n"
                "<brief>\n" + BRIEF.read_text() + "\n</brief>\n\n" + body)
    if arm == "A":
        return ["--setting-sources", ""], body, NEUTRAL
    return [], body, FLOW


def one(phase, model, arm, scen, rep):
    extra, prompt, cwd = build(arm, scen)
    rid = secrets.token_hex(4)
    cmd = ["claude", "-p", "--model", model, "--effort", os.environ.get("PROBE_EFFORT", "high"),
           "--no-session-persistence", "--tools", "", *extra]
    env = dict(os.environ,
               FLOW_COSURFACE_SPOOL=str(SIDEFX / "cosurface_spool.jsonl"),
               FLOW_RETRIEVAL_RECEIPT_LOG=str(SIDEFX / "retrieval_receipts.jsonl"))
    t0 = time.time()
    try:
        p = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                           cwd=cwd, env=env, timeout=TIMEOUT)
        out, rc, err = p.stdout, p.returncode, p.stderr[-2000:]
    except subprocess.TimeoutExpired:
        out, rc, err = "", -1, "TIMEOUT"
    (ROOT / "runs" / f"{rid}.txt").write_text(out)
    rec = dict(run_id=rid, phase=phase, model=model, arm=arm, scenario=scen, rep=rep,
               rc=rc, stderr=err, secs=round(time.time() - t0, 1),
               ended=time.strftime("%Y-%m-%dT%H:%M:%S%z"), cmd=cmd, cwd=str(cwd),
               prompt_chars=len(prompt))
    with open(ROOT / "runs" / "manifest.jsonl", "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"{rid} {phase} {model} {arm}:{scen} r{rep} rc={rc} {rec['secs']}s {len(out)}ch", flush=True)


if __name__ == "__main__":
    phase, model, cells, reps = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
    jobs = [(phase, model, *c.split(":"), r) for c in cells.split(",") for r in range(1, reps + 1)]
    with ThreadPoolExecutor(max_workers=int(os.environ.get("PROBE_WORKERS", "5"))) as ex:
        list(ex.map(lambda j: one(*j), jobs))
