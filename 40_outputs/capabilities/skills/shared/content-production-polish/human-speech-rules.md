---
type: skill_reference
name: human-speech-rules
description: Detailed methods and examples for Vikki-human-speech skill (methods #1-15)
author: 老顽童
status: enriched
reviewed_by: pending
updated_at: 2026-06-30
---

# Vikki 讲人话方法库

Use this reference when doing a deep content review or full rewrite.  
Each method follows a 5-part structure: **Problem → Fix → Pattern → Hard vs Human → Why it works.**

> ⚠️ The 15 methods below are the detailed execution guide for the HARD CONSTRAINTS and PREFERENCES defined in SKILL.md. When a constraint is triggered (e.g., "排比不超过3行"), use the corresponding method here (#5) to execute the fix, not just the short rule.

---

## 1. 抽象词落地法

Problem: The draft uses concepts the audience cannot picture.

Trigger words include: 模型、变量、系统、结构、认知、底层逻辑、元能力、判断系统、商业闭环、价值跃迁、推理半径、抓手、赋能、沉淀、内驱力、自驱力、成长型思维、情绪管理、边界感.

How to fix:

1. Keep the concept only if it is necessary.
2. Immediately translate it with "说白了就是".
3. Add one concrete scene.

Pattern:

```text
所谓 X，说白了就是：____。
放到具体场景里，就是：____。
```

Examples:

```text
[AI/商业] Hard: 熟练工的底层逻辑是，我掌握了一套已知动作。
[AI/商业] Human: 熟练工是什么？就是这件事我做过很多遍，所以我手快、熟、出错少。

[亲子教育] Hard: 培养孩子的内驱力，关键是让他体验到自主感。
[亲子教育] Human: 内驱力说白了就是：孩子自己想干这件事。不是你催他干，是他觉得"我要试试"。
比如孩子突然说"我想自己试一下做这个蛋糕"，你别上去帮，让他折腾。搞砸了也没关系，他想干这件事本身，比蛋糕好不好吃重要。

[情感/生活] Hard: 情绪管理的核心是觉察和暂停。
[情感/生活] Human: 情绪管理说白了就是：发火之前能停一秒。你跟老公吵架，话到嘴边想摔门出去——这时候停一下，问自己：我到底气的是什么？这一秒的暂停，比事后冷静半小时管用。
```

Why it works: The audience stops decoding terminology and starts seeing a behavior.

---

## 2. 先场景，后概念

Problem: The draft defines a concept before the audience knows why they should care.

How to fix:

1. Start with a scene the audience has experienced.
2. Show the mistake or tension inside that scene.
3. Name the concept only after the audience has felt the problem.

Pattern:

```text
你有没有遇到过这种情况：____。
表面看是____，其实真正的问题是____。
这就是我说的 X。
```

Examples:

```text
[AI/商业] Hard: AI 时代真正值钱的人，是能在新问题面前重新建模型的人。
[AI/商业] Human: 比如你让 AI 写一条短视频脚本。普通人上来就问：给我一个爆款模板。高手会先问：我要说服谁？他为什么不信？这条视频最后要让他做什么？这就不是套模板了，这是在建模型。

[亲子教育] Hard: 家长要学会放手，让孩子在试错中建立成长型思维。
[亲子教育] Human: 你有没有遇到过这种情况：孩子写作业磨蹭，你一催他就更慢，最后你忍不住替他写了。表面看是你帮他解决了问题，其实真正的问题是——他从此觉得"写作业是妈妈的事"。这就是我要说的"替孩子做"vs"让孩子自己试"。

[生活/健康] Hard: 减肥的核心不是控制热量，而是建立可持续的饮食习惯。
[生活/健康] Human: 你有没有发现，每次减肥前三天特别有动力，第五天就开始馋。表面看是你意志力不够，其实是你的饮食计划太极端了，身体扛不住。这就不是意志力问题，是方法问题。
```

Why it works: The audience understands the model through use, not through definition.

---

## 3. 一句话只放一个判断

Problem: One sentence carries too many layers.

How to fix:

1. Split long sentences.
2. Put one idea in one sentence.
3. Use the next sentence to explain or qualify.

Examples:

```text
[AI/商业] Hard: 你能不能在没有答案的时候，先建立一个可验证的模型。
[AI/商业] Human: 真正厉害的人，不是手里有标准答案。没答案的时候，他也能先搭一个判断框架。然后拿结果去验证：我刚才这么拆，对不对。

[亲子教育] Hard: 孩子的学习动力需要家长在自主性、胜任感和归属感三个维度同时给予支持才能持续发展。
[亲子教育] Human: 孩子要自己想学，有三个条件。第一个：他觉得这事我自己能搞定。第二个：他觉得做这件事有人认可我。第三个：他觉得这件事跟我有关系，不是别人逼我做的。三个缺一个，动力就断了。
```

Why it works: The listener can follow one step at a time.

---

## 4. 用笨例子替代高级解释

Problem: The draft sounds correct but cannot be remembered.

How to fix:

Use examples with four parts:

1. Who is involved?
2. What situation are they in?
3. What exactly did they do?
4. What result or difference appears?

Examples:

```text
[AI/商业] Hard: 会建模的人用 AI，是在让 AI 扩大自己的推理半径。
[AI/商业] Human: 两个人都让 AI 写文案。第一个人说：帮我写 10 条标题。第二个人说：我的用户是刚开始做副业的 35 岁女性，她怕被骗，也怕自己学不会。我要让她相信这件事可以小步开始，你先帮我拆 5 个切入角度。前者是在要答案，后者是在指挥 AI 一起思考。

[亲子教育] Hard: 青少年需要自主决策的机会来发展自我效能感。
[亲子教育] Human: 我朋友的孩子今年初二，之前成绩中等。他妈妈做了一个决定：周末的时间让他自己安排，只给一条底线——不能整天打游戏。这孩子第一周确实打了一整天游戏。但第二周他自己说"这样不行"，开始主动安排学习时间。他妈妈什么都没催，但孩子自己转过来了。

[销售] Hard: 优秀的销售会通过共情建立信任，再引导客户做出购买决策。
[销售] Human: 两个销售卖同一款课。第一个开口就说"我们的课效果特别好"。第二个先问："你现在最大的卡点是什么？是找不到客户，还是找到了但成交率低？"客户一听就觉得：这个人懂我。然后第二个销售才说：针对你这个卡点，我有个方案。第一个是在推销，第二个是在解决问题。
```

Why it works: A "笨例子" gives the audience a mental handle.

---

## 5. 控制排比和"不是……而是……"

Problem: AI drafts often create artificial force by stacking parallel sentences.

**HARD CONSTRAINT (from SKILL.md #1)**:

- Keep continuous parallelism to 3 lines or fewer.
- Use "不是……而是……" no more than 1-2 times in a 1000-character口播.
- Keep the strongest contrast; rewrite the rest as direct speech.

Examples:

```text
[AI/商业] Hard: 不是掌握答案，而是拥有生成答案的能力。不是会用模型，而是会重建模型。
[AI/商业] Human: 答案会越来越便宜。真正贵的是判断：这个问题到底该怎么拆，这个方法换个条件还成不成立。

[亲子教育] Hard: 不是给孩子更多选择，而是让他学会自己做选择。不是替他规划路径，而是让他自己探索路径。
[亲子教育] Human: 很多家长以为"给孩子选择"就是让他自由。但其实关键是：他自己做的选择，哪怕选错了，也比你替他选对的更有价值。因为他自己选过，下次才知道怎么选。
```

Why it works: Sparse contrast feels like judgment. Dense contrast feels like generated copy.

---

## 6. 把"很多人"改成"某一种人"

Problem: "很多人""大多数人""真正高手" are too floating.

How to fix:

Name the audience or behavior more specifically.

Examples:

```text
[AI/商业] Hard: 很多人现在用 AI 的方式，其实还是熟练工思维。
[AI/商业] Human: 很多刚开始用 AI 做内容的人，第一反应不是想用户，而是找提示词。他不问这条内容要解决什么问题，上来就问：有没有现成模板？

[亲子教育] Hard: 很多家长在孩子青春期时会感到焦虑。
[亲子教育] Human: 很多孩子刚上初中的妈妈，最焦虑的不是成绩，而是——孩子突然不爱跟她说话了。放学回来就关门，问一句"今天怎么样"，回你一句"还行"，就没了。

[销售] Hard: 大多数销售失败是因为不够了解客户。
[销售] Human: 很多刚做销售的人，接到客户第一反应是介绍产品。他没想过：这个客户为什么来找我？他现在最头疼什么？他如果不解决这个头疼，他不会买。
```

Why it works: Specific people and actions create credibility.

---

## 7. 建立用户脑内字幕

Problem: The draft assumes the audience understands the jump.

How to fix:

After every abstract claim, ask what the audience is silently asking:

- "什么意思？"
- "跟我有什么关系？"
- "我怎么判断自己有没有这个问题？"
- "那我下一步怎么办？"

Then answer immediately.

Examples:

```text
[AI/商业] Claim: 未来的分水岭，是会不会带着模型使用 AI。
[AI/商业] Brain subtitle: 模型到底是什么？
[AI/商业] Follow-up: 模型不是一个高大上的词。它就是你做判断时的顺序。比如写文案之前，你先判断用户是谁、他卡在哪里、他凭什么信你、最后让他做什么。

[亲子教育] Claim: 青少年需要被看见，而不是被管。
[亲子教育] Brain subtitle: "被看见"到底是什么意思？是夸他？
[亲子教育] Follow-up: 不是夸。是他说了一句话，你真的听了，而且回应了。比如孩子说"今天老师不公平"，你的第一反应不是"老师怎么会不公平呢"，而是"你觉得哪里不公平？"——这就叫被看见。
```

Why it works: It removes the audience's hidden confusion before they drop off.

---

## 8. 保留真人呼吸感

Problem: AI drafts are too complete, clean, symmetrical, and polished.

How to fix:

Use light conversational turns:

- 说白了
- 我举个例子
- 你会发现
- 问题来了
- 这就麻烦了
- 这句话听起来有点抽象，我换个说法

Use them to turn logic, not to fill space.

Examples:

```text
[AI/商业] 这句话听起来有点抽象，我换个说法。
你不是缺 AI 工具，你是缺判断工具。

[亲子教育] 说白了，孩子不想学习，不是因为他懒。
问题来了：他为什么不想学？你有没有问过他，还是你直接开始催了？

[销售] 你会发现，客户说"我考虑一下"，其实不是真的在考虑。
我举个例子：他说"考虑一下"的时候，心里在想的是"你还没说服我"。这时候你催他，没用。你要问他考虑的是什么。
```

Why it works: The speaker appears to be helping the listener understand, not performing an essay.

---

## 9. 用边界替代绝对化

Problem: Strong but overbroad claims hurt trust.

How to fix:

1. Identify whether the claim is fact, judgment, assumption, or experience.
2. Add scope when needed.
3. Avoid turning a useful judgment into a false universal claim.

Examples:

```text
[AI/商业] Hard: 答案会越来越便宜。
[AI/商业] Human: 普通答案会越来越便宜。比如标题、提纲、总结、模板，AI 都能批量给。但结合你业务阶段、用户状态和风险做出来的判断，不会便宜。

[亲子教育] Hard: 放手是最好的教育方式。
[亲子教育] Human: 放手在很多情况下是对的，但不是所有时候。孩子遇到安全风险的时候，你必须管。放手的前提是：这件事搞砸的后果他能承受。如果他承受不了，你还得扶一把。
```

Why it works: The sentence stays sharp but becomes more trustworthy.

---

## 10. 一篇稿子只设一个主对立面

Problem: Too many contrasts make the content scattered.

How to fix:

Choose one main contrast and let the whole draft serve it.

Useful contrasts:

- 套招的人 vs 建模的人
- 要答案的人 vs 拆问题的人
- 讲道理的人 vs 解决用户困惑的人
- 写得漂亮的人 vs 让人信的人
- 替孩子做的人 vs 让孩子自己试的人
- 推销产品的人 vs 解决客户问题的人

Examples:

```text
[AI/商业] Main contrast: 套招的人 vs 建模的人
套招的人问：有没有模板？
建模的人问：这个问题为什么发生？
套招的人让 AI 给答案。
建模的人让 AI 帮他验证判断。

[亲子教育] Main contrast: 替孩子做的人 vs 让孩子自己试的人
替孩子做的人说：你别动，我来。
让孩子自己试的人说：你先试试，搞砸了也没关系。
替孩子做的人，孩子越来越不想做。
让孩子自己试的人，孩子越来越想自己搞定。
```

Why it works: The audience remembers one mental frame.

---

## 11. 让每段承担一个功能

Problem: The draft circles around the same point.

How to fix:

Assign each paragraph one job:

1. Open with a misconception or pain.
2. Explain why the old method fails.
3. Show one concrete example.
4. State the sharper judgment.
5. Handle the audience's objection.
6. Give the next action.

For short video, prefer this order:

```text
误区 → 场景 → 差别 → 判断 → 行动
```

For公众号, prefer this order:

```text
现象 → 问题 → 案例 → 原理 → 边界 → 方法 → 结论
```

Why it works: The draft gains forward movement instead of repeating slogans.

---

## 12. 结尾给行动，不只给升华

**HARD CONSTRAINT (from SKILL.md #2)**: Ending must contain at least 1 executable action. Do not end only with升华.

Problem: The ending sounds powerful but leaves the audience with nothing to do.

How to fix:

End with a question, checklist, or next action.

Examples:

```text
[AI/商业] Weak ending: AI 时代真正的金饭碗，不是会用模型，而是会重建模型。
[AI/商业] Human ending: 所以下次你用 AI，别急着问它要模板。先问自己四个问题：我要解决谁的问题？他现在卡在哪里？影响结果的关键变量是什么？我怎么验证这个判断？这四个问题，比一百个提示词都重要。

[亲子教育] Weak ending: 放手，是给孩子最好的礼物。
[亲子教育] Human ending: 所以今天回家，试试一件事：孩子让你帮忙的时候，先说"你先试试"。如果他搞砸了，别急着批评，先说"你觉得哪里出问题了？下次可以怎么改？"这一句话，比帮他做一百次有用。

[销售] Weak ending: 真正的销售不是卖产品，而是解决问题。
[销售] Human ending: 所以下次见客户，别先开口介绍产品。先问三个问题：你现在最头疼什么？你已经试过什么方法？如果这个问题解决了，对你意味着什么？这三个问题回答完，你自然就知道该卖什么了。
```

Why it works: The audience can immediately use the idea.

---

## Full Rewrite Pattern For AI-Flavored Drafts

Use this pattern when the source draft is abstract but the core insight is useful:

```text
1. 先保留一个最锋利的主判断。
2. 删除重复金句，只留 1-2 句。
3. 把第一个抽象概念改成具体场景。
4. 每个核心概念后面补一个例子或反例。
5. 把长句拆成口播短句。
6. 把密集排比改成问题链或场景链。
7. 补一段"你可能会问"的异议处理。
8. 结尾给用户下一步怎么做。
```

> After completing the 8-step rewrite, run Step 5.5 verification gate from SKILL.md to ensure all 4 core standards pass.

---

## Suggested Diagnostic Labels

Use these labels in reviews:

- 概念太密
- 先讲道理，后讲人
- 口播节奏不自然
- 金句过载
- 排比堆砌
- 例子不足
- 边界不清
- 主线分散
- 只有升华，没有行动
- 有观点，但没有用户场景

---

## 13. 信息 × 情绪配比法（Vikki）

Problem: The draft is either too dense (cognitive overload) or too emotional (no substance). Information alone feels like a lecture; emotion alone feels empty.

How to fix:

1. Set the platform-appropriate information density first:
   - Short video: 1 case or key judgment per second.
   - Live stream: breathing room, one idea per 1-2 minutes.
   - Article: medium density, examples before concepts.
2. Attach one emotional beat to each key information point: surprise,共鸣, or a turning question.
3. Use the rule: **information is the warhead, emotion is the guidance system**.

Pattern:

```text
信息点：____。
情绪落点：____（你是不是也…？/ 说白了… / 问题来了。）
```

Examples:

```text
[AI/商业] Hard: AI 时代真正值钱的是会建模型的人。
[AI/商业] Human: 会建模型的人用 AI，是在让 AI 扩大自己的判断半径。说白了，不是 AI 多厉害，是你得先知道该问什么。很多人一上来就要模板，其实连问题都没拆清楚。

[亲子教育] Hard: 家长要培养孩子的内驱力。
[亲子教育] Human: 内驱力说白了就是孩子自己想干。不是你在后面催，是他自己说"我要试试"。你有没有发现，你越催，他越慢？问题就在这：他把你当成任务发布器了。

[销售] Hard: 好的销售会先诊断客户需求。
[销售] Human: 两个销售卖同一款课。第一个开口就说"我们课特别好"。第二个先问："你现在最头疼的是找不到客户，还是找到了但成交率低？"客户一听就觉得：这个人懂我。你看，同样的产品，第二句话就赢了。

[健康] Hard: 减肥的核心是建立可持续的饮食习惯。
[健康] Human: 每次减肥前三天特别有劲，第五天就开始馋。你不是意志力差，是你的计划太极端了。说白了就是：身体扛不住，它在报复你。

[知识付费] Hard: 做课要找到用户的真实痛点。
[知识付费] Human: 很多人做课是从"我会什么"出发，而不是从"用户为什么睡不着"出发。你晚上失眠的时候，想的是"我要学个模型"，还是"我怎么才能把这件事搞定"？
```

Why it works: Information tells the audience what to know; emotion makes them care. Content without emotion is not remembered; content without information is not trusted.

---

## 14. 短视频 6 维度检查法（大馨）

Problem: Short videos often fail not because the文案 is bad, but because a critical link — positioning, hook, structure, delivery, conversion, or data design — is missing.

How to fix:

Before publishing, run through the 6-dimension checklist:

1. **定位与受众**：一句话说清 IP 定位；谁在看？核心痛点是什么？
2. **选题与钩子**：工具型还是痛点型？前 3 秒有没有"你是不是… + 1 分钟就能… + 方法具体"？
3. **文案结构**：反常识开场 → 痛点共鸣 → 方法论输出 → 案例证明 → 总结 + 转化钩子。
4. **表现力与情绪**：亢奋型还是行动派？有没有屏幕录制/字幕高亮？场景是否建立专业感？
5. **转化设计**：公域 → 关注/私信 → 资料/粉丝群 → 付费，路径是否清晰？
6. **数据特征**：有没有互动设计（"试完回来告诉我"）？有没有争议点？播放量能否估算？

Pattern:

```text
【定位】____（一句话 IP + 受众痛点）
【钩子】____（3 秒公式）
【结构】反常识 → 痛点 → 方法 → 案例 → 转化
【表现力】____（情绪 + 演示 + 场景）
【转化】____（下一步行动）
【数据】____（互动 / 争议 / 估算）
```

Examples:

```text
[AI/商业] 实体获客教学型口播
- 定位：帮高客单专业服务者从"做内容"转向"做生意"的操盘手。
- 钩子：你是不是想做短视频，但根本不知道怎么开始？今天 1 分钟，我教你找到赛道里所有能变现的对标账号。
- 结构：反常识（不是先拍，是先找对标）→ 痛点（不知道谁是真同行）→ 方法（3 步找账号）→ 案例（某客户找到 50 个对标后起量）→ 转化（试完回来告诉我你找到了多少）。
- 表现力：屏幕录制 + 字幕高亮关键数字 + 办公室场景。
- 转化：评论区扣"对标"，领完整 SOP。
- 数据：引导"试完回来告诉我"，低门槛互动。

[亲子教育] 痛点纠偏型
- 定位：帮小学家长解决"孩子写作业磨蹭"问题。
- 钩子：孩子写作业磨蹭，你越催他越慢？不是你脾气差，是你方法错了。
- 结构：反常识（磨蹭不是懒）→ 痛点（催多了孩子把你当任务发布器）→ 方法（3 句话替代催促）→ 案例（朋友孩子从催不动到自己安排）→ 转化（今晚就试）。
- 表现力：居家场景 + 真实语气 + 配合简单动作演示。
- 转化：评论区分享你今晚想试哪一句。
- 数据："越催越慢"是强共鸣点，适合引发评论。

[销售] 创始人 IP 故事型
- 定位：ToB 销售教练，帮销售从"推销产品"转向"解决问题"。
- 钩子：我做了 10 年销售，发现 90% 的人第一句话就错了。
- 结构：缘起（为什么做销售培训）→ 创业折扣点（被客户拒绝 100 次）→ 突破重生（学会先诊断）→ 方法论（3 个问题开场）→ 价值观（销售是传递价值）。
- 表现力：办公室书架背景 + 真诚叙事 + 适度停顿。
- 转化：私信"诊断"，领销售开场问题清单。
- 数据："第一句话就错了"是争议点 + 好奇点。

[健康] 通用可移植公式
- 定位：帮上班族解决"反复减肥失败"。
- 钩子：减肥失败不是你意志力差，是你的计划太反人类。
- 结构：行业痛点（反复失败）→ 概念升级（不是减热量，是建习惯）→ 经典案例（某学员 3 个月不节食减 8 斤）→ X 步框架（3 个饮食替换法）→ 万能公式（吃饱 + 替换 + 记录）。
- 表现力：厨房场景 + 实物展示 + 轻松语气。
- 转化：评论区扣"替换"，领 21 天饮食替换表。
- 数据："不节食"是贪婪开关 + 争议点。

[知识付费] 痛点型钩子
- 定位：帮知识博主做课变现。
- 钩子：你的课卖不动，可能不是内容不好，是你把课做成了"知识百科"。
- 结构：反常识（好课不是内容多）→ 痛点（用户买课是为了解决问题，不是为了学习）→ 方法（1 课 1 结果）→ 案例（某老师从 50 节缩到 8 节，销量翻 3 倍）→ 转化（点击下方，领做课自检表）。
- 表现力：书桌前讲解 + 白板演示课程结构对比。
- 转化：点击主页链接领资料。
- 数据："知识百科"是身份攻击 + 好奇点。
```

Why it works: Short video is a system, not just文案. The 6-dimension checklist prevents fixing words while ignoring the conversion path.

---

## 15. 人性开关植入法（大馨 + Vikki）

Problem: The draft has information and structure, but the audience still does not act or share. Rational argument changes belief; emotional triggers change behavior.

How to fix:

Plant at least one of the 5 human switches at the key decision point:

1. **贪婪**：占便宜、稀缺、专属感（"前 50 名""免费领""错过再等一年"）。
2. **恐惧**：错过、落后、被比较（"你再不开始，同行已经跑远了"）。
3. **归属**：同类、圈子、身份认同（"做 IP 的人一看就懂""我们这种人"）。
4. **好奇**：信息差、反常识、未解之谜（"很多人都不知道…""真正的秘密是…"）。
5. **行动**：立刻试用、零风险、低门槛（"今晚就试""试完回来告诉我""先加微信领资料"）。

Pattern:

```text
痛点 + 开关 + 下一步
```

Examples:

```text
[AI/商业] 贪婪 + 行动
"这 3 个提示词模板，我自己团队内部用了半年。今天免费分享，前 100 人扫码领。领完今晚就试一条，明天告诉我效果。"

[亲子教育] 归属 + 行动
"做妈妈的都懂：孩子写作业的时候，最难的不是孩子，是我们自己。今晚试试这句话——'你先试，搞砸了我陪你'。评论区告诉我孩子的反应。"

[销售] 恐惧 + 好奇
"你有没有算过，你今年因为'我再考虑一下'丢了多少单？真正的问题不是客户犹豫，是你没问到他犹豫的是什么。下一单你试试这个问法…"

[健康] 归属 + 恐惧
"反复减肥的人都有一个共同错觉：觉得自己意志力差。其实不是。是你用的方法本来就不是给人长期坚持的。换个方法，身体会自己配合你。"

[知识付费] 好奇 + 贪婪
"为什么有些老师的课只有 8 节，却卖得比 80 节的还好？因为他们做对了一件事：把课做成了'结果承诺'，不是'知识清单'。想要这个做课框架的，评论区扣'结果'。"
```

Hard vs Human:

- Hard: "点击链接购买课程。"
- Human: "如果你也想知道为什么同样是做课，有人 8 节卖爆、有人 80 节没人买——评论区扣'结果'，我把框架发你。"

Why it works: People share and buy when an emotional switch is flipped. The switch must be tied to a clear next step, or the energy dissipates.

---

## Mini Scoring Rubric（Optional — add when user asks for score or when comparing versions）

```text
听得懂: 1-5
像人说: 1-5
信得过: 1-5
有转化: 1-5
AI味风险: 低 / 中 / 高
```

Do not let scoring replace revision. Always provide the actual improved wording.
