---
title: "原理图与BOM交叉验证报告"
type: "concept"
status: "draft"
source_refs: [src_20260606_04f43d43]
created_at: "2026-06-06T06:31:13+00:00"
updated_at: "2026-06-06T06:31:13+00:00"
---

# 原理图与BOM交叉验证报告

## Summary

**项目名称**：广冷电子 — 红外光栅板（HX-SMJ-03）   **分析日期**：2026-06-06   **分析文件**： | 模块 | 器件型号 | 关键参数 | |------|---------|---------| | DC-DC降压 | **JW5026** | 24V→5V/1A，VIN(max)=28V | | 反接保护 | **SS24** | 40V/2A，VF=550mV@2A | | TVS过压保护 | **P6SMB30CA** | Vrwm=25.

6V，Vbr(min)=28.

4V | | 移位寄存器 | **SN74LV595APWR** | 串转并，驱动发射管 | | 运放 | **LMV358IPWR** | 接收信号放大 | | 模拟开关 | **CD4051BPWR** | 8选1多路器 | | 红外发射管 | **IR333C-A** | 940nm | | 红外接收管 | **PT334-6B** | 940nm | | 发射管电流 | 50mA | 5%占空比 | **设计分析PDF中的DCDC计算**： - 公式：`VOUT = 0.

## Source Refs

- `src_20260606_04f43d43` -> `10_raw/sources/src_20260606_04f43d43-原理图与bom交叉验证报告.md`

## Reusable Knowledge

- 8V），启动浪涌可能超过30V - JW5026的28V最大输入对于24V系统几乎没有安全余量，极易因浪涌损坏 - TPS54360的60V耐压为24V系统提供了充足的安全裕度 - **结论**：V1.
- 7V）更安全 - 工业环境存在感性负载尖峰，SS36更可靠 - **结论**：V2.
- 2V，为24V系统提供了合理余量 - **结论**：原理图/选型报告/BOM使用P6SMB33CA是正确的，设计分析PDF中的P6SMB30CA可能是旧版或笔误 | 参数 | AP2302B (MOSFET) | S9014 (三极管) | |------|-----------------|---------------| | 类型 | N-MOSFET | NPN三极管 | | 驱动方式 | 电压驱动 | 电流驱动 | | 开关速度 | **快** | 较慢 | | 导通压降 | 很小（RDS(on)×I） | VCE(sat) ~0.

## Open Questions

- TODO: What open questions does this source raise?

## Output Opportunities

- Content:
- Code:
- Capability:
