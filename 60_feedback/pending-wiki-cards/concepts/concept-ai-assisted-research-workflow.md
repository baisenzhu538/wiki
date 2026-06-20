---
title: "AI 辅助调研全流程"
type: concept
status: draft
confidence: 0.80
domain:
  - research-methodology
author: yitang
reviewed_by: pending
source_refs:
  - "00_inbox/调研专题/一堂-调研武器库培训-口述.txt"
  - "00_inbox/调研专题/系统调研AI教练背后_vlm_desc.md"
created_at: "2026-06-20"
updated_at: "2026-06-20"
diagnostic_signals:
  - "AI工具链"
  - "调研流程自动化"
  - "人机协同"
related:
  - "[[framework-wanghuan-ai-five-level-ladder]]"
  - "[[concept-ji-hao-ai-collaboration-methodology]]"
---

# AI 辅助调研全流程

AI 在商业调研中不是替代人，而是在调研流程的每个环节嵌入为增强工具。

## AI 覆盖的调研环节

| 调研阶段 | AI可做的事 | 典型工具（截至2026年初） |
|:---------|:----------|:---------------------|
| 信息搜索 | 多源并行搜索、自动翻译外文资料、信源可信度初筛 | Perplexity, 秘塔 |
| 信息整理 | 自动分类、结构化提取、关键数字核验 | ChatGPT, Claude |
| 报告草写 | 生成结构化初稿、格式化输出、引用管理 | Gamma, Claude |
| 数据分析 | 趋势识别、异常检测、跨源对比 | ChatGPT+插件 |
| 假设验证 | 模拟Pre-Mortem、反向论证、逻辑一致性检查 | Claude |

## 边界

AI 能做的是"量"的放大，不是"质"的替代：
- AI 可以读100份财报→人只需要读AI挑出的3份异常报告
- AI 不能替代"现场感"——蹲店、数人头、感受用户真实场景，这些仍然是人的核心优势
- AI 不能替代"判断"——OSCAR中的R(Reasoning)这一步，人必须自己完成

### [Critique]

- **Assumption**：此卡中工具清单时效性极强，需每季度更新。
- **Boundary**：适用于公开信息密集型调研（行业分析、竞品扫描）。对于高度依赖一手访谈的调研（如用户需求深挖），AI的辅助价值递减。

### [Synthesis]

- 对接 [[framework-wanghuan-ai-five-level-ladder]]：AI辅助调研覆盖了从"效率"到"作品"的多个层级
- 对接 [[concept-ji-hao-ai-collaboration-methodology]]：人做判断，AI做放大

---

## 更新记录

- 2026-06-20：初始版本。来源：武器库培训口述 + AI教练冰山图VLM。
