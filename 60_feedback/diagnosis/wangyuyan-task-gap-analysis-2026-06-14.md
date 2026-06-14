# 王语嫣任务深挖：遗漏项、断点与深度质量要求

> 面向：欧阳锋、黄药师  
> 来源：老顽童二次深挖 + 独立验证  
> 时间：2026-06-14  
> 关联文件：
> - `60_feedback/kcard-batch-migration-feedback-2026-06-14.md`（首次迁移反馈）
> - `60_feedback/issues/fb_20260614_a3d9242a-王语嫣15张卡迁移反馈的独立判断.md`
> - `60_feedback/diagnosis/huangyaoshi-review-wangyuyan-capacity-20260614.md`
> - `60_feedback/knowledge-cards-draft/README.md`

---

## 0. 深度质量标准（本次诊断与后续执行的共同底线）

高质量 ≠ 信息多。深度必须同时满足以下四条：

1. **可验证**：每个核心断言必须能追溯到具体 source（录音 ID、报告页码、访谈对象、时间戳）。
2. **可决策**：每张卡必须回答「这张卡帮读者做什么决定」，而不是只描述现象。
3. **可连接**：卡的 `related` 字段必须指向知识库中已有的工具/框架/案例，避免孤岛。
4. **可迭代**：卡的 `confidence`/`trust_level` 必须诚实，低置信度处必须标注「待原文复核」。

本诊断本身也按此标准执行：不列目录，只列「问题 + 证据 + 根因 + 验收标准」。

---

## 一、已确认完成项（附证据）

| 事项 | 证据 |
|---|---|
| 15 张 kcard 草稿迁入 `30_wiki/` | `30_wiki/concepts/fd-forward-deployment.md` 等 15 个文件存在，索引已更新 |
| 约 72 条 itingnao source 注册 | `90_control/source-registry.yaml` 中 `src_20260614` 出现 166 次，对应约 72 条新增 source |
| `30_wiki/index.md` 更新 | 已追加 15 条标准 Markdown 链接 |
| Lint 定向检查无新增问题 | 对 15 张新卡 grep 未命中 ERROR/WARNING |

---

## 二、重大遗漏项（含具体证据与根因）

### 2.1 智能药柜 19 张知识卡草稿全部未迁移（P0）

#### 问题
`60_feedback/knowledge-cards-draft/` 下 19 个文件，frontmatter 完整、质量 B+，但**全部未进入 `30_wiki/]`**。

#### 具体证据
以 `kc_p0_01_national-policy-redlines.md` 为例：

```yaml
---
id: "kc-p0-01-national-policy-redlines"
confidence: 0.95
domain:
  - "healthcare"
  - "pharmaceutical-retail"
  - "policy-compliance"
query_triggers:
  - "自助售药机能卖什么药"
  - "智能药柜政策红线"
  - "药柜能不能卖处方药"
related:
  - "kc-p0-02-regional-policy-map"
  - "master-decision-hygiene"
  - "master-systems-thinking"
source_refs:
  - "corr_20260613_smart-medicine-cabinet-iteration-4-policy-compliance.md"
  - "国家药监局 2024 年第 48 号公告"
trust_level: "high"
---
```

该卡已有：
- 明确的决策问题（能不能卖处方药）
- 5 个具体 query_triggers
- 7 个 related 链接
- 0.95 confidence 和 high trust_level

这已经不是「草稿」，而是可直接入库的资产。

#### 根因分析
1. **任务边界定义错误**：`README.md` 写明「待段誉/知识库维护团队复核后迁移」，但「段誉/知识库维护团队」这个角色在项目任务板中不存在。
2. **pipeline 断点**：黄药师指出「老顽童的任务队列里没有这些」。产出→执行的管道没有打通。
3. **批量处理惯性**：本次迁移只处理了用户明确提到的「15 张卡」，没有主动扫描 `60_feedback/` 下其他已就绪资产。

#### 验收标准
- [ ] 19 张卡按 P0 → P1 → P2 分级迁移到 `30_wiki/`
- [ ] P0 卡需先完成专业复核（医药监管、财务、法务、O2O 运营）
- [ ] 迁移时统一 `source_refs` 格式（见 §2.3）
- [ ] 迁移后在 `30_wiki/index.md` 添加索引
- [ ] 运行 `kdo lint`，确保无新增 ERROR/WARNING

---

### 2.2 1 张 pending wiki 卡未迁移（P1）

#### 问题
`60_feedback/pending-wiki-cards/frameworks/sales-pitch-bias-patterns.md` 已获欧阳锋 A 级评审（`review_grade: "A"`、`confidence: 0.92`、`status: reviewed`），但目标位置 `30_wiki/frameworks/sales-pitch-bias-patterns.md` **不存在**。

#### 具体证据
该卡 frontmatter：

```yaml
title: "销售话术偏误识别模式库"
type: framework
status: reviewed
review_grade: "A"
reviewed_by: "欧阳锋"
review_date: "2026-06-13"
review_note: "🟢放行。方法论资产，可复用于任何供应商评估。"
confidence: 0.92
```

#### 根因分析
这是一个已评审通过、等待入库的卡，但没有被纳入本次迁移范围。说明 pending-wiki-cards 目录没有被当作迁移输入源扫描。

#### 验收标准
- [ ] 确认卡是否仍有效（欧阳锋已放行，应有效）
- [ ] 迁移到 `30_wiki/frameworks/sales-pitch-bias-patterns.md`
- [ ] 注册 source（当前 `source_refs: ["src_20260613_qishijian_transcript"]` 需确认是否存在）
- [ ] 更新 `30_wiki/index.md`

---

### 2.3 第二批 9 张复合卡 source_refs 不完整（P1）

#### 问题
第二批卡片正文引用了 8 份 theme summary，但 frontmatter `source_refs` 中**只注册了底层 itingnao 录音 src，未注册 theme summary 本身**。

#### 具体证据
以 `30_wiki/concepts/ai-hackathon-pitches.md` 为例：

- 正文第 2 段明确写：「本卡基于 `90_control/itingnao-kit/work/theme-ai-hackathon-pitches-summary.md` 中的 11 条录音 meetingSummary 摘要提炼而成。」
- 正文还列出了 11 个原始录音 ID（`rec-4023226` 到 `rec-4046714`）。
- 但 frontmatter `source_refs` 只包含 src 列表，没有 `theme-ai-hackathon-pitches-summary.md` 对应的 source ID。

其他 8 张卡情况相同：

| 卡片 | 正文引用的 theme summary |
|---|---|
| `30_wiki/concepts/ai-hackathon-pitches.md` | `theme-ai-hackathon-pitches-summary.md` |
| `30_wiki/frameworks/ai-methodology-tools.md` | `theme-ai-methodology-tools-summary.md` |
| `30_wiki/concepts/finance-legal-business-operations.md` | `theme-finance-legal-business-summary.md` |
| `30_wiki/concepts/industry-ai-cases.md` | `theme-industry-ai-cases-summary.md` |
| `30_wiki/concepts/business-validation-models-collaboration.md` | `theme-other-summary.md` |
| `30_wiki/concepts/personal-growth-complex-systems.md` | `theme-personal-growth-summary.md` |
| `30_wiki/concepts/product-business-strategy.md` | `theme-product-business-summary.md` |
| `30_wiki/concepts/supply-chain-beverage.md` | `theme-supply-chain-beverage-summary.md` |
| `30_wiki/concepts/yitang-methodology-system.md` | `theme-yitang-methodology-summary.md` |

#### 根因分析
1. 迁移时只把 itingnao 录音当作 source，没有把 AI/人工生成的 theme summary 当作中间产物纳入溯源。
2. theme summary 本身尚未注册到 `90_control/source-registry.yaml`。
3. 没有统一的 source 类型定义：录音是 `transcript`，theme summary 应该是 `compilation` 或 `theme-summary`。

#### 验收标准
- [ ] 8 份 theme summary 注册为 source，类型建议 `compilation`
- [ ] 每份 theme summary 的 source 记录包含：生成方式（AI/人工/混合）、摘要时间、覆盖录音列表
- [ ] 9 张卡的 `source_refs` 同时包含：theme summary source + 底层 itingnao src
- [ ] 正文中「rec-XXXXXXX」列表可保留，但需确保对应 src 已注册

---

### 2.4 68 条 itingnao 录音未进入任何主题摘要（P2）

#### 问题
`10_raw/itingnao/compact/` 共有 177 条录音，其中 **68 条（38.4%）未出现在任何 theme summary 中**。

#### 具体证据
通过脚本比对 `compact/` 中的文件名 ID 与 `90_control/itingnao-kit/work/` 中所有 `.md`/`.json` 文件引用的 ID：

```
compact total: 177
theme_ids found: 339（含重复引用）
uncovered count: 68
first 30 uncovered:
1241665, 1254543, 1396750, 1422729, 1428540, 1485627,
1595288, 1708003, 1883124, 2083979, 2132253, 2354777,
2431721, 2447560, 2690270, 2793285, 4202631, 4205951,
4376859, 4528361, 4785075, 4873420, 4880681, 4921466,
5019929, 5129381, 5132055, 5404488, 5422235, 5512553
```

#### 根因分析
1. 本次 theme summary 只覆盖了 8 个非药柜主题（AI 方法论、个人成长、产品商业等）。
2. 智能药柜/医疗/诊所/硬件供应链类录音（约 72 条聚焦录音）未被系统聚类。
3. `focused-index.json` 虽已识别 72 条重点录音，但没有生成对应的 theme summary。

#### 验收标准
- [ ] 欧阳锋确认这 68 条是「已处理但未聚合」还是「确实未处理」
- [ ] 对药柜/医疗/供应链相关录音生成 3-5 份 theme summary
- [ ] 对其中高价值录音直接生成 concept/case/dk 卡
- [ ] 更新 `10_raw/itingnao/focused-progress.json`，记录处理状态

---

### 2.5 4 张 dk 卡缺 confidence 字段（归属老顽童，但与王语嫣入口评估有关）

#### 问题
`30_wiki/dark-knowledges/` 下 4 张建模类 dk 卡缺少 `confidence` 字段：

- `dk-modeling-ai-without-judgment.md`
- `dk-modeling-counterexample-driven.md`
- `dk-modeling-essence-predictive.md`
- `dk-modeling-sop-execution-locks.md`

#### 关键澄清
- 这 4 张卡的 `reviewed_by` 是「老顽童」，不是王语嫣。
- **补 confidence 不是王语嫣的任务**，应由老顽童完成。
- 但今天 `00_inbox/建模能力/` 刚进入新素材 `一堂-建模能力培训-truman-口述.txt`，王语嫣可能负责入口质量评估。

#### 根因分析
1. dk 卡 schema 对 `confidence` 字段未强制，但入库门禁会检查。
2. 老顽童在批量产卡时 frontmatter 格式不统一（有的有 confidence，有的没有）。
3. 新口述稿到达后，没有自动触发「是否覆盖/补充现有 dk 卡」的评估流程。

#### 验收标准
- [ ] 老顽童给 4 张 dk 卡添加 `confidence` 字段（参考同批次其他卡可填 `0.85`）
- [ ] 统一 `source_person` 写法（当前 4 张均为 `Truman`，但需确认一致性）
- [ ] 王语嫣对新口述稿做入口质量评估，判断是否需要补充/替换现有 dk 卡内容
- [ ] 运行 `kdo validate` 确认无 schema 错误

---

## 三、流程断点：不是王语嫣个人的遗漏

### 3.1 角色定义滞后于实际产出

#### 证据
`90_control/AGENTS.md` 定义王语嫣为「Consultant，只诊断、提问、写反馈，不动手」。

但黄药师审查发现：
> "`60_feedback/knowledge-cards-draft/` 下 16 张卡，包含完整 frontmatter（id、type、domain、related、source_refs、query_triggers）。格式比很多已入库的卡还规范。`kc_p0_01_national-policy-redlines.md` 的 related 字段挂了 7 张卡，source_refs 指向真实的调研报告，query_triggers 包含 5 个具体的搜索触发词。这不是诊断——这是在生产。"

#### 根因
角色定义基于「王语嫣只能写文字建议」的假设，但实际她的产出已达到可直接入库水平。继续按旧角色执行，造成：
- 王语嫣写草稿 → 老顽童从零重写 → 双份劳动
- 高质量草稿在 `60_feedback/` 中悬空

#### 深度建议
欧阳锋需要做一个二元决策：

**选项 A：升级王语嫣为「草稿生产者」**
- 允许她直接产出带 frontmatter 的知识卡草稿
- 老顽童从「从零写」改为「精修 + 入库」
- 王语嫣的输出直接进入 `60_feedback/knowledge-cards-draft/`，评审后迁移

**选项 B：严格限制为 Consultant**
- 王语嫣只写诊断报告和转交清单
- 老顽童根据清单从零生产
- 但当前 19 张药柜卡需要明确转交人和截止时间

**推荐选项 A**，因为黄药师已证明她的草稿质量超过老顽童初稿。

---

### 3.2 王语嫣 → 老顽童 的任务管道断裂

#### 证据
黄药师指出：
> "智能药柜 19 张卡的建议、七件事 4 张卡的转交——全部在等老顽童。但从 dashboard 看，老顽童的任务队列里没有这些。"

#### 根因
没有标准化的「转交格式」。口头交代、文件命名、目录放置都不够强制，导致任务在交接处丢失。

#### 深度建议：建立标准转交模板

在 `70_product/tasks/` 下为每一次王语嫣 → 老顽童转交创建文件：

```markdown
## 转交批次：<主题> <日期>

| # | 卡ID | 类型 | 优先级 | 来源诊断 | 状态 | 验收标准 |
|---|------|------|--------|----------|------|----------|
| 1 | kc-p0-01-national-policy-redlines | concept | P0 | 智能药柜 iteration-4 | 草稿已就绪 | 复核政策内容后迁入 30_wiki |
| 2 | kc-p0-02-regional-policy-map | concept | P0 | 智能药柜 iteration-4 | 草稿已就绪 | 补充各省最新政策后入库 |

## 阻塞项
- P0-1 需医药监管同事复核
- P0-3 需财务模型假设复核

## 建议执行人
- 老顽童：迁移与精修
- 王语嫣：复核入口质量
```

---

### 3.3 Theme summary 质量未标记

#### 证据
8 份 theme summary 均由 AI 从 itingnao meetingSummary 聚合生成，但文件中没有：
- 生成方式标记（AI/人工/混合）
- 摘要时间
- 覆盖录音完整列表
- 置信度自评

#### 根因
itingnao-kit 的摘要脚本只输出内容，不输出元数据。

#### 深度建议
每份 theme summary 头部增加标准元数据块：

```yaml
---
generated_by: ai-summary-v1.2
reviewed_by: ""
generation_date: 2026-06-14
source_count: 11
source_ids:
  - 4023226
  - 4023228
  - ...
confidence: 0.75  # AI 摘要默认降级
---
```

---

## 四、优先级与执行建议

| 优先级 | 事项 | 负责人 | 原因 | 验收标准 |
|---|---|---|---|---|
| **P0** | 迁移智能药柜 19 张卡 | 老顽童执行，王语嫣复核 | 核心产出悬空，质量 B+ | 迁入 30_wiki/，index 更新，lint 通过 |
| **P0** | 第二批 9 张复合卡原文回填 | 王语嫣 | 未核对原文即入库是污染风险 | 每个低置信断言补原文证据 |
| **P1** | 注册 8 份 theme summary 为 source | 老顽童/欧阳锋 | 修复溯源链 | source_refs 包含 theme summary source |
| **P1** | 迁移 sales-pitch-bias-patterns.md | 老顽童 | 已获欧阳锋 A 级放行 | 迁入 30_wiki/frameworks/ |
| **P1** | 给 4 张 dk-modeling-* 卡补 confidence | 老顽童 | 入库门禁会 BLOCK | validate 通过 |
| **P2** | 处理 68 条未覆盖 itingnao 录音 | 欧阳锋分配 | 潜在高价值素材 | 生成 theme summary 或直接产卡 |
| **P2** | 重新定义王语嫣产出边界 | 欧阳锋/黄药师 | 角色滞后于能力 | 发布角色更新到 AGENTS.md |
| **P2** | 建立标准转交模板 | 欧阳锋 | 防止产出悬空 | 70_product/tasks/ 下有标准格式 |

---

## 五、需要欧阳锋和黄药师拍板的三个问题

1. **王语嫣是否可以升级为「草稿生产者」？** 即：她的知识卡草稿经评审后可直接进入迁移队列，老顽童只负责精修和最终入库。
2. **68 条未覆盖录音中，药柜/医疗/供应链类是否优先处理？** 如果需要，建议由欧阳锋分配 3-5 个 theme summary 任务。
3. **theme summary 是否应注册为独立 source 并标记生成方式？** 这是溯源链完整性的关键，但会增加 source 注册表复杂度。

---

## 六、关键文件清单

| 路径 | 说明 |
|---|---|
| `60_feedback/knowledge-cards-draft/*.md` | 待迁移的 19 张智能药柜卡 |
| `60_feedback/pending-wiki-cards/frameworks/sales-pitch-bias-patterns.md` | 已评审通过但未迁移的 framework |
| `30_wiki/concepts/ai-hackathon-pitches.md` 等 9 张 | 第二批复合卡，需补 source_refs 和原文 |
| `90_control/itingnao-kit/work/theme-*-summary.md` | 8 份未注册 source 的主题摘要 |
| `10_raw/itingnao/compact/*.json` | 177 条录音，其中 68 条未覆盖 |
| `30_wiki/dark-knowledges/dk-modeling-*.md` | 4 张缺 confidence 的 dk 卡 |
| `00_inbox/建模能力/一堂-建模能力培训-truman-口述.txt` | 新到达的口述稿素材 |
| `60_feedback/diagnosis/huangyaoshi-review-wangyuyan-capacity-20260614.md` | 黄药师对王语嫣产能的完整评估 |

---

## 七、本诊断自身的局限

1. 未读取 68 条未覆盖录音的具体内容，只是做了 ID 比对。
2. 未对 19 张药柜卡做内容深度复核，只是抽样检查了 `kc_p0_01` 的 frontmatter。
3. 未验证 `90_control/source-registry.yaml` 中 72 条新增 source 的元数据质量（这是欧阳锋的任务）。

如需我继续对某一项做更深入的逐文件检查，请指定具体范围。
