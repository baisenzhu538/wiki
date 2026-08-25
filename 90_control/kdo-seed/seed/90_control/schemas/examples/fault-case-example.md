---
title: 示例·固件升级偶发变砖排查案（虚拟示例）
type: fault-case
created_at: "2026-08-26"
updated_at: "2026-08-26"
status: draft
source_refs: [src_example]
symptom: OTA 升级约 2% 设备变砖（指示灯不亮，串口无输出），集中在电池电量 <20% 批次
location: 先排升级包完整性（换包复现率不变）→ 排串口日志（变砖机无 bootloader 输出）→ 示波器抓升级过程 3.3V rail，发现写入中段电压跌落到 2.9V
root_cause: flash 大页擦写峰值电流 + 低电量电池内阻升高 → rail 跌落触发 BOR 复位，恰好打断 flash 写 → bootloader 区半写
fix: 升级前置电量检查（<30% 拒绝升级）+ bootloader 区双bank 冗余写；验证=低电量压力测试 200 台次零变砖
prevention:
  - 产测加低电量 OTA 用例
  - 电源域设计评审清单加「峰值电流×最低电量」交叉项
severity: critical
artifact_path: logs/ota-brick-2026-05/（示波器截图+串口日志）
---

# 固件升级偶发变砖排查案（示例卡——虚拟内容，仅展示 schema 用法）

> 五段链条（现象→定位→根因→修复→预防）是资产形态；排查路径本身是暗知识，不许只写根因。
