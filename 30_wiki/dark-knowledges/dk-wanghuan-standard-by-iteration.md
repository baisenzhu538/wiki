---

id: dk-wanghuan-standard-by-iteration
title: 王欢暗知识：标准不清时，用AI对抗AI生成标准
type: dk
dark_knowledge_type: workflow
status: enriched
domain:
- src_unknown
- src_unknown
- src_unknown
created_at: '2026-06-19'
updated_at: '2026-06-20'
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
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown
  - src_unknown-double-triangle
  - src_unknown
  - src_unknown
  - src_unknown
diagnostic_signals:
- signal: src_unknown
  framework_lens: 标准来自迭代——标准不是想出来的，是迭代出来的
  follow_up_question: "让AI先生成一版，再让另一个AI调研最佳实践来评审，迭代7-8轮标准自然浮现。"
- signal: src_unknown
  framework_lens: 标准来自迭代——用AI按最高标准挑毛病，把模糊直觉具象化
  follow_up_question: "请AI自己按最高标准找问题，它能帮你把'感觉不对'翻译成具体标准。"
- signal: src_unknown
  framework_lens: 标准来自迭代——AI对抗AI，在迭代中建立标准
  follow_up_question: "用AI对抗AI的方法：生成初版→调研最佳实践→评审→修改→迭代到成熟。"
- signal: src_unknown
  framework_lens: 标准来自迭代——设定终止条件
  follow_up_question: "设定'连续两轮无重大问题'终止条件，避免无限迭代。"
- signal: src_unknown
  framework_lens: 标准来自迭代——用不同模型/视角做评审，避免互相附和
  follow_up_question: "评审者和生成者用不同模型了吗？同模型容易互相附和。"
tags:
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
- src_unknown
---
# 王欢暗知识：标准不清时，用AI对抗AI生成标准

> **Burn line**: 当你不知道“好”的标准是什么，不要空想，先让 AI 出一版，再用另一个 AI 按最高标准挑毛病，反复迭代，标准自然浮现。
>
> **来源**：王欢 AI 实战分享课后问答（2026-06-18）

---

## 一、核心洞察

很多人卡在 AI 协作的起点：**我不知道我要什么，所以我无法告诉 AI 我要什么**。

王欢的解法：**用魔法打败魔法**。

1. 先让 AI 出一个初版（默认它不合格）。
2. 再让另一个 AI/评审者按“最高标准”挑毛病。
3. 把问题清单扔回给生成 AI，要求修改。
4. 反复迭代 7-8 轮，直到两个 AI 都挑不出大毛病。

> 标准不是想出来的，是迭代出来的。

---

## 二、为什么有效

| 常见困境 | 传统做法 | 王欢做法 |
|:---|:---|:---|
| 我没做过书，不知道书的标准 | 查资料、问专家、憋方案 | 让 AI 出初版 → 让 AI 调研全球最佳实践 → 用最佳实践评审初版 |
| 我不知道这个设计好不好 | 凭感觉判断 | 让多个 AI 分别生成和评审，用对抗迭代逼近标准 |
| 我不知道怎么验收 | 先定义完整 checklist | 在迭代中把“不满意”具象化为可检查的条目 |

核心逻辑：
- src_unknown
- src_unknown
- src_unknown

---

## 三、操作方法

### 3.1 五步循环

```
步骤 1：让 AI 生成初版（不预设质量）
        ↓
步骤 2：让另一个 AI 调研“这件事的全球最佳实践/最高标准”
        ↓
步骤 3：用最佳实践作为评审标准，让 AI 挑初版的毛病
        ↓
步骤 4：把问题清单扔回生成 AI，要求修改
        ↓
步骤 5：重复步骤 2-4，直到 AI 挑不出大毛病，人也挑不出大毛病
```

### 3.2 关键心态

- src_unknown
- src_unknown
- src_unknown

### 3.3 示例：做一本没做过的书

王欢原话场景：团队除了李老师没人做过书，但要把书做出来。

1. 让 AI 出一版书的结构和设计。
2. 让另一个 AI 调研“全球最佳出版社做书的标准”。
3. 用这些标准评审第一版：配色、排版、内容结构、章节逻辑。
4. 把问题扔回 AI 修改。
5. 迭代 7-8 轮，直到方案成熟。

---

## 四、适用边界

| 适用 | 不适用 |
|:---|:---|
| 你完全没做过某类事，标准模糊 | 已有明确行业标准和验收 checklist |
| 创意类、设计类、内容类任务 | 安全关键型、有硬性合规要求的任务 |
| 个人或团队探索新项目 | 需要一次性做对、不能返工的任务 |

---

## 五、常见失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| **对初版太宽容** | 看了一眼觉得“还行”，不再迭代 | 强制默认初版不合格 |
| **评审标准太泛** | 评审 AI 只会说“不够好” | 要求评审 AI 引用具体最佳实践 |
| **迭代没有终止条件** | 永远觉得还能更好 | 设定“连续两轮无重大问题”终止 |
| **只用一个模型** | 评审者和生成者同模型，容易互相附和 | 用不同模型/不同视角做评审 |

---

## 六、与其他卡片的关系

- src_unknown
- src_unknown
- src_unknown
- src_unknown

---

## 七、Action Triggers

| 触发场景 | 第一个动作 |
|:---|:---|
| 我不知道这件事的“好”标准是什么 | 让 AI 先生成一版，再让另一个 AI 调研最佳实践来评审 |
| 我对 AI 输出说不出哪里不对 | 请 AI 自己按最高标准找问题 |
| 新项目没人有经验 | 用 AI 对抗 AI，在迭代中建立标准 |
| 创意方案总是平庸 | 引入外部评审者（另一个 AI/模型/专家） |

---

*基于王欢 2026-06-18 AI 实战分享课后问答整理。*
