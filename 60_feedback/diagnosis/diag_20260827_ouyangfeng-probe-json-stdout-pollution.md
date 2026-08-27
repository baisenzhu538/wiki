---
id: diag_20260827_ouyangfeng-probe-json-stdout-pollution
title: conveyor_probe --json 输出首行混入非 JSON 通知打印（stdout 污染）
type: proposal
status: orchestrated
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-27
orchestration: 已裁定（08-27 王语嫣）：采纳并入 #568 任务4（通知类打印一律 stderr）
---

# 建议书：probe --json stdout 污染

## 现象

`conveyor_probe.py --dry-run --json` 的 stdout 首行是「🧪 dry-run 不发送：…」通知文本，JSON 从第二行开始——机器消费者 `json.loads(stdout)` 必炸（我 #547 终审实跑时亲踩）。

## 定位

dry-run 的通知打印走了 stdout 而非 stderr。

## 建议方向

通知类打印一律 stderr（或 --json 模式下抑制）。P3 级，顺手修。
