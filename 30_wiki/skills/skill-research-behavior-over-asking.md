---

id: skill-research-behavior-over-asking
title: 行为证据重于口头证据
type: skill
status: enriched
confidence: 0.80
trust_level: high
language: zh-CN
domain:
- research
- yitang
source_person: 王语嫣
source_context: yitang 域 152 张 case 卡跨案例合成，洞察 1
source_refs:
- 60_feedback/audit/synthesis_yitang.md
- 30_wiki/dk/dk-yitang-behavior-over-asking.md
created_at: "2026-06-25"
updated_at: "2026-06-25"
author: 王语嫣
reviewed_by: 欧阳锋
review_date: "2026-06-25"
related:
  - '[[tool-yitang-18-strategy-tool-mapping]]'
  - '[[yitang-research-domain-digest]]'
  - '[[dk-research-triangulation-stop-rule]]'
  - '[[tool-yitang-research-cross-validation]]'
  - '[[skill-research-triangulation-stop-rule]]'
- "[[dk-yitang-behavior-over-asking]]"
- "[[yitang-research-domain-digest]]"
- "[[tool-yitang-user-interview-5steps]]"
- "[[yt-research-user-jtbd]]"
- "[[framework-demand-iceberg]]"
diagnostic_signals:
  - signal: "访谈总结里全是'用户说''用户认为'，很少出现'用户做了什么'"
    framework_lens: 行为证据优先
    follow_up_question: "你能复述用户最近一次遇到该问题的具体场景和行为吗？"
  - signal: "团队把'访谈对象点头'当成'需求被验证'"
    framework_lens: 愿望 vs 行为
    follow_up_question: "用户为这个需求付过费吗？最近一次花了多少？"
  - signal: "远程访谈后无法还原现场语境"
    framework_lens: 现场语境缺失
    follow_up_question: "能否让用户展示订单、聊天记录、App 使用界面或相册截图？"
---

# 行为证据重于口头证据

> **Burn line**：用户嘴里说的多是「愿望」，真实行为里才藏着「需求」。

---

## 何时使用

- 验证新品类或新场景的需求存在性
- 远程用户访谈中需要还原真实使用语境
- 产品方向争议时，用行为证据替代「我觉得用户需要」
- 与 `[[tool-yitang-user-interview-5steps]]`、`[[yt-research-user-jtbd]]` 组合使用

---

## 核心框架：行为证据优先的访谈 SOP

| 步骤 | 动作 | 示例问题 |
|:---|:---|:---|
| 1. 场景锚定 | 让用户描述最近一次遇到该问题的具体情境 | 「上次你遇到这个问题是什么时候、在哪里？」 |
| 2. 替代方案回溯 | 追问当前和过去用过的解决方案 | 「你当时先试了什么？为什么没继续用？」 |
| 3. 付费行为验证 | 把问题落到真实支出或时间投入 | 「你为这个事付过费吗？最近一次花了多少？」 |
| 4. 现场证据补充 | 索要照片、录屏、订单记录、聊天记录 | 「能给我看看你手机里的相关记录吗？」 |
| 5. 交叉验证 | 用 2-3 个用户的同类行为故事互证 | 寻找重复出现的场景、替代方案和痛点 |

---

## 远程访谈还原现场语境的技巧

- 让用户打开相册/购物记录/App 使用记录，边看边说
- 要求用户描述「当时周围还有什么人、在做什么、前 10 分钟在做什么」
- 用「如果明天这个问题解决了，你今天会怎么做？」把未来愿望拉回当下行为

---

## 快速检查单

- [ ] 访谈问题以「你最近一次是怎么做的？」开头，而不是「你会……吗？」
- [ ] 每个问题后追问「当时还试过什么？为什么没继续？」
- [ ] 记录了用户付费/时间投入的具体行为
- [ ] 索要了至少一个现场证据（截图、订单、聊天记录）
- [ ] 访谈总结中「用户做了什么」不少于「用户说了什么」

---

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 把愿望当需求 | 用户说会买，但实际没有任何付费/使用痕迹 | 强制追问「现在怎么解决」「付过费吗」 |
| 误读行为 | 用户现在用某方案是因为「没得选」而非满意 | 同时问「为什么不满意」「什么情况下会换」 |
| 过度追求行为证据 | 早期探索阶段就蹲点一周，拖慢节奏 | 先用 3-5 个深度行为访谈验证方向 |
| 线上行为当真实意图 | 点击/搜索受算法推荐驱动 | 线上行为与 JTBD 故事互证 |

---

## 适用边界

- **适用**：需求存在性尚未验证的早期调研；用户有真实替代方案可观察；访谈对象确实是目标用户
- **不适用**：已有大规模用户行为数据只需统计验证；完全创新品类用户尚未形成任何解决行为；样本偏差严重

---

## 行动触发器

- 当要写访谈提纲时 → 把所有「你会……吗？」改成「你最近一次是怎么做的？」
- 当访谈对象说「想要」时 → 追问「现在怎么解决」「付过费吗」
- 当远程访谈结束时 → 索要一个现场证据

---

## 关联卡片

- `[[dk-yitang-behavior-over-asking]]`：暗知识卡，含更多案例
- `[[tool-yitang-user-interview-5steps]]`：用户访谈五步法
- `[[yt-research-user-jtbd]]`：JTBD 故事公式
- `[[framework-demand-iceberg]]`：需求冰山模型

---

*作者：王语嫣 | 复核：欧阳锋 | 来源：yitang 域跨案例合成报告*
