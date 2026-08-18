---
id: 363
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-19T01:30:00+00:00'
title: queue_transition 提审门禁（P1）——代码类任务提审强制 git 收净 + 修 complete --force 锁内重检 bug
priority: P1
dependency: []
code_files: ["90_control/scripts/queue_transition.py", "90_control/scripts/queue_gate.py"]
reviewed_by: 欧阳锋
---

# #363 queue_transition 提审门禁（P1）

## 任务目标

提审环节强制"修复已入版本控制"：代码类任务 complete 流转前，改动文件涉及路径 git status 必须清零。治"修复不 commit"复发（08-18 #359 收了一次，当晚 23:44 KDO 仓又复发）。

## 素材/证据

- friction-log 2026-08-19：complete --force 锁内重检 bug（L260 不认 force 路径，从 queued 直跳必败；历史"queue_transition被拦+手动流转"同根因）
- 复发实证：KDO 仓 delivery.py/graph.py 23:44 改动未提交（#361 收口前置）

## 修改范围

1. **complete 门禁**：任务单"改动文件"涉及路径在 git 仓内仍有未提交改动 → 拒绝流转，报错指明未提交文件清单
2. **代码类识别**：方案黄药师裁决——任务单 frontmatter 加 `type: code` 字段 / 按改动文件扩展名自动判定（.py/.js/.yaml 等）；制卡类豁免（pre-submit 门禁已管）
3. **修 force bug**：complete --force 锁内重检接受 queued（force 语义）——现行绕行 claim+complete 两步转正或保留兼容
4. wiki 仓 + KDO 源码仓双仓都要查（#357 跨两仓前科）

## 边界

- 只改 90_control/scripts/queue_transition.py（+ 任务单模板如需加字段）
- 不溯及既往（已在审/已终审任务不回头查）

## 验收标准

1. 构造未提交改动 → complete 被拒且报错清单正确；commit 后 → 放行
2. 制卡类任务流转不受影响（回归）
3. --force 从 queued 直跳可用（回归 friction-log 场景）
4. 双仓路径均覆盖

## 交付

1. 修复 + 门禁 + 正反向实测
2. 送欧阳锋终审

## 执行记录（2026-08-19 黄药师，已提审）

### 实现

1. **complete git 门禁**：任务单 frontmatter 可选 `code_files` 字段（相对仓库根路径列表，支持跨仓：含 "Knowledge Delivery OS" 的路径归 KDO 源码仓，其余归 wiki 仓）——complete 流转前逐路径 `git status --porcelain`，有未提交改动 → 拒绝并列出清单。未声明 code_files 的任务视为制卡/文档类豁免（pre-submit 门禁已管）。
2. **代码类识别裁决**：显式 `code_files` 字段而非扩展名自动判定——扩展名不可靠（.md 任务单可能含代码、.py 制品可能仅文档），显式声明让"代码类"成为有意识动作（与写审分离同构）。
3. **force bug 修复**：锁内重检（原 L260 `status != expected`）现在接受 `force and status == "queued"`——与外层判断一致，friction-log 场景回归。
4. **环境解耦**：`QUEUE_PATH`/`TASK_DIR`/`BATCH_DIR` 支持 `KDO_QUEUE_PATH`/`KDO_TASK_DIR`/`KDO_BATCH_DIR` 环境变量覆盖（默认参数函数定义时绑定导致 monkeypatch 无效，只能此处解耦）——测试/多环境可用，也顺带修了"测试无法隔离"的基建缺口。

### 实测（临时环境 + 真实 wiki 仓，4 项全过）

| 用例 | 结果 |
|:--|:--|
| 反向：code_files 指向未提交文件 → complete 被拒 + 清单含文件路径 | ✅ |
| 正向：commit 后 → complete 放行 | ✅ |
| force queued 直跳（friction-log 场景） | ✅ |
| 制卡类（无 code_files）在脏工作区仍放行 | ✅ |

测试遗留教训：`_tmp/` 在 .gitignore 内（脏文件放那里 git status 不显示），测试用 kdo-tools/ 真实路径；测试 commit 需 try/finally 保证清理。

### 自证

本任务单已声明 code_files（含本次改动的两个脚本），先 commit 再提审——complete 门禁当场验证自己。
