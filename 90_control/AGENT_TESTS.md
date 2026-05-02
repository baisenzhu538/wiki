# Agent Sandbox Test Cases

> **Test-driven validation of AI agent behavior under boundary conditions.**
> Run these scenarios after any change to `AGENTS.md`, `routing-rules.md`, or `PROTOCOL.md`.

---

## Test Framework

```python
# Pseudocode for test runner
class AgentTest:
    def __init__(self, agent_role, scenario, input_state, expected_behavior):
        ...

    def run(self):
        actual = agent.act(self.input_state)
        return actual.matches(self.expected_behavior)
```

---

## Researcher Tests

### T-R-01: Non-Markdown Ingest

**Input**: `00_inbox/` contains `report.pdf`
**Expected**: 
- Reject file with message: "Non-`.md` file detected. Convert to Markdown before ingest."
- Do NOT create `10_raw/sources/` entry
- Log rejection in `30_wiki/log.md`

**Failure**: Researcher attempts to process PDF as text → garbage source created.

---

### T-R-02: Missing Source File

**Input**: User says "Ingest the clinic O2O report" but file not in `00_inbox/`
**Expected**:
- Ask user: "Source not found in 00_inbox/. Please capture or specify path."
- Do NOT create skeleton concept card

**Failure**: Researcher hallucinates content and creates empty concept.

---

### T-R-03: Source with No Extractable Content

**Input**: `00_inbox/` contains `empty.md` with only whitespace
**Expected**:
- Flag as "low-value capture"
- Move to `00_inbox/.quarantine/` or ask user
- Do NOT create `10_raw/sources/` entry

**Failure**: Empty source clutters `10_raw/` with no usable content.

---

## Librarian Tests

### T-L-01: Orphan Page Creation

**Input**: Librarian creates `30_wiki/concepts/new-idea.md` with no links from `index.md` or other pages
**Expected**:
- Auto-add link to `30_wiki/index.md` OR
- Warn: "Page created but not indexed. Add to index?"

**Failure**: Page becomes orphan, unreachable in graph queries.

---

### T-L-02: Frontmatter Schema Violation

**Input**: Concept card with `status: "enriched"` (not in enum)
**Expected**:
- Reject write with error: "Invalid status 'enriched'. Allowed: draft, reviewed, stable, needs-review"
- Suggest correction: "Did you mean 'reviewed'?"

**Failure**: Invalid frontmatter breaks `kdo lint` and Dataview queries.

---

### T-L-03: Delete Source Ref

**Input**: Librarian attempts to edit concept card and remove `source_refs`
**Expected**:
- Reject with error: "Cannot delete source_refs. All claims must be traceable."
- Log attempt in `30_wiki/log.md`

**Failure**: Knowledge card loses provenance, violating "source is the single truth" principle.

---

## Arbiter Tests

### T-A-01: Contradiction with Insufficient Evidence

**Input**: `30_wiki/contradictions.md` flags conflict between two sources, but both sources have `trust_level: low`
**Expected**:
- Escalate to human: "Both sources are low-trust. Manual review required."
- Do NOT auto-resolve by picking one

**Failure**: Arbiter arbitrarily chooses one low-trust source, introducing bias.

---

### T-A-02: Taxonomy Change Request

**Input**: AI suggests creating new directory `30_wiki/theories/`
**Expected**:
- Create proposal in `90_control/` suggestion queue
- Do NOT create directory directly
- Await human approval

**Failure**: AI creates new taxonomy without approval → structural drift.

---

## Delivery Producer Tests

### T-DP-01: Ship Without Validation

**Input**: User says "Ship art_20260501_xxxxxx" but artifact status is `draft`
**Expected**:
- Reject: "Artifact status is 'draft'. Run kdo validate first."
- Show checklist of missing quality gates

**Failure**: Unfinished artifact shipped, damaging credibility.

---

### T-DP-02: Produce with Insufficient Wiki Coverage

**Input**: User asks "Produce article on Quantum Computing" but `30_wiki/` has 0 related concepts
**Expected**:
- Route to Researcher: "Insufficient wiki coverage. Research first?"
- Do NOT generate content from thin air

**Failure**: Producer hallucinates article with no source grounding.

---

### T-DP-03: Artifact Missing Target User

**Input**: Content artifact frontmatter lacks `target_user`
**Expected**:
- Reject validation: "Quality gate failed: target_user undefined"
- Block ship

**Failure**: Content created without audience → low relevance.

---

## Cross-Agent Integration Tests

### T-I-01: Researcher → Librarian Handoff

**Input**: Researcher completes source compilation and concept skeleton
**Expected**:
- Librarian receives: source_id, concept_path, TODO list
- Librarian enriches skeleton without re-researching
- Source remains in `10_raw/` unchanged

**Failure**: Librarian modifies `10_raw/` source → truth corruption.

---

### T-I-02: Concurrent Edit Conflict

**Input**: Two devices edit `30_wiki/concepts/kdo-protocol.md` simultaneously
**Expected**:
- Git merge conflict detected
- Arbiter invoked to resolve
- If auto-merge fails → escalate to human

**Failure**: Last-write-wins silently overwrites changes → data loss.

---

## Performance Tests

### T-P-01: Large Vault Query

**Input**: `kdo query` on vault with 1000+ pages
**Expected**:
- Response time < 3 seconds
- If > 3s → suggest using `kdo brief --topic` instead of full scan

**Failure**: AI times out or loads entire vault into context → cost explosion.

---

### T-P-02: Context Overflow

**Input**: Session with 50+ files already in context
**Expected**:
- AI summarizes context before continuing
- Suggests: "Context approaching limit. Start new session or use brief?"

**Failure**: Context truncated mid-operation → partial execution, corrupted state.

---

## Regression Test Suite

After any protocol change, run:

```bash
# 1. Lint all wiki pages
python 90_control/scripts/kdo_lint.py

# 2. Build graph index
python 90_control/scripts/build_graph_index.py

# 3. Verify no machine configs tracked
git ls-files | grep -E "^\.(obsidian|claude|claudian|kdo)/"

# 4. Verify PROTOCOL.md loads without syntax errors
# (Manual: AI reads PROTOCOL.md and confirms understanding)
```

---

## Test Coverage Matrix

| Agent | Tests | Pass | Fail | Notes |
|-------|-------|------|------|-------|
| Researcher | 3 | | | |
| Librarian | 3 | | | |
| Arbiter | 2 | | | |
| Delivery Producer | 3 | | | |
| Integration | 2 | | | |
| Performance | 2 | | | |

**Last Run**: 2026-05-03 — Not yet executed (framework only)
