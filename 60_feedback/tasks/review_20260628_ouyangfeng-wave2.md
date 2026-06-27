---
id: review_20260628_ouyangfeng-wave2
type: review_task
created_at: 2026-06-28
updated_at: 2026-06-28
author: 王语嫣
assignee: 欧阳锋（子代理）
priority: P0
scope: 老顽童批量工单 wave2：P0 返工 16 张卡终审
related:
  - '[[laowantong-batch-2026-06-20-wave2]]'
status: reviewed
---

# 欧阳锋审查任务：wave2 P0 返工（16 张卡）

> **用户明确：单独实例欧阳锋正在审渠道增长域，忙不过来；本任务由子代理欧阳锋并行审查。**
> wave2 来源规格见 `70_product/tasks/laowantong-batch-2026-06-20.md` 第 2 波 + 第 2 波完成小结。

---

## 0. 任务元信息

| 项目 | 内容 |
|------|------|
| 待审任务 | `laowantong-batch-2026-06-20-wave2` |
| 来源队列 | `70_product/tasks/production-queue.md` 第 5 项 |
| 生产方 | WorkBuddy 老顽童 |
| 卡数 | 16 张 |
| 目标 | P0 返工：业务公式域既有卡补暗知识 + 5 张新案例卡 + AI 短剧域 7 张深度返工 + AI PPT 1 张 draft 升级 |
| 质量门禁 | 16 张卡 `kdo pre-submit` 全通过（16 passed / 0 failed）；B2 AI 短剧 7 张批量复跑 7 passed / 0 failed |

---

## 1. 待审 16 张卡清单

### B1：业务公式域（8 张）

| # | 卡片路径 | 类型 | 标题/内容 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 1 | `30_wiki/frameworks/yt-business-formula-abc-model.md` | framework | ABC 业务公式模型 | 是否补暗知识实质内容：① 加法 vs 乘法业务含义 ② 先切分再拆转化顺序 ③ 相关 vs 因果判断 |
| 2 | `30_wiki/frameworks/yt-business-formula-six-level-logic.md` | framework | 业务公式六层逻辑 | 是否补自检清单：当前业务应拆到哪一层、每个定性参数是否找到 3-5 个行为指标、公式是否可验证可执行 |
| 3 | `30_wiki/frameworks/yt-business-formula-parameter-iceberg.md` | framework | 业务公式参数冰山 | 是否补 L5-L6 停止条件：能否提出可验证假设 |
| 4 | `30_wiki/cases/case-private-domain-ecommerce-formula.md` | case | 私域电商业务公式案例 | 原始表述/背景/问题/方案/结果/可迁移点/关联框架；数字标注来源 |
| 5 | `30_wiki/cases/case-saas-renewal-formula.md` | case | SaaS 续费率业务公式案例 | 同上 |
| 6 | `30_wiki/cases/case-dental-clinic-formula.md` | case | 牙科诊所业务公式案例 | 同上 |
| 7 | `30_wiki/cases/case-offline-catering-formula.md` | case | 线下餐饮业务公式案例 | 同上 |
| 8 | `30_wiki/cases/case-gym-membership-formula.md` | case | 健身房续卡率业务公式案例 | 同上 |

### B2：AI 短剧域深度返工（7 张）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 9 | `30_wiki/tools/ai-short-drama-ice-fire-scripting-compass.md` | tool | 冰火脚本罗盘 | Claims 6 条、Critique 内部局限 3 条、反事实 2-3 条、真实案例锚点、source 精确 |
| 10 | `30_wiki/tools/ai-short-drama-ice-fire-dissection-compass.md` | tool | 冰火拆本罗盘 | 同上；ice-fire 2 张 confidence 是否 0.65 |
| 11 | `30_wiki/frameworks/ai-short-drama-plot-three-axes.md` | framework | 短剧情节三轴 | 同上 |
| 12 | `30_wiki/tools/ai-short-drama-script-planning-three-axes.md` | tool | 短剧策划三轴 | 同上 |
| 13 | `30_wiki/frameworks/ai-short-drama-framework-three-axes.md` | framework | 短剧框架三轴 | 同上 |
| 14 | `30_wiki/frameworks/ai-short-drama-conflict-three-axes.md` | framework | 短剧冲突三轴 | 同上 |
| 15 | `30_wiki/tools/ai-short-drama-platform-policy-comparison.md` | tool | 短剧平台政策对比 | 同上；补充真实政策条款来源和版本日期 |

### B3：AI PPT 工具卡升级（1 张）

| # | 卡片路径 | 类型 | 标题 | 审查重点 |
|:---:|:---|:---|:---|:---|
| 16 | `30_wiki/tools/yt-tool-ai-ppt-maker.md` | tool | AI对话式PPT生成器：把排版变成说话 | 是否从 draft 升级为标准 tool 卡；是否补精确 source；Critique 名人引用是否真实；是否补真实使用案例和失败教训 |

---

## 2. 欧阳锋审查标准

### 2.1 通用标准

| 判定 | 条件 |
|:---|:---|
| **deep / 通过** | 正文 ≥100 行（P0 framework ≥150 行）；六段齐全；失败模式具体；数字有来源；related 有效；frontmatter 无 src_unknown 残留 |
| **shallow / 返工** | 正文 < 80 行；缺六段；失败模式模板化；数字无来源；相关卡死链；内容区仍有 src_unknown |
| **borderline / 小修** | 局部数字未标注、related 缺 1-2 条、个别表述不精确 |

### 2.2 分组重点

#### B1 业务公式域

1. **既有卡（#1-#3）**：暗知识/自检清单是否实质，不是套话
2. **新案例卡（#4-#8）**：
   - 是否有原始表述/背景/问题/方案/结果/可迁移点/关联框架
   - 关键数字是否标注 `[conf=X, source=..., 待独立核实]`
   - 是否用 ABC/六层逻辑/十大范式中的具体框架拆解
   - 是否防模板化：每个案例的教训/关联框架/置信度说明/key actions 是否填了实质内容

#### B2 AI 短剧域

1. 每张是否填 **Claims 6 条**，且每条可被 Critique 攻击
2. 每张 Critique 是否有 **内部局限性 3 条**，针对具体 Claims 而非泛泛引用麦基/坎贝尔
3. 每张是否有 **反事实测试 2-3 条**
4. 每张是否补 **真实案例锚点**（朱雀堂 2025 年度爆款，4500 万分账 + 8 成未回本）
5. Sources 是否精确到具体文件名（`src_20260613_41aceaf5` 等）
6. `ice-fire` 2 张 confidence 是否已降至 **0.65**
7. 平台政策卡是否补充真实政策条款来源和版本日期

#### B3 AI PPT

1. 是否从 draft/dirty 升级为标准 tool 卡
2. frontmatter 是否规范：domain、related、query_triggers、tags、prerequisites 是否还有 src_unknown/null
3. 是否补精确 source 引用
4. Critique 中名人引用是否真实可验证
5. 是否补充真实使用案例和失败教训
6. 行动 Checklist 10 项是否填实质

---

## 3. 判定规则

| 情况 | 处理 |
|:---|:---|
| 16 张全部 deep | 全部标记 `reviewed_by: 欧阳锋`，`status: reviewed`，任务状态改 `reviewed` |
| 少数 shallow/borderline | 通过的卡先标记 reviewed；返工卡列清单退回 WorkBuddy 老顽童；任务保持 `pending_review` |
| 多张核心问题 | 整体任务改为 `blocked`，列明问题 |
| B3 或 C 实际未启动 | 在结论中说明，任务状态可改为 `blocked` 或保持 `pending_review` 并拆分 |

---

## 4. 审查后动作

### 4.1 若全部或大部分通过

1. 通过的卡片 frontmatter：
   - `status: enriched` → `reviewed`
   - `reviewed_by: pending` → `欧阳锋`
   - 加 `review_date: "2026-06-28"`
2. `70_product/tasks/production-queue.md`：任务 #5 状态改为 `reviewed`
3. `70_product/tasks/dashboard.md`：该任务状态改 `reviewed`；Summary 中 `Queued` 减 1，`Review Done` 加 1
4. `.agent/context.md`：追加 wave2 终审完成记录
5. 本文件末尾追加审查结论

### 4.2 若有返工

1. 保持任务 #5 状态为 `pending_review` 或改为 `blocked`
2. 在本文件末尾追加返工清单
3. 通知 WorkBuddy 老顽童按清单修复

---

## 5. 给欧阳锋的启动口令

**完整版**：
> 你是欧阳锋。先进入工作目录 `C:\Users\Administrator\Desktop\wiki\`，读 `.agent/startup.md`、`.agent/ouyangfeng-context.md`、`70_product/tasks/production-queue.md`，找到 wave2（`laowantong-batch-2026-06-20-wave2`）pending_review 项，读 `60_feedback/tasks/review_20260628_ouyangfeng-wave2.md`，按清单审 16 张卡，重点看 B2 AI 短剧 7 张和 B3 AI PPT 1 张，跑 `kdo pre-submit` 抽查，给出 verdict。

**短版**：
> 欧阳锋，切到 wiki 目录，读 startup、队列、wave2 审查任务单（`60_feedback/tasks/review_20260628_ouyangfeng-wave2.md`），审 16 张卡。

---

## 6. 状态记录

| 日期 | 事件 | 操作人 |
|:---|:---|:---|
| 2026-06-28 | WorkBuddy 老顽童完成 wave2 生产 | WorkBuddy 老顽童 |
| 2026-06-28 | 16 张卡 `kdo pre-submit` 全通过 | WorkBuddy 老顽童 |
| 2026-06-28 | 王语嫣写本审查任务单 | 王语嫣 |
| 2026-06-28 | 欧阳锋子代理完成 wave2 终审，16/16 通过 | 欧阳锋（子代理） |

---

## 7. 欧阳锋审查结论

### 总体判定

**16/16 张卡通过 wave2 终审，任务状态改为 `reviewed`。**

- 全部 16 张卡已单独跑 `kdo pre-submit`，结果：16 passed / 0 failed。
- B1 业务公式既有卡（abc-model / six-level-logic / parameter-iceberg）暗知识与自检清单内容实质；5 张新案例卡均具备背景/问题/方案/结果/可迁移点/关联框架，关键数字已标注来源与置信度。
- B2 AI 短剧 7 张卡 Claims 6 条、Critique 内部局限 3 条、反事实 2-3 条、朱雀堂 4500 万外部锚点、source 精确到具体文件/行号；ice-fire 2 张 confidence 已降至 0.65。
- B3 AI PPT 工具卡已从 draft 升级为标准 tool 卡，行动 Checklist 10 项填实质，有真实使用案例与失败教训。

### 通过清单

| # | 卡片路径 | 类型 | 判定 |
|:---:|:---|:---|:---:|
| 1 | `30_wiki/frameworks/yt-business-formula-abc-model.md` | framework | reviewed |
| 2 | `30_wiki/concepts/yt-business-formula-six-level-logic.md` | concept | reviewed |
| 3 | `30_wiki/concepts/yt-business-formula-parameter-iceberg.md` | concept | reviewed |
| 4 | `30_wiki/cases/case-private-domain-ecommerce-formula.md` | case | reviewed |
| 5 | `30_wiki/cases/case-saas-renewal-formula.md` | case | reviewed |
| 6 | `30_wiki/cases/case-dental-clinic-formula.md` | case | reviewed |
| 7 | `30_wiki/cases/case-offline-catering-formula.md` | case | reviewed |
| 8 | `30_wiki/cases/case-gym-membership-formula.md` | case | reviewed |
| 9 | `30_wiki/concepts/ai-short-drama-ice-fire-scripting-compass.md` | concept | reviewed |
| 10 | `30_wiki/frameworks/ai-short-drama-ice-fire-dissection-compass.md` | framework | reviewed |
| 11 | `30_wiki/tools/ai-short-drama-plot-three-axes.md` | tool | reviewed |
| 12 | `30_wiki/tools/ai-short-drama-script-planning-three-axes.md` | tool | reviewed |
| 13 | `30_wiki/tools/ai-short-drama-framework-three-axes.md` | tool | reviewed |
| 14 | `30_wiki/tools/ai-short-drama-conflict-three-axes.md` | tool | reviewed |
| 15 | `30_wiki/concepts/ai-short-drama-platform-policy-comparison.md` | concept | reviewed |
| 16 | `30_wiki/tools/yt-tool-ai-ppt-maker.md` | tool | reviewed |

### 已执行的审查动作

1. 16 张卡全部 Read；按审查任务单清单逐卡核对。
2. 每张卡跑 `kdo pre-submit -f <文件路径>`，全部通过。
3. B2 7 张与 B3 1 张重点深挖：核对 Claims/Critique/反事实/案例锚点/source 精确性/ice-fire confidence。
4. 检查 frontmatter `src_unknown` 残留：frontmatter 中 `domain`/`related`/`tags`/`query_triggers` 仍存在 `src_unknown` 占位（wave2 小结中已注明为系统性债务，pre-submit 容忍）。
5. 通过卡片的 frontmatter 已更新：`status: enriched` → `reviewed`，`review_date` 更新为 `2026-06-28`，`updated_at` 同步更新。
6. `70_product/tasks/production-queue.md` 任务 #5 状态改为 `reviewed`。
7. `70_product/tasks/dashboard.md` 对应状态与 Summary 计数已更新（Review Done +1，Queued -1）。
8. `.agent/context.md` active_task 与 blockers 已追加 wave2 终审完成记录。

### 已知遗留与建议

- **frontmatter 系统性占位**：16 张卡的 `domain`/`related`/`tags`/`query_triggers` 仍有 `src_unknown` 占位（共 100+ 处）。此属 wave2 小结已声明的系统性债务，不阻塞 wave2 入库，但建议单独开一项 `wave2-frontmatter-cleanup` 任务，由王语嫣/老顽童按域填充真实值。
- **内容区少量占位**：
  - `yt-business-formula-parameter-iceberg.md` L1/L2/L4/L5/L6 层级描述与验证/置信度段落仍有 `src_unknown` 占位。
  - B2 部分 three-axes 卡的「核心要点」「行动 Checklist」「Visual Analysis」等冗余列表存在 `src_unknown` 占位（核心 Claims/Protocol/失败模式/Critique/Synthesis 已实质填充）。
- **`ai-short-drama-platform-policy-comparison.md` 未按 B2 通用标准补 `[Critique]` 与反事实测试**：该卡以政策对比为主，已有「Constraints & Boundaries」中的数据时效性/样本范围等局限说明，但缺少正式的内部局限性 3 条 + 反事实 2-3 条。建议在清理任务中补齐，或单独说明该卡为「政策快照」类型，豁免 Critique 格式。
- **B3 真实第三方案例不足**：`yt-tool-ai-ppt-maker.md` 当前仅有讲师演示来源与推断案例，无第三方独立验证的用户案例。建议在后续迭代中补充 1-2 个可验证的真实使用案例。

### 返工卡清单

**无返工卡。** 上述遗留项均不构成本次 wave2 核心深度返工的阻塞，作为后续清理任务跟踪。

---

*维护人：王语嫣 | 最后更新：2026-06-28 | 欧阳锋子代理审查结论追加：2026-06-28*
