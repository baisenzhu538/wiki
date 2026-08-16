---
title: Data Curator Skill
type: capability
subtype: skill
status: ready
target_user: AI agent or human performing data curation on a KDO workspace
delivery_channel: local
source_refs: []
wiki_refs: []
definition_of_done:
  - task boundary explicit
  - inputs and outputs explicit
  - tool permissions declared
  - eval cases present
  - feedback path declared
  - all 5 phases have dry-run gating
  - batch limit of 5 cards enforced
artifact_id: kdo_builtin_data_curator_v1
created_at: 2026-05-31
updated_at: 2026-05-31
origin: builtin
---

# Data Curator Skill

## Capability Type

skill

## Mission

Systematically audit, clean, tag, chunk, and validate all concept cards in the KDO wiki,
producing a data-quality report, normalized frontmatter, a controlled taxonomy,
and an atomic chunk registry — with human gating at every phase.

This skill addresses two structural gaps in KDO:
1. **No atomic-level chunking**: knowledge is addressable only at the card level (500-2000 words),
   preventing precise citation, contradiction detection, and automated verification of individual claims.
2. **No multi-dimensional tagging**: `domain` has only 4 values with 27/384 cards populated,
   `tags` has only 13/384 cards with values, and no controlled vocabulary exists.

## Target User

AI agent or human performing data curation on a KDO workspace.
Invoked by the Architect (欧阳锋) or Builder (黄药师).

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `phase` | enum | no | `full` | `audit` \| `clean` \| `tag` \| `chunk` \| `validate` \| `full` |
| `scope` | string | no | `all` | `all` \| `domain:<name>` \| `card:<id>` \| `batch:<n>` |
| `dry_run` | bool | no | `true` | Preview changes without writing. Always default-true for safety. |
| `batch_size` | int | no | `5` | Max cards per batch (enforces KF-022). Reduce to 3 for pilot. |
| `backup` | bool | no | `true` | Create backup before writing. Backups go to `60_feedback/data-quality/backups/`. |

## Outputs

| Phase | Output | Location |
|-------|--------|----------|
| Audit | Data quality report (JSON) | `60_feedback/data-quality/audit-YYYY-MM-DD.json` |
| Clean | Normalized card frontmatter | `30_wiki/concepts/<card>.md` (written per-batch after approval) |
| Tag | Tag registry + tagged cards | `90_control/tag-registry.yaml` + `30_wiki/concepts/<card>.md` |
| Chunk | Chunk registry | `.kdo/state.json` (new `chunks` key) |
| Validate | Pass/fail matrix (JSON) | `60_feedback/data-quality/validate-YYYY-MM-DD.json` |
| All phases | Run metrics | `60_feedback/data-quality/run-NNN.json` |

## Tool Permissions

| Tool | Allowed operations | Requires approval |
|------|--------------------|-------------------|
| `Read` | Read card files, schemas, state.json | No |
| `Write` | Write cleaned card files, tag-registry.yaml | Yes (per batch) |
| `Edit` | Edit card frontmatter | Yes (per batch) |
| `Bash` / `PowerShell` | Run audit/clean/tag/chunk/validate Python scripts | No (read-only phases), Yes (write phases) |
| `Git` | Commit after each batch | No |

## Procedure

### Phase 0: Pre-flight

1. **Verify workspace state.**
   ```
   kdo status
   kdo lint --structure-report
   ```
2. **Confirm no concurrent kdo processes** (F-KDO-003).
3. **Create backup directory** at `60_feedback/data-quality/backups/`.

### Phase 1: Audit

1. **Run the audit scanner.**
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/audit_cards.py \
     --scope all --output 60_feedback/data-quality/audit-2026-05-31.json
   ```
2. **Review the report.** The report contains:
   - Per-card defect list (missing fields, inconsistent values, quote issues)
   - Full-library summary statistics (by field, by type, by status)
   - Recommended cleaning rules with confidence scores
3. **Human gate**: Review findings, adjust inference rules if needed. Approve to proceed to Phase 2.

### Phase 2: Clean

1. **Select pilot cards** (3 cards covering different patterns):
   - Pilot A: Gen A rich card (has domain/tags/difficulty) — e.g., `master-systems-thinking`
   - Pilot B: Gen B minimal card (JSON-style frontmatter) — e.g., `business-analysis`
   - Pilot C: OCR card (minimal frontmatter, OCR-derived) — e.g., `ocr-一堂-个人修炼-科学学习ipo模型`
2. **Dry-run each pilot.**
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/clean_cards.py \
     --card master-systems-thinking --dry-run
   ```
3. **Review diff. Human approves.**
4. **Write pilot card.**
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/clean_cards.py \
     --card master-systems-thinking --write --backup
   ```
5. **Verify.**
   ```
   kdo lint --diff
   kdo validate
   ```
6. **After all 3 pilots pass**: proceed to Batch 1 (5 cards).
7. **Repeat in batches of 5** until all 384 cards cleaned.
8. **Schema update**: Extend `90_control/schemas/concept.yaml`:
   - Add `enriched` to `status` enum
   - Add `tool`, `framework` to `type` enum

### Phase 3: Tag

1. **Create the controlled vocabulary.**
   ```
   # Write 90_control/tag-registry.yaml with the 4-dimension taxonomy
   ```
2. **Human reviews and approves the controlled vocabulary.**
3. **Dry-run pilot cards.**
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/tag_cards.py \
     --card master-systems-thinking --dry-run
   ```
4. **Review proposed tags. Human confirms or adjusts.**
5. **Write. Verify. Repeat in batches of 5.**
6. **Gate**: All cards have non-empty `tags` field with values from the registry.

### Phase 4: Chunk

1. **Dry-run pilot cards.**
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/chunk_cards.py \
     --card master-systems-thinking --dry-run
   ```
2. **Review chunk inventory.** Confirm chunk types and boundaries make sense.
3. **Write to state.json** (card body is NOT modified in Phase 4).
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/chunk_cards.py \
     --card master-systems-thinking --write --backup
   ```
4. **Verify state.json integrity.**
5. **Repeat in batches of 5.**
6. **Gate**: All cards have >= 1 chunk registered. Chunk IDs are unique and traceable.

### Phase 5: Validate

1. **Run full validation.**
   ```
   python 40_outputs/capabilities/skills/data-curator/scripts/validate_clean.py \
     --all --output 60_feedback/data-quality/validate-2026-05-31.json
   ```
2. **Review pass/fail matrix.** Each dimension has a per-card pass/fail.
3. **Target**: >= 95% pass rate per dimension.
4. **For failures**: Fix manually or re-run Phase 2/3 for those cards.
5. **Final gate**: `kdo lint` zero errors + `kdo validate` zero Failed for concept cards.

## Failure Modes

| Condition | Response |
|-----------|----------|
| Card has no frontmatter (`---` delimiters) | Skip card, log to report, flag as `missing_frontmatter` |
| Card has malformed YAML in frontmatter | Skip card, log parse error, flag for manual fix |
| Card body has no `##` headings (cannot chunk) | Mark as single-chunk card with type `raw` |
| `kdo lint` fails after batch write | Revert from backup, investigate, fix script, re-run |
| `state.json` locked by another process (F-KDO-003) | Wait and retry. Do NOT force-write. |
| Batch write produces content corruption (P-4 / C-10) | Revert from backup immediately. Review script logic. Re-test on single pilot before re-attempting batch. |
| Tag inference produces wrong tags for a card | Human overrides during review gate. Log override to run metrics. |
| Chunk boundary splits a claim mid-sentence | Adjust boundary detection logic. Re-chunk affected cards. |
| CJK content triggers regex silent failure (F-KDO-001) | Never use regex for CJK content extraction. Use structural parsing (heading-based). |

## Eval Cases

### Case 1 — Audit detects all defect types on a known-bad card

**Setup**: Create a test card with: curly quotes in status, `domain: yitang` (scalar not list),
`confidence: 0.8` (1 decimal), missing `tags`, missing `id`.

**Expected**:
- Audit report flags 5 defects: curly_quotes(1), domain_format(1), decimal_places(1), missing_field_tags(1), missing_field_id(1)
- No false positives on correctly formatted cards

### Case 2 — Clean normalizes a Gen B card without destroying content

**Setup**: Take `business-analysis.md` (JSON-style frontmatter, minimal fields).

**Expected**:
- `--dry-run` shows only frontmatter changes, zero body changes
- After `--write`: `status: enriched` (unquoted), `domain` added (inferred), frontmatter keys sorted
- `kdo lint` passes, `kdo validate` passes
- Card body unchanged (git diff shows only frontmatter hunk)

### Case 3 — Tag applies correct inference rules

**Setup**: Take `yt-panproduct-execution-roi-analysis.md` (yitang domain card).

**Expected**:
- `--dry-run` proposes `#method/product-design` + `#domain/entrepreneurship` + `#method/evaluation-method`
- No tags outside the controlled vocabulary
- Existing body content unchanged

### Case 4 — Chunk produces valid state.json entries

**Setup**: Take `master-decision-hygiene.md` (well-structured card with Claims + Critique + Synthesis).

**Expected**:
- `--dry-run` shows >= 5 chunks of at least 3 different types
- All chunk IDs follow `<slug>/<type>/<NNN>` pattern
- After `--write`: state.json has entries with valid `inherited.source_refs`

### Case 5 — Validate catches regressions

**Setup**: After Phase 2-4, manually break one card (remove `tags`, delete a chunk entry).

**Expected**:
- `validate_clean.py` reports FAIL for `tags_nonempty` and `chunks_exist` on the broken card
- Other cards still show PASS

### Case 6 — Dry-run writes nothing

**Setup**: Run any write-phase script with `--dry-run` on any card.

**Expected**:
- Script prints proposed changes to stdout
- File on disk is unchanged (verified by `git diff` showing no changes)
- state.json is unchanged

## Feedback Path

- `60_feedback/data-quality/` — Audit reports, validation matrices, run metrics
- `60_feedback/data-quality/backups/` — Pre-write backups of card files and state.json
- `60_feedback/corrections/` — Tag misclassifications, chunk boundary errors
- `60_feedback/issues/` — Blocking issues (malformed cards, parse failures)

## 触发词

**触发场景**：对 KDO wiki 概念卡进行系统化审计/清洗/标注/分块/校验时——批量检查卡片质量、frontmatter 合规、断链修复、重复卡合并、卡片分块重组。

**负面例子（不要触发）**：单张卡内容创作（那是单卡生产）；文章写作；不涉及卡片文件结构的操作。
