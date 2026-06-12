# 洪七公后续任务

> **更新：2026-06-12**
> **性质：第二轮临时支援老顽童。** 老顽童管线还是堵着，你分担两张卡。

---

## 🎯 任务

| 顺序 | 任务 | 状态 | 估算 |
|:----:|:-----|:----:|:----:|
| **1** | **🔴 Pyramid Principle 桥接卡** | **🔜** | **2h** |
| **2** | **旧卡补互链 P0 — 3 对** | ⏳ | 1h |

---

## 任务 1：Pyramid Principle 桥接卡

### 基础信息

| 字段 | 内容 |
|:----|:------|
| 卡名 | `concept-minto-pyramid-principle` |
| 标题 | "金字塔原理：结论先行的结构化沟通框架" |
| 类型 | `framework` |
| 存放路径 | `30_wiki/frameworks/concept-minto-pyramid-principle.md` |
| domain | `["consulting", "yitang"]` |

### 格式要求

跟 7-S、Trusted Advisor 完全一样。三个硬条件：

1. **Bridge 节**已写 ↔ 与一堂体系的桥接关系
2. **`bridges_to`** frontmatter 已填（至少 1 条）
3. **Synthesis 链接 ≥5 个**（含至少 2 个同域横向链接）

### 攻击者

不要跟 7-S（Mintzberg+Pfeffer）和 Trusted Advisor（Kahneman+Christensen）重复。

建议组合：**Taleb**（金字塔结构在不确定性下脆弱）+ **Eric Ries**（精益创业反对过度计划）
或者：**Mintzberg**（沟通不是控制）+ 任选另一位

### 源材料

`60_feedback/diagnosis/diag_20250611_consulting-skills-research.md` — 王语嫣的 Gap 说明中有 Pyramid Principle 的桥接建议。

### 参考模版

直接复制你刚写的 `30_wiki/frameworks/concept-maister-trusted-advisor.md` 的 frontmatter 结构，替换内容。

---

## 任务 2：旧卡补互链 P0 — 3 对

等任务 1 完成后再来领具体配对清单。

### 背景

王语嫣诊断发现知识库缺少经典商业框架，她识别了 8 个缺口。老顽童已完成前 4 张（MECE、Issue Tree、Hypothesis-Driven、5 Whys），剩余 4 张需要分担。你接其中 2 张：

| 顺序 | 卡名 | 类型 | 估算 |
|:----:|:-----|:----:|:----:|
| **1** | **7-S Framework**（组织诊断框架） | `framework` | 2h |
| **2** | **Trusted Advisor**（咨询关系模型） | `framework` | 1.5h |

### 源材料

**必读：** `60_feedback/diagnosis/diag_20250611_consulting-skills-research.md`
- 这个文件里王语嫣写明了每张卡的来源、桥接关系、Gap 说明
- 你要做的就是把她的 Gap 说明翻译成一张完整的概念卡

### 你的模版（照填就行）

老顽童已经产了 4 张桥接卡，格式完全一致。每张卡必须包含以下 4 个部分：

---

#### ① frontmatter（文件头部 `---` 之间的内容）

```yaml
---
id: "concept-mckinsey-7s"              # 唯一ID
title: "7-S Framework：组织诊断的七维模型"  # 标题
type: "framework"                       # 类型：framework / tool
status: "draft"
domain:
  - "consulting"
  - "yitang"                            # 涉及一堂体系就加 yitang
source_refs:
  - "Peters, T. J., & Waterman, R. H. (1982). *In Search of Excellence*. Harper & Row."
  - "Waterman, R. H., Peters, T. J., & Phillips, J. R. (1980). 'Structure is not organization.' *Business Horizons*, 23(3), 14-26."
bridges_to:
  - target: "yt-model-entrepreneur-map"   # 关联的已有一堂卡ID
    relation: "provides_foundation_for"    # 关系类型
    description: "7-S 提供了组织诊断的完整维度"
    context: "一堂的'创业修炼地图'和'管理修炼地图'涉及组织能力评估，但缺少系统性的诊断维度。7-S 补充了这个缺口"
diagnostic_signals:                       # 诊断信号，至少 2 条
  - signal: "用户说'我们团队好像出了问题，但不知道是哪里'"
    framework_lens: "7-S 检查：从 7 个维度逐一排查，识别哪个维度是薄弱环节"
    follow_up_question: "如果用一句话说你们团队最痛的地方，是战略不清、结构不对、还是人不对？"
  - signal: "用户说'我们做了组织调整但问题还在'"
    framework_lens: "7-S 检查：组织调整是否只动了结构（Structure），忽略了共享价值观（Shared Values）等软要素"
    follow_up_question: "你们做组织调整的时候，有没有同步调整考核方式（Systems）和人员配置（Staff）？"
related:
  - "concept-mckinsey-mece"
  - "yt-model-entrepreneur-map"
  - "yt-management-toolkit-overview"
tags:
  - "#scene/business-analysis"
  - "#scene/entrepreneurship"
  - "#consulting"
created_at: "2026-06-11"
updated_at: "2026-06-11"
---
```

**注意事项：**
- `id` 不能和现有卡片重复。7-S 用 `concept-mckinsey-7s`，Trusted Advisor 用 `concept-maister-trusted-advisor`
- `related` 至少填 3-4 个关联卡。可以直接参考 MECE/Issue Tree 的写法
- `domain` 标内容不标出身——如果内容涉及一堂体系，就加 `yitang`

---

#### ② Summary + Claims（卡片正文开头）

格式参考已有的 MECE 卡（`30_wiki/frameworks/concept-mckinsey-mece.md`）：

```markdown
# 7-S Framework：组织诊断的七维模型

> 来源：Peters & Waterman (1982). *In Search of Excellence*
> 核心：组织不能只靠"画结构图"来诊断——7 个要素（3 硬 + 3 软 + 1 核心）必须匹配。

## Summary

用 2-4 句话介绍这个框架的核心内容。

## Claims

### 7 个维度

| 分类 | 维度 | 核心问题 |
|:----|:-----|:---------|
| 硬件要素 | Strategy（战略） | ... |
| 硬件要素 | Structure（结构） | ... |
| 硬件要素 | Systems（系统） | ... |
| 软件要素 | Style（风格） | ... |
| 软件要素 | Staff（人员） | ... |
| 软件要素 | Skills（技能） | ... |
| 核心 | Shared Values（共享价值观） | ... |
```

不要把 Wikipedia 整段搬过来。用自己的话压缩成核心要点。

---

#### ③ Bridge to 一堂体系（最重要的部分）

这是"桥接卡"区别于普通概念卡的核心。必须写清楚：

```markdown
## Bridge to 一堂体系

| 桥接目标 | 桥接关系 | 使用场景 |
|:---------|:---------|:---------|
| [[yt-model-entrepreneur-map]] | 7-S 提供了组织诊断的维度框架 | 创业者在评估团队能力时，用 7-S 逐一扫描七个维度，而不是只凭直觉说"我们团队还行" |
| [[yt-management-toolkit-overview]] | 管理工具箱中的 tool 卡可以与 7-S 各维度对应 | 在搭建管理体系时，用 7-S 检查是否每个维度都有工具覆盖 |

**案例：**
一堂的"创业修炼地图"把组织能力列为起盘阶段的核心能力，但没有给出"怎么诊断组织能力"的方法。7-S 可以补这个缺口：当创业者说"我们团队需要加强管理"时，先不急着上 OKR 或招 HR，先用 7-S 做一次组织体检——薄弱环节在策略、结构还是人员？不同薄弱环节对应不同的管理工具箱 tool 卡。
```

---

#### ④ Critique（至少 2 位攻击者）

参考 MECE（Kahneman+Taleb）和 Issue Tree（Christensen+Mintzberg）。**不要选跟已有卡重复的攻击者组合。**

Trusted Advisor 的 Critique 特别重要——这张卡本身就是王语嫣角色的理论支撑，Critique 应该帮助她理解"可信顾问"的边界在哪。

建议攻击者：
- **7-S** → Mintzberg（战略不是结构）+ Pfeffer（权力视角）
- **Trusted Advisor** → Kahneman（信任的认知偏差）+ 或 Christensen（过度依赖关系）

---

#### ⑤ Action Triggers（至少 3 条）

| 触发场景 | 第一个动作 | 成功指标 |
|:---------|:----------|:---------|
| 创业者说"我们团队好像有问题" | 用 7-S 七维清单逐一扫描，标记"正常/黄灯/红灯" | 30 分钟内完成团队体检，定位 1-2 个最短板 |
| ...至少 3 条... | ... | ... |

---

### 存放路径

| 卡名 | 路径 |
|:-----|:-----|
| 7-S Framework | `30_wiki/frameworks/concept-mckinsey-7s.md` |
| Trusted Advisor | `30_wiki/frameworks/concept-maister-trusted-advisor.md` |

### 完成顺序

1. 产 7-S → 通知欧阳锋审查
2. 审完再产 Trusted Advisor → 通知欧阳锋审查
3. **每张卡都先给欧阳锋看再产下一张，不要两张一起产**

### 参考资料（边写边参考）

- `30_wiki/frameworks/concept-mckinsey-mece.md` — MECE 卡，格式模版
- `30_wiki/frameworks/concept-mckinsey-hypothesis-driven.md` — Hypothesis-Driven 卡，另一个格式参考
- `60_feedback/diagnosis/diag_20250611_consulting-skills-research.md` — 王语嫣的诊断记录，含桥接建议
- `90_control/schemas/concept.yaml` — 官方 schema，含所有字段定义

---

## 记住

1. **这是临时支援老顽童。** 你不是变成 Producer，是帮老顽童分担两张卡。
2. **每张卡必须通过三条红线**才会被欧阳锋接受：
   - ✅ Bridge 节已写
   - ✅ `bridges_to` frontmatter 已填（至少 1 条）
   - ✅ Synthesis 链接 ≥5 个（含至少 2 个同域横向链接）
3. **遇到不确定的**——比如某个字段怎么填、某个桥接关系对不对——先产一个版本，在通知欧阳锋审查时把你的疑问写出来，我来帮你判断。不要自己卡住。
4. **不要改别人的卡。** 只写新卡。
