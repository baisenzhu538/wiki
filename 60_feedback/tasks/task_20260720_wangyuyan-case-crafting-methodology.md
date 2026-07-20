---
id: task_20260720_wangyuyan-case-crafting
task_id: 196
assignee: laowantong
status: queued
created_at: 2026-07-20
updated_at: 2026-07-20
domain: content-production
priority: P1
source: 00_inbox/案例打造法-李頔/
diagnosis: 60_feedback/diagnosis/diag_20260720_wangyuyan-case-crafting-methodology.md
---

# 案例打磨四步法 · 卡片化生产任务

## 任务目标

将李頔（一堂教研负责人/案例中心负责人）的"案例打磨四步法"转化为 KDO wiki 卡片，填补 content-production 域中"案例"这一体裁空白。

## 素材

| 文件 | 路径 |
|:--|:--|
| 口述逐字稿 | `00_inbox/案例打造法-李頔/一堂-案例打磨方法-李頔-口述.txt` |
| 结构化笔记 | `00_inbox/案例打造法-李頔/一堂-案例打磨方法-李頔-笔记.txt` |

## 卡片规格

### P0（骨架卡，2张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 1 | framework-yitang-case-crafting-four-step | framework | 案例打磨四步法 | 四步完整框架：事实复盘(加法)→选定魂儿(减法)→挖专业度(选择)→打磨表达(呈现)；好案例四标准：主线清晰+事实支撑+借假修真+有故事性；每步的核心动作与产出物 |
| 2 | concept-yitang-case-jiejiaxiuzhen | concept | 借假修真：案例是载体，方法论是真经 | 为什么案例不是目的而是手段；教学教材分离的底层逻辑；三个层次的价值传递（同行→类似业务→非同行） |

### P1（工具+暗知识，4张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 3 | tool-yitang-case-fact-review-checklist | tool | 案例事实复盘清单 | 六类事实(起点/问题/过程/节点/结果/弯路) + 自访六问 + 事实池构建方法 + "做了≠必须讲，真实≠重要"筛选原则 |
| 4 | tool-yitang-case-storyline-selector | tool | 案例故事线选择决策树 | 三种故事线(英雄之旅/难题攻坚/时间线)的适用场景判断 + 选择决策树 + 各故事线的经典案例（秦鹏难题攻坚/建模课时间线） |
| 5 | dk-yitang-case-crafting-pitfalls | dk | 案例打磨五大失败模式 | 空(跳过事实复盘)/散(没定魂)/浅(停在What)/听不进(缺表达设计)/包装感(先定主题再找材料) + 识别信号 + 修复方法 |
| 6 | dk-yitang-case-before-after | dk | Before-After对比心法 | 对比四维度（结果/判断方式/工作方式/理解方式）；Before不讲得很蠢（过去往往有合理性）；对比越贴近听众习惯代入感越强 |

### P2（补充层，2张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 7 | concept-yitang-case-soul-selection | concept | 案例定魂：向内三问+向外三问 | 向外的三层（同行学到什么/类似业务借鉴什么/非同行带走什么） + 向内的三层（拿到什么结果/为什么觉得好/做对了什么）；3-5句检验法 |
| 8 | case-yitang-case-crafting-modeling-course | case | 高阶建模课：一次事实复盘的真实过程 | 建模课团队如何通过摊开事实（还原每个模型的初版→迭代→质变的完整过程）提炼出建模方法论；作为四步法第一步的完整演示案例 |

**合��：8张（5新卡 + 3可合并/降级）**

**实际产出**：建议先产 P0(2) + P1(4) = 6张核心卡；P2 的2张可择机补或合并入 P0/P1 的正文节。

## 验收标准

1. 所有卡 source_refs 必须引用口述稿行号（一等证据），不能只引笔记
2. framework 卡必须含：四步流程图、每步的卡点→解法映射、Before-After 案例
3. tool 卡必须可独立执行（读者拿到就能用，不需要先读其他卡）
4. related ≥5 且 ≥2 跨域（必须链接到 framework-yitang-shishi-qiushi / framework-yitang-nine-layer-deep-dig / content-production 系列 / framework-kdo-modeling-methodology）
5. 提交前跑 `kdo pre-submit`

## 已有卡关联（必须建立 related）

| 已有卡 | 关系类型 | 回链要求 |
|:--|:--|:--|
| framework-yitang-shishi-qiushi | 四步法第一步是其案例场景落地 | 关系型（双向） |
| framework-yitang-nine-layer-deep-dig | 挖专业度与9层深挖同构 | 关系型（双向） |
| framework-一堂-表达力火箭模型 | 打磨表达的理论基础 | 引用型（单向） |
| content-production skill系列 | 四步法是内容生产在案例体裁的专项化 | 引用型（单向） |
| framework-kdo-modeling-methodology | 四步法本身是方法论建模产物 | 引用型（单向） |

## 边界说明

- 不覆盖：纯学术案例论文写作（已有 FBR 7-String 等框架）
- 不覆盖：非业务型故事分享
- 不单独建域：归入 content-production 域
