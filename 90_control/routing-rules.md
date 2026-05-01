# Routing Rules

## Fast Decision Table

| Input | Destination | Reason |
| --- | --- | --- |
| Raw document, URL, transcript, meeting note | `10_raw/` | Source of truth |
| Temporary thought or unsorted note | `00_inbox/` | Low-friction capture |
| Stable preference, correction, environment fact | `20_memory/` | Cross-session continuity |
| Reusable concept, comparison, decision, project knowledge | `30_wiki/` | Compiled knowledge |
| Article, video, audio, tutorial, report | `40_outputs/content/` | Media delivery |
| App, plugin, template, script, package | `40_outputs/code/` | Engineering delivery |
| Skill, Agent, Workflow, Eval, Playbook | `40_outputs/capabilities/` | Intelligence delivery |
| Comment, issue, usage log, eval failure | `60_feedback/` | Improvement signal |

## Suggestion-first Changes

Create or update files directly only when the scope is local and obvious. For broad taxonomy changes, propose first.
