---
id: "corr-20250611-domain-label-audit"
title: "Domain Label Audit — Corrections & Action Items"
type: "correction"
created_at: "2026-06-11"
updated_at: "2026-06-11"
domain: ["master", "diagnosis"]
status: "pending_review"
---

# Domain 标签审计——勘误与执行清单

> 作者：王语嫣
> 扫描范围：`30_wiki/concepts/*.md` 全量 1124 张
> 参考：`kdo-concept-map-20260611.md` 原诊断
> 结论：原诊断中 3 处被数据夸大，1 处方向正确但结论不完整。本文档是修正版。

---

## 勘误 1：design 域 "孤岛" 被高估

### 原诊断
> "design 域 32 张卡 100% 孤岛"

### 实际情况
- design 域 32 张卡确实 100% 单 domain，但它们是**正确归类的**——内容与 domain 匹配
- 真正的问题是：**大量设计内容散落在其他域，未归入 design 域**

### 散落的设计内容（部分清单）

| 卡群 | 数量估算 | 当前 domain | 问题 |
|:-----|:---------|:------------|:-----|
| 月白设计技能卡（skill-月白-*） | ~80 | `[]` 或 `[ai-collaboration]` | 内容全是 AI 生图/海报/电商设计，domain 未标 design |
| 泛产品设计 OCR 素材（ocr-泛产品设计-*） | ~15 | `[yitang]` 或 `[ai-saas]` | 标题含"设计"、"审美"，domain 未标 design |
| 纪浩/马易 设计相关技能卡 | ~10 | `[ai-collaboration]` 或 `[]` | 内容涉及 UI/Agent 界面设计，domain 未标 design |
| 紫鲸AI/视觉Prompt 等 | ~5 | `[ai-saas]` 或 `[yitang]` | 内容是 AI 视觉/设计，domain 未标 design |
| 泛产品设计方法论卡（yt-泛产品设计-*） | ~10 | `[yitang]` | 内容是产品设计原则/落地，domain 未标 design |

**估算：知识库中内容涉设计的卡片约 120 张，其中仅 32 张归入了 design 域。**

### 修正建议
1. **不是给 design 域 32 张卡补 bridges_to**，而是把散落在其他域的 ~80 张设计卡的 domain 补上 `design`
2. **月白技能卡群（~80 张）是重灾区**：domain 大量为空，建议批量补填 `[design, ai-collaboration]`
3. **泛产品设计 OCR 素材**建议统一改为 `[yitang, design]`

---

## 勘误 2：master 域 "未下沉" 被夸大

### 原诊断
> "master 域 54/61 单 domain，元能力未下沉"

### 实际情况
- `master-cognitive-bias-checklist` 的 related 字段有 **8 条**，其中 5 条指向 yitang 科学决策域（`yt-decision-y-model`、`yt-decision-canvas` 等）
- `yt-concept-weapon-arsenal` 的 related 有 **3 条**，指向一堂讲香/表达力域
- 多张 master 卡的 related 字段已经建立了跨域连接

### 修正建议
- master 域的桥接**主要靠 related 字段**而非 domain 共现
- 建议将原诊断中的 "master 孤岛率 88.5%" 修正为 "master 域 domain 共现率低，但 related 边密度已达标"
- **不需要专门行动**——继续保持当前 related 填充节奏即可

---

## 勘误 3：未识别的问题——月白技能卡 domain 大规模为空

### 发现
- 月白技能卡（`skill-月白-*`）约 80 张，大部分 domain 字段为 `[]`
- 这些卡的内容是 AI 设计/生图/电商海报，应当标为 `[design, ai-collaboration]`

### 执行建议
- 由黄药师写一个快速脚本，检测所有 `skill-月白-*` 卡的 domain 字段
- 如果为空，批量填充 `[design, ai-collaboration]`
- 约 10 分钟可完成

---

## 勘误 4：未识别的问题——ai 相关 domain 标签混乱

### 发现
- `ai` / `ai-collaboration` / `ai-native` / `ai-models` / `ai-saas` 五个标签同时存在
- 同一个概念（如"提示词工程"）可能出现在不同的 ai 标签下

### 执行建议
- 建议合并为两个标签：`ai` 和 `ai-collaboration`
- `ai-native` 和 `ai-models` 归入 `ai`
- `ai-saas` 如果内容是产品，改为 `product`；如果是方法论，改为 `ai`

---

## 执行清单（优先级排序）

| 顺序 | 任务 | 负责人 | 估算时间 | 依据 |
|:---:|:-----|:--------|:--------|:-----|
| 1 | 月白技能卡批量补 domain `[design, ai-collaboration]` | 黄药师 | 10min | 约 80 张卡大规模空值 |
| 2 | 泛产品设计 OCR 素材 domain 补 `design` | 老顽童 | 10min | ~15 张卡标题含"设计"、"审美" |
| 3 | `ai-saas` / `ai-native` / `ai-models` 标签归并 | 黄药师 | 15min | 标签混乱导致搜索漏匹配 |
| 4 | 更新概念卡地图 `kdo-concept-map-20260611.md` 的勘误节 | 王语嫣 | 5min | 本文档已完成 |
| 5 | 验证：重新运行概念卡地图脚本，确认 design 域卡数从 32 → ~120 | 王语嫣 | 5min | 验收执行效果 |

---

## 附录：本次审计用的关键词列表

### 设计相关关键词
设计、视觉、审美、UI、UX、界面、品牌、配色、排版、生图、AIGC、提示词、美术、风格、构图、色彩、质感、素材、画布、版式、字体、标志、海报、主视觉、详情页、包装、Midjourney、Stable Diffusion、DALL-E、工具箱、模板

### AI 相关关键词
AI、人工智能、大模型、GPT、LLM、生成式、Agent、智能体、算法、机器学习、深度学习、神经网络、变历器、扩散模型、推理、训练、精调、上下文、上下文工程、大语言模型、多模态、文生图、图生文
