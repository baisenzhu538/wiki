---
id: concept-kdo-feature-registry
title: "KDO Feature 注册表：原子化最小技术单位"
type: concept
status: draft
domain:
  - kdo
  - master
author: 黄药师
reviewed_by: 待审
review_date: 2026-08-08
confidence: 0.85
trust_level: observed
source_refs:
  - 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
  - cap_hub/features.json
created_at: 2026-08-08
updated_at: 2026-08-16
tags:
  - audience:huangyaoshi
  - scene:reference
  - skill-level:advanced
aliases:
  - Feature注册表
  - KDO Feature
  - 原子能力清单
discoverable_by:
  - Feature注册表
  - KDO Feature
  - 原子能力
diagnostic_signals:
  - signal: 'KDO 能力以"任务单"为粒度——#217 一次加了三个 Feature，独立性和可测试性差'
    severity: medium
    implication: '新 Feature 加入时没有原子化注册——不知道当前有哪些 Feature、各自什么状态'
  - signal: 'cap_hub 以工具为单位而非 Feature——Agent 看到的是一堆脚本而不是原子能力'
    severity: medium
    implication: 'Agent 启动时无法快速了解 KDO 到底能做什么'
related:
  - '[[concept-kdo-component-library]]'
  - '[[framework-kdo-modeling-methodology]]'
  - '[[kdo-moc]]'
  - '[[master-moc]]'
  - '[[framework-kdo-self-attack]]'
  - '[[dk-tool-chain-naming-is-infrastructure]]'
---

# KDO Feature 注册表

> **定位**：属于 KDO 工厂建设——Feature 注册表是 cap_hub 的组织原则。与 concept-kdo-component-library（17 张通用牌）互补：组件库是行为牌，Feature 注册表是原子能力清单。

> **来源**：Truman Feature 思维（口述 L1402-1450）——"所有工具拆完一共也就几十个特性。不要盯着工具名，盯着最小的技术特性。可操作、可测试、可组合。"

## 什么是 Feature

Feature = KDO 的原子化最小技术单位。每个 Feature：
- **独立可测**：一条命令 / 一个测试用例验证
- **独立可组合**：不依赖其他 Feature
- **独立可迭代**：修一个不影响其他

Feature ≠ Skill。Skill 是封装逻辑，Feature 是原子特性。

## 20 个已注册 Feature

| ID | 名称 | 分类 | 独立测试 |
|:--|:--|:--|:--|
| F1_UPDATED_AT | updated_at 必填 | 门禁 | 缺 updated_at → ERROR |
| F2_BACKLINK | 双向链接 | 门禁 | A→B 无回链 → ERROR |
| F3_DUPLICATE_ID | 重复 ID 检测 | 门禁 | 同 id 两文件 → ERROR |
| F4_MOC_DEADLINK | MOC 死链 | 门禁 | MOC 死链 → ERROR |
| DK_7_SECTIONS | dk 七段 | 门禁 | 缺 Critique → ERROR |
| SEC_TYPO | 段名拼写 | 门禁 | Critque → ERROR |
| R6_SEARCH | 搜索可达性 | 门禁 | 空 title → ERROR |
| DUP_KEY | 重复键阻断 | 门禁 | 双 aliases → ERROR |
| REVIEW_MARK | 终审标记 | CLI | review_mark --dry-run |
| REACH_CHECK | 可发现性自查 | CLI | reachability-check.py |
| HINT_MAP | 错误场景化提示 | UX | 错误输出带修复建议 |
| CARD_CHECKLIST | 复审自检 | CLI | checklist.py 全 PASS |
| AUTH_FRESHNESS_SLA | 认证新鲜度 SLA | 门禁 | 缺 reverify_by → ERROR |
| DECISION_CLASSIFY | 决策分类 | CLI | kdo decision add |
| SKILL_CRYSTALLIZE | 经验→技能结晶 | CLI | 扫描复盘→draft skill |
| SKILL_LIFECYCLE | Skill 生命周期 | CLI | draft→published→deprecated |
| R1_REVIEW_INFRA | lint 审查四类规则 | 门禁 | R1-a~R1-d |
| SKILL_BRIDGE_SYNC | 双轨 Skill 同步 | CLI | shared→.claude 单向同步 |
| FEISHU_DOC_MCP | 飞书文档操作 | CLI | lark-cli create/fetch/update |


## 使用方式

- 新 Feature 加入：先注册到 `cap_hub/features.json`，再实现
- 启动时查询：`python -m cap_hub list` 显示全部 Feature
- 原子化原则：一个 Feature = 一个独立测试用例 = 一个注册条目

## Feature 设计原则（来自 Truman 口述）

1. **不被工具带走**：新工具火了 → 看它比现有工具多了哪几个 Feature → 需要就加，不需要就不加
2. **特性清单 = 武器库**：把所有能力打开，打成 Feature 清单，沿着清单工作
3. **可测试是底线**：因为是"可操作的最小单位"，所以每一个都能测——不测的不注册
