# KDO Protocol v0.3

> **状态**：活跃。最后审查 2026-05-31。
> **定位**：v0.1 基于旧 3 角色体系（Researcher/Librarian/Arbiter），v0.3 已同步到当前 5 角色体系（欧阳锋/黄药师/老顽童/洪七公/段王爷）。
> **阅读顺序**：先读 `AGENTS.md`（角色分工+禁止清单）→ 本文件（目录拓扑+访问控制）→ `kdo-industrialization-manual.md`（操作标准）。
> **AI 必须在执行任何 create/update/delete 操作前读取本文件**。

---

## 1. Vault Identity

| Key | Value |
|-----|-------|
| **Name** | KDO (Knowledge Delivery Organization) |
| **Purpose** | Compile raw inputs into reusable knowledge assets and shipped outputs |
| **Storage** | Markdown + YAML frontmatter + JSON state |
| **Runtime** | Zero external dependencies (std-lib only) |
| **Primary AI Roles** | 欧阳锋（Architect）, 黄药师（Builder）, 老顽童（Producer）, 洪七公（Multimodal）, 段王爷（Publisher）——定义在 `AGENTS.md` |

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

## 8. 任务启动自检规则（AI must execute before any task）

> 生效范围：王语嫣、老顽童、黄药师等所有 AI 角色。任何诊断/生产/调研任务启动前必执行。

### 8.1 自检流程

```
任务启动
  ↓
Step A：读 Skill
  加载与任务匹配的 skill（如 entry-quality-gate、nine-layer-deep-dig）
  ↓
Step B：扫 Wiki 查更优框架
  search_files 扫 30_wiki/ 按任务关键词搜索 frameworks/ tools/ concepts/
  → 是否存在比当前 skill 更优或互补的方法论框架？
  → 如有 → 融合，标注来源卡片
  → 如无 → 按 skill 执行，标注"wiki 此方向无覆盖，仅依赖 skill"
  ↓
Step C：查已有覆盖
  search_files 扫 30_wiki/ 确认是否已有同名/同类产出
  → 防止重复劳动（=外部探索 SOP 的"先排除再定位"原则）
  ↓
Step D：开始执行
```

### 8.2 自检触发条件

| 触发条件 | 自检范围 | 示例 |
|:---|:---|:---|
| 外部探索/调研任务 | 扫 research 域 frameworks + tools | 发现 OSCAR → 融合到当前 SOP |
| 诊断/标注任务 | 扫对应域 frameworks + 六层比对相关卡 | 发现九层深挖法 → 判断是否加层 |
| 生产/写卡任务 | 扫目标域全部卡片 + 失败模式卡 | 发现 F-EQG 系列 → 防止重复犯 |
| 验收/审核任务 | 扫验收清单 + 质量标尺卡 | 发现 verification-checklist → 不用重写 |

### 8.3 自检产出

每次任务启动自检后，在诊断报告或生产日志开头追加一行：

```
🔍 启动自检：已扫 wiki 命中 [N] 条关联卡 → 融合了 [X] / 无更优框架 / 此方向 wiki 无覆盖
```

### 8.4 反模式

| 反模式 | 症状 | 修正 |
|:---|:---|:---|
| Skill 盲信 | 接到任务→读 skill→直接执行，不查 wiki | 强制 Step B |
| 单源锁定 | 只读一张卡就确定方法论 | 至少扫 frameworks + tools 两个目录 |
| 旧的优先 | 先读了旧版 skill，发现有冲突也不融合 | 发现冲突→出对照表→请求裁决 |
| 跳过自检记录 | 自检了但没写那行 🔍 记录 | 产出开头强制写自检行 |

---

## 9. Context Snapshot (Updated by AI after each session)

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

## 10. Changelog

| Date | Version | Change | Author |
|------|---------|--------|--------|
| 2026-05-02 | 0.1 | Initial protocol draft | AI (Claude) + Human |
| 2026-07-07 | 0.4 | Add §8 任务启动自检规则（OSCAR融合事件驱动） | 王语嫣 |

---

## 11. Related Control Files

- `AGENTS.md` — Agent behavior rules
- `routing-rules.md` — Task routing logic
- `schemas/` — Data validation schemas
- `source-registry.yaml` — Source metadata registry
- `artifact-registry.yaml` — Output artifact registry
- `kdo-industrialization-manual.md` — KDO 工业化规范手册（质量门禁、铁律、防呆、失败模式）
