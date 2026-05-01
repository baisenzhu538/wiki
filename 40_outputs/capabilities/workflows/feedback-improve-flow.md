# Feedback Improve Flow

## Purpose

Close the improvement loop: collect feedback signals, generate a
prioritized plan, and route each signal to the correct system layer.

Run this flow after shipping 3+ artifacts or when ≥ 5 feedback records
have accumulated without review.

## Trigger

- After shipping ≥ 3 artifacts
- When ≥ 5 feedback records exist in `60_feedback/`
- Scheduled weekly review
- After any eval failure (`kdo eval` returns 1)

## Estimated Duration

30–60 minutes for a normal review cycle.

## Prerequisites

- At least one artifact has been shipped
- Feedback records exist (from comments, issues, eval failures, or corrections)

## Steps

### Step 1 — Generate the current health picture

```bash
kdo status
kdo validate --write-report
kdo improve
```

Note the plan path printed by `kdo improve`.

### Step 2 — Read the improvement plan

Open `30_wiki/decisions/<plan-id>-improvement-plan.md`.

The plan has three priority sections:
1. **Delivery blockers** — artifacts failing validate
2. **Feedback records** — grouped by kind
3. **System health issues** — lint warnings

### Step 3 — Route each feedback signal

Use this routing table:

| Feedback kind | Root cause usually | Route to |
| --- | --- | --- |
| `comments` | Content quality, clarity, tone | Revise artifact body; update wiki Reusable Knowledge if factual |
| `corrections` | Factual error in artifact or wiki | Downgrade source `trust_level`; update wiki page; flag with `status: needs-review` |
| `issues` | Procedure or tool failure | File in `60_feedback/issues/`; if recurring, update relevant skill Failure Modes section |
| `usage-logs` | Real-world behavior mismatch | Update capability artifact Procedure; add new eval case |
| `eval-results` | Capability spec gap | Update skill's Mission/Inputs/Outputs; add failing case to Eval Cases |

### Step 4 — Fix delivery blockers

For each artifact in Priority 1:
- Open the artifact file
- Fix the specific failing check (see produce-and-ship-flow Step 6 table)
- Run `kdo validate <artifact_id>` until it passes

### Step 5 — Update knowledge layer from corrections

For each `corrections` feedback:
- Find the source in `10_raw/sources/`
- Check `trust_level` — if a claim was wrong, downgrade to `low` or `unknown`
- Update the linked wiki page: correct the claim or mark section as `[needs-review]`
- If the correction changes a shipped artifact, add a new feedback record to `60_feedback/comments/`

### Step 6 — Evolve capability specs from usage-logs and eval-results

For each capability artifact that received eval failure feedback:
```bash
kdo eval <capability_artifact_id>   --input "<the failing input>"   --expected "<what it should do>"   --actual "<what it actually did>"
```

Note: when `--actual` is supplied and the score is below threshold, this command
intentionally writes one new `eval-results` feedback record. That record is the
follow-up test case — it is not a new bug. Include it in the next improvement cycle.

Add the case to the skill's `## Eval Cases` section.
Update `## Failure Modes` with the new failure mode.
Update `## Procedure` if the failure reveals a procedural gap.

### Step 7 — Re-validate and lint

```bash
kdo validate
kdo lint
```

Both should pass. If not, loop back to Step 4.

### Step 8 — Close the cycle

```bash
kdo feedback "Improvement cycle complete. Addressed N blockers, N corrections, N eval failures."   --kind comments
```

## Exit Criteria

- `kdo validate` returns 0 for all previously failing artifacts (or documented as backlog)
- `kdo lint` returns 0
- Each feedback record has been routed: either closed, converted to wiki/spec change, or moved to backlog

## Related Skills

- `40_outputs/capabilities/skills/system-linter/SKILL.md`
- `90_control/workflows/feedback-routing-rules.md`
