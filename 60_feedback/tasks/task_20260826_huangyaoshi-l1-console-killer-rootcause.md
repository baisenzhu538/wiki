---
id: 547
assignee: huangyaoshi
status: queued
updated_at: '2026-08-26T23:30:00+00:00'
version: v0.2
instance: huangyaoshi
code_files:
  - kdo-tools/l1_capture.py
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
