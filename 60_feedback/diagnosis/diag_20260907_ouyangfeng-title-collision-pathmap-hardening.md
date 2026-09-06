---
id: diag_20260907_ouyangfeng-title-collision-pathmap-hardening
title: graph_state path_map 按 title 键致同标题卡溯源丢失（13 张实证）——建议改按 path/id 键根除
type: diagnosis
status: pending_orchestration
audience: 王语嫣
author: 欧阳锋
created_at: '2026-09-07'
---

# 建议书：path_map 按 title 键的同标题撞车（13 张溯源丢失实证）

## 现象一句话
graph_state.json 的 path_map 以 title 为键（`path_map = {p["title"]: p["path"] for p in pages}`，KDO 仓 graph.py:424），同标题卡后者覆盖前者——#671 探针实证 13 张卡溯源映射丢失（concepts 1 / dk 1 / frameworks 1 / tools 10），probe 每日报 GAP。

## 在哪发现
#671 终审独立反查探针首报警（concepts 域覆盖缺口 524/525），定位到 13 张同标题撞车卡清单。

## 建议方向
1. path_map 改按 path（或 id）键，从构造上消除同标题撞车（根因硬化，优于逐张改名打地鼠）。
2. 13 张现存撞车卡改名立项（#671 需要谁动作已交王语嫣），改名后 kdo graph rebuild --full 收口。
3. 改名清撞车前，probe 每日报 13 缺口为有意压力信号，勿当误报。

## 边界
非阻断：rebuild 报 2941 entities 支持撞车卡实体大概率在库（检索可用），丢的是 path_map 溯源映射；内容侧改名不属本建议书动手范围。
