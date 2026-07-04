---
id: tool-Truman-Feature特性层训练法
title: Feature 特性层训练法：把 AI 基本功拆成可测试的最小单位
type: tool
status: draft
author: 老顽童
reviewed_by: pending
confidence: 0.88
trust_level: high
language: zh-CN
created_at: 2026-07-04
updated_at: 2026-07-04
domain:
- ai-collaboration
- yitang
source_refs:
- 00_inbox/人机协作双三角/一堂双三角-人机协作模型-口述.txt
- 00_inbox/AI-study/一堂-AI学习-AI工具应用AMA口述.txt
- 10_raw/sources/src_20260609_03491271-ocr-一堂-ai学习-truman自用的ai-featureset.md
related:
- "[[concept-yihang-ai-feature-thinking]]"
- "[[concept-yihang-dual-triangle-core]]"
- "[[tool-Truman-AI能力分层学习路径]]"
- "[[method-yitang-y-model-engine-cycle]]"
---

# Feature 特性层训练法：把 AI 基本功拆成可测试的最小单位

> **一句话定义**：Feature 特性层训练法来自 Truman 的 AI 工具应用 AMA——把 AI 基本功从"会用工具"下沉到"掌握 Feature（最小可操作技术特性）"，用 A/B 测试、Feature 对比、Y模型 循环来持续打磨，让能力不随工具迭代而贬值。

---

## 一、原始表述

> "第三个我们说的基本功，说的是 AI 基本功啊，就是 AI 上的那些工具，那些特性。"（双三角口述稿，行 1210）

> "不要老盯着工具，你去盯着每一个工具那些特有的最小的技术特性。"（双三角口述稿，行 1408）

> "每一个特性都有可能让你实现 A/B 测试的结果提升。"（双三角口述稿，行 1418）

> "特性是原子化的最小技术单位，叫可操作的原子化的最小技术单位。"（双三角口述稿，行 1426）

---

## 二、操作步骤

| 步骤 | 动作 | 具体做法 | 示例 |
|:---|:---|:---|:---|
| **1** | **列出当前任务需要的 Feature** | 不要从"用哪个工具"开始，先想这个任务需要什么技术特性 | 要做邮件营销 → 需要：temperature 控制（风格一致性）、few-shot（给案例）、长上下文（放产品信息） |
| **2** | **Feature 对比选工具** | 把候选工具拆成 Feature 清单，只比较 Feature 差异 | ChatGPT vs Claude：多模态、长上下文长度、代码执行——只比这几个差异，不比"谁更好" |
| **3** | **A/B 测试每个关键 Feature** | 控制变量——有它 vs 没它，结果是否变好 | Truman 团队只调了 temperature 一个参数，成本降到 1/40 |
| **4** | **沉淀有效 Feature 组合** | 把验证有效的 Feature 组合固化为 Skill | "邮件营销 Skill = temperature 0.3 + few-shot 5 个案例 + 长上下文产品信息 + JSON 输出格式" |
| **5** | **Y模型 循环迭代** | 每次使用后复盘：哪个 Feature 效果不如预期？有没有新 Feature 可以试？ | 发现长上下文塞太多产品信息反而降低质量 → 改渐进披露（分批给信息）→ 再测 |

---

## 三、适用场景

- 需要持续用 AI 做某个高价值重复任务（邮件营销/客服/内容生产）
- 团队在争论"用哪个工具/模型"——先用 Feature 清单对齐需求
- 现有 AI 工作流效果不稳定，需要系统性诊断和优化
- 新工具或新模型出现时，想快速评估是否值得迁移

---

## 四、不适用场景

- 一次性、低风险的简单 AI 任务——直接用默认设置即可
- 纯创意探索阶段——还没有可量化的评估标准时，Feature A/B 测试没有意义
- 工具的整体 UX 体验本身就是核心价值（如 Cursor 的 Tab 补全）——无法单独拆 Feature 测试

---

## 五、失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **Feature 堆砌** | 把所有知道的 Feature 都加上，提示词越来越长 | 每次只加一个 Feature，验证有效再保留 |
| **只比工具不比 Feature** | 争论"ChatGPT vs Claude"但没有具化到 Feature 差异 | 强制列出：工具 A 比工具 B 多了哪几个 Feature？ |
| **Feature 清单过时** | 用半年前的 Feature 清单评估新工具 | 每季度更新一次 Feature 清单 |
| **忽略审美和场景** | 把 Feature 调优当成唯一手段，不提升审美判断 | Feature 只能放大标准，不能创造标准——先建审美，再调 Feature |

---

## 六、Critique

**[Simplicity Advocate]**
> "Feature 思维把简单问题复杂化。大多数人的 AI 问题不是不知道 Feature，是连提示词都写不清楚。"

**回应**：Feature 训练法不是给初学者的第一步——初学者应该先用默认设置把基本流程跑通。Feature 训练法是给已经跑通了基本流程但卡在"效果不稳定/不知道如何进一步提升"的人。

---

## Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| 学了一个新工具但感觉和旧工具差不多 | 列出两个工具的 Feature 清单，找出真正的差异 |
| AI 输出质量不稳定 | 挑一个 Feature，做有它 vs 没它的 A/B 对比 |
| 想追一个新工具 | 先回答：它比我现在的工具多了哪几个 Feature？这些 Feature 是我当前任务需要的吗？ |
