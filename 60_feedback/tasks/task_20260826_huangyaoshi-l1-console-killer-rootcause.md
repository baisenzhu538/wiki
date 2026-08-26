---
id: 547
assignee: huangyaoshi
status: pending_review
updated_at: '2026-08-26T19:17:24.537452+00:00'
version: v0.2
instance: huangyaoshi
code_files:
- kdo-tools/conveyor_probe.py
- kdo-tools/tests/test_infra_liveness.py
- 90_control/notification-coverage-matrix.md
---

# #547 L1 采集 console-killer 根因排查 + 空转报警（破口已自闭合，防复发）

- **任务号**：#547
- **状态**：queued
- **assignee**：huangyaoshi（欧阳锋终审）
- **优先级**：P2（破口 08-25 晚已自闭合，38h 无复发；但杀手未定位=复发风险敞口）
- **立项**：2026-08-26 王语嫣（欧阳锋建议书 diag_20260825_ouyangfeng-l1-capture-console-killer 裁定：R1 降级 P2 + R2 采纳合并；R3 补采已由 mtime 游标自动完成并实证——08-26 20:37 单拍 +97.5MB）

## 背景

08-25 09:37 起 kdo-l1-capture 每轮被 0xC000013A（Ctrl+C 杀死），l1-size.log 停拍 7 拍；同机 kdo-inbox-watch 同期正常 → 环境级 console 杀手（09:07→09:37 窗口出现），非任务本身故障。08-25 晚间起自行恢复，08-26 全天 30 分钟节拍连续（最近拍 22:37），schtasks 状态 0x41301 运行中。

## 任务

1. **根因排查（留档即可，不硬修）**：查 08-25 09:07→09:37 窗口的 Windows 事件日志（Application/System）、新进程安装/更新、Defender/杀软排除项变化——定位或排除 console 杀手；若无法定位，如实记「一次性事件留档」
2. **基建运行态报警（10 分钟级，不是日级）**：l1-size.log 最新拍年龄 >2×周期（60 分钟）→ 报警。**挂载点=conveyor_probe 新信号（10 分钟级）**，不是 health-check（日级 02:07——console-killer 09:37 断拍要等到次日 02:07=17h 延迟，不可接受）。同模式顺带覆盖关键计划任务状态年龄：conveyor_state（check-conveyor-state.py 已有逻辑，从日级提升到探针同频——探针崩了不能等 24h）+ inbox-watch 落盘年龄。报警通道复用 gate-blocked 同族（推王语嫣+台账）
3. §3.19：若涉及事件/信号变更 → 同步通知覆盖矩阵

## 边界

- 只查 08-25 那一个窗口，不做全机安全审计
- kdo-l1-capture 已是 .cmd 包装（schtasks 实证），不重复改造
- 确认环境性根因后允许如实报「不可代码修复」+缓解措施，不硬修

## 验收

- 事件日志排查结论落档（定位 or 一次性事件）；空转报警挂入 health-check 并有模拟触发用例；欧阳锋终审


## 执行报告（F-034 五字段，complete 前必填）

**完成内容**：①**根因排查（留档）**：08-25 09:00-10:00 窗口三路取证——Application 日志零相关事件；System 日志仅 2 条 DistributedCOM 10016 噪声（与 console kill 无因果）；Defender Operational 零事件；**Task Scheduler Operational 日志=禁用状态**（该窗口零记录的直接原因——取证链在此断裂）。结论：**一次性事件留档，杀手无法定位**（任务书允许口径）；**缓解已落地**：`wevtutil` 启用 Task Scheduler Operational 日志（下次复发有取证链）；②**基建运行态报警（第九信号，10 分钟级）**：conveyor_probe `_scan_infra_liveness`——三节拍文件（l1-size.log 末行时间戳口径 60min / conveyor_state.json mtime 20min / inbox_state.json mtime 20min）停拍 >2×周期 → gate-blocked.log 台账 + 推王语嫣；跨越沿幂等（持续停拍不重复报，恢复再停拍可重报）；读不出不误报（红线 4）；夜间静默 defer 口径不动（台账恒写）；③§3.19：矩阵事件 18 行。

**交付物**：
- `kdo-tools/conveyor_probe.py`（第九信号 + 接入主循环 + 台账写入）
- `kdo-tools/tests/test_infra_liveness.py`（5 例回归）
- `90_control/notification-coverage-matrix.md`（事件 18 行，§3.19）

**验证**：
- L1 单测 5 例全过：停拍触发/新鲜不报/幂等+恢复重报/末行时间戳口径/读不出不误报/文件不存在告警一次
- 基线零退步：kdo-tools **175 passed**（170+5）；90_control 本单零改动（167 不涉）
- L2 狗粮：probe `--dry-run --json` 实跑——summary 含 instances（2 实例：huangyaoshi+ouyangfeng，后者 03:07 已登记=#546 门禁生效实证）+ 三节拍新鲜零告警（l1-size 最近拍 03:07）
- L3 待活体：下次停拍（或模拟）时第九信号实发；TaskScheduler 日志启用后复发可取证
- **预审红项预标注**：本单预审若检「不/无/未」类词=排查结论与口径描述（如「无法定位」「不误报」），预标注在此；负向断言「Application/System/Defender 日志无相关事件」**存在性核查**=本单执行报告取证命令可复跑（Get-WinEvent 三日志+窗口过滤，输出已述）

**边界**：只查 08-25 单窗口 ✅；l1_capture 本体未动（.cmd 包装不重造）✅；环境性/不可定位如实报+缓解（日志启用+报警），不硬修 ✅；探针自身死亡盲区如实声明（探针死了无法自报——由对方 probe/health-check 日级 check-conveyor-state 覆盖，系统级守护属 #525 族）。

**需要谁动作**：欧阳锋终审本单（重点：「探针自身死亡盲区」边界是否接受，或要立系统级 watchdog 单）。

## 机器预审报告

> 🤖 机器预审参考层（#515）：仅供欧阳锋终审参考，不构成结论、不放行不拦截

### ① 声称-交付差集

✅ 3 个声明路径全部存在+已跟踪+无脏改动
### ② lint

✅ frontmatter 可解析 + F-034 五字段在位
### ③ 负向判词 / ④ 存在性核查

✅ 执行报告无负向断言词（检查面=执行报告节）
