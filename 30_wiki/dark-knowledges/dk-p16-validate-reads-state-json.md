---
id: dk-p16-validate-reads-state-json
title: P-16：validate 优先读取 state.json 而非文件 frontmatter
type: dk
dark_knowledge_type: failure
status: reviewed
domain: master
source_person: system
source_context: pitfalls.md P-16
source_refs:
- 10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[kdo-yaml-frontmatter-safety]]'
- '[[yt-foresight-ab-steady-state]]'
- '[[dk-state-residue-is-the-silent-killer]]'
- '[[dk-f3-state-json-race-condition]]'
- '[[proposal-yaml-frontmatter-standardization]]'
- '[[dk-ji-hao-newbie-can-validate]]'
- '[[tool-yitang-research-validate-assumption]]'
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: system
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
---

# P-16：validate 优先读取 state.json 而非文件 frontmatter

## 原始表述 / 核心洞察

> **症状**：在文件 frontmatter 里更新了 `source_refs` 和 `wiki_refs`，`kdo validate` 仍然报 "Missing"。
>
> **根因**：`validate_artifact()` 优先读取 `artifact.get("source_refs")`——数据来自 `.kdo/state.json`，不读文件 frontmatter。同时 `90_control/artifact-registry.yaml` 又是第三份拷贝。三处数据独立维护、可以不一致，没有同步机制。
>
> **对策**：
> - **短期**：修改后必须同时更新 state.json（用 Python 脚本 or `kdo` 命令）
> - **长治**：validate 应以文件 frontmatter 为 source of truth，state.json 和 registry 只做缓存/索引。发现不一致时自动同步或报 warning
> - **优先级**：P1——每次手动改文件都要记住还有 state.json，极易遗忘

**核心洞察**：当同一信息被存储在多个独立位置且缺乏自动同步时，"修改了 A 却读 B" 的迷惑性错误必然发生。验证逻辑必须以单一 truth source 为准，缓存只能作为派生视图。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **确认数据来源**：在手动修改 frontmatter 前，先确认 validate 读的是哪份数据——state.json 还是文件？
2. **同步更新多处**：手动修改 frontmatter 时，同步更新 `.kdo/state.json` 和 `artifact-registry.yaml`（如果存在）
3. **用脚本更新**：如果可能，用 `kdo` 命令（如 `kdo update` 或自定义脚本）来更新，而非手动编辑，确保多处同步
4. **验证修复**：更新后运行 `kdo validate`，确认报错已消除
5. **以文件为准**：如果需要确保一致性，始终以文件 frontmatter 为准，然后将其同步到 state.json 而非反之

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 表象 | 根因 | 修复 / 规避 |
|---|---|---|---|
| 修改 frontmatter 后 validate 仍报 Missing | 手动更新了 `source_refs` / `wiki_refs`，`kdo validate` 依旧报错 | validate 优先读取 `.kdo/state.json` 中的缓存，而非文件 frontmatter | 同步更新 `.kdo/state.json`；优先使用 `kdo` 命令或脚本统一写入 |
| 三份数据互相不一致 | 同一卡片的 `source_refs` / `wiki_refs` 在文件、state.json、registry.yaml 中值不同 | 三处数据独立维护，无自动同步机制 | 明确以文件 frontmatter 为唯一 truth source，其他两处仅作缓存/索引并自动同步 |
| 误以为是系统 bug | 反复检查文件修改无误，验证结果却始终未变 | 不了解 validate 的数据读取优先级 | 排障时先检查 `.kdo/state.json` 中的缓存值，再核对文件 frontmatter |

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

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
