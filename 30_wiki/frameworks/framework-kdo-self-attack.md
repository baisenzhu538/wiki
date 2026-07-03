---
id: framework-kdo-self-attack
title: KDO 知识自攻击框架：用对抗 Agent 在交付前主动找出弱点
type: framework
status: reviewed
confidence: 0.86
trust_level: high
domain:
- kdo
- quality
- meta-methodology
author: 王语嫣
reviewed_by: 欧阳锋
review_date: '2026-06-27'
created_at: '2026-06-27'
quality_labels:
- cited
- insight
- principle
- quality
- validated
updated_at: '2026-07-03'
source_refs:
- 40_outputs/capabilities/skills/shared/kdo-self-attack/SKILL.md
- 30_wiki/frameworks/framework-ouyangfeng-review-methodology.md
- 30_wiki/frameworks/framework-yitang-research-quality-gate.md
- 30_wiki/frameworks/framework-yitang-six-layer-cross-validation.md
- 30_wiki/frameworks/framework-yitang-nine-layer-deep-dig.md
related:
- framework-ouyangfeng-review-methodology
- framework-yitang-research-quality-gate
- framework-yitang-six-layer-cross-validation
- framework-yitang-nine-layer-deep-dig
- tool-demand-blindspot-checklist
- yt-decision-y-model
- dk-yitang-Y-model-pitfalls
- tool-yitang-Y-model-application
---
# KDO 知识自攻击框架：用对抗 Agent 在交付前主动找出弱点

> 一句话：在知识卡片交付审查之前，用四路对抗 Agent 主动攻击其逻辑、证据、完整性和时效性，把问题发现在用户和终审者之前。

---

## 1. 为什么需要自攻击

知识卡片常见的质量问题不是作者不会写，而是作者**看不出自己的问题**：

- 把相关性当成因果性；
- 把讲师口述数字当成已核实事实；
- 只找支持性证据，忽略反例；
- 同一个概念在卡的前后漂移；
- 引用的方法/工具已经过时。

传统审查是「他检」：欧阳锋或用户发现问题后再返工。自攻击是「自检前置」：让四个专门找茬的 Agent 在提交前先打一轮，把 🔴 致命和 🟡 严重问题修掉，再进入审查。

---

## 2. 四路攻击 Agent

```
知识卡片
  ├── Attacker A: 逻辑攻击
  ├── Attacker B: 证据攻击
  ├── Attacker C: 完整性攻击
  └── Attacker D: 时效性攻击
  ↓
合并攻击报告 → 修复 → 重新攻击 → 提交
```

### 2.1 Attacker A：逻辑攻击

| 攻击目标 | 典型问题 |
|:---|:---|
| 核心主张 | 是否存在偷换概念？「X 很重要」是否被说成「X 是唯一方案」？ |
| 因果关系 | 推断 A→B 是否忽略了混淆变量 C？是否把相关性当因果？ |
| 循环论证 | 结论和前提是否互相引用？ |
| 概念一致性 | 同一个术语在卡的不同位置含义是否一致？ |

**攻击信号示例**：
> 卡的 summary 声称「工业化生产决定企业天花板」，但文中只给出一堂做课一个案例，从「一堂成功」跳到「决定所有企业天花板」是过度泛化。

### 2.2 Attacker B：证据攻击

| 攻击目标 | 典型问题 |
|:---|:---|
| source_refs 覆盖 | 每条关键 Claim 是否有对应来源？ |
| 数字可追溯 | 关键数字是官方数据、多源交叉，还是讲师口述？ |
| 来源层级 | 核心结论是否至少达到 L2 权威或 L3 多源？ |
| 幸存者偏差 | 证据是否只来自成功案例？失败案例是否被排除？ |

**攻击信号示例**：
> 「市场规模 500 亿」没有 source_refs，且来自单篇行业自媒体，应标注为「待独立核实」或降级 confidence。

### 2.3 Attacker C：完整性攻击

| 攻击目标 | 典型问题 |
|:---|:---|
| 反例缺失 | 是否明确写了 When NOT to Use？ |
| 视角盲区 | 从竞对、用户、监管、执行者角度看，卡是否遗漏了什么？ |
| 跨域矛盾 | 与相关卡片是否有观点冲突未标注？ |
| 「大象」测试 | 有没有一个显而易见的问题，整张卡都没提？ |

**攻击信号示例**：
> 增长飞轮卡强调了「飞轮能自我强化」，但没有讨论外部环境变化（平台政策、技术颠覆）导致飞轮断裂的案例。

### 2.4 Attacker D：时效性攻击

| 攻击目标 | 典型问题 |
|:---|:---|
| 数据时效 | 关键数字是什么时候的？超过 2 年的是否需要更新？ |
| 方法演进 | 2025-2026 年该领域有没有新研究、新工具未被引用？ |
| 工具可用性 | 引用的 API/工具是否仍然可用？ |
| 共识漂移 | 业界最佳实践是否已经改变？ |

**攻击信号示例**：
> 卡中推荐的某款 SEO 工具在 2025 年后已被搜索引擎算法更新削弱，应补充说明适用边界或替换案例。

---

## 3. 操作流程

### 3.1 单卡自攻击

```
1. 卡片正文完成、frontmatter 已填
2. 运行 /kdo-self-attack <card-id>
3. 读取 60_feedback/adversarial/atk_<card-id>_<date>.md
4. 修复所有 🔴 致命问题
5. 修复大部分 🟡 严重问题（确实无法修复的需标注理由）
6. 重新运行 /kdo-self-attack 确认修复
7. 提交：卡片 + 攻击报告 + 修复记录
```

### 3.2 批量/定期自攻击

| 场景 | 命令 |
|:---|:---|
| 域批量抽检 | `/kdo-self-attack --domain yitang --sample 5` |
| 每周定期自检 | `/kdo-self-attack --domain yitang --random 3` |
| 重点卡深度攻击 | `/kdo-self-attack <card-id> --deep` |

---

## 4. 问题分级与修复标准

| 级别 | 定义 | 修复要求 |
|:---:|:---|:---|
| 🔴 致命 | 核心主张错误、逻辑链断裂、关键证据造假 | 必须修复，否则不得提交 |
| 🟡 严重 | 证据不足、重要反例缺失、来源层级过低 | 原则上修复；无法修复需降 confidence 并标注 |
| 🟢 轻微 | 表述不精确、related 不足、格式问题 | 尽量修复；可批量处理 |

---

## 5. When NOT to Use

- **卡片尚未完成初稿**：自攻击需要完整 Claims 和 Evidence 才能攻击，半成品攻击无效。
- **纯元数据/索引卡**：没有知识主张的卡片（如目录、log）不需要自攻击。
- **紧急修复类 patch**：如修正 frontmatter 语法错误，直接修即可，不必跑完整四路攻击。
- **缺乏原始素材支撑**：如果 source_refs 本身就不存在，自攻击会大量误报，应先补素材。

---

## 6. 常见失败模式

| 失败模式 | 症状 | 修复 |
|:---|:---|:---|
| 把自攻击当形式 | 攻击报告生成后不看、不修，直接提交 | 将攻击报告修复率纳入提交门禁 |
| 攻击者编造漏洞 | 为了「找出问题」而虚构不存在的缺陷 | 攻击必须基于事实和原文，禁止 hallucination |
| 只修轻微不修严重 | 🟢 修了很多表述，🔴🟡 没动 | 强制按级别排序修复 |
| 过度攻击导致瘫痪 | 对一张小卡跑十轮深度攻击 | 按卡片优先级选择攻击深度 |
| 自攻击替代交叉验证 | 认为自攻击通过就不需要外部验证 | 自攻击是前置自检，不替代六层交叉验证 |

---

## 7. Critique

- **攻击者的偏见**：四路攻击 Agent 本身基于训练数据和提示词，可能对某些领域过度敏感或过度宽松；需要定期用已知的优质卡和劣质卡校准攻击标准。
- **创新 vs 保守**：过度自攻击可能让卡片趋于平庸——作者为了避免被攻击，只写最安全的结论。需要保留「高置信度但可争议」的 Claims，并在 Critique 中主动说明。
- **成本问题**：深度四路攻击对每张卡消耗不低；建议 P0 框架卡和关键 case 卡必跑，P2 工具卡可抽检。
- **不能替代真人审查**：自攻击擅长找逻辑和证据问题，但对战略判断、语境微妙性、用户真实需求的把握仍弱于真人终审。

---

## 8. 与现有流程的关系

```
生产完成
  ↓
自攻击（生产者负责）
  ↓
欧阳锋审查（他检）
  ↓
王语嫣验收 / 用户反馈
```

- 自攻击是 **Pre-Review**，不是审查的替代。
- 欧阳锋审的是「卡 + 攻击报告 + 修复记录」，而不是裸卡。
- 它与 `framework-yitang-research-quality-gate` 的门禁 5（对立面检验）互补：质量门禁是人工自检清单，自攻击是对抗 Agent 自动化执行。

---

## 9. 行动触发器

当你准备提交一张卡时，先问自己：

1. 这张卡的核心主张如果被故意反驳， weakest link 在哪里？
2. 卡里的关键数字，来源层级够吗？是否有「口述待独立核实」标注？
3. 有没有一个明显场景，这个框架完全不适用，但卡里没有写？
4. 引用的方法/工具/数据是否有可能在 2025-2026 年已经过时？

如果四个问题答不上来，先跑 `/kdo-self-attack`。

---

## 欧阳锋审查结论

**审查日期**：2026-06-27  
**审查结果**：✅ 通过（deep）

**审查依据**：
- 正文 174 行（>120 行），结构完整；
- 具备 Critique（第 7 节）、失败模式（第 6 节）、行动触发器（第 9 节）；
- 数字极少且主要为方法论，无来源缺失风险；
- 四路攻击 Agent 定义清晰、可执行；
- When NOT to Use 覆盖 4 个合理场景；
- 失败模式具体，每条含症状 + 修复，无模板话；
- 与 `framework-ouyangfeng-review-methodology`、`framework-yitang-research-quality-gate` 等框架逻辑自洽，互为补充；
- `related` 中 5 个 wikilink 全部有效；
- `kdo pre-submit` 检查通过（1 file, 1 passed, 0 failed）。

**状态变更**：`status: enriched` → `reviewed`，`reviewed_by: pending` → `欧阳锋`。

