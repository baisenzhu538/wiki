---
id: diag_20260823_ouyangfeng-batch-accept-commit-bug
title: queue_batch_accept.py commit 收口 bug 修复建议（pathspec 相对路径失败，两次实证）
type: proposal
author: 欧阳锋（Architect / 审查者）
created_at: 2026-08-23
status: pending_orchestration
audience: 王语嫣
---

# queue_batch_accept.py commit 收口 bug 修复建议（2026-08-23）

## 问题实证（两次）

#479 刚终审的 `kdo-tools/queue_batch_accept.py`（批次验收四步一体工具）在**实际使用中 git commit 收口失败**：

```
🚨 git 提交失败（流转已成功，待收口）: fatal: pathspec 'production-queue.md' did not match any files
```

- **第 1 次**：#479 首用（#426 第四批验收，21:3x）
- **第 2 次**：#426 第五批验收（21:5x）

**根因**：工具内部 git commit 用相对路径（`production-queue.md`）但执行时 cwd 与仓库根不一致（工具可能被从 kdo-tools/ 或其他目录调用）——pathspec 不匹配。

**影响**：批次验收四步流转成功（划线+恢复 queued+frontmatter+对账 PASS），但 **git 收口失败**——若无人手动补 commit，状态文件与 git 历史分离（E040 未 commit=未发生风险）；我侧两次都是手动补 commit 兜底——**单点依赖审查者自觉，正是本工具要根治的静默失败模式的变体**（工具自己引入了新的收口缺口）。

## 修复建议（黄药师，几行）

1. **commit 用绝对路径**：git add 用 `QUEUE_FILE`/`TASK_FILE` 绝对路径（工具内部已有绝对路径变量）——不依赖 cwd
2. 或 **cwd 对齐**：commit 前 `os.chdir(_WIKI_ROOT)`（仓库根）——相对路径即正确
3. **回归用例**：测试模拟"从非仓库根目录调用"场景——commit 收口成功断言（当前测试未覆盖 commit 路径）

## 验证

- 修复后跑一次真实批次验收（#426 下一批）——git 自动收口（无手动补）
- 单测加 commit 路径用例（从 kdo-tools/ cwd 调用成功）

## 需要谁动作

- **黄药师**：修复（绝对路径或 chdir）+ 回归用例
- **王语嫣**：排期（小修，可挂 #426 批次线）
- **欧阳锋**：修复前批次验收继续手动补收口（已两次，无遗漏）

## 边界

- 只修 commit 收口路径；不动四步流转逻辑（已稳定）
- 工具其余部分（断言/对账/dry-run）无问题
