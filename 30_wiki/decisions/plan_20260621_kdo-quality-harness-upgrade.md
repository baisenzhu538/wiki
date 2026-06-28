---
id: plan_20260621_kdo-quality-harness-upgrade
title: KDO 质量体系升级——Harness Engineering 三原则落地
type: improvement-plan
status: active
domain:
  - master
  - kdo
source_refs:
  - 00_inbox/Harness Engineering：让 AI 像团队一样写出生产级代码.md
  - 60_feedback/diagnosis/diag_20260621_Harness Engineering文档诊断.md
  - 30_wiki/frameworks/framework-yitang-research-quality-gate.md
  - 30_wiki/frameworks/framework-wanghuan-gan-three-roles.md
created_at: "2026-06-21"
author: 黄药师
reviewed_by: 欧阳锋
confidence: 0.9
trust_level: high
related:
  - [[framework-yitang-research-quality-gate]]
  - [[framework-wanghuan-gan-three-roles]]
  - [[concept-harness-cattle-not-pets]]
  - [[concept-harness-scoring-anchors]]
  - [[tool-harness-adversarial-tester]]
---
# KDO 质量体系升级——Harness Engineering 三原则落地

> 来源：王欢 Harness Engineering 文章 + 王语嫣诊断 + 黄药师独立判断
> 核心命题：Harness 做代码质量，KDO 做知识质量——同构问题，可直接迁移

---

## 原则 1: GAN 对抗门禁——四路并行评审

### 现状
老顽童写卡 → 自己审 → 入库。王语嫣/欧阳锋审查是事后抽检，不是入库前的 BLOCKING 步骤。

### 升级后
```
Generator(老顽童) 产出卡片
  ↓
四路并行评审（全部 BLOCKING）
├── 王语嫣: 诊断视角——与已有卡片对照、置信度标记、盲区识别
├── 欧阳锋: 架构视角——三信号(反例具体性/案例区分度/跨域连接)
├── kdo lint: 格式视角——frontmatter/source_refs/wikilink 死链
└── Adversarial Agent: 对抗视角——"如果这张卡有错误，最可能在哪？"
  ↓
全部 ≥ 3/5 → 合成修正 → 入库
任一 < 3/5 → 退回 Generator，附修复简报
```

### 实现
- src_unknown
- src_unknown
- src_unknown

### 反例：supplement 卡绕过管线
`framework-yitang-research-weapon-supplement-2026.md` 直接写入 `30_wiki/`，跳过了诊断→审核管线。四路并行评审会在此卡入库前就拦截。

---

## 原则 2: 锚定评分——1-5 分 + 语义锚点 + "取较低值"

### 现状
卡片 confidence 使用 0-1 连续值。问题是：(1) 0.85 和 0.88 的差异不可解释；(2) 评分者"中间偏好"导致 confidence 集中在 0.8-0.9；(3) 一个慷慨的评分者可以"冲平"严格的评分者。

### 升级后
卡片评审使用 1-5 锚定评分，每个分值有明确的语义锚点：

| 分 | 语义锚点 | 卡片标准 |
|:--|:--|:--|
| **5** | 可发布——无已知缺陷，已通过对抗测试 | 四路评审全部 ≥4，零 CRITICAL 发现 |
| **4** | 可靠——有小问题但不影响使用 | 核心框架完整，source_refs 真实，≥2 外部攻击者 |
| **3** | 可用——骨架完整但深度不足 | Claims 清晰，Critique 有但不够深入 |
| **2** | 草稿——需要大量修改 | 有内容框架但缺 Critique/Boundary/Action Triggers |
| **1** | 不可用——需要重写 | 空壳、拼凑、或违反铁律 |

**"取较低值"规则**：多路评审中，最终分数 = min(各路分数)。不允许高分"冲平"低分——短木板决定木桶容量。

**通过门槛**：
- src_unknown
- src_unknown
- src_unknown

### 实现
- src_unknown
- src_unknown
- src_unknown

---

## 原则 3: "牲口而非宠物"——Agent 实例隔离

### 现状
同一个 Agent 会话可以既写卡又审自己的卡。老顽童的 supplement 卡就是这样绕过管线的——不是故意违规，是没有工程手段阻止。

### 升级后
写卡和审卡必须是**不同的 Agent 实例**。实例隔离的工程手段：

| 规则 | 实现 |
|:--|:--|
| **写审分离** | 产卡 Agent 的 `author` 字段不得与 `reviewed_by` 字段相同 |
| **新鲜实例** | 每次审查启动新的 Agent 会话——不带前序对话的包袱 |
| **自审检测** | `kdo lint` 新增检查：`author == reviewed_by` → BLOCKING ERROR |
| **管线闸门** | 卡片 status 从 `draft` → `enriched` 前，必须有非 author 的 `reviewed_by` |

### 实现
- src_unknown
- src_unknown
- src_unknown

---

## 实施路径

| 阶段 | 内容 | 产出 |
|:--|:--|:--|
| **Phase 1（今天）** | 锚定评分 + 自审检测 | `scoring-anchors.yaml` + kdo_lint 升级 |
| **Phase 2（本周）** | 对抗评审脚本 | `adversarial-card-review.py` |
| **Phase 3（本周）** | 四路并行门禁集成 | 更新 `kcard-quality-gate.py` + startup.md |
| **Phase 4（下周）** | Agent 实例隔离 SOP | 更新所有 Agent context |

---

*黄药师 · 2026-06-21 · Harness Engineering 三原则落地*
