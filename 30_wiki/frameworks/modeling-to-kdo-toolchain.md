---
id: modeling-to-kdo-toolchain
title: 建模三段论 → KDO 工具链映射：从 SOP 到本质的知识管理落地
type: framework
source_refs:
- src_20260614_8269ccdb
- src_20260614_42f1e977
- src_20260614_623cfbfd
status: draft
confidence: 0.85
domain:
- kdo
- yitang
created_at: '2026-06-14'
author: 黄药师
reviewed_by: pending
review_date: '2026-06-14'
trust_level: high
related:
- '[[modeling-capability-for-kdo]]'
- '[[modeling-three-stages]]'
- '[[modeling-capability-system]]'
- '[[modeling-level-map]]'
tags:
- '#method/modeling'
- '#kdo'
- '#meta-method'
- '#pipeline'
diagnostic_signals:
- signal: 我写了一张卡但不知道怎么验证它够不够好
  framework_lens: 三段论门禁映射
  follow_up_question: 你的卡处于L3（流程）、L4（抽象）还是L5（本质）？对应的门禁标准不同。
- signal: 素材进了inbox不知道怎么推进到wiki
  framework_lens: KDO管线五阶段
  follow_up_question: 素材是P0/P1/P2哪个级别？P0走王语嫣门禁，P2老顽童直接消化。
updated_at: '2026-06-16'
---
# 建模三段论 → KDO 工具链映射

> **Burn line**: 建模不是抽象概念——每个阶段都有对应的 KDO 命令和检查项。

---

## 一、阶段对应

| Truman 建模阶段 | 分数 | KDO 管线阶段 | 核心命令 | 质量门 |
|:--|:--:|:--|:--|:--|
| **流程建模** | 60 | `60_feedback` → `30_wiki/concepts/` | `kdo scaffold --new tool` | 执行率、TODO清理 |
| **抽象建模** | 75 | `30_wiki/frameworks/` | `kdo scaffold --new framework` | 跨域链接、Synthesis ≥5 wikilinks |
| **本质提炼** | 85 | `30_wiki/decisions/` | `kdo scaffold --new concept` | 可推导性、可证伪性 |

---

## 二、流程建模 → KDO（L3: 60分）

```
"这个任务高频重复吗？→ 是 → 做SOP/Checklist"
```

**KDO 对应**：

| Truman 动作 | KDO 命令/检查 |
|:--|:--|
| 写 checklist / SOP | `kdo scaffold --new tool --topic "XX清单"` |
| 标注执行率 | `status: enriched` → `status: stable`（跟踪使用次数） |
| 复盘 → 补丁 | `kdo lint` 发现断裂 → `kdo scaffold --card <id>` 修补 |
| 专人执行SOP | `60_feedback/inbox-queue/` → 王语嫣 cron 自动分配 |

**门禁**：

| 检查项 | 标准 |
|:--|:--|
| TODO清理 | 0个残留TODO（纯执行文档不应有TODO） |
| 可执行性 | 每一步有具体动作词（"打开X → 检查Y → 记录Z"） |
| 迭代痕迹 | `source_refs` 中包含至少一条反馈记录 |

**例**：药柜选址四步法 `method-medical-cabinet-site-selection.md` = L3 流程建模。

---

## 三、抽象建模 → KDO（L4: 75分）

```
"这个问题跨场景出现吗？→ 是 → 抽象模型/方法论"
```

**KDO 对应**：

| Truman 动作 | KDO 命令/检查 |
|:--|:--|
| 提炼方法论 | `kdo scaffold --new framework --topic "XX方法论"` |
| 案例验证 | source_refs ≥ 3，至少含1个反例 |
| 武器库建立 | `related` 链接 ≥ 5 张卡 |
| 跨域迁移 | `bridges_to` 非空（至少跨1个域） |

**门禁**：

| 检查项 | 标准 |
|:--|:--|
| Synthesis 出链 | ≥ 5 wikilinks |
| 有反例 | `Constraints` 表中至少1行标注"反例/失效场景" |
| diagnostic_signals | 至少2条，有具体场景+追问 |
| 置信度 | `confidence ≥ 0.7` |

**例**：建模三段论 `modeling-three-stages` = L4 抽象建模。有阶段定义、典型错误、决策树。

---

## 四、本质提炼 → KDO（L5: 85分）

```
"这涉及战略/底层判断吗？→ 是 → 本质提炼"
```

**KDO 对应**：

| Truman 动作 | KDO 命令/检查 |
|:--|:--|
| 本质要素 | `type: decision`（不放入 concepts/，放 decisions/） |
| 可推导性测试 | 用 `kdo query` 搜索跨域验证 |
| 学科经典对标 | `bridges_to` 链接到外部理论框架 |
| 五个为什么 | `Open Questions` 节前3条必须为自反性问题 |

**门禁**：

| 检查项 | 标准 |
|:--|:--|
| 可推导性 | Claims 中至少1条可以从底层要素推导出上层结论 |
| 跨域验证 | `bridges_to` 跨 ≥ 2 个域 |
| 自反性 | Open Questions 必须包含"这个本质在什么条件下会不成立" |
| 置信度 | `confidence ≥ 0.8`，多信源验证 |

**例**：王语嫣的"强监管、低频消费、线下履约类项目的认知偏差模式" = L5 本质提炼。从药柜提取的底层模式，可迁移到金融、教育、医疗AI。

---

## 五、决策：什么时候用哪个阶段？

```
任务高频重复？ ──是→ L3 流程建模 (tool/checklist)
    │否
    ↓
问题跨场景出现？ ──是→ L4 抽象建模 (framework/methodology)
    │否
    ↓
涉及战略/底层判断？ ──是→ L5 本质提炼 (decision)
    │否
    ↓
保持经验沉淀，不进 wiki（留 inbox 或 60_feedback）
```

**KDO 的命令选择**：

```bash
# L3: 具体操作流程
kdo scaffold --new tool --topic "XX操作清单" --domain yitang

# L4: 可迁移方法论
kdo scaffold --new framework --topic "XX方法论" --domain yitang,product

# L5: 路线决策
kdo scaffold --new concept --topic "XX本质提炼" --domain kdo,master
# → 审核通过后手工移入 decisions/
```

---

## Open Questions

- L3→L4 的升级信号是什么？卡片什么时候从 "tool" 升级为 "framework"？
- L4 框架的置信度阈值（0.7）是否过低？本质提炼的 0.8 是否过高？
- 是否应该有一个"反建模"检查项——不是所有经验都需要建模，有些保持纯经验就够了？

---

黄药师 · 2026-06-14 · 基于 Truman 高阶建模课程 + KDO 管线设计实践
