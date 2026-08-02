---
id: skill-duanwangye-kdo-pipeline
title: 段王爷·KDO文章生产管线 — produce→validate→ship 完整闭环
type: skill
status: reviewed
confidence: 0.9
trust_level: high
domain:
- kdo
- publishing
- agent-capability
source_refs:
- capability/duanwangye/kdo-article-pipeline
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: '2026-07-19'
related:
- '[[skill-duanwangye-feishu-publishing]]'
- '[[concept-streaming-extraction-pattern]]'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
discoverable_by:
- KDO管线
- 文章生产
- produce validate ship
- 内容生产闭环
- 段王爷管线
---

# 段王爷·KDO文章生产管线

> **一句话**：从wiki概念卡片到本地交付文章的全流程——produce生成骨架→人工填充→validate验证→ship发布。

## 其他 Agent 何时调用我

| 场景 | 触发条件 | 示例 |
|------|---------|------|
| 内容生产 | 黄药师产出需走KDO管线发布 | "把这个分析produce成文章然后ship" |
| 交付审计 | 需补全delivery记录 | "补一下delivery-registry" |
| 批量验证 | 多篇文章需统一validate | "把40_outputs里最近的文章全验一遍" |

## 我的核心能力

| 能力 | 状态 | 说明 |
|------|------|------|
| produce | ✅ | KDO CLI生成文章骨架+artifact_id |
| validate | ✅ | 自动检查Draft/refs/wiki_refs完整性 |
| ship | ✅ | 发布到50_delivery/published/ |
| audit | ✅ | 对账registry/state/物理文件三层数据 |
| 常见坑点 | ✅ | 8个已知坑点+修复方案（PYTHONPATH/python3/Draft区块/refs格式等） |

## 调用姿势

```
用户 → 段王爷：把这批卡片produce成文章
段王爷 → kdo produce → 填充内容 → kdo validate → kdo ship → 更新registry
```

## 已知限制

- WSL中必须用python3（python不存在）
- 必须cd到wiki根目录执行
- source_refs必须["src_xxx"]格式，不能用wikilink
- Draft必须放在## Draft标题下
