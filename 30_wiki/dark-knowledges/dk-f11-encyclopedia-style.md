---

id: dk-f11-encyclopedia-style
title: F-KDO-011：百科词条化→概念卡写成定义→分类→特征→应用场景
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-011
source_refs:
- 10_raw/sources/src_20260619_d967c8f5_90_control_failure_modes.md#F-KDO-011
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
  - '[[tool-strategy-lifecycle]]'
  - '[[dk-f7-surface-translation]]'
  - '[[proposal-deep-synthesis-infrastructure]]'
  - '[[dk-f9-generic-critique]]'
  - '[[dk-p4-batch-format-empty]]'
- '[[master-first-principles]]'
- '[[dk-c8-format-complete-mind-empty]]'
- '[[kdo-flywheel]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-verified-by-case
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 卡片标题或正文出现「XX 的定义」「XX 的分类」「XX 的应用」等百科词条式结构
- 正文缺少 [Condense]/[Critique]/[Synthesis] 三步编译区块标记
---
# F-KDO-011：百科词条化→概念卡写成定义→分类→特征→应用场景

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

- 你准备创建一张新概念卡， tempted 按"定义→分类→特征→应用场景"的百科结构来写
- 你审查别人提交的卡片，发现正文缺少 `[Condense]`/`[Critique]`/`[Synthesis]` 区块标记
- 你培训新 Builder 时，需要解释"知识卡片"和"百科词条"的区别
- 你设计卡片模板或 Lint 规则时，需要检测百科词条化结构

## 操作方法

1. **理解区别**：百科词条的目标是"全面描述一个概念"；KDO 概念卡的目标是"提取核心洞见 + 质疑 + 建立关联"
2. **强制三步结构**：每张概念卡必须包含三个区块：
   - `[Condense]`：3-5 条核心结论（不是定义）
   - `[Critique]`：外部攻击 + 边界 + 反例（不是应用场景）
   - `[Synthesis]`：与其他卡片的实质关联（不是分类）
3. **替换标题**：把「XX 的定义」改成「XX 的核心洞见」；把「XX 的分类」改成「XX 的适用边界」
4. **增加攻击者**：百科词条没有攻击者，KDO 卡片必须有 ≥2 位外部攻击者——这是最大的结构差异
5. **验证**：完成后问自己"这张卡能被直接复制到百度百科吗？"——如果能，说明是百科词条化，需要重写

## 适用边界

- 适用于所有 concept/tool/framework 类型的知识卡片
- 不适用于纯 reference 卡（如"术语表""人物简介"）——这些确实只需要百科式描述
- 如果源材料本身就是百科式的（如维基百科条目），三步编译法仍然适用：Condense 提取百科条目中对你最有价值的 3-5 条信息，Critique 质疑其可靠性，Synthesis 关联到已有知识
- 百科词条化和表层翻译式提炼（F-KDO-007）经常同时出现——如果检测到其中一个，应同时检查另一个
- 新 Builder 最容易犯这个错误——需要在入职培训中重点强调

## 常见失败模式

| 失败信号 | 典型表现 | 后果 |
|---|---|---|
| 标题是「XX 的定义/分类/应用」 | 卡片按定义→分类→特征→应用场景展开 | 结构完整，但缺少批判性加工 |
| 缺少 `[Critique]` 区块 | 只有 `[Condense]` 或 `[Synthesis]` | 无法识别边界与反例 |
| 应用场景被当作知识本身 | 罗列使用场景，未提炼迁移条件 | 新情境下无法复用 |
| 分类树占主导 | 用分类体系替代核心洞见 | 信息整理≠知识萃取 |
| 可被直接复制到百度百科 | 内容通用、无攻击者、无个人判断 | 卡片失去 KDO 价值 |

## 为什么值钱

- **百科词条化和知识萃取是两种完全不同的认知活动**：前者是"整理已有信息"，后者是"加工提炼出新的认知价值"
- 百科词条化的卡片极具迷惑性——它有结构、有标题、有内容，读者读完会觉得"很完整"，但实际上没有任何批判性加工
- 这是方法论混淆的经典案例：Builder 知道要"写卡片"，但不知道 KDO 的"卡片"和一般的"笔记"有什么区别
- 任何 AI 训练语料中都不会有"KDO 的概念卡不能用百科词条结构"这条知识

## 与其他知识的关联

- [[dk-f7-surface-translation]] — 交叉模式：百科词条化的卡片往往同时有表层翻译式提炼的 Condense——两者都是"用信息整理替代知识萃取"
- [[master-first-principles]] — 第一性原理：回到"知识卡片的目的"。如果目的是"萃取洞见"，那么百科词条结构就是错误的起点
- [[dk-c8-format-complete-mind-empty]] — 同构风险：格式完整≠思维完整，百科词条化是"结构正确但理解缺席"的典型
- `90_control/failure-modes.md` → F-KDO-011（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #11（不准用百科词条结构写概念卡）
