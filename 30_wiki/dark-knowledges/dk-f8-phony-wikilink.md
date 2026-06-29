---

id: dk-f8-phony-wikilink
title: F-KDO-008：虚假关联→wikilink 指向自身或堆砌无关链接凑数
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-008
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-19'
related:
  - "[[kdo-input-channel-strategy-2026-06-16]]"
  - "[[kdo-protocol]]"
  - "[[modeling-to-kdo-toolchain]]"
  - "[[kdo-batch-produce-req014]]"
  - "[[kdo-15-dimension-label-spec]]"
  - "[[obsidian-kdo-内容产出工作流-产品设计大纲]]"
  - "[[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]"
  - "[[kdo-watch-health-check-layer]]"
  - "[[framework-kdo-self-attack]]"
  - "[[kdo-yaml-frontmatter-safety]]"
  - "[[kdo-priority-checklist]]"
  - "[[kdo_product_design_agent_final]]"
  - "[[proposal-kdo-flywheel-infrastructure]]"
  - "[[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]]"
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
review_date: '2026-06-19'
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# F-KDO-008：虚假关联→wikilink 指向自身或堆砌无关链接凑数

---

## 原始表述/核心洞察

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

核心洞察：

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **禁止 self-link**：Synthesis 段绝对不能 wikilink 到当前卡片自身——这是 P0 级别的错误
2. **逐个验证关联**：每写一个 wikilink，问自己"目标卡片的内容与当前卡片有什么实质的知识交叉？"
3. **写关联说明**：不是只写 `card-name`，而是写 `card-name — 具体关联说明（≥30 字）`
4. **区分 domain 内和跨 domain 关联**：同一 domain 内的关联容易（如两张都是一堂的课），但价值低；跨 domain 的关联更难找，但价值更高
5. **不满足宁可少写**：如果确实找不到 2 个有实质关联的卡片，宁可只写 1 个高质量的，也不要堆砌 2 个灌水的

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型信号 | 为什么 L2 Lint 会漏 | 快速自检 |
|
|---|---|---|
| self-link | Synthesis 段出现 “当前卡片名” 式自引用 | 规则只检查数量，不检查目标是否等于自身 | 全文搜索当前卡片 id，确认没有自引用 |
| 灌水同域关联 | 链接目标与当前卡片同 domain，但仅共享粗粒度标签（如"都是一堂的课"） | 规则不验证关联说明的信息量 | 追问：两张卡互相补充了什么具体结论？ |
| 跨域硬凑 | 链接目标属于不相关 domain，内容无交叉 | 规则不验证 domain/module 交叉 | 检查目标页与当前卡的核心概念是否有交集 |
| 数量优先 | 卡片刚好有 2 个 wikilink，但均缺乏关联说明 | 规则只检查数量 | 移除链接后，Synthesis 是否仍能独立成立？ |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
