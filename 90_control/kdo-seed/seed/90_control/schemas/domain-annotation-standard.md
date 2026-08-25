# Domain 标注规范

> `domain` 字段的标注标准。全库卡片必须遵守。
> 生效日期：2026-06-11。旧卡逐步修正，新卡严格执行。

---

## 核心原则

**domain = 内容属于什么领域，不是素材来自什么人。**

```
❌ 按出身标：月白是设计师 → 所有卡 domain: ["design"]
✅ 按内容标：这张卡讲的是需求分层的商业分析方法 → domain: ["design", "yitang", "business-strategy"]
```

---

## 标注规则

### 1. 第一个 domain = 主要话题域

卡片内容最核心属于哪个领域。判断方法：读一遍 **Summary + 第一个 Claim**。如果这两处让你用一个词概括"这张卡关于什么"——那个词就是第一个 domain。

### 2. 第二个及以后 = 内容涉及的关联域

卡片讨论到了其他域的核心概念、方法或框架。判断方法：读 **Critique 的第一句话 + Synthesis 的第一条关联**。如果出现了另一个域的核心概念——加那个域。

### 3. domain 和 tags 必须一致

如果 `tags` 里有 `#scene/business-analysis`，`domain` 里应该有一个对应的域标签（如 `business-strategy` 或 `yitang`）。如果 `tags` 里有 `#domain/AI`，`domain` 里应该有 `ai`。

**两个字段不是冗余——它们回答不同的问题：**
- `domain`：这张卡在知识体系里属于哪几个域（给图聚类、域检索用）
- `tags`：这张卡涉及什么场景和方法（给语义检索、诊断匹配用）

### 4. 不是"来源是谁"而是"内容关于什么"

`source_person` 和 `source_context` 已经记录了来源信息。`domain` 不需要重复这个信息。

---

## 判定流程

```
读 Summary
  → 这张卡的核心话题是什么域？→ 第一个 domain

读 第一个 Claim
  → 论证过程中引用了哪个域的概念？→ 追加 domain

读 Critique 第一句话
  → 批评的角度来自哪个域的视角？→ 追加 domain

读 Synthesis 第一条
  → 关联的目标卡属于哪个域？→ 如果讨论深入，追加 domain
```

---

## 正确示例

```yaml
# ✅ 正确：内容讲了设计、商业策略、AI 协作三个维度
domain: ["design", "business-strategy", "ai-collaboration"]

# ✅ 正确：纯 yitang 域的方法论卡
domain: ["yitang"]

# ✅ 正确：桥接卡——连接一堂体系和经典商业框架
domain: ["yitang", "business-strategy"]
bridges_to:
  - target: "xxx"
    relation: "provides_foundation_for"
```

---

## 错误示例

```yaml
# ❌ 错误：按出身标——因为素材来自月白（设计师），就只标 design
# 但这张卡实际在讲需求分层的商业分析方法
domain: ["design"]

# ❌ 错误：domain 为空
# 没有 domain 的卡片在图里会成为孤岛
domain: []

# ❌ 错误：tags 里已经有 #scene/business-analysis 但 domain 里没有对应域
domain: ["ai"]
tags:
  - "#scene/business-analysis"   # ← domain 里缺 business-strategy 或 yitang
```

---

## 全库现状（2026-06-11 扫描）

| 指标 | 数值 |
|:-----|:----:|
| 总卡片 | 1,130 |
| domain-tags 不一致 | 830（73%） |
| domain-tags 一致 | 300（27%） |

**73% 的卡片存在不同程度的"domain 标出身不标内容"问题。** 修复策略：新卡严格执行本规范；旧卡由老顽童按域分批修正，王语嫣抽查验证。

---

## 域值建议（非穷举）

| domain 值 | 含义 | 典型卡片 |
|:----------|:-----|:---------|
| `yitang` | 一堂课程体系 | yt-* 前缀卡 |
| `business-strategy` | 商业策略与分析 | case-*, framework 卡 |
| `design` | 设计领域 | 月白 skill 卡 |
| `ai` | 人工智能 | AI 相关 concept/skill 卡 |
| `ai-collaboration` | 人机协作 | 纪浩/半肥猫 skill 卡 |
| `product` | 产品管理 | 产品内核相关卡 |
| `entrepreneur` | 创业 | 创业预判/增长相关卡 |
| `decision-making` | 决策科学 | 科学决策域卡片 |
| `knowledge-management` | 知识管理 | KDO 系统卡 |
| `note-taking` | 笔记方法 | 清单体笔记卡 |
| `electronics` | 电子工程 | 广冷电子调试卡 |

> 这不是封闭枚举——如果卡片内容涉及上表之外的域，使用小写英文描述性值（如 `healthcare`、`education`）。

---

## 执行规则

| 谁 | 做什么 | 时机 |
|:--|:-----|:-----|
| **老顽童** | 产新卡时严格按本规范标注 domain | 每次写卡 |
| **老顽童** | 按域分批修正旧卡的 domain（优先级：design 域 32 张 → OCR 卡 → 扫描器批量 skill 卡） | 有空时逐批修 |
| **王语嫣** | 诊断时抽查 domain 是否仍然"标出身不标内容" | 每次诊断 |
| **黄药师** | `kdo lint` 增加 domain-tags 一致性检查（WARN） | 后续 Task |
| **欧阳锋** | 审查新卡时检查 domain 是否符合规范 | 每次审查 |
