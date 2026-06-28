---


id: dk-f11-encyclopedia-style
title: F-KDO-011：百科词条化→概念卡写成定义→分类→特征→应用场景
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-011
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- [[tool-strategy-lifecycle]]
- [[dk-f7-surface-translation]]
- [[proposal-deep-synthesis-infrastructure]]
- [[dk-f9-generic-critique]]
- [[dk-p4-batch-format-empty]]
- [[master-first-principles]]
- [[dk-c8-format-complete-mind-empty]]
- [[kdo-flywheel]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown# F-KDO-011：百科词条化→概念卡写成定义→分类→特征→应用场景
---
## 原始表述

> **触发场景**：Builder 创建知识卡片时
>
> **表现**：概念卡写成百科词条结构——「定义 → 分类 → 特征 → 应用场景」——而非三步编译（浓缩→质疑→对标）。这种卡"看起来完整"但没有经过批判性加工
>
> **根因**：Builder 用百科词条的 mental model 理解"知识卡片"，混淆了"信息整理"和"知识萃取"
>
> **触发信号**：卡片正文缺少 `[Condense]`/`[Critique]`/`[Synthesis]` 区块标记；或标题为「XX 的定义」「XX 的分类」「XX 的应用」
>
> **防御措施**：① L2 Lint：检测是否包含三步编译法的三个强制区块标记② Concept Card Step 0：Builder 在写卡前必须确认理解三步编译法与百科词条的区别
>
> **关联**：与 F-KDO-007（表层翻译式提炼）有交叉——百科词条化的卡往往同时有表层翻译式提炼的 Condense

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **理解区别**：百科词条的目标是"全面描述一个概念"；KDO 概念卡的目标是"提取核心洞见 + 质疑 + 建立关联"
2. **强制三步结构**：每张概念卡必须包含三个区块：
   - src_unknown
   - src_unknown
   - src_unknown
3. **替换标题**：把「XX 的定义」改成「XX 的核心洞见」；把「XX 的分类」改成「XX 的适用边界」
4. **增加攻击者**：百科词条没有攻击者，KDO 卡片必须有 ≥2 位外部攻击者——这是最大的结构差异
5. **验证**：完成后问自己"这张卡能被直接复制到百度百科吗？"——如果能，说明是百科词条化，需要重写

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败信号 | 典型表现 | 后果 |
|
|---|---|
| 标题是「XX 的定义/分类/应用」 | 卡片按定义→分类→特征→应用场景展开 | 结构完整，但缺少批判性加工 |
| 缺少 `[Critique]` 区块 | 只有 `[Condense]` 或 `[Synthesis]` | 无法识别边界与反例 |
| 应用场景被当作知识本身 | 罗列使用场景，未提炼迁移条件 | 新情境下无法复用 |
| 分类树占主导 | 用分类体系替代核心洞见 | 信息整理≠知识萃取 |
| 可被直接复制到百度百科 | 内容通用、无攻击者、无个人判断 | 卡片失去 KDO 价值 |

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
- src_unknown
