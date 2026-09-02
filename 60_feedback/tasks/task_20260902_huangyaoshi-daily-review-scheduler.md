---
id: task_20260902_huangyaoshi-daily-review-scheduler
title: 四主力每日复盘计划任务化（老朱 09-02 直令：复盘按 Truman 规定格式定期做+内化迭代）——schtasks 每日拉起 headless 复盘
seq: 623
status: queued
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 直令：「定期把复盘按照规定格式进行并内化迭代，安排下去作为任务让他们定期去做」
reviewer: 欧阳锋
---

# #623 每日复盘计划任务化（黄药师）

## 背景

老朱 09-02 直令：复盘（Truman 格式+内化迭代）从「会话收尾靠自觉」升级为「定期任务」。现状：复盘靠各角色会话收尾或老朱触发，无定时机制；headless 实例无会话记忆（每次全新会话），复盘输入必须全部来自仓库文件。

## 任务

1. **注册系统级计划任务** `kdo-daily-review`：每日 23:37（与 02:30 backup 错开），S4U 无窗（infrastructure-inventory 硬纪律），依次用 `90_control/scripts/kimi-headless-launch.py <role> "<复盘指令>"` 拉起三角色（laowantong/huangyaoshi/ouyangfeng；王语嫣自有收尾纪律不占此任务）
2. **复盘指令模板**（写进任务脚本，不从零发挥）：读本角色 todos 今日行 + `git log --since=today --author 或 grep 实例名` + 当日任务单 → 按 agents/agent-os.md §10.2 Truman 章写复盘 → `python kdo-tools/daily-context-save.py save --agent <role> --truman --file <路径>`（禁 --stdin，F-030）→ 新错误入该角色错误模式库
3. **空班豁免**：当日该角色零 commit 零 todos 新增 → 跳过不拉起（F-062 成本纪律）
4. **首跑验证**：注册后 `--` 手动触发一次，确认三角色的复盘文件落盘且自检等级 🟢/🟡（🔴 打回）

## 红线

- 复盘内容不许编造——无产出就如实写「今日无施工」（诚实空班记录也是资产）
- 计划任务一律 S4U 无窗；任务登记进 infrastructure-inventory

## 交付

- 计划任务注册实证（schtasks query 输出）+ 首跑三份复盘落盘证据 + 执行报告
- claim/complete 走 `python 90_control/scripts/queue_transition.py`（complete 623）
