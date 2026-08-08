---


id: concept-yihang-ai-feature-thinking
title: AI 基本功的 Feature 思维：把工具拆成最小可操作技术特?
type: concept
status: reviewed
author: 老顽?
reviewed_by: ŷ
review_date: 2026-07-04
confidence: 0.90
trust_level: high
language: zh-CN
created_at: 2026-07-04
updated_at: '2026-07-04'
domain:
- ai-collaboration
- yitang
source_refs:
- 00_inbox/人机协作双三?一堂双三角-人机协作模型-口述.txt
- 00_inbox/AI-study/一?AI学习-AI工具应用AMA口述.txt
- 10_raw/sources/src_20260609_03491271-ocr-一?ai学习-truman自用的ai-featureset.md
aliases:
  - Feature思维
  - AI基本功
  - 技术特性原子化
discoverable_by:
  - AI 基本功的 Feature 思维：把工具拆成最小可操作技
  - 基本功的
  - 把工具拆成最小可操作技术特?
related:
  - '[[framework-truman-feature-thinking-core]]'
  - '[[framework-truman-feature-layered-system]]'
  - '[[concept-truman-feature-four-scenarios]]'
- "[[concept-yihang-dual-triangle-core]]"
- "[[tool-Truman-Feature特性层训练法]]"
- "[[tool-Truman-AI能力分层学习路径]]"
- "[[method-yitang-y-model-engine-cycle]]"
---
# AI 基本功的 Feature 思维：把工具拆成最小可操作技术特�?
> **一句话定义**：Feature 思维 = �?AI 工具拆成最小可操作技术特性（Feature），围绕特性组合而非工具名字来思考、选型、练习和决策。Feature 位于底层大模型与上层工具之间，是 AI 基本功的最小单位�?
---

## 一、核心命�?
1. **基本�?�?会用工具**。今天学 ChatGPT、明天学 Coze、后天学 Cursor，是"工具迷信"——被工具名字带着走，永远在追新，永远没积累�?2. **基本�?= 掌握 AI 工具�?Feature（最小可操作技术特性）**。Feature 是位于底层大模型与上层工具之间的中间层，跨工具可迁移�?3. **Feature 是原子化的、可测试的、可组合�?*�?拆完之后一共也就几十个特�?（口述稿 L1426），例如 temperature、渐进披露、长时记忆、思维链、加案例、加约束�?4. **Skill �?Feature 的封装逻辑**�?它跟 skill 是两套东西，skill 就是一个封装逻辑"（口述稿 L1428-1429）——Feature 是原子，Skill 是把原子按场景打包后的可复用逻辑�?5. **Feature 思维让人不被工具带走**。新工具火不火不重要，重要的�?它比现有工具多了哪几�?Feature"�?
---

## 二、原文依�?
### 双三角课�?
> "第三个我们说的基本功，说的是 AI 基本功啊，就�?AI 上的那些工具，那些特性�?（双三角口述稿，�?1210�?
> "不要老盯着工具，你去盯着每一个工具那些特有的最小的技术特性�?（双三角口述稿，�?1408�?
> "特性是原子化的最小技术单位，叫可操作的原子化的最小技术单位。它�?skill 是两套东西，skill 就是一个封装逻辑�?（双三角口述稿，�?1426-1428�?
### AI 上手第一�?/ AI 工具应用 AMA

> "这在基于底层的大模型和上面的工具中间呢，要抽出了一层叫�?feature 啊。它是指的一些封装啊，包括渐进披露啊，包�?data pack 等等�?（AMA 口述，行 154-156�?
> "基于这个逻辑我们构建�?Y模型，整�?Y模型都是在特�?feature 的基础上去构建的�?（AMA 口述，行 160�?
> "你如果理解了 feature 这套逻辑，工具对你来说就没有那么重要。你用什么工具？其实你用的就是那些特性�?（AMA 口述，行 180-184�?
---

## 三、关键案例：一个参数让成本降到 1/40

| 要素 | 内容 |
|:---|:---|
| **人物** | Truman / 业务团队 / 莹莹 |
| **背景** | 用国外模型跑一轮邮件，花了几万块钱，效果还不理�?|
| **动作** | 有人想到一个过去没用过的参数—�?*temperature**，只调了一个参�?|
| **结果** | 用约 **1/40 的成�?*，达到跟全球最好模型差不多的水�?|

> "我们用国外的模型做跑一轮，几万封一封信花了我们几万块钱……后来只要突然间想到了一个参数……然后调了一�?temperature……跟国外模型一模一样。就一个参数�?（双三角口述稿，�?1380-1388�?
> "所以我们用了大�?40 分之 1 的成本，达到了跟全球最好的模型的水准，就靠调一个小的参数�?（双三角口述稿，�?1392�?
**教训**：不是工具不行，是不懂工具的最小技术特性。基本功不是会换工具，而是会调特性�?
### 补充案例

| 案例 | Feature | 效果 |
|:---|:---|:---|
| **豆包做图：文生图 vs 代码画图** | 技术路线选择 | 莹莹用代码画�?4 小时全是秃头小人；Truman 加了一�?�?Midjourney"就出好图——不是审美差距，是不知道有这�?Feature（口述稿 L1348-1376�?|
| **龙虾 vs 爱马�?* | Feature 对比 | "龙虾火是因为有三四个核心特性，爱马仕又多了那么一两个……你如果用那个特性就用爱马仕，不用就接着用龙�?（口述稿 L1432-1436�?|

---

## 四、概念澄清：Feature vs 工具 vs Skill

| 概念 | 定义 | 例子 |
|:---|:---|:---|
| **Feature（特性）** | AI 工具的最小可操作技术单位，原子化、可测试、跨工具 | temperature、渐进披露、长时记忆、思维链、加案例、加约束 |
| **工具** | 把多�?Feature 打包后的产品 | ChatGPT、Coze、Cursor、Claude、Kimi、Codex |
| **Skill** | �?Feature 按特定场景封装后的可复用逻辑 | 口喷提示词、PPT 渲染工作流、论文初�?Agent |
| **基本�?* | 掌握 Feature 清单，并能根据场景组�?Feature | 知道什么时候调 temperature、什么时候加浏览器、什么时候用长时记忆 |
| **工具迷信** | 被工具名字带着走，忽略底层 Feature | 因为某个工具火了就切换，结果没用到新 Feature |

---

## 五、Truman 自用 AI FeatureSet

来源：`10_raw/sources/src_20260609_03491271-ocr-一�?ai学习-truman自用的ai-featureset.md`

| 层级 | Feature 清单 |
|:---|:---|
| **LLM 层（大模型层�?* | 选模型、使用不同版本、模型参数、同时抽卡、模型组�?|
| **提示词层** | 提示词迭代、数字角�?用户角色、任务要求、背景信息、行文规则、负面限制、输出要求、风格设定、多轮对�?|
| **上下文控制层** | 更大上下文、渐进式披露、复制粘贴、分层标注、重点标注、主动摘要、使�?Skill |
| **数据�?* | 给案例集、专家资料、用多模态、联网搜索、接�?API、使�?RAG、数据分�?|
| **协作�?* | AI 高阶角色、反向提示、反向教学、反向采访、反向记录、使�?CoV、使�?ReACT |
| **效率�?* | 拆分任务、拆解环节、分离场景、多轮确认、使�?CoT、设计工作流、分支环、使用插件、模型匹配、并行调度、效率提�?|

---

## 六、常�?Feature 示例（跨来源汇总）

| 类别 | Feature 示例 | 来源 |
|:---|:---|:---|
| 模型参数 | temperature、top_p、max_tokens、frequency_penalty | 双三角口述稿 + FeatureSet |
| 上下文工�?| 长上下文、RAG、渐进披露、长时记忆、摘要压�?| FeatureSet + AMA |
| 推理增强 | 思维链（CoT）、自我一致性、ReACT | AMA + 双三角口述稿 |
| 外部能力 | 浏览器使用、代码执行、文件读写、API 调用 | 双三角口述稿 |
| 输入增强 | 加案例（few-shot）、加约束、加角色、加输出格式 | FeatureSet |
| 输出控制 | JSON 模式、结构化输出、Function calling | FeatureSet |
| 多模�?| 图像理解、语音输入、视频分�?| FeatureSet |
| 协作机制 | �?Agent 并行、红蓝军对抗、迭代反�?| FeatureSet + 双三角口述稿 |
| 数据增强 | Data Pack、案例集、专家资料、联网搜�?| AMA + FeatureSet |

---

## 七、Feature 思维的实操价�?
### 对个人：不被工具带走

新工具出现时只问�?它比我现在用的工具多了哪几个 Feature�?——如果新 Feature 不是当前任务需要的，继续用旧工具。如果新 Feature 能提升结果，快速迁移�?
### �?Agent 设计：原子化能力

Agent 的能力不应该按工具划分，而应该按 Feature 划分。一�?Agent 可以组合"思维�?+ 长时记忆 + 工具调用"三个 Feature，而不是绑定到某个具体模型。这�?Agent 可以随着工具升级无缝迁移�?
### �?KDO 建设

应该把热门工具拆解为 Feature 清单，沉淀�?concept/method/tool 卡。避�?KDO 出现"追热点工具卡"而缺�?底层 Feature �?。双三角画布中的"基本�?格子，未来可以填�?Feature 清单而不是工具列表�?
---

## 八、Critique

### 内部局�?
1. **Feature 清单需要持续维�?*：新模型/新工具持续出现，Feature 清单如果不更新会过时�?2. **某些工具的整�?UX 就是其价�?*：拆�?Feature 后可能丢失整体体验优势（�?Cursor �?Tab 补全体验）�?3. **Feature 思维有学习门�?*：初学者需要先理解每个 Feature 是什么，才能�?Feature 思维思考�?
### 外部攻击

**[Tool Maximalist]**
> "Feature 思维把工具拆得太碎。一个新手连 ChatGPT 都还没用熟，你让他学几十�?Feature？这是在增加认知负担�?

**回应**：Feature 思维不是让初学者一开始就学全�?Feature，而是给进阶者一个不迷失在工具海洋里的框架。初学者可以先�?3-5 个最常用�?Feature 开始——temperature、few-shot、CoT、RAG——而不是试图掌握全部�?
---

## 九、Synthesis

| 关系 | 目标�?| 说明 |
|:---|:---|:---|
| 能力框架 | [[concept-yihang-dual-triangle-core]] | Feature 思维是双三角"基本�?要素的核心内�?|
| 操作方法 | [[tool-Truman-Feature特性层训练法]] | Feature 思维的刻意练习方�?|
| 学习路径 | [[tool-Truman-AI能力分层学习路径]] | 从零基础�?Feature 专家的进阶路�?|
| 底层引擎 | [[method-yitang-y-model-engine-cycle]] | Feature 层的掌握程度�?Y模型 循环�?理论侧·科学类�?的输入质量决定因�?|

---

## Action Triggers

| 触发场景 | 第一个动�?|
|:---|:---|
| 看到一个新 AI 工具火了 | 不问"好不好用"，问"它比现有工具多了哪几�?Feature" |
| 学了很多工具但感觉没有积�?| 把你用的工具拆成 Feature 清单，看哪些 Feature 是重复的 |
| 团队在争�?用哪个模�?工具" | 先用 Feature 清单对齐需求，再根�?Feature 覆盖度选工�?|
