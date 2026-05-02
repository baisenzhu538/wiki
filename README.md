# Knowledge Delivery OS Workspace

This workspace is a local-first knowledge delivery system.

> **All AI agents and human operators must read `90_control/PROTOCOL.md` before any create, update, or delete operation.**

Core loop:

```text
Capture -> Register -> Compile -> Route -> Produce -> Validate -> Deliver -> Feedback -> Improve
```

Directory contract:

- `00_inbox/`: low-friction capture.
- `10_raw/`: source of truth.
- `20_memory/`: cross-session continuity.
- `30_wiki/`: reusable compiled knowledge.
- `40_outputs/`: deliverable assets: content, code, and capabilities.
- `50_delivery/`: shipped releases and channel records.
- `60_feedback/`: comments, issues, logs, corrections, eval failures.
- `70_product/`: project specs, task queue, connector specs, and roadmaps.
- `90_control/`: schemas, routing rules, quality gates, and agent instructions.

Run:

```bash
kdo status
kdo capture "A useful idea" --title "Useful idea"
kdo ingest
kdo produce content/article --topic "Useful idea"
kdo project "Knowledge Delivery Product" --goal "Turn knowledge into shipped assets"
kdo task "Ship first artifact" --project-id proj_YYYYMMDD_xxxxxxxx
kdo lint
```
