---
name: Vikki-human-speech
description: Review and rewrite Chinese self-media content so it sounds like a real person instead of AI-generated copy. Use when checking or improving口播稿、短视频脚本、直播话术、公众号文章、小红书文案、销售文案, especially for problems like抽象难懂、AI味重、排比堆砌、概念太密、说教感强、没有场景、没有例子、转化弱, or when the user asks to"讲人话""去AI味""改得口语化""让用户听懂""让表达更有商业价值"" Vikki-human-speech".
---

# Vikki 讲人话检查

## Core Standard

Use this skill to make content satisfy four standards:

1. **听得懂**: Translate abstract concepts into scenes, examples, comparisons, and plain words.
   - Threshold: No more than 3 untranslated abstract words in the full text; each must have a "说白了就是" translation. At least 2 concrete scenes or conversations.
2. **听得下去**: Make the rhythm sound like speech, with short sentences, pauses, turns, and occasional natural filler.
   - Threshold: No continuous 3 sentences over 20 characters each; at least 2 oral transitions (说白了 / 你看 / 我举个例子 / 这就麻烦了).
3. **信得过**: Separate facts, judgments, assumptions, and boundaries. Do not exaggerate to make language sharper.
   - Threshold: At least 2 boundary markers ("我的判断是" / "这只是我观察的" / "很多人会以为……但实际情况是").
4. **用得上**: Give the audience a concrete judgment, action, question, or next step.
   - Threshold: Ending contains at least 1 executable action (checklist / question / decision framework / next step).

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

After rewriting, verify the corrected text passes all 4 core standards:

- **听得懂 check**: Full-text abstract words ≤ 3, each with translation; ≥ 2 concrete scenes.
- **听得下去 check**: No 3 consecutive sentences > 20 chars; ≥ 2 oral transitions.
- **信得过 check**: ≥ 2 boundary markers separating fact/judgment/assumption.
- **用得上 check**: Ending has ≥ 1 executable action, question, or checklist.

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
- Mini Scoring Rubric（听得懂 / 像人说 / 信得过 / 有转化 1-5 + AI味风险 级别）— add when the user asks for a score or when comparing multiple versions.

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

> 💡 上述原则的详细执行方法、正反示例和"Why it works"参见 `references/human-speech-rules.md`（方法 #1-12）。

## Gotchas（执行中模型易犯的错误）

1. **改写≠变温和**：模型可能把"讲人话"理解为"把尖锐判断改成温和观点"。必须保留原文的商业锋芒。如果原文有明确立场，改后版本必须保留同样立场，只是表达方式更易懂。
2. **用抽象词解释抽象词**：模型可能用"另一个抽象词解释抽象词"而非"具体场景+行为"。发现此类情况必须回到方法 #1（抽象词落地法），强制要求"说白了就是 + 具体场景"。
3. **平台惯性**：模型可能把公众号风格套用到短视频口播。每个平台必须匹配 Platform Notes 中的对应策略。短视频 = 短句强节奏；直播 = 信任+异议处理；公众号 = 可有更多推理；小红书 = 痛点先行。
4. **升华依赖症**：模型结尾倾向使用金句升华而非给行动。Step 5.5 的"用得上"检查会拦截这个问题，但也要在改写时主动避免。
5. **排比审美**：模型天生喜欢排比和"不是……而是……"。必须逐句扫描控制用量（HARD CONSTRAINT #1）。

## Platform Notes

- **短视频口播**: Use shorter sentences, stronger first 3 seconds, visible scene examples, and fewer nested explanations.
- **直播话术**: Add trust-building, objection handling, and conversational turns. Avoid lecture tone.
- **公众号文章**: Allow more structure and reasoning, but still use examples before dense concepts.
- **小红书文案**: Start from a recognizable pain point or experience. Avoid grand theory unless immediately grounded.
