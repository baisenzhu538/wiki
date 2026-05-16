---
id: yt-prompt-brainstorming
title: AI头脑风暴工作流
type: tool
status: enriched
domain:
  - yitang
  - ai
language: zh-CN
version: 1
difficulty: intermediate
confidence: 0.85
prerequisites:
  - yt-model-prompt-engineering
component_of:
  - yt-model-prompt-engineering
source_refs:
  - 10_raw/sources/一堂-拆书会-吴恩达提示词课程.md
  - 10_raw/assets/yitang/拆书会第202期-吴恩达AI提示词课程.pdf
query_triggers:
  - 头脑风暴
  - AI创意
  - 独特资源
  - 独特约束
  - 发散收敛
  - 选项生成
  - AI杀手应用

tags:
  - '#yitang'
  - '#ai'
  - '#prompt-engineering'
  - '#brainstorming'
  - '#creativity'
created_at: '2026-05-13'
updated_at: '2026-05-13'
estimated_tokens: 2000
---

# AI 头脑风暴工作流

> [[yt-model-prompt-engineering]] 的子工具。写作是 AI 最高频场景（24.5%），但头脑风暴（仅 3.9%）才是 AI 最强的用法。AI 应该用来拔高你的上限，而不是抬高你的下限。

## Claims

### 核心判断：头脑风暴是 AI 杀手应用

- claim:01 [conf=0.90] 写作即使最好提示词也只能出 75 分——因为 AI 缺少你独特的判断、真实的故事、思想密度。头脑风暴有可能做到 95 分——因为关键输入不是 AI 的知识，而是**你的独特资源和约束**，这些东西只有你有

- claim:02 [conf=0.85] AI 头脑风暴的本质：你提供独特输入，AI 提供组合能力和搜索广度（全网知识 + 快速模式匹配），然后你用自己的判断力筛选和深化。人在这个回路中是决策者，AI 是选项生成器

### 头脑风暴工作流

- claim:03 [conf=0.85] **Step 1 — 输入独特资源**：你有什么别人没有的？（不只是钱）过去做成过什么事？团队有什么独特能力？在这个行业泡了多久、看到过什么别人看不到的东西？老客户对你的真实评价是什么？

- claim:04 [conf=0.85] **Step 2 — 输入独特约束**：钱不够多，团队不够大，窗口期只有三个月，上市公司不能碰舆情红线，不想请代言人，甲方内部团队执行能力有限……这些不是"不利条件"，它们是 AI 产出可落地方案的**必要前提**。没有约束的方案漂亮但执行不了。带着约束的方案才可能变成下周就能做的事

- claim:05 [conf=0.80] **Step 3 — 生成多个不同方向的方案**：不是"给我 10 个获客方法"——太普通了，AI 只会给你安全、常见、似曾相识的答案。问法："基于以上我的独特资源和约束，请从以下 5 个不同方向给我各出 1 个方案——(1) 零成本方向 (2) 杠杆他人资源的方向 (3) 极速验证方向（3天内出结果）(4) 反常识方向（同行都不这么做但可能有效）(5) 你最不看好的方向但告诉我为什么它可能成功"

- claim:06 [conf=0.80] **Step 4 — 发散后收敛**：从 N 个方向中选出 2-3 个最有潜力的分别深挖。深挖时 AI 的追问："这个方向最关键的一个假设是什么？如果这个假设不成立，整个方案是否还有价值？""它可以进一步拆成哪 3 个不同版本？"

### 为什么头脑风暴比写作更适合 AI

- claim:07 [conf=0.85] 写作的输出质量上限由"独特判断 + 真实故事 + 思想密度"决定——这三样 AI 都没有，所以上限 75 分。头脑风暴的输出质量上限由"独特输入的质量 + AI 组合搜索的广度"决定——独特输入你来提供，AI 负责广度，所以上限 95 分。创业中真正的好创意，往往是在限制中逼出来的

## Constraints & Boundaries

- claim:boundary-01 [conf=0.85] 头脑风暴的前提是你自己有一个值得解决的问题。如果问题本身是模糊的（"帮我想想怎么能赚钱"），AI 的头脑风暴会变成乱枪打鸟——每个方向都很宽、每个都不深入。对策：先花时间把问题定义清楚（一个具体的、有约束的、可判断的问题），再启动头脑风暴

- claim:boundary-02 [conf=0.80] 不要在第一轮头脑风暴后就做决定。AI 生成的选项看起来都很合理——这是它的谄媚本能在起作用（生成的每个选项都会附带一个让人信服的理由）。判断标准：让 AI 自己给每个方案打分并说明最可能失败的原因——只有 AI 自己能指出致命缺陷的方案，才值得深挖

## Framework Gallery

### 关联概念
- [[yt-model-prompt-engineering]] — 父框架：提示词工程总框架
- [[yt-prompt-iterative-prompting]] — 迭代提示词——头脑风暴的 Step 4 需要迭代深入
- [[yt-prompt-anti-flattery]] — 反谄媚——头脑风暴产生的选项天然被 AI 合理化了，需要反谄媚过滤
- [[yt-concept-context-engineering]] — 上下文工程——独特资源+独特约束就是头脑风暴的上下文

### 外部攻击：Mihaly Csikszentmihalyi的"三元创造力" + Teresa Amabile的"创造力要素理论"

**Mihaly Csikszentmihalyi**（克莱蒙研究大学心理学教授，"Creativity: Flow and the Psychology of Discovery and Invention"作者，创造力系统模型的创始人）论证：真正的创意突破不是在个人脑中完成的事件——它发生在个体（individual）、领域（domain，文化中的符号规则）、和场域（field，决定哪些创新有价值的社会守门人）三者的交互中。Csikszentmihalyi的挑战：AI头脑风暴的"95分"潜力来自AI对"领域"维度的控制——它能搜索全网知识、快速度匹配、生成你没想到的组合。但创意的另外两个维度——个体维度的独特生命体验（你为什么选这个组合而不是那个组合的判断）、场域维度的社会验证（用户/市场/同行会不会接受这个创新）——AI完全不参与。把AI头脑风暴定位为"95分"可能高估了"领域搜索"在创造力总价值中的占比——对于很多突破性创新，"领域搜索"恰好是最容易被替代、最不稀缺的那一块。

**Teresa Amabile**（哈佛商学院教授，"Creativity in Context: Update to the Social Psychology of Creativity"作者，创造力要素理论componential theory of creativity创始人）通过40年实证研究证明：创造力需要三个核心要素——领域相关技能（domain-relevant skills）、创造力相关过程（creativity-relevant processes）、和内在任务动机（task motivation）。Amabile的挑战：AI头脑风暴提供了领域搜索和组合（对应要素1"领域技能"），但要素2（创造力过程——你识别一个好想法的能力、你打破认知定式的思维习惯）和要素3（内在动机——你对解决这个问题本身的深层兴趣）必须来自你。AI给你10个方案，你看完后觉得"都一般"→你没有足够的创造力过程去判断哪个方案的方向是对的只是执行不够好vs哪个方案的方向本身就是死胡同。AI帮你省了搜索时间，但AI不能替你建立"识别一个好想法的能力"——这个能力来自你自己做过大量"从模糊想法→清晰方案"的实践积累。

## Synthesis

| 关系 | 目标节点 | 说明 |
|------|---------|------|
| 父框架 | [[yt-model-prompt-engineering]] | 提示词工程总框架——头脑风暴对应7层工作流中的"选项层"（生成多方案）+ "假设层"（拆解关键假设） |
| 互补工具 | [[yt-prompt-iterative-prompting]] | 迭代——发散后的每个方向都需要迭代深挖（Step 4） |
| 互补工具 | [[yt-prompt-anti-flattery]] | 反谄媚——头脑风暴的产出自带"合理化包装"，必须经过反谄媚过滤才能看到真实质量 |
| 理论基础 | [[yt-concept-context-engineering]] | 上下文工程——独特输入 = 高质量的上下文。垃圾输入 → 垃圾头脑风暴 |
