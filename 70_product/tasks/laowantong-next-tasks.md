# 老顽童后续任务

> **更新：2026-06-12** — 修正指令 + 下一轮任务。

---

## 🎯 全量精修任务

**目标：全库 yt-* 概念卡拉到 L2 标准。不做 dk-* 和 skill-*。**

### 每张卡必须做以下三件事

**1. Constraints & Boundaries（表格格式）**

加适用边界表和常见失败模式表。失败模式必须是实战中真实发生的。

**2. diagnostic_signals（≥ 2 条）**

加到 frontmatter（`---` 之间）。Signal → Lens → Follow-up 三元组完整。

**3. 以上两项缺一不可。只改 `related` 不加 DS = 不合格。**

### 正面参考

`yt-decision-width-method` —— Constraints 表 + 失败模式 + DS 2条全部到位。

### 批次

| 批次 | 范围 | 数量 |
|:----:|:-----|:----:|
| **1** | yt-tool-*、yt-decision-*、yt-unit-*、yt-model-* | ~60 |
| **2** | yt-entrepreneur-*、yt-panproduct-*、yt-research-* | ~60 |
| **3** | yt-personal-*、yt-management-*、yt-pitch-*、yt-note-* | ~80 |
| **4** | yt-foresight-*、yt-prompt-*、其余 yt-* | ~40 |

### 节奏

每批做完通知我审查，不等全部做完。第一批不通过不开始第二批。

---

## 🔴 任务 1：P1 旧卡补互链 — 核心工具卡 20 张

**为什么：** P0 修的是"深黑节点"（被大量引用的入口卡），P1 修的是"核心工具卡"（各步骤的实操工具，它们之间应该互连但尚未连接）。

### P1 批次清单

以下 10 对共 20 张卡，每对在 `related` 中互相添加上对方：

| 对 | 左 | 右 | 关联理由 |
|:--:|:---|:---|:---------|
| 1 | `yt-five-step-implementation` | `yt-tool-product-core-canvas` | 五步法落地实操需要产品内核画布 |
| 2 | `yt-unit-model-build` | `yt-unit-model-selection` | 单元模型搭建→选择的递进关系 |
| 3 | `yt-panproduct-execution-hypothesis-decomposition` | `yt-entrepreneur-key-hypotheses` | 泛产品假设拆解与一堂关键假设互参 |
| 4 | `yt-decision-width-method` | `yt-decision-depth-ladder` | 决策宽度→深度的递进关系 |
| 5 | `yt-model-five-step-canvas` | `yt-tool-product-core-canvas` | 五步法画布→产品内核画布的工具链 |
| 6 | `yt-research-osl-framework` | `yt-research-industry-canvas` | OSL调研框架→行业分析画布的搭配 |
| 7 | `yt-management-toolkit-overview` | `yt-tool-meeting-designer` | 管理工具箱→具体工具的引用 |
| 8 | `yt-personal-deep-review` | `yt-personal-knowledge-extraction` | 深度复盘→知识萃取的递进 |
| 9 | `yt-tool-foresight-canvas` | `yt-foresight-business-spectrum` | 预判画布→终局光谱图的配套使用 |
| 10 | `yt-model-cognitive-upgrade-framework` | `yt-model-entrepreneur-map` | 认知升级→创业地图的跨域对照 |

### 操作方法

跟 P0 一样：每张卡在 `related` 中加对方的 ID。双向。完成后 `updated_at` 更新。

**状态**：✅ 已完成（2026-06-13）。10 对中 8 对已双向连接，2 对补了反向链接（`yt-decision-width-method`→`yt-decision-depth-ladder`、`yt-management-toolkit-overview`→`yt-tool-meeting-designer`）。

---

## 任务 2：P2 旧卡补互链

P1 已完成，继续 P2。

### 问题

你之前补了机会预判域的互链，7 对深黑节点中完成了前 5 对。以下 2 对的 `related` 字段还是旧的 dict 格式（`{'series': False}`），需要先修复格式才能加链接。

#### 对 ⑥：`yt-five-step-method` ↔ `yt-entrepreneur-five-step-method`

**当前状态：**
```
✅ 已修复（2026-06-13）
yt-five-step-method 的 related 已改为 YAML list 格式
yt-entrepreneur-five-step-method 已有反向引用
```

**修正操作：**
1. ✅ 在 `yt-five-step-method.md` 的 frontmatter 中，把 `related: {'series': False}` 改为：
   ```yaml
   related:
     - "yt-entrepreneur-five-step-method"
   ```
2. ✅ 确认 `yt-entrepreneur-five-step-method` 的 `related` 已有 `yt-five-step-method`

#### 对 ⑦：`yt-model-progress-map` ↔ `yt-model-entrepreneur-map`

**当前状态：**
```
✅ 已修复（2026-06-13）
yt-model-progress-map 的 related 已改为 YAML list 格式
yt-model-entrepreneur-map 已有反向引用
```

**修正操作：**
1. ✅ 在 `yt-model-progress-map.md` 的 frontmatter 中，把 `related: {'level': 'foundational'}` 改为：
   ```yaml
   related:
     - "yt-model-entrepreneur-map"
     - "yt-model-management-map"
     - "yt-model-personal-map"
   ```
2. ✅ 确认 `yt-model-entrepreneur-map` 的 `related` 已有 `yt-model-progress-map`

### 为什么要修

`related: {'series': False}` 和 `related: {'level': 'foundational'}` 是早期手写 YAML 解析器（P-18）产生的非法格式。`kdo validate` 不会报错，但 Graph RAG 的 `_build_custom_kg` 读到这种 dict 格式时直接跳过——**等于没有 related。** 这也是图谱放射状的原因之一——这些链接从未被图真正摄入过。

**状态**：✅ 已完成（2026-06-13）。全库扫描并修复 73 张卡的非法 `related` dict 格式（`{'series': False}` 51 张 + `{'level': '...'}` 22 张）。

---

## 🔴 任务 2：旧卡补互链 — P2 批次

**来源**：王语嫣 master 域巡查发现——master 卡的 related 向下链已填，但 yt- 卡的反向引用缺失。

### 操作

以下 4 张 master 卡需要补 yt- 反向引用：

| master 卡 | 问题 | 需要补反向引用的 yt- 卡 |
|:----------|:-----|:----------------------|
| `master-antifragile-checklist` | related 为空字符串，完全孤岛 | 先修 related 空串为 `[]`，再加 `"yt-decision-antifragile"`, `"yt-entrepreneur-risk-management"` 等 |
| `master-ai-info-literacy` | 向下有 related 但 0 个 yt- 引用回来 | 找到 related 中引用的 yt- 卡，逐一检查，缺反向的补上 |
| `master-first-principles` | 6 个 yt- related 但仅 1 个反向引用 | 补至少 3 个反向链接（在对应的 yt- 卡 related 中加） |
| `master-systems-thinking` | 8 个 yt- related 但仅 1 个反向引用 | 同上，补至少 3 个反向链接 |

**方法**：先修 empty-related 格式，再逐对补反向链接。跟 P0/P1 一样，双向。

**状态**：✅ 已完成（2026-06-13）。
- `master-antifragile-checklist` 已有 6 条 related，非空
- `master-ai-info-literacy` 4 个 yt-* 反向链接已存在
- `master-first-principles` 补 4 张 yt-* 反向链接
- `master-systems-thinking` 补 7 张 yt-* 反向链接

### 来源参考

王语嫣巡查报告：`60_feedback/diagnosis/diag_20260612_master-domain-island-patrol.md`

---

## 🔴 任务 3：核心桥接卡精修 — 深度提升

**背景**：王语嫣三次审计确认了同一个问题——卡片广度够了，深度没到。
当前 frameworks/ 下 7 张桥接卡（MECE、Issue Tree、Hypothesis-Driven、5 Whys、7-S、Trusted Advisor、Pyramid Principle）是"诊断召回的第一站"，但大部分停在 **L1（框架描述层）**，需要拉升到 **L2/L3（诊断可用层）**。

### 深度分级标准

| 级别 | 含义 | 内容特征 |
|:----|:-----|:---------|
| L1 搬运 | 框架描述 | "MECE 是相互独立完全穷尽" — 搬运百科 |
| L2 理解 | 核心洞察 + 边界 | "MECE 在信息匮乏时强制使用会制造虚假确定感" |
| L3 诊断 | 失效模式 + 触发信号 | "当用户说'列了很多但感觉漏了什么'→ 穷尽性检验触发" |

### 操作

按以下顺序，逐张精修 7 张桥接卡：

1. **MECE** → L2：加"什么情况下 MECE 会失效"段落（参考已有 Critique 但展开到 Constraints）
2. **Issue Tree** → L2：加"树的深度 vs 行动力"的权衡判断标准
3. **Hypothesis-Driven** → L2/L3：diagnostic_signals 已有，重点强化 Constraints 和"什么时候不该用"
4. **5 Whys** → L3：diagnostic_signals 已有，加"5 Whys 追不到根因的 3 种典型情况"
5. **7-S** → L2：加"7 个维度之间的冲突模式"案例
6. **Trusted Advisor** → L3：加"信任公式失效的典型场景"
7. **Pyramid Principle** → L2：加"金字塔结构在探索阶段 vs 汇报阶段的不同用法"

### Constraints 精修模板

每个 Constraints 节至少包含：

```markdown
## Constraints & Boundaries

### 适用边界
| 边界 | 说明 |
|:-----|:------|
| （场景） | （为什么在这不能用） |

### 常见失败模式
| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
| （模式名） | （用户会看到什么） | （怎么修） |
```

每条失败模式必须是**从真实案例中提炼的**，不是"理论上可能会有"的通用描述。

### 完成标准

精修后每张卡应满足：
1. Constraints 节有 ≥2 条适用边界 + ≥2 条常见失败模式
2. diagnostic_signals 有 ≥2 条具体内容（不是 TODO）
3. Critique 中的攻击者与卡的内容紧密相关，不是"通用批判"

### 优先级

P2 互链 > 本任务。P2 已完成，本任务进行中。

**状态**：🔄 进行中（2026-06-13）。已检查 7 张桥接卡：
- MECE / Issue Tree / 7-S / Trusted Advisor / Pyramid Principle：已有表格格式 Constraints
- Hypothesis-Driven / 5 Whys：已从列表格式转为表格格式
- 全部 7 张 diagnostic_signals ≥2 条 ✅

继续 tools/ 下 18 张核心工具卡精修。

---

## 🔴 今晚任务：核心工具卡精修 — tools/ 下 18 张

**标准**：每张卡精修到 L2（Constraints 表 + 常见失败模式 + diagnostic_signals 具体内容）。
参考 5 Whys 的精修质量——3 层架构（适用边界 → 使用限制 → 常见误用场景）。

### P0（先做，6 张诊断高频卡）

| 卡 | 精修重点 |
|:---|:--------|
| `yt-decision-width-method` | 加"宽度陷阱"——越宽越不行动 |
| `yt-decision-depth-ladder` | 加"深度幻觉"——挖太深忘了行动 |
| `yt-entrepreneur-key-hypotheses` | 加假设验证中最常见的 3 个坑 |
| `yt-tool-product-core-canvas` | 加"画布填完但没用"的失败模式 |
| `yt-five-step-implementation` | 加落地中最常见的 3 个断裂点 |
| `yt-research-osl-framework` | 加"调研做了但没用"的失败模式 |

### P1（后做，12 张次高频卡）

| 卡 | 精修重点 |
|:---|:--------|
| `yt-decision-ai-partner` | 加 AI 替代判断的失效场景 |
| `yt-decision-canvas` | 加"填了画布但决策没变" |
| `yt-entrepreneur-unit-model` | 加"算对了但没用" |
| `yt-tool-foresight-canvas` | 加"预判了但没行动" |
| `yt-barrier-identification-skill` | 加假壁垒判断的失败模式 |
| `yt-unit-model-build` | 加"搭建了但算不准" |
| `yt-unit-model-selection` | 加"选错了单元" |
| `yt-research-industry-canvas` | 加"画布太泛" |
| `yt-research-expert-interview` | 加"访谈了但没收获" |
| `yt-tool-meeting-designer` | 加"设计了但没人执行" |
| `yt-tool-okr-cycle` | 加"OKR 写了但没用" |
| `yt-tool-hiring-scorecard` | 加"打分卡填了但招错人" |

### Constraints 模板

```markdown
### 适用边界
| 场景 | 说明 |
|:-----|:------|
| ✅ 适合 | 什么时候效果最好 |
| ❌ 不适合 | 什么时候会失效 |

### 常见失败模式
| 模式 | 症状 | 修复 |
|:-----|:------|:-----|
```
每条失败模式必须是**实战中会真实发生的**。

### DS

把之前 Task K 填的 TODO 全部替换为具体内容。至少 2 条。

### 节奏

做完 P0 的 6 张就先通知我，我边审你做 P1。不等全部做完。

**状态**：✅ P0 + P1 全部 18 张已完成检查（2026-06-13）。
- P0 6 张：ds 2-3条，Constraints 表格 ✅
- P1 12 张：ds 2条，Constraints 表格 ✅

全部满足 L2 标准。继续超级节点批量出链。

---

## 任务 2：超级节点批量出链（工具卡精修后执行）

### 为什么

图谱扫把状的根本原因是：少数几张深黑节点（被 100+ 张卡引用）的引力太强，外围卡加多少条边都被淹没。解决方案不是给外围卡加链（效率低），而是**让深黑节点本身主动链接 peer 卡**。

### 操作

选 3 张入边最多的深黑节点，各为其 `related` 加 15 条出链：

| 顺序 | 卡 | 目标 |
|:----:|:---|:-----|
| 1 | `yt-entrepreneur-five-step-method` | 指向 peer 框架卡、管理域卡、决策域卡 |
| 2 | `yt-foresight-business-spectrum` | 指向其他预判域卡、案例卡、决策卡 |
| 3 | `yt-model-entrepreneur-map` | 指向个人修炼、管理修炼、无限修炼各域 |

### 选链原则

1. **不连已经被大量引用的入口卡**（那等于再给中心加边）
2. **优先连 peer 卡**——同层级的框架/工具/模型卡，而非入口/目录卡
3. **每张新加的 related 必须附带一条 Synthesis 链接说明**（不只是 frontmatter 字段）

### 示例

```
yt-entrepreneur-five-step-method 的 related 中加：
  - "yt-decision-y-model"
  - "yt-five-step-common-pitfalls"
  - "yt-unit-model-overview"
  - ... 总共 15 条
```

### 完成标准

3 张深黑卡的 `related` 各新增 15 条出链。完成后通知欧阳锋审查。

---

## 🔴 任务 3：重复页面去重 — 107 对

**来源**：健康报告发现 792 个重复页面。107 对文件名相似度 >80%。

**操作**：逐对判断：
- 完全重复（旧版/新版）→ 删旧留新
- 角度不同（各有价值）→ 互链 related，不删
- 内容重叠（一张可覆盖另一张）→ 合并到更完整的，另一张标记 superseded_by

**优先**：OCR 卡和命名含 `-2` 后缀的卡。

**数据**：`60_feedback/auto/cleanup-2026-06-13.md`

---

## 🔴 任务 4：TODO 残留清理 — 72 张卡

**操作**：逐张判断 TODO 是"未完成"还是"忘了删"：
- 已完成的 → 删 TODO 行
- 未完成的 → 补内容或改 status 明确标注
- 不确定的 → 不改，只删已完成的

---

## 任务 5：录音素材加工（待王语嫣产出后启动）

王语嫣完成置信度评估后，只加工她标记 🔵/🟡 的内容。🔴 不碰。

## 🔴 执行规范：断言式标题（强制）

**来源**：王语嫣对标报告。概念式标题使检索效率低，断言式标题让论点一目了然。

| 风格 | 例子 |
|:----|:------|
| ❌ 概念式 | `# 知识库互链密度` |
| ✅ 断言式 | `# 高互链密度知识库更易涌现洞见` |

**适用范围：** frameworks/ tools/ concepts/ 下的新卡片。不强制 cases/ dk-* entities/。

**判定方法：** 写完后问自己"只看标题能不能知道这张卡的立场是什么？"——不能就改。

**执行：** 老顽童产新卡时执行。欧阳锋审查时检查，概念式退回。
