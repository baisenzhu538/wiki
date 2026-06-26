---


id: skill-ban-fei-mao-zhui-wen-ai-zheng-ju-bing-biao-zhu-xin-yuan
title: 技能：追问 AI 证据并标注信源
type: "tool"
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- AIGC大模型
prerequisite_skills:
- skill-半肥猫-边学边练边沉淀的AI学习法
related:
  - '[[dk-modeling-ai-judgment-limit]]'
  - '[[skill-ban-fei-mao-yong-ai-zuo-jie-gou-hua-yong-hu-diao-yan]]'
  - '[[dk-ban-fei-mao-real-business-is-the-engine]]'
  - '[[skill-ban-fei-mao-gao-su-ai-dang-qian-ri-qi-xian-zhi-shu-ju-shi-xiao]]'
  - '[[dk-ban-fei-mao-silky-answer-warning]]'
  - '[[concept-半肥猫-ai-learning-toolification-methodology]]'
  - '[[skill-ban-fei-mao-you-xian-shi-yong-guan-fang-quan-wei-xin-yuan-zuo-zheng-ju]]'
  - '[[dk-ban-fei-mao-silky-answer-warning]]'
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-19'
pipeline:
- confidence-draft
- confidence-source-cited
- confidence-verified-by-case
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 'AI给出"听起来很有道理"但找不到一手数据支撑的回答'
  lens: 证据 vs 推理
  follow_up: 这是 AI 的推理还是证据？如果是证据，具体来源、时间、样本量、方法是什么？
- signal: 'AI标注了来源，但你无法独立验证该来源是否存在'
  lens: 可验证性
  follow_up: 这个信源能否通过搜索引擎、数据库或报告原文独立核实？
- signal: '在低容错场景中直接采信 AI 回答并执行'
  lens: 风险分级
  follow_up: 这个场景的错误代价是什么？是否已经验证信源并标注不确定性？

---
# 技能：追问 AI 证据并标注信源

## 用一句话讲清楚

在采信 AI 回答前，先用结构化追问把它从"讨好型回答机"逼成"证据型分析师"，并验证、标注可核实的信源。

## 核心要点

- **AI 大部分回答是基于模式匹配的推理，而非实际数据**。如果不追问，AI 会用"听起来很有道理的推理"填补缺少数据的部分，逻辑自洽但缺少一手数据支撑。
- **追问需要结构化的问题清单**。不是简单问"你有证据吗"，而是逐层区分"这是推理还是证据—数据来源是什么—如果是推理，前提条件是什么—前提不成立时结论是否还成立"。
- **信源标注的目的是可验证性**。要求 AI 标注引用信源和出处，不是为了"看起来专业"，而是为了让人可以去核实；无法验证的标注等于没有标注。
- **追问本身也有成本和边界**。信源验证可能很耗时；权威信源也可能经过叙事包装；过度追问还可能让 AI 生成更精致的假证据。

## 边界

| 维度 | 适用 | 不适用 |
|------|------|--------|
| 任务性质 | AI 帮助做调研、分析、决策支持 | 纯创意发散、脑暴、思维导图 |
| 输出用途 | 需要将 AI 回答转化为可执行方案 | 只需要"灵感"而非"准确" |
| 容错要求 | 低容错场景（金融、医疗、法律、保险） | 假设性讨论、无后果的随意尝试 |
| 时间资源 | 有足够时间验证关键信源 | 时间极度紧张、无法做任何验证 |

## 失败模式

| 失败模式 | 典型症状 | 对策 |
|----------|----------|------|
| 追问不深入 | AI 给出模糊信源或泛泛而谈 | 使用结构化问题清单逐层推进 |
| 盲目相信 AI 信源标注 | 信源是编造的或链接失效 | 用搜索引擎、数据库、报告原文快速检验 |
| 只追问一次 | AI"编得更好看"但未验证 | 多轮迭代追问，直到可验证或明确存疑 |
| 证据仪式感 | 追问的证据不影响决策结果 | 先判断该证据是否改变最终决策 |
| 迷信权威信源 | 权威机构数据也可能有叙事包装 | 结合小数据、一手体感和可验证预测能力评估 |
| 过度追问触发防御性编造 | AI 生成更精致、更像真的假证据 | 明确底线："不要扩写、不要营销话术、不要过度推断" |

## 行动 Checklist

- [ ] 获取 AI 回答后，先问："这是推理还是证据？"
- [ ] 如果是证据，追问数据来源、时间、样本量、方法
- [ ] 要求 AI 标注具体信源名称、网址、报告标题、发布日期
- [ ] 独立快速检查关键信源是否真实存在
- [ ] 告诉 AI 底线："不要扩写、不要变成营销话术、不要过度推断"
- [ ] 根据场景容错要求决定验证深度，避免无意义的证据仪式感
- [ ] 对无法验证或存疑的信息，在输出中明确标注不确定性

## 相关卡/互链

- [[concept-半肥猫-ai-learning-toolification-methodology]] — L1 三轮检查的第一轮
- [[skill-ban-fei-mao-you-xian-shi-yong-guan-fang-quan-wei-xin-yuan-zuo-zheng-ju]] — 追问证据后如何判断信源优先级的具体技能
- [[skill-ai-four-elements-validation]] — 纪浩的四要素验证，与半肥猫的证据追问同属前置判断
- [[case-ban-fei-mao-conversion-hacker-skill]] — 在 Skill 制作中应用证据追问的实践
- [[dk-ban-fei-mao-silky-answer-warning]] — "AI 回答越丝滑越有问题"，这是要追问证据的原因

## 来源

- 半肥猫，AI 俱乐部 AI 学习落地分享
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
