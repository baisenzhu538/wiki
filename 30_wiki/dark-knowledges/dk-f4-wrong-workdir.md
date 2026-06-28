---

id: dk-f4-wrong-workdir
title: F-KDO-004：错误工作目录执行 pipeline 命令→命令静默失败、无报错、无文件变更
type: dk
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-004
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-19'
related:
- [[knowledge-delivery-os-快速体验指南-飞书云文档]]
- [[dk-f3-state-json-race-condition]]
- [[modeling-capability-for-kdo]]
- [[proposal-kdo-flywheel-infrastructure]]
- [[workflow-knowledge-collision]]
- [[dk-c10-batch-tool-no-dry-run]]
- [[master-decision-hygiene]]
pipeline:
- src_unknown
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# F-KDO-004：错误工作目录执行 pipeline 命令→命令静默失败、无报错、无文件变更
---
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

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **执行前确认目录**：运行任何 kdo pipeline 命令前，先执行 `pwd` 确认当前目录是 wiki 根目录
2. **标准化入口**：将 wiki 根目录路径写入环境变量或别名，如 `alias kdo-cd='cd /mnt/c/Users/Administrator/Desktop/wiki'`
3. **脚本中显式切换**：在自动化脚本开头加入 `cd /mnt/c/Users/Administrator/Desktop/wiki || exit 1`
4. **观察命令输出**：注意 kdo 命令启动时打印的 `workspace root` 信息——如果识别的根目录不对，立即停止
5. **验证副作用**：执行后检查 `state.json` 或目标文件是否有变化，确认命令实际生效

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 常见失败模式

| 失败模式 | 典型信号 | 根因 | 修复动作 |
|
|---|---|---|
| 工作目录错误导致 `find_workspace()` 静默降级 | `pwd` 不是 wiki 根目录；命令返回 0 但无文件变化 | CLI 从非 wiki 目录启动，`find_workspace()` 找不到 `.kdo/` 或找到错误目录，工具默认不报错 | 执行前先 `cd` 到 wiki 根目录；脚本中使用 `cd /path/to/wiki \|\| exit 1` |
| 依赖子目录的隐式上游遍历 | 在 wiki 子目录（如 `30_wiki/`）执行也能“成功” | `find_workspace()` 向上遍历父目录直到发现 `.kdo/` | 始终切换到 wiki 根目录，不依赖隐式定位 |
| CI/远程脚本未设置工作目录 | cron、ssh 或 CI 中直接调用 kdo | 环境默认目录不是 wiki | 脚本开头强制 `cd` 并校验 `.kdo/` 目录存在 |
| 只看 exit code 0 不检查副作用 | 命令“成功”但 state.json/目标文件 unchanged | 静默降级未生成错误 | 执行后检查目标文件哈希或状态变化，确认实际生效 |

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
