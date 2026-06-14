# Stage 3 作者深度审查报告：老顽童 · AI 短剧系列

**审查日期**：2026-06-14  
**审查样本清单**：`C:/Users/Administrator/Desktop/wiki/60_feedback/audit/.stage3-tmp/laowantong-ai-short-drama.txt`  
**审查人**：知识库质量审查员（自动审查）  
**审查范围**：老顽童创作的 AI 短剧方法论卡片，覆盖「冰火写本/拆本罗盘」及 4 把「三板斧」工具 + 1 张平台政策对比概念卡。

---

## 1. 审查样本数

| 序号 | 文件路径 | 类型 |
|------|----------|------|
| 1 | `30_wiki/concepts/ai-short-drama-ice-fire-scripting-compass.md` | concept |
| 2 | `30_wiki/concepts/ai-short-drama-platform-policy-comparison.md` | concept |
| 3 | `30_wiki/frameworks/ai-short-drama-ice-fire-dissection-compass.md` | framework |
| 4 | `30_wiki/tools/ai-short-drama-conflict-three-axes.md` | tool |
| 5 | `30_wiki/tools/ai-short-drama-framework-three-axes.md` | tool |
| 6 | `30_wiki/tools/ai-short-drama-plot-three-axes.md` | tool |
| 7 | `30_wiki/tools/ai-short-drama-script-planning-three-axes.md` | tool |

**合计：7 张卡片**（2 concept、1 framework、4 tool）。

---

## 2. 问题分类统计

| 问题维度 | 问题数 | 占比 | 严重程度 |
|----------|--------|------|----------|
| 内容完整性 | 2 | 22% | 中 |
| Source 可验证性 | 3 | 33% | 中 |
| Confidence / Trust 一致性 | 2 | 22% | 低 |
| 与其他卡片关系 | 1 | 11% | 低 |
| 类型特定检查 | 2 | 22% | 中 |
| **总计** | **10** | — | — |

> 注：单张卡片可能涉及多个问题维度，故问题数合计大于卡片数。

---

## 3. 总体质量评估

本批次卡片整体质量**良好**，呈现出较强的方法论体系感：

- **体系闭环完整**：「写本罗盘 → 拆本罗盘 → 4 把三板斧」形成从正向创作、逆向拆解到专项工具的完整链路，`related` 关联清晰。
- **工具卡规范度高**：4 张 tool 卡均包含 Purpose、Protocol、AI 使用方式、When NOT to Use、Constraints、Action Triggers，符合工具卡交付标准。
- **自我批判意识强**：多数卡片包含 [Critique] 章节，主动指出模板化、同质化、AI 边界等风险，增强可信度。
- **主要短板集中在「平台政策对比卡」**：该卡名为「政策对比」，但缺少可落地的具体政策数据（分成比例、投稿入口、结算周期等），更像「对比表的元描述」，内容完整性和可验证性明显弱于同批次其他卡片。

---

## 4. 具体卡片问题清单

### 4.1 `concepts/ai-short-drama-ice-fire-scripting-compass.md`

**状态**：整体无明显问题， minor issue。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | Action Triggers 中提到「用 5 分钟填写『剧本基地』七要素」，但本卡未完整列出这七要素（仅在触发场景中零散出现 6 个，缺少「核心欲望/核心阻碍」的明确对应），读者若不跳转到 `script-planning-three-axes` 会缺字段。 | 在当前卡片的 Action Triggers 或 Constraints 中补一个「剧本基地七要素」内联清单，或明确链接到 `script-planning-three-axes` 的七要素表格。 |
| Source 可验证性 | C5 商业化验证数据（30+ 本、签约 2 本、创作时间压缩到 10 分钟初稿）有具体行号引用（`transcript.md:605-613`），可验证性高；但 C1-C4 部分核心公式/五维拆分的引用同时依赖图片 source 和口述 transcript，未给出每一维对应的精确行号。 | 如 transcript 中有分维度讲解位置，建议补充到具体行号，减少跨 source 推断。 |
| Confidence / Trust | 卡片 confidence=0.75，trust_level=medium；内部 claims 为 0.75-0.9，分布合理。C6 市场数据（1000 亿/12.8 万部/95% AI 辅助）置信 0.75 与来源为单一口述一致，无明显不一致。 | 无需调整。 |
| 卡片关系 | 与拆本罗盘、4 把三板斧均有 `related` 链接；顶层 overview 与下层工具分工清晰。 | 无需调整。 |
| 类型特定检查（concept） | 定义清晰（同心圆五维），有 visual analysis、claims、boundaries、critique、synthesis，概念卡要素完整。 | 无明显问题。 |

### 4.2 `concepts/ai-short-drama-platform-policy-comparison.md`

**状态**：**问题最突出**的一张卡，内容深度和可验证性均不足。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | 卡片标题为「主流短剧平台政策对比：抖音/红果/快手/腾讯/爱奇艺/优酷/芒果」，但正文**未呈现原始对比表的具体数据**（投稿入口、分成比例/分账比例、结算周期、最低集数、审核周期、新人扶持细则等），仅描述「原图为表格形式，横向五列、纵向七行」。读者无法基于本文做出平台选择决策。 | 必须在正文中嵌入原始对比表的核心数据（至少包含：平台、投稿方式、分成/分账模式、题材偏好、新人友好度的具体等级/星级）。如原始素材已 OCR，应把表格内容摘录到卡片 Reusable Knowledge 或新增「平台政策对比表」章节。 |
| 内容完整性 | Reusable Knowledge 中的决策规则（如「女频甜宠→优先抖音/红果」）虽然可操作，但**缺少数据支撑**，未说明这些规则来自表格哪一单元格或演讲者哪一句原话，容易变成经验断言。 | 为每条决策规则追加 source 标注（图片单元格位置或 transcript 行号）。 |
| Source 可验证性 | C1-C3 的平台-题材匹配断言引用的是 `src_20260613_500dbed8-platform-policy-comparison.md:11-14`，但卡片本身没有展示该表格内容，导致读者**无法在当前卡片内验证**断言是否忠实于原表。 | 在 Sources 或正文中补充归档后表格的摘要/转录，使 source 与断言在同一卡片内可对照。 |
| Source 可验证性 | C5「平台政策变化快，需每季度复核」、C6「可转化为 AI prompt 模板」引用了笔记 source，但 C5 明确标注为「推断」，这是诚实的；C6 与 `notes.md:128-133` 的对应关系较合理。 | C5 已是推断，保持当前 confidence=0.75 即可。 |
| Confidence / Trust | 卡片 confidence=0.75、trust_level=medium。考虑到该卡大量依赖单一图片 source 且未在卡片内转录表格，实际可验证性低于同批次其他卡片，0.75 略显偏高；建议调整为 **0.65-0.70** 或 trust_level 降为 low。 | 在补齐表格数据前，将 confidence 下调至 0.65-0.70，或增加 `verification_status: partial` 标识。 |
| 类型特定检查（concept） | 作为 concept 卡，定义是「平台政策对比知识」，但缺乏清晰的概念边界、反例和与其他概念的区别；Open Questions 写得较好，弥补了部分不足。 | 在补齐数据后，补充「什么情况下本表不适用」的边界说明（已有一点，可再细化到具体平台类型）。 |

### 4.3 `frameworks/ai-short-drama-ice-fire-dissection-compass.md`

**状态**：整体无明显问题， minor issue。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | [Critique] 已指出「缺少量化指标，钩子密度没有给出参考值」。这是一个真实的内容缺口，但卡片已通过 self-critique 披露，读者可知。 | 如原培训材料或笔记中有「每集 X 个钩子/每分钟 Y 次转折」的参考值，建议补充到 Protocol 或 Constraints；如无，可在 Critique 中保留该条并标注「待补充」。 |
| Source 可验证性 | C1-C6 的 claims 均未给出具体行号，仅列出 source ID。相比写本罗盘，拆本罗盘的断言更偏向方法论提炼，line-level 引用难度更大，但「文本语言」「钩子密度」等维度在 transcript 中应有对应讲解。 | 尽量为 C1-C6 补充 transcript 行号；如确实无法定位，可在 Claims 中标注「方法论归纳，source 为整体培训材料」。 |
| Confidence / Trust | confidence=0.75，claims 0.75-0.9，与内容质量匹配；框架卡以结构化清单为主，无过度自信。 | 无需调整。 |
| 卡片关系 | 与写本罗盘形成「拆本↔写本」闭环，与 plot/script-planning 等工具卡关联清晰。 | 无需调整。 |
| 类型特定检查（framework） | 有适用范围、五维操作清单、案例场景（拆本动作），符合 framework 卡要求。 | 无明显问题。 |

### 4.4 `tools/ai-short-drama-conflict-three-axes.md`

**状态**：无明显问题。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | Protocol 三步均有明确动作、检查项和示例；AI prompt 可直接复制使用。 | 无明显问题。 |
| Source 可验证性 | 引用 `transcript.md:2125` 和 `notes.md:98-114`，有具体位置。 | 无明显问题。 |
| Confidence / Trust | confidence=0.75，claims 0.75-0.9，合理。 | 无需调整。 |
| 类型特定检查（tool） | 有使用步骤、边界条件、When NOT to Use、示例 prompt，符合 tool 卡要求。 | 无明显问题。 |

### 4.5 `tools/ai-short-drama-framework-three-axes.md`

**状态**：整体无明显问题， minor issue。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | C2（1-3 集完成入局）、C3（中间 60%-70% 集数）等断言未在 Claims 中给出具体 source 行号，仅列出 source ID。 | 补充 transcript 或 notes 中的对应行号，尤其「1-3 集」「60%-70%」这类量化结论。 |
| 内容完整性 | Visual Analysis 提到每栏有英文标注（Essential Information of Situation / Step Information Iteration / Station Conclusion Elevation），这些英文疑似 OCR 误读或原图 Chinglish，本卡未做说明。 | 在 Visual Analysis 或 Critique 中增加一句说明：英文标注疑似原图 OCR 误差/非标准表达，不影响中文方法论理解。 |
| Source 可验证性 | 与 script-planning 工具卡共用部分英文标注（如 Essential Information of Situation），说明原图设计存在一致性问题，需在审查中披露。 | 同上，增加说明即可。 |
| 类型特定检查（tool） | 有 protocol、prompt、when not to use、constraints、action triggers，案例示例清晰。 | 无明显问题。 |

### 4.6 `tools/ai-short-drama-plot-three-axes.md`

**状态**：无明显问题。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | Protocol 三步均有 checklist；AI prompt 完整；When NOT to Use 覆盖 4 个典型失效场景。 | 无明显问题。 |
| Source 可验证性 | 引用 `transcript.md:1989` 和 `notes.md:25-46`，位置明确。 | 无明显问题。 |
| Confidence / Trust | confidence=0.75，claims 0.75-0.9，合理。C5「三斧有先后顺序」略显绝对，但已作为方法论主张提出，confidence=0.8 合适。 | 无需调整。 |
| 类型特定检查（tool） | 完全符合 tool 卡要求。 | 无明显问题。 |

### 4.7 `tools/ai-short-drama-script-planning-three-axes.md`

**状态**：整体无明显问题， minor issue。

| 维度 | 问题描述 | 处理建议 |
|------|----------|----------|
| 内容完整性 | 七要素表格完整且有示例；Protocol 三步清晰。 | 无明显问题。 |
| 内容完整性 | [Critique] 已指出英文标注存在 OCR 错误和疑似乱码，这是有价值的自我披露。 | 可在 Visual Analysis 中也简要提示，帮助读者理解英文标注不可靠。 |
| Source 可验证性 | C1-C6 的 claims 大多未给出精确行号，仅列 source ID；其中 C2（七要素）和 C3（10-15 节点）是卡片核心，建议补充 source。 | 为七要素、10-15 节点、分阶段投喂等关键结论补充 transcript/notes 行号。 |
| 类型特定检查（tool） | 有适用范围、操作步骤、示例表格、prompt、边界条件，符合 tool 卡要求。 | 无明显问题。 |

---

## 5. 卡片间关系专项审查

| 检查项 | 结论 | 说明 |
|--------|------|------|
| 重复内容 | 未发现严重重复 | 顶层罗盘与下层工具存在自然的层级覆盖（overview vs. detail），不属于冗余。 |
| 概念/术语一致性 | 基本一致 | 「剧本基地七要素」在 `script-planning-three-axes` 中完整定义，`ice-fire-scripting-compass` 的 Action Trigger 中零散引用，建议补齐或显式链接。 |
| 数据/断言一致性 | 基本一致 | 「内容走向 15 个关键节点」在写本罗盘诊断信号、`script-planning` 的 10-15 节点范围内，无冲突。 |
| 过时风险 | 中 | `platform-policy-comparison` 政策时效性已在 Constraints 中披露，但卡片本身数据缺失，未来更新时难以 diff。 |
| 关联完整性 | 良好 | 所有卡片均通过 frontmatter `related` 建立双向/多向链接，形成方法网络。 |

---

## 6. 批量处理建议

### 6.1 可脚本化批量修复

| 批量任务 | 实现方式 | 优先级 |
|----------|----------|--------|
| 统一 source_refs 格式 | 检查所有卡片 `source_refs` 是否仅含 ID、是否缺少行号；对 tool/framework 卡批量提示补行号。 | 中 |
| 校验 `related` 链接完整性 | 脚本检查 7 张卡片的 `related` 是否互链，发现单向链接时自动提示补双向链接。 | 低 |
| 标准化 confidence 范围 | 对「主要依赖单一图片 source 且未在卡片内转录」的卡片（如 platform-policy-comparison）批量调低 confidence 或增加 `verification_status: partial`。 | 中 |
| 检查英文标注/OCR 误差披露 | 脚本扫描 Visual Analysis 中的英文标注，对疑似乱码/OCR 误差的卡片批量添加提示语。 | 低 |

### 6.2 必须人工判断处理

| 人工任务 | 原因 | 优先级 |
|----------|------|--------|
| 补全 `platform-policy-comparison` 平台政策对比表 | 需要从原始图片/OCR/归档 source 中提取具体数据（分成比例、投稿方式、题材偏好细则等），无法由脚本生成。 | **高** |
| 为拆本罗盘、框架三板斧、剧本策划三板斧的核心 claims 补充 transcript 行号 | 需要人工回听/回读原始材料，定位「1-3 集」「60%-70%」「10-15 节点」等具体出处。 | 中 |
| 评估并调整 `platform-policy-comparison` 的 confidence/trust_level | 需要人工判断「未转录表格」对可验证性的影响程度，决定下调至 0.65 还是 0.70，或标记为 low trust。 | 中 |
| 决定是否将「剧本基地七要素」内联到写本罗盘 | 涉及卡片内容架构选择：是重复清单还是仅加链接，需要人工决策。 | 低 |
| 验证 C6 市场数据（1000 亿/12.8 万部/95% AI 辅助） | 单一口述来源的强数据声明，建议人工核对 transcript 上下文及是否有其他独立来源 corroborate。 | 中 |

---

## 7. 审查结论

- **通过但需修订**：`ice-fire-scripting-compass`、`ice-fire-dissection-compass`、`conflict-three-axes`、`framework-three-axes`、`plot-three-axes`、`script-planning-three-axes` 共 6 张卡片质量达标，仅需 minor 补充（source 行号、OCR 说明、少量内联链接）。
- **需显著返工**：`platform-policy-comparison` 1 张卡片，必须补全具体平台政策对比数据后才能视为合格的概念卡；在此之前建议降低 confidence 并标注 `verification_status: partial`。

**整体建议**：优先处理 `platform-policy-comparison` 的数据补全，其次统一补充 tool/framework 卡中核心 claims 的精确 source 行号，以提升全库的可验证性和可信度。
