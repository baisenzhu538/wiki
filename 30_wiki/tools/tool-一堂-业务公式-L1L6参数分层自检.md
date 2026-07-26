---
id: tool-一堂-业务公式-L1L6参数分层自检
title: 工具：业务公式 L1-L6 参数分层自检——看得清/讲得明/做得准 + 符号因果校验
type: tool
status: pending_review
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.84
trust_level: high
language: zh-CN
created_at: 2026-07-09
updated_at: 2026-07-09
domain:
- yitang
- key-assumptions
- business-formula
source_refs:
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-冰山模型图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-6层逻辑关系图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-口述.txt L178-L194
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-笔记.txt L31-L71
related:
- '[[framework-一堂-业务公式拆解-总纲]]'
- '[[yt-business-formula-parameter-iceberg]]'
- '[[yt-business-formula-six-level-logic]]'
- '[[yt-business-formula-abc-model]]'
- '[[yt-business-formula-qualitative-metrics-library]]'
- '[[dk-yitang-business-formula-plus-times-trap]]'
- '[[framework-一堂-关键假设]]'
- '[[business-formula-domain-digest]]'
- '[[yt-tool-business-formula-parameter-arsenal]]'
- '[[tool-yitang-business-formula-l5-mining-and-verification]]'
- '[[dk-yitang-business-formula-recursive-levels]]'
- '[[dk-yitang-business-formula-skip-level-entry]]'
- '[[dk-yitang-formula-unmeasurable-metrics]]'
quality_labels:
- actionable
- framework
tags:
- audience:executor
- scene:execution
- skill-level:advanced
aliases:
- 业务公式拆解
- 关键假设C-拆解业务公式
---

# 工具：业务公式 L1-L6 参数分层自检

> **一句话**：拿到一个业务公式草稿，用本工具跑一遍——先定位它在 L1-L6 哪一层，再用「看得清/讲得明/做得准」三要素和 7 问清单判断够不够深，最后用 +×/因果校验防错。输出「当前层 + 缺口 + 是否停钻」。原理见 [[yt-business-formula-parameter-iceberg]] / [[yt-business-formula-six-level-logic]]，总纲见 [[framework-一堂-业务公式拆解-总纲]]。

---

## 何时用

**适合用**：
- 公式写出来了，但不确定够不够深、能不能指导动作
- 团队对公式有争议（有人说看大盘就行，有人说要拆到本质）
- 要把定性关键假设落到可验证参数，需要确认下钻到哪层停

**不要用**：
- 还没有关键假设、没有公式草稿 → 先回 [[framework-一堂-关键假设]] 做假设识别，再用 [[yt-business-formula-abc-model]] 写公式
- 把本工具当财务建模/预算工具 → 它是诊断「公式够不够支撑决策」，不替代财务模型
- 公式团队根本无法执行 → 再深也没用，回退到 L4 可操作层

---

## 需要什么

| 输入 | 必需 | 说明 |
|:---|:---:|:---|
| 一个业务公式草稿（ABC 形式） | 是 | A 目标 / B 参数 / C 逻辑关系；没有先用 [[yt-business-formula-abc-model]] 写 |
| 每个关键参数的数据来源 | 是 | 没有数据来源的参数标「不可测」，不能进入验证 |
| 行业/历史基准 | 否 | 有则可到 L5 定量；无则先停在 L3-L4，标「待补基准」 |

---

## 操作步骤

**Step 1：定位当前层级**

对照冰山（L1 基础/L2 财务/L3 分层/L4 转化/L5 创新/L6 魔法），判断当前公式最深拆到哪一层：

| 当前最深 | 特征 | 够不够 |
|---|---|---|
| L1-L2 | 只有流量/营收/毛利率等大盘与财务 | 不够——无法指导动作，继续下钻 |
| L3-L4 | 切了人群/渠道，拆了漏斗断点 | 多数业务够——能提出可验证假设，可停 |
| L5-L6 | 参数有基准/空间，或触达本质 | 战略/创新场景需要——但要防过度复杂 |

**Step 2：三要素自检（看得清/讲得明/做得准）**

| 要素 | 自检问题 | 不过则 |
|---|---|---|
| 看得清 | 能用一句话说出当前主要矛盾吗？ | 回到目标 A，重述主要矛盾 |
| 讲得明 | 要素列全了吗？分了先后吗？ | 补全参数 B，按前置性排序 |
| 做得准 | 每个假设有行为指标和基准吗？ | 给定性参数配 3-5 个行为指标（查 [[yt-business-formula-qualitative-metrics-library]]） |

**Step 3：7 问分层自检**

逐问回答，任一「否」即定位到缺口：

- [ ] 1. 当前公式能否提出**可验证假设**？（否→下钻到 L3-L4）
- [ ] 2. 每个**定性参数**是否找到 3-5 个行为指标？（否→「我觉得」改「我看到」）
- [ ] 3. 是否已**先切分（+）再拆转化（×）**？（否→重拆，避免总指标掩盖子群体）
- [ ] 4. 运算符号是否写对：+ 是叠加、× 是漏斗？（否→进 Step 4 校验）
- [ ] 5. 是否区分了**相关与因果**？（否→画因果链，做控制变量）
- [ ] 6. 是否为关键参数找到**行业/历史基准**？（否→无法判断高低，先补基准到 L5）
- [ ] 7. 公式团队**能否执行**？（否→拆太复杂，回退到 L4 可操作层）

**Step 4：+×/因果校验（接 [[dk-yitang-business-formula-plus-times-trap]]）**

| 检查 | 规则 | 反例 |
|---|---|---|
| 拆解顺序 | 先切分（+，同维度独立可加）再拆转化（×，串联漏斗） | 没切人群就直接拆「总转化率」 |
| 加法资源 | 投边际产出最高项，不平均分 | 满意度=环境+服务+产品后给三项平均用力 |
| 乘法资源 | 投最弱环节（瓶颈），不强项 | 续费率=使用深度×价值感知×价格接受度，却去拉已经最强的项 |
| 相关≠因果 | 用 `→` 标因果（干预点）、`~` 标相关（监控点）；资源只投 `→` | 把「投放↑转化↑」当因果加大投放 |

**Step 5：停钻判定 + 输出**

- **停钻标准**：一个参数是否需要继续拆到 L6，只有一个标准——**它能不能提出可验证假设？能，就停；不能，继续拆。**
- 输出格式：`当前最深 L[X] → 缺口：[第 N 问不过] → 动作：[下钻/补基准/回退 L4] → 是否停钻：[是/否]`

---

## 常见坑

| 坑 | 症状 | 修复 |
|---|---|---|
| **停在 L1-L2** | 只看大盘财务，无法指导动作 | 强制下钻到 L3-L4：切人群/渠道，拆漏斗断点 |
| **L2 陷阱** | 把相关当因果，看到同向就加大投入 | 推到 L3 因果层，控制变量验证 |
| **L4 陷阱** | 公式完美但参数不准，结论错 | 给参数找基准校准到 L5，防虚假确定性 |
| **L6 陷阱** | 公式过复杂，团队无法执行 | 回退到 L4 可操作层；拆得深不如拆得准 |
| **+× 写错** | 漏斗当加法平均用力，或叠加当乘法求全 | 先切分再拆转化；乘法投最弱、加法投边际最高 |
| **定性停在口号** | 「信任度」没有行为指标 | 查 [[yt-business-formula-qualitative-metrics-library]]，配 3-5 个行为指标 |
| **一次堆多范式** | 想把所有层所有范式都跑一遍 | 选一个主范式/主矛盾，其他只解决子参数 |

---

## 自检

- [ ] 定位了当前最深层级（L1-L6）
- [ ] 三要素（看得清/讲得明/做得准）逐项过
- [ ] 7 问全过，或明确标出不过的是哪几问 + 补哪层
- [ ] +×/因果校验过，相关没当因果、漏斗没当加法
- [ ] 给出「停钻 / 继续下钻 / 回退 L4」的明确结论

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|---|---|
| 上位总纲 | [[framework-一堂-业务公式拆解-总纲]] | 本工具是其自检操作层 |
| 原理·冰山 | [[yt-business-formula-parameter-iceberg]] | L1-L6 参数分层原理 |
| 原理·六层 | [[yt-business-formula-six-level-logic]] | 理解深度与停钻判定 |
| 原理·ABC | [[yt-business-formula-abc-model]] | 公式构造语法（自检的输入） |
| 指标库 | [[yt-business-formula-qualitative-metrics-library]] | 定性参数配行为指标 |
| 符号防错 | [[dk-yitang-business-formula-plus-times-trap]] | +×/相关因果校验来源 |
| 入口 | [[framework-一堂-关键假设]] | 自检服务于关键假设定量化 |
