---
id: tool-mcp-reachability-check
title: "MCP 可发现性自查——新卡提交前验证外部 Agent 能否搜到"
type: tool
status: reviewed
domain: kdo
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.80
trust_level: observed
aliases:
  - 可发现性自查
  - reachability check
  - mcp搜索验证
  - 搜索可达性自查
source_refs:
  - kdo-tools/mcp-reachability-check.py
diagnostic_signals:
  - signal: '老顽童提交新卡前不自检搜索可达性——外部Agent搜不到但pre-submit不报错'
    severity: high
    implication: '创新者的窘境案例：卡已入库但小昭搜不到——空title+缺aliases'
  - signal: 'pre-submit只查结构不查搜索——#219补了title/aliases但未验证搜索生效'
    severity: medium
    implication: '门禁和实际搜索之间有gap——此工具补上'
  - signal: 'import被site-packages MCP SDK劫持——脚本无法运行'
    severity: medium
    implication: '已用importlib.util绝对路径加载修复'
related:
  - '[[tool-kdo-help]]'
  - '[[dk-delivery-path-type-bug]]'
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[framework-kdo-self-attack]]'
  - '[[dk-P42-agent-fact-check-gap]]'
  - '[[dk-c8-format-complete-mind-empty]]'
created_at: 2026-08-04
updated_at: 2026-08-04
review_date: 2026-08-04
tags:
  - audience:producer
  - scene:pre-submit
  - skill-level:beginner
discoverable_by:
  - 可发现性自查
  - reachability
  - MCP搜索测试
---
# MCP 可发现性自查

> **定位**：属于 KDO 生产工具——老顽童提卡前自检。pre-submit 查结构（YAML/字段/段名），此工具查搜索可达性（外部 Agent 能否搜到）。两者互补。


## 一句话

新卡提交前，用真实搜索关键词验证外部 Agent（小昭/Codex）能否搜到这张卡。

## 用法

```bash
python kdo-tools/mcp-reachability-check.py <card_path> --keywords "关键词1,关键词2"
```

## 输出示例

```
[MCP] MCP 可发现性自查
   卡片: framework-christensen-disruptive-innovation

   [PASS] '创新者的窘境' → 命中 (排名 #2)
   [PASS] 'Christensen'    → 命中 (排名 #2)
   [PASS] '破坏性创新'      → 命中 (排名 #1)

[PASS] 可发现性 100/100 — 全部命中，可以提交。
```

## 何时用

老顽童提交新卡前跑一次。pre-submit 不查搜索可达性（只查结构），这个工具补上"外部 Agent 能否搜到"的验证。

## 失败模式

| 失败模式 | 症状 | 修复 |
|:--|:--|:--|
| import 劫持 | `from mcp.tools import search` 被 site-packages MCP SDK 拦截 | 脚本已用 importlib.util 绝对路径加载 |
| 关键字选择不当 | 自查全绿但用户实际搜索词不同 | 加用户反馈的搜索词——不只测自己能想到的词 |
| 只测 BM25 不测 Graph | BM25 命中但语义搜索失败 | 脚本内 search() 走完整 RRF 融合——已覆盖双路径 |


## 使用场景

- 老顽童完成新卡生产，准备提交 pending_review 前
- 给卡片补了 aliases/title 后——验证外部 Agent 现在能否搜到
- 欧阳锋审查前自检——确认"这张卡对外部 Agent 是否可见"
- #219 类元数据修复后——验证搜索可达性闭环是否合上

## 操作步骤

1. 确定要测试的关键词（中文常用名/英文名/别名/领域术语）
2. 运行 `python kdo-tools/mcp-reachability-check.py <card_path> --keywords "词1,词2,词3"`
3. 检查输出：全部 [PASS] → 可提交；有 [FAIL] → 补全 aliases 后重跑
4. 补全后重跑到 100% 通过

## 适用边界

- 验证的是 BM25+Graph RAG 双路径搜索可达性
- 不验证用户实际会用的搜索词（需要从反馈中收集真实搜索词）
- 依赖 kdo_search 的 RRF 融合——如果 search 入口本身坏了（如 delivery Path bug），自查也会误报

## 为什么值钱

1. **补上 pre-submit 的盲区**：pre-submit 只查结构不查搜索——此工具补上"外部 Agent 能否搜到"
2. **防止"创新者的窘境"重演**：卡已入库终审通过但外部 Agent 搜不到——空 title+缺 aliases
3. **零成本集成**：老顽童提交前跑一条命令，10 秒完成

## 与其他知识的关联

- tool-kdo-help → 互补：一个是新人引导，一个是提交前自检
- dk-delivery-path-type-bug → 如果自查全绿但实际搜不到——先查 delivery Path bug
- dk-E010-duplicate-key-detection → 同为 pre-submit 之后追加的门禁

## Critique

### 内部局限
- 只测 BM25+Graph 双路径——不测用户实际搜索行为（实际搜索词可能和测试词不同）
- 依赖 kdo_search 入口健康——如果 delivery Path bug 复发，自查会误报通过

### 外部挑战
- "pre-submit 已经够用了"——pre-submit 只查结构不查搜索，两者互补非替代
- "老顽童自己记住要写 aliases 就行了"——创新者的窘境案例证明靠人记不住，需要工具强制
