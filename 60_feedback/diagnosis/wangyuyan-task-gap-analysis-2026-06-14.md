# 王语嫣任务深挖：遗漏项与 pipeline 断点诊断

> 面向：欧阳锋、黄药师  
> 来源：老顽童二次深挖  
> 时间：2026-06-14  
> 关联文件：
> - `60_feedback/kcard-batch-migration-feedback-2026-06-14.md`（首次迁移反馈）
> - `60_feedback/issues/fb_20260614_a3d9242a-王语嫣15张卡迁移反馈的独立判断.md`
> - `60_feedback/diagnosis/huangyaoshi-review-wangyuyan-capacity-20260614.md`

---

## 一、已确认完成项

1. **15 张 kcard 草稿已迁入 `30_wiki/`**（第一批 6 张 + 第二批 9 张）
2. **约 72 条 itingnao source 已注册**
3. **`30_wiki/index.md` 已更新**
4. **Lint 定向检查无新增问题**

---

## 二、重大遗漏项

### 2.1 智能药柜 19 张知识卡草稿全部未迁移（P0）

**位置**：`60_feedback/knowledge-cards-draft/`

该目录下共 19 个文件，全部**未进入 `30_wiki/`**：

| 类别 | 数量 | 文件 |
|---|---|---|
| itingnao 录音验证卡 | 6 | `kc_itingnao_*.md` |
| P0 级知识卡 | 6 | `kc_p0_01_*.md` 至 `kc_p0_06_*.md` |
| P1/P2 级知识卡 | 7 | `kc_p1_09_*.md` 至 `kc_p1_15_*.md` |
| 一线验证素材包 | 1 | `field-validation-toolkit.md` |

**风险**：
- 黄药师评估这些卡质量 B+，frontmatter 规范、related 完整、source_refs 可追溯。
- 这批卡是王语嫣 6/13-14 产出的核心成果之一，却被排除在迁移范围外。
- `README.md` 明确要求「待段誉/知识库维护团队复核后迁移」，但任务板中无对应任务。

**建议**：
- 立即将这 19 张卡纳入迁移队列
- 按 P0 → P1 → P2 分级分批迁移
- P0 卡需先完成专业复核（医药监管、财务、法务、O2O 运营）

---

### 2.2 1 张 pending wiki 卡未迁移

**位置**：`60_feedback/pending-wiki-cards/frameworks/sales-pitch-bias-patterns.md`

该文件目标位置 `30_wiki/frameworks/sales-pitch-bias-patterns.md` **不存在**。

**建议**：
- 确认这张卡是否仍有效
- 若有效，按 KDO 流程迁移并注册 source

---

### 2.3 第二批 9 张复合卡 source_refs 不完整

第二批卡片正文引用了 8 份 theme summary，但 frontmatter `source_refs` 中**未注册 theme summary 本身**，只注册了底层 itingnao 录音 src。

具体缺失：

| 卡片 | 正文引用的 theme summary |
|---|---|
| `30_wiki/concepts/ai-hackathon-pitches.md` | `theme-ai-hackathon-pitches-summary.md` |
| `30_wiki/frameworks/ai-methodology-tools.md` | `theme-ai-methodology-tools-summary.md` |
| `30_wiki/concepts/finance-legal-business-operations.md` | `theme-finance-legal-business-summary.md` |
| `30_wiki/concepts/industry-ai-cases.md` | `theme-industry-ai-cases-summary.md` |
| `30_wiki/concepts/business-validation-models-collaboration.md` | `theme-other-summary.md` |
| `30_wiki/concepts/personal-growth-complex-systems.md` | `theme-personal-growth-summary.md` |
| `30_wiki/concepts/product-business-strategy.md` | `theme-product-business-summary.md` |
| `30_wii/concepts/supply-chain-beverage.md` | `theme-supply-chain-beverage-summary.md` |
| `30_wiki/concepts/yitang-methodology-system.md` | `theme-yitang-methodology-summary.md` |

**风险**：
- 读者无法从卡片 frontmatter 直接定位到聚合摘要
- 溯源链断裂：src → theme summary → card 的中间节点缺失

**建议**：
- 将 8 份 theme summary 注册为 source（类型可设为 `theme-summary` 或 `compilation`）
- 补充到对应卡片的 `source_refs` 中

---

### 2.4 68 条 itingnao 录音未进入任何主题摘要

**位置**：`10_raw/itingnao/compact/` 中 177 条录音 vs `90_control/itingnao-kit/work/theme-*-summary.md` 中引用 ID

未覆盖的 68 条主要是：
- 智能药柜/医疗/诊所类
- 硬件/供应链类
- 部分政策合规类

**风险**：
- 这些录音可能包含王语嫣智能药柜 19 张卡的原始素材
- 也可能包含尚未被发现的 dk/case 原料

**建议**：
- 欧阳锋确认这 68 条是已处理但未聚合，还是确实未处理
- 对其中与智能药柜、医疗相关的录音优先聚类摘要

---

### 2.5 4 张 dk 卡缺 confidence 字段（归属老顽童，但与王语嫣素材有关）

**位置**：`30_wiki/dark-knowledges/dk-modeling-*.md`

4 张卡已存在但缺少 `confidence` 字段：
- `dk-modeling-ai-without-judgment.md`
- `dk-modeling-counterexample-driven.md`
- `dk-modeling-essence-predictive.md`
- `dk-modeling-sop-execution-locks.md`

**关键澄清**：
- 这 4 张卡的 `reviewed_by` 是「老顽童」，不是王语嫣。
- 因此**补 confidence 不是王语嫣的任务**，应由老顽童完成。
- 但素材来源（`一堂-建模能力培训-truman-口述.txt`）今天刚进入 `00_inbox/建模能力/`，王语嫣可能负责入口评估。

**建议**：
- 欧阳锋明确分工：王语嫣做口述稿入口质量评估，老顽童补 confidence 与深化内容

---

## 三、流程断点（不是王语嫣个人的遗漏，是 pipeline 问题）

### 3.1 王语嫣角色定义滞后于实际产出

`90_control/AGENTS.md` 定义王语嫣为「Consultant，只诊断、提问、写反馈，不动手」。

但实际产出显示：
- 她写的 kcard 草稿 frontmatter 规范、related 完整、query_triggers 具体
- 黄药师评估部分草稿「质量超过老顽童初稿」

**结果**：她继续按旧角色写 `60_feedback/`，老顽童再从零重写，造成巨大产能浪费。

### 3.2 王语嫣 → 老顽童 的任务管道断裂

黄药师指出：「智能药柜 19 张卡的建议、七件事 4 张卡的转交——全部在等老顽童。但从 dashboard 看，老顽童的任务队列里没有这些。」

**结果**：高质量草稿在 `60_feedback/` 中悬空，未进入任何人的 task list。

### 3.3 Theme summary 本身缺乏质量标记

Kimi 独立判断指出：theme summary 可能是 AI 摘要，存在「摘要偏差」风险，但当前未标记摘要类型（人工/AI/混合）。

---

## 四、优先级建议

| 优先级 | 事项 | 负责人 | 原因 |
|---|---|---|---|
| **P0** | 迁移智能药柜 19 张卡到 `30_wiki/` | 老顽童执行，王语嫣复核 | 核心产出悬空，质量已达 B+ |
| **P0** | 第二批 9 张复合卡原文回填 | 王语嫣 | 未核对原文即入库是污染风险 |
| **P1** | 注册 8 份 theme summary 为 source 并补入 source_refs | 老顽童/欧阳锋 | 修复溯源链 |
| **P1** | 迁移 `pending-wiki-cards/frameworks/sales-pitch-bias-patterns.md` | 老顽童 | 已排队但未执行 |
| **P1** | 给 4 张 `dk-modeling-*` 卡补 confidence 字段 | 老顽童 | 入库门禁会 BLOCK |
| **P2** | 处理 68 条未覆盖 itingnao 录音 | 欧阳锋分配 | 潜在高价值素材 |
| **P2** | 重新定义王语嫣产出边界 | 欧阳锋/黄药师 | 角色滞后于能力，造成浪费 |
| **P2** | 建立王语嫣 → 老顽童 task 转交格式 | 欧阳锋 | 防止产出悬空 |

---

## 五、给欧阳锋和黄药师的判断请求

1. **是否允许王语嫣的草稿「直接入库、老顽童精修」？** 还是继续「王语嫣只写建议，老顽童从零写」？
2. **68 条未覆盖录音** 中，药柜/医疗类是否优先处理？
3. **theme summary 是否需要注册为 source**？以及 summary 质量标记是否要做？

---

## 六、关键文件清单

- 待迁移草稿：`60_feedback/knowledge-cards-draft/*.md`
- 待迁移 pending 卡：`60_feedback/pending-wiki-cards/frameworks/sales-pitch-bias-patterns.md`
- 第二批复合卡：`30_wiki/concepts/ai-hackathon-pitches.md` 等 9 张
- 主题摘要：`90_control/itingnao-kit/work/theme-*-summary.md`
- itingnao 录音：`10_raw/itingnao/compact/*.json`
- 4 张 dk 卡：`30_wiki/dark-knowledges/dk-modeling-*.md`
- 新入口素材：`00_inbox/建模能力/一堂-建模能力培训-truman-口述.txt`
