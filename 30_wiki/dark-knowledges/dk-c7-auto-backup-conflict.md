---
id: dk-c7-auto-backup-conflict
title: C-7：Obsidian auto-backup 干扰 commit 拆分→staged 文件被自动打包提交
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- 10_raw/sources/src_20260619_f35cd8b6_20_memory_corrections.md#C-7
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[dk-c10-batch-tool-no-dry-run]]'
- '[[master-knowledge-compound]]'
- '[[dk-c8-format-complete-mind-empty]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-formatted
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: "`git log` 里突然出现名为 'backup' 或 'auto backup' 的 commit，且包含多个本应按类型拆分的变更"
  framework_lens: "Obsidian Git 的 auto-backup 约每 20 分钟触发一次，会提交所有已 staged 的变更"
  follow_up_question: "检查提交内容是否跨类型混合；若已混合，评估是否需要 `git reset` 或 `git rebase -i` 重新拆分"
- signal: "准备拆分 commit 时已 staged 多组文件，但中途离开/中断，回来后变更已被自动提交"
  framework_lens: "auto-backup 不识别用户的 commit 拆分意图，只识别 staged 状态"
  follow_up_question: "下次拆分 commit 时，是否先 stage 一组立即 commit，再处理下一组？"
- signal: "同一 backup commit 里同时出现概念卡、格式修复、索引更新等不同类型的变更"
  framework_lens: "commit 历史被永久性破坏，后续 `git blame`、`git revert`、`git log --grep` 都会失效"
  follow_up_question: "该 backup commit 是否需要拆分重建，以恢复可检索、可回滚的历史？"
---# C-7：Obsidian auto-backup 干扰 commit 拆分→staged 文件被自动打包提交

## 原始表述 / 核心洞察

> staged 了文件准备手动按类型拆分为 3 个 commit，auto-backup 抢在前面把所有 37 个文件打成了一个 backup commit。
>
> 根因：Obsidian Git 插件的 auto-backup 定时（约 20 分钟）自动提交所有已 staged 的变更。
>
> 修正：如果要拆分 commit，不要一次 stage 所有文件——先 stage 一组 → commit → 再 stage 下一组。或者临时关闭 auto-backup。

**核心洞察**：在常规 Git 工作流里，"先 stage 再分批 commit"是天经地义的操作；但 Obsidian Git 的 auto-backup 把 "staged = 待提交" 这个中间状态当作可自动提交的信号。工具链叠加后，**一个本来安全的中间状态变成了风险窗口**。

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

| 边界 | 说明 |
|:-----|:------|
| ✅ 适用 | 使用 Obsidian Git 插件且需要手动拆分 commit 的场景 |
| ❌ 不适用 | 单个 commit 就能搞定的简单变更（1-2 个文件且逻辑单一） |
| 时间窗口 | 风险只在 Obsidian 运行且 vault 已打开时存在；关闭 Obsidian 或 vault 未打开时不会触发 |
| 工具限定 | 使用命令行 Git（而非 Obsidian Git 插件）时，auto-backup 不会干扰 |
| 代价放大 | 团队协作场景下，混乱的 commit 历史会影响 `git blame` 和回滚操作，代价更高 |

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| 中途离开导致被 auto-backup 打包 | 准备拆 commit 时 staged 多组文件，中断后回来发现已生成 backup commit | 若已提交：用 `git reset --soft HEAD~1` 回到 staged 状态，重新分组 commit；若未推送可重写历史 |
| 一次性 stage 全部文件 | 习惯性 `git add .` 后想慢慢拆分，结果 auto-backup 在 20 分钟内提交全部 | 改成分组 stage：先 add 第一组 → commit → 再 add 第二组；或临时关闭 auto-backup |
| 误把 backup commit 当作完成 | 看到 backup commit 以为变更已安全提交，后续直接继续工作 | 检查该 commit 是否跨类型混合；若混合，使用 `git rebase -i` 拆分或 reset 后重新提交 |
| 关闭 auto-backup 后忘记开启 | 临时关闭后长期未恢复，失去自动备份保护 | 拆完 commit 后立即恢复 auto-backup；可在个人 checklist 中增加该检查项 |

## 为什么值钱

- **Obsidian Git auto-backup + staged 文件的行为组合是 KDO 工作流特有的**：在任何 Git 教程里，"staged 文件等待 commit"是天经地义的操作，没有人会提醒你"定时插件会偷走你的 staged 变更"
- 这个坑的代价不是"丢了一个文件"，而是 **commit 历史被永久性破坏**：37 个文件被打成一个无意义的 "backup" commit，无法按类型回滚、无法做 `git blame` 追踪
- 揭示了工具链叠加时的涌现问题：Obsidian Git 单独使用没问题，Git 单独使用也没问题，但两者叠加 + staged 文件 + 20 分钟定时器 = 灾难
- 任何 AI 训练语料中都不会有"Obsidian Git 的 auto-backup 会把你 staged 的文件全部打包提交"这条知识——这是具体插件、具体工作流、具体操作顺序三者叠加的产物

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一模式：自动化工具在不合时宜的时机执行操作。C-10 是 scaffold 在未经验证时跑批量，C-7 是 auto-backup 在 commit 拆分完成前自动提交——两者都是"自动化抢占了本应人工控制的节点"
- [[master-knowledge-compound]] — 知识复利的前提是"可检索、可溯源的 commit 历史"。C-7 破坏的不仅是当前 commit，更是未来所有依赖 `git log`、`git blame`、`git revert` 的知识复利积累
- [[dk-c8-format-complete-mind-empty]] — 同一深层模式：输出/状态看起来"完成"了（backup commit 已生成、format 已合规），但内部结构已失控。两者都提醒：不能只看表面完成，必须检查内容/结构是否符合意图
- `20_memory/corrections.md` → C-7（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
