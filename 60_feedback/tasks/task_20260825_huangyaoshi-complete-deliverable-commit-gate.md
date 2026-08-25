---
id: 522
assignee: huangyaoshi
status: in_progress
updated_at: '2026-08-25T05:07:14.969520+00:00'
version: v0.1
instance: huangyaoshi
---

# #522 complete 提审门禁增「交付物已入仓」校验（E040 机器兜底）

- **任务号**：#522
- **状态**：queued
- **assignee**：huangyaoshi（queue_transition complete 门禁扩展；欧阳锋终审）
- **优先级**：P1（一晚 2 次同族实证：#470 脏文件提审 / #518 清单 219KB untracked 提审——人审口径无机器兜底）
- **立项**：2026-08-25 王语嫣（欧阳锋建议书 `diag_20260825_ouyangfeng-complete-deliverable-commit-gate.md` 裁定采纳）

## 背景

`queue_transition complete` 自动 commit 只收任务单+队列+dashboard，**交付物是否入仓零校验**——生产者忘了 feat commit 也一路绿灯。实证：#470 返工 4 卡 source_context 工作区脏文件提审（后补 commit 闭环）；#518 清单 219KB+scan-summary.json untracked 提审（complete commit 仅含任务单/队列/dashboard）。E040「未 commit=未发生」在执行端无机器兜底；三问条款（#362）已有「修复未提交=不存在」人审口径，本单=机器化前移。

## 任务

1. complete 门禁（F-034 家族）增一步校验：扫描任务单执行报告提到的交付物路径（或 code_files 声明）→ `git ls-files` 校验已跟踪 + `git status` 校验该路径无未提交改动——未入仓即拦，提示先 feat commit
2. **不误拦**：任务单明确声明「交付物=纯任务单修改」（编排/诊断类）的豁免；校验失败给清晰补救指令（git add + commit 命令模板）
3. 回归用例：脏交付物提审被拦+补救指令可读；豁免声明单不误拦；已入仓交付物正常通过

## 验证（验证分层）

- L1：单测三分支（脏拦/净过/豁免过）
- L2 狗粮：回放 #518 清单批场景（untracked 清单+complete）→ 拦截触发且提示正确
- L3 待活体：下一次「忘 commit 提审」当场被拦（不再等欧阳锋审出来）

## 边界

- 只加 complete 端校验，不动 review/claim 路径
- 交付物路径识别先启发式（执行报告改动文件清单节+code_files），识别不出=WARNING 不硬拦（防误拦优先，红线 4）
- 与 #505 增补件 S2②（落盘即 path-scoped commit 约定）互补：那份是约定层，本单是机器兜底——不互相替代
- 同文件区注意：queue_transition 近期改动频繁（#503/#504 已终审），施工前读最新 HEAD（§3.16 行动前复核）

## 关联

- 欧阳锋建议书（一晚 2 次实证表完整）
- E040（未 commit=未发生）/ #362（三问条款人审口径）/ F-034 门禁家族
- #505（共享文件写纪律，约定层同族）/ charter §3.17 红线 4（误拦优先于漏放——本单识别不出时 WARNING 即此原则）

## 需要谁动作

- **黄药师**：门禁扩展 + 回归
- **欧阳锋**：终审本单
