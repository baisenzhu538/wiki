---

id: dk-modeling-ai-self-retrospection
title: AI 也会重复犯同样的错：每次漂亮交付后，必须让它当场总结一个自查清单
type: dk
dark_knowledge_type: workflow
status: enriched
domain:
- yitang
- ai-saas
source_person: Truman
source_context: 一堂建模能力培训（AI 辅助建模案例），2026-06-12
source_refs:
- 10_raw/sources/src_20260614_8269ccdb-一堂-建模能力培训-truman-口述.md
- 10_raw/sources/src_20260614_42f1e977-一堂-建模能力培训-truman-笔记.md
created_at: '2026-06-14'
updated_at: '2026-06-18'
related:
  - [[yitang-domain-digest]]
  - [[tool-制作行业化要素检查清单]]
  - [[tool-月白-供应商信息对齐清单法]]
  - [[ocr-一堂-案例拆解-课程清单]]
  - [[tool-稀缺资源清单]]
  - [[tool-清单式笔记法]]
  - [[tool-用清单体记备忘笔记]]
  - [[tool-月白-工厂对接信息清单制作]]
  - [[轻量级诊所HIS调研全清单]]
  - [[tool-清单小抄工具箱法]]
  - [[ocr-一堂-科学决策-稀缺资源清单]]
  - [[ocr-一堂-科学决策-关键训练清单重要]]
  - [[ocr-一堂-ai清单体笔记系统故事线-truman-图片01]]
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
trust_level: high
reviewed_by: 欧阳锋
review_date: '2026-06-18'
author: 老顽童
confidence: 0.89
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown# AI 也会重复犯同样的错：每次漂亮交付后，必须让它当场总结一个自查清单

---

## 原始表述 / 核心洞察

> 我最近建议所有一堂的同学要尝试养成一个习惯：让 AI 学会自己复盘自己。不是 AI 帮助人复盘，而是它帮助自己复盘。你做了一个工作，做得很漂亮，过去人要总结这个经验是非常难的，ROI 很低。现在你要习惯性地让 AI 当场立刻就总结一个自查清单，把这一次的经验自动化地变成下一次的基础。这个工作其实还挺重要的。比如我当时跟好几个平台去做课程插图和 PPT，过程中不断纠偏：这个图颜色不对、这个图流程不对、这个图缺了个什么东西。交完活之后，我让一个 agent 扫描所有对话窗口，把所有反馈合并同类项，封装了一个叫 Design Taste 的技能。下一次再做的时候，它会基于这个再去做，明显聪明很多。AI 自己干活，AI 自己复盘，AI 下次自己吸收，这个循环会越来越快。

**核心洞察**：AI 协作的真正复利不在于单次生成更快，而在于让 AI 把一次成功交付的纠偏经验自动沉淀为自查清单 / skill，下一次任务先自查、再交付。这样 AI 从"每次都从头教的新实习生"变成"越用越顺手的老员工"。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **只在"漂亮交付"后做**
   复盘的对象必须是一次你满意的输出。失败的交付也能复盘，但优先把成功经验固化。

2. **当场立刻做**
   在对话上下文还热乎的时候做，不要等几天。因为：
   - src_unknown
   - src_unknown
   - src_unknown

3. **指定扫描范围**
   让 AI 扫描：
   - src_unknown
   - src_unknown
   - src_unknown
   明确关键词，避免扫进无关内容。

4. **强制输出一个自查清单**
   不要让它泛泛总结"要注意设计"。要让它输出：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

5. **封装成可复用资产**
   把清单变成：
   - src_unknown
   - src_unknown
   - src_unknown
   下次同类任务先加载这个资产。

6. **下次任务先自查**
   交付前让 AI 用上次总结的技能给自己打分，而不是等人来喷。

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型症状 | 修复方法 |
|
|---|---|
| 过早封装 | 只成功一次就总结成 skill，下次任务反而被僵化规则束缚 | 累积 2–3 次样本，区分"通用规则"与"单次特例" |
| 扫描范围过宽 | 自查清单混入无关反馈，出现相互矛盾的要求 | 限定对话窗口/文件范围，明确关键词与任务边界 |
| 只总结不加载 | 清单写在对话里，下次没加载，AI 继续犯错 | 立即导出为 skill / system prompt / eval case，并在新任务开头加载 |
| 人放弃终审 | AI 归因错误，把正确方向当成错误来规避 | 人必须逐条审校，尤其是 P0 级规则 |
| 复盘失败交付 | 把错误样本固化成规则，导致错误复利 | 优先复盘漂亮交付；失败案例只用于补充"Not To Do" |
| 清单过度冗长 | 几十条规则导致 AI 执行时忽略重点 | 按 P0/P1/P2 分级，每次任务只强制加载 P0 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
