---

id: dk-p20-bigram-fail
title: P-20：pre-screen bigram 匹配对中文文本完全失效
type: dark-knowledge
dark_knowledge_type: failure
status: enriched
domain:
- master
source_person: system
source_context: pitfalls.md P-20
source_refs:
- 10_raw/sources/src_20260619_1545a6ee_.agent_pitfalls.md#P-20
created_at: 2026-06-03
updated_at: '2026-06-19'
related:
  - '[[dk-yb32-doubao-size-composition]]'
  - '[[ouyangfeng-labeling-research-review]]'
  - '[[data-labeling-best-practices-report]]'
- '[[dk-p7-ocr-skip]]'
- '[[dk-c1-cjk-regex-silent-fail]]'
- '[[master-ai-info-literacy]]'
- '[[master-first-principles]]'
pipeline:
- confidence-draft
- confidence-source-cited
author: unknown
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 'tag-registry 的 includes/excludes 全是英文，但 KDO chunk 是中文，pre-screen 返回 0 candidates'
  framework_lens: '这是跨语言文本匹配中的"词典-语料语言不一致"故障：英文 bigram/keyword 对中文语料天然无覆盖'
  follow_up_question: '检查 tag-registry 中对应维度的 includes 是否包含中文关键词；若匹配率为 0，立即禁用 pre-screen 或切换为 LLM/Embedding 预筛'
- signal: '相同管线对英文素材正常返回 candidates，对中文素材返回空'
  framework_lens: '症状随语言切换而变化，说明匹配规则带有英语中心主义偏见，不是内容质量问题'
  follow_up_question: '分别用中英两种语料的 chunk 做匹配实验；若只有英文命中，确认需要双语词典或语言无关的匹配策略'
- signal: 'pre-screen 过滤后下游 LLM 收到的候选集为空或严重偏斜'
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

- **跨语言 bigram 失效不是"匹配算法 bug"，而是"词典语言与目标语料语言不一致"的结构性问题。** 只要 includes/excludes 是英文而 chunk 是中文，任何基于 n-gram 或关键词的预筛都会返回空。
- **"0 candidates" 是静默失败：** pre-screen 不会报错，只会输出一个"正常"的空结果，容易被误判为"这批内容真的不相关"。
- **英语中心主义是隐形假设：** 很多工具、库和默认配置以英文为基准设计，中文内容需要显式做双语化或语言无关化改造。
- **短期绕过的关键是利用 LLM 的语言无关性：** 在单选或全维度标注场景下，直接把候选送给 LLM，让模型自己判断维度归属，比修复跨语言匹配更快、更稳。
- **长期方案要替换匹配层：** 从"关键词匹配"升级为"语义匹配"（Embedding 或 LLM），才能彻底摆脱语言边界。

## 使用场景

- 你设计一个需要预筛候选的自动化管线
- 你的素材是中文，但规则/词典是英文
- 你发现匹配率为 0 或极低
- 你需要设计跨语言的文本匹配策略
- 你审查 pre-screen 输出时，看到"0 candidates"但 exit code 正常，需要判断这是真无关还是语言不匹配

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

- 这是"英语中心主义"的实战教训：很多工具默认英文，但中文内容需要特殊处理
- 极具隐蔽性：pre-screen 返回 0 candidates 不是错误，而是"正常"的空结果
- **AI 训练语料中不会有这条**：没有任何文档会写"英文 bigram 对中文 chunk 完全失效"
- 它把"语言偏见"从用户体验问题下沉到自动化管线的数据漏斗问题，揭示了默认配置中隐形的语言假设

## 与其他知识的关联

- [[dk-p7-ocr-skip]] — 同样是"中文内容在自动化管线中被排斥"的问题
- [[dk-c1-cjk-regex-silent-fail]] — 同一根因在不同阶段的变体：C-1 是 regex 词边界对 CJK 失效，P-20 是英文 bigram 对中文 chunk 失效，都暴露了工具默认配置的英语中心主义
- [[master-ai-info-literacy]] — 信息素养要求识别工具的语言偏见和默认假设，P-20 是"英文优先 pipeline"的典型盲区
- [[master-first-principles]] — 从第一性原理看，预筛的目的是"找到相关候选"，不是"执行关键词匹配"；当匹配语言与语料语言不一致时，应回到目的重新选择工具
- `.agent/pitfalls.md` → P-20（原始记录）

## 老顽童疑问（2026-06-03）

无疑问，请欧阳锋审查。
