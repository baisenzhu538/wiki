---
title: 示例·电源管理模块卡（虚拟示例）
type: module
created_at: "2026-08-26"
updated_at: "2026-08-26"
status: draft
source_refs: [src_example]
responsibility: 全机电源分配与低功耗管理（保证各 rail 上电时序与休眠漏电极限）
interface_contract:
  - 对上游（电池/充电）：输入 3.6-4.35V，反接保护承诺
  - 对下游（主控/射频）：3.3V rail 上电 10ms 内稳定，纹波 <30mV
  - 对固件：GPIO7 低电平=允许进休眠（契约，不是实现细节）
dependencies:
  - "[[spec-example]]（电源时序协商协议）"
owner: 硬件组·某工
hw_fw_versions:
  - PCB revC + FW 1.4.2 起生效（revB 无 GPIO7 契约）
artifact_path: eda/mainboard/revC/power-section/
---

# 电源管理模块（示例卡——虚拟内容，仅展示 schema 用法）

> 定位声明：本卡管「为什么这么设计+对外的承诺」；原理图/PCB 在 artifact_path 原仓。

## 设计意图

（为什么选这颗 PMU/为什么时序这样定——认知核心）

## 踩坑

（revB→revC 迁移期 GPIO7 契约不存在的兼容性坑）
