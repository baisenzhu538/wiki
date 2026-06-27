---

id: plan_20260531_data-curator-v1.3
title: Data Curator Skill — 数据清洗+原子切分+多维标签 实施方案 v1.3
type: improvement-plan
status: draft
domain:
- src_unknown
tags:
- src_unknown
- src_unknown
source_refs:
- src_20260531_ai-data-understanding
- src_20260531_ai-data-lecture-02
- src_20260531_ai-data-lecture-03
- src_20260531_ai-data-chat
created_at: 2026-05-31
updated_at: '2026-06-16'
version: 1.3
supersedes:
- src_unknown
- src_unknown.1
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
author: unknown
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# Data Curator Skill 实施方案 v1.3

## v1.3 修正记录（2026-05-31，用户审查反馈）

| # | 问题 | 修正 |
|---|------|------|
| 1 | **"互仓"术语错误** | 更正为**"湖仓"（Data Lakehouse）**——先扔湖里（inbox），养大了再进仓（wiki）。KDO 的 `00_inbox/` 就是湖，`30_wiki/` 就是仓。 |
| 2 | **暗知识严重遗漏** | 补充暗知识专节——四类我们已经在 KDO 中积攒但从未处理的暗数据。 |
| 3 | **颗粒度假原子** | 当前 `##` heading 级切分产出的是"大块"不是"原子"。真正的原子级是单条主张/规则/事实。附 KDO 实例对比。 |
| 4 | **使用深度判断错误** | 不是"query 一下就行"——湖仓架构中，inbox 本身就是湖，问题在于什么样的素材值得从湖（inbox）提升到仓（wiki）做全链路处理。这是 A（预判）和 D（识别）要解决的。 |

---

## 版本变更记录

| 版本 | 日期 | 触发源 | 核心新增 |
|------|------|--------|---------|
| v1.0 | 05-31 | 黄药师+用户架构讨论 | 五阶段流水线、4维标签、10类chunk |
| v1.1 | 05-31 | 一堂AI数据第一课口述01（案例篇） | 查字典→食材思维、+source_type维度、+process/error chunk、ROI框架 |
| **v1.3** | 05-31 | 口述02+03+闲聊篇（方法论+体系+实操篇） | **6+1管线框架、双飞轮架构、6级成熟度模型、3层处理工序、湖仓策略、5级使用深度、清单笔记标准格式、3种反馈模式、多Agent协作、暗知识专章、真原子粒度** |

---

## Before vs After：这次四篇教给我什么

### 1. Before：我有一个清洗管线。After：我需要一个完整的价值创造管线。

| | Before (v1.1) | After (v1.3) |
|------|-------------|------------|
| **管线模型** | Audit → Clean → Tag → Chunk → Validate | **A→D→U→C→I→T + 治理**（6+1 管线框架） |
| **起点** | 从"有什么卡"开始（扫描文件） | **从"预判价值"开始**（以终为始，先想清楚数据未来怎么用） |
| **终点** | 验证通过率达标 | **闭环飞轮**：使用→反馈→回到预判→下一轮 |
| **护栏** | 无 | **治理层贯穿全程**（合规/安全/隐私/反污染） |

**A.D.U.C.I.T 框架**（一堂数据飞轮6+1）：
```
预判(Anticipate) → 识别(Detect) → 收集(Unearth) → 处理(Clean) → 使用(Implement) → 反馈(Track)
                                                                                    ↑
                                                         治理(Governance) ← 贯穿全程
```

**对应 KDO 现有管线**：
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

### 2. Before：我关注数据的结构质量。After：我需要关注数据在场景中的价值层级。

**双飞轮模型**（数据和场景互相增强）：
```
左轮：数据循环                    右轮：场景循环
预判—识别—收集—处理—使用—反馈    微观(教材) → 中观(燃料) → 宏观(护城河)
       ↑                              ↑                    ↑
  治理护栏(合规/安全)              战略护栏(使命/愿景)
```

**三层场景价值**：

| 层级 | 比喻 | 数据角色 | KDO对应 |
|------|------|---------|---------|
| **微观（Micro）** | 教材 | 单次对话的上下文参考 | 单卡 query → AI 回答 |
| **中观（Meso）** | 燃料 | 业务工作流的稳定数据供给 | 域内多卡 → AI 完成复杂任务 |
| **宏观（Macro）** | 护城河 | 公司/个人的稀缺数据资产 | 全库 → 行业级竞争优势 |

**这个框架对 KDO 的影响**：我们不应该平等对待所有卡片。应该按场景价值分层：
- src_unknown
- src_unknown
- src_unknown

### 3. Before：我有一个 5 层成熟度模型。After：我需要一个 6 层模型 + 明确的自评体系。

| L | v1.1 模型 | **v1.3 一堂6级模型** | 特征 |
|---|----------|-------------------|------|
| 1 | Raw Prompt | **没意识** | 凭手感，无存储 |
| 2 | Data Pack | **爱收集** | 存了但不处理，盲堆 |
| 3 | Extraction+Guide | **随机处理** | 时做时停，无确定性 |
| 4 | Atomic RAG | **稳定运行** | 系统自动处理，流程化 |
| 5 | Multi-DB+Router | **闭环飞轮** | 有反馈自增强 |
| 6 | — | **无限加速** | 十年视角，碾压级壁垒 |

**KDO 当前水平**：L2-L3（卡片已存储，但处理不稳定、无反馈闭环）。  
**v1.3 目标**：L4（管线稳定运行）+ 部分 L5（反馈闭环）。

### 4. Before：我只有"清洗"一个处理概念。After：处理有三道工序——粗加工、精加工、注入灵魂。

**米其林餐厅类比**：

| 工序 | 做什么 | 对应 KDO 操作 | AI 友好度 |
|------|--------|-------------|----------|
| **粗加工（洗菜）** | 转写、OCR、去重、修格式 | capture → ingest（已有） | AI 能吃了 |
| **精加工（切块装盘）** | 切片、结构化、Markdown/JSON/表格 | enrich → chunk（v1.1 新增） | AI 消化好 |
| **注入灵魂（调味）** | 标注（多维标签）+ 萃取（提炼方法论指南） | tag → 萃取指南（v1.3 新增） | AI 产出飞跃 |

**关键洞察**：我们的 tag 体系（v1.1 的 5 维标签）就是"注入灵魂"中的**标注**环节。但我们还缺**萃取**——从一组数据中提炼出一个方法论指南，统领这组数据。这对应 KDO 的三步编译法中的 **Synthesis（对标）**。

---

## 修正 2：暗知识 — 我们漏掉了什么

### 什么是暗知识

> "私有数据、暗知识和 know-how —— 不是来自于大模型内置的，来自于你们公司内部，只有你有的数据，是你得去提炼出来的东西。真正值钱的是这些东西。" —— Truman

公开的通用知识越来越不值钱。值钱的是**只有你有的、AI 没见过的、需要提炼才能用的**数据。

### 案例：月白 Design 域 — 一次暗知识系统性丢失

**我们做了什么**：月白 6 个小时的口述/分享 → 3 张概念卡（Condense/Question/Synthesize）

**我们漏掉了什么**（只按文章结构做组织编排，漏掉了大量关键数据）：

#### 漏掉类型 1：个人工作流暗知识（零捕获）

月白在口述中提到的具体工作方法，全都在 Condense 环节被过滤掉了：

| 月白实际说的 | 卡片里有吗 | 暗知识价值 |
|------------|----------|-----------|
| 用 NotebookLM 处理课程链接作为学习参考 | ❌ 完全没有 | **工具使用暗知识**：具体什么链接、为什么用 NotebookLM 而不是别的、效果如何 |
| 用 Cubox 给设计团队配工具，买回来两天就放弃 | ❌ 完全没有 | **失败暗知识**：为什么放弃？什么团队结构不适合？ |
| "很多设计师习惯特别糟糕，一个背景文件花几十个图层" | ❌ 完全没有 | **行业暗知识**：月白自己的文件组织标准是什么？为什么只留4个图层组？ |
| "我见过很多团队想用AI协作，根本用不起来" | ❌ 完全没有 | **组织暗知识**：用不起来的根因？月白观察到的模式？ |

这些是 Truman 说的"过程数据"——比结果值钱。月白不光分享了"设计三阶段"，还分享了他**怎么学会的**、**什么工具好用**、**什么团队会失败**。这些全丢了。

#### 漏掉类型 2：个人体悟/金句（无结构捕获）

| 月白说的 | 卡片里有吗 |
|---------|----------|
| "审美向外，品味向内。你的品味就是你所有过去艺术的积累。关于美这件事情的理解会化成你的品味，然后向外展现成为你的审美。" | ❌ |
| "AI强的是出选项，人才能做选择。选择需要审美策略和商业理解。" | ✅ 在 Condense 第4条 |
| "AI洪流中仍然可以听见艺术的回响" | ❌ |
| "回归基本功，知道什么时候该用、什么时候不该用。不该用比该用更重要。" | ❌ |
| "AI 质价比"这个概念 | ❌ |

6 句关键体悟，只捕获了 1 句。其余 5 句被三步编译法判定为"不够核心"而丢弃。

#### 漏掉类型 3：教学过程的元知识

月白不只是分享设计知识——他分享的**教学方法本身**就是暗知识。比如他说"15分钟学会不用PS做顶级海报"的承诺、线下6小时工坊的学员反馈、阿蕊老师和他的线上协作流程。这些对 KDO 的 delivery pipeline 有直接参考价值，全部丢失。

#### 漏掉类型 4：专家个人的学习路径

月白用 6 个月从零建立 AI 设计知识体系的过程（"去年10月才开始"→"四五个月建立完整工作流"），这是一条完整的**个人数据飞轮案例**——完全符合 A.D.U.C.I.T 框架的每一步。但我们只抽取了最终的知识卡片，丢了整条路径。

### 为什么漏了——三步编译法的结构性盲区

```
Condense → 问"核心结论是什么" → 丢掉过程、工具、体悟
Question  → 问"前提假设对不对" → 不关心"专家自己怎么想的"
Synthesize → 做概念对标 → 只对卡不对人、只对结论不对方法
```

**三步编译法的设计目标是提取稳定知识，不是捕获暗知识。** 稳定知识适合卡片化（结论、边界、关联）。暗知识需要不同的捕获格式——**操作日志、工具清单、学习路径、失败记录、个人体悟**。

### KDO 暗知识清单（已积攒但从未处理）

| 类型 | KDO 已有数据 | 位置 | 估算原子量 |
|------|------------|------|-----------|
| 专家工作流 | 月白口述稿、Truman口述稿 | `00_inbox/` | ~80个 procedure chunk |
| 工具使用暗知识 | NotebookLM用法、Cubox教训、图层管理标准 | `00_inbox/` 口述稿中 | ~30个 claim chunk |
| 纠偏过程 | corrections(12) + failure-modes(22) + pitfalls(15) | `20_memory/` + `90_control/` | ~80个 error_data chunk |
| 决策过程 | decisions.md + context.md + 审查意见 | `.agent/` + `70_product/tasks/` | ~50个 process_data chunk |
| 个人体悟/金句 | 月白"品味向内"、Truman"攒牌"等 | 散落口述稿 | ~40个 claim chunk |
| 学习路径 | 月白6个月AI设计之路 | `00_inbox/design/` | ~20个 process_data chunk |
| BA对比 | 卡片版本迭代 + git diff | 全库（从未结构化） | 未知，完全缺失 |

---

## 修正 4：双轨捕获 — 稳定知识 + 暗知识 并行

### 问题

三步编译法（Condense→Question→Synthesize）的目标是**提取稳定知识**。它天然会丢弃过程、工具、体悟、学习路径。这不是三步编译法的 bug——这是它的设计边界。

### 方案：产品轨（稳定知识）+ 过程轨（暗知识）

```
口述/分享/对话 → 原始素材
                      ├── 产品轨（已有）：三步编译法 → 概念卡 → wiki
                      │     产出：结论、边界、关联、可复用知识
                      │
                      └── 过程轨（新增）：暗知识萃取 → 暗知识卡 → wiki
                            产出：工作流、工具用法、失败记录、学习路径、个人体悟
```

### 过程轨的编译模板

不套用 Condense/Question/Synthesize，而是独立的六字段模板：

```yaml
# 暗知识卡 frontmatter
type: dark-knowledge          # 新 card type
dark_knowledge_type: workflow | tool_usage | failure | learning_path | insight | comparison
source_person: 月白 | Truman | 欧阳锋 | ...
source_context: "AIGC设计基础01线上分享"  # 这句话是在什么场景下说的
captured_from: "00_inbox/design/AI设计-AI设计基础01.txt"  # 溯源
```

**正文结构**（六字段，不是三步编译）：

```markdown
## 原始表述
> [月白的原话]

## 使用场景
这条知识在什么情况下用？（具体场景，不要泛化）

## 操作方法
具体怎么做？（步骤级，不要抽象成"原则"）

## 适用边界
什么情况下有效？什么时候不适用？

## 为什么值钱
为什么这条知识是 AI 语料里没有的？

## 与其他知识的关联
链接到相关的概念卡、工具卡、其他暗知识卡
```

### 月白 NotebookLM 案例的暗知识卡速写

```markdown
---
title: "月白用NotebookLM处理课程链接作为学习参考"
type: dark-knowledge
dark_knowledge_type: tool_usage
source_person: 月白
source_context: "AIGC设计基础线上分享"
---

## 原始表述
> 月白提到把课程链接扔给 NotebookLM 处理，作为学习参考。

## 使用场景
- src_unknown
- src_unknown
- src_unknown

## 操作方法
1. 收集课程/文章链接
2. 导入 NotebookLM
3. NotebookLM 基于这些内容生成摘要、回答提问
4. 将提炼后的内容作为后续 AI 协作的上下文

## 适用边界
- src_unknown
- src_unknown
- src_unknown

## 为什么值钱
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联
- src_unknown
- src_unknown
```

### 两条轨道的协同

| | 产品轨（已有） | 过程轨（新增） |
|------|-------------|-------------|
| 编译方法 | 三步编译法 | 六字段模板 |
| 产出类型 | concept/tool/framework/entity | **dark-knowledge** |
| 粒度 | 卡片级（500-2000字） | **原子事实级（50-200字/条）** |
| 存储位置 | `30_wiki/concepts/` | `30_wiki/concepts/`（同一目录，type区分） |
| 适用素材 | 已有明确知识结构的分享 | 所有口述稿、对话、分享——只要有"只有这个人知道"的信息 |
| label 要求 | domain + tags | domain + tags **+ source_person + dark_knowledge_type** |

### 当前假原子 vs 真原子

当前 v1.1 的 chunk 是**按 `##` 标题切分**。以 `master-decision-hygiene.md` 为例（pilot 结果：16 chunks）：

```
假原子（当前）：
  chunk: "## 核心主张" → 整个 section 作为一个 chunk（可能300-800字，含3-8条独立主张）

真原子（应该是）：
  chunk: "决策卫生五步法 Step 1: 独立判断" → 单条主张（50-150字）
  chunk: "Step 1 的反例: 先看别人的方案再自己判断" → 单条边界（30-80字）
  chunk: "Step 1 的底层原理: 锚定效应" → 单条原理（20-60字）
```

### 真原子的标准

| 维度 | 假原子（v1.1） | 真原子（v1.3） |
|------|---------------|---------------|
| **粒度** | heading 级（200-2000字/块） | **主张/事实/规则级**（30-200字/块） |
| **一块对应** | 一个章节 | **一个可独立引用、独立验证的最小单元** |
| **数量** | 5-16 块/卡 | **20-80 块/卡** |
| **例子** | "## 核心主张"整段 | "锚定效应导致决策偏离"、"独立判断的反例是群体思维"、"决策卫生五步法的使用前提是..." |
| **能否独立回答 query** | 部分能 | **每条都能** |
| **能否被独立反驳** | 不能（太粗） | **能 — 这是矛盾检测的前提** |

### KDO 实例：corrections.md 的原子化

```
原文：
"C-10: 基础设施工具改后直接跑批量 → 71 张卡攻击者内容被清空"

假原子（1个chunk）：整条 C-10 作为一个 chunk

真原子（至少 5 个 chunk）：
  chunk 1/error_data: "改了 enrich 脚本后未 dry-run 单卡，直接批量跑"
  chunk 2/error_data: "71 张卡的 Critique section 内容被空字符串覆盖"
  chunk 3/constraint:  "基础设施修改后必须先 dry-run 单卡，验证通过才能批量"
  chunk 4/constraint:  "批量写入前须经人类明确批准（来源：F-KDO-014）"
  chunk 5/process_data: "修复方式：从 git 回滚每张卡，逐一恢复内容"
  chunk 6/claim:       "batch dry-run 的单卡验证通过 ≠ 批量安全（关联 P-4、C-10）"
```

### KDO 实例：口述稿的暗知识萃取

`00_inbox/AI-study/AI数据/一堂-AI数据第一课口述02.txt` 中 Truman 关于"识别"环节的自曝：

```
原文片段：
"我们讨论完之后，发现有四类之前完全忽略了的高质量数据：
1. 双三角模型 — 我们最重要的战略资产，数据散在各处，没存语音
2. BA对比 — 我给下属的反馈随着时间消失了
3. 学员介绍 — 某些作业的小题目，没留存
4. 及时复盘 — 最近刚学会，任务完成立刻让AI复盘，价值巨大"

假原子（1个chunk）：整段作为 "example" chunk

真原子（至少 8 个 chunk）：
  chunk 1/claim:       "识别阶段的核心产出是找到被忽略的高价值数据"
  chunk 2/example:     "一堂案例：双三角模型虽有大量访谈，但语音散落各处未集中存储"
  chunk 3/example:     "一堂案例：Truman 给下属的 review 反馈随时间消失，未存为 AI 语料"
  chunk 4/example:     "一堂案例：学员在作业中提交的自我介绍是高质量数据但未留存"
  chunk 5/procedure:   "及时复盘战术：趁聊天框 session 还在，让 AI 立即复盘全过程→存为笔记"
  chunk 6/claim:       "复盘窗口极短——过了30分钟到一两周，数据永久丢失"
  chunk 7/error_data:  "常见错误：以为'存了'就够了。实际四类数据都没意识到要存"
  chunk 8/constraint:  "不要把所有数据都存——只存 ROI 为正的。判别标准：未来是否会后悔没存"
```

```
小鱼苗 → 池塘 → 数据库 → 数据湖 → 数据海洋
（随手存）（慢慢积累）（结构化）（规模化）（AI驱动）
```

**三个原则**：
1. **原始优先**：先保留原始数据，再加工。加工错了还能回溯。
2. **动手不纠结**：一旦怀疑未来有用，直接存。纠结的成本 > 存储的成本。
3. **防AI叠加污染**：AI生成→AI再分析的叠加数据谨慎存储，不如不存。

**对 KDO 的影响**：capture 环节的 `00_inbox/` 应该更宽松——低门槛快速捕获，不要求立刻分类。但需要标记数据来源代际（原始 vs AI生成 vs AI叠加），防止污染。

### 5. Before：我以为"使用"就是 query。After：inbox 本身就是湖仓的"湖"，问题在于什么值得从湖升仓。

**湖仓架构在 KDO 中的映射**：

```
湖（Lake）= 00_inbox/     — 低门槛快速捕获，什么都往里扔
仓（Warehouse）= 30_wiki/ — 经过识别、清洗、打标、切分的高质量数据
```

"我们先把素材放到 inbox 里面，这本身就是湖仓的概念。至于哪些内容值得被真正地进行识别和清洗，这才是需要重点考虑的。" —— 用户

**问题不是"怎么 query"，而是"什么值得从湖升仓"**。这恰恰是 A.D.U.C.I.T 框架中 A（预判）和 D（识别）要回答的：

| 步骤 | 问题 | KDO 实现 |
|------|------|---------|
| A 预判 | 这个素材未来 AI 怎么用？值不值得处理？ | 入库前先估值（微观/中观/宏观） |
| D 识别 | 我现在有什么？哪些是隐藏的暗知识？ | 盘点 inbox + 已有 wiki，找遗漏 |
| 升仓决策 | ROI 为正？ | 使用频率 × 独特性 × 保质期 > 处理成本 |

**当前 KDO 的最大漏洞**：inbox 里的素材（口述稿、截图、聊天记录）大量堆积，但没有自动化的"升仓决策"机制。结果是湖里的鱼很多，但没有哪条被捞出来做成罐头。

| 级 | 方式 | 成本 | KDO 当前 |
|----|------|------|---------|
| L1: 投喂 | 单次对话上下文 | 极低 | ✅ kdo query |
| L2: 封装 | 系统提示词 / Data Pack | 低 | ⏸ 部分（skill） |
| L3: 检索 | RAG / 知识库 / Graph RAG | 中 | ✅ kdo graph query |
| L4: 配置 | Workflow / Agent 节点 | 高 | ⏸ 待建设 |
| L5: 训练 | Fine-tuning | 极高 | ❌ 暂不需要 |

**原则**："不要用战术上的勤奋（堆数据微调）掩盖战略上的懒惰（不懂业务）。先 1→2→3→4，实在不行再 5。"

### 7. Before：我没有"反馈"环节。After：反馈有三种模式 + 是飞轮闭合的关键。

| 模式 | 机制 | KDO 对应 |
|------|------|---------|
| **人工反馈** | 人 review → 加规则 → 重新应用 | kdo feedback → kdo improve |
| **监督反馈** | 专门 Agent 监控其他 Agent | ⏸ 待建设（evaluation agent） |
| **鱿鱼游戏反馈** | A vs B PK + 交叉审查 | ⏸ 实验性 |

**关键**：如果没有反馈，AI 就像一个永远不听劝的实习生——犯错下次还犯。有了反馈，飞轮才能闭合。

### 8. Before：我不知道最佳数据格式。After：清单笔记是人机最大公约数。

> "清单笔记是人类大脑和 AI 大脑之间效率最高、损害最低的 API 接口。AI 喜欢结构化、逻辑清晰、模块化、少幻觉的东西。人类喜欢不学就会、没有心理负担、不需要教学的东西。清单体正好两头都满足。"

**对 KDO 的格式启示**：
- src_unknown
- src_unknown
- src_unknown

### 9. Before：我构建的是单 agent 的检索系统。After：多 Agent 协作需要统一的文档底盘。

从闲聊篇的 Truman 多 Agent 实践：
> "全部围着 Markdown 文件夹协作。默认不依赖记忆，所有必要上下文全靠文档。随时换 Agent，只要读一下文档就能加载到最佳状态。"

**对 KDO 的架构启示**：
- src_unknown
- src_unknown
- src_unknown

---

## v1.3 方案更新

### 管线框架重构：从五阶段到 6+1

```
原管线（v1.1）：
Phase 1: Audit → Phase 2: Clean → Phase 3: Tag → Phase 4: Chunk → Phase 5: Validate

v1.3 重新映射为 A.D.U.C.I.T + Governance：
A（预判） — Phase 0: 每张卡入库前先做价值预判（微观/中观/宏观）
D（识别） — Phase 1: 审计 + 识别隐藏的高价值数据
U（收集） — Phase 0.5: 湖仓升仓决策 — inbox=湖, wiki=仓, 预判什么值得升仓
C（处理） — Phase 2-4: Clean(粗加工) → Tag+Chunk(精加工) → 萃取指南(注入灵魂)
I（使用） — Phase 5: Validate + 五级使用深度评估
T（反馈） — Phase 6: 闭环反馈（人工/监督/鱿鱼游戏）
治理     — 贯穿：防泄露/防污染/防 AI 叠加/合规护栏
```

### 新增 Phase 0：价值预判（A）

**在卡片入库前，先回答三个问题**：
1. 这张卡属于微观（教材）、中观（燃料）还是宏观（护城河）？
2. 它的预期使用频率？独特性？保质期？
3. ROI 是否为正？（使用价值 > 处理成本）

**输出**：卡片 frontmatter 新增字段：
```yaml
value_tier: micro | meso | macro
expected_usage_frequency: high | medium | low
uniqueness: unique | rare | common
expiry: volatile | current | stable | evergreen
```

### 新增 Phase 0.5：湖仓升仓决策（U）

**规则**：
1. `00_inbox/` 低门槛捕获 — 截图、录音、链接、笔记，先存再说
2. 标记 `data_generation: original | ai_generated | ai_on_ai`（防叠加污染）
3. 定期（周级）从 inbox → raw sources → wiki cards 的升级管道

### Phase 2-4 扩展：三层处理工序

| 层 | v1.1 操作 | v1.3 新增强化 |
|----|----------|-------------|
| 粗加工 | Clean（日期/引号/枚举） | + OCR 自动触发 + 格式转换（PDF/图片→Markdown） |
| 精加工 | Tag（5维）+ Chunk（12类） | + **萃取指南**（每组相关卡片提炼一个方法论摘要，作为"指南"chunk） |
| 注入灵魂 | ❌ 无 | + **黄金测评集**（每域 10-50 个 QA 对，作为验证标准） |

**萃取指南（v1.3 新增 chunk 子类型）**：
```
chunk_type: extraction_guide
来源：一组相关 claim chunk → 提炼 → 1 个 extraction_guide
内容：统领这组数据的核心方法论、规则、原则
示例：4 篇睡前故事 → 1 篇"睡前故事创作指南"
```

### Phase 5 扩展：五级使用深度评估

`kdo validate` 增加卡片使用深度评级：
```yaml
usage_depth: feed | packaged | retrieval | configured | trained
```
**默认**：所有卡片最低 `feed`（可被单次对话引用）。高价值卡片逐步升级。

### Phase 6 新增：闭环反馈（T）

| 模式 | 实现 |
|------|------|
| 人工反馈 | `kdo feedback` → `kdo improve`（已有）— 增加"反馈必须回到卡片标注"的闭环 |
| 监督反馈 | 新增 evaluation agent 定期抽查 AI 使用卡片后的产出质量 |
| 实验反馈 | A/B 对比：同一 query，卡片清洗前 vs 清洗后的 AI 回答质量 delta |

### 治理层新增（贯穿全程）

| 风险层 | 机制 |
|--------|------|
| 物理安全 | Git + 坚果云备份（已有） |
| 数据污染 | `data_generation` 字段标记 AI 代际，防叠加 |
| 隐私合规 | source_refs 的 `rights` 字段：private/public/licensed |
| 过期管理 | `expiry` 字段 + 定期审查（`kdo lint --stale`） |

### 新增格式标准：清单笔记作为一等格式

在 `30_wiki/` 中，鼓励以下卡片类型使用清单体：
- src_unknown
- src_unknown
- src_unknown

清单体标准：
```markdown
## 核心清单
1. **[要点]** — 一句话解释。
2. **[要点]** — 一句话解释。
   - src_unknown
   - src_unknown
```

### 6 级成熟度自评嵌入

`kdo status` 增加数据成熟度自评输出：
```
Data Maturity: L3 (随机处理)
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
```

---

## 交付物清单（v1.3 更新）

| 文件 | v1.1 | v1.3 | 变更 |
|------|------|------|------|
| `SKILL.md` | ⏸️ | ⏸️ 待更新 | +6+1框架 +双飞轮 +成熟度 +治理 |
| `audit_cards.py` | ✅ | ⏸️ 扩展 | +value_tier推断 +data_generation检测 |
| `clean_cards.py` | ✅ | ✅ 不变 | — |
| `tag_cards.py` | ⏸️ | ⏸️ 扩展 | +萃取指南生成 +黄金测评集 |
| `chunk_cards.py` | ⏸️ | ⏸️ 扩展 | +extraction_guide 类型 +usage_depth |
| `validate_clean.py` | ⏸️ | ⏸️ 扩展 | +AI产出质量delta +成熟度自评 |
| `tag-registry.yaml` | ⏸️ v2 | ⏸️ v3 | +data_generation 维度(3值) +value_tier 维度(3值) |
| 新增: `schema/extraction-guide.yaml` | ❌ | ✅ 新增 | 萃取指南 schema |
| 新增: `scripts/feedback_loop.py` | ❌ | ⏸️ 新增 | 反馈闭环脚本 |

---

## 迭代设计更新

- src_unknown
- src_unknown
- src_unknown
- src_unknown
