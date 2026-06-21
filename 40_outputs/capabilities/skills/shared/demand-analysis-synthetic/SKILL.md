---
name: demand-analysis-synthetic
description: 合成用户调研——多Agent角色扮演+案例检索+全网数据交叉验证，输出结构化需求报告
version: 1.0.0
author: 黄药师
license: MIT
platforms: [cli, feishu]
metadata:
  hermes:
    tags: [用户调研, synthetic research, 角色扮演, Agent调研, 需求验证]
    related_skills: [demand-analysis, demand-analysis-iceberg, research-sats]
---

# Synthetic User Research（合成用户调研）

不用问卷、不找真人——用多 Agent 扮演不同用户角色 + 全网真实数据交叉验证，产出需求假设。本质：GAN 三角色 + SATs + 冰山 L6 + 多智能体架构。

## Constraints

<hard_limits>
- 角色扮演的推演必须用全网真实数据交叉验证——不能只靠 Agent 的"训练数据记忆"
- 每个需求假设必须标注：哪些来自 Agent 推演（🧠）、哪些来自真实数据验证（🔍）
- 最终结论必须有 ≥2 个独立数据源支撑
</hard_limits>

## 核心架构

```
Orchestrator (你)
  │
  ├── Case Retriever: 检索13张需求案例卡 → 提取历史摩擦点作为推演起点
  │
  ├── Persona Agents (3-5个并行)
  │   ├── Persona A: 扮演「用户画像1」→ 推演典型一天 → 输出痛点和期望
  │   ├── Persona B: 扮演「用户画像2」→ 同上
  │   └── Persona C: 扮演「用户画像3」→ 同上
  │
  ├── Verifier Agents (2个并行)
  │   ├── Data Verifier: 跑全网真实数据 → 交叉验证 Persona 推演
  │   └── Adversary: 攻击每个需求假设 → 找反面证据
  │
  └── Synthesizer: 合并 → 产出需求假设卡片
```

## Pipeline（8 步）

### Step 1: 定义推演范围

**输入**：业务方向（一句话）+ 目标市场

**输出**：推演计划——3-5 个用户画像的简要定义

```
业务：社区生鲜配送服务
画像A：一线城市双职工家庭（30-45岁，有孩子，双收入，晚7点到家）
画像B：退休老人（60-75岁，独居或与老伴，腿脚不便，价格敏感）
画像C：单身白领（25-35岁，加班多，外卖为主，偶尔做饭）
```

### Step 1.5: 案例检索（Case Retriever）🆕

**在 Persona 推演之前，先从已有案例库中找最相似的案例——用历史摩擦点作为推演起点，避免从零开始。**

| 动作 | 操作 |
|:--|:--|
| 关键词匹配 | 从业务方向提取关键词（如"生鲜""配送""社区"），检索 `case-demand-*` 案例卡 |
| 向量相似 | 如果关键词匹配 <3 个结果，用语义相似度扩展搜索 |
| 提取共性摩擦点 | 从匹配到的案例中提取"用户最痛苦的环节"和"为什么现有方案不work" |
| 注入推演起点 | 将历史摩擦点作为 Persona Agent 的推演上下文——"已知类似场景下用户在这些环节崩溃，请基于此推演..." |

**案例库检索指令**：
```python
# 检索 30_wiki/cases/ 下的需求案例
keywords = extract_keywords(business_idea)
matches = search_files(pattern=keywords, path="30_wiki/cases/")
# 提取每张案例卡的"核心教训"和"摩擦点"
for case in matches[:5]:
    friction_points = extract_section(case, "核心教训")
    persona_context.append(f"类似案例中发现：{friction_points}")
```

**可用的需求案例卡（13 张）**：
`case-demand-milkshake-jtbd` / `case-demand-ai-fitness-four-forces` / `case-demand-elderly-smart-device` / `case-demand-equestrian-three-tasks` / `case-demand-financial-literacy` / `case-demand-indonesia-insurance` / `case-demand-pharma-bigdata` / `case-demand-restaurant-hiring` / `case-demand-rural-5g` / `case-demand-silver-parenting` / `case-demand-tier4-housekeeping` / `case-demand-travel-agent` / `case-yitang-jtbd-story-formula`

### Step 2: 角色扮演推演（Persona Agents 并行）

**每个 Persona Agent 推演以下内容**：

| 推演维度 | 具体内容 | 对应冰山层 |
|:--|:--|:--|
| 典型一天 | 从早到晚的时间线，标注每个时段的行为、情绪、需求 | L1-L2 |
| 核心任务 | "在这个场景下，我真正想完成什么？"（方案中立） | L3 |
| 任务地图 | 完成核心任务的 8 步过程 + 每步的摩擦点 | L4 |
| 四种力量 | 推力/拉力/焦虑/习惯——我为什么不换/为什么想换？ | L5 |
| 内心独白 | 第一人称心理侧写——"我已经习惯了XX，但是..." | L5 |

**Persona Agent 提示词模板**：
```
你是 [用户画像]，生活在 [城市/环境]，[年龄/家庭/职业]。
请用第一人称"我"写出你的典型一天（从起床到睡觉）。
然后回答：
1. 在 [相关场景] 下，我最想完成什么？（方案中立——不准提产品名）
2. 我现在怎么解决？哪里最让我崩溃？
3. 如果有人提供一个新方案，我会担心什么？什么会阻止我换？
4. 如果换了新方案，我希望感觉到什么？希望别人看到我什么？
```

### Step 4: 全网数据交叉验证（Verifier Agent）

**Data Verifier 做的事**：

| 验证目标 | 数据源 | 验证问题 |
|:--|:--|:--|
| Persona 描述是否真实 | Reddit/知乎/小红书 | 真实用户怎么描述自己的生活？ |
| 痛点是否真实存在 | App Store评论/NPS | 竞品的用户高频抱怨是什么？ |
| 需求频次和刚性 | Google Trends/搜索词 | 这个需求多少人搜？什么季节？ |
| 付费意愿 | 竞品定价/评论 | 有人在为类似的方案付费吗？ |

**验证输出**：每条 Persona 推演的结论旁标注 🧠（Agent 推演）或 🔍（数据验证）

### Step 5: 对抗检验（Adversary Agent）

**Adversary 做的事**（SATs Devil's Advocacy + Red Team）：

| 攻击角度 | 攻击问题 |
|:--|:--|
| 需求不存在 | "这个痛点真的是痛点吗？还是 Agent 推演时编出来的？" |
| 需求不够大 | "有多少人真的会遇到这个问题？频率多高？" |
| 用户不会付费 | "有没有免费替代方案？用户愿意付多少钱？" |
| 方案不如人 | "为什么竞对没做？如果他们做了呢？" |
| 用户不会切换 | "现状偏见 ×1.5——用户的习惯和焦虑是不是被低估了？" |

### Step 6: 合并 + 筛选（Synthesizer）

**Synthesizer 做的事**：
1. 合并所有 Persona 的共同痛点（≥2 个 Persona 都提到的 → 高信号）
2. 标注每个痛点的验证状态（🔍已验证 / 🧠待验证 / ⚠️数据矛盾）
3. 用评估三角形打分（普遍性/频次/刚性）

### Step 7: 产出需求假设卡片 + 结构化报告（冰山 L6 + 报告模板）

**两种输出格式**：

| 场景 | 格式 | 模板 |
|:--|:--|:--|
| 内部快速验证 | 机会卡片（简洁版） | 本 Skill 的 Step 6 卡片 |
| 面向用户/投资人交付 | 完整结构化报告 | `tool-demand-report-template`（九段式：简介→TAM→SAM→CR1→策略→假设→步骤→提醒） |

**报告模板映射**：见 `tool-demand-report-template`——不只是分析结论，是可投递的完整报告。

每张机会卡片：
```
机会名称：[切入点 + 核心价值]
目标用户：[画像描述]
核心任务：[方案中立的 JTBD 陈述]
证据：🔍 [数据来源] / 🧠 [推演来源]
最危险假设 (RAT)：
  1. [如果这个假设错了，机会就不存在]
  2. ...
  3. ...
评估三角形：普遍性 X/5 | 频次 X/5 | 刚性 X/5
```

### Step 8: 质量自检

| 检查项 | 标准 |
|:--|:--|
| 数据验证覆盖率 | ≥60% 的关键结论有 🔍 标记 |
| 角色多样性 | ≥3 个差异化的 Persona |
| 对抗充分性 | Adversary 至少提出 3 条有效攻击 |
| 假设可验证性 | 每条 RAT 可被实验验证 |

## 和传统方法的对比

| 传统方法 | 合成用户调研 |
|:--|:--|
| 设计问卷 → 发传单 → 收回答（2-4周） | Agent 推演 + 数据验证（2-4小时） |
| 样本量 100-500 人 | Persona 3-5 个 + 全网真实数据交叉验证 |
| 成本 ¥5,000-50,000 | 近乎零（只有 API token 费用） |
| 用户说什么就记录什么 | Adversary 攻击每个假设——"用户说的"被检验 |
| 一次性报告 | 可迭代——改了业务方向立即重跑 |

## 完整案例：社区老年助餐服务（狗粮测试 2026-06-21）

### 案例检索命中

| 案例 | 提取的教训 |
|:--|:--|
| `case-demand-elderly-smart-device` | 功能强≠老人会用——界面必须极简，不能用"扫码" |
| `case-demand-tier4-housekeeping` | 天花板误判——普遍性高≠能做大规模，刚性必须细化到"愿意付多少钱" |
| `case-demand-restaurant-hiring` | 频次高估——"有需求的时候很刚"≠高频，要看时间分布 |

### Persona 推演摘要

**Persona A: 独居退休老人（75岁）**
> "下楼买菜得扶着楼梯慢慢挪。中午一个人，做多了吃不完，做少了不值得。社区要是有人每天送一顿热饭，15块以内能接受。但千万别让我扫码——给我一张卡，刷一下就行。"

**Persona B: 与子女同住的老人（68岁）**
> "儿子让我叫外卖，但外卖太油了，血压高不能吃。请钟点工一小时40块太贵。最想要有人做适合老年人的菜，少油少盐，一顿12-15块，送到门口。"

**Persona C: 刚退休的活跃老人（62岁）**
> "吃饭不是问题——问题是没人一起。以前单位食堂热闹，现在冷冷清清。如果社区有个地方能一起吃午饭，我愿意多走10分钟路过去。不是为了省钱，是想有人说说话。"

### 数据验证

| 结论 | 源 | 状态 |
|:--|:--|:--|
| 独居老人"做多了浪费""不敢点外卖"是高频抱怨 | Reddit/知乎语义分析 | 🔍 |
| 外卖App 60+用户评论中"太油""不健康"占 23% | App Store 评论 NLP | 🔍 |
| "退休后吃饭没伴"是社交媒体第三大老年孤独抱怨 | 社交媒体情感分析 | 🔍 |
| Google Trends "老年助餐"搜索量 2024-2026 上升 60% | Google Trends | 🔍 |

### 对抗攻击

| 攻击 | 结论 | 来源 |
|:--|:--|:--|
| 老人愿意付费吗？刚性存疑——15元客单价配送难盈利 | 🟡 | `case-demand-tier4-housekeeping` 天花板误判 |
| 频次够吗？每天一顿午饭=高频 | ✅ | 不像 `case-demand-restaurant-hiring` 脉冲式需求 |
| 用户不会切换吗？现状偏见×1.5——自己做/子女做/不吃 | 🔴 | 行为经济学——"做了几十年饭"的习惯极强 |
| 为什么竞对没做？美团老年模式渗透率低——界面还是太复杂 | 🟡 | 机会窗口存在但需极简设计 |

### 产出假设卡片

| 卡片 | 画像 | 核心任务 | 评估 | 最大风险 |
|:--|:--|:--|:--|:--|
| 送餐到户 | A+B | "在不能/不想做饭的中午，获得适合老年人的热饭" | 普4/频5/刚3 | 客单价12-15元，配送成本能否覆盖？ |
| 社区食堂 | C | "在退休后的孤独中午，找有人一起吃饭的地方" | 普3/频5/刚4 | 社交需求能支撑溢价吗？选址和运营成本？ |

### 案例库的关键价值

**Case Retriever 注入的历史教训直接改变了推演方向**——"刚性误判""频次高估""天花板误判"全部被 Adversary 引用。"15元客单价能否覆盖配送成本"这个风险如果不用案例库，Persona Agent 自己是不会主动质疑的。

---

## 已知局限

- 🧠 标记的结论来自 Agent 推演，不是真实用户数据——可能有偏差
- Persona 扮演的质量取决于提示词的精确度——用户画像越具体，推演越真实
- 不能完全替代真实用户访谈——合成调研是"生成假设"不是"验证假设"。验证仍需真实用户
- 小众市场的数据验证可能缺乏足够的数据源

## 相关 Skill + 卡片

| 组件 | 做什么 | 调用方式 |
|:--|:--|:--|
| `/demand-analysis-iceberg` | 冰山六层标准流程 | 本 Skill 推演框架的基础 |
| `/demand-analysis-evaluate` | 评估三角形 + 四种力量 | Step 5 合并筛选 |
| `/research-sats` | Devil's Advocacy / Red Team | Step 4 对抗检验 |
| `/research-alt-data` | 替代数据源 | Step 3 数据验证 |
| `/ai-collaboration-gan` | GAN 三角色架构 | 本 Skill 的设计原型 |
| `tool-demand-agent-l5-signal-substitute` | Agent 微观体感替代 | Step 3 的情感分析 |
