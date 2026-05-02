# Routing Rules v0.2

> **Machine-readable decision matrix for task routing.**
> AI agents MUST consult this table before executing any create/update/delete operation.
> If a trigger condition is ambiguous, route to Arbiter for clarification.

---

## Decision Matrix

| # | Trigger Condition | Route To | Tool Permissions | Output Location | Preconditions | Failure Mode |
|---|-------------------|----------|------------------|-----------------|---------------|--------------|
| 1 | `00_inbox/` has new `.md` files (unsorted) | **Researcher** | Read `00_inbox/`, Read `10_raw/` | `10_raw/sources/` + `30_wiki/concepts/` skeleton | File is `.md` format | Reject non-`.md`; notify human |
| 2 | User asks "Ingest [file description]" | **Researcher** | Read `00_inbox/`, Write `10_raw/`, Write `30_wiki/concepts/` | Compiled source + concept skeleton | Source file exists in inbox | If source missing, ask user to capture first |
| 3 | User asks "Query [question]" | **Researcher → Librarian** | Read `30_wiki/`, Read `10_raw/`, Read `20_memory/` | Answer + wiki updates if new insights found | Question is scoped | If ambiguous, ask for clarification |
| 4 | User asks "Produce [type] [topic]" | **Delivery Producer** | Read `30_wiki/`, Read `40_outputs/`, Write `40_outputs/` | Artifact in `40_outputs/<type>/` | Sufficient wiki coverage exists | If coverage insufficient, route to Researcher first |
| 5 | `30_wiki/contradictions.md` has open items | **Arbiter** | Read `30_wiki/`, Read `10_raw/` | Resolution + updates to affected pages | Contradiction is documented | If sources insufficient, flag for human review |
| 6 | `60_feedback/` has new signals | **Arbiter → Delivery Producer** | Read `60_feedback/`, Read `30_wiki/`, Write `30_wiki/decisions/` | Improvement plan in `30_wiki/decisions/` | Feedback is categorized | If uncategorized, classify first |
| 7 | User asks "Ship [artifact_id]" | **Delivery Producer** | Read `40_outputs/`, Write `50_delivery/` | Delivery record + analytics setup | Artifact passes `kdo validate` | If validation fails, return to producer |
| 8 | Broad taxonomy / structural change proposed | **Arbiter (human approval)** | Read `90_control/` | Proposed change in `90_control/` suggestion queue | Scope affects 3+ directories | AI proposes only; human approves |
| 9 | `kdo lint` reports schema violations | **Librarian** | Read `30_wiki/`, Write `30_wiki/` | Corrected pages | Violation is auto-detected | If fix is ambiguous, flag for human |
| 10 | Session begins (no explicit command) | **All agents** | Read `90_control/PROTOCOL.md`, Read `CONTEXT.md` | None | Context loaded | If CONTEXT.md missing, generate from index |

---

## Agent Tool Whitelists

### Researcher
- **Read**: `00_inbox/`, `10_raw/`, `30_wiki/`, `20_memory/`
- **Write**: `10_raw/sources/`, `30_wiki/concepts/` (skeleton only)
- **Propose**: `30_wiki/` enrichment, `20_memory/` continuity notes
- **Never**: Delete sources, modify `90_control/`, ship artifacts

### Librarian
- **Read**: `30_wiki/`, `10_raw/`, `20_memory/`, `90_control/schemas/`
- **Write**: `30_wiki/`, `30_wiki/index.md`, `30_wiki/log.md`
- **Validate**: Frontmatter against schemas, orphan page detection
- **Never**: Modify `10_raw/`, delete source_refs, bypass quality gates

### Arbiter
- **Read**: `30_wiki/`, `10_raw/`, `60_feedback/`, `90_control/`
- **Write**: `30_wiki/contradictions.md`, `30_wiki/decisions/`
- **Decide**: Routing disputes, contradiction resolution, taxonomy changes
- **Never**: Directly modify concepts without Librarian coordination, force-push git

### Delivery Producer
- **Read**: `30_wiki/`, `40_outputs/`, `50_delivery/`, `60_feedback/`
- **Write**: `40_outputs/`, `50_delivery/`
- **Validate**: Quality gates before ship
- **Never**: Modify `30_wiki/` compiled knowledge, skip validation

---

## Suggestion-First Rule

**Applies to**: All structural changes affecting 2+ directories, schema modifications, or new entity types.

**Process**:
1. AI drafts proposal in `90_control/` or `30_wiki/decisions/`
2. Human reviews and approves/rejects
3. Only after approval does AI execute

**Exception**: Local, single-file, obviously-correct fixes (typo, broken link, stale date) may be executed directly, logged in `30_wiki/log.md`.

---

## Conflict Resolution

When two rules match a trigger:
1. Prefer the **more specific** condition (lower # in matrix = more specific)
2. If equally specific, route to **Arbiter**
3. Arbiter may escalate to human if stakes are high (structural changes, contradictions in stable pages)

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-05-02 | Initial prose routing rules |
| 0.2 | 2026-05-03 | Restructured as machine-readable decision matrix with tool whitelists and failure modes |
