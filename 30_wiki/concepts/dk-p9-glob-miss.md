---
id: dk-p9-glob-miss
title: "P-9：Glob 漏扫子目录 → 误判文件缺失 → 来回打脸"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-9"
source_refs:
  - .agent/pitfalls.md#P-9
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - dk-p8-toolkit-forget
contradicts:
  - [[master-first-principles]]
  - [[master-ai-info-literacy]]
---

# P-9：Glob 漏扫子目录 → 误判文件缺失 → 来回打脸

## 原始表述

> **症状**：用户说设计域文件在 `00_inbox/design/`，执行 `Glob "00_inbox/*design*/**/*"` + `Glob "00_inbox/**/*.txt"` 均返回空。结论"文件不存在"。用户指出文件就在那里后，改用 PowerShell `Get-ChildItem -Recurse` 立即找到：`design\AI设计-AI设计基础01.txt` (72KB) 和 `AI设计-AI设计师实操培训01.txt` (122KB)。误判导致任务文件被错误标注为"阻塞"后又回滚，浪费时间+信誉。
>
> **根因**：Glob 工具对特定路径模式（含中文名？子目录深度？）可能漏匹配。单一工具判断"不存在"是危险的。
>
> **对策**：
> - **查文件是否存在：先用 PowerShell `Get-ChildItem -Path ... -Recurse`，再按需 Glob/Grep**
> - 永远不要用一个工具的 negative result 作为最终结论
> - 宣布"文件缺失"前，至少用两种工具交叉验证
> - 本次误判已直接导致用户不满（"连你都失忆了"）

## 使用场景

- 你需要确认某个文件夹下是否存在特定类型的文件
- 你使用 Glob 工具扫描文件系统，返回空结果
- 你需要基于文件存在性做决策（如"是否阻塞""是否跳过"）
- 你怀疑某个工具可能漏匹配（特别是涉及中文路径、子目录、特殊字符时）

## 操作方法

1. **不要用一个工具的 negative result 作为最终结论**：
   - Glob 返回空 ≠ 文件不存在
   - `ls` 看不到 ≠ 文件不存在
   - 任何工具的"未找到"都需要二次验证

2. **交叉验证流程**：
   - 第一步：PowerShell `Get-ChildItem -Path <dir> -Recurse`（最可靠的全量扫描）
   - 第二步：`find <dir> -type f`（WSL/Unix 环境）
   - 第三步：如果前两步都为空，再宣布"文件缺失"

3. **Glob 的已知限制**：
   - 中文文件名可能漏匹配
   - 深层子目录可能截断
   - 特殊字符（空格、括号、连字符）可能转义失败
   - 符号链接可能不被追踪

4. **宣布"文件缺失"前的 checklist**：
   - [ ] 已用至少两种独立工具扫描
   - [ ] 已检查父目录是否存在
   - [ ] 已确认文件扩展名/模式正确
   - [ ] 已询问用户确认（如果可能）

5. **不要做的事**：
   - 不要 Glob 返回空就立即宣布"文件不存在"
   - 不要把"我没找到"等同于"它不存在"
   - 不要在未核实的情况下将任务标记为"阻塞"

## 适用边界

- 适用于所有涉及文件系统扫描的场景
- 不适用于明确知道文件不存在的情况（如首次创建目录）
- **与 P-8 的区别**：P-8 是"忘了有工具"，P-9 是"工具有缺陷但盲目信任"。两者可能同时发生
- 在远程文件系统（如 SMB、NFS、云存储）上，Glob 的限制可能更多
- 如果文件权限不足，即使存在也可能扫描不到——这与 Glob 缺陷不同

## 为什么值钱

- 这是**工具可信度**的实战教训：每个工具都有边界条件，"返回空"不等于"事实为空"
- 极具破坏力：一次"文件不存在"的误判直接导致任务文件错误标注、用户不满（"连你都失忆了"）
- 揭示了"negative result"的普遍风险：不仅是 Glob，任何工具的"未找到""未匹配""未触发"都需要警惕
- **AI 训练语料中不会有这条**：没有任何文档会写"Glob 对中文文件名可能漏匹配，先用 PowerShell 验证"

## 与其他知识的关联

- [[dk-p8-toolkit-forget]] — P-8 和 P-9 是同一事件的两种失败：P-8 是"忘了用 OCR 工具"，P-9 是"用了 Glob 工具但盲目信任其 negative result"。如果当时先用 PowerShell 验证，就不会误判
- [[dk-p15-unverified]] — P-15 是"声称完成但实际未做"，P-9 是"声称不存在但实际存在"——两者都是"未经独立验证就下结论"
- `.agent/pitfalls.md` → P-9（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
