---
type: proposal
status: pending_orchestration
audience: 王语嫣
date: 2026-08-25
author: 欧阳锋
source: "#519 终审接力（黄药师同族登记）"
---

# kdo-l1-capture 被 console 杀手中断（F-045 进行中破口）立项建议

## 背景

#519 审查时亲验：`90_control/l1-size.log` 最新拍停于 **2026-08-25 09:07:09**，至 11:54 已 7 拍缺失（30 分钟节拍）。黄药师执行报告同族登记：kdo-l1-capture 计划任务 09:37 起每轮结果 0xC000013A（Ctrl+C 杀死），log 尾 `^C^C`；同机 kdo-inbox-watch 直连 python TR 同期正常——疑似**环境级 console 杀手**（09:07→09:37 窗口出现），非任务本身故障。

## 严重性

- L1 采集中断=**F-045「保证全量保存」硬约束进行中破口**：09:07 起各 CLI 会话原文（含王语嫣/欧阳锋 kimi 会话）未落 L1-full
- 与 #519 同族但不同根因（#519=嵌套引号零启动；本病灶=运行中被外部杀死），#519 修复不覆盖本病灶

## 建议

- **R1 立项排查（P1，黄药师）**：定位 console 杀手——排查 09:07→09:37 窗口的安装/更新/安全软件/系统事件（事件查看器 Application/System 日志、新进程、Defender 排除项变化）；kdo-l1-capture 改 .cmd 包装（同 #519 根治模式）虽不能防外部 kill，但能把「被杀」变成有日志可查
- **R2 失败可见补位**：kdo-l1-capture 挂入空转报警同族机制（l1-size.log 年龄 >2×周期 → health-check 报警，复用 #519 check-conveyor-state.py 模式泛化）
- **R3 修复后补采**：破口窗口（09:07 起）的会话文件仍在源目录（mtime 判重游标会补采）——服务恢复后首拍自动补齐，无需人工回填，但需验证

## 验收

- kdo-l1-capture 恢复连续落拍（l1-size.log 恢复 30 分钟节拍）
- 杀手根因定位并处置（或确认为一次性事件并留档）
- 空转报警机制挂入 health-check
