---
id: "ocr-婚礼操盘-用户和场景"
created_at: 2026-05-21
domain:
  - "yitang"
source_refs:
  - "src_20260522_94ee2a08"
status: "enriched"
title: "OCR: 婚礼操盘-用户和场景"
type: "concept"
updated_at: 2026-05-22
tags:
  - #scene/ai-collaboration
  - #scene/business-analysis
  - #scene/knowledge-management/tagging
  - #scene/learning-methodology/mental-models
  - #scene/note-taking/checklist-method
  - #scene/note-taking/level-diagnosis
  - #scene/skill-engineering
pipeline:
  - confidence-source-cited
---

# OCR: 婚礼操盘-用户和场景

## Summary

原图: `00_inbox/婚礼操盘-用户和场景.

png` 婚礼操盘：用户与场景分析 传统方式 我们的设计 我们列了一个优先级排序： 1.

新郎新娘同学、同事、好友。

## Source Refs

- `src_20260522_94ee2a08` -> `10_raw/sources/src_20260522_94ee2a08-ocr-婚礼操盘-用户和场景.md`

## Reusable Knowledge

- 婚礼操盘的用户优先级排序为：双方父母 > 双方至亲长辈 > 新郎新娘的同学/同事/好友 > 双方远亲和邻里乡亲。
- 传统婚礼方式采用"基本不分层"的宾客对待模式，与分层精细化运营形成对比。
- 婚礼场景设计需区分用户层级，针对不同关系亲疏采取差异化服务策略。

## Open Questions

- 该优先级排序的具体依据是什么（情感亲密度、礼金金额、社交义务、还是其他维度）？
- "基本不分层"的传统方式在实际操作中是否存在隐性分层（如主桌/副桌安排），而非真正的无差别对待？
- 分层精细化运营的具体服务差异体现在哪些环节（座位安排、菜品档次、互动流程、礼品回馈等）？
- 新郎新娘自身在优先级排序中的位置为何缺失，其自主权与父母期望如何平衡？
- "邻里乡亲"被归入最低优先级，是否考虑了地域文化差异（如农村/城市、北方/南方）对社区关系重视程度的不同？
- 该排序是否经过用户验证，还是仅为策划方的假设性框架？
- OCR 提取的">>"符号是否为原图中的视觉层级指示（如箭头/缩进），其实际含义是"远大于"还是排版错误？


## Critique

### 内部局限

- **场景特定性强：本卡片内容高度依赖于婚礼这一特定场景，其方法论的跨场景迁移性未被验证。
- **情感因素未被量化：婚礼规划涉及大量情感决策，未被量化的情感因素可能导致方法论的不稳定性。

### 外部攻击

#### Daniel Kahneman — “情感决策中的噪声”

Daniel Kahneman 在《噪声》中证明：即使是经验丰富的专家，在情感决策中也会受到噪声干扰。Kahneman 会质疑：**当你用"科学方法"去规划婚礼时，你是否忽视了情感的不可预测性？**

#### Herbert Simon — “有限理性下的情感决策”

Herbert Simon 会质疑：**婚礼规划中的"最优解"可能不存在，因为情感价值观的多元性使得"最优"本身就是一个主观概念。**

### 不要用的场景

- **商业项目的冷静分析：婚礼规划中的情感因素可能会干扰冷静的商业分析。
- **跨文化婚礼规划：不同文化对婚礼的期待和仪式差异巨大，通用方法论可能不适用。

## Synthesis

### 与本库其他概念的关联

- [[yt-decision-project-management]] — 项目管理的理论基础
- [[yt-decision-user-research]] — 用户研究的方法论补充

### 可迁移场景

- 婚礼规划：用本框架快速定位婚礼的关键要素
- 活动策划：将婚礼规划方法迁移到其他大型活动策划

## Output Opportunities

Content: <analysis: "婚礼操盘用户分层模型批判性评估" — 运用一堂方法论中的"段位"框架（管理修炼地图）和IPO科学学习模型，对OCR提取的婚礼宾客优先级排序进行假设验证分析，输出结构化决策检查清单，覆盖隐性分层识别、地域文化变量、新人自主权平衡等开放问题>
Code: <template: `wedding-stakeholder-prioritizer.md` — 可复用的Markdown决策模板，将"双方父母/至亲/好友/远亲邻里"四级框架转化为可配置的权重评分表，集成一堂"清单体笔记"方法论，支持按地域文化标签（农村/城市/南北）动态调整优先级>
Capability: <workflow: "OCR→KDO 结构化审校流水线" — 整合PaddleOCR ONNX双模Skill与KDO协议，建立"机器提取→人工校对→结构还原→开放问题生成→输出机会识别"五步工作流，特别针对视觉层级符号（如">>"箭头/缩进）的语义消解和排版歧义处理>
