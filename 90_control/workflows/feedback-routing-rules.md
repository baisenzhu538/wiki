# Feedback Routing Rules

## Purpose

This file defines how feedback signals are routed to the correct system layer.
Follow these rules to ensure feedback improves the system rather than accumulating
as unread records.

## Routing Table

| feedback kind | primary trigger | update target | update action |
| --- | --- | --- | --- |
| `comments` | Content quality, tone, structure, clarity | Artifact body | Revise draft; update wiki Reusable Knowledge if factual claim changed |
| `corrections` | Factual error in artifact or wiki | Source trust level + wiki page | Downgrade source `trust_level`; add `[needs-review]` to wiki section; flag derived artifacts |
| `issues` | Tool failure, procedure error, ingest anomaly | Skill `## Failure Modes` + `## Procedure` | Add failure mode; update procedure step; create `kdo eval` case if capability-related |
| `usage-logs` | Behavior observed during real use | Capability `## Procedure` + `## Eval Cases` | Add eval case with real input/output; update procedure if mismatch found |
| `eval-results` | `kdo eval` scored < 80% | Capability spec | Update Mission/Inputs/Outputs/Procedure; add failing case to Eval Cases |

## Escalation Rules

1. **Three or more `corrections` for the same source** → mark source `trust_level: low`;
   review all derived wiki pages and artifacts.

2. **Three or more `issues` for the same procedure step** → that step is a design
   problem, not an execution problem; redesign the step or split it.

3. **Eval score consistently < 60%** → the capability artifact is not fit for agent
   execution; return to draft status and rebuild the spec from scratch.

4. **Any correction that changes a shipped artifact's core claim** → create a new
   feedback record of kind `corrections` linked to the artifact; consider a revised
   delivery to the same channel.

## What NOT to do with feedback

- Do not delete feedback records, even after the issue is resolved.
  Closed feedback is still signal for the next improvement cycle.
- Do not merge `corrections` silently into wiki pages without recording what changed.
- Do not use `--advisory` on `kdo validate` to hide failures;
  it is only for introspection, not for bypassing quality gates before shipping.

## Feedback → Wiki update criteria

Update a wiki page when:
- A `corrections` record identifies a factual error in the page
- A `comments` record identifies that the page's Reusable Knowledge is
  missing a key concept that would have prevented a content error
- A `usage-logs` record shows the page's Output Opportunities section
  is missing a proven use case

Do NOT update a wiki page when:
- The feedback is about tone or style in a derived artifact (update the artifact, not the wiki)
- The feedback is about a delivery channel format (update the artifact or channel config)

## Review cadence

| Feedback volume | Recommended review frequency |
| --- | --- |
| < 5 records | After next shipping event |
| 5–20 records | Weekly |
| > 20 records | Before next artifact is shipped |
