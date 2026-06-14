# 30_wiki 全库深度审查阶段 3 报告：huangyaoshi-review-legacy-sample

**审查批次**：legacy / 黄药师样本  
**样本文件**：`C:/Users/Administrator/Desktop/wiki/60_feedback/audit/.stage3-tmp/huangyaoshi-review-legacy-sample.txt`  
**审查样本数**：40 张卡片  
**审查日期**：2026-06-14  
**审查维度**：内容完整性、Source 可验证性、Confidence/Trust 一致性、与其他卡片关系、类型特定检查  
**审查结论**：仅审查并输出报告，未修改任何原文件。

---

## 1. 总体结论

本次审查的 40 张卡片整体结构较为完整，绝大多数卡片具备：
- 清晰的 `Summary` / `Claims` / `Critique` / `Constraints & Boundaries` / `Synthesis` / `Action Triggers` 结构；
- 明确的适用边界与失败模式；
- 与其他 wiki 卡片的关联链接。

但存在几类**系统性问题**：
1. **Source 溯源薄弱**：大量课程衍生卡片只引用通用的 `10_raw/sources/一堂-课程地图精华串讲.md`，未指向具体课程逐字稿或原始讲义，导致可验证性差。
2. **YAML/元数据质量参差**：存在重复键、`null` 标签/流水线、字段拼写错误、实体卡 YAML 结构损坏等问题。
3. **模板重复与内容漂移**：多张落地卡片出现重复的“不要用的场景”段落，部分概念卡重复出现 Taleb/Simon 批判模板。
4. **类型标注与内容不匹配**：部分 `tool`/`concept` 标签与正文结构不符；`case` 卡中的数据缺乏可验证来源。
5. **过时与重叠关系**：`yt-model-prediction-model` 已被新版替代但未标记；`yt-research-weaponry-course` 与 `yt-entrepreneur-research-camp` 存在内容重叠。

---

## 2. 问题分类统计

| 问题分类 | 涉及卡片数 | 占比 | 典型表现 |
|---|---:|---:|---|
| **A. Source 溯源不足/不可验证** | 24 | 60% | source_refs 为空、仅指向课程总串讲/图片、src ID 无路径映射、缺少原始课程/报告原文 |
| **B. YAML/元数据质量** | 12 | 30% | 重复键、null 标签/流水线、字段名错误、YAML 结构损坏、id 异常 |
| **C. 内容完整性（课程介绍化/空泛）** | 8 | 20% | 正文大量“本课程属于…课程配有选课口令”式描述，缺少可执行步骤或真实案例 |
| **D. 类型标注与内容不匹配** | 8 | 20% | tool/framework/concept/skill 标签与正文结构不符 |
| **E. 重复/冲突/过时** | 5 | 12.5% | 已被替代未标记、同类方法论卡片重叠、案例数据无法交叉验证 |
| **F. Confidence/Trust 一致性** | 9 | 22.5% | confidence 偏高但来源薄弱、缺失 confidence、trust_level 与来源质量不匹配 |
| **G. 模板重复/冗余段落** | 7 | 17.5% | “不要用的场景”、Taleb/Simon 批判等模板在同一张卡中重复出现 |

> 注：单张卡片可能同时属于多个分类，因此占比之和大于 100%。

---

## 3. 具体卡片问题清单

### 3.1 存在明显问题的卡片

| 序号 | 文件路径 | 问题分类 | 问题描述 | 处理建议 |
|---|---|---|---|---|
| 1 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-growth-flywheel.md` | A/C/D/F | `source_refs` 仅指向通用课程地图串讲，未指向“增长飞轮”课程原文；正文大量“本课程属于…配有选课口令”式课程介绍；`type: tool` 但正文以框架/课程概述为主；confidence 0.8 与薄弱来源不匹配。 | 将 source_refs 替换为增长飞轮课程逐字稿/讲义；补充飞轮地图填写模板或检查清单，或改 `type` 为 `framework`；在补充具体来源前 confidence 降至 0.7。 |
| 2 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-five-step-canvas.md` | A/B/C | `source_refs` 仅两张 PNG 截图，无原始课程文本；YAML 存在重复 `updated_at` 键；正文缺少可下载/可填写的画布模板或完整示例。 | 补充五步法画布课程讲义/口述稿来源；删除重复键；在正文中附加空白画布模板或一个已填写的示例。 |
| 3 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-research-camp.md` | B/E | YAML 存在重复 `updated_at` 键；与 `yt-research-weaponry-course` 同源（一堂调研行动营），部分内容重叠。 | 删除重复键；在两张卡片 Synthesis 中明确分工：本卡侧重“行动营结构与学习路径”，武器库卡侧重“18/13 招执行策略”，或考虑合并。 |
| 4 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-five-step-method.md` | A/B/C/D/F | `source_refs` 仅通用课程地图串讲；YAML `tags`/`pipeline` 含大量 `null`；正文是课程目录式概述，缺少可执行步骤；`type: tool` 与正文框架总纲定位不符。 | 补充五步法核心课程原文；清理 null 字段；增加“五步工作流”操作步骤，或改 `type` 为 `framework`；confidence 降至 0.7。 |
| 5 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-barriers.md` | A/C/D/F | `source_refs` 仅通用课程地图串讲；正文课程介绍化；`type: tool` 但更像是壁垒框架/课程卡。 | 补充壁垒课程原文；减少 boilerplate；改 `type` 为 `framework` 或增加工具化检查清单。 |
| 6 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-fab-persuasion.md` | B | YAML 中 `review_by: 2026-12-06` 疑似 `review_date` 拼写错误，与已有的 `reviewed_by` 混淆。 | 将 `review_by` 改为 `review_date`，并统一日期格式。 |
| 7 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-milestone-breakdown.md` | A/B/C | `source_refs` 仅一张 PNG；正文出现两个重复的“不要用的场景”表格；缺少里程碑拆解的完整示例。 | 补充落地卡片课程/讲义来源；删除重复段落；增加一个真实项目的里程碑拆解示例。 |
| 8 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\paddleocr-skill.md` | A/B/D/F | `source_refs` 为空字符串；缺少 `confidence`；`type: concept` 与正文“本地 ONNX 部署 Skill”不符；`trust_level: high` 缺乏来源支撑。 | 添加 source_refs 指向 `SKILL.md`、`ocr-paddle.cjs`、模型文件等；将 `type` 改为 `skill` 或 `tool`；补充 `confidence`（建议 0.85）。 |
| 9 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\graph-rag.md` | A/B/D/F | 完全缺失 `source_refs`；缺少 `confidence`；`type: concept` 但正文是系统架构/实现提案；`trust_level: medium` 与无来源状态不匹配；存在 `[Critique]` 与后续 `Critique` 重复段落。 | 添加 source_refs（GraphRAG 论文、Neo4j 工具、KDO Protocol、相关课程）；将 `type` 改为 `framework` 或 `system`；补充 `confidence`；删除重复批判段落。 |
| 10 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-business-growth.md` | A/C/D/F | `source_refs` 仅通用课程地图串讲；正文课程介绍化；`type: tool` 与框架/课程定位不符。 | 补充业务增长课程原文；增加增长实验模板或渠道矩阵工具，或改 `type` 为 `framework`。 |
| 11 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-product-design.md` | A/C/D/F | `source_refs` 仅通用课程地图串讲；正文前半为课程目录 boilerplate；`type: tool` 但更像 framework/课程卡。 | 补充泛产品设计系列课程原文；删减课程介绍段落；改 `type` 为 `framework` 或强化工具化输出。 |
| 12 | `C:\Users\Administrator\Desktop\wiki\30_wiki\entities\紫鲸AI.md` | A/B/C/F | YAML 结构损坏：`source_refs:` 后紧跟 `id: 紫鲸AI` 与列表项混排；`source_refs` 中的 src ID 未映射到具体文件；缺少 `confidence`；核心数据（BrandKG 42%→89%、定价等）无引用。 | 修复 YAML 结构；将 src ID 映射为 `10_raw/sources/...` 路径；补充 `confidence`；为关键数据添加来源标注。 |
| 13 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-y-model-ruler.md` | B | YAML 中 `review_by: 2026-12-06` 疑似 `review_date` 拼写错误。 | 修正为 `review_date`。 |
| 14 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-management-trilogy.md` | A/B/C | `source_refs` 仅 PNG 图片；出现两个重复“不要用的场景”表格；缺少真实管理三段论应用示例。 | 补充来源；删除重复段落；增加项目启动/资源不足场景的应用示例。 |
| 15 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-entrepreneur-map.md` | A/B | `source_refs` 仅通用课程地图串讲+图片；YAML `tags`/`pipeline` 含大量 `null`。 | 补充创业地图原文/讲义；清理 null 字段。 |
| 16 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-ai-capability.md` | A/C/D/F | `source_refs` 仅通用课程地图串讲；正文课程介绍化；`type: tool` 但更像 framework/课程卡。 | 补充 AI 能力课程原文；改 `type` 为 `framework` 或增加工具化提示词/检查清单。 |
| 17 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-prediction-model.md` | A/E | 正文已声明被 `yt-foresight-model-taxonomy` 替代，但 `status: enriched`，且无 `deprecation_reason`；`source_refs` 仅一张图片。 | 将 `status` 改为 `deprecated` 或 `superseded`，添加 `superseded_by` 与 `deprecation_reason`；降低 confidence 或归档。 |
| 18 | `C:\Users\Administrator\Desktop\wiki\30_wiki\cases\case-five-step-growth-first-lever.md` | C/E | 三个“跨越路径”均为匿名原型（“一堂早期”、“某 SaaS 工具”、“某知识付费产品”），LTV/CAC 变化等核心数据无来源引用，无法验证 outcome。 | 为每个案例补充来源（课程案例原文、企业财报、公开报道），或明确标注为“教学匿名案例，数据为示意”；添加“可验证结果”小节。 |
| 19 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-unit-model.md` | A/C | `source_refs` 仅通用课程地图串讲；Bill Aulet 批判段落被截断为 “…” 未完成；正文课程介绍化。 | 补充单元模型课程原文；补全 Bill Aulet 批判；删减 boilerplate。 |
| 20 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-entrepreneur-truth-seeking.md` | A/C/D/F | `source_refs` 仅通用课程地图串讲；正文课程介绍化；`type: tool` 与课程卡/框架卡定位不符。 | 补充实事求是课程原文；增加红队/蓝队操作模板，或改 `type` 为 `framework`。 |
| 21 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-research-weaponry-course.md` | A/B/D/E | `source_refs` 仅 src ID 无路径映射；`type: concept` 但正文是方法论/技能内容；与 `yt-entrepreneur-research-camp` 存在重叠；缺少 `confidence`。 | 映射 src ID 到 `10_raw/sources/...`；将 `type` 改为 `skill` 或 `tool`；与调研行动营卡明确分工；补充 `confidence`。 |
| 22 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-industry-canvas.md` | A/B/C | `source_refs` 仅 PNG 图片；出现两个重复“不要用的场景”表格；缺少行业画布应用示例。 | 补充来源；删除重复段落；增加一个行业（如咖啡、SaaS）的完整画布示例。 |
| 23 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\互联网医院模式深度调研报告.md` | A/B/C/F | `source_refs` 仅一个 src ID 且无路径映射；缺少 `confidence`；`type: concept` 与“深度调研报告”属性不符；出现重复 Taleb/Simon 批判段落；核心数据（3756 家、4190 亿元等）未在 source_refs 中体现。 | 映射 src ID；将 `type` 改为 `report` 或 `case`；补充政策文件/企业财报来源；添加 `confidence`；删除重复批判段落。 |
| 24 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-system-course-map-lecture.md` | A/B/F | `source_refs` 为空字符串；`id` 值异常（包含 src ID）；缺少 `confidence`；`status: reviewed` 但无 trust_level。 | 添加课程地图串讲原文来源；修正 `id`；补充 `confidence` 与 `trust_level`。 |
| 25 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-execution-business-modeling.md` | A/B/C | `source_refs` 仅 PNG 图片；出现两个重复“不要用的场景”表格；缺少业务公式拆解示例。 | 补充来源；删除重复段落；增加一个真实业务的公式拆解示例。 |
| 26 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\skill-马易-业务为先的AI中台建设.md` | A/C | `source_refs` 为空；confidence 0.85 缺乏来源支撑；示例（电商评论分类）为通用示意，未说明是否真实案例。 | 添加马易原始课程/分享来源；如示例为虚构，标注“示意案例”；补充真实失败案例。 |
| 27 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-business-spectrum.md` | B | YAML `tags`/`pipeline` 含 `null`；`id` 未加引号。 | 清理 null 字段；规范 `id` 格式。 |
| 28 | `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-foresight-deliverables-four-levels.md` | D/C | `type: concept` 但正文是“交付物四层级”框架；关键数据“L1 成功率<10%，L4 翻 3 倍”无来源。 | 改 `type` 为 `framework`；为成功率数据补充来源或标注为经验估算。 |

### 3.2 未发现明显问题的卡片

以下 12 张卡片在来源、结构、类型、confidence 一致性等方面相对完整，建议保持当前质量并持续维护：

- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\concept-five-step-growth-to-barrier-transition.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-personal-pitch-toolkit.md`（Action Triggers 表格首列格式可微调）
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-muse-ai-framework.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-emotionalization.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-scenarization.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-agent-architecture.md`（来源为 AI 思维卡二次加工，建议未来补 AIMA 原书来源）
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-panproduct-demand-motivation-resistance.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-pitch-conflict.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-tool-foresight-canvas.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-personal-y-model-practice.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-dual-triangle-competitiveness.md`
- `C:\Users\Administrator\Desktop\wiki\30_wiki\concepts\yt-model-ipo-learning-strategy.md`

---

## 4. 批量处理建议

### 4.1 可通过脚本/规则批量处理（低人工判断）

| 批量任务 | 处理规则 | 预期效果 |
|---|---|---|
| **清理 YAML 重复键** | 检测同一 frontmatter 中重复出现的 `updated_at`、`不要用的场景`、Taleb/Simon 批判等键/段落，保留最后一个或合并。 | 消除 6 张以上卡片的模板重复与重复键。 |
| **规范化 null 字段** | 将 `tags`、`pipeline`、`related` 中的 `null` 值统一清空或删除；修复 `id` 未加引号、字段名拼写错误（`review_by` → `review_date`）。 | 修复约 10 张卡片的元数据质量。 |
| **Source 空值/弱来源标记** | 自动列出 `source_refs` 为空、仅含 `一堂-课程地图精华串讲.md`、仅含 PNG/JPG、仅含 src ID 的卡片，生成待补源清单。 | 快速定位 24 张 Source 薄弱卡片。 |
| **类型不一致标记** | 根据正文标题与结构启发式匹配（如标题含“技能”“Skill”但 `type: concept`，或含“画布”“模型”但 `type: tool`），输出待人工复核列表。 | 辅助发现 8 张类型标注异常卡片。 |
| **缺失 confidence/trust_level 检测** | 扫描 frontmatter 中缺失 `confidence` 或 `trust_level` 的卡片。 | 发现 6 张以上需补充的卡片。 |

### 4.2 必须由人工判断处理

| 任务 | 原因 | 建议操作 |
|---|---|---|
| **为课程衍生卡片补具体来源** | 需要判断每张卡片真正对应哪一门课程/讲义/口述稿，无法仅凭文件名推断。 | 建立“课程名 → 原始文件路径”映射表，由熟悉一堂课程体系的同学逐张核对并替换 `source_refs`。 |
| **合并或拆分重叠卡片** | `yt-research-weaponry-course` 与 `yt-entrepreneur-research-camp` 内容重叠但角度不同，需人工决定是合并、保留双卡还是重定向。 | 由领域负责人明确两张卡的分工，必要时在 Synthesis 中互指并统一口径。 |
| **处理已替代卡片** | `yt-model-prediction-model` 已被新版替代，是否归档、重定向或保留历史版本需人工决策。 | 更新 `status` 为 `deprecated`，添加 `superseded_by`，并在相关卡片中移除指向旧版的推荐链接。 |
| **案例数据验证** | `case-five-step-growth-first-lever` 等匿名案例的数据需要核对原始课程或公开资料，判断是否可公开引用。 | 人工补充来源，或改为“教学示意案例”并降低 confidence。 |
| **类型重分类** | 大量 `tool`/`concept` 边界模糊，需要结合内容深度与使用场景判断。 | 由内容负责人逐张裁定，优先保持同主题卡片类型一致（如“讲香十指”子卡统一为 `tool`，“画布/模型”统一为 `framework`）。 |
| **补全截断/缺失批判** | `yt-entrepreneur-unit-model` 中 Bill Aulet 批判被截断，需要人工补写。 | 由熟悉对应学者观点的同学补全并标注来源。 |
| **制定 Source 映射规范** | src ID（如 `src_20260501_9962715b`）与文件路径的对应关系需要规范化。 | 建立 src ID → `10_raw/sources/<filename>` 的索引脚本，并在 future cards 中统一使用可解析路径。 |

---

## 5. 优先级建议

1. **P0（立即）**：修复 YAML 结构损坏（紫鲸AI）、空 source_refs（PaddleOCR、graph-rag、system-course-map-lecture、skill-马易）、已替代卡片状态（prediction-model）。这些问题影响卡片解析与可信度。  
2. **P1（本周）**：为 24 张 Source 薄弱卡片建立补源清单，优先补齐课程地图串讲衍生的 7 张核心卡片（五步法、业务增长、壁垒、单元模型、实事求是、AI 能力、泛产品设计）。  
3. **P2（本月）**：清理模板重复段落、规范化 null 字段、统一类型标注、处理重叠关系。  
4. **P3（持续）**：建立“新增卡片 Source 与 confidence 自检清单”，避免同类问题在新入库卡片中复发。

---

*报告结束。*
