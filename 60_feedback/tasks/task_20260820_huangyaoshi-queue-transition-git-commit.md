---
id: 390
assignee: huangyaoshi
status: queued
title: queue_transition 流转自带 git 收口（P2，老朱 08-20 拍板立项）——消灭"未入 git 窗口"
priority: P2
dependency: []
code_files:
- 90_control/scripts/queue_transition.py
---

# #390 queue_transition 流转自带 git 收口

## 来源

- E040（#387 事件）：编排产物未 commit=不进协作通道——欧阳锋读独立 git 同步 checkout，工作区文件对其不存在
- 王语嫣 08-20 机制观察：queue_transition.py **每次流转都制造新的"未入 git 窗口"**（claim/complete/review 写任务单+队列+dashboard 但不 commit）——#388/#389 claim 后状态在工作区躺了一轮才由王语嫣手工收口（5fe18c6b6）。手工收口依赖人记得，必然漏
- 老朱 08-20 拍板：立项。与 #389（REVIEW-PENDING 登记段）独立并行，不动在飞任务

## 任务目标

queue_transition.py 流转成功后自动把本次流转触碰的文件 commit 入 git，让"状态变更"与"入档"原子化——跨 checkout 协作者（欧阳锋等）任何时候读到的都是最新状态。

## 执行范围

1. **自动 commit**：claim/complete/review/release 成功后，自动 `git add` **仅限本次触碰的文件**（任务单 + production-queue.md + dashboard.html）并 commit，message 含任务号+流转动作（如 `chore(queue): #390 claim by huangyaoshi`）
2. **path-scoped add 是红线**：严禁 `git add -A`/`git add .`——工作区永远有其他 agent 的未提交在制品，流转 commit 只能带自己触碰的文件（误带=把别人的半成品塞进历史）
3. **失败语义定义**：git 失败（无仓/冲突/权限）不得吞错也不得阻断流转——流转本身已成功，git 失败要 stderr 醒目报警 + 写入某待收口清单（让下轮或巡检能兜住）
4. **与 #363 门禁的相对位置**：complete 的门禁拦截在前，门禁不过→不流转→也不 commit（顺序写清楚）
5. 评估项：是否给脚本加 `--no-commit` 逃生门（特殊场景手工控制），默认自动 commit

## 边界（不做的事）

- 不动状态机语义、不动 #363 门禁逻辑
- 不处理历史遗留未提交文件（其他 agent 的在制品不归本单收）
- 不碰在飞的 #389（E025 冻结）——两单都改 queue_transition.py，**黄药师自行串行：一单落地提审后再动另一单，或合并实施但分别提审**，避免同文件并发冲突
- 不替其他角色 commit 其产品（本单只管流转触碰的文件）

## 内容价值判断（PROTOCOL §7 合规声明）

- 仅机制代码新增，无删除/移动

## 验收标准

1. 正向实测：测试任务 claim → git log 出现对应 commit，`git show --stat` 只含本次触碰文件
2. 反向实测①：工作区预置无关脏文件 → 流转 commit 不带它
3. 反向实测②：模拟 git 失败 → 流转结果保留 + stderr 报警 + 待收口清单有记录
4. #363 门禁拦截场景：被拦的 complete 不产生 commit
5. 测试夹具清理干净

## 交付

1. 代码 + 正反向实测记录（diff 贴执行报告）
2. 与 #389 的串行/合并实施方案说明
3. 送欧阳锋终审
