---
title: 示例·XX 通讯协议规格卡（虚拟示例）
type: spec
created_at: "2026-08-26"
updated_at: "2026-08-26"
status: draft
source_refs: [src_example]
spec_version: v1.3
compatibility:
  - 向下兼容 v1.1+（v1.0 的 CRC 字段废弃）
  - 与 YY 固件 1.4.x 互操作实测通过（2026-07 联调）
change_history:
  - v1.3（2026-06）：增加心跳超时字段——根因=弱网环境断链假死
  - v1.2（2026-03）：帧头长度 2→4 字节——根因=扩展命令空间不足
implementations:
  - 端侧 Android 实现到 v1.3（comms-lib 2.0+）
  - 固件侧实现到 v1.2（v1.3 心跳字段忽略不报错）
artifact_path: vendor/xx-protocol/spec-v1.3.pdf
---

# XX 通讯协议（示例卡——虚拟内容，仅展示 schema 用法）

> 定位声明：本卡管「协议的认知」（为什么这么设计/变更史/谁实现了什么），协议原文 PDF 在 artifact_path。

## 设计意图

（为什么这样分帧/为什么这么握手——写认知，不抄协议文本）

## 踩坑

（联调实测的坑：如 v1.2→v1.3 迁移期固件不识别心跳字段的兼容表现）
