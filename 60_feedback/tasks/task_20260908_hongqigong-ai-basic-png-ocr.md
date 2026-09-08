---
id: task_20260908_hongqigong-ai-basic-png-ocr
title: "补采：AI基本功域 27 张无产物 PNG OCR 补采评估（优先 040618 四种工作状态图，#682 编排）"
seq: 687
status: queued
assignee: hongqigong
created_by: wangyuyan
created_at: 2026-09-08
decision_source: 老朱 09-08 19:25 拍板全做（#682 编排）
reviewer: 欧阳锋
instance: hongqigong
updated_at: ''
---

# #687 洪七公补采工单：AI基本功域 27 张无产物 PNG OCR 补采评估

> 规格源=诊断报告 `60_feedback/diagnosis/diag_20260908_wangyuyan-ai-data-ai-basic-deep-dig.md` §3.2-E 覆盖清点【实证】。

## 背景（存在性核查锚）

`00_inbox/AI基本功/` E 组 34 张 PNG 中：9 张已有逐件文本产物（040104/040231/040423/040213/022915/040155/022955/批注035424/批注035952）；**27 张无任何文本产物覆盖**——含 040618 四种工作状态图、040032/040241/040312/040348 等课程图、08-07 批注 4 张、08-08 批注 7 张、微信图片 1 张、224017/224024 等。`_vlm_output/` 5 件时间戳与本目录 PNG 不精确吻合，不能断定覆盖；VLM识别成果_20260808.md 声称「34图全覆盖」实为聚合摘要（口径矛盾，欧阳锋建议书已指出）。

## 工作项

1. **补采评估**：逐张核对 27 张无产物 PNG，产出「PNG × 是否已有产物 × 建议（OCR补采/确认已覆盖/登记不采）」评估表
2. **优先补采**：`一堂DOC-20260808040618.png`（四种工作状态图）为首件 OCR 补采
3. **OCR 纪律**：图片必须先 OCR 成结构化文本再处理（AGENTS.md 图片输入纪律）；默认 EasyOCR skill（`40_outputs/capabilities/skills/image-ocr-easyocr/`），fallback PaddleOCR.js；产物落 `00_inbox/AI基本功/` 同目录（OCR_ 前缀）
4. 补采产物为素材层——是否产卡由王语嫣另行诊断裁定，本单不产卡

## 验收标准

1. 27 张逐张落判评估表（含存在性核查：每张核对产物是否真无）
2. 040618 完成 OCR 补采，产物文件落盘
3. 补采过程中发现源文件与编译物归属错位/不一致 → 记 `60_feedback/corrections/`（只标记不自行改卡）
4. 欧阳锋终审

## 边界

- 只补采评估+OCR，不产 30_wiki 卡，不改卡片主体
- 与 #683/#684/#685 产卡线无依赖冲突，可按自身节奏执行
