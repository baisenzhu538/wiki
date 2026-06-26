---

id: skill-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai
title: 技能：清洗资料为 Markdown 格式喂给 AI
type: tool
status: enriched
author: 半肥猫
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_refs:
  - 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
related:
  - '[[concept-半肥猫-ai-learning-toolification-methodology]]'
  - '[[skill-ban-fei-mao-an-yu-yi-qie-fen-wen-dang-zuo-xiang-liang-hua]]'
  - '[[dk-ban-fei-mao-atomic-no-standard]]'
  - '[[skill-半肥猫-课程Skill化的八步工作流]]'
  - '[[skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]]'
domain:
  - ai-collaboration
  - yitang
source_person: 半肥猫
source_context: AI俱学乐部-AI学习落地 分享
tools_required:
  - 文本编辑工具
prerequisite_skills:
  - skill-半肥猫-边学边练边沉淀的AI学习法
created_at: 2026-06-07
updated_at: '2026-06-19'
diagnostic_signals:
  - source_refs 为空，原始来源未归档至 10_raw/sources/
  - 清洗成本与信息损失的量化证据不足

---

# 技能：清洗资料为 Markdown 格式喂给 AI

## 用一句话讲清楚

把原始资料（PDF、网页、Word 等）通过标准化 Markdown 清洗流程去除格式噪音、补全结构标记，转化为 AI 能高效理解的结构化输入，从而提升 AI 输出质量的上限。

## 核心要点

- **AI 的输入质量直接决定输出质量的上限**：原始资料格式混乱、噪音冗余、结构缺失，直接喂给 AI 会导致"垃圾进垃圾出"。
- **格式统一比内容丰富更重要（在喂给 AI 时）**：AI 对 Markdown 的理解远优于对 PDF/Word/网页杂糅格式的理解。一个格式规范的短文档，比一个格式混乱的长文档更有价值。
- **清洗不是翻译，是结构化的去噪**：清洗的核心不是把内容改写成"更好的中文"，而是保留原意的同时去除格式噪音、补全结构标记、统一层级关系。
- **Markdown 是 AI 的"通用语"**：几乎所有 AI 工具都原生支持 Markdown 解析，且 Markdown 的层级结构（标题、列表、引用）能被 AI 准确理解。

## 边界

### 适用场景

- ✅ 需要把外部资料（PDF、网页、Word）喂给 AI 时
- ✅ 准备建立知识库的前置步骤
- ✅ 课程资料整理为结构化文档

### 不适用场景

- ❌ 资料本身就是 Markdown 格式且结构良好
- ❌ 只需要 AI 做简单摘要，不需要深度分析
- ❌ 时间极度紧张，可以接受较低质量输出

## 失败模式

| 失败模式 | 表现 | 对策 |
|---|---|---|
| 只转换格式不处理结构 | AI 仍难以理解内容重点 | 必须添加标题层级和列表标记 |
| 过度清洗丢失信息 | 内容不完整或原意被改变 | 清洗前去噪，清洗后验证 |
| 不同来源资料格式不统一 | 知识库混乱、难以检索 | 建立统一的 Markdown 模板 |
| 低估清洗成本 | 大规模资料清洗成为瓶颈 | 先评估 ROI，优先清洗高频使用资料 |

## 行动 Checklist

- [ ] 收集原始资料并确认使用目的
- [ ] 将原始资料转换为 Markdown 格式
- [ ] 结构化处理：添加标题层级、列表标记、引用格式
- [ ] 去噪：去除页眉页脚、广告、无关链接
- [ ] 验证：快速阅读确认结构清晰、内容完整
- [ ] 归档清洗后的文档并更新相关标签

## 相关卡/互链

- [[concept-半肥猫-ai-learning-toolification-methodology]] — AI 学习工具化方法论
- [[skill-ban-fei-mao-an-yu-yi-qie-fen-wen-dang-zuo-xiang-liang-hua]] — 清洗后的文档才能做语义切分
- [[dk-ban-fei-mao-atomic-no-standard]] — 原子化没有固定标准，清洗粒度需灵活
- [[skill-半肥猫-课程Skill化的八步工作流]] — 清洗是八步工作流中的第 2 步（资料预处理）
- [[skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]] — 清洗后需要原子化标签来组织

## 来源

- 半肥猫，AI俱学乐部 AI 学习落地分享
