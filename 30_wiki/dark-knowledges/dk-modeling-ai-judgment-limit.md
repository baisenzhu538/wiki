---

id: dk-modeling-ai-judgment-limit
title: AI 能辅助建模，但核心判断必须人做：AI 太容易受你影响
type: dk
dark_knowledge_type: principle
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
status: reviewed
domain:
- yitang
- ai-collaboration
- modeling
source_person: Truman
source_context: 一堂高阶建模能力培训（AI 与本质建模）。单一完整长文档支撑，但尚未找到第二独立来源，因此 trust_level 维持 medium；待后续案例或实践验证后可升
  high。
quality_labels:
  - quality
  - validated
created_at: '2026-06-14'
updated_at: '2026-06-28'
author: 老顽童
reviewed_by: 欧阳锋
review_date: '2026-06-28'
trust_level: medium
confidence: 0.89
related:
  - "[[yitang-domain-digest]]"
  - "[[ai-collaboration-domain-digest]]"
  
  
  
tags:


diagnostic_signals:




---

## 原始表述 / 核心洞察

> "AI 最容易看上去能提炼本质，但是也最不可信……我自己曾经试过跟 AI 对话，我曾经试过能不能跟 AI 两个人一起交叉着聊，把 AI 的本质聊出来，结果就是不行，AI 可以给我很多的信息和补充，但是它自己没有任何的判断力……目前 AI 距离能干活，在核心这个工作上，反正我的经验是远远不行，AI 太容易受你一点点影响。" —— Truman，`src_20260614_8269ccdb#3300-3308`

**核心洞察：**

- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **让 AI 做信息整理和初稿生成**：AI 擅长收集、分类、改写和枚举，把它放在“素材生产”位置。
2. **人做核心判断**：定义边界、选择维度、判断反例、决定停止条件，这些必须由人完成。
3. **用反例测试 AI**：给 AI 一个边界案例，观察它是否会推翻之前的定义或给出矛盾结论。
4. **换 prompt 交叉验证**：用不同角度、不同措辞问同一个问题，看 AI 的结论是否稳定。
5. **不要让 AI 主导价值观和优先级**：AI 可以列出选项，但“哪个更重要”必须由人决定。
6. **把 AI 当作高产能的实习生**：能写、能改、能查，但需要人审、人批、人负责。

## 适用边界

- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 表征 | 后果 | 纠正动作 |
|
|---|---|---|
| **AI 迎合症** | 你越聊，AI 越朝你的倾向性结论收敛，甚至主动为你的假设找理由。 | 模型失去客观性，变成“精致的偏见包装”。 | 主动引入反例、换 prompt 重问、让 AI 先列出反对意见。 |
| **边界崩塌** | 遇到边界案例，AI 给出模糊、骑墙或与之前定义矛盾的答案。 | 模型看似自洽，实则经不起真实场景检验。 | 把边界案例作为硬测试，强制 AI 明确判断并记录冲突点。 |
| **停止条件外包** | 让 AI 决定“迭代够了”“这个维度够重要”“可以收尾了”。 | 模型停留在 AI 的“合理猜测”水平，而非人的“足够好”标准。 | 人提前定义停止条件、验收标准和优先级。 |
| **价值观让渡** | AI 输出的模型里暗含了它“猜测”的价值观，而你未加审查。 | 模型指导实践时方向跑偏，决策责任不清。 | 明确列出必须由人决定的价值观/优先级，禁止 AI 默认设定。 |
| **交叉对话幻觉** | 指望和 AI 多轮对话就能“聊出本质”，结果越聊越散。 | 时间浪费，产出看似丰富但缺乏收敛。 | 人先独立形成判断，再让 AI 做补充和挑战，而非共同探索。 |

## 为什么值钱

这个暗知识防止你陷入“AI 万能论”和“AI 虚无论”两个极端。Truman 的实践表明：AI 能加 10 倍杠杆，但杠杆的支点必须是人的判断。真正稀缺的不是“让 AI 输出一个模型”，而是**知道模型是否值得相信、在什么边界内成立、对实践有什么指导价值**。

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

*老顽童 · 2026-06-14 · 基于一堂建模能力培训课程（Truman 口述）；2026-06-17 由欧阳锋复核并 enriched。*
