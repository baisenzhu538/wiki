---


id: skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian
title: 技能：用 YAML 格式做知识库原子化标签
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
source_person: 半肥猫
source_context: AI俱学乐部-AI学习落地 分享
source_refs:
  - 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- 文本编辑工具
- 知识库管理工具
prerequisite_skills:
- skill-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai
related:
  - '[[dk-p19-quote-yaml]]'
  - '[[skill-ban-fei-mao-fei-shu-duo-wei-biao-ge-zi-jian-ji-qi-ren-zuo-tuan-dui-shu-ju-xie-tong]]'
  - '[[skill-ban-fei-mao-zhui-wen-ai-zheng-ju-bing-biao-zhu-xin-yuan]]'
  - '[[skill-ban-fei-mao-an-yu-yi-qie-fen-wen-dang-zuo-xiang-liang-hua]]'
  - '[[dk-f13-handwritten-yaml-parser]]'
  - '[[concept-半肥猫-ai-learning-toolification-methodology]]'
  - '[[skill-ban-fei-mao-an-yu-yi-qie-fen-wen-dang-zuo-xiang-liang-hua]]'
  - '[[dk-ban-fei-mao-atomic-no-standard]]'
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-19'
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- 单一口述来源，缺乏多源交叉验证
- source_refs 未指向 10_raw/sources/ 下的可审计文件
pipeline:
- confidence-draft
- confidence-source-cited

---
# 技能：用 YAML 格式做知识库原子化标签

## 用一句话讲清楚

用 YAML frontmatter 为每份原子化文档打上结构化标签，让 AI 在检索时同时阅读“内容 + 标签”，从而在毫秒级定位最相关的知识片段。

## 核心要点

- **原子化是可扩展的前提**：一份 50 页的综合文档，AI 只能整体匹配；拆成 50 个单主题文档后，AI 可以精准匹配到最相关的片段。
- **YAML 标签是“给 AI 的索引”，不是“给人看的分类”**：标签设计要服务于 AI 的筛选逻辑与语义关系表达。
- **标签体系应业务驱动**：维度可包括主题、类型、版本、日期、适用场景、风险等级等，没有通用最佳模板。
- **标签值必须标准化**：例如日期统一为 `YYYY-MM-DD`，类型使用枚举值，避免检索时匹配失败。

## 边界

### 适用场景

- ✅ 建立可扩展的知识库
- ✅ 需要 AI 精准检索特定类型知识的场景
- ✅ 多人协作、需要统一知识组织标准的团队

### 不适用场景

- ❌ 个人临时笔记，不需要长期维护
- ❌ 内容量小（<20 篇），检索效率不是问题
- ❌ 团队没有共识的标签标准，强行推行会导致混乱

## 失败模式

| 失败模式 | 征兆 | 应对 |
|---|---|---|
| 标签设计过于复杂 | 维护成本高、使用率低 | 从 3-5 个核心维度开始，逐步扩展 |
| 标签值不统一 | AI 检索时匹配失败或召回偏差 | 建立标签值枚举规范并做校验 |
| 标签和内容脱节 | 标签不能反映实际内容 | 定期做标签审计，与内容同步更新 |
| YAML 格式错误 | 整篇文档 frontmatter 解析失败 | 使用带 YAML 语法高亮的编辑器并做 lint 检查 |

## 行动 Checklist

- [ ] 将文档拆分为单主题原子化单元
- [ ] 为每篇文档顶部添加 YAML frontmatter
- [ ] 根据业务场景定义 3-5 个核心标签维度
- [ ] 制定标签值枚举规范并写入团队约定
- [ ] 使用 YAML 语法高亮编辑器编辑 frontmatter
- [ ] 定期检查标签与内容的一致性并更新旧标签

## 相关卡 / 互链

- [[skill-半肥猫-课程Skill化的八步工作流]] — 标签设计是八步中的第 6 步（目录结构设计）
- [[skill-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]] — 清洗后的文档才能打标签
- [[skill-ban-fei-mao-an-yu-yi-qie-fen-wen-dang-zuo-xiang-liang-hua]] — 标签和向量化是两种不同维度的组织方式
- [[dk-ban-fei-mao-atomic-no-standard]] — “原子化没有固定标准”，标签粒度需要灵活

## 来源

- 半肥猫，AI俱学乐部 AI 学习落地分享

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
