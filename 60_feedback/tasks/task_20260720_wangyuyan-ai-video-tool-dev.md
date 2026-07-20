---
id: task_20260720_wangyuyan-ai-video-tool
task_id: 197
assignee: hermes
status: reviewed
created_at: 2026-07-20
updated_at: '2026-07-20T17:02:34.471570+00:00'
domain: ai-collaboration
priority: P1
source: 00_inbox/AI口播工具开发经验/
diagnosis: 60_feedback/diagnosis/diag_20260720_wangyuyan-ai-video-tool-dev.md
reviewed_by: 欧阳锋
review_date: '2026-07-20'
grade: A
---

# AI口播工具开发经验 · 卡片化生产任务

## 任务目标

将付则宇的"AI口播短视频自动化工具开发经验"转化为KDO wiki卡片，聚焦**审美优先→网感组件化→AI自动化**的方法论提取。

## 素材

| 文件 | 路径 |
|:--|:--|
| 口述逐字稿 | `00_inbox/AI口播工具开发经验/AI口播工具开发经验分享-付则宇-口述.txt` |
| 结构化笔记 | `00_inbox/AI口播工具开发经验/AI口播工具开发经验分享-付则宇-笔记.txt` |

## 卡片规格

### P0（骨架卡，2张）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 1 | framework-ai-video-production-aesthetics-first | framework | AI产品开发·审美与体系的分工 | 🔴修正：双面呈现。§A 复盘后的认知框架（四步法：拆→建→推→练）+ §B 真实过程的教训（L1754-1760：实际顺序是反的——先追Hyper Friends一个月→发现不对→才回头拆视频）。§哲学基础："审美负责定义结果，体系负责让结果重复发生"(L1786-1794)。三层账本(认知/时间/经济) |
| 2 | concept-ai-video-wanggan-componentization | concept | 网感组件化：画面节奏+元素搭配的可量化体系 | 9类视频分类(竖屏怼脸/横屏专业/画中画/重剪辑/人像板书/表演型/信息流/含装饰/纯素材)；网感四要素(画面节奏/字幕/动画/音效)；"剪映几百个动画，常用就小几十个" |

### P1（工具+暗知识+案例，6张：4原卡 + 2增量）

| # | id | type | title | 核心内容 |
|:--|:--|:--|:--|:--|
| 3 | tool-ai-video-market-gap-assessment | tool | AI工具市场信息差评估矩阵 | 先建审美标准→用标准量现有工具→判断自建vs借用。含：审美标准定义模板、工具能力边界测试清单、信息差判断三问 |
| 4 | tool-ai-video-cost-optimization | tool | AI工具开发成本优化清单 | 企业认证多账号薅羊毛/中转商API(测试期按次付费)/百度秒达免费短信验证。含成本对比表(正规API vs 中转商，差价10-50倍) |
| 5 | dk-ai-video-common-pitfalls | dk | AI视频工具开发五大失败模式 | 调研无标准(凭感觉)/技术先于审美(Hyper Freaks1个月教训)/过度依赖AI分析/工具边界不清/忽略市场信息差 |
| 6 | case-fuzeyu-ai-koubo-tool-dev | case | 付则宇AI口播工具：从16小时到零门槛 | 完整案例：首条视频→痛点发现→300+视频拆解→组件化→AI串联→产品落地。含关键数据(1700播放→20咨询→1海外订单)和关键决策(为什么不用数字人/为什么选商用API优先) |
| 🔴7 | dk-post-hoc-framework-vs-messy-reality | dk | 真实过程≠复盘结构 | 🔴深挖增量：付则宇L1754-1760亲述实际顺序是反的。四步法=事后认知重构。含：为什么人会事后合理化、复盘时如何区分真实过程和方法论提炼 |
| 🔴8 | dk-market-info-gap-to-product-strategy | dk | 市场信息差→产品策略决策链 | 🔴深挖增量：L878-920完整推理——老工具仍有人不知→渗透率极低→用户不要认知要结果→零门槛+80分>100分。含论证链模板 |

**合计：8张（2 P0 + 6 P1）** — 2026-07-20 深挖迭代追加2张dk

## 验收标准

1. 所有卡 source_refs 必须引用口述稿行号
2. framework 卡必须含：四步法流程图（与四字诀对齐）、三层账本框架、市场信息差论证
3. tool 卡必须可独立执行
4. related ≥5 且 ≥2 跨域
5. 提交前跑 `kdo pre-submit`

## 已有卡关联（必须建立 related）

**核心发现：付则宇的"审美→组件化→自动化"与四字诀「拆建推练」完全同构，且与#196案例打磨四步法同源。**

### 关系型（双向，必须）

| 已有卡 | 同构关系 | 回链内容 |
|:--|:--|:--|
| framework-一堂-基本功-四字诀拆建推练 | 方法论骨架同构：拆(视频网感)→建(组件)→推(AI串联)→练(批量产出) | 四字诀卡新增"AI产品开发"作为场景实例 |
| framework-yitang-case-crafting-four-step (#196) | 同源四步法结构：都是"拆→建→推→练"，不同域(案例打磨vs产品开发)，互相印证 | #196卡新增related链接 |
| framework-一堂-表达力火箭模型 | 产品审美递进：卖点(80分标准)→专业度(组件化规则)→打动(网感节奏)→逐字稿(AI模板) | 火箭模型卡新增"AI视频产品"作为应用场景 |

### 引用型（单向，必须）

| 已有卡 | 关系 | 引用内容 |
|:--|:--|:--|
| framework-wanghuan-harness-seven-stages | AI产品开发的完整流程框架 | framework卡引用Harness作为产品开发方法论依据 |
| framework-yitang-research-weapon-system | 300+视频拆解=调研武器库实战应用 | case/ tool卡引用调研武器库 |
| framework-一堂五步法-单元模型 | 三层账本的成本量化逻辑 | concept卡引用单元模型思维 |

## 域归属

归入 **ai-collaboration** 域（AI产品开发方法论），同时与 content-production 域（短视频内容生产）桥接。

## 边界说明

- 不覆盖：纯技术实现细节（代码/API对接文档）
- 不覆盖：通用短视频运营策略（选题/账号定位）
- 不单独建域：方法论层面归入 ai-collaboration，案例可被 content-production 域引用
