---
id: task_20260720_wangyuyan-ai-video-tool
task_id: 197
assignee: hermes
status: queued
created_at: 2026-07-20
updated_at: '2026-07-21T19:30:00.000000+00:00'
domain: ai-collaboration
priority: P1
source: 00_inbox/AI口播工具开发经验/
diagnosis: 60_feedback/diagnosis/diag_20260720_wangyuyan-ai-video-tool-dev.md
review_audit: 60_feedback/audit/audit-20260721-wangyuyan-197-198-pre-review.md
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

---

## 补审记录（欧阳锋，2026-07-21）

**异常说明**：Hermes 老顽童提交 #197 后，`queue_transition.py review --verdict fail` 执行时报"任务197不在队列中"错误，但队列条目被异常标记为 `reviewed`。手动修正队列和任务单状态为 `queued`。

**终审结论**：🔴 **FAIL — 退回修复**

### 🔴 必须修复（4项，阻塞通过）

| # | 问题 | 影响范围 |
|---|------|----------|
| 1 | `diagnostic_signals` 字段全局缺失 | 全部 8 张卡 |
| 2 | 3 张 dk 卡缺少独立 Critique section（dk 六段要求含外部批判） | dk-ai-video-common-pitfalls, dk-post-hoc-framework-vs-messy-reality, dk-market-info-gap-to-product-strategy |
| 3 | dk-post-hoc 和 dk-market-info 在 `dark-knowledges/` 有旧版残留（diff 确认是同一张卡的旧 frontmatter）——需删除旧版 | 2 张 |
| 4 | `tool-ai-video-cost-optimization` related 仅 3 个，验收标准要求 ≥5 | 1 张 |

### 🟡 建议修复（3项，入库前应修）

| # | 问题 | 说明 |
|---|------|------|
| 5 | concept 卡仅 1 个外部攻击者（Opus.pro），建议补到 ≥2 | 可补组件化文献/Design Token 研究 |
| 6 | 4 张 tool/dk 卡无外部 Critique（tool-market, tool-cost, dk-pitfalls, dk-market-info） | 各补 1-2 个 |
| 7 | dk-pitfalls related 仅 4 个 | 差 1 个达标 |

### ✅ 亮点

- framework 卡 §A/§B 双面呈现设计优秀——"复盘框架 vs 真实执行顺序"的诚实标注
- 全部 related 外链 ID 实际存在（lint 报死链为跨目录查找限制）
- 行号引用精确，Claims/Evidence/Synthesis/Action Triggers/Failure Modes 完整
- 跨域桥接设计合理

---

## 复核后修复清单（王语嫣 2026-07-21 追加）

> 复核报告：`60_feedback/audit/audit-20260721-wangyuyan-197-198-pre-review.md`  
> 本任务单已退回 `queued`，修复完成后再提交 `pending_review`。

### 🔴 阻塞项（必须修复）

| # | 问题 | 修复动作 | 验收标准 |
|:---|:---|:---|:---|
| 1 | **重复版本冲突** | 合并 `30_wiki/ai-collaboration/` 与标准目录的重复卡片 | 每个 ID 只在标准目录存在一份 canonical 版本 |
| 2 | **增量 dk 卡无标准目录版本** | 在 `dark-knowledges/` 下为两张增量 dk 卡建标准版本 | `dk-post-hoc-framework-vs-messy-reality` 和 `dk-market-info-gap-to-product-strategy` 各在 `dark-knowledges/` 有一份 |
| 3 | **`diagnostic_signals` 占位符** | 合并时保留标准目录的真实 ds，删除 ai-collaboration/ 的 placeholder | 全部 8 张卡 ds ≥2 且为真实信号 |
| 4 | **`dk-ai-video-common-pitfalls` related=4** | 补充 1 个相关卡 | related ≥5 |
| 5 | **3 张 dk 卡 Critique 确认** | 确保标准目录版本的 3 张 dk 卡均含独立 Critique section | 每张 dk 卡有 ≥1 条外部批判 |

### 🟡 建议修复

| # | 问题 | 说明 |
|:---|:---|:---|
| 6 | concept 卡外部攻击者 ≥2 | 当前仅 Opus.pro |
| 7 | 4 张 tool/dk 卡外部 Critique | tool-market、tool-cost、dk-pitfalls、dk-market-info |

### 修复后流程

1. 老顽童/Hermes 按清单修复
2. 跑 `kdo pre-submit` 和 `kdo lint`
3. 确认无重复 ID、无跨目录死链
4. 提交 `pending_review`

---

## 修复后验证结果（王语嫣 2026-07-21）

### ✅ 已完成

- 6 份 `ai-collaboration/` 副本已删除
- 2 张增量 dk 卡已移入 `dark-knowledges/`
- 无重复 ID

### ❌ 仍未达标（从 pending_review 退回 queued）

| 卡片 | 问题 |
|:---|:---|
| `framework-ai-video-production-aesthetics-first` | **缺 Critique** |
| `concept-ai-video-wanggan-componentization` | **缺 Critique** |
| `tool-ai-video-market-gap-assessment` | **缺 Critique** |
| `tool-ai-video-cost-optimization` | **缺 Critique** |
| `case-fuzeyu-ai-koubo-tool-dev` | **缺 Critique** |
| `dk-ai-video-common-pitfalls` | **related=4**，未达 ≥5 |
| `dk-post-hoc-framework-vs-messy-reality` | **`diagnostic_signals` 仍是占位符** |
| `dk-market-info-gap-to-product-strategy` | **`diagnostic_signals` 仍是占位符** |

**结论**：重复清理完成，但内容修复未完成。已退回 `queued`，补齐后再提交终审。
