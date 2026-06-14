---

title: "YAML 标注对 KDO 知识库的启发——从自由填字段到结构化索引"
type: "improvement-plan"
domain:
  - kdo
  - ai-saas
  - design
  - yitang
status: "draft"
source_refs:
  - "00_inbox/AI俱乐部-AI学习落地-半肥猫-口述.txt"
created_at: 2026-06-06
updated_at: 2026-06-06
domain:
id: "proposal-yaml-frontmatter-standardization"
author: "legacy"
reviewed_by: "pending"
confidence: 0.7
trust_level: "low"
---

# YAML 标注对 KDO 知识库的启发

> 半肥猫在 AI 学习落地分享中强调：写笔记一定要做 YAML 标注。
> 
> 这不是一个"好习惯"的问题，而是一个**知识检索和复用的基础设施**问题。

## 问题：KDO 的 frontmatter 缺少规范

KDO 目前每张卡都有 YAML frontmatter，但存在三个问题：

### 问题 1：字段不一致

同一信息在不同卡里用不同字段：

```yaml
# 卡 A
source_refs: ["src_xxx"]
tags: ["#domain/design", "#source_type/dark-knowledge"]

# 卡 B  
source_refs: ["src_yyy"]
tags: ["design", "dark-knowledge"]    # 少了 # 号
```

没有统一规范，全靠写卡人的自觉。

### 问题 2：缺少「查询驱动」的字段设计

当前字段更多是"记录型"的（记录这张卡是什么），而不是"查询型"的（让这张卡能被什么样的检索找到）。例如：

- `query_triggers` 字段（黄药师已经在个别卡上用）——指定"用户在搜什么词时会命中这张卡"
- `when_to_use` 字段（技能卡需要）——"什么时候该用这个技能"
- `prerequisite_skills` 字段（技能卡需要）——"用这个技能之前需要会什么"

这些字段如果标准化，检索精度会大幅提升。

### 问题 3：缺少必填校验

当前没有机制检查"一张卡是否缺少了该类型的必填字段"。结果就是技能卡漏了操作步骤、概念卡漏了边界条件——直到用的时候才发现。

## 半肥猫的启发：YAML 是索引骨架，不是装饰

半肥猫的做法是：**每一条笔记的 YAML 字段决定了这条笔记将来能被什么方式找到。** 这不是写完了再补的元数据，而是写之前就该想好的检索策略。

应用到 KDO：

```
写卡前先想：这张卡将来会因为什么问题被搜到？
  → 把这个问题转化成 YAML 字段
    → 写卡
      → 检索时通过这些字段命中
```

## 改进建议

### 1. 按类型定义必填字段

| 卡片类型 | 必填字段 |
|:--------|:---------|
| concept（概念卡） | id, title, type, status, domain, source_refs, created_at |
| skill（技能卡） | id, title, type, status, tools_required, prerequisite_skills, feedback_path |
| dark-knowledge（暗知识卡） | id, title, type, dark_knowledge_type, source_person, source_context |

### 2. 新增字段

| 字段 | 用途 | 适用类型 |
|:----|:-----|:--------|
| `query_triggers` | 用户搜什么词时命中此卡 | 所有类型 |
| `when_to_use` | 什么场景用此技能 | skill |
| `prerequisite_skills` | 前置技能 | skill |
| `tools_required` | 需要的工具/环境 | skill |
| `common_failures` | 常见失败模式 | skill |

### 3. 自动化校验

黄药师的 kdo validate 可以扩展：检查每张卡的 frontmatter 是否包含其类型对应的必填字段。缺失时报 WARN（不 BLOCK，但让写卡人知道漏了）。

## 讨论问题

交给黄药师和老顽童讨论：

1. 新增字段的命名和格式是否合理？
2. 必填校验是 WARN 还是 BLOCK？
3. skill 类型是否需要单独的模板？
4. 历史存量卡是否要批量补齐？

---

*提案人：欧阳锋 · 2026-06-06*
*待讨论：黄药师 + 老顽童*
