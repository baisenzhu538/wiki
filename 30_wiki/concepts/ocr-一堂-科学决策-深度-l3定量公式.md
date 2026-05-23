---
title: "OCR: 一堂-科学决策-深度-L3定量公式"
type: "concept"
status: "enriched"
source_refs: ["src_20260522_80e1b943"]
created_at: "2026-05-21T20:13:55+00:00"
updated_at: "2026-05-22T07:13:24+00:00"
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

## Output Opportunities

Content: tutorial
Code: tool
Capability: playbook

## Critique

#### Kahneman — “公式的伪安全感”
Kahneman 在《思考，快与慢》中证实，人类系统 1 天生偏好将复杂决策压缩为简单公式——即使这个公式的输入是极度不确定的。L3 的“定量公式”恰恰善长了这种偏好：当你看到 A+B+C+D×C 这样的公式时，你会产生一种"这个决策已经被精确计算了”的错觉。但每个变量的不确定性都会在公式中被放大，而且公式本身可能是基于一个不适用的模型。你是否注意到，你在看到公式的瞬间就对结果产生了信任？

#### Taleb — “公式的脆弱性放大器”
Taleb 论证，在复杂系统中，任何公式都是脆弱性的放大器——因为公式假设了变量之间的线性关系，而真实世界往往是非线性的。L3 的 A+B+C+D×C 中，任何一个变量的小幅偏差都可能导致整个结果的大幅偏离，而你可能对这个偏差毫无察觉。更可怕的是，公式给了你一个“精确答案”，让你停止了对其他可能性的探索。你上一次使用公式做出的决策，在事后回看时，公式中哪个变量的估计误差最大？

## Synthesis

### 与本库其他概念的关联

- [[yt-decision-depth-ladder]] — 深度梯子，L3 是其第三级走进阶
- [[yt-decision-canvas]] — 同域决策画布，定量公式是其某些维度的精确化
- [[master-decision-hygiene]] — 通用决策卫生，提醒公式的脆弱性放大作用

### 可迁移场景

- 已有充足数据的业务决策：用定量公式做出精确的财务预测
- 投资决策的快速计算：在数据充足时用公式比直觉判断更可靠

## dont-use

- 不要在输入变量不确定性极高时使用定量公式，公式会放大这种不确定性
- 不要将公式当作“终极答案”，它只是在特定假设下的近似
- 不要在缺乏对变量关系线性假设的检验时使用，非线性系统中公式可能完全失效

## Action Triggers

- 当你已有充足数据需要做出精确财务预测时，用定量公式替代直觉判断
- 当你在使用公式时感到"结果太精确了”的不安时，用 Kahneman 视角检查每个输入变量的不确定性
- 当你的公式结果与实际业务感知出现尖锐矛盾时，用 Taleb 视角检查是否忽略了非线性效应或尾部风险