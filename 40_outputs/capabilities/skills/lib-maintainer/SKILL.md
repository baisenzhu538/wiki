---
name: lib-maintainer
version: "1.0.0"
allowed-tools:
  - Bash
  - Read
  - Write
description: |
  通用文档库自动索引引擎。口述需求→自动Schema设计→解析入库→结构化索引。
  支持 PDF/Excel/Word/PPT/图片/音频。Agent自动完成，人只需说"把这个文件夹做成库"。
  触发词：建库、做成库、索引这个文件夹、文档入库、资产库、整理文档、
  做个知识库、文档太多找不到、帮我建个库、把文件整理一下。
status: draft
owner: huangyaoshi
---

# LibMaintainer 通用文档库引擎

你口述需求 → Agent 自动完成建库。支持全类型文档，产出结构化索引。

## 使用方法

直接说：
- "把 `~/documents/产品手册` 做成产品库，按品类和型号检索"
- "把 `~/notes/` 做成知识库，能按标签和日期查"
- "把这个文件夹里的合同做成客户资料库"

Agent 会自动：设计字段 → 解析文档 → 提取内容 → 建索引 → 出报告。

## 库目录

所有库统一存在 `~/exflower/vault/{库名}/` 下，与 Obsidian wiki 物理隔离。
