---
id: diag_20260709_yitang-key-assumptions-business-formula-deep-dive
title: 关键假设 + 业务公式拆解域深挖诊断报告：方法论入口缺总框架卡、ABCD 卡与 orchestrator Agent
type: diagnosis
status: active
source: 00_inbox/一堂-关键假设课-truman-口述.txt + 00_inbox/关键假设C-拆解业务公式
source_refs:
  - 00_inbox/一堂-关键假设课-truman-口述.txt L22-L80,L364-L402,L584,L818,L962-L982,L1064-L1074,L1560,L1644,L1810,L1982-L1998,L2460-L2482
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-口述.txt L10,L182-L194,L360,L510,L682-L694,L860,L1356-L1374,L1476-L1504,L1772,L1972,L2324,L2384,L2418,L2474-L2524
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-笔记.txt L15-L86
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式-逐字稿01.txt
  - 00_inbox/一堂-关键假设-关键假设ABCD模型_paddle_ocr.txt
  - 00_inbox/一堂-关键假设-关键假设三板斧_paddle_ocr.txt
  - 00_inbox/一堂-关键假设-商业画布259（9）_paddle_ocr.txt
  - 00_inbox/一堂-关键假设-烤炉案例_paddle_ocr.txt
  - 00_inbox/一堂-关键假设-奶茶案例_paddle_ocr.txt
  - 00_inbox/一堂-关键假设-五步法259（5）_paddle_ocr.txt
  - 00_inbox/一堂-关键假设-五步法259（2）_paddle_ocr.txt
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-ABC模型图_paddle_ocr.txt
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-6层逻辑关系图_paddle_ocr.txt
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-冰山模型图_paddle_ocr.txt
  - 00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-十大业务公式范式_paddle_ocr.txt
reviewer: 欧阳锋
created_at: 2026-07-09
updated_at: 2026-07-09
related:
  - "[[concept-一堂-key-assumptions]]"
  - "[[concept-一堂-hypothesis-driven-business-methodology]]"
  - "[[concept-一堂-business-prediction]]"
  - "[[framework-一堂五步法]]"
  - "[[yt-business-formula-abc-model]]"
  - "[[yt-business-formula-parameter-iceberg]]"
  - "[[yt-business-formula-six-level-logic]]"
  - "[[yt-business-formula-ten-paradigms]]"
  - "[[yt-business-formula-l6-essence-formulas]]"
  - "[[yt-business-formula-business-pattern-selector]]"
  - "[[yt-business-formula-qualitative-metrics-library]]"
  - "[[tool-一堂-hypothesis-validation-three-axe]]"
  - "[[tool-key-assumptions-check]]"
  - "[[tool-first-principles-assumption-classify]]"
  - "[[case-一堂-陈贤敏汉堡-hypothesis-validation]]"
  - "[[case-一堂-无人餐厅-hypothesis-failure]]"
  - "[[dk-mckinsey-hypothesis-driven-pitfalls]]"
  - "[[dk-yitang-business-formula-plus-times-trap]]"
  - "[[framework-lean-abcd-model]]"
  - "[[yt-decision-abcd-model]]"
  - "[[framework-yitang-project-abcd-classification]]"
---

# 关键假设 + 业务公式拆解域深挖诊断报告

> 王语嫣编排，只诊断不写卡。所有源自口述稿/OCR/笔记的数字、比例、人数均降级为「课程经验值 / 课程案例口径」，不作为外部事实断言。

## 执行摘要

**关键假设课是一堂整个课程体系的「第一节必修课」与方法论入口**：Truman 自述这是「所有课里面听的人数最多、受好评最多的课」，是「我送给大家的一节商业必修课」，历经「六轮大的升级」、直播间累计触达人数为课程经验值量级（`一堂-关键假设课-truman-口述.txt:22-62,104`）。它的内核只有一句话——**用假设驱动业务**（`:364-402`），方法论骨架是**关键假设三板斧：先做加法、再做减法、最后快速验证**（`:1064-1074`），本质被收敛为**风险管理**（`:2474`）。

**业务公式拆解（孔源）则是关键假设体系的「核心骨架」与「灵魂」**：孔源口述明确表态——「这一次我们也是把关键假设 ABCD 的体系的最后一块拼图拼上了」「业务公式也是一套关键假设 ABCD 体系串起来的核心骨架，才是真正贯穿整套体系的灵魂」（`孔源-业务公式拆解-口述.txt:2474-2500`）。也就是说，**关键假设（定性）→ 业务公式（定量）** 本应是一条贯通主线。

但 **wiki 现状是「两条链各自为政、入口缺总纲」**：关键假设侧只有零散 concept/tool/case，业务公式侧 7 张 `yt-business-formula-*` 已较完整却挂在管理域、与关键假设主线无贯通；**缺一张关键假设主线总框架卡、缺关键假设 ABCD 模型卡、缺「关键假设↔业务公式」贯通卡、缺本域 orchestrator Agent Spec**。

**深挖价值：高。评级：A-（建议尽快入队 #145，作为 #141 五步法 orchestrator 的「第一节必修课」前置入口）。**

---

## 一、域结构总览

```
关键假设 + 业务公式拆解（一堂方法论入口层）
├── 定位：第一节必修课、六轮升级、方法论入口（truman-口述:22-80）
├── 核心命题：用假设驱动业务；Idea不值钱，关键假设才价值千金（:364-402, :584）
├── 方法骨架：关键假设三板斧 = 加法（解构要素）→ 减法（找风险最高假设）→ 验证（最便宜策略）（:1064-1074）
├── 场景分类：关键假设 ABCD 模型（成败问题 + 效率问题）
│       A 商业场景  B 决策场景（宏观—微观）  C 增长场景  D 转化场景（关键假设ABCD模型_OCR）
├── 风险本质：关键假设的本质就是风险管理（:2474）；某关键假设失败=业务巨大硬伤（:1810）
└── 定量贯通：业务公式拆解（孔源）= 关键假设 ABCD 体系的「核心骨架/灵魂」（:2474-2500）
        ├── ABC 模型：A 目标（Ambition）/ B 参数（Basis）/ C 逻辑关系（Connection）（ABC模型图_OCR）
        ├── 参数冰山 L1-L6：基础→财务→分层→转化→创新→魔法参数（冰山模型图_OCR）
        ├── 六层逻辑关系：L1模糊→L2相关→L3因果→L4公式→L5定量→L6动态（6层逻辑关系图_OCR）
        ├── 十大业务公式范式：流量变现/线索转化/门店收入/用户周期/连续留存…（十大范式_OCR）
        └── 三要素 / 三突破：看得清·讲得明·做得准；多维度分层·参数量化·逻辑关系验证（笔记:15-71）
```

**核心判断**：关键假设是「道」（假设驱动 + 风险管理），三板斧是「法」（加减验证），ABCD 是「场景定位器」，业务公式是「术」（把定性假设拆到 L1-L6 可验证参数）。四者本应是一张总框架卡的四根柱子，目前散落在 15+ 张卡里，没有统摄。

---

## 二、素材证据（带路径 / 行号）

### 2.1 关键假设主线（Truman 口述，全篇 3234 行）

| # | 证据点 | 精确来源 |
|---|--------|---------|
| 1 | 课程定位：第一节必修课、听过人数最多、六轮升级、商业必修课 | `00_inbox/一堂-关键假设课-truman-口述.txt:22-62, 104` |
| 2 | 核心命题：「用假设来驱动业务」「你这个业务/渠道/产品的关键假设是什么」 | 同上 `:364-372` |
| 3 | 关键假设定义与 Y 模型引出 | 同上 `:388-402` |
| 4 | 「Idea 往往不值钱，背后的关键假设才价值千金」 | 同上 `:584` |
| 5 | 「不要把创业理解成铁板一块，识别风险最高的关键假设」 | 同上 `:818` |
| 6 | 直面失败、拆假设远好过没假设意识 | 同上 `:962-982` |
| 7 | **三板斧**：先做加法再减法最后快速验证；加法=解构要素、减法=找风险最高、验证=最便宜策略 | 同上 `:1064-1074` |
| 8 | 五步法早期即用在自己身上测关键假设；五步法天然包含精益/关键假设/假设驱动 | 同上 `:1560, 1644` |
| 9 | 「如果某一个关键假设失败不成立，这个业务有巨大硬伤」 | 同上 `:1810` |
| 10 | 业务成不成取决于关键假设预判成不成；招人看 L3-L5 能否定性定量描述生意 | 同上 `:1982-1998` |
| 11 | **关键假设的本质就是风险管理**；三个方向找关键假设 | 同上 `:2460-2482` |

### 2.2 业务公式拆解（孔源 口述 2576 行 + 笔记 114 行 + 逐字稿 1091 行）

| # | 证据点 | 精确来源 |
|---|--------|---------|
| 12 | ABC 业务模型贯穿全篇 | `00_inbox/关键假设C-拆解业务公式/孔源-业务公式拆解-口述.txt:10, 510` |
| 13 | 业务公式有效三要素：**看得清 / 讲得明 / 做得准** | 同上 `:182-194, 682-694, 2384`；`笔记:24-27` |
| 14 | 十大业务公式范式（让学员「都见过」） | 同上 `:360, 860`；`十大业务公式范式_OCR` |
| 15 | **L1/L2 只是「业务科目」，到不了战略层；L4-L6 才触及本质** | 同上 `:1356-1374, 1692, 1972`；`笔记:49-52` |
| 16 | 拆到 L5/L6 是「洞察本质」，非常难 | 同上 `:1476-1504, 1574, 2418` |
| 17 | 逻辑关系：先切分再转化；明确加减乘除；别一上来先用乘法，先 ABC 相加再乘 | 同上 `:1772, 2324`；`笔记:59-70` |
| 18 | **业务公式 = 关键假设 ABCD 体系「最后一块拼图 / 核心骨架 / 灵魂」**；线下已有五步法训练营、科学决策 ROI 训练营 | 同上 `:2474-2500` |
| 19 | 训练营能力清单：6 层 L1-L6 进阶、五把手术刀、5 种切分维度、4 种拆法、十大算式 | 同上 `:2522-2524`；`笔记:102` |
| 20 | 三大认知突破：多维度分层拆解 / 参数量化（定性→行为指标）/ 逻辑关系验证（区分相关因果） | `笔记:31-71` |
| 21 | 案例口径（均为课程经验值）：私域电商人均贡献、企业培训续费、口腔诊所成交；转化率/复购率行业对照 | `笔记:42-44, 20` |

### 2.3 OCR / 模型图

| 文件 | 关键内容 |
|------|---------|
| `一堂-关键假设-关键假设ABCD模型_paddle_ocr.txt` | YitangABCDStrategyModel：成败问题 + 效率问题；A 商业场景 / B 决策场景（宏观—微观）/ C 增长场景 / D 转化场景 |
| `一堂-关键假设-关键假设三板斧_paddle_ocr.txt` | YitangΩModel：找关键假设（减法）→ 拆解假设（加法）→ 验证（明确目标/坚持/调整/放弃）→ 迭代假设（贝叶斯定理） |
| `一堂-关键假设-商业画布259（9）_paddle_ocr.txt` | 商业画布 2020：细分用户/需求/解决方案/收入/核心指标/核心卖点/替代方案/成本/获客渠道/壁垒 |
| `孔源-业务公式拆解-ABC模型图_paddle_ocr.txt` | A 目标（拆子目标/挑战目标）/ B 参数（关键财务·运营·业务要素·行为动作）/ C 逻辑关系（相关因果/分支路径/+-×÷）；借鉴公式（实事求是）vs 创新公式（解放思想） |
| `孔源-业务公式拆解-6层逻辑关系图_paddle_ocr.txt` | L1 模糊→L2 相关→L3 因果→L4 公式→L5 定量→L6 动态；安慰剂/体温计/方向盘/X 光片/刻度尺/导航仪；R=f(A,B,C)→R=(A+B)×C×D→自建模型 |
| `孔源-业务公式拆解-冰山模型图_paddle_ocr.txt` | L1 基础→L2 财务→L3 分层→L4 转化→L5 创新→L6 魔法参数；从上往下拆解 / 从下往上涌现 |
| `孔源-业务公式拆解-十大业务公式范式_paddle_ocr.txt` | ①流量变现 ②线索转化 ③门店收入 ④用户周期 ⑤连续留存 ⑥工业生产 ⑦脱离成本 ⑧留存节点 ⑨连续动作 ⑩动作节点；关注收入/收益侧，需综合 ROI/单元模型/财务模型 |
| `一堂-关键假设-烤炉案例 / 奶茶案例_paddle_ocr.txt` | 两个验证案例图（与现有 case 卡互补） |
| `一堂-关键假设-五步法259（5）/（2）_paddle_ocr.txt` | 五步法 259 口号图（信息较薄，仅 2 行） |

---

## 三、wiki 现状（已用 Glob/Grep 核实）

### 3.1 已有（存在但分散）

| 类型 | 实际文件 | 状态 | 评价 |
|---|---|---|---|
| concept | `concepts/concept-一堂-key-assumptions.md` | reviewed | 定义清晰，但 `source_refs: pending_archive: src_unknown`，缺口述行号 |
| concept | `concepts/concept-一堂-hypothesis-driven-business-methodology.md` | reviewed | 假设驱动方法论，未关联总框架 |
| concept | `concepts/concept-一堂-business-prediction.md` | reviewed | 业务预测，未关联业务公式总纲 |
| framework/concept | `frameworks/yt-business-formula-abc-model.md` | reviewed | 引用 `10_raw/sources` 归档路径，质量高，但挂在业务公式簇、未接关键假设主线 |
| concept | `concepts/yt-business-formula-six-level-logic.md` | reviewed | 六层逻辑，散落 |
| concept | `concepts/yt-business-formula-ten-paradigms.md` | reviewed | 十大范式，散落 |
| concept | `concepts/yt-business-formula-parameter-iceberg.md` | reviewed | 参数冰山，散落 |
| concept | `concepts/yt-business-formula-l6-essence-formulas.md` | reviewed | L6 本质公式，散落 |
| framework | `frameworks/yt-business-formula-business-pattern-selector.md` | reviewed | 范式选择器 |
| framework | `frameworks/yt-business-formula-qualitative-metrics-library.md` | reviewed | 定性指标库 |
| tool | `tools/tool-一堂-hypothesis-validation-three-axe.md` | reviewed | 三板斧操作工具；`source_refs: pending_archive`，trust_level medium |
| tool | `tools/tool-key-assumptions-check.md` | reviewed | 关键假设检查 |
| tool | `tools/tool-first-principles-assumption-classify.md` | reviewed | 第一性原理假设分类 |
| case | `cases/case-一堂-陈贤敏汉堡-hypothesis-validation.md` | reviewed | 验证案例 |
| case | `cases/case-一堂-无人餐厅-hypothesis-failure.md` | reviewed | 失败案例 |
| dk | `dark-knowledges/dk-mckinsey-hypothesis-driven-pitfalls.md` | reviewed | 麦肯锡假设驱动陷阱 |
| dk | `dark-knowledges/dk-yitang-business-formula-plus-times-trap.md` | reviewed（补审标记） | +× 写错陷阱；`source_person: 孔阳`、`pending_archive` 引用 |

> 旁证（非本域，避免重名）：`framework-lean-abcd-model`（精益）、`yt-decision-abcd-model`（决策）、`framework-yitang-project-abcd-classification`（管项目）均含「ABCD」但分属他域；`raw/ocr/ocr-一堂-科学决策-关键假设abcd模型.md`、`raw/ocr/ocr-一堂-单元模型-abcd策略模型.md` 为原始 OCR，未蒸馏为本域卡。**关键假设 ABCD（YitangABCDStrategyModel）无对应卡。**

### 3.2 缺失（核心缺口）

1. **关键假设主线总框架卡**：统摄「假设驱动命题 + 三板斧骨架 + ABCD 场景 + 风险管理本质 + 与业务公式贯通 + 与五步法第一节必修课关系」。
2. **关键假设 ABCD 模型卡**（A 商业/B 决策/C 增长/D 转化；成败 vs 效率）——与他域 ABCD 显式区分。
3. **关键假设↔业务公式贯通 / 业务公式总纲卡**：落实孔源「业务公式是 ABCD 体系核心骨架/灵魂」（`:2474-2500`），把 7 张 `yt-business-formula-*` 子卡收编成可导航总纲，并打通「定性假设→L1-L6 定量参数」。
4. **三板斧方法骨架卡**（加法/减法/验证/贝叶斯迭代）——与现有 `tool-一堂-hypothesis-validation-three-axe`（操作清单）分工。
5. **本域 orchestrator Agent Spec**：关键假设识别→拆解→验证→定量化的总入口与跨域调度。
6. **现有卡 source_refs 补全**：`concept-一堂-key-assumptions`、`tool-一堂-hypothesis-validation-three-axe` 等仍为 `pending_archive: src_unknown`，缺精确口述行号。

---

## 四、缺口判断与深挖价值

**缺口性质**：不是「知识不存在」，而是「知识已卡片化但未成链、未定量贯通、无入口 Agent」。关键假设侧有定义无总纲；业务公式侧有 7 张叶子无总纲；两侧之间缺孔源亲自点名的「核心骨架/灵魂」贯通。

**深挖价值：高（A-）**

| 维度 | 评级 | 依据 |
|---|---|---|
| 素材完整度 | A | 1 篇主课口述（3234 行）+ 孔源口述/笔记/逐字稿 + 11 张 OCR 模型图齐全，且自带 L1-L6/三板斧/ABCD/ABC/十大范式结构化框架 |
| 理论自洽性 | A | 假设驱动→三板斧→ABCD 场景→业务公式定量化→风险管理，闭环自洽；孔源亲口把业务公式定位为 ABCD 体系「核心骨架/灵魂」 |
| 入口地位 | A | Truman 定义为「第一节必修课」「商业必修课」，是全课程体系入口 |
| wiki 现状 | C+ | 卡片不少但分散、无总纲、无贯通、无 Agent、部分 source_refs 缺失 |
| Agent 必要性 | A | 「识别关键假设→拆 L1-L6→设计最便宜验证」是天然可编排工作流，且是 #141 五步法 orchestrator 的前置入口 |

---

## 五、矛盾 / 差异点

| # | 差异点 | 来源 A | 来源 B | 建议处理 |
|---|--------|--------|--------|---------|
| 1 | **主讲人署名「孔源」vs「孔阳」** | 任务与文件名用「孔源」；目录 `00_inbox/关键假设C-拆解业务公式/孔源-…` | `孔源-业务公式拆解-笔记.txt:5,108` 与 `dk-yitang-business-formula-plus-times-trap`（`source_person: 孔阳`）用「孔阳」 | 新卡 source 标注统一用「孔源（笔记正文作孔阳）」；在贯通卡脚注说明署名差异，避免回链混乱 |
| 2 | **「关键假设 ABCD」与他域 ABCD 同名** | 本域 YitangABCDStrategyModel：商业/决策/增长/转化四场景（成败+效率） | lean/decision/project 三张 ABCD 卡含义不同 | 新建卡显式命名 `关键假设-ABCD模型`，related 互链并注明边界，防误用 |
| 3 | **三板斧「方法骨架」vs 现有「操作工具」** | OCR/口述：加法→减法→验证→贝叶斯迭代（方法论） | `tool-一堂-hypothesis-validation-three-axe`（操作清单） | 新建 framework 讲骨架，tool 讲操作，双向 related，不重复内容 |
| 4 | **业务公式 7 张子卡粒度不一** | abc-model/selector/qualitative-metrics 在 frameworks/ | six-level-logic/ten-paradigms/parameter-iceberg/l6-essence 在 concepts/ | 用一张「业务公式总纲」framework 统摄导航，不搬动现有卡，仅补 related |
| 5 | **「业务公式 = 关键假设 ABCD 核心骨架」 vs 现有归类** | 孔源 `:2474-2500` 明确归属关键假设 ABCD 体系 | 现有 `yt-business-formula-*` 挂 yitang/management，无关键假设回链 | 总纲卡建立关键假设→业务公式单向/双向 related，正名归属 |

---

## 六、可直接 Agent 化的环节

| # | Agent 环节 | 解决的问题 | 输入 | 输出 | 调用/转交 | 边界风险 |
|---|---|---|---|---|---|---|
| 1 | 关键假设识别 | 用户说不清业务依赖什么前提 | 业务描述 | 关键假设清单（前置性×风险性排序） | 总框架卡、`tool-key-assumptions-check` | 不能替代行业判断 |
| 2 | 三板斧编排 | 拆解/验证顺序混乱 | 关键假设清单 | 加法解构→减法收敛→最便宜验证方案 | 三板斧卡、`tool-一堂-hypothesis-validation-three-axe` | 避免过早下结论 |
| 3 | ABCD 场景定位 | 不知道问题属哪类 | 业务问题 | 商业/决策/增长/转化归类 + 成败/效率判断 | 关键假设 ABCD 卡 | 防止与他域 ABCD 混淆 |
| 4 | 业务公式定量化 | 假设停在定性、无法验证 | 关键假设 + 业务类型 | ABC 公式 + L1-L6 参数分层 + 最便宜买点 | 业务公式总纲卡 + 7 张子卡 | 不替代财务建模 |
| 5 | 风险/证伪扫描 | 把相关当因果、+× 写错 | 公式草稿 | 因果/相关校验 + +× 符号校验 | `dk-yitang-business-formula-plus-times-trap`、`dk-mckinsey-hypothesis-driven-pitfalls` | 不能预测未来 |
| 6 | 跨域调度 | 需要深入需求/产品/五步法 | 当前阶段 + 问题 | 转交对应子域 Agent | #140 需求、#138 产品内核、#141 五步法 | 调度前先做假设识别 |

---

## 七、本域专属 Agent 设计（草案，详情移交任务 spec）

- **名称**：`agent-一堂-关键假设教练`
- **一句话**：关键假设与业务公式的总入口——帮用户识别关键假设、用三板斧收敛风险、用 ABCD 定位场景、用业务公式拆到 L1-L6 可验证参数，并按需调度子域 Agent。
- **边界**：只提供结构化诊断与验证方案，不替代商业/财务/法务决策；不替他域 Agent 做单步深挖。
- **默认 TCPR**：C（Coach，先识别假设与风险）；问「怎么拆」→ T；共同梳理 → P；有数据要算 → R；想跳过验证直接执行 → C→T 用「Idea 不值钱/风险管理」纠偏。
- **工作流（高层）**：边界确认 → 假设识别 → ABCD 场景定位 → 三板斧收敛（加/减/验证）→ 业务公式 ABC+L1-L6 定量化 → +×/因果校验 → 输出最便宜验证方案 + 风险警示 → 必要时转交 #138/#140/#141。

---

## 八、建议新建 / 升级清单（详见任务 spec）

- **P0**：`framework-一堂-关键假设`（总框架/主线总纲）+ `agent-一堂-关键假设教练`（agent-spec）。
- **P1**：`framework-一堂-关键假设-ABCD模型`、`framework-一堂-关键假设-三板斧`、`framework-一堂-业务公式拆解-总纲`（贯通关键假设 ABCD + 统摄 7 张子卡）。
- **P2**：`tool-一堂-关键假设-ABCD场景分类器`、`tool-一堂-业务公式-L1L6参数分层自检`；并对 `concept-一堂-key-assumptions`、`concept-一堂-hypothesis-driven-business-methodology`、`concept-一堂-business-prediction`、`tool-一堂-hypothesis-validation-three-axe`、`tool-key-assumptions-check`、`tool-first-principles-assumption-classify`、两张 dk、两张 case 做 related/source_refs 升级；7 张 `yt-business-formula-*` 批量回链总纲。

---

## 九、与 #138 / #140 / #141 的衔接关系

- **#141 一堂五步法 orchestrator（最强关联）**：关键假设课 = 五步法商业分析版的「第一节必修课/入口」（truman `:1560,1644` 自述用五步法测关键假设、五步法天然包含假设驱动）。本域总框架卡应作为 #141 总框架卡的「第 0 步/前置入口」被引用；`agent-一堂-关键假设教练` 在 #141 orchestrator 启动时先做假设识别。**依赖 #141 reviewed。**
- **#140 需求分析域（冰山 L1-L6）**：需求冰山的「假设分解」与关键假设识别、业务公式 L1-L6 参数分层同构；本域 ABCD「决策场景/转化场景」可调用 #140 的 L1-L6 工具卡。建议 related 互链，避免重复造冰山。**依赖 #140 reviewed。**
- **#138 产品内核域**：产品内核验证（`yt-product-kernel-hypothesis-test`）本质是关键假设验证在产品阶段的落地；本域三板斧/验证工具是 #138 的内核验证上游。**related 互链。**
- **基础设施依赖**：Agent 注册与入口协议依赖 **#143 跨域双三角诊断 Agent**（域注册扩展协议）；OCR/VLM/检索共享能力依赖 **#144 P-23 能力中台 Phase 1**。

**结论**：本域是 #141 的「第一节必修课前置入口」、#140 的「假设层上游」、#138 的「验证方法上游」。排在 #141 之后入队（编号 #145）最自然。

---

## 十、最终判断与入队建议

**评级：A-（高价值，方法论入口层，建议尽快入队）**

- 来源可靠：主课 + 孔源培训双源，OCR 模型图完整。
- 入口地位突出：Truman 亲定「第一节必修课」，孔源亲定业务公式为「关键假设 ABCD 体系灵魂」。
- 现状是「有料无链」：补足总纲 + ABCD + 贯通 + Agent 即可成网，工程量可控、复用率高。
- 与 #138/#140/#141 形成清晰上下游，不重复造轮子。

**建议入队编号**：`#145`
**任务名称**：`task_20260709_wangyuyan-key-assumptions-business-formula-agent`
**优先级**：P0
**Assignee**：老顽童
**Reviewer**：欧阳锋
**预计产出**：6 张新卡（4 framework + 2 tool）+ 1 个 agent-spec + 约 6-8 张现有卡 related/source_refs 升级 + 7 张业务公式子卡批量回链

---

## 跨域联动边界

> 本诊断是 #141 五步法 orchestrator 的前置入口，可与 [[framework-一堂五步法]]、[[concept-five-step-growth-to-barrier-transition]] 联动；业务公式定量化可复用 #140 需求冰山 L1-L6 工具卡族。

*王语嫣 2026-07-09*
