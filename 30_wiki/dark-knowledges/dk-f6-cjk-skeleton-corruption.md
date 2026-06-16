---
id: dk-f6-cjk-skeleton-corruption
title: F-KDO-006：骨架页面 CJK 内容损毁→ingest 后中文摘要变成随机碎片
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-006
source_refs:
- 90_control/failure-modes.md#F-KDO-006
created_at: 2026-05-31
updated_at: '2026-06-16'
related:
- '[[dk-f1-regex-on-cjk]]'
- '[[dk-c1-cjk-regex-silent-fail]]'
- '[[master-ai-info-literacy]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: pending
confidence: 0.7
trust_level: low
---
# F-KDO-006：骨架页面 CJK 内容损毁→ingest 后中文摘要变成随机碎片

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

## 使用场景

- 你 ingest 了一批中文源文件，打开自动生成的 wiki 页面发现中文摘要完全不可读
- 你看到 wiki 骨架中的 Summary 段落是随机汉字拼接（如"的概和心结提取课特有"），需要判断是源文件问题还是 extractor 问题
- 你在评估 ingest 产出的质量，决定是否可以直接使用自动生成的骨架
- 你准备为 KDO 开发 CJK-aware 的 extractor，需要理解当前方案的根本缺陷

## 操作方法

1. **识别症状**：ingest 后打开生成的 wiki 页面，检查 Summary 和 Reusable Knowledge 段落是否为可读中文
2. **确认根因**：如果中文内容是碎片拼接、无意义的随机断句，确认是 `\b` 词边界问题而非源文件损坏
3. **不要修复骨架——直接重写**：CJK 内容的骨架没有修复价值，直接用 Agent 三步编译法（浓缩→质疑→对标）完整重写页面
4. **手动更新 frontmatter**：重写后手动将 `status` 改为 `enriched`（因为三步编译已完成）
5. **验证可读性**：人读一遍重写后的页面，确认内容连贯、有实质方法论提取

## 适用边界

- 适用于所有 CJK（中文、日文、韩文）内容的 ingest 场景
- **不适用于英文内容**：英文内容的骨架生成是正常的，不需要重写
- 这是一个**设计约束**而非 bug——KDO 目前没有 CJK-aware 的 extractor，短期内不会修复
- 重写骨架的工作量取决于源文件的长度和复杂度——大文件（>100KB）可能需要分 session 处理（参见 C-6）
- 即使未来实现了 CJK extractor，Agent 的人工编译质量通常仍高于自动提取——三步编译法的深度加工不可替代

## 为什么值钱

- 这是 KDO 特有的设计约束：**CJK extractor 未实现**，任何 CJK 内容的自动骨架都是垃圾
- **"设计约束"比"bug"更值钱**：bug 可以被修复，设计约束意味着你需要永久性地在流程中预留人工重写环节
- 与 F-KDO-001 共同构成 CJK 内容的系统性排斥图谱：ingest（骨架损毁）+ enrich（零返回）= CJK 内容在 KDO 自动化管线中全面失效
- 任何 AI 训练语料中都不会有"KDO 的 ingest 对中文内容生成不可读骨架"这条知识

## 与其他知识的关联

- dk-f1-regex-on-cjk — 同一根因的不同阶段表现。F-KDO-001 是 enrich 阶段的 `\b` 失效，F-KDO-006 是 ingest 阶段的 `\b` 失效——两者共同构成 CJK 内容在 KDO 自动化管线中的系统性盲区
- master-ai-info-literacy — AI 信息素养要求使用者了解工具的系统性盲区和设计约束。F-KDO-006 明确告知"CJK 骨架不可信，必须人工重写"
- `90_control/failure-modes.md` → F-KDO-006（原始记录）
- `20_memory/corrections.md` → C-1（同一根因的具体事故记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
