---
id: "dk-f14-accuracy-measurement-mismatch"
title: "F-KDO-014：准确率声明的测量口径不一致"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "failure-modes.md F-KDO-014"
source_refs:
  - "90_control/failure-modes.md#F-KDO-014"
tags:
  - "#boundary/requires-human-judgment"
  - "confidence-draft"
  - "confidence-source-cited"
  - "#domain/knowledge-management"
  - "#method/evaluation-method"
  - "#scene/ai-collaboration"
  - "#scene/learning-methodology/feedback-loop"
  - "#scene/skill-engineering/eval-testing"
  - "#source_type/error"
created_at: 2026-05-31
updated_at: 2026-05-31
related:
  - "dk-p15-claimed-done-not-verified"
  - "master-systems-thinking"
contradicts:
  - "master-decision-hygiene"
  - "master-ai-info-literacy"
  - "master-systems-thinking"
---

# F-KDO-014：准确率声明的测量口径不一致

## 原始表述

> **触发条件**：声称某个工具、流程或 AI Agent 的"准确率"时，没有明确测量方法。
>
> **表现**：报告中写"准确率 95%"、"错误率 <5%"、"缺失率仅有 2%"——数字看起来很好，但没有人知道这个数字是怎么算出来的。不同人、不同时间、不同场景下的"准确率"完全不可比。
>
> **根因**：
> - 没有明确的测量方法定义（数据集是什么？覆盖哪些维度？计算公式是什么？）
> - 没有 Gold Standard 基线做比对，数字出自"感觉"或小规模抽样
> - 不同版本、不同配置下的测量结果直接比较，没有控制变量
>
> **防御措施**：
> - **每个准确率声明必须附带测量方法**：明确数据集、覆盖维度、计算方式
> - **用 Gold Standard 做比对**：不是"我觉得"，而是"我跟标准答案比对过"
> - **跑 `_verify_gold_standard.py`**：不要凭感觉报数字，用可重复的脚本测量
> - **控制变量**：比较两个版本的准确率时，确保数据集、配置、测量脚本完全一致
>
> **状态**：Gold Standard 基线已建立，但模式未归档入库。

## 使用场景

- 你需要声称某个工具或流程的准确率（如"kdo validate 准确率"、"OCR 识别准确率"）
- 你在审查他人提交的"准确率"数字时，需要判断是否可信
- 你在比较两个不同版本/方案的性能时，需要确保测量口径一致
- 你在设计评估指标时，需要定义"什么叫准确"

## 操作方法

1. **定义测量方法**：声称准确率前，先回答三个问题：数据集是什么？覆盖了哪些维度？计算公式是什么？
2. **建立 Gold Standard**：准备一组经过人工校准的标准答案，作为比对基准
3. **用可重复脚本测量**：写一个自动化脚本（如 `_verify_gold_standard.py`），而非凭感觉报数字
4. **附带测量详情**：每次报准确率时，同时附带：数据集规模、覆盖维度、测量时间、脚本版本
5. **控制变量比较**：比较两个版本时，确保只有一个变量不同，其余全部一致

## 适用边界

- 适用于所有涉及"准确率"、"错误率"、"完成率"等定量指标声明的场景
- 不适用于纯主观评估（如"用户满意度"）——这些本身就没有绝对标准，需要定义自己的评估框架
- 如果数据集很小（<100 样本），"准确率"数字本身就不稳定——需要报出置信区间
- Gold Standard 的建立是成本高的：对于快速迭代的实验性项目，可以先用简化版本，但必须明确说明
- **"准确率 95%"如果没有测量方法，就等于没有说**——这是底线

## 为什么值钱

- 这是系统评估中的核心问题：**没有测量方法的数字是毫无意义的**
- "准确率 95%"极具迷惑性——它看起来很专业，但可能是在一个极小的、经过筛选的数据集上测的
- 揭示了科学评估中的一个核心原理：**测量结果的价值不在于数字本身，而在于测量过程是否可重复、可验证**
- 任何 AI 训练语料中都不会有"KDO 项目中准确率声明必须附带 Gold Standard 比对"这条知识

## 与其他知识的关联

- dk-p15-claimed-done-not-verified — 同一模式："声称了一个没有验证方法的数字"。P-15 是"完工报告中的数字不可信"，F-14 是"准确率声明中的数字不可比"——两者都是"数字需要验证方法才有意义"
- master-systems-thinking — 系统思维中的"反馈循环"：如果测量方法不一致，反馈循环就会失效——你以为在改进，实际上在比较两个不同的东西
- `90_control/failure-modes.md` → F-KDO-014（原始记录）

## 老顽童疑问（2026-05-31）

无疑问，请欧阳锋审查。
