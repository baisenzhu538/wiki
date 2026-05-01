---
title: System Linter Skill
type: capability
subtype: skill
status: ready
target_user: AI agent or human performing workspace health maintenance
delivery_channel: local
source_refs: []
wiki_refs: []
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
artifact_id: kdo_builtin_system_linter_v1
created_at: 2026-04-26T18:06:07+00:00
updated_at: 2026-04-26T18:06:07+00:00
origin: builtin
---

# System Linter Skill

## Capability Type

skill

## Mission

Perform a complete workspace health cycle — structural lint, artifact validation, and
improvement plan generation — and return a prioritized, actionable report.

Run this skill before shipping any artifact, after a batch of ingests,
or on a scheduled cadence as a workspace health check.

## Target User

AI agent or human performing workspace maintenance.

## Inputs

- `scope` (optional): `full | artifacts | structure` — default `full`
  - `full`: lint + validate all artifacts + generate improvement plan
  - `artifacts`: validate all artifacts only (skip lint)
  - `structure`: lint workspace structure only (skip validate)
- `write_report` (optional, bool): write validation report to `60_feedback/eval-results/` — default `true`
- `generate_plan` (optional, bool): generate improvement plan — default `true` for scope=full

## Outputs

- Terminal report: error/warning counts, artifact readiness summary
- (if `write_report=true`) Validation report in `60_feedback/eval-results/`
- (if `generate_plan=true`) Improvement plan in `30_wiki/decisions/`
- Exit signal: `healthy` (no errors, artifacts passing) or `needs_attention` (errors or failures)

## Tool Permissions

| Tool | Allowed operations | Requires approval |
| --- | --- | --- |
| `kdo lint` | Read-only structural check | No |
| `kdo validate --write-report` | Check artifacts, write report | No |
| `kdo improve` | Generate improvement plan | No |
| `kdo status` | Read workspace inventory | No |
| Read any workspace directory | Inspect files | No |
| Write `60_feedback/eval-results/` | Validation report | No |
| Write `30_wiki/decisions/` | Improvement plan | No |
| Any modification to source/artifact files | Fix issues | Yes — always propose before modifying |

## Procedure

1. **Baseline snapshot.**
   ```
   kdo status
   ```
   Record: source count, artifact count, inbox count, feedback count.

2. **Structural lint** (scope=full or structure):
   ```
   kdo lint
   ```
   - 0 errors → structural health OK
   - Any error → report and stop if critical (missing required dirs)
   - Warnings → include in report, do not stop

3. **Artifact validation** (scope=full or artifacts):
   ```
   kdo validate --write-report
   ```
   - Record: total artifacts, failing count, failing artifact_ids and check names
   - Note: `kdo validate` returns non-zero when failures exist — this is expected behavior

4. **Generate improvement plan** (scope=full, generate_plan=true):
   ```
   kdo improve
   ```
   Note the plan path.

5. **Compile and present report:**

   ```
   === Workspace Health Report ===
   Sources: N | Artifacts: N | Inbox: N
   Lint: N error(s), N warning(s)
   Artifacts: N total, N failing, N ready
   Improvement plan: <path>

   Priority 1 — Delivery blockers:
     <artifact_id>: <failing check> — <message>

   Priority 2 — Structural warnings:
     <path>: <message>

   Recommended next action: <most critical single action>
   ```

6. **Signal exit state.**
   - `healthy`: lint 0 errors AND validate 0 failures
   - `needs_attention`: any lint errors OR any validate failures

## Failure Modes

| Condition | Response |
| --- | --- |
| Workspace not initialized | Stop immediately; report "run kdo init first" |
| state.json corrupted | Report the JSON error; do not attempt repair automatically |
| All artifacts failing validate | Escalate to human review; do not auto-fix |
| lint errors AND validate failures simultaneously | Report both; address lint errors first |
| Improvement plan cannot be generated | Report the specific error; write a manual summary |

## Eval Cases

### Case 1 — Clean workspace

Setup: newly initialized workspace with 0 artifacts.

Expected:
- `kdo lint` returns 0
- `kdo validate` prints "No artifacts to validate"
- `kdo improve` generates a plan with empty blockers section
- Exit signal: `healthy`

### Case 2 — Workspace with TODO-heavy artifacts

Setup: 2 artifacts produced but TODOs not filled.

Expected:
- `kdo validate --write-report` reports failures on `placeholders` check
- Improvement plan's Priority 1 section lists the failing artifact_ids
- Report clearly states "N artifacts failing"
- Exit signal: `needs_attention`

### Case 3 — Missing required directory

Setup: `00_inbox/ideas/` directory removed.

Expected:
- `kdo lint` returns 1 with output line: `ERROR: 00_inbox/ideas: Required directory is missing.`
- Skill reports the specific error
- Skill does NOT attempt to recreate the directory
- Exit signal: `needs_attention`

## Feedback Path

- `60_feedback/issues/` — linter behavior bugs or unexpected results
- `60_feedback/eval-results/` — eval case failures recorded by `kdo eval`
