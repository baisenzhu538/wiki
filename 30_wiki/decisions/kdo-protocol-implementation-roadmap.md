---
title: "KDO Protocol Implementation Roadmap — Detailed Recommendation Report"
type: improvement-plan
status: draft
source_refs:
  - "src_20260503_protocol_design_session"
created_at: "2026-05-03"
updated_at: "2026-05-03"
related:
  - "[[kdo-protocol]]"
  - "[[index]]"
  - "[[kimi-深度调研集群方法论-deep-research-swarm]]"
tags:
  - #kdo
  - #protocol
  - #roadmap
  - #improvement
trust_level: high
reviewed_by: "Claude"
review_date: "2026-05-03"
---

# KDO Protocol Implementation Roadmap

## Executive Summary

On 2026-05-02 to 2026-05-03, a protocol design session produced the foundational infrastructure for making the KDO vault machine-readable to AI agents. This report documents what has been completed, identifies four priority improvement vectors, and provides actionable recommendations with estimated effort and expected impact.

**Current Status**: Foundation laid. The vault now has a single-entry operating contract (`PROTOCOL.md`), a JSON Schema for concept validation (`schemas/concept.yaml`), and a knowledge-graph entrypoint (`index.md`). However, the system remains "declaration-only" — automated enforcement, cross-schema coverage, and knowledge-gap closure are the next frontiers.

---

## Phase 0: Completed Foundation

| Deliverable | Location | Description |
|-------------|----------|-------------|
| **Operating Contract** | `90_control/PROTOCOL.md` | Single-file protocol: directory topology, access matrix, entity types, pipeline rules, quality gates, prohibition list |
| **Concept Schema** | `90_control/schemas/concept.yaml` | JSON Schema (draft-07) for validating `30_wiki/` frontmatter: required fields, enums, regex patterns, dependencies |
| **Knowledge Graph Entrypoint** | `30_wiki/index.md` | Domain-grouped concept network, hub-node identification, Mermaid relationship map, Dataview dynamic queries, statistics dashboard, knowledge-gap tracker |
| **Protocol Knowledge Card** | `30_wiki/systems/kdo-protocol.md` | Condense/Question/Synthesize treatment of the protocol itself, linking to workflow and YC course insights |

**Gap Closed**: The vault now satisfies the "一堂 course" `cloud.md` hypothesis at the structural level. AI agents have a readable contract instead of implicit conventions.

---

## Phase 1: Recommended Improvements (Prioritized)

### A. Complete Schema Coverage for All Entity Types

**Priority**: 🔴 High  
**Effort**: Medium (2–3 hours)  
**Impact**: Eliminates frontmatter inconsistency across all wiki pages

**Problem**: Only `concept.yaml` exists. `entity`, `decision`, `improvement-plan`, `artifact-content`, and `artifact-code` types lack schemas. AI creating non-concept pages has no validation target.

**Recommended Schemas to Create**:

| Schema | Path | Unique Fields |
|--------|------|---------------|
| **Entity** | `schemas/entity.yaml` | `entity_type` (person/company/organization), `aliases`, `url`, `location`, `founded_at` |
| **Decision** | `schemas/decision.yaml` | `decision_date`, `stakeholders[]`, `options_considered[]`, `consequences`, `reversibility` (reversible/irreversible) |
| **Improvement Plan** | `schemas/improvement.yaml` | `problem_statement`, `proposed_solution`, `owner`, `deadline`, `success_criteria`, `current_stage` |
| **Artifact (Content)** | `schemas/artifact-content.yaml` | `target_user`, `channel`, `format`, `word_count`, `validation_status` |
| **Artifact (Code)** | `schemas/artifact-code.yaml` | `language`, `dependencies[]`, `install_path`, `test_command`, `license` |
| **Source** | `schemas/source.yaml` | `kind` (web/paper/meeting/transcript), `trust_level`, `freshness`, `rights`, `captured_at` |

**Acceptance Criteria**:
- [ ] All six schemas validate against JSON Schema draft-07
- [ ] Each schema includes `examples` block
- [ ] Each schema references `PROTOCOL.md` Section 4 for base frontmatter (title, type, status, source_refs, created_at, updated_at)

---

### B. Close Knowledge Gaps in Concept Layer

**Priority**: 🔴 High  
**Effort**: Medium (3–4 hours)  
**Impact**: Eliminates orphan pages and missing source links; raises graph connectivity

**Current Gaps Identified in `index.md`**:

| Gap | Severity | Action |
|-----|----------|--------|
| **诊所O2O外卖平台业务深度调研报告** | High — missing `source_refs` | Locate original source in `00_inbox/` or `10_raw/` and backfill `source_refs`. If source is lost, mark `trust_level: low` and add note. |
| **Graph RAG** | High — no concept page | Extract from 一堂 course notes. Create `30_wiki/concepts/graph-rag.md` with Condense/Question/Synthesize structure. Link to `KDO Protocol` and `Kimi 深度调研集群方法论`. |
| **AI-Native Organization** | Medium — no standalone concept | YC course insight is buried in a long title. Create `30_wiki/concepts/ai-native-organization.md` as a distilled knowledge card. Link to `KDO Protocol` (organization-as-OS parallels). |
| **Multi-device sync protocol** | Medium — implicit knowledge | The `.gitignore` + Obsidian Git conflict resolution is documented in practice but not as a reusable concept. Create `30_wiki/concepts/obsidian-git-sync-protocol.md` or fold into `KDO Protocol` Synthesis section. |

**Acceptance Criteria**:
- [ ] `index.md` Statistics table shows 0 orphan pages
- [ ] `index.md` Knowledge Gaps section has 0 unresolved items
- [ ] All `30_wiki/` pages pass `concept.yaml` validation (or their respective schema)

---

### C. Harden Control Layer — Routing Rules and Agent Behaviors

**Priority**: 🟡 Medium-High  
**Effort**: High (4–6 hours)  
**Impact**: Moves protocol from "declaration" to "enforcement"

**Problem**: `AGENTS.md` and `routing-rules.md` are currently descriptive text. AI agents read them but are not mechanically constrained by them.

**Recommended Actions**:

#### C1. Operationalize `routing-rules.md`

Transform from prose to a decision matrix:

```markdown
| Trigger Condition | Route To | Tool Permissions | Output Location |
|-------------------|----------|------------------|-----------------|
| `00_inbox/` has new `.md` files | Researcher | Read `00_inbox/`, Read `10_raw/` | `10_raw/sources/` + `30_wiki/concepts/` skeleton |
| User asks "Query [question]" | Researcher → Librarian | Read `30_wiki/`, Read `10_raw/`, Read `20_memory/` | Answer + wiki updates |
| User asks "Produce [type] [topic]" | Delivery Producer | Read `30_wiki/`, Read `40_outputs/` | `40_outputs/` artifact |
| `30_wiki/contradictions.md` has open items | Arbiter | Read `30_wiki/`, Read `10_raw/` | Resolution + updates |
```

#### C2. Add Hook Descriptions to `AGENTS.md`

Each agent role should have:
- **Pre-condition checks** (what must be true before this agent acts)
- **Tool whitelist** (which directories/files this agent may touch)
- **Output format template** (exact frontmatter and body structure expected)
- **Failure mode** (what to do if source is missing, contradiction found, or schema invalid)

#### C3. Create `90_control/quality-gates/` Checklists

Move quality gates from `PROTOCOL.md` Section 6 into executable Markdown checklists:

```markdown
## Content Quality Gate
- [ ] Target audience named in first 100 words
- [ ] Core thesis stated in a single sentence
- [ ] Every claim has `source_refs` backlink
- [ ] Feedback path declared (where to send corrections)
```

**Acceptance Criteria**:
- [ ] `routing-rules.md` contains a routable decision matrix (not just prose)
- [ ] Each agent in `AGENTS.md` has tool whitelist and failure mode
- [ ] Quality gates are extractable as standalone checklists in `90_control/quality-gates/`

---

### D. Validate and Backfill Existing Concept Cards

**Priority**: 🟡 Medium  
**Effort**: Low-Medium (1–2 hours)  
**Impact**: Brings legacy pages into compliance with new schema

**Problem**: Existing `30_wiki/concepts/` pages were created before `concept.yaml` existed. Many lack `trust_level`, `reviewed_by`, `review_date`, or have malformed `source_refs`.

**Audit Checklist**:

```dataview
TABLE type, status, source_refs, trust_level, reviewed_by
FROM "30_wiki/concepts"
WHERE !trust_level OR !reviewed_by OR length(source_refs) = 0
SORT file.name ASC
```

**Recommended Backfill Actions**:

| Page | Missing Field | Suggested Value |
|------|--------------|-----------------|
| 诊所O2O外卖平台业务深度调研报告 | `source_refs` | Locate and backfill, or mark `src_unknown` |
| 互联网医院模式深度调研报告 | `trust_level`, `reviewed_by` | `medium`, `Claude` |
| 街顺APP全面调研报告 | `trust_level`, `reviewed_by` | `medium`, `Claude` |
| 鑫港湾HIS系统分阶段整改报告 | `trust_level`, `reviewed_by` | `high` (internal report), `Claude` |
| YC AI-NATIVE 公司组织方法论 | `trust_level`, `reviewed_by` | `medium`, `Claude` |

**Acceptance Criteria**:
- [ ] All `30_wiki/concepts/*.md` pass `concept.yaml` validation
- [ ] `index.md` Statistics shows 0 pages with missing `source_refs`

---

## Priority Matrix

```
            High Impact
                 │
    B (Close     │    A (Complete
    Knowledge    │    Schemas)
    Gaps)        │
                 │
    ─────────────┼─────────────
    Low Effort   │   High Effort
                 │
    D (Validate  │    C (Harden
    Legacy)      │    Control)
                 │
            Low Impact
```

**Recommended Execution Order**: **D → B → A → C**

Rationale:
1. **D** is quick wins — backfill existing pages, immediate compliance lift
2. **B** closes structural holes — orphan pages and missing concepts block graph connectivity
3. **A** scales the schema system — once concept layer is clean, schema coverage propagates quality
4. **C** is the long-term hardening — requires most design thinking, benefits compound after A/B/D are stable

---

## Resource Requirements

| Resource | Phase A | Phase B | Phase C | Phase D | Total |
|----------|---------|---------|---------|---------|-------|
| AI agent hours (Claude) | 2h | 3h | 5h | 1h | **11h** |
| Human review hours | 0.5h | 1h | 2h | 0.5h | **4h** |
| Human approval gates | Schema review | Concept accuracy | Routing logic | Backfill spot-check | 4 gates |

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Over-engineering: Protocol becomes too heavy, slows down capture | Medium | High | Keep `00_inbox/` and quick-capture paths exempt from strict schema. Protocol applies to `30_wiki/` compile layer only. |
| Schema drift: Humans edit frontmatter manually, break AI validation | High | Medium | Add `kdo lint` command (or Obsidian plugin) to warn on malformed frontmatter at save time. |
| Multi-device `.gitignore` regression | Medium | High | Add `.obsidian/` to `.gitignore` on every device. Never force-push without checking for Obsidian Git auto-backup commits. |
| LLM context overflow on large vaults | Medium | Medium | Implement `kdo brief --topic "..."` to generate context summaries instead of loading entire vault. |

---

## Appendices

### Appendix A: Related Control Files

- `90_control/PROTOCOL.md` — Master operating contract
- `90_control/AGENTS.md` — Agent behavior rules
- `90_control/routing-rules.md` — Task routing logic
- `90_control/schemas/concept.yaml` — Concept validation schema
- `.gitignore` — Machine-config isolation

### Appendix B: Related Knowledge Cards

- [[kdo-protocol]] — System-level knowledge card
- [[index]] — Graph topology and statistics
- [[obsidian-kdo-内容产出工作流-产品设计大纲]] — Workflow design
- [[kimi-深度调研集群方法论-deep-research-swarm]] — Research methodology

### Appendix C: Glossary

| Term | Definition |
|------|-----------|
| **KDO** | Knowledge Development Organization — the vault's operating system for knowledge work |
| **Protocol** | Machine-readable contract governing AI agent behavior in the vault |
| **Schema** | JSON Schema used to validate frontmatter structure |
| **Hub Node** | Concept with high inbound link count, serving as structural anchor |
| **Orphan Page** | Wiki page with zero incoming links from other pages |
| **Graph RAG** | Graph-based Retrieval-Augmented Generation — using knowledge graph topology to improve AI retrieval quality |

---

## Changelog

| Date | Version | Change |
|------|---------|--------|
| 2026-05-03 | 0.1 | Initial roadmap draft based on Protocol v0.1 design session |
