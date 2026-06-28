---

id: log
type: index
status: draft
title: log
domain:
- master
source_refs:
- src_unknown
author: system
reviewed_by: pending
confidence: 0.5
trust_level: low
created_at: '2026-06-16'
updated_at: '2026-06-17'
source_context: （原始 source 无法追溯，已标记为 src_unknown，待后续补充）
---
# Wiki Log

Chronological record of knowledge operations.

- src_unknown
  - src_unknown
- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown



## Session Report: 2026-05-02 ~ 2026-05-03 — KDO Protocol Structural Hardening

**Duration**: ~10 hours (multi-turn session)  
**Agent**: Claude Opus 4.7  
**Human**: Linhai Zhu  
**Objective**: Resolve multi-device sync conflicts and implement the `cloud.md`-style AI operating contract for the KDO vault.

### Key Decisions

1. **`.gitignore` hardened to blanket-ignore machine configs**: `.obsidian/`, `.claude/`, `.claudian/`, `.kdo/` — prevents future cross-device config conflicts.
2. **Force-push cleanup executed**: Removed 38 tracked machine-config files (224KB deletions) from git index; remote reset to clean state.
3. **`90_control/PROTOCOL.md` created**: Single-entry AI operating contract — directory topology, access matrix, entity types, pipeline rules, quality gates, prohibition list.
4. **All 7 JSON Schemas drafted**: `concept`, `entity`, `decision`, `improvement-plan`, `artifact-content`, `artifact-code`, `source` — frontmatter validation now machine-readable.
5. **`routing-rules.md` rewritten as decision matrix**: 10 trigger conditions × 4 agent roles with tool whitelists and failure modes.
6. **Graph RAG index generated**: `build_graph_index.py` produced `30_wiki/.graph/index.json` with 23 nodes and 28 edges.
7. **`kdo lint` and `kdo validate` scripts created**: Automated frontmatter schema checking and pre-ship quality gates (pure stdlib, zero dependencies).
8. **Knowledge layer upgraded**: `index.md` rebuilt as knowledge-graph entrypoint with Mermaid map, Dataview queries, hub-node identification, and gap tracking.

### Files Created (17)

| # | File | Type |
|---|------|------|
| 1 | `90_control/PROTOCOL.md` | AI operating contract |
| 2 | `90_control/schemas/concept.yaml` | JSON Schema |
| 3 | `90_control/schemas/entity.yaml` | JSON Schema |
| 4 | `90_control/schemas/decision.yaml` | JSON Schema |
| 5 | `90_control/schemas/improvement.yaml` | JSON Schema |
| 6 | `90_control/schemas/artifact-content.yaml` | JSON Schema |
| 7 | `90_control/schemas/artifact-code.yaml` | JSON Schema |
| 8 | `90_control/schemas/source.yaml` | JSON Schema |
| 9 | `90_control/CONTEXT.md` | Session context snapshot |
| 10 | `90_control/BRIDGE.md` | Cross-tool input protocol |
| 11 | `90_control/AGENT_TESTS.md` | Sandbox test cases (15 scenarios) |
| 12 | `90_control/scripts/build_graph_index.py` | Graph RAG builder |
| 13 | `90_control/scripts/kdo_lint.py` | Frontmatter linter |
| 14 | `90_control/scripts/kdo_validate.py` | Quality gate validator |
| 15 | `30_wiki/systems/kdo-protocol.md` | Knowledge card |
| 16 | `30_wiki/systems/obsidian-git-sync-protocol.md` | Multi-device sync SOP |
| 17 | `30_wiki/concepts/graph-rag.md` | Knowledge card |

### Files Modified (6)

| File | Change |
|------|--------|
| `.gitignore` | Simplified to blanket-ignore `.obsidian/`, `.claude/`, `.claudian/`, `.kdo/` |
| `30_wiki/index.md` | Rebuilt as knowledge graph entrypoint with domains, Mermaid map, Dataview queries |
| `90_control/routing-rules.md` | Restructured as machine-readable decision matrix |
| `30_wiki/concepts/互联网医院模式深度调研报告.md` | Backfilled `trust_level`, `reviewed_by`, `review_date`; status `enriched` → `reviewed` |
| `30_wiki/concepts/街顺app全面调研报告.md` | Backfilled metadata; status `enriched` → `reviewed` |
| `30_wiki/concepts/鑫港湾his系统分阶段整改报告.md` | Backfilled metadata |
| `30_wiki/concepts/yc-...markdown.md` | Backfilled metadata; status `enriched` → `reviewed` |

### Deliverables

- src_unknown
- src_unknown

### Metrics

| Metric | Before | After |
|--------|--------|-------|
| Schema coverage | 1 (`concept`) | 7 |
| Tracked machine-config files | 38 | 0 |
| Graph index nodes | 0 | 23 |
| Graph index edges | 0 | 28 |
| Routing rules (prose) | 1 table | 10-row decision matrix + whitelists |
| Orphan pages (claimed) | 1 (诊所O2O) | 0 (source_refs confirmed present) |

### Known Issues / Next Session

1. `kdo_lint.py` has false positives on old ISO-8601 timestamp formats in `created_at`/`updated_at` — needs batch backfill of legacy date formats.
2. `kdo_validate.py` framework ready but not yet battle-tested against real artifacts.
3. Agent sandbox tests (`AGENT_TESTS.md`) are specification-only — no automated runner yet.
4. Graph RAG is static JSON only — no query API or LLM integration layer.
5. Cross-tool bridge (`BRIDGE.md`) is protocol-only — zero implementations exist.

### References

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

- src_unknown

---

## Session Report: 2026-05-03 — Full Vault Traversal & Health Assessment

**Duration**: ~2 hours (multi-turn traversal + file analysis)  
**Agent**: Claude Opus 4.7  
**Human**: Linhai Zhu  
**Objective**: Traverse entire vault, assess structural integrity and data quality, produce constructive feedback as persistent knowledge.

### Key Decisions

1. **Assessment formalized**: Traversal results written to `60_feedback/assessments/claude-20260503-kdo仓库遍历与健康度评估.md` rather than left as chat-only ephemera.
2. **Improvement plan consolidated**: Created `plan_20260503_f3e9a2b1` in `30_wiki/decisions/`, superseding 8 redundant prior plans (`plan_20260501_*`).
3. **P0 priority reaffirmed**: Enrich stage (0/12 sources enriched) identified as the single biggest blocker. Artifact shell rate (8/10 failing validate) and empty 20_memory/ are secondary blockers.

### Files Created (2)

| # | File | Type |
|---|------|------|
| 1 | `60_feedback/assessments/claude-20260503-kdo仓库遍历与健康度评估.md` | Health assessment report |
| 2 | `30_wiki/decisions/plan_20260503_f3e9a2b1-improvement-plan.md` | Consolidated improvement plan |

### Files Modified (1)

| File | Change |
|------|--------|
| `30_wiki/log.md` | Appended session report and traversal record |

### Metrics (Post-Traversal)

| Metric | Count / Status |
|--------|----------------|
| Sources ingested | 12 |
| Sources enriched | 0 (unchanged — P0 blocker) |
| Artifacts total | 10 |
| Artifacts failing validate | 8 |
| Broken wikilinks | 14 |
| Improvement plans (active) | 1 (`plan_20260503_f3e9a2b1`) |
| Improvement plans (superseded) | 8 |
| Memory layer fill rate | ~0% |
| Contradictions recorded | 0 |

### Known Issues / Next Session

1. **P0**: Execute full enrich on 1 source (recommended: 互联网医院) to prove pipeline is repairable.
2. **P0**: Fix artifact status drift — 4 artifacts are shells but not marked as `stub`.
3. **P1**: Fix 14 broken wikilinks; promote broken-link lint from warning to error.
4. **P1**: Populate 20_memory/ with continuity notes and user preferences.
5. **P2**: Align pip-installed kdo CLI with source scripts; eliminate version drift.
6. **P3**: Ship 1 real artifact and collect ≥1 human feedback to replace simulated loop.

### References

- src_unknown
- src_unknown
- src_unknown
- src_unknown

- 00_inbox/调研专题/一堂-调研行动营启动_原文润色.txt

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - 00_inbox/调研专题/一堂-调研行动营启动_原文润色.txt
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/调研专题/一堂-调研武器库课程_原文润色.txt

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/ideas/DeepSeek V4在知识管理中的应用.md

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/调研专题/一堂-调研武器库课程_原文润色.txt

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/ideas/用这个免费API，让你的 Agent 拥有「看」的能力.md

- src_unknown

- 00_inbox/ideas/一堂-个人修炼-IPO模型实操课口述.md

- 00_inbox/ideas/一堂-个人修炼-科学学习逐字稿.md

- 00_inbox/ideas/一堂-创业必修-调研武器库.md

- 00_inbox/ideas/一堂-创业必修-调研行动营.md

- 00_inbox/ideas/一堂-创业必修-需求分析.md

- 00_inbox/ideas/一堂-案例拆解-串讲口述.md

- 10_raw/sources/一堂-课程地图精华串讲.md

- src_unknown

- src_unknown

- 00_inbox/ideas/一堂-个人修炼-IPO模型实操课口述.md

- 00_inbox/ideas/一堂-个人修炼-科学学习逐字稿.md

- 00_inbox/ideas/一堂-创业必修-调研武器库.md

- 00_inbox/ideas/一堂-创业必修-调研行动营.md

- 00_inbox/ideas/一堂-创业必修-需求分析.md

- 00_inbox/ideas/一堂-案例拆解-串讲口述.md

- 10_raw/sources/一堂-课程地图精华串讲.md

- 00_inbox/ideas/用这个免费API，让你的 Agent 拥有「看」的能力.md

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/ideas/test-sprint2-gate.md

- src_unknown

- src_unknown

- 10_raw/sources/src_20260620_deep-research-skill/SKILL.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/ach-methodology.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/analysis-frameworks.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/bias-checklist.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/ci-platforms.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/databases-index.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/market-sizing.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/report-guide.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/research-principles.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/style-guide.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/references/weapon-action-templates.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/templates/fact-card.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/templates/report-structure.md

- 10_raw/sources/src_20260620_business-research-skill-v2.1.0/templates/weapon-checklist.md

- 00_inbox/ideas/Truman的个人成长五步法.md

- 00_inbox/ideas/truman的选择：两条职业成长路线.md

- 00_inbox/ideas/一堂-个人修炼-Y模型.md

- 00_inbox/ideas/一堂-个人修炼-Y模型实操口述版.md

- 00_inbox/ideas/一堂-个人修炼-全景图MUSE模型.md

- 00_inbox/ideas/一堂-个人修炼-双三角模型.md

- 00_inbox/ideas/一堂-个人修炼-提问刻意练习画布.md

- 10_raw/sources/一堂-个人修炼-泛产品设计工具篇口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计探索营口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计概念口述版.md

- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO-全景策略.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO完整清单.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO模型.md

- 00_inbox/ideas/一堂-个人修炼-科学提问刻意练习.md

- 00_inbox/ideas/一堂-个人修炼-解放思想.md

- 00_inbox/ideas/一堂-个人修炼-课程清单.md

- 00_inbox/ideas/一堂-个人修身-Y模型探索营2口述版.md

- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计02口述.md

- 10_raw/sources/一堂-个人修身-泛产品设计实操口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计审美口述.md

- 10_raw/sources/一堂-创业-调研行动营口述01.md

- 00_inbox/ideas/一堂-创业必修-课程清单.md

- 00_inbox/ideas/一堂-地图-个人地图_conv.md

- 00_inbox/ideas/一堂-地图-创业地图_conv.md

- 00_inbox/ideas/一堂-地图-管理地图_conv.md

- 00_inbox/ideas/一堂-案例拆解-课程清单.md

- 00_inbox/ideas/一堂-泛产品设计-十年苦练30招.md

- 00_inbox/ideas/一堂-管理必修-课程清单.md

- 10_raw/sources/一堂-读书会-SPIN销售法口述.md

- 00_inbox/ideas/一堂个人地图：高潜力成长者修炼全景图.md

- 00_inbox/ideas/一堂五步法-产品内核画布.md

- 00_inbox/ideas/一堂五步法画布.md

- 00_inbox/ideas/一堂产品内核-十大典型指标.md

- 00_inbox/ideas/一堂刻意练习十年成长指数.md

- 00_inbox/ideas/一堂最佳转化率动力曲线图.md

- 00_inbox/ideas/一堂泛产品设计-十年修炼爬山地图.md

- 00_inbox/ideas/一堂泛产品设计-多出牌多练习.md

- 00_inbox/ideas/一堂泛产品设计36计-全套地图.md

- 00_inbox/ideas/一堂深度复盘冰山图.md

- 00_inbox/ideas/一堂转化率-10大容易浪费的触点.md

- 00_inbox/ideas/一堂进步大地图.md

- 00_inbox/ideas/一堂进步大地图_compressed.md

- 00_inbox/ideas/优秀泛产品设计者的自我修养.md

- 00_inbox/ideas/婚礼操盘-用户和场景.md

- 00_inbox/ideas/婚礼规划.md

- 00_inbox/ideas/审美提升的层级.md

- 00_inbox/ideas/微信图片_20260507004746_32_32.md

- 00_inbox/ideas/微信图片_20260507004751_33_32.md

- 00_inbox/ideas/微信图片_20260507004755_34_32.md

- 00_inbox/ideas/微信图片_20260507004758_35_32.md

- 00_inbox/ideas/微信图片_20260507004801_37_32.md

- 00_inbox/ideas/微信图片_20260507004802_38_32.md

- 00_inbox/ideas/微信图片_20260507004804_39_32.md

- 00_inbox/ideas/微信图片_20260507004806_40_32.md

- 00_inbox/ideas/微信图片_20260507004811_41_32.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践建模.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践收集.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践池子.md

- 00_inbox/ideas/泛产品设计-审美卡片-美好作品想象.md

- 00_inbox/ideas/泛产品设计-审美工具箱指南.md

- 00_inbox/ideas/泛产品设计-用户卡片-一堂五步法.md

- 00_inbox/ideas/泛产品设计-用户卡片-动力阻力.md

- 00_inbox/ideas/泛产品设计-用户卡片-场景推演.md

- 00_inbox/ideas/泛产品设计-用户卡片-多视角思考.md

- 00_inbox/ideas/泛产品设计-用户卡片-峰终定律.md

- 00_inbox/ideas/泛产品设计-用户卡片-惊喜公式.md

- 00_inbox/ideas/泛产品设计-用户卡片-用户分层.md

- 00_inbox/ideas/泛产品设计-用户卡片-用户视角.md

- 00_inbox/ideas/泛产品设计-用户卡片-行业分析画布.md

- 00_inbox/ideas/泛产品设计-用户卡片-需求挖掘.md

- 00_inbox/ideas/泛产品设计-用户卡片-项目背景分析.md

- 00_inbox/ideas/泛产品设计-落地卡片-ROI分析.md

- 00_inbox/ideas/泛产品设计-落地卡片-业务建模.md

- 00_inbox/ideas/泛产品设计-落地卡片-低成本测试MVP.md

- 00_inbox/ideas/泛产品设计-落地卡片-假设拆解.md

- 00_inbox/ideas/泛产品设计-落地卡片-内核和边界.md

- 00_inbox/ideas/泛产品设计-落地卡片-努力仿真.md

- 00_inbox/ideas/泛产品设计-落地卡片-十倍速验证.md

- 00_inbox/ideas/泛产品设计-落地卡片-善用佳软.md

- 00_inbox/ideas/泛产品设计-落地卡片-复盘迭代.md

- 00_inbox/ideas/泛产品设计-落地卡片-攻坚会.md

- 00_inbox/ideas/泛产品设计-落地卡片-灵感闪现.md

- 00_inbox/ideas/泛产品设计-落地卡片-管理三段论.md

- 00_inbox/ideas/泛产品设计-落地卡片-解放思想.md

- 00_inbox/ideas/泛产品设计-落地卡片-设计原则.md

- 00_inbox/ideas/泛产品设计-落地卡片-逻辑MECE.md

- 00_inbox/ideas/泛产品设计-落地卡片-酝酿式打磨.md

- 00_inbox/ideas/泛产品设计-落地卡片-里程碑拆解.md

- 00_inbox/ideas/泛产品设计-落地卡片-风险管理.md

- 00_inbox/ideas/泛产品设计-需求工具箱指南.md

- 00_inbox/ideas/泛产品设计的应用场景示意图.md

- 00_inbox/ideas/泛产品设计者的三大自我修养.md

- 00_inbox/ideas/泛产品设计者的自我修养.md

- 00_inbox/ideas/泛产品设计落地工具篇指南.md

- 00_inbox/ideas/泛产品设计落地篇.md

- 00_inbox/ideas/萃取总结.md

- 00_inbox/ideas/顶级产品追求的方向-乔布斯.md

- 00_inbox/ideas/项目背景问题思考的8个维度.md

- 00_inbox/ideas/预判模型.md

- 00_inbox/ideas/一堂-个人修炼-Y模型实操口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计工具篇口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计探索营口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计概念口述版.md

- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md

- 00_inbox/ideas/一堂-个人修身-Y模型探索营2口述版.md

- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计02口述.md

- 10_raw/sources/一堂-个人修身-泛产品设计实操口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计审美口述.md

- 10_raw/sources/一堂-创业-调研行动营口述01.md

- 10_raw/sources/一堂-读书会-SPIN销售法口述.md

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/ideas/Truman的个人成长五步法.md

- 00_inbox/ideas/truman的选择：两条职业成长路线.md

- 00_inbox/ideas/一堂-个人修炼-Y模型.md

- 00_inbox/ideas/一堂-个人修炼-Y模型实操口述版.md

- 00_inbox/ideas/一堂-个人修炼-全景图MUSE模型.md

- 00_inbox/ideas/一堂-个人修炼-双三角模型.md

- 00_inbox/ideas/一堂-个人修炼-提问刻意练习画布.md

- 10_raw/sources/一堂-个人修炼-泛产品设计工具篇口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计探索营口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计概念口述版.md

- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO-全景策略.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO完整清单.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO模型.md

- 00_inbox/ideas/一堂-个人修炼-科学提问刻意练习.md

- 00_inbox/ideas/一堂-个人修炼-解放思想.md

- 00_inbox/ideas/一堂-个人修炼-课程清单.md

- 00_inbox/ideas/一堂-个人修身-Y模型探索营2口述版.md

- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计02口述.md

- 10_raw/sources/一堂-个人修身-泛产品设计实操口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计审美口述.md

- 10_raw/sources/一堂-创业-调研行动营口述01.md

- 00_inbox/ideas/一堂-创业必修-课程清单.md

- 00_inbox/ideas/一堂-地图-个人地图_conv.md

- 00_inbox/ideas/一堂-地图-创业地图_conv.md

- 00_inbox/ideas/一堂-地图-管理地图_conv.md

- 00_inbox/ideas/一堂-案例拆解-课程清单.md

- 00_inbox/ideas/一堂-泛产品设计-十年苦练30招.md

- 00_inbox/ideas/一堂-管理必修-课程清单.md

- 10_raw/sources/一堂-读书会-SPIN销售法口述.md

- 00_inbox/ideas/一堂个人地图：高潜力成长者修炼全景图.md

- 00_inbox/ideas/一堂五步法-产品内核画布.md

- 00_inbox/ideas/一堂五步法画布.md

- 00_inbox/ideas/一堂产品内核-十大典型指标.md

- 00_inbox/ideas/一堂刻意练习十年成长指数.md

- 00_inbox/ideas/一堂最佳转化率动力曲线图.md

- 00_inbox/ideas/一堂深度复盘冰山图.md

- 00_inbox/ideas/一堂转化率-10大容易浪费的触点.md

- 00_inbox/ideas/一堂进步大地图.md

- 00_inbox/ideas/一堂进步大地图_compressed.md

- 00_inbox/ideas/优秀泛产品设计者的自我修养.md

- 00_inbox/ideas/婚礼操盘-用户和场景.md

- 00_inbox/ideas/婚礼规划.md

- 00_inbox/ideas/审美提升的层级.md

- 00_inbox/ideas/微信图片_20260507004746_32_32.md

- 00_inbox/ideas/微信图片_20260507004751_33_32.md

- 00_inbox/ideas/微信图片_20260507004755_34_32.md

- 00_inbox/ideas/微信图片_20260507004758_35_32.md

- 00_inbox/ideas/微信图片_20260507004801_37_32.md

- 00_inbox/ideas/微信图片_20260507004802_38_32.md

- 00_inbox/ideas/微信图片_20260507004804_39_32.md

- 00_inbox/ideas/微信图片_20260507004806_40_32.md

- 00_inbox/ideas/微信图片_20260507004811_41_32.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践建模.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践收集.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践池子.md

- 00_inbox/ideas/泛产品设计-审美卡片-美好作品想象.md

- 00_inbox/ideas/泛产品设计-审美工具箱指南.md

- 00_inbox/ideas/泛产品设计-用户卡片-一堂五步法.md

- 00_inbox/ideas/泛产品设计-用户卡片-动力阻力.md

- 00_inbox/ideas/泛产品设计-用户卡片-场景推演.md

- 00_inbox/ideas/泛产品设计-用户卡片-多视角思考.md

- 00_inbox/ideas/泛产品设计-用户卡片-峰终定律.md

- 00_inbox/ideas/泛产品设计-用户卡片-惊喜公式.md

- 00_inbox/ideas/泛产品设计-用户卡片-用户分层.md

- 00_inbox/ideas/泛产品设计-用户卡片-用户视角.md

- 00_inbox/ideas/泛产品设计-用户卡片-行业分析画布.md

- 00_inbox/ideas/泛产品设计-用户卡片-需求挖掘.md

- 00_inbox/ideas/泛产品设计-用户卡片-项目背景分析.md

- 00_inbox/ideas/泛产品设计-落地卡片-ROI分析.md

- 00_inbox/ideas/泛产品设计-落地卡片-业务建模.md

- 00_inbox/ideas/泛产品设计-落地卡片-低成本测试MVP.md

- 00_inbox/ideas/泛产品设计-落地卡片-假设拆解.md

- 00_inbox/ideas/泛产品设计-落地卡片-内核和边界.md

- 00_inbox/ideas/泛产品设计-落地卡片-努力仿真.md

- 00_inbox/ideas/泛产品设计-落地卡片-十倍速验证.md

- 00_inbox/ideas/泛产品设计-落地卡片-善用佳软.md

- 00_inbox/ideas/泛产品设计-落地卡片-复盘迭代.md

- 00_inbox/ideas/泛产品设计-落地卡片-攻坚会.md

- 00_inbox/ideas/泛产品设计-落地卡片-灵感闪现.md

- 00_inbox/ideas/泛产品设计-落地卡片-管理三段论.md

- 00_inbox/ideas/泛产品设计-落地卡片-解放思想.md

- 00_inbox/ideas/泛产品设计-落地卡片-设计原则.md

- 00_inbox/ideas/泛产品设计-落地卡片-逻辑MECE.md

- 00_inbox/ideas/泛产品设计-落地卡片-酝酿式打磨.md

- 00_inbox/ideas/泛产品设计-落地卡片-里程碑拆解.md

- 00_inbox/ideas/泛产品设计-落地卡片-风险管理.md

- 00_inbox/ideas/泛产品设计-需求工具箱指南.md

- 00_inbox/ideas/泛产品设计的应用场景示意图.md

- 00_inbox/ideas/泛产品设计者的三大自我修养.md

- 00_inbox/ideas/泛产品设计者的自我修养.md

- 00_inbox/ideas/泛产品设计落地工具篇指南.md

- 00_inbox/ideas/泛产品设计落地篇.md

- 00_inbox/ideas/萃取总结.md

- 00_inbox/ideas/顶级产品追求的方向-乔布斯.md

- 00_inbox/ideas/项目背景问题思考的8个维度.md

- 00_inbox/ideas/预判模型.md

- 00_inbox/ideas/一堂-个人修炼-Y模型实操口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计工具篇口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计探索营口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计概念口述版.md

- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md

- 00_inbox/ideas/一堂-个人修身-Y模型探索营2口述版.md

- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计02口述.md

- 10_raw/sources/一堂-个人修身-泛产品设计实操口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计审美口述.md

- 10_raw/sources/一堂-创业-调研行动营口述01.md

- 10_raw/sources/一堂-读书会-SPIN销售法口述.md

- src_unknown

- 00_inbox/ideas/Truman的个人成长五步法.md

- 00_inbox/ideas/truman的选择：两条职业成长路线.md

- 00_inbox/ideas/一堂-个人修炼-Y模型.md

- 00_inbox/ideas/一堂-个人修炼-Y模型实操口述版.md

- 00_inbox/ideas/一堂-个人修炼-全景图MUSE模型.md

- 00_inbox/ideas/一堂-个人修炼-双三角模型.md

- 00_inbox/ideas/一堂-个人修炼-提问刻意练习画布.md

- 10_raw/sources/一堂-个人修炼-泛产品设计工具篇口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计探索营口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计概念口述版.md

- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO-全景策略.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO完整清单.md

- 00_inbox/ideas/一堂-个人修炼-科学学习IPO模型.md

- 00_inbox/ideas/一堂-个人修炼-科学提问刻意练习.md

- 00_inbox/ideas/一堂-个人修炼-解放思想.md

- 00_inbox/ideas/一堂-个人修炼-课程清单.md

- 00_inbox/ideas/一堂-个人修身-Y模型探索营2口述版.md

- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计02口述.md

- 10_raw/sources/一堂-个人修身-泛产品设计实操口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计审美口述.md

- 10_raw/sources/一堂-创业-调研行动营口述01.md

- 00_inbox/ideas/一堂-创业必修-课程清单.md

- 00_inbox/ideas/一堂-地图-个人地图_conv.md

- 00_inbox/ideas/一堂-地图-创业地图_conv.md

- 00_inbox/ideas/一堂-地图-管理地图_conv.md

- 00_inbox/ideas/一堂-案例拆解-课程清单.md

- 00_inbox/ideas/一堂-泛产品设计-十年苦练30招.md

- 00_inbox/ideas/一堂-管理必修-课程清单.md

- 10_raw/sources/一堂-读书会-SPIN销售法口述.md

- 00_inbox/ideas/一堂个人地图：高潜力成长者修炼全景图.md

- 00_inbox/ideas/一堂五步法-产品内核画布.md

- 00_inbox/ideas/一堂五步法画布.md

- 00_inbox/ideas/一堂产品内核-十大典型指标.md

- 00_inbox/ideas/一堂刻意练习十年成长指数.md

- 00_inbox/ideas/一堂最佳转化率动力曲线图.md

- 00_inbox/ideas/一堂泛产品设计-十年修炼爬山地图.md

- 00_inbox/ideas/一堂泛产品设计-多出牌多练习.md

- 00_inbox/ideas/一堂泛产品设计36计-全套地图.md

- 00_inbox/ideas/一堂深度复盘冰山图.md

- 00_inbox/ideas/一堂转化率-10大容易浪费的触点.md

- 00_inbox/ideas/一堂进步大地图.md

- 00_inbox/ideas/一堂进步大地图_compressed.md

- 00_inbox/ideas/优秀泛产品设计者的自我修养.md

- 00_inbox/ideas/婚礼操盘-用户和场景.md

- 00_inbox/ideas/婚礼规划.md

- 00_inbox/ideas/审美提升的层级.md

- 00_inbox/ideas/微信图片_20260507004746_32_32.md

- 00_inbox/ideas/微信图片_20260507004751_33_32.md

- 00_inbox/ideas/微信图片_20260507004755_34_32.md

- 00_inbox/ideas/微信图片_20260507004758_35_32.md

- 00_inbox/ideas/微信图片_20260507004801_37_32.md

- 00_inbox/ideas/微信图片_20260507004802_38_32.md

- 00_inbox/ideas/微信图片_20260507004804_39_32.md

- 00_inbox/ideas/微信图片_20260507004806_40_32.md

- 00_inbox/ideas/微信图片_20260507004811_41_32.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践建模.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践收集.md

- 00_inbox/ideas/泛产品设计-审美卡片-最佳实践池子.md

- 00_inbox/ideas/泛产品设计-审美卡片-美好作品想象.md

- 00_inbox/ideas/泛产品设计-审美工具箱指南.md

- 00_inbox/ideas/泛产品设计-用户卡片-一堂五步法.md

- 00_inbox/ideas/泛产品设计-用户卡片-动力阻力.md

- 00_inbox/ideas/泛产品设计-用户卡片-场景推演.md

- 00_inbox/ideas/泛产品设计-用户卡片-多视角思考.md

- 00_inbox/ideas/泛产品设计-用户卡片-峰终定律.md

- 00_inbox/ideas/泛产品设计-用户卡片-惊喜公式.md

- 00_inbox/ideas/泛产品设计-用户卡片-用户分层.md

- 00_inbox/ideas/泛产品设计-用户卡片-用户视角.md

- 00_inbox/ideas/泛产品设计-用户卡片-行业分析画布.md

- 00_inbox/ideas/泛产品设计-用户卡片-需求挖掘.md

- 00_inbox/ideas/泛产品设计-用户卡片-项目背景分析.md

- 00_inbox/ideas/泛产品设计-落地卡片-ROI分析.md

- 00_inbox/ideas/泛产品设计-落地卡片-业务建模.md

- 00_inbox/ideas/泛产品设计-落地卡片-低成本测试MVP.md

- 00_inbox/ideas/泛产品设计-落地卡片-假设拆解.md

- 00_inbox/ideas/泛产品设计-落地卡片-内核和边界.md

- 00_inbox/ideas/泛产品设计-落地卡片-努力仿真.md

- 00_inbox/ideas/泛产品设计-落地卡片-十倍速验证.md

- 00_inbox/ideas/泛产品设计-落地卡片-善用佳软.md

- 00_inbox/ideas/泛产品设计-落地卡片-复盘迭代.md

- 00_inbox/ideas/泛产品设计-落地卡片-攻坚会.md

- 00_inbox/ideas/泛产品设计-落地卡片-灵感闪现.md

- 00_inbox/ideas/泛产品设计-落地卡片-管理三段论.md

- 00_inbox/ideas/泛产品设计-落地卡片-解放思想.md

- 00_inbox/ideas/泛产品设计-落地卡片-设计原则.md

- 00_inbox/ideas/泛产品设计-落地卡片-逻辑MECE.md

- 00_inbox/ideas/泛产品设计-落地卡片-酝酿式打磨.md

- 00_inbox/ideas/泛产品设计-落地卡片-里程碑拆解.md

- 00_inbox/ideas/泛产品设计-落地卡片-风险管理.md

- 00_inbox/ideas/泛产品设计-需求工具箱指南.md

- 00_inbox/ideas/泛产品设计的应用场景示意图.md

- 00_inbox/ideas/泛产品设计者的三大自我修养.md

- 00_inbox/ideas/泛产品设计者的自我修养.md

- 00_inbox/ideas/泛产品设计落地工具篇指南.md

- 00_inbox/ideas/泛产品设计落地篇.md

- 00_inbox/ideas/萃取总结.md

- 00_inbox/ideas/顶级产品追求的方向-乔布斯.md

- 00_inbox/ideas/项目背景问题思考的8个维度.md

- 00_inbox/ideas/预判模型.md

- 00_inbox/ideas/一堂-个人修炼-Y模型实操口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计工具篇口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计探索营口述版.md

- 10_raw/sources/一堂-个人修炼-泛产品设计概念口述版.md

- 00_inbox/ideas/一堂-个人修炼-知识萃取探索营口述版.md

- 00_inbox/ideas/一堂-个人修身-Y模型探索营2口述版.md

- 00_inbox/ideas/一堂-个人修身-思维模型口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计02口述.md

- 10_raw/sources/一堂-个人修身-泛产品设计实操口述版.md

- 10_raw/sources/一堂-个人修身-泛产品设计审美口述.md

- 10_raw/sources/一堂-创业-调研行动营口述01.md

- 10_raw/sources/一堂-读书会-SPIN销售法口述.md

- src_unknown

- src_unknown

- 00_inbox/Anthropic 官方发布：《创始人手册：打造 AI 原生初创公司》.md

- src_unknown

- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
- src_unknown
  - 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-X型Y型决策习惯对比_vlm_desc.md
  - 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-商业模式-完整财务公式决策_vlm_desc.md
  - 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-关键假设ABCD模型_vlm_desc.md
  - 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-ROI决策评估画布_vlm_desc.md
  - 00_inbox/_vlm_reprocess/科学决策/一堂-科学决策-深度-L3定量公式_vlm_desc.md


- 10_raw/sources/AI设计-AI设计基础01_cleaned.md

- 10_raw/sources/AI设计-AI设计师实操培训01_cleaned.md

- 00_inbox/design/prompts/ai-image-generation.md

- 00_inbox/ideas/2026-05-17-hci-decision-double-triangle.md

- 00_inbox/links/aima-ai-thinking-card-links.md

- 00_inbox/ocr_ingest/src_ocr_ocr_screenshot2.md

- 00_inbox/ocr_ingest/src_ocr_ocr_snipaste_2026_05_15_21_39_40.md

- 00_inbox/ocr_ingest/src_ocr_screenshot1.md

- 00_inbox/ocr_ingest/src_ocr_screenshot2.md

- 00_inbox/ocr_ingest/src_ocr_truman的个人成长五步法.md

- 00_inbox/ocr_ingest/src_ocr_truman的选择：两条职业成长路线.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_y模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_全景图muse模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_双三角模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_提问刻意练习画布.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_科学学习ipo_全景策略.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_科学学习ipo完整清单.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_科学学习ipo模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_科学提问刻意练习.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_表达力火箭模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_表达力火箭模型_执行武器库.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_解放思想.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_讲香十指模型_超级武器库.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_讲香基本功.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_讲香基本功_十指模型修炼地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂_个人修炼_课程清单.md

- 00_inbox/ocr_ingest/src_ocr_一堂_创业必修_课程清单.md

- 00_inbox/ocr_ingest/src_ocr_一堂_地图_个人地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂_地图_个人地图_conv.md

- 00_inbox/ocr_ingest/src_ocr_一堂_地图_创业地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂_地图_创业地图_conv.md

- 00_inbox/ocr_ingest/src_ocr_一堂_地图_管理地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂_地图_管理地图_conv.md

- 00_inbox/ocr_ingest/src_ocr_一堂_案例拆解_课程清单.md

- 00_inbox/ocr_ingest/src_ocr_一堂_泛产品设计_十年苦练30招.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_roi决策评估画布.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_roi决策评估画布_案例01.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_roi决策评估画布_案例02.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_roi决策评估画布_案例03.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_roi决策评估画布_案例04.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_roi高阶训练全景图.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_x型y型决策习惯对比.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_一堂双三角磨合追求_从入门到无限进步.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_人机协作决策.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_关键假设abcd模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_关键训练清单（重要））.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_决策三角形.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_发现决策.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_商业模式_完整财务公式决策.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_宽度_个人.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_宽度_企业.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_宽度_团队.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_l1优先级定性.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_l2部分定量.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_l3定量公式.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_l4_案例01.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_l4严格财务公式.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_你的业务是一次抽样实验.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_决策经验值.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_案例01.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_案例02.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_案例03.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_案例04.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_案例05.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_深度_案例06.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_稀缺机会窗口.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_稀缺资源清单.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_项目方案评估三角形.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_高度_两种典型的思考习惯.md

- 00_inbox/ocr_ingest/src_ocr_一堂_科学决策_高水平共识曲线（重要）.md

- 00_inbox/ocr_ingest/src_ocr_一堂_管理必修_课程清单.md

- 00_inbox/ocr_ingest/src_ocr_一堂y模型_科学成事道理.md

- 00_inbox/ocr_ingest/src_ocr_一堂y模型steps策略集.md

- 00_inbox/ocr_ingest/src_ocr_一堂y模型实操工作流.md

- 00_inbox/ocr_ingest/src_ocr_一堂个人地图：高潜力成长者修炼全景图.md

- 00_inbox/ocr_ingest/src_ocr_一堂五步法_产品内核画布.md

- 00_inbox/ocr_ingest/src_ocr_一堂五步法画布.md

- 00_inbox/ocr_ingest/src_ocr_一堂产品内核_十大典型指标.md

- 00_inbox/ocr_ingest/src_ocr_一堂刻意练习十年成长指数.md

- 00_inbox/ocr_ingest/src_ocr_一堂提炼过的因果模型.md

- 00_inbox/ocr_ingest/src_ocr_一堂最佳转化率动力曲线图.md

- 00_inbox/ocr_ingest/src_ocr_一堂泛产品设计36计_全套地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂泛产品设计_十年修炼爬山地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂泛产品设计_多出牌多练习.md

- 00_inbox/ocr_ingest/src_ocr_一堂深度复盘冰山图.md

- 00_inbox/ocr_ingest/src_ocr_一堂转化率_10大容易浪费的触点.md

- 00_inbox/ocr_ingest/src_ocr_一堂进步大地图.md

- 00_inbox/ocr_ingest/src_ocr_一堂进步大地图_compressed.md

- 00_inbox/ocr_ingest/src_ocr_优秀泛产品设计者的自我修养.md

- 00_inbox/ocr_ingest/src_ocr_婚礼操盘_用户和场景.md

- 00_inbox/ocr_ingest/src_ocr_婚礼规划.md

- 00_inbox/ocr_ingest/src_ocr_审美提升的层级.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004746_32_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004751_33_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004755_34_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004758_35_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004801_37_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004802_38_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004804_39_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004806_40_32.md

- 00_inbox/ocr_ingest/src_ocr_微信图片_20260507004811_41_32.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_审美卡片_最佳实践建模.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_审美卡片_最佳实践收集.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_审美卡片_最佳实践池子.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_审美卡片_美好作品想象.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_审美工具箱指南.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_一堂五步法.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_动力阻力.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_场景推演.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_多视角思考.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_峰终定律.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_惊喜公式.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_用户分层.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_用户视角.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_行业分析画布.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_需求挖掘.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_用户卡片_项目背景分析.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_roi分析.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_业务建模.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_低成本测试mvp.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_假设拆解.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_内核和边界.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_努力仿真.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_十倍速验证.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_善用佳软.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_复盘迭代.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_攻坚会.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_灵感闪现.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_管理三段论.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_解放思想.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_设计原则.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_逻辑mece.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_酝酿式打磨.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_里程碑拆解.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_落地卡片_风险管理.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计_需求工具箱指南.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计的应用场景示意图.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计者的三大自我修养.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计者的自我修养.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计落地工具篇指南.md

- 00_inbox/ocr_ingest/src_ocr_泛产品设计落地篇.md

- 00_inbox/ocr_ingest/src_ocr_萃取总结.md

- 00_inbox/ocr_ingest/src_ocr_顶级产品追求的方向_乔布斯.md

- 00_inbox/ocr_ingest/src_ocr_项目背景问题思考的8个维度.md

- 00_inbox/ocr_ingest/src_ocr_预判模型.md

- 00_inbox/prompts/business-analysis.md

- 00_inbox/prompts/learning-thinking.md

- 00_inbox/prompts/meta-prompt-eng.md

- 00_inbox/prompts/product-ux.md

- 00_inbox/prompts/tools-workflows.md

- 00_inbox/prompts/writing-content.md

- 00_inbox/visual-prompt-system_SKILL.md

- 00_inbox/water-sense/.water-sense-config.md

- 00_inbox/water-sense/2026-05-17.md

- 00_inbox/water-sense/2026-05.md

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/ai-native-five-levels.md

- 00_inbox/AI-study/asking-the-right-questions-critical-thinking.md


- src_unknown

- src_unknown

- src_unknown

- 00_inbox/AI应用场景01.md

- 00_inbox/AI时代自进化组织形式.md

- src_unknown

- src_unknown

- 00_inbox/yitang-unit-model-ai-transcript.md

- src_unknown

- 00_inbox/design/AI设计-AI设计基础01.txt

- 00_inbox/design/AI设计-AI设计师实操培训01.txt

- 00_inbox/design/AI设计-文创案例设计课口述.txt

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/AI-study/AI数据/AI数据理解第一课表格.md

- 00_inbox/数据标注维度最佳实践调研报告.md

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- 00_inbox/半肥猫-AI学习落地-口述.md

- 00_inbox/广冷电子/_archive/07_logs/HX-SMJ故障分析报告.md

- 00_inbox/广冷电子/_archive/07_logs/PROJECT_CATALOG.md

- 10_raw/literature/README.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_10.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_11.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_12.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_13.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_14.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_15.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_16.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_17.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_3.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_4.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_5.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_6.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_7.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_8.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCBA加工要求_9.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCB加工要求_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/HX-SMJ-01_V1.0 PCB加工要求_2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/PCB加工要求_HX-SMJ-01.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01-继电器板/PCB加工要求_HX-SMJ-01_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01B-主控板/PCB加工要求_HX-SMJ01主控板V2.0.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01B-主控板/HX-SMJ01B-12306_V2.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01B-主控板/HX-SMJ01B-12306_V2.0 PCB加工要求_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01B-主控板/HX-SMJ01B-12306_V2.0 PCB加工要求_2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-01B-主控板/PCB加工要求_HX-SMJ01主控板V2.0.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-A-红外板-A/HX-SMJ-03B-A_V2.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-A-红外板-A/HX-SMJ-03B-A_V2.0 PCB加工要求_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-A-红外板-A/HX-SMJ-03B-A_V2.0 PCB加工要求_2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-A-红外板-A/PCB加工要求_HX-SMJ-03B-A_V2.2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-A-红外板-A/PCB加工要求_HX-SMJ-03B-A_V2.2_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-B-红外板-B/HX-SMJ-03B-B_V2.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-B-红外板-B/HX-SMJ-03B-B_V2.0 PCB加工要求_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-B-红外板-B/HX-SMJ-03B-B_V2.0 PCB加工要求_2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-B-红外板-B/PCB加工要求_HX-SMJ-03B-B_V2.2.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-03B-B-红外板-B/PCB加工要求_HX-SMJ-03B-B_V2.2_1.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-04B-货道电机板/PCB加工要求_HX-SMJ-04B.md

- 00_inbox/广冷电子/广冷001/02_pcb/HX-SMJ-04B-货道电机板/PCB加工要求_HX-SMJ-04B_1.md

- 00_inbox/广冷电子/广冷001/06_logs/BOM差异分析报告.md

- 00_inbox/广冷电子/广冷001/06_logs/交叉验证综合报告.md

- 00_inbox/广冷电子/广冷001/06_logs/原理图BOM交叉验证报告.md

- 00_inbox/广冷电子/广冷001/06_logs/原理图独立验证报告.md

- 00_inbox/广冷电子/广冷001/06_logs/固件源码分析报告.md

- 00_inbox/广冷电子/广冷001/06_logs/坐标一致性验证报告.md

- 00_inbox/广冷电子/_archive/07_logs/HX-SMJ故障分析报告.md

- 00_inbox/广冷电子/_archive/07_logs/PROJECT_CATALOG.md

- 10_raw/literature/README.md

- 00_inbox/广冷电子/广冷001/广冷-PCB制板-2025年/广冷-PCB制版要求/HX-SMJ-02B_V2.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/广冷-PCB制板-2025年/广冷-PCB制版要求/HX-SMJ-02B_V2.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/广冷-PCB/广冷PCBA/广冷华旭-PCB板卡资料-加密/售卖机板卡设计说明.md

- 00_inbox/广冷电子/广冷001/广冷-PCB/广冷PCBA/广冷华旭-PCB板卡资料-加密/售卖机板卡设计说明.md

- 00_inbox/广冷电子/广冷001/广冷-PCB/广冷PCBA/广冷华旭-PCB板卡资料-加密/售卖机板卡设计说明.md

- 00_inbox/广冷电子/广冷001/广冷-PCB/广冷评审文件 - V1.1/1.系统功能概述/1.系统功能概述.md

- 00_inbox/广冷电子/广冷001/广冷-PCB/广冷评审文件 - V1.1/2.原理主要参数计算/2.原理主要参数计算.md

- 00_inbox/广冷电子/广冷001/广冷-PCB制板-2025年/广冷-PCB制版要求/HX-SMJ-02B_V2.0 PCB加工要求.md

- 00_inbox/广冷电子/广冷001/广冷2/串口设备通信/串口一级通讯协议/巨米串口通讯协议.md

- 00_inbox/广冷电子/广冷001/广冷2/串口设备通信/串口协议应用/指令CMD使用一览.md

- 00_inbox/广冷电子/广冷001/广冷2/串口设备通信/串口协议应用/自动售货机二级专用协议 - 20201230.md

- 00_inbox/广冷电子/广冷001/广冷2/串口设备通信/二级通用设备协议/巨米设备通讯协议.md

- 00_inbox/广冷电子/广冷001/广冷2/串口设备通信/自动售货机二级专用协议/自动售货机二级专用协议.md

- 00_inbox/广冷电子/广冷001/广冷2/串口设备通信/错误码规则及错误码列表.md

- 00_inbox/广冷电子/广冷001/欧阳锋建议书.md

- 00_inbox/广冷电子/广冷001/资料/售卖机板卡设计说明(1).md

- 00_inbox/广冷电子/广冷001/广冷-PCB/广冷PCBA/广冷华旭-PCB板卡资料-加密/售卖机板卡设计说明.md

- 00_inbox/广冷电子/广冷001/资料/整体电控方案说明.md

- 00_inbox/广冷电子/广冷001/资料/高铁自助售货机-电控方案-广冷.md

- 00_inbox/广冷电子/广冷001/资料整理方案.md

- 00_inbox/广冷电子/广冷001/资料整理方案_执行版.md

- 00_inbox/水水-拆书会偶然-口述.md

- 00_inbox/纪浩-AI协作方法论-口述.md

- 00_inbox/马易-AI落地场景识别-口述.md

- src_unknown

- 00_inbox/AI俱乐部-人和AI协作-纪浩-五层结构-结构化.md

- 00_inbox/AI俱乐部-人和AI协作-纪浩-参考案例-结构化.md

- 00_inbox/paddle_batch/AI俱乐部-人和AI协作-纪浩-五层结构-图片01_paddle_ocr.md

- 00_inbox/paddle_batch/AI俱乐部-人和AI协作-纪浩-参考案例-图片02_paddle_ocr.md

- 00_inbox/paddle_batch/ocr_Snipaste_2026-05-15_21-39-40_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-AI学习-truman自用的AI FeatureSet_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-AI学习-提问工程化_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-AI学习-提问进化路线图_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-AI清单体笔记（系统故事线）-truman-图片01_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-AI清单体笔记（训练段位图）-truman-图片02_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-TCPR模型-皇冠模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-Y模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-全景图MUSE模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-双三角模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-提问刻意练习画布_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-科学学习IPO-全景策略_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-科学学习IPO完整清单_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-科学学习IPO模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-科学提问刻意练习_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-表达力火箭模型-执行武器库_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-表达力火箭模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-解放思想_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-讲香十指模型-超级武器库_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-讲香基本功-十指模型修炼地图_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-讲香基本功_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-个人修炼-课程清单_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-人机协作-双三角模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-创业必修-课程清单_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-ABCD策略模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-TCPR底层网络协议_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-修炼地图_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-动态预测_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单sku模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单商圈模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单城市模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单客户模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单履约模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单柜子模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单用户模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单订单模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单销售模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-单门店模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-基准值_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-壁垒预判_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-外部对抗地图_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-多模型情况_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-学练用_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-对抗小抄01_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-对抗小抄02_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-对抗小抄_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-扭蛋机案例_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-找全成本实操难点_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-找单元模型实操难点_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-找基准值实操难点_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-斧子、尺子、梯子_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-斧子尺子梯子详解_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-最简单元模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-段位专家_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-示例01_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-示例_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-规模对抗实操难点_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-规模经济对抗武器库_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-单元模型-象限分析法_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-ROI决策评估画布-案例01_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-ROI决策评估画布-案例02_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-ROI决策评估画布-案例03_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-ROI决策评估画布-案例04_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-ROI决策评估画布_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-ROI高阶训练全景图_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-X型Y型决策习惯对比_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-关键假设ABCD模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-关键训练清单（重要））_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-决策三角形_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-深度-L1优先级定性_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-深度-L2部分定量_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-深度-L3定量公式_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-深度-L4-案例01_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-深度-L4严格财务公式_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-科学决策-高水平共识曲线（重要）_paddle_ocr.md

- 00_inbox/paddle_batch/一堂-高阶体系探索营-三种咨询可能性_paddle_ocr.md

- 00_inbox/paddle_batch/一堂DOC-单元模型-十大单元模型_paddle_ocr.md

- 00_inbox/paddle_batch/一堂Y模型-科学成事道理_paddle_ocr.md

- 00_inbox/paddle_batch/泛产品设计-落地卡片-ROI分析_paddle_ocr.md

- 00_inbox/paddle_batch/泛产品设计-落地卡片-低成本测试MVP_paddle_ocr.md

- 00_inbox/paddle_batch/泛产品设计-落地卡片-逻辑MECE_paddle_ocr.md

- src_unknown

- src_unknown
- src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
    - src_unknown
    - src_unknown
    - src_unknown
    - src_unknown
    - src_unknown
    - src_unknown
    - src_unknown
    - src_unknown
  - src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown

- src_unknown
