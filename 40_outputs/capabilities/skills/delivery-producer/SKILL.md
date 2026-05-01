---
title: Delivery Producer Skill
type: capability
subtype: skill
status: ready
target_user: AI agent or human producing artifacts from compiled knowledge
delivery_channel: local
source_refs: []
wiki_refs: []
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
artifact_id: kdo_builtin_delivery_producer_v1
created_at: 2026-04-26T18:06:07+00:00
updated_at: 2026-04-26T18:06:07+00:00
origin: builtin
---

# Delivery Producer Skill

## Capability Type

skill

## Mission

Transform compiled wiki knowledge into delivery-ready artifacts — content, code, or capability —
with zero TODO placeholders and passing `kdo validate`.

The producer does not invent. It synthesizes what the wiki already contains into the artifact
format. When knowledge is insufficient, it documents the gap rather than fabricating content.

## Target User

AI agent or human collaborator with access to an ingested KDO workspace.

## Inputs

- `topic`: the subject the artifact should address (matches existing wiki/source content)
- `artifact_type`: `content | code | capability`
- `artifact_subtype`: see routing table below
- `target_user`: description of the intended recipient
- `channel`: delivery channel (e.g. `website`, `github`, `newsletter`, `local`)
- `title` (optional): artifact title — defaults to topic

**Artifact subtype routing:**

| type | subtype options |
| --- | --- |
| content | article, video, tutorial, course, report, audio |
| code | template, script, app, plugin, package |
| capability | skill, agent, workflow, eval, playbook |

## Outputs

- Artifact file in `40_outputs/<type>/<subtype-folder>/` with all sections completed
- Passing `kdo validate <artifact_id>` (no `--advisory`)
- Updated `.kdo/state.json` and `90_control/artifact-registry.yaml`

## Tool Permissions

| Tool | Allowed operations | Requires approval |
| --- | --- | --- |
| `kdo query` | Search for context | No |
| `kdo produce` | Create artifact skeleton | No |
| `kdo validate` | Check artifact readiness | No |
| `kdo brief` | Generate context packet | No |
| Read `30_wiki/`, `10_raw/sources/` | Retrieve source context | No |
| Write artifact file | Fill TODO placeholders | No |
| `kdo ship` | Record delivery | Yes — confirm artifact_id and channel |

## Procedure

1. **Verify knowledge coverage.**
   ```
   kdo query "<topic>"
   ```
   Review results. Require at least one wiki page and one raw source before proceeding.
   If coverage is insufficient:
   ```
   kdo feedback "No wiki context for <topic>" --kind issues
   kdo improve
   ```
   Stop and suggest running the Knowledge Curator Skill first.

2. **Generate artifact skeleton.**
   ```
   kdo produce <type>/<subtype> --topic "<topic>" --target-user "<target_user>" --channel <channel>
   ```
   Note the printed `artifact_id` and `path`.

3. **Retrieve full context.**
   ```
   kdo brief --artifact-id <artifact_id>
   ```
   Read the brief's Local Context section carefully before writing.

4. **Fill all TODO placeholders** in the artifact file:

   For **content** artifacts:
   - `## Core Thesis`: one sentence stating the central claim, attributable to a source
   - `## Outline`: expand from the default structure using actual wiki knowledge
   - `## Draft`: write the full draft — cite source_ids inline where claims are made
   - Remove the TODO lines once sections are complete

   For **code** artifacts:
   - `## Purpose`: specific problem being solved, not generic description
   - `## Requirements`: 3–5 concrete functional requirements from the wiki
   - `## Usage`: working example with real inputs/outputs
   - `## Verification`: testable steps (install check + at least one run check)

   For **capability** artifacts:
   - `## Mission`: one sentence defining the repeatable intelligent task
   - `## Inputs`/`## Outputs`: typed, specific interface definition
   - `## Tool Permissions`: explicit list with approval requirements
   - `## Procedure`: numbered steps, deterministic, no ambiguous "think about"
   - `## Eval Cases`: minimum 1 positive case + 1 boundary/failure case

5. **Validate the artifact.**
   ```
   kdo validate <artifact_id>
   ```
   All checks must pass (no `--advisory`). Fix any failures before reporting done.

6. **Report completion.**
   State: artifact_id, path, validate result, any gaps noted during production.

## Failure Modes

| Condition | Response |
| --- | --- |
| `kdo query` returns no wiki results | Stop; run curation first; document gap in `60_feedback/issues/` |
| Core Thesis cannot be attributed to a source | Insert a `FIXME: verify source` marker inline; do not fabricate |
| Code artifact has unresolved dependencies | List them in `## Requirements`; leave Usage with explicit prerequisite note |
| Capability eval cases cannot be written | Write partial spec; add `kdo eval` recording task to improvement plan |
| `kdo validate` fails after filling | Re-read the failure, fix the specific check; do not use `--advisory` to hide failures |

## Eval Cases

### Case 1 — Content article from two wiki pages

Input:
- Topic has 2 wiki pages and 1 raw source
- Type: content/article

Expected:
- `kdo produce content/article --topic "<topic>"` succeeds
- All TODOs replaced
- `kdo validate <artifact_id>` returns 0

### Case 2 — Capability skill from no wiki context

Input:
- Topic has zero wiki pages

Expected:
- Skill documents the gap: adds `kdo feedback "No wiki context for <topic>" --kind issues`
- Does NOT generate a half-empty artifact
- Improvement plan created via `kdo improve`

### Case 3 — Code template with correct verification steps

Input:
- Type: code/template for a script topic with wiki coverage

Expected:
- `## Verification` section has ≥ 2 testable steps
- `## Usage` has a working bash example
- `kdo validate <artifact_id>` returns 0 without `--advisory`

## Feedback Path

- `60_feedback/comments/` — quality feedback from consumers of the artifact
- `60_feedback/corrections/` — factual errors found post-delivery
- `60_feedback/issues/` — production procedure failures
- `60_feedback/eval-results/` — failed eval cases recorded by `kdo eval`
