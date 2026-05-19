---
id: validate-v15-upgrade-plan
title: "kdo validate --v15 --upgrade-plan：从诊断到可行动的升级路线图"
status: pending
priority: P1
assigned_to: 黄药师
reviewer: 欧阳锋
created: 2026-05-19
depends_on: quality-gate-automation-v15
---

## 背景

`kdo validate --v15` 已完成：205 张卡，45 pass / 89 fail / 71 warn。诊断有了，但信息是"平的"——89 张 FAILED 列表不能告诉执行者"先修哪张、为什么、工作量大不大"。

当前人工判断升级优先级靠翻卡+经验。本工单把这一步自动化。

## 目标

`kdo validate --v15 --upgrade-plan` 在 validate 结果之上输出一个**按优先级排序的分批升级计划**，让执行者（老顽童或黄药师）可以直接拿 plan 开工。

## 分组逻辑

按三维交叉分组，优先级从高到低：

### 第一优先级：全信号缺失（full_check 结构 × 3 信号全 0）

这些卡连 [Critique] 节都没有，需要从零建。工作量大但价值也最大——修一张等于从 0→3 信号。

排序：按被引用次数（in-degree）降序——被引越多的卡，修了辐射效应越大。

```
Batch A (Critical): 3-signal-missing, high-citation
  示例：yt-personal-deep-review（pan-product, 0/2/0, cited by 12）
```

### 第二优先级：缺外部攻击（full_check 结构，don't-use/Action Triggers 齐全）

这些卡有完整的 Synthesis/Action Triggers，只缺 [Critique] 节。加一段 Critique + 两位攻击者即可过关。工作量中等。

```
Batch B (High): missing-attacks-only
  示例：yt-pitch-metaphor（pan-product, 外部攻击 0/2, dont-use ✓, AT ✓）
```

### 第三优先级：缺 Action Triggers（full_check 结构，攻击+don't-use 齐全）

有 Critique、有不要用场景，只缺 Action Triggers。补一个表即可。工作量最小。

```
Batch C (Medium): missing-action-triggers-only
  示例：yt-personal-pan-product-aesthetics（pan-product-upgraded, AT 2/3）
```

### 第四优先级：降级检查不通过（research 结构）

research 卡要求低（≥1 攻击、≥1 don't-use、≥1 AT），但很多旧 research 卡连这个最低标准都没过。

```
Batch D (Low): research-downgraded-failures
```

### 第五优先级：WARNING（research/other/catalog-index）

不算 fail，但值得关注。

```
Batch E (Triage): warnings
```

## 工作量估计

每张卡的工作量估算规则（基于 Batch C 实际数据）：

| 缺什么 | 估时 | 依据 |
|--------|------|------|
| 缺 [Critique] 整节（含攻击者） | 60 min | 需研究两位跨范式学者 + 写攻击段落 |
| 缺 不要用场景 | 20 min | 3 行表，每行需场景+失效+替代 |
| 缺 Action Triggers | 15 min | 3 行表，每行需触发+动作+指标 |
| 全信号缺失 | 90 min | 上述三者之和，但有磨合损耗 |
| research 降级 | 30 min | 标准降低但信息获取更难 |

## 命令行接口

```bash
kdo validate --v15 --upgrade-plan              # 全库升级计划
kdo validate --v15 --upgrade-plan --domain yitang  # 按域
kdo validate --v15 --upgrade-plan --json       # JSON 输出（给 CI）
kdo validate --v15 --upgrade-plan --batch-size 10  # 每批最多 N 张
```

### 输出格式

```
v1.5 Upgrade Plan
=================
Total cards needing upgrade: 160 (89 fail + 71 warn)
Estimated total effort: ~80 hours

Batch A — CRITICAL: Full 3-signal missing, high citation (8 cards, ~12h)
  yt-personal-deep-review          (pan-product, cited:12, est:90m)  ✗ATK ✗DU ✗AT
  yt-personal-knowledge-management (pan-product, cited:8,  est:90m)  ✗ATK ✗DU ✗AT
  ...

Batch B — HIGH: Missing external attacks only (12 cards, ~8h)
  yt-pitch-metaphor          (pan-product, cited:3, est:60m)  ✗ATK
  ...

Batch C — MEDIUM: Missing Action Triggers only (5 cards, ~1.5h)
  yt-personal-pan-product-aesthetics  (pan-product-upgraded, cited:2, est:15m)  AT 2/3
  ...

Batch D — LOW: Research downgrade failures (18 cards, ~9h)
  ...

Batch E — TRIAGE: Warnings (71 cards, ~35h)
  ...
```

## 技术实现

- 位置：`kdo/commands/quality.py`（`cmd_validate_v15` 内，`--upgrade-plan` 分支）
- 复用：`_parse_card_sections`、`_count_*`、`classify_card_structure`、`_read_frontmatter`
- 新增：`_card_citation_count(card_id)` —— 扫描全库 wikilink 计数（可复用 `links.py` 的反向链接逻辑）
- 新增：`_estimate_upgrade_effort(checks, structure)` —— 按缺失信号估算分钟数
- ~120-150 行代码
- ~5 个新 test cases

## 验收标准

- [ ] 五种 Batch（A-E）分组逻辑正确
- [ ] 被引次数排序（高引优先）
- [ ] 工作量估计合理（与实际 Batch C 数据偏差 <30%）
- [ ] `--domain` / `--batch-size` 过滤正常
- [ ] JSON 输出可用
- [ ] pytest ≥5 新 test cases，全绿
- [ ] 对 205 张真实卡输出 plan，无崩溃

## 不做

| 候选项 | 理由 |
|--------|------|
| 自动分配执行人（老顽童 vs 黄药师） | 人事判断，暂不自动化 |
| 自动生成 card-diff / 模板 | 卡内容差异太大，模板无意义 |
| 依赖外部图数据库算 PageRank | 零依赖原则，wikilink count 够用 |
| 自动修卡 | 超出 scope——这是路线图工具，不是修复工具 |

## 相关

- [[70_product/tasks/quality-gate-automation-v15.md]] — 前置工单
- [[70_product/tasks/fix-validate-v15-domain-filter.md]] — domain filter bug（已修 ✅）
- [[70_product/tasks/kdo-infrastructure-backlog-proposal.md]] — 原始 backlog
