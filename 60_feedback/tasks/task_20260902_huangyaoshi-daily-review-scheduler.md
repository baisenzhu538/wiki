---
id: task_20260902_huangyaoshi-daily-review-scheduler
title: 四主力每日复盘计划任务化（老朱 09-02 直令：复盘按 Truman 规定格式定期做+内化迭代）——schtasks 每日拉起 headless 复盘
seq: 623
status: in_progress
assignee: huangyaoshi
created_by: wangyuyan
created_at: 2026-09-02
decision_source: 老朱 09-02 直令：「定期把复盘按照规定格式进行并内化迭代，安排下去作为任务让他们定期去做」
reviewer: 欧阳锋
instance: huangyaoshi
code_files:
  - kdo-tools/daily_review.py
  - kdo-tools/kdo-daily-review.cmd
  - kdo-tools/kdo-daily-review.xml
  - 90_control/infrastructure-inventory.md
updated_at: '2026-09-03T01:05:00+00:00'
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

## 执行报告（2026-09-03 黄药师）

**交付物**：`kdo-tools/daily_review.py`（调度主脚本）+ `kdo-tools/kdo-daily-review.cmd`（ASCII 包装）+ `kdo-tools/kdo-daily-review.xml`（S4U 计划任务定义）+ 基建总表登记 2 行（§3 工具族 + §5 计划任务）；commit 05bfee667。
**完成内容**：
1. schtasks `kdo-daily-review` 已注册（每日 23:37，S4U 无窗——XML 照 #607 vault-git-backup 模板，LogonType=S4U，MultipleInstancesPolicy=IgnoreNew；`schtasks /query` 实证下次运行 2026/9/3 23:37）
2. `daily_review.py`：三角色（laowantong/huangyaoshi/ouyangfeng；王语嫣不占——自有收尾纪律）顺序经 kimi-headless-launch.py 拉起；**空班豁免**（F-062）：git log 今日 commit + todos 今日行双判据，零活动跳过；**复盘指令模板内嵌**（不从零发挥）：todos 今日行/git log/任务单三路素材 → agents/agent-os.md §10.2 Truman 11 章 → daily-context-save.py save --truman（禁 --stdin）→ 错误模式库追加 → todos 收尾行；禁编造（无产出如实写「今日无施工」）
3. 同日多实例=同文件追加节（命名铁律）；日志 logs/daily-review.log 每次运行留痕
**验证**：①计划任务注册实证：schtasks query 返回下次运行 2026/9/3 23:37 ✓ ②**首跑手动触发（00:50:50）**：三实例全拉起 rc=0（laowantong todos 今日 1 条 / huangyaoshi commit 12 / ouyangfeng commit 2）③三份复盘落盘：桌面/agent复盘/{laowantong|huangyaoshi|ouyangfeng}/daily-context/2026-09-03.md 均已含「00:50 场」追加节（文件 14295B/15149B/10594B）④三实例自检全 **🟡 B 级**（daily-context-save 输出，无 🔴），todos 收尾行已落（[2026-09-03 00:53/00:55] 复盘完成）
**边界**：①首跑时三角色 09-03 复盘文件已由 00:30-00:49 其他收尾会话先行创建——本任务首跑按设计追加节而非新建，正是同日多实例合并口径 ②空班豁免首跑未触发（三角色今日均有活动）；豁免判据=git log 消息含角色名/中文名 + todos 日期行，代码无单测（git 依赖判定，验证走首跑实证）——若欧阳锋要求补测试再立项 ③今晚 23:37 排程路径将首次自动触发（自然验证点）；实例日志名按秒错开防串写 ④kimi-headless-launch 拉起为 DETACHED 进程，S4U 排程下先例实证可跑（门铃/复盘首跑均 S4U 同类）
**需要谁动作**：欧阳锋终审 #623；观察点=今晚 23:37 自动首拍落盘（logs/daily-review.log 留痕）
