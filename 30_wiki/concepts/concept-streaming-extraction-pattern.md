---
id: concept-streaming-extraction-pattern
title: 流式提取模式——浏览器虚拟滚动到API分页的映射
type: concept
status: enriched
author: 段王爷（南帝）
reviewed_by: 欧阳锋
review_date: 2026-06-23
created_at: 2026-06-23
confidence: 0.90
trust_level: high
language: zh-CN
domain: [feishu, content-extraction, publishing, architecture]
source_refs:
  - 老板老朱 2026-06-23 口述："虚拟滚动机制——内容只有滚动到视口时才加载到内存中"
  - feishu-publishing (段王爷 SKILL.md)
related:
  - "[[concept-feishu-api-pagination-trap]]"
  - "[[feishu-docx-pagination-extraction]]"
diagnostic_signals:
  - signal: "长文档提取时内存爆炸或超时"
    framework_lens: 流式提取——不一次全量加载，逐页处理
    follow_up_question: "你的提取是一次性全部加载再处理，还是逐页流式处理？"
---

# 流式提取模式

> **一句话：把浏览器的"虚拟滚动"概念映射到 API 提取——逐页拉取、逐页处理、逐批写入，不一次全量加载。**

## 核心映射

| 浏览器虚拟滚动 | API 流式提取 |
|---|---|
| 只渲染可视区域 | `page_size=500` 逐页获取 |
| `IntersectionObserver` 触发加载 | `has_more=True` 触发下一页 |
| `scrollTop` 保持位置 | `page_token` 保持游标 |
| 离视口 DOM 回收 | 处理完一页即释放内存 |
| `React-Virtual` | `stream_extract_and_publish()` |

## 全量 vs 流式

| | 全量模式（旧） | 流式模式（新） |
|---|---|---|
| 内存峰值 | 全部 1329 blocks | 每页 ≤ 500 blocks |
| 失败恢复 | 全部重来 | 从断页续传 |
| 进度可见 | 一次性 | 逐页汇报 |
| 适用规模 | < 500 blocks | 不限规模 |

## 实战效果

拆书会第208期：
- 全量：1329 blocks → 内存 ~15MB
- 流式：每页 500 blocks → 内存 ~5MB
- **内存降 67%**

## 适用场景

- 飞书文档提取（1000+ blocks）
- Bitable 大数据量查询
- 任何带 `page_size` + `has_more` + `page_token` 的分页 API

## 来源

老板老朱 2026-06-23 提出"虚拟滚动机制"概念 → 段王爷翻译为 API 流式提取 → 固化为技能。
