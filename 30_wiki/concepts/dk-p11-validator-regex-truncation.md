---
id: dk-p11-validator-regex-truncation
title: "P-11：validator `section_content` regex 在 `###` 处截断——所有文章 word count 失效"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-11"
source_refs:
  - .agent/pitfalls.md#P-11
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c1-regex-on-cjk
  - master-systems-thinking
---

# P-11：validator `section_content` regex 在 `###` 处截断——所有文章 word count 失效

## 原始表述

> **症状**：一篇1800字完整文章，`kdo validate` 报 "Draft section is empty (0 words)"。加了内容后仍只统计到46 words。
>
> **根因**：`validation.py:section_content()` 的正则 `(?=^##|\Z)` 用 `^##` 作为section结束标记。`###` 行以 `##` 开头，被正则误判为同级heading，导致提取只截取到第一个 `###` 之前的文字。所有使用三级标题的文章（几乎全部）都命中此bug。
>
> **对策**：
> - **临时绕路**：在 `## Draft` 和第一个 `### Part N` 之间插入一段引导文字
> - **根治**：将正则改为 `(?=^##(?!#)|\Z)` 或 `(?=^##\s|\Z)`——只匹配同级 `## ` heading，不匹配更深级别
> - **优先级**：P0——阻塞所有文章类artifact的有意义验证

## 使用场景

- 你运行 `kdo validate` 时发现文章的 word count 严重偏低（如 1800 字文章只统计到 46 字）
- 你在写使用三级标题（`###`）的文章，需要确认 validator 能正确解析
- 你在调试 `kdo validate` 的结果时，需要判断是"文章真的太短"还是"validator 有 bug"
- 你在修改 KDO 的验证逻辑时，需要理解 regex 边界的细节

## 操作方法

1. **识别症状**：如果文章明明很长但 validator 报 "0 words"或极低的字数，立即怀疑 regex 截断 bug
2. **临时绕路**：在 `## Draft` 下面、第一个 `###` 之上面插入一段文字（如"本文为..."），让正则能提取到这段文字
3. **修复正则**：将 `validation.py` 中的 `(?=^##|\Z)` 改为 `(?=^##(?!#)|\Z)` 或 `(?=^##\s|\Z)`
4. **回归测试**：修复后用多篇使用 `###` 标题的文章测试，确认 word count 正确
5. **检查其他 regex**：在代码库中搜索类似的 `(?=^##|\Z)` 模式，确认没有其他地方有相同 bug

## 适用边界

- 适用于所有使用 `kdo validate` 验证文章的场景
- 不适用于不使用三级标题的文章——如果文章只用 `##` 标题，不会触发此 bug
- 不适用于非文章类的验证（如卡片、feedback）——这些通常不涉及 `###` 标题
- 根治方案需要修改源码，如果你没有代码修改权限，只能使用临时绕路
- 此 bug 的隐蔽性极高：它不报错，只是给出错误的 word count——很容易让人误代码"文章不够长"

## 为什么值钱

- 这是 KDO CLI 特有的技术漏洞：**regex 边界匹配的细微差异导致整个验证系统失效**
- 此 bug 极具迷惑性：它不会崩溃或报错，只是默默地给出错误的数据——让人误代码"我的文章太短"
- 暴露了正则表达式设计中的一个经典陷阱：`**^##** 不仅匹配 `## `，还匹配 `###`、`####` 等更深级别的 heading**
- 任何 AI 训练语料中都不会有"KDO 的 validator 正则在 ### 处截断文章内容"这条知识

## 与其他知识的关联

- [[dk-c1-regex-on-cjk]] — 同一深层模式：regex 边界问题导致静默失败。C-1 是"`\b` 不识别 CJK 词边界"，P-11 是"`^##` 误匹配 `###`"——两者都是"正则表达式边界定义不严格导致静默错误"
- [[master-systems-thinking]] — 系统思维中的"细节决定成败"：一个小小的 regex 边界差异（`^##` vs `^##(?!#)`）导致了整个验证系统对所有文章失效
- `.agent/pitfalls.md` → P-11（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
