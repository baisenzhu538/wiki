---
id: 482
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-23T15:51:54.153736+00:00'
version: v0.1
depends_on:
- 479
instance: huangyaoshi
---
# #482 queue_batch_accept.py commit 收口 pathspec bug 修复（#479 修单）

- **任务号**：#482
- **状态**：queued
- **assignee**：huangyaoshi（基建单一实例；终审=欧阳锋；编排=王语嫣）
- **优先级**：P1（#426 批次线正在用 #479，收口 bug 影响 E040「未 commit=未发生」）
- **立项**：2026-08-24 王语嫣（欧阳锋建议书 `diag_20260823_ouyangfeng-batch-accept-commit-bug` 裁定采纳，两次实证）
- **依赖**：#479（#479 queue_batch_accept.py 已 reviewed，本单修其 commit 收口 bug）

## 背景（欧阳锋两次实证）

#479 刚终审的 `kdo-tools/queue_batch_accept.py` 实际使用中 **git commit 收口失败**：
```
🚨 git 提交失败（流转已成功，待收口）: fatal: pathspec 'production-queue.md' did not match any files
```
- 第 1 次：#479 首用（#426 第四批验收，21:3x）
- 第 2 次：#426 第五批验收（21:5x）

**根因**：工具内部 git commit 用相对路径（`production-queue.md`），但执行时 cwd 与仓库根不一致（从 kdo-tools/ 或其他目录调用）——pathspec 不匹配。

**影响**：批次验收四步流转成功（划线+恢复 queued+frontmatter+对账 PASS），但 git 收口失败——状态文件与 git 历史分离（E040 风险）；欧阳锋两次手动补 commit 兜底——**工具自己引入了新的收口缺口**（要根治静默失败的工具自己有静默收口 bug）。

## 任务

### 修复（二选一或组合，黄药师定）
1. **commit 用绝对路径**：git add 用 `QUEUE_FILE`/`TASK_FILE` 绝对路径（工具内部已有绝对路径变量）——不依赖 cwd
2. **cwd 对齐**：commit 前 `os.chdir(_WIKI_ROOT)`（仓库根）——相对路径即正确

### 回归用例
- 测试模拟"从非仓库根目录调用"场景（如 cwd=kdo-tools/）——commit 收口成功断言
- 当前测试未覆盖 commit 路径（#479 测试盲区，E028 同族：测试覆盖≠全功能正确）

## 验证
- L1：单测加 commit 路径用例（从 kdo-tools/ cwd 调用成功）
- L2 狗粮：#426 下一批真实批次验收走 #479——git 自动收口（无手动补）
- L3 待活体：连续 N 批零手动补 commit

## 边界
- 只修 commit 收口路径；不动四步流转逻辑（已稳定：断言/对账/dry-run 无问题）
- 工具其余部分无改动
- E050 commit path-scoped 纪律保留（禁 add -A）

## 关联
- 欧阳锋建议书 `diag_20260823_ouyangfeng-batch-accept-commit-bug`（裁定采纳立项）
- #479（queue_batch_accept.py 工具，已 reviewed，本单修其 bug）/ #426（tags 分批治理，批次线）/ #453（queue-archive 复用模式）
- E040（未 commit=未发生）/ E050（commit path-scoped）/ E028（测试覆盖≠全功能）

## 需要谁动作
- **黄药师**：修复（绝对路径或 chdir）+ 回归用例
- **欧阳锋**：修复前批次验收继续手动补收口（已两次无遗漏）；终审本单
- **王语嫣**：编排核验（#426 下一批走 #479 自动收口验证）

## 执行报告（2026-08-23 黄药师）

**完成内容**：#479 queue_batch_accept.py commit 收口 pathspec bug 修复——git add 路径从 basename 改 relative_to(WIKI) 相对路径（+git -C WIKI），任意 cwd 调用均正确。

**交付物**（改动文件清单）：
1. `kdo-tools/queue_batch_accept.py`：新增 `_commit_add_paths(task_id)`（relative_to(WIKI) 相对路径）+ `_git_commit` 改用它
2. `kdo-tools/tests/test_queue_batch_accept.py`：TestCommitPaths 2 用例（路径相对根断言 + 真实队列文件 git add --dry-run 从任意 cwd 成功）

**验证**（命令+输出）：
- L1 单测：`pytest tests/test_queue_batch_accept.py` → **7 passed**；kdo-tools 全量 → **62 passed**
- L2 狗粮：①根因复现——旧代码 `QUEUE_FILE.name`="production-queue.md"（basename）但文件在 `70_product/tasks/` 子目录，pathspec 必然不匹配（欧阳锋两次实证同因）；②修复后 `git add --dry-run <relative_to(WIKI)>` 从任意 cwd 返回 0；③修复前测试覆盖盲区（#479 测试未覆盖 commit 路径，E028 同族）已补
- L3 待活体：#426 第六批验收走工具，commit 收口自动成功实证（E040 缺口闭合）

**未做项**：
- 无

**需要谁动作**：
- 王语嫣：#426 后续批次验收继续走工具（commit 收口已修）
- 欧阳锋：终审本单（抽「路径构造/回归用例/狗粮」）
