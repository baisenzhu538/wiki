---
title: "高密度素材复合编译策略"
type: decision
status: draft
domain:
  - kdo
source_refs:
  - "30_wiki/decisions/kdo-ec-industrialization-migration-proposal.md"
created_at: "2026-05-10"
tags:
  - "#kdo"
  - "#enrichment"
  - "#methodology"
---

# 高密度素材复合编译策略

> 欧阳锋制定，黄药师执行。适用于本次 inbox 中「知识地图 + 口述稿」混合素材的 enrichment 策略。

## 背景

2026-05-10 批处理了 inbox 中 ~60 份素材，经 OCR + kdo ingest 后产生 97 张 wiki 骨架。素材包含两类：

| 类型 | 数量 | 特征 |
|------|:--:|------|
| 知识地图（OCR）| ~85 张 | 高密度视觉框架，每张包含一个完整心智模型 |
| 口述稿（transcript）| 12 份 | 长篇课程逐字稿（4-12 万字/份），对知识地图的深度讲解 |

**关键判断：这些不是独立原子概念，而是上下位关系的知识集群。**

## 问题

默认 `kdo ingest` 按"一文件一卡片"生成了 97 张独立 wiki 骨架。如果逐张做三步编译，会导致：

1. **碎片化**：读者看不到方法论全貌
2. **关联断裂**：口述稿和知识地图之间的佐证关系丢失
3. **质量低下**：单张 OCR 文字不足 300 字，无法满足 L2 Condense ≥3 条的要求

## 决策：三层复合编译法

不逐张处理。按主题聚类，将口述稿（主干）和知识地图（枝叶）合并编译为 ~12 张复合概念卡。

### 三层结构

```
Layer 1: 口述稿 → 方法论主干（Condense）
         从长篇口述中提取结构化的方法论框架
              ↓
Layer 2: 知识地图 → 框架可视化 + 案例佐证
         将 OCR 卡片作为框架的「证据附件」和「检查清单」
              ↓
Layer 3: 跨域对标 → 建立与现有 wiki 的链接网络（Synthesis）
         关联已有概念卡（五步法、Y模型、科学学习IPO 等）
```

### 复合卡片结构模板

```markdown
---
title: "方法论名称"
type: concept
status: enriched
source_refs: ["src_xxx", "src_yyy", ...]
domain: ["master"]
---

# 方法论名称

## Condense（核心原则）
从口述稿提炼 5-8 条原则，每条含：
- 原则陈述
- 来源口述稿的关键段落引用
- 适用的场景

## Framework Gallery（框架附件）
嵌入相关知识地图的 OCR 文字：
- 卡片 1：框架说明（摘录 OCR 核心文字）
- 卡片 2：检查清单
- ...

## Critique（质疑）
- 具体假设：[至少 1 条]
- 边界与反例：[至少 1 条]
- 可靠性评估：高/中/低 + 理由

## Synthesis（对标）
- [[已有概念 A]]：互补关系
- [[已有概念 B]]：冲突或需要调和
- 可迁移场景：[至少 2 个]
```

## 聚类方案

| # | 复合卡片标题 | 素材来源 | 优先级 |
|---|------------|---------|:--:|
| 1 | 泛产品设计方法论 | 5 份口述 + 30 张卡片（用户/审美/落地）| P0 |
| 2 | 一堂五步法详解 | 画布卡 + 产品内核卡 + 指标卡 | P1 |
| 3 | 用户视角工具箱 | 8 张用户卡片 | P1 |
| 4 | 审美方法论 | 4 张审美卡 + 审美口述 | P1 |
| 5 | 落地执行体系 | 18 张落地卡 + 实操口述 | P1 |
| 6 | Y模型实操指南 | Y模型卡片 + 2 份口述 | P1 |
| 7 | 科学学习IPO体系 | IPO模型卡 + 口述 | P1 |
| 8 | SPIN销售法 | 口述稿 | P1 |
| 9 | 思维模型提炼方法 | 口述稿 | P2 |
| 10 | 知识萃取方法论 | 口述稿 | P2 |
| 11 | 调研方法论 | 调研口述 + 课程清单 | P2 |
| 12 | 个人成长地图 | 个人地图 + 五步法 + 进步大地图 | P2 |
| 13 | 转化率优化体系 | 转化率触点 + 动力曲线 | P3 |
| 14 | 婚礼/项目管理 | 婚礼规划卡 | P3 |

## 执行规范

### 每一步的要求

1. **读取素材**：先读口述稿全文建立理解，再扫相关知识地图 OCR
2. **合并编译**：在口述稿的 wiki 骨架上扩展，将知识地图作为 `## Framework Gallery` 附件融入。**不要为知识地图单独创建 wiki 卡片**——它们作为附件更有价值
3. **三步编译**：Condense ≥5 条 / Critique 含至少一个关键词（假设/边界/反例/前提）/ Synthesis ≥2 个 wikilink
4. **验证**：跑 `kdo lint --wiki-path <path>` 确认 0 warning

### Kimi LLM 使用

```bash
# 单张 enrich（LLM 模式）：
kdo enrich --wiki-path 30_wiki/concepts/<target>.md --llm

# 验证：
kdo lint --wiki-path 30_wiki/concepts/<target>.md
```

LLM 配置在 `C:\Users\Administrator\.kdo\config.yaml`，需填入 Kimi API Key。

### 禁止事项

- ❌ 不要逐张处理知识地图为独立卡片
- ❌ 不要在没读口述稿的情况下直接 enrich
- ❌ 不要跳过 Critique（L2 强制要求）
- ❌ 不要创建只有 3 句话的 stub 卡
- ❌ 单次会话不要处理超过 3 个复合卡片（防 context overload）

## 验收标准

| 标准 | 阈值 |
|------|:--:|
| L2 Condense | ≥5 条实质性中文 bullets |
| L2 Critique | 含「假设」「边界」「反例」「前提」至少 1 个 |
| L2 Synthesis | ≥2 个有效 wikilink（非 self-link） |
| 全文字数 | >500 字 |
| `kdo lint` | 此卡 0 warning |

## 已有 wiki 骨架清理

当前 `30_wiki/concepts/` 下有 97 张从知识地图 OCR 创建的独立骨架。这些卡片**不需要单独 enrich**——它们的内容将在复合编译时作为 Framework Gallery 附件融入对应的口述稿卡片。

复合卡片完成后，未被合并的 OCR 独立骨架可以：
1. 保留为 stub（后续有需要再扩展）
2. 或通过 `kdo` 清理

此决策由黄药师在执行时根据实际内容判断。

---

> 审批人：欧阳锋 | 执行人：黄药师 | 状态：待执行
