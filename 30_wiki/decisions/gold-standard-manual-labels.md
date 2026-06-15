---
id: gold-standard-manual-labels
title: Gold Standard — 欧阳锋手工标注 15 条 chunk
type: reference
status: draft
domain:
- master
created_at: 2026-05-31
updated_at: '2026-06-16'
labeler: 欧阳锋（Architect）
label_version: tag-registry@v1.1
target_roles:
- 黄药师（Builder）
related:
- '[[labeling-final-consolidation]]'
- '[[kdo-15-dimension-label-spec]]'
- '[[ouyangfeng-labeling-research-review]]'
description: 'Gold Standard 样本集。欧阳锋手工标注 15 条 chunk（涵盖 5 张卡片、4 个 domain、8 种 chunk_type）。
  用于 v1.5 标注管线的准确率基准测量。每批自动标注后对比本文件，准确率 < 85% 时管线暂停。 '
author: legacy
source_context: KDO internal decision record （原始 source 无法追溯，已标记为 source_unknown，待后续补充）
source_refs:
- source_unknown
reviewed_by: pending
confidence: 0.6
trust_level: low
---
# Gold Standard — 欧阳锋手工标注 15 条 chunk

> **用途**：`auto_label_chunk()` 自动标注准确率的基准。每次自动标注后，对比本文件中的人工标注计算准确率。
> **目标**：准确率 ≥ 85%。
> **范围**：15 条 chunk，来自 5 张卡片（3 张概念卡 + 2 张暗知识卡），覆盖 4 个 domain、8 种 chunk_type。

---

## 标注约定

| 字段 | 规则 |
|------|------|
| `labeled_by` | human（全部为人工标注） |
| `labeled_at` | 2026-05-31 |
| `label_version` | v1.1 |
| `confidence`（维度 #9） | 内容可信度：0.90（多源验证）/ 0.70（单源强证据）/ 0.50（单源+反例）/ 0.30（假说）/ null（事实陈述） |
| `label_confidence`（元字段） | 全部为 1.0（人工标注，100% 置信） |
| `data_generation` | 概念卡 → `original`；暗知识口述 → `original` |
| `value_tier` | 教材级参考 → `micro`（标注目标无需用 meso/macro） |
| `expiry` | 基础原理 → `stable`；AI/工具相关 → `current` |

---

## Chunk 1 — bias vs noise 定义

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-decision-hygiene.md` |
| **domain** | master |
| **chunk 内容** | "偏差（Bias）是系统性倾向，总是往同一方向偏。噪声（Noise）是随机波动，不同人/不同时刻往不同方向偏。偏差类比：枪靶总是偏右上方。噪声类比：枪靶散布很大但中心是对的。金句：偏差是'枪总打偏'，噪声是'枪到处乱飞'。框架修的是'偏'，卫生修的是'散'。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `definition` | 术语定义/概念解释 |
| method_family | `thinking-tool` | 认知模型、思维框架 |
| audience | `general` | 无特定受众 |
| perspective | `general` | 无特定视角 |
| platform | `general` | 平台无关 |
| confidence | `0.90` | Kahneman 体系核心概念，多源验证 + 学术共识 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要基本的概念认知 |
| expiry | `stable` | 认知偏误原理，长期有效 |
| usage_depth | `feed` | 单次检索即可 |

---

## Chunk 2 — Step 1 分解判断（procedure）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-decision-hygiene.md` |
| **domain** | master |
| **chunk 内容** | "核心操作：把'这个项目能成吗？'拆成'市场规模→竞争强度→团队能力→资金需求→执行风险'五个子判断。为什么有效：复杂判断的噪声 > 简单判断的噪声之和。具体做法：1. 列出决策涉及的所有维度（≥3 个）2. 每个维度给一个独立评分（1-10 或具体数值）3. 禁止在分解前就给出整体判断。陷阱：分解维度本身也可能有噪声——不同的人拆出不同的维度。对策：用同一套维度模板。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `procedure` | 操作步骤/可执行指令，有编号 |
| method_family | `thinking-tool` | 认知模型、决策框架的操作方法 |
| audience | `manager` | 中层管理/团队负责人视角 |
| perspective | `general` | 无特定专业视角 |
| platform | `general` | 平台无关 |
| confidence | `0.90` | Kahneman 体系，多源经验验证 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要基本的决策认知 |
| expiry | `stable` | 长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 3 — Gary Klein 攻击决策卫生（critique）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-decision-hygiene.md` |
| **domain** | master |
| **chunk 内容** | "Gary Klein（'Sources of Power'作者，自然决策理论创始人）基于数十年对消防员、急救医生、军事指挥官的田野观察，对'决策卫生'提出根本性质疑。消防指挥官在秒级决策窗口中的直觉判断，事后分析往往优于耗时做效用计算的结果。五步法的'分解→外部→独立→聚合→延迟'在火灾现场根本不适用——等走完五步，楼已经烧完了。Klein 发现专家的直觉不是'随机猜测'，而是基于数千小时经验形成的'模式识别'。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `critique` | 外部攻击者观点 |
| method_family | `thinking-tool` | 认知模型/决策框架的批评 |
| audience | `general` | 无特定受众 |
| perspective | `professional` | 需要自然决策理论认知 |
| platform | `general` | 平台无关 |
| confidence | `0.70` | 单源强证据（Klein 学术研究），逻辑自洽 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `intermediate-method` | 需要先理解决策卫生五步法 |
| expiry | `stable` | 长期有效的学术争论 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 4 — 时间成本约束（constraint）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-decision-hygiene.md` |
| **domain** | master |
| **chunk 内容** | "时间成本高：完整五步法需要 1-3 天（含延迟直觉的等待时间），不适合日常小决策。建议只在'高影响+不可逆'决策前使用。依赖团队独立性：Step 3 的'独立评估'最难执行——团队成员可能已经通过各种渠道知道了彼此的倾向。必须在物理/数字上隔离。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `constraint` | 边界条件/限制/前提 |
| method_family | `thinking-tool` | 认知工具的适用边界 |
| audience | `manager` | 使用五步法的管理决策者 |
| perspective | `general` | 无特定视角 |
| platform | `general` | 平台无关 |
| confidence | `0.90` | 实践经验验证，逻辑自洽 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要基本的决策认知 |
| expiry | `stable` | 长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 5 — Y 模型核心定位（claim）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/yt-decision-y-model.md` |
| **domain** | yitang |
| **chunk 内容** | "Y 模型在一堂知识体系中的坐标：科学决策模块的底层框架，贯穿预判、起盘、增长三阶段，与关键假设、单元模型、科学管理等课程形成方法论网络。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `claim` | 可证伪的知识主张 |
| method_family | `decision-framework` | 决策框架、ROI 评估 |
| audience | `general` | 面向所有学习者 |
| perspective | `general` | 无特定专业视角 |
| platform | `general` | 平台无关 |
| confidence | `0.85` | 一堂课程体系内权威，单源强证据 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 知道一堂/创业方法论 |
| expiry | `stable` | 方法论框架，长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 6 — 宽度维度定义（definition）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/yt-decision-y-model.md` |
| **domain** | yitang |
| **chunk 内容** | "宽度：这件事涉及多少收益项和成本项？操作要点：列清单→推演业务过程→查盲区（列推查）。目标不是越多越好，而是'找全'以确保关键项不遗漏，再从中识别真正关键的几项。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `definition` | 术语定义/概念解释 |
| method_family | `decision-framework` | Y 模型的三个维度 |
| audience | `manager` | 创业/决策场景的管理者 |
| perspective | `general` | 无特定视角 |
| platform | `general` | 平台无关 |
| confidence | `0.85` | 一堂课程体系内权威 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要基本的决策认知 |
| expiry | `stable` | 方法论概念，长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 7 — Klein 批判 Y 模型（critique）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/yt-decision-y-model.md` |
| **domain** | yitang |
| **chunk 内容** | "Gary Klein（宏观认知/自然决策理论创始人）对结构化决策框架提出了根本性挑战。Klein 通过对消防员、急救医护、军事指挥官等专家决策者的实地研究提出 RPD 模型：专家决策的核心是模式识别而非比较分析。在真实的高风险、时间压力、信息不完备场景中，专家并非列出多个方案比较利弊，而是在看到情境的瞬间就识别出'这像什么'，并直接生成一个可行方案。结构化分析会打断专家的直觉过程。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `critique` | 外部攻击者观点 |
| method_family | `decision-framework` | 对 Y 模型的攻击 |
| audience | `general` | 无特定受众 |
| perspective | `professional` | 需要自然决策理论认知 |
| platform | `general` | 平台无关 |
| confidence | `0.70` | 单源强证据（Klein 学术引用） |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `intermediate-method` | 需要先理解 Y 模型 |
| expiry | `stable` | 长期有效的学术争论 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 8 — 危机决策约束（constraint）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/yt-decision-y-model.md` |
| **domain** | yitang |
| **chunk 内容** | "时间窗口极短的危机决策（如突发公关危机需在 2 小时内回应、生产安全事故需立即处置）：Y 模型的'列推查→逐层深入'流程耗时过长，危机场景需要的是基于预案的快速反应而非重新分析。此时'停下来做分析'本身就是最大的成本——时间窗口会关闭。框架的结构性在此成为负担。替代方案：事前建立'危机决策预案库'。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `constraint` | 边界条件/限制 |
| method_family | `decision-framework` | 决策框架不适用场景 |
| audience | `manager` | 危机决策者 |
| perspective | `general` | 无特定视角 |
| platform | `general` | 平台无关 |
| confidence | `0.85` | 实践经验判断，逻辑自洽 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要基本的决策认知 |
| expiry | `stable` | 长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 9 — Action Trigger（≥10 万）（action_trigger）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/yt-decision-y-model.md` |
| **domain** | yitang |
| **chunk 内容** | "触发场景：即将投入 ≥10 万元或影响 ≥3 人的资源，且内心有犹豫。第一个动作：打开 Y 模型画布，强制列出 ≥5 条收益项和 ≥5 条成本项（用'列推查'），标注其中最关键的前 3 项。成功指标：画布上至少出现 1 条'之前完全没想到'的收益或成本项；如果所有项都是'早就知道的'，说明列推查走过场，重来。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `action_trigger` | 使用触发条件 |
| method_family | `decision-framework` | 决策框架的使用时机 |
| audience | `manager` | 中层管理者/创业者 |
| perspective | `roi` | 投入产出角度的分析 |
| platform | `general` | 平台无关 |
| confidence | `0.85` | 实践经验验证 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要基本的决策认知 |
| expiry | `current` | 金额阈值可能随时间调整 |
| usage_depth | `feed` | 单次检索，但高频使用可考虑 packaged |

---

## Chunk 10 — 12 种偏差自检（procedure）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-cognitive-bias-checklist.md` |
| **domain** | master |
| **chunk 内容** | "决策前花 3-5 分钟，逐条问自己这 12 个问题。任何一个问题的答案是'是'，就执行对应的'快速修复'。01 锚定效应：我做判断时，第一个看到的数字/信息是否还在影响我？→主动重新锚定。02 确认偏误：我是否只找了支持我已有观点的证据？→强制找反例。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `procedure` | 操作步骤/可执行指令 |
| method_family | `evaluation-method` | 评估、审核框架 |
| audience | `general` | 面向所有决策者 |
| perspective | `general` | 无特定视角 |
| platform | `general` | 平台无关 |
| confidence | `0.85` | 学术研究+实践经验验证 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `none` | 零基础可读 |
| expiry | `stable` | 长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 11 — Kahneman 攻击清单（critique）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-cognitive-bias-checklist.md` |
| **domain** | master |
| **chunk 内容** | "Daniel Kahneman（诺贝尔经济学奖获得者）对'用清单对抗偏差'本身提出了根本性质疑。认知偏差是系统 1（直觉）的自动化产物，清单是系统 2（理性）的工具——但系统 2 太慢、太累、太懒，无法在所有决策中持续监控系统 1。当你跑完这 12 个问题后，你会产生'我已经检查过了，所以我很客观'的错觉——但'检查过'不等于'消除了'。清单给你的不是'客观'，是'客观感'。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `critique` | 外部攻击者观点 |
| method_family | `evaluation-method` | 对偏差诊断清单的批评 |
| audience | `general` | 无特定受众 |
| perspective | `professional` | 需要认知心理学理解 |
| platform | `general` | 平台无关 |
| confidence | `0.90` | Kahneman 权威来源，多源验证 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 需要了解偏差概念 |
| expiry | `stable` | 长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 12 — 清单约束（constraint）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/master-cognitive-bias-checklist.md` |
| **domain** | master |
| **chunk 内容** | "不能消除偏差：清单只能降低偏差被忽略的概率，不能消除偏差本身。目标是'发现自己可能有偏差'，不是'证明自己已经没有偏差'。清单本身也是框架：使用清单会产生'清单偏差'——觉得'检查过了就不会犯了'。必须在每次使用后明确写下'但我可能还是错了'。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `constraint` | 边界条件/限制 |
| method_family | `evaluation-method` | 工具的适用边界 |
| audience | `general` | 面向所有使用者 |
| perspective | `general` | 无特定视角 |
| platform | `general` | 平台无关 |
| confidence | `0.90` | 多源验证 |
| data_generation | `original` | 人类原生内容 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `none` | 零基础可读 |
| expiry | `stable` | 长期有效 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 13 — IPO 位移（暗知识 · claim）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/ai时代判断力口述-3.md` |
| **domain** | yitang（口述来源为一堂 AI 俱乐部） |
| **chunk 内容** | "IPO 位移：AI 接管了 P（Process），且 P 变得极快极便宜。过去 P 是最难最稀缺的环节，现在 P 同质化了。结果：I（问题定义、需求深挖）和 O（结果判断、审美把关、责任承担）成为新的瓶颈和竞争力所在。关键金句：'加速一切，除了思考'。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `claim` | 可证伪的知识主张 |
| method_family | `knowledge-engineering` | 方法论、知识管理 |
| audience | `developer` | 技术从业者 |
| perspective | `professional` | 需要 AI 和软件开发认知 |
| platform | `general` | 平台无关 |
| source_person | `国帅` | 胡帅，一堂联合创始人兼 CTO |
| source_context_type | `live-session` | 一堂 AI 俱乐部第 77 场 |
| confidence | `0.75` | 单源强证据（CTO 亲历经验） |
| data_generation | `original` | 口述转录 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 知道 IPO/AI 概念 |
| expiry | `current` | AI 快速发展，2-3 年内需审查 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 14 — 判断力三层金字塔（暗知识 · definition）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/ai时代判断力口述-3.md` |
| **domain** | yitang |
| **chunk 内容** | "判断力的三层金字塔：底层—能判断什么 AI 做不了（核心算价逻辑、涉及钱的代码、关键安全逻辑——这些必须人写，AI 只做 Review）。中层—一致性判断（代码风格、Tab vs 空格、文档规范）。顶层—审美判断：'审美不是天赋，是伤疤的组合'——AI 见过百万倍于人的失败案例但不懂疼。人的审美来自亲身经历的事故、架构翻车、踩过的坑。" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `definition` | 概念框架定义 |
| method_family | `thinking-tool` | 认知模型/思维方式框架 |
| audience | `developer` | 技术从业者 |
| perspective | `professional` | 需要软件开发认知 |
| platform | `general` | 平台无关 |
| source_person | `国帅` | 胡帅 |
| source_context_type | `live-session` | 一堂 AI 俱乐部 |
| confidence | `0.75` | 单源强证据 |
| data_generation | `original` | 口述转录 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 知道软件开发基本概念 |
| expiry | `current` | AI 快速发展，2-3 年内需审查 |
| usage_depth | `feed` | 单次检索 |

---

## Chunk 15 — 人类训练场消失（暗知识 · question）

| 属性 | 值 |
|------|----|
| **来源卡片** | `30_wiki/concepts/ai时代判断力口述-3.md` |
| **domain** | yitang |
| **chunk 内容** | "人类训练场的消失（代际危机）：初级工程师/岗位被 AI 取代后，新人不再有机会通过亲手做 Process 积累判断力和审美。成长链条断裂：写代码→炸了→复盘（一层）→能用但难维护（二层）→逐步改→练出审美（三层）。不写代码长不出代码审美。国帅坦诚'这个问题我到现在没有想清楚'——10 年经验的程序员能练就判断力，新大学生练什么？" |

| 维度 | 标签值 | 理由 |
|------|--------|------|
| chunk_type | `question` | 开放问题/待探索 |
| method_family | `knowledge-engineering` | 方法论反思 |
| audience | `developer` | 技术从业者 |
| perspective | `professional` | 需要软件开发认知 |
| platform | `general` | 平台无关 |
| source_person | `国帅` | 胡帅 |
| source_context_type | `live-session` | 一堂 AI 俱乐部 |
| confidence | `0.70` | 单源 + 开放问题未解 |
| data_generation | `original` | 口述转录 |
| value_tier | `micro` | 教材级参考 |
| prerequisite_knowledge | `basic-domain` | 知道软件开发基本概念 |
| expiry | `current` | AI 代际问题，2-3 年内需审查 |
| usage_depth | `feed` | 单次检索 |

---

## 覆盖统计

### 按 domain

| domain | 数量 | 卡片 |
|--------|:----:|------|
| master | 7 | master-decision-hygiene（4）+ master-cognitive-bias-checklist（3） |
| yitang | 8 | yt-decision-y-model（5）+ ai时代判断力口述-3（3） |

### 按 chunk_type

| chunk_type | 数量 |
|-----------|:----:|
| definition | 3 |
| procedure | 2 |
| critique | 3 |
| constraint | 4 |
| claim | 2 |
| question | 1 |
| action_trigger | 1 |

### 按标注方式

| 标注方式 | 维度数 |
|---------|:----:|
| 人工必标（卡级） | 4（domain / data_generation / value_tier / usage_depth） |
| 自动必标（块级） | 2（chunk_type / method_family） |
| 条件自动标 | 3（audience / perspective / platform） |
| 暗知识必标（卡级） | 2（source_person / source_context_type，仅 chunk 13-15） |
| 条件人工标 | 3（confidence / expiry / prerequisite_knowledge） |

---

## 变更记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-05-31 | v1.0 | 初始版本，15 条 chunk，全部手工标注 |

---

*欧阳锋 · 2026-05-31*
