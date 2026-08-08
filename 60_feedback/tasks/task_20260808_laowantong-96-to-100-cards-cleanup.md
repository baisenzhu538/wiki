---
id: task_20260808_laowantong-96-to-100-cards-cleanup
task_id: 257
assignee: laowantong
status: queued
updated_at: 2026-08-08
domain: ai-basic
priority: P1
---

# #257 卡文件 "96→100" 残留清扫（老顽童侧 2 处）

## 背景

周期表已 100/100 终态，但全库残留"96"写死引用（欧阳锋 #256 终审建议转王语嫣——排独立清扫任务一次性清完，统一改"周期表 JSON"不带数字，根治写死问题）。本任务=老顽童侧卡文件清扫。

## 清扫清单（卡文件 2 处）

1. `30_wiki/frameworks/framework-truman-feature-layered-system.md` **L58**：层数分布"96 Feature"写死 → 改为"周期表 JSON"（不带数字）
2. `30_wiki/dark-knowledges/dk-key-hypothesis-still-hope.md` **L46**：diagnostic_signal"96个"写死 → 同上

## 统一口径（根治原则）

- 涉及周期表数量/层数分布的引用：**一律写"周期表 JSON"或"100 个 Feature"（当前终态）**，不带"96"
- 若未来再补 Feature：引用不写死数字，写"以周期表 JSON 为准"

## 验收标准

1. 两处修改完成，git diff 仅数字/引用改动
2. pre-submit PASS；lint 0 新增

## 边界

- agent 侧/工具侧/README 清扫归 #258（黄药师）
- 不追溯其他历史文档（只清本批 6 处中的卡文件部分）
