---
id: "ocr-一堂-科学决策-深度-l3定量公式"
created_at: 2026-05-21
domain:
  - "yitang"
source_refs:
  - "src_20260522_80e1b943"
status: "enriched"
title: "OCR: 一堂-科学决策-深度-L3定量公式"
type: "concept"
updated_at: 2026-05-22
tags:
  - #scene/business-analysis
  - #scene/learning-methodology
pipeline:
  - #boundary/requires-human-judgment
  - confidence-source-cited
---

# OCR: 一堂-科学决策-深度-L3定量公式



## Summary

原图: `00_inbox/科学决策/一堂-科学决策-深度-L3定量公式.

png` 单元模型ROI深度：L3定量公式 A+B+C+D X C 定量 定钱 - 本文件由 PaddleOCR ONNX pipeline 自动提取 - 可能存在连字/误识，需要人工校对 - 视觉结构信息（标题/正文/表格分块）未在 OCR 中体现，需要结合原图理解



## Source Refs

- `src_20260522_80e1b943` -> `10_raw/sources/src_20260522_80e1b943-ocr-一堂-科学决策-深度-l3定量公式.md`



## Reusable Knowledge

- The "单元模型ROI深度" (Unit Model ROI Depth) framework includes a Level 3 (L3) quantitative formula for decision-making.
- The L3 quantitative formula is expressed as: A+B+C+D × C, combining multiple weighted factors with a multiplier effect.
- The framework distinguishes between "定量" (quantification/measurement) and "定钱" (monetization/setting monetary value) as two distinct stages of analysis.



## Open Questions

- What do variables A, B, C, and D specifically represent in the L3 quantitative formula, and are they standard metrics or context-dependent?
- Is the formula's structure (A+B+C+D × C) mathematically unambiguous, or does it require parentheses to clarify operator precedence (i.e., (A+B+C+D) × C versus A+B+C+(D×C))?
- What is the unit of measurement for each variable, and how are heterogeneous units reconciled in the summation?
- What evidence or validation exists that this specific formula structure produces reliable ROI predictions across different decision contexts?
- How does the "定量" (quantification) stage feed into or differ from the "定钱" (monetization) stage—are they sequential, iterative, or applied to different components of the formula?
- What threshold or benchmark values define "深度" (depth) in this framework, and how is the L3 level distinguished from L1 and L2?
- Given OCR extraction errors are noted, what critical ambiguities in the original visual layout (e.g., fraction bars, subscripts, table cells) might fundamentally alter the formula's interpretation?



## Critique

#### Meehl — “严格公式的统计预测优势”
Meehl 在《临床与统计预测》中证实，简单的统计模型在预测上几乎始终优于专家的主观判断。但这个结论有一个前提：模型的输入变量必须是可靠的。L3 的定量公式虽然看起来很科学，但如果输入变量的不确定性很高，公式的精确性只会放大这种不确定性。你确定你的各变量估计误差在公式中不会被放大到让结论失效的程度吗？

#### Tetlock — “专家预测的边界”
Tetlock 在《超级预测者》中证实，即使是最优秀的预测者，在面对高不确定性的复杂系统时也会失效。定量公式假设了一个“可以被预测的世界”，但在创业和战略决策中，很多关键变量本质上是不可预测的。你的公式是否考虑了“未知的未知”？



## Synthesis

### 与本库其他概念的关联

- [[yt-decision-depth-ladder]] — 深度梯子，L3 是其第三级走进阶
- [[yt-decision-canvas]] — 同域决策画布，定量公式是其某些维度的精确化
- [[master-decision-hygiene]] — 通用决策卫生，提醒公式的脆弱性放大作用

### 可迁移场景

- 已有充足数据的业务决策：用定量公式做出精确的财务预测
- 投资决策的快速计算：在数据充足时用公式比直觉判断更可靠



### 不要用的场景

- 不要在输入变量不确定性极高时使用定量公式，公式会放大这种不确定性
- 不要将公式当作“终极答案”，它只是在特定假设下的近似
- 不要在缺乏对变量关系线性假设的检验时使用，非线性系统中公式可能完全失效



## Action Triggers

- 当你已有充足数据需要做出精确财务预测时，用定量公式替代直觉判断
- 従你在使用公式时对输入数据的准确性感到不安时，用 Meehl 的“统计预测”视角检查模型的输入可靠性
- 従你的公式结果与实际业务感知出现尖锐矛盾时，用 Tetlock 的“专家预测边界”视角质问是否忽略了不可预测的变量



## Output Opportunities

Content: tutorial
Code: tool
Capability: playbook
