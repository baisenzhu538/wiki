---
id: "dk-p20-bigram-fail"
title: "P-20：pre-screen bigram 匹配对中文文本完全失效"
type: "dark-knowledge"
dark_knowledge_type: "failure"
status: "draft"
domain:
  - "master"
source_person: "system"
source_context: "pitfalls.md P-20"
source_refs:
  - ".agent/pitfalls.md#P-20"
created_at: 2026-06-03
updated_at: 2026-06-03
related:
  - "dk-p7-ocr-skip"
contradicts:
  - "master-ai-info-literacy"
  - "master-first-principles"
tags:
  - None
  - None
  - None
  - None
  - None
pipeline:
  - None
  - None
  - "confidence-draft"
  - "confidence-source-cited"
author: "legacy"
reviewed_by: "pending"
confidence: 0.7
trust_level: "low"
---

# P-20：pre-screen bigram 匹配对中文文本完全失效

## 原始表述

> **症状**：tag-registry v1.1 的 `includes`/`excludes` 字段全是英文描述（如 "falsifiable knowledge claim, testable assertion"），但 KDO 的 chunk 90% 是中文。bigram 匹配跨语言完全失效，pre-screen 返回 0 candidates。
>
> **根因**：tag-registry 设计时未考虑中英双语场景。英文 includes 对中文 chunk 无匹配价值。
>
> **对策**：
> - tag-registry 的 includes 必须包含中文关键词（中英双语）
> - 短期内绕过 pre-screen，直接送全维度候选给 LLM（单选模式不需要 pre-screen 过滤）
> - 长期：pre-screen 改为 LLM-based（"这个 chunk 可能属于哪些维度？"）或中文 Embedding 匹配

## 使用场景

- 你设计一个需要预筛候选的自动化管线
- 你的素材是中文，但规则/词典是英文
- 你发现匹配率为 0或极低
- 你需要设计跨语言的文本匹配策略

## 操作方法

1. **识别跨语言问题**：
   - 检查规则/词典的语言与目标文本的语言是否一致
   - 如果不一致，bigram/keyword 匹配可能失效

2. **短期绕过**：
   - 禁用 pre-screen，直接送全量候选给下游
   - 如果下游是 LLM，它可以自己判断
   - 确保不会因为 pre-screen 过滤掉有价值的候选

3. **中英双语词典**：
   - 每个 includes/excludes 字段同时包含中文和英文
   - 例："可证伪的知识声明, falsifiable knowledge claim"
   - 确保两种语言的 chunk 都能被匹配

4. **长期改进**：
   - 考虑使用 Embedding 匹配而非关键词匹配
   - 或者使用 LLM 做预筛
   - 这些方法对语言不敏感

5. **不要做的事**：
   - 不要用英文规则匹配中文文本
   - 不要假设"英文关键词足够了"
   - 不要在匹配率为 0 时还坚持使用原方案

## 适用边界

- 适用于所有跨语言文本匹配场景
- 不适用于单语言场景
- **与 P-7 的区别**：P-7 是"跳过了图片"，P-20 是"匹配不了中文"——同样是"中文内容在自动化管线中被排斥"

## 为什么值钱

- 这是"英语中心主义"的实战教训：很多工具默认英文，但中文内容需要特殊处理
- 极具隐蔽性：pre-screen 返回 0 candidates 不是错误，而是"正常"的空结果
- **AI 训练语料中不会有这条**：没有任何文档会写"英文 bigram 对中文 chunk 完全失效"

## 与其他知识的关联

- dk-p7-ocr-skip — 同样是"中文内容在自动化管线中被排斥"的问题
- `.agent/pitfalls.md` → P-20（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
