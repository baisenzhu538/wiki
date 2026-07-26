---
id: dk-p11-regex-cutoff
title: P-11：validator `section_content` regex 在 `###` 处截断——所有文章 word count 失效
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: pitfalls.md P-11
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-18'
related:
- '[[ai-short-drama-ice-fire-dissection-compass]]'
- '[[writing-content]]'
- '[[tool-strategy-12-word-test]]'
- '[[dk-c1-cjk-regex-silent-fail]]'
- '[[case-toc-content-platform-correlation-trap]]'
- '[[tool-yitang-content-ip-research]]'
- '[[tool-note-keyword-bolding]]'
- '[[case-lean-zhanglei-failure-counterfactual]]'
- '[[dk-f1-regex-on-cjk]]'
- '[[dk-tool-as-phased-validator]]'
- '[[yt-lean-b2b-b2c-hardware-content-testing]]'
diagnostic_signals:
- src_unknown
- src_unknown
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium# P-11：validator `section_content` regex 在 `###` 处截断——所有文章 word
  count 失效
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
---

## 原始表述

> **症状**：一篇1800字完整文章，`kdo validate` 报 "Draft section is empty (0 words)"。加了内容后仍只统计到46 words。
>
> **根因**：`validation.py:section_content()` 的正则 `(?=^##|\Z)` 用 `^##` 作为section结束标记。`###` 行以 `##` 开头，被正则误判为同级heading，导致提取只截取到第一个 `###` 之前的文字。所有使用三级标题的文章（几乎全部）都命中此bug。
>
> **对策**：
> - **临时绕路**：在 `## Draft` 和第一个 `### Part N` 之间插入一段引导文字
> - **根治**：将正则改为 `(?=^##(?!#)|\Z)` 或 `(?=^##\s|\Z)`——只匹配同级 `## ` heading，不匹配更深级别
> - **优先级**：P0——阻塞所有文章类artifact的有意义验证

## 核心洞察

基于正则的 Markdown heading 解析器如果只用前缀匹配（`^##`），会把更深级别的标题（`###`）误判为同级标题边界，导致 section 被提前截断。这个 bug 极具隐蔽性：内容看起来完好，但验证/统计结果严重失真。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别 regex 截断问题**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **临时绕过**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **根治修复**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **regex 设计原则**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 症状 | 根因 | 修复/绕过 |
|
|---|---|---|
| 内容被误报为空 | `kdo validate` 报 "Draft section is empty (0 words)" | regex `(?=^##|\Z)` 把 `###` 当作 section 结束边界 | 改为 `(?=^##(?!#)\|\Z)` 或 `(?=^##\s\|\Z)` |
| word count 远小于实际 | 1800 字文章只统计到 46 words | section 提取在第一个 `###` 处截断 | 在 `## Draft` 与第一个 `###` 之间插入引导文字临时绕过 |
| 强制绕过导致数据失真 | 手动改字数或删标题让验证通过 | 未修复 regex，掩盖真实 bug | 修复 regex 并跑全量回归测试 |

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
