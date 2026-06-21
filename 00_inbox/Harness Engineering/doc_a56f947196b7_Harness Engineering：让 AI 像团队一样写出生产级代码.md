# Harness Engineering：让 AI 像团队一样写出生产级代码

> 一行提示词，四小时后交付一个能跑的应用。这不是魔法，是工程。
> 
> 

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODU2NGQzZTdhMWVmM2M3MjU0NjY0Mzc0ODFhOWM5MzVfNTAzMjQ1YjM0OGQyZGNhNWM2ODZiM2Q1OTBlYTY3NTBfSUQ6NzY1MzY3NjkzMjMyMzY5MTQ3NF8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：多个专业 Agent 围绕同一个目标协作，质量在分工与对抗中涌现*

---

## 为什么单个 AI Agent 不够用？

你大概率经历过这一幕：兴冲冲地让 Claude 或 GPT 帮你写个应用，它刷刷刷吐出几百行代码，缩进工整、命名漂亮，看上去无懈可击。然后你一运行——登录跳不过去，刷新就报错，随便输个空值整个页面白屏。

代码"看起来对"，但它根本没打算认真跑给你看。

很多人第一反应是怪模型不够聪明。其实不是。问题出在**架构**上，而不是脑子上。

想想我们让 AI 干的事：写代码 → 自我检查 → 修改。这等于让同一个大脑既当作者又当批判者。人都做不到的事，凭什么指望模型做到？它会下意识替自己的选择辩护，而不是冷静地把自己的破绽摊开来看。

**Harness Engineering** 要拆掉的，正是这堵"自己审自己"的墙。

---

## 什么是 Harness？

先别急着把 Harness 当成又一个"AI 编程工具"。它更像一种思路——一套跑在 Claude Code 里的多 Agent 编排系统，灵感直接来自机器学习里的 **GAN（生成对抗网络）**：

- **生成器（Generator）** 负责创作

- **判别器（Discriminator）** 负责攻击和批判

- 两者你来我往地对抗，质量就在拉扯中螺旋上升

GAN 只有两个角色。Harness 走得更远——它把整支**软件工程团队**搬了进来，每个角色各司其职，谁也别想糊弄过去：

看明白这张表，你就抓住了 Harness 的灵魂：它信奉的不是"找一个更强的模型"，而是"用一套更好的分工"。质量不是某个天才写出来的，是被一群挑剔的角色逼出来的。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGIxMjYwMzk2OTI3ZWExODRlNzUzOWJkMzIwNGUxMjNfOTJkYzA1OTNmMGEwNzhiZjg3NzQ2MjUyZTk0ZGEzOTdfSUQ6NzY1MzY3NjkyODUyMzg2NTA0N18xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：7 个角色的层级关系——Planner 在顶层规划，Generator 实现，4 个 Evaluator 并行评审，Integration Tester 在每个 Sprint 边界做回归*

---

## 核心架构：GAN 启发的对抗设计

Harness 的对抗不是一招鲜，而是层层加码的四道关。每一道都堵住前一道堵不住的漏。

### 1\. 角色分离

最根本的一刀：Generator 永远不许评价自己写的代码。生成归生成，评估归评估，由完全独立的 Agent 接手。这样一来，"自我辩护"那点小心思根本没有滋生的土壤——写的人和挑刺的人，压根不是同一个。

### 2\. 多角度同时评审

光有一个挑刺的还不够。每一轮迭代，**4 个 Evaluator 同时上场**，从四个互不重叠的视角往代码里扎：

快乐路径验证（功能测试）

\+

主动攻击（对抗测试）

\+

跨模型代码审查（Codex）

\+

跨模型架构审查（Gemini）

一个角度漏掉的，另一个角度大概率能逮住。

### 3\. 模型异构

这一层很关键。Codex 来自 OpenAI，Gemini 来自 Google，两者是完全不同的模型家族，训练数据分布不一样，盲区自然也不重合。换句话说——一个模型拍胸脯说"没问题"的代码，另一个可能一眼就看出毛病。**单一审查员的盲点，靠不同血统的审查员互相照亮。**

### 4\. 主动攻击 vs 被动审查

普通的代码审查是"读一遍，提点意见"。对抗测试员（Adversarial Tester）不这么干——它的成功标准很赤裸：**找到 bug**。找不到，就算它失职。

于是它会真刀真枪地造恶意输入：空值、超长字符串、SQL 注入字符、并发竞争条件……专挑你没想到的地方下手。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGMzMjBmYWUyNDVmMTk2NjQ2Y2EzNWIwYTMzYmM0NTNfNzUxYTFlZjBkNmYzYTkzYjgwMWE0MGU4MjI2YTUwMTJfSUQ6NzY1MzY3NjkyNjU1MjU0MjM5NF8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：代码经过四层过滤——快乐路径验证、主动攻击探测、跨模型代码审查 A、跨模型架构审查 B，每层都会将不合格代码"筛出"，只有全部通过才能到达底部*

---

## 整体工作流

一次完整的 Harness 构建，要走完六个阶段：

Phase 0: 预检与初始化

↓

Phase 1: 规划（Planner / Opus 运行一次）

↓

Phase 1\.5: 技术栈选型

↓

Phase 1\.6: 主验收计划

↓

Phase 2\-5: Sprint 循环（可多次）

↓

Phase 5\.5: 抛光冲刺（自动插入）

↓

Phase 6: 交付管道（文档 \+ 克隆测试 \+ 审计）

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=OGY2MzUyOGZmZjI1ODlkZWU1MGNlNGJiMGQ0NmFhNTRfYThkMjAyZmFmMTZiZmFiZDk0MzEwNGJjOWNlYTU3M2RfSUQ6NzY1MzY3NjkzNTE1OTE1NTkxMV8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：六个阶段从初始化流向交付，Sprint Loop 是整个系统的核心引擎——循环对抗直到质量达标*

### Sprint 内部循环：对抗的核心

外面六个阶段是骨架，真正的发动机藏在每个 Sprint 内部——一个不达标就不放行的**对抗迭代循环**：

Generator 写代码（全新实例，从 checkpoint 重建状态）

↓

冒烟检查（确保应用能启动）

↓

4 个 Evaluator 并行评审 ──────────────┐

↓                                  │

合并评估报告                           │

↓                                  │

PASS → 下一 Sprint              FAIL → 生成修复简报

↓

新 Generator 实例重新实现

（最多 5 次迭代）

这里有个反直觉、却特别聪明的设计：Generator 被当成"**牲口而非宠物**"。每一轮迭代都换一个全新实例，从 checkpoint 文件重新加载状态，而不是让同一个 Agent 一直跑下去。

为什么这么狠？因为一个连续工作的 Agent，会对自己写下的烂代码产生"情感依附"——舍不得删，总想修修补补圆回来。换个新实例，它没有包袱，看到烂代码只会觉得"这谁写的，重来"。

---

## 评分体系：锚定 1\-5 分制

Harness 故意用 **1\-5 分制**，而不是看起来更精细的 1\-10 分制。理由特别实在：

> LLM 评估者在 1\-10 分制下会集中打 7\-8 分（"中间偏好"），抹平了迭代间的进步差异。1\-5 分制配合**明确的语义锚点**，迫使评估者引用具体标准。
> 
> 

说白了，分档少了、每档含义又写得死死的，评估者就没法和稀泥，只能掰着具体标准给分。

**通过门槛（所有维度统一）：**

- 任何维度不低于 3 分

- 最终加权平均 ≥ 4\.0 分（取 Codex 和 Gemini 评分的**较低值**）

- 零个 CRITICAL 级对抗发现

注意那个"取较低值"——这是防止两个评审里有一个心软给高分，把另一个的低分"冲平"。短板说了算，木桶原理。

至于权重，会按项目类型（前端应用 / 后端 API / CLI 工具 / 数据可视化 / 游戏）自动调整 rubric 的各维度比重，不搞一刀切。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ZGQxZDQyNDQ3MjllNzgxODkxMmQ4YjE3ODI5Mjc3ZThfYzgwMWQ2MTAwZGI2ZTg3NmNlNDdhYTNiZmRjZWE5NDZfSUQ6NzY1MzY3NjkyODY5MTU3MTY1MF8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：五维雷达图（功能性、设计质量、原创性、健壮性、测试覆盖\)，中心金色环为 4\.0 通过线，两侧分别是 Codex 和 Gemini 的独立评分柱——最终取较低值，不允许高分"冲平"低分*

---

## 模型分工：为什么这样选？

不同的活，交给不同的模型干，钱花在刀刃上：

规划和最终把关用最贵最强的 Opus，但都只跑一次；高频迭代的写代码、跑测试交给性价比更高的 Sonnet；评审则刻意跨家族，让三种不同血统的模型互相校准。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YmZjYTI4NWM1NjI3MzhjYmFiZjViNDE1MDk0MGM4YjZfMjA1YmE4MzU1M2QwMzQ3Mzk0ZWI2ZTNjYzE1N2Q5MTFfSUQ6NzY1MzY3NjkyNTY0NjQyNTI2OF8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：三台望远镜（代表 Anthropic / OpenAI / Google 三个不同训练分布的模型族\)从不同角度聚焦同一份代码，三角测量消除各自盲区*

---

## 美学与品味：不是事后的装饰

很多 AI 生成的应用一眼就能认出来——通用渐变背景、千篇一律的紫色按钮、满屏 lorem ipsum。Harness 不接受这种"AI 烂活"，它把美学当成贯穿全程的**持续压力**，而不是临交付前刷的一层漆：

1. **Planner 产出品味参考**：如"感觉像 Linear 遇上 Notion"，具体描述风格锚点

2. **技术栈选型时考虑美学**：Tailwind \> 原始 CSS，shadcn/ui \> Material UI 默认样式

3. **Generator 每次生成前读 design\-taste\.md**：风格导向从第一行代码开始生效

4. **对抗测试员检查"AI 烂活"特征**：通用渐变背景色、默认 Material 颜色、lorem ipsum 占位文字

5. **抛光冲刺**：交付前自动插入一个额外 Sprint，专注微交互、空状态设计、排版节奏

6. **美学评审员（Opus）做最终判断**：整体评分 \< 4\.0/5 触发再次抛光

从第一行代码到最后一次评审，"好不好看"始终是一道硬指标，而不是有空再说的加分项。

---

## 文件系统：Harness 的"工作台"

Harness 干活时所有的草稿、笔记、状态快照都摊在 `.harness/` 目录里（自动进 \.gitignore，不污染仓库）；只有真正的交付物，才会提交到项目根目录：

\.harness/

├── product\-spec\.md          \# Planner 的产品规格

├── tech\-stack\.md            \# 技术选型（Generator 不可擅自更改）

├── rubric\.md                \# 项目评分标准

├── design\-taste\.md          \# 美学方向文档

├── master\-acceptance\.md     \# 跨 Sprint 集成测试计划

├── budget\.yml               \# 预算配置

├── checkpoint\.md            \# 当前状态快照（每轮评估后更新）

├── events\.jsonl             \# 只追加的事件流（时间机器）

├── decision\-log\.md          \# 决策引擎的每次裁决记录

├── lessons\.md               \# 错误记忆飞轮

└── delivery/

├── aesthetic\-review\.md  \# 最终美学评审

├── fresh\-clone\-report\.md \# 干净克隆的冒烟测试

└── audit\-trail\.md       \# 从规格到交付的人类可读旅程



项目根目录（提交到 Git）/

├── README\.md                \# 面向用户的文档

├── CHANGELOG\.md             \# Sprint 历史

└── KNOWN\_LIMITATIONS\.md     \# 已知局限（削减的功能、延迟的高危发现）

其中 `events.jsonl` 是一份只增不改的事件流——相当于一台时间机器，整个构建过程发生了什么，回头都能逐帧倒带。

---

## 快速上手

### 前置要求

Harness 要调动三家的模型，所以除了 Claude Code，还得把另外两个 CLI 装上：

## 1\. Claude Code（已有）

## 2\. Codex CLI（OpenAI）

## npm install \-g @openai/codex

## 3\. Gemini CLI（Google）

## npm install \-g @google/gemini\-cli



## 验证

codex \-\-version

gemini \-\-version

要是两个外部 CLI 都没装，自动模式会很干脆地在 `BLOCKED.md` 里停下来，告诉你卡在哪。只缺一个的话则进入降级模式，对应的审查结果会标上 "Source: Claude Fallback"，让你心里有数。

### 三个核心命令

# 自动模式（默认）：一次性端到端交付

/harness build "创建一个浏览器端音乐制作 DAW"



# 监督模式：每个阶段人工审批

/harness build \-\-supervised "构建一个带精灵编辑器的 2D 复古游戏制作工具"



# 从需求文档构建

/harness build \-\-requirements \./spec\.md



# 暂停当前构建

/harness stop



# 从中断点恢复

/harness resume

---

## 两种模式：如何选择？

撒手不管还是全程盯着，取决于一个问题：AI 猜错了，代价有多大。

### 自动模式（默认）

适合那些**目标清楚、容错较高**的活：CRUD 应用、内部工具、原型、演示项目。

- 决策引擎全自动运行

- 歧义通过预设规则解决，记录在 `ambiguities.md`

- 一次运行，最终交付 SHIPPED / PARTIAL\_SHIP / BLOCKED 三种结果之一

- 覆盖约 **70% 的"标准"需求**

按一下回车，去喝杯咖啡，回来看结果。

### 监督模式（\-\-supervised）

适合**需求模糊、风险高，或者你想亲手调教 Harness 品味**的场景。

- 在每个阶段边界暂停，等待你审批

- 你可以：继续（Continue）/ 下一 Sprint / 修改范围 / 直接交付（Ship）

- 适合当"AI 猜错的代价"高于"人工花时间"的情况

一句话——常规活儿放手让它跑，关键活儿你来掌舵。

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=NDgyOWEwYzE2ZDViNTJiOWFjY2Q0YTY1ZTYyYmZkNjJfYzBiYzdhYWM5ODQzNTcwZTI2ZWZkZjE5MTdhNjE2YzJfSUQ6NzY1MzY3NjkyMzg1NTM0MjU2N18xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)


*图：左——自动模式如火箭一次性发射，沿弧线直达目标；右——监督模式如精密手术，每一步由人工确认后推进*

---

## 交付管道：真正的"完成"

功能全做完、集成测试也过了，Harness 并不会就地停下喊收工。它会触发一条交付管道，把"能跑"再往"能交付"推一程：

Aesthetic Reviewer（Opus）评审

↓ 评分 ≥ 4\.0

Documentation Generator 写文档（提交到根目录）

↓

Fresh Clone Tester（干净环境克隆 \+ 按 README 运行）

↓

Audit Trail Generator（生成从规格到交付的完整旅程）

↓

输出最终结果

特别留意中间那步 Fresh Clone Tester——它会在一个干净环境里重新克隆代码，严格照着 README 一步步跑起来。这一关专治"在我机器上能跑"的老毛病：文档漏写一条依赖，到这里就原形毕露。

跑完，你会拿到一份这样的成绩单：

=== SHIPPED ===



Project: Music DAW

Verdict: All gates green, aesthetic 4\.3/5



Sprint summary: 6 completed \(\+ 1 polish sprint\)

Total iterations: 23 \(46% of iteration budget\)

Wall clock: 2h 14m \(56% of wall\-clock budget\)

External CLI calls: 48 \(40% of CLI budget\)



Quality scores \(anchored 1\-5\):

Functionality    4\.5/5

Design Quality   4\.2/5

Originality      4\.0/5

Robustness       4\.1/5

Test Coverage    3\.8/5

Weighted average: 4\.2/5\.0

Aesthetic review: 4\.3/5\.0



Adversarial: 3 CRITICAL found and fixed, 1 MEDIUM deferred



Run it: npm run dev

注意最后那行 Adversarial——3 个 CRITICAL 被找出来当场修掉，1 个 MEDIUM 明确标注为延后。它不假装代码完美，而是诚实地把账记清楚，这恰恰是生产级交付该有的样子。

---

## 为什么 Harness 有效？

单个 Agent 的天花板，是**模型能力**定的。
Harness 的天花板，是**围绕它搭的那套系统**定的。

这两句话差着一个量级。前者只能等下一代模型变强，后者今天就能靠工程把现有模型榨出更多价值。

它背后那个真正的洞见是：**让一个独立的评估者变严格，远比教会生成者自我批评要容易得多。** 自我批评是反人性的，独立审查却只是分工而已。不同模型家族 \+ 主动攻击者，把判别能力放大到了任何单一审查员都够不着的高度。

这才是 GAN 思想最值钱的地方——它从来不只是一种训练技巧，而是一套系统设计的哲学：**对抗，逼出质量。**

---

huanwang\.org                                             \[申请备注：项目、写歌、技术、观察\]

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=ODgzNzU2Nzc2OWJhMmM5Mjc5NmM0NDA5YzYyYWM4NzJfZjFjODE5ZWUzZjU0NTMxNjkwYWM0MTI5MmRjODJiNmNfSUQ6NzY1MzY3NzI5MDI2MTUzMTg0OV8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=MTY1NGUwMGQxNTc0MWZjMWViNjAyYTM0NjYzMGFiNjlfZjc5ZDMxZjBiNjE4OWM3Njc0MmYyZWExYmEyZmJlZjNfSUQ6NzY1MzY3NzI5MjY0Mzc4MTg2NV8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)

![Image](https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/authcode/?code=YzA0YzU4YmJiNTgzMDhlODBiMDNkODYyZjkxODQ3OTFfNjIzN2JiMzY0MzQzZDdmNDk5YzU4Y2JkM2FlZmFmYWNfSUQ6NzY1MzY3NzI5MjUzODk0MDM1Ml8xNzgyMDE5Mzc0OjE3ODIxMDU3NzRfVjM)



