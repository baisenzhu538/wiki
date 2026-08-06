---
id: tool-kdo-help
title: "kdo_help MCP 工具——外部 Agent 首次接入 KDO 的结构化引导"
type: tool
status: reviewed
domain: kdo
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.80
trust_level: observed
aliases:
  - kdo_help
  - 新人引导
  - MCP引导
  - KDO接入引导
source_refs:
  - kdo-tools/mcp/tools.py
diagnostic_signals:
  - signal: '外部Agent首次接入KDO不知如何检索——工具描述是技术参数非操作手册'
    severity: high
    implication: '小昭接到任务后反复尝试才找到正确检索路径——kdo_help一次调用即可消除摸索成本'
  - signal: 'MCP tool description无路由信息——Agent不知道搜不到时换什么工具'
    severity: medium
    implication: 'kdo_help补上了搜索模式+评分指引+工具路由网'
  - signal: '新Agent接入无标准化onboarding——每次都是重新摸索'
    severity: medium
    implication: 'kdo_help=可复用的新人引导——一次调用理解KDO完整检索模型'
related:
  - '[[tool-mcp-reachability-check]]'
  - '[[framework-kdo-self-attack]]'
  - '[[dk-delivery-path-type-bug]]'
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[dk-P42-agent-fact-check-gap]]'
  - '[[dk-c8-format-complete-mind-empty]]'
created_at: 2026-08-04
updated_at: 2026-08-04
review_date: 2026-08-04
tags:
  - audience:external-agent
  - scene:onboarding
  - skill-level:beginner
discoverable_by:
  - kdo_help
  - 新人引导
  - MCP引导
---
# kdo_help MCP 工具

> **定位**：属于 KDO MCP 工具集——外部 Agent 的首次接入引导。与 tool-mcp-reachability-check 互补：一个是新人引导（怎么用），一个是提交前自检（能否被搜到）。


## 一句话

外部 Agent（小昭/Codex）首次接入 KDO 时调用一次，返回：KDO 是什么、怎么搜最有效、常见搜索模式。

## 返回内容

- KDO 是什么：~2,500 张精选商业方法论卡（framework/tool/case/dk/concept）
- 怎么搜：kdo_search → kdo_read → kdo_graph 三步
- 搜索模式："X 是什么"找 framework / "X 怎么做"找 tool / "有什么坑"找 dk / "有没有案例"找 case
- 评分指引：high >70 直接用 / medium 40-70 需 kdo_read 验证 / low <40 换关键词

## 何时调用

外部 Agent 接到 KDO 相关任务时，先调 kdo_help 了解检索策略，再调 kdo_search。一次调用即可理解 KDO 的完整检索模型。

## 失败模式

| 失败模式 | 症状 | 修复 |
|:--|:--|:--|
| 引导内容过时 | 新增工具/搜索模式未更新到 kdo_help | 每次 MCP 工具变更时同步更新 help_guide() |
| Agent 不调用 | 外部 Agent 不知道 kdo_help 存在 | tool description 中增加"首次接入请先调 kdo_help" |
| 引导太啰嗦 | Agent 上下文被长引导占满 | help_guide 返回值已做结构化分层——Agent 可按需跳读 |


## 使用场景

- 新外部 Agent（小昭/Codex/新的 MCP client）首次接入 KDO 时
- Agent 搜了几次都返回空或低分结果——不知道该换什么策略
- MCP 工具列表更新后——Agent 需要重新了解可用工具和路由

## 操作步骤

1. 外部 Agent 首次接入时调用 `kdo_help` 一次
2. 阅读返回的 what_is_kdo / how_to_search / common_patterns / score_guide
3. 按 search → read → graph 三步执行实际检索
4. 遇到 0 结果时参考 score_guide 换策略

## 适用边界

- kdo_help 返回的是静态引导——不包含实时索引状态或最新卡片统计
- 搜索模式是通用模板——具体领域可能有更优的搜索策略
- 新 Agent 仍需实际调用 kdo_search 来验证引导是否有效

## 为什么值钱

1. **消除新 Agent 的摸索成本**：一次调用理解 KDO 完整检索模型——不用反复试错
2. **标准化 onboarding**：每个新接入的 Agent 都从同一份引导开始——不会因为"前任没交代"而走弯路
3. **降低支持成本**：Agent 不需要人类手把手教怎么搜 KDO

## 与其他知识的关联

- tool-mcp-reachability-check → 互补：引导是"怎么用"，自检是"能被搜到吗"
- dk-delivery-path-type-bug → 如果按引导搜还是 0 结果——先查这个 bug
- MCP 工具路由网（#220）→ kdo_help 是路由网的入口文档

## Critique

### 内部局限
- 引导内容是静态的——新增 MCP 工具或搜索模式变更时需手动同步更新 help_guide()
- 搜索模式是通用模板——不覆盖所有域的特定搜索策略

### 外部挑战
- "Agent 自己探索比读引导更快"——探索成本是每次 N 次失败的 kdo_search 调用，kdo_help 一次调用消除这个成本
- "引导太长占上下文"——已做结构化分层，Agent 可按需跳读
