---
id: tool-yitang-ai-assisted-organize
title: AI辅助整理：把访谈录音/会议记录结构化
type: tool
status: enriched
author: 老顽童
reviewed_by: pending
created_at: 2026-06-21
confidence: 0.85
trust_level: high
language: zh-CN
domain:
- yitang
- research
source_refs:
- 00_inbox/调研专题/调研超级武器库_ocr_text.md
related:
- '[[tool-yitang-ai-assisted-analysis]]'
- '[[tool-yitang-research-normalize-summary]]'
- '[[framework-yitang-research-quality-gate]]'
- '[[concept-yitang-ai-research-human-loop]]'
- '[[tool-prompt-usp-quick-scan]]'
updated_at: '2026-06-30T16:07:51+00:00'
tags:
- audience:executor
- scene:execution
- skill-level:advanced
aliases:
- 调研专题
- 调研超级武器库
---

# AI辅助整理

> 用AI把访谈录音、会议纪要、口述稿快速结构化——提取关键信息、归类、生成摘要，让研究者从“听写”转向“判断”。

## Purpose

解决定性资料整理的“体力劳动”问题：访谈录音/会议记录通常信息密度低、口语化严重、结构散乱。本工具通过给AI设定分类框架，把原始素材快速转化为可检索、可比较、可提炼的结构化笔记，为后续分析节省 60% 以上的整理时间。

## Protocol

1. **准备原始素材**：拿到录音转文字稿、会议纪要或口述文本，先做一次粗筛，删除空泛寒暄、重复语句和明显口误。
2. **选择整理框架**：根据研究目标指定输出结构，例如“背景/需求/解决方案/商业模式/竞争/风险”六步法，或“事实/观点/情绪/待验证假设”四象限。
3. **编写AI提示词**：在提示词中明确角色（资深行业研究员）、输出格式（Markdown 表格/ bullet list）、颗粒度（逐条 vs. 合并），并要求AI标注置信度与原文出处。
4. **分段处理与人工复核**：对超过模型上下文的长文档分段输入；逐段核对关键数据、数字、引语，确认AI没有遗漏“语气犹豫”“情绪转折”等非文本信号。
5. **输出结构化卡片**：把整理结果导入笔记系统，打上标签，与研究问题、假设清单和待验证事项建立双向链接。

## When NOT to Use

| 场景 | 原因 | 替代方案 |
|------|------|----------|
| 受访对象涉及高度敏感或法律风险信息 | AI可能在云端处理，存在泄露与合规风险 | 本地脱敏转写 + 人工整理 |
| 原始录音质量极差（噪音大、多人重叠发言） | 转写错误率高，AI整理会“ garbage in, garbage out” | 先人工校对转写稿，再使用本工具 |
| 研究目标是生成全新洞察而非结构化归类 | AI擅长归纳已有信息，不擅长跨领域创造性连接 | 先用本工具整理，再使用人工工作坊/类比推理 |
| 关键决策依赖单一访谈中的微妙信号 | AI容易漏掉停顿、情绪、非语言线索 | 研究者逐句回听原文，结合现场观察 |

## 质疑

- **具体假设**：本工具默认“原始文本已能承载主要信息”，但访谈研究的有效信息往往藏在语气、沉默和语境中，AI无法自动识别这些非文本信号。
- **边界**：AI整理适合“信息归类、摘要、去重”，不适合“事实核查、因果推断、价值判断”。
- **反例**：当受访者用模糊措辞“可能吧”“我们还在看”表达保留态度时，AI可能把中性语气误判为肯定陈述，导致后续分析出现系统性偏差。
- **前提**：提示词必须清晰、框架必须与研究问题匹配；如果研究者本身没有明确问题，AI只会给出“看上去整齐但实则无关”的整理结果。
- **外部反对者**：**Peter Drucker** 会批评说，“用AI把混乱结构化”并不能替代研究者对“该问什么问题”的判断；工具整理得再漂亮，如果问题错了，也只是把错误分类得更清晰。

## Synthesis

- [[tool-yitang-ai-assisted-analysis]]：结构化整理后，通常需要进一步做对比分析与模式识别。
- [[tool-yitang-research-normalize-summary]]：整理结果可作为规范化摘要的输入，统一输出格式。
- [[framework-yitang-research-quality-gate]]：在整理完成后，用研究质量门检查是否满足置信度与可复核要求。
- [[concept-yitang-ai-research-human-loop]]：强调AI整理必须保留人工复核闭环，避免“黑箱结构化”。

---

*卡片类型：tool | 审核状态：待审*
