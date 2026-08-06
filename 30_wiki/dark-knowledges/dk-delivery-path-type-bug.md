---
id: dk-delivery-path-type-bug
title: "delivery.py Path类型bug：字符串root→TypeError被吞→搜索永远0结果"
type: dk
status: reviewed
domain: kdo
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.90
trust_level: observed
aliases:
  - delivery bug
  - Path类型bug
  - 搜索0结果
  - _try_bm25_query
source_refs:
  - C:/Users/Administrator/Knowledge Delivery OS 0.0.1/kdo/commands/delivery.py
diagnostic_signals:
  - signal: 'kdo_search对所有人返回0结果——BM25+Graph双路径沉默失败'
    severity: critical
    implication: '小昭搜创新者的窘境永远0结果——不只是索引过期，是入口坏了'
  - signal: '_try_bm25_query中except Exception吞TypeError——bug隐蔽数周'
    severity: high
    implication: '单元测试全部通过但端到端搜索失败——异常被静默吞掉'
  - signal: 'SearchIndex.__init__未做Path类型校验'
    severity: medium
    implication: '防御性修复已应用——调用方做Path强转，SearchIndex自身未修'
related:
  - '[[dk-E010-duplicate-key-detection]]'
  - '[[framework-kdo-self-attack]]'
  - '[[dk-c8-format-complete-mind-empty]]'
  - '[[dk-P42-agent-fact-check-gap]]'
  - '[[dk-c5-todo-false-positive]]'
  - '[[dk-modeling-essence-predictive]]'
created_at: 2026-08-04
updated_at: 2026-08-04
review_date: 2026-08-04
tags:
  - audience:builder
  - scene:debugging
  - skill-level:advanced
discoverable_by:
  - delivery bug
  - Path类型
  - 搜索0结果
  - TypeError被吞
---
# delivery.py Path 类型 bug

> **定位**：属于 KDO 事故教训库的 dk 系列——记录了 #222/#223 事故后发现的搜索管道底层 bug。与 E010（重复键）不同：这个是静默失败（不报错但永远返回空），更难发现。


## 原始表述

`_try_bm25_query` 和 `_try_graph_query` 接收 `root` 参数后直接传给 `SearchIndex(root)`。`SearchIndex.load()` 中执行 `self.root / ".kdo" / "search_index.json"`。

如果 `root` 是字符串 → `str / str` → TypeError → 被 `except Exception: return None` 吞掉 → 调用方收到空列表。

这意味着 kdo_search 对所有人（包括外部 Agent 小昭）实际是坏的——不只是"索引过期"，是入口就坏了。

## 使用场景

- 任何接受路径参数并传递给 Path 运算的函数
- `except Exception` 过于宽泛的地方——TypeError 被吞导致 bug 隐蔽数周
- 调试"为什么搜索永远返回 0 结果"

## 操作方法

修复（已应用）：在 `_try_bm25_query` 和 `_try_graph_query` 入口处加 `root = Path(root)` 类型强转。

## 适用边界

- 两个函数都已加 Path 强转
- 其他 `Path / str` 运算的函数可能同源——需全量扫描
- CLI 入口传 Path 时不受影响

## 为什么值钱

1. "搜索 0 结果"的最根本根因——比"索引过期"更深一层
2. `except Exception` 的经典反模式——吞 TypeError 使 bug 隐蔽
3. 欧阳锋的端到端验证才是真正的验收——仅跑单元测试无法发现

## 与其他知识的关联

- dk-E010-duplicate-key-detection → 同为 #222/#223 事故后发现的基础设施缺陷
- framework-kdo-self-attack → 端到端验证 > 单元测试——此bug靠欧阳锋小昭实测发现
- dk-c5-todo-false-positive → 同模式：脚本输出数字不等于真实结果
- dk-P42-agent-fact-check-gap → 同模式：需要独立验证

## Critique

### 内部局限
- 修复是防御性的（入口强转），未修根因（SearchIndex.__init__ 应自己做 Path 转换）
- 其他类似 `root / path` 运算可能还有同类 bug

### 外部挑战
- "为什么不修 SearchIndex 本身"——改动半径更大，防御性修复破坏半径最小
