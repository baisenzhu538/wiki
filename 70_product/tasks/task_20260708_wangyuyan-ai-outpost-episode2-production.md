---
id: task_20260708_wangyuyan-ai-outpost-episode2-production
type: task
status: in_progress
owner: 王语嫣
assignee: kimi-code
reviewer: 欧阳锋
priority: P1
created_at: 2026-07-08
updated_at: '2026-07-08'
estimated_cards: 8
dependencies: []
source_diagnosis: 60_feedback/diagnosis/diag_20260708_ai-outpost-episode2-nine-layer.md
---

# AI前哨站第2集卡片化：8 张卡（4 P0 + 4 P1）

> 来源：`00_inbox/AI前哨站第2集`（口述稿 + 笔记 + 拆书稿）
> 诊断：`60_feedback/diagnosis/diag_20260708_ai-outpost-episode2-nine-layer.md`
> 目标：把「AI前哨站第二期」关于 AI 原生组织、Token Capital、品味系统、Builder 幻觉等前沿观点沉淀为 KDO 卡片，并与现有 AI 原生组织、人在环、双三角竞争力等卡片桥接。

---

## 一、任务目标

1. 生产 4 张 P0 骨架卡：
   - `framework-ai-native-organization-two-modes`（AI控制台 vs Agent平台）
   - `concept-token-capital`（Token Capital）
   - `framework-taste-as-judgment-system`（品味系统）
   - `dk-ai-builder-illusion`（Builder 幻觉）
2. 生产 4 张 P1 工具/案例/agent-spec 卡：
   - `concept-jevons-paradox-in-ai`（杰文斯悖论在 AI 时代）
   - `tool-open-closed-problem-classifier`（开放/封闭问题分类器）
   - `case-ai-search-commerce-platform-hedge`（AI 搜索不会取代平台）
   - `agent-spec-codex-teammate`（Codex 队友式使用规范）
3. 反向更新 14 张已有相关卡的 `related` 字段。
4. 所有数据必须标注 `[确认]`/`[假设]`/`[空白]`。

---

## 二、source_refs（必须写入目标卡 frontmatter）

### 内部素材

- `00_inbox/AI前哨站第2集/水水-AI前哨-第二期-口述.txt`
- `00_inbox/AI前哨站第2集/水水-AI前哨-第二期-笔记.txt`（注意：笔记中的马斯洛需求层次、技术接受模型、第一性原理等理论关联为笔记作者二次加工，原始口述稿与拆书稿均未出现，只能作为 `[假设]` 或外部拓展，不能作为核心 claim 的强证据）
- `00_inbox/AI前哨站第2集/AI前哨站第2集-水水拆书.md`

### 关键外部来源

- `https://www.lennysnewsletter.com/p/openai-codex-lead-on-the-new-shape`（Andrew Ambrosino）
- `https://openai.com/index/how-agents-are-transforming-work/`（OpenAI）
- `https://www.anthropic.com/research/claude-code-expertise`（Anthropic）
- `https://www.possible.fm/podcasts/satya-nadella-on-making-human-and-token-capital-compound`（Satya Nadella）
- `https://addyo.substack.com/p/loop-engineering`（Addy Osmani）
- `https://www.lennysnewsletter.com/p/father-of-the-ipod-and-iphone-on`（Tony Fadell）
- `https://www.ycombinator.com/library/Qh-inside-yc-s-ai-playbook`（Pete Koomen）
- `https://developers.openai.com/codex/learn/best-practices`（OpenAI Codex）
- `https://www.notion.com/blog/steam-steel-and-infinite-minds-ai`（Ivan Zhao）
- `https://a16z.com/podcasts/ben-marc/`（Andreessen & Horowitz）
- `https://stratechery.com/`（Michael Morton / Ben Thompson，付费墙）

---

## 三、卡片生产清单

| 序号 | 卡片 ID | 类型 | 标题 | 核心内容 | 质量要求 |
|------|---------|------|------|----------|----------|
| 1 | `framework-ai-native-organization-two-modes` | framework | AI原生组织的两种形态：AI控制台 vs Agent平台 | 开放问题 vs 封闭问题；AI 控制台（人驱动、保护心流）vs Agent 平台（AI 驱动、工业化）；切换信号、失败模式 | 必须区分两种形态的进入/退出标准；含 When NOT to Use |
| 2 | `concept-token-capital` | concept | Token Capital：AI时代的第三种资本结构 | 人力资本、数字资产、token capital 三元结构；定义、积累路径、治理原则、与 token 效价工具的关系 | 含外部攻击：token capital 是否会被模型厂商稀释？ |
| 3 | `framework-taste-as-judgment-system` | framework | 品味系统：判断力×审美×系统思维 | taste 五维（判断力、审美、系统思维、方向感、表达/交互）；训练路径；与 AI 生成能力的关系 | 必须与 `concept-AI时代双三角竞争力` 互链；把口述稿 L1-L107「高客单/奢侈品用户洞察」作为品味重要性的教学案例/论据写入（美式台球 vs 斯诺克、奢侈品毫无用处才显洞察）；与 `dk-wanghuan-creativity-in-description-and-taste` 弱引用 |
| 4 | `dk-ai-builder-illusion` | dk | Builder幻觉：用AI做出东西≠完成从0到1 | 现象、根因、反向信号、Action Triggers；与「做出来不是从0到1」「fast fashion 软件/速生速朽」的关联 | 必须包含至少 3 个真实失败信号； Tony Fadell 的 fast fashion software 论断作为根因/结果段落并入，不单独建卡 |
| 5 | `concept-jevons-paradox-in-ai` | concept | 杰文斯悖论在AI时代 | 成本下降→需求爆发；AI 让原本不敢提的问题被提出；与「降本增效尽头是价格战」的关系 | 含历史案例（煤炭/蒸汽机）和 AI 案例 |
| 6 | `tool-open-closed-problem-classifier` | tool | 开放/封闭问题分类器 | 5-7 个判别问题 + 决策树 + 推荐形态（AI 控制台/Agent 平台/混合） | 可直接调用；含失败模式（把开放问题硬塞给 Agent 平台） |
| 7 | `case-ai-search-commerce-platform-hedge` | case | AI搜索导流品牌官网，但不会取代电商平台 | 4-8 倍增速、平台履约能力护城河、购物即娱乐、Amazon Subscribe & Save 1-3% | 数据必须标注 `[确认]`/`[假设]`；含失败模式（效率叙事忽视消费动机） |
| 8 | `agent-spec-codex-teammate` | agent-spec | Codex队友式使用规范 | 提示词四要素、AGENTS.md、Plan 模式、技能 vs 自动化、会话管理、常见错误 | TCPR 默认 **P（Practice）**；含 System Prompt、输入门、输出门、Few-shot |

---

## 四、反向更新已有卡片清单

以下卡片需在生产完成后追加 `related` 回链（注意：当前为 draft/pending 的卡只做弱引用，不依赖其内容）：

- `concept-ai-native-organization-five-steps`
- `concept-yihang-human-in-the-loop-dual-triangle`
- `concept-AI时代双三角竞争力`
- `dk-wanghuan-creativity-in-description-and-taste`（⚠️ 与本卡主题高度重叠，边界见「王语嫣拍板事项」第 4 条）
- `framework-yihang-aesthetic-judgment-training`（⚠️ 当前 status: draft / reviewed_by: pending，只做弱引用，不依赖其内容）
- `tool-月白-Token效价比决策法`
- `tool-月白-Token智甲比控制法`
- `framework-founder-ip-three-positioning`
- `prd-as-ai-instruction`
- `sk-ai-prd-for-ai`
- `tool-Truman-人在环渐进自动化策略`
- `yt-decision-y-model`
- `framework-yitang-y-model-dual-triangle-synergy`
- `concept-yitang-ai-research-human-loop`

---

## 五、「Codex队友式使用规范」agent-spec 规格

### 5.1 一句话定义

一个把 OpenAI Codex 当作「需要持续配置和改进的队友」来使用的实践型 Agent。默认以 P（Practice）身份输出可执行动作：读 AGENTS.md、写提示词四要素、规划任务、运行测试、更新规范。

### 5.2 默认 TCPR 身份

- `tcp_role: P`（Practice/实践）
- `tcp_default_mode: Codex 队友式协作教练`
- `tcp_switch_trigger`：
  - 用户问「为什么」「怎么做」→ 切换为 **T（教学）**
  - 用户只给模糊需求 → 切换为 **C（咨询）**，先诊断
  - 用户要求复盘/评估长期效果 → 切换为 **R（研究/复盘）**

### 5.3 输入门

| 输入类型 | 字段 | 必需 | 缺失时行为 |
|----------|------|------|------------|
| 任务一句话描述 | task_summary | 是 | 无法进入下一步 |
| 代码库/项目路径 | repo_path | 否 | 标注为「待确认」 |
| 现有 AGENTS.md / 规范 | agents_md | 否 | 提示用户先创建或读取 |
| 约束条件（架构/标准） | constraints | 否 | 标注为「待确认」 |
| 完成标志 | done_criteria | 否 | 帮助用户定义 |

### 5.4 输出门（P 模式）

每次对话结束必须输出：

1. **当前动作清单**：who / what / when / 依赖。
2. **提示词四要素草稿**：目标、上下文、约束、完成标志。
3. **AGENTS.md 更新建议**：哪些规则应写入持久规范，哪些应留在单次提示词。
4. **技能 vs 自动化判断**：当前工作流应做成 Skill 还是 Automation。
5. **待确认项清单**：所有标注为「待确认」的输入。
6. **风险摘要**：最高 3 个风险 + 建议动作。

### 5.5 反幻觉规则

- 不假设代码库结构；必须读取 AGENTS.md 或询问。
- 所有外部数据必须标注 `[确认]`/`[假设]`/`[空白]`。
- 不推荐用户直接全自动化；必须强调验证仍是人的责任。
- 当用户输入不足时，追问而非编造。

### 5.6 System Prompt 核心规则

```markdown
# Role
你是「Codex 队友式协作教练」，帮用户把 Codex 从一次性助手变成持续改进的队友。

## TCPR 身份
默认 P（Practice/实践）身份：直接输出动作和可执行规范。
若用户问方法论，切换为 T；若信息不足，切换为 C；若要求复盘，切换为 R。

## 核心工作流
1. 读取 AGENTS.md / 项目规范 → 2. 明确任务四要素 → 3. 判断 Skill vs Automation → 4. 输出动作清单 → 5. 运行/验证 → 6. 更新规范

## 输出原则
- 每次输出必须包含「下一步动作清单」。
- 所有建议必须标注置信度：确认 / 假设 / 空白。
- 关键合并/部署节点需要用户确认。
- 强调：验证仍是人的责任，loop 无人值守犯错也无人值守。

## 常见错误提醒
- 不要把持久规则堆进提示词。
- 不要像监工一样盯着 Codex 一步步执行，让它并行工作。
- 不要一个线程对应一个项目，导致上下文膨胀。
```

### 5.7 Few-shot 示例要求

至少 3 个示例：

1. **新增功能**：用户提供任务描述 → Agent 输出四要素 + AGENTS.md 更新建议 + 动作清单。
2. **调试 bug**：用户提供报错 → Agent 输出排查计划 + 测试命令 + 回归检查清单。
3. **建立自动化工作流**：用户提供重复任务 → Agent 输出 Skill 版本 + Automation 触发条件 + 验证周期。

---

## 六、生产顺序建议

1. **第一批**：`tool-open-closed-problem-classifier`（先定义分类器，后续卡引用它）
2. **第二批**：`framework-ai-native-organization-two-modes`（基于分类器展开双形态）
3. **第三批**：`concept-token-capital` + `framework-taste-as-judgment-system`
4. **第四批**：`dk-ai-builder-illusion` + `concept-jevons-paradox-in-ai`
5. **第五批**：`case-ai-search-commerce-platform-hedge`
6. **第六批**：`agent-spec-codex-teammate`（信息最充分，放最后收尾）
7. **第七批**：反向更新 14 张已有卡片 related

---

## 七、验收标准

1. 8 张目标卡全部 `kdo pre-submit` PASS。
2. 所有新卡 `related ≥ 7`；framework/agent-spec `related ≥ 10`。
3. 14 张已有卡完成反向 related 更新，无新增死链。
4. 所有数据标注 `[确认]`/`[假设]`/`[空白]`；来源不明数据不得作为强证据。具体规则：
   - OpenAI/Anthropic 等已外部验证的数据：标 `[确认]` 并附来源 URL。
   - 拆书稿/口述稿中「2026 年 6 月」等近未来日期：以原始发布日期为准，标 `[确认]`。
   - 「雷军为小米省 300 亿营销成本」等无来源口述数据：不得作为强证据；如必须提及，标 `[空白]` 并注明「讲师估算，无来源」。
5. 「闲庭落木」来源若无法确认，不得作为强证据，只能标注为「待验证观点」。
6. agent-spec 必须包含 System Prompt、输入门、输出门、TCPR 身份、Few-shot、迭代日志、风险与边界。
7. 全量产出通过欧阳锋终审。

---

## 八、风险与阻塞

| 风险 | 影响 | 应对 |
|------|------|------|
| 口述稿重复导致卡片冗余 | 内容重复 | 以拆书稿为纲，口述稿仅作案例/引语补充 |
| 「Cubox」口误混入生产 | 事实错误 | 统一校正为 Codex；必要时脚注说明 |
| 未来日期/数据被误当作已验证 | 可信度下降 | 所有数据标注 `[确认]`/`[假设]`/`[空白]` |
| 与现有 AI 原生组织卡重叠 | 重复造轮子 | P0 聚焦「双形态」这一差异化洞察，其余补充进已有卡 |
| 闲庭落木来源无法确认 | 影响开放/封闭问题框架的外部背书 | 如无法确认，改为「业内观察」并降低置信度 |

---

## 九、王语嫣拍板事项（已确认）

针对老顽童开工前对齐问题，统一答复如下：

| # | 问题 | 王语嫣决定 |
|---|------|-----------|
| 1 | 高客单/奢侈品片段是否入队？ | **方案 B**：并入 `framework-taste-as-judgment-system`，作为「品味为何重要」的教学案例/论据（口述稿 L1-L107：美式台球 vs 斯诺克、奢侈品毫无用处才显洞察）。不单独建卡，避免本期膨胀。 |
| 2 | P2 卡片是否本次生产？ | **方案 B**：只把 `dk-fast-fashion-software` 并入 `dk-ai-builder-illusion`（作为根因/结果段落）。其余 P2（购物即娱乐、Loop Engineering 五模块、仁慈 Taste Maker）不扩展，留给后续任务。 |
| 3 | `framework-yihang-aesthetic-judgment-training` 是 draft 怎么办？ | 本任务对其只做**弱引用**，不依赖其内容；反向链接时注明目标卡为 draft。不单独推动其终审。 |
| 4 | `framework-taste-as-judgment-system` 与王欢 dk 的边界？ | 接受分工：本卡是 **Ambrosino/Codex 视角下的品味系统五维框架**（判断力/审美/系统思维/方向感/表达交互）；`dk-wanghuan-creativity-in-description-and-taste` 是 **王欢视角下的创造力重新分配暗知识**（问题描述 + 验收审美）。两者互链但不重复。 |
| 5 | 「雷军 300 亿」等无来源数据？ | **不写入任何卡片正文**；如必须作为口述引用，标 `[空白]` 并注明「讲师估算，无来源」。 |

---

## 十、产出后动作

1. 老顽童完成生产并跑 `kdo pre-submit`。
2. 将本任务状态改为 `pending_review`。
3. 欧阳锋按队列终审。
4. 终审通过后，黄药师执行 `kdo index --rebuild` 并监控 GraphRAG 桥接效果。
5. 王语嫣更新 `.agent/kb-evolution-direction.md`。
