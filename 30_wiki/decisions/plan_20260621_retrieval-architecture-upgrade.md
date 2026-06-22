---

id: plan_20260621_retrieval-architecture-upgrade
title: 检索架构升级 —— 从向量匹配到域路由 + 混合检索 + 工作流组装
type: improvement-plan
status: active
domain:
  - master
  - kdo
source_refs:
  - 30_wiki/decisions/plan_20260621_domain-index-infrastructure.md
  - 60_feedback/diagnosis/diag_20260620_调研专题素材验收.md
created_at: "2026-06-21"
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.9
trust_level: high
related:
  - '[[plan_20260621_domain-index-infrastructure]]'
  - '[[framework-yitang-research-quality-gate]]'
  - '[[tool-yitang-18-strategy-tool-mapping]]'
  - '[[yitang-research-domain-digest]]'
  - '[[system-yitang-research-workflow]]'
---

# 检索架构升级方案

> 提交：黄药师 → 审查：欧阳锋 · 2026-06-21

## 问题

kdo query "用一堂调研方法论做上市公司研报分析" 实测返回：
- #1 关键词加粗三重结构（笔记技巧，无关）
- #2 超级武器库元概念（擦边）
- 应返回的 `tool-yitang-financial-report-intelligence`、`framework-yitang-high-level-plan`、`tool-yitang-comparable-company-selection` 全部未命中

**根因**：纯向量相似度检索（384维 MiniLM），无域感知、无关键词增强、无图遍历。中文语义相近不等于任务相关。

## 用户场景

> "调研老百姓大药房，从研报中分析药品零售市场变化，结合一堂方法论，做纵向和横向对比分析"

Agent 需要：查公开信息（线上研报）→ 用 OSCAR 定目标缩范围 → 财报解读 → 对标公司选择 → 产出深度对比报告

当前检索无法支撑这个工作流。

## 方案：三层检索架构

```
用户查询
  ↓
Layer 1: 域路由器
  ├── 关键词+模板匹配 → 识别"调研"域
  ├── 加载域索引入口卡 → 获取候选卡片池（~20-30张）
  └── 输出：候选池 + 域工作流骨架
  ↓
Layer 2: 混合检索
  ├── BM25 关键词（精确匹配"研报""上市公司""对标"）
  ├── 向量相似度（语义召回）
  ├── 图遍历（沿 wikilink 从框架卡走到工具卡）
  └── 加权融合排序
  ↓
Layer 3: 工作流组装
  ├── 排序后的卡片 → 按类型分组
  ├── 生成建议执行路径：框架 → 工具 → 案例
  └── 输出：结构化检索结果 + 建议工作流
```

## 实现路径

### Phase 1：域路由器（今天）

- `query-domain.py`：输入查询 → 识别域 → 返回候选卡片池
- 简单关键词+模板匹配，不依赖外部模型
- 输出候选池 + 建议卡片列表

### Phase 2：混合检索（本周）

- BM25 + 向量融合
- 图遍历增强：从命中的框架卡沿 `related` wikilink 扩展到工具卡和案例卡
- 集成进 `kdo query --domain-aware`

### Phase 3：工作流组装（下周）

- 根据卡片 `type` 和 `bridges_to` 自动生成执行路径
- Agent 可直接消费的结构化指令

## 验收标准

用"老百姓大药房 研报 一堂方法论 调研"查询，期望返回 Top 5：
1. `framework-yitang-high-level-plan`（OSC：定目标→缩范围→列清单）
2. `tool-yitang-financial-report-intelligence`（财报/招股书解读）
3. `tool-yitang-comparable-company-selection`（对标公司选择）
4. `framework-yitang-high-level-execution`（AR：获取情报→正确归因）
5. `framework-yitang-six-layer-cross-validation`（六层交叉验证）

## Phase 1 实测结果（2026-06-21）

原型 `query-domain.py` 已交付并实测。

**正确**：
- 域识别准确（"调研"关键词命中）
- 域索引入口卡候选池机制正常
- framework/tool 类型加权生效

**暴露的系统性依赖**：
- 域索引入口卡刚建骨架，TODO 行未填 → 候选池不够精准
- Wave 3 工具卡（`tool-yitang-financial-report-intelligence` 等）尚未产出 → 方法论匹配缺失
- 等 Wave 1-3 完成后重新验证

**下一步**：Phase 2 混合检索（BM25 + 向量 + 图遍历）待 Wave 3 交付后开发
