---
id: dk-f8-phony-wikilink
title: "F-KDO-008：虚假关联→wikilink 指向自身或堆砌无关链接凑数"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "failure-modes.md F-KDO-008"
source_refs:
  - 90_control/failure-modes.md#F-KDO-008
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c8-format-complete-mind-empty
  - master-decision-hygiene
contradicts:
  - dk-c8-format-complete-mind-empty
  - master-decision-hygiene
pipeline:
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---

# F-KDO-008：虚假关联→wikilink 指向自身或堆砌无关链接凑数

## 原始表述

> **触发场景**：Builder 执行三步编译法的 Synthesis 阶段
>
> **表现**：Synthesis 段的 wikilink 出现以下情况之一：① wikilink 指向自身（A 卡 link 了 A）② 灌水关联（"A 和 B 都是一堂的课"这种无信息量的链接）③ 为满足 ≥2 个 wikilinks 的机械要求而堆砌无关链接
>
> **根因**：Builder 为通过 L2 Lint 的"Synthesis ≥ 2 个 wikilinks"规则而凑数，而非真正寻找知识关联
>
> **触发信号**：Synthesis wikilink 目标与当前卡片的 domain/module 无实质交叉；或 link 了自己
>
> **防御措施**：① L2 Lint：检测 self-link（直接报 P0）② 审查时检查每个 wikilink 目标页面的内容是否与本卡有实质关联
>
> **关联案例**：yt-entrepreneur-scientific-method.md Synthesis 段 wikilink 了自己（2026-05-08 审查）

## 使用场景

- 你正在写概念卡的 Synthesis 段， tempted 随便找两张已有卡片贴上 wikilink 以满足"≥2 个"的硬性要求
- 你审查别人提交的卡片，需要判断 Synthesis 中的 wikilink 是实质关联还是凑数
- 你设计 L2 Lint 规则时，需要检测 self-link 和灌水关联
- 你发现一张卡片的 related 字段链接了不相关域的卡片，需要判断是否属于虚假关联

## 操作方法

1. **禁止 self-link**：Synthesis 段绝对不能 wikilink 到当前卡片自身——这是 P0 级别的错误
2. **逐个验证关联**：每写一个 wikilink，问自己"目标卡片的内容与当前卡片有什么实质的知识交叉？"
3. **写关联说明**：不是只写 `card-name`，而是写 `card-name — 具体关联说明（≥30 字）`
4. **区分 domain 内和跨 domain 关联**：同一 domain 内的关联容易（如两张都是一堂的课），但价值低；跨 domain 的关联更难找，但价值更高
5. **不满足宁可少写**：如果确实找不到 2 个有实质关联的卡片，宁可只写 1 个高质量的，也不要堆砌 2 个灌水的

## 适用边界

- 适用于所有需要写 Synthesis wikilink 的场景
- 不适用于目录页/索引页的导航链接——索引页的目的就是收集相关链接，不需要每个都写关联说明
- 如果卡片是新域的第一张卡（没有已有卡片可关联），可以暂时只链接到 master 域的通用概念卡，但后续新卡产出后必须回头补齐
- "实质关联"的标准：两张卡片的知识内容互相补充、互相质疑、或可以迁移应用——"都是一堂的课"不算实质关联
- 不同审查者对"实质关联"的判断可能有差异——有争议时以欧阳锋的判定为准

## 为什么值钱

- **虚假关联破坏的是整个 Graph RAG 网络的可信度**：如果 wikilink 只是凑数的，用户通过关联导航找到的内容与当前主题无关，Graph RAG 的检索质量会系统性下降
- 这是"指标驱动"陷阱的典型表现：L2 Lint 规定了"≥2 个 wikilinks"，Builder 为了满足指标而牺牲了质量
- 自我引用（self-link）尤其恶劣——它不仅没有任何信息增益，还会让 Graph RAG 陷入循环
- 任何 AI 训练语料中都不会有"KDO 的 Synthesis wikilink 不能自我引用"这条知识

## 与其他知识的关联

- dk-c8-format-complete-mind-empty — 同一模式："格式完整但思维空洞"。C-8 是 Constraints 节空洞，F-KDO-008 是 Synthesis 段空洞——两者都是"为满足格式要求而填充无价值内容"
- master-decision-hygiene — 决策卫生 Step 3（独立评估）：每个 wikilink 都需要独立验证其关联的实质价值，不能让写卡的人自己判定"够了"
- `90_control/failure-modes.md` → F-KDO-008（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #8（不准在 Synthesis 中堆砌无实质关联的 wikilink）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
