---
title: "广冷电子 — HX-SMJ 红外光栅故障分析报告"
type: "concept"
status: "draft"
source_refs: [src_20260606_c49e4e04]
created_at: "2026-06-06T06:31:08+00:00"
updated_at: "2026-06-06T06:31:08+00:00"
---

# 广冷电子 — HX-SMJ 红外光栅故障分析报告

## Summary

> 分析日期：2026-06-04 > 分析人：欧阳锋（Architect） > 背景：离职工程师留下的红外对射板资料混乱，2025-11 批次存在"斜着对射"故障 这是一个**自动售货机红外光栅检测系统**，共 6 种电路板： | 板号 | 名称 | 说明 | |:----|:-----|:------| | HX-SMJ-01B | **主控板** | STM32F103ZE MCU，CAN 总线主节点 | | HX-SMJ-03B-A | **红外板-A（主控红外板）** | V2.

2 自带 STM32F103RCT7 | | HX-SMJ-03B-B | **红外板-B（外设红外板）** | 无 MCU，通过 20pin 排线连 A 板 | | HX-SMJ-01 | 继电器板 | — | | HX-SMJ-04B | 货道电机板 | — | | HX-SMJ-02 | 4G/WiFi 通信板 | — | ``` 发送通道（16路）：   STM32 → QD1/QD2 → SN74LV595 (×2) → AP2302B MOSFET (×16) → IR333C-A 红外发射管 接收通道（16路）：   PT334-6B 接收管 → LMV358IDR 运放 → CD4051BPWR 多路器 (×2) → STM32 ``` - 早期设计、手焊、出过货给客户 ✅ - 资料记录不完整，知道研发过程有问题 - 他手中的版本是 **V2.

0 架构** - 在黄工留下的资料基础上整理出 **V2.

## Source Refs

- `src_20260606_c49e4e04` -> `10_raw/sources/src_20260606_c49e4e04-广冷电子-hx-smj-红外光栅故障分析报告.md`

## Reusable Knowledge

- > 分析日期：2026-06-04 > 分析人：欧阳锋（Architect） > 背景：离职工程师留下的红外对射板资料混乱，2025-11 批次存在"斜着对射"故障 这是一个**自动售货机红外光栅检测系统**，共 6 种电路板： | 板号 | 名称 | 说明 | |:----|:-----|:------| | HX-SMJ-01B | **主控板** | STM32F103ZE MCU，CAN 总线主节点 | | HX-SMJ-03B-A | **红外板-A（主控红外板）** | V2.

## Open Questions

- TODO: What open questions does this source raise?

## Output Opportunities

- Content:
- Code:
- Capability:
