---
id: dk-p16-validate-reads-state-json
title: "P-16：validate 优先读取 state.json 而非文件 frontmatter"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: system
source_context: "pitfalls.md P-16"
source_refs:
  - .agent/pitfalls.md#P-16
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-p15-claimed-done-not-verified
  - master-systems-thinking
related:
  - master-first-principles
  - master-systems-thinking
pipeline:
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---

# P-16：validate 优先读取 state.json 而非文件 frontmatter

## 原始表述

> **症状**：在文件 frontmatter 里更新了 `source_refs` 和 `wiki_refs`，`kdo validate` 仍然报 "Missing"。
>
> **根因**：`validate_artifact()` 优先读取 `artifact.get("source_refs")`——数据来自 `.kdo/state.json`，不读文件 frontmatter。同时 `90_control/artifact-registry.yaml` 又是第三份拷贝。三处数据独立维护、可以不一致，没有同步机制。
>
> **对策**：
> - **短期**：修改后必须同时更新 state.json（用 Python 脚本 or `kdo` 命令）
> - **长治**：validate 应以文件 frontmatter 为 source of truth，state.json 和 registry 只做缓存/索引。发现不一致时自动同步或报 warning
> - **优先级**：P1——每次手动改文件都要记住还有 state.json，极易遗忘

## 使用场景

- 你手动修改了卡片的 frontmatter（如 `source_refs`、`wiki_refs`），但 `kdo validate` 仍然报错
- 你在调试"明明改了为什么还报 Missing"的问题
- 你在设计数据流时，需要确定哪份数据是 source of truth
- 你在维护 KDO 系统时，需要理解 state.json 和文件系统之间的关系

## 操作方法

1. **确认数据来源**：在手动修改 frontmatter 前，先确认 validate 读的是哪份数据——state.json 还是文件？
2. **同步更新多处**：手动修改 frontmatter 时，同步更新 `.kdo/state.json` 和 `artifact-registry.yaml`（如果存在）
3. **用脚本更新**：如果可能，用 `kdo` 命令（如 `kdo update` 或自定义脚本）来更新，而非手动编辑，确保多处同步
4. **验证修复**：更新后运行 `kdo validate`，确认报错已消除
5. **以文件为准**：如果需要确保一致性，始终以文件 frontmatter 为准，然后将其同步到 state.json 而非反之

## 适用边界

- 适用于所有涉及手动修改 KDO 卡片 frontmatter 的场景
- 不适用于通过 `kdo` 命令自动更新的场景——命令通常会自动同步 state.json
- 如果 state.json 和文件之间已经有自动同步机制，此问题可能已经被解决
- 三份数据拷贝（文件、state.json、registry.yaml）是一个设计缺陷，而非配置错误——即使每个人都按步骤操作，仍然可能出现不一致
- **长治方案是单一 truth source**，而非多份拷贝——这需要系统层面的修改

## 为什么值钱

- 这是 KDO 特有的数据一致性问题：**同一个信息存储在三个独立的地方，没有同步机制**
- "修改了文件但 validate 还报错"极其迷惑人——用户会认为自己的修改没问题，从而怀疑系统是不是坏了
- 揭示了系统设计中的一个核心原理：**多份数据拷贝必然导致不一致，唯一的解决方案是单一 truth source + 自动同步**
- 任何 AI 训练语料中都不会有"KDO 的 validate 优先读取 state.json 而非文件 frontmatter"这条知识

## 与其他知识的关联

- dk-p15-claimed-done-not-verified — 同一模式："验证结果不可靠"。P-15 是"执行者的报告不可信"，P-16 是"系统的验证逻辑读错了数据源"——两者都是"以为已验证但实际验证的是错误的东西"
- master-systems-thinking — 系统思维中的"状态一致性"原则：当同一信息存储在多个独立位置时，必须有明确的 truth source 和同步机制，否则不一致是必然结果
- `.agent/pitfalls.md` → P-16（原始记录，未编号段落）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
