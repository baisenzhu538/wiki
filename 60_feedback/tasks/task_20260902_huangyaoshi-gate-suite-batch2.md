---
id: task_20260902_huangyaoshi-gate-suite-batch2
title: 门禁套件批2：git 大文件三层门禁（391MB zip 断 push 3 个月实证）+ complete 交付未入仓 WARNING（#622 打回实证）
seq: 625
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-03
decision_source: 老顽童建议书 diag_20260902_laowantong-large-file-git-gate + 欧阳锋建议书 prop_20260902_ouyangfeng-complete-gate-uncommitted-deliverables（09-03 王语嫣裁定并单）
reviewer: 欧阳锋
instance: huangyaoshi-kimi
updated_at: '2026-09-02T16:21:06.517909+00:00'
---

# #625 门禁套件批2（黄药师）

## 任务 1：git 大文件三层门禁（老顽童建议书，事故背景：391MB zip 断 push 3 个月、5826 commits 积压）

1. **.gitignore 规则扩展**（防新增）：inbox 压缩包/视频/采集大 json 白名单机制
2. **pre-commit 或 pre-submit 拦截**：git 跟踪文件 >100MB 硬拦、>15MB WARNING（现有 46MB mp4 族是增长中的雷）
3. **存量处置方案**：>15MB 在跟踪文件的清单+处置建议（漂移预警——只出清单和建议，不动文件，处置归王语嫣编排/老朱拍板）

## 任务 2：complete 交付未入仓 WARNING（欧阳锋建议书，#622 被打回实证：哨兵代码全在工作区没 commit）

`queue_transition.py complete` 对仓库内交付物路径加机械检查：涉及文件有未提交 diff/untracked → WARNING 打印+台账留痕（不拦截）。机器预审①可顺势补「已入仓」维度。

## 红线

- 任务 1 第三层只出清单不动文件
- 各项回归用例随附；门禁文案说人话（命中时告诉生产者怎么办）

## 交付

- 两任务 diff + 回归 + 存量大文件清单 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 625）
