---

id: dk-c7-auto-backup-conflict
title: C-7：Obsidian auto-backup 干扰 commit 拆分→staged 文件被自动打包提交
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: Builder
source_context: 2026-05-03
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- [[dk-p14-zombie]]
- [[dk-p15-unverified]]
- [[obsidian-git-sync-protocol]]
- [[EC工业化规范手册]]
- [[dk-c10-batch-tool-no-dry-run]]
- [[master-knowledge-compound]]
- [[dk-c8-format-complete-mind-empty]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: src_unknown
  framework_lens: Obsidian Git 的 auto-backup 约每 20 分钟触发一次，会提交所有已 staged 的变更
  follow_up_question: 检查提交内容是否跨类型混合；若已混合，评估是否需要 `git reset` 或 `git rebase -i` 重新拆分
- signal: src_unknown
  framework_lens: auto-backup 不识别用户的 commit 拆分意图，只识别 staged 状态
  follow_up_question: 下次拆分 commit 时，是否先 stage 一组立即 commit，再处理下一组？
- signal: src_unknown
  framework_lens: commit 历史被永久性破坏，后续 `git blame`、`git revert`、`git log --grep` 都会失效
  follow_up_question: 该 backup commit 是否需要拆分重建，以恢复可检索、可回滚的历史？# C-7：Obsidian auto-backup 干扰 commit 拆分→staged 文件被自动打包提交
---
## 原始表述 / 核心洞察

> staged 了文件准备手动按类型拆分为 3 个 commit，auto-backup 抢在前面把所有 37 个文件打成了一个 backup commit。
>
> 根因：Obsidian Git 插件的 auto-backup 定时（约 20 分钟）自动提交所有已 staged 的变更。
>
> 修正：如果要拆分 commit，不要一次 stage 所有文件——先 stage 一组 → commit → 再 stage 下一组。或者临时关闭 auto-backup。

**核心洞察**：在常规 Git 工作流里，"先 stage 再分批 commit"是天经地义的操作；但 Obsidian Git 的 auto-backup 把 "staged = 待提交" 这个中间状态当作可自动提交的信号。工具链叠加后，**一个本来安全的中间状态变成了风险窗口**。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别风险时机**：Obsidian Git 的 auto-backup 约每 20 分钟触发一次，会自动提交所有已 staged 的变更
2. **分步 stage，不要一次性全加**：如果要拆 3 个 commit，只 `git add` 第一组文件（如 `git add 30_wiki/concepts/new-card.md`）
3. **立即 commit 第一组**：`git commit -m "feat: add X concept card"`
4. **再 stage 第二组** → commit → 再 stage 第三组 → commit
5. **备选方案**：如果必须一次性 stage 所有文件（如批量重命名），临时关闭 auto-backup（Obsidian → Settings → Community Plugins → Obsidian Git → 关闭 Auto Backup）→ 手动拆 commit → 完成后再开启

## 适用边界

| 边界 | 说明 |
|:
--|:------|
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
