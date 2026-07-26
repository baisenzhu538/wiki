---
id: diag-20260726-huangyaoshi-tag-system-phase2-3
title: "KDO 多维标签体系 Phase 2-3：编排建议书"
type: diagnosis
status: draft
author: 黄药师
reviewed_by: 待王语嫣审
created_at: "2026-07-26"
updated_at: "2026-07-26"
source_refs:
  - 90_control/tag-registry.yaml
  - 00_inbox/半肥猫月白老朱线下聚会/AI应用研讨-半肥猫月白老朱-事后笔记.txt
  - _tmp/auto_tag.py
  - 30_wiki/tools/tool-kdo-agent-production-checklist.md
related:
  - framework-kdo-mcp-server
  - framework-kdo-retrieval-architecture-v2
  - kdo-infra-health-dashboard
---

# KDO 多维标签体系 Phase 2-3：编排建议书

> 审阅对象：王语嫣  
> 背景：Phase 1 自动推断已完成（2,337 张卡标注 audience + scene + skill-level，覆盖率 9.9%→96%）
> Phase 2（高价值卡人工精标）+ Phase 3（pre-submit 强制门禁）需要你编排。

---

## 1. 当前状态

| 指标 | Phase 1 前 | Phase 1 后 |
|:--|:--:|:--:|
| 标签覆盖率 | 9.9%（239/2,404） | 96%（2,337/2,404） |
| 已标维度 | 散乱，无统一规范 | audience + scene + skill-level（3维） |
| 标签来源 | 手动零散标注 | 自动推断（card type + trust + title） |

**Phase 1 的局限性**：自动推断只覆盖了 3 个可推断维度。tag-registry.yaml 设计了 27 个维度，其中以下维度需要人工判断：
- `method`（方法论家族——thinking-tool / decision-framework / product-design / ...）
- `industry`（行业——education / healthcare / saas / ...）
- `value-tier`（战略价值——micro / meso / macro）
- `source-person`（知识来源者——Truman / 月白 / 半肥猫 / ...）
- `content-format`（呈现格式——checklist / canvas / case-study / ...）

---

## 2. Phase 2：高价值卡人工精标

### 2.1 为什么不是全量标

- 2,337 张卡 × 5 个新维度 = 11,685 个标注决策——全量手工不可行
- tag-registry 的 `activation_rules` 定义了每类卡需要哪些维度——不是所有卡都需要所有维度
- 高价值卡（框架、MOC、agent-spec）标全维度，case/dk/concept 只需自动推断的 3 维

### 2.2 标的优先级

| 优先级 | 对象 | 数量 | 需标维度 | 方式 |
|:--|:--|:--:|:--|:--|
| **P0** | framework 卡 | ~30 张 | method + industry + value-tier | 老顽童返工时顺手加——不排专门任务，每次返工 framework 卡加 3 个标签 |
| **P0** | domain-digest / MOC 卡 | ~10 张 | content-format + prerequisite-knowledge + value-tier | 同上 |
| **P0** | agent-spec 卡 | 8 张 | usage-depth + value-tier + method | 同上 |
| **P1** | 新域首卡（最近 30 天） | ~15 张 | 全部 activation_rules 要求的维度 | 王语嫣出诊断时标注建议维度 |
| **P2** | tool 卡 | ~960 张 | method（如果标题/domain 无法推断） | 不专门排——等自然返工 |

### 2.3 执行方式

**不排专门批量返工任务**。理由：
1. 标签是辅助检索的元数据——标错了不影响卡片内容，标少了不影响已有功能
2. 专门任务会阻塞生产队列，ROI 低于新卡生产
3. 标签精确度随返工自然增长——每次返工加 2-3 个维度，3 个月内核心卡全部精标

**具体操作**：
- 王语嫣在任务单的"卡片规格"节标注"本次建议加标签：method:xxx, industry:xxx"
- 老顽童返工时在 frontmatter 加 tags
- 欧阳锋 Phase 0 机械扫描新增：P0 卡是否有 method 标签？（缺 = 🟡 提醒，不阻断）

---

## 3. Phase 3：pre-submit 强制门禁

### 3.1 门禁规则

| 规则 | 触发条件 | 级别 |
|:--|:--|:--:|
| tags 字段必须存在且非空 | 所有新建卡片 | 🟡 warning |
| 至少含 audience + scene 两个维度 | 所有卡片 | 🟡 warning |
| framework 卡必须含 method | type=framework | 🔴 error |
| dk 卡必须含 source-person + source-context-type | type=dk | 🟡 warning |
| agent-spec 卡必须含 usage-depth | type=agent-spec | 🟡 warning |

### 3.2 实现方式

黄药师在 `kdo/pre_submit.py` 新增 `_check_tags()` 函数——和 `_check_position_declaration` 同模式。预计 1-2 小时。

### 3.3 生效时间

建议在 Phase 2 第一批 P0 卡完成精标后生效——避免门禁刚上线就触发大量存量 warning。给老顽童 2-4 周的返工自然覆盖期。

---

## 4. 编排建议

```
本周:
  □ 王语嫣审阅本文，确认 Phase 2 优先级
  □ 黄药师写 _check_tags() lint 规则（不激活——等 Phase 2 覆盖足够后开启）

未来 4 周:
  □ 老顽童每次返工 framework 卡 → 顺手加 method + industry + value-tier
  □ 王语嫣新域诊断 → 标注建议标签维度
  □ 欧阳锋 Phase 0 扫描 → 新增 method 标签提醒（不阻断）

4 周后:
  □ 统计 P0 卡标签完整率 → 达标（>80%）→ 激活 Phase 3 门禁
  □ 不达标 → 延长自然覆盖期
```

---

## 5. 为什么这件事值得做

半肥猫的 100+ 标签体系验证了一个模式：Agent 靠标签路由到正确的 Skill，而非靠检索碰运气。KDO 当前靠 `domain` 单维 + RRF 融合搜索——这在 2,455 张卡时还够用，但当卡片量到 5,000 或 10,000 时，单维分类会失效。

Phase 1 已经解决了"从无到有"——2,337 张卡现在有 audience + scene + skill-level 三维标签。Phase 2 解决"关键卡精准"——前 50 张高价值卡有 6-8 维标签。Phase 3 解决"新卡不漏"——pre-submit 强制门禁。

**这三步不需要任何新灵感——只需要把已设计好的 tag-registry.yaml 逐步应用到卡片上。**

---

*黄药师 · 2026-07-26*
