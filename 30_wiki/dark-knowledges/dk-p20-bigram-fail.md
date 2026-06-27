---

id: dk-p20-bigram-fail
title: P-20：pre-screen bigram 匹配对中文文本完全失效
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- src_unknown
source_person: system
source_context: pitfalls.md P-20
source_refs:
- src_unknown
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
pipeline:
- src_unknown
- src_unknown
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- src_unknown
  framework_lens: '这是跨语言文本匹配中的"词典-语料语言不一致"故障：英文 bigram/keyword 对中文语料天然无覆盖'
  follow_up_question: '检查 tag-registry 中对应维度的 includes 是否包含中文关键词；若匹配率为 0，立即禁用 pre-screen 或切换为 LLM/Embedding 预筛'
- src_unknown
  framework_lens: '症状随语言切换而变化，说明匹配规则带有英语中心主义偏见，不是内容质量问题'
  follow_up_question: '分别用中英两种语料的 chunk 做匹配实验；若只有英文命中，确认需要双语词典或语言无关的匹配策略'
- src_unknown
  framework_lens: '自动化管线的"预筛层"成为了语言歧视层，把中文内容系统性排除在后续处理之外'
  follow_up_question: '在 pre-screen 前后分别抽样检查候选集语言分布；若中文候选显著缺失，改为全量直送 LLM 或引入中文 Embedding'
---# P-20：pre-screen bigram 匹配对中文文本完全失效

## 原始表述

> **症状**：tag-registry v1.1 的 `includes`/`excludes` 字段全是英文描述（如 "falsifiable knowledge claim, testable assertion"），但 KDO 的 chunk 90% 是中文。bigram 匹配跨语言完全失效，pre-screen 返回 0 candidates。
>
> **根因**：tag-registry 设计时未考虑中英双语场景。英文 includes 对中文 chunk 无匹配价值。
>
> **对策**：
> - tag-registry 的 includes 必须包含中文关键词（中英双语）
> - 短期内绕过 pre-screen，直接送全维度候选给 LLM（单选模式不需要 pre-screen 过滤）
> - 长期：pre-screen 改为 LLM-based（"这个 chunk 可能属于哪些维度？"）或中文 Embedding 匹配

## 核心洞察

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 使用场景

- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown

## 操作方法

1. **识别跨语言问题**：
   - src_unknown
   - src_unknown

2. **短期绕过**：
   - src_unknown
   - src_unknown
   - src_unknown

3. **中英双语词典**：
   - src_unknown
   - src_unknown
   - src_unknown

4. **长期改进**：
   - src_unknown
   - src_unknown
   - src_unknown

5. **不要做的事**：
   - src_unknown
   - src_unknown
   - src_unknown

## 适用边界

| 边界 | 说明 |
|:-----|:------|
| ✅ 适合 | 规则/词典与目标文本语言不一致的跨语言预筛场景 |
| ✅ 适合 | 需要解释为什么 pre-screen 对中文返回 0 candidates |
| ❌ 不适合 | 纯英文语料与英文规则的匹配场景 |
| ❌ 不适合 | 已经使用 LLM/Embedding 做语义预筛的场景 |
| ⚠️ 注意 | 短期绕过会增加 LLM 调用成本，单选/低并发场景可接受 |
| ⚠️ 注意 | 双语词典需要持续维护，否则新维度加入时仍会漏配 |

## 常见失败模式

| 失败模式 | 真实症状 | 可执行修复 |
|:-----|:------|:------|
| 英文规则匹配中文 chunk | pre-screen 返回 0 candidates，但人工阅读 chunk 明显相关 | 为 includes/excludes 补充中文关键词；或直接绕过 pre-screen 全量送 LLM |
| 只有英文素材命中 | 同管线对英文内容正常，对中文内容返回空 | 检查 tag-registry 是否中英双语；将匹配策略改为 Embedding/LLM |
| 临时绕过后成本暴涨 | 关闭 pre-screen 后全量候选涌入下游，延迟/费用激增 | 仅在单选/低并发场景 bypass；长期改用轻量 Embedding 预筛 |
| 双语词典维护遗漏 | 新增维度只有英文 includes，中文 chunk 再次漏筛 | 建立"新增维度必须同时提供中英 includes"的 checklist |
| 把"0 candidates"当"无相关 chunk" | 批量流水线静默失败，中文内容被系统性排除 | 在 pre-screen 后加入命中数告警；按语言分布抽样检查候选集 |

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

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
