---
id: dk-c7-auto-backup-conflict
title: "C-7：Obsidian auto-backup 干扰 commit 拆分→staged 文件被自动打包提交"
type: dark-knowledge
dark_knowledge_type: failure
status: draft
domain:
  - master
source_person: Builder
source_context: 2026-05-03
source_refs:
  - 20_memory/corrections.md#C-7
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - dk-c10-batch-tool-no-dry-run
  - master-knowledge-compound
pipeline:
  - confidence-draft
  - confidence-source-cited
author: legacy
reviewed_by: pending
confidence: 0.7
trust_level: low
---

# C-7：Obsidian auto-backup 干扰 commit 拆分→staged 文件被自动打包提交

## 原始表述

> staged 了文件准备手动按类型拆分为 3 个 commit，auto-backup 抢在前面把所有 37 个文件打成了一个 backup commit。
>
> 根因：Obsidian Git 插件的 auto-backup 定时（约 20 分钟）自动提交所有已 staged 的变更。
>
> 修正：如果要拆分 commit，不要一次 stage 所有文件——先 stage 一组 → commit → 再 stage 下一组。或者临时关闭 auto-backup。

## 使用场景

- 你在 Obsidian 中编辑 KDO vault，准备把不同类型的变更拆分成独立的 commit（如"新增概念卡"、"修复格式"、"更新索引"）
- 你 `git add` 了一批文件准备分批 commit，但还没开始拆分时突然有事离开
- 你发现 commit 历史里出现了一个名为 "backup" 或 "auto backup" 的 commit，包含了本应分开提交的变更
- 你使用 Obsidian Git 插件管理 vault，需要理解 auto-backup 的行为边界

## 操作方法

1. **识别风险时机**：Obsidian Git 的 auto-backup 约每 20 分钟触发一次，会自动提交所有已 staged 的变更
2. **分步 stage，不要一次性全加**：如果要拆 3 个 commit，只 `git add` 第一组文件（如 `git add 30_wiki/concepts/new-card.md`）
3. **立即 commit 第一组**：`git commit -m "feat: add X concept card"`
4. **再 stage 第二组** → commit → 再 stage 第三组 → commit
5. **备选方案**：如果必须一次性 stage 所有文件（如批量重命名），临时关闭 auto-backup（Obsidian → Settings → Community Plugins → Obsidian Git → 关闭 Auto Backup）→ 手动拆 commit → 完成后再开启

## 适用边界

- 适用于所有使用 **Obsidian Git 插件** 且需要**手动拆分 commit** 的场景
- **不适用于单个 commit 就能搞定的简单变更**：如果只有 1-2 个文件且逻辑单一，auto-backup 不会带来问题
- 如果 Obsidian 关闭或 vault 未打开，auto-backup 不会触发——风险只在 Obsidian 运行期间存在
- 如果 vault 不在 Git 管理下，此问题完全不存在
- 使用命令行 Git（而非 Obsidian Git 插件）时，auto-backup 不会干扰——这是插件特有的行为
- 团队协作场景下，混乱的 commit 历史会影响 `git blame` 和回滚操作，代价更高

## 为什么值钱

- **Obsidian Git auto-backup + staged 文件的行为组合是 KDO 工作流特有的**：在任何 Git 教程里，" staged 文件等待 commit"是天经地义的操作，没有人会提醒你"定时插件会偷走你的 staged 变更"
- 这个坑的代价不是"丢了一个文件"，而是 **commit 历史被永久性破坏**：37 个文件被打成一个无意义的 "backup" commit，无法按类型回滚、无法做 `git blame` 追踪
- 揭示了工具链叠加时的涌现问题：Obsidian Git 单独使用没问题，Git 单独使用也没问题，但两者叠加 + staged 文件 + 20 分钟定时器 = 灾难
- 任何 AI 训练语料中都不会有"Obsidian Git 的 auto-backup 会把你 staged 的文件全部打包提交"这条知识——这是具体插件、具体工作流、具体操作顺序三者叠加的产物

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一模式：自动化工具在不合时宜的时机执行操作。C-10 是 scaffold 在未经验证时跑批量，C-7 是 auto-backup 在 commit 拆分完成前自动提交——两者都是"自动化抢占了本应人工控制的节点"
- [[master-knowledge-compound]] — 知识复利的前提是"可检索、可溯源的 commit 历史"。C-7 破坏的不仅是当前 commit，更是未来所有依赖 `git log`、`git blame`、`git revert` 的知识复利积累
- `20_memory/corrections.md` → C-7（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
