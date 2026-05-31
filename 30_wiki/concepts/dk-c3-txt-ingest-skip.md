---
id: dk-c3-txt-ingest-skip
title: "C-3：.txt 文件被 kdo ingest 静默跳过→state.json 无变化但返回成功"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: Builder
source_context: "2026-05-03"
source_refs:
  - 20_memory/corrections.md#C-3
tags:
  - "#source_type/error"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c1-cjk-regex-silent-fail
  - master-ai-info-literacy
---

# C-3：.txt 文件被 kdo ingest 静默跳过→state.json 无变化但返回成功

## 原始表述

> `kdo ingest` 对 `.txt` 文件静默返回成功，但什么都不做。无错误信息，state.json 无变化。
>
> 根因：ingest 只识别 `.md` 扩展名，非 `.md` 文件直接跳过。
>
> 修正：ingest 前检查扩展名，如果是 `.txt` 先 `cp file.txt file.md` 再 ingest。
>
> 关联失败模式：F-KDO-002（已录入 AGENTS.md 禁止清单）

## 使用场景

- 你有一批 `.txt` 格式的口述稿/素材文件要导入 KDO vault，运行 `kdo ingest` 后看到 "success" 但 vault 里找不到新文件
- 你写自动化脚本批量处理 `00_inbox/` 中的原始素材，脚本跑完但输出目录为空
- 你检查 `state.json` 确认 ingest 状态，发现文件数量没有增加，需要判断是重复文件还是被静默跳过
- 你在设计 KDO 的 ingest 管线，需要确认支持哪些输入格式

## 操作方法

1. **检查文件扩展名**：运行 ingest 前，先 `ls` 确认待处理文件的扩展名——`.txt` 会被跳过
2. **手动转换**：对 `.txt` 文件执行 `cp file.txt file.md`，再运行 `kdo ingest file.md`
3. **批量处理脚本**：如果文件量大，用循环自动转换——`for f in *.txt; do cp "$f" "${f%.txt}.md"; done`
4. **验证 state.json**：ingest 后检查 `state.json`，确认文件计数确实增加了
5. **内容清理（可选）**：如果 `.txt` 内容不是标准 Markdown，转换后可能需要补充 frontmatter 或调整格式

## 适用边界

- 适用于所有 `.txt` → `.md` 的转换场景——KDO ingest 只认 `.md`
- **不适用于其他格式**：`.docx`、`.pdf`、`.html` 需要更复杂的转换（先用 Python 脚本转 Markdown），不能简单改扩展名
- 即使改了 `.md` 扩展名，如果内容是完全无结构的纯文本，ingest 后仍需人工补充 frontmatter 和结构化标记
- 如果你使用的是 KDO 的批量 ingest 命令，需要先把 `.txt` 全部转换完再跑批量，不要指望 ingest 自动处理
- 自定义 ingest 插件或修改了 `extractors.py` 的情况，需要确认插件自身的扩展名白名单

## 为什么值钱

- 这是 KDO CLI 特有的行为：`kdo ingest` 的扩展名白名单只包含 `.md`，`.txt` 被设计为"静默跳过"而非报错——这个设计决策本身不在任何文档中明确说明
- **"返回成功但什么都不做"是最危险的失败模式**：exit code 为 0，日志里没有 error，你唯一发现的方式是事后检查 `state.json` 或 vault 目录
- 暴露了 CLI 工具中"静默跳过"这一反模式：对不支持的输入格式，应该选择报错（fail fast）还是静默跳过？KDO 选择了后者，代价是用户需要靠经验才能发现
- 任何 AI 训练语料中都不会有"kdo ingest 跳过 .txt 但返回成功"这条知识——这是具体工具实现层面的暗知识

## 与其他知识的关联

- [[dk-c1-cjk-regex-silent-fail]] — 同一模式：KDO CLI 工具的"静默失败"。C-1 是 enrich 对中文返回 0，C-3 是 ingest 对 .txt 跳过——两者都是"exit code 为 0 + 无实质输出"
- [[master-ai-info-literacy]] — AI 信息素养要求使用者了解工具的输入格式白名单和盲区。C-3 是"ingest 工具扩展名白名单盲区"的具体案例
- `90_control/failure-modes.md` → F-KDO-002（已录入 AGENTS.md 禁止清单：不准直接将 .txt 丢给 kdo ingest）
- `20_memory/corrections.md` → C-3（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
