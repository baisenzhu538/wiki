---
id: dk-c5-todo-false-positive
title: C-5：TODO 字符串匹配过宽→正文中的 TODOs/TODOable 被误报为占位符
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[kdo-watch-health-check-layer]]'
- '[[dk-c4-selfcheck-superseded]]'
- '[[master-cognitive-bias-checklist]]'
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# C-5：TODO 字符串匹配过宽→正文中的 TODOs/TODOable 被误报为占位符
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
---
## 原始表述/核心洞察

> 正文中出现 `TODO` 字符串（如"TODOs"、"TODOable"）被误报为"有 TODO 占位符"。
>
> 根因：使用粗粒度字符串匹配 `if "TODO" in line`。
>
> 修正：已修复。改为 `"TODO:"` 精确匹配（含冒号）。

核心洞察：**占位符检测必须匹配指令标记的精确边界，而不是关键字的子串出现**。`TODO:`（带冒号的待办指令）与 `TODOs`/`TODOable`（普通词汇）在语义上完全不同；将两者混为一谈会系统性降低告警可信度，引发告警疲劳。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别精确模式**：TODO 占位符的标准格式是 `TODO:`（含冒号），表示"此处需要后续补充"
2. **拒绝子串搜索**：不要用 `if "TODO" in line` 这类粗粒度匹配——它会匹配到 "TODOs"、"TODOable"、"关于TODO的研究"等所有包含子串的情况
3. **使用精确匹配或正则边界**：推荐 `if "TODO:" in line` 或正则 `r'\bTODO:\b'`。如果语言支持，用单词边界 + 冒号双重约束
4. **区分语义场景**：
   - src_unknown
   - src_unknown
5. **验证修复**：跑自检，确认包含 "TODOs"、"TODOable" 的正文不再被误报，同时真正的 `TODO:` 占位符仍能被正确捕获

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| 子串匹配误报 | 正文中 "TODOs"、"TODOable" 被标红 | 使用 `if "TODO" in line` 粗粒度匹配 | 改为 `"TODO:"` 精确匹配或正则边界 |
| 边界假设错误 | 认为所有含 TODO 子串的都是占位符 | 未区分"指令占位符"与"普通词汇" | 建立"冒号+上下文"的判定标准 |
| 修复后漏报真阳性 | 真正的 `TODO:` 占位符不再被捕获 | 过度收紧规则（如要求前后空格） | 用 `TODO:` 精确匹配保留对标准格式的召回 |
| 代码块示例误报 | 展示 `# TODO: fix this` 的代码块被标红 | 精确匹配未排除代码块/注释上下文 | 增加上下文判断或排除代码块 |
| 告警疲劳导致忽略真问题 | 审查者因大量假阳性而关闭/忽略报告 | 假阳性率超过人类容忍阈值 | 先修规则降低噪音，再恢复审查纪律 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
