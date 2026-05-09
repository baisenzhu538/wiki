---
title: "黄药师任务接力棒"
type: memory
status: active
created_at: "2026-05-09"
---

# 黄药师任务接力棒

> 每条任务结束时更新。下一轮 `/new` 后只读此文件，不读任何规范。

## 刚刚完成

Sprint 2 终审通过 — gate.py + enrich 举证 + 端到端验收

## 下一步做什么

在 `workspace.py` 的 `lint_workspace()` 中新增 L2 内容质量检查：
1. Condense 实质性 — ≥3 条中文有内容行 → 不足 P1 warning
2. Critique 指名假设 — 含"具体假设"\"边界"\"反例"\"前提"至少一个 → 一个都没 P1 warning
3. Synthesis wikilink — ≥2 个 `[[...]]`，无 self-link → 不足或自指 P1 warning
4. 全文 > 500 字
5. 全部只输出 warning，不阻断

写完对 vault 跑一次，确认能检出三张模式 A 卡。改完自更新本文件。

## 需要的文件路径

- 修改：`kdo/workspace.py` → `lint_workspace()`
- KDO 源码根：`C:\Users\Administrator\Knowledge Delivery OS 0.0.1\`
