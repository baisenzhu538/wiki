---
id: dk-f14-accuracy-measurement-mismatch
title: F-KDO-014：准确率声明的测量口径不一致
type: dk
dark_knowledge_type: failure
status: reviewed
domain:
- master
source_person: system
source_context: failure-modes.md F-KDO-014
aliases:
  - FKDO014：准确率声明的测量口径不一致
  - system
  - 准确率声明的测量口径不一致
  - 率声明的测量口径不一致
source_refs:
- src_unknown
created_at: 2026-05-31
updated_at: '2026-06-18'
related:
- '[[kdo-input-channel-strategy-2026-06-16]]'
- '[[kdo-protocol]]'
- '[[modeling-to-kdo-toolchain]]'
- '[[kdo-batch-produce-req014]]'
- '[[kdo-15-dimension-label-spec]]'
- '[[obsidian-kdo-内容产出工作流-产品设计大纲]]'
- '[[tool-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]'
- '[[kdo-watch-health-check-layer]]'
- '[[framework-kdo-self-attack]]'
- '[[kdo-yaml-frontmatter-safety]]'
- '[[kdo-priority-checklist]]'
- '[[kdo_product_design_agent_final]]'
- '[[proposal-kdo-flywheel-infrastructure]]'
- '[[yc-放出一套ai-native-公司组织方法论直接把公司当操作系统来设计中层管理变成了-markdown]]'
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
- src_unknown
- src_unknown# F-KDO-014：准确率声明的测量口径不一致
tags:
- audience:executor
- scene:reference
- skill-level:intermediate
---

## 原始表述/核心洞察

> **原始表述**：在 KDO 项目 failure-modes 中记录为 F-KDO-014——声称某个工具、流程或 AI Agent 的"准确率"时，没有明确测量方法。
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

**核心洞察**："准确率 95%"如果没有附带测量方法、数据集、Gold Standard 和计算口径，就等于没有说。测量结果的价值不在于数字本身，而在于测量过程是否可重复、可验证、可比较。

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **定义测量方法**：声称准确率前，先回答三个问题：数据集是什么？覆盖了哪些维度？计算公式是什么？
2. **建立 Gold Standard**：准备一组经过人工校准的标准答案，作为比对基准
3. **用可重复脚本测量**：写一个自动化脚本（如 `_verify_gold_standard.py`），而非凭感觉报数字
4. **附带测量详情**：每次报准确率时，同时附带：数据集规模、覆盖维度、测量时间、脚本版本
5. **控制变量比较**：比较两个版本时，确保只有一个变量不同，其余全部一致

## 适用边界

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

| 失败模式 | 典型症状 | 为什么危险 |
|
|---|---|
| 无测量方法的准确率声明 | "准确率 95%"但给不出数据集、公式、Gold Standard | 数字无法复现，决策建立在幻觉上 |
| 跨版本/跨场景直接比较 | 不同数据集、配置、脚本得出的准确率放在一起比 | 看似在比较性能，实则在比较测量条件 |
| Gold Standard 缺失 | 准确率来自"感觉"或小规模抽样 | 缺少可比对、可审计的客观基准 |
| 小样本点估计 | 在 <100 样本上报告单一准确率 | 数字不稳定，容易被异常值扭曲 |
| 把主观正确感当客观准确率 | "我觉得差不多 95%" | 混淆直觉与测量，无法审计 |

## 为什么值钱

- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 与其他知识的关联

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
