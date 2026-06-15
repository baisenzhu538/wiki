---
id: plan_20260531_data-curator-v1.1
title: Data Curator Skill — 数据清洗+原子切分+多维标签 实施方案 v1.1
type: improvement-plan
status: superseded
superseded_by: plan_20260531_data-curator-v1.3
domain:
- master
tags:
- '#domain/knowledge-management'
- '#method/evaluation-method'
source_refs:
- src_20260531_ai-data-understanding
created_at: 2026-05-31
updated_at: '2026-06-16'
version: 1.1
supersedes:
- plan_20260531_data-curator-v1
related: []
author: legacy
reviewed_by: pending
confidence: 0.75
trust_level: medium-low
---
# Data Curator Skill 实施方案 v1.1

## 版本变更记录

| 版本 | 日期 | 触发 | 变更要点 |
|------|------|------|---------|
| v1.0 | 2026-05-31 | 黄药师+用户架构讨论 | 五阶段流水线、4维标签、10类chunk、pilot dry-run |
| **v1.1** | 2026-05-31 | 一堂 AI数据理解第一课（Truman口述） | **理念层重构**：查字典→食材思维；**5维标签**（+source_type）；**12类chunk**（+process_data/error_data）；**分库架构**；**ROI评估**；**五层成熟度模型** |

## 来源

- v1.0：黄药师+用户架构讨论
- **v1.1 新输入**：`00_inbox/AI-study/一堂-AI数据第一课口述01.txt`（Truman，一堂AI数据必修课·认知篇）

---

## 理念层重构（v1.1 新增）

### v1.0 的底层假设 → v1.1 的修正

| 维度 | v1.0（查字典思维） | v1.1（食材思维） |
|------|-------------------|-----------------|
| **数据消费者** | 系统/人 — 查得到、筛得准 | **AI** — 吃进去、产出好 |
| **评估标准** | 字段填没填、格式对不对 | **AI 用了这数据后输出变好了吗？** |
| **数据形式偏好** | 结构化、规范化、一致化 | **非结构化也有效**，只要 AI 能理解 |
| **错误数据处理** | 清理掉（contradicts 是死字段） | **错误数据是高价值训练材料**（Not Do List） |
| **组织目标** | 可过滤、可统计、可检索 | **降低幻觉、提升完成度、精准控制输出** |

### 核心原则（来自文档）

1. **出口变了**：数据从"给人查字典"变为"给 AI 当食材"。评估数据好坏不再看"准不准"，而看"好不好用"。
   > "工序总是在变，数据是不会变的。只要积累得足够扎实，不管换什么工具都能套上去跑。"
2. **形式变了**：三类过去被丢弃的数据现在最值钱——多样数据（聊天记录/口述稿）、过程数据（决策理由/修改记录）、错误数据（bad case/纠偏材料）。
3. **成本变了**：AI 全链路参与——采集、处理、建模、分析。数据建设从百万级降到万级。
4. **数据是资产，模型不重要**：
   > "数据是我的资产，上面套什么模型无所谓，我也不依赖那个模型，我依赖的是文档系统。"

### 五层数据成熟度模型（来自大眉毛案例）

```
L1: Raw Prompt          → 只有提示词，无数据        → ~20% AI 质量
L2: Data Pack           → 加少量案例/最佳实践       → ~50%
L3: Extraction + Guide  → 萃取规则 + 创作指南       → ~60-65%
L4: Atomic RAG          → 原子化切分 + 多维标注     → ~80-85%
L5: Multi-DB + Router   → 分库架构 + 导航路由       → ~90-95%
```

**KDO 当前对应层级**：L2-L3（卡片级组织，有关联但无原子化 RAG）。
**v1.1 目标**：将管线打通到 L4，预留 L5 分库架构。

---

## 五阶段流水线（v1.1 更新）

```
Phase 1: Audit（只读）    → 数据质量报告
Phase 2: Clean（逐卡写）   → frontmatter 规范化 + 缺失字段推断
Phase 3: Tag（逐卡写）     → 受控词表（5维）+ 全库打标  ← v1.1 扩展
Phase 4: Chunk（写 state） → 原子主张注册表（12类chunk）← v1.1 扩展
Phase 5: Validate（只读）  → 通过率矩阵 + AI产出验证  ← v1.1 新增验证维度
```

## 安全约束（不变）

| 约束 | 来源 | 规则 |
|------|------|------|
| 批量上限 5 张卡 | KF-022 | 每批 ≤ 5 张，逐批审查 |
| 先 dry-run 单卡 | C-10 | 禁止基础设施修改后直接批量 |
| 中文不跑 regex enrich | C-1 / F-KDO-001 | 用结构化解析（heading-based） |
| 标签禁止脚本自动生成 | C-9 | AI 推断 + 人类确认 |
| 完成=代码+数据+验证 | P-15 | 每批写完跑 kdo lint + kdo validate |
| 编辑前必须 Read | F-KDO-016 | 写卡前确认当前文件状态 |

---

## Phase 3: Tag（v1.1 更新）

### 受控词表扩展：4维 → 5维

| 维度 | namespace | v1.0 | v1.1 | 说明 |
|------|-----------|------|------|------|
| 方法论 | `#method/*` | ✅ 10值 | ✅ 不变 | thinking-tool, decision-framework... |
| 领域 | `#domain/*` | ✅ 7值 | ✅ 不变 | healthcare-it, ai-engineering... |
| 质量信号 | `#quality/*` | ✅ 5值 | ✅ 不变 | needs-review, stub, ocr-card... |
| 图谱角色 | `#role/*` | ✅ 5值 | ✅ 不变 | hub, leaf, bridge, reference, index |
| **数据来源类型** | **`#source_type/*`** | ❌ 无 | ✅ **新增** | 见下表 |

### 新增维度：`#source_type/*`

| 值 | 含义 | 示例 | AI 训练价值 |
|----|------|------|------------|
| `raw` | 原始素材 | 口述稿、截图、PDF原文 | 基础材料 |
| `structured` | 结构化知识 | 概念卡、框架图、对照表 | 正向训练 |
| `process` | 过程数据 | 修改记录、决策理由、评审录音 | **高** — 教 AI "为什么这样改" |
| `error` | 错误/纠偏数据 | Bad case、反例、Not Do List | **最高** — 比正向案例更稀缺 |
| `diverse` | 多样非结构化 | 聊天记录、即兴发言、骂人的话术 | 中高 — 教 AI 多样风格 |

### 多维标注原则（v1.1 新增）

> "对同一条数据，从专业角度、平台角度、受众角度、合规角度分别标注。标注的维度越多越细，AI 在这个单点上的幻觉越小。" —— 大眉毛案例

同一条 chunk 应有 ≥ 2 个视角的 tag：

| 视角 | 标注内容 | 示例（中医煲汤食谱） |
|------|---------|-------------------|
| 专业视角 | 领域解释、知识体系归属 | 中医解释（经络温补）/ 西医解释（成分原理） |
| 受众视角 | 目标用户、话术适配 | 信中医的人怎么说 / 信科学的人怎么说 |
| 平台视角 | 合规规则、平台适配 | 违禁词映射（"便秘"→"排便不畅"） |
| 场景视角 | 使用场景、触发条件 | 什么时候用这个食谱 / 什么人不适合 |

### 标签推理规则更新

v1.0 规则：文件名前缀 → domain tag → 内容关键词  
v1.1 新增：
- **`#source_type/process`**：检测到修改记录、对比版本、评审标注 → 自动标记
- **`#source_type/error`**：检测到反例、bad case、Not Do List → 自动标记
- **`#source-type/diverse`**：检测到口述稿、聊天记录格式 → 自动标记

---

## Phase 4: Chunk（v1.1 更新）

### 块类型扩展：10类 → 12类

| 类型 | v1.0 | v1.1 | 说明 |
|------|------|------|------|
| claim | ✅ | ✅ | 可证伪的知识主张 |
| constraint | ✅ | ✅ | 边界条件、限制 |
| critique | ✅ | ✅ | 外部攻击者观点 |
| synthesis | ✅ | ✅ | 跨域洞察 |
| question | ✅ | ✅ | 开放问题 |
| action_trigger | ✅ | ✅ | 使用/不使用规则 |
| procedure | ✅ | ✅ | 操作流程 |
| definition | ✅ | ✅ | 术语定义 |
| example | ✅ | ✅ | 具体案例 |
| reference | ✅ | ✅ | 引用来源 |
| **process_data** | ❌ | ✅ **新增** | 决策过程、修改理由、评审记录、改前→改后对比 |
| **error_data** | ❌ | ✅ **新增** | Bad case、犯错记录、反例、Not Do List |

### 新增块类型的识别规则

```python
# process_data: 检测到修改/对比/评审信号
HEADING_TYPE_MAP_ADDITIONS = [
    (r"(?i)修改|改前|改后|review|评审|决策理由|为什么.*改", "process_data"),
    (r"(?i)bad.?case|反例|不要用|not.?do|犯错|纠偏|踩坑", "error_data"),
]
```

---

## Phase 5: Validate（v1.1 更新）

### 验证维度扩展

v1.0：12 个结构验证维度  
v1.1 新增：

| 维度 | 说明 |
|------|------|
| `source_type_tagged` | 卡片是否标注了 `#source_type/*` |
| `multi_perspective_tagged` | 关键 chunk 是否有多视角标注 |
| `process_data_captured` | 卡片是否捕获了过程数据（如有） |
| `error_data_captured` | 卡片是否记录了反例/边界（如有） |

---

## 分库架构设计（v1.1 新增，L5 预留）

当前 v1.1 实现 L4（原子 RAG），预留 L5 分库架构：

```
KDO Knowledge Graph
├── 专业库（Professional DB）
│   ├── 概念卡 → 领域知识
│   ├── 框架卡 → 方法论
│   └── 实体卡 → 公司/人物/工具
├── 流量库（Traffic DB）
│   ├── 平台规则 → 违禁词、合规
│   ├── 受众话术 → 不同人群的措辞
│   └── 视觉规范 → 颜色、排版
├── 语气库（Voice DB）
│   ├── 口述稿 → Truman风格
│   ├── 评审录音 → 纠偏材料
│   └── 修改记录 → 过程数据
└── 导航层（Router）
    ├── 跨库索引
    ├── 场景→库的映射规则
    └── 检索优先级
```

**当前状态**：Phase 4 先写入平铺 chunk registry（`state.json`）。  
**预留接口**：chunk 元数据中预留 `target_library` 字段，后续按 `#source_type/*` 自动路由。

---

## 交付物清单（v1.1 更新）

| 文件 | v1.0 状态 | v1.1 状态 | 变更 |
|------|----------|----------|------|
| `SKILL.md` | ✅ | ⏸️ 待更新 | 理念层+新增维度+ROI评估 |
| `audit_cards.py` | ✅ | ✅ 不变 | — |
| `clean_cards.py` | ✅ | ✅ 不变 | — |
| `tag_cards.py` | ✅ | ⏸️ 待扩展 | +source_type 推理 + 多维标注逻辑 |
| `chunk_cards.py` | ✅ | ⏸️ 待扩展 | +process_data +error_data 识别 |
| `validate_clean.py` | ✅ | ⏸️ 待扩展 | +4 个新验证维度 |
| `tag-registry.yaml` | ✅ v1 (27值) | ⏸️ 待扩展 v2 | +source_type 维度(5值) |
| `concept.yaml` | ⏸️ | ⏸️ | 不变 |
| `state.json` | ⏸️ | ⏸️ 待扩展 | +target_library 字段 |

---

## ROI 评估框架（v1.1 新增）

每批清洗完成后，增加 AI 产出验证：

```
1. 选 1 张清洗前卡片 → kdo query 相关问题 → 记录 AI 回答质量（1-5分）
2. 同一张卡清洗+打标+分块后 → kdo query 同样问题 → 对比评分
3. 记录 delta 到 run metrics
```

**目标**：L4 卡片（原子 RAG）的 AI 产出质量应 ≥ L2 卡片（未处理）的 1.5 倍。

---

## 迭代设计（v1.1 更新）

- **v1.0**（✅ 完成）：方案定义 + 脚本实现 + pilot dry-run
- **v1.1**（✅ 当前）：理念层重构 + 5维标签 + 12类chunk + 分库预留 + ROI框架
- **v1.2**（待输入）：等待 4 篇口述文章输入 → 进一步迭代
- **v2.0**（待定）：384 张卡全量完成 + 分库架构实施

## 待输入

- [ ] 用户提供的 4 篇口述文章 → 触发 v1.2 迭代
- [ ] 每次迭代更新版本号和变更记录
