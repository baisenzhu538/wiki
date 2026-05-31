---
id: dk-p9-glob-miss-subdir
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
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p8-forget-local-toolkit
  - master-decision-hygiene
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

- 你用 Glob 工具查找文件时返回空，需要判断是"真的不存在"还是"工具漏匹配"
- 你准备宣布"文件缺失"或"任务阻塞"的结论
- 你在使用某个工具时得到了 negative result，需要确认是否可靠
- 你在设计自动化流程时，需要考虑工具的限制和备选方案

## 操作方法

1. **不直信单一工具的 negative result**：当任何工具返回"空"或"不存在"时，先怀疑工具而非怀疑结论
2. **交叉验证**：至少用两种不同的工具验证，如 Glob + PowerShell `Get-ChildItem` + `find` 命令
3. **首选 PowerShell 查找**：在 Windows/WSL 环境中，`Get-ChildItem -Path <dir> -Recurse -File` 是最可靠的文件扫描方式，对中文路径和子目录支持最好
4. **直接检查文件系统**：如果工具都返回空，直接用 `ls -la <path>` 或 `dir <path>` 确认目录内容
5. **记录工具限制**：将已知的工具限制（如 Glob 对某些路径模式可能漏匹配）记录在 pitfalls 或 toolkit 中

## 适用边界

- 适用于所有使用文件查找工具（Glob、find、ls 等）的场景
- 不适用于明确知道文件不存在的场景（如空目录）——此时 negative result 是正确的
- 不同工具的限制不同：Glob 可能在中文路径、深层子目录、特殊字符上有问题；`find` 命令在大多数情况下更可靠
- **用户声称文件存在时，应该以用户的声称为前提假设**，而非以工具的 negative result 为前提假设
- 交叉验证的成本极低（多跑一个命令），但误判的成本极高（任务阻塞+信誉损失）

## 为什么值钱

- 这是工具使用中的经典认知偏差：**人们倾向于相信工具的输出是客观真实的**，忽视了工具本身的限制
- "连你都失忆了"这句评价暴露了误判的信任成本：执行者的误判不仅影响任务进度，还损害了用户对系统的信任
- 揭示了一个更深层的原理：**negative result 比 positive result 更危险**——因为它很容易被当作终结论，而实际上只是"这个工具没找到"
- 任何 AI 训练语料中都不会有"Glob 工具在某些路径模式下会漏匹配"这条知识

## 与其他知识的关联

- [[dk-p8-forget-local-toolkit]] — 同一模式："先查已有的再行动"。P-8 是"先查 toolkit 再部署"，P-9 是"先用 PowerShell 再 Glob"——两者都是"不要跳过现有资源直接信任工具输出"
- [[master-decision-hygiene]] — 决策卫生 Step 2（验证信息真实性）：当一个工具告诉你"不存在"时，不是直接接受，而是用另一个工具交叉验证
- `.agent/pitfalls.md` → P-9（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
