---
id: "dk-p11-regex-cutoff"
title: "P-11：validator `section_content` regex 在 `###` 处截断——所有文章 word count 失效"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "pitfalls.md P-11"
source_refs:
  - ".agent/pitfalls.md#P-11"
tags:
  - "confidence-draft"
  - "confidence-source-cited"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
  - "#scene/ai-collaboration"
  - "#scene/knowledge-management/tagging"
  - "#scene/learning-methodology/feedback-loop"
  - "#scene/skill-engineering/eval-testing"
  - "#source_type/error"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - "dk-f13-handwritten-yaml-parser"
contradicts:
  - "master-first-principles"
  - "kdo-yaml-frontmatter-safety"
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

- 你使用 `kdo validate` 验证文章类 artifact，发现 word count 异常低
- 你写 Markdown 时使用三级标题（`###`）组织内容
- 你维护一个基于正则的解析器，需要处理多级标题
- 你排查"为什么内容明明有但工具报告为空"

## 操作方法

1. **识别 regex 截断问题**：
   - 症状：内容明明存在，但解析器报告为空或极短
   - 检查点：内容中是否有 `###` 三级标题？正则是否用了 `^##` 匹配？
   - 验证：手动提取 section 内容，对比解析器输出

2. **临时绕过**：
   - 在 `## Draft` 和第一个 `###` 之间插入一段引导文字
   - 这样即使被截断，截断前的内容也有足够字数通过验证
   - 标记为"待根治"，记录在技术债务中

3. **根治修复**：
   - 将正则 `(?=^##|\Z)` 改为 `(?=^##(?!#)|\Z)`
   - 或使用 `(?=^##\s|\Z)` 确保只匹配 `## ` 后跟空格的同级 heading
   - 修复后全量测试：跑所有文章的 validate，确认无回归

4. **regex 设计原则**：
   - 匹配 heading 时明确级别：`^##\s` 只匹配二级，`^###\s` 只匹配三级
   - 不要用前缀匹配（`^##` 会同时匹配 `##` 和 `###`）
   - 解析 Markdown 时考虑使用专用库（如 `markdown-it`、`mistune`）而非手写正则

5. **不要做的事**：
   - 不要手写正则解析 Markdown 结构——除非非常简单的场景
   - 不要假设"内容有字就不会报空"——正则可能在第一个 `###` 处就截断了
   - 不要在未修复 regex 的情况下强制通过验证（如手动改字数）

## 适用边界

- 适用于所有基于正则解析 Markdown heading 的场景
- 不适用于使用专用 Markdown 解析库的场景
- **与 P-18 的区别**：P-18 是"手写 YAML 解析器导致数据丢失"，P-11 是"手写 regex 解析器导致内容截断"——两者都是"手写解析器 vs 标准库"的问题
- 如果内容中没有三级标题，P-11 不触发——但这在文章中很少见
- 正则的贪婪/非贪婪模式也可能导致类似截断问题

## 为什么值钱

- 这是**手写解析器的经典陷阱**：正则看似正确，但边界条件（`###` 以 `##` 开头）导致灾难性后果
- 极具隐蔽性：1800 字的文章被截断到 46 字，但用户只看到了"0 words"的错误报告，不会想到是正则 bug
- 影响范围广：所有使用三级标题的文章都命中，而三级标题是文章组织的常用方式
- **AI 训练语料中不会有这条**：没有任何文档会写"`^##` 正则也会匹配 `###`，导致 Markdown section 提取截断"

## 与其他知识的关联

- dk-f13-handwritten-yaml-parser — F-KDO-013 和 P-11 是同一类问题：手写解析器在边界条件下失效。YAML 解析器拍扁嵌套结构，regex 解析器截断多级标题
- dk-p18-yaml-parser — P-18 是 P-11 的姊妹篇：都是"不要手写解析器"的实战教训
- `90_control/failure-modes.md` → F-KDO-013（手写 YAML 解析器）
- `.agent/pitfalls.md` → P-11（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
