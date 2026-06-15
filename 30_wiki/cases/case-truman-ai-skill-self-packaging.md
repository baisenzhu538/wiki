---
id: case-truman-ai-skill-self-packaging
title: AI 自复盘自封装：Truman 的 design case 技能是如何让 AI 自己包装出来的
type: case
source_refs:
- src_20260614_8269ccdb
status: enriched
confidence: 0.7
domain:
- yitang
- ai-collaboration
created_at: '2026-06-14'
author: 黄药师（基于 Truman 口述提取）
reviewed_by: 黄药师
review_date: '2026-06-14'
trust_level: medium
related:
- '[[modeling-capability-for-kdo]]'
- '[[modeling-three-stages]]'
- '[[case-truman-livestream-sop-iteration]]'
- '[[modeling-to-kdo-toolchain]]'
- '[[case-truman-ai-skill-engineering-guide]]'
tags:
- '#domain/skill-engineering'
- '#content-format/case-study'
- '#self-improvement'
- '#domain/yitang'
diagnostic_signals:
- signal: 每次做AI项目都要重新调prompt，做完就丢了
  framework_lens: AI自复盘——让AI总结这次经验变下次基础
  follow_up_question: 你最后一次项目结束时，有没有让AI扫描你全程的纠偏记录、自动生成一个skill？
- signal: 我的AI技能库都是人手工整理的，效率很低
  framework_lens: 让AI跨工具扫描+合并同类项+封装
  follow_up_question: 你用过哪些AI工具？它们的对话/反馈记录是明文存储的吗？如果是，可以直接让另一个AI去读。
source_context: （单一 source 为完整长文档，内容充分支撑 high trust） （单一 source，P1 收尾时从 high 降为 medium，待补充第二来源或充分验证后再升回
  high）
updated_at: '2026-06-16'
---
# AI 自复盘自封装：Truman 怎么让 AI 把自己包装成一个技能

> **Burn line**: 不是人写 skill——是 AI 扫描你所有的纠偏记录，自己把自己的经验封装成 skill。

---

## 一、人话版摘要

Truman 花了两周做了大量课程插图和 PPT，中间跟 AI 来回纠偏无数次——"颜色不对""流程不对""缺了某个东西"。活干完之后，他没有总结，而是让 Cubox 去扫描所有 AI 工具里的纠偏记录，自动合并同类项，输出一个叫 "design case" 的技能包。

这个技能包比他自己预期的好得多，包含：使用场景、审美底盘、协作流程（先发散再收敛→先看懂参考→每轮只搞一个主问题→诚实判断可控性）、track list、评审表、不同类型的图应该考虑什么、硬性坑清单。

整个过程 AI 自己做，他只需喷一段提示词。

---

## 二、五步自封装流程

### Step 1：标记扫描范围

让一个 AI（如 Cubox/Codex）去读其他 AI 工具的本地存储。关键前提：**这些工具的对话和反馈记录是明文存的。**

> "我说你帮我扫描12345，你帮你把别的这个工具你帮我去扫描一下它的数据库。"

### Step 2：定义输出目标

只需一句话："帮我做一个叫 design case 的技能"。

不需要定义技能格式、字段、分类——AI 自己会从纠偏记录里反推。

### Step 3：AI 自动合并同类项

AI 扫描完所有纠偏记录后，自动：

- **分类**：颜色问题归一类，流程问题归一类，缺失元素归一类
- **拆维度**：审美底盘 / 协作流程 / 评审表 / 硬性坑
- **控工作流**：先发散再收敛，每轮只搞一个主问题

> "告诉我把我的建议合并同类项给我做一个拆分例子。"

### Step 4：AI 生成结构化 skill

输出包含：

| 组成部分 | 说明 |
|:--|:--|
| 使用场景 | 什么时候调用这个 skill |
| 审美底盘 | 可接受/不可接受的视觉标准 |
| 协作流程 | 先看懂参考 → 先发散再收敛 → 每轮一个主问题 |
| track list | 检查项清单，逐项打勾 |
| 评审表 | 不同类型图要考虑什么 |
| 硬性坑 | "出现一次我喷一次"→ 自动提取为禁止项 |

### Step 5：下次迭代时自吸收

下次再做图时，AI 基于这个 skill 自动执行，明显聪明很多。

> "以后下一次再做的时候，它会基于这个再去做，下一次就会明显聪明很多。"

---

## 三、为什么这比人手工整理强

| 人手工整理 skill | AI 自封装 |
|:--|:--|
| 靠记忆，容易忘 | 扫描全部记录，不遗漏 |
| 提炼成本高，一个小时起步 | AI 几分钟完成 |
| 分类维度靠人判断，可能有盲区 | AI 合并同类项，发现人没注意到的模式 |
| 只总结，不自执行 | 下次自动执行 |

---

## 四、前提条件

1. **AI 工具的记录必须是可读的。** Cubox、Antigravity 等本地工具大多用明文存。（Truman 原话："本地几乎都是用文档和数据库的方式存的"）
2. **需要一个能跨工具扫描的 AI。** Codex 可以翻 Antigravity 的数据库。
3. **关键词驱动。** "你只要指定关键词，它几乎都能扫出来。"

---

## 五、可迁移：KDO 怎么用这个模式

| Truman 的做法 | KDO 可直接复用 |
|:--|:--|
| 工作完成 → AI 扫描全记录 → 封装 skill | 老顽童写卡完成 → AI 扫描 source/correction/diagnosis → 自动生成下次写卡的注意事项 |
| 纠偏记录 = skill 素材 | `60_feedback` = 知识卡迭代的素材 |
| track list = QA 门禁 | 自迭代检测器 (Task M/N/Q/S) = KDO 的 track list |

**KDO 最应该做的**：让 AI 定期扫描 `60_feedback/corrections/` 下的纠正记录，自动提出新的门禁规则建议。

---

## 六、反模式

| 反模式 | Truman 的做法 |
|:--|:--|
| 做完就丢，不总结 | 做完立刻让 AI 扫描封装 |
| 人手工总结 | AI 自动合并同类项 |
| 技能库靠人维护 | 每次项目结束自动更新 skill |
| 只总结不执行 | skill 含 track list，下次自动检查 |

---

## Open Questions

- KDO 什么时候能有这个能力？——让 AI 扫描 `60_feedback/` 自动生成门禁规则。
- 跨工具扫描的前提是"记录可读"——Hermes 的 session 记录是明文吗？
- 如果老顽童每完成一个域就让 AI 自动封装一个 skill，产能能提多少？

---

黄药师 · 2026-06-14 · 源材料：Truman 高阶建模课口述第 1194-1234 行
