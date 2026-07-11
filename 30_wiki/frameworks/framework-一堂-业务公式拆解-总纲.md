---
id: framework-一堂-业务公式拆解-总纲
title: 一堂业务公式拆解总纲：关键假设 ABCD 体系的核心骨架与灵魂（贯通定性→定量）
type: framework
status: pending_review
author: 老顽童
reviewed_by: 欧阳锋
confidence: 0.86
trust_level: high
language: zh-CN
created_at: 2026-07-09
updated_at: 2026-07-09
domain:
- yitang
- key-assumptions
- business-formula
source_refs:
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-口述.txt L178-L194,L2474-L2500
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-笔记.txt L15-L86
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-ABC模型图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-冰山模型图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-6层逻辑关系图_paddle_ocr.txt
- 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-十大业务公式范式_paddle_ocr.txt
related:
- '[[framework-一堂-关键假设]]'
- '[[framework-一堂-关键假设-ABCD模型]]'
- '[[yt-business-formula-abc-model]]'
- '[[yt-business-formula-parameter-iceberg]]'
- '[[yt-business-formula-six-level-logic]]'
- '[[yt-business-formula-ten-paradigms]]'
- '[[yt-business-formula-l6-essence-formulas]]'
- '[[yt-business-formula-business-pattern-selector]]'
- '[[yt-business-formula-qualitative-metrics-library]]'
- '[[tool-一堂-业务公式-L1L6参数分层自检]]'
- '[[concept-一堂-business-prediction]]'
- '[[dk-yitang-business-formula-plus-times-trap]]'
diagnostic_signals:
- signal: 团队说"我们的关键假设是用户会买单"，但说不清差多少、先动哪
  lens: 假设停在定性——没有拆到可验证参数
  follow-up: 用本卡把假设写成ABC公式，下钻到能提出可验证假设的L层（通常L3-L5）
- signal: 公式写出来了，但把漏斗当加法平均用力
  lens: 逻辑关系写错——+×混淆、相关当因果
  follow-up: 接dk-yitang-business-formula-plus-times-trap，先切分（+）再拆转化（×），区分相关/因果
quality_labels:
- principle
- framework
- cited
- actionable
---

# 一堂业务公式拆解总纲：关键假设 ABCD 体系的核心骨架与灵魂

> **一句话**：业务公式拆解不是「把营收拆成流量×转化×客单」这一组固定变量，而是**关键假设 ABCD 体系的核心骨架与灵魂**——它把定性关键假设，经 **ABC 模型 × 参数冰山 L1-L6 × 六层逻辑 × 十大范式**，拆到能提出可验证假设的定量参数。本卡是贯通总纲与 7 张子卡的导航。来源：孔源业务公式拆解培训（口述/笔记/逐字稿 + 4 张模型图）。[^1]

---

## 一、定位：关键假设 ABCD 体系的「最后一块拼图 / 核心骨架 / 灵魂」

> 孔源原话：「这一次我们也是把**关键假设 ABCD 的体系的最后一块拼图**拼上了。」（`孔源-口述:2474`）「咱们**业务公式也是一套关键假设 ABCD 体系串起来的核心骨架，才是真正贯穿整套体系的灵魂**。」（`:2500`）

这意味着业务公式不是关键假设之外的另一门课，而是**关键假设从「定性」走向「定量」的那座桥**：

- 关键假设回答「成不成、哪条最脆弱」（[[framework-一堂-关键假设]]）；
- ABCD 回答「这条假设属于哪类场景」（[[framework-一堂-关键假设-ABCD模型]]）；
- **业务公式回答「这条假设差多少、先动哪、怎么证伪」**——把「我觉得用户会买单」拆成「流量×转化×客单，分别对应 L1-L6 哪几层、哪个低于基准、用哪个实验证伪」。

> 线下训练营体系也印证这一贯通：「在业务关键假设 ABCD 体系里，线下训练营已经有了五步法训练营和科学决策 ROI 训练营」（`:2482`），业务公式训练营是其第三块拼图。

---

## 二、四件套一张图

```
关键假设（定性）
   ↓
A 目标 Ambition  ──  B 参数 Basis  ──  C 逻辑关系 Connection      ← ABC 模型（构造语法）
                          │                      │
                          ↓                      ↓
                  参数冰山 L1-L6            六层逻辑关系
              基础→财务→分层→转化→     模糊→相关→因果→公式→定量→动态
                  创新→魔法          (安慰剂→体温计→方向盘→X光片→刻度尺→导航仪)
                          │                      │
                          └──────────┬───────────┘
                                     ↓
                          十大业务公式范式（让学员「都见过」的结构库）
              流量变现/线索转化/门店收入/用户周期/连续留存/…
                                     ↓
                          最便宜验证买点（针对最弱环节证伪）
```

四件套各司其职，缺一不可：

| 件套 | 角色 | 子卡 |
|---|---|---|
| **ABC 模型** | 公式的构造语法：目标=参数⊗逻辑关系 | [[yt-business-formula-abc-model]] |
| **参数冰山 L1-L6** | 参数按深度分层：水面上靠经验，水面下靠分析/创新 | [[yt-business-formula-parameter-iceberg]] |
| **六层逻辑关系** | 人对公式的理解深度：从模糊安慰剂到动态导航仪 | [[yt-business-formula-six-level-logic]] |
| **十大范式** | 常见业务的结构库：先借鉴（实事求是）再创新（解放思想） | [[yt-business-formula-ten-paradigms]] |

> 「先掌握十大业务公式，再探索自己的公式」（ABC 模型图 OCR）——借鉴公式（实事求是）vs 创新公式（解放思想）是两个取向，新业务偏创新但要防拍脑袋，成熟业务偏借鉴但要防照搬。

---

## 三、三要素与三大认知突破

### 三要素：看得清 / 讲得明 / 做得准

> 孔源：「业务公式如果真的是要在我们业务进行过程中要用，那必须满足这三点。」（`孔源-口述:178-194`；`笔记:24-27`）

| 要素 | 含义 | 自检 |
|---|---|---|
| **看得清** | 明确业务的根本矛盾在哪个问题、这个问题该怎么判断 | 能用一句话说出当前主要矛盾吗？ |
| **讲得明** | 这个矛盾下有哪些要素、构成什么、解决优先级是什么 | 要素是否列全、是否分了先后（不眉毛胡子一把抓）？ |
| **做得准** | 面对要素能提出哪些假设、有无清晰判断依据 | 每个假设有没有行为指标与基准？ |

### 三大认知突破（`笔记:31-71`）

| 突破 | 从 | 到 |
|---|---|---|
| **多维度分层拆解** | 看大盘总指标 | 切用户/渠道/行为/场景/SKU（L3） |
| **参数量化** | 定性「我觉得」 | 给每个定性参数配 3-5 个行为指标（L4-L5） |
| **逻辑关系验证** | 把相关当因果、+× 乱写 | 区分相关/因果，先切分（+）再拆转化（×）（接 [[dk-yitang-business-formula-plus-times-trap]]） |

---

## 四、统摄导航：7 张子卡

本卡不替代 7 张 `yt-business-formula-*` 子卡，只给它们在贯通链中的位置，按需下钻：

| 子卡 | 类型 | 在贯通链中的位置 | 回答的问题 |
|---|---|---|---|
| [[yt-business-formula-abc-model]] | framework | 入口·构造语法 | 公式由哪三要素构成？目标/参数/逻辑关系怎么写？ |
| [[yt-business-formula-parameter-iceberg]] | concept | 参数深度 | 当前参数在水面上（L1-L2）还是水面下（L3-L6）？够不够深？ |
| [[yt-business-formula-six-level-logic]] | concept | 理解深度 | 我对公式的理解在 L1 模糊还是 L6 动态？够不够支撑决策？ |
| [[yt-business-formula-ten-paradigms]] | concept | 结构库 | 我的业务最接近哪个范式？该借鉴哪个结构？ |
| [[yt-business-formula-l6-essence-formulas]] | concept | 本质层 | 销售/留存/复购的本质公式（L6 魔法参数）是什么？ |
| [[yt-business-formula-business-pattern-selector]] | framework | 范式选择器 | 多个范式候选时，怎么选主范式、怎么组合？ |
| [[yt-business-formula-qualitative-metrics-library]] | framework | 定性指标库 | 定性参数（如信任度）能配哪 3-5 个行为指标？ |

> 粒度说明：abc-model / selector / qualitative-metrics 在 `frameworks/`，six-level-logic / ten-paradigms / parameter-iceberg / l6-essence 在 `concepts/`——本总纲不搬动它们，仅在此建立导航与双向 related。

---

## 五、贯通链：定性假设 → L1-L6 定量参数（落地）

把一条关键假设拆到可验证，固定走这五步：

```
1. 写目标（A）：用一句话写出要提升的业务结果，≤5 个变量，可量化/可决策/可分层
2. 列参数（B）：按 财务/行为/节点/要素 四类列出影响目标的变量
3. 定关系（C）：判断参数间是 + 、× 、因果（→）还是相关（~）——资源只投 →，~ 只监控
4. 下钻层（冰山）：从 L1 大盘往下，直到「能提出可验证假设」的那层（通常 L3-L5）就停
5. 找基准+设买点：给关键参数找行业/历史基准判断高低，针对最弱环节设计证伪实验
```

**停钻标准**（接 [[yt-business-formula-parameter-iceberg]]）：一个参数是否需要继续拆到 L6，只有一个标准——**这个参数能不能提出可验证的假设？能，就停；不能，继续拆。**

> 口径约束：所有数字、比例、转化率、行业对照均为**课程经验值 / 课程案例口径**（`笔记:42-44` 的私域电商人均贡献、企业培训续费、口腔诊所成交等），降级使用，不作外部事实断言。

---

## When NOT to Use

- **业务尚无关键假设**：先回 [[framework-一堂-关键假设]] 做假设识别，没假设就拆公式是「为拆而拆」。
- **从 0 到 1 无范式的新品类**：十大范式帮不上，先用 [[yt-business-formula-abc-model]] 自建创新公式，并接受其「拍脑袋」风险。
- **把它当财务建模替代品**：业务公式是「找抓手、做证伪」的诊断工具，不是预算/估值模型；最终财务结论交专业财务。
- **一次性堆叠多个范式**：先定位「下一步最渴望提升什么」选一个主范式，其他范式只解决主范式里的某个子参数（接 [[yt-business-formula-ten-paradigms]] 使用边界）。

## Failure Modes

| 失败模式 | 症状 | 修复 |
|---|---|---|
| **停在 L1-L2** | 只看大盘和财务，无法指导动作 | 下钻到 L3-L4：切人群/渠道，拆漏斗断点 |
| **把相关当因果** | 看到「投放↑转化↑」就加大投放 | 推到 L3 因果层，控制变量验证（接 [[dk-yitang-business-formula-plus-times-trap]]） |
| **+× 写错** | 把漏斗当加法平均用力，或把叠加当乘法求全 | 先切分（+）再拆转化（×）；乘法投最弱环节，加法投边际最高 |
| **照搬范式变量** | 直接套「流量×转化×客单」，不管自身业务 | 范式给结构，变量按自身业务重定义 |
| **公式完美参数不准** | L4 形式对、结论错（虚假确定性） | 给参数找基准，用历史/行业数据校准到 L5 |
| **拆到 L6 失可操作** | 公式过复杂，团队无法执行 | 回退到 L4 可操作层；拆得深不如拆得准 |

## Action Triggers

| 触发场景 | 第一个动作 | 成功指标 |
|---|---|---|
| 关键假设停在定性无法证伪 | 走贯通五步：写 A→列 B→定 C→下钻→找基准 | 每条关键假设有 ABC 公式 + 应下钻到的 L 层 |
| 不知用哪个范式 | 查十大范式 + [[yt-business-formula-business-pattern-selector]] | 选定一个主范式 |
| 定性参数配不出指标 | 查 [[yt-business-formula-qualitative-metrics-library]] | 每个定性参数有 3-5 个行为指标 |
| 想确认公式够不够用 | 用 [[tool-一堂-业务公式-L1L6参数分层自检]] 跑 7 问 | 7 问全过，或明确要补哪一层 |

## Synthesis

| 关系 | 目标节点 | 说明 |
|---|---|---|
| 总纲·贯通 | [[framework-一堂-关键假设]] | 本卡是其「术」柱，定性→定量的桥 |
| 场景入口 | [[framework-一堂-关键假设-ABCD模型]] | A/B 成败类落 ABC，C/D 效率类落 L4 漏斗 |
| 子卡·语法 | [[yt-business-formula-abc-model]] | ABC 构造语法 |
| 子卡·参数深度 | [[yt-business-formula-parameter-iceberg]] | L1-L6 冰山 |
| 子卡·理解深度 | [[yt-business-formula-six-level-logic]] | 六层逻辑关系 |
| 子卡·结构库 | [[yt-business-formula-ten-paradigms]] | 十大范式 |
| 子卡·本质 | [[yt-business-formula-l6-essence-formulas]] | L6 本质公式 |
| 子卡·选择器 | [[yt-business-formula-business-pattern-selector]] | 范式选择 |
| 子卡·指标库 | [[yt-business-formula-qualitative-metrics-library]] | 定性指标库 |
| 操作自检 | [[tool-一堂-业务公式-L1L6参数分层自检]] | L1-L6 分层 + 三要素自检 |
| 上游 | [[concept-一堂-business-prediction]] | 预判选方向，公式把方向的关键假设定量化 |
| 符号防错 | [[dk-yitang-business-formula-plus-times-trap]] | +×/相关因果防错口诀 |

[^1]: **署名差异说明**：本批素材文件名与任务单用「孔源」（目录 `00_inbox/关键假设C-拆解业务公式/孔源-…`），而 `孔源-业务公式拆解-笔记.txt:5,108` 与 [[dk-yitang-business-formula-plus-times-trap]]（`source_person: 孔阳`）正文作「孔阳」。本任务统一标注为「**孔源（笔记正文作孔阳）**」，回链时保持此口径，避免署名混乱。

> 核心心法：**关键假设回答「哪条最脆弱」，业务公式回答「那条差多少、先动哪、怎么证伪」。** 定性不定量，假设永远是口号；定量不证伪，公式永远是 PPT。
