---
id: dk-f4-wrong-workdir
title: F-KDO-004：错误工作目录执行 pipeline 命令→命令静默失败、无报错、无文件变更
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-004
source_refs:
- 10_raw/sources/src_20260619_d967c8f5_90_control_failure_modes.md#F-KDO-004
created_at: 2026-05-31
updated_at: '2026-06-19'
related:
- '[[dk-c10-batch-tool-no-dry-run]]'
- '[[master-decision-hygiene]]'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-reviewed
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 命令返回 0 但无任何文件变化
- 在非 wiki 根目录（如 ~/.claude/plugins/）执行 kdo pipeline 命令
- 执行后 state.json 或目标文件的时间戳/哈希 unchanged
---# F-KDO-004：错误工作目录执行 pipeline 命令→命令静默失败、无报错、无文件变更

## 原始表述/核心洞察

> **触发命令**：`kdo revise --scan`, `kdo improve --apply` 等
>
> **表现**：命令静默失败——不报错、不更新文件、不改变 state.json
>
> **根因**：命令依赖 `find_workspace()` 定位 wiki 根目录。从非 wiki 目录（如 `~/.claude/plugins/`）执行时，`find_workspace()` 要么找不到要么找到错误的目录
>
> **触发信号**：命令返回 0 但无任何文件变化
>
> **防御措施**：① 命令启动时打印当前识别的 workspace root ② `find_workspace()` 失败时 exit(1) 并给出明确信息而非静默降级 ③ 在 AGENTS.md 禁止清单中列出
>
> **禁止行为**：**不准在 `~/.claude/plugins/` 或任何非 wiki 根目录下执行 KDO pipeline 命令**
>
> **正确做法**：始终 `cd /mnt/c/Users/Administrator/Desktop/wiki` 后执行

核心洞察：**KDO pipeline 命令对工作目录有强依赖，而 CLI 的静默降级让“跑错目录”看起来像是“成功执行”**。只要当前目录不是 wiki 根目录，`find_workspace()` 就可能定位失败或定位到错误的目录，后续所有文件/状态操作都在错误上下文中运行，结果是无报错、无变更、无反馈——这是最危险的失败形态。

## 使用场景

- 你刚打开一个新的终端/session， tempted 直接运行 `kdo improve --apply` 而没有先确认当前目录
- 你从其他项目的目录（如 `~/.claude/plugins/`、`~/Downloads/`）切换过来，忘记 `cd` 到 wiki 根目录
- 你写自动化脚本或 cron job 调用 kdo 命令时，需要确保工作目录设置正确
- 你调试一个"命令返回成功但没有任何效果"的问题，需要排查是否是工作目录错误

## 操作方法

1. **执行前确认目录**：运行任何 kdo pipeline 命令前，先执行 `pwd` 确认当前目录是 wiki 根目录
2. **标准化入口**：将 wiki 根目录路径写入环境变量或别名，如 `alias kdo-cd='cd /mnt/c/Users/Administrator/Desktop/wiki'`
3. **脚本中显式切换**：在自动化脚本开头加入 `cd /mnt/c/Users/Administrator/Desktop/wiki || exit 1`
4. **观察命令输出**：注意 kdo 命令启动时打印的 `workspace root` 信息——如果识别的根目录不对，立即停止
5. **验证副作用**：执行后检查 `state.json` 或目标文件是否有变化，确认命令实际生效

## 适用边界

- 适用于所有会修改 wiki 内容或 state 的 KDO pipeline 命令（`kdo improve`、`kdo revise`、`kdo scaffold --write` 等）
- 不适用于只读查询命令（`kdo query`、`kdo lint`、`kdo validate`）——这些命令即使工作目录错误也通常不会破坏数据
- `find_workspace()` 的查找逻辑是向上遍历父目录直到找到 `.kdo/` 文件夹——如果你在 wiki 的子目录中执行，可能也能工作，但不建议依赖这个行为
- 在 CI/CD 或远程执行环境中，工作目录的设置更加关键——必须在脚本中显式 `cd`

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|---|---|---|---|
| 工作目录错误导致 `find_workspace()` 静默降级 | `pwd` 不是 wiki 根目录；命令返回 0 但无文件变化 | CLI 从非 wiki 目录启动，`find_workspace()` 找不到 `.kdo/` 或找到错误目录，工具默认不报错 | 执行前先 `cd` 到 wiki 根目录；脚本中使用 `cd /path/to/wiki \|\| exit 1` |
| 依赖子目录的隐式上游遍历 | 在 wiki 子目录（如 `30_wiki/`）执行也能“成功” | `find_workspace()` 向上遍历父目录直到发现 `.kdo/` | 始终切换到 wiki 根目录，不依赖隐式定位 |
| CI/远程脚本未设置工作目录 | cron、ssh 或 CI 中直接调用 kdo | 环境默认目录不是 wiki | 脚本开头强制 `cd` 并校验 `.kdo/` 目录存在 |
| 只看 exit code 0 不检查副作用 | 命令“成功”但 state.json/目标文件 unchanged | 静默降级未生成错误 | 执行后检查目标文件哈希或状态变化，确认实际生效 |

## 为什么值钱

- 这是 KDO CLI 特有的行为：`find_workspace()` 的静默降级设计让错误工作目录下的执行看起来"成功"了
- **"返回 0 但什么都不做"是最危险的失败模式**：没有错误信息可供调试，用户只能靠经验猜测"是不是目录错了"
- 暴露了 CLI 工具设计中"默认行为 vs 显式失败"的权衡：KDO 选择了静默降级（兼容子目录执行），代价是错误工作目录时完全不报错
- 任何 AI 训练语料中都不会有"kdo improve 在 ~/.claude/plugins/ 下执行会静默失败"这条知识

## 与其他知识的关联

- [[dk-c10-batch-tool-no-dry-run]] — 同一深层模式：自动化操作前的环境确认缺失。C-10 是"跳过 dry-run 验证"，F-KDO-004 是"跳过工作目录确认"——两者都是"本应人工确认的节点被惯性跳过"
- [[master-decision-hygiene]] — 决策卫生 Step 1：在执行任何操作前，先确认前提条件（此处是"我在正确的目录下吗？"）
- `90_control/failure-modes.md` → F-KDO-004（原始记录）
- `90_control/AGENTS.md` → 禁止清单 #2（不准在非 wiki 根目录执行 pipeline 命令）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
