---
id: dk-wanghuan-spec-trap
title: 王欢暗知识：Spec 陷阱——过度拆解会锁死 AI 上限
type: dk
dark_knowledge_type: insight
status: reviewed
domain:
- human-ai-collaboration
- ai-collaboration
- yitang
created_at: '2026-06-19'
quality_labels:
- cited
- quality
- validated
updated_at: 2026-06-28
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享（2026-06-18 授课）中的 harness 流程与销售策略案例
source_refs:
- 10_raw/sources/src_20260619_1ffb2cef_wanghuan_harness的七个阶段_示意图.md
- 10_raw/sources/src_20260619_2b457485_wanghuan_harness的七个阶段_示意图_ocr.md
- 10_raw/sources/src_20260619_536bca67_wanghuan_actor_director_oral.txt
- 10_raw/sources/src_20260619_a3a2a803_wanghuan_actor_director_notes.txt
diagnostic_signals:
- signal: src_unknown
  lens: over-specification
  follow_up: 把 spec 拆成"方向 + 约束 + 验收"，删掉具体执行步骤
- signal: src_unknown
  lens: implicit-freeze
  follow_up: 在文档里显式标注"哪些不能改"，而不是"哪些必须按我说的做"
- signal: src_unknown
  lens: means-ends-confusion
  follow_up: 把验收标准前置，执行路径交给 AI 探索
related:
- '[[dk-wanghuan-tacit-decision-extraction-cross-domain]]'
- '[[dk-wanghuan-paced-sales-decision]]'
- '[[dk-wanghuan-agent-platform-director-mode]]'
- '[[yt-five-step-method]]'
- '[[dk-tool-as-phased-validator]]'
- '[[ai-collaboration-domain-digest]]'
- '[[yitang-domain-digest]]'
tags:
aliases:
  - 王欢暗知识：Spec陷阱过度拆解会锁死AI上限
  - 王欢暗知识
  - 陷阱
  - 过度拆解会锁死
  - 上限
  - 王欢
aliases:
  - 王欢暗知识：Spec陷阱过度拆解会锁死AI上限
  - 王欢暗知识
  - 陷阱
  - 过度拆解会锁死
  - 上限
  - 王欢
- audience:executor
- scene:reference
- skill-level:intermediate
review_date: '2026-06-28'
aliases:
- 的七个阶段
- 示意图
---

# 王欢暗知识：Spec 陷阱——过度拆解会锁死 AI 上限

> **Burn line**：导演的工作不是写满每一步，而是说清方向、划好红线、验收结果。

## 原始表述

当你把任务拆解得过细、规定得过死时，看似在"控制 AI"，实际上是在用你自己的认知天花板把 AI 的上限也封死；更反直觉的是，**只定方向 + 定好不能动的边界**，往往比"把每一步都写清楚"能得到更好的结果。

## 使用场景

- **AI 协作任务设计**：需要 AI 探索更优解的创意/分析/策略任务
- **产品需求文档编写**：定义方向、红线、验收标准，而非每一步执行细节
- **销售策略萃取**：用 PACED/PECED 定义决策方向，具体话术让 AI 生成
- **Harness 流程设计**：七阶段流程中 product-spec.md 的编写规范
- **组织角色转型**：从"执行者"转为"导演"，学会约束空间而非规定动作

## 操作方法

1. **定义方向**：说清楚"去哪里"，而不是"怎么走"
2. **划定红线**：明确"绝对不能出现什么""哪些不能动"
3. **设定验收标准**：用业务结果验收，而不是技术栈或格式
4. **留出探索空间**：把执行路径交给 AI 探索和迭代
5. **设计对抗循环**：生成→评审→迭代，逐步收敛

## 适用边界

| 适用 | 不适用 |
|:---|:---|
| 任务存在多种可行路径，需要 AI 探索更优解 | 任务路径已经高度标准化，必须严格合规 |
| 你的核心目标是"结果达标"，而不是"过程可控" | 安全、医疗、金融等强监管场景，必须留痕每一步 |
| 你有能力定义清晰的验收标准 | 你连验收标准都给不出来 |
| 团队愿意把程序员/作者从执行者转为质量守门人 | 组织文化高度依赖"可见的忙碌" |
| 使用多轮 Sprint / 对抗迭代来逐步收敛 | 只有一次出结果的机会 |

## 为什么值钱

1. **突破认知天花板**：AI 的执行上限 = 你的 spec 上限，过度拆解锁死 AI
2. **控制焦虑的解药**：过度拆解的背后是人的控制焦虑，约束空间比规定动作更有效
3. **导演式控制**：人负责方向、红线、验收，AI 负责路径、细节、迭代
4. **效率跃迁**：克服 Spec 陷阱是从"演员"转向"导演"的关键一跃

## 与其他知识的关联

- [[dk-wanghuan-tacit-decision-extraction-cross-domain]]——王欢隐性判断萃取，导演思维
- [[dk-wanghuan-paced-sales-decision]]——王欢 PACED 销售决策，方向+约束+验收
- [[dk-wanghuan-agent-platform-director-mode]]——王欢 Agent 平台导演模式
- [[yt-five-step-method]]——一堂五步法，系统化任务设计框架
- [[dk-tool-as-phased-validator]]——分阶段校验器，验收标准设计方法

---

## 失败模式 / 常见走偏

| 适用 | 不适用 |
|:---|:---|
| 任务存在多种可行路径，需要 AI 探索更优解 | 任务路径已经高度标准化，必须严格合规 |
| 你的核心目标是"结果达标"，而不是"过程可控" | 安全、医疗、金融等强监管场景，必须留痕每一步 |
| 你有能力定义清晰的验收标准 | 你连验收标准都给不出来 |
| 团队愿意把程序员/作者从执行者转为质量守门人 | 组织文化高度依赖"可见的忙碌" |
| 使用多轮 Sprint / 对抗迭代来逐步收敛 | 只有一次出结果的机会 |

---

## 失败模式 / 常见走偏

| 走偏模式 | 触发原因 | 后果 | 纠偏动作 |
|:---|:---|:---|:---|
| **5 页 spec 才启动** | 担心 AI 不懂 | AI 没开始就已经被限制在你的思路里 | 先给 1 页：方向 + 红线 + 验收 |
| **把格式当标准** | 误以为"用表格输出"就是高质量 | 格式对了，内容仍然空洞 | 区分格式偏好与内容质量红线 |
| **中途无版本控制地加细节** | 看到 AI 输出后不断补限制 | AI 越改越碎，丢失原有亮点 | 先冻结不能动的部分，再提优化方向 |
| **用技术选型替代验收标准** | 认为"用某某框架"就能保证质量 | 技术对了，业务目标仍然不达 | 用业务结果验收，而不是技术栈 |
| **只定正面要求，不定负面约束** | 怕限制 AI 创造力 | AI 不断加你不想要的东西 | 明确"绝对不能出现什么" |
| **把 AI 当黑盒执行器** | 不信任 AI 的探索能力 | 自己成为瓶颈 | 设计"生成-评审-迭代"的对抗循环 |

---

## 行动 Checklist

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接

---

## 相关卡 / 互链

- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接
- 待补充链接

---

## Critique

**攻击者 1：合规与风控经理**
> "在金融、医疗、航空这些领域，每一步都必须可追溯、可审计。你只定方向，出了问题谁负责？"
>
> **回应**：Spec 陷阱反对的是"不必要的细节控制"，不是反对合规。在高监管场景，红线、约束、审计轨迹必须保留；但即便如此，也仍然可以把"技术实现路径"交给 AI 探索，而不是把每个函数都预先规定。控制的是风险边界，不是执行路径。

**攻击者 2：完美主义管理者**
> "我不写细，AI 做出的东西肯定不符合我的审美/习惯。"
>
> **回应**：如果你说不清楚"符合"的标准，写再细也没用，因为 AI 无法推断你的隐性偏好。更好的做法是把审美/习惯转译成可检查的约束（例如"不能出现紫色渐变"、"必须使用无衬线字体"），然后让 AI 在约束内探索。你会发现 AI 给出的方案往往有你没想到的解法。

**不要用**：
- 待补充链接
- 待补充链接
- 待补充链接

---

## Synthesis

"Spec 陷阱"揭示了 AI 协作中一个深刻的反直觉原则：**控制欲越强，结果越差**。王欢在 harness 流程和销冠萃取案例中都展示了同一套逻辑：人负责"方向、红线、验收"，AI 负责"路径、细节、迭代"。这不是放任，而是一种更高级的控制——通过约束空间而不是规定动作来实现目标。对于从"演员"转向"导演"的个人和组织来说，克服 Spec 陷阱是效率从 30% 跃迁到 300% 的关键一跃。

---

*基于王欢 2026-06-18 AI 实战分享中的 harness 流程与销售策略案例整理。*
