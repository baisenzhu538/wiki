---
id: dk-c5-todo-false-positive
title: "C-5：TODO 字符串匹配过宽→正文中的 TODOs/TODOable 被误报为占位符"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: Builder
source_context: "2026-05-03"
source_refs:
  - 20_memory/corrections.md#C-5
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c4-selfcheck-superseded
  - master-cognitive-bias-checklist
---

# C-5：TODO 字符串匹配过宽→正文中的 TODOs/TODOable 被误报为占位符

## 原始表述

> 正文中出现 `TODO` 字符串（如"TODOs"、"TODOable"）被误报为"有 TODO 占位符"。
>
> 根因：使用粗粒度字符串匹配 `if "TODO" in line`。
>
> 修正：已修复。改为 `"TODO:"` 精确匹配（含冒号）。

## 使用场景

- 你运行 `kdo self-check` 或 lint 检查卡片中的 TODO 占位符，发现报告中出现了大量假阳性
- 你写脚本搜索 TODO 标记时，需要区分"TODO 作为指令占位符"和"TODO 作为普通词汇"
- 你审查自检报告，看到正文中的"这篇文章讲 TODOs 管理"被标红，需要确认匹配规则是否过宽
- 你设计新的占位符检测规则（如 FIXME、HACK、XXX），需要避免复刻 C-5 的错误

## 操作方法

1. **识别精确模式**：TODO 占位符的标准格式是 `TODO:`（含冒号），表示"此处需要后续补充"
2. **拒绝子串搜索**：不要用 `if "TODO" in line` 这类粗粒度匹配——它会匹配到 "TODOs"、"TODOable"、"关于TODO的研究"等所有包含子串的情况
3. **使用精确匹配或正则边界**：推荐 `if "TODO:" in line` 或正则 `r'\bTODO:\b'`。如果语言支持，用单词边界 + 冒号双重约束
4. **区分语义场景**：
   - 占位符指令：`TODO: 补充案例`、`TODO: 验证数据`
   - 普通词汇：`TODOs`（复数名词）、`TODOable`（形容词）、`TODO 列表是一种管理工具`
5. **验证修复**：跑自检，确认包含 "TODOs"、"TODOable" 的正文不再被误报，同时真正的 `TODO:` 占位符仍能被正确捕获

## 适用边界

- 适用于所有通过**字符串匹配**检测占位符/标记的工具和脚本
- **不适用于结构化标记**：如果 TODO 是通过 frontmatter（如 `status: needs-todo`）或 HTML 注释（`<!-- TODO -->`）标记的，不需要字符串匹配，自然不会有这个问题
- 如果 `TODO:` 出现在代码块示例中（如展示一段 Python 注释 `# TODO: fix this`），精确匹配 `"TODO:"` 仍可能误报，需要额外排除代码块或添加上下文判断
- 不同语言/工具的字符串边界行为不同（如 Python 的 `in` 是子串匹配，正则的 `\b` 是单词边界）——实现前必须确认当前语言的行为
- 如果占位符标记采用了其他格式（如 `[TODO]`、`{{TODO}}`），匹配规则需要相应调整，但原则不变：精确匹配 > 子串匹配

## 为什么值钱

- 粗粒度字符串匹配是脚本中最常见、最隐蔽的错误来源之一，但"TODO 子串匹配误报"这个具体案例只有 KDO 的 self-check 才会遇到
- 误报的代价不是"报告多了一行"，而是**告警可信度的系统性下降**：当审查者连续看到 10 个假阳性后，第 11 个真阳性也会被忽略
- 这是工程实践中"精确性 vs 召回率"权衡的经典案例：子串匹配召回率高但精确率低，精确匹配牺牲了极边缘情况（如有人写 `TODO - 补充案例` 不带冒号）但大幅降低了噪音
- 任何 AI 训练语料中都不会有"KDO 的 self-check 对 TODO 应该用 `TODO:` 精确匹配而非子串搜索"这条知识

## 与其他知识的关联

- [[dk-c4-selfcheck-superseded]] — 同一模式：自检工具的匹配规则缺陷导致假阳性。C-4 是 skip 集合缺失，C-5 是字符串匹配过宽——两者共同构成"self-check 报告不可信"的风险
- [[master-cognitive-bias-checklist]] — 认知偏差中的"告警疲劳"（Alarm Fatigue）：当假阳性率超过阈值，人类会系统性忽略所有告警。C-4 和 C-5 叠加时，self-check 机制形同虚设
- `20_memory/corrections.md` → C-5（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
