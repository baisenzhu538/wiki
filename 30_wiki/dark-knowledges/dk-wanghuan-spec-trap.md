---

id: dk-wanghuan-spec-trap
title: 王欢暗知识：Spec 陷阱——过度拆解会锁死 AI 上限
type: dark-knowledge
dark_knowledge_type: insight
status: enriched
domain:
- human-ai-collaboration
- ai-collaboration
- yitang
created_at: '2026-06-19'
updated_at: '2026-06-20'
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
- signal: 你给 AI 的 spec 越写越长，输出反而越死板、越没惊喜
  lens: over-specification
  follow_up: 把 spec 拆成"方向 + 约束 + 验收"，删掉具体执行步骤
- signal: AI 严格遵守你的每一句话，结果把原本可用的代码/文案改坏了
  lens: implicit-freeze
  follow_up: 在文档里显式标注"哪些不能改"，而不是"哪些必须按我说的做"
- signal: 团队争论"AI 没按我的意思做"，而不是"结果是否达标"
  lens: means-ends-confusion
  follow_up: 把验收标准前置，执行路径交给 AI 探索
related:
  - '[[dk-modeling-ai-judgment-limit]]'
  - '[[dk-wanghuan-ai-lifts-personal-ceiling]]'
  - '[[dk-wanghuan-magic-defeats-magic]]'
  - '[[dk-wanghuan-standard-by-iteration]]'
  - '[[tool-wanghuan-ai-dual-role-coach]]'
- '[[framework-wanghuan-harness-seven-stages]]'
- '[[dk-wanghuan-magic-defeats-magic]]'
- '[[tool-wanghuan-ai-business-profile]]'
- '[[framework-wanghuan-actor-director-mode]]'
- '[[case-wanghuan-education-sales-paced]]'
tags:
- 王欢
- spec陷阱
- 过度拆解
- 只定方向不定细节
- 暗知识
---

# 王欢暗知识：Spec 陷阱——过度拆解会锁死 AI 上限

> **Burn line**：导演的工作不是写满每一步，而是说清方向、划好红线、验收结果。

---

## 用一句话讲清楚

当你把任务拆解得过细、规定得过死时，看似在"控制 AI"，实际上是在用你自己的认知天花板把 AI 的上限也封死；更反直觉的是，**只定方向 + 定好不能动的边界**，往往比"把每一步都写清楚"能得到更好的结果。

---

## 核心洞察

1. **AI 的执行上限 = 你的 spec 上限**  
   你把每一步都写死了，AI 就没有搜索更好路径的空间。它只能做一个"更听话的执行者"，而不是一个"能帮你发现更优解的协作者"。

2. **"不能做什么"比"用什么技术做"更重要**  
   王欢在课程里反复强调：在 Markdown 文件里定义清楚哪些东西不能动、哪些底线不能碰，比告诉 AI"用 React 还是 Vue"更重要。前者保护价值，后者只是手段。

3. **过度拆解的背后是人的控制焦虑**  
   担心 AI 做错，所以越写越细。但结果是把 AI 困在你的思维模式里，反而复制了你的盲区。

4. **方向 + 约束 + 验收 = 导演式控制**  
   好的 spec 只回答三个问题：去哪里（方向）、哪些红线不能碰（约束）、什么叫到了（验收）。中间路径交给 AI 去探索和迭代。

---

## 王欢的两个现场案例

### 案例 A：Harness 七阶段里的 product-spec.md

- **Phase 1 Planner** 只输出三样东西：功能优先级、审美方向、迭代计划。
- 同时标出所有**高风险歧义**，但不提前解决所有细节。
- **Phase 2-5 Sprint 对抗循环** 才是细节被逐步填充的地方。
- 如果 Phase 1 就把每个函数都定好，后面的 Sprint 就没有意义了。

### 案例 B：教育机构销冠萃取

- 如果只给新人"话术脚本"，就是把销售过程 spec 到了每一句话。
- 结果是：新人在错误时机说出正确的话。
- 王欢团队把"策略"和"话术"分开：用 PECED/PACED 框架定义决策方向（痛点→消费能力→期望→决策时机），具体话术让 AI 在模拟对练中生成。

---

## 边界

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

- [ ] 写 spec 前，先问自己："我最care的是结果，还是过程？"
- [ ] spec 控制在 1 页以内：方向（1 段）、约束（3-5 条否定句）、验收（3-5 条可检查标准）。
- [ ] 显式标注"绝对不能改/不能丢"的元素，而不是"必须按这个顺序做"。
- [ ] 给 AI 至少 3 个探索版本的空间，再进入收敛。
- [ ] 验收时先看"是否达标"，再看"是否按我的方式做"。
- [ ] 每轮迭代后，把"意外但有效"的部分沉淀进新的方向描述，而不是简单加更多限制。

---

## 相关卡 / 互链

- [[framework-wanghuan-harness-seven-stages]]：Harness 把"方向 + 约束 + 验收"拆成了可工程化的七阶段流程。
- [[dk-wanghuan-magic-defeats-magic]]：没有标准时怎么建标准；Spec 陷阱是标准过多时的另一面。
- [[tool-wanghuan-ai-business-profile]]：在"我的输出标准"里只写红线，不写执行细节。
- [[framework-wanghuan-actor-director-mode]]：从"演员"到"导演"的身份切换。
- [[case-wanghuan-education-sales-paced]]：策略与话术分离，是"只定方向不定细节"的销售落地。

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
- 不要用于安全关键、强合规、必须逐步留痕的场景。
- 不要在团队还没建立验收标准时就取消过程控制。
- 不要以"给 AI 自由"为借口逃避管理者的责任——方向和红线的定义必须更清楚。

---

## Synthesis

"Spec 陷阱"揭示了 AI 协作中一个深刻的反直觉原则：**控制欲越强，结果越差**。王欢在 harness 流程和销冠萃取案例中都展示了同一套逻辑：人负责"方向、红线、验收"，AI 负责"路径、细节、迭代"。这不是放任，而是一种更高级的控制——通过约束空间而不是规定动作来实现目标。对于从"演员"转向"导演"的个人和组织来说，克服 Spec 陷阱是效率从 30% 跃迁到 300% 的关键一跃。

---

*基于王欢 2026-06-18 AI 实战分享中的 harness 流程与销售策略案例整理。*
