---
id: dk-f2-txt-ingest-skip
title: "F-KDO-002：非 .md 文件 ingest 静默跳过→state.json 无变化但用户以为成功"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "failure-modes.md F-KDO-002"
source_refs:
  - 90_control/failure-modes.md#F-KDO-002
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c3-txt-ingest-skip
  - master-ai-info-literacy
---

# F-KDO-002：非 .md 文件 ingest 静默跳过→state.json 无变化但用户以为成功

## 原始表述

> **触发命令**：`kdo ingest`
>
> **表现**：对 `.txt` 文件：无输出、无报错、state.json 无变化、无源文件创建。用户以为 ingest 成功了。
>
> **根因**：`kdo ingest` 只扫描 `00_inbox/*.md`，其他扩展名被静默忽略
>
> **触发信号**：`ls 10_raw/sources/` 没有新文件产生；state.json 的 `ingested_inbox_files` 列表无新增
>
> **防御措施**：ingest 完成后：① 打印实际处理的文件数量 ② 对 `00_inbox/` 中剩余的非 .md 文件给出 warning ③ 建议在 ingest 前跑 `find 00_inbox -type f` 确认所有文件都是 .md
>
> **临时绕过**：`cp file.txt file.md && rm file.txt` 后重新 ingest
>
> **关联文件**：`kdo/commands/ingestion.py`

## 使用场景

- 你有 `.txt` 格式的口述稿或素材要导入 KDO，运行 `kdo ingest` 后看到无输出但以为成功了
- 你写自动化脚本批量处理 `00_inbox/` 中的原始素材，脚本跑完但没有生成新的源文件
- 你检查 `state.json` 确认 ingest 状态，发现 `ingested_inbox_files` 列表没有增加
- 你在设计 KDO 的 ingest 管线，需要确认支持哪些输入格式

## 操作方法

1. **检查文件扩展名**：运行 ingest 前，先 `find 00_inbox -type f` 确认所有文件都是 `.md` 格式
2. **非 .md 文件先转换**：对 `.txt` 文件执行 `cp file.txt file.md`，然后再运行 `kdo ingest`
3. **批量处理脚本**：如果文件量大，用循环自动转换——`for f in 00_inbox/*.txt; do cp "$f" "${f%.txt}.md"; done`
4. **验证 state.json**：ingest 完成后检查 `state.json`，确认 `ingested_inbox_files` 列表有新增
5. **读取骨架验证**：打开自动生成的 wiki 页面，确认内容没有被碎片化（特别是 CJK 内容，参见 F-KDO-006）

## 适用边界

- 适用于所有 `.txt` → `.md` 的转换场景——KDO ingest 只认 `.md`
- **不适用于其他格式**：`.docx`、`.pdf`、`.html` 需要更复杂的转换（先用 Python 脚本转 Markdown），不能简单改扩展名
- 即使改了 `.md` 扩展名，如果内容是完全无结构的纯文本，ingest 后仍需人工补充 frontmatter 和结构化标记
- 自定义 ingest 插件或修改了 `ingestion.py` 的情况，需要确认插件自身的扩展名白名单
- 对于已有 `.md` 文件，ingest 会正常处理，不需要额外操作

## 为什么值钱

- 这是 KDO CLI 特有的行为：`kdo ingest` 的扩展名白名单只包含 `.md`，非 `.md` 被设计为"静默跳过"而非报错
- **"返回成功但什么都不做"是最危险的失败模式**：exit code 为 0，日志里没有 error，你唯一发现的方式是事后检查 `state.json` 或源文件目录
- 暴露了 CLI 工具中"静默跳过"这一反模式：对不支持的输入格式，应该选择报错（fail fast）还是静默跳过？KDO 选择了后者，代价是用户需要靠经验才能发现
- 任何 AI 训练语料中都不会有"kdo ingest 跳过 .txt 但返回成功"这条知识——这是具体工具实现层面的暗知识

## 与其他知识的关联

- [[dk-c3-txt-ingest-skip]] — corrections 层面的具体事故记录：2026-05-03 Builder 报告 .txt 被 ingest 静默跳过。F-KDO-002 是这个具体事故的模式化抽象
- [[master-ai-info-literacy]] — AI 信息素养要求使用者了解工具的输入格式白名单和盲区。F-KDO-002 是"ingest 工具扩展名白名单盲区"的具体案例
- `90_control/failure-modes.md` → F-KDO-002（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #3（不准用 `kdo ingest` 处理 .txt 文件）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
