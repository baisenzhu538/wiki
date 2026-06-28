---

id: "ocr-一堂五步法画布"
created_at: 2026-05-21
domain:
  - src_unknown
source_refs:
  - 10_raw/sources/src_20260522_2a547df5-ocr-一堂五步法画布.md
status: draft
title: "OCR: 一堂五步法画布"
type: concept
updated_at: 2026-05-22
pipeline:
  - src_unknown
author: "老顽童"
reviewed_by: pending
confidence: 0.6
trust_level: low
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
---

# OCR: 一堂五步法画布

## Summary

原图: `00_inbox/一堂五步法画布.

png` 一堂五步法画布YitangFive-stepCanvas 假设 需求 解决方案 商业模式 增衣 壁垒 我的业务 价值假设 增长假设 - 本文件由 PaddleOCR ONNX pipeline 自动提取 - 可能存在连字/误识，需要人工校对 - 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解

## Source Refs

- src_unknown

## Reusable Knowledge

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Open Questions

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## Critique

### 内部局限

- src_unknown
- src_unknown
- src_unknown

### 外部攻击

#### Clayton Christensen — “增长假设和壁垒假设是矛盾的”

Clayton Christensen 在《创新者的艳境》中证明：企业为了追求增长，往往会打破自己的壁垒（如进入低端市场）。五步法画布将"增长/壁垒"合并为最后一步，暗示两者可以同步考量。但 Christensen 会质疑：**增长和壁垒天然对立**。你的壁垒越高，你越难进入新市场获取增长；你越追求增长，你越需要打破现有壁垒。将两者合并处理，可能让创业者忽略这种根本性张力。

#### Rita McGrath — “临时优势时代，壁垒是幻观”

Rita McGrath 在《临时优势的竞争》中提出：在当今快速变化的环境中，**持续的竞争优势已经不复存在**，企业需要不断进入和退出市场，而非构建静态壁垒。画布最后一步的"壁垒"暗示企业需要构建"护城河"，但 McGrath 会警告：在技术变革加速的时代，任何壁垒都可能在短期内被打破。投入过多资源构建壁垒，可能让企业变得僵化。

### 不要用的场景

- src_unknown
- src_unknown

## Synthesis

### 与本库其他概念的关联

- src_unknown
- src_unknown

### 可迁移场景

- src_unknown
- src_unknown

## Output Opportunities

Content: <article: "一堂五步法画布实战手册" — 结构化教程，将OCR提取的框架与一堂方法论体系总图中的四张地图对齐，提供从假设验证到壁垒构建的完整工作流，含画布填写示例与常见逻辑陷阱（如"假设-需求"循环风险）的规避策略>
Code: <script: `yitang-canvas-ocr-reconstructor.py` — Python工具，输入PaddleOCR原始输出+一堂五步法画布模板结构，自动修复"增衣→增长"等典型误识，重建画布五栏视觉布局，输出Markdown格式结构化画布及置信度标注>
Capability: <playbook: "OCR-方法论画布联合校验工作流" — 整合PaddleOCR ONNX pipeline的已知bug教训（dict索引偏移、全角空格处理）与一堂类结构化画布的语义校验规则，建立"OCR提取→术语库匹配→人工复核→KDO入库"的四阶段标准作业程序>
