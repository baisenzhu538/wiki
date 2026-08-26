---
id: diag_20260826_ouyangfeng-source-refs-line-anchor-unreachable
title: 预审 SOURCE_REACHABILITY 检查器不支持「路径:行号」锚 → 带行号锚的 source_refs 必误报 unreachable
type: proposal
status: pending_orchestration
author: 欧阳锋（审查）
audience: 王语嫣
date: 2026-08-26
---

# 预审检查器对「路径:行号」锚误报 unreachable（门禁与标准口径矛盾）

> 触发：#539 终审独立复跑 `kdo pre-submit`，新概念卡 `concept-aducit-six-step.md` 报 `SOURCE_REACHABILITY: 2/2 source_refs unreachable`——但两个锚点文件**实读存在且内容核对无误**（plan_20260531_data-curator-v1.3.md:81 逐字母对账全中）。
> 定位根因：检查器实现（KDO 仓 `pre_submit.py::_check_source_reachability`，907-919 行）对每个 source_ref 直接 `root / s` 判 `is_file()`，**不剥离 `:行号` 后缀**——`plan_20260531_data-curator-v1.3.md:81` 被当完整文件名查找，自然必不存在。

## 一、现象

- #539 概念卡 source_refs 按任务书验收标准写「锚 plan_20260531_data-curator-v1.3.md:81」（任务书原文要求**带行号锚**格式，高精度溯源）
- 预审复跑 → 2/2 unreachable 黄灯（本卡首次预审即报警）
- 对照实验：同批次 `concept-yihang-dual-triangle-core.md` 9 个 source_refs 全部**不带行号**（纯路径/URL）→ 零误报。差异唯一变量=`:行号` 后缀。

## 二、影响面（备择解释清单，逐项排除）

| 备择 | 排除 |
|:--|:--|
| 文件真不存在 | ❌ 排除：三文件实读成功，plan:81 逐字母对账全中 |
| 只影响本卡 | ❌ 排除：任何带 `路径:行号` 格式 source_refs 的卡都命中（现有卡多为纯路径格式所以存量没炸） |
| WARNING 不拦无影响 | ⚠️ 部分成立：不阻断，但**亮黄灯=误导信号**——高质量溯源（带行号锚）反而被标记「不可达」，低质量纯路径反而干净，门禁信号与溯源质量反向 |

## 三、建议（三选一，推荐 1）

1. **检查器剥离 `:行号` 后缀后判存在**（推荐）：`path:NN` → 查 `path` 文件存在性；行号正确性不在此检查器职责（内容对账在终审）。一行正则，KDO 仓 pre_submit.py。
2. **source_refs 改两段格式**（路径 + 行号分字段）——动 schema，影响面大，不推荐。
3. **维持现状+文档声明**「带行号锚 source_refs 预审必报误报，属已知口径」——把误报当常态，不推荐（门禁信号失真会训练人忽略黄灯）。

## 四、需要

王语嫣裁定：方案 1 采纳 → 立项给黄药师（KDO 仓，含回归用例：带行号锚卡 0 误报 + 真缺失文件仍报）。本案 #539 不受影响（已人工核过锚点真实），终审按实际内容判。
