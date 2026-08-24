---
id: diag_20260825_ouyangfeng-complete-deliverable-commit-gate
title: complete 提审门禁缺"交付物已入仓"校验——一晚 2 次未 commit 提审
type: proposal
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: '2026-08-25'
source: "#470 返工（4 卡脏文件提审）+ #518（清单 219KB+summary untracked 提审）一晚 2 次实证"
---

# complete 门禁增"交付物入仓"校验（同族第 2 次，铁律升级）

## 现象（一晚 2 次同族）

| 单 | 交付物 | 状态 |
|:--|:--|:--|
| #470 返工 | 4 卡 source_context 修改 | 工作区脏文件提审（后补 19a59e778 闭环） |
| #518 清单批 | 清单 219KB + scan-summary.json | untracked（`??`），complete commit 仅含任务单/队列/dashboard |

`queue_transition complete` 只收任务单+队列+dashboard，**交付物是否入仓零校验**——生产者忘了 feat commit 也一路绿灯（E040"未 commit=未发生"在执行端无机器兜底）。

## 建议（最小改动）

complete 门禁（F-034 家族）增一步：**扫描任务单执行报告提到的交付物路径（或 code_files 声明），git ls-files 校验已跟踪 + git status 校验无该路径未提交改动**——未入仓即拦，提示先 feat commit。三问条款（#362）已有"修复未提交=不存在"的人审口径，本建议=把人审口径机器化前移。

## 边界

- 不误拦：任务单明确声明"交付物=纯任务单修改"（如编排/诊断类）的豁免；校验失败给清晰补救指令（git add + commit 命令模板）
- 与 #505 增补件 S2②（落盘即 path-scoped commit）同族——本建议是机器兜底，那份是约定层

*欧阳锋 · 2026-08-25 · 同族第 2 次实证触发铁律升级（v2.3 规则 11）*
