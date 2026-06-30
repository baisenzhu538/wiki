---
name: Vikki-human-speech
description: Review and rewrite Chinese self-media content so it sounds like a real person instead of AI-generated copy. Use when checking or improving口播稿、短视频脚本、直播话术、公众号文章、小红书文案、销售文案, especially for problems like抽象难懂、AI味重、排比堆砌、概念太密、说教感强、没有场景、没有例子、转化弱, or when the user asks to"讲人话""去AI味""改得口语化""让用户听懂""让表达更有商业价值"" Vikki-human-speech".
version: 2.0.0
author: 老顽童
status: enriched
reviewed_by: pending
updated_at: 2026-06-30
---

# Vikki 讲人话检查

## Core Standard

Use this skill to make content satisfy six standards:

1. **听得懂**: Translate abstract concepts into scenes, examples, comparisons, and plain words.
   - Threshold: No more than 3 untranslated abstract words in the full text; each must have a "说白了就是" translation. At least 2 concrete scenes or conversations.
2. **听得下去**: Make the rhythm sound like speech, with short sentences, pauses, turns, and occasional natural filler.
   - Threshold: No continuous 3 sentences over 20 characters each; at least 2 oral transitions (说白了 / 你看 / 我举个例子 / 这就麻烦了).
3. **信得过**: Separate facts, judgments, assumptions, and boundaries. Do not exaggerate to make language sharper.
   - Threshold: At least 2 boundary markers ("我的判断是" / "这只是我观察的" / "很多人会以为……但实际情况是").
4. **用得上**: Give the audience a concrete judgment, action, question, or next step.
   - Threshold: Ending contains at least 1 executable action (checklist / question / decision framework / next step).
5. **记得住**: Make the core insight sticky through controlled information density, one memorable contrast, and rhythm.
   - Threshold: The content has **1 clear main contrast** (e.g., 套招的人 vs 建模的人); information density matches the platform; and at least 1 phrase or scene the audience can repeat after one listen.
6. **愿意传**: Give the audience an emotional trigger and a low-friction sharing reason.
   - Threshold: The content contains at least 1 of — a recognizable pain point ("你是不是也…"), a curiosity gap ("很多人都不知道…"), a social-identity signal ("做XX的人一看就懂"), or an interactive CTA ("试完回来告诉我…").

Do not merely make the copy simpler. Preserve useful sharpness, business judgment, and conversion intent.

## Default Workflow

When the user provides a draft, perform this sequence:

### Step 1: State the main diagnosis

Say whether the draft is mainly too abstract, too AI-like, too repetitive, too article-like, too soft, or too far from the audience.

### Step 1.5: Diagnosis coverage self-check（HARD CONSTRAINT）

Before proceeding, verify your diagnosis covers all 7 Quick Diagnosis Checklist signals:

- [ ] Abstract density — checked
- [ ] Scene absence — checked
- [ ] AI rhythm — checked
- [ ] Concept-first writing — checked
- [ ] Gold-sentence overload — checked
- [ ] Weak boundary — checked
- [ ] No next step — checked

Output: "7 项中 N 项命中，M 项不适用。主诊断基于命中的 K 项。"

**Do not skip this step.** If you miss signals, your diagnosis is incomplete and downstream fixes will be partial.

### Step 2: Identify the core argument

Extract the one sentence the audience should remember. If the draft has multiple competing arguments, choose the strongest one and say what was deprioritized.

Self-check: Is the core argument singular? If you listed more than one, pick the strongest and mark others as "deprioritized."

### Step 3: Mark non-human-sounding parts

Point out representative phrases or sentence types, not every minor wording issue.

Self-check: Are these representative patterns, not nitpicks? Each marked item should be a structural problem, not a single word choice.

### Step 4: Explain why they fail

Tie each problem to audience comprehension, trust, rhythm, or conversion. **This step must appear in the output.** Skipping the causal chain means the user only sees "what was changed" but never understands "why."

### Step 5: Rewrite with intent

Provide a corrected version that is clearer, more oral, more concrete, and more commercially useful.

### Step 5.5: Rewrite verification gate（HARD CONSTRAINT）

After rewriting, verify the corrected text passes all 6 core standards:

- **听得懂 check**: Full-text abstract words ≤ 3, each with translation; ≥ 2 concrete scenes.
- **听得下去 check**: No 3 consecutive sentences > 20 chars; ≥ 2 oral transitions.
- **信得过 check**: ≥ 2 boundary markers separating fact/judgment/assumption.
- **用得上 check**: Ending has ≥ 1 executable action, question, or checklist.
- **记得住 check**: 1 main contrast is explicit; information density matches the platform; at least 1 phrase/scene is repeatable.
- **愿意传 check**: At least 1 emotional trigger or sharing hook is present (pain point / curiosity gap / identity signal / interactive CTA).

If any standard fails, **go back to Step 5 and rewrite again. Do not proceed with a failing version.**

### Step 6: Give reusable rules

End with the 3-6 most important writing rules the user should carry into the next draft.

---

Keep questions minimal. Ask only when a missing fact changes the judgment materially, such as target audience, platform, product, offer, compliance boundary, or desired action.

## Quick Diagnosis Checklist

Check the draft against these signals:

- **Abstract density**: Does it pile up words like模型、变量、结构、认知、系统、底层逻辑、价值、闭环 without translation?
- **Scene absence**: Is there no具体人、具体场景、具体动作?
- **AI rhythm**: Are there dense parallel sentences, repeated "不是……而是……", symmetrical clauses, or overly polished transitions?
- **Concept-first writing**: Does it define concepts before showing a problem the audience recognizes?
- **Gold-sentence overload**: Does every sentence try to be a slogan, leaving no breathing room?
- **Weak boundary**: Are facts, opinions, assumptions, and experiences mixed together?
- **No next step**: Does the audience understand the point but not know what to do with it?

For detailed methods and examples, read `references/human-speech-rules.md` when a user asks for a deep review, a full rewrite, or a reusable content standard.

## Output Format

**Standard format（all fields required）：**

```markdown
**结论**「必填」一句话判断这篇稿子的最大问题和最值得保留的地方。

**主要问题**「必填」至少 2 个，每个必须包含三段式：
1. 问题名：原句/现象 → 为什么不像人话（因果链）→ 怎么改
   ⚠️ 禁止只写"怎么改"而跳过因果链。

**修改版**「必填」给一版可直接使用的改稿。

**以后写同类稿子的规则**「必填」3-6 条最关键规则。
```

**Compact format（use for single-problem quick fixes）：**

```markdown
**核心问题**「必填」
**改法**「必填」
**改后版本**「必填」
```

**Optional fields:**
- Mini Scoring Rubric（听得懂 / 像人说 / 信得过 / 有转化 / 记得住 / 愿意传 1-5 + AI味风险 级别）— add when the user asks for a score or when comparing multiple versions.

## HARD CONSTRAINTS vs PREFERENCES

### HARD CONSTRAINTS（违反 = 不合格）

1. **排比上限**：连续排比不超过 3 行。"不是……而是……"不超过 2 次 / 千字。
2. **结尾行动**：结尾必须包含至少 1 个可执行行动（清单 / 问题 / 判断框架 / 下一步）。不得仅以升华结束。
3. **保留锋利度**：保留原文锋利观点和商业意图。不得扁平化为中性总结。
4. **因果链不可跳过**：每个主要问题必须包含"原句 → 为什么 → 怎么改"三段式。只写改法不写原因 = 不合格。
5. **诊断覆盖率**：Step 1.5 必须逐项确认 7 个诊断信号是否命中。不可跳过。

### PREFERENCES（建议遵循，可按场景调整）

1. Prefer concrete examples over elegant abstractions.
2. Prefer one strong contrast over many scattered contrasts.
3. Use口语化 transitions（说白了 / 我举个例子 / 问题就在这 / 你可能会问），but only when they help the listener turn a corner.
4. Keep rhetorical devices sparse overall. One strong "不是……而是……" is better than five.
5. Preserve the user's position and business intent as a default stance.

> 💡 上述原则的详细执行方法、正反示例和"Why it works"参见 `references/human-speech-rules.md`（方法 #1-15）。

## Gotchas（执行中模型易犯的错误）

1. **改写≠变温和**：模型可能把"讲人话"理解为"把尖锐判断改成温和观点"。必须保留原文的商业锋芒。如果原文有明确立场，改后版本必须保留同样立场，只是表达方式更易懂。
2. **用抽象词解释抽象词**：模型可能用"另一个抽象词解释抽象词"而非"具体场景+行为"。发现此类情况必须回到方法 #1（抽象词落地法），强制要求"说白了就是 + 具体场景"。
3. **平台惯性**：模型可能把公众号风格套用到短视频口播。每个平台必须匹配 Platform Notes 中的对应策略。短视频 = 短句强节奏；直播 = 信任+异议处理；公众号 = 可有更多推理；小红书 = 痛点先行。
4. **升华依赖症**：模型结尾倾向使用金句升华而非给行动。Step 5.5 的"用得上"检查会拦截这个问题，但也要在改写时主动避免。
5. **排比审美**：模型天生喜欢排比和"不是……而是……"。必须逐句扫描控制用量（HARD CONSTRAINT #1）。

## Platform Notes

### 短视频口播
- **大馨 6 维度检查清单**：定位与受众 → 选题与钩子 → 文案结构 → 表现力与情绪 → 转化设计 → 数据特征。
- **前 3 秒钩子**：痛点直击（"你是不是…"）+ 结果承诺（"1 分钟就能…"）+ 方法具体（"找到全网同行"）。
- **结构公式**：反常识开场 → 痛点共鸣 → 方法论输出 → 案例证明 → 总结 + 转化钩子。
- **信息密度**：每秒 1 个案例或 1 个关键判断；紧凑，不绕弯。
- **4 个可复用脚本模板**（按需填空）：
  1. **实体获客教学型口播**：【钩子】你是不是想做XX但不知道怎么开始？今天X分钟，我教你找到赛道里所有能变现的对标账号。→【方法论】第一步…第二步…第三步…→【转化】试完回来告诉我你找到了多少。
  2. **痛点纠偏型万能公式**：行业痛点（危机感）→ 概念升级（信息差）→ 经典案例（降低理解）→ X步框架（工具价值）→ 万能公式（收藏理由）。
  3. **创始人 IP 故事型公式**：缘起（为什么做）→ 创业折扣点 → 突破重生 → 教育理念 → 方法论 → 价值观。适用于教育、健康、美业、留学、高端服务、知识付费。
  4. **通用可移植公式**：行业痛点 → 概念升级 → 经典案例 → X步框架 → 万能公式。

### 直播话术
- 节奏比短视频慢，重点在**信任建立 + 异议处理 + 即时互动**。
- 每 3-5 分钟设计一次"用户可能会问"的转折，把 lecture 变成对话。
- 转化路径要清晰：公域观看 → 关注/私信 → 领取资料/进粉丝群 → 付费课程或陪跑。
- 保留真诚人设，避免"全程高光"；适当暴露真实困境更容易建立信任。

### 小红书文案
- **痛点先行**：第一句必须让读者觉得"这说的就是我"。
- **情绪标签**：用"姐妹们""谁懂啊""救命"等社区语气降低距离感。
- **信息克制**：一篇笔记讲透 1 个痛点 + 1 个方法 + 1 个可执行下一步。
- **结尾互动**：用低门槛问题引导评论（"你们有没有遇到过这种情况？""评论区告诉我"）。

### 公众号文章
- 允许更多结构和推理，但**案例必须在概念之前**。
- 推荐结构：现象 → 问题 → 案例 → 原理 → 边界 → 方法 → 结论。
- 适当使用小标题、引用、列表，帮助读者在深度阅读中定位。
- 结尾除了行动，还可以给出"如果只能记住一句话"的核心摘要。

### 销售文案
- **先诊断，后卖药**：先问客户卡点和已尝试的方法，再引出方案。
- **5 个人性开关**：贪婪（占便宜/稀缺）、恐惧（错过/落后）、归属（同类/圈子）、好奇（信息差）、行动（立刻试用/零风险）。
- **信任三件套**：方法背书 + 步骤清晰 + 学员/客户案例证明。
- **CTA 设计**：一个主行动 + 一个低门槛 fallback（"先加微信领资料"）。

### 跨域提示
- AI/商业、亲子教育、销售、健康、知识付费 5 个高频域的示例参见 `references/human-speech-rules.md` 方法 #13-#15。
