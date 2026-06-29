---
id: dk-p9-glob-miss
title: P-9：Glob 漏扫子目录 → 误判文件缺失 → 来回打脸
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-9
source_refs:
  - src_unknown
created_at: 2026-06-03
updated_at: 2026-06-28
related:
- [[dk-p8-toolkit-forget]]
- [[dk-p15-unverified]]
- [[master-first-principles]]
- [[master-ai-info-literacy]]
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown# P-9：Glob 漏扫子目录 → 误判文件缺失 → 来回打脸
---
## 原始表述 / 核心洞察

> **症状**：用户说设计域文件在 `00_inbox/design/`，执行 `Glob "00_inbox/*design*/**/*"` + `Glob "00_inbox/**/*.txt"` 均返回空。结论"文件不存在"。用户指出文件就在那里后，改用 PowerShell `Get-ChildItem -Recurse` 立即找到：`design\AI设计-AI设计基础01.txt` (72KB) 和 `AI设计-AI设计师实操培训01.txt` (122KB)。误判导致任务文件被错误标注为"阻塞"后又回滚，浪费时间+信誉。
>
> **根因**：Glob 工具对特定路径模式（含中文名、子目录深度、特殊字符）可能漏匹配。单一工具判断"不存在"是危险的。
>
> **核心洞察**：**任何工具的 negative result 都不是事实本身**。"我没找到"≠"它不存在"；在宣布文件缺失前，必须至少用两种独立工具交叉验证。
>
> **对策**：
> - **查文件是否存在：先用 PowerShell `Get-ChildItem -Path ... -Recurse`，再按需 Glob/Grep**
> - 永远不要用一个工具的 negative result 作为最终结论
> - 宣布"文件缺失"前，至少用两种工具交叉验证
> - 本次误判已直接导致用户不满（"连你都失忆了"）

## 原始表述

- src_unknown（待补充来源原话）

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **不要用一个工具的 negative result 作为最终结论**：
   - src_unknown
   - src_unknown
   - src_unknown

2. **交叉验证流程**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **Glob 的已知限制**：
   - src_unknown
   - src_unknown
   - src_unknown
   - src_unknown

4. **宣布"文件缺失"前的 checklist**：
   - src_unknown
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

| 失败模式 | 典型症状 | 根因 | 止损动作 |
|
|---|---|---|
| **Glob 漏扫子目录** | `Glob "dir/**/*.ext"` 返回空，但文件实际存在 | Glob 对递归深度、中文路径、特殊字符处理有边界 | 改用 `Get-ChildItem -Recurse` 或 `find -type f` 做全量枚举 |
| **把 negative result 当结论** | 直接宣布"文件不存在"并标记任务阻塞 | 未对单一工具的"未找到"做二次确认 | 至少两种独立工具确认后再下结论；优先使用系统原生递归命令 |
| **忽略中文/特殊字符路径** | 含中文、空格、括号的文件反复漏匹配 | Glob 转义、编码或分词规则不一致 | 先用无模式过滤的全量列表，再本地过滤；避免过度依赖通配符 |

## 为什么值钱

- src_unknown
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

## 审查记录

- src_unknown
- src_unknown
