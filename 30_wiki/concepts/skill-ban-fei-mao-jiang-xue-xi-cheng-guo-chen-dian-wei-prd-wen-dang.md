---


id: skill-ban-fei-mao-jiang-xue-xi-cheng-guo-chen-dian-wei-prd-wen-dang
title: "技能：将学习成果沉淀为 PRD 文档"
type: tool
status: enriched
domain:
  - ai-collaboration
  - yitang- ai-collaboration
- learning
source_person: 半肥猫
source_context: AI俱乐部-AI学习落地 分享
source_refs:
- 10_raw/sources/src_20260617_f1830fa6-半肥猫-ai学习落地-口述.md
tools_required:
- AIGC大模型
- 文档编辑工具
prerequisite_skills:
- skill-半肥猫-边学边练边沉淀的AI学习法
related:
  - '[[skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]]'
  - '[[skill-ban-fei-mao-qing-xi-zi-liao-wei-markdown-ge-shi-wei-gei-ai]]'
  - '[[skill-ban-fei-mao-fei-shu-duo-wei-biao-ge-zi-jian-ji-qi-ren-zuo-tuan-dui-shu-ju-xie-tong]]'
  - '[[skill-ban-fei-mao-zhui-wen-ai-zheng-ju-bing-biao-zhu-xin-yuan]]'
  - '[[skill-半肥猫-边学边练边沉淀的AI学习法]]'
- '[[concept-半肥猫-ai-learning-toolification-methodology]]'
- '[[skill-半肥猫-课程Skill化的八步工作流]]'
- '[[skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]]'
- '[[dk-ban-fei-mao-atomic-no-standard]]'
- '[[case-ban-fei-mao-conversion-hacker-skill]]'
created_at: 2026-06-07
reviewed_by: 欧阳锋
updated_at: '2026-06-19'
author: 半肥猫
confidence: 0.88
trust_level: medium
diagnostic_signals:
- signal: 学完课程后只留下零散笔记，两周后遗忘 80%
  lens: 消耗品式学习
  follow_up: 在每次学习/对话产生阶段性成果时，让 AI 输出一份 PRD 结构备忘录
- signal: 沉淀的文档自己都不想再看第二遍
  lens: 缺少产品化思维
  follow_up: 用 PRD 五要素（问题、用户、场景、功能、边界）重检文档，删除流水账
- signal: 团队里同样的错误反复出现，经验无法复用
  lens: 能力未外化为资产
  follow_up: 把个人 PRD 上传到共享知识库，并指定 1 名维护人和 review 周期
pipeline:
- confidence-draft
- confidence-source-cited

---
# 技能：将学习成果沉淀为 PRD 文档

## 用一句话讲清楚

每次学习或 AI 对话到达阶段性成果时，用 PRD 的结构把“我知道了”写成“别人能直接用的产品说明书”，让知识从消耗品变成可复用资产。

## 核心要点

- **沉淀是学习的终极目标，而不是副产品**：大多数人学完一门课后，知识存在脑子里，两周后忘掉 80%。只有把学习成果沉淀为文档 / 工具 / SOP / Skill，才能让知识变成可复利用的资产。
- **PRD 是“能力外化”的最佳载体**：半肥猫强调不是写“笔记”，而是写“可以被别人用的产品说明书”。PRD 的结构（问题定义、目标用户、使用场景、功能描述、边界条件）能强制你把“我懂了”变成“别人能用”。
- **每次 AI 对话到阶段性成果时，就让 AI 写一份备忘录**：这不是额外工作，而是对话的自然延伸——“这一页我们聊到这里，请帮我整理一份备忘录”。这份备忘录就是沉淀。
- **沉淀必须包含决策逻辑**：不仅要记录“做了什么”，还要记录“为什么这么做”“什么时候不该这么做”，否则无法复用。
- **PRD 需要维护，不是一次性产出**：写一份 PRD 可能只要 1 小时，但保持最新、反馈业务变化，需要持续投入。

## 边界

### 适用场景

- ✅ 学完一门方法论课程后需要落地
- ✅ 完成一个项目后需要复盘
- ✅ 希望将个人经验变成团队可复用的资产
- ✅ 与 AI 讨论完一个阶段性问题，需要固化当前结论

### 不适用场景

- ❌ 纯消耗性学习（如阅读、听书）无需落地时
- ❌ 学习内容本身就是通用知识（如汉字、数学公式）
- ❌ 时间极度紧张，只能“学完就走”
- ❌ 作者对课程理解不深，尚未区分事实与推理

## 失败模式

| 失败模式 | 征兆 | 应对 |
|---|---|---|
| 沉淀变成“记录流水账” | 文档只有过程，没有可执行结构 | 用 PRD 五要素（问题、用户、场景、功能、边界）强制产品化 |
| 只沉淀“做了什么”，没沉淀“为什么这么做” | 后人看了文档仍无法做决策 | 每条核心判断都补充决策逻辑和适用条件 |
| 沉淀后不复盘、不更新 | 文档过时被束之高阁 | 设定维护周期（建议每季度 review），并指定维护人 |
| PRD 范围模糊导致滥用 | 什么场景都答，高风险场景给出错误建议 | 在 PRD 中明确拒绝条件和边界条件 |
| 把 PRD 当能力本身 | 能调用文档但关掉 AI 后无法独立分析 | 保留 20% 无 AI 练习，每周手写一次核心判断 |

## 行动 Checklist

- [ ] 完成学习/项目或 AI 对话到达阶段性成果
- [ ] 与 AI 讨论产品化可能性，确认目标用户和使用场景
- [ ] 让 AI 用 PRD 结构整理：问题定义、目标用户、使用场景、功能描述、边界条件
- [ ] 对 PRD 做三轮检查：是否可执行、是否可复用、是否有边界
- [ ] 补充决策逻辑和“什么时候不该用”
- [ ] 将 PRD 存入知识库，并打上 YAML 标签
- [ ] 设定维护周期和负责人，到期 review

## 相关卡 / 互链

- [[concept-半肥猫-ai-learning-toolification-methodology]] — 沉淀是半肥猫三层方法论的核心转化：消耗品变资产
- [[skill-半肥猫-课程Skill化的八步工作流]] — 沉淀后的产品化路径
- [[skill-ban-fei-mao-yong-yaml-ge-shi-zuo-zhi-shi-ku-yuan-zi-hua-biao-qian]] — 沉淀后的知识库管理方法
- [[case-ban-fei-mao-conversion-hacker-skill]] — 沉淀的完整实例：转化率黑客 Skill
- [[dk-ban-fei-mao-atomic-no-standard]] — 原子化没有固定标准，沉淀的切分需要灵活

## 来源

- 半肥猫，AI 俱乐部 AI 学习落地分享

## Feedback Path

- 60_feedback/comments/ — 使用此技能后有任何反馈，提交到这里
