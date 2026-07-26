---
id: tool-versioned-iteration
title: 版本迭代法：0.5→0.9逐版验证
type: tool
status: draft
confidence: 0.85
trust_level: medium
domain:
- innovation
author: 老顽童
reviewed_by: 待审
review_date: '2026-07-26'
created_at: '2026-07-26'
updated_at: '2026-07-26'
quality_labels:
- actionable
discoverable_by:
- MVP测试
- 模型重建
- 迭代策略
diagnostic_signals:
- signal: 一版改太多
  lens: 只改一个变量
  follow_up: 只改一个变量
- signal: 旧模型不work但不知道怎么改
  lens: 先粉碎再重建
  follow_up: 先粉碎再重建
source_refs:
- 00_inbox/解放思想探索营/案例分享-口述.txt
- 00_inbox/解放思想探索营/案例分享-笔记.txt
related:
- framework-yitang-thought-liberation-lightning
tags:
- audience:executor
- scene:execution
- skill-level:intermediate
aliases:
- 案例分享
- 解放思想探索营
---
# 版本迭代法

> 定位：属于 [[framework-yitang-thought-liberation-lightning]] 的配套工具。

> 每版只测一个变量

## 操作步骤

1. 0.5版核心假设→0.6验证→0.7-0.8每次一个变量→0.9粉碎旧模型→1.0

## 适用边界

- 创新业务/模型验证
- 不适用：单一个体/无需此方法的场景

## 失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 跳过此工具直接拍脑袋 | 效果不稳定 | 回到操作步骤重新执行 |
