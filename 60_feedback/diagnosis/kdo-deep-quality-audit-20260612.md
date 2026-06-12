---
title: KDO Vault 深度质量审计
diagnostician: 王语嫣
date: 2026-06-12
type: diagnosis
source: 全库 30_wiki/ 七维扫描
supersedes: kdo-concept-map-20260612.md
---

# KDO Vault 深度质量审计报告

> **上一轮**（概念卡地图）：目录结构 + domain 标签 + bridge 分布
> **本轮**（深度审计）：diagnostic_signals / 外部攻击者 / Constraints / 断链 / 陈旧度 / source_refs / 类型匹配 — 7 个维度

---

## 一、诊断信号覆盖 — 🚨 P0（我的核心武器）

**现状**：全库 1258 张卡，仅 **7 张**有 `diagnostic_signals` 字段。

| 区域 | 总卡数 | 有 signals | 覆盖率 | 等级 |
|:-----|------:|----------:|:------:|:----:|
| frameworks/ | 7 | **4** | 57% | 🟡 |
| tools/ | 36 | **3** | 8% | 🔴 |
| concept-* | 14 | **2** | 14% | 🔴 |
| yt-*（一堂） | 238 | **1** | **0.4%** | 🚨 |

**这意味着**：`kdo query` 的 `diagnostic_signals → follow_up_question` 链路几乎完全断裂。这是我王语嫣做诊断时最核心的武器——没有它，诊断靠人工翻卡，无法自动化召回。

**根因判断**：`diagnostic_signals` 是 agent-native 格式（v1.3+）的新要求。238 张 yt- 卡在升级 sprint 中只覆盖了 frontmatter 格式（type/domain/status）但跳过了 diagnostic_signals。

**建议**：
- P0：批量脚本为每张卡填充 diagnostic_signals（至少 1-2 条 trigger + framework_lens + follow_up）
- P0：给 frameworks/ 和 tools/ 中缺少 signals 的卡补上
- P0：在自迭代检测器 A 中增加"新卡必须有 diagnostic_signals"规则

---

## 二、外部攻击者 — 🚨 P0（老朱硬性要求）

**现状**：全库 **零张卡有 `attacker:` 字段**。

老朱的要求（2026-05-17，写入 memory）：
- 每张 tool 卡 **≥2 位攻击者**
- 攻击必须有紧迫感——"让用工具的人睡不着觉"
- Constraints 和外部攻击不能重叠

**这意味着**：所有卡片的外部批判维度完全缺失。即便声称通过 v1.5 标准的卡（如 McKinsey 桥接卡）也没有 attacker。

**检查 7 张 bridge framework 卡**：`7-S / Trusted Advisor / Hypothesis-Driven / MECE / Issue Tree / Minto / Pyramid` — **全部 0 attacker**。

**建议**：
- P0：全部 7 张 framework 卡 + 36 张 tool 卡 + 14 张 concept-* 卡批量补 `attacker:` 字段
- P0：在工业化手册门禁中增加"attacker 字段非空"规则

---

## 三、Constraints 字段 — 🚨 P0

**现状**：frameworks/（7 张）、tools/（36 张）、concept-*（14 张）**全都没有 `constraints:` 字段**。

即使加上 `prior_constraints`、`limitations` 等变体——也没有。

**这意味着**：卡片的"适用边界"信息完全没有显式标注。诊断时无法快速判断"这个框架/工具在什么时候不适用"。

**对比 v1.5 标准**：
- v1.5 要求 Constraints = 内部局限，外部攻击 = 不同范式的批判
- **两者都缺失**，所以不存在"重叠"问题——连空的都没法检查是否重叠

---

## 四、Type-Directory 错配 — 🟡 P1

yt- 卡片全部放在 `concepts/` 目录，但它们的内在 `type` 字段显示：

| yt- 内在 type | 数量 | 应放目录 |
|:--------------|:---:|:---------|
| `tool` | **123** | `tools/` |
| `framework` | **48** | `frameworks/` |
| `concept` | **46** | `concepts/` ✅ |
| `skill` | **3** | `tools/` |
| `dk` | **3** | `dark-knowledges/` |
| 无 type 或空 | **15** | 未知 |

**问题**：123 张工具卡 + 48 张框架卡放在 concepts/ 下，导致：
1. `kdo validate` 断言链断裂（按目录判断类型）
2. `kdo query` 按 type 筛选时行为异常
3. 常规概念卡查询被 171 张非概念卡干扰

**建议**：
- P1：批量搬迁——yt-tool-* → tools/, yt-model-* → frameworks/
- 或：目录不动但更新 `type` 字段使断言链能识别

---

## 五、卡片陈旧度 — 🟡 P1

| 维度 | 数据 |
|:-----|:-----|
| **最早更新批次** | 2026-05-08（30 张 yt- 卡未动过） |
| **最近大批更新** | 2026-05-11（51 张卡） |
| **最近 7 天有改动** | 1237 张（说明近期活跃度高） |
| **超过 15 天无改动** | 0 张 |
| **仍为 draft 状态** | 620 张（~49%） |
| **已 enriched** | 476 张（~38%） |
| **已 reviewed** | 47 张 |
| **已 superseded/deprecated** | 4 张 |
| **stable** | 4 张 |

**解读**：
- 整个 vault 创建时间不到 2 个月，没有真正"过期"的卡
- 但 ~49% 的卡还卡在 draft，说明**大批量产出后的审查通道严重阻塞**
- 从 draft → enriched → reviewed → stable 的管线不畅

---

## 六、source_refs — 🟡 P1

**frameworks/**：7 张全部有 source_refs，且无空值（✅ 规范）
**tools/**：36 张全部有 source_refs，且无空值（✅ 规范）
**concept-***：14 张全部有 source_refs，且无空值（✅ 规范）
**yt-***：205/238 有 source_refs 字段（✅ 86%）
**yt-*** 中 `source_refs: []`：0 张（✅ 无空值）

**结论**：source_refs 在 bridge 卡和概念卡上表现良好。yt- 卡 86% 覆盖率但仍有 33 张缺少 source_refs。相比 Sprint 9 时 52 张空值的状态已有显著改善。

---

## 七、断链（Broken Wikilinks）— 🟡 P1

在 frameworks/ 和 tools/ 的 `bridges_to` / `related` / `wiki_refs` 中，发现以下目标指向不存在的文件：

| 断链 | 来源卡 | 类型 |
|:-----|:-------|:-----|
| `[[concept-minto-pyramid-principle]]` | MECE | related |
| `[[concept-mckinsey-hypothesis-driven]]` | MECE | related |
| `[[diag_20250611_consulting-skills-research]]` | Trusted Advisor | bridges_to |
| `[[master-cognitive-bias-checklist]]` | 单元模型 | related |
| `[[master-systems-thinking]]` | 单元模型 | related |
| `[[yt-product-kernel-three-questions]]` | Trusted Advisor | bridges_to |
| `[[skill-mece体系框架法]]` | MECE | wiki_refs |
| `[[skill-纪浩-*]]`（3 条） | 纪浩概念卡 | related |
| `[[yt-foresight-15-char-mantra]]` | concept-一堂-product-kernel | related |
| `[[concept-minto-pyramid-principle]]`（等） | 多个 | wiki_refs |

**估算**：10-15 条断链。严重程度中等——不影响功能但会让 kdo graph 图有缺失的节点。

**建议**：
- P1：运行 `kdo validate` 的断链检测（如果有），或写脚本扫描 `[[xxx]]` → 文件存在性
- P1：断链目标中有 5 个是明确的未来卡（master-*, diag_*），可在诊断反馈中标注"待创建"

---

## 八、总结：三大 P0 + 四大 P1

| 优先级 | 问题 | 指标 |
|:------:|:-----|:-----|
| 🚨 **P0** | **diagnostic_signals 覆盖率 0.6%** | 1258 张中仅 7 张有 |
| 🚨 **P0** | **外部攻击者（attacker）全空** | 0/1258 |
| 🚨 **P0** | **Constraints 字段全空** | 0/57（bridge + tool + concept） |
| 🟡 P1 | Type-Directory 错配 | 171 张 yt- 放错目录 |
| 🟡 P1 | 审查管线阻塞 | 49% 卡在 draft |
| 🟡 P1 | 断链 | ~15 条 |
| 🟡 P1 | source_refs 缺失 | 33 张 yt- 卡 |

**核心判断**：
> KDO vault 存在 **"广度够了，深度没到"** 的问题。卡片数量（1258）和 domain 覆盖率在快速扩张，但 agent-native 格式的关键字段（diagnostic_signals / attacker / constraints）几乎全部缺失。这些字段是"诊断可召回"的基础设施——没有它们，我就算翻遍全库也找不到该用哪张卡。

---

## 九、建议行动路线

```
Week 1（P0 全修）：
  A. diagnostic_signals 批量填充 → frameworks/ + tools/ + concept-*
  B. Attacker 字段批量填充 → 同上
  C. Constraints 字段批量填充 → 同上

Week 2（P1 补完）：
  D. yt- 卡片 type → 目录对齐（黄药师脚本迁移）
  E. 断链修复（欧阳锋判定 → 老顽童补卡或删链）
  F. 33 张缺 source_refs 的 yt- 卡补源

持续：
  G. 自迭代检测器 A 增加"新卡三字段必填"规则
```

---

*本诊断不修改 30_wiki/ 下任何文件。*
