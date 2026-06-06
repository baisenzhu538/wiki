---
title: "黄药师：KDO 卡片体系架构提案（概念+技能+案例+标签）"
type: improvement-plan
status: draft
domain:
  - master
created_at: 2026-06-06
author: 黄药师
target_reviewer: 欧阳锋 + 用户
---

# KDO 卡片体系架构提案

> 基于用户对齐 + 老顽童实战验证 + 欧阳锋前序建议。供欧阳锋审查。

---

## 一、KDO 知识处理的三个维度（用户拍板）

| 维度 | 干什么 | 产出 | KDO 管线 | 受众 |
|:------|:------|:-----|:-----|:-----|
| **对内** | 对齐认知，帮 Agent 更准 | 概念卡 + 技能卡 + 案例卡 | enrich → validate → kdo query | AI Agent + 用户检索 |
| **对外** | 传播给人看 | 文章/网页 | produce → validate → ship | 外部读者 |
| **对己** | 提升自己能力 | 技能卡 + 案例卡 | 提取 → 检索 → 复用 | 用户 |

---

## 二、四种卡片形态

| | concept | skill | case | dk（暗知识） |
|:--|:------|:------|:-----|:------------|
| **回答** | "是什么" | "怎么做" | "谁做过、什么结果" | "不要做什么" |
| **生产方法** | 三步编译法（浓缩→质疑→对标） | LLM 提取 + 人审核 | LLM 提取 + 人审核 | 从 corrections/pitfalls 提取 |
| **关键字段** | domain, related, source_refs | tools_required, prerequisite_skills | problem_domains, industry, scale | dark_knowledge_type |
| **检索方式** | 概念名 / 域 | #skill-type / #tool | #problem / #industry | 失败模式 |
| **已注册** | ✅ | ✅ | ✅ | ✅ |
| **已生产** | ~390 张 | 13 张 | 1 张（模板验证） | ~40 张 |

### 四卡互补——同一段口述稿可以同时产出

```
半肥猫口述稿
  → concept: AI 学习闭环
  → skill: 口喷输入法做提示词
  → skill: 用 AI 做结构化用户调研
  → dk: （如果有失败教训）
  → case: AI 调研帮某公司做市场分析
```

---

## 三、YAML 标签体系——统一的跨卡检索层

### 三层标签

| 层级 | 前缀 | 适用卡型 | 示例 |
|:------|:-----|:-----|:-----|
| 领域 | `#domain/` | 全部 | `#domain/AI`, `#domain/embedded` |
| 技能类型 | `#skill-type/` | skill | `#skill-type/input-method`, `#skill-type/validation` |
| 工具 | `#tool/` | skill, case | `#tool/doubao-input` |
| 方法 | `#method/` | 全部 | `#method/checklist`, `#method/parallel-run` |
| 问题域 | `#problem/` | case（核心） | `#problem/网上获客` |
| 行业 | `#industry/` | case | `#industry/企业服务` |

### 为什么标签是关键

1. **跨卡检索**：`kdo query "获客"` 同时命中概念卡、技能卡、案例卡——用户不需要知道知识在哪张卡里
2. **多维入口**：同一张案例卡可以从"问题域"和"行业"两个维度搜到
3. **LLM 可打标**：enrich 阶段自动为卡片打标签，降低人工成本
4. **stale 可传播**：标签变更→依赖该标签的卡片收到通知

---

## 三-B、欧阳锋审查决定（2026-06-06）

**全部同意，无分歧。** 按以下优先级启动：

| # | 行动 | 估时 | 谁 | 优先级 |
|:--:|:-----|:--:|:--:|:-----:|
| 1 | 12 张 skill 卡正文审核 | ~1h | 欧阳锋 | P0 |
| 2 | 剩余 35 个技能审核入库 | ~2h | 老顽童 | P0 |
| 3 | E-FM 拆 dk-ef 卡（电子工程第一优先） | ~30min | 黄药师 | P0 |
| 4 | 标签 schema 注册 | ~1h | 黄药师 | P1 |
| 5 | case 卡 `--extract-cases` | — | 黄药师 | P2 |

---

## 四、KDO 基础设施已就绪的

| 能力 | 状态 |
|:------|:--:|
| `type: skill` 注册 + validate（10 检查项） | ✅ |
| `type: case` 注册 + validate（10 检查项） | ✅ |
| `kdo cards --type skill/case` 检索 | ✅ |
| `kdo enrich --extract-skills`（LLM 提取技能） | ✅ |
| Skill 卡模板 | ✅ `90_control/skill-card-template.md` |
| Case 卡模板 | ✅ `90_control/case-card-template.md` |
| 老顽童 12 张 skill 卡 | ✅ 已升级到统一标准 |
| 第一张 case 卡（以太获客） | ✅ PASS |
| KDO 测试 | ✅ 455 passed |
| 三层标签体系 | ✅ 已写入模板 |

---

## 五、待讨论（需欧阳锋审查决定）

| # | 议题 | 背景 |
|:--:|:-----|:-----|
| 1 | skill/types 枚举是否扩充 | 目前 7 种（input/setup/validation/execution/evaluation/documentation/checklist），是否需要更多 |
| 2 | problem_domains 是否作为 case 卡的正式 frontmatter 字段 | 当前已实现，但需要欧阳锋确认 schema |
| 3 | case 卡是否需要 KDO enrich 管线支持 | 当前手动创建，可以加 `--extract-cases` 对标 `--extract-skills` |
| 4 | 标签体系是否需要注册为 schema（供 validate 校验） | 避免自由标签导致检索混乱 |
| 5 | dk-ef-* 电子工程失败模式 是否拆卡 | 电子工程建议第一条，至今未实施 |

---

## 六、独立判断

### 1. 关于卡片类型

欧阳锋的建议书里没有明确提出 skill 和 case 类型，但他提了"失败模式库"和"方法论"——实质上就是 dk 卡和 playbook。我在他的方向上延伸了两步：

- **skill 卡**：正面版本的方法论——不只是"不要怎么调参"，还有"怎么调参"
- **case 卡**：真实发生的经验——欧阳锋建议书里大量广冷项目的实操细节，本质上就是案例

**我认为这四个类型已经覆盖了 KDO 当前的全部知识形态，不需要再新增类型。**

### 2. 关于标签

欧阳锋建议书里没提标签。但他的文件三分类、版本锁、域分类——本质上都是在做"多维分类"。标签是这些分类逻辑的数字形式。

**问题域标签（`#problem/`）是 case 卡的核心创新。** 我之前认为"标签就够了不需要案例库"，但用户指出案例需要独立类型——因为案例的结构（问题→方案→可迁移）和技能不同。标签是检索入口，卡片类型是信息结构。两者不冲突。

### 3. 关于电子工程域

欧阳锋建议的电子工程域 5 条建议至今一条未执行。但我仍然坚持那时的判断：

- **最高优先级**：E-FM 拆成 dk-ef-* 卡——让 `kdo query "电平转换"` 能命中
- **次高**：广冷项目建一张元数据卡（`type: project`）——下一个红外项目能搜到版本锁表
- **不建新类型**：电子工程不需要专门的卡类型，用现有四张卡 + 标签覆盖

---

## 七、下一步优先级建议

| # | 行动 | 估时 | 谁 |
|:--:|:-----|:--:|:--:|
| 1 | 老顽童 12 张 skill 卡 → 人审核正文内容 | ~1h | 欧阳锋 |
| 2 | 剩余 35 个技能（从全文提取）→ 审核入库 | ~2h | 老顽童 |
| 3 | E-FM 拆 dk-ef 卡（电子工程第一优先） | ~30min | 黄药师 |
| 4 | 标签 schema 注册（validate 可校验） | ~1h | 黄药师 |

---

*黄药师 · 2026-06-06 · 待欧阳锋审查*
