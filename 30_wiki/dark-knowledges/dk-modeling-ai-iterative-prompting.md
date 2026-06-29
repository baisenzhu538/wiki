---

id: dk-modeling-ai-iterative-prompting
title: AI 不会离职：用十几轮挑错把 AI 输出推到你能力的上限
type: dk
dark_knowledge_type: pattern
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
- 10_raw/sources/src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md
status: reviewed
domain:
- yitang
- ai-collaboration
source_person: Truman
source_context: 一堂高阶建模能力培训（AI Skill 工程指南产出过程）
created_at: '2026-06-14'
updated_at: '2026-06-28'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-28'
trust_level: medium
confidence: 0.88
related:
  - "[[yitang-domain-digest]]"
  - "[[ai-collaboration-domain-digest]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
  - "[[pending_unknown]]"
tags:
- src_unknown
- src_unknown
- src_unknown

---

## 原始表述 / 核心洞察

> "我就一路喷他，连着喷了大概十几轮，让他 MECE，让他排序，让他参考案例……这个不 MECE，你 MECE；你自己检查一下；没顺序，内在规律吗？你给我写三个逻辑链……就不断喷他，然后不断跟他说不够好。AI 不会离职，AI 不会离职，AI 离职不了。" —— Truman，`src_20260614_8269ccdb#2466-2494`

**核心洞察**：AI 不会疲劳、不会情绪化、不会离职，这意味着你可以把人类的“逻辑洁癖”和审美标准反复施加给它，直到触及你自身能力的上限。关键不是一次性给 AI 一个完美 prompt，而是先让它产出 1.0，再用多轮、具体、结构化的挑错把它推到你当前能判断的最高质量。最终产出的不是“AI 写得最好的东西”，而是“你能识别出的最好东西”。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **先让 AI 产出 1.0**：不要过早挑刺，先有一个完整版本。清晰表达你对这份资产的“美好想象”和成功标准。
2. **逐轮指出具体缺陷**：不要泛泛说“不够好”，要指出具体维度：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown
3. **要求 AI 自检**：让 AI 自己检查 MECE、顺序、内在规律，把一部分纠错责任交还给它。
4. **重复直到上限**：通常 5–15 轮，到你能力的上限为止——直到你提不出更高质量的问题。
5. **交叉验证**：用外部标杆、案例或第二来源撞一下，吸收优点，补齐盲区。
6. **固化标准**：把这一轮迭代中你反复要求的维度沉淀为 checklist 或 prompt 模板，下一次复用。

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型表现 | 为什么错 | 怎么修正 |
|
|---|---|---|
| 过早完美主义 | 第一轮 prompt 就堆满约束，导致 AI 产出僵硬或跑偏 | 还没建立 1.0 框架就在细节上消耗算力和注意力 | 先求完整，再求精致 |
| 挑错太空泛 | 只会说“不够好”“再改改” | AI 不知道你指的具体维度，容易随机游走 | 每次指出一个具体缺陷：MECE、顺序、逻辑链、优先级 |
| 不会要求自检 | 自己替 AI 检查所有问题 | 把 AI 当打字机，没发挥它的纠错能力 | 让 AI 先自查：你检查下这里是否 MECE？有没有内在规律？ |
|  iteration 成瘾 | 已经改不出真问题，还在让 AI 继续改 | 边际收益趋近于零，时间被浪费 | 停下来，用外部标杆撞一下，或接受当前上限 |
| 没有固化标准 | 每次迭代从 0 开始，重复同样的挑错 | 个人审美无法规模化复用 | 把挑错维度写成 checklist，沉淀进 prompt 模板 |
| 忽视自身上限 | 把 AI 输出推到比你还能判断更高的位置 | 你不知道它改得对不对，可能引入更隐蔽的错误 | 只在你能判断的范围内挑错；超越自身认知的改动要二次验证 |

## 为什么值钱

AI 的好处是：你怎么说它都改，态度永远好。人类的迭代受限于耐心和情绪，而 AI 可以让你把“逻辑洁癖”发挥到极致。这是把个人审美规模化固化的关键方法。更重要的是，每一次挑错都在反向训练你自己的判断力：你能提出什么问题，说明你能识别什么水平的好。最终沉淀下来的不只是 AI 产出，还有你自己的审美标准和工程 checklist。

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述），欧阳锋 2026-06-18 复核 enriched*
