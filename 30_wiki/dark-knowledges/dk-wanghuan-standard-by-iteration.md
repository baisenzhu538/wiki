---
id: dk-wanghuan-standard-by-iteration
title: 王欢暗知识：标准不清时，用AI对抗AI生成标准
type: dk
dark_knowledge_type: workflow
status: reviewed
domain:
  - human-ai-collaboration
  - ai-collaboration
  - yitang
created_at: '2026-06-19'
updated_at: 2026-06-28
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.88
trust_level: medium
source_person: 王欢
source_context: 王欢 AI 实战分享课后问答（2026-06-18）
source_refs:
- 10_raw/sources/src_20260619_536bca67_wanghuan_actor_director_oral.txt
- 10_raw/sources/src_20260619_a3a2a803_wanghuan_actor_director_notes.txt
related:
  - [[dk-modeling-ai-judgment-limit]]
  - [[master-ai-info-literacy]]
  - [[dk-wanghuan-ai-lifts-personal-ceiling]]
  - [[dk-wanghuan-magic-defeats-magic]]
  - [[tool-wanghuan-ai-dual-role-coach]]
  - human-ai-collaboration-double-triangle
  - framework-wanghuan-actor-director-mode
  - concept-wanghuan-adversarial-generation
  - framework-wanghuan-bitcoe-prompt-framework
diagnostic_signals:
- signal: src_unknown
  framework_lens: 标准来自迭代——标准不是想出来的，是迭代出来的
  follow_up_question: 让AI先生成一版，再让另一个AI调研最佳实践来评审，迭代7-8轮标准自然浮现。
- signal: src_unknown
  framework_lens: 标准来自迭代——用AI按最高标准挑毛病，把模糊直觉具象化
  follow_up_question: 请AI自己按最高标准找问题，它能帮你把'感觉不对'翻译成具体标准。
- signal: src_unknown
  framework_lens: 标准来自迭代——AI对抗AI，在迭代中建立标准
  follow_up_question: 用AI对抗AI的方法：生成初版→调研最佳实践→评审→修改→迭代到成熟。
- signal: src_unknown
  framework_lens: 标准来自迭代——设定终止条件
  follow_up_question: 设定'连续两轮无重大问题'终止条件，避免无限迭代。
- signal: src_unknown
  framework_lens: 标准来自迭代——用不同模型/视角做评审，避免互相附和
  follow_up_question: 评审者和生成者用不同模型了吗？同模型容易互相附和。
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
review_date: '2026-06-28'
---
# 王欢暗知识：标准不清时，用AI对抗AI生成标准

> **Burn line**: 当你不知道“好”的标准是什么，不要空想，先让 AI 出一版，再用另一个 AI 按最高标准挑毛病，反复迭代，标准自然浮现。

## 原始表述

很多人卡在 AI 协作的起点：**我不知道我要什么，所以我无法告诉 AI 我要什么**。

王欢的解法：**用魔法打败魔法**。先让 AI 出一个初版（默认它不合格），再让另一个 AI/评审者按“最高标准”挑毛病，把问题清单扔回给生成 AI 要求修改，反复迭代 7-8 轮，直到两个 AI 都挑不出大毛病。

> 标准不是想出来的，是迭代出来的。

## 使用场景

- **完全没做过某类事**：如团队没人做过书，但要把书做出来
- **创意/设计/内容类任务**：标准模糊，需要迭代逼近
- **新项目探索**：个人或团队探索新项目，没有现成标准
- **验收标准不清**：不知道“好”的标准是什么，无法定义 checklist
- **AI 输出说不出哪里不对**：凭感觉判断，需要具象化标准

## 操作方法

1. **五步循环**：
   - 步骤 1：让 AI 生成初版（不预设质量）
   - 步骤 2：让另一个 AI 调研“这件事的全球最佳实践/最高标准”
   - 步骤 3：用最佳实践作为评审标准，让 AI 挑初版的毛病
   - 步骤 4：把问题清单扔回生成 AI，要求修改
   - 步骤 5：重复步骤 2-4，直到 AI 挑不出大毛病，人也挑不出大毛病
2. **关键心态**：
   - 强制默认初版不合格
   - 评审 AI 必须引用具体最佳实践，不能只说“不够好”
   - 设定“连续两轮无重大问题”终止条件
   - 评审者和生成者用不同模型，避免互相附和
3. **示例：做一本没做过的书**：
   - 让 AI 出一版书的结构和设计
   - 让另一个 AI 调研“全球最佳出版社做书的标准”
   - 用这些标准评审第一版：配色、排版、内容结构、章节逻辑
   - 把问题扔回 AI 修改，迭代 7-8 轮直到方案成熟

## 适用边界

| 适用 | 不适用 |
|:---|:---|
| 你完全没做过某类事，标准模糊 | 已有明确行业标准和验收 checklist |
| 创意类、设计类、内容类任务 | 安全关键型、有硬性合规要求的任务 |
| 个人或团队探索新项目 | 需要一次性做对、不能返工的任务 |

## 为什么值钱

1. **突破标准困境**：不知道标准时，用迭代代替空想，标准自然浮现
2. **对抗迭代鲁棒性**：生成器+评审器分离，标准质量远高于单一判断
3. **最佳实践内化**：通过调研最佳实践+评审，把外部标准转化为内部标准
4. **效率跃迁**：7-8 轮迭代后标准成熟，后续同类任务可直接复用

## 与其他知识的关联

- [[dk-wanghuan-magic-defeats-magic]]——用 AI 对抗 AI 建立标准，同一方法论
- [[dk-wanghuan-spec-trap]]——王欢 Spec 陷阱，方向+约束+验收的导演思维
- [[dk-wanghuan-creativity-in-description-and-taste]]——创造力重新分配，验收审美方法
- [[yt-five-step-method]]——一堂五步法，系统化迭代框架
- [[dk-tool-as-phased-validator]]——分阶段校验器，迭代验证方法

---

## 失败模式 / 常见走偏

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **对初版太宽容** | 看了一眼觉得“还行”，不再迭代 | 强制默认初版不合格 |
| **评审标准太泛** | 评审 AI 只会说“不够好” | 要求评审 AI 引用具体最佳实践 |
| **迭代没有终止条件** | 永远觉得还能更好 | 设定“连续两轮无重大问题”终止 |
| **只用一个模型** | 评审者和生成者同模型，容易互相附和 | 用不同模型/不同视角做评审 |
