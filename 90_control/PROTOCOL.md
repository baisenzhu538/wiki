# KDO Protocol v0.1

> Machine-readable operating contract for AI agents interacting with this vault.
> Human intent: AI must read this file BEFORE any create/update/delete operation.

---

## 1. Vault Identity

| Key | Value |
|-----|-------|
| **Name** | KDO (Knowledge Development Organization) |
| **Purpose** | Compile raw inputs into reusable knowledge assets and shipped outputs |
| **Storage** | Markdown + YAML frontmatter + JSON state |
| **Runtime** | Zero external dependencies (std-lib only) |
| **Primary AI Roles** | Researcher, Librarian, Arbiter (defined in `AGENTS.md`) |

---

## 2. Directory Topology

```
00_inbox/          → ENTRANCE: low-friction capture (read-only for AI cleanup)
10_raw/            → SOURCE OF TRUTH: immutable raw materials (READ-ONLY)
20_memory/         → CROSS-SESSION CONTINUITY (read, append-only)
30_wiki/           → COMPILED KNOWLEDGE LAYER (primary AI workspace)
40_outputs/        → DELIVERABLES: content, code, capabilities
50_delivery/       → SHIP RECORDS
60_feedback/       → SIGNALS for improvement loop
70_product/        → PRODUCT EXECUTION
90_control/        → PROTOCOLS, schemas, agent rules (this file)
.kdo/              → MACHINE STATE (ignored by git)
```

### 2.1 Access Matrix

| Directory | Human | AI Read | AI Write | Notes |
|-----------|-------|---------|----------|-------|
| `00_inbox/` | RW | R | **Archive only** | AI moves processed items to `10_raw/` or `30_wiki/` |
| `10_raw/` | RW | R | **NO** | Immutable source of truth |
| `20_memory/` | RW | R | **Append** | AI may add corrections, preferences, continuity notes |
| `30_wiki/` | RW | R | **RW** | Primary AI workspace; writes must follow Section 4 |
| `40_outputs/` | RW | R | **RW** | Artifact production; must pass quality gates |
| `50_delivery/` | RW | R | **Append** | Record ship events |
| `60_feedback/` | RW | R | **Append** | Log feedback signals |
| `70_product/` | RW | R | **RW** | Task/project management |
| `90_control/` | RW | R | **Propose only** | AI suggests changes; human approves |
| `.kdo/` | - | R | **RW** | Machine state; git-ignored |

---

## 3. Entity Types & Locations

| Type | Path Pattern | Schema | Status Values |
|------|-------------|--------|---------------|
| **Concept** | `30_wiki/concepts/*.md` | `schemas/concept.yaml` | `draft`, `reviewed`, `stable`, `needs-review` |
| **Entity** | `30_wiki/entities/*.md` | `schemas/entity.yaml` | `draft`, `reviewed`, `stable`, `needs-review` |
| **Decision** | `30_wiki/decisions/*.md` | `schemas/decision.yaml` | `proposed`, `accepted`, `superseded` |
| **Comparison** | `30_wiki/concepts/*.md` | `schemas/comparison.yaml` | `draft`, `reviewed`, `stable` |
| **Improvement Plan** | `30_wiki/decisions/*.md` | `schemas/improvement.yaml` | `planned`, `in-progress`, `done` |
| **Source** | `10_raw/sources/*.md` | `schemas/source.yaml` | `ingested`, `enriched`, `linked` |
| **Artifact (Content)** | `40_outputs/content/*.md` | `schemas/artifact-content.yaml` | `draft`, `validated`, `shipped` |
| **Artifact (Code)** | `40_outputs/code/**` | `schemas/artifact-code.yaml` | `draft`, `validated`, `shipped` |
| **Capability** | `40_outputs/capabilities/**` | `schemas/capability.yaml` | `draft`, `evaluated`, `stable` |

---

## 4. Knowledge Card Protocol

All pages in `30_wiki/` MUST follow this contract.

### 4.1 Frontmatter (YAML)

```yaml
---
title: "Human-readable title"
type: concept | entity | comparison | decision | improvement-plan | system | trend
status: draft | reviewed | stable | needs-review
source_refs:
  - "source_id_1"
  - "source_id_2"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
related:
  - "[[Related Concept]]"
---
```

### 4.2 Body Structure

```markdown
# Title

Brief summary (1-2 sentences).

## Core Points

- Point 1
- Point 2

### [Critique]

- Assumption: ...
- Boundary: ...
- Reliability: High/Medium/Low — reason

### [Synthesis]

- Links to [[Existing Concept]]
- Conflicts with [[Another Concept]]
- Transferable to: scenario X, scenario Y
```

### 4.3 Link Rules

- **Create before link**: Before writing `[[New Concept]]`, check if the target page exists
- **Use wiki-links**: `[[concept-name]]` or `[[folder/concept-name]]`
- **Bidirectional**: When adding a link from A → B, consider if B should reference A
- **No orphan pages**: Every concept should be reachable from `30_wiki/index.md` or another concept

---

## 5. Pipeline Rules

### 5.1 KDO Full Pipeline

```
capture → ingest → enrich → produce → validate → ship → feedback → improve
```

### 5.2 State Transitions (AI must enforce)

| Stage | Input | Output | Validation |
|-------|-------|--------|------------|
| Capture | `00_inbox/` | Ingest-ready markdown | Format check |
| Ingest | Raw file | `10_raw/sources/` + `30_wiki/` skeleton | Source metadata complete |
| Enrich | Skeleton with TODOs | Completed knowledge card | All TODOs resolved |
| Produce | Wiki query results | `40_outputs/` artifact | Quality gate passed |
| Validate | Artifact | Validated artifact | Checklist in `schemas/quality-gates/` |
| Ship | Validated artifact | `50_delivery/` record | Channel + URL recorded |

---

## 6. Quality Gates (AI must enforce before write)

### 6.1 Content Artifacts
- [ ] Target audience defined
- [ ] Core thesis clear
- [ ] Structure complete
- [ ] Claims traceable to `source_refs`
- [ ] Feedback path declared

### 6.2 Code Artifacts
- [ ] Installation path documented
- [ ] Usage example exists
- [ ] Validation steps exist
- [ ] Failure modes named
- [ ] Version/release path declared

### 6.3 Capability Artifacts
- [ ] Task boundary defined
- [ ] Input/output spec clear
- [ ] Tool permissions declared
- [ ] Failure handling documented
- [ ] Evaluation cases exist or planned

---

## 7. Prohibition List (AI must NOT)

- ❌ **Never** modify files in `10_raw/` after ingestion
- ❌ **Never** delete `source_refs` from a knowledge card
- ❌ **Never** create wiki pages without frontmatter
- ❌ **Never** overwrite `90_control/` files without human approval
- ❌ **Never** commit `00_inbox/` items without processing
- ❌ **Never** leave TODO placeholders in `30_wiki/` pages (use `kdo enrich` or resolve manually)
- ❌ **Never** create orphan pages (no incoming links from index or other pages)

---

## 8. Context Snapshot (Updated by AI after each session)

```yaml
# This section is AI-maintained. Append only.
# Last updated: 2026-05-02

active_topics:
  - "Obsidian-Git multi-device sync conflict resolution"
  - "KDO Protocol design (this file)"
  - "AI-workflow integration (一堂课程 insights)"

recent_additions:
  - "90_control/PROTOCOL.md"

open_contradictions:
  - none

attention_required:
  - "Ensure all devices sync to commit 95e8fcd"
```

---

## 9. Changelog

| Date | Version | Change | Author |
|------|---------|--------|--------|
| 2026-05-02 | 0.1 | Initial protocol draft | AI (Claude) + Human |

---

## 10. Related Control Files

- `AGENTS.md` — Agent behavior rules
- `routing-rules.md` — Task routing logic
- `schemas/` — Data validation schemas
- `source-registry.yaml` — Source metadata registry
- `artifact-registry.yaml` — Output artifact registry
