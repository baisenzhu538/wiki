---
id: dk-E010-duplicate-key-detection
title: E010：frontmatter重复键——一次批量写入摧毁2350张卡的根因
type: dk
status: reviewed
domain: kdo
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.95
trust_level: medium
aliases:
- E010
- 重复键检测
- 双aliases事故
- 并行写入事故
- DUPLICATE KEY
source_refs:
- 60_feedback/tasks/task_20260803_huangyaoshi-duplicate-key-lint.md
- 90_control/scripts/kdo_lint.py
diagnostic_signals:
- signal: '#222/#223事故后lint仍无重复键检测——DUPLICATE_KEY门禁缺失'
  severity: critical
  implication: 任何老顽童提交的双aliases卡片都不会被拦截——事故会重演
- signal: 存量131张卡含重复键——现在提交都不会被拦
  severity: high
  implication: 王语嫣验证：lint确实无同文件重复键检测
- signal: 欧阳锋洞察：一行正则即可永久封堵事故根因模式
  severity: low
  implication: 实现成本极低——与F3同模式
related:
- '[[concept-kdo-component-library]]'
- '[[framework-kdo-self-attack]]'
- '[[dk-c8-format-complete-mind-empty]]'
- '[[dk-P42-agent-fact-check-gap]]'
- '[[dk-delivery-path-type-bug]]'
- '[[dk-c5-todo-false-positive]]'
created_at: 2026-08-04
updated_at: 2026-08-04
review_date: 2026-08-04
tags:
- audience:builder
- scene:reference
- skill-level:advanced
discoverable_by:
- E010
- 重复键检测
- 双aliases
- 并行写入事故
- frontmatter破坏
---
# E010：frontmatter重复键——一次批量写入摧毁2350张卡

> **定位**：属于 KDO 事故教训库的 E 系列——E010 是 #222/#223 并行写入事故的终极防线缺口。与 #217 F3（跨文件重复 ID 检测）同模式、同文件。


## 原始表述

2026-08-03，#222（飞书老顽童）和 #223（hermes 老顽童）两个实例并行执行 aliases 回填。两个实例都用"追加 aliases 块"模式——在已有 frontmatter 中插入新 `aliases:` 块而非合并。结果 ~2,350 张卡 YAML 全坏。

如果 pre-submit 有 `^aliases:` 出现 ≥2 次 → ERROR 的检测——246 张双 aliases 会在提交时被拦截，整个事故根本不会发生。

## 使用场景

- 批量写入任何 frontmatter 字段前，跑 lint 验证
- 审查老顽童批量任务交付时
- 设计新 pre-submit 门禁规则时参考

## 操作方法

`kdo lint` 已内置 DUPLICATE_KEY 检测（#228）——对 aliases/tags/related/diagnostic_signals/discoverable_by/source_refs 六个关键字段做重复键检查。重复键 → ERROR 阻断提交。正常卡不受影响。

## 适用边界

- 检测覆盖六个标准键，非标准键需手动更新 DUPLICATE_CHECK_KEYS
- 不检测语义重复（两个 aliases 块内容相同但 key 名不同）
- 第一版只拦新提交，不追溯存量（存量纳入 #223 恢复）

## 为什么值钱

1. 防止 C-10 级事故重演——一次批量写入破坏 2,350 张卡
2. 零成本——一行正则 + 一个 for 循环
3. 可推广——同模式可用于任何"同键不可重复"的校验场景

## 与其他知识的关联

- #217 F3 重复 ID 检测（跨文件）→ 同模式，同文件内
- #222/#223 事故根因 → 直接来源
- concept-kdo-component-library 牌 #14（先跑脚本确认再下结论）

## Critique

### 内部局限
- 只检测六个标准键，新增字段需手动更新
- 不检测语义重复

### 外部挑战
- "重复键检测 = 事后补救，真正的防线是禁止并行写入"——#227 修复后已改串行+目录划分
- "YAML 允许重复键"——PyYAML 允许，但 Obsidian/Graph RAG/搜索索引不认第二个值
