---

id: dk-f6-cjk-skeleton-corruption
title: F-KDO-006：骨架页面 CJK 内容损毁→ingest 后中文摘要变成随机碎片
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-006
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
  - "[[kdo-input-channel-strategy-2026-06-16]]"
  - "[[kdo-protocol]]"
  - "[[modeling-to-kdo-toolchain]]"
  - "[[kdo-batch-produce-req014]]"
  - "[[kdo-15-dimension-label-spec]]"
  - "[[obsidian-kdo-内容产出工作流-产品设计大纲]]"
  - "[[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]"
  - "[[kdo-watch-health-check-layer]]"
  - "[[dk-f1-regex-on-cjk]]"
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
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: regex 的 `\b` 词边界对 CJK 字符不生效，extractor 在随机位置切分中文，导致摘要不可读
  follow_up_question: 不要尝试修复骨架，直接对中文页面执行 Agent 三步编译（浓缩→质疑→对标）并更新 status=enriched
- signal: src_unknown
  framework_lens: KDO 当前没有 CJK-aware 的 extractor，CJK 内容的自动骨架生成是系统性设计约束而非个案 bug
  follow_up_question: 确认源文件本身可读；若源文件正常，则判定为 extractor 问题，直接重写页面并记录为 F-KDO-006# F-KDO-006：骨架页面
    CJK 内容损毁→ingest 后中文摘要变成随机碎片

---

## 原始表述

> **触发命令**：`kdo ingest`
>
> **表现**：自动生成的 `30_wiki/concepts/<page>.md` 骨架中，Summary 和 Reusable Knowledge 段落是随机断裂的中文碎片，不可读
>
> **根因**：`kdo ingest` 的 extractor 用 regex 提取段落摘要——`\b` 不识别中文词边界，在随机位置断句。与 F-KDO-001 同一根因。
>
> **触发信号**：读自动生成的 wiki 页面骨架，中文内容为无意义的碎片拼接
>
> **防御措施**：这是设计约束而非 bug——CJK extractor 未实现。当前所有 CJK 内容的骨架都是垃圾，需由 Agent 重写
>
> **临时绕过**：ingest 后立即读 wiki 页面，用三步 CJK 编译（浓缩→质疑→对标）完整重写
>
> **关联**：与 F-KDO-001 共享根因，但触发阶段不同（ingest vs enrich）

## 核心洞察

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

1. **识别症状**：ingest 后打开生成的 wiki 页面，检查 Summary 和 Reusable Knowledge 段落是否为可读中文
2. **确认根因**：如果中文内容是碎片拼接、无意义的随机断句，确认是 `\b` 词边界问题而非源文件损坏
3. **不要修复骨架——直接重写**：CJK 内容的骨架没有修复价值，直接用 Agent 三步编译法（浓缩→质疑→对标）完整重写页面
4. **手动更新 frontmatter**：重写后手动将 `status` 改为 `enriched`（因为三步编译已完成）
5. **验证可读性**：人读一遍重写后的页面，确认内容连贯、有实质方法论提取

## 适用边界

| 边界 | 说明 |
|:
--|:------|
| ✅ 适用 | 所有 CJK（中文、日文、韩文）内容的 ingest 场景 |
| ❌ 不适用 | 纯英文内容：英文内容的骨架生成是正常的，不需要重写 |
| 设计约束 | 当前 KDO 没有 CJK-aware 的 extractor，这是设计约束而非临时 bug，短期内不会自动消失 |
| 工作量约束 | 重写骨架的工作量取决于源文件的长度和复杂度——大文件（>100KB）可能需要分 session 处理（参见 C-6） |
| 质量约束 | 即使未来实现了 CJK extractor，Agent 的人工编译质量通常仍高于自动提取——三步编译法的深度加工不可替代 |

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| 中文摘要碎化 | 自动生成骨架的 Summary 出现无意义汉字碎片，如"的概和心结提取课特有" | 不修复骨架，直接重写页面；完成后 `status=enriched` 并人工读一遍 |
| Reusable Knowledge 段落断裂 | 可复用知识段落变成随机关键词拼接，无法提取方法论 | 用 Agent 三步编译法重新提炼核心概念、反例和边界 |
| 误判为源文件损坏 | 看到中文碎片后怀疑原始素材有问题，反复检查源文件 | 先确认源文件可读；若源文件正常，立即判定为 extractor 设计约束，转人工重写 |
| 局部修补骨架 | 试图只替换破碎段落、保留自动生成的其余结构 | 停止局部修补，CJK 骨架整体不可信，必须完整重写 |

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
- src_unknown

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
