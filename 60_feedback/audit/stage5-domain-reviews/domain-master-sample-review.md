# 30_wiki Domain 专项审查报告（Stage 5 · Master 样本）

## 基本信息

| 项目 | 内容 |
|------|------|
| 审查样本数 | **30 张卡片** |
| 清单文件 | `C:/Users/Administrator/Desktop/wiki/60_feedback/audit/.stage5-tmp/domain-master-sample.txt` |
| 审查日期 | 2026-06-14 |
| 审查维度 | Domain 一致性、内容完整性、Source 可验证性、Confidence/Trust 一致性、卡片间关系、类型特定检查 |
| 审查说明 | **仅审查并输出报告，未修改原文件。** |

---

## 样本分布

| 类型 | 数量 | 文件 |
|------|:--:|------|
| dark-knowledge | 14 | dk-f2, dk-c1, dk-f6, dk-f3, dk-f11, dk-f14, dk-p2, dk-p4, dk-p6, dk-p10, dk-p13, dk-p17, dk-modeling-counterexample-driven, dk-yb20-ai-eye-high-principle |
| concept | 6 | yt-business-formula-six-level-logic, yt-business-formula-parameter-iceberg, yt-business-formula-ten-paradigms, yt-concept-peas-insight, ocr-婚礼规划, sprint-2-门禁举证验收 |
| tool | 4 | yt-unit-model-selection, yt-unit-model-dynamic, master-cognitive-bias-checklist, master-first-principles |
| decision | 4 | data-curator-role-division, ouyangfeng-labeling-research-review, ouyangfeng-data-alignment-response |
| improvement-plan | 3 | plan_20260531_data-curator-v1.1, proposal-prompt-injection-infrastructure, proposal-kdo-flywheel-infrastructure |

| Domain 分布 | 数量 | 备注 |
|-------------|:--:|------|
| master | 23 | 含 KDO 项目暗知识、决策、改进方案、通用方法论工具 |
| yitang | 5 | 业务公式、单元模型等一堂课程内容 |
| entrepreneur | 2 | 单元模型工具中通过 `yitang.map: entrepreneur` 引入 |
| business-strategy | 3 | 业务公式概念卡附带 |
| design | 1 | dk-yb20-ai-eye-high-principle |

---

## 问题分类统计

| 问题大类 | 出现次数 | 涉及卡片数 | 典型表现 |
|----------|:--------:|:----------:|----------|
| Source 可验证性不足 | 8 | 8 | source_refs 缺失、来源描述模糊（如“消化全库后提炼”“Aristotle, Elon Musk”） |
| 内容完整性/深度不足 | 7 | 7 | 暗知识卡缺少案例、OCR 卡质量差且 Open Questions 过多、Sprint 2 卡过薄 |
| Frontmatter/格式/结构问题 | 6 | 6 | 重复字段、重复章节、Markdown 语法缺陷、章节为空 |
| 卡片间关系标注错误 | 5 | 12+ | `contradicts` 字段被大量误用于“相关/纠正”关系 |
| Domain 一致性 | 3 | 3 | 单元模型工具缺少 `yitang` domain、婚礼规划卡 domain 宽泛 |
| Confidence/Trust 校准 | 3 | 3 | OCR 卡与 Sprint 2 卡 trust 偏高、部分工具卡 confidence 偏高 |
| 类型特定检查 | 2 | 4 | tool 卡存在大量视觉描述噪音、concept 卡定义/案例不足 |

> 注：同一卡片可能同时命中多个问题大类。

---

## 具体卡片问题清单

### P0 / 严重（需优先处理）

| 文件路径 | 主要问题 | 处理建议 |
|----------|----------|----------|
| `30_wiki/dark-knowledges/dk-yb20-ai-eye-high-principle.md` | **内容严重不足**：原始引用语句不完整（“你只会从一个许愿变成一个。”断句）；“对象性”概念未定义；无具体案例/数据/outcome；操作步骤仅 3 条高度抽象。 | 补全原始引用上下文；给出 1-2 个月白课程中的真实 before/after 案例；把“对象性”拆解为可执行的 prompt/描述模板；若无法补充则降权为 stub。 |
| `30_wiki/concepts/ocr-婚礼规划.md` | **OCR 质量与内容完整性双差**：Summary 中文件路径断行（`00_inbox/婚礼规划.\n\npng`）；Reusable Knowledge 基于婚礼单一高度场景，迁移性未验证；Open Questions 多达 9 条，说明原始素材尚未被充分理解；Critique 中 `**` 未闭合；domain 标为 `master` 过于宽泛。 | 人工校对原图并修复 OCR 文本；明确这是 `personal` 域的仪式事件案例卡，还是 master 域的“仪式化事件个性化框架”；补全方法论定义与跨场景案例；修复 Markdown 语法。 |
| `30_wiki/concepts/sprint-2-门禁举证验收.md` | **概念卡过薄**：仅 3 段 Summary、1 条通用 Critique、无具体案例；trust_level=medium 与内容深度不匹配。 | 补充 ingest→enrich→gate 端到端的真实运行示例；增加失败模式案例；将 trust 降至 medium-low 或 low，直到内容补全。 |

### P1 / 重要（建议下一批次处理）

| 文件路径 | 主要问题 | 处理建议 |
|----------|----------|----------|
| `30_wiki/tools/yt-unit-model-selection.md`<br>`30_wiki/tools/yt-unit-model-dynamic.md` | **Domain 标注不一致**：两张卡 frontmatter 中 `domain` 只有 `entrepreneur` + `master`，缺少 `yitang`；但正文明确定义为一堂课程工具，且 `yitang.map: entrepreneur`。其他一堂卡片（如 yt-business-formula-*）均含 `yitang`。 | 统一将 domain 修正为 `yitang, entrepreneur, master`（或按 registry 规范合并 `entrepreneur` 进 `yitang`）。 |
| `30_wiki/concepts/master-cognitive-bias-checklist.md`<br>`30_wiki/concepts/master-first-principles.md` | **Source 可验证性差**：source_refs 为 `{'来源': '消化全库后提炼'}` / `{'来源': 'Aristotle, Elon Musk'}`，无法追溯到具体材料。 | 为认知偏差清单引用具体文献（Kahneman《噪声》《快思慢想》等）或 vault 卡片；为第一性原理引用 Musk 具体访谈/演讲或 Aristotle 具体文本章节。 |
| `30_wiki/decisions/data-curator-role-division.md`<br>`30_wiki/decisions/ouyangfeng-labeling-research-review.md`<br>`30_wiki/decisions/ouyangfeng-data-alignment-response.md`<br>`30_wiki/decisions/proposal-prompt-injection-infrastructure.md`<br>`30_wiki/decisions/proposal-kdo-flywheel-infrastructure.md` | **Source/refs 缺失或不足**：无 `source_refs` 字段；proposal 类未记录触发对话/会议；decision 类缺少可核对的原始输入。 | 在 frontmatter 中补充 `source_refs` 或 `source_context`（如会议日期、触发对话、相关任务文件路径）。 |
| `30_wiki/dark-knowledges/dk-p17-accuracy-gap.md`<br>`30_wiki/dark-knowledges/dk-f14-accuracy-measurement-mismatch.md` | **卡片间关系缺失/冗余**：两者是同一主题（准确率测量口径）的具体事故与模式抽象，但互相未在 `related` 中链接；dk-f14 的 `related` 指向 `dk-p15-claimed-done-not-verified`，未指向 dk-p17。 | 在两张卡的 `related` 中互链；考虑将 F-KDO-014 与 P-17 合并或明确父子关系。 |
| `30_wiki/tools/yt-unit-model-selection.md`<br>`30_wiki/tools/yt-unit-model-dynamic.md` | **视觉描述噪音**：两张卡均包含大量“原图为二维矩阵…空间层级…留白运用…”等图像描述文字（-selection 约 100 行、-dynamic 约 30 行），对工具使用价值极低，且未与操作方法结合。 | 将 Visual Analysis 精简为“见原图/资产链接”或只保留与决策直接相关的 1-2 句话；其余移至原始素材归档。 |
| `30_wiki/concepts/yt-concept-peas-insight.md` | **结构重复/空章节**：“内部局限”标题下无内容；存在两个“不要用的场景”表格（其中一个为模板化残留）。 | 删除空“内部局限”或补充内容；删除第二个模板化“不要用的场景”。 |
| `30_wiki/concepts/master-cognitive-bias-checklist.md`<br>`30_wiki/concepts/master-first-principles.md` | **章节重复**：均有“五、外部攻击”与后续独立的 `## Critique` 重复批判 Taleb/Simon；末尾还有模板化的“不要用的场景”。 | 合并重复 Critique；删除或补全模板化残留章节。 |

### P2 / 轻微（可批量脚本化处理）

| 文件路径 | 主要问题 | 处理建议 |
|----------|----------|----------|
| `30_wiki/dark-knowledges/dk-modeling-counterexample-driven.md` | **Frontmatter 重复字段**：`trust_level: high` 出现两次。 | 脚本去重，保留一个。 |
| `30_wiki/dark-knowledges/dk-f2-txt-ingest-skip.md`<br>`30_wiki/dark-knowledges/dk-c1-cjk-regex-silent-fail.md`<br>`30_wiki/dark-knowledges/dk-f6-cjk-skeleton-corruption.md`<br>`30_wiki/dark-knowledges/dk-p2-tmux-cache.md`<br>`30_wiki/dark-knowledges/dk-p4-batch-format-empty.md`<br>`30_wiki/dark-knowledges/dk-p10-oral-ban.md`<br>`30_wiki/dark-knowledges/dk-p13-token-burn.md`<br>`30_wiki/dark-knowledges/dk-p17-accuracy-gap.md`<br>`30_wiki/dark-knowledges/dk-p6-session-resume-fail.md`<br>`30_wiki/dark-knowledges/dk-f14-accuracy-measurement-mismatch.md` | **`contradicts` 字段系统性误用**：大量将 `master-systems-thinking`、`master-first-principles`、`master-ai-info-literacy`、`master-decision-hygiene`、`master-knowledge-compound` 等概念卡标记为 `contradicts`，而实际关系应为 `related` 或 `corrects`。 | 批量审查所有 dark-knowledge 卡的 `contradicts` 字段；建立规则：failure/insight 型暗知识一般不应 contradict 通用方法论概念卡，除非确有逻辑对立。 |
| `30_wiki/tools/yt-unit-model-selection.md` | **转义字符残留**：正文出现 `\"用户数\"` 等转义引号。 | 脚本清理 `"` → `"`。 |
| `30_wiki/concepts/ocr-婚礼规划.md` | **Markdown 语法错误**：Summary 中路径换行异常；Critique 中 `**` 未闭合。 | 脚本/人工修复 Markdown。 |

### 无明显问题卡片

以下卡片在本次审查范围内未观察到明显问题，或仅有可接受的草稿状态（low trust + pending review）：

- `30_wiki/dark-knowledges/dk-f2-txt-ingest-skip.md`
- `30_wiki/dark-knowledges/dk-c1-cjk-regex-silent-fail.md`
- `30_wiki/dark-knowledges/dk-f6-cjk-skeleton-corruption.md`
- `30_wiki/dark-knowledges/dk-f3-state-json-race-condition.md`
- `30_wiki/dark-knowledges/dk-p2-tmux-cache.md`
- `30_wiki/dark-knowledges/dk-p4-batch-format-empty.md`
- `30_wiki/dark-knowledges/dk-p10-oral-ban.md`
- `30_wiki/dark-knowledges/dk-p13-token-burn.md`
- `30_wiki/dark-knowledges/dk-p6-session-resume-fail.md`
- `30_wiki/concepts/yt-business-formula-six-level-logic.md`
- `30_wiki/concepts/yt-business-formula-parameter-iceberg.md`
- `30_wiki/concepts/yt-business-formula-ten-paradigms.md`
- `30_wiki/decisions/plan_20260531_data-curator-v1.1.md`（状态为 superseded，符合预期）

> 注：上述“无明显问题”仅针对本次 6 个审查维度；部分卡片仍处于 draft/pending review 状态，本身符合低 confidence/low trust 标注。

---

## 批量处理建议

### 可脚本化批量修复

| 修复项 | 脚本策略 | 预计影响卡片数 |
|--------|----------|:-------------:|
| Frontmatter 重复字段去重 | 解析 YAML，检测并删除重复 key（如 `trust_level`） | 1+ |
| Markdown 语法基础检查 | 检测未闭合 `**`、未闭合代码块、路径内异常换行 | 2+ |
| 转义引号清理 | 将正文中的 `\"` 替换为 `"` | 1+ |
| `contradicts` 字段批量审计 | 输出所有 `contradicts` 指向 `master-*` 概念卡的清单，供人工二次确认 | 10+ |
| `source_refs` 缺失检测 | 扫描所有 decision/improvement-plan/concept/tool 卡片，列出无 `source_refs` 的文件 | 8+ |
| 视觉描述噪音标记 | 检测“Visual Analysis”章节长度，超过阈值（如 20 行）自动标注意见 | 2+ |
| 重复章节检测 | 检测同一文件中“Critique/外部攻击/不要用的场景”等章节的重复出现 | 3+ |

### 必须人工判断

| 处理项 | 原因 | 建议执行者 |
|--------|------|-----------|
| Domain 归属校准（单元模型工具是否加 `yitang`） | 涉及 KDO domain registry 规范与 yitang map 的映射关系 | 欧阳锋 / 黄药师 |
| `contradicts` vs `related` 语义修正 | 需要理解卡片实际逻辑关系，脚本只能辅助 | 欧阳锋 / 内容审查员 |
| Source 补充（master-cognitive-bias-checklist、master-first-principles 等） | 需要人工查找原始文献或 vault 卡片 | 老顽童 / 黄药师 |
| dk-yb20 内容补全 | 需要回看月白口述稿原文件，提取真实案例 | 老顽童 |
| ocr-婚礼规划 人工校对 | 必须对照原图确认 OCR 误识与符号语义 | 洪七公 / 老顽童 |
| Sprint 2 门禁举证验收 内容深化 | 需要补充真实运行示例与失败案例 | 黄药师 |
| 视觉分析章节取舍 | 需判断哪些图像描述对工具使用有实际价值 | 老顽童 |

---

## Domain 级结论

### 整体质量判断

| Domain | 整体质量 | 主要风险点 | 优先处理建议 |
|--------|:--------:|------------|--------------|
| **master** | 中等 | ① 暗知识卡 `contradicts` 字段系统性误用；② 多张 decision/proposal 卡缺少 source_refs；③ 部分工具卡存在来源模糊或结构冗余 | 先批量修复关系字段与 source_refs，再人工补全关键 decision/proposal 的来源上下文 |
| **yitang** | 较高 | ① 单元模型工具 domain 标注与一堂课程体系不一致；② 部分工具卡视觉描述噪音过大 | 统一 domain 标注规范，清理视觉分析噪音 |
| **business-strategy** | 较高 | 与 yitang 高度绑定，需确认是否应独立成 domain | 与 yitang domain 规范对齐 |
| **design** | 低 | dk-yb20 内容严重不足，原始引用断裂，案例缺失 | 优先补全该卡内容或降级为 stub |
| **entrepreneur** | — | 仅作为 `yitang.map` 出现，frontmatter domain 中未统一 | 明确 entrepreneur 是 yitang 子域还是独立 domain |

### 最大风险点

1. **`contradicts` 字段滥用导致图谱关系污染**：大量暗知识卡将“相关/纠正/案例”关系标记为“矛盾”，会严重误导下游 RAG/图谱检索。这是本次样本中最普遍的结构性问题，建议优先脚本化审计。

2. **Source 可验证性薄弱**：30 张卡中约 8 张存在 source_refs 缺失或模糊来源，尤以 decision/proposal 类为甚。作为知识库，决策类卡片缺少可追溯来源将削弱可信度。

3. **低质量 OCR 卡直接 enriched**：`ocr-婚礼规划.md` 存在大量未解决的 Open Questions 和语法错误，却被标记为 `enriched`/`trust_level: medium`，存在“状态字段与实际质量脱钩”的风险。

4. **模板化残留与结构冗余**：`master-cognitive-bias-checklist`、`master-first-principles`、`yt-concept-peas-insight` 等卡存在重复章节，暗示批量生成/升级过程中未做人工清理。

### 优先处理建议

1. **P0 立即处理**：补全 `dk-yb20-ai-eye-high-principle.md` 内容；修复 `ocr-婚礼规划.md` 的 OCR 与 domain；深化 `sprint-2-门禁举证验收.md`。
2. **批量脚本第一批次**：清理 `contradicts` 误用、修复 Markdown 语法、补充缺失的 `source_refs` 清单、去重 frontmatter 字段。
3. **人工审查第二批次**：校准 yitang/entrepreneur/business-strategy 的 domain 规范；清理工具卡视觉描述噪音；补充 decision/proposal 的来源上下文。
4. **建立门禁规则**：
   - `concept` 卡 enriched 前必须关闭所有 Open Questions 或明确标记为 unresolved；
   - `tool` 卡 Visual Analysis 章节长度超过阈值需人工确认；
   - `dark-knowledge` 卡 `contradicts` 字段必须经脚本+人工双重校验；
   - decision/proposal 类卡片必须包含 `source_refs` 或 `source_context`。

---

*审查员：Kimi Code CLI（Stage 5 Domain 专项审查）*
